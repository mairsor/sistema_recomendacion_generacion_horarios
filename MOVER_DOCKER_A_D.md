# Guía para Mover Docker al Disco D

## Problema
Docker está usando el disco C y ya no hay suficiente espacio. Necesitamos mover Docker y WSL2 al disco D.

## Solución: Mover WSL2 al Disco D

### Paso 1: Detener Docker Desktop
1. Cierra Docker Desktop completamente
2. Verifica que no hay procesos de Docker corriendo

### Paso 2: Detener WSL
```powershell
wsl --shutdown
```

### Paso 3: Crear directorio en disco D
```powershell
mkdir D:\WSL
mkdir D:\WSL\docker-desktop
mkdir D:\WSL\docker-desktop-data
```

### Paso 4: Exportar las distribuciones de Docker
```powershell
# Exportar docker-desktop
wsl --export docker-desktop D:\WSL\docker-desktop.tar

# Exportar docker-desktop-data (la que contiene todas las imágenes y contenedores)
wsl --export docker-desktop-data D:\WSL\docker-desktop-data.tar
```

### Paso 5: Desregistrar las distribuciones originales
```powershell
# Desregistrar docker-desktop
wsl --unregister docker-desktop

# Desregistrar docker-desktop-data
wsl --unregister docker-desktop-data
```

### Paso 6: Importar en disco D
```powershell
# Importar docker-desktop
wsl --import docker-desktop D:\WSL\docker-desktop D:\WSL\docker-desktop.tar --version 2

# Importar docker-desktop-data
wsl --import docker-desktop-data D:\WSL\docker-desktop-data D:\WSL\docker-desktop-data.tar --version 2
```

### Paso 7: Limpiar archivos temporales (opcional)
```powershell
# Una vez verificado que todo funciona, puedes borrar los .tar
Remove-Item D:\WSL\docker-desktop.tar
Remove-Item D:\WSL\docker-desktop-data.tar
```

### Paso 8: Iniciar Docker Desktop
Abre Docker Desktop y verifica que funciona correctamente.

### Paso 9: Verificar ubicación
```powershell
# Ver dónde están las distribuciones WSL
wsl --list -v
```

## Opción Alternativa: Solo cambiar ubicación de imágenes en Docker Desktop

Si prefieres no mover WSL completo:

1. Abre Docker Desktop
2. Ve a **Settings** → **Resources** → **Advanced**
3. Cambia **Disk image location** a `D:\DockerData`
4. Reinicia Docker Desktop

## Verificación Final

Después de mover, verifica:

```powershell
# Ver info de Docker
docker info

# Listar imágenes (deberías ver tus imágenes existentes)
docker images

# Ver espacio usado
docker system df
```

## Notas Importantes

- **Tiempo**: El proceso puede tomar 10-30 minutos dependiendo del tamaño de tus datos Docker
- **Espacio necesario**: Temporalmente necesitarás espacio en C para los archivos .tar durante la exportación
- **Backup**: Si tienes datos importantes en contenedores, considera hacer backup antes
- **Alternativa rápida**: Si tienes poco espacio en C, puedes limpiar Docker primero:
  ```powershell
  docker system prune -a --volumes
  ```
  Esto eliminará todo (imágenes, contenedores, volúmenes no usados)

## Script Automatizado

Puedes usar este script para automatizar el proceso:

```powershell
# Script: mover-docker-a-d.ps1

Write-Host "=== Moviendo Docker a Disco D ===" -ForegroundColor Cyan

# Detener Docker Desktop
Write-Host "1. Por favor, cierra Docker Desktop manualmente" -ForegroundColor Yellow
Read-Host "Presiona Enter cuando hayas cerrado Docker Desktop"

# Detener WSL
Write-Host "2. Deteniendo WSL..." -ForegroundColor Green
wsl --shutdown
Start-Sleep -Seconds 5

# Crear directorios
Write-Host "3. Creando directorios en D:\WSL..." -ForegroundColor Green
New-Item -ItemType Directory -Path "D:\WSL" -Force
New-Item -ItemType Directory -Path "D:\WSL\docker-desktop" -Force
New-Item -ItemType Directory -Path "D:\WSL\docker-desktop-data" -Force

# Exportar
Write-Host "4. Exportando docker-desktop (esto puede tomar varios minutos)..." -ForegroundColor Green
wsl --export docker-desktop D:\WSL\docker-desktop.tar

Write-Host "5. Exportando docker-desktop-data (esto tomará más tiempo)..." -ForegroundColor Green
wsl --export docker-desktop-data D:\WSL\docker-desktop-data.tar

# Desregistrar
Write-Host "6. Desregistrando distribuciones originales..." -ForegroundColor Green
wsl --unregister docker-desktop
wsl --unregister docker-desktop-data

# Importar
Write-Host "7. Importando docker-desktop en D:\WSL..." -ForegroundColor Green
wsl --import docker-desktop D:\WSL\docker-desktop D:\WSL\docker-desktop.tar --version 2

Write-Host "8. Importando docker-desktop-data en D:\WSL..." -ForegroundColor Green
wsl --import docker-desktop-data D:\WSL\docker-desktop-data D:\WSL\docker-desktop-data.tar --version 2

Write-Host "=== Proceso completado ===" -ForegroundColor Cyan
Write-Host "Ahora puedes iniciar Docker Desktop" -ForegroundColor Yellow
Write-Host ""
Write-Host "Para limpiar los archivos .tar (después de verificar que todo funciona):" -ForegroundColor Yellow
Write-Host "Remove-Item D:\WSL\docker-desktop.tar" -ForegroundColor Gray
Write-Host "Remove-Item D:\WSL\docker-desktop-data.tar" -ForegroundColor Gray
```

## Troubleshooting

### Error: "No se puede acceder al archivo"
- Asegúrate de que Docker Desktop está completamente cerrado
- Verifica que no hay procesos de Docker en el Administrador de Tareas

### Docker no inicia después de mover
- Verifica con `wsl --list -v` que ambas distribuciones están en estado "Stopped"
- Reinicia Windows
- Si persiste, puedes revertir importando desde los .tar originales en C

### Espacio no liberado en C
- Después de mover, el espacio en C solo se liberará si borras los archivos .tar
- También puedes necesitar limpiar: `docker system prune -a`
