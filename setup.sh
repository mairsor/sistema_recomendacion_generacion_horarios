#!/bin/bash
# setup.sh - Script para clonar todos los repositorios del proyecto
# Sistema de Recomendación y Generación de Horarios - UNI
# Fecha: 2025-11-20

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Sistema de Recomendación y Generación de Horarios - UNI      ║${NC}"
echo -e "${BLUE}║  Clonando repositorios del proyecto...                        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}\n"

# URLs de los repositorios
BACKEND_REPO="https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git"
FRONTEND_REPO="https://github.com/mairsor/predictor-recomendador-generador_frontend"
RECOMENDADOR_REPO="https://github.com/Vouresz/Mod_Recomendador"

# Función para clonar repositorio
clone_repo() {
    local repo_url=$1
    local target_dir=$2
    local display_name=$3
    
    echo -e "${YELLOW}► Procesando: $display_name${NC}"
    
    if [ -d "$target_dir/.git" ]; then
        echo -e "${GREEN}  ✓ $target_dir ya existe, actualizando...${NC}"
        cd "$target_dir"
        git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || git pull
        cd ..
    else
        echo -e "${BLUE}  → Clonando en $target_dir...${NC}"
        git clone "$repo_url" "$target_dir"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}  ✓ Completado${NC}"
        else
            echo -e "${RED}  ✗ Error al clonar${NC}"
        fi
    fi
    echo ""
}

# Verificar que Git esté instalado
if ! command -v git &> /dev/null; then
    echo -e "${RED}✗ Git no está instalado. Por favor instala Git primero.${NC}"
    exit 1
fi

echo -e "${BLUE}[1/3] Clonando Backend...${NC}"
clone_repo "$BACKEND_REPO" "backend" "Backend (Node.js/NestJS)"

echo -e "${BLUE}[2/3] Clonando Frontend...${NC}"
clone_repo "$FRONTEND_REPO" "frontend" "Frontend (React/Next.js)"

echo -e "${BLUE}[3/3] Clonando Módulo Recomendador...${NC}"
clone_repo "$RECOMENDADOR_REPO" "recomendador_cursos_api" "API Recomendador de Cursos"

echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✓ Todos los repositorios clonados exitosamente               ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${BLUE}Estructura del proyecto:${NC}"
ls -la --color=auto 2>/dev/null || ls -la

echo -e "\n${YELLOW}Próximos pasos:${NC}"
echo -e "  1. Revisar cada módulo en su carpeta"
echo -e "  2. Configurar variables de entorno en .env"
echo -e "  3. Ejecutar: ${GREEN}docker-compose up -d --build${NC}"
echo -e "  4. Acceder a: http://localhost:3000 (Frontend)\n"
