import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host='172.232.188.183',
    port=5435,
    user='admin',
    password='admin123',
    database='schedule_db',
    cursor_factory=RealDictCursor
)
cur = conn.cursor()

print("=" * 80)
print("VERIFICACIÓN DE DATOS - DIAGNÓSTICO")
print("=" * 80)
print()

# Verificar distribución por año
cur.execute("""
    SELECT 
        LEFT(codigo, 4) as año_ingreso,
        MIN(ciclo_relativo) as ciclo_min,
        MAX(ciclo_relativo) as ciclo_max,
        AVG(ciclo_relativo) as ciclo_prom,
        MIN(creditos_aprobados) as cred_min,
        MAX(creditos_aprobados) as cred_max,
        AVG(creditos_aprobados) as cred_prom,
        COUNT(*) as total
    FROM alumno
    GROUP BY LEFT(codigo, 4)
    ORDER BY año_ingreso
""")

print("📊 Distribución por año de ingreso:")
print()
print(f"{'Año':<6} {'Total':<7} {'Ciclo':<20} {'Créditos':<30}")
print(f"{'':6} {'':7} {'Min-Max-Prom':<20} {'Min-Max-Prom':<30}")
print("-" * 70)
for r in cur.fetchall():
    ciclo_str = f"{r['ciclo_min']}-{r['ciclo_max']}-{r['ciclo_prom']:.1f}"
    cred_str = f"{r['cred_min']}-{r['cred_max']}-{r['cred_prom']:.1f}"
    print(f"{r['año_ingreso']:<6} {r['total']:<7} {ciclo_str:<20} {cred_str:<30}")

# Ver casos problemáticos de 2019
print("\n" + "=" * 80)
print("⚠️  ESTUDIANTES DE 2019 CON CICLO BAJO (deberían estar en ciclo 3-5):")
print("=" * 80)
cur.execute("""
    SELECT codigo, ciclo_relativo, creditos_aprobados, 
           (SELECT COUNT(*) FROM matricula WHERE alumno_id = alumno.id) as num_matriculas,
           (SELECT COUNT(*) FROM matricula WHERE alumno_id = alumno.id AND nota_final >= 10) as matriculas_aprobadas
    FROM alumno
    WHERE LEFT(codigo, 4) = '2019' AND ciclo_relativo <= 2
    ORDER BY codigo
    LIMIT 10
""")

print(f"{'Código':<15} {'Ciclo':<7} {'Créditos':<10} {'Matrículas':<12} {'Aprobadas':<10}")
print("-" * 65)
for r in cur.fetchall():
    print(f"{r['codigo']:<15} {r['ciclo_relativo']:<7} {r['creditos_aprobados']:<10} {r['num_matriculas']:<12} {r['matriculas_aprobadas']:<10}")

# Ver casos problemáticos de 2025
print("\n" + "=" * 80)
print("⚠️  ESTUDIANTES DE 2025 CON MUCHOS CRÉDITOS (deberían estar en ciclo 1):")
print("=" * 80)
cur.execute("""
    SELECT codigo, ciclo_relativo, creditos_aprobados, 
           (SELECT COUNT(*) FROM matricula WHERE alumno_id = alumno.id) as num_matriculas,
           (SELECT COUNT(*) FROM matricula WHERE alumno_id = alumno.id AND nota_final >= 10) as matriculas_aprobadas
    FROM alumno
    WHERE LEFT(codigo, 4) = '2025' AND creditos_aprobados > 50
    ORDER BY creditos_aprobados DESC
    LIMIT 10
""")

print(f"{'Código':<15} {'Ciclo':<7} {'Créditos':<10} {'Matrículas':<12} {'Aprobadas':<10}")
print("-" * 65)
for r in cur.fetchall():
    print(f"{r['codigo']:<15} {r['ciclo_relativo']:<7} {r['creditos_aprobados']:<10} {r['num_matriculas']:<12} {r['matriculas_aprobadas']:<10}")

# Ver ejemplo detallado de un alumno problemático
print("\n" + "=" * 80)
print("🔍 EJEMPLO DETALLADO - Alumno 20250001P:")
print("=" * 80)
cur.execute("""
    SELECT 
        a.codigo,
        a.ciclo_relativo,
        a.creditos_aprobados,
        a.promedio
    FROM alumno a
    WHERE codigo = '20250001P'
""")
alumno = cur.fetchone()
if alumno:
    print(f"Código: {alumno['codigo']}")
    print(f"Ciclo relativo: {alumno['ciclo_relativo']}")
    print(f"Créditos aprobados: {alumno['creditos_aprobados']}")
    print(f"Promedio: {alumno['promedio']}")
    
    print("\nMatrículas del alumno:")
    cur.execute("""
        SELECT 
            m.id,
            co.semestre,
            c.codigo as curso_codigo,
            c.nombre as curso_nombre,
            c.creditos,
            m.nota_final,
            m.estado
        FROM matricula m
        JOIN curso_ofertado co ON m.curso_ofertado_id = co.id
        JOIN curso c ON co.curso_id = c.id
        WHERE m.alumno_id = (SELECT id FROM alumno WHERE codigo = '20250001P')
        ORDER BY co.semestre, c.codigo
    """)
    
    print(f"{'Semestre':<10} {'Código':<10} {'Curso':<30} {'Créd':<5} {'Nota':<6} {'Estado':<12}")
    print("-" * 80)
    for m in cur.fetchall():
        nota = f"{m['nota_final']:.2f}" if m['nota_final'] else "N/A"
        print(f"{m['semestre']:<10} {m['curso_codigo']:<10} {m['curso_nombre']:<30} {m['creditos']:<5} {nota:<6} {m['estado']:<12}")

cur.close()
conn.close()

print("\n" + "=" * 80)
print("DIAGNÓSTICO COMPLETADO")
print("=" * 80)
