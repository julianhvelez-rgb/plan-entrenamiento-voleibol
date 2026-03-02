@echo off
chcp 65001 > nul
color 0A
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║      🏐 ENTRENAMIENTO DE VOLEIBOL - APP TABLETA 🏐          ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo.
echo    📱 Iniciando servidor para tableta...
echo.
echo    ⏳ Espera unos segundos...
echo.
timeout /t 2 /nobreak > nul

python app_tableta_simple.py

pause
