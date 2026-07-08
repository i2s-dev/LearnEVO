#Requires -Version 5.1
# EvoERP Frida Test Suite -- interactive step-by-step capture runner.
# Run via START.bat, not by double-clicking this file.

Set-Location $PSScriptRoot

$projectRoot = Split-Path $PSScriptRoot -Parent
$logsDir     = Join-Path $PSScriptRoot "logs"
$testsDir    = Join-Path $PSScriptRoot "tests"

function Write-Header {
    Clear-Host
    Write-Host ""
    Write-Host "  ============================================" -ForegroundColor Cyan
    Write-Host "    EvoERP Frida Test Suite"                   -ForegroundColor Cyan
    Write-Host "  ============================================" -ForegroundColor Cyan
    Write-Host ""
}

function Pause-ForUser {
    param([string]$Message)
    Write-Host ""
    Write-Host "  $Message" -ForegroundColor Yellow
    Write-Host "  Press ENTER when ready..." -ForegroundColor DarkGray
    $null = Read-Host
}

function Get-Timestamp {
    Get-Date -Format "yyyy-MM-dd_HHmm"
}

function Start-FridaScript {
    param([string]$ScriptName, [string]$LogFile, [string]$ExtraArgs = '')
    # /k keeps the window open after exit (success or crash) so errors are readable.
    $cmdLine = "python `"$testsDir\$ScriptName`" --log `"$LogFile`" $ExtraArgs".TrimEnd()
    $proc = Start-Process `
        -FilePath "cmd.exe" `
        -ArgumentList "/k $cmdLine" `
        -WorkingDirectory $projectRoot `
        -PassThru
    return $proc
}

function Stop-FridaScript {
    param($Proc)
    if ($Proc -and -not $Proc.HasExited) {
        Stop-Process -Id $Proc.Id -Force -ErrorAction SilentlyContinue
        Start-Sleep -Milliseconds 500
    }
}

function Show-LogSummary {
    param([string]$LogFile)
    if (-not (Test-Path $LogFile)) {
        Write-Host "  [!] Log file not found: $LogFile" -ForegroundColor Red
        return
    }
    $lines   = Get-Content $LogFile
    $setkeys = @($lines | Where-Object { $_ -match '^--- SetKey|^>>> SetKey' })
    $unknown = @($lines | Where-Object { $_ -match 'UNKNOWN|UNRECOGNIZED' })

    Write-Host ""
    Write-Host "  --- Log Summary ---"                                        -ForegroundColor Green
    Write-Host "  Log saved : $LogFile"                                       -ForegroundColor Green
    Write-Host "  SetKey calls captured : $($setkeys.Count)"                 -ForegroundColor White

    if ($unknown.Count -gt 0) {
        Write-Host "  UNKNOWN KEYS FOUND: $($unknown.Count) line(s)" -ForegroundColor Magenta
        $unknown | ForEach-Object { Write-Host "    $_" -ForegroundColor Magenta }
    } else {
        Write-Host "  No new unknown keys detected." -ForegroundColor DarkGray
    }
    Write-Host ""
}

# ----------------------------------------------------------
#  TEST 01 -- All Twofish Key Capture
# ----------------------------------------------------------
function Run-Test01 {
    Write-Header
    Write-Host "  TEST 01 -- All Twofish Key Capture"                             -ForegroundColor White
    Write-Host "  Captures every SetKey call during EVO boot and login."          -ForegroundColor DarkGray
    Write-Host "  Use this to confirm which keys fire and in what order."         -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  Known keys:"                                                     -ForegroundColor DarkGray
    Write-Host "    K_A  d97f0567...  (unknown purpose)"                          -ForegroundColor DarkGray
    Write-Host "    K_B  a898d21e...  (RWN files)"                                -ForegroundColor DarkGray
    Write-Host "    K_C  507d2b20...  (suwin6.dcy)"                               -ForegroundColor DarkGray
    Write-Host "    K_D  691e8041...  (DCY files)"                                -ForegroundColor DarkGray
    Write-Host ""

    Pause-ForUser "STEP 1: Make sure EvoERP is FULLY CLOSED. Kill evoerp.exe and tp7runtime.exe in Task Manager if running."

    $logFile = Join-Path $logsDir "test01-key-capture-$(Get-Timestamp).txt"
    Write-Host ""
    Write-Host "  [*] Starting capture script..." -ForegroundColor Cyan
    Write-Host "      A separate console window will open showing live output." -ForegroundColor DarkGray
    Write-Host ""
    $proc = Start-FridaScript "01-key-capture.py" $logFile
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP now (StartEvo.exe). The script will auto-attach."

    Pause-ForUser "STEP 3: Log in with your EVO credentials. Wait until the main menu is visible."

    Pause-ForUser "STEP 4: Open 2-3 modules (e.g. Inventory, then Accounts Receivable). Each module load fires hooks."

    Write-Host ""
    Write-Host "  [*] Stopping capture..." -ForegroundColor Cyan
    Stop-FridaScript $proc

    Show-LogSummary $logFile

    Write-Host "  Paste the contents of the log file into the chat when prompted." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  TEST 02 -- K_A File-Open Hook
# ----------------------------------------------------------
function Run-Test02 {
    Write-Header
    Write-Host "  TEST 02 -- K_A File-Open Hook"                                          -ForegroundColor White
    Write-Host "  Watches all file opens alongside SetKey calls."                         -ForegroundColor DarkGray
    Write-Host "  When K_A fires, we see which file was opened just before it."          -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  K_A key: d97f05679438037073c30628734764020859f77e"                     -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  IMPORTANT: K_A fires very early -- at EVO startup, before login."      -ForegroundColor Yellow
    Write-Host "  The script must be running before the EVO window appears."             -ForegroundColor Yellow
    Write-Host ""

    Pause-ForUser "STEP 1: Make sure EvoERP is FULLY CLOSED."

    $logFile = Join-Path $logsDir "test02-ka-file-hook-$(Get-Timestamp).txt"
    Write-Host ""
    Write-Host "  [*] Starting capture script..." -ForegroundColor Cyan
    Write-Host "      A separate console window will open -- watch it for K_A events." -ForegroundColor DarkGray
    Write-Host ""
    $proc = Start-FridaScript "02-ka-file-hook.py" $logFile
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP NOW. The script will auto-attach and watch for K_A."

    Pause-ForUser "STEP 3: Log in with your credentials."

    Pause-ForUser "STEP 4: Open 2-3 modules to trigger additional key loads."

    Write-Host ""
    Write-Host "  [*] Stopping capture..." -ForegroundColor Cyan
    Stop-FridaScript $proc

    Show-LogSummary $logFile

    Write-Host "  Paste the contents of the log file into the chat when prompted." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  TEST 03 -- YN Slot Mapper
# ----------------------------------------------------------
function Run-Test03 {
    Write-Header
    Write-Host "  TEST 03 -- YN Slot Mapper"                                                   -ForegroundColor White
    Write-Host "  Two-pronged attack on the 162 unknown YN[N] <-> ISTS.CFG key mappings."     -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  Prong A: Hook BTRCALLID to capture BKYSMSTR record at startup."             -ForegroundColor DarkGray
    Write-Host "           BKYSMSTR is ~1045 bytes. YN[N] = byte offset 8+N."                 -ForegroundColor DarkGray
    Write-Host "  Prong B: Scan process memory for known key strings (CRHOLD, MRPDAY ...)"    -ForegroundColor DarkGray
    Write-Host "           If found in a table, dump the full 250-entry key list."             -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  NOTE: BTRCALLID is in w3btrv7.dll which only loads when EVO accesses"       -ForegroundColor Yellow
    Write-Host "  the database. The hook will activate once the DLL loads."                   -ForegroundColor Yellow
    Write-Host ""

    Pause-ForUser "STEP 1: Make sure EvoERP is FULLY CLOSED."

    $logFile = Join-Path $logsDir "test03-yn-mapper-$(Get-Timestamp).txt"
    $triggerFile = "$logFile.scan_trigger"

    Write-Host ""
    Write-Host "  [*] Starting capture script..." -ForegroundColor Cyan
    Write-Host "      Watch the separate console window for BKYSMSTR records." -ForegroundColor DarkGray
    Write-Host ""
    $proc = Start-FridaScript "03-yn-slot-mapper.py" $logFile
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP now. The script will auto-attach."

    Pause-ForUser "STEP 3: Log in with your credentials. Watch for BKYSMSTR records in the capture window."

    Pause-ForUser "STEP 4: Open 2-3 modules to capture additional DB reads."

    # Trigger the memory scan
    Write-Host ""
    Write-Host "  [*] Triggering Prong B memory scan..." -ForegroundColor Cyan
    Write-Host "      (watch the capture window -- scan takes 10-30 seconds)" -ForegroundColor DarkGray
    Set-Content -Path $triggerFile -Value "scan" -NoNewline
    Start-Sleep -Seconds 15

    Write-Host ""
    Write-Host "  [*] Stopping capture..." -ForegroundColor Cyan
    Stop-FridaScript $proc
    if (Test-Path $triggerFile) { Remove-Item $triggerFile -Force }

    Show-LogSummary $logFile

    Write-Host "  Paste the contents of the log file into the chat when prompted." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  TEST 04 -- ISTS.CFG Key Collector (pre-attach, EVO must be CLOSED first)
# ----------------------------------------------------------
function Run-Test04 {
    Write-Header
    Write-Host "  TEST 04 -- ISTS.CFG Key Collector"                                          -ForegroundColor White
    Write-Host "  Hooks BTRCALLID before EVO launches; captures ISTS.CFG records"            -ForegroundColor DarkGray
    Write-Host "  as EVO reads them at startup and login."                                   -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  IMPORTANT: EVO must be FULLY CLOSED before starting this test."            -ForegroundColor Yellow
    Write-Host "  The hook must be in place before EVO reads ISTS.CFG at startup."          -ForegroundColor Yellow
    Write-Host ""

    Pause-ForUser "STEP 1: Close EVO completely. Kill evoerp.exe and tp7runtime.exe in Task Manager if running."

    $logFile     = Join-Path $logsDir "test04-ists-cfg-dump-$(Get-Timestamp).txt"
    $triggerFile = "$logFile.dump_trigger"

    Write-Host ""
    Write-Host "  [*] Starting collector -- capture window will open and wait for EVO..." -ForegroundColor Cyan
    Write-Host ""
    $proc = Start-FridaScript "04-ists-cfg-table-dump.py" $logFile "--trigger `"$triggerFile`""
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP (StartEvo.exe). Watch the capture window -- keys will stream in during login."

    Pause-ForUser "STEP 3: Log in with your credentials. Watch the key count climb. Wait until it stops."

    Write-Host ""
    Write-Host "  [*] Requesting dump..." -ForegroundColor Cyan
    Set-Content -Path $triggerFile -Value "dump" -NoNewline
    $proc.WaitForExit(30000) | Out-Null

    if (Test-Path $logFile) {
        $lines    = Get-Content $logFile
        $keyLines = @($lines | Where-Object { $_ -match '^\s+#\s*\d' })
        Write-Host ""
        Write-Host "  --- Capture Summary ---"                              -ForegroundColor Green
        Write-Host "  Log saved    : $logFile"                              -ForegroundColor Green
        Write-Host "  Keys captured: $($keyLines.Count)"                   -ForegroundColor White
    } else {
        Write-Host "  [!] Log not found." -ForegroundColor Red
    }

    if (Test-Path $triggerFile) { Remove-Item $triggerFile -Force }

    Write-Host ""
    Write-Host "  Paste the contents of the log file into the chat." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  TEST 05 -- ISTS.CFG Full Table Walker
# ----------------------------------------------------------
function Run-Test05 {
    Write-Header
    Write-Host "  TEST 05 -- ISTS.CFG Full Table Walker"                                       -ForegroundColor White
    Write-Host "  Hooks BTRCALLID; scans all memory 800ms after BKYSMSTR is read."            -ForegroundColor DarkGray
    Write-Host "  Finds the FULL ISTS.CFG table and maps entry order to YN slots."            -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  IMPORTANT: EVO must be FULLY CLOSED. Start this script first."              -ForegroundColor Yellow
    Write-Host ""

    Pause-ForUser "STEP 1: Make sure EvoERP is FULLY CLOSED."

    $logFile = Join-Path $logsDir "test05-ists-full-$(Get-Timestamp).txt"
    Write-Host ""
    Write-Host "  [*] Starting walker -- capture window will open and wait for EVO..." -ForegroundColor Cyan
    Write-Host ""
    $proc = Start-FridaScript "05-ists-cfg-full-table.py" $logFile
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP now. The hook fires automatically during login."

    Pause-ForUser "STEP 3: Log in. Wait for the scan to complete (watch the capture window)."

    $proc.WaitForExit(120000) | Out-Null

    if (Test-Path $logFile) {
        $lines    = Get-Content $logFile
        $entryLines = @($lines | Where-Object { $_ -match '^\s+\d+\s+[A-Z]' })
        Write-Host ""
        Write-Host "  --- Summary ---"                          -ForegroundColor Green
        Write-Host "  Log saved       : $logFile"              -ForegroundColor Green
        Write-Host "  Table entries   : $($entryLines.Count)"  -ForegroundColor White
    } else {
        Write-Host "  [!] Log not found." -ForegroundColor Red
    }

    Write-Host ""
    Write-Host "  Paste the contents of the log file into the chat." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  TEST 05b -- ISTS.CFG Value Capture (manual trigger)
# ----------------------------------------------------------
function Run-Test05b {
    Write-Header
    Write-Host "  TEST 05b -- ISTS.CFG Value Capture"                                          -ForegroundColor White
    Write-Host "  Captures BKYSMSTR + ISTS.CFG entry values; fires on manual trigger."        -ForegroundColor DarkGray
    Write-Host "  Use after full login to get WOCALC/STDCST/DCSEQ (not just 334 early keys)." -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  IMPORTANT: EVO must be FULLY CLOSED. Start this script first."              -ForegroundColor Yellow
    Write-Host ""

    Pause-ForUser "STEP 1: Make sure EvoERP is FULLY CLOSED."

    $logFile     = Join-Path $logsDir "test05b-value-$(Get-Timestamp).txt"
    $triggerFile = "$logFile.scan_trigger"

    Write-Host ""
    Write-Host "  [*] Starting capture -- window will open and wait for EVO..." -ForegroundColor Cyan
    Write-Host ""
    $proc = Start-FridaScript "05b-ists-cfg-value-capture.py" $logFile "--trigger `"$triggerFile`""
    Start-Sleep -Seconds 1

    Pause-ForUser "STEP 2: Launch EvoERP. Log in FULLY and wait until the main EVO menu is on screen."

    Pause-ForUser "STEP 3: Open WO-A and one other module (e.g. IN-A) so all RWN files are loaded."

    Write-Host ""
    Write-Host "  [*] Firing scan trigger..." -ForegroundColor Cyan
    Set-Content -Path $triggerFile -Value "scan" -NoNewline
    $proc.WaitForExit(120000) | Out-Null

    if (Test-Path $logFile) {
        $lines = Get-Content $logFile
        $tbl   = @($lines | Where-Object { $_ -match '^\s+\d+\s+[A-Z]' })
        Write-Host ""
        Write-Host "  --- Summary ---"                          -ForegroundColor Green
        Write-Host "  Log saved    : $logFile"                  -ForegroundColor Green
        Write-Host "  Table entries: $($tbl.Count)"             -ForegroundColor White
    } else {
        Write-Host "  [!] Log not found." -ForegroundColor Red
    }
    if (Test-Path $triggerFile) { Remove-Item $triggerFile -Force }

    Write-Host ""
    Write-Host "  Paste the log file contents into the chat." -ForegroundColor Yellow
    Pause-ForUser "Press ENTER to return to the menu."
}

# ----------------------------------------------------------
#  MAIN MENU
# ----------------------------------------------------------
while ($true) {
    Write-Header
    Write-Host "  Select a test to run:" -ForegroundColor White
    Write-Host ""
    Write-Host "   1   Key Capture       -- log all Twofish keys during boot/login"               -ForegroundColor Gray
    Write-Host "   2   K_A File Hook     -- identify which file type uses K_A"                    -ForegroundColor Gray
    Write-Host "   3   YN Slot Mapper    -- capture BKYSMSTR record + scan for key strings"       -ForegroundColor Gray
    Write-Host "   4   ISTS.CFG Dump     -- walk in-memory table, extract all key names"          -ForegroundColor Gray
    Write-Host "   5   Full Table Walk   -- dump entire ISTS.CFG table right after BKYSMSTR"      -ForegroundColor Gray
    Write-Host "   5b  Value Capture     -- BKYSMSTR + entry values, manual trigger after login"  -ForegroundColor Gray
    Write-Host "   Q   Quit"                                                                       -ForegroundColor Gray
    Write-Host ""

    $choice = Read-Host "  Choice"

    switch ($choice.Trim().ToUpper()) {
        '1'     { Run-Test01 }
        '2'     { Run-Test02 }
        '3'     { Run-Test03 }
        '4'     { Run-Test04 }
        '5'     { Run-Test05 }
        '5B'    { Run-Test05b }
        'Q'     { Write-Host ""; Write-Host "  Bye." -ForegroundColor DarkGray; Write-Host ""; exit }
        default { Write-Host "  Invalid choice." -ForegroundColor Red; Start-Sleep -Seconds 1 }
    }
}
