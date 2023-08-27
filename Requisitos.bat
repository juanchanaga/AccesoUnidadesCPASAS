@echo off

:: Verificar si Chocolatey está instalado
echo Verificando si Chocolatey está instalado...
choco --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
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

:: Verificar si las bibliotecas requeridas están instaladas
echo Verificando si las bibliotecas requeridas están instaladas...
python -c "import getpass" > nul 2>&1
if %errorlevel% neq 0 (
    echo Bibliotecas requeridas no están instaladas. Instalando...
    python -m pip install getpass
) else (
    echo Bibliotecas requeridas ya están instaladas.
)

:: Verificar si la biblioteca subprocess.run está instalada
echo Verificando si la biblioteca subprocess.run está instalada...
python -c "import subprocess.run" > nul 2>&1
if %errorlevel% neq 0 (
    echo Biblioteca subprocess.run no está instalada. Instalando...
    python -m pip install subprocess.run
) else (
    echo Biblioteca subprocess.run ya está instalada.
)

echo Instalación completada.
pause
