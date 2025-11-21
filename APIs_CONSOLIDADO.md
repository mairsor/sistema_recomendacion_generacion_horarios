# Documentación Consolidada de APIs - Sistema de Horarios UNI

Documentación completa de las tres APIs que componen el sistema de recomendación y generación de horarios.

## 🏗️ Arquitectura de APIs

El sistema está compuesto por tres microservicios independientes que se comunican a través de una red Docker:

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend                              │
│                    (React/Next.js)                           │
│                   http://localhost:3000                      │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────┐
│                     Backend API                             │
│                   (NestJS/Node.js)                          │
│                  http://localhost:4000                      │
│  • Autenticación JWT                                        │
│  • CRUD Alumnos, Profesores, Cursos                        │
│  • Gestión de Matrículas                                    │
└─────┬──────────────────────────────────────┬───────────────┘
      │                                      │
      ▼                                      ▼
┌─────────────────────────┐      ┌─────────────────────────┐
│  Predictor Demanda API  │      │ Recomendador Cursos API │
│     (FastAPI/Python)    │      │    (FastAPI/Python)     │
│  http://localhost:8000  │      │  http://localhost:8001  │
│  • Predicción ML        │      │  • Filtrado Colaborativo│
│  • RandomForest         │      │  • Filtrado por Contenido│
│  • Gestión Modelos      │      │  • Recomendaciones      │
└─────────────────────────┘      └─────────────────────────┘
```

---

## 📚 APIs Disponibles

### 1. Backend API (NestJS) - Puerto 4000

**Descripción**: API principal del sistema que gestiona autenticación, usuarios, cursos, matrículas y coordinación general.

**Tecnologías**: NestJS, TypeScript, Prisma ORM, PostgreSQL, JWT

**Base URL**: `http://localhost:4000`

**Documentación completa**: [backend/API_DOCUMENTATION.md](./backend/API_DOCUMENTATION.md)

#### 🔑 Endpoints principales:

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/auth/login` | Iniciar sesión | ❌ |
| POST | `/auth/logout` | Cerrar sesión | ✅ |
| GET | `/alumno` | Listar alumnos | ✅ |
| POST | `/alumno` | Crear alumno | ✅ |
| POST | `/alumno/upload` | Carga masiva CSV | ✅ |
| GET | `/profesor` | Listar profesores | ✅ |
| GET | `/curso` | Listar cursos | ✅ |
| GET | `/ofertado` | Cursos ofertados | ✅ |
| POST | `/matricula` | Crear matrícula | ✅ |
| GET | `/demanda` | Obtener demanda | ❌ |

**Ejemplo de uso:**
```bash
# Login
curl -X POST http://localhost:4000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "alumno@uni.edu.pe", "password": "pass123"}'

# Listar cursos (con token)
curl http://localhost:4000/curso \
  -H "Authorization: Bearer <token>"
```

---

### 2. Predictor de Demanda API (FastAPI) - Puerto 8000

**Descripción**: API de Machine Learning para predicción de demanda de matrícula usando Random Forest.

**Tecnologías**: FastAPI, Python, scikit-learn, pandas, pydantic

**Base URL**: `http://localhost:8000`

**Documentación completa**: [predictor_demanda_api/README.md](./predictor_demanda_api/README.md)

**Swagger UI**: http://localhost:8000/docs

**ReDoc**: http://localhost:8000/redoc

#### 🤖 Endpoints principales:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/v1/predictions` | Crear predicción |
| GET | `/api/v1/predictions/{id}` | Obtener predicción por ID |
| GET | `/api/v1/predictions` | Listar todas las predicciones |
| GET | `/api/v1/predictions/curso/{codigo}` | Predicciones por curso |
| GET | `/api/v1/results` | Listar archivos de resultados |
| GET | `/api/v1/results/{filename}` | Descargar resultado CSV |
| DELETE | `/api/v1/results/{filename}` | Eliminar resultado |
| GET | `/api/v1/models` | Listar modelos entrenados |
| GET | `/api/v1/models/{filename}` | Info de modelo específico |
| DELETE | `/api/v1/models/{filename}` | Eliminar modelo |

**Ejemplo de uso:**
```bash
# Crear predicción para un curso
curl -X POST http://localhost:8000/api/v1/predictions \
  -H "Content-Type: application/json" \
  -d '{
    "codigo_curso": "CIB02",
    "semestre": "2025-2",
    "modo": "auto"
  }'

# Listar modelos disponibles
curl http://localhost:8000/api/v1/models
```

**Respuesta de predicción:**
```json
{
  "prediction_id": "pred_20251120_103045",
  "codigo_curso": "CIB02",
  "semestre": "2025-2",
  "demanda_predicha": 45,
  "modelo_usado": "modelo_especifico_CIB02.pkl",
  "confianza": 0.89,
  "features_usados": [
    "alumnos_previos",
    "variacion_matricula",
    "creditos",
    "tipo_curso_O"
  ],
  "timestamp": "2025-11-20T10:30:45.123Z"
}
```

---

### 3. Recomendador de Cursos API (FastAPI) - Puerto 8001

**Descripción**: Sistema híbrido de recomendación que combina filtrado colaborativo y filtrado basado en contenido.

**Tecnologías**: FastAPI, Python, pandas, scikit-learn, Knowledge Graph

**Base URL**: `http://localhost:8001`

**Documentación completa**: [recomendador_cursos_api/API_DOCUMENTATION.md](./recomendador_cursos_api/API_DOCUMENTATION.md)

**Swagger UI**: http://localhost:8001/docs

#### 🎯 Endpoints principales:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/students` | Listar estudiantes |
| GET | `/api/students/{id}` | Info de estudiante |
| GET | `/api/courses` | Listar cursos |
| GET | `/api/courses/{id}` | Info de curso |
| POST | `/api/recommendations` | Generar recomendaciones |
| GET | `/api/recommendations/{student_id}` | Recomendaciones de estudiante |
| POST | `/api/train` | Entrenar modelos |
| GET | `/api/health` | Estado del sistema |

**Ejemplo de uso:**
```bash
# Obtener recomendaciones para un estudiante
curl -X POST http://localhost:8001/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "ALUMNO_001",
    "top_n": 5,
    "method": "hybrid"
  }'
```

**Respuesta de recomendación:**
```json
{
  "student_id": "ALUMNO_001",
  "recommendations": [
    {
      "course_id": "CIB02",
      "course_name": "Ingeniería de Software",
      "score": 0.92,
      "reason": "Alta compatibilidad con tu historial académico",
      "prerequisites_met": true
    },
    {
      "course_id": "CIP01",
      "course_name": "Programación Avanzada",
      "score": 0.87,
      "reason": "Estudiantes similares tomaron este curso",
      "prerequisites_met": true
    }
  ],
  "method_used": "hybrid",
  "timestamp": "2025-11-20T10:35:00.000Z"
}
```

---

## 🔄 Flujo de Integración

### Escenario 1: Matrícula con Predicción

```mermaid
sequenceDiagram
    Frontend->>Backend: POST /auth/login
    Backend-->>Frontend: JWT Token
    Frontend->>Backend: GET /curso (lista cursos)
    Backend->>Predictor: POST /api/v1/predictions
    Predictor-->>Backend: Demanda predicha
    Backend-->>Frontend: Cursos + Demanda
    Frontend->>Backend: POST /matricula
    Backend-->>Frontend: Matrícula confirmada
```

### Escenario 2: Recomendación de Cursos

```mermaid
sequenceDiagram
    Frontend->>Backend: GET /alumno/:id
    Backend-->>Frontend: Info estudiante
    Frontend->>Recomendador: POST /api/recommendations
    Recomendador-->>Frontend: Cursos recomendados
    Frontend->>Backend: GET /curso/:id (detalles)
    Backend-->>Frontend: Info completa del curso
```

---

## 🔐 Autenticación entre Servicios

### Backend API (NestJS)
Requiere JWT Bearer Token para endpoints protegidos:
```bash
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### APIs de ML (FastAPI)
No requieren autenticación actualmente (internas al sistema Docker).

---

## 🌐 Variables de Entorno

Configuración necesaria en `.env`:

```env
# Base de datos compartida
DB_HOST=tu-servidor-postgres.com
DB_PORT=5432
DB_NAME=horarios_uni_db
DB_USER=postgres
DB_PASSWORD=tu_password_seguro

# Backend (NestJS)
BACKEND_PORT=4000
JWT_SECRET=tu_jwt_secret_super_seguro
JWT_EXPIRES_IN=24h

# Predictor de Demanda (FastAPI)
PREDICTOR_PORT=8000
PREDICTOR_DATA_PATH=/app/data
PREDICTOR_MODELS_PATH=/app/models

# Recomendador (FastAPI)
RECOMENDADOR_PORT=8001
RECOMENDADOR_DATA_PATH=/app/data
RECOMENDADOR_MODELS_PATH=/app/models

# Red Docker
DOCKER_NETWORK=horarios_network
```

---

## 🚀 Inicio Rápido

### Levantar todos los servicios:
```bash
docker-compose up -d --build
```

### Ver logs:
```bash
# Todos los servicios
docker-compose logs -f

# Servicio específico
docker-compose logs -f backend
docker-compose logs -f predictor_demanda_api
docker-compose logs -f recomendador_cursos_api
```

### Verificar salud:
```bash
# Backend
curl http://localhost:4000

# Predictor
curl http://localhost:8000

# Recomendador
curl http://localhost:8001/api/health
```

---

## 📊 Comparación de APIs

| Característica | Backend | Predictor | Recomendador |
|----------------|---------|-----------|--------------|
| **Framework** | NestJS | FastAPI | FastAPI |
| **Lenguaje** | TypeScript | Python | Python |
| **Puerto** | 4000 | 8000 | 8001 |
| **Base de datos** | PostgreSQL | CSV/Archivos | CSV/Archivos |
| **Autenticación** | JWT ✅ | No ❌ | No ❌ |
| **Swagger UI** | No | Sí ✅ | Sí ✅ |
| **ML/IA** | No | Sí (RandomForest) | Sí (Híbrido) |
| **Docs** | API_DOCUMENTATION.md | README.md | API_DOCUMENTATION.md |

---

## 🛠️ Herramientas de Testing

### Postman Collection
Importa las colecciones para probar todos los endpoints:
- `postman/backend.postman_collection.json`
- `postman/predictor.postman_collection.json`
- `postman/recomendador.postman_collection.json`

### cURL Examples
Ver archivos individuales de documentación para ejemplos completos de cURL.

---

## 📝 Códigos de Respuesta HTTP Comunes

| Código | Significado | APIs afectadas |
|--------|-------------|----------------|
| 200 | OK | Todas |
| 201 | Created | Backend, Predictor, Recomendador |
| 400 | Bad Request | Todas |
| 401 | Unauthorized | Backend |
| 403 | Forbidden | Backend |
| 404 | Not Found | Todas |
| 422 | Validation Error | FastAPI (Predictor, Recomendador) |
| 500 | Internal Server Error | Todas |

---

## 🐛 Troubleshooting

### Problema: "Connection refused" al llamar API
**Solución**: Verifica que Docker Compose esté corriendo:
```bash
docker-compose ps
```

### Problema: "Unauthorized" en Backend
**Solución**: Verifica que el token JWT sea válido y esté en el header:
```bash
Authorization: Bearer <token>
```

### Problema: Predictor no encuentra modelo
**Solución**: Entrena un modelo primero usando los scripts:
```bash
cd predictor_demanda_api
bash scripts/ejecutar_modo_general.sh
```

---

## 📚 Enlaces a Documentación Detallada

1. **[Backend API (NestJS)](./backend/API_DOCUMENTATION.md)** - Documentación completa con todos los endpoints
2. **[Predictor de Demanda API](./predictor_demanda_api/README.md)** - Guía completa de ML y predicciones
3. **[Recomendador de Cursos API](./recomendador_cursos_api/API_DOCUMENTATION.md)** - Sistema híbrido de recomendación

---

## 💡 Mejores Prácticas

1. **Siempre valida los tokens JWT** antes de hacer requests al Backend
2. **Usa los Swagger UIs** de FastAPI para explorar endpoints interactivamente
3. **Monitorea los logs** de Docker para debugging
4. **Entrena los modelos de ML** antes de hacer predicciones
5. **Usa paginación** en endpoints con muchos resultados
6. **Maneja errores** apropiadamente en el frontend

---

## 🔮 Roadmap de APIs

- [ ] Agregar autenticación JWT a APIs de ML
- [ ] Implementar rate limiting
- [ ] Agregar métricas y logging centralizado
- [ ] Crear webhooks para notificaciones
- [ ] Implementar GraphQL como alternativa
- [ ] Agregar cache con Redis
- [ ] Implementar versionado de API (v2)

---

## 👥 Soporte

Para preguntas o problemas:
- **Email**: soporte@sistema-horarios-uni.edu.pe
- **Issues**: GitHub Issues de cada repositorio
- **Docs**: Revisa la documentación específica de cada API

---

**Última actualización**: Noviembre 20, 2025
