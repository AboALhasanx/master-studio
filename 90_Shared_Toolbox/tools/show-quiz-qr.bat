@ECHO off
TITLE Master Studio - Quiz QR Portal
chcp 65001 >nul
set PY="C:/Users/gokoq/AppData/Local/Programs/Python/Python312/python.exe"
set SCRIPT=%~dp0quiz_qr.py
echo ============================================================
echo   MASTER STUDIO - QUIZ QR PORTAL
echo ============================================================
echo.
%PY% -X utf8 "%SCRIPT%" %*
echo.
echo [QR shown] - press any key to close.
pause >nul
