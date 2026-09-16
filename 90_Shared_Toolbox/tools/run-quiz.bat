@ECHO off
SETLOCAL
SET SCRIPT_DIR=%~dp0
python "%SCRIPT_DIR%quiz_runner.py" %*
