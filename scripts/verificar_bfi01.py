import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

conn = psycopg2.connect(**DB_CONFIG)

print("=" * 80)
print("ANÁLISIS DE BFI01")
print("=" * 80)

with conn.cursor(cursor_factory=RealDictCursor) as cur:
    # Total de secciones y matrículas
    cur.execute("""
        SELECT 
            COUNT(DISTINCT co.id) as total_secciones,
            COUNT(m.id) as total_matriculas,
            COUNT(DISTINCT m.id) as matriculas_unicas
        FROM curso c
        JOIN curso_ofertado co ON c.id = co.curso_id
        LEFT JOIN matricula m ON co.id = m.curso_ofertado_id
        WHERE c.codigo = 'BFI01'
    """)
    
    totales = cur.fetchone()
    print(f"\nTOTALES:")
    print(f"  • Secciones ofertadas: {totales['total_secciones']}")
    print(f"  • Total matrículas: {totales['total_matriculas']}")
    print(f"  • Matrículas únicas: {totales['matriculas_unicas']}")
    
    # Secciones con y sin matrículas
    cur.execute("""
        SELECT 
            co.semestre,
            co.codigo_seccion,
            COUNT(m.id) as alumnos
        FROM curso c
        JOIN curso_ofertado co ON c.id = co.curso_id
        LEFT JOIN matricula m ON co.id = m.curso_ofertado_id
        WHERE c.codigo = 'BFI01' AND co.semestre < '2025-2'
        GROUP BY co.id, co.semestre, co.codigo_seccion
        ORDER BY co.semestre, co.codigo_seccion
    """)
    
    secciones = cur.fetchall()
    con_alumnos = [s for s in secciones if s['alumnos'] > 0]
    sin_alumnos = [s for s in secciones if s['alumnos'] == 0]
    
    print(f"\n  • Secciones con alumnos: {len(con_alumnos)}")
    print(f"  • Secciones sin alumnos: {len(sin_alumnos)}")
    
    print(f"\nSECCIONES CON ALUMNOS:")
    for s in con_alumnos:
        print(f"  {s['semestre']}-{s['codigo_seccion']}: {s['alumnos']} alumnos")
    
    print(f"\nSECCIONES SIN ALUMNOS:")
    for s in sin_alumnos[:10]:  # Solo primeras 10
        print(f"  {s['semestre']}-{s['codigo_seccion']}: 0 alumnos")
    if len(sin_alumnos) > 10:
        print(f"  ... y {len(sin_alumnos) - 10} más")
    
    # Verificar cuántos alumnos están en ciclo 1
    cur.execute("""
        SELECT COUNT(DISTINCT id) as total_alumnos_ciclo1
        FROM alumno
        WHERE ciclo_relativo = 1
    """)
    
    alumnos_ciclo1 = cur.fetchone()['total_alumnos_ciclo1']
    print(f"\nTOTAL ALUMNOS EN CICLO 1: {alumnos_ciclo1}")
    print(f"Deberían matricularse en BFI01 (curso de ciclo 1)")

conn.close()
print("\n" + "=" * 80)
