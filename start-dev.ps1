# Script para iniciar Backend y Frontend para pruebas

Write-Host "🚀 Iniciando servicios para pruebas de integración..." -ForegroundColor Green
Write-Host ""

# Configuración
$BACKEND_DIR = "d:\Estudios\Universidad Nacional de Ingeniería\8. Octavo Ciclo\Ingeniería de Software (CIB02)\Proyecto\modelo_predictor_demanda\backend"
$FRONTEND_DIR = "d:\Estudios\Universidad Nacional de Ingeniería\8. Octavo Ciclo\Ingeniería de Software (CIB02)\Proyecto\modelo_predictor_demanda\frontend"

Write-Host "📦 Backend: $BACKEND_DIR" -ForegroundColor Cyan
Write-Host "🌐 Frontend: $FRONTEND_DIR" -ForegroundColor Cyan
Write-Host ""

# Iniciar Backend en una nueva ventana de PowerShell
Write-Host "🔧 Iniciando Backend (puerto 3003)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$BACKEND_DIR'; npm run start:dev"

# Esperar un poco para que el backend inicie
Start-Sleep -Seconds 5

# Iniciar Frontend en una nueva ventana de PowerShell
Write-Host "🎨 Iniciando Frontend (puerto 3001)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$FRONTEND_DIR'; npm run dev"

Write-Host ""
Write-Host "✅ Servicios iniciados!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Información:" -ForegroundColor Cyan
Write-Host "   Backend:  http://localhost:3003/api" -ForegroundColor White
Write-Host "   Frontend: http://localhost:3001" -ForegroundColor White
Write-Host "   Test:     http://localhost:3001/test" -ForegroundColor White
Write-Host ""
Write-Host "🔑 Credenciales de prueba:" -ForegroundColor Cyan
Write-Host "   Email:    admin@uni.edu.pe" -ForegroundColor White
Write-Host "   Password: admin123" -ForegroundColor White
Write-Host ""
Write-Host "Para detener los servicios, cierra las ventanas de PowerShell abiertas." -ForegroundColor Gray
