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
print("ANÁLISIS DETALLADO - ESTUDIANTES 2022")
print("=" * 80)

try:
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    
    # Ver distribución de matrículas para 2022
    cur.execute("""
        SELECT 
            a.codigo,
            a.ciclo_relativo,
            a.creditos_aprobados,
            COUNT(m.id) as total_matriculas,
            SUM(CASE WHEN m.estado = 'Aprobado' THEN 1 ELSE 0 END) as aprobadas,
            STRING_AGG(DISTINCT co.semestre, ', ' ORDER BY co.semestre) as semestres
        FROM alumno a
        LEFT JOIN matricula m ON a.id = m.alumno_id
        LEFT JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
        WHERE a.codigo LIKE '2022%'
        GROUP BY a.codigo, a.ciclo_relativo, a.creditos_aprobados
        ORDER BY total_matriculas DESC, a.codigo
        LIMIT 20
    """)
    
    resultados = cur.fetchall()
    print(f"\n{'Código':<15} {'Ciclo':<6} {'Créd':<6} {'Matr':<6} {'Aprob':<6} Semestres")
    print("-" * 80)
    for r in resultados:
        print(f"{r['codigo']:<15} {r['ciclo_relativo']:<6} {r['creditos_aprobados']:<6} {r['total_matriculas'] or 0:<6} {r['aprobadas'] or 0:<6} {r['semestres'] or ''}")
    
    # Ver semestres disponibles desde 2022
    cur.execute("""
        SELECT DISTINCT semestre 
        FROM curso_ofertado 
        WHERE semestre >= '2022-1' 
        ORDER BY semestre
    """)
    semestres = [r['semestre'] for r in cur.fetchall()]
    print(f"\n📅 Semestres disponibles desde 2022-1: {', '.join(semestres)}")
    print(f"   Total: {len(semestres)} semestres")
    
    # Estadísticas generales de 2022
    cur.execute("""
        SELECT 
            COUNT(DISTINCT a.id) as total_2022,
            COUNT(DISTINCT CASE WHEN m.id IS NOT NULL THEN a.id END) as con_matriculas,
            COUNT(DISTINCT CASE WHEN m.id IS NULL THEN a.id END) as sin_matriculas,
            AVG(a.ciclo_relativo) as ciclo_promedio,
            AVG(a.creditos_aprobados) as creditos_promedio
        FROM alumno a
        LEFT JOIN matricula m ON a.id = m.alumno_id
        WHERE a.codigo LIKE '2022%'
    """)
    stats = cur.fetchone()
    
    print(f"\n📊 Estadísticas estudiantes 2022:")
    print(f"   • Total: {stats['total_2022']}")
    print(f"   • Con matrículas: {stats['con_matriculas']}")
    print(f"   • Sin matrículas: {stats['sin_matriculas']}")
    print(f"   • Ciclo promedio: {stats['ciclo_promedio']:.1f}")
    print(f"   • Créditos promedio: {stats['creditos_promedio']:.1f}")
    
    # Ver un ejemplo detallado
    cur.execute("""
        SELECT 
            a.codigo,
            co.semestre,
            c.codigo as codigo_curso,
            c.nombre as nombre_curso,
            c.creditos,
            m.nota_final,
            m.estado
        FROM alumno a
        JOIN matricula m ON a.id = m.alumno_id
        JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
        JOIN curso c ON co.curso_id = c.id
        WHERE a.codigo LIKE '2022%'
        ORDER BY a.codigo, co.semestre
        LIMIT 30
    """)
    
    matriculas = cur.fetchall()
    if matriculas:
        print(f"\n🔍 Ejemplo - Primeras matrículas de estudiantes 2022:")
        print(f"{'Código':<15} {'Semestre':<10} {'Curso':<10} {'Nombre':<40} {'Créd':<5} {'Nota':<6} {'Estado'}")
        print("-" * 110)
        for m in matriculas:
            print(f"{m['codigo']:<15} {m['semestre']:<10} {m['codigo_curso']:<10} {m['nombre_curso']:<40} {m['creditos']:<5} {m['nota_final']:<6.2f} {m['estado']}")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)
