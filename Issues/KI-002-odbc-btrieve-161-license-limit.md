# KI-002 — ODBC (DSN=DBA) queries fail with Btrieve Error 161 (license/session limit)

Status: FIXED on this PC (other PCs unchecked)
Date: 2026-10-12

## Symptom
Read-only pyodbc query against `DSN=DBA` (`SELECT ... FROM WOMAT WHERE WOMAT_WOPRE=? AND WOMAT_WOSUF=?`)
fails at SQLPrepare:

    [Zen][ODBC Engine Interface][Data Record Manager]A key has reached a maximum limit for user count,
    session count, or data in use, or has changed state to expired or disabled.(Btrieve Error 161)
    Unable to open table: WOMAT.

Connection itself succeeds and catalog calls (`cursor.columns(table='WOMAT')`) work; opening the table fails.

## Root cause (CONFIRMED 2026-10-12)
NOT a license problem on i2s-evo. The **64-bit** `DBA` system DSN
(`HKLM\SOFTWARE\ODBC\ODBC.INI\DBA`) still has `ServerName=i2s109-solidcrm.1583` (old server,
192.168.0.239). Only the 32-bit DSN (WOW6432Node) was repointed to `i2s-evo.1583`.
64-bit Python (pyodbc) uses the 64-bit DSN -> connects to the OLD server, which is still powered on
and answering on TCP 1583; its Zen license was moved to i2s-evo, so its engine refuses to open
tables -> Error 161.

Verified: clilcadm -i on i2s-evo = all keys Active (20 + 30x1 user-count increases = 50 users;
leftover expired temporary key 9/20/2026 is harmless). bmon snapshot on i2s-evo = 9 users in use,
peak 10, max 50.

## Attempts
1. 2026-10-12 — query WOMAT for 56273-22 / 56268-8 / 55553-1 / 55968-1 → Error 161.
2. 2026-10-12 — immediate retry → Error 161 (no change).

## Next steps / workaround
- Check Zen Control Center / License Administrator on i2s-evo for seat count in use vs licensed and key state.
- Retry when fewer EVO users are logged in.
- Fallback: check the data in EVO itself (WO-A → Material Issues button).

## Lesson
Every ODBC session consumes a Zen license seat; workspace tools (programs/, ad-hoc queries) can be
blocked during busy hours.

## Workaround / fix
- Workaround (works now): DSN-less connection string
  `Driver={Pervasive ODBC Interface};ServerName=i2s-evo.1583;DBQ=DBA;`
- Fix: change 64-bit DSN ServerName to `i2s-evo.1583` (needs local admin on each PC); also
  power off / retire i2s109-solidcrm so stale DSNs fail loudly instead of returning Error 161.
- Caveat found while testing: WORKORD's ODBC DDF definition decodes garbage (MTWO_WIP_WOPRE as
  ~1e+189 floats) - do not trust WORKORD via ODBC until the DDF is checked.

## Fix applied 2026-10-12 (this PC: I21988t)
User confirmed i2s109-solidcrm is retired — DO NOT USE. Via elevated script:
- `HKLM\SOFTWARE\ODBC\ODBC.INI\DBA` ServerName `i2s109-solidcrm.1583` -> `i2s-evo.1583`
- Driver `C:\Program Files\Actian\PSQL\bin\odbcci64.dll` (missing) -> `C:\Program Files\Actian\Zen\bin\odbcci64.dll`
Verified: `DSN=DBA` from 64-bit Python returns WOMAT rows from i2s-evo (55968-1 = 106 rows).
Other PCs may still have the stale 64-bit DSN — check `HKLM\SOFTWARE\ODBC\ODBC.INI\DBA` on each.
Lesson: a server migration must update BOTH the 32-bit (WOW6432Node) and 64-bit DSNs.
