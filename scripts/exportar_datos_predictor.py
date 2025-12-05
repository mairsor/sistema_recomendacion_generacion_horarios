#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para exportar datos de PostgreSQL al formato CSV del predictor de demanda.

Genera un archivo CSV con el mismo formato que matriculas_por_curso.csv:
- curso_ofertado_id
- nombre_seccion
- codigo_curso
- semestre
- creditos
- tipo_curso
- profesor_id
- profesor_popularidad
- alumnos_previos
- variacion_matricula
- num_prerrequisitos
- tasa_aprobacion
- franja_horaria
- alumnos_elegibles
- cupo_maximo
- alumnos_matriculados
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import csv
import os
from collections import defaultdict

# Configuración de conexión
DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

# Archivo de salida
OUTPUT_FILE = '../predictor_demanda_api/data/matriculas_por_curso_generado.csv'

def calcular_franja_horaria(turno):
    """Calcula la franja horaria basada en el turno."""
    if turno is None or turno == '':
        return 1
    
    turno_lower = turno.lower()
    
    if 'mañana' in turno_lower or 'manana' in turno_lower:
        return 1
    elif 'tarde' in turno_lower:
        return 2
    elif 'noche' in turno_lower:
        return 3
    else:
        return 1  # Por defecto

def calcular_popularidad_profesor(conn, profesor_id):
    """Calcula la popularidad de un profesor basada en notas promedio y tasa de aprobación."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT 
                AVG(m.nota_final) as promedio_notas,
                COUNT(CASE WHEN m.estado = 'Aprobado' THEN 1 END)::float / 
                NULLIF(COUNT(CASE WHEN m.estado IN ('Aprobado', 'Desaprobado') THEN 1 END), 0) as tasa_aprobacion
            FROM matricula m
            JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
            WHERE co.profesor_id = %s
            AND m.estado IN ('Aprobado', 'Desaprobado')
        """, (profesor_id,))
        
        result = cur.fetchone()
        
        if result['promedio_notas'] is None or result['tasa_aprobacion'] is None:
            return 0.75  # Valor por defecto
        
        # Normalizar: nota promedio (escala 7-16 a 0-1) + tasa aprobación, dividido entre 2
        nota_norm = (float(result['promedio_notas']) - 7) / 9  # 7-16 -> 0-1
        popularidad = (nota_norm + float(result['tasa_aprobacion'])) / 2
        
        return round(max(0.5, min(1.0, popularidad)), 2)

def contar_prerrequisitos(conn, curso_id):
    """Cuenta cuántos prerrequisitos tiene un curso."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) 
            FROM curso_prerrequisito 
            WHERE curso_id = %s
        """, (curso_id,))
        return cur.fetchone()[0]

def calcular_tasa_aprobacion(conn, curso_id, semestre_hasta):
    """Calcula la tasa de aprobación histórica de un curso."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                COUNT(CASE WHEN m.estado = 'Aprobado' THEN 1 END)::float / 
                NULLIF(COUNT(CASE WHEN m.estado IN ('Aprobado', 'Desaprobado') THEN 1 END), 0) as tasa
            FROM matricula m
            JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
            WHERE co.curso_id = %s
            AND co.semestre < %s
            AND m.estado IN ('Aprobado', 'Desaprobado')
        """, (curso_id, semestre_hasta))
        
        result = cur.fetchone()[0]
        return round(result if result else 0.75, 2)

def calcular_alumnos_elegibles(conn, curso_id, ciclo_curso, semestre):
    """
    Estima cuántos alumnos son elegibles para tomar el curso.
    - Si es ciclo 1: todos los alumnos de ciclo 1+
    - Si es ciclo N: alumnos de ciclo N+ que cumplan prerrequisitos
    """
    try:
        ciclo_num = int(ciclo_curso)
    except:
        ciclo_num = 1
    
    with conn.cursor() as cur:
        # Contar alumnos en el ciclo adecuado al momento del semestre
        cur.execute("""
            SELECT COUNT(DISTINCT a.id)
            FROM alumno a
            WHERE a.ciclo_relativo >= %s
        """, (ciclo_num,))
        
        return cur.fetchone()[0]

def exportar_datos():
    """Función principal que exporta los datos."""
    print("=" * 80)
    print("EXPORTADOR DE DATOS PARA PREDICTOR DE DEMANDA")
    print("=" * 80)
    print()
    
    # Conectar a la base de datos
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Conexión exitosa a la base de datos\n")
    except Exception as e:
        print(f"✗ Error al conectar: {e}")
        return
    
    # Obtener datos de cursos ofertados
    print("📊 Extrayendo datos de cursos ofertados...")
    
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        # Solo cursos con matrículas completadas (no 2025-2) y con al menos 1 alumno
        cur.execute("""
            SELECT 
                co.id as curso_ofertado_id,
                co.codigo_seccion,
                c.codigo as codigo_curso,
                c.nombre as nombre_curso,
                co.semestre,
                c.creditos,
                c.tipo as tipo_curso,
                c.ciclo as ciclo_curso,
                co.profesor_id,
                co.turno,
                co.cupos_disponibles as cupo_maximo,
                c.id as curso_id,
                COUNT(m.id) as alumnos_matriculados
            FROM curso_ofertado co
            JOIN curso c ON co.curso_id = c.id
            INNER JOIN matricula m ON co.id = m.curso_ofertado_id
            WHERE co.semestre < '2025-2'  -- Solo histórico completo
            GROUP BY co.id, co.codigo_seccion, c.codigo, c.nombre, co.semestre, 
                     c.creditos, c.tipo, c.ciclo, co.profesor_id, co.turno, 
                     co.cupos_disponibles, c.id
            HAVING COUNT(m.id) > 0  -- Solo secciones con al menos 1 alumno
            ORDER BY co.semestre, c.codigo, co.codigo_seccion
        """)
        
        cursos = cur.fetchall()
    
    print(f"✓ Obtenidos {len(cursos)} registros de cursos ofertados\n")
    
    # Preparar datos para CSV
    print("🔄 Procesando datos...")
    datos_csv = []
    
    # Diccionario para almacenar alumnos previos por curso
    alumnos_por_curso_semestre = defaultdict(int)
    
    for i, curso in enumerate(cursos):
        # Calcular métricas
        profesor_popularidad = calcular_popularidad_profesor(conn, curso['profesor_id'])
        num_prerrequisitos = contar_prerrequisitos(conn, curso['curso_id'])
        tasa_aprobacion = calcular_tasa_aprobacion(conn, curso['curso_id'], curso['semestre'])
        franja_horaria = calcular_franja_horaria(curso['turno'])
        alumnos_elegibles = calcular_alumnos_elegibles(conn, curso['curso_id'], 
                                                       curso['ciclo_curso'], curso['semestre'])
        
        # Obtener alumnos previos (del semestre anterior)
        key_actual = f"{curso['codigo_curso']}_{curso['semestre']}"
        
        # Buscar semestre anterior
        año, periodo = curso['semestre'].split('-')
        if periodo == '1':
            semestre_anterior = f"{int(año) - 1}-2"
        else:
            semestre_anterior = f"{año}-1"
        
        key_anterior = f"{curso['codigo_curso']}_{semestre_anterior}"
        alumnos_previos = alumnos_por_curso_semestre.get(key_anterior, curso['alumnos_matriculados'])
        
        # Guardar valor actual para futuros cálculos
        alumnos_por_curso_semestre[key_actual] = curso['alumnos_matriculados']
        
        # Calcular variación
        if alumnos_previos > 0:
            variacion_matricula = round((curso['alumnos_matriculados'] - alumnos_previos) / alumnos_previos, 3)
        else:
            variacion_matricula = 0.0
        
        # Nombre de sección
        nombre_seccion = f"{curso['codigo_curso']}-{curso['semestre']}-{curso['codigo_seccion']}"
        
        # Cupo máximo (si es NULL, usar el 120% de matriculados)
        cupo_maximo = curso['cupo_maximo'] if curso['cupo_maximo'] else int(curso['alumnos_matriculados'] * 1.2)
        
        datos_csv.append({
            'curso_ofertado_id': curso['curso_ofertado_id'],
            'nombre_seccion': nombre_seccion,
            'codigo_curso': curso['codigo_curso'],
            'semestre': curso['semestre'],
            'creditos': curso['creditos'],
            'tipo_curso': curso['tipo_curso'],
            'profesor_id': curso['profesor_id'],
            'profesor_popularidad': profesor_popularidad,
            'alumnos_previos': alumnos_previos,
            'variacion_matricula': variacion_matricula,
            'num_prerrequisitos': num_prerrequisitos,
            'tasa_aprobacion': tasa_aprobacion,
            'franja_horaria': franja_horaria,
            'alumnos_elegibles': alumnos_elegibles,
            'cupo_maximo': cupo_maximo,
            'alumnos_matriculados': curso['alumnos_matriculados']
        })
        
        if (i + 1) % 100 == 0:
            print(f"  Procesados {i + 1}/{len(cursos)} cursos...")
    
    print(f"✓ Procesamiento completado\n")
    
    # Escribir CSV
    print(f"💾 Escribiendo archivo: {OUTPUT_FILE}")
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'curso_ofertado_id', 'nombre_seccion', 'codigo_curso', 'semestre',
            'creditos', 'tipo_curso', 'profesor_id', 'profesor_popularidad',
            'alumnos_previos', 'variacion_matricula', 'num_prerrequisitos',
            'tasa_aprobacion', 'franja_horaria', 'alumnos_elegibles',
            'cupo_maximo', 'alumnos_matriculados'
        ]
        
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datos_csv)
    
    print(f"✓ Archivo generado exitosamente")
    print(f"✓ Total de registros: {len(datos_csv)}\n")
    
    # Estadísticas
    print("📈 Estadísticas de los datos exportados:")
    print(f"   • Semestres: {min(d['semestre'] for d in datos_csv)} a {max(d['semestre'] for d in datos_csv)}")
    print(f"   • Cursos únicos: {len(set(d['codigo_curso'] for d in datos_csv))}")
    print(f"   • Profesores: {len(set(d['profesor_id'] for d in datos_csv))}")
    print(f"   • Total matrículas: {sum(d['alumnos_matriculados'] for d in datos_csv):,}")
    print(f"   • Promedio por curso: {sum(d['alumnos_matriculados'] for d in datos_csv) / len(datos_csv):.1f}")
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("EXPORTACIÓN COMPLETADA")
    print("=" * 80)
    print(f"\n📄 Archivo generado: {os.path.abspath(OUTPUT_FILE)}")
    print("\n💡 Siguiente paso:")
    print("   Actualiza tu predictor para usar: matriculas_por_curso_generado.csv")
    print("=" * 80)

if __name__ == "__main__":
    exportar_datos()
