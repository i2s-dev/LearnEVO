# Tier 11 — Module Archive and Extended Tables

Status: partial | Source: DDF field-name analysis (Pass 108)

Field meanings are inferred from names unless noted. All field lists extracted from
`samples/ddf/schema.json`.

## The EvoERP Archive Pattern

A key finding from analyzing these table families: **every major transaction module
has its own archive clone of the BKARINV/BKARINVL invoice record structure.** This
is how EvoERP implements historical retention — when records are purged from the live
tables, they are copied to module-specific archive tables.

| Live table | Module archive header | Module archive line |
|------------|----------------------|---------------------|
| BKARINV (84f) | ISSRAINV, ISSRCH, ISSRMH, ISSRMINV (SR) | ISSRAIVL, ISSRCL, ISSRMIVL, ISSRML |
| BKARINV (84f) | ISRMINV, ISRMAINV (RMA) | ISRMINVL, ISRMAIVL |
| BKARINV (84f) | ISSSOH, ISSSRH (SS staging) | ISSSOL, ISSSRL |
| BKAPPOL (38f) | ISAPOPOL, ISAPARFL (AP PO lines) | — |
| BKAPPO (57f) | ISAPOPO, ISAPARFQ (AP PO headers) | — |

All archive headers carry identical BKAR_INV_* or BKAP_PO_* field schemas —
structure is determined by the field prefix, not the table name.

### ISSR_INFO — Shared Service Record Info (54 fields)

The `ISSR_INFO_*` field prefix appears across multiple tables:
`ISSRAINF`, `ISSRHINF`, `ISSRINFO`, `ISSOAINF`, `ISSOHINF`, `ISSOINFO`,
`ISRMAINF`, `ISRMHINF`, `ISRMINFO`.

These 54-field records store service / RMA header metadata:
- `ISSR_INFO_SRNUM` — service record / order number (PK)
- `ISSR_INFO_UID` — user ID
- `ISSR_INFO_CODE` — status/type code
- `ISSR_INFO_DATE_1..5` — up to 5 date stamps (open/receive/close/etc.)
- `ISSR_INFO_AL_1..20` — 20 alphanumeric extra fields (custom data slots)

---

## ISSO* — SO Module IS Tables (10 tables)

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSOBOX | 22 | Shipping box detail (live) — ISSO_BOX_SONUM+LINE+BOX+CODE+QTY+LOT. Tracks how items are packed into boxes for SO shipment. PK: SONUM+LINE+BOX |
| ISSOABOX | 22 | Alternate/archive ISSOBOX (same structure) |
| ISSOHBOX | 22 | History ISSOBOX |
| ISSOAHBX | 22 | Another history box variant |
| ISSOINFO | 54 | SO service info record — ISSR_INFO_* (see above); current live copy |
| ISSOAINF | 54 | SO service info — archive copy |
| ISSOHINF | 54 | SO service info — history copy |
| ISSOALOT | 14 | SO lot transaction — BKAR_TXN_* (lot/serial movement from SO posting) |
| ISSOASER | 14 | SO serial transaction — same BKAR_TXN_* structure |
| ISSOREVU | 12 | SO review/approval — IS_SOVU_SONUM+DEPT+EMPNME+EMPNUM+MOTPAS+ADATE — SO approval workflow (requires department supervisor sign-off before release) |

**Key:** ISSOBOX (22f) is the packing slip / box contents table — each row is one item assigned to one box in one SO shipment. It feeds the Bill of Lading (BOL) module.

---

## ISSR* — Service Repair (SR) Archive Tables (21 tables)

The ISSR* family stores archived / historical SR module transactions. Like ISAR* for AR,
these are copies of SR records retained after purge.

### Invoice archive pairs

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSRAINV, ISSRCH, ISSRMH, ISSRMINV | 84 each | SR invoice header archive — BKAR_INV_* structure |
| ISSRAIVL, ISSRCL, ISSRMIVL, ISSRML | 28 each | SR invoice line archive — BKAR_INVL_* structure |
| ISSRHINF, ISSRAINF, ISSRINFO | 54 each | SR service info — ISSR_INFO_* (see above) |

### Service-specific tables

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSRFQH | 57 | SR RFQ / PO header — BKAP_PO_* structure — service vendor quote |
| ISSRFQL | 38 | SR RFQ / PO line — BKAP_POL_* structure |
| ISSRMMS, ISSRMMS | 12 | SR material / misc link — ISSR_MMS_SRVNUM+LINEID+INVNUM+WOPRE+WOSUF+PART — links SR service record to WO/invoice/part |
| ISSRTXN, ISSRTXNS | 14 each | SR inventory transaction — BKAR_TXN_* — inventory moves from SR |
| ISSRADSC, ISSRDESC | 5 each | SR description text lines — BK_DESC_CODE+NUM+LINE+NOTES+DESC |

---

## ISRM* — RMA Archive Tables (14 tables)

The ISRM* family stores Return Material Authorization data.

### RMA core record

| Table | Fields | Purpose |
|-------|--------|---------|
| ISRMAI | 54 | RMA item record — IS_RMA_NUM+PART+LINEID+DATE+RCPTDATE+CLOSDATE + ~48 more. Live current. |
| ISRMAAI | 54 | RMA archive item record — same structure as ISRMAI |

### Invoice archive copies

| Table | Fields | Purpose |
|-------|--------|---------|
| ISRMINV, ISRMAINV | 84 each | RMA invoice header — BKAR_INV_* |
| ISRMINVL, ISRMAIVL | 28 each | RMA invoice line — BKAR_INVL_* |
| ISRMHINF, ISRMAINF, ISRMINFO | 54 each | RMA service info — ISSR_INFO_* |

### Support tables

| Table | Fields | Purpose |
|-------|--------|---------|
| ISRMAC | 3 | RMA code/reason — IS_RMA_CODE+DESC+EXTRA — reason-code catalog |
| ISRMADSC, ISRMDESC | 5 each | RMA description text lines |
| ISRMTXN, ISRMTXNS | 14 each | RMA inventory transaction — BKAR_TXN_* |

---

## ISSS* — SO/SR Staging Tables (4 tables)

Work-area / staging tables used during SO and SR posting:

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSSOH | 84 | SO staging header — BKAR_INV_* (pre-post work area for SO invoice) |
| ISSSOL | 28 | SO staging line — BKAR_INVL_* |
| ISSSRH | 84 | SR staging header — BKAR_INV_* |
| ISSSRL | 28 | SR staging line — BKAR_INVL_* |

These are temporary records; they are written during the posting process, validated, then
either committed to live tables or discarded. Not retained long-term.

---

## ISST* — WO Production Scan Tracking (4 tables)

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSTRACK | 13 | WO scan tracking record — IS_STRACK_WOPRE+WOSUF+OPER+TIME+DATE+PROC + 7 more — logs each production scan event (barcode scan at a workstation) |
| ISSTEQUI | 3 | Equipment classification — IS_STYPE_TYPE+WHO+ASSET — asset tracking type |
| ISSTTYPE | 3 | Type code table (same structure as ISSTEQUI) |
| ISSTYPE | 3 | Scan type code catalog — IS_STYPE_TYPE+WHO+ASSET |

---

## ISPO* — PO Tracking / Receiving (7 tables)

| Table | Fields | Purpose |
|-------|--------|---------|
| ISPOBOX | 22 | PO receiving box — ISSO_BOX_* structure — packing boxes received against a PO |
| ISPOTRK | 7 | PO shipment tracking — IS_TRK_ORD+NUM+SHPVIA+CDATE+RDATE+STATUS — inbound shipment status (carrier/expected date/received date) |
| ISPOHTRK | 7 | PO history tracking — same structure as ISPOTRK |
| ISPOLOG | 9 | PO activity log — ISPO_LOG_EMP+DATE+TIME+WHO+PRGM+PONUM + 3 more — audit trail of PO accesses |
| ISPODESC | 1 | PO description code — single-field code table |
| ISPOS | 2 | PO supplier class — BKCM_ACCL_CODE+CLASS — supplier classification |
| ISPOSC | 2 | PO supplier category — BKCM_ACCC_CCODE+DESC — supplier category |

---

## ISAP* — AP Extended / Archive Tables (15 tables)

The ISAP* family extends the AP module with archive copies and extended data tables.

### Archive pairs (PO/vendor/check)

| Table | Fields | Purpose |
|-------|--------|---------|
| ISAPOPO | 57 | AP archive PO header — BKAP_PO_* (same as BKAPPO) |
| ISAPOPOL | 38 | AP archive PO line — BKAP_POL_* |
| ISAPARFQ | 57 | AP archive PO (FQ variant — pre-firmed/RFQ) |
| ISAPARFL | 38 | AP archive PO line (FL variant) |
| ISAPAVND | 72 | AP archive vendor — BKAP_VEND* — full vendor record snapshot |
| ISAPACHK | 12 | AP archive check — BKAP_CHK_VNDCOD+INVNUM+INVAMT+AMTPD+DISC+TYPE |
| ISAPAINL | 390 | AP archive invoice line — 390 fields (the largest AP table) — stores up to 75 GL distribution lines per invoice (26-period structure) |
| ISAPAINT | 19 | AP archive invoice transaction — BKAP_INVT_* |
| ISAPHQT | 49 | AP header quote — BKRFQ_* clone — AP-side RFQ record |

### Extended data tables

| Table | Fields | Purpose |
|-------|--------|---------|
| ISAPEX | 33 | AP extended vendor data — ISAPEX_VEND+LONGNAME+NUM_1..10 — 10 custom numeric fields per vendor |
| ISAPCHG | 32 | AP change log — ISAP_CHG_PONUM+LINEID+PCODE+CDATE+USER+REVLVL — tracks every field change on a PO with timestamp and user |
| ISAPHCHG | 32 | AP header change log — same structure as ISAPCHG |
| ISAPQPO | 66 | AP quote PO — ISAP_QPO_PCODE+PQTY+VNDCOD+PPRCE+PDISC+UM + 60 more — vendor price quotation for an item (price/discount/UOM per vendor) |
| ISAPPROJ | 12 | AP project link — ISAP_PROJ_FROM+CUST+VEND+JOURN+INV+LINE — links AP invoices to projects for job-cost allocation |

**Key:** ISAPAINL (390 fields) is one of the largest tables in the system. Like ISAPAINL in tier5 docs, it stores an archived invoice with up to 75 GL distribution lines embedded as arrays — this is how multi-department AP invoices are stored in an archival flat structure.

---

## ISPR* — Extended Payroll Tables (7 tables)

| Table | Fields | Purpose |
|-------|--------|---------|
| ISPRMSTR | 384 | IS extended payroll master — BKPR_EMP_NUM+FNMI+LNME+ADD+CSZ+ST + 378 more — IS-era extension to BKPRMSTR with additional payroll fields. One of the largest tables. |
| ISPRSALE | 87 | IS payroll sales class rates — BKPR_SLS_EMPNUM + CLASS_1..N + RATE_1..N + HOW_1..N arrays — commission/rate structure by employee and sales class |
| ISPREQ | 25 | WO labor request — IS_PREQ_WOPRE+WOSUF+OPER+WC+EMP+RDATE + 19 more — pre-approved labor request linked to a specific WO operation |
| ISPRTEMP | 15 | Payroll GL temp — ISPR_TRN_GLACCT+GLDPT+DATE+CODE+INVC+DESC + 9 more — GL staging table for payroll journal entries |
| ISPRUDF | 31 | Payroll user-defined fields — ISPR_UDF_DIV+DIVNAM+NUM+DESC+FIT+FUTA + 25 more — custom per-division payroll setup (FIT/FUTA rates etc.) |
| ISPRESN | 1 | Payroll reason code — IS_PRESN_REASON (single field) |
| ISPRINFO | 4 | Payroll program info — ISPR_INFO_PROG+DESC+MISC+TYPE — program/module info record |

**Key:** ISPREQ (25f) is the **WO labor authorization** table — before labor can be posted to a WO operation, a request record is created here. This connects the payroll module to the WO module for labor cost control.

---

## IS-Custom Manufacturing Spec Tables (Pass 547, 2026-07-02)

These tables are used exclusively by J7 custom programs (not standard T7*/T6* programs).
Confirmed from rwn_symbols.json J7 DB access analysis.

### ISCONVRT — Unit Conversion Table (9 fields)

| Field | Notes |
|-------|-------|
| IS.CONV.ITEM | Item code (PK) — item requiring non-standard conversion |
| IS.CONV.PUM | Purchasing unit of measure (e.g. LB, EA, FT) |
| IS.CONV.SUM | Stocking unit of measure |
| IS.CONV.WTCONV | Weight conversion factor (numeric) — converts between PUM and SUM |

Used by J7RCCONVTABLE (manage conversion factors) and J7RCPITEX (RC Physical
Inventory Tax Export — converts purchased weight to stocked units for tax reporting).
ISCONVRT supplements the standard per-item UOM conversion fields in BKICMSTR;
it is used for items in the RC customer system that require a different conversion
rate than the standard item master.

### ISCCICM — Mattress Cover/Fabric Product Specification (59 fields, all confirmed)

Extended item specification for mattress cover and fabric products.
Keyed by item CODE (item code). Used by T7CCCITM (CC-C item maintenance) and
J7CCITEMSYNC (item sync). Full 59-field DDF schema confirmed from fields-misc.md.

**Key fields (selected from 59 total):**

| Field | Type | Notes |
|-------|------|-------|
| ISCC_ICM_CODE | STRING(15) | Item code (PK) |
| ISCC_ICM_CUST | STRING(60) | Customer code / customer-specific variant |
| ISCC_ICM_DESC | STRING(30) | Description |
| ISCC_ICM_DESC2 | STRING(30) | Description line 2 |
| ISCC_ICM_PNAME | STRING(60) | Product name (marketing name) |
| ISCC_ICM_COLLEC | STRING(120) | Collection/line name |
| ISCC_ICM_FSIZE | STRING(30) | Finished size (mattress dimensions) |
| ISCC_ICM_FABRIC | STRING(60) | Fabric/ticking material description |
| ISCC_ICM_TCOLOR | STRING(60) | Ticking color |
| ISCC_ICM_STRIPE | STRING(25) | Stripe/pattern |
| ISCC_ICM_CUSHTY | STRING(60) | Cushion type (comfort level) |
| ISCC_ICM_POLY | STRING(20) | Polyurethane foam specification |
| ISCC_ICM_CONST | STRING(60) | Construction description |
| ISCC_ICM_FILIT_1..4 | STRING(15) each | Fill material types 1-4 (mattress layers) |
| ISCC_ICM_FILQTY_1..4 | STRING(20) each | Fill quantities 1-4 |
| ISCC_ICM_LAWLAB | STRING(60) | Law label text (US federal mattress label requirement) |
| ISCC_ICM_SEWNOT | STRING(60) | Sewing notation/instruction |
| ISCC_ICM_HINGE | STRING(25) | Handle/hinge attachment type |
| ISCC_ICM_BTNCOD | STRING(25) | Button/binding code |
| ISCC_ICM_BTNQTY | NUMERIC(8) | Button/binding quantity |
| ISCC_ICM_TIECOD | STRING(25) | Ticking tie code |
| ISCC_ICM_TIEMTR | STRING(30) | Tie material |
| ISCC_ICM_TIEQTY | NUMERIC(8) | Tie quantity |
| ISCC_ICM_FABLAB | STRING(60) | Fabric label text |
| ISCC_ICM_LABLOC | STRING(60) | Label location (where to sew label on cover) |
| ISCC_ICM_SOLIDF | STRING(25) | SolidWorks CAD file path (3D model reference) |
| ISCC_ICM_PDF | STRING(60) | PDF spec sheet path |
| ISCC_ICM_AMTPP | STRING(25) | Amount per piece |
| ISCC_ICM_PERCOM | STRING(25) | Per-component |
| ISCC_ICM_SPY | STRING(25) | Selling price Y |
| ISCC_ICM_BOXNO | STRING(30) | Box number |
| ISCC_ICM_BOXQTY | STRING(30) | Box quantity |
| ISCC_ICM_CVL | STRING(25) | Cover level |
| ISCC_ICM_CUBE | STRING(30) | Cubic feet/inches |
| ISCC_ICM_CWEIGH | NUMERIC(8,6) | Component weight |
| ISCC_ICM_HAVPIC | STRING(60) | Has picture flag |

Used by T7CCCITM (CC-C item maintenance) and J7CCITEMSYNC to sync mattress cover specs
between BKICMSTR (standard item master) and ISCCICM + ISICMSTR. Also opens BKBMDIM,
BKRTSPEC, BKBMMSTR, BKBMNOTE, BKBMREMK for complete routing+BOM spec management.

**Note:** Earlier documentation described this as "door hardware" based on HINGE/SPY/SOLIDF
fields only — full schema confirmed as **mattress cover manufacturing** via FABRIC/TCOLOR/
STRIPE/CUSHTY/POLY/LAWLAB/SEWNOT fields. SPY = Selling Price Y (not "spy hole").
