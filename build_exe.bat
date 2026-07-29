@echo off
cls
echo ========================================================
echo   COMPILANDO SISTEMA PACIENTES (ONEFILE + CONSOLE)
echo ========================================================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

pyinstaller --noconfirm --onefile --console --add-data "app/templates;app/templates" --add-data "app/static;app/static" --add-data "instance/sgpn_nutricion.db;instance" --icon="app/static/img/icons/logo.ico" --name "SistemaPacientes" run.py

if %errorlevel% eq 0 (
    echo.
    echo ========================================================
    echo   ¡COMPILACION EXITOSA!
    echo ========================================================
    echo Archivo generado en: dist\SistemaPacientes.exe
    echo.
) else (
    echo.
    echo [ERROR] Fallo la compilacion.
    echo.
)
pause
