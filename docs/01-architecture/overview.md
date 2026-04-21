# EvoERP Architecture — High-Level

Status: draft.

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
