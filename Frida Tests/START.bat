@echo off
taskkill /F /IM evoerp.exe      >nul 2>&1
taskkill /F /IM tp7runtime.exe  >nul 2>&1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0run-tests.ps1"
pause
