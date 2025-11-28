# 🐳 Resumen de Actualización Docker

## Fecha: 27 de Noviembre, 2025

### 📋 Cambios Realizados

#### 1. **Docker Compose Principal** (`docker-compose.yml`)
- ✅ Configuración de healthchecks mejorada para todos los servicios
- ✅ Dependencias entre servicios con `condition: service_healthy`
- ✅ Variables de entorno consolidadas y documentadas
- ✅ Volúmenes persistentes para datos y modelos ML
- ✅ Red interna Docker (`horarios_network`) para comunicación entre servicios
- ✅ Build args para frontend (variables NEXT_PUBLIC_*)
- ✅ Configuración CORS explícita

#### 2. **Dockerfiles Actualizados**

**Frontend** (`frontend/Dockerfile`)
- ✅ Multi-stage build optimizado
- ✅ Soporte para variables de entorno en build-time
- ✅ Usuario no-root para seguridad
- ✅ Healthcheck con wget

**Backend** (`backend/dockerfile`)
- ✅ Multi-stage build con Prisma
- ✅ Script de entrypoint para migraciones automáticas
- ✅ Usuario no-root
- ✅ Volúmenes para logs y Prisma

**Predictor API** (`predictor_demanda_api/Dockerfile`)
- ✅ Healthcheck actualizado con urllib (sin dependencia de requests)
- ✅ Curl instalado para healthchecks
- ✅ Workers configurables

**Recomendador API** (`recomendador_cursos_api/Dockerfile`)
- ✅ Eliminada dependencia de PyTorch (optimización)
- ✅ Usuario no-root
- ✅ Healthcheck mejorado

#### 3. **Dependencias Actualizadas**

**Predictor API** (`predictor_demanda_api/requirements.txt`)
- ✅ Agregado `requests>=2.31.0` para healthchecks

**Recomendador API** (`recomendador_cursos_api/requirements.txt`)
- ✅ Migrado de Flask a FastAPI
- ✅ Agregado SQLAlchemy y psycopg2-binary
- ✅ Agregado Pydantic para validación
- ✅ Agregado requests para HTTP

#### 4. **Configuración de Entorno**

**`.env.docker`** - Actualizado
```bash
# URLs públicas (para frontend en navegador)
NEXT_PUBLIC_BACKEND_URL=http://localhost:3003
NEXT_PUBLIC_PREDICTOR_URL=http://localhost:8000
NEXT_PUBLIC_RECOMENDADOR_URL=http://localhost:8001

# URLs internas (para comunicación backend)
PREDICTOR_API_URL=http://predictor_demanda_api:8000
RECOMENDADOR_API_URL=http://recomendador_cursos_api:8001
```

#### 5. **Scripts de Utilidad**

**Scripts de Inicio:**
- ✅ `docker-start.sh` (Linux/Mac)
- ✅ `docker-start.ps1` (Windows PowerShell)
  - Build automático de imágenes
  - Inicio ordenado de servicios
  - Verificación de configuración
  - Muestra de logs iniciales

**Scripts de Verificación:**
- ✅ `docker-verify.sh` (Linux/Mac)
- ✅ `docker-verify.ps1` (Windows PowerShell)
  - Verifica estado de contenedores
  - Verifica healthchecks
  - Prueba conectividad externa
  - Prueba comunicación interna entre servicios
  - Muestra uso de recursos

**Entrypoint Backend:**
- ✅ `backend/docker-entrypoint.sh`
  - Espera a que la BD esté disponible
  - Genera Prisma Client
  - Aplica migraciones en desarrollo
  - Inicia la aplicación

#### 6. **Documentación**

**`DOCKER_DEPLOYMENT.md`** - Guía completa
- ✅ Requisitos previos
- ✅ Inicio rápido
- ✅ Comandos útiles
- ✅ Verificación del despliegue
- ✅ Solución de problemas
- ✅ Monitoreo
- ✅ Configuración de producción

**`docker-compose.dev.yml`** - Entorno de desarrollo
- ✅ Hot reload para todos los servicios
- ✅ Volúmenes de código fuente montados
- ✅ Logs en modo debug

#### 7. **Archivos .dockerignore**
- ✅ `frontend/.dockerignore`
- ✅ `backend/.dockerignore`
- ✅ `predictor_demanda_api/.dockerignore`
- ✅ `recomendador_cursos_api/.dockerignore`

### 🎯 Arquitectura de Red

```
┌─────────────────────────────────────────────────────────┐
│                    Docker Network                        │
│                  (horarios_network)                      │
│                                                          │
│  ┌──────────────┐         ┌──────────────┐             │
│  │   Frontend   │◄───────►│   Backend    │             │
│  │  (Next.js)   │         │  (NestJS)    │             │
│  │  Port: 3000  │         │  Port: 3003  │             │
│  └──────────────┘         └──────┬───────┘             │
│         ▲                         │                      │
│         │                         ├──────────────┐      │
│         │                         ▼              ▼      │
│    (navegador)          ┌──────────────┐ ┌──────────┐  │
│         │               │  Predictor   │ │Recomenda │  │
│         │               │   (FastAPI)  │ │   dor    │  │
│         │               │  Port: 8000  │ │Port: 8001│  │
│         │               └──────────────┘ └──────────┘  │
│         │                      ▲              ▲         │
│         └──────────────────────┴──────────────┘         │
│                                                          │
└─────────────────────────────────────────────────────────┘
                          ▲
                          │
                  ┌───────┴────────┐
                  │   PostgreSQL   │
                  │    (Externo)   │
                  └────────────────┘
```

### 🔑 Conceptos Clave

1. **Comunicación Cliente-Servidor:**
   - Frontend (navegador) → APIs: usa `localhost` (NEXT_PUBLIC_*)
   - Backend → APIs internas: usa nombres de servicio Docker

2. **Healthchecks:**
   - Todos los servicios tienen healthchecks configurados
   - Servicios esperan a que dependencias estén `healthy`
   - Start period configurado para dar tiempo de inicialización

3. **Volúmenes Persistentes:**
   - `predictor_data`: Datos de entrenamiento
   - `predictor_models`: Modelos ML entrenados
   - `predictor_results`: Resultados de predicciones
   - `recomendador_models`: Modelos de recomendación
   - `recomendador_data`: Datos de recomendación

4. **Seguridad:**
   - Todos los servicios corren con usuarios no-root
   - Variables de entorno separadas del código
   - JWT_SECRET configurable
   - CORS configurado explícitamente

### 📦 Comandos de Despliegue

#### Producción:
```bash
# Iniciar todo el sistema
./docker-start.sh  # Linux/Mac
.\docker-start.ps1 # Windows

# Verificar sistema
./docker-verify.sh  # Linux/Mac
.\docker-verify.ps1 # Windows

# Ver logs
docker-compose --env-file .env.docker logs -f

# Detener
docker-compose --env-file .env.docker down
```

#### Desarrollo:
```bash
# Iniciar en modo desarrollo
docker-compose -f docker-compose.dev.yml --env-file .env.docker up

# Ver logs de un servicio
docker-compose -f docker-compose.dev.yml logs -f backend

# Reconstruir un servicio
docker-compose -f docker-compose.dev.yml build --no-cache frontend
```

### ✅ Checklist de Despliegue

Antes de desplegar en producción:

- [ ] Actualizar `.env.docker` con credenciales reales
- [ ] Cambiar `JWT_SECRET` por uno seguro
- [ ] Verificar conexión a base de datos PostgreSQL
- [ ] Configurar firewall para puertos 3000, 3003, 8000, 8001
- [ ] Configurar backup de volúmenes Docker
- [ ] Configurar logs externos (opcional)
- [ ] Configurar monitoreo (opcional)
- [ ] Configurar reverse proxy con SSL (recomendado)

### 🐛 Solución Rápida de Problemas

**Servicios no inician:**
```bash
docker-compose --env-file .env.docker logs
```

**Error de base de datos:**
```bash
docker exec horarios_backend npx prisma db pull
```

**Reconstruir todo:**
```bash
docker-compose --env-file .env.docker down -v
docker-compose --env-file .env.docker build --no-cache
docker-compose --env-file .env.docker up -d
```

**Limpiar sistema completo:**
```bash
docker-compose --env-file .env.docker down -v
docker system prune -a
```

### 📞 Soporte

Para más información, consulta:
- `DOCKER_DEPLOYMENT.md` - Guía completa de despliegue
- `DOCKER_USAGE_GUIDE.md` - Guía de uso existente
- `docker-compose.yml` - Comentarios en configuración
- Logs de cada servicio: `docker-compose logs [servicio]`

---
**Sistema listo para desplegar** ✅
