@echo off
REM =======================================================================
REM  LearnEVO Help - one-click launcher
REM
REM  1. Kills any zombie help server from a previous session (stale
REM     servers keep browsers serving cached pre-fix CSS).
REM  2. Starts server.py, which sends Cache-Control: no-store.
REM  3. Auto-detects a free port starting at 8765 and opens the browser.
REM     Ctrl+C (or close this window) to stop.
REM =======================================================================

cd /d "%~dp0\learnevo-help"

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  Python is not on your PATH. Install Python 3 from python.org,
    echo  or edit this file to point at a Python installation.
    echo.
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0learnevo-help\kill-help-server.ps1"

python server.py
pause
