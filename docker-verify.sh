#!/bin/bash
# Script de verificación del sistema Docker
# Sistema de Recomendación y Generación de Horarios - UNI

set -e

echo "=================================================="
echo "Verificación del Sistema Docker"
echo "=================================================="
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Cargar variables de entorno
if [ -f .env.docker ]; then
    set -a
    source .env.docker
    set +a
else
    echo -e "${RED}Error: No se encontró .env.docker${NC}"
    exit 1
fi

echo "1. Verificando estado de contenedores..."
docker-compose --env-file .env.docker ps
echo ""

echo "2. Verificando healthchecks..."
for service in horarios_frontend horarios_backend predictor_demanda_api recomendador_cursos_api; do
    health=$(docker inspect --format='{{.State.Health.Status}}' $service 2>/dev/null || echo "no healthcheck")
    if [ "$health" = "healthy" ]; then
        echo -e "  ✓ $service: ${GREEN}healthy${NC}"
    elif [ "$health" = "no healthcheck" ]; then
        echo -e "  - $service: ${YELLOW}no healthcheck${NC}"
    else
        echo -e "  ✗ $service: ${RED}$health${NC}"
    fi
done
echo ""

echo "3. Verificando conectividad de endpoints..."

# Frontend
if curl -s -o /dev/null -w "%{http_code}" http://localhost:${FRONTEND_PORT} | grep -q "200\|301\|302"; then
    echo -e "  ✓ Frontend (port ${FRONTEND_PORT}): ${GREEN}OK${NC}"
else
    echo -e "  ✗ Frontend (port ${FRONTEND_PORT}): ${RED}ERROR${NC}"
fi

# Backend
if curl -s -o /dev/null -w "%{http_code}" http://localhost:${BACKEND_PORT}/api | grep -q "200\|404"; then
    echo -e "  ✓ Backend (port ${BACKEND_PORT}): ${GREEN}OK${NC}"
else
    echo -e "  ✗ Backend (port ${BACKEND_PORT}): ${RED}ERROR${NC}"
fi

# Predictor
if curl -s -o /dev/null -w "%{http_code}" http://localhost:${PREDICTOR_PORT}/health | grep -q "200"; then
    echo -e "  ✓ Predictor API (port ${PREDICTOR_PORT}): ${GREEN}OK${NC}"
else
    echo -e "  ✗ Predictor API (port ${PREDICTOR_PORT}): ${RED}ERROR${NC}"
fi

# Recomendador
if curl -s -o /dev/null -w "%{http_code}" http://localhost:${RECOMENDADOR_PORT}/api/health | grep -q "200"; then
    echo -e "  ✓ Recomendador API (port ${RECOMENDADOR_PORT}): ${GREEN}OK${NC}"
else
    echo -e "  ✗ Recomendador API (port ${RECOMENDADOR_PORT}): ${RED}ERROR${NC}"
fi
echo ""

echo "4. Verificando comunicación interna entre servicios..."

# Backend -> Predictor
if docker exec horarios_backend curl -s -o /dev/null -w "%{http_code}" http://predictor_demanda_api:8000/health | grep -q "200"; then
    echo -e "  ✓ Backend -> Predictor: ${GREEN}OK${NC}"
else
    echo -e "  ✗ Backend -> Predictor: ${RED}ERROR${NC}"
fi

# Backend -> Recomendador
if docker exec horarios_backend curl -s -o /dev/null -w "%{http_code}" http://recomendador_cursos_api:8001/api/health | grep -q "200"; then
    echo -e "  ✓ Backend -> Recomendador: ${GREEN}OK${NC}"
else
    echo -e "  ✗ Backend -> Recomendador: ${RED}ERROR${NC}"
fi
echo ""

echo "5. Verificando uso de recursos..."
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
echo ""

echo "6. Verificando volúmenes..."
docker volume ls | grep -E "predictor|recomendador"
echo ""

echo "=================================================="
echo "Verificación completada"
echo "=================================================="
