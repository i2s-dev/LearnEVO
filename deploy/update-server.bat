@echo off
REM =======================================================================
REM  Load the evo-help image from tar and (re)start the container.
REM  This is the ONLY script that needs to run on i2s-odin.
REM
REM  Place this file, docker-compose.yml, and evo-help.tar all in the
REM  SAME folder (e.g. C:\deploy\evo-help\). Then double-click, or:
REM      update-server.bat
REM
REM  First run and every subsequent update use the exact same command.
REM =======================================================================
setlocal EnableDelayedExpansion
cd /d "%~dp0"

echo.
echo  Working directory: %cd%
echo.

set "MISSING="
if not exist "evo-help.tar"       set "MISSING=!MISSING! evo-help.tar"
if not exist "docker-compose.yml" set "MISSING=!MISSING! docker-compose.yml"

if defined MISSING (
    echo  *** Missing required file(s): !MISSING!
    echo.
    echo  All three files must live in the same folder as this script:
    echo      %cd%
    echo.
    echo  Required:
    echo      docker-compose.yml
    echo      evo-help.tar
    echo      update-server.bat  (this file^)
    echo.
    pause
    exit /b 1
)

where docker >nul 2>&1
if errorlevel 1 (
    echo  *** Docker is not on PATH. Install Docker Desktop / Engine first.
    pause
    exit /b 1
)

echo [1/2] Loading image from evo-help.tar ...
docker load -i evo-help.tar
if errorlevel 1 (
    echo  *** docker load failed.
    pause
    exit /b 1
)

echo.
echo [2/2] (Re)creating the container ...
docker compose up -d --force-recreate
if errorlevel 1 (
    echo  *** docker compose up failed.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Done.
echo  Service:  http://%COMPUTERNAME%:8765/
echo ============================================================
echo.
pause
