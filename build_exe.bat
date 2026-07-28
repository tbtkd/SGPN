@echo off
TITLE Compilador SGPN - Sistema de Gestion de Pacientes y Nutricion (OneFile)
COLOR 0B
CLS

echo ========================================================
echo   INICIANDO COMPILACION CON PYINSTALLER (ONEFILE + CONSOLE)
echo ========================================================

:: Verificar entorno virtual
IF EXIST .venv\Scripts\activate.bat (
    echo [INFO] Activando entorno virtual (.venv)...
    call .venv\Scripts\activate.bat
) ELSE IF EXIST venv\Scripts\activate.bat (
    echo [INFO] Activando entorno virtual (venv)...
    call venv\Scripts\activate.bat
) ELSE (
    echo [ADVERTENCIA] No se encontro entorno virtual local. Usando Python del sistema...
)

:: Verificar instalacion de PyInstaller
python -c "import PyInstaller" 2>nul
if %errorlevel% neq 0 (
    echo [INFO] PyInstaller no esta instalado. Instalando dependencias...
    pip install pyinstaller
)

echo [INFO] Limpiando compilaciones anteriores (build, dist)...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [INFO] Ejecutando PyInstaller para empaquetar SistemaPacientes en un unico archivo .exe...
pyinstaller --noconfirm --onefile --console ^
    --add-data "app/templates;app/templates" ^
    --add-data "app/static;app/static" ^
    --add-data "instance/sgpn_nutricion.db;instance" ^
    --icon="app/static/img/icons/logo.ico" ^
    --name "SistemaPacientes" ^
    run.py

if %errorlevel% eq 0 (
    echo.
    echo ========================================================
    echo   ¡COMPILACION EXITOSA!
    echo ========================================================
    echo El ejecutable unico se encuentra disponible en:
    echo dist\SistemaPacientes.exe
    echo (Sin carpeta _internal - Totalmente autonomo)
    echo.
) else (
    echo.
    echo [ERROR] Ocurrio un fallo durante la compilacion. Revise los mensajes anteriores.
    echo.
)

pause
