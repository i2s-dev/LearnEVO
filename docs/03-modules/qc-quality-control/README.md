# Quality Control (QC)

Status: verified | Pass 436 (2026-07-01)

- **Module code**: `QC`
- **Tables**: 4 (`BKQCMSTR`, `BKQCTRAN`, `ISNCR`, `ISCAR`)
- **UI forms**: 15 (prefixes `T7QC`, `T6QC`, `T7DSQC`)
- **Menu operations**: 20 (QC-A through QC-H, QC-F and QC-G each have sub-menus)

> **Note:** `menu_codes.csv` has NO entries for QC — the QC module codes were not exported
> into that file. All menu codes below are confirmed from `samples/BKMENUSU.TXT` directly.

→ See **[help-content.md](help-content.md)** for user-facing vendor help text
(QC-A through QC-G-A: 11 topics from `EvoHELP.CHM`).

---

## Three-tier architecture

The QC module has three distinct subsystems:

1. **Receiving QC (PO-side)** — records quantity received, bought off, and rejected per PO
   receipt. Data flows from `PO-J-C Enter Inspection Buyoffs` into `BKQCMSTR` + `BKQCTRAN`.
   Reports: QC-A (by vendor/item), QC-E (vendor performance).

2. **Production scrap / WO-side QC** — records scrap during WO material issuance (WO-G)
   and Parts Requester (WO-K-M, WO-K-R). Reports: QC-B (materials scrap), QC-C (production
   scrap), QC-D (labor quality, includes employee filter).

3. **Non-Conformance Report (NCR) + Corrective Action Report (CAR)** — formal QMS tracking
   in `ISNCR` / `ISCAR`. Entered via `QC-F-A Enter NCR`, dispositioned via `QC-F-C`, closed
   via `QC-F-D`. CARs linked to NCRs via `IS_NCR_CAR` field.

---

## Menu operations (20)

| Code | Operation | Program |
|------|-----------|---------|
| `QC-A` | Quality Control Receiving Report | T7QCA.RWN |
| `QC-B` | Quality Control Materials Report | T7QCB.RWN |
| `QC-C` | Production Scrap Report | T7QCC.RWN |
| `QC-D` | Quality Control Labor Report | T7QCD.RWN |
| `QC-E` | Vendor Quality Performance | t7pojd.RWN (shared with PO-J-D) |
| `QC-F` | Non-Conformance Reporting *(sub-menu)* | — |
| `QC-F-A` | Enter NCR | T7QCFA.RWN |
| `QC-F-B` | Print NCR | T7QCFB.RWN |
| `QC-F-C` | Disposition NCR | T7QCFC.RWN |
| `QC-F-D` | Close NCR | T7QCFD.RWN |
| `QC-F-E` | View NCR | T7QCFE.RWN |
| `QC-F-F` | NCR Listing | T7QCFF.RWN |
| `QC-G` | Corrective Action *(sub-menu)* | — |
| `QC-G-A` | Enter CAR | T7QCGA.RWN |
| `QC-G-B` | Print CAR | T7QCGB.RWN |
| `QC-G-C` | View CAR | T7QCGC.RWN |
| `QC-G-D` | List CAR | T7QCGD.RWN |
| `QC-H` | QC Defaults | T7DSQC.RWN |

Also accessible from other modules:
| Code | Module | Description |
|------|--------|-------------|
| `PO-J-B` | PO | Print Inventory in QC → t7pojb.RWN |
| `PO-J-D` | PO | Vendor Quality Performance Report → t7pojd.RWN |
| `LM-H` | LM | Purge QC Receipts |
| `RO-F` | RO | Enter QC Codes (routing scrap codes) |
| `RO-J-E` | RO | Print QC Codes |
| `RO-M` | RO | Enter Testing Method → t7qcmthd.RWN |
| `RO-N` | RO | Enter Testing Requirements → t7qcspec.RWN |

---

## UI forms (15 in samples/dfm/)

| DFM file | Caption (from DFM) | Purpose |
|----------|--------------------|---------|
| `T7QCA.DFM` | New Screen | QC-A filter: Date/Item/ItemClass/Vendor/QC+Scrap Code ranges |
| `T7QCB.DFM` | New Screen | QC-B filter: Date/ParentItem/WO/ComponentItem ranges, active/archived toggle |
| `T7QCC.DFM` | New Screen | QC-C filter: Date/ParentItem/ScrapCode/WO ranges, active/archived toggle |
| `T7QCD.DFM` | New Screen | QC-D filter: Date/ParentItem/QC+Scrap/WO/Employee/SeqNum ranges |
| `T7QCFA.DFM` | New Screen | QC-F-A NCR entry form (39 fields — see NCR field detail below) |
| `T7QCMTHD.DFM` | Enter Testing Method | RO-M: Test code + description + revision + date (per-routing) |
| `T7QCRESULTS.DFM` | QC Testing Results | Testing results report filter: WO#/Item#/QC Report# ranges |
| `T7QCRSLT.DFM` | New Screen | QC results entry (stub/launcher form, 0 fields) |
| `T7QCSPEC.DFM` | Enter Testing Requirements | RO-N: Test# + min/max + units + I/B batch mode per item |
| `t7qcfb.DFM` | New Screen | QC-F-B: Print NCR filter |
| `t7qcgb.DFM` | New Screen | QC-G-B: Print CAR filter |

> DFMs for QC-F-C (Disposition NCR), QC-F-D (Close NCR), QC-F-E (View NCR),
> QC-G-A (Enter CAR), QC-G-C/D (View/List CAR), and T7DSQC (QC Defaults)
> are not in `samples/dfm/` — they exist on the network share but were not copied.

---

## Database tables

### BKQCMSTR — QC Receiving Events (14 fields)

One record per PO receive event. Written by `PO-J-C Enter Inspection Buyoffs`.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKQC_VEND_CODE` | STRING | 10 | Vendor code (PK 1) |
| `BKQC_RECV_DATE` | DATE | 4 | Receipt date (PK 2) |
| `BKQC_PO_NUM` | FLOAT | 8 | PO number (PK 3) |
| `BKQC_RECVR_NUM` | FLOAT | 8 | Receiver number |
| `BKQC_POL_ITM_NO` | STRING | 10 | Item / part number received |
| `BKQC_PKSLIP_NUM` | STRING | 15 | Packing slip number |
| `BKQC_QTY_RECVD` | FLOAT/2dec | 8 | Quantity received |
| `BKQC_QTY_BUYOFF` | FLOAT/2dec | 8 | Quantity accepted (bought off) |
| `BKQC_QTY_REJECT` | FLOAT/2dec | 8 | Quantity rejected |
| `BKQC_PKSLIP_QTY` | FLOAT/2dec | 8 | Packing slip stated quantity |
| `BKQC_PROD_CODE` | STRING | 15 | Product code |
| `BKQC_UNIT_COST` | FLOAT/4dec | 8 | Unit cost |
| `BKQC_EXTRA` | STRING | 25 | Extra / user-defined |
| `BKQC_OUT_DATE` | DATE | 4 | Out / disposition date |

**Live data (i2 Systems, DSN=DBA):**
| Metric | Value |
|--------|------:|
| Total receive events | 53,300 |
| Total qty received | 90,391,770 |
| Total qty bought off | 88,814,517 |
| Total qty rejected | 1,564,898 |
| Overall rejection rate | ~1.73% |
| Active through | 2026-06-30 (module is current) |

### BKQCTRAN — QC Transaction Detail (21 fields)

One record per part number within a receive event. Linked to BKQCMSTR.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKQC_TRN_PO` | FLOAT | 8 | PO number (FK → BKQCMSTR) |
| `BKQC_TRN_VEND` | STRING | 10 | Vendor code |
| `BKQC_TRN_CODE` | STRING | 15 | Part number being inspected |
| `BKQC_TRN_RECNUM` | FLOAT | 8 | Receiver number |
| `BKQC_TRN_GQTY` | FLOAT/4dec | 8 | Gross quantity |
| `BKQC_TRN_BQTY` | FLOAT/4dec | 8 | Buyoff (accepted) quantity |
| `BKQC_TRN_UQTY` | FLOAT/4dec | 8 | Unknown/uncertain quantity |
| `BKQC_TRN_SCRAP` | STRING | 2 | Scrap code (2-char) |
| `BKQC_TRN_REWORK` | STRING | 2 | Rework code (2-char) |
| `BKQC_TRN_PODTE` | DATE | 4 | PO date |
| `BKQC_TRN_ARDTE` | DATE | 4 | Arrival date |
| `BKQC_TRN_BODTE` | DATE | 4 | Buyoff date |
| `BKQC_TRN_EMPNUM` | UBINARY | 2 | Employee number (inspector) |
| `BKQC_TRN_RECVNM` | FLOAT | 8 | Receiver number (duplicate reference) |
| `BKQC_TRN_FAULT` | STRING | 1 | Fault flag |
| `BKQC_TRN_BROKEN` | STRING | 1 | Broken flag |
| `BKQC_TRN_FIXQTY` | FLOAT/4dec | 8 | Quantity fixed/reworked |
| `BKQC_TRN_POQTY` | FLOAT/4dec | 8 | PO line quantity |
| `BKQC_TRN_INVCD` | STRING | 1 | Inventory code |
| `BKQC_TRN_FLAG` | STRING | 1 | Processing flag |
| `BKQC_TRN_EXTRA` | STRING | 100 | Extra / user-defined (100 chars) |

**Live data:** 54,216 records; avg 1.02 items per receive event.

### ISNCR — Non-Conformance Report Master (27 fields)

One record per NCR. Written by `QC-F-A Enter NCR`.

| Field | Type | Meaning |
|-------|------|---------|
| `IS_NCR_NUM` | FLOAT | NCR number (PK) — sequential 1..N |
| `IS_NCR_PART` | STRING/15 | Parent part number (item being non-conformed) |
| `IS_NCR_COMP` | STRING/15 | Component part number (if WO component is the defect source) |
| `IS_NCR_LOT` | STRING/15 | Lot number |
| `IS_NCR_SERIAL` | STRING/25 | Serial number |
| `IS_NCR_CDATE` | DATE | Created date |
| `IS_NCR_WHO` | STRING/15 | Created by (user code) |
| `IS_NCR_QTY` | FLOAT/2dec | Non-conforming quantity |
| `IS_NCR_DCODE` | STRING/10 | Defect code |
| `IS_NCR_DESC` | STRING/60 | Description of non-conformity |
| `IS_NCR_ICR` | STRING/1 | Inventory Check Required flag |
| `IS_NCR_ORIG` | STRING/1 | Origin: `I`=In-house, `V`=Vendor |
| `IS_NCR_WOPRE` | FLOAT | Work Order prefix (for in-house NCRs) |
| `IS_NCR_WOSUF` | UBINARY | Work Order suffix |
| `IS_NCR_MACH` | STRING/4 | Machine code |
| `IS_NCR_TOOL` | STRING/15 | Tool code |
| `IS_NCR_WC` | STRING/12 | Work Center |
| `IS_NCR_PONUM` | FLOAT | PO number (for vendor-origin NCRs) |
| `IS_NCR_RMA` | FLOAT | RMA number |
| `IS_NCR_ACTION` | STRING/1 | Corrective Action Required flag |
| `IS_NCR_CAR` | FLOAT | CAR number (FK → ISCAR when CAR is created) |
| `IS_NCR_DISP` | STRING/10 | Disposition code |
| `IS_NCR_DWHO` | STRING/15 | Dispositioned by |
| `IS_NCR_DDATE` | DATE | Dispositioned date |
| `IS_NCR_STATUS` | STRING/1 | Status: `O`=Open, `C`=Closed |
| `IS_NCR_SCRAP` | STRING/2 | Scrap code |
| `IS_NCR_QC` | STRING/2 | QC code |

**Live data (i2 Systems):**
| Metric | Value |
|--------|-------|
| Total NCRs | 74 |
| Date range | 2020-02-12 to 2026-06-11 |
| NCR# range | 1 to 74 |
| All status | O (Open) — none closed in this installation |
| Origin: I (In-house) | 45 |
| Origin: V (Vendor) | 29 |
| IS_NCR_ACTION | all blank — no CARs have been triggered |

### ISCAR — Corrective Action Report (same structure as ISNCR)

ISCAR uses identical field names to ISNCR (`IS_NCR_*` prefix — DBA/EVO naming artifact).
**Live data: 0 records** — the CAR process has never been used at i2 Systems.

---

## NCR Workflow

```
QC-F-A Enter NCR
  → Create ISNCR record
    IS_NCR_ORIG = I (In-house) or V (Vendor)
    IS_NCR_PART = item, IS_NCR_QTY = qty, IS_NCR_DESC = description
    For I: WO#/WC/Machine/Tool captured
    For V: PO#/RMA# captured
    IS_NCR_STATUS = 'O' (Open)

QC-F-B Print NCR
  → Print formal NCR document from ISNCR

QC-F-C Disposition NCR
  → Set IS_NCR_DISP (disposition code), IS_NCR_DWHO, IS_NCR_DDATE
  → Set IS_NCR_SCRAP (scrap code) or IS_NCR_QC (QC code)
  → Optionally set IS_NCR_ACTION = 'Y' → triggers CAR creation

QC-F-D Close NCR
  → Set IS_NCR_STATUS = 'C' (Closed)

QC-G-A Enter CAR (if action required)
  → Create ISCAR record linked via IS_NCR_CAR
  → Formal corrective action tracking
```

---

## Notes & open questions

- All 74 live NCRs have status `O` (Open) — EvoERP's "Close NCR" step has never been
  used at i2 Systems. This likely means NCR closure is handled outside EvoERP (e.g. manually
  in a separate QMS system).
- `IS_NCR_ACTION` is blank on all records → the EvoERP CAR workflow (QC-G) has never been
  triggered. The ISCAR table has 0 records confirming this.
- `BKQC_TRN_SCRAP` and `BKQC_TRN_REWORK` are 2-char codes — same format as BKYS.YN[QC code]
  config values. Mapping to RO-F QC code definitions is inferred.
- T7QCMTHD (Enter Testing Method) and T7QCSPEC (Enter Testing Requirements) are accessed from
  RO-M and RO-N respectively — they are part of the **Routings** module's quality setup, not
  the standalone QC menu. They define per-routing-operation test specs used by
  T7QCRESULTS (QC Testing Results report).
