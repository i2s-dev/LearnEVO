# EvoERP Workstation Setup Procedure

Status: **partial** — derived from analysis of existing workstation files, registry, and share contents.

Last updated: 2026-07-02 (Pass 564)

---

## Overview

EvoERP uses a thin-client model: almost everything runs from the network share. A workstation
only needs a handful of local files plus the Pervasive SQL client and TAS Pro runtime.

```
Workstation (C:\ISTS\)                 Server (\\i2s109-solidcrm\DBAMFG$\)
─────────────────────────────────      ─────────────────────────────────────
tp7runtime.exe     ← runtime           EvoERPmenu.rwn   ← entry program
StartEvo.exe       ← launcher          T7*.RWN          ← all programs
taspro7.ini        ← path config       T7*.DFM          ← all forms
EvoSettings.INI    ← workstation prefs *.DCY            ← data dictionaries
WHOAMI.DBA         ← identity          *.RTM            ← reports
CHMHELP.EVO        ← CHM installed     *.B              ← business data
EvoHELP.CHM        ← help file
```

---

## Step-by-Step Setup

### 1. Install Pervasive PSQL Client (32-bit)

**Required version:** Pervasive PSQL v11.30 (32-bit) — must match server version.

**Installers available on share:**
```
\\i2s109-solidcrm\DBAMFG$\Pervasive\
  PSQL-Client-11.30.030.000-win.x86.exe   ← base client installer
  PSQLv11Patch_Client_x86.msp              ← client patch
```

Install order: base installer → patch. After installation, the ODBC driver will
appear in Windows ODBC Data Source Administrator as **"Pervasive ODBC Client Interface"**.

The 32-bit client is required because `tp7runtime.exe` is a 32-bit process.

### 2. Register Pervasive ODBC DSN

Open the **32-bit ODBC Data Source Administrator** (`C:\Windows\SysWOW64\odbcad32.exe`) and
create a **System DSN** with these settings:

| Field | Value |
|-------|-------|
| DSN Name | `DBA` |
| Driver | Pervasive ODBC Client Interface |
| Server Name | `i2s109-SOLIDCRM.1583` (server with port suffix) |
| Database Name | `DBA` |
| TCP Port | `1583` |

The `.1583` port suffix in the server name is the Pervasive ODBC Client convention; the
`TCPPort` attribute is set separately but redundantly in the DSN definition.

**Second DSN (ABI, optional):**
Same settings but `DSN Name=ABI DBA`, `Database Name=ABI` — for the legacy ABI company data.

**EVOADMIN DSN (server-side only):**
StartEvo.exe references a DSN named `EVOADMIN` for pre-login access control validation.
This DSN is not found in the workstation ODBC registry — it may be auto-created by
StartEvo.exe at first launch or only registered on the server. Details unconfirmed.

### 3. Create C:\ISTS\ and Copy Runtime

Create `C:\ISTS\` and copy from the workstation distribution (CD, USB, or share):
- `tp7runtime.exe` — TAS Pro 7 runtime interpreter
- `StartEvo.exe` — EvoERP launcher (.NET application)
- `qtintf70.dll` + supporting DLLs — TAS Pro 7 Qt interface
- Runtime support libraries (`.dll` files that ship with TAS Pro 7)
- `robocopy.exe` — ships in C:\ISTS\ (used by update process)

*Note: The exact set of DLLs is inferred from tp7runtime.exe dependencies, not directly cataloged.*

### 4. Configure taspro7.ini

Create or edit `C:\ISTS\taspro7.ini`:

```ini
[Setup]
DataDictPath=\\I2S109-SOLIDCRM\DBAMFG$\
DfltRunPrg=\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn
DefaultPath=\\I2S109-SOLIDCRM\DBAMFG$\
```

- **DataDictPath** — where TAS Pro looks for DDF schema files and other shared assets.
- **DfltRunPrg** — the entry-point program launched at runtime start.
- **DefaultPath** — base path for bare-name program chains (`CALL "T7SOA"` → `\\...\T7SOA.RWN`).

StartEvo.exe also reads `DEFAULTPATH` (mixed case) and `DFLTCOMPANYCODE` from taspro7.ini
for its own pre-launch setup and writes `DFLTCOMPANYCODE` back after user company selection.

### 5. Create WHOAMI.DBA — Workstation Sentinel File

`C:\ISTS\WHOAMI.DBA` exists at `C:\ISTS\WHOAMI.DBA` as a 2-byte CRLF-only file (Pass 112
confirmed: `0x0D 0x0A` only — content is empty). The network share copy is also 2 bytes.

**Role:** Presence-only sentinel — the file's existence signals the workstation is set up.
Content is not read by the runtime; EvoERP functions normally with an empty file.

This parallels `CHMHELP.EVO` (35-byte text sentinel for CHM installation).
The workstation identity is tracked at runtime via `ISLOG` (IS_LOG_WHO field)
and `BKSY.USER.COMP` from login, not from WHOAMI.DBA content.

### 6. Install EvoHELP.CHM

Copy `EvoHELP.CHM` from the share to `C:\ISTS\EvoHELP.CHM`. StartEvo.exe creates
`C:\ISTS\CHMHELP.EVO` (a plain text sentinel file) after successful CHM installation.
Content: `"EvoHELP now set for this computer\r\n"`.

If `CHMHELP.EVO` is missing, StartEvo.exe may prompt to install the CHM.

### 7. evo:// URI Scheme (auto-registered)

StartEvo.exe registers the `evo://` custom URI scheme in the Windows registry at first
run via `ProcessEvoUri`. This allows external links of the form `evo://open/<code>` to
launch a specific EvoERP module from a browser or email. No manual step required.

### 8. EvoSettings.INI (auto-created per workstation)

`C:\ISTS\EvoSettings.INI` is created/updated automatically by EvoERP at runtime.
It stores per-workstation preferences for all users sharing this workstation:

```ini
[General]
; Theme, window positions, etc.

[Users]
; Per-user (by login code) preferences

[EMAIL]
; Email integration settings (SMTP host, port, credentials)

[CALENDAR]
; Calendar/reminder integration settings
```

No manual configuration needed — EvoERP manages this file.

---

## Key Files and Their Locations

| File | Location | Purpose | Configured by |
|------|----------|---------|---------------|
| `taspro7.ini` | `C:\ISTS\` | Share path routing | Manual (setup) |
| `WHOAMI.DBA` | `C:\ISTS\` | Workstation identity | Manual (setup) |
| `EvoSettings.INI` | `C:\ISTS\` | Per-workstation preferences | EvoERP (auto) |
| `CHMHELP.EVO` | `C:\ISTS\` | CHM installation sentinel | StartEvo.exe |
| `EvoHELP.CHM` | `C:\ISTS\` | Integrated help file | Manual (setup) |
| ODBC DSN `DBA` | Windows registry | Pervasive connection | Manual (setup) |

---

## Robocopy-Based Updates

StartEvo.exe uses `robocopy /z /r:10 /w:1` internally to copy updated program files
from the share to local paths during version updates. The `/z` flag = restartable mode
(handles network interruption), `/r:10` = 10 retries, `/w:1` = 1 second wait between retries.

`robocopy.exe` also ships in `C:\ISTS\` for deployment scripting outside of StartEvo.exe.

---

## Multi-Company and Multi-Site

EvoERP supports multiple companies on the same installation. Company routing is handled
server-side via `FILELOC` (Btrieve routing table): the same program code accesses different
`.B` data files depending on the company code in use. No workstation-level company
configuration is needed.

**Terminal Server / Citrix deployment:** Not specifically documented. The thin-client
architecture (all data on share, stateless runtime) is inherently compatible with TS/Citrix
deployments. Each session would need its own WHOAMI.DBA identity (or use a shared one for
all sessions on that host). Specific configuration unknown. C:20/100.

---

**Confidence: 68/100** — taspro7.ini structure fully confirmed; Pervasive client version and
installer paths confirmed; ODBC DSN fields confirmed from registry analysis; WHOAMI.DBA
confirmed as 2-byte CRLF sentinel (presence-only, content unused, C:95); EVOADMIN DSN source
uncertain; exact runtime DLL set not cataloged; CHMHELP.EVO confirmed;
evo:// URI registration confirmed from StartEvo.exe strings.
