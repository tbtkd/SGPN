@echo off
setlocal enabledelayedexpansion
cls

echo ========================================================
echo   COMPILANDO SISTEMA PACIENTES (ONEFILE + CONSOLE)
echo ========================================================
echo.

:: 1. Validar que PyInstaller este disponible
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] PyInstaller no esta instalado o no esta activado el entorno virtual.
    echo Por favor activa tu entorno virtual ^(ej. venv\Scripts\activate^) e intenta de nuevo.
    echo.
    pause
    exit /b 1
)

:: 2. Limpieza de carpetas y archivos temporales previos
echo [--] Limpiando compilaciones anteriores...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /f /q *.spec

:: Validar si la carpeta dist no se pudo borrar (por ejemplo, si el .exe estaba abierto)
if exist dist (
    echo.
    echo [ERROR] No se pudo eliminar la carpeta 'dist'. 
    echo Asegurate de cerrar 'SistemaPacientes.exe' si esta ejecutandose.
    echo.
    pause
    exit /b 1
)

echo [--] Iniciando empaquetado con PyInstaller...
echo.

:: 3. Ejecutar PyInstaller
pyinstaller --noconfirm --onefile --console ^
  --add-data "app/templates;app/templates" ^
  --add-data "app/static;app/static" ^
  --add-data "instance/sgpn_nutricion.db;instance" ^
  --icon="app/static/img/icons/logo.ico" ^
  --name "SistemaPacientes" run.py

:: 4. Evaluacion de Errores
if %errorlevel% equ 0 (
    if exist "dist\SistemaPacientes.exe" (
        echo.
        echo ========================================================
        echo   ¡COMPILACION EXITOSA!
        echo ========================================================
        echo Archivo generado en: dist\SistemaPacientes.exe
        echo.
    ) else (
        echo.
        echo [ERROR] PyInstaller finalizo sin codigo de error, pero no se encontro el .exe en dist\
        echo.
    )
) else (
    echo.
    echo ========================================================
    echo   [ERROR] FALLO LA COMPILACION CON CODIGO %errorlevel%
    echo ========================================================
    echo Revisa los mensajes anteriores en la consola para identificar la causa.
    echo.
)

pause