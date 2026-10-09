# EvoWindowManager.ps1 — Manage EVO form window positions and sizes
# Registry: HKCU\Software\Addsum\TAS Pro 7\Form Loc Size Storage

# When running as .ps1 directly, self-elevate if not admin.
# When compiled to .exe by ps2exe, $PSCommandPath is null — skip this block entirely;
# the -RequireAdmin EXE manifest already handles UAC elevation.
if ($PSCommandPath -and
    -not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
        [Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell.exe "-ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

$ErrorActionPreference = 'Stop'

try {

Add-Type -AssemblyName System.Windows.Forms

Add-Type -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;

public class EvoWM {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left, Top, Right, Bottom; }

    [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc f, IntPtr lp);
    [DllImport("user32.dll")] public static extern int  GetWindowText(IntPtr h, StringBuilder s, int n);
    [DllImport("user32.dll")] public static extern int  GetWindowTextLength(IntPtr h);
    [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
    [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
    [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);

    public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);

    public static List<IntPtr> GetVisibleWindows(uint pid) {
        var list = new List<IntPtr>();
        EnumWindows((h, lp) => {
            uint p; GetWindowThreadProcessId(h, out p);
            if (p == pid && IsWindowVisible(h) && GetWindowTextLength(h) > 0)
                list.Add(h);
            return true;
        }, IntPtr.Zero);
        return list;
    }
}
'@

# ── Constants ──────────────────────────────────────────────────────────────
$REG_BASE   = 'HKCU:\Software\Addsum\TAS Pro 7\Form Loc Size Storage'
$SWP_NOSIZE = 0x0001
$SWP_NOMOVE = 0x0002
$SWP_NOZORDER = 0x0004

# ── Coordinate helpers ─────────────────────────────────────────────────────

function ConvertTo-SignedCoord([long]$raw) {
    $bytes = [BitConverter]::GetBytes([uint32]($raw -band 0xFFFFFFFF))
    return [BitConverter]::ToInt32($bytes, 0)
}

function ConvertTo-DWord([int]$signed) {
    $bytes = [BitConverter]::GetBytes([int32]$signed)
    return [BitConverter]::ToUInt32($bytes, 0)
}

# ── Monitor helpers ────────────────────────────────────────────────────────

function Get-PrimaryBounds {
    return [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
}

function Get-MonitorForWindow([IntPtr]$hwnd) {
    $rect = New-Object EvoWM+RECT
    [EvoWM]::GetWindowRect($hwnd, [ref]$rect) | Out-Null
    $cx = ($rect.Left + $rect.Right)  / 2
    $cy = ($rect.Top  + $rect.Bottom) / 2
    foreach ($scr in [System.Windows.Forms.Screen]::AllScreens) {
        if ($scr.Bounds.Contains($cx, $cy)) { return $scr.Bounds }
    }
    return Get-PrimaryBounds
}

function Get-CenterCoords([int]$monLeft, [int]$monTop, [int]$monW, [int]$monH, [int]$winW, [int]$winH) {
    return @{
        Left = $monLeft + [int](($monW - $winW) / 2)
        Top  = $monTop  + [int](($monH - $winH) / 2)
    }
}

# ── Window enumeration ─────────────────────────────────────────────────────

function Get-LiveEvoWindows {
    $proc = Get-Process -Name evoerp -ErrorAction SilentlyContinue
    if (-not $proc) { return @() }

    $handles = [EvoWM]::GetVisibleWindows([uint32]$proc.Id)
    $idx = 1
    $result = @()
    foreach ($h in $handles) {
        $sb = New-Object System.Text.StringBuilder(512)
        [EvoWM]::GetWindowText($h, $sb, 512) | Out-Null
        $title = $sb.ToString()
        if (-not $title) { continue }

        $rect = New-Object EvoWM+RECT
        [EvoWM]::GetWindowRect($h, [ref]$rect) | Out-Null

        $result += [PSCustomObject]@{
            Index  = $idx
            HWND   = $h
            Title  = $title
            Left   = $rect.Left
            Top    = $rect.Top
            Width  = $rect.Right  - $rect.Left
            Height = $rect.Bottom - $rect.Top
        }
        $idx++
    }
    return $result
}

# ── Registry helpers ───────────────────────────────────────────────────────

function Get-RegEntries {
    if (-not (Test-Path $REG_BASE)) { return @() }
    $entries = @()
    Get-ChildItem $REG_BASE | ForEach-Object {
        try {
            $v = Get-ItemProperty $_.PSPath
            $entries += [PSCustomObject]@{
                Name    = $_.PSChildName
                RegPath = $_.PSPath
                Top     = ConvertTo-SignedCoord $v.Top
                Left    = ConvertTo-SignedCoord $v.Left
                Width   = [int]$v.Width
                Height  = [int]$v.Height
            }
        } catch { }
    }
    return $entries
}

function Find-RegEntry($win, $regEntries) {
    # Match by stored position (EVO writes position on close; matches on open)
    $byPos = $regEntries | Where-Object { $_.Left -eq $win.Left -and $_.Top -eq $win.Top } | Select-Object -First 1
    if ($byPos) { return $byPos }

    # Fallback: match by module code in title (e.g. "IN-A" -> T7INA-*)
    if ($win.Title -match '^([A-Z]{2,4})-([A-Z])\s') {
        $code = 'T7' + $Matches[1] + $Matches[2]
        return $regEntries | Where-Object { $_.Name -like "$code-$code" } | Select-Object -First 1
    }
    if ($win.Title -match 'Evo.*ERP|EVO.*ERP') {
        return $regEntries | Where-Object { $_.Name -eq 'EVOERPMENU-EVOERPMENU' } | Select-Object -First 1
    }
    return $null
}

function Write-RegPosition($regPath, [int]$left, [int]$top) {
    Set-ItemProperty -Path $regPath -Name 'Left' -Value (ConvertTo-DWord $left) -Type DWord
    Set-ItemProperty -Path $regPath -Name 'Top'  -Value (ConvertTo-DWord $top)  -Type DWord
}

function Write-RegSize($regPath, [int]$width, [int]$height) {
    Set-ItemProperty -Path $regPath -Name 'Width'  -Value ([uint32]$width)  -Type DWord
    Set-ItemProperty -Path $regPath -Name 'Height' -Value ([uint32]$height) -Type DWord
}

# ── Live window operations ─────────────────────────────────────────────────

function Move-EvoWindow($hwnd, [int]$left, [int]$top) {
    [EvoWM]::SetWindowPos($hwnd, [IntPtr]::Zero, $left, $top, 0, 0,
        ($SWP_NOSIZE -bor $SWP_NOZORDER)) | Out-Null
    [EvoWM]::SetForegroundWindow($hwnd) | Out-Null
}

function Resize-EvoWindow($hwnd, [int]$width, [int]$height) {
    [EvoWM]::SetWindowPos($hwnd, [IntPtr]::Zero, 0, 0, $width, $height,
        ($SWP_NOMOVE -bor $SWP_NOZORDER)) | Out-Null
}

# ── Auto-size helper (70% of monitor, centered) ────────────────────────────

function Get-AutoSizeAndCenter($monBounds) {
    $w = [int]($monBounds.Width  * 0.70)
    $h = [int]($monBounds.Height * 0.70)
    $l = $monBounds.Left + [int](($monBounds.Width  - $w) / 2)
    $t = $monBounds.Top  + [int](($monBounds.Height - $h) / 2)
    return @{ Left = $l; Top = $t; Width = $w; Height = $h }
}

# ── Actions ────────────────────────────────────────────────────────────────

function Action-CenterWindow($win, $regEntries) {
    $mon    = Get-MonitorForWindow $win.HWND
    $center = Get-CenterCoords $mon.Left $mon.Top $mon.Width $mon.Height $win.Width $win.Height
    Move-EvoWindow $win.HWND $center.Left $center.Top

    $reg = Find-RegEntry $win $regEntries
    if ($reg) {
        Write-RegPosition $reg.RegPath $center.Left $center.Top
        Write-Host "  Centered on current monitor. Registry updated." -ForegroundColor Green
    } else {
        Write-Host "  Centered on current monitor. (No registry key matched — live only.)" -ForegroundColor Yellow
    }
}

function Action-ResizeWindow($win, $regEntries) {
    Write-Host "  Current size: $($win.Width) x $($win.Height)"
    $w = Read-Host '  New width '
    $h = Read-Host '  New height'
    [int]$iw = $w.Trim(); [int]$ih = $h.Trim()
    Resize-EvoWindow $win.HWND $iw $ih

    $reg = Find-RegEntry $win $regEntries
    if ($reg) {
        Write-RegSize $reg.RegPath $iw $ih
        Write-Host "  Resized to ${iw}x${ih}. Registry updated." -ForegroundColor Green
    } else {
        Write-Host "  Resized to ${iw}x${ih}. (No registry key matched — live only.)" -ForegroundColor Yellow
    }
}

function Action-ResetPosition($win, $regEntries) {
    $mon    = Get-PrimaryBounds
    $center = Get-CenterCoords $mon.Left $mon.Top $mon.Width $mon.Height $win.Width $win.Height
    Move-EvoWindow $win.HWND $center.Left $center.Top

    $reg = Find-RegEntry $win $regEntries
    if ($reg) {
        Write-RegPosition $reg.RegPath $center.Left $center.Top
        Write-Host "  Moved to center of primary monitor. Registry updated." -ForegroundColor Green
    } else {
        Write-Host "  Moved to center of primary monitor. (No registry key matched — live only.)" -ForegroundColor Yellow
    }
}

function Action-ResetSize($win, $regEntries) {
    # Auto-size: 70% of primary monitor, centered — applied immediately to live window
    $mon  = Get-PrimaryBounds
    $auto = Get-AutoSizeAndCenter $mon
    Move-EvoWindow   $win.HWND $auto.Left $auto.Top
    Resize-EvoWindow $win.HWND $auto.Width $auto.Height

    $reg = Find-RegEntry $win $regEntries
    if ($reg) {
        Remove-Item -Path $reg.RegPath -Force
        Write-Host "  Live window: $($auto.Width)x$($auto.Height), centered on primary. Registry key deleted (EVO resets on next open)." -ForegroundColor Green
    } else {
        Write-Host "  Live window: $($auto.Width)x$($auto.Height), centered on primary. (No registry key found — EVO will create one on next close.)" -ForegroundColor Green
    }
}

# ── All-windows (0) actions ─────────────────────────────────────────────────

function Action-CenterAll($liveWindows, $regEntries) {
    $mon = Get-PrimaryBounds
    foreach ($win in $liveWindows) {
        $center = Get-CenterCoords $mon.Left $mon.Top $mon.Width $mon.Height $win.Width $win.Height
        Move-EvoWindow $win.HWND $center.Left $center.Top
    }
    foreach ($reg in $regEntries) {
        $center = Get-CenterCoords $mon.Left $mon.Top $mon.Width $mon.Height $reg.Width $reg.Height
        Write-RegPosition $reg.RegPath $center.Left $center.Top
    }
    Write-Host "  Centered $($liveWindows.Count) live windows and $($regEntries.Count) registry entries on primary monitor." -ForegroundColor Green
}

function Action-ResizeAll($liveWindows, $regEntries) {
    $w = Read-Host '  New width  (applies to all)'
    $h = Read-Host '  New height (applies to all)'
    [int]$iw = $w.Trim(); [int]$ih = $h.Trim()
    foreach ($win in $liveWindows) { Resize-EvoWindow $win.HWND $iw $ih }
    foreach ($reg in $regEntries)  { Write-RegSize $reg.RegPath $iw $ih }
    Write-Host "  Resized $($liveWindows.Count) live windows and $($regEntries.Count) registry entries to ${iw}x${ih}." -ForegroundColor Green
}

function Action-ResetPositionAll($regEntries) {
    $mon = Get-PrimaryBounds
    foreach ($reg in $regEntries) {
        $center = Get-CenterCoords $mon.Left $mon.Top $mon.Width $mon.Height $reg.Width $reg.Height
        Write-RegPosition $reg.RegPath $center.Left $center.Top
    }
    Write-Host "  Reset position of all $($regEntries.Count) registry entries to primary monitor center." -ForegroundColor Green
    Write-Host "  Takes effect the next time each EVO form is opened." -ForegroundColor Gray
}

function Action-ResetSizeAll($liveWindows, $regEntries) {
    $confirm = Read-Host "  Auto-size all live windows (70% of primary) and delete all registry entries. Type YES to confirm"
    if ($confirm -ne 'YES') { Write-Host "  Cancelled." -ForegroundColor Gray; return }

    $mon  = Get-PrimaryBounds
    $auto = Get-AutoSizeAndCenter $mon
    foreach ($win in $liveWindows) {
        Move-EvoWindow   $win.HWND $auto.Left $auto.Top
        Resize-EvoWindow $win.HWND $auto.Width $auto.Height
    }
    foreach ($reg in $regEntries) { Remove-Item -Path $reg.RegPath -Force }
    Write-Host "  $($liveWindows.Count) live windows auto-sized to $($auto.Width)x$($auto.Height) and centered." -ForegroundColor Green
    Write-Host "  $($regEntries.Count) registry entries deleted. EVO will write fresh entries on next close." -ForegroundColor Green
}

# ── Main loop ──────────────────────────────────────────────────────────────

while ($true) {
    Clear-Host
    Write-Host '============================================================' -ForegroundColor Cyan
    Write-Host '  EVO Window Manager' -ForegroundColor Cyan
    Write-Host '============================================================' -ForegroundColor Cyan
    Write-Host ''

    $liveWindows = Get-LiveEvoWindows
    $regEntries  = Get-RegEntries

    # Window list
    if ($liveWindows.Count -eq 0) {
        Write-Host '  [EVO is not running — registry-only actions available]' -ForegroundColor Yellow
        Write-Host ''
    } else {
        Write-Host '  OPEN EVO WINDOWS' -ForegroundColor White
        Write-Host '  ─────────────────────────────────────────────────────'
        Write-Host ('  {0,-3}  {1}' -f '0', 'All windows')
        foreach ($w in $liveWindows) {
            Write-Host ('  {0,-3}  {1}' -f $w.Index, $w.Title)
            Write-Host ('       Pos: {0},{1}   Size: {2}x{3}' -f $w.Left, $w.Top, $w.Width, $w.Height) -ForegroundColor DarkGray
        }
        Write-Host ''
    }

    # Action list
    Write-Host '  ACTIONS' -ForegroundColor White
    Write-Host '  ─────────────────────────────────────────────────────'
    Write-Host '  a   Center Window        (on its current monitor)'
    Write-Host '  b   Resize Window        (enter width and height)'
    Write-Host '  c   Reset Position       (move to primary monitor center)'
    Write-Host '  d   Auto-size & Reset     (resize live window to 70% of primary, delete registry key)'
    Write-Host ''
    Write-Host '  q   Quit'
    Write-Host ''
    Write-Host '  Type a window number + action.  Examples: 1a  2b  0c' -ForegroundColor DarkGray
    Write-Host '  "0" applies the action to all windows / all registry entries.' -ForegroundColor DarkGray
    Write-Host ''

    $cmd = (Read-Host '  Command').Trim().ToLower()

    if ($cmd -eq 'q') { break }

    if ($cmd -notmatch '^(\d+)([a-d])$') {
        Write-Host '  Invalid — use <number><letter>, e.g. 1a or 0c' -ForegroundColor Red
        Start-Sleep -Seconds 2
        continue
    }

    $winNum = [int]$Matches[1]
    $action = $Matches[2]

    Write-Host ''

    if ($winNum -eq 0) {
            switch ($action) {
                'a' { Action-CenterAll        $liveWindows $regEntries }
                'b' { Action-ResizeAll        $liveWindows $regEntries }
                'c' { Action-ResetPositionAll $regEntries }
                'd' { Action-ResetSizeAll     $liveWindows $regEntries }
            }
        } else {
            $win = $liveWindows | Where-Object { $_.Index -eq $winNum } | Select-Object -First 1
            if (-not $win) {
                Write-Host "  Window #$winNum not found." -ForegroundColor Red
                Start-Sleep -Seconds 2
                continue
            }
            switch ($action) {
                'a' { Action-CenterWindow  $win $regEntries }
                'b' { Action-ResizeWindow  $win $regEntries }
                'c' { Action-ResetPosition $win $regEntries }
                'd' { Action-ResetSize     $win $regEntries }
            }
        }

    Write-Host ''
    Write-Host '  Press any key to continue...' -ForegroundColor DarkGray
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}

Write-Host ''
Write-Host '  EVO Window Manager closed.' -ForegroundColor Cyan
Write-Host ''

} catch {
    Write-Host ''
    Write-Host "  ERROR: $_" -ForegroundColor Red
    Write-Host '  Press any key to exit...' -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}
# SIG # Begin signature block
# MIIfqgYJKoZIhvcNAQcCoIIfmzCCH5cCAQExDzANBglghkgBZQMEAgEFADB5Bgor
# BgEEAYI3AgEEoGswaTA0BgorBgEEAYI3AgEeMCYCAwEAAAQQH8w7YFlLCE63JNLG
# KX7zUQIBAAIBAAIBAAIBAAIBADAxMA0GCWCGSAFlAwQCAQUABCBYpucL+bvP31Iz
# LWTZVvHFIunY9v2qb5ivUOUYsFWN4qCCGLowggV8MIIDZKADAgECAhAuHOQL/XxG
# jUrls+iOrpM3MA0GCSqGSIb3DQEBCwUAMFYxCzAJBgNVBAYTAlVTMQswCQYDVQQI
# DAJDVDEPMA0GA1UEBwwGTW9ycmlzMRMwEQYDVQQKDAppMiBTeXN0ZW1zMRQwEgYD
# VQQDDAtpMlRTaW5jbGFpcjAeFw0yNjA1MjIxOTE5NDVaFw0zNjA1MjIxOTI5NDVa
# MFYxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDVDEPMA0GA1UEBwwGTW9ycmlzMRMw
# EQYDVQQKDAppMiBTeXN0ZW1zMRQwEgYDVQQDDAtpMlRTaW5jbGFpcjCCAiIwDQYJ
# KoZIhvcNAQEBBQADggIPADCCAgoCggIBAOCPn2MroOMIMkmy7ulBPA30+wmBK+o3
# 8uxm2tkcRalfWpd1A1iPcz+GRjpYctKkwOSAA3lAS4o+yUiYQDk42doTxavSwd+G
# 2rcKwglVtJRnbcB6jnXoP5k9VKu3/qbGX+h+nyDsnidOkcsdVV5Feae0qNmGDszq
# BpqYvxoaTzzlaHZBZDQprqYJUoNFCoE1TMQK6p/i2CoVxziQjkA7wtGncxyChK7m
# o64kVRO+/DRBQryFQfn6UX8zxaEwMvqsvlz3rwQ4I5w0eB/Qp07eXrI8uSctAzk7
# L6PgG/9NoNbuuwA38YS64LIRhfkvGTEfqcm68RKYj3JBwESrlybMGjp6hthX5IzM
# WjiScTpw02deFzNErzKf1EFXWHH5xeYUebR90tZFzilofh3etKdURsSoHw74o1kp
# hIWcBdTvnDDREwCA5oSV+Ff3OMbkWp8+Y0sE8iGV600FjMGlUcev42405eiDPgcV
# gbZ24e1JBiuTlRh4UNEwjyqCOuo44diZpvbDHhc/1mH8ZPkOdku+F/dHY78TZW1m
# dS7lr5p41/2+cuDR8erYG5n4bHgVmwiOSFG8fnaeH132cAv9QEOz88Mrfst2gpPb
# 5y0qRc73EtxmpvvM4t1qeJkMeNUdYJYy9EdrEp/IrHzwSSjJAdhLcBHPH2wmLZhl
# HoYbwumowTIlAgMBAAGjRjBEMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggr
# BgEFBQcDAzAdBgNVHQ4EFgQULv4aiViHkBG9pm1bwAS6V8y1F5kwDQYJKoZIhvcN
# AQELBQADggIBAF4C1hF1dsOZoMuA2B9wfB8Ukqpha9h5S3gN+R3Gkw5rA9VzY1te
# ZITZtUXrHajCZOH8WV45LleidyOsZF0tJavS6Ho0YBKybD62tWP6/pTapzZttQG8
# VkFDlkEsGmBYLpel+yJQ5ZGZk0/swwZiCKqTIgu2kXrAk9kb72ikQimSLliOST1t
# Ew0q5PmHpqz5HCieTSp+jfoDhfzaJtIhtjJHb8ponIANReDJDVx6JdoI/r6BQTv/
# WAIVB+Rgci26mRdaC1ABIciP4EIph/mMHVpc3op+330Q0JF5FK0SCNTIffQrfdhh
# BXvPFWZOQXiEVm5hawltoQo1yi/nGhrnPDYJVBXZ0Ro+fcfL6Ev9aC7wH88yiBhV
# xYkaLMPk7yrmoD8sP79Um6mSfyTlDZPsVBEv0E9OFvc7wJ3F5LwOjW8xsAJskKd/
# Ie2KotkuN6L225unSRfv/0wOpUlbD8UNN2n5jpSb6zjo7ucBh1mZlH2G4KgdGQGX
# 3y0KM8ffXvjvHIi5rJSf3wdj0pXvbdjb5UrjjdjIRJJhM/A6lGgRoblSf/fgmv/y
# Vts24NEy2cUrESN1ni1ICWWr+aK5vMb9aKIreJgBLde3A3dP3JG+AXDbZi99DPaj
# UfcmeFIT1K2hu9prmkqMPeLVgBpG6MxNeTRBEcI1DN11CqT9wlpf8iFtMIIFjTCC
# BHWgAwIBAgIQDpsYjvnQLefv21DiCEAYWjANBgkqhkiG9w0BAQwFADBlMQswCQYD
# VQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGln
# aWNlcnQuY29tMSQwIgYDVQQDExtEaWdpQ2VydCBBc3N1cmVkIElEIFJvb3QgQ0Ew
# HhcNMjIwODAxMDAwMDAwWhcNMzExMTA5MjM1OTU5WjBiMQswCQYDVQQGEwJVUzEV
# MBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29t
# MSEwHwYDVQQDExhEaWdpQ2VydCBUcnVzdGVkIFJvb3QgRzQwggIiMA0GCSqGSIb3
# DQEBAQUAA4ICDwAwggIKAoICAQC/5pBzaN675F1KPDAiMGkz7MKnJS7JIT3yithZ
# wuEppz1Yq3aaza57G4QNxDAf8xukOBbrVsaXbR2rsnnyyhHS5F/WBTxSD1Ifxp4V
# pX6+n6lXFllVcq9ok3DCsrp1mWpzMpTREEQQLt+C8weE5nQ7bXHiLQwb7iDVySAd
# YyktzuxeTsiT+CFhmzTrBcZe7FsavOvJz82sNEBfsXpm7nfISKhmV1efVFiODCu3
# T6cw2Vbuyntd463JT17lNecxy9qTXtyOj4DatpGYQJB5w3jHtrHEtWoYOAMQjdjU
# N6QuBX2I9YI+EJFwq1WCQTLX2wRzKm6RAXwhTNS8rhsDdV14Ztk6MUSaM0C/CNda
# SaTC5qmgZ92kJ7yhTzm1EVgX9yRcRo9k98FpiHaYdj1ZXUJ2h4mXaXpI8OCiEhtm
# mnTK3kse5w5jrubU75KSOp493ADkRSWJtppEGSt+wJS00mFt6zPZxd9LBADMfRyV
# w4/3IbKyEbe7f/LVjHAsQWCqsWMYRJUadmJ+9oCw++hkpjPRiQfhvbfmQ6QYuKZ3
# AeEPlAwhHbJUKSWJbOUOUlFHdL4mrLZBdd56rF+NP8m800ERElvlEFDrMcXKchYi
# Cd98THU/Y+whX8QgUWtvsauGi0/C1kVfnSD8oR7FwI+isX4KJpn15GkvmB0t9dmp
# sh3lGwIDAQABo4IBOjCCATYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQU7Nfj
# gtJxXWRM3y5nP+e6mK4cD08wHwYDVR0jBBgwFoAUReuir/SSy4IxLVGLp6chnfNt
# yA8wDgYDVR0PAQH/BAQDAgGGMHkGCCsGAQUFBwEBBG0wazAkBggrBgEFBQcwAYYY
# aHR0cDovL29jc3AuZGlnaWNlcnQuY29tMEMGCCsGAQUFBzAChjdodHRwOi8vY2Fj
# ZXJ0cy5kaWdpY2VydC5jb20vRGlnaUNlcnRBc3N1cmVkSURSb290Q0EuY3J0MEUG
# A1UdHwQ+MDwwOqA4oDaGNGh0dHA6Ly9jcmwzLmRpZ2ljZXJ0LmNvbS9EaWdpQ2Vy
# dEFzc3VyZWRJRFJvb3RDQS5jcmwwEQYDVR0gBAowCDAGBgRVHSAAMA0GCSqGSIb3
# DQEBDAUAA4IBAQBwoL9DXFXnOF+go3QbPbYW1/e/Vwe9mqyhhyzshV6pGrsi+Ica
# aVQi7aSId229GhT0E0p6Ly23OO/0/4C5+KH38nLeJLxSA8hO0Cre+i1Wz/n096ww
# epqLsl7Uz9FDRJtDIeuWcqFItJnLnU+nBgMTdydE1Od/6Fmo8L8vC6bp8jQ87PcD
# x4eo0kxAGTVGamlUsLihVo7spNU96LHc/RzY9HdaXFSMb++hUD38dglohJ9vytsg
# jTVgHAIDyyCwrFigDkBjxZgiwbJZ9VVrzyerbHbObyMt9H5xaiNrIv8SuFQtJ37Y
# OtnwtoeW/VvRXKwYw02fc7cBqZ9Xql4o4rmUMIIGtDCCBJygAwIBAgIQDcesVwX/
# IZkuQEMiDDpJhjANBgkqhkiG9w0BAQsFADBiMQswCQYDVQQGEwJVUzEVMBMGA1UE
# ChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSEwHwYD
# VQQDExhEaWdpQ2VydCBUcnVzdGVkIFJvb3QgRzQwHhcNMjUwNTA3MDAwMDAwWhcN
# MzgwMTE0MjM1OTU5WjBpMQswCQYDVQQGEwJVUzEXMBUGA1UEChMORGlnaUNlcnQs
# IEluYy4xQTA/BgNVBAMTOERpZ2lDZXJ0IFRydXN0ZWQgRzQgVGltZVN0YW1waW5n
# IFJTQTQwOTYgU0hBMjU2IDIwMjUgQ0ExMIICIjANBgkqhkiG9w0BAQEFAAOCAg8A
# MIICCgKCAgEAtHgx0wqYQXK+PEbAHKx126NGaHS0URedTa2NDZS1mZaDLFTtQ2oR
# jzUXMmxCqvkbsDpz4aH+qbxeLho8I6jY3xL1IusLopuW2qftJYJaDNs1+JH7Z+Qd
# SKWM06qchUP+AbdJgMQB3h2DZ0Mal5kYp77jYMVQXSZH++0trj6Ao+xh/AS7sQRu
# QL37QXbDhAktVJMQbzIBHYJBYgzWIjk8eDrYhXDEpKk7RdoX0M980EpLtlrNyHw0
# Xm+nt5pnYJU3Gmq6bNMI1I7Gb5IBZK4ivbVCiZv7PNBYqHEpNVWC2ZQ8BbfnFRQV
# ESYOszFI2Wv82wnJRfN20VRS3hpLgIR4hjzL0hpoYGk81coWJ+KdPvMvaB0WkE/2
# qHxJ0ucS638ZxqU14lDnki7CcoKCz6eum5A19WZQHkqUJfdkDjHkccpL6uoG8pbF
# 0LJAQQZxst7VvwDDjAmSFTUms+wV/FbWBqi7fTJnjq3hj0XbQcd8hjj/q8d6ylgx
# CZSKi17yVp2NL+cnT6Toy+rN+nM8M7LnLqCrO2JP3oW//1sfuZDKiDEb1AQ8es9X
# r/u6bDTnYCTKIsDq1BtmXUqEG1NqzJKS4kOmxkYp2WyODi7vQTCBZtVFJfVZ3j7O
# gWmnhFr4yUozZtqgPrHRVHhGNKlYzyjlroPxul+bgIspzOwbtmsgY1MCAwEAAaOC
# AV0wggFZMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFO9vU0rp5AZ8esri
# kFb2L9RJ7MtOMB8GA1UdIwQYMBaAFOzX44LScV1kTN8uZz/nupiuHA9PMA4GA1Ud
# DwEB/wQEAwIBhjATBgNVHSUEDDAKBggrBgEFBQcDCDB3BggrBgEFBQcBAQRrMGkw
# JAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBBBggrBgEFBQcw
# AoY1aHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0VHJ1c3RlZFJv
# b3RHNC5jcnQwQwYDVR0fBDwwOjA4oDagNIYyaHR0cDovL2NybDMuZGlnaWNlcnQu
# Y29tL0RpZ2lDZXJ0VHJ1c3RlZFJvb3RHNC5jcmwwIAYDVR0gBBkwFzAIBgZngQwB
# BAIwCwYJYIZIAYb9bAcBMA0GCSqGSIb3DQEBCwUAA4ICAQAXzvsWgBz+Bz0RdnEw
# vb4LyLU0pn/N0IfFiBowf0/Dm1wGc/Do7oVMY2mhXZXjDNJQa8j00DNqhCT3t+s8
# G0iP5kvN2n7Jd2E4/iEIUBO41P5F448rSYJ59Ib61eoalhnd6ywFLerycvZTAz40
# y8S4F3/a+Z1jEMK/DMm/axFSgoR8n6c3nuZB9BfBwAQYK9FHaoq2e26MHvVY9gCD
# A/JYsq7pGdogP8HRtrYfctSLANEBfHU16r3J05qX3kId+ZOczgj5kjatVB+NdADV
# ZKON/gnZruMvNYY2o1f4MXRJDMdTSlOLh0HCn2cQLwQCqjFbqrXuvTPSegOOzr4E
# Wj7PtspIHBldNE2K9i697cvaiIo2p61Ed2p8xMJb82Yosn0z4y25xUbI7GIN/TpV
# fHIqQ6Ku/qjTY6hc3hsXMrS+U0yy+GWqAXam4ToWd2UQ1KYT70kZjE4YtL8Pbzg0
# c1ugMZyZZd/BdHLiRu7hAWE6bTEm4XYRkA6Tl4KSFLFk43esaUeqGkH/wyW4N7Oi
# gizwJWeukcyIPbAvjSabnf7+Pu0VrFgoiovRDiyx3zEdmcif/sYQsfch28bZeUz2
# rtY/9TCA6TD8dC3JE3rYkrhLULy7Dc90G6e8BlqmyIjlgp2+VqsS9/wQD7yFylIz
# 0scmbKvFoW2jNrbM1pD2T7m3XDCCBu0wggTVoAMCAQICEAqA7xhLjfEFgtHEdqeV
# dGgwDQYJKoZIhvcNAQELBQAwaTELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDkRpZ2lD
# ZXJ0LCBJbmMuMUEwPwYDVQQDEzhEaWdpQ2VydCBUcnVzdGVkIEc0IFRpbWVTdGFt
# cGluZyBSU0E0MDk2IFNIQTI1NiAyMDI1IENBMTAeFw0yNTA2MDQwMDAwMDBaFw0z
# NjA5MDMyMzU5NTlaMGMxCzAJBgNVBAYTAlVTMRcwFQYDVQQKEw5EaWdpQ2VydCwg
# SW5jLjE7MDkGA1UEAxMyRGlnaUNlcnQgU0hBMjU2IFJTQTQwOTYgVGltZXN0YW1w
# IFJlc3BvbmRlciAyMDI1IDEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoIC
# AQDQRqwtEsae0OquYFazK1e6b1H/hnAKAd/KN8wZQjBjMqiZ3xTWcfsLwOvRxUwX
# cGx8AUjni6bz52fGTfr6PHRNv6T7zsf1Y/E3IU8kgNkeECqVQ+3bzWYesFtkepEr
# vUSbf+EIYLkrLKd6qJnuzK8Vcn0DvbDMemQFoxQ2Dsw4vEjoT1FpS54dNApZfKY6
# 1HAldytxNM89PZXUP/5wWWURK+IfxiOg8W9lKMqzdIo7VA1R0V3Zp3DjjANwqAf4
# lEkTlCDQ0/fKJLKLkzGBTpx6EYevvOi7XOc4zyh1uSqgr6UnbksIcFJqLbkIXIPb
# cNmA98Oskkkrvt6lPAw/p4oDSRZreiwB7x9ykrjS6GS3NR39iTTFS+ENTqW8m6TH
# uOmHHjQNC3zbJ6nJ6SXiLSvw4Smz8U07hqF+8CTXaETkVWz0dVVZw7knh1WZXOLH
# gDvundrAtuvz0D3T+dYaNcwafsVCGZKUhQPL1naFKBy1p6llN3QgshRta6Eq4B40
# h5avMcpi54wm0i2ePZD5pPIssoszQyF4//3DoK2O65Uck5Wggn8O2klETsJ7u8xE
# ehGifgJYi+6I03UuT1j7FnrqVrOzaQoVJOeeStPeldYRNMmSF3voIgMFtNGh86w3
# ISHNm0IaadCKCkUe2LnwJKa8TIlwCUNVwppwn4D3/Pt5pwIDAQABo4IBlTCCAZEw
# DAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU5Dv88jHt/f3X85FxYxlQQ89hjOgwHwYD
# VR0jBBgwFoAU729TSunkBnx6yuKQVvYv1Ensy04wDgYDVR0PAQH/BAQDAgeAMBYG
# A1UdJQEB/wQMMAoGCCsGAQUFBwMIMIGVBggrBgEFBQcBAQSBiDCBhTAkBggrBgEF
# BQcwAYYYaHR0cDovL29jc3AuZGlnaWNlcnQuY29tMF0GCCsGAQUFBzAChlFodHRw
# Oi8vY2FjZXJ0cy5kaWdpY2VydC5jb20vRGlnaUNlcnRUcnVzdGVkRzRUaW1lU3Rh
# bXBpbmdSU0E0MDk2U0hBMjU2MjAyNUNBMS5jcnQwXwYDVR0fBFgwVjBUoFKgUIZO
# aHR0cDovL2NybDMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0VHJ1c3RlZEc0VGltZVN0
# YW1waW5nUlNBNDA5NlNIQTI1NjIwMjVDQTEuY3JsMCAGA1UdIAQZMBcwCAYGZ4EM
# AQQCMAsGCWCGSAGG/WwHATANBgkqhkiG9w0BAQsFAAOCAgEAZSqt8RwnBLmuYEHs
# 0QhEnmNAciH45PYiT9s1i6UKtW+FERp8FgXRGQ/YAavXzWjZhY+hIfP2JkQ38U+w
# tJPBVBajYfrbIYG+Dui4I4PCvHpQuPqFgqp1PzC/ZRX4pvP/ciZmUnthfAEP1HSh
# TrY+2DE5qjzvZs7JIIgt0GCFD9ktx0LxxtRQ7vllKluHWiKk6FxRPyUPxAAYH2Vy
# 1lNM4kzekd8oEARzFAWgeW3az2xejEWLNN4eKGxDJ8WDl/FQUSntbjZ80FU3i54t
# px5F/0Kr15zW/mJAxZMVBrTE2oi0fcI8VMbtoRAmaaslNXdCG1+lqvP4FbrQ6IwS
# BXkZagHLhFU9HCrG/syTRLLhAezu/3Lr00GrJzPQFnCEH1Y58678IgmfORBPC1JK
# kYaEt2OdDh4GmO0/5cHelAK2/gTlQJINqDr6JfwyYHXSd+V08X1JUPvB4ILfJdmL
# +66Gp3CSBXG6IwXMZUXBhtCyIaehr0XkBoDIGMUG1dUtwq1qmcwbdUfcSYCn+Own
# cVUXf53VJUNOaMWMts0VlRYxe5nK+At+DI96HAlXHAL5SlfYxJ7La54i71McVWRP
# 66bW+yERNpbJCjyCYG2j+bdpxo/1Cy4uPcU3AWVPGrbn5PhDBf3Froguzzhk++am
# i+r3Qrx5bIbY3TVzgiFI7Gq3zWcxggZGMIIGQgIBATBqMFYxCzAJBgNVBAYTAlVT
# MQswCQYDVQQIDAJDVDEPMA0GA1UEBwwGTW9ycmlzMRMwEQYDVQQKDAppMiBTeXN0
# ZW1zMRQwEgYDVQQDDAtpMlRTaW5jbGFpcgIQLhzkC/18Ro1K5bPojq6TNzANBglg
# hkgBZQMEAgEFAKCBhDAYBgorBgEEAYI3AgEMMQowCKACgAChAoAAMBkGCSqGSIb3
# DQEJAzEMBgorBgEEAYI3AgEEMBwGCisGAQQBgjcCAQsxDjAMBgorBgEEAYI3AgEV
# MC8GCSqGSIb3DQEJBDEiBCDLt+1xsWCaKqGk0OIpwoWDhCpoSgdEHGBWJJB7Rx59
# AzANBgkqhkiG9w0BAQEFAASCAgCsoSwtx5VTo4mNDR+yJUmwVVrKvNwWT1Wr7cLJ
# oPw4159bcmCWLCjOKHwnFKPpUezNkYk6KoCUStdv3l3G+nQzL6pmtLBgWx10G+Tn
# cAG1Wrjra9jtNZv8R7X7MaHlqJsk2Eq5uTL2cbYKTA+PbOBEInzYOjuduzcaFj+5
# p7eg0gEgeaAkjzhS3aH8q8NJynBCcG1dDbqalGgIZ5LMMteeTxkK0OPcpeMn6yHX
# BcsZzmw/zGSHd+83gjrBLoikXykWAlvpBpY8ajaDB7e61hbzuvznjh5EQytgmy24
# XB0oln7Cmwzi1xJKveSblh9t7D0MQbOhDFRZNrC+cZz3wxa1pmcvQ35oon/tuL2Q
# Tn/Cxr1fZeZ5EYhXEu4exfrPp6hG8XhGd8/wAUQgwIzyH/7xUexIHfglY858+nqO
# MzK8cW/HnSf8J8XQMTD4dgIdHoOXHf5a1oF2wHLqDhKfg6hUExFsUp12FVgiplzK
# Ixoa7Hk1v4NOyzxSXW1SgrwjucFSiofMNeZh+CqjlPECVhp9PighQtLUY/Py/2jy
# wVYvWSlGXSITPz52GhJbO7a2KmzCeFJKUEnxY3pMHwyw8YKPyBiS8XJAgIiisLyF
# MnR3j8fPnr9CE1EZFri+OSKXMT1GmGgYRV4L+VR3HqgTAXRClAVuOfR7uHBShnxx
# siSeRqGCAyYwggMiBgkqhkiG9w0BCQYxggMTMIIDDwIBATB9MGkxCzAJBgNVBAYT
# AlVTMRcwFQYDVQQKEw5EaWdpQ2VydCwgSW5jLjFBMD8GA1UEAxM4RGlnaUNlcnQg
# VHJ1c3RlZCBHNCBUaW1lU3RhbXBpbmcgUlNBNDA5NiBTSEEyNTYgMjAyNSBDQTEC
# EAqA7xhLjfEFgtHEdqeVdGgwDQYJYIZIAWUDBAIBBQCgaTAYBgkqhkiG9w0BCQMx
# CwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0yNjA4MjcxNzE0MjhaMC8GCSqG
# SIb3DQEJBDEiBCD6hPSUUYfJrpiKrMAd46f5mTGeqoGrYlyf7hu3F4qxuTANBgkq
# hkiG9w0BAQEFAASCAgBgfOQjFLeGdupynhAPi8Dv8Ys9Xy7b/swp0Akao42U7SQJ
# pRmIF7bfioyFFUjQcEer2PqQFQVlmW+hSbIShyASB/lT07AyCq5O0LS3vaIzBwbv
# w/88ykwEQEppKWx0l47PV21iczsqWH790N5ORnIuBFbJvDyno4Kg/K2zIX9IAPNS
# dNbQrjx8IbgtplQBJiRT4k8C7A91jzzVDySashehkznX7Fdxay/67yb6KElmWfU8
# r5wnp++rc4N34CIH9NzOalLnuQTnfZ6u6PfAp17abgLLoKX3sSV7hVBsIspxk3hE
# N0vN1vfse+j+Cp9u1gt13U8kXmU6TH15H9WFyZWvInmcoGVxd4MrWlHolzN9ZbOl
# 8etzY3wf7KO0LW1Zng+Ai1ns0V/QQGPRLUftAodHb/R6l9NX2S9fecppMTAuzqiS
# SExehhF5MB8GsyFUsbV+FDxS4OSePiyXrGem6B1IQcvvkYJ+uhVDfU7PXuGqi52z
# G0q5wfdBiAYnBqlhlRzeOkRH1+9ORxU9pikEBb8J7ME7HMfX3uRwxOhSmQzgKbq9
# cj9Tsu3AkwaHaH4A1lU4bQcCP3w8Wtdqu97S9o7nRQ60ENmvUwaDgH807jFOFACv
# gbsKpISsI+BLPz1RUgTzH+bdA8mO6uaUbwuF22d+dEzX0emAA62VrG8OqXI8yg==
# SIG # End signature block
