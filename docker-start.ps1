# Script de inicio para el sistema completo con Docker (PowerShell)
# Sistema de Recomendación y Generación de Horarios - UNI

$ErrorActionPreference = "Stop"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Sistema de Recomendación y Generación de Horarios" -ForegroundColor Cyan
Write-Host "Universidad Nacional de Ingeniería (UNI)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que existe el archivo .env
if (-not (Test-Path ".env.docker")) {
    Write-Host "Error: No se encontró el archivo .env.docker" -ForegroundColor Red
    Write-Host "Por favor, copia .env.example a .env.docker y configura las variables"
    exit 1
}

Write-Host "✓ Archivo .env.docker encontrado" -ForegroundColor Green
Write-Host ""

# Leer configuración del .env.docker
Get-Content .env.docker | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        [Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

Write-Host "Configuración cargada:"
Write-Host "  - Frontend Port: $env:FRONTEND_PORT"
Write-Host "  - Backend Port: $env:BACKEND_PORT"
Write-Host "  - Predictor Port: $env:PREDICTOR_PORT"
Write-Host "  - Recomendador Port: $env:RECOMENDADOR_PORT"
Write-Host "  - Database Host: $env:DB_HOST"
Write-Host ""

# Limpiar contenedores anteriores (opcional)
$clean = Read-Host "¿Deseas limpiar contenedores y volúmenes anteriores? (y/N)"
if ($clean -eq "y" -or $clean -eq "Y") {
    Write-Host "Limpiando contenedores y volúmenes anteriores..." -ForegroundColor Yellow
    docker-compose --env-file .env.docker down -v
    Write-Host "✓ Limpieza completada" -ForegroundColor Green
    Write-Host ""
}

# Construir imágenes
Write-Host "Construyendo imágenes Docker..." -ForegroundColor Yellow
docker-compose --env-file .env.docker build --no-cache

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Imágenes construidas exitosamente" -ForegroundColor Green
} else {
    Write-Host "✗ Error al construir las imágenes" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Iniciar servicios
Write-Host "Iniciando servicios..." -ForegroundColor Yellow
docker-compose --env-file .env.docker up -d

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Servicios iniciados exitosamente" -ForegroundColor Green
} else {
    Write-Host "✗ Error al iniciar los servicios" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Esperar a que los servicios estén listos
Write-Host "Esperando a que los servicios estén listos..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Verificar estado de los servicios
Write-Host ""
Write-Host "Estado de los servicios:"
docker-compose --env-file .env.docker ps
Write-Host ""

# Mostrar logs
Write-Host "Mostrando logs de los últimos 50 mensajes..." -ForegroundColor Yellow
docker-compose --env-file .env.docker logs --tail=50
Write-Host ""

# URLs de acceso
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Sistema iniciado correctamente!" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "URLs de acceso:"
Write-Host "  🌐 Frontend:     http://localhost:$env:FRONTEND_PORT" -ForegroundColor Cyan
Write-Host "  🔧 Backend:      http://localhost:$env:BACKEND_PORT/api" -ForegroundColor Cyan
Write-Host "  🤖 Predictor:    http://localhost:$env:PREDICTOR_PORT/docs" -ForegroundColor Cyan
Write-Host "  💡 Recomendador: http://localhost:$env:RECOMENDADOR_PORT/api/health" -ForegroundColor Cyan
Write-Host ""
Write-Host "Comandos útiles:"
Write-Host "  Ver logs:        docker-compose --env-file .env.docker logs -f"
Write-Host "  Detener:         docker-compose --env-file .env.docker down"
Write-Host "  Reiniciar:       docker-compose --env-file .env.docker restart"
Write-Host "  Ver estado:      docker-compose --env-file .env.docker ps"
Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
