# Checklist Docker - Sistema de Horarios UNI

## ✅ Archivos de Configuración Docker

### Docker Compose
- [x] `docker-compose.yml` - Orquestación de 4 servicios
- [x] Red interna `horarios_network` configurada
- [x] Variables de entorno configuradas
- [x] Healthchecks para todos los servicios
- [x] Volúmenes persistentes configurados

### Dockerfiles Creados

#### Backend (NestJS)
- [x] `backend/Dockerfile` - Multi-stage build optimizado
- [x] `backend/.dockerignore` - Excluir archivos innecesarios
- [x] Prisma Client generation incluido
- [x] Usuario no-root configurado
- [x] Healthcheck con curl

#### Frontend (Next.js)
- [x] `frontend/Dockerfile` - Multi-stage build optimizado
- [x] `frontend/.dockerignore` - Excluir node_modules
- [x] `frontend/next.config.js` - Configurado para standalone
- [x] Usuario no-root configurado
- [x] Healthcheck con curl

#### Predictor de Demanda API (FastAPI)
- [x] `predictor_demanda_api/Dockerfile` - Ya existía
- [x] Usuario no-root configurado
- [x] Volúmenes para data, models, results
- [x] Healthcheck mejorado con curl

#### Recomendador de Cursos API (FastAPI)
- [x] `recomendador_cursos_api/Dockerfile` - Creado
- [x] `recomendador_cursos_api/.dockerignore` - Creado
- [x] Usuario no-root configurado
- [x] Volúmenes para models, data
- [x] Healthcheck con curl

## ✅ Red Interna Docker

### Configuración de Red
```yaml
networks:
  horarios_network:
    driver: bridge
    name: horarios_network
```

### Comunicación Interna
Todos los servicios pueden comunicarse usando nombres de contenedor:

- `http://backend:4000` - Backend API
- `http://predictor_demanda_api:8000` - Predictor API
- `http://recomendador_cursos_api:8001` - Recomendador API
- `http://frontend:3000` - Frontend (no usado internamente)

### URLs Configuradas en Frontend
```env
NEXT_PUBLIC_BACKEND_URL=http://backend:4000
NEXT_PUBLIC_PREDICTOR_URL=http://predictor_demanda_api:8000
NEXT_PUBLIC_RECOMENDADOR_URL=http://recomendador_cursos_api:8001
```

### URLs Configuradas en Backend
```env
PREDICTOR_API_URL=http://predictor_demanda_api:8000
RECOMENDADOR_API_URL=http://recomendador_cursos_api:8001
```

## ✅ Variables de Entorno

### Archivo .env.example
- [x] Configuración de puertos
- [x] Variables de PostgreSQL
- [x] JWT secrets
- [x] URLs de microservicios
- [x] Configuración CORS

### Crear .env
```bash
cp .env.example .env
# Editar con credenciales reales de PostgreSQL
```

## ✅ Puertos Expuestos

| Servicio | Puerto Host | Puerto Container |
|----------|-------------|------------------|
| Frontend | 3000 | 3000 |
| Backend | 4000 | 4000 |
| Predictor | 8000 | 8000 |
| Recomendador | 8001 | 8001 |

## ⚠️ Acciones Pendientes Antes de docker-compose up

### 1. Configurar .env
```bash
cp .env.example .env
nano .env  # Editar con credenciales reales
```

**Campos críticos a configurar:**
- `DB_HOST` - Dirección del servidor PostgreSQL
- `DB_PORT` - Puerto PostgreSQL (default: 5432)
- `DB_NAME` - Nombre de la base de datos
- `DB_USER` - Usuario de PostgreSQL
- `DB_PASSWORD` - Contraseña de PostgreSQL
- `JWT_SECRET` - Secret seguro para JWT (min 32 caracteres)

### 2. Verificar Backend tiene entrypoint.sh
El Dockerfile del backend referencia `entrypoint.sh`. Verificar que existe o ajustar Dockerfile.

### 3. Verificar requisitos del Frontend
- Asegurar que `package.json` tiene todas las dependencias
- Next.js configurado para `standalone` output

### 4. Base de Datos PostgreSQL
- PostgreSQL debe estar corriendo y accesible
- Las migraciones de Prisma deben ejecutarse:
```bash
cd backend
npx prisma migrate deploy
```

## 🚀 Comandos para Iniciar

### Build y Start
```bash
# Construir e iniciar todos los servicios
docker-compose up -d --build

# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f predictor_demanda_api
docker-compose logs -f recomendador_cursos_api
```

### Verificar Estado
```bash
# Ver estado de contenedores
docker-compose ps

# Ver salud de servicios
docker ps --format "table {{.Names}}\t{{.Status}}"
```

### Probar Servicios
```bash
# Backend
curl http://localhost:4000

# Predictor
curl http://localhost:8000

# Recomendador
curl http://localhost:8001/api/health

# Frontend
curl http://localhost:3000
```

## 🔧 Debugging

### Ver logs en tiempo real
```bash
docker-compose logs -f [servicio]
```

### Ejecutar comando dentro de contenedor
```bash
docker-compose exec backend sh
docker-compose exec predictor_demanda_api sh
```

### Reiniciar servicio específico
```bash
docker-compose restart backend
```

### Reconstruir un servicio
```bash
docker-compose up -d --build --force-recreate backend
```

### Detener todos los servicios
```bash
docker-compose down
```

### Detener y eliminar volúmenes
```bash
docker-compose down -v
```

## 📋 Verificación de Red Interna

### Desde el backend, verificar conectividad:
```bash
docker-compose exec backend sh
curl http://predictor_demanda_api:8000
curl http://recomendador_cursos_api:8001/api/health
exit
```

### Verificar red Docker:
```bash
docker network ls | grep horarios
docker network inspect horarios_network
```

## ✅ Todo Listo Para Docker Compose

**Estado**: ✅ **READY**

Todos los Dockerfiles están creados y el `docker-compose.yml` está configurado correctamente con:
- Red interna `horarios_network`
- Comunicación entre servicios por nombre
- Healthchecks configurados
- Volúmenes persistentes
- Variables de entorno configuradas
- Build multi-stage optimizado
- Usuarios no-root por seguridad

**Siguiente paso**: Configurar `.env` con credenciales reales y ejecutar `docker-compose up -d --build`

---

**Fecha de verificación**: 2025-11-20
