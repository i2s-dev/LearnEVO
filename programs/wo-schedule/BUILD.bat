@echo off
cd /d "%~dp0"

set OUT=C:\ProgramData\i2Systems\Tools\wo-schedule
set EXE64=%OUT%\WO-Schedule.exe
set EXE32=%OUT%\WO-Schedule-x86.exe
set SIGNTOOL=C:\Program Files (x86)\Windows Kits\10\bin\10.0.28000.0\x64\signtool.exe
set PY32=C:\Python312-32\python.exe

echo [1/6] Building 64-bit EXE...
python -m PyInstaller --onefile --windowed --name "WO-Schedule" --distpath "%OUT%" main.py
if errorlevel 1 ( echo BUILD FAILED (64-bit). & pause & exit /b 1 )

echo [2/6] Signing 64-bit EXE...
"%SIGNTOOL%" sign /sha1 B93F080C077A15FBDB3A0850B47429CB142CADF4 /fd SHA256 /tr "http://timestamp.digicert.com" /td SHA256 "%EXE64%"
if errorlevel 1 ( echo SIGNING FAILED (64-bit). & pause & exit /b 1 )

echo [3/6] Verifying 64-bit signature...
"%SIGNTOOL%" verify /pa "%EXE64%"
if errorlevel 1 ( echo VERIFICATION FAILED (64-bit). & pause & exit /b 1 )

echo [4/6] Building 32-bit EXE...
"%PY32%" -m PyInstaller --onefile --windowed --name "WO-Schedule-x86" --distpath "%OUT%" main.py
if errorlevel 1 ( echo BUILD FAILED (32-bit). & pause & exit /b 1 )

echo [5/6] Signing 32-bit EXE...
"%SIGNTOOL%" sign /sha1 B93F080C077A15FBDB3A0850B47429CB142CADF4 /fd SHA256 /tr "http://timestamp.digicert.com" /td SHA256 "%EXE32%"
if errorlevel 1 ( echo SIGNING FAILED (32-bit). & pause & exit /b 1 )

echo [6/6] Verifying 32-bit signature...
"%SIGNTOOL%" verify /pa "%EXE32%"
if errorlevel 1 ( echo VERIFICATION FAILED (32-bit). & pause & exit /b 1 )

echo.
echo Done. Output:
echo   64-bit: %EXE64%
echo   32-bit: %EXE32%
pause
