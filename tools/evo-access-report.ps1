# evo-access-report.ps1
# Queries DSN=DBA (cross-database to EVOB for security tables) and produces:
#   PS-E equivalent — every user and their assigned security level
#   PS-F equivalent — every security level and which users belong to it
#
# Security tables live in the EVOB database (E:\DBAMFG\DEFAULT\ on i2s-evo).
# Business data (DBA = E:\DBAMFG\I2\) is a separate named database.

$timestamp = Get-Date -Format "yyyy-MM-dd_HHmm"
$outDir    = Join-Path $PSScriptRoot "outputs"
$outFile   = Join-Path $outDir "EVO-Access-Report_$timestamp.txt"

if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force $outDir | Out-Null }

$lines = [System.Collections.Generic.List[string]]::new()

function Out-Line {
    param([string]$s = "")
    $lines.Add($s)
    Write-Host $s
}
function Out-Sep {
    param([string]$c = "-", [int]$w = 72)
    Out-Line ($c * $w)
}

Out-Line "EVO USER ACCESS REPORT"
Out-Line ("Generated : " + (Get-Date -Format "yyyy-MM-dd  HH:mm"))
Out-Sep "=" 72
Out-Line ""

# ── Connect ───────────────────────────────────────────────────────────
$conn = New-Object System.Data.Odbc.OdbcConnection("DSN=DBA")
try {
    $conn.Open()
} catch {
    Write-Host ""
    Write-Host "ERROR: Cannot connect to DSN=DBA." -ForegroundColor Red
    Write-Host "       Is the Pervasive SQL service reachable on i2s-evo?" -ForegroundColor Red
    Write-Host ""
    Write-Host $_.Exception.Message
    Write-Host ""
    pause
    exit 1
}

# ── Load all users (from EVOB = DEFAULT directory) ────────────────────
$cmd = $conn.CreateCommand()
$cmd.CommandText = 'SELECT BKPS_USER_CODE, BKPS_USER_SEC, BKPS_USER_MENU FROM "EVOB"..BKPSUSER ORDER BY BKPS_USER_CODE'
$rdr = $cmd.ExecuteReader()
$users = [System.Collections.Generic.List[PSCustomObject]]::new()
while ($rdr.Read()) {
    $users.Add([PSCustomObject]@{
        Code = $rdr["BKPS_USER_CODE"].ToString().Trim()
        Sec  = $rdr["BKPS_USER_SEC"].ToString().Trim()
        Menu = $rdr["BKPS_USER_MENU"].ToString().Trim()
    })
}
$rdr.Close()

# ── Load security level descriptions (from EVOB) ──────────────────────
$cmd2 = $conn.CreateCommand()
$cmd2.CommandText = 'SELECT BKSL_MSTR_LEVEL, BKSL_MSTR_DESC FROM "EVOB"..BKSLMSTR ORDER BY BKSL_MSTR_LEVEL'
$rdr2 = $cmd2.ExecuteReader()
$levelMap = @{}
while ($rdr2.Read()) {
    $levelMap[$rdr2["BKSL_MSTR_LEVEL"].ToString().Trim()] = $rdr2["BKSL_MSTR_DESC"].ToString().Trim()
}
$rdr2.Close()

$conn.Close()

# ── PS-E: every user ──────────────────────────────────────────────────
Out-Line "PS-E  —  ALL USERS AND THEIR SECURITY LEVEL"
Out-Sep
Out-Line ("{0,-18} {1,-10} {2,-6} {3}" -f "USER CODE", "SEC LEVEL", "MENU#", "LEVEL DESCRIPTION")
Out-Sep "-" 72

foreach ($u in $users) {
    $desc = if ($levelMap.ContainsKey($u.Sec)) { $levelMap[$u.Sec] } else { "(not in BKSLMSTR)" }
    Out-Line ("{0,-18} {1,-10} {2,-6} {3}" -f $u.Code, $u.Sec, $u.Menu, $desc)
}

Out-Line ""
Out-Line ("Total users: " + $users.Count)
Out-Line ""
Out-Line ""

# ── PS-F: every security level with its users ─────────────────────────
Out-Line "PS-F  —  ALL SECURITY LEVELS AND USERS ASSIGNED TO EACH"
Out-Sep

$byLevel    = $users | Group-Object -Property Sec | Sort-Object Name
$usedLevels = [System.Collections.Generic.HashSet[string]]::new()

foreach ($grp in $byLevel) {
    $code = $grp.Name
    $usedLevels.Add($code) | Out-Null
    $desc = if ($levelMap.ContainsKey($code)) { $levelMap[$code] } else { "(not in BKSLMSTR)" }
    Out-Line ""
    Out-Line ("  LEVEL $code  —  $desc")
    foreach ($u in ($grp.Group | Sort-Object Code)) {
        Out-Line ("      $($u.Code)  (menu set: $($u.Menu))")
    }
}

foreach ($lvl in ($levelMap.Keys | Sort-Object)) {
    if (-not $usedLevels.Contains($lvl)) {
        Out-Line ""
        Out-Line ("  LEVEL $lvl  —  $($levelMap[$lvl])")
        Out-Line "      (no users assigned)"
    }
}

Out-Line ""
Out-Sep "=" 72
Out-Line ("Users: " + $users.Count + "    Levels defined: " + $levelMap.Count)
Out-Line ""
Out-Line "NOTE: To see which specific menu items each level can access,"
Out-Line "      run PS-E or PS-F from within EVO (Password Security menu)."

# ── Save ──────────────────────────────────────────────────────────────
$lines | Out-File -FilePath $outFile -Encoding utf8
Write-Host ""
Write-Host ("Report saved: $outFile") -ForegroundColor Green
Write-Host ""

# SIG # Begin signature block
# MIIfqgYJKoZIhvcNAQcCoIIfmzCCH5cCAQExDzANBglghkgBZQMEAgEFADB5Bgor
# BgEEAYI3AgEEoGswaTA0BgorBgEEAYI3AgEeMCYCAwEAAAQQH8w7YFlLCE63JNLG
# KX7zUQIBAAIBAAIBAAIBAAIBADAxMA0GCWCGSAFlAwQCAQUABCD6wGJMzHXxySum
# ZdTXKarPGfbcxbeCymxkbYL/MGG+r6CCGLowggV8MIIDZKADAgECAhAuHOQL/XxG
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
# MC8GCSqGSIb3DQEJBDEiBCBibZXVlI3YTYUKxmvBqtQsJ2AIpBhRLlMUq4yPHTs+
# lDANBgkqhkiG9w0BAQEFAASCAgCRcU+m5/viAagV6BNUnz1tTKjJHWJnNU99/juk
# 33pOVLIKJ0n4cjvTZ3Y72xUsKLKt/jlP4jW2PXrroUsG/Cp9x3lAweFEFIQrhA+O
# Cnth86kJQ6lW1QqM6hN20k9U23GouLJxS0mTqovTlj6RP4yT+7LHGRCkwbrU1xZf
# A9CUjuKN8m7ldYhFo15ZXFYz3GKP+zlzcwTVJzOSsHOIiVSLlmdqjqmx3Q7n8CaZ
# 3EhIyTIBlrBIEcdEJ7V+C6MgfM6zCDDFdCrGk2VT3jMvgrYHcJPSbdFIw9AMNgiG
# u4bNQ2BOEjS2eSGgSVfs9WvUfw0rZ3JljmXCZHN4AzRvZgC1Wpjx037oJ5A/hRf0
# sHfBOqC1cBA4KYkAMGquBuIOxPJs+DihWQfyJxxVz7EOHPHwtjHnf60wcaeAMBn+
# Rxh8kjXdPBK00Gr5SobgoqNaQXNJz/nABF6wAEuPDTUJP/si/rFYzm3u7OMGEABK
# 7L8KIHTL/hA5+HCj3a1CZ+18hhMZS6rbbYN24cmc0EnGJLKkS7UrJzZZbJ2RMzLz
# YjRat8ykRcWPiRMoRbdR8cdtPhPeOly/XJ5u5ttn9KbHOih2MnNfg/KA710M/NYj
# FceYPTqfDvSYZj5U1I307N4VynYLH8CkH++MnJo2VpbOhk1nFMGRg6qT2S69CTBW
# Trcu3qGCAyYwggMiBgkqhkiG9w0BCQYxggMTMIIDDwIBATB9MGkxCzAJBgNVBAYT
# AlVTMRcwFQYDVQQKEw5EaWdpQ2VydCwgSW5jLjFBMD8GA1UEAxM4RGlnaUNlcnQg
# VHJ1c3RlZCBHNCBUaW1lU3RhbXBpbmcgUlNBNDA5NiBTSEEyNTYgMjAyNSBDQTEC
# EAqA7xhLjfEFgtHEdqeVdGgwDQYJYIZIAWUDBAIBBQCgaTAYBgkqhkiG9w0BCQMx
# CwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0yNjA4MTIxODQ5NTdaMC8GCSqG
# SIb3DQEJBDEiBCD8hXUDXpLZ5l0DH1oXFeevTwRuKL8IWWlX5E+yab6xRjANBgkq
# hkiG9w0BAQEFAASCAgCQkTY3w8PqGL4ovS7zZGr9TJbc95/UxiNOr9oDqovwvoEI
# r19m17EfmXhX9J9RFF+FNEKoFGSpUQQ3/GceQKDSrZkuvVCA8EnePemDHjT3+u0L
# O82nrf8Nxjpwb58qj+a6RtHnSBhJRheMxZcUq01wIPIOMs/L7yYtE8rz82l/mKQN
# GlCjc6J7jNATE+vVKoZiS3VTilnF+AxlC6R5ZS8JWc+DMV7WhW19gxED/d9KUqud
# DT8LBWntZGsZCTJZqfgAvgDEVahVre7MRIvsch6RcBPx0GWmit3ImaUSGx5Zw4Dm
# HvUFIo6ZdJrcmKvxLts6P54Ok5C06xok88dMz4DNxA2xGzCWGbU2vZENK30j3mbR
# qCXVtQ9XO1Uu8ggK0S8kF43KhzTysPK9dBw/dngIQmzZDn4usSqpC6hChFehPYX5
# mLOPEdcrPFUFCrBm/scI4MzrsiieoGTcjbm+XrMLzYDi3T7bIUmvFDh2RoynCBop
# 53FbcXVIVRkkLWvwZUw9gxD4pEhVIEhyh8KD6VR8b4xYUOFIs3b6IltZmL1NYbgT
# +qr51INbYDeNI8zsTEWF5PMw60RBQwsVFCF05tK2308M9zvXcG9M1om56tP/8TuH
# Yvq0WcM6NnFU/wmQCVoR3kxM+M4RJ9Qlhy6kZ0PPvTswnWF8I4m8iOQB0U7kAA==
# SIG # End signature block
