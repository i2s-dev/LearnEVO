# EDI (ED)

Status: verified | Binary analysis Pass 320 2026-06-26.

Sources: BKMENUSU.TXT, DFM inventory, DDF schema, binary string extraction of 9 BKED*/ISEDI*/T6EDI*.RUN programs.

- **Module code**: `ED`
- **Tables**: 6 (prefixes `BKED`)
- **UI forms**: 3 (T7EDII.DFM, t7ediftp.DFM, t7edudf.DFM)
- **Menu operations**: 6

## Architecture — CandoEDI middleware

**EvoERP does NOT parse X12 directly.** All X12 translation is handled by **CandoEDI**, an
external EDI translation program. EvoERP's ED module reads and writes flat intermediate files
that CandoEDI produces/consumes.

### Inbound flow (trading partner → EVO SO)

```
Trading partner  →  X12 850 PO  →  CandoEDI  →  DBASO.IN (flat)
DBASO.IN  →  ED-B (BKEDB/ISEDIB/t6edib)  →  BKEDIH + BKEDIL staging tables
BKEDIH/BKEDIL  →  ED-C (edit/review)
ED-C  →  ED-D (BKEDD/ISEDID)  →  BKARINV + BKARINVL (live SO)
```

### Outbound flow (EVO invoice/ACK → trading partner)

```
BKARINV/BKARINVL  →  ED-E (T6EDIE/t6ediex)  →  DBASO.OUT + DBASHIP.OUT flat files
DBASO.OUT  →  CandoEDI  →  X12 810 Invoice or X12 855 ACK  →  trading partner
DBASHIP.OUT  →  CandoEDI  →  X12 856 ASN (via DEP module)  →  trading partner
```

### Intermediate flat files (confirmed from binary strings)

| File | Direction | Contents |
|------|-----------|---------|
| `DBASO.IN` | CandoEDI → EvoERP | Translated inbound X12 850 PO (flat, one line per field) |
| `DBASO.OUT` | EvoERP → CandoEDI | Exported SO/invoice data for translation to X12 |
| `DBASHIP.OUT` | EvoERP → CandoEDI | Ship-to/ASN data for translation to X12 856 |
| `CAEDI.ON` | CandoEDI → EvoERP | CandoEDI output notification (triggers import hook) |
| `HOOK` | EvoERP internal | Trigger file; `HOOK.SONUM` = SO number passed to post-import hook |

### X12 version numbers

X12 version identifiers (004010, 005010, etc.) are **not present in EvoERP binaries** — they
are configured entirely within CandoEDI. No version strings appear in any of the 9 EDI
RUN files analyzed.

---

## X12 transaction sets confirmed

| Set | Type | Direction | Evidence |
|-----|------|-----------|---------|
| 850 | Purchase Order | Inbound | DBASO.IN import path; BKEDIH = BKARINV PO staging |
| 860 | PO Change | Inbound | ISEDID.RUN: "This is an 860 and will delete Existing Sales Order(s)" |
| 810 | Invoice | Outbound | t6ediex.RUN: `_IN810_ZZMacola.A` string; "Export Invoices or Acknowledgements" |
| 855 | PO Acknowledgement | Outbound | T6EDIE.RUN: "Export Invoices or Acknowledgements" |
| 856 | ASN | Outbound | BKMENUSU: DEP-F = "Export 856 ASN"; T7DEP* programs |

Note: 856 ASN generation is handled by the **DEP** module (T7DEP* programs), not the ED
module programs. DEP is the outbound compliance/ASN subsystem.

The `_IN810_ZZMacola.A` string in t6ediex.RUN confirms an integration variant for
Macola ERP trading partners. `ZZ` is the X12 "Mutually Defined" qualifier.

---

## Menu operations

| Code | Operation | Legacy module file(s) | Notes |
| ---- | --------- | --------------------- | ----- |
| `ED-B` | Import EDI Orders | BKEDB;ISEDIB;ISEDIX;NBEDIB;t6edib | Reads DBASO.IN → BKEDIH/BKEDIL staging |
| `ED-C` | Edit EDI Orders | BKEDC | Grid editor for BKEDIH/BKEDIL staging |
| `ED-D` | Convert EDI Orders to Sales Orders | BKEDD;ISEDID;t6edid | BKEDIH/BKEDIL → BKARINV/BKARINVL; handles 860 deletes |
| `ED-E` | Export EDI Orders | T6EDIE;t6ediex | BKARINV → DBASO.OUT; exports Invoices or ACKs |
| `ED-G` | Master EDI Set-up | BKEDG | Sets BKEDMSTR path + DUNS + next import number |
| `ED-H` | Error report | ISEDIH | BKEDIH error scan: invalid customer, ship-to code |

---

## Variable namespaces (binary-confirmed)

### BKEDI.DUN.* — Trading partner DUNS mapping (BKEDIDUN table, 7 fields)

| Var | Field | Purpose |
|-----|-------|---------|
| BKEDI.DUN.DUNS | BKEDI_DUN_DUNS | Trading partner DUNS number (key) |
| BKEDI.DUN.CUST | BKEDI_DUN_CUST | Matching EvoERP customer code |
| BKEDI.DUN.EDI | BKEDI_DUN_EDI | Trading partner EDI ID qualifier (X12 ISA06/ISA08) |
| BKEDI.DUN.EFFDT | BKEDI_DUN_EFFDT | Effective date for this trading relationship |
| BKEDI.DUN.PRODS | BKEDI_DUN_PRODS | Product/UPC code mapping flag |
| BKEDI.DUN.ADVS | BKEDI_DUN_ADVS | Advance ship notice (ASN 856) enabled flag |
| BKEDI.DUN.SHPCD | BKEDI_DUN_SHPCD | Default ship-to code for this partner |

### BKEDI.MST.* — EDI master config (BKEDMSTR table, 3 fields)

| Var | Field | Purpose |
|-----|-------|---------|
| BKEDI.MST.PATH | BKEDI_MST_PATH | Path to CandoEDI import files (DBASO.IN location) |
| BKEDI.MST.DUNS | BKEDI_MST_DUNS | Our own DUNS number (sent as ISA06 in X12) |
| BKEDI.MST.NEXTN | BKEDI_MST_NEXTN | Next EDI import sequence number |

### BKEDI.NOTE.* — EDI order notes (BKEDNOTE table, 3 fields)

| Var | Field | Purpose |
|-----|-------|---------|
| BKEDI.NOTE.EDI | BKEDI_NOTE_EDI | EDI order number link |
| BKEDI.NOTE.SO | BKEDI_NOTE_SO | Converted SO number link |
| BKEDI.NOTE.NOTE | BKEDI_NOTE_NOTE | Note text |

---

## UI forms (3)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7EDII.DFM` | ED-I-I | 10 | 37 | 0 |
| `t7ediftp.DFM` | EDI  FTP Program | 7 | 9 | 0 |
| `t7edudf.DFM` | New Screen | 2 | 2 | 0 |

---

## Database tables (6)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) | Notes |
| ----- | ------------ | -----: | -------------------- | ----- |
| **BKEDIDUN** | `BKEDIDUN.B` | 7 | `BKEDI_DUN_CUST`, `BKEDI_DUN_DUNS`, `BKEDI_DUN_EDI` | Trading partner DUNS ↔ customer mapping |
| **BKEDIH** | `BKEDIH.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` | EDI staging header — byte-for-byte BKARINV clone |
| **BKEDIL** | `BKEDIL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` | EDI staging lines — byte-for-byte BKARINVL clone |
| **BKEDMSTR** | `BKEDMSTR.B` | 3 | `BKEDI_MST_NEXTN`, `BKEDI_MST_DUNS`, `BKEDI_MST_PATH` | CandoEDI path + our DUNS + counter |
| **BKEDNOTE** | `BKEDNOTE.B` | 3 | `BKEDI_NOTE_EDI`, `BKEDI_NOTE_SO`, `BKEDI_NOTE_NOTE` | Order notes linking EDI# to SO# |
| **BKEDPOST** | `BKEDPOST.B` | 2 | `BKEDI_POST_INVN`, `BKEDI_POST_CUST` | Export posting log |

---

## Multi-era implementations

The ED module has 4 implementation generations (DBA, ISEDI, NB, T6) all active on the
network share:

| Prefix | Era | Example | Note |
|--------|-----|---------|------|
| `BKED*` | DBA original | BKEDB.RUN | References CandoEDI in error messages |
| `ISEDI*` | IS/EvoIS era | ISEDIB.RUN | Adds ISEDINFOA table; otherwise same logic |
| `NBEDI*` | NB unknown | NBEDIB.RUN | Purpose unclear — may be network-backup variant |
| `t6edi*` / `T6EDI*` | TAS Pro 6 | t6edib.RUN | Full source tag: "t6edib.src DBA.LIB" |

ED-B dispatches to all four inbound programs depending on configuration.

---

## Live Data Analysis (Pass 421, 2026-06-30)

| Table | Count | Notes |
|-------|------:|-------|
| BKEDIH | 0 | EDI inbound order headers — not used at i2 Systems |
| BKEDIL | 0 | EDI inbound order lines — not used at i2 Systems |

**Key insight:** EDI is licensed but not actively used at i2 Systems — BKEDIH/BKEDIL are
empty. No X12 850 orders are being received electronically. The CandoEDI middleware and
all the BKED*/ISEDI* plumbing exists but is idle.

---

**Confidence: 90/100** — CandoEDI middleware architecture fully confirmed from binary
strings; 5 X12 transaction sets confirmed (850/860/810/855/856); variable namespaces
extracted; X12 version numbers confirmed N/A in EvoERP (configured in CandoEDI only);
live data confirms module is licensed but idle at i2 Systems (Pass421).
Remaining gap: internal CandoEDI format of DBASO.IN/DBASO.OUT flat files not analyzed
(CandoEDI proprietary format, no RUN file for it).
