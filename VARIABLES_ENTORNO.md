# Variables de Entorno - Sistema de Recomendación y Predicción de Demanda

## 📋 Resumen de Auditoría

**Fecha:** 27 de noviembre de 2025  
**Estado:** ✅ Todas las URLs críticas ahora usan variables de entorno

---

## 🔧 Cambios Realizados

### ✅ Corregidas (ahora usan variables de entorno):

1. **`frontend/services/predictorService.ts`**
   - ❌ Antes: `const PREDICTOR_API_URL = 'http://localhost:8000';`
   - ✅ Ahora: `const PREDICTOR_API_URL = process.env.NEXT_PUBLIC_PREDICTOR_URL || 'http://localhost:8000';`

2. **`frontend/app/admin/demand-results/page.tsx`**
   - ❌ Antes: `` const url = `http://localhost:8000/api/v1/results/${filename}/download`; ``
   - ✅ Ahora: Usa `process.env.NEXT_PUBLIC_PREDICTOR_URL`

3. **`frontend/app/test/page.tsx`**
   - ❌ Antes: `<p>URL: http://172.232.188.183:3003</p>`
   - ✅ Ahora: `<p>URL: {process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:3003'}</p>`

---

## 📁 Archivos `.env` Necesarios

### Para compartir con el equipo (4 archivos):

```
modelo_predictor_demanda/
├── .env                    # Desarrollo local
├── .env.docker             # Docker Compose
├── backend/.env            # Backend NestJS
└── frontend/.env.local     # Frontend Next.js
```

---

## 🔍 URLs que SÍ están bien configuradas

### Frontend (`frontend/services/`)

✅ **api.ts**
```typescript
const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:3003';
const PREDICTOR_URL = process.env.NEXT_PUBLIC_PREDICTOR_URL || 'http://localhost:8000';
const RECOMENDADOR_URL = process.env.NEXT_PUBLIC_RECOMENDADOR_URL || 'http://localhost:8001';
```

✅ **recommenderService.ts**
```typescript
const RECOMMENDER_API_URL = process.env.NEXT_PUBLIC_RECOMENDADOR_URL || 'http://localhost:8001';
```

✅ **predictorService.ts** (✅ Corregido)
```typescript
const PREDICTOR_API_URL = process.env.NEXT_PUBLIC_PREDICTOR_URL || 'http://localhost:8000';
```

### Backend Python (`predictor_demanda_api/`)

✅ **modelo_predictor/src/conexion_db.py**
```python
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'schedule_db')
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
```

---

## 📝 URLs que NO requieren cambios (son correctas)

### Docker Compose
- ✅ Usa variables de entorno: `${BACKEND_PORT:-3003}`, `${PREDICTOR_PORT:-8000}`, etc.
- ✅ Health checks usan `localhost` internamente (correcto dentro del contenedor)

### Archivos de Configuración
- ✅ `docker-compose.yml` - Todas las URLs usan variables
- ✅ `next.config.js` - `domains: ['localhost']` es necesario para Next.js Image optimization

### Scripts de Testing (no críticos)
- ⚠️ `recomendador_cursos_api/test_api.py` - Tiene `localhost:5000` pero es solo para pruebas locales
- ⚠️ `predictor_demanda_api/main.py` - Log message con URL (solo informativo)

---

## 🎯 Variables de Entorno Requeridas

### Frontend (`.env.local`)
```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:3003
NEXT_PUBLIC_PREDICTOR_URL=http://localhost:8000
NEXT_PUBLIC_RECOMENDADOR_URL=http://localhost:5000
```

### Backend (`backend/.env`)
```env
DATABASE_URL=postgresql://admin:admin123@172.232.188.183:5435/schedule_db
PORT=3003
JWT_SECRET=A7f7b2a9H42J4d45bQbar8d81a714bV6m786124pg2e4d8m88f0222f3b6c77za3
JWT_EXPIRES_IN=8h
PREDICTOR_API_URL=http://localhost:8000
RECOMENDADOR_API_URL=http://localhost:8001
```

### Docker Compose (`.env.docker`)
```env
FRONTEND_PORT=3000
BACKEND_PORT=3003
PREDICTOR_PORT=8000
RECOMENDADOR_PORT=8001
DB_HOST=172.232.188.183
DB_PORT=5435
DB_NAME=schedule_db
DB_USER=admin
DB_PASSWORD=admin123
JWT_SECRET=A7f7b2a9H42J4d45bQbar8d81a714bV6m786124pg2e4d8m88f0222f3b6c77za3
JWT_EXPIRATION=8h
```

### Raíz del Proyecto (`.env`)
```env
NODE_ENV=development
FRONTEND_PORT=3000
BACKEND_PORT=4000
PREDICTOR_PORT=8000
RECOMENDADOR_PORT=8001
DB_HOST=172.232.188.183
DB_PORT=5435
DB_NAME=matricula_inteligente
DB_USER=admin
DB_PASSWORD=admin123
DATABASE_URL=postgresql://admin:admin123@172.232.188.183:5435/matricula_inteligente
```

---

## ✅ Verificación Final

**Estado de URLs en el código:**

| Archivo | URL | Estado |
|---------|-----|--------|
| `frontend/services/api.ts` | 3 URLs | ✅ Variables de entorno |
| `frontend/services/recommenderService.ts` | 1 URL | ✅ Variable de entorno |
| `frontend/services/predictorService.ts` | 1 URL | ✅ Corregido |
| `frontend/app/admin/demand-results/page.tsx` | 1 URL | ✅ Corregido |
| `frontend/app/test/page.tsx` | 1 URL | ✅ Corregido |
| `predictor_demanda_api/modelo_predictor/src/conexion_db.py` | DB config | ✅ Variables de entorno |
| `docker-compose.yml` | Todas | ✅ Variables de entorno |

---

## 📦 Archivos que NO se deben compartir

❌ **NO compartir:**
- `env/` - Entorno virtual de Python (se regenera con `pip install`)
- `node_modules/` - Dependencias de Node.js (se instalan con `npm install`)
- `.next/` - Build de Next.js
- `dist/` - Build del backend
- `__pycache__/` - Cache de Python

---

## 🚀 Instrucciones para el Equipo

1. **Clonar el repositorio**
2. **Copiar los 4 archivos `.env`** en sus ubicaciones correctas
3. **Instalar dependencias:**
   - Frontend: `cd frontend && npm install`
   - Backend: `cd backend && npm install`
   - Predictor: `cd predictor_demanda_api && python -m venv env && .\env\Scripts\activate && pip install -r requirements.txt`
   - Recomendador: `cd recomendador_cursos_api && pip install -r requirements.txt`
4. **Ejecutar servicios:**
   - Frontend: `npm run dev` (puerto 3000)
   - Backend: `npm run start:dev` (puerto 3003)
   - Predictor: `python main.py` (puerto 8000)
   - Recomendador: `python apy.py` (puerto 5000/8001)

---

## 📞 Contacto

Si encuentran algún problema con las variables de entorno, verificar:
1. Que los 4 archivos `.env` estén en las ubicaciones correctas
2. Que las URLs en los `.env` coincidan con los puertos en uso
3. Que el frontend esté usando variables `NEXT_PUBLIC_*` (no secretas)
