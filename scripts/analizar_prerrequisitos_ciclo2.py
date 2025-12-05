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

conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
cur = conn.cursor()

# Prerrequisitos de ciclo 2
cur.execute("""
    SELECT 
        c.codigo, 
        c.nombre,
        c2.codigo as prereq_codigo,
        c2.nombre as prereq_nombre,
        c2.ciclo as prereq_ciclo
    FROM curso c
    LEFT JOIN curso_prerrequisito p ON c.id = p.curso_id
    LEFT JOIN curso c2 ON p.prereq_id = c2.id
    WHERE c.ciclo = '2'
    ORDER BY c.codigo
""")

rows = cur.fetchall()

print("\n" + "=" * 100)
print("PRERREQUISITOS DE CURSOS DE CICLO 2")
print("=" * 100)
print(f"\n{'Curso':<10} {'Nombre del Curso':<45} {'Prereq':<10} {'Nombre Prerrequisito':<30} {'Ciclo'}")
print("-" * 100)

for r in rows:
    prereq = r['prereq_codigo'] or 'N/A'
    prereq_nombre = r['prereq_nombre'] or 'Sin prerrequisito'
    prereq_ciclo = r['prereq_ciclo'] or '-'
    print(f"{r['codigo']:<10} {r['nombre']:<45} {prereq:<10} {prereq_nombre:<30} {prereq_ciclo}")

conn.close()
print("=" * 100)
