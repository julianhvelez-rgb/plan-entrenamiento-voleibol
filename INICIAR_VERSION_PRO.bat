@echo off
chcp 65001 > nul
color 0C
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║      🏐 ENTRENAMIENTO DE VOLEIBOL - VERSIÓN PRO 🏐          ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo.
echo    ✨ Características de la Versión Pro:
echo.
echo       🎨 Logo profesional de voleibol
echo       🏐 Visualización de CADA ejercicio en cancha
echo       📊 10+ tipos de diagramas diferentes
echo       💾 Guardar planes de entrenamiento
echo       🎯 Detección inteligente de ejercicios
echo       📐 Cancha con colores realistas
echo.
echo    ⏳ Iniciando aplicación profesional...
echo.
timeout /t 3 /nobreak > nul

cd /d "%~dp0"

if exist "dist\EntrenamientoVoleibol_Pro.exe" (
    start "" "dist\EntrenamientoVoleibol_Pro.exe"
    echo.
    echo    ✅ Aplicación Pro iniciada correctamente
    echo.
    echo    📝 Ubicación del escritorio:
    echo       EntrenamientoVoleibol_Pro.exe
    echo.
) else (
    echo.
    echo    ⚠️  No se encuentra el ejecutable Pro
    echo.
    echo    📂 Buscando en el escritorio...
    echo.
    
    if exist "%USERPROFILE%\OneDrive\Desktop\EntrenamientoVoleibol_Pro.exe" (
        start "" "%USERPROFILE%\OneDrive\Desktop\EntrenamientoVoleibol_Pro.exe"
        echo    ✅ Aplicación iniciada desde el Escritorio
    ) else (
        echo    ❌ No se encuentra EntrenamientoVoleibol_Pro.exe
        echo.
        echo    Verifica que el archivo existe en:
        echo    - dist\EntrenamientoVoleibol_Pro.exe
        echo    - Escritorio\EntrenamientoVoleibol_Pro.exe
    )
)

echo.
echo    Puedes cerrar esta ventana
echo.
timeout /t 5
exit
