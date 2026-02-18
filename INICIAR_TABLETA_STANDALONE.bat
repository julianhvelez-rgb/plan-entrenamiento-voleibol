@echo off
chcp 65001 >nul
cls
echo ═══════════════════════════════════════════════════════════════
echo   🏐 ENTRENAMIENTO DE VOLEIBOL - APP STANDALONE
echo ═══════════════════════════════════════════════════════════════
echo.
echo 📱 Iniciando aplicación independiente...
echo.
echo ═══════════════════════════════════════════════════════════════
echo.

REM Verificar si pywebview está instalado
python -c "import webview" 2>nul
if %errorlevel% neq 0 (
    echo ❌ pywebview no está instalado
    echo.
    echo 📦 Instalando dependencias necesarias...
    pip install pywebview flask
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Error al instalar dependencias
        echo    Por favor ejecuta manualmente: pip install pywebview flask
        echo.
        pause
        exit /b 1
    )
    echo ✅ Instalado correctamente
    echo.
)

REM Verificar si Flask está instalado
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo 📦 Instalando Flask...
    pip install flask
)

echo ✅ Iniciando aplicación...
echo.

REM Iniciar la aplicación standalone
python app_tableta_standalone.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Error al iniciar la aplicación
    echo.
    pause
)
