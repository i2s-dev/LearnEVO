# Supporting Subsystems

Status: draft — assembled from filename inventory, JAR contents, help
topics, and string dumps.

These are the EVO features that **aren't modules** but run alongside
them.

## EvoNotes — in-app notes / CRM

| Component | File |
| --------- | ---- |
| Main      | `EvoNotes.RWN` |
| Archive   | `EvoNotesARCH.RWN` |
| Search    | `EvoNoteSearch.RWN` |
| Print     | `EvoNotesPrt.RWN` |
| Report    | `EvoNotesRpt.RWN` |
| Migration | `classic2evonts.DFM` — migrate old "Classic" notes in |
| Entry form | `EVOENOTES.DFM` ("Entering Notes") |
| Context   | `ENPM.DFM` ("Evo Notes:") |
| Per-customer entry | accessible from `T7ARA*` customer forms |

EvoNotes is a per-record, append-only note log. Any master record
(customer, vendor, item, work order, etc.) has an **Evo Notes button**
available — a TAS program call wires the current record's key into
EvoNotes before opening it. The CHM section `using_evo_notes` +
`evo_notes_search` is the user-facing doc.

## EvoScheduler — cron-like scheduler

| Component | File |
| --------- | ---- |
| Main      | `EvoScheduler.RWN` |
| Lightweight | `EvoSched.RWN` |
| Setup     | `EvoSchedSetup.RWN` |
| Auto-MRP  | `AUTOT7MRF.RWN` — scheduler variant of `MR-F` |

The scheduler reads a job table (schedule name, program to run,
start time / interval, next-run date) and invokes target RWN files.
Likely backed by a `BKSCHED*` or similar table. Paired with
`EvoService.RWN` for unattended execution.

## EvoService — Windows service harness

| Component | File | Procs | Purpose |
| --------- | ---- | ----- | ------- |
| Install   | `EvoServiceSetup.RWN` | 49 | Configures service: SMTP email (EMAIL.CFG.SMTP/USER/PASS/EMAIL/NAME), SMTPPORT, ISTS.PATH, ESETTINGS (EvoSettings.INI path); handles 32/64-bit registry (THIRTYTWO/SIXTYFOUR vars) |
| Uninstall | `EvoServiceRemove.RWN` | 18 | Removes service; WHOAMIFULL = full workstation identity; same 32/64-bit registry handling |
| Runner    | `EvoService.RWN` | 27 | Opens ISSCHED + ISREMIND; variables: ISTS.CFG.WTIME (poll wait time in ms), ISTS.CFG.USINI (user.ini path); polls ISSCHED on WTIME interval, dispatches scheduled jobs and processes ISREMIND reminder triggers |

Runs EVO programs as a Windows service so that `EvoScheduler` jobs fire
whether or not a user is logged in. The service itself is a small (27-proc)
tp7runtime process that polls ISSCHED and ISREMIND on a configurable
interval (ISTS.CFG.WTIME). SMTP is configured in Setup so the service can
send reminder/trigger emails without user interaction.

**Service ↔ Scheduler confirmed interaction (Pass 113, 2026-06-19):**

EvoService.RWN is the **single program** that drives BOTH scheduler execution and reminder dispatch:
- Opens `ISSCHED` (scheduled jobs) + `ISREMIND` (reminders) — both tables in same service run
- `SCHED.H` = current ISSCHED record handle (scheduled job being processed)
- `REMIND.H` = current ISREMIND record handle (reminder entry being dispatched)
- `REMREC` / `REMCNTR` = reminder record + loop counter (iterates through pending reminders)
- `PARSTO` = "params store" — holds IS.SCHED.PARAM1..9 values when spawning a job subprocess
- `A.RET` / `A.RET2` = return values from spawned programs (checked for error handling)
- `ISTS.CFG.WTIME` = poll interval in milliseconds (configured at setup time)

EvoSched.RWN (21 procs) is a lightweight standalone variant used for **testing** — opens ISSCHED only (no ISREMIND), polls via ISTS.CFG.PTIME. It is NOT the production service runner.

| Component | Opens | Role |
|-----------|-------|------|
| EvoService.RWN | ISSCHED + ISREMIND | Production service: fires scheduled jobs AND reminder notifications |
| EvoSched.RWN | ISSCHED only | Test runner: fires scheduled jobs only (no reminders) |
| EvoScheduler.RWN (TA-N) | ISSCHED + FILELOC + BKSYMSTR | Admin UI: create/edit/delete ISSCHED job records |
| EvoSchedSetup.RWN | ISREMIND + ISIS + ISLOG | Setup: configures poll interval, email SMTP, ISTS.PATH |
| EvoServiceSetup.RWN | LANGDICT only | Service install: SCM registration, 32/64-bit registry path |
| EvoServiceRemove.RWN | LANGDICT only | Service uninstall: SCM deregistration |

## EvoBackup — built-in backup

| Component | File | Procs | Purpose |
| --------- | ---- | ----- | ------- |
| Main      | `EvoERPbackup.RWN` | 76 | Backup engine with cloud + local modes (see below) |
| Form      | `EvoERPBACKUP.DCY` | — | UI form for backup configuration |

**Confirmed variables (Pass 107):**
- `COMP.TAG` / `COMP.EXT` / `COMP.NAME` — per-company file selection
- `ZIPFILES` / `ZIPNAME` — ZIP archive management (uses `zipdll.dll`)
- `FULLSYSTEM` / `COMPDATA` / `CUSTOM` — three backup scope modes (full system / company data only / custom selection)
- `GLACIERKEY` — AWS Glacier archive key (**cloud backup to AWS confirmed**)
- `GS_ARCH` / `GS_BACKUP` / `GS_NONE` — Glacier storage class flags
- `MON` / `TUE` / ... — day-of-week schedule flags
- `FILELOC` — source file index (used to enumerate all Btrieve files)

EvoERPbackup opens FILELOC (all file paths) and BKSYMSTR (system config) for target
resolution. Output destination: `\\i2s109-solidcrm\Bak Up\` for local or
AWS Glacier for cloud. The `GS_*` variables confirm this is a real supported
backup tier, not a stub.

## EvoDC — Data Collection (shop-floor / handheld)

Distinct subsystem from the DC module docs — these are the *runtime*
infrastructure files:

| Component | File |
| --------- | ---- |
| Main      | `EvoDC.RWN` |
| Main menu | `EvoDCmenu.RWN` / `EvoDCmenu2.RWN` |
| Setup     | `EvoDCsetup.RWN` |
| Demo workstations | `EvoDemoWks.RWN` |
| Mobile setup | `EvoMobilSetup.RWN` / `EvoMobileSetup.RWN` |
| Label tables | `BKDC*` (7 tables, see
  [../03-modules/dc-data-collection/README.md](../03-modules/dc-data-collection/README.md)) |
| Handheld forms | `T7HH*` (44 forms) |

Paired `BKDCLAB` / `BKDCHLAB` / `BKDCPLAB` / `BKDCCLAB` tables store
label designs for wave labels / palette labels / carton labels.
`EvoMobileSetup` is the PDA / RF-barcode-gun client.

## EvoLinks — document attachments

| Component | File | Procs | Purpose |
| --------- | ---- | ----- | ------- |
| Main      | `EvoLinks.RWN` | 156 | Full CRUD for ISLINKS records; entity-aware (resolves BKARCUST/BKAPVEND/BKICMSTR/BKCMACCN for display context) |
| Converter | `EvoLinkCVT.RWN` | 10 | One-time migration of old-format ISLINKS records to current schema |

"Links" are **document attachments** on any record — PDFs, emails, photos.
Stored in `\\…\LinkDoc\` on the share. Help topic `using_evo_links`.

**Confirmed IS.LNK.* fields from EvoLinks.RWN variable list (Pass 107):**
- `IS.LNK.UID` — parent record key (entity this doc is attached to)
- `IS.LNK.LINK` — file path / URL of linked document
- `IS.LNK.APP` — module code owner (`AR`, `PO`, `SO`, etc.)
- `IS.LNK.TYPES` / `IS.LNK.PCB` / `IS.LNK.DEF` — 100-element type-code arrays
- `IS.LNK.GLOBAL` — Y = visible across all companies
- `IS.LNK.OPENWITH` — flag controlling which app opens the file
- `IS.LNK.DATE` — date attached
- `IS.LNK.NOTE` — short description note
- `IS.LNK.WHO` — attached-by user
- `IS.LNK.ATYPE` — attachment type code
- `IS.LNK.EXTRA` — supplemental metadata
- `IS.LNK.PRIVATE` — hidden from other users
- `IS.LNK.SORT` — display order within attachment list
- `IS.LNK.ALPHA` — secondary alpha sort key
- `ALERTS` — notification trigger on document updates
- `LEXIST` — check-if-link-exists flag
- `GEN.ID` — auto-generated ID for new records

ISLINKS schema (311 fields total) is documented in the EvoLinks section below.

## EvoFNO — "Features & Options"

| Component | File |
| --------- | ---- |
| Main      | `EvoFNO.RWN` |
| SO tie-in | `EvoFNOSO.RWN` |
| PO tie-in | `EvoFNOPO.RWN` |
| WO tie-in | `EvoFNOWO.RWN` |

"Features and Options" is EVO's **option-configurator** — the Dell-laptop
"choose your CPU / RAM / screen" style. Help topic
`using_features_and_options_in_sales_orders` + `setting_up_features_and_options`.

## EvoUpdate — in-app updates

| Component | File | Procs | Role |
| --------- | ---- | ----- | ---- |
| Launcher  | `EvoUpdate.RWN` | 9 | Checks for updates via WEBLINK (download URL); reads ISTS.CFG.PASSWD/CFGLVL for auth |
| Schema migrator | `EvoERPupd.RWN` | 77 | Full schema migration engine (see below) |
| Payroll migrator | `EvoPRupd.RWN` | 51 | Payroll-specific migration variant |
| Setup     | `EvoUPDSetup.RWN` | 18 | Configures update path (FILE_NAME, ISTS.PATH) |
| Runtime patcher | `UPDTP7.EXE` | — | Binary executable; patches tp7runtime.exe and related TP7 runtime files (see below) |

**EvoERPupd.RWN is the schema migration engine** (Pass 107). Key variables:
- `FILE_DEF` / `FD_ARRAY` — file definition array (reads FILEDICT/FILEDBF)
- `FLD_NAME` / `FLD_TYPE` / `FLD_SIZE` / `FLD_DEC` / `FLD_ARRAY` — new field spec
- `OLD_FLD_TYPE` / `OLD_FLD_SIZE` / `OLD_FLD_ARRAY` / `OLD_FLD_OFFSET` — current field spec  
- `FLD_OFFSET` / `RESTRUCT_FLD` — field restructure flag: if old ≠ new, restructure Btrieve file
- `UFORCE` / `CLOG` — force-update and change-log flags

The engine reads FILEDICT+FILEDBF+FILEKEY (Pervasive DDF), compares schema against
FILE*.UPD manifests, and restructures Btrieve B-tree files in-place. This is how EVO
adds new fields to existing tables without losing live data.

Pulls new `.RWN`/`.DFM`/`.DCY`/`.RTM` releases from Addsum and applies
them to the share. `.UPD` files carry the DDF schema migrations.

**UPDTP7.EXE — TP7 runtime patcher (Pass 113, 2026-06-19):**
- 32-bit Visual C++ Win32 executable, 85,680 bytes total
- PE code sections end at offset 0xF000; **24,240-byte encrypted overlay** follows
- Overlay bytes start `4A 02 02 02...` — high-frequency 0x02 bytes + scattered strings; cipher not decoded
- The overlay contains the embedded patch payload (replacement runtime files or binary patches)
- Generates a batch script at runtime (`@echo off`, `if not exist X mkdir X`, `attrib +h X`) to create a hidden working directory in %TEMP%
- Uses `CreateProcessA` to launch the generated batch + patched files; `GetTempPathA` for staging area
- Error sentinel: `"Error #bdembed1 -- Quiting"` — "bdembed" = binary/BD embed; fatal if extraction fails
- Two obfuscated directory-name strings in overlay: `DFDHERGDCV` and `DFDHERGGZV` (appear to be encoded temp folder names)
- **Role distinction:** EvoERPupd.RWN handles *Btrieve schema migrations* (table restructures); UPDTP7.EXE handles *tp7runtime.exe binary patching* (replaces the executable itself)

## Evo Notes Search (`EvoNoteSearch`) + Drill-Down (`EvoERPDrillM`)

Cross-record search and drill-down navigation. `EvoERPDrillM.RWN`
provides the "drill into source" feature where you can click a GL
entry and jump back to the originating AP check or AR invoice.
Tables: likely `BKDRILL*` / drill-map tables.

## Calendar + reminders

Help topic `google_calendar`. Files:

- `CALREM.RWN` / `calrem.DFM` — calendar reminder core (142 procs)
- `CALREMGC.DFM` — Google Calendar sync dialog (DFM-only; no separate RWN — sync is invoked from within CALREM.RWN)
- `CALDRILL.DFM` / `CALGRIDDRILL.DFM` / `calDDsel.DFM` — calendar drill-down
- `CALENDARS\` folder on the share — calendar data files

**CALREM.RWN confirmed DB fingerprint (Pass 107, 142 procs):**
Tables: `BKYSMSTR`, `ISREMIND`, `BKARCUST`, `BKAPVEND`, `BKICMSTR`, `BKCMACFC`,
`BKCMACCN`, `BKPSUSER`, `BKSYHELP`, `DBAHLPID`, `TASCOLOR`, `ISLOG`, `ISDRILL`, `MKAHIST`

Key variables: `CAL.DAY`, `CAL.MONTH`, `ENTRY.DATE`, `DATE_TYPE`, `START.DATE`, `CHK.DATE`
— confirms CALREM is a full calendar view that reads ISREMIND entries by date range,
cross-referenced to customers/vendors/items for display context.

No `CALREMGC.RWN` file was found in the 1,122 RWN catalog — Google Calendar sync is
handled inside CALREM.RWN itself (called from the CALREMGC.DFM dialog form).

## Chart demo / reusable charts

- `ChartDemo.DFM`, `chartBarModal.DFM`, `chartLineModal.DFM`,
  `chartPieModal.DFM` — modal chart surfaces callable from any
  program. Wired to the runtime keywords `SET_CHARTDATA`,
  `SET_CHARTCOLOR`, `SET_CHARTSERIESLABEL`, etc.

## CRM Dashboard

`CRMDASHBOARD.RWN` + `CRMDASHBOARD.DFM` — consolidated customer view.

## CashFlow / CommissionRpt / BOMTree / EditBOMTree — EvoPVT.jar launchers

All four are confirmed **EvoPVT.jar launcher stubs** (Pass 107). Each has the same
signature: 26–27 procs, with shared launcher variables:
- `HOST` / `PORT` — Pervasive PSQL connection (server + port for JDBC)
- `TREEDEST` — output destination identifier passed to EvoPVT.jar
- `COMP` — company code
- `JAVA.PATH` / `JAVA.NAME` — path to java.exe and EvoPVT.jar
- `DFM` — DFM filename to load for the UI
- `NOPE` — abort/cancel flag

| Program | DFM | Role | Extra tables opened |
|---------|-----|------|---------------------|
| `BOMTREE.RWN` | `BOMTree.DFM` | Visual BOM tree explorer (read-only) | None beyond launcher set |
| `EDITBOMTREE.RWN` | `EditBOMTree.DFM` | Interactive BOM tree editor | None beyond launcher set |
| `CASHFLOW.RWN` | `CashFlowReport.DFM` | Cash-flow forecast | BKARCUST, BKAPVEND, BKCMACCN, BKICMSTR, ISLINKS, BKAPDESC |
| `COMMISSIONRPT.RWN` | — | Commission report viewer | BKARCUST, BKAPVEND, BKCMACCN, BKICMSTR, ISLINKS, BKAPDESC |
| `CRMDASHBOARD.RWN` | `CRMDASHBOARD.DFM` | CRM customer dashboard | BKARCUST, BKAPVEND, BKCMACCN, BKICMSTR |

The TAS launcher passes HOST/PORT/COMP/TREEDEST to EvoPVT.jar as argv. EvoPVT.jar
opens a JavaFX TabularView/tree-view window connected to the Pervasive PSQL instance.
**Note:** `EVOBSR.RWN` does NOT exist — the "Business Score Report" mentioned in older
docs was an error. The business scoreboard is `EVOBS.RWN` (EVOBS module, opens ISBSF).

## FNO / MRP helpers

- `AUTOT7MRF.RWN` — auto MRP (scheduled)
- `EvoEMTrns.RWN` — email transmissions
- `EvoCSI` — "Check Settings & Info" (likely diagnostic)
- `EvoBS` / `EvoVIEW` — business-status / generic viewer

## EvoNotes — note tables (Pass 106k)

EvoNotes is NOT a single table — each module has its own `*NOTE` table:

| Table | Module | Purpose |
|-------|--------|---------|
| `BKAPNOTE` | AP | AP vendor/transaction notes |
| `BKBMNOTE` | BM | Bill-of-materials notes |
| `BKEDNOTE` | ED | EDI notes |
| `BKQTNOTE` | QT | Quote notes |
| `BKSONOTE` | SO | Sales-order notes |
| `ISANOTES` | IS | General IS notes |
| `ISNOTES` | IS | General notes store |
| `ISSNOTES` | IS | System notes |
| `MKTNOTE` | MKT | Marketing notes |

Standard schema pattern (from `BKAPNOTE` DDF):
```
BKAP_NOTE_SRCH1   STRING  10   — first search key (e.g., vendor code)
BKAP_NOTE_SRCH2   STRING  10   — second search key (e.g., document number)
BKAP_NOTE_DATE    DATE     4   — note date
BKAP_NOTE_ENTBY   STRING  10   — entered-by user
BKAP_NOTE_NOTES_1 STRING  76   — note text line 1
... (additional _NOTES_N lines for continuation)
```
Primary key = SRCH1 + SRCH2 + DATE (composite — allows multiple notes per document).

## EvoScheduler — ISSCHED (confirmed Pass 106f)

Schedule table: `ISSCHED.B` (confirmed in Pass 106f). 24-field schema:
`NAME` (PK) + `DESC` + `PROG` + `CO` + `TYPE` (O/D/W/M) + `DATE` + `TIME` +
`RECUR` + `LOG` + `EXTRA` + `LDATE/LTIME` + `WHO` + `EMAIL` + `PARAM1..9` + `PARAM0`
See `HELP-RESOURCES.md` §AUTO/Batch for the full details.

## EvoLinks — ISLINKS schema (confirmed Pass 106k)

`ISLINKS.B` — 311-field schema (DDF confirmed):

| Field | Size | Meaning |
|-------|------|---------|
| `IS_LNK_UID` | 48 | Parent record key — the EvoERP record this document is attached to |
| `IS_LNK_LINK` | 256 | File path / URL of the linked document |
| `IS_LNK_APP` | 10 | Module code (e.g., `AR`, `PO`, `SO`) that owns this link |
| `IS_LNK_TYPES_1..100` | 1×100 | Array: which of 100 document type codes apply |
| `IS_LNK_PCB_1..100` | 1×100 | Array: "print check box" flags per type code |
| `IS_LNK_DEF_1..100` | 1×100 | Array: default-include flags per type code |
| `IS_LNK_GLOBAL` | 1 | Global flag: `Y` = visible to all companies |
| `IS_LNK_OPENWITH` | 1 | Open-with behavior flag |
| `IS_LNK_DATE` | 4 | Date document was attached |
| `IS_LNK_WHO` | 15 | User who attached it |
| `IS_LNK_ATYPE` | 3 | Attachment type code |
| `IS_LNK_EXTRA` | 100 | Supplemental metadata |
| `IS_LNK_PRIVATE` | 1 | Private flag: hides from other users |
| `IS_LNK_SORT` | 8 (FLOAT) | Sort order within attachment list |

The 100-element arrays (TYPES/PCB/DEF) are TAS `array 100` occurrences — each index
position maps to one of up to 100 configurable document-type categories (e.g., "quote",
"drawing", "PO confirmation"). EvoLinks stores ONE record per attached file, with the
bitmask of applicable types in the array columns.
