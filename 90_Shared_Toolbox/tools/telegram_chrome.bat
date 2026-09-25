@echo off
REM Master-Studio Telegram debug Chrome launcher
set CHROME=C:\Users\gokoq\AppData\Local\ms-playwright\chromium-1243\chrome-win64\chrome.exe
set PROFILE=%~dp0.tg-profile
if not exist "%PROFILE%" mkdir "%PROFILE%"
start "" "%CHROME%" --remote-debugging-port=9222 --user-data-dir="%PROFILE%" --no-first-run --no-default-browser-check about:blank
echo Debug Chromium launched on http://127.0.0.1:9222
