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

`taspro7.ini` sets `DfltCompanyCode=` empty and the login program chooses
one. Multiple companies' data likely coexist by being **prefixed** in
the same share, or by sitting in **parallel subdirectories** from
`DefaultPath`. The network share I saw (`\\I2S109-SOLIDCRM`) has
`evo-ERP\ISTS\…` and other top-level dirs — these may be per-company
drops. Confirming this is a **todo**.

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
4. The `PV.EXE` (PostView) tool is available as a print preview /
   viewer for older `.TXT` spools.

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
