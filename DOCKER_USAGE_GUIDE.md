# Guía de Uso - Docker Compose

## ⚠️ Diferencias Clave: Local vs Docker

### 🔧 Configuración Local (Desarrollo)
```bash
# Backend en: http://localhost:3003
# Frontend en: http://localhost:3001
# Variables en: backend/.env y frontend/.env.local
```

**Frontend se comunica directamente con backend:**
```
NEXT_PUBLIC_BACKEND_URL=http://localhost:3003
```

---

### 🐳 Configuración Docker (Producción)

**IMPORTANTE:** En Docker, hay DOS tipos de URLs:

#### 1. URLs INTERNAS (entre contenedores)
```yaml
# Backend puede llamar a las APIs de Python usando nombres de servicio:
PREDICTOR_API_URL=http://predictor_demanda_api:8000
RECOMENDADOR_API_URL=http://recomendador_cursos_api:8001
```

#### 2. URLs EXTERNAS (navegador → contenedores)
```yaml
# El frontend (Next.js) se ejecuta en el NAVEGADOR del usuario
# Por lo tanto debe usar localhost, NO los nombres de servicio Docker:
NEXT_PUBLIC_BACKEND_URL=http://localhost:3003
NEXT_PUBLIC_PREDICTOR_URL=http://localhost:8000
NEXT_PUBLIC_RECOMENDADOR_URL=http://localhost:8001
```

---

## 🚀 Instrucciones de Uso

### 1. Preparar el archivo .env

Copiar `.env.docker` a `.env`:
```bash
cp .env.docker .env
```

O en Windows PowerShell:
```powershell
Copy-Item .env.docker .env
```

### 2. Construir las imágenes

```bash
docker-compose build
```

### 3. Iniciar los servicios

```bash
docker-compose up -d
```

### 4. Ver logs

```bash
# Todos los servicios
docker-compose logs -f

# Solo backend
docker-compose logs -f backend

# Solo frontend
docker-compose logs -f frontend
```

### 5. Verificar estado

```bash
docker-compose ps
```

### 6. Detener servicios

```bash
docker-compose down
```

### 7. Reconstruir después de cambios en código

```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

---

## 🌐 Acceso a los Servicios

Una vez iniciados los contenedores:

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:3003/api
- **Predictor API:** http://localhost:8000
- **Recomendador API:** http://localhost:8001

---

## 🔑 Usuarios de Prueba

Los mismos que en desarrollo local:

| Email | Password | Rol |
|-------|----------|-----|
| admin@uni.edu.pe | admin123 | ADMIN |
| juan.perez@uni.edu.pe | alumno123 | ALUMNO |
| maria.gonzalez@uni.edu.pe | profesor123 | PROFESOR |

---

## 🐛 Troubleshooting

### El frontend no puede conectarse al backend

**Síntoma:** Error de red en el navegador al intentar login

**Solución:** Verificar que `NEXT_PUBLIC_BACKEND_URL` use `localhost`, NO el nombre del servicio Docker:
```yaml
# ❌ INCORRECTO
NEXT_PUBLIC_BACKEND_URL=http://backend:3003

# ✅ CORRECTO
NEXT_PUBLIC_BACKEND_URL=http://localhost:3003
```

### El backend no puede conectarse a las APIs de Python

**Síntoma:** El backend reporta errores al llamar predictor/recomendador

**Solución:** Verificar que las URLs internas usen nombres de servicio Docker:
```yaml
# ✅ CORRECTO (comunicación interna)
PREDICTOR_API_URL=http://predictor_demanda_api:8000
RECOMENDADOR_API_URL=http://recomendador_cursos_api:8001
```

### La base de datos no se conecta

**Verificar:**
1. La base de datos PostgreSQL está corriendo en `172.232.188.183:5435`
2. Las credenciales son correctas en `.env`
3. El firewall permite conexiones desde los contenedores

### Puerto 3003 ya en uso

```bash
# Detener el backend local si está corriendo
# O cambiar el puerto en docker-compose.yml:
ports:
  - "3004:3003"  # Mapear 3004 (host) → 3003 (container)
```

---

## 📝 Notas Importantes

1. **Seed de Base de Datos:** Los usuarios de prueba deben ser creados manualmente o con el seed script en el backend local antes de usar Docker.

2. **Variables de Entorno:** El archivo `.env` en la raíz es para Docker Compose. Los `.env` en `backend/` y `frontend/` son para desarrollo local.

3. **Red Interna:** Todos los contenedores están en la red `horarios_network`, permitiendo comunicación entre ellos usando nombres de servicio.

4. **CORS:** El backend debe permitir peticiones desde `http://localhost:3000` (origen del frontend en Docker).

5. **JWT Secret:** En producción real, cambiar el `JWT_SECRET` por uno seguro y único.

---

## 🔄 Flujo de Comunicación

```
Navegador del Usuario
    ↓
    | HTTP (localhost:3000)
    ↓
[Frontend Container] ─────────┐
                              |
    ↑                         |
    | Server-Side Rendering   |
    ↓                         |
Navegador hace llamadas a:    |
    ↓                         |
    | HTTP (localhost:3003)   |
    ↓                         |
[Backend Container] ←─────────┘
    ↓
    | HTTP interno (nombre servicio)
    ↓
[Predictor API] + [Recomendador API]
    ↓
    | PostgreSQL (172.232.188.183:5435)
    ↓
[Base de Datos Externa]
```

---

## ✅ Checklist de Migración Local → Docker

- [ ] Copiar `.env.docker` a `.env`
- [ ] Verificar que `NEXT_PUBLIC_BACKEND_URL=http://localhost:3003` en docker-compose.yml
- [ ] Construir imágenes: `docker-compose build`
- [ ] Iniciar servicios: `docker-compose up -d`
- [ ] Verificar logs: `docker-compose logs -f`
- [ ] Probar login en: http://localhost:3000/test
- [ ] Verificar que las APIs internas funcionen (predictor, recomendador)

---

## 📚 Comandos Útiles

```bash
# Ver contenedores corriendo
docker-compose ps

# Reiniciar un servicio específico
docker-compose restart backend

# Ver logs de un servicio
docker-compose logs -f backend

# Ejecutar comando dentro de un contenedor
docker-compose exec backend sh

# Limpiar todo (contenedores, redes, volúmenes)
docker-compose down -v

# Reconstruir sin caché
docker-compose build --no-cache backend
```
