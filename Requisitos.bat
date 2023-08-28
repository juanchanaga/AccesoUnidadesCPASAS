@echo off

:: Verificar si Chocolatey está instalado
echo Verificando si Chocolatey está instalado...
choco --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
) else (
    echo Chocolatey ya está instalado.
)

:: Verificar si Python está instalado
echo Verificando si Python está instalado...
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado. Instalando Python...
    choco install python -y
) else (
    echo Python ya está instalado.
)

echo Instalación completada.
pause
