#!/bin/bash
# Script de inicio para el sistema completo con Docker
# Sistema de Recomendación y Generación de Horarios - UNI

set -e

echo "=================================================="
echo "Sistema de Recomendación y Generación de Horarios"
echo "Universidad Nacional de Ingeniería (UNI)"
echo "=================================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar que existe el archivo .env
if [ ! -f .env.docker ]; then
    echo -e "${RED}Error: No se encontró el archivo .env.docker${NC}"
    echo "Por favor, copia .env.example a .env.docker y configura las variables"
    exit 1
fi

echo -e "${GREEN}✓ Archivo .env.docker encontrado${NC}"
echo ""

# Cargar variables de entorno
set -a
source .env.docker
set +a

echo "Configuración cargada:"
echo "  - Frontend Port: ${FRONTEND_PORT}"
echo "  - Backend Port: ${BACKEND_PORT}"
echo "  - Predictor Port: ${PREDICTOR_PORT}"
echo "  - Recomendador Port: ${RECOMENDADOR_PORT}"
echo "  - Database Host: ${DB_HOST}"
echo ""

# Limpiar contenedores anteriores (opcional)
read -p "¿Deseas limpiar contenedores y volúmenes anteriores? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Limpiando contenedores y volúmenes anteriores...${NC}"
    docker-compose --env-file .env.docker down -v
    echo -e "${GREEN}✓ Limpieza completada${NC}"
    echo ""
fi

# Construir imágenes
echo -e "${YELLOW}Construyendo imágenes Docker...${NC}"
docker-compose --env-file .env.docker build --no-cache

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Imágenes construidas exitosamente${NC}"
else
    echo -e "${RED}✗ Error al construir las imágenes${NC}"
    exit 1
fi
echo ""

# Iniciar servicios
echo -e "${YELLOW}Iniciando servicios...${NC}"
docker-compose --env-file .env.docker up -d

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Servicios iniciados exitosamente${NC}"
else
    echo -e "${RED}✗ Error al iniciar los servicios${NC}"
    exit 1
fi
echo ""

# Esperar a que los servicios estén listos
echo -e "${YELLOW}Esperando a que los servicios estén listos...${NC}"
sleep 10

# Verificar estado de los servicios
echo ""
echo "Estado de los servicios:"
docker-compose --env-file .env.docker ps
echo ""

# Mostrar logs
echo -e "${YELLOW}Mostrando logs de los últimos 20 segundos...${NC}"
docker-compose --env-file .env.docker logs --tail=50
echo ""

# URLs de acceso
echo "=================================================="
echo -e "${GREEN}Sistema iniciado correctamente!${NC}"
echo "=================================================="
echo ""
echo "URLs de acceso:"
echo "  🌐 Frontend:     http://localhost:${FRONTEND_PORT}"
echo "  🔧 Backend:      http://localhost:${BACKEND_PORT}/api"
echo "  🤖 Predictor:    http://localhost:${PREDICTOR_PORT}/docs"
echo "  💡 Recomendador: http://localhost:${RECOMENDADOR_PORT}/api/health"
echo ""
echo "Comandos útiles:"
echo "  Ver logs:        docker-compose --env-file .env.docker logs -f"
echo "  Detener:         docker-compose --env-file .env.docker down"
echo "  Reiniciar:       docker-compose --env-file .env.docker restart"
echo "  Ver estado:      docker-compose --env-file .env.docker ps"
echo ""
echo "=================================================="
