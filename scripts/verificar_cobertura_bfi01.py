#!/usr/bin/env python3
"""Verificar que todos los alumnos de ciclo 1 estén matriculados en BFI01"""

import psycopg2
from psycopg2.extras import RealDictCursor

# Configuración de conexión
DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'database': 'schedule_db',
    'user': 'admin',
    'password': 'admin123'
}

def verificar_cobertura():
    """Verifica la cobertura de BFI01 entre alumnos de ciclo 1"""
    try:
        conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        
        print("=" * 80)
        print("VERIFICACIÓN DE COBERTURA BFI01")
        print("=" * 80)
        print()
        
        # Total de alumnos en ciclo 1
        cur.execute("SELECT COUNT(*) as total FROM alumno WHERE ciclo_relativo = 1")
        total_ciclo1 = cur.fetchone()['total']
        
        # Alumnos de ciclo 1 matriculados en BFI01
        cur.execute("""
            SELECT COUNT(DISTINCT m.alumno_id) as total
            FROM matricula m
            JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
            JOIN curso c ON co.curso_id = c.id
            JOIN alumno a ON m.alumno_id = a.id
            WHERE c.codigo = 'BFI01' AND a.ciclo_relativo = 1
        """)
        ciclo1_bfi01 = cur.fetchone()['total']
        
        # Alumnos de ciclo 1 SIN BFI01
        cur.execute("""
            SELECT a.codigo, a.nombres
            FROM alumno a
            WHERE a.ciclo_relativo = 1
            AND a.id NOT IN (
                SELECT DISTINCT m.alumno_id
                FROM matricula m
                JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
                JOIN curso c ON co.curso_id = c.id
                WHERE c.codigo = 'BFI01'
            )
            ORDER BY a.codigo
            LIMIT 10
        """)
        alumnos_sin_bfi01 = cur.fetchall()
        
        print(f"RESULTADOS:")
        print(f"  • Total alumnos ciclo 1: {total_ciclo1}")
        print(f"  • Matriculados en BFI01: {ciclo1_bfi01}")
        print(f"  • NO matriculados en BFI01: {total_ciclo1 - ciclo1_bfi01}")
        print(f"  • Cobertura: {ciclo1_bfi01/total_ciclo1*100:.1f}%")
        print()
        
        if alumnos_sin_bfi01:
            print("ALUMNOS DE CICLO 1 SIN BFI01 (primeros 10):")
            for alumno in alumnos_sin_bfi01:
                print(f"  - {alumno['codigo']}: {alumno['nombres']}")
            print()
        
        # Verificar matrículas totales por semestre
        cur.execute("""
            SELECT co.semestre, COUNT(DISTINCT m.alumno_id) as total_alumnos
            FROM matricula m
            JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
            JOIN curso c ON co.curso_id = c.id
            WHERE c.codigo = 'BFI01'
            GROUP BY co.semestre
            ORDER BY co.semestre
        """)
        por_semestre = cur.fetchall()
        
        print("MATRÍCULAS BFI01 POR SEMESTRE:")
        total_matriculas = 0
        for sem in por_semestre:
            print(f"  {sem['semestre']}: {sem['total_alumnos']} alumnos")
            total_matriculas += sem['total_alumnos']
        print(f"  TOTAL: {total_matriculas} matrículas")
        print()
        
        cur.close()
        conn.close()
        
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    verificar_cobertura()
