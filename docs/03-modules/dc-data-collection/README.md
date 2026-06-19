# Data Collection (Shop Floor) (DC)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `DC`
- **Tables**: 7 (prefixes `BKDC`)
- **UI forms**: 26 (prefixes `T7DC`, `T6DC`, `EVODC`)
- **Menu operations**: 7

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

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `DC-A` | Print Transfer Labels | J5ISDCA;J6ISDCA |
| `DC-D` | View/Print Labor Status | BKDCD;t6dcd |
| `DC-E` | Print Labor Tickets | BKDCE;T6DCE |
| `DC-F` | Print Employee Tickets | BKDCF;T6DCF |
| `DC-G` | Edit Labor Transactions | BKDCG;BKDCGMSG;CBKWOM;J5HDWOM |
| `DC-H` | Filelock on TOOL - | AUTODCH;BKDCH;UMCDCP |
| `DC-I` | View | BKDCI |

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

## Notes

- All five LAB_* tables share identical schemas. The distinction is purely lifecycle stage: collect → review → post → archive.
- BKDCTLAB may be used as a working/temp table during DC-H posting — its exact role is inferred from the name ("transaction") but not confirmed without RWN source.
- The scrap reason codes (LAB_SCRAPCD_1..5) allow a single operation to report up to 5 distinct failure modes with separate quantities — important for QC analysis.
- `LAB_CYCLE_*` fields track cycle time independently of clock-in/clock-out, supporting cycle time studies and rate analysis.
- DC-A prints transfer labels (J5ISDCA = i2 custom program); DC-H is the core posting program (AUTODCH = automated version for batch mode).
