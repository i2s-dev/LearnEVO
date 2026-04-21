@echo off
REM Launcher for the LearnEVO Help browser.
REM - Kills any prior help server (zombies cause cached-CSS bugs).
REM - Runs server.py (sends Cache-Control: no-store; picks free port).
REM Ctrl+C to stop the server.

cd /d "%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0kill-help-server.ps1"

python server.py
