# Modelo de Predicción de Demanda de Cursos - UNI

Sistema modular para predecir la demanda de matrícula de cursos usando Random Forest Regressor. Incluye modelo general (todos los cursos), modelos específicos por curso, y un sistema iterador para procesamiento masivo.

Este proyecto corresponde al curso CIB02 – Ingeniería de Software (FIEE UNI) y se desarrolla como un prototipo funcional (MVP), con datos simulados y validación de algoritmos.

## 📋 Características

- **Modelo General**: Entrena con datos de todos los cursos para tener una base robusta
- **Modelos Específicos**: Ajuste fino por curso cuando hay suficiente historia
- **Sistema Iterador**: Procesa todos los cursos automáticamente usando la mejor estrategia disponible
- **Configuración YAML**: Hiperparámetros y features configurables por archivo
- **Metadata Completa**: Cada modelo incluye métricas, features y timestamp
- **Modular y Extensible**: Diseñado para reemplazar cálculos Python por vistas SQL en el futuro

## 🏗️ Estructura del Proyecto

```
modelo_predictor_demanda/
├── src/
│   ├── __init__.py
│   ├── utilidades_modelo.py    # Funciones compartidas (carga, preprocessing, métricas)
│   ├── modelo_general.py       # Entrena modelo global
│   ├── modelo_especifico.py    # Entrena modelo por curso
│   └── modelo_todos.py         # Itera y predice para todos los cursos
├── configs/
│   ├── general_model.yml       # Configuración del modelo general
│   └── ejemplo_CIB02.yml       # Configuración para curso específico
├── data/
│   └── matriculas_por_curso.csv # Dataset de ejemplo
├── models/                     # Modelos .pkl y metadata .json (generado)
├── results/                    # Predicciones CSV (generado)
├── modelo_predictor/           # Código legacy (mantener por ahora)
├── pruebas_automatizadas/      # Tests existentes
├── requirements.txt            # Dependencias Python
└── README.md                   # Este archivo
```

## 📊 Formato del Dataset

El archivo CSV debe contener las siguientes columnas:

### Columnas Obligatorias

| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| `curso_ofertado_id` | int | ID único de la sección (PK) | `1` |
| `nombre_seccion` | string | Nombre descriptivo de la sección | `"CIB02-2023-1-A"` |
| `codigo_curso` | string | Código del curso | `"CIB02"` |
| `semestre` | string | Periodo académico | `"2025-2"` |
| `creditos` | int | Créditos del curso | `4` |
| `tipo_curso` | string | Obligatorio (O) o Electivo (E) | `"O"` |
| `profesor_id` | int | ID del profesor (FK) | `1` |
| `alumnos_previos` | int | Matriculados en ciclo anterior | `45` |
| `variacion_matricula` | float | Cambio % respecto ciclo anterior | `0.1` (10%) |
| `num_prerrequisitos` | int | Cantidad de prerrequisitos | `2` |
| `tasa_aprobacion` | float | Tasa de aprobación histórica (0-1) | `0.80` (80%) |
| `franja_horaria` | int | 1=mañana, 2=tarde, 3=noche | `1` |
| `experiencia_anios` | int | Años de experiencia del profesor | `10` |
| `cupo_maximo` | int | Capacidad máxima de la sección | `50` |
| `alumnos_matriculados` | int | **TARGET** - Alumnos realmente matriculados | `48` |

### Columnas Opcionales

| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| `profesor_popularidad` | float | Popularidad del profesor (0-1) | `0.85` |
| `alumnos_elegibles` | int | Alumnos que pueden matricularse | `60` |

**Nota**: Si `alumnos_elegibles` no está presente, se calculará automáticamente usando la fórmula:
```
alumnos_elegibles = max(alumnos_previos * 1.2, cupo_maximo)
```

En el futuro, esto se reemplazará por una vista SQL que cuente estudiantes que aprobaron prerrequisitos.

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
cd modelo_predictor_demanda
```

### 2. Crear entorno virtual
```bash
python -m venv env
```

### 3. Activar entorno virtual

**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 💻 Uso

### 1. Entrenar Modelo General

Entrena un modelo con datos de todos los cursos:

```bash
python -m src.modelo_general --config configs/general_model.yml --data data/matriculas_por_curso.csv
```

**Salida:**
- `models/modelo_demanda_general_vYYYYMMDD.pkl` - Modelo serializado
- `models/modelo_demanda_general_vYYYYMMDD.json` - Metadata (features, métricas, hiperparámetros)
- `models/general_metrics.json` - Métricas consolidadas

### 2. Entrenar Modelo Específico

Entrena un modelo para un curso específico:

```bash
python -m src.modelo_especifico --course CIB02 --config configs/ejemplo_CIB02.yml --data data/matriculas_por_curso.csv
```

**Con flag `--force`** (entrenar aunque no haya historia suficiente):
```bash
python -m src.modelo_especifico --course CIB02 --data data/matriculas_por_curso.csv --force
```

**Salida:**
- `models/modelo_demanda_CIB02_vYYYYMMDD.pkl`
- `models/modelo_demanda_CIB02_vYYYYMMDD.json`

### 3. Procesar Todos los Cursos

Itera por todos los cursos y genera predicciones:

```bash
python -m src.modelo_todos --data data/matriculas_por_curso.csv --general_model models/modelo_demanda_general_v20251113.pkl
```

**Entrenar modelo general automáticamente si no existe:**
```bash
python -m src.modelo_todos --data data/matriculas_por_curso.csv --train_general
```

**No entrenar nuevos modelos específicos (solo usar existentes):**
```bash
python -m src.modelo_todos --data data/matriculas_por_curso.csv --no_train_specific --general_model models/modelo_demanda_general_latest.pkl
```

**Salida:**
- `results/predicciones_YYYYMMDD_HHMMSS.csv` - Predicciones para todos los cursos

Formato del CSV de resultados:
```csv
codigo_curso,n_registros_historia,cupo_maximo_promedio,alumnos_previos_promedio,prediccion_demanda,mae_si_disponible,modelo_usado
CIB02,6,50.0,46.5,49.2,1.8,especifico_nuevo (modelo_demanda_CIB02_v20251113.pkl)
MAT101,6,70.0,67.5,70.1,2.3,especifico_cached (modelo_demanda_MAT101_v20251110.pkl)
QUI301,4,30.0,25.0,26.5,,general
```

## ⚙️ Configuración

Los archivos `.yml` en `configs/` controlan el comportamiento de los modelos:

```yaml
# Features a usar
features:
  - creditos
  - alumnos_previos
  - variacion_matricula
  - num_prerrequisitos
  - tasa_aprobacion
  - franja_horaria
  - experiencia_anios
  - alumnos_elegibles
  - cupo_maximo
  - tipo_curso

# Hiperparámetros de RandomForest
hyperparams:
  n_estimators: 300
  max_depth: 12
  min_samples_split: 5
  min_samples_leaf: 2
  random_state: 42
  n_jobs: -1

# Variable objetivo
target: alumnos_matriculados

# Train/test split
test_size: 0.2

# Mínimo de semestres de historia (solo para modelos específicos)
min_history_semesters: 6

# Directorio de salida
output_dir: models/
```

## 📈 Métricas

Los modelos se evalúan con:

- **MAE** (Mean Absolute Error): Error promedio en número de alumnos
- **RMSE** (Root Mean Squared Error): Error cuadrático medio
- **R²** (Coefficient of Determination): Varianza explicada por el modelo

Ejemplo de salida:
```
MÉTRICAS DEL MODELO GENERAL
======================================================================
MAE:  2.15 alumnos
RMSE: 3.42 alumnos
R²:   0.9248
======================================================================
```

## 🔧 Funciones Principales (utilidades_modelo.py)

### Carga de Datos
- `cargar_datos_csv(path)` - Lee y valida CSV
- `get_data_from_db(conn_params)` - Stub para futuro uso con SQL (NotImplementedError)

### Preprocesamiento
- `calcular_alumnos_elegibles(df)` - Calcula columna si falta (aproximación pandas)
- `preparar_features(df, features)` - Imputación, one-hot encoding, split X/y

### Modelado
- `entrenar_rf_regressor(X, y, params)` - Entrena RandomForest
- `evaluar_regresor(model, X_test, y_test)` - Calcula métricas

### Persistencia
- `guardar_modelo_y_metadata(model, features, metrics, ...)` - Guarda .pkl y .json
- `cargar_modelo(path)` - Carga modelo desde .pkl

## 🧪 Tests

### Pruebas unitarias en utilidades_modelo.py
```bash
python src/utilidades_modelo.py
```

### Pruebas automatizadas existentes
```bash
cd pruebas_automatizadas
pytest test_demanda.py -v
```

## 🔮 Roadmap y TODOs

### Implementaciones Futuras

1. **Vista SQL para `alumnos_elegibles`**
   - Reemplazar `calcular_alumnos_elegibles()` 
   - Usar `get_data_from_db()` que retorne vista SQL con:
   ```sql
   SELECT COUNT(DISTINCT estudiante_id) as alumnos_elegibles
   FROM estudiantes_aprobados_prerrequisitos
   WHERE curso_id = X AND estudiante_id NOT IN (
       SELECT estudiante_id FROM aprobados WHERE curso_id = X
   )
   ```

2. **CLI mejorado con Typer**
   - Descomenta `typer>=0.9` en requirements.txt
   - Interfaces interactivas para configuración

3. **Validación cruzada**
   - Implementar K-Fold CV para modelos específicos
   - Validación temporal (train en semestres anteriores, test en recientes)

4. **Features adicionales**
   - Promedio de calificaciones históricas
   - Tasa de deserción por curso
   - Correlación con cursos simultáneos

5. **Optimización de hiperparámetros**
   - Grid Search o Random Search automático
   - Guardar mejores parámetros en metadata

## 📝 Notas Técnicas

### Compatibilidad de Features

**IMPORTANTE**: Al usar `modelo_todos.py`, las features deben ser consistentes entre el modelo general y los específicos. El sistema aplica one-hot encoding a columnas categóricas, por lo que:

- Si entrenas con `tipo_curso`, todas las predicciones necesitan esa columna
- El orden de las columnas después de one-hot debe coincidir
- Usa los mismos archivos de configuración para consistencia

### Versionado de Modelos

Los archivos incluyen fecha en el nombre:
```
modelo_demanda_CIB02_v20251113.pkl
modelo_demanda_CIB02_v20251113.json
```

Esto permite:
- Comparar rendimiento entre versiones
- Rollback a modelos anteriores
- Auditoría de cambios

### Metadata JSON

Ejemplo de metadata guardada:
```json
{
  "model_name": "modelo_demanda_CIB02_v20251113",
  "curso": "CIB02",
  "date": "2025-11-13T14:30:45.123456",
  "features": ["creditos", "alumnos_previos", "tipo_curso_O", ...],
  "metrics": {
    "MAE": 2.15,
    "RMSE": 3.42,
    "R2": 0.9248
  },
  "n_train": 48,
  "n_test": 12,
  "hyperparams": {
    "n_estimators": 300,
    "max_depth": 12,
    "random_state": 42
  },
  "config_hash": "a3f5b2c8d9e1f4..."
}
```

## 🤝 Contribuciones

Para agregar nuevas funcionalidades:

1. Mantén la modularidad (separa funciones en utilidades_modelo.py)
2. Documenta con docstrings (formato numpy)
3. Añade pruebas unitarias
4. Actualiza este README
5. Registra cambios en metadata JSON

## 📄 Licencia

Proyecto académico - Universidad Nacional de Ingeniería (UNI)
Curso: Ingeniería de Software (CIB02)

---

**Última actualización**: 2025-11-13
**Versión**: 1.0.0
