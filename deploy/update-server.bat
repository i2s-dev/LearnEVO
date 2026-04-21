@echo off
REM =======================================================================
REM  Load the evo-help image from tar and (re)start the container.
REM  This is the ONLY script that needs to run on i2s111-CTDC4.
REM
REM  Place this file, docker-compose.yml, and evo-help.tar all in the
REM  same folder (e.g. C:\deploy\evo-help\). Then double-click, or:
REM      update-server.bat
REM
REM  First run and every subsequent update use the exact same command.
REM =======================================================================
setlocal
cd /d "%~dp0"

if not exist evo-help.tar (
    echo  evo-help.tar not found in %cd%.
    echo  Copy a fresh tar from the workstation first.
    exit /b 1
)

if not exist docker-compose.yml (
    echo  docker-compose.yml not found in %cd%.
    exit /b 1
)

echo.
echo [1/2] Loading image from evo-help.tar ...
docker load -i evo-help.tar
if errorlevel 1 goto :deploy_failed

echo.
echo [2/2] (Re)creating the container ...
docker compose up -d --force-recreate
if errorlevel 1 goto :deploy_failed

echo.
echo ============================================================
echo  Done.
echo  Service: http://%COMPUTERNAME%:8765/
echo ============================================================
goto :eof

:deploy_failed
echo.
echo  *** DEPLOY FAILED ***
exit /b 1
