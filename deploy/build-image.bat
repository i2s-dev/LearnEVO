@echo off
REM =======================================================================
REM  Build the evo-help Docker image on this workstation and save it to
REM  a tar file ready to ship to i2s111-CTDC4.
REM
REM  Produces:  deploy\evo-help.tar   (~65 MB; not checked into git)
REM
REM  Usage:
REM      deploy\build-image.bat
REM =======================================================================
setlocal
cd /d "%~dp0\.."

echo.
echo  Repo root: %cd%
echo.

echo [1/3] Regenerating help content from docs/ ...
python learnevo-help\build.py
if errorlevel 1 goto :build_failed

echo.
echo [2/3] Building Docker image evo-help:latest ...
docker build -t evo-help:latest .
if errorlevel 1 goto :build_failed

echo.
echo [3/3] Saving image to deploy\evo-help.tar ...
if not exist deploy md deploy
docker save evo-help:latest -o deploy\evo-help.tar
if errorlevel 1 goto :build_failed

echo.
echo ============================================================
echo  Done.
echo  Copy these three files to C:\deploy\evo-help\ on i2s111-CTDC4
echo  (they must all end up in the SAME folder):
echo    deploy\evo-help.tar
echo    docker-compose.yml
echo    deploy\update-server.bat
echo ============================================================
echo.
pause
goto :eof

:build_failed
echo.
echo  *** BUILD FAILED ***
pause
exit /b 1
