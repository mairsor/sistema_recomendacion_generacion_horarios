# add_submodules.ps1 - Script para agregar submódulos de Git
# Sistema de Recomendación y Generación de Horarios - UNI
# Fecha: 2025-11-20

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║  Agregando submódulos de Git al proyecto                      ║" -ForegroundColor Blue
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Blue

# URLs de los repositorios
$BACKEND_REPO = "https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git"
$FRONTEND_REPO = "https://github.com/mairsor/predictor-recomendador-generador_frontend"
$RECOMENDADOR_REPO = "https://github.com/Vouresz/Mod_Recomendador"

Write-Host "► Paso 1: Eliminando carpetas vacías si existen..." -ForegroundColor Yellow
Remove-Item -Path "backend" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "frontend" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "recomendador_cursos_api" -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "✓ Carpetas eliminadas`n" -ForegroundColor Green

Write-Host "► Paso 2: Agregando submódulo 'backend'..." -ForegroundColor Yellow
git submodule add $BACKEND_REPO backend
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Backend agregado exitosamente`n" -ForegroundColor Green
} else {
    Write-Host "✗ Error al agregar backend`n" -ForegroundColor Red
}

Write-Host "► Paso 3: Agregando submódulo 'frontend'..." -ForegroundColor Yellow
git submodule add $FRONTEND_REPO frontend
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Frontend agregado exitosamente`n" -ForegroundColor Green
} else {
    Write-Host "✗ Error al agregar frontend`n" -ForegroundColor Red
}

Write-Host "► Paso 4: Agregando submódulo 'recomendador_cursos_api'..." -ForegroundColor Yellow
git submodule add $RECOMENDADOR_REPO recomendador_cursos_api
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Recomendador agregado exitosamente`n" -ForegroundColor Green
} else {
    Write-Host "✗ Error al agregar recomendador`n" -ForegroundColor Red
}

Write-Host "► Paso 5: Inicializando y actualizando submódulos..." -ForegroundColor Yellow
git submodule init
git submodule update
Write-Host ""

Write-Host "► Paso 6: Verificando submódulos..." -ForegroundColor Yellow
git submodule status
Write-Host ""

Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✓ Submódulos agregados exitosamente                          ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Green

Write-Host "Próximos pasos:" -ForegroundColor Yellow
Write-Host "  1. Revisar archivo .gitmodules creado"
Write-Host "  2. Hacer commit de los cambios:"
Write-Host "     git add .gitmodules backend frontend recomendador_cursos_api" -ForegroundColor Cyan
Write-Host "     git commit -m `"Agregar submódulos: backend, frontend y recomendador`"" -ForegroundColor Cyan
Write-Host "     git push" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para clonar el proyecto completo en el futuro, usar:"
Write-Host "  git clone --recurse-submodules [URL_DEL_REPO]" -ForegroundColor Cyan
Write-Host ""
