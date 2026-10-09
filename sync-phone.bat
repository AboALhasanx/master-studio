@echo off
title Master Studio - Phone Sync
cls
echo =======================================================
echo   Master Studio: Local High-Speed Phone Sync (ADB)
echo =======================================================
echo.
echo   Double-click = incremental sync of the study folders.
echo   Optional flags (pass after the .bat name):
echo     --all        also mirror toolbox + dashboard + docs
echo     --dry-run    show what would change, change nothing
echo     --prune      list phone files that no longer exist here
echo     --clean --yes  delete them (exact mirror)
echo     --pull       bring phone files back into _inbox_from_phone\
echo     --wifi IP    connect over Wi-Fi first
echo.
python "%~dp090_Shared_Toolbox\tools\phone_sync.py" %*
echo.
pause
