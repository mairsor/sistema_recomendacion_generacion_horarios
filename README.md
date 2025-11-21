# Sistema de Recomendación y Generación de Horarios - UNI

Sistema completo de gestión académica que integra predicción de demanda de matrícula, recomendación de cursos y generación automática de horarios para la Universidad Nacional de Ingeniería.

## 🏗️ Arquitectura del Sistema

```
sistema_horarios_uni/
├── frontend/                    # Interfaz de usuario (React/Next.js)
├── backend/                     # API principal (NestJS/Node.js)
├── predictor_demanda_api/       # API de predicción de demanda (FastAPI/Python)
├── recomendador_cursos_api/     # API de recomendación de cursos (FastAPI/Python)
├── docker-compose.yml           # Orquestación de servicios
├── .env                         # Variables de entorno
└── README.md                    # Este archivo
```

## 🚀 Inicio Rápido

### 1. Clonar repositorios

**Usando Git Bash:**
```bash
bash setup.sh
```

**Usando PowerShell:**
```powershell
.\setup.ps1
```

**Manualmente:**
```bash
git clone https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git backend
git clone https://github.com/mairsor/predictor-recomendador-generador_frontend frontend
git clone https://github.com/mairsor/predictor-demanda-api.git predictor_demanda_api
git clone https://github.com/Vouresz/Mod_Recomendador recomendador_cursos_api
```

### 2. Configurar variables de entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar con tus credenciales de PostgreSQL
nano .env  # o usa tu editor preferido
```

### 3. Levantar todos los servicios

```bash
# Construir e iniciar todos los contenedores
docker-compose up -d --build

# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend
```

## 🌐 Acceso a los Servicios

Una vez levantados los contenedores:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:4000
- **Predictor de Demanda API**: http://localhost:8000
  - Docs: http://localhost:8000/docs
- **Recomendador de Cursos API**: http://localhost:8001
  - Docs: http://localhost:8001/docs

## 📦 Microservicios

### 🎨 Frontend
- **Tecnología**: React / Next.js
- **Puerto**: 3000
- **Repositorio**: [predictor-recomendador-generador_frontend](https://github.com/mairsor/predictor-recomendador-generador_frontend)

### 🔧 Backend
- **Tecnología**: NestJS / Node.js
- **Puerto**: 4000
- **Repositorio**: [schedule-recommendation-backend](https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git)
- **Funciones**:
  - Autenticación y autorización
  - Gestión de usuarios
  - CRUD de cursos y horarios
  - Integración con APIs de ML

### 📊 Predictor de Demanda API
- **Tecnología**: FastAPI / Python
- **Puerto**: 8000
- **Repositorio**: [predictor-demanda-api](https://github.com/mairsor/predictor-demanda-api)
- **Funciones**:
  - Predicción de demanda de matrícula por curso
  - Modelos de Machine Learning (RandomForest)
  - Gestión de modelos entrenados
  - Exportación de resultados

### 🎯 Recomendador de Cursos API
- **Tecnología**: FastAPI / Python
- **Puerto**: 8001
- **Repositorio**: [Mod_Recomendador](https://github.com/Vouresz/Mod_Recomendador)
- **Funciones**:
  - Recomendación personalizada de cursos
  - Filtrado colaborativo
  - Análisis de historial académico

## 🔗 Comunicación entre Servicios

Los microservicios se comunican a través de una **red interna de Docker** (`horarios_network`):

```
Frontend → Backend → Predictor API
                  → Recomendador API
                  → PostgreSQL (servidor externo)
```

**Ejemplo de llamada desde Backend a Predictor:**
```javascript
const response = await fetch('http://predictor_demanda_api:8000/api/v1/predictions', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ scope: 'all', model_type: 'auto' })
});
```

## 🗄️ Base de Datos

El sistema utiliza **PostgreSQL** alojado en un servidor externo. Todos los microservicios se conectan a la misma base de datos.

**Configuración en `.env`:**
```env
DB_HOST=tu_servidor_postgresql.com
DB_PORT=5432
DB_NAME=uni_horarios_db
DB_USER=postgres
DB_PASSWORD=tu_password
```

## 🛠️ Comandos Útiles

### Docker Compose

```bash
# Iniciar servicios
docker-compose up -d

# Detener servicios
docker-compose down

# Ver logs
docker-compose logs -f [servicio]

# Reiniciar un servicio
docker-compose restart [servicio]

# Reconstruir servicios
docker-compose up -d --build --force-recreate

# Ver estado de servicios
docker-compose ps

# Ejecutar comando en un contenedor
docker-compose exec [servicio] bash
```

### Desarrollo Individual

**Backend:**
```bash
cd backend
npm install
npm run dev
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Predictor API:**
```bash
cd predictor_demanda_api
pip install -r requirements.txt
python main.py
```

**Recomendador API:**
```bash
cd recomendador_cursos_api
pip install -r requirements.txt
python main.py
```

## 🧪 Testing

```bash
# Backend
cd backend && npm test

# Predictor API
cd predictor_demanda_api && pytest

# Recomendador API
cd recomendador_cursos_api && pytest
```

## 📚 Documentación

- **API Predictor**: http://localhost:8000/docs (Swagger UI)
- **API Recomendador**: http://localhost:8001/docs (Swagger UI)
- **Backend**: Consultar README de cada repositorio

## 🤝 Equipo de Desarrollo

**Universidad Nacional de Ingeniería (UNI)**  
**Curso**: Ingeniería de Software (CIB02)  
**Semestre**: 2025-2

## 📄 Licencia

Proyecto académico - Universidad Nacional de Ingeniería

---

**Última actualización**: 2025-11-20  
**Versión**: 1.0.0
