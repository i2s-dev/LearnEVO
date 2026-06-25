# SD — Standard Detail Codes

Status: verified | Pass 251 (2026-06-25)

---

## Overview

The SD Standard Detail Codes subsystem provides a cross-module lookup table for defect/failure classification. It manages two tables: ISSTYPE (category master) and ISSDET (detail code master). These codes are consumed by SPC (quality data collection), SR (service/repair), NCR (non-conformance reports), and other quality-related modules.

**Name collision warning:** "SD" also refers to "System Defaults" in the BKSYMSTR/BKYSMSTR editor. This document covers only Standard Detail Codes (T7SDET). See `docs/03-modules/sd-system-defaults/` for System Defaults.

Access: **NOT in BKMENUSU.TXT or menu_codes.csv.** Subsystem access only (not reachable from the main EvoERP operator menu). Also distinct from T7SMPI ("SM-P-I → Enter Defect Codes") which manages the separate ISDEFECT table.

---

## Programs (1)

| Program | Procs | Lib | DB Files |
|---------|-------|-----|----------|
| T7SDET.RWN | 58 | EVO.LIB | ISSDET, ISSTYPE, ISNCR, ISMCR, BKARCUST, BKAPVEND, LANGDICT, FILELOC, ISDRILL, ... (18 unique) |

Standard EVO.LIB CRUD editor template — same pattern as T7SETYPE, T7SEPROC.

---

## Tables (2)

### ISSTYPE — Category master (3 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_STYPE_TYPE | STRING/60 | PK — full category description (60 chars) |
| IS_STYPE_WHO | STRING/40 | Last-modified-by user |
| IS_STYPE_ASSET | STRING/25 | Asset/station association |

### ISSDET — Detail code master (4 fields)
| Field | Type | Notes |
|-------|------|-------|
| IS_SDET_TYPE | STRING/20 | PK part 1 — abbreviated category code |
| IS_SDET_DETAIL | STRING/20 | PK part 2 — detail code |
| IS_SDET_WHO | STRING/40 | Last-modified-by user |
| IS_SDET_SUB | STRING/1 | Sub-classification flag |

Compound PK: IS_SDET_TYPE + IS_SDET_DETAIL.

**Size mismatch note:** ISSTYPE.TYPE is STRING/60 (full description as key) while ISSDET.TYPE is STRING/20 (abbreviated code). These fields are the same logical concept (category type) but stored at different sizes — they may be separate naming dimensions rather than a direct FK relationship. The exact join logic is not confirmed from binary.

---

## Named Variables (T7SDET)

From `rwn_symbols.json`:
- `IS.SDET.TYPE`, `IS.SDET.DETAIL`, `IS.SDET.WHO`, `IS.SDET.SUB` — working fields for ISSDET
- `IS.STYPE.TYPE`, `IS.STYPE.WHO`, `IS.STYPE.ASSET` — working fields for ISSTYPE
- `ISSDET.H`, `ISSTYPE.H` — table handles
- `ETBCOMBOVAL` — combo-box selection value (standard EVO.LIB pattern)
- `ADD.NEW`, `WHOAMI`, `REPLNK_REC_HOLD` — standard EVO.LIB CRUD scaffolding vars

---

## Cross-Module Usage

| Module | Program | How ISSDET is used |
|--------|---------|-------------------|
| SPC | T7SPC (148p) | IS_SPC_TYPE + IS_SPC_DETAIL FK into ISSDET compound PK |
| SPC | T7SPCREP, T7SPCREP2, T7SPCLIVEREP, T7SPCREPPPM | Report filtering/display by TYPE+DETAIL |
| SPC | T7SPCLIVEGRID | Live grid — also uses ISSDET for range filtering |
| SR | T7SRA (15p, stub launcher) | ISSDET in DB file list — detail codes in service/repair |
| NCR | via T7SDET DB list | ISNCR in T7SDET's 18 DB files — NCR references detail codes |

---

## Relationship to Other "Defect Code" Tables

EvoERP has multiple defect/error classification tables that are NOT the same:

| Table | Manager | Purpose |
|-------|---------|---------|
| ISSTYPE + ISSDET | T7SDET | Standard Detail Codes — cross-module quality classification |
| ISSETYPE | T7SETYPE | AOI error type codes (used by ISSERR in SPC) |
| ISSEPROC | T7SEPROC | AOI process codes (used by ISSERR in SPC) |
| ISDEFECT | T7SMPI (menu: SM-P-I) | Separate defect code table — unrelated to ISSDET |

---

**Confidence: 88/100** — Table schemas confirmed from DDF; program details confirmed from rwn_symbols.json; cross-module FK relationships inferred from named vars and DB file lists. The ISSTYPE.TYPE (STRING/60) vs ISSDET.TYPE (STRING/20) size discrepancy means the exact join/hierarchy relationship is inferred, not confirmed from bytecode.
