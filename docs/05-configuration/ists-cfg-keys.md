# ISTS.CFG.* Configuration Key Directory
Status: partial | verified-from-rwn-strings

## Overview

EvoERP stores its runtime configuration in two places:
- **BKSYMSTR** (286 fields) — structured system configuration record
- **BKYSMSTR** (195+ YN[N] boolean flags) — yes/no parameter array

The `ISTS.CFG.*` naming scheme is the **key namespace** used inside TAS Pro source and compiled
programs to look up configuration values. These keys map to fields in BKYSMSTR/BKSYMSTR at runtime.

**Total unique keys found: 535** (extracted via grep across 2,575 rwn_strings files)

---

## Key Extraction Technique

```
grep -h "ISTS\.CFG\." samples\rwn_strings\*.txt | sort -u
```

Grep pattern across all `.txt` files in `samples/rwn_strings/` — every program's string dump
is searched. Keys that appear in many files are global system flags; keys in 1–3 files are
module-specific toggles.

---

## Prevalence Distribution

| Occurrence bucket | Key count | Meaning |
|-------------------|-----------|---------|
| 400+ files | ~9 keys | Global system flags (every module reads these) |
| 100–399 files | ~50 keys | Cross-module flags |
| 10–99 files | ~200 keys | Module-family flags |
| 1–9 files | ~276 keys | Module-specific toggles |

### Most widespread keys (400+ files — read by essentially all programs)

| Key | Likely meaning |
|-----|---------------|
| ISTS.CFG.ACCESS | User access/permission check |
| ISTS.CFG.PASSWD | Password validation flag |
| ISTS.CFG.CFGLVL | Configuration security level |
| ISTS.CFG.ATOS | Auto-save / auto-post flag |
| ISTS.CFG.COORD | Screen coordinate mode |
| ISTS.CFG.DDNUM | Data dictionary number |
| ISTS.CFG.DIVOHD | Division overhead flag |
| ISTS.CFG.HREP | HR/employee report flag |
| ISTS.CFG.MAKCUS | Make-to-customer flag |

---

## Functional Categories

### Access & Security
```
ISTS.CFG.ACCESS     — global access check
ISTS.CFG.PASSWD     — password required flag
ISTS.CFG.ARPSWD     — AR password
ISTS.CFG.CRPSWD     — credit override password
ISTS.CFG.FUPSWD     — future pricing password
ISTS.CFG.SOPSWD     — SO password
ISTS.CFG.WOPSWD     — WO password
ISTS.CFG.CFGLVL     — configuration access level
```

### Accounts Payable (AP*)
```
ISTS.CFG.APSORT     — AP sort order
ISTS.CFG.APADTE     — AP date A
ISTS.CFG.APBDTE     — AP date B
ISTS.CFG.APDUP      — AP duplicate voucher check
ISTS.CFG.APOPEN     — AP open item mode
ISTS.CFG.APSORT     — AP sort preference
```

### Accounts Receivable (AR*)
```
ISTS.CFG.ARSORT     — AR sort order
ISTS.CFG.ARADTE     — AR date
ISTS.CFG.ARLCST     — AR last cost flag
ISTS.CFG.ARNEG      — AR negative balance handling
```

### Sales Order (SOA*, SOE*)
Over 70 SO-related keys, including:
```
ISTS.CFG.SOACDT     — SO acknowledgment date
ISTS.CFG.SOEDTE     — SO end date
ISTS.CFG.SOBACK     — backorder handling
ISTS.CFG.SOCRED     — credit check on SO
ISTS.CFG.SOHOLD     — SO hold flag
ISTS.CFG.SOINVP     — SO invoice print
ISTS.CFG.SOPACK     — SO packing list flag
ISTS.CFG.SOSHIP     — SO auto-ship flag
ISTS.CFG.SOPRICE    — SO pricing method
ISTS.CFG.SOTAX      — SO tax calculation
```

### Purchase Order (PO*)
Over 80 PO-related keys, including:
```
ISTS.CFG.POAUTO     — PO auto-generate
ISTS.CFG.POCONS     — PO consolidation
ISTS.CFG.POEDTE     — PO expiration date
ISTS.CFG.POMIN      — PO minimum quantity
ISTS.CFG.POPRICE    — PO pricing method
ISTS.CFG.PORECV     — PO receiving mode
ISTS.CFG.PORQST     — PO requisition mode
ISTS.CFG.POVEND     — PO vendor approval
ISTS.CFG.POXREF     — PO cross-reference
```

### Work Order (WO*)
44+ WO-related keys:
```
ISTS.CFG.WOAROP     — WO AR operation
ISTS.CFG.WOBASE     — WO base calculation
ISTS.CFG.WOCALC     — WO cost calculation method
ISTS.CFG.WOGKIT     — WO kit generation
ISTS.CFG.WOGNEG     — WO negative quantity flag
ISTS.CFG.WOOPEN     — WO open flag
ISTS.CFG.WOONLY     — WO-only mode
ISTS.CFG.WOOVER     — WO override flag
ISTS.CFG.WOROUT     — WO routing flag
ISTS.CFG.WOSTEP     — WO step processing
```

### Data Collection (DC*)
```
ISTS.CFG.DCBSER     — DC barcode serial
ISTS.CFG.DCCQTY     — DC current quantity
ISTS.CFG.DCDQTY     — DC daily quantity
ISTS.CFG.DCPDTE     — DC process date
ISTS.CFG.DCSEQ      — DC sequence
ISTS.CFG.DCSQTY     — DC scanned quantity
ISTS.CFG.DCSYNC     — DC synchronize flag
```

### Inventory / Costing
```
ISTS.CFG.STDCST     — standard cost flag
ISTS.CFG.UPLCST     — upload cost flag
ISTS.CFG.NEGCST     — negative cost handling
ISTS.CFG.INCSTD     — include standard flag
ISTS.CFG.QTYADJ     — quantity adjustment
ISTS.CFG.QWOQTY     — WO quantity
ISTS.CFG.EPOQTY     — PO expected quantity
```

### Reporting
```
ISTS.CFG.REPRT      — report output flag
ISTS.CFG.ROAPPH     — RO append history
ISTS.CFG.QCRPT      — QC report flag
ISTS.CFG.TPRTNT     — print-to-network flag
```

### EDI / Integration
```
ISTS.CFG.EDIBOL     — EDI bill of lading
ISTS.CFG.EDIOUT     — EDI outbound flag
```

### Credit Card Processing
```
ISTS.CFG.CCDEF      — CC default
ISTS.CFG.CCFEE      — CC fee
ISTS.CFG.CCPSW      — CC password
ISTS.CFG.CCUID      — CC user ID
```

### EvoNotes
```
ISTS.CFG.EVONTS     — EvoNotes enabled toggle
```

### Ship-Via
```
ISTS.CFG.VIAMST     — ship-via master toggle
```

---

## Module Mapping

Keys are distributed across 2,575 program files. The file prefix reveals the module:

| File prefix | Module |
|-------------|--------|
| BKA*.txt | Accounts Payable (AP) programs |
| BKAR*.txt | Accounts Receivable (AR) programs |
| BKSO*.txt | Sales Order (SO) programs |
| BKPO*.txt / BKAP*.txt | Purchase Order (PO) programs |
| BKWO*.txt / BKWOA*.txt | Work Order (WO) programs |
| BKGL*.txt | General Ledger (GL) programs |
| BKPR*.txt | Payroll (PR) programs |
| BKIC*.txt | Inventory (IN) programs |
| BKDC*.txt | Data Collection (DC) programs |
| BKJ7*.txt | J7 customization programs |

---

## Notes on Mapping to YN[N] Array

In TAS Pro source code, BKYSMSTR flags are accessed as `YN[N]` where N is the array index.
The `ISTS.CFG.*` key string is the human-readable alias for the same flag — programs use
the key string to look up the numeric index at runtime.

Known mappings (from SRC analysis):
- `YN[38]` = ISTS.CFG.WOCALC (routing auto-sequence)
- `YN[228]` = ISTS.CFG.DCSEQ (DC screen mode)
- `YN[229]` = ISTS.CFG.DCSYNC (DC auto-close)

Full YN[N] ↔ ISTS.CFG.* mapping not yet extracted — would require either SRC files
or runtime debugging.

---

*Last updated: 2026-06-11*
*Confidence: 68/100 — 535 unique keys cataloged from string dumps; functional categories inferred from key names; exact BKYSMSTR index mapping not yet complete for most keys.*
