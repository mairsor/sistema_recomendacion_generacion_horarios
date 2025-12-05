import psycopg2
import sys

# Configuración de la base de datos
DB_CONFIG = {
    'host': '172.232.188.183',
    'port': 5435,
    'user': 'admin',
    'password': 'admin123',
    'database': 'schedule_db'
}

print("=" * 80)
print("EJECUTOR DE SQL - MATRÍCULAS")
print("=" * 80)
print()

# Leer el archivo SQL
sql_file = r"d:\Estudios\Universidad Nacional de Ingeniería\8. Octavo Ciclo\Ingeniería de Software (CIB02)\Proyecto\modelo_predictor_demanda\scripts\generar_matriculas.sql"

print(f"📄 Leyendo archivo SQL: {sql_file}")
try:
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    print("✓ Archivo leído correctamente")
except Exception as e:
    print(f"✗ Error al leer archivo: {e}")
    sys.exit(1)

# Conectar a la base de datos
print()
print("🔌 Conectando a la base de datos...")
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    print("✓ Conexión exitosa")
except Exception as e:
    print(f"✗ Error de conexión: {e}")
    sys.exit(1)

# Ejecutar el SQL
print()
print("⚙️  Ejecutando SQL...")
print("   Esto puede tardar varios segundos...")
try:
    cur.execute(sql_content)
    conn.commit()
    print("✓ SQL ejecutado exitosamente")
    print(f"✓ {cur.rowcount} filas afectadas")
except Exception as e:
    conn.rollback()
    print(f"✗ Error al ejecutar SQL: {e}")
    cur.close()
    conn.close()
    sys.exit(1)

# Verificar resultados
print()
print("🔍 Verificando resultados...")
try:
    # Contar matrículas
    cur.execute("SELECT COUNT(*) FROM matricula")
    total_matriculas = cur.fetchone()[0]
    print(f"✓ Total matrículas: {total_matriculas}")
    
    # Verificar ciclo relativo de algunos alumnos
    cur.execute("""
        SELECT codigo, ciclo_relativo, creditos_aprobados, promedio
        FROM alumno
        WHERE codigo IN ('20170001H', '20190001J', '20220001V', '20250001P')
        ORDER BY codigo
    """)
    alumnos = cur.fetchall()
    print()
    print("Ejemplos de alumnos:")
    print(f"{'Código':<15} {'Ciclo':<6} {'Créditos':<10} {'Promedio':<8}")
    print("-" * 45)
    for alumno in alumnos:
        print(f"{alumno[0]:<15} {alumno[1]:<6} {alumno[2]:<10} {alumno[3]:<8.2f}")
    
except Exception as e:
    print(f"✗ Error al verificar: {e}")
finally:
    cur.close()
    conn.close()

print()
print("=" * 80)
print("PROCESO COMPLETADO")
print("=" * 80)
