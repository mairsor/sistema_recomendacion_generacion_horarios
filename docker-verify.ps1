# Script de verificación del sistema Docker (PowerShell)
# Sistema de Recomendación y Generación de Horarios - UNI

$ErrorActionPreference = "Stop"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Verificación del Sistema Docker" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Cargar variables de entorno
if (-not (Test-Path ".env.docker")) {
    Write-Host "Error: No se encontró .env.docker" -ForegroundColor Red
    exit 1
}

Get-Content .env.docker | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        [Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

Write-Host "1. Verificando estado de contenedores..."
docker-compose --env-file .env.docker ps
Write-Host ""

Write-Host "2. Verificando healthchecks..."
$services = @("horarios_frontend", "horarios_backend", "predictor_demanda_api", "recomendador_cursos_api")
foreach ($service in $services) {
    try {
        $health = docker inspect --format='{{.State.Health.Status}}' $service 2>$null
        if ($health -eq "healthy") {
            Write-Host "  ✓ $service`: " -NoNewline; Write-Host "healthy" -ForegroundColor Green
        } elseif ($health -eq "") {
            Write-Host "  - $service`: " -NoNewline; Write-Host "no healthcheck" -ForegroundColor Yellow
        } else {
            Write-Host "  ✗ $service`: " -NoNewline; Write-Host $health -ForegroundColor Red
        }
    } catch {
        Write-Host "  ✗ $service`: " -NoNewline; Write-Host "container not found" -ForegroundColor Red
    }
}
Write-Host ""

Write-Host "3. Verificando conectividad de endpoints..."

# Frontend
try {
    $response = Invoke-WebRequest -Uri "http://localhost:$env:FRONTEND_PORT" -UseBasicParsing -TimeoutSec 5
    Write-Host "  ✓ Frontend (port $env:FRONTEND_PORT): " -NoNewline; Write-Host "OK" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Frontend (port $env:FRONTEND_PORT): " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
}

# Backend
try {
    $response = Invoke-WebRequest -Uri "http://localhost:$env:BACKEND_PORT/api" -UseBasicParsing -TimeoutSec 5
    Write-Host "  ✓ Backend (port $env:BACKEND_PORT): " -NoNewline; Write-Host "OK" -ForegroundColor Green
} catch {
    if ($_.Exception.Response.StatusCode.value__ -eq 404) {
        Write-Host "  ✓ Backend (port $env:BACKEND_PORT): " -NoNewline; Write-Host "OK" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Backend (port $env:BACKEND_PORT): " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
    }
}

# Predictor
try {
    $response = Invoke-WebRequest -Uri "http://localhost:$env:PREDICTOR_PORT/health" -UseBasicParsing -TimeoutSec 5
    Write-Host "  ✓ Predictor API (port $env:PREDICTOR_PORT): " -NoNewline; Write-Host "OK" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Predictor API (port $env:PREDICTOR_PORT): " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
}

# Recomendador
try {
    $response = Invoke-WebRequest -Uri "http://localhost:$env:RECOMENDADOR_PORT/api/health" -UseBasicParsing -TimeoutSec 5
    Write-Host "  ✓ Recomendador API (port $env:RECOMENDADOR_PORT): " -NoNewline; Write-Host "OK" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Recomendador API (port $env:RECOMENDADOR_PORT): " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
}
Write-Host ""

Write-Host "4. Verificando comunicación interna entre servicios..."

# Backend -> Predictor
try {
    $result = docker exec horarios_backend curl -s -o /dev/null -w "%{http_code}" http://predictor_demanda_api:8000/health
    if ($result -eq "200") {
        Write-Host "  ✓ Backend -> Predictor: " -NoNewline; Write-Host "OK" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Backend -> Predictor: " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
    }
} catch {
    Write-Host "  ✗ Backend -> Predictor: " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
}

# Backend -> Recomendador
try {
    $result = docker exec horarios_backend curl -s -o /dev/null -w "%{http_code}" http://recomendador_cursos_api:8001/api/health
    if ($result -eq "200") {
        Write-Host "  ✓ Backend -> Recomendador: " -NoNewline; Write-Host "OK" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Backend -> Recomendador: " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
    }
} catch {
    Write-Host "  ✗ Backend -> Recomendador: " -NoNewline; Write-Host "ERROR" -ForegroundColor Red
}
Write-Host ""

Write-Host "5. Verificando uso de recursos..."
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
Write-Host ""

Write-Host "6. Verificando volúmenes..."
docker volume ls | Select-String -Pattern "predictor|recomendador"
Write-Host ""

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Verificación completada" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
