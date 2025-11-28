# Script para mover Docker Desktop y WSL2 al Disco D
# Proyecto: Sistema de Recomendación y Generación de Horarios - UNI
# Propósito: Liberar espacio en disco C moviendo Docker al disco D

param(
    [switch]$SkipCleanup = $false
)

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║     Mover Docker Desktop y WSL2 al Disco D                ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Verificar que estamos ejecutando como administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "⚠️  ADVERTENCIA: Se recomienda ejecutar este script como Administrador" -ForegroundColor Yellow
    Write-Host ""
}

# Verificar espacio disponible
Write-Host "📊 Verificando espacio en discos..." -ForegroundColor Cyan
$driveC = Get-PSDrive C
$driveD = Get-PSDrive D
Write-Host "   Disco C - Libre: $([math]::Round($driveC.Free/1GB, 2)) GB" -ForegroundColor Gray
Write-Host "   Disco D - Libre: $([math]::Round($driveD.Free/1GB, 2)) GB" -ForegroundColor Gray
Write-Host ""

if ($driveD.Free -lt 20GB) {
    Write-Host "⚠️  ADVERTENCIA: Disco D tiene menos de 20GB libres. Verifica que hay suficiente espacio." -ForegroundColor Yellow
    $continue = Read-Host "¿Deseas continuar? (s/n)"
    if ($continue -ne "s") {
        Write-Host "❌ Operación cancelada" -ForegroundColor Red
        exit
    }
}

# Paso 1: Verificar Docker Desktop
Write-Host "🐳 Verificando Docker Desktop..." -ForegroundColor Cyan
$dockerProcess = Get-Process "Docker Desktop" -ErrorAction SilentlyContinue
if ($dockerProcess) {
    Write-Host "⚠️  Docker Desktop está ejecutándose" -ForegroundColor Yellow
    Write-Host "   Por favor, cierra Docker Desktop completamente:" -ForegroundColor Yellow
    Write-Host "   1. Click derecho en el icono de Docker en la bandeja del sistema" -ForegroundColor Gray
    Write-Host "   2. Selecciona 'Quit Docker Desktop'" -ForegroundColor Gray
    Write-Host ""
    Read-Host "Presiona Enter cuando hayas cerrado Docker Desktop"
    
    # Verificar nuevamente
    Start-Sleep -Seconds 2
    $dockerProcess = Get-Process "Docker Desktop" -ErrorAction SilentlyContinue
    if ($dockerProcess) {
        Write-Host "❌ Docker Desktop aún está ejecutándose. Por favor ciérralo y ejecuta el script nuevamente." -ForegroundColor Red
        exit 1
    }
}
Write-Host "✅ Docker Desktop no está ejecutándose" -ForegroundColor Green
Write-Host ""

# Paso 2: Detener WSL
Write-Host "🔄 Deteniendo WSL..." -ForegroundColor Cyan
wsl --shutdown
Start-Sleep -Seconds 5

# Verificar que WSL se detuvo
$wslStatus = wsl --list --verbose 2>&1
Write-Host "✅ WSL detenido" -ForegroundColor Green
Write-Host ""

# Paso 3: Crear directorios
Write-Host "📁 Creando directorios en D:\WSL..." -ForegroundColor Cyan
$wslPath = "D:\WSL"
$dockerDesktopPath = "$wslPath\docker-desktop"
$dockerDataPath = "$wslPath\docker-desktop-data"

try {
    New-Item -ItemType Directory -Path $wslPath -Force | Out-Null
    New-Item -ItemType Directory -Path $dockerDesktopPath -Force | Out-Null
    New-Item -ItemType Directory -Path $dockerDataPath -Force | Out-Null
    Write-Host "✅ Directorios creados" -ForegroundColor Green
} catch {
    Write-Host "❌ Error al crear directorios: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Paso 4: Exportar docker-desktop
Write-Host "📦 Exportando docker-desktop..." -ForegroundColor Cyan
Write-Host "   (esto puede tomar 2-5 minutos)" -ForegroundColor Gray
$dockerDesktopTar = "$wslPath\docker-desktop.tar"
try {
    wsl --export docker-desktop $dockerDesktopTar
    if (Test-Path $dockerDesktopTar) {
        $size = [math]::Round((Get-Item $dockerDesktopTar).Length/1MB, 2)
        Write-Host "✅ docker-desktop exportado ($size MB)" -ForegroundColor Green
    } else {
        throw "El archivo .tar no se creó"
    }
} catch {
    Write-Host "❌ Error al exportar docker-desktop: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Paso 5: Exportar docker-desktop-data
Write-Host "📦 Exportando docker-desktop-data..." -ForegroundColor Cyan
Write-Host "   (esto tomará más tiempo, 5-30 minutos dependiendo del tamaño)" -ForegroundColor Gray
$dockerDataTar = "$wslPath\docker-desktop-data.tar"
try {
    wsl --export docker-desktop-data $dockerDataTar
    if (Test-Path $dockerDataTar) {
        $size = [math]::Round((Get-Item $dockerDataTar).Length/1MB, 2)
        Write-Host "✅ docker-desktop-data exportado ($size MB)" -ForegroundColor Green
    } else {
        throw "El archivo .tar no se creó"
    }
} catch {
    Write-Host "❌ Error al exportar docker-desktop-data: $_" -ForegroundColor Red
    Write-Host "   Los archivos exportados están en $wslPath" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# Paso 6: Desregistrar distribuciones originales
Write-Host "🗑️  Desregistrando distribuciones originales..." -ForegroundColor Cyan
try {
    Write-Host "   Desregistrando docker-desktop..." -ForegroundColor Gray
    wsl --unregister docker-desktop
    
    Write-Host "   Desregistrando docker-desktop-data..." -ForegroundColor Gray
    wsl --unregister docker-desktop-data
    
    Write-Host "✅ Distribuciones desregistradas" -ForegroundColor Green
} catch {
    Write-Host "❌ Error al desregistrar: $_" -ForegroundColor Red
    Write-Host "   Puedes revertir importando desde los archivos .tar" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# Paso 7: Importar en disco D
Write-Host "📥 Importando distribuciones en disco D..." -ForegroundColor Cyan

Write-Host "   Importando docker-desktop..." -ForegroundColor Gray
try {
    wsl --import docker-desktop $dockerDesktopPath $dockerDesktopTar --version 2
    Write-Host "✅ docker-desktop importado en D:" -ForegroundColor Green
} catch {
    Write-Host "❌ Error al importar docker-desktop: $_" -ForegroundColor Red
    exit 1
}

Write-Host "   Importando docker-desktop-data..." -ForegroundColor Gray
try {
    wsl --import docker-desktop-data $dockerDataPath $dockerDataTar --version 2
    Write-Host "✅ docker-desktop-data importado en D:" -ForegroundColor Green
} catch {
    Write-Host "❌ Error al importar docker-desktop-data: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Paso 8: Verificar
Write-Host "🔍 Verificando distribuciones WSL..." -ForegroundColor Cyan
wsl --list --verbose
Write-Host ""

# Paso 9: Limpiar archivos .tar (opcional)
if (-not $SkipCleanup) {
    Write-Host "🧹 Limpieza de archivos temporales..." -ForegroundColor Cyan
    $cleanup = Read-Host "¿Deseas eliminar los archivos .tar ahora? Esto liberará espacio en D: (s/n)"
    if ($cleanup -eq "s") {
        try {
            Remove-Item $dockerDesktopTar -Force
            Remove-Item $dockerDataTar -Force
            Write-Host "✅ Archivos .tar eliminados" -ForegroundColor Green
        } catch {
            Write-Host "⚠️  Error al eliminar archivos .tar: $_" -ForegroundColor Yellow
            Write-Host "   Puedes eliminarlos manualmente desde: $wslPath" -ForegroundColor Gray
        }
    } else {
        Write-Host "ℹ️  Los archivos .tar se conservan en: $wslPath" -ForegroundColor Cyan
        Write-Host "   Puedes eliminarlos manualmente más tarde con:" -ForegroundColor Gray
        Write-Host "   Remove-Item $dockerDesktopTar" -ForegroundColor Gray
        Write-Host "   Remove-Item $dockerDataTar" -ForegroundColor Gray
    }
} else {
    Write-Host "ℹ️  Archivos .tar conservados (flag -SkipCleanup)" -ForegroundColor Cyan
}
Write-Host ""

# Resumen final
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║              ✅ Proceso Completado                         ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Siguientes pasos:" -ForegroundColor Cyan
Write-Host "   1. Inicia Docker Desktop" -ForegroundColor White
Write-Host "   2. Verifica que funciona correctamente (docker images, docker ps)" -ForegroundColor White
Write-Host "   3. Si todo funciona bien, los datos ya están en disco D:" -ForegroundColor White
Write-Host ""
Write-Host "📍 Ubicaciones:" -ForegroundColor Cyan
Write-Host "   - docker-desktop: $dockerDesktopPath" -ForegroundColor Gray
Write-Host "   - docker-desktop-data: $dockerDataPath" -ForegroundColor Gray
Write-Host ""
Write-Host "💡 Comandos útiles:" -ForegroundColor Cyan
Write-Host "   - Ver distribuciones WSL: wsl --list -v" -ForegroundColor Gray
Write-Host "   - Ver info de Docker: docker info" -ForegroundColor Gray
Write-Host "   - Ver espacio usado: docker system df" -ForegroundColor Gray
Write-Host ""

# Calcular espacio estimado liberado
$totalSize = 0
if (Test-Path $dockerDesktopTar) {
    $totalSize += (Get-Item $dockerDesktopTar).Length
}
if (Test-Path $dockerDataTar) {
    $totalSize += (Get-Item $dockerDataTar).Length
}
if ($totalSize -gt 0) {
    $totalSizeGB = [math]::Round($totalSize/1GB, 2)
    Write-Host "💾 Espacio aproximado que se liberará en C: después de limpiar: $totalSizeGB GB" -ForegroundColor Green
}

Write-Host ""
Write-Host "Presiona Enter para finalizar..." -ForegroundColor Gray
Read-Host
