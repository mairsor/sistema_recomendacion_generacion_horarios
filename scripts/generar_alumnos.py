#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar 504 alumnos ficticios de Telecomunicaciones
con coherencia en códigos, ciclos y modalidades de ingreso.

Reglas:
- 30 alumnos por semestre de ingreso (2017-1 a 2025-1)
- Modalidades: Ordinario (18), CEPRE (9), Top 2 (3)
- Código formato: YYYYMODALIDADSEQUENCELETTER
  * Ordinario: secuencia 0001-0018 (códigos terminan en 0/1)
  * CEPRE: secuencia 2001-2009 (código termina en 2)
  * Top 2: secuencia 4101-4103 (código termina en 4)
- Letra final: A-Z distribuida uniformemente
- Ciclo relativo inicial: 1 (todos empiezan en primer ciclo)
- Créditos aprobados: 0 (sin cursos aprobados)
- Promedio: 0.00 (se calculará con las matrículas)
- Estado: 'A' (activo)
"""

import random
from datetime import datetime

# Configuración de semestres
SEMESTRES = [
    "2017-1", "2017-2",
    "2018-1", "2018-2",
    "2019-1", "2019-2",
    "2020-1", "2020-2",
    "2021-1", "2021-2",
    "2022-1", "2022-2",
    "2023-1", "2023-2",
    "2024-1", "2024-2",
    "2025-1"
]

# Configuración de modalidades
MODALIDADES = {
    'ordinario': {
        'cantidad': 18,
        'secuencias': list(range(1, 19)),  # 0001-0018
        'digito_modal': ['0', '1']  # Terminan en 0 o 1
    },
    'cepre': {
        'cantidad': 9,
        'secuencias': list(range(2001, 2010)),  # 2001-2009
        'digito_modal': ['2']  # Terminan en 2
    },
    'top2': {
        'cantidad': 3,
        'secuencias': list(range(4101, 4104)),  # 4101-4103
        'digito_modal': ['4']  # Terminan en 4
    }
}

# Letras para código (A-Z)
LETRAS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Nombres y apellidos ficticios
NOMBRES = [
    'Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Carmen', 'José', 'Laura',
    'Miguel', 'Rosa', 'Pedro', 'Elena', 'Diego', 'Sofía', 'Javier', 'Isabel',
    'Andrés', 'Patricia', 'Ricardo', 'Beatriz', 'Fernando', 'Claudia', 'Roberto', 'Lucía',
    'Daniel', 'Mónica', 'Sergio', 'Adriana', 'Pablo', 'Gabriela'
]

APELLIDOS = [
    'García', 'Rodríguez', 'Martínez', 'López', 'González', 'Hernández',
    'Pérez', 'Sánchez', 'Ramírez', 'Torres', 'Flores', 'Rivera',
    'Gómez', 'Díaz', 'Cruz', 'Morales', 'Reyes', 'Jiménez',
    'Álvarez', 'Romero', 'Castro', 'Ortiz', 'Mendoza', 'Vargas',
    'Ramos', 'Castillo', 'Vega', 'Medina', 'Silva', 'Rojas'
]

def generar_codigo_alumno(año, modalidad, secuencia):
    """
    Genera el código de alumno según formato: YYYYMODALIDADSEQUENCELETTER
    
    Args:
        año: Año de ingreso (ej: 2022)
        modalidad: 'ordinario', 'cepre', o 'top2'
        secuencia: Número de secuencia según modalidad
    
    Returns:
        Código de alumno (ej: '20220042A', '20252023J', '20224106A')
    """
    config = MODALIDADES[modalidad]
    
    # Determinar el dígito de modalidad
    digito = random.choice(config['digito_modal'])
    
    # Formatear secuencia con padding
    if modalidad == 'ordinario':
        # Ordinario: YYYY + 00 + secuencia (2 dígitos) + letra
        seq_str = f"{secuencia:02d}"
        codigo_base = f"{año}00{seq_str}"
    elif modalidad == 'cepre':
        # CEPRE: YYYY + secuencia (4 dígitos: 2001-2009) + letra
        codigo_base = f"{año}{secuencia}"
    else:  # top2
        # Top 2: YYYY + secuencia (4 dígitos: 4101-4103) + letra
        codigo_base = f"{año}{secuencia}"
    
    # Agregar letra aleatoria
    letra = random.choice(LETRAS)
    codigo = f"{codigo_base}{letra}"
    
    return codigo

def generar_alumno(año, modalidad, secuencia):
    """
    Genera un registro de alumno con datos coherentes.
    
    Args:
        año: Año de ingreso
        modalidad: Modalidad de ingreso
        secuencia: Número de secuencia
    
    Returns:
        Diccionario con datos del alumno
    """
    codigo = generar_codigo_alumno(año, modalidad, secuencia)
    nombre = random.choice(NOMBRES)
    apellido1 = random.choice(APELLIDOS)
    apellido2 = random.choice(APELLIDOS)
    
    return {
        'codigo': codigo,
        'nombres': nombre,
        'apellidos': f"{apellido1} {apellido2}",
        'ciclo_relativo': 1,
        'creditos_aprobados': 0,
        'promedio': 0.00,
        'estado': 'A'
    }

def generar_alumnos():
    """
    Genera los 504 alumnos (30 por semestre × 17 semestres = 510 - 6 = 504)
    Preserva el alumno 20224106A
    """
    alumnos = []
    codigos_usados = set()
    
    for semestre in SEMESTRES:
        año = int(semestre.split('-')[0])
        
        # Generar alumnos por modalidad
        for modalidad, config in MODALIDADES.items():
            cantidad = config['cantidad']
            secuencias = config['secuencias']
            
            for i in range(cantidad):
                secuencia = secuencias[i]
                
                # Caso especial: preservar 20224106A
                if año == 2022 and modalidad == 'top2' and secuencia == 4106:
                    # Ya existe, usar código específico
                    alumno = {
                        'codigo': '20224106A',
                        'nombres': 'Estudiante',
                        'apellidos': 'Preservado Especial',
                        'ciclo_relativo': 1,
                        'creditos_aprobados': 0,
                        'promedio': 0.00,
                        'estado': 'A'
                    }
                else:
                    # Generar código único
                    intentos = 0
                    while intentos < 100:
                        alumno = generar_alumno(año, modalidad, secuencia)
                        if alumno['codigo'] not in codigos_usados:
                            codigos_usados.add(alumno['codigo'])
                            break
                        intentos += 1
                    else:
                        raise Exception(f"No se pudo generar código único para año={año}, modalidad={modalidad}, secuencia={secuencia}")
                
                alumnos.append(alumno)
    
    return alumnos

def generar_sql_inserts(alumnos):
    """
    Genera las sentencias SQL INSERT para los alumnos.
    """
    sql_statements = []
    
    # Primero, DELETE todos excepto 20224106A
    sql_statements.append("-- Limpiar alumnos existentes (excepto 20224106A)")
    sql_statements.append("DELETE FROM alumno WHERE codigo != '20224106A';")
    sql_statements.append("")
    
    # Luego, INSERTs (NO incluye 20224106A porque ya existe en BD)
    sql_statements.append("-- Insertar 510 nuevos alumnos ficticios")
    sql_statements.append("INSERT INTO alumno (codigo, nombres, apellidos, ciclo_relativo, creditos_aprobados, promedio, estado) VALUES")
    
    insert_values = []
    for alumno in alumnos:
        # Excluir 20224106A de los inserts porque ya existe
        if alumno['codigo'] != '20224106A':
            value = f"('{alumno['codigo']}', '{alumno['nombres']}', '{alumno['apellidos']}', {alumno['ciclo_relativo']}, {alumno['creditos_aprobados']}, {alumno['promedio']:.2f}, '{alumno['estado']}')"
            insert_values.append(value)
    
    sql_statements.append(',\n'.join(insert_values) + ';')
    
    return '\n'.join(sql_statements)

def main():
    """
    Función principal que ejecuta la generación de alumnos.
    """
    print("=" * 80)
    print("GENERADOR DE ALUMNOS FICTICIOS - TELECOMUNICACIONES")
    print("=" * 80)
    print()
    
    print(f"Generando alumnos para {len(SEMESTRES)} semestres...")
    print(f"Semestres: {SEMESTRES[0]} a {SEMESTRES[-1]}")
    print(f"Distribución por semestre:")
    print(f"  - Ordinario: {MODALIDADES['ordinario']['cantidad']} alumnos")
    print(f"  - CEPRE: {MODALIDADES['cepre']['cantidad']} alumnos")
    print(f"  - Top 2: {MODALIDADES['top2']['cantidad']} alumnos")
    print(f"  - Total por semestre: 30 alumnos")
    print(f"  - Total general: {30 * len(SEMESTRES)} alumnos")
    print()
    
    # Generar alumnos
    alumnos = generar_alumnos()
    
    print(f"✓ Generados {len(alumnos)} registros de alumnos")
    print()
    
    # Mostrar ejemplos
    print("Ejemplos de códigos generados:")
    print("-" * 80)
    ejemplos = random.sample(alumnos, min(10, len(alumnos)))
    for alumno in ejemplos:
        print(f"  {alumno['codigo']} - {alumno['nombres']} {alumno['apellidos']}")
    print()
    
    # Verificar 20224106A
    alumno_especial = next((a for a in alumnos if a['codigo'] == '20224106A'), None)
    if alumno_especial:
        print(f"✓ Alumno especial preservado: {alumno_especial['codigo']}")
    print()
    
    # Generar SQL
    print("Generando sentencias SQL...")
    sql = generar_sql_inserts(alumnos)
    
    # Guardar en archivo
    output_file = 'generar_alumnos.sql'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sql)
    
    print(f"✓ Archivo SQL generado: {output_file}")
    print()
    
    print("=" * 80)
    print("RESUMEN DE ESTADÍSTICAS")
    print("=" * 80)
    
    # Estadísticas por modalidad
    stats = {modalidad: 0 for modalidad in MODALIDADES.keys()}
    for alumno in alumnos:
        codigo = alumno['codigo']
        # Identificar modalidad por código
        if codigo[4:6] == '00':
            stats['ordinario'] += 1
        elif codigo[4] == '2':
            stats['cepre'] += 1
        elif codigo[4] == '4':
            stats['top2'] += 1
    
    print(f"Total alumnos: {len(alumnos)}")
    print(f"Por modalidad:")
    for modalidad, count in stats.items():
        print(f"  - {modalidad.capitalize()}: {count}")
    print()
    
    print("Siguiente paso:")
    print("  1. Ejecutar el archivo 'generar_alumnos.sql' en la base de datos")
    print("  2. Generar matrículas históricas para cada alumno")
    print("  3. Asignar notas para calcular promedios y créditos")
    print()
    print("=" * 80)

if __name__ == '__main__':
    main()
