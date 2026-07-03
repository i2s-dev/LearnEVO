# EvoERP Architecture — High-Level

Status: draft.

## Product heritage (confirmed from ISDCABOUT.DCY, 2026-06-17)

- **"Evolved from DBA Classic 2004.1"** — EvoERP grew directly out of DBA Manufacturing
  Classic version 2004.1.
- **Copyright: "Evo ~ ERP Copyright © 2007 Evo ERP Inc."** — rebranded/launched ~2007.
- `START_UP.DBA` on the share is the old DBA Classic boot program (TAS Pro 6 compiled),
  containing legacy registration for "American Backplane Inc." (Ser No 75790,
  Exp 12/31/30, 15 users) — the original customer install before i2 Systems.
- `CHMHELP.EVO` = plain-text workstation marker: "EvoHELP now set for this computer".

## Login and startup flow (confirmed from DCY decryption, 2026-06-17)

EvoERP startup sequence (all forms confirmed from decrypted DCY files):

1. `ISSPLASH.DCY` — "Loading Evolution ~ ERP...." splash while runtime initializes
2. `EVOMENU_LOGIN.DCY` — Login dialog: User Name + Password (TTASStrLists hold company/user lists)
   - Password change: `EVOCHANGEPASS.DCY` (requires old password)
   - Admin password reset: `EVORESETPASS.DCY` (no old password required)
3. `EVOMENU_SELCOMP.DCY` — "Choose Company" dropdown
4. `EvoERPmenu.RWN` — builds the module menu tree at runtime into the 8 TTASStrLists in `EVOERPMENU.DCY`
5. Module selected → `EVOMENU_RUNPRG.DCY` dispatches to the target `.RWN` by filename
6. `EVOEXPIRE.DCY` — shown at any login if the annual license is within the warning window

Data Collection login path is separate:
- `EVODC_LOGIN.DCY` — "Evo ~ ERP Hand Held" login form
- `EVODCMENU2.DCY` — 10-slot configurable tile menu (admin assigns programs to tiles)
- `EVODC.DCY` — standard DC menu: Labor/Prod, Prod Only, Labor Only, Part Request, Shift In/Out, Dashboard

License model: **annual subscription**. Warning shown via `EVOEXPIRE.DCY` as expiry approaches.

## System-wide shared dialogs

These forms are reused across all modules — they are loaded by any module that needs them:

| DCY file | Purpose |
|---|---|
| `PRINTTLL.DCY` | Universal print dialog — Print / Preview / Email / File output; auto-email option |
| `NZEMAILTLL.DCY` | Email composition — To/Cc/BCC/Subject/Form; customer+vendor contact grids |
| `NZEDEFS.DCY` | Email default settings (subject template, body, signature, BCC self) |
| `WBKLOOKUP.DCY` | Standard list-picker: Select / Edit / Add / Delete with DataGrid |
| `WBKLUGRID.DCY` | Admin: configure lookup grids (table, form, security level, sort, UDF) |
| `GETALPHAGEN.DCY` | Generic 1-field text input ("Get Alpha General") |
| `T7POPGET.DCY` | Generic 5-field popup input with Lookup button |
| `EVOMESSAGE.DCY` | Single-line message box (modal) |
| `EVOEMSG.DCY` | Broadcast message to all users or a specific user |
| `EVOUSERS.DCY` | Active user list — Logout / Lock logins / Clear / Message / User Count |
| `T7CLOADING.DCY` | "Loading Data" animated spinner (shown during background data fetches) |
| `T7JAVARUN.DCY` | "Java Evo Loading..." wait screen (shown while EvoPVT.jar task runs) |
| `EVOERROR.DCY` | File open error dialog |
| `IMAGEPRINT.DCY` | "Printing Linked Documents" progress (EvoLinks attachment printing) |

## EvoSettings.INI — per-workstation settings file (confirmed 2026-06-17)

Location: `C:\ISTS\EvoSettings.INI` — standard Windows INI format, per workstation.

**Key sections and their meaning:**

`[Users]` — Global user preferences (all users on this workstation):
| Key | Type | Meaning |
|---|---|---|
| `Toolbar` | 0/1 | Toolbar visible/hidden |
| `OpenListINB`, `OpenListSOA`, etc. | 0/1 | Open browse list on module entry |
| `Language` | string | UI language override |
| `Sounds` | `.T.`/`.F.` | Enable sounds (uses TAS Pro boolean syntax) |
| `DefPrinter` | string | Default printer name |
| `DefPrintPath` | string | Default PDF/file output path |
| `Reminder`, `Notification` | `.T.`/`.F.` | Reminder/notification system on/off |
| `RemSeconds` | integer | Reminder check interval in seconds |
| `QuickPrint` | string | Quick-print printer name |
| `CheckForUpdates` | `.T.`/`.F.` | Auto-check for updates on startup |
| `TopMost` | 0/1 | EvoERP window always-on-top |

`[User:USERNAME]` — Per-user overrides (one section per user):
| Key | Meaning |
|---|---|
| `AutoReStartEvoNum` | Module code to auto-open after login |

`[EMAIL CO# <company> User:<username>]` — Per-user, per-company email config:
Fields: `SMTP`, `PORT`, `SEC` (security mode), `EMAIL`, `NAME`, `USER`, `PASS`, `BCC`,
`Subject`, `Body1`–`Body10` (multi-line body template), `Signature1`–`Signature10`,
`Attach Path`, `EFAIL` (email-on-failure), `ECB` (CC business?), `EVB` (vendor BCC?)

`[ARA]`, `[APA]`, `[INA]`, `[INB]`, `[POA]`, `[SOA]`, `[WOA]` — Per-module UI state:
| Key | Meaning |
|---|---|
| `SAVE ACCESS` | 0/1 — whether to remember last-accessed record in this module |
| `EvoorClassicScreen` | empty/value — switch between Evo (modern) and Classic (DBA-era) UI |
| `Converted` | flag — whether the module's data has been migrated to the new format |

`[HOT BUTTONS]` — 6 user-configurable toolbar shortcuts (Program N, Icon N, Hint N):
Each button launches any `.RWN` by filename, shows a custom icon and tooltip.

**Key insight:** Boolean values use TAS Pro's `.T.` / `.F.` syntax even in this plain INI file,
consistent with xBase lineage. Email credentials are stored as plaintext in this file — no encryption.

## DC Module menu structure (confirmed from EVODC.DCY, 2026-06-17)

The Data Collection entry-point menu (EVODC.DCY = TEditForm3) exposes:
- **Labor/Prod.** — combined labor hours + production count entry
- **Prod. Only** — production count entry without labor tracking
- **Labor Only** — time/labor entry without production count
- **Part Request** — material request from an open work order
- **Shift In/Out** — attendance/shift clock in and out
- **Dashboard** — DC overview summary

## View-Only mode (confirmed from EVOVIEW.DCY, 2026-06-17)

EVOVIEW.DCY (TEditForm2) = read-only EvoERP mode. Exposes six modules:
View Inventory, View Work Orders, View Purchase Orders, View Sales Orders,
View Customers, View Vendors. Used for users who need read access only.

## StartEvo.exe — .NET launcher (confirmed 2026-06-18)

`C:\ISTS\StartEvo.exe` is a **.NET assembly** (confirmed from `_CorExeMain` and PDB path
`D:\prog\evoerp\StartEvo\obj\Release\StartEvo.pdb`). It is the true entry-point before
`tp7runtime.exe` is involved.

Key functions extracted from embedded UTF-16 strings:

| Function name | Purpose |
|---|---|
| `DomainAuthenticateAndLaunchEvo` | Active Directory / domain auth before launching |
| `KillEvoProcesses` | Terminates stale evoerp.exe processes on startup |
| `LaunchEvoWithUser` | Spawns `evoerp.exe` (= `tp7runtime.exe`) under the authenticated user |
| `RunTas` | Internal wrapper — calls the TAS runtime with arguments |
| `GetEvoDir` | Reads `DEFAULTPATH` from `taspro7.ini` to find the share path |
| `UpdateIniFile` | Writes back to `taspro7.ini` after user/company selection |
| `ProcessEvoUri` | Handles `evo://` deep-link URIs (e.g. from emails or browsers) |
| `PsqlCommand` / `PsqlConnection` | Directly queries Pervasive PSQL |

**PSQL query from StartEvo.exe:**
```sql
SELECT count(*) FROM tas_menus WHERE menu_name = ? AND program_name = ?
```
DSN used: `Server DSN=EVOADMIN;Host=<server>;Port=<port>` — a Pervasive Server DSN named
"EVOADMIN". This validates which programs a user/license is permitted to run before the
runtime even starts. `tas_menus` is the PSQL SQL engine's view of `BKMENUSU.DBF`
(the xBase menu database — see Menu System section).

**`evo://` URI scheme:** EvoERP registers a custom Windows URI handler so links of the form
`evo://open/<code>` can launch a specific module from outside the application (e.g. from
an email or browser link). StartEvo.exe handles this via `ProcessEvoUri`.

**Deployment:** `robocopy /z /r:10 /w:1` is embedded — used during updates to robustly
copy new RWN/DFM/DCY files to the share with retry.

**INI keys read:** `DEFAULTPATH` and `DFLTCOMPANYCODE` from `taspro7.ini` — the share
root and the last-used company code.

## Local DLL and utility dependencies (Pass 568, 2026-07-03)

Files in `C:\ISTS\` (confirmed via directory listing + binary string analysis):

| File | Size | Identity | Role |
|------|------|----------|------|
| `tp7runtime.exe` | 29.5 MB | TAS Pro 7 runtime interpreter | Runs `.RWN` programs |
| `evoerp.exe` | 29.5 MB | Same binary — alternate name | Identical to tp7runtime.exe |
| `StartEvo.exe` | — | .NET launcher | Domain auth, update check, URI handler |
| `qtintf70.dll` | 4.1 MB | Qt Interface v7.0 | TAS Pro 7 GUI layer (Qt 4.x framework) |
| `c4dll.dll` | 422 KB | **CodeBase DLL v6.5** (Sequiter Software Inc.) | dBASE/xBase file access for `.DBF`+`.MDX` files |
| `unzdll.dll` | 120 KB | TZipMaster unzip DLL | ZIP decompression (EvoBackup restore, update install) |
| `zipdll.dll` | 138 KB | TZipMaster zip DLL | ZIP compression (EvoBackup archive creation) |
| `quricol32.dll` | 223 KB | **Quricol QR Barcode Library** (Serhiy Perevoznyk, libpng-based) | QR code generation; used by IS2DBAR per-item 2D barcode config |
| `robocopy.exe` | 80 KB | Windows Robocopy | Mass file sync during startup / update deployment |
| `PV.EXE` | 61 KB | **Process Viewer v3.11.1.1** (Igor Nys, 2000-2005) | Process management: kill/list/wait for `tp7runtime.exe` |
| `UPDTP7.EXE` | 86 KB | TAS Pro 7 file updater (custom) | Generates batch scripts for targeted file patching |
| `RBDsgnr.exe` | 6.2 MB | Nevrona ReportBuilder Designer | RTM report template editor |

**Key architectural finding:** EvoERP uses TWO database engines simultaneously:
- **Pervasive PSQL / Btrieve** (`btv32.dll` etc.) — for all business data `.B` files
- **CodeBase** (`c4dll.dll`) — for the TAS Pro 7 internal data dictionary files
  (`.DBF`/`.MDX` format): BKMENUSU, filedict, filedfld, fileloc, FILEFAST, OCCURS, etc.

This is why `BKMENUSU` has both a `.B` Btrieve file (for PSQL access) and a `.DBF`/`.MDX`
pair (for direct CodeBase access by the TAS runtime). Both formats are maintained in sync
by the runtime.

## Three-tier view

### Tier 1 — Client (`C:\ISTS\`)

- A **thin client install**. Everything application-specific is on the
  network. Local files are only the runtime, shared DLLs, and a few
  caches.
- Identity per workstation: `WHOAMI.DBA`.
- Personalization: `taspro7.ini`.

### Tier 2 — Shared code + data (`\\i2s109-solidcrm\DBAMFG$\`)

- Compiled program files (`.RWN`, `.RUN`).
- Form layouts (`.DFM`).
- Data dictionaries (`.DCY`).
- Report templates (`.RTM`).
- Actual business data (Btrieve `.B` files, DBFs, `.TXT` exports).
- This share is authoritative for **every user**. All workstations
  read the same menu, forms, and records from here.

### Tier 3 — Runtime / compute

- `tp7runtime.exe` on each workstation is stateless: it interprets
  the RWNs and keeps its session state in memory + on the shared
  files it has open.
- **Concurrency** is handled by the TAS Pro lock model (see `lock N`
  vs. `lock W` in `.SRC`), backed by whatever locking the Btrieve
  engine or the `c4dll` DBF engine provides.

## The "company" concept

EvoERP supports multiple companies on the same installation. Company routing is handled
at the file level (confirmed from `FILELOC.B`, Pass 103d):
- `FILELOC.B` contains 386 table entries × up to 6 companies = 3,613 routing records
- Each row: logical table name → physical file path (with company suffix `.BI2`, `.BAT`, etc.)
- At login, `EVOMENU_SELCOMP.DCY` presents the company list; the runtime then loads
  FILELOC for that company and routes all `open <TABLE>` calls to the correct physical file
- Company codes at i2 Systems: `I2` (production), `AT`, `AB`, `CA`, `IT`, `99` (others)
- The network share subdirectory layout (`evo-ERP\ISTS\`, `2004.1\`, etc.) reflects
  different installation generations, not per-company separation

## Update / deployment

- The presence of `EvoUPDSetup.RWN`, `EvoUpdate.RWN`, `EvoERPupd.RWN`,
  `EvoPRupd.RWN`, plus `.UPD` definition files, indicates an in-app
  update system that pulls new `.RWN`/`.DFM`/`.DCY` files from
  somewhere (likely a vendor-hosted update URL) and replaces them on
  the share.
- `robocopy.exe` ships in `C:\ISTS` — deployments may also use robocopy
  between machines.
- `EvoPVT.jar` suggests a Java-based helper — purpose unknown
  (*open-question*). Could be a print-viewer or a transformer.

## Auxiliary services

- **Scheduler**: `EvoScheduler.RWN`, `EvoSched.RWN`, `EvoSchedSetup.RWN`.
  A cron-like inside the app — runs canned reports or data jobs.
- **Service mode**: `EvoService.RWN`, `EvoServiceSetup.RWN`,
  `EvoServiceRemove.RWN`. A Windows-service harness, probably for
  running the scheduler headless.
- **Notes system**: a cluster of `EvoNotes*.RWN` — internal CRM/notes.
- **Backup**: `EvoERPbackup.RWN` + `zipdll.dll`/`unzdll.dll` + the
  `Recovered\` folder on the network.
- **Mobile / DC (data collection)**: `EvoDC*.RWN`, `EvoMobileSetup.RWN`
  — barcode / handheld workstation support.

## The report pipeline

1. A TAS Pro program (`.RWN`) collects data via `open / find / enter`.
2. It calls a `.RTM` (ReportBuilder) template for formatting.
3. Output goes to a printer (via `GENERIC.CTL`/printer overlay) or to
   PDF (local `PDFS\` then sometimes to the shared `EVOReports\`).
4. **Pass 568 correction:** `PV.EXE` is NOT "PostView" — it is
   **Process Viewer v3.11.1.1** (Igor Nys, 2000-2005), a command-line
   process management utility (`pv -k`, `pv -l`, `pv -p`). Used to
   kill/check/manage `tp7runtime.exe` / `evoerp.exe` processes during
   startup or update. Confirmed from binary string extraction.

## Data model — what I think lives in the Btrieve store

From the `open <table>` statements in `BKAWLB.SRC`:
- `BKARCUST` — AR customer master
- `BKICMSTR` — Inventory-item master (BK)
- `MTICMSTR` — Inventory-item master (MT — second generation)
- `WORKORD` — Work orders
- `BKSYMSTR` — System master (company/user/setup)

Field naming convention: **table-abbreviation-prefix** + dotted name,
e.g. `bksy.comp.name` = `BKSYMSTR.COMPANY.NAME` (logical field inside
the `BKSYMSTR` record).

## Drawing the rest of the owl

Every time I resolve a new `open <tablename>`, I'll add it to the
module docs and eventually produce a `docs/04-data-dictionary/` page
per table with its fields and cross-references.
