# Guía de Despliegue con Docker

Sistema de Recomendación y Generación de Horarios - UNI

## 📋 Requisitos Previos

- Docker Engine 20.10+ instalado
- Docker Compose 2.0+ instalado
- Al menos 4GB de RAM disponible
- 10GB de espacio en disco
- Acceso a la base de datos PostgreSQL externa

## 🚀 Inicio Rápido

### 1. Configurar Variables de Entorno

Copia el archivo de ejemplo y edita las variables:

```bash
cp .env.example .env.docker
```

Edita `.env.docker` con tus configuraciones:

```bash
# Base de datos (IMPORTANTE: actualizar con tus credenciales)
DB_HOST=tu_servidor_postgresql.com
DB_PORT=5432
DB_NAME=schedule_db
DB_USER=admin
DB_PASSWORD=tu_password_seguro

# JWT Secret (IMPORTANTE: cambiar en producción)
JWT_SECRET=tu_secreto_super_seguro_minimo_32_caracteres

# Puertos (opcional, usar defaults)
FRONTEND_PORT=3000
BACKEND_PORT=3003
PREDICTOR_PORT=8000
RECOMENDADOR_PORT=8001
```

### 2. Iniciar el Sistema

#### En Linux/Mac:
```bash
chmod +x docker-start.sh
./docker-start.sh
```

#### En Windows (PowerShell):
```powershell
.\docker-start.ps1
```

#### Manualmente:
```bash
# Construir imágenes
docker-compose --env-file .env.docker build

# Iniciar servicios
docker-compose --env-file .env.docker up -d

# Ver logs
docker-compose --env-file .env.docker logs -f
```

## 📦 Servicios Disponibles

| Servicio | Puerto | URL | Descripción |
|----------|--------|-----|-------------|
| Frontend | 3000 | http://localhost:3000 | Interfaz web (Next.js) |
| Backend | 3003 | http://localhost:3003/api | API principal (NestJS) |
| Predictor | 8000 | http://localhost:8000/docs | API de predicción (FastAPI) |
| Recomendador | 8001 | http://localhost:8001/api/health | API de recomendación (FastAPI) |

## 🔧 Comandos Útiles

### Ver estado de los servicios
```bash
docker-compose --env-file .env.docker ps
```

### Ver logs en tiempo real
```bash
# Todos los servicios
docker-compose --env-file .env.docker logs -f

# Un servicio específico
docker-compose --env-file .env.docker logs -f frontend
docker-compose --env-file .env.docker logs -f backend
docker-compose --env-file .env.docker logs -f predictor_demanda_api
docker-compose --env-file .env.docker logs -f recomendador_cursos_api
```

### Reiniciar servicios
```bash
# Todos los servicios
docker-compose --env-file .env.docker restart

# Un servicio específico
docker-compose --env-file .env.docker restart backend
```

### Detener servicios
```bash
# Detener sin eliminar contenedores
docker-compose --env-file .env.docker stop

# Detener y eliminar contenedores
docker-compose --env-file .env.docker down

# Detener y eliminar contenedores + volúmenes
docker-compose --env-file .env.docker down -v
```

### Reconstruir un servicio
```bash
# Reconstruir todo
docker-compose --env-file .env.docker build --no-cache

# Reconstruir un servicio específico
docker-compose --env-file .env.docker build --no-cache frontend
```

### Acceder a un contenedor
```bash
docker exec -it horarios_frontend sh
docker exec -it horarios_backend sh
docker exec -it predictor_demanda_api bash
docker exec -it recomendador_cursos_api bash
```

## 🔍 Verificación del Despliegue

### 1. Healthchecks
```bash
# Ver estado de salud de todos los servicios
docker-compose --env-file .env.docker ps

# Verificar endpoints manualmente
curl http://localhost:3000                      # Frontend
curl http://localhost:3003/api                  # Backend
curl http://localhost:8000/health               # Predictor
curl http://localhost:8001/api/health           # Recomendador
```

### 2. Verificar conectividad de red interna
```bash
# Desde el backend, verificar acceso a predictor
docker exec horarios_backend curl http://predictor_demanda_api:8000/health

# Desde el backend, verificar acceso a recomendador
docker exec horarios_backend curl http://recomendador_cursos_api:8001/api/health
```

## 🐛 Solución de Problemas

### Problema: Servicios no inician
```bash
# Ver logs detallados
docker-compose --env-file .env.docker logs

# Verificar que los puertos no estén ocupados
netstat -tulpn | grep -E '3000|3003|8000|8001'  # Linux
netstat -an | findstr -E '3000|3003|8000|8001'  # Windows
```

### Problema: Error de conexión a base de datos
```bash
# Verificar variables de entorno
docker-compose --env-file .env.docker config

# Probar conexión desde un contenedor
docker exec horarios_backend node -e "console.log(process.env.DATABASE_URL)"
```

### Problema: Frontend no puede conectarse a Backend
- Verificar que `NEXT_PUBLIC_BACKEND_URL` use `localhost` (no el nombre del contenedor)
- El frontend se ejecuta en el navegador del usuario, no dentro de Docker

### Problema: Imágenes obsoletas
```bash
# Limpiar todo y reconstruir
docker-compose --env-file .env.docker down -v
docker system prune -a
docker-compose --env-file .env.docker build --no-cache
docker-compose --env-file .env.docker up -d
```

## 📊 Monitoreo

### Ver uso de recursos
```bash
docker stats
```

### Ver volúmenes
```bash
docker volume ls
docker volume inspect predictor_models
```

### Ver red
```bash
docker network ls
docker network inspect horarios_network
```

## 🔐 Seguridad

1. **NUNCA** commitear el archivo `.env.docker` con credenciales reales
2. Cambiar `JWT_SECRET` en producción
3. Usar contraseñas fuertes para la base de datos
4. Configurar CORS apropiadamente en producción
5. Usar HTTPS en producción (configurar reverse proxy como Nginx)

## 📝 Configuración de Producción

Para producción, considera:

1. **Reverse Proxy (Nginx/Traefik)**
   - SSL/TLS certificates
   - Load balancing
   - Rate limiting

2. **Logging y Monitoring**
   - Agregador de logs (ELK Stack, Loki)
   - Métricas (Prometheus + Grafana)
   - Alertas

3. **Backups**
   - Base de datos
   - Volúmenes de Docker
   - Configuraciones

4. **CI/CD**
   - GitHub Actions
   - GitLab CI
   - Jenkins

## 🆘 Soporte

Para problemas o preguntas:
- Revisar logs: `docker-compose --env-file .env.docker logs -f`
- Verificar configuración: `docker-compose --env-file .env.docker config`
- Consultar documentación de cada servicio en sus respectivas carpetas
