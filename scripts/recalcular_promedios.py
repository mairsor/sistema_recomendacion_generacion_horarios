import psycopg2
from psycopg2.extras import RealDictCursor

# Configuración de la base de datos
DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'user': 'admin',
    'password': 'admin123',
    'database': 'schedule_db'
}

print("=" * 80)
print("RECALCULADOR DE PROMEDIOS")
print("=" * 80)
print()

# Conectar a la base de datos
print("🔌 Conectando a la base de datos...")
try:
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    print("✓ Conexión exitosa")
except Exception as e:
    print(f"✗ Error de conexión: {e}")
    exit(1)

print()
print("⚙️  Recalculando promedios de todos los alumnos...")

try:
    # SQL para actualizar promedios
    sql = """
    UPDATE alumno a
    SET promedio = (
        SELECT COALESCE(AVG(m.nota_final), 0)
        FROM matricula m
        WHERE m.alumno_id = a.id
        AND m.nota_final >= 10
        AND m.estado = 'Aprobado'
    )
    """
    cur.execute(sql)
    conn.commit()
    print(f"✓ {cur.rowcount} alumnos actualizados")
    
except Exception as e:
    conn.rollback()
    print(f"✗ Error al recalcular promedios: {e}")
    cur.close()
    conn.close()
    exit(1)

# Verificar resultados
print()
print("🔍 Verificando resultados...")
try:
    cur.execute("""
        SELECT 
            codigo,
            ciclo_relativo,
            creditos_aprobados,
            promedio,
            CASE 
                WHEN LEFT(codigo, 4) = '2017' THEN '2017'
                WHEN LEFT(codigo, 4) = '2019' THEN '2019'
                WHEN LEFT(codigo, 4) = '2022' THEN '2022'
                WHEN LEFT(codigo, 4) = '2025' THEN '2025'
            END as año_ingreso
        FROM alumno
        WHERE codigo IN ('20170001H', '20190001J', '20220001V', '20250001P')
        ORDER BY codigo
    """)
    alumnos = cur.fetchall()
    
    print()
    print("Ejemplos de alumnos:")
    print(f"{'Código':<15} {'Año':<5} {'Ciclo':<6} {'Créditos':<10} {'Promedio':<8}")
    print("-" * 55)
    for alumno in alumnos:
        print(f"{alumno['codigo']:<15} {alumno['año_ingreso']:<5} {alumno['ciclo_relativo']:<6} {alumno['creditos_aprobados']:<10} {float(alumno['promedio']):<8.2f}")
    
    # Estadísticas generales
    print()
    print("📊 Estadísticas generales:")
    cur.execute("""
        SELECT 
            COUNT(*) as total_alumnos,
            AVG(creditos_aprobados) as promedio_creditos,
            AVG(promedio) as promedio_general,
            MAX(ciclo_relativo) as max_ciclo,
            MIN(ciclo_relativo) as min_ciclo
        FROM alumno
    """)
    stats = cur.fetchone()
    print(f"Total alumnos: {stats['total_alumnos']}")
    print(f"Promedio créditos: {float(stats['promedio_creditos']):.2f}")
    print(f"Promedio general: {float(stats['promedio_general']):.2f}")
    print(f"Ciclo mínimo: {stats['min_ciclo']}")
    print(f"Ciclo máximo: {stats['max_ciclo']}")
    
    # Distribución por ciclo
    print()
    print("📊 Distribución por ciclo:")
    cur.execute("""
        SELECT 
            ciclo_relativo,
            COUNT(*) as cantidad
        FROM alumno
        GROUP BY ciclo_relativo
        ORDER BY ciclo_relativo
    """)
    distribucion = cur.fetchall()
    print(f"{'Ciclo':<8} {'Cantidad':<10}")
    print("-" * 20)
    for d in distribucion:
        print(f"{d['ciclo_relativo']:<8} {d['cantidad']:<10}")
    
except Exception as e:
    print(f"✗ Error al verificar: {e}")
finally:
    cur.close()
    conn.close()

print()
print("=" * 80)
print("PROCESO COMPLETADO")
print("=" * 80)
