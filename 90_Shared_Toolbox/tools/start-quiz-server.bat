@ECHO off
TITLE Master Studio - Quiz Server (LAN :5000)
cd /d "%~dp0..\..\91_Dashboard"
set PY="C:/Users/gokoq/AppData/Local/Programs/Python/Python312/python.exe"
echo ============================================================
echo   MASTER STUDIO - QUIZ SERVER
echo   Listening on 0.0.0.0:5000  ^(LAN + localhost^)
echo   Keep this window OPEN while studying.
echo ============================================================
echo.
%PY% app.py
echo.
echo [Server stopped] - press any key to close.
pause >nul
