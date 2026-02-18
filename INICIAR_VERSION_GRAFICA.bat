@echo off
chcp 65001 > nul
color 0B
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║      🏐 ENTRENAMIENTO DE VOLEIBOL - VERSIÓN GUI  🏐          ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    ✨ Iniciando versión con interfaz gráfica moderna...
echo.
timeout /t 2 /nobreak > nul

cd /d "%~dp0"
start "" "dist\EntrenamientoVoleibol_GUI.exe"

echo.
echo    ✅ Aplicación GUI iniciada correctamente
echo.
echo    📝 Características:
echo       • Interfaz con ventanas y botones
echo       • Diagramas de cancha en colores  
echo       • Pestañas para fácil navegación
echo       • Muy fácil de usar
echo.
echo    Puedes cerrar esta ventana
echo.
timeout /t 4
exit
