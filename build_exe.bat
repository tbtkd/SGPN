@echo off
setlocal enabledelayedexpansion
cls

echo ========================================================
echo   COMPILANDO SISTEMA PACIENTES (ONEFILE + BD EXTERNA)
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

:: 2. Validar que todos los archivos y carpetas obligatorios existan
echo [--] Validando integridad de recursos y dependencias...

if not exist "app\templates" (
    echo [ERROR] La carpeta obligatoria 'app\templates' no existe.
    pause
    exit /b 1
)

if not exist "app\static" (
    echo [ERROR] La carpeta obligatoria 'app\static' no existe.
    pause
    exit /b 1
)

if not exist "app\static\img\icons\logo.ico" (
    echo [ERROR] El archivo de icono obligatorio 'app\static\img\icons\logo.ico' no existe.
    pause
    exit /b 1
)

:: Validar si la base de datos base existe en instance local
if not exist "instance" mkdir instance
if not exist "instance\sgpn_nutricion.db" (
    echo [ADVERTENCIA] No se encontro 'instance\sgpn_nutricion.db'. Se creara un archivo base vacio.
    type nul > "instance\sgpn_nutricion.db"
)

:: 3. Limpieza de carpetas y archivos temporales previos
echo [--] Limpiando compilaciones anteriores...
if exist build rmdir /s /q build
if exist dist\SistemaPacientes.exe del /f /q dist\SistemaPacientes.exe
if exist *.spec del /f /q *.spec

if exist dist\SistemaPacientes.exe (
    echo.
    echo [ERROR] No se pudo eliminar el ejecutable en 'dist'. 
    echo Asegurate de cerrar 'SistemaPacientes.exe' si esta ejecutandose.
    echo.
    pause
    exit /b 1
)

echo [--] Iniciando empaquetado con PyInstaller...
echo.

:: 4. Ejecutar PyInstaller 
:: =========================================================================================
:: OPCION A (EMPAQUETADO INTERNO TOTAL): Usa la siguiente linea si deseas incrustar la BD dentro del .exe
:: pyinstaller --noconfirm --onefile --console --add-data "app/templates;app/templates" --add-data "app/static;app/static" --add-data "instance/sgpn_nutricion.db;instance" --icon="app/static/img/icons/logo.ico" --name "SistemaPacientes" run.py

:: OPCION B (ACTIVA - BD EXTERNA): La BD se mantiene fuera en la carpeta dist\instance\ para ser visible/reemplazable
pyinstaller --noconfirm --onefile --console ^
  --add-data "app/templates;app/templates" ^
  --add-data "app/static;app/static" ^
  --icon="app/static/img/icons/logo.ico" ^
  --name "SistemaPacientes" run.py
:: =========================================================================================

:: 5. Evaluacion y Despliegue de Base de Datos externa en dist\instance\
if %errorlevel% equ 0 (
    if exist "dist\SistemaPacientes.exe" (
        echo [--] Configurando directorio de base de datos externa en 'dist\instance\'...
        if not exist "dist\instance" mkdir "dist\instance"
        
        :: Copiar la BD a dist\instance SOLO si no existe previa (para NO sobreescribir datos reales)
        if not exist "dist\instance\sgpn_nutricion.db" (
            echo [--] Copiando base de datos inicial a 'dist\instance\sgpn_nutricion.db'...
            copy "instance\sgpn_nutricion.db" "dist\instance\sgpn_nutricion.db" >nul
        ) else (
            echo [NOTA] Se detecto una base de datos existente en 'dist\instance\sgpn_nutricion.db'.
            echo        NO se sobreescribio para preservar la informacion existente.
        )

        echo.
        echo ========================================================
        echo   ¡COMPILACION Y CONFIGURACION EXITOSA!
        echo ========================================================
        echo Ejecutable generado en : dist\SistemaPacientes.exe
        echo Base de datos visible en: dist\instance\sgpn_nutricion.db
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