@echo off
chcp 65001 >nul
cls
echo ═══════════════════════════════════════════════════════════════
echo   🏐 ENTRENAMIENTO DE VOLEIBOL - VERSIÓN TABLETA
echo ═══════════════════════════════════════════════════════════════
echo.
echo 📱 Iniciando servidor web para tabletas...
echo.
echo ⚠️  IMPORTANTE: NO cierres esta ventana mientras uses la app
echo.
echo ═══════════════════════════════════════════════════════════════
echo.

REM Verificar si Flask está instalado
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Flask no está instalado
    echo.
    echo 📦 Instalando Flask...
    pip install flask
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Error al instalar Flask
        echo    Por favor ejecuta manualmente: pip install flask
        echo.
        pause
        exit /b 1
    )
    echo ✅ Flask instalado correctamente
    echo.
)

echo ✅ Iniciando servidor...
echo.

REM Iniciar la aplicación
python app_tableta.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Error al iniciar el servidor
    echo.
    pause
)
