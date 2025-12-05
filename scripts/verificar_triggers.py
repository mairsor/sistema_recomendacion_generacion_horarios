#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

print("=" * 80)
print("TRIGGERS EN TABLA ALUMNO")
print("=" * 80)

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Consultar triggers
    cur.execute("""
        SELECT tgname, proname as function_name, tgenabled
        FROM pg_trigger t
        JOIN pg_proc p ON t.tgfoid = p.oid
        WHERE tgrelid = 'alumno'::regclass
        AND tgisinternal = false
        ORDER BY tgname
    """)
    
    triggers = cur.fetchall()
    
    if triggers:
        print(f"\n✓ {len(triggers)} triggers encontrados:\n")
        for tgname, func, enabled in triggers:
            status = "ENABLED" if enabled == 'O' else "DISABLED"
            print(f"  • {tgname}")
            print(f"    Función: {func}")
            print(f"    Estado: {status}\n")
    else:
        print("\n⚠️  No se encontraron triggers en la tabla alumno\n")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")
