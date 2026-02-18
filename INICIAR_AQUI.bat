@echo off
chcp 65001 > nul
color 0A
cls
echo.
echo ═══════════════════════════════════════════════════════════════
echo    🏐 SISTEMA DE ENTRENAMIENTO DE VOLEIBOL 🏐
echo ═══════════════════════════════════════════════════════════════
echo.
echo    Iniciando aplicación...
echo.
timeout /t 2 /nobreak > nul

cd /d "%~dp0"
start "" "dist\EntrenamientoVoleibol.exe"

echo.
echo    ✓ Aplicación iniciada correctamente
echo.
echo    Puedes cerrar esta ventana
echo.
timeout /t 3
exit
