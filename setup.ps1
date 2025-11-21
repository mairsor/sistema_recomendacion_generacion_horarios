# setup.ps1 - Script para clonar todos los repositorios del proyecto
# Sistema de Recomendación y Generación de Horarios - UNI
# Fecha: 2025-11-20

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║  Sistema de Recomendación y Generación de Horarios - UNI      ║" -ForegroundColor Blue
Write-Host "║  Clonando repositorios del proyecto...                        ║" -ForegroundColor Blue
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Blue

# URLs de los repositorios
$BACKEND_REPO = "https://github.com/EduardoVillegasB02/schedule-recommendation-backend.git"
$FRONTEND_REPO = "https://github.com/mairsor/predictor-recomendador-generador_frontend"
$RECOMENDADOR_REPO = "https://github.com/Vouresz/Mod_Recomendador"

# Función para clonar repositorio
function Clone-Repo {
    param (
        [string]$RepoUrl,
        [string]$TargetDir,
        [string]$DisplayName
    )
    
    Write-Host "► Procesando: $DisplayName" -ForegroundColor Yellow
    
    if (Test-Path "$TargetDir\.git") {
        Write-Host "  ✓ $TargetDir ya existe, actualizando..." -ForegroundColor Green
        Set-Location $TargetDir
        try {
            git pull origin main 2>$null
            if ($LASTEXITCODE -ne 0) {
                git pull origin master 2>$null
            }
            if ($LASTEXITCODE -ne 0) {
                git pull
            }
        }
        catch {
            Write-Host "  ⚠ No se pudo actualizar" -ForegroundColor Yellow
        }
        Set-Location ..
    } else {
        Write-Host "  → Clonando en $TargetDir..." -ForegroundColor Cyan
        git clone $RepoUrl $TargetDir
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✓ Completado" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Error al clonar" -ForegroundColor Red
        }
    }
    Write-Host ""
}

# Verificar que Git esté instalado
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "✗ Git no está instalado. Por favor instala Git primero." -ForegroundColor Red
    exit 1
}

Write-Host "[1/3] Clonando Backend..." -ForegroundColor Blue
Clone-Repo -RepoUrl $BACKEND_REPO -TargetDir "backend" -DisplayName "Backend (Node.js/NestJS)"

Write-Host "[2/3] Clonando Frontend..." -ForegroundColor Blue
Clone-Repo -RepoUrl $FRONTEND_REPO -TargetDir "frontend" -DisplayName "Frontend (React/Next.js)"

Write-Host "[3/3] Clonando Módulo Recomendador..." -ForegroundColor Blue
Clone-Repo -RepoUrl $RECOMENDADOR_REPO -TargetDir "recomendador_cursos_api" -DisplayName "API Recomendador de Cursos"

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✓ Todos los repositorios clonados exitosamente               ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Green

Write-Host "Estructura del proyecto:" -ForegroundColor Blue
Get-ChildItem | Format-Table Name, Mode, LastWriteTime

Write-Host "`nPróximos pasos:" -ForegroundColor Yellow
Write-Host "  1. Revisar cada módulo en su carpeta"
Write-Host "  2. Configurar variables de entorno en .env"
Write-Host "  3. Ejecutar: " -NoNewline
Write-Host "docker-compose up -d --build" -ForegroundColor Green
Write-Host "  4. Acceder a: http://localhost:3000 (Frontend)`n"
