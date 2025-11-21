# Comandos para agregar submódulos manualmente
# Sistema de Recomendación y Generación de Horarios - UNI

# ========================================
# INSTRUCCIONES MANUALES
# ========================================

# 1. Abrir Git Bash o PowerShell en el directorio del proyecto
# 2. Copiar y pegar los comandos uno por uno

# ========================================
# Paso 1: Eliminar carpetas vacías (si existen)
# ========================================
rm -rf backend frontend predictor_demanda_api recomendador_cursos_api

# ========================================
# Paso 2: Agregar submódulos
# ========================================

# Backend
git submodule add https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git backend

# Frontend
git submodule add https://github.com/mairsor/predictor-recomendador-generador_frontend frontend

# Predictor de Demanda
git submodule add https://github.com/mairsor/predictor-demanda-api.git predictor_demanda_api

# Recomendador de Cursos
git submodule add https://github.com/Vouresz/Mod_Recomendador recomendador_cursos_api

# ========================================
# Paso 3: Inicializar y actualizar submódulos
# ========================================
git submodule init
git submodule update

# ========================================
# Paso 4: Verificar submódulos agregados
# ========================================
git submodule status

# ========================================
# Paso 5: Hacer commit de los cambios
# ========================================
git add .gitmodules backend frontend predictor_demanda_api recomendador_cursos_api
git commit -m "Agregar submódulos: backend, frontend, predictor y recomendador"
git push origin main

# ========================================
# COMANDOS ÚTILES PARA SUBMÓDULOS
# ========================================

# Actualizar todos los submódulos a la última versión
git submodule update --remote --merge

# Actualizar un submódulo específico
cd backend
git pull origin main
cd ..
git add backend
git commit -m "Actualizar submódulo backend"
git push

# Clonar proyecto con submódulos (para otros desarrolladores)
git clone --recurse-submodules https://github.com/mairsor/sistema_recomendacion_generacion_horarios.git

# Si ya clonaste sin --recurse-submodules
git submodule init
git submodule update

# Ver cambios en submódulos
git diff --submodule

# ========================================
# TROUBLESHOOTING
# ========================================

# Si hay error "already exists in the index"
git rm --cached backend
git rm --cached frontend
git rm --cached recomendador_cursos_api
# Luego volver a ejecutar git submodule add

# Si hay conflictos al actualizar
cd backend
git checkout main
git pull
cd ..
git add backend
git commit -m "Resolver conflicto en submódulo backend"
