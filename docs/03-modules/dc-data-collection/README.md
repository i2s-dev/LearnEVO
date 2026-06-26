# Data Collection (Shop Floor) (DC)

Status: verified | Pass 338 (2026-06-26)

- **Module code**: `DC`
- **Tables**: 7 (prefixes `BKDC`) + 4 auxiliary (BKCPMSTR, BKPRINFO, ISWOEX, ISNCR)
- **UI forms**: 26 (prefixes `T7DC`, `T6DC`, `EVODC`)
- **Menu operations**: 9 core (DC-A through DC-I, no DC-J) + DC-K/L/M/N T7-only

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 14 help topics from `EvoHELP.CHM` (overview + DC-A through DC-N,
13 programs — no DC-J). Hoists the three-modes model (Labor+Production
/ Production Only / Labor Only), shift/buffer/lunch handling, and
the multi-WO auto-close/reopen behavior into a shared "Design model"
section, then documents each program's specific behavior + setup-flag
tie-ins. Cross-linked to WO, SH, JC, PR modules and into the shop-
floor hardware / barcode setup notes.

## Menu operations

> ⚠️ **Pass 338 corrections** (2026-06-26): DC-A, DC-B, DC-C, DC-H were wrong or missing in prior auto-generated table. TAS6 BKDC*.RUN binaries are authoritative.

| Code | Operation | TAS6 file(s) | T7 file(s) | Notes |
| ---- | --------- | ------------ | ---------- | ----- |
| `DC-A` | **Enter Labor/Production** *(was "Print Transfer Labels" — wrong)* | BKDCA, BKDCA2~1 | T7DCA, T7DCA2 | Three-mode entry: Labor+Production / Production Only / Labor Only |
| `DC-B` | **Enter Production Only** *(was missing)* | BKDCB (8KB dispatch→BKDCA) | — | Dispatch stub calling BKDCA in Production-only mode |
| `DC-C` | **Enter Labor Only** *(was missing)* | BKDCC (9KB dispatch→BKDCA) | — | Dispatch stub calling BKDCA in Labor-only mode |
| `DC-D` | View/Print Labor Status | BKDCD | T7DCD | Also exports to CheckMark Payroll (identical logic to WO-L-E); BKHLAB=history access |
| `DC-E` | Print Labor Tickets | BKDCE | T7DCE | Uses bkdce.rtm report template |
| `DC-F` | Print Employee Tickets | BKDCF | T7DCF | Uses bkdcf.rtm report template |
| `DC-G` | Edit Labor Transactions | BKDCG, BKDCGMSG | T7DCG | Edit/Delete only — "cannot Add Labor records with this program, use DC-A/B/C"; BKDCGMSG = message-display variant for scanner terminals |
| `DC-H` | **Post Labor Transactions** *(was "Filelock on TOOL -" — garbled)* | BKDCH | T7DCH | Also accessible as **WO-N Post Labor Batches** — same program, two menu paths; opens BKBMMSTR for BOM-based backflush during posting |
| `DC-I` | Select Active/Archive Work Orders | BKDCI | — | WO browser/filter for DC context; multi-date selection; "View Work Order Notes" mode; links to LW-A Enter Work Orders |

## UI forms (26)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `EVODCS.DFM` | New Screen | 0 | 2 | 0 |
| `EvoDCmenu.DFM` |  | 0 | 1 | 0 |
| `EvoDCmenu2.DFM` |  | 0 | 7 | 0 |
| `EvoDCsetup.DFM` | Create Workstation Setup | 3 | 11 | 0 |
| `T7DCA.DFM` |  | 0 | 1 | 0 |
| `T7DCA2.DFM` |  | 0 | 1 | 0 |
| `T7DCALabel.DFM` | Print Transfer Label | 16 | 45 | 0 |
| `T7DCANotes.DFM` | Notes Caption | 0 | 7 | 0 |
| `T7DCAPstdLab.dfm` | New Screen | 2 | 4 | 0 |
| `T7DCBSERIAL.DFM` | Enter Serial Numbers | 5 | 22 | 0 |
| `T7DCD.DFM` | DC-D | 24 | 59 | 0 |
| `T7DCE.DFM` | DC-E Print Labor Tickets | 6 | 24 | 0 |
| `T7DCF.DFM` | DC-E Print Employee Tickets | 4 | 22 | 0 |
| `T7DCG.DFM` |  | 0 | 1 | 0 |
| `T7DCH.DFM` | DC-H | 10 | 38 | 0 |
| `T7DCK.DFM` | DC-K | 7 | 28 | 0 |
| `T7DCL.DFM` |  | 0 | 1 | 0 |
| `T7DCM.DFM` |  | 0 | 1 | 0 |
| `T7DCN.DFM` | DC-N | 6 | 27 | 0 |
| `T7DCPSF.DFM` | HH-L  Paperless Shop Floor | 36 | 109 | 0 |
| `T7DCPSFComps.DFM` |  | 0 | 1 | 0 |
| `T7DCPSFECO.DFM` |  Eco | 10 | 35 | 0 |
| `T7DCSOLookup.DFM` |  | 0 | 1 | 0 |
| `t7DCPSFNotes.DFM` | Notes Caption | 0 | 12 | 0 |
| `t7DCina.DFM` | T7INA | 41 | 123 | 0 |
| `t7dcb.DFM` |  | 0 | 1 | 0 |

## Database tables (7)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKDCCFG** | `BKDCCFG.B` | 7 | `BKDC_CFG_IDLEP`, `BKDC_CFG_IDLES`, `BKDC_CFG_BANKP` |
| **BKDCCLAB** | `BKDCCLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCHLAB** | `BKDCHLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCLAB** | `BKDCLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCPLAB** | `BKDCPLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |
| **BKDCSHFT** | `BKDCSHFT.B` | 34 | `BKDC_SH_NAME1`, `BKDC_SH_NAME2`, `BKDC_SH_NAME3` |
| **BKDCTLAB** | `BKDCTLAB.B` | 50 | `LAB_DATE`, `LAB_EMP`, `LAB_WOPRE` |

## Table documentation (confirmed from DDF schema.md, Pass 111b 2026-06-19)

### BKDCCFG — Data Collection Configuration (7 fields)

Single-row configuration table (no PK — one row per company).

| Field | Type | Meaning |
|-------|------|---------|
| `BKDC_CFG_IDLEP` | FLOAT | Idle period threshold (minutes — when scanner is considered idle) |
| `BKDC_CFG_IDLES` | UBINARY | Idle seconds component |
| `BKDC_CFG_BANKP` | FLOAT | Bank (clock-in) period |
| `BKDC_CFG_BANKS` | UBINARY | Bank seconds component |
| `BKDC_CFG_IMPPTH` | STRING 60 | Import path (where scanner data files arrive) |
| `BKDC_CFG_EXPPTH` | STRING 60 | Export path (where label/ticket files are written) |
| `BKDC_CFG_JOBTME` | STRING 60 | Job time data path |

---

### LAB_* tables — Labor Transaction family (50 fields each)

Five tables share the same 50-field schema. The table role distinguishes them:

| Table | Role |
|-------|------|
| **BKDCCLAB** | Collected (raw) labor — scanner input awaiting review |
| **BKDCLAB** | Current labor — reviewed / approved transactions |
| **BKDCPLAB** | Posted labor — transactions posted to WO (WORKORD updated) |
| **BKDCHLAB** | History labor — archived posted transactions |
| **BKDCTLAB** | Transaction labor — working/temp table during processing |

Primary key (all 5 tables): `LAB_DATE` + `LAB_EMP` + `LAB_WOPRE` + `LAB_WOSUF` + `LAB_OPER`

**Core fields:**

| Field | Type | Meaning |
|-------|------|---------|
| `LAB_DATE` | DATE | Date of labor entry (PK 1) |
| `LAB_EMP` | UBINARY | Employee number (PK 2 — FK → BKPRMSTR) |
| `LAB_WOPRE` | FLOAT | Work order prefix (PK 3 — FK → WORKORD) |
| `LAB_WOSUF` | UBINARY | Work order suffix (PK 4) |
| `LAB_OPER` | UBINARY | Operation number (PK 5 — FK → ROUTING) |
| `LAB_POSTED` | STRING 1 | Posted flag (Y = posted to WO, N = pending) |
| `LAB_SHIFT` | UBINARY | Shift number (FK → BKDCSHFT) |
| `LAB_START` | TIME | Clock-in time for this operation |
| `LAB_FINISH` | TIME | Clock-out time for this operation |
| `LAB_PARTS` | FLOAT | Parts completed (good parts count) |
| `LAB_SCRAPPED` | FLOAT | Parts scrapped |
| `LAB_NOJOBS` | UBINARY | Number of jobs run on this operation |
| `LAB_RUNHRS` | FLOAT | Total run hours (computed from START/FINISH minus breaks) |
| `LAB_SETUPHRS` | FLOAT | Setup hours |
| `LAB_REGOVER` | STRING 1 | Regular (R) or overtime (O) |
| `LAB_EXTRA` | STRING 50 | Extra / user-defined |
| `LAB_APPROVAL` | STRING 1 | Supervisor approval flag (Y = approved) |
| `LAB_ADT_SUPER` | STRING 100 | Audit: supervisor who approved |
| `LAB_ADT_IN` | STRING 100 | Audit: clock-in record |
| `LAB_ADT_OUT` | STRING 100 | Audit: clock-out record |
| `LAB_ESSDATE` | DATE | ESS (Employee Self-Service) date |
| `LAB_DATE1` | DATE | Additional date 1 |
| `LAB_DATE2` | DATE | Additional date 2 |
| `LAB_SCRAPCD_1..5` | STRING 2 | Up to 5 scrap reason codes |
| `LAB_SCRAPQTY_1..5` | FLOAT | Corresponding scrap quantities |
| `LAB_JCNUM` | STRING 12 | Job cost number (FK → JC module) |
| `LAB_CYCLE_HR/MIN/SEC` | UBINARY | Cycle time components (hours, minutes, seconds) |
| `LAB_CYCLE_PARTS` | FLOAT | Parts per cycle |
| `LAB_CYCLE_NOTE` | STRING 255 | Cycle time note |
| `LAB_GEN_DATE_1/2` | DATE | User-defined dates 1–2 |
| `LAB_GEN_ALPHA_1/2` | STRING 30 | User-defined alpha fields 1–2 |
| `LAB_GEN_NUM_1/2` | FLOAT | User-defined numeric fields 1–2 |
| `LAB_GEN_FLAG_1..5` | STRING 1 | User-defined flags 1–5 |

---

### BKDCSHFT — Shift Schedule (34 fields)

Single-row per company (no PK). Defines the time windows for up to 3 shifts. All time-of-day fields are of type TIME.

| Field group | Meaning |
|---|---|
| `BKDC_SH_NAME1/2/3` | Shift names |
| `BKDC_SH_BUFFER_1/2/3` | Clock-in grace buffer before shift start |
| `BKDC_SH_START_1/2/3` | Shift start times |
| `BKDC_SH_BRK1IN_1/2/3` | Break 1 start times |
| `BKDC_SH_BRK1OUT_1/2/3` | Break 1 end times |
| `BKDC_SH_LUNCHIN_1/2/3` | Lunch break start times |
| `BKDC_SH_LUNCHOT_1/2/3` | Lunch break end times |
| `BKDC_SH_BRK2IN_1/2/3` | Break 2 start times |
| `BKDC_SH_BRK2OUT_1/2/3` | Break 2 end times |
| `BKDC_SH_FIN_1/2/3` | Shift end times |
| `BKDC_SH_FINBUF_1/2/3` | Clock-out grace buffer after shift end |
| `BKDC_SH_EXTRA` | Extra / notes |

---

## DC data flow (confirmed from table structure + help content)

```
Scanner / keyboard input
  → BKDCCLAB  (raw collected labor — LAB_POSTED = N)
  
DC-G: Edit Labor Transactions
  → Review BKDCCLAB; correct errors
  → Supervisor approves (LAB_APPROVAL = Y)
  
DC-H: Post Labor
  → Copy approved BKDCCLAB rows to BKDCLAB (LAB_POSTED = Y)
  → Update WORKORD operation hours (WOPROC_RUNHRS / SETUPHRS / PARTSMAD / SCRAP)
  → GL post via BKGLTRAN (labor cost to WO)
  → Move to BKDCPLAB (posted archive)
  → Archived to BKDCHLAB (history)

BKDCSHFT: controls break/lunch time deduction from LAB_START..LAB_FINISH
  to compute net LAB_RUNHRS for each transaction
```

## Programs (25 total) — Pass 266 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7DC* + EvoDC* entries.

### Group 1 — Core labor scanning

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7DCPSF.RWN` | 290 | ISTECH.LIB | **DC-PSF** primary scan / labor collection; BKDCLAB+WOROUT+WORKORD+BKICMSTR; **BKPR.EMP 107-var** |
| `T7DCA.RWN` | 284 | ISTECH.LIB | **DC-A** labor entry / clock-in-out; BKDCLAB+WORKORD+BKPRMSTR+ISWOEX; **LAB.CYCLE 80-var** (cycle time tracking namespace) |
| `t7dcb.RWN` | 252 | ISTECH.LIB | **DC-B** bin/location scan; BKICMSTR+BKDCLAB+BKPRMSTR+WORKORD; BKPR.EMP 107-var |
| `T7DCA2.RWN` | 128 | ISTECH.LIB | **DC-A2** labor entry variant; BKDCLAB+BKPRMSTR+BKYSMSTR+WORKORD; BKPR.EMP 92-var + MTWO.WIP 70-var |

### Group 2 — Review / approval / posting

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7DCG.RWN` | 192 | ISTECH.LIB | **DC-G** labor review / supervisor approval; BKDCLAB+WORKORD+MACHINE+TASCOLOR; BKPR.EMP 107-var + MTWO.WIP 71-var |
| `T7DCH.RWN` | 181 | ISTECH.LIB | **DC-H** labor posting; BKDCLAB+BKDCCFG+BKPRMSTR+WORKORD; BKPR.EMP 103-var + MTWO.WIP 71-var |

### Group 3 — Reports

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7DCD.RWN` | 151 | LISTG60.LIB | **DC-D** labor detail report; BKPRMSTR+BKPRINFO+BKCPMSTR; BKPR.EMP 105-var + **BKPR.GL 86-var** (payroll GL cost) |
| `T7DCL.RWN` | 145 | LISTG60.LIB | **DC-L** labor history report; BKPRMSTR+MKAHIST+BKDCLAB+BKPRINFO; BKPR.EMP 105-var + MTWO.WIP 71-var |
| `T7DCM.RWN` | 102 | EVO.LIB | **DC-M** labor management report; BKPRMSTR+BKDCLAB; BKPR.EMP 105-var |

### Group 4 — Employee / configuration

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7DCN.RWN` | 89 | LISTG60.LIB | **DC-N** employee schedule entry; BKPRMSTR+CALENDAR+BKDCLAB+CLASMSTR; BKPR.EMP 103-var |
| `T7DCF.RWN` | 86 | LISTG60.LIB | **DC-F** DC configuration / employee setup; BKPRMSTR; BKPR.EMP 103-var |
| `T7DCE.RWN` | 85 | LISTG60.LIB | **DC-E** operation / workcenter assignment; WOROUT+WORKORD; MTWO.WIP 71-var |
| `T7DCK.RWN` | 69 | LISTG60.LIB | **DC-K** DC admin/key entry; BKDCLAB+BKPRMSTR; BKPR.EMP 103-var |

### Group 5 — Labels and special functions

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7DCALabel.RWN` | 89 | LISTG60.LIB | **DC-A-LABEL** WO tray / NCR label printing; ISWOTRAY+ISNCR+BKPRMSTR; BKPR.EMP 105-var + MTWO.WIP 71-var |
| `t7DCina.RWN` | 240 | LISTG60.LIB | **DC-INA** item master inquiry (from DC); BKICMSTR+MTICMSTR+BKAPVEND+BKARCUST; **BKIC.PROD 315-var** + **BKIC.LOC 297-var** — full item master browser embedded in DC |
| `T7DCSOLookup.RWN` | 52 | EVO.LIB | **DC-SO-LOOKUP** SO lookup from DC terminal; BKARINV; BKAR.INV 86-var |

### Group 6 — Menu / session management

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `EvoDCmenu2.RWN` | 65 | EVO.LIB | DC menu v2; BKSYMSTR+BKAPDESC+BKMENUSU+ISEXUSER; ISTS.CFG 542-var |
| `EvoDC.RWN` | 51 | ISTECH.LIB | DC session launcher; BKSYMSTR+ISLOG+MKAHIST; ISTS.CFG 529-var |
| `EvoDCsetup.RWN` | 7 | NZEVO.LIB | DC NZL setup stub; DCL.PERIOD 2-var (labor period dates) |
| `T7DCC.RWN` | 17 | NZLICE.LIB | NZL license stub — no business logic |

### Notable namespace findings

| Namespace | Count | Program | Meaning |
|-----------|------:|---------|---------|
| `LAB.CYCLE` | 80 | T7DCA | Labor cycle time tracking — independent of clock-in/clock-out |
| `BKPR.EMP` | 107 | T7DCPSF, t7dcb, T7DCG | Employee master accessor — all scan programs need full employee record |
| `BKPR.GL` | 86 | T7DCD | Payroll GL cost data — DC reports carry payroll-side cost fields |
| `BKIC.PROD` | 315 | t7DCina | Item master accessor embedded in DC (matches IN-A count) |
| `MTWO.WIP` | 71 | t7dcb, T7DCG, T7DCH | WIP accessor — DC updates WO operations at scan time |
| `DCL.PERIOD` | 2 | EvoDCsetup | DC labor period dates (period open/close control) |

### New tables discovered in DC programs

| Table | Appears In | Inferred Role |
|-------|-----------|---------------|
| `ISWOEX` | T7DCA | WO exceptions / extensions — additional WO data accessed at scan time |
| `BKDCCFG` | T7DCH | DC configuration — posting parameters and options |
| `BKCPMSTR` | T7DCD | CP (company/plant) master — cost pool or plant-level cost grouping |
| `BKPRINFO` | T7DCD, T7DCL | Payroll info — additional employee pay data beyond BKPRMSTR |
| `MKAHIST` | T7DCL, EvoDC | MKA history — manufacturer activity log |
| `ISLOG` | EvoDC | IS event log — session/login audit log |
| `DCL.PERIOD` | EvoDCsetup | DC labor period control (open/close dates for posting) — namespace only |
| `ISNCR` | T7DCALabel | Non-Conformance Report — DCLabel prints NCR tags on failing parts |
| `TASCOLOR` | T7DCG | TAS color table — screen color configuration for DC-G review UI |

---

---

## Pass 338 — TAS6 BKDC* binary analysis (2026-06-26)

All 11 BKDC*.RUN files extracted and analyzed. This pass corrected the menu table and confirmed workflow details.

### Complete TAS6 BKDC* inventory (11 files)

| File | Size | Title (from binary) | Role |
|------|-----:|---------------------|------|
| BKDCA | 225 KB | "Enter Labor/Production" | DC-A main entry |
| BKDCA2~1 | 135 KB | "Enter Labor/Production" (variant) | DC-A2 variant — directly writes WOLABOR; has "Reporting Labor?" prompt |
| BKDCB | 8 KB | "Enter Production Only" | DC-B dispatch → BKDCA |
| BKDCC | 9 KB | "Enter Labor Only" | DC-C dispatch → BKDCA |
| BKDCD | 202 KB | "DC-D View/Print Labor Status" | DC-D report + CheckMark export |
| BKDCE | 148 KB | "DC-E Print Labor Tickets" | Uses bkdce.rtm; WO range filter |
| BKDCF | 127 KB | "DC-F Print Employee Tickets" | Uses bkdcf.rtm; employee-based tickets |
| BKDCG | 236 KB | "DC-G Edit Labor Transactions" | Review/edit; cannot add records |
| BKDCGMSG | 179 KB | "DC-G Edit Labor Transactions" | DC-G variant with message formatting for scanner displays |
| BKDCH | 286 KB | "DC-H Post Labor Transactions" / "WO-N Post Labor Batches" | Same program, two menu paths |
| BKDCI | 252 KB | "DC-I Select Active/Archive Work Orders" | WO browser with date-based filtering |

### Key findings

**DC-A architecture** — BKDCA opens: `BKDCSHFT`, `BKDCLAB`, `BKPRMSTR`, `BKICMSTR`, `MTICMSTR`, `BKDCPLAB`, `BKDCTLAB`. Validates Employee number, allows "Enter Machine NO." for machine-based time capture. Calls `ISDCA.RUN` for transfer label printing (that is the separate label function — not the main DC-A operation title). The three scan modes (Labor+Production / Production Only / Labor Only) are invoked through DC-A, DC-B (dispatch), and DC-C (dispatch).

**BKDCA2~1.RUN** — second DC-A variant (135KB vs 225KB). Directly opens `WOLABOR` (bypasses BKDCCLAB staging — posts straight to WO labor table). Has `"Reporting Labor?"` prompt and `BKDCTLAB` handle. This is likely the workstation variant used when DC-A is configured for direct posting (no review step).

**DC-H = WO-N confirmed** — BKDCH.RUN contains both `"DC-H  Post Labor Transactions"` and `"WO-N  Post Labor Batches"` title strings. Also opens `BKBMMSTR` (BOM master) — confirms that DC-H performs BOM-based backflush material issue during posting. `BKDCCLAB` (raw collected) + `BKDCLAB` (reviewed) + `BKDCCFG` (posting config) all opened. F10=Post All hotkey confirmed.

**DC-D CheckMark integration** — BKDCD.RUN contains identical CheckMark export message to WO-L-E: "Now run 'Enter Hours' (then click 'Import Hours') in CheckMark Payroll using this file name." Print options: `Print by Emp# or WO# [E/W]`, `Print Details [Y/N]`, `Print Shift only [Y/N]`. Opens `BKDCHLAB` (history) for historical reports. `BKCPMSTR` confirmed (CP master = company/plant cost pool table used for DC costing reports).

**BKDCGMSG** — smaller variant of DC-G (179KB vs 236KB). Missing `BKSYMSTR` (system master) that BKDCG has, suggesting it's a simplified version for dedicated DC terminals that don't need full system context. Both contain identical "You cannot Add Labor records with this program. Use DC-A, B, or C." message.

**DC-I WO browser** — Opens `BKICMSTR`, `MTICMSTR`, `CLASMSTR`. Multi-date WO selection ("you may enter an unlimited number" of dates). Two modes: "DC-I View [Work Order]" and "DC-I View Work Order Notes". Links to "LW-A Enter Work Orders". Allows Work Center filter.

### Table accessors confirmed

| TAS6 handle | DDF table | Confirmed in |
|-------------|-----------|-------------|
| `BKDCPLABA` | BKDCPLAB | BKDCA, BKDCG, BKDCH |
| `BKDCTLABA` | BKDCTLAB | BKDCA |
| `BKDCSHFTA` | BKDCSHFT | BKDCA, BKDCG, BKDCH |
| `BKDCLABA` | BKDCLAB | BKDCG, BKDCH, BKDCD |
| `BKDCCLABA` | BKDCCLAB | BKDCH |
| `BKDCHLABL` | BKDCHLAB | BKDCD |
| `BKDCIA` | (self) | BKDCI |
| `WOLABORA` | WOLABOR | BKDCA2~1 (direct post variant) |

---

## Notes

- All five LAB_* tables share identical schemas. The distinction is purely lifecycle stage: collect → review → post → archive.
- BKDCTLAB confirmed as working/temp table opened by DC-A during data entry (not DC-H). DC-H uses BKDCCLAB (raw) and BKDCLAB (reviewed) directly.
- The scrap reason codes (LAB_SCRAPCD_1..5) allow a single operation to report up to 5 distinct failure modes with separate quantities — important for QC analysis.
- `LAB_CYCLE_*` fields track cycle time independently of clock-in/clock-out, supporting cycle time studies and rate analysis.
- BKDCA2~1.RUN bypasses BKDCCLAB staging and writes WOLABOR directly — used when DC is configured for direct-post mode (no approval step).
- AUTODCH (referenced in prior menu table) = automated/batch DC-H variant not in the 11-file TAS6 set; UMCDCP = i2 custom DC-H extension.
- Transfer labels are printed by calling `ISDCA.RUN` from within DC-A (not a separate menu operation).
