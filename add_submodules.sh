#!/bin/bash
# add_submodules.sh - Script para agregar submódulos de Git
# Sistema de Recomendación y Generación de Horarios - UNI
# Fecha: 2025-11-20

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  Agregando submódulos de Git al proyecto                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# URLs de los repositorios
BACKEND_REPO="https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git"
FRONTEND_REPO="https://github.com/mairsor/predictor-recomendador-generador_frontend"
RECOMENDADOR_REPO="https://github.com/Vouresz/Mod_Recomendador"

echo "► Paso 1: Eliminando carpetas vacías si existen..."
rm -rf backend frontend recomendador_cursos_api 2>/dev/null
echo "✓ Carpetas eliminadas"
echo ""

echo "► Paso 2: Agregando submódulo 'backend'..."
git submodule add "$BACKEND_REPO" backend
if [ $? -eq 0 ]; then
    echo "✓ Backend agregado exitosamente"
else
    echo "✗ Error al agregar backend"
fi
echo ""

echo "► Paso 3: Agregando submódulo 'frontend'..."
git submodule add "$FRONTEND_REPO" frontend
if [ $? -eq 0 ]; then
    echo "✓ Frontend agregado exitosamente"
else
    echo "✗ Error al agregar frontend"
fi
echo ""

echo "► Paso 4: Agregando submódulo 'recomendador_cursos_api'..."
git submodule add "$RECOMENDADOR_REPO" recomendador_cursos_api
if [ $? -eq 0 ]; then
    echo "✓ Recomendador agregado exitosamente"
else
    echo "✗ Error al agregar recomendador"
fi
echo ""

echo "► Paso 5: Inicializando y actualizando submódulos..."
git submodule init
git submodule update
echo ""

echo "► Paso 6: Verificando submódulos..."
git submodule status
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  ✓ Submódulos agregados exitosamente                          ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Próximos pasos:"
echo "  1. Revisar archivo .gitmodules creado"
echo "  2. Hacer commit de los cambios:"
echo "     git add .gitmodules backend frontend recomendador_cursos_api"
echo "     git commit -m \"Agregar submódulos: backend, frontend y recomendador\""
echo "     git push"
echo ""
echo "Para clonar el proyecto completo en el futuro, usar:"
echo "  git clone --recurse-submodules [URL_DEL_REPO]"
echo ""
