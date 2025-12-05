#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

print("=" * 80)
print("VERIFICACIÓN DE DUPLICADOS - MISMO CURSO EN MISMO SEMESTRE")
print("=" * 80)

try:
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    
    # Buscar duplicados: mismo alumno, mismo curso_id, mismo semestre
    cur.execute("""
        SELECT 
            a.codigo,
            co.semestre,
            c.codigo as codigo_curso,
            c.nombre as nombre_curso,
            COUNT(*) as veces
        FROM matricula m
        JOIN alumno a ON m.alumno_id = a.id
        JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
        JOIN curso c ON co.curso_id = c.id
        GROUP BY a.codigo, co.semestre, c.codigo, c.nombre
        HAVING COUNT(*) > 1
        ORDER BY veces DESC, a.codigo
        LIMIT 20
    """)
    
    duplicados = cur.fetchall()
    
    if duplicados:
        print(f"\n❌ {len(duplicados)} casos de duplicados encontrados:\n")
        print(f"{'Alumno':<15} {'Semestre':<10} {'Código':<10} {'Curso':<40} {'Veces'}")
        print("-" * 90)
        for d in duplicados:
            print(f"{d['codigo']:<15} {d['semestre']:<10} {d['codigo_curso']:<10} {d['nombre_curso']:<40} {d['veces']}")
    else:
        print("\n✅ No se encontraron duplicados de curso_id en mismo semestre\n")
    
    # Estadísticas generales
    cur.execute("""
        SELECT 
            COUNT(DISTINCT a.id) as alumnos,
            COUNT(*) as matriculas,
            AVG(cnt) as prom_matriculas
        FROM (
            SELECT alumno_id, COUNT(*) as cnt
            FROM matricula
            GROUP BY alumno_id
        ) sub, alumno a
        WHERE sub.alumno_id = a.id
    """)
    
    stats = cur.fetchone()
    print(f"\n📊 Estadísticas:")
    print(f"   • Total alumnos: {stats['alumnos']}")
    print(f"   • Total matrículas: {stats['matriculas']}")
    print(f"   • Promedio por alumno: {stats['prom_matriculas']:.1f}\n")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")

print("=" * 80)
print("VERIFICACIÓN COMPLETADA")
print("=" * 80)
