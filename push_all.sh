#!/bin/bash
# Script para hacer push en todos los submódulos y el repositorio principal
# Uso: ./push_all.sh "mensaje del commit"

if [ -z "$1" ]; then
    echo "Error: Debes proporcionar un mensaje de commit"
    echo "Uso: ./push_all.sh \"mensaje del commit\""
    exit 1
fi

COMMIT_MESSAGE="$1"
FAILED_REPOS=()

echo "==========================================="
echo "Push automático en todos los repositorios"
echo "Mensaje: $COMMIT_MESSAGE"
echo "==========================================="
echo ""

# Función para hacer push en un submódulo
push_submodule() {
    local submodule=$1
    echo "📦 Procesando: $submodule"
    
    if [ ! -d "$submodule" ]; then
        echo "   ⚠️  Directorio no encontrado, saltando..."
        return
    fi
    
    cd "$submodule" || return
    
    # Verificar si hay cambios
    if [[ -z $(git status -s) ]]; then
        echo "   ℹ️  No hay cambios para commitear"
    else
        git add .
        git commit -m "$COMMIT_MESSAGE"
        
        if git push origin main; then
            echo "   ✅ Push exitoso"
        else
            echo "   ❌ Error en push"
            FAILED_REPOS+=("$submodule")
        fi
    fi
    
    cd ..
    echo ""
}

# Push en cada submódulo
push_submodule "backend"
push_submodule "frontend"
push_submodule "predictor_demanda_api"
push_submodule "recomendador_cursos_api"

# Push en repositorio principal
echo "📦 Procesando: Repositorio principal"
git add .

if [[ -z $(git status -s) ]]; then
    echo "   ℹ️  No hay cambios para commitear"
else
    git commit -m "$COMMIT_MESSAGE"
    
    if git push origin main; then
        echo "   ✅ Push exitoso"
    else
        echo "   ❌ Error en push"
        FAILED_REPOS+=("repositorio-principal")
    fi
fi

echo ""
echo "==========================================="
echo "Resumen"
echo "==========================================="

if [ ${#FAILED_REPOS[@]} -eq 0 ]; then
    echo "✅ Todos los push se completaron exitosamente"
else
    echo "❌ Errores en los siguientes repositorios:"
    for repo in "${FAILED_REPOS[@]}"; do
        echo "   - $repo"
    done
    exit 1
fi
