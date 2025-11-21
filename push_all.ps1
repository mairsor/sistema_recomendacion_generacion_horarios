# Script para hacer push en todos los submódulos y el repositorio principal
# Uso: .\push_all.ps1 "mensaje del commit"

param(
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage
)

$FailedRepos = @()

Write-Host "==========================================="
Write-Host "Push automático en todos los repositorios"
Write-Host "Mensaje: $CommitMessage"
Write-Host "==========================================="
Write-Host ""

# Función para hacer push en un submódulo
function Push-Submodule {
    param([string]$Submodule)
    
    Write-Host "📦 Procesando: $Submodule" -ForegroundColor Cyan
    
    if (-not (Test-Path $Submodule)) {
        Write-Host "   ⚠️  Directorio no encontrado, saltando..." -ForegroundColor Yellow
        return
    }
    
    Push-Location $Submodule
    
    # Verificar si hay cambios
    $status = git status -s
    if ([string]::IsNullOrWhiteSpace($status)) {
        Write-Host "   ℹ️  No hay cambios para commitear" -ForegroundColor Gray
    }
    else {
        git add .
        git commit -m $CommitMessage
        
        if ($LASTEXITCODE -eq 0) {
            git push origin main
            if ($LASTEXITCODE -eq 0) {
                Write-Host "   ✅ Push exitoso" -ForegroundColor Green
            }
            else {
                Write-Host "   ❌ Error en push" -ForegroundColor Red
                $script:FailedRepos += $Submodule
            }
        }
    }
    
    Pop-Location
    Write-Host ""
}

# Push en cada submódulo
Push-Submodule "backend"
Push-Submodule "frontend"
Push-Submodule "predictor_demanda_api"
Push-Submodule "recomendador_cursos_api"

# Push en repositorio principal
Write-Host "📦 Procesando: Repositorio principal" -ForegroundColor Cyan
git add .

$status = git status -s
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "   ℹ️  No hay cambios para commitear" -ForegroundColor Gray
}
else {
    git commit -m $CommitMessage
    
    if ($LASTEXITCODE -eq 0) {
        git push origin main
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ✅ Push exitoso" -ForegroundColor Green
        }
        else {
            Write-Host "   ❌ Error en push" -ForegroundColor Red
            $FailedRepos += "repositorio-principal"
        }
    }
}

Write-Host ""
Write-Host "==========================================="
Write-Host "Resumen"
Write-Host "==========================================="

if ($FailedRepos.Count -eq 0) {
    Write-Host "✅ Todos los push se completaron exitosamente" -ForegroundColor Green
}
else {
    Write-Host "❌ Errores en los siguientes repositorios:" -ForegroundColor Red
    foreach ($repo in $FailedRepos) {
        Write-Host "   - $repo" -ForegroundColor Red
    }
    exit 1
}
