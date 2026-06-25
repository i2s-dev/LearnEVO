# SP — Statistical Process Control (SPC)

Status: verified | Pass 251 (2026-06-25)

---

## Overview

The SP/SPC subsystem is EvoERP's quality data collection and reporting engine. It captures per-operation pass/fail counts, AOI (automated optical inspection) machine defect data, and component serial traceability — all keyed to Work Order + Operation.

Access: **NOT in the main EvoERPmenu / BKMENUSU.TXT.** Accessed via a dedicated scan terminal or subsystem menu (likely the DC/data-collection menu), not the standard operator menus.

---

## Programs (9 total)

| Program | Procs | Lib | Role |
|---------|-------|-----|------|
| T7SPC.RWN | 148 | LISTG60.LIB | Main SPC data entry — scan-driven WO/operation entry for all three tracks |
| T7SPCREP.RWN | 105 | — | SPC reporting |
| T7SPCREP2.RWN | 105 | — | SPC reporting (alternate layout) |
| T7SPCLIVEREP.RWN | 50 | — | Live SPC reporting |
| T7SPCREPPPM.RWN | 104 | — | SPC PPM (parts-per-million defect rate) reporting |
| T7SPCLIVEGRID.RWN | 5 | T7spclivegrid.SRC | Real-time live defect grid (has source) |
| T7SPCMEMO2ALPHA.RWN | 25 | ISTECH.LIB | Batch converter: AOI 1000-char memo fields → shorter alpha summaries |
| T7SETYPE.RWN | 52 | EVO.LIB | CRUD editor for ISSETYPE (error type master) |
| T7SEPROC.RWN | 52 | EVO.LIB | CRUD editor for ISSEPROC (process code master) |

T7SETYPE and T7SEPROC are standard EVO.LIB CRUD editors — same template as T7SDET. They maintain the lookup tables used by T7SPC when recording machine error data.

---

## Tables (7 total)

### ISSTYPE — Category master (3 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_STYPE_TYPE | STRING/60 | PK — full category description (60 chars) |
| IS_STYPE_WHO | STRING/40 | Last-modified-by user |
| IS_STYPE_ASSET | STRING/25 | Asset/station association |

### ISSDET — Detail code master (4 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SDET_TYPE | STRING/20 | PK part 1 — abbreviated category code (20 chars) |
| IS_SDET_DETAIL | STRING/20 | PK part 2 — detail code |
| IS_SDET_WHO | STRING/40 | Last-modified-by user |
| IS_SDET_SUB | STRING/1 | Sub-classification flag |

Note: ISSTYPE.TYPE is STRING/60 (full description key) while ISSDET.TYPE is STRING/20 (abbreviated code) — these are likely separate dimensions, not directly FK-linked by the same field value. The SD module (T7SDET) manages both tables.

### ISSETYPE — Error type master (2 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SETYPE_ERR | STRING/25 | PK — error type code |
| IS_SETYPE_WHO | STRING/40 | Last-modified-by user |

### ISSEPROC — Process code master (2 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SEPROC_PROC | STRING/25 | PK — process code |
| IS_SEPROC_WHO | STRING/40 | Last-modified-by user |

### ISSPC — Operator SPC record (20 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SPC_WOPRE | FLOAT/8 | WO prefix (PK part 1) |
| IS_SPC_WOSUF | UBINARY/2 | WO suffix (PK part 2) |
| IS_SPC_OPER | UBINARY/2 | Operation number |
| IS_SPC_EMPNUM | UBINARY/2 | Employee number |
| IS_SPC_DATE | DATE/4 | Date of entry |
| IS_SPC_TIME | TIME/4 | Time of entry |
| IS_SPC_GOOD | UBINARY/2 | Good unit count |
| IS_SPC_REWORK | UBINARY/2 | Rework unit count |
| IS_SPC_SIDE | STRING/1 | Board side (e.g. T/B for top/bottom) |
| IS_SPC_TYPE | STRING/20 | Detail type FK → ISSDET.TYPE |
| IS_SPC_DETAIL | STRING/20 | Detail code FK → ISSDET.DETAIL |
| IS_SPC_EXTRA | STRING/100 | Free-form notes |
| IS_SPC_TESTR | STRING/1 | Test result flag |
| IS_SPC_TESTT | STRING/30 | Test type |
| IS_SPC_TESTE_1 | STRING/60 | Test extra field 1 |
| IS_SPC_TESTE_2 | STRING/60 | Test extra field 2 |
| IS_SPC_TESTE_3 | STRING/60 | Test extra field 3 |
| IS_SPC_ANOTES | STRING/1000 | Audit notes (long memo) |
| IS_SPC_CUST | STRING/10 | Customer code |
| IS_SPC_PART | STRING/15 | Part number |

### ISSERR — AOI machine error record (14 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SERR_WOPRE | FLOAT/8 | WO prefix |
| IS_SERR_WOSUF | UBINARY/2 | WO suffix |
| IS_SERR_OPER | UBINARY/2 | Operation number |
| IS_SERR_TIME | TIME/4 | Time of entry |
| IS_SERR_DATE | DATE/4 | Date of entry |
| IS_SERR_ERROR | STRING/25 | Error type code → ISSETYPE.ERR |
| IS_SERR_PROCESS | STRING/25 | Process code → ISSEPROC.PROC |
| IS_SERR_COUNT | UBINARY/2 | Error count |
| IS_SERR_REF | STRING/50 | Reference designator |
| IS_SERR_EXTRA | STRING/50 | Extra info |
| IS_SERR_SERIAL | STRING/20 | Serial number |
| IS_SERR_ADOF | STRING/1000 | AOI defect-of-failure raw text (1000 chars) |
| IS_SERR_ADIAG | STRING/1000 | AOI diagnosis raw text (1000 chars) |
| IS_SERR_AREWORK | STRING/1000 | AOI rework instructions raw text (1000 chars) |

Display vars IS.SERR.DOF / IS.SERR.DIAG / IS.SERR.REWORK are shorter display versions; ADOF/ADIAG/AREWORK hold the full 1000-char machine output. T7SPCMEMO2ALPHA converts the long memos to shorter alpha summaries.

### ISSTRACK — Component serial traceability (13 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_STRACK_WOPRE | FLOAT/8 | WO prefix |
| IS_STRACK_WOSUF | UBINARY/2 | WO suffix |
| IS_STRACK_OPER | UBINARY/2 | Operation number |
| IS_STRACK_TIME | TIME/4 | Time |
| IS_STRACK_DATE | DATE/4 | Date |
| IS_STRACK_PROC | STRING/25 | Process code |
| IS_STRACK_PSER | STRING/20 | Parent serial number |
| IS_STRACK_COMP | STRING/15 | Component part number |
| IS_STRACK_CSER | STRING/20 | Component serial number |
| IS_STRACK_NOTE | STRING/1000 | Notes (long memo) |
| IS_STRACK_EXTRA | STRING/50 | Extra info |
| IS_STRACK_AR | STRING/1 | Accept/reject flag |
| IS_STRACK_CLOT | STRING/15 | Component lot number |

---

## Architecture — Three-Track Data Collection

T7SPC is scan-driven: operator scans employee badge → scans WO barcode → scans operation.

**Track 1 — Operator SPC (ISSPC):** Records good/rework unit counts per WO+operation+employee. Linked to ISSDET category/detail codes for defect classification. Entry variables: SCAN.EMP, SCAN.WO, SCAN.OPER.

**Track 2 — AOI Machine Errors (ISSERR):** Records machine-detected defects from AOI equipment. Three 1000-char fields (ADOF/ADIAG/AREWORK) hold raw AOI output text. Lookup: ISSETYPE (error types) + ISSEPROC (process codes).

**Track 3 — Component Traceability (ISSTRACK):** Records parent→component serial number relationships, enabling full component genealogy tracing.

---

## T7SPCLIVEGRID — Real-Time Defect Grid

5-procedure program (has `.SRC` source file: `T7spclivegrid.SRC`). Displays a live grid of defect counts. Notable: contains **hardcoded defect code comparison variables** that appear to be i2 Systems-specific manufacturing defects:

| Var | Defect Code |
|-----|-------------|
| BILBD | Billable Board |
| BOHOS | Board Hot OS (or similar) |
| BDDAM | Board Damage |
| DAMGD | Damaged |
| FOD | Foreign Object Debris |
| INSUF | Insufficient (solder) |

These are hardcoded into the live grid logic, not looked up from ISSDET — suggesting they are special-cased defect types that drive summary metrics.

Grid range variables: FROM.DATE/THRU.DATE, FROM.TYPE/THRU.TYPE, FROM.DETAIL/THRU.DETAIL, TOP (top-N filter), REFRESH (auto-refresh flag).

---

## Cross-Module Integration

- **T7ROJA (RO-J-A Routing Job Analysis, 106p, LISTG60.LIB):** Reads ISSPC directly — SPC quality data appears in routing job analysis reports.
- **T7SRA (SR-A Service/Repair Entry, 15p, NZLICE.LIB):** Stub launcher; DB list includes ISSDET — detail codes used in service/repair workflows.
- **NCR module:** ISNCR appears in T7SDET's DB file list, confirming SPC detail codes feed into non-conformance reports.

---

## Source Files

Only T7SPCLIVEGRID has a recoverable `.SRC` source file (`T7spclivegrid.SRC`). All other SP programs are binary-only `.RWN` (Twofish-CFB encrypted).

---

**Confidence: 90/100** — All table schemas confirmed from DDF (`samples/ddf/schema.md`); all program details confirmed from `samples/rwn_symbols.json`; architecture inferred from variable names and DB file lists. The only gap is the exact UI flow and menu path for T7SPC entry (not in BKMENUSU), which is inferred as scan-terminal/subsystem access.
