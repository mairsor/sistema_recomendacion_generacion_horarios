#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar matrículas históricas de alumnos de Telecomunicaciones.

Reglas:
- Semestres disponibles: 2020-2 hasta 2025-2 (11 semestres)
- Alumnos antiguos (2017-2020) empiezan con créditos iniciales
- 5-7 cursos por semestre
- Tasa de aprobación: ~80% (varía según popularidad del profesor)
- Notas: 7-16, mayoría entre 10-12
- Nota ≥ 10 = aprobado
- Respetar prerrequisitos
- Respetar orden de ciclos (electivos desde ciclo 6)
- Alumnos tardan 11-12 ciclos en egresar
- 2025-2: matrículas sin nota final
"""

import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
import random
from datetime import datetime, date
from collections import defaultdict
import json

# Configuración de conexión a la base de datos
DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

# Semestres disponibles en la base de datos
SEMESTRES_DISPONIBLES = [
    "2020-2", "2021-1", "2021-2",
    "2022-1", "2022-2", "2023-1",
    "2023-2", "2024-1", "2024-2",
    "2025-1", "2025-2"
]

# Configuración de simulación
CURSOS_POR_SEMESTRE_MIN = 5
CURSOS_POR_SEMESTRE_MAX = 7
TASA_APROBACION_BASE = 0.80
CICLOS_PARA_EGRESAR = random.randint(11, 12)  # 11-12 ciclos
NOTA_APROBATORIA = 10.0

# Rangos de créditos por ciclo relativo
CREDITOS_POR_CICLO = {
    1: (0, 21),    # Hasta 21 créditos = ciclo 1
    2: (22, 43),   # 22+ créditos = ciclo 2 (permite avanzar con 6 cursos de ciclo 1)
    3: (44, 65),
    4: (66, 89),
    5: (90, 111),
    6: (112, 131),
    7: (132, 152),
    8: (153, 169),
    9: (170, 188),
    10: (189, 206),
    'egresado': 208
}

def conectar_db():
    """Establece conexión con la base de datos."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"✗ Error al conectar a la base de datos: {e}")
        sys.exit(1)

def obtener_alumnos(conn):
    """Obtiene todos los alumnos de la base de datos."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT id, codigo, nombres, apellidos, ciclo_relativo, 
                   creditos_aprobados, promedio
            FROM alumno
            ORDER BY codigo
        """)
        alumnos = cur.fetchall()
        print(f"✓ Obtenidos {len(alumnos)} alumnos")
        return alumnos

def obtener_cursos(conn):
    """Obtiene todos los cursos con sus créditos y ciclo."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT id, codigo, nombre, tipo, ciclo, creditos
            FROM curso
            ORDER BY ciclo, codigo
        """)
        cursos = cur.fetchall()
        print(f"✓ Obtenidos {len(cursos)} cursos")
        return cursos

def obtener_prerrequisitos(conn):
    """Obtiene los prerrequisitos de cada curso."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT curso_id, prereq_id
            FROM curso_prerrequisito
        """)
        prereqs_raw = cur.fetchall()
        
        # Organizar en diccionario: curso_id -> [prereq_ids]
        prereqs = defaultdict(list)
        for row in prereqs_raw:
            prereqs[row['curso_id']].append(row['prereq_id'])
        
        print(f"✓ Obtenidos prerrequisitos para {len(prereqs)} cursos")
        return dict(prereqs)

def obtener_cursos_ofertados(conn):
    """Obtiene los cursos ofertados por semestre."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT co.id, co.curso_id, co.profesor_id, co.semestre, 
                   co.codigo_seccion, co.turno, co.cupos_disponibles,
                   c.codigo as curso_codigo, c.nombre as curso_nombre,
                   c.ciclo, c.creditos, c.tipo,
                   p.popularidad
            FROM curso_ofertado co
            JOIN curso c ON co.curso_id = c.id
            LEFT JOIN profesor p ON co.profesor_id = p.id
            ORDER BY co.semestre, c.ciclo, c.codigo
        """)
        cursos_ofertados = cur.fetchall()
        
        # Organizar por semestre
        ofertados_por_semestre = defaultdict(list)
        for co in cursos_ofertados:
            ofertados_por_semestre[co['semestre']].append(co)
        
        print(f"✓ Obtenidos {len(cursos_ofertados)} cursos ofertados")
        return dict(ofertados_por_semestre)

def calcular_creditos_iniciales(año_ingreso, semestre_inicio="2020-2"):
    """
    Calcula los créditos aprobados iniciales para alumnos que ingresaron antes de 2020-2.
    Esto representa los cursos que ya aprobaron antes de nuestros registros.
    """
    año_inicio = int(semestre_inicio.split('-')[0])
    ciclo_inicio = int(semestre_inicio.split('-')[1])
    
    # Calcular cuántos semestres cursaron antes de 2020-2
    año_diff = año_inicio - año_ingreso
    semestres_cursados = año_diff * 2
    
    # Ajustar por ciclo
    if ciclo_inicio == 2:
        semestres_cursados += 1
    
    if semestres_cursados <= 0:
        return 0
    
    # Estimar créditos: ~22 créditos por semestre (considerando tasa de aprobación)
    # Con variación aleatoria ±15%
    creditos_teoricos = semestres_cursados * 22
    variacion = random.uniform(0.85, 1.15)
    creditos = int(creditos_teoricos * variacion)
    
    # No puede exceder 206 créditos (máximo antes de egresar)
    return min(creditos, 206)

def determinar_ciclo_relativo(creditos):
    """Determina el ciclo relativo según los créditos aprobados."""
    if creditos >= 208:
        return 11  # Egresado
    
    for ciclo, rango in CREDITOS_POR_CICLO.items():
        if isinstance(ciclo, int):
            min_cred, max_cred = rango
            if min_cred <= creditos <= max_cred:
                return ciclo
    
    return 1  # Por defecto

def verificar_prerrequisitos_cumplidos(curso_id, cursos_aprobados, prerrequisitos):
    """Verifica si un alumno ha aprobado todos los prerrequisitos de un curso."""
    if curso_id not in prerrequisitos:
        return True  # No tiene prerrequisitos
    
    prereqs_requeridos = prerrequisitos[curso_id]
    return all(prereq_id in cursos_aprobados for prereq_id in prereqs_requeridos)

def filtrar_cursos_disponibles(cursos_ofertados, ciclo_alumno, cursos_aprobados, 
                                cursos_matriculados_semestre, prerrequisitos):
    """
    Filtra los cursos que un alumno puede tomar en un semestre.
    - Ciclos 1-5: solo cursos de su ciclo
    - Ciclos 6+: cursos de su ciclo + electivos
    """
    disponibles = []
    
    for curso in cursos_ofertados:
        curso_id = curso['curso_id']
        ciclo_curso = curso['ciclo']
        tipo_curso = curso['tipo']
        
        # Ya aprobó este curso
        if curso_id in cursos_aprobados:
            continue
        
        # Ya está matriculado en este curso este semestre
        if curso_id in cursos_matriculados_semestre:
            continue
        
        # Verificar prerrequisitos
        if not verificar_prerrequisitos_cumplidos(curso_id, cursos_aprobados, prerrequisitos):
            continue
        
        # Filtrar por ciclo
        try:
            ciclo_curso_num = int(ciclo_curso) if ciclo_curso.isdigit() else 0
        except:
            ciclo_curso_num = 0
        
        # Antes del ciclo 6: puede tomar cursos de su ciclo o ciclos anteriores
        if ciclo_alumno < 6:
            if ciclo_curso_num <= ciclo_alumno and ciclo_curso_num > 0:
                disponibles.append(curso)
        else:
            # Ciclo 6+: puede tomar cursos de su ciclo o anteriores, o electivos
            if ciclo_curso_num <= ciclo_alumno or tipo_curso == 'E':
                disponibles.append(curso)
    
    return disponibles

def generar_nota(popularidad_profesor):
    """
    Genera una nota realista según la popularidad del profesor.
    - Popularidad alta: mejor distribución de notas
    - Popularidad baja: más notas bajas
    """
    if popularidad_profesor is None:
        popularidad_profesor = 0.5  # Por defecto
    else:
        popularidad_profesor = float(popularidad_profesor)
    
    # Ajustar probabilidad de aprobar según popularidad
    probabilidad_aprobar = TASA_APROBACION_BASE + (popularidad_profesor - 0.5) * 0.2
    probabilidad_aprobar = max(0.6, min(0.95, probabilidad_aprobar))
    
    if random.random() < probabilidad_aprobar:
        # Aprobado: nota entre 10 y 16, mayoría entre 10-12
        if random.random() < 0.7:
            nota = random.uniform(10.0, 12.5)
        else:
            nota = random.uniform(12.5, 16.0)
    else:
        # Desaprobado: nota entre 7 y 9.9
        nota = random.uniform(7.0, 9.9)
    
    return round(nota, 2)

def generar_matriculas_alumno(alumno, cursos_ofertados_por_semestre, prerrequisitos, todos_cursos, conn):
    """
    Genera el historial de matrículas para un alumno desde 2020-2 hasta 2025-2.
    Para alumnos antiguos (2017-2019), asigna créditos iniciales arbitrarios.
    """
    alumno_id = alumno['id']
    codigo_alumno = alumno['codigo']
    año_ingreso = int(codigo_alumno[:4])
    
    # Calcular créditos iniciales para alumnos que ingresaron antes de 2020-2
    creditos_acumulados = calcular_creditos_iniciales(año_ingreso)
    
    # Determinar qué cursos de ciclos inferiores "ya aprobó" (aproximación)
    # Para simplificar, asumimos que aprobó los cursos básicos según sus créditos
    cursos_aprobados = set()
    ciclo_actual = determinar_ciclo_relativo(creditos_acumulados)
    
    # Marcar cursos de ciclos anteriores como "aprobados" para validar prerrequisitos
    if creditos_acumulados > 0:
        cursos_basicos = [c for c in todos_cursos if c['ciclo'].isdigit() and int(c['ciclo']) < ciclo_actual]
        # Seleccionar aleatoriamente cursos que sumarían aproximadamente los créditos
        creditos_simulados = 0
        random.shuffle(cursos_basicos)
        for curso in cursos_basicos:
            if creditos_simulados < creditos_acumulados:
                cursos_aprobados.add(curso['id'])
                creditos_simulados += curso['creditos']
    
    matriculas = []
    
    print(f"  Procesando alumno {codigo_alumno} (año {año_ingreso}, créditos iniciales: {creditos_acumulados}, ciclo: {ciclo_actual})")
    
    # Determinar semestre de ingreso del alumno
    # Formato: YYYY (año) + 0/1/2/4 (modalidad) + secuencia
    mes_ingreso = codigo_alumno[4]  # 0/1 = marzo (semestre 1), 2/4 = agosto (semestre 2)
    if mes_ingreso in ['0', '1']:
        semestre_ingreso = f"{año_ingreso}-1"
    else:
        semestre_ingreso = f"{año_ingreso}-2"
    
    # Solo generar matrículas para semestres disponibles en BD (2020-2 a 2025-2)
    # Y solo desde el semestre en que ingresó el alumno
    for semestre in SEMESTRES_DISPONIBLES:
        año_semestre = int(semestre.split('-')[0])
        periodo_semestre = int(semestre.split('-')[1])
        
        # Validar que el alumno ya haya ingresado
        año_ingreso_efectivo = int(semestre_ingreso.split('-')[0])
        periodo_ingreso = int(semestre_ingreso.split('-')[1])
        
        if año_semestre < año_ingreso_efectivo:
            continue  # Semestre anterior al ingreso
        if año_semestre == año_ingreso_efectivo and periodo_semestre < periodo_ingreso:
            continue  # Mismo año pero periodo anterior
        
        # Si ya egresó, no se matricula más
        if creditos_acumulados >= 208:
            break
        
        # Obtener cursos disponibles para este semestre
        cursos_ofertados = cursos_ofertados_por_semestre.get(semestre, [])
        if not cursos_ofertados:
            continue
        
        # Filtrar cursos que puede tomar
        cursos_matriculados_semestre = set()
        cursos_disponibles = filtrar_cursos_disponibles(
            cursos_ofertados, 
            ciclo_actual, 
            cursos_aprobados, 
            cursos_matriculados_semestre,
            prerrequisitos
        )
        
        if not cursos_disponibles:
            continue
        
        # Eliminar duplicados por curso_id (múltiples secciones del mismo curso)
        # Mantener solo una sección por curso
        cursos_unicos = {}
        for curso in cursos_disponibles:
            curso_id = curso['curso_id']
            if curso_id not in cursos_unicos:
                cursos_unicos[curso_id] = curso
        cursos_disponibles = list(cursos_unicos.values())
        
        # Si no hay cursos disponibles, saltar este semestre
        if not cursos_disponibles:
            continue
        
        # PRIORIZACIÓN: Separar cursos obligatorios del ciclo actual
        cursos_obligatorios_ciclo = []
        cursos_otros = []
        
        for curso in cursos_disponibles:
            tipo_curso = curso['tipo']
            ciclo_curso = curso['ciclo']
            
            try:
                ciclo_curso_num = int(ciclo_curso) if ciclo_curso and str(ciclo_curso).isdigit() else 0
            except:
                ciclo_curso_num = 0
            
            # Curso obligatorio del ciclo actual
            if tipo_curso == 'O' and ciclo_curso_num == ciclo_actual:
                cursos_obligatorios_ciclo.append(curso)
            else:
                cursos_otros.append(curso)
        
        # SELECCIÓN: Priorizar obligatorios del ciclo actual
        cursos_seleccionados = []
        
        # 1. Matricular TODOS los cursos obligatorios del ciclo actual
        cursos_seleccionados.extend(cursos_obligatorios_ciclo)
        
        # 2. Rellenar con otros cursos hasta alcanzar 5-7 cursos totales
        num_obligatorios = len(cursos_obligatorios_ciclo)
        espacios_restantes = CURSOS_POR_SEMESTRE_MAX - num_obligatorios
        
        if espacios_restantes > 0 and cursos_otros:
            # Calcular cuántos cursos adicionales tomar
            if len(cursos_otros) >= espacios_restantes:
                num_adicionales = random.randint(
                    max(1, CURSOS_POR_SEMESTRE_MIN - num_obligatorios),
                    espacios_restantes
                )
            else:
                # Tomar todos los disponibles si no hay suficientes
                num_adicionales = len(cursos_otros)
            
            if num_adicionales > 0:
                cursos_adicionales = random.sample(cursos_otros, num_adicionales)
                cursos_seleccionados.extend(cursos_adicionales)
        
        # Si no se seleccionó ningún curso, saltar
        if not cursos_seleccionados:
            continue
        
        # Generar matrículas
        for curso_ofertado in cursos_seleccionados:
            curso_id = curso_ofertado['curso_id']
            curso_ofertado_id = curso_ofertado['id']
            creditos = curso_ofertado['creditos']
            popularidad = curso_ofertado['popularidad']
            
            # Marcar curso como matriculado en este semestre para evitar duplicados
            cursos_matriculados_semestre.add(curso_id)
            
            # Generar nota (excepto para 2025-2)
            if semestre == "2025-2":
                nota_final = None  # Sin nota aún
                estado = "Matriculado"
            else:
                nota_final = generar_nota(popularidad)
                estado = "Aprobado" if nota_final >= NOTA_APROBATORIA else "Desaprobado"
                
                # Si aprobó, actualizar créditos y cursos aprobados
                if nota_final >= NOTA_APROBATORIA:
                    creditos_acumulados += creditos
                    cursos_aprobados.add(curso_id)
            
            # Crear registro de matrícula
            mes = "03" if semestre.endswith('1') else "09"
            matricula = {
                'alumno_id': alumno_id,
                'curso_ofertado_id': curso_ofertado_id,
                'fecha_matricula': f"{año_semestre}-{mes}-01",
                'nota_final': nota_final,
                'estado': estado
            }
            matriculas.append(matricula)
            cursos_matriculados_semestre.add(curso_id)
        
        # Actualizar ciclo relativo después de cada semestre
        ciclo_actual = determinar_ciclo_relativo(creditos_acumulados)
    
    return matriculas

def generar_sql_inserts(matriculas, output_file):
    """Genera el archivo SQL con los INSERTs de matrículas."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("-- Limpiar datos existentes con TRUNCATE CASCADE\n")
        f.write("TRUNCATE TABLE log_ciclo_relativo, log_creditos, matricula RESTART IDENTITY CASCADE;\n\n")
        
        f.write("-- Resetear créditos de alumnos SIN TRIGGERS (se recalcularán después)\n")
        f.write("ALTER TABLE alumno DISABLE TRIGGER trigger_actualizar_ciclo_relativo;\n")
        f.write("UPDATE alumno SET creditos_aprobados = 0, ciclo_relativo = 1, promedio = 0;\n")
        f.write("ALTER TABLE alumno ENABLE TRIGGER trigger_actualizar_ciclo_relativo;\n\n")
        
        f.write(f"-- Insertar {len(matriculas)} matrículas\n")
        f.write("INSERT INTO matricula (alumno_id, curso_ofertado_id, fecha_matricula, nota_final, estado) VALUES\n")
        
        values = []
        for m in matriculas:
            nota = f"{m['nota_final']:.2f}" if m['nota_final'] is not None else "NULL"
            value = f"({m['alumno_id']}, {m['curso_ofertado_id']}, '{m['fecha_matricula']}', {nota}, '{m['estado']}')"
            values.append(value)
        
        f.write(',\n'.join(values) + ';\n')
    
    print(f"✓ Archivo SQL generado: {output_file}")

def main():
    """Función principal."""
    print("=" * 80)
    print("GENERADOR DE MATRÍCULAS HISTÓRICAS - TELECOMUNICACIONES")
    print("=" * 80)
    print()
    
    # Conectar a la base de datos
    conn = conectar_db()
    
    try:
        # Obtener datos necesarios
        print("\n📊 Cargando datos de la base de datos...")
        alumnos = obtener_alumnos(conn)
        cursos = obtener_cursos(conn)
        prerrequisitos = obtener_prerrequisitos(conn)
        cursos_ofertados_por_semestre = obtener_cursos_ofertados(conn)
        
        print(f"\n🎓 Generando matrículas para {len(alumnos)} alumnos...")
        print(f"📅 Semestres: {SEMESTRES_DISPONIBLES[0]} a {SEMESTRES_DISPONIBLES[-1]}")
        print()
        
        todas_matriculas = []
        
        for i, alumno in enumerate(alumnos, 1):
            if i % 50 == 0:
                print(f"  Progreso: {i}/{len(alumnos)} alumnos procesados...")
            
            matriculas_alumno = generar_matriculas_alumno(
                alumno, 
                cursos_ofertados_por_semestre, 
                prerrequisitos,
                cursos,
                conn
            )
            todas_matriculas.extend(matriculas_alumno)
        
        print(f"\n✓ Total de matrículas generadas: {len(todas_matriculas)}")
        
        # Generar archivo SQL
        output_file = 'generar_matriculas.sql'
        generar_sql_inserts(todas_matriculas, output_file)
        
        print("\n" + "=" * 80)
        print("PROCESO COMPLETADO")
        print("=" * 80)
        print(f"📄 Archivo generado: {output_file}")
        print(f"📊 Total matrículas: {len(todas_matriculas)}")
        print("\nSiguiente paso:")
        print("  Ejecutar el archivo SQL en la base de datos para insertar las matrículas")
        print("=" * 80)
        
    finally:
        conn.close()

if __name__ == '__main__':
    main()
