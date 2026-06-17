# Service / Repair (SR)

Status: partial — RWN symbols analyzed 2026-06-17.

- **Module code**: `SR`
- **UI forms**: 12 (T7SR*.DFM)
- **RWN programs**: 16 (T7SRA, T7SRB, T7SRBK, T7SRC, T7SRD, T7SRDISPACH, T7SRE, T7SRF, T7SRG, T7SRGA, T7SRI, T7SRINFO, T7SRK, + stubs)
- **Menu operations**: 9

---

## Key architecture finding: Service Orders are BKARINV records

Service Orders in EvoERP are AR invoices — they use the same table (BKARINV) as Sales Orders
and AR invoices. This is the same pattern as the SO module. The ISSR* DDF entries are Btrieve
alternate-index definitions pointing to the same physical data files, not separate tables.

Confirmed: ISSRAINV, ISSRINV, ISSRMH, ISSRMINV, ISSRCH are all 84-field views of BKARINV
(0 field difference). ISSRAIVL, ISSRINVL, ISSRMIVL, ISSRML, ISSRCL are all 28-field views
of BKARINVL (0 field difference).

---

## Menu operations

| Code | Operation | RWN file |
| ---- | --------- | -------- |
| `SR-A` | View/Enter Service/Repair Orders | T7SRA.RWN (also ISSRA legacy) |
| `SR-B` | Print S/R or Quotes | T7SRB.RWN |
| `SR-C` | Convert Service/Repair Orders | T7SRC.RWN |
| `SR-D` | Print S/R Pick Ticket | T7SRD.RWN |
| `SR-E` | Release Service/Repair Orders | T7SRE.RWN |
| `SR-F` | Print/Reprint S/R Invoices | T7SRF.RWN |
| `SR-G` | Post Service/Repair Invoices | T7SRG + T7SRGA.RWN |
| `SR-H` | Convert RMA Orders | (T6-era ISSRH) |
| `SR-I` | SR Invoice Inquiry | T7SRI.RWN |
| `SR-K` | Equipment Master (Make/Model/Serial) | T7SRK.RWN |
| `SR-T` | View Service/Repair Orders (alt) | T7SRA / ISSRA2 |
| `SR-DISPATCH` | Dispatch Manager | T7SRDISPACH.RWN |
| `SR-INFO` | S&R Misc. Information | T7SRINFO.RWN |
| `SR-BK` | Live Work Center Schedule / Backflush | T7SRBK.RWN |

---

## Workflow

```
SR-A entry (T7SRA) → equipment via ISSRMMS
         ↓
SR-B print / SR-D pick ticket
         ↓
SR-E release (T7SRE) — issues parts from WO, posts INVTXN
         ↓
SR-F invoice print (T7SRF) → SR-G post (T7SRGA) → BKGLTRAN + BKGLX
         ↓
SR-I inquiry (T7SRI) — review posted service invoices
```

---

## SR-specific tables

### ISSRMMS — Service Equipment (Make/Model/Serial)
12 fields — one row per equipment item per service order line.

| Field | Type | Size | Meaning |
|---|---|---|---|
| ISSR_MMS_SRVNUM | FLOAT | 8 | Service order number (FK → BKARINV) |
| ISSR_MMS_LINEID | UBINARY | 2 | Line ID within service order |
| ISSR_MMS_INVNUM | FLOAT | 8 | Invoice number (FK → BKARINV) |
| ISSR_MMS_WOPRE | FLOAT | 8 | Work order prefix (FK → WORKORD) |
| ISSR_MMS_WOSUF | UBINARY | 2 | Work order suffix |
| ISSR_MMS_PART | STRING | 15 | Part/item code (FK → BKICMSTR) |
| ISSR_MMS_MAKE | STRING | 50 | Equipment make |
| ISSR_MMS_MODLE | STRING | 50 | Equipment model |
| ISSR_MMS_SERIAL | STRING | 50 | Serial number |
| ISSR_MMS_INDATE | DATE | 4 | Equipment received date |
| ISSR_MMS_OUTDTE | DATE | 4 | Equipment returned date |
| ISSR_MMS_EXTRA | STRING | 150 | Extra notes |

### ISSRINFO — Service Order Extended Info
54 fields — 20 configurable alpha slots × 25 chars + 5 date slots (× 2 groups = 40 alpha + 10 dates).

Primary key: ISSR_INFO_SRNUM + ISSR_INFO_UID
- ISSR_INFO_CODE (15) — config code defining what the alpha/date slots mean
- ISSR_INFO_DATE_1..5 (date) — first group of 5 dates
- ISSR_INFO_ALPHA_1..20 (25 each) — first group of 20 alpha fields
- ISSR_INFO_DATE1..5 (date) — second group of 5 dates (EXTRA at offset 651)
- ISSR_INFO_AL1..20 (25 each) — second group of 20 alpha fields
- Total capacity: 40 alpha values + 10 dates per service record

### ISARINVX — AR Invoice Extension
4 fields. Hangs off BKARINV to add two extra 100-char text fields.
- ISAR_INV_SONUM + ISAR_INV_NUM (PK)
- ISAR_INV_EXTRA1 (100), ISAR_INV_EXRTA2 (100, typo in DDF name)

### ISSOREVU — SO/SR Approval Workflow
12 fields — department-level approval gate for service (and SO) orders.
- IS_SOVU_SONUM (8) — order number (PK part 1)
- IS_SOVU_DEPT (25), IS_SOVU_EMPNME (25), IS_SOVU_EMPNUM (2) — reviewer
- IS_SOVU_MOTPAS (10) — manager override password
- IS_SOVU_ADATE/EDATE (dates) — approval/effective dates
- IS_SOVU_APPROVE (1), IS_SOVU_REQUIRE (1) — approval status flags
- IS_SOVU_ENTBY (25), IS_SOVU_ENTMOT (10) — entered by + manager
- IS_SOVU_EXTRA (100)

### ISSRFQH / ISSRFQL — Service RFQ Header / Lines
57 / 38 fields — uses BKAP_PO_* and BKAP_POL_* field prefixes.
Service RFQs (requests for quote on service parts/labor) are built on the PO infrastructure.
- ISSRFQH: all fields identical in structure to BKAPPO (57f)
- ISSRFQL: all fields identical in structure to BKAPPOL (38f)

### Supporting SR tables (small)
- **ISSDET** (4f) — Service detail codes: IS_SDET_TYPE + IS_SDET_DETAIL + IS_SDET_WHO + IS_SDET_SUB
- **ISORDECO** (13f) — Order decoration/special instructions: SONUM + PONUM + UNUM + PART + DRAW + ...
- **ISNTYPE** (4f) — Note type codes: TYPE(3) + DESC(30) + SEC(security level) + EXTRA(100)
- **ISUDFINV** (8f) — User-defined invoice field mapping: maps custom field names to byte offsets in BKARINV
- **BKISTAX** (13f) — Historical tax totals by code/date: TAX_CODE + DATE + TRFLAG + TAXABL + NONTAX + ...
- **BKARHTAX** (5f) — Historical AR tax per invoice: INVNO + CODE + ID + PID + AMOUNT
- **ISARTXNB** (23f) — AR transaction batch: SONUM + CODE + LINEID + BIN + LOC + ...

---

## UI forms (12)

| DFM file | Caption | Fields | Controls |
| -------- | ------- | -----: | -------: |
| T7SRB.DFM | SR-B (print options) | 22 | 50 |
| T7SRBK.DFM | Live Work Center Schedule | 6 | 25 |
| T7SRD.DFM | SR-D (pick ticket) | 28 | 59 |
| T7SRE.DFM | SR-E (release) | 0 | 1 |
| T7SRF.DFM | SO-F (invoice print — shared with SO) | 56 | 109 |
| T7SRG.DFM | SRG (post options) | 7 | 29 |
| T7SRGA.DFM | SR-G-A Order Posting | 2 | 7 |
| T7SRI.DFM | SR-I (inquiry) | 26 | 61 |
| T7SRINFO.DFM | S&R Misc. Information | 26 | 61 |
| T7SRK.DFM | SR-K (equipment — blank wrapper?) | 0 | 1 |
| T7SRMMS.DFM | Make, Model and Serial Number | 6 | 21 |
| T7SRS.DFM | SR-S (blank wrapper?) | 0 | 1 |

---

## Notes

- T7SRF.DFM caption is "SO-F" — SR invoicing reuses the same form as SO invoicing.
- T7SRA is the main entry but it was not found at first via DFM search (no T7SRA.DFM);
  the RWN exists with 15 procs and opens ISSDET, WORKORD, ISSPC, ISSERR.
- T7SRGA opens the most tables of any SR program (45+ unique tables) — it is the
  full AR/GL posting routine for service invoices.

**Confidence: 72/100** — Workflow and key tables confirmed from RWN symbols;
individual form field meanings and per-operation business logic need DFM deep-read.
