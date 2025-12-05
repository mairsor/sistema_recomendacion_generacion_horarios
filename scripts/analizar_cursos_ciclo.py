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
print("CURSOS POR CICLO EN LA BASE DE DATOS")
print("=" * 80)

try:
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    
    # Contar cursos por ciclo
    cur.execute("""
        SELECT 
            ciclo,
            COUNT(*) as total_cursos,
            STRING_AGG(DISTINCT codigo, ', ' ORDER BY codigo) as codigos
        FROM curso
        WHERE ciclo ~ '^[0-9]+$'
        GROUP BY ciclo
        ORDER BY CAST(ciclo AS INTEGER)
    """)
    
    cursos_ciclo = cur.fetchall()
    
    print(f"\n📚 Cursos por ciclo:")
    print(f"{'Ciclo':<8} {'Total':<8} Códigos")
    print("-" * 80)
    for c in cursos_ciclo:
        print(f"{c['ciclo']:<8} {c['total_cursos']:<8} {c['codigos'][:60]}...")
    
    # Ver cursos ofertados por ciclo
    cur.execute("""
        SELECT 
            c.ciclo,
            COUNT(DISTINCT co.id) as ofertas,
            COUNT(DISTINCT co.semestre) as semestres
        FROM curso c
        JOIN curso_ofertado co ON c.id = co.curso_id
        WHERE c.ciclo ~ '^[0-9]+$'
        GROUP BY c.ciclo
        ORDER BY CAST(c.ciclo AS INTEGER)
    """)
    
    ofertas = cur.fetchall()
    
    print(f"\n📅 Cursos ofertados por ciclo:")
    print(f"{'Ciclo':<8} {'Ofertas':<10} {'Semestres'}")
    print("-" * 80)
    for o in ofertas:
        print(f"{o['ciclo']:<8} {o['ofertas']:<10} {o['semestres']}")
    
    # Ver ejemplo de ciclo 2
    cur.execute("""
        SELECT DISTINCT c.codigo, c.nombre, c.creditos, c.tipo
        FROM curso c
        WHERE c.ciclo = '2'
        ORDER BY c.codigo
    """)
    
    cursos_2 = cur.fetchall()
    
    print(f"\n🔍 Cursos de ciclo 2:")
    print(f"{'Código':<10} {'Nombre':<45} {'Créd':<6} {'Tipo'}")
    print("-" * 80)
    for c in cursos_2:
        print(f"{c['codigo']:<10} {c['nombre']:<45} {c['creditos']:<6} {c['tipo']}")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")

print("\n" + "=" * 80)
