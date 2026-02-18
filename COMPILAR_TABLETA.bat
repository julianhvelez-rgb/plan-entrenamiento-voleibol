@echo off
chcp 65001 >nul
cls
echo ═══════════════════════════════════════════════════════════════
echo   🏐 COMPILAR APLICACIÓN TABLETA STANDALONE
echo ═══════════════════════════════════════════════════════════════
echo.
echo Esta herramienta creará un archivo .exe independiente
echo que NO requiere navegador web externo.
echo.
echo ═══════════════════════════════════════════════════════════════
echo.

REM Verificar si pywebview está instalado
echo 📦 Verificando dependencias...
python -c "import webview" 2>nul
if %errorlevel% neq 0 (
    echo.
    echo ❌ pywebview no está instalado
    echo 📦 Instalando dependencias necesarias...
    echo.
    pip install pywebview flask pyinstaller
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Error al instalar dependencias
        echo    Por favor ejecuta manualmente: pip install pywebview flask pyinstaller
        echo.
        pause
        exit /b 1
    )
    echo ✅ Dependencias instaladas correctamente
    echo.
) else (
    echo ✅ Dependencias OK
    echo.
)

REM Verificar si PyInstaller está instalado
python -c "import PyInstaller" 2>nul
if %errorlevel% neq 0 (
    echo 📦 Instalando PyInstaller...
    pip install pyinstaller
)

echo ═══════════════════════════════════════════════════════════════
echo   🔨 INICIANDO COMPILACIÓN
echo ═══════════════════════════════════════════════════════════════
echo.
echo ⚙️  Esto puede tomar varios minutos...
echo ⚠️  No cierres esta ventana hasta que termine
echo.

REM Limpiar compilaciones anteriores
if exist "build" rmdir /s /q "build"
if exist "dist\EntrenamientoVoleibol_Tableta" rmdir /s /q "dist\EntrenamientoVoleibol_Tableta"

REM Compilar con PyInstaller
pyinstaller --clean --noconfirm EntrenamientoVoleibol_Tableta.spec

if %errorlevel% equ 0 (
    echo.
    echo ═══════════════════════════════════════════════════════════════
    echo   ✅ COMPILACIÓN EXITOSA
    echo ═══════════════════════════════════════════════════════════════
    echo.
    echo 📁 El ejecutable está en:
    echo    dist\EntrenamientoVoleibol_Tableta.exe
    echo.
    echo 🚀 Para ejecutar la aplicación:
    echo    1. Ve a la carpeta "dist"
    echo    2. Haz doble clic en "EntrenamientoVoleibol_Tableta.exe"
    echo.
    echo 💡 Puedes copiar este .exe a cualquier PC con Windows
    echo    y funcionará sin instalar Python ni nada más.
    echo.
    echo ═══════════════════════════════════════════════════════════════
    
    REM Abrir carpeta dist
    explorer dist
) else (
    echo.
    echo ═══════════════════════════════════════════════════════════════
    echo   ❌ ERROR EN LA COMPILACIÓN
    echo ═══════════════════════════════════════════════════════════════
    echo.
    echo Por favor revisa los mensajes de error arriba.
    echo.
)

echo.
pause
