# EvoERP Data Dictionary — Tier 4 Tables

Status: partial — extracted from Pervasive DDF schema 2026-06-17.

---

## BKCM* Family — Contact Manager (CM Module)

The `BKCM*` prefix = **Contact Manager** (EvoERP's internal CRM system). 46 tables total.
Used by the CM module (CM-A through CM-J menu codes) for prospect/customer relationship tracking.

### Family overview

| Table | Fields | Purpose |
|---|---|---|
| BKCMACCN | 154 | Account contact names — up to 30+ contacts per account |
| BKCMCUST | 106 | CM customer view — mirrors BKARCUST fields for CM context |
| BKCMMHST | 72 | Marketing history — activity codes + dates per item |
| BKCMACCT | 41 | CM account master — name, address, contacts |
| BKCMDE | 41 | CM data exchange / EDI variant |
| BKCMEACT | 41 | CM e-commerce account |
| BKCMDUN | 36 | D&B (Dun & Bradstreet) integration data |
| BKCMPCNT | 24 | CM prospect contact |
| BKCMACTH | 21 | Account history |
| BKCMEACH | 21 | E-commerce account history |
| BKCMREP | 14 | Sales rep table |
| BKCMCNTD | 12 | Contact detail |
| BKCMACTF | 11 | Account flags |
| BKCMEACF | 11 | E-commerce account flags |
| BKCMTERR | 11 | Sales territory |
| … | … | 31 additional smaller tables |

### BKCMACCT — CM Account Master (41 fields)

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKCM_ACCT_CODE | STRING | 10 | Account code (primary key) |
| BKCM_ACCT_OLDCD | STRING | 10 | Old/legacy account code |
| BKCM_ACCT_ALPHA | STRING | 6 | Alpha sort key |
| BKCM_ACCT_NAME | STRING | 30 | Account name |
| BKCM_ACCT_ADD1/2/3 | STRING | 30 | Address lines |
| BKCM_ACCT_CITY | STRING | 26 | City |
| BKCM_ACCT_STATE | STRING | 2 | State |
| BKCM_ACCT_ZIP | STRING | 10 | Zip code |
| BKCM_ACCT_CNTRY | STRING | 30 | Country |
| BKCM_ACCT_CONT1 | STRING | 30 | Primary contact name |

### BKCMACCN — Account Contact Names (154 fields)

Stores up to 10 contacts per account. Each contact has: name, title, phone, fax, email, and custom fields.

Key pattern: BKCM_ACCN_CONT_1..10 (30 chars each), BKCM_ACCN_TITLE_1..10, BKCM_ACCN_PHONE_1..10, etc.

### BKCMREP — Sales Rep Table (14 fields)

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKCM_REP_REP | STRING | 5 | Rep code (primary key) |
| BKCM_REP_FNMEMI | STRING | 25 | First name / middle initial |
| BKCM_REP_LNAME | STRING | 25 | Last name |
| BKCM_REP_EMP | UBINARY | 2 | Employee number |
| BKCM_REP_PSWD | STRING | 10 | Rep password |
| BKCM_REP_DHCODE | STRING | 2 | Default hour code |
| BKCM_REP_DFCODE | STRING | 3 | Default frequency code |
| BKCM_REP_DDCODE | STRING | 2 | Default duration code |
| BKCM_REP_VIEW | STRING | 1 | View permission (Y/N) |
| BKCM_REP_CHANGE | STRING | 1 | Change permission (Y/N) |
| BKCM_REP_GWARN | STRING | 1 | Goal warning flag (Y/N) |
| BKCM_REP_AADD | STRING | 1 | Auto-add flag (Y/N) |
| BKCM_REP_GMTRX | STRING | 1 | Goal matrix flag |
| BKCM_REP_DGMTR | STRING | 1 | Default goal matrix |

**Note:** BKCM_REP_PSWD is a separate password for CM access, distinct from the EvoERP
login password in AHSYLOG. Reps can have their own CM login with limited access.

### BKCMMHST — Marketing History (72 fields)

Tracks marketing activities per item (call, visit, mailing, etc.):
- BKCM_MHST_MCODE (15) — item/prospect code
- BKCM_MHST_DESC (25) — activity description
- BKCM_MHST_MDATE — activity date
- BKCM_MHST_CLASS_1..9 — up to 9 classification codes (5 chars each)
- Additional date, amount, and flag fields

---

## ISLBLMAP — Label Definition / Mapping Table

**Purpose:** Maps items and customers to label print templates (`.RTM` files).
Each row defines one label variant for an item, with per-field color customization.

This is the core of EvoERP's label printing system. The J7DCMatLabels (mattress label)
and J7CCSOLabels (corrugated box label) modules read from this table.

Primary key: IS_LABEL_ITEM + IS_LABEL_NUM
Record size: ~893 bytes, 102 fields

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | IS_LABEL_ITEM | STRING | 15 | Item/part number |
| 15 | IS_LABEL_NUM | STRING | 15 | Label number/variant code |
| 30 | IS_LABEL_DESC | STRING | 30 | Label description |
| 60 | IS_LABEL_DFLT | STRING | 1 | Default label flag (Y/N) |
| 61 | IS_LABEL_OBS | STRING | 1 | Obsolete flag (Y/N) |
| 62 | IS_LABEL_CDATE | DATE | 4 | Created date |
| 66 | IS_LABEL_EDATE | DATE | 4 | Expiry date (when label becomes obsolete) |
| 70 | IS_LABEL_CUST | STRING | 10 | Customer code (customer-specific label) |
| 80 | IS_LABEL_VEND | STRING | 10 | Vendor code (vendor-specific label) |
| 90 | IS_LABEL_RTM | STRING | 12 | **ReportBuilder template name** (the .RTM file used to print this label) |
| 102–189 | IS_LABEL_NTYPE_1..30 | STRING | 3 each | 30 note type codes — identifies which data field to place at each label position |
| 192–491 | IS_LABEL_FCOLOR_1..30 | STRING | 10 each | Foreground color per field slot (30 slots) |
| 492–791 | IS_LABEL_BCOLOR_1..30 | STRING | 10 each | Background color per field slot (30 slots) |
| 792 | IS_LABEL_FLAG | STRING | 1 | User flag |
| 793 | IS_LABEL_EXTRA | STRING | 100 | Extra notes |

**Key insight:** IS_LABEL_RTM points to the `.RTM` report template that handles layout.
The IS_LABEL_NTYPE_1..30 array assigns data sources to label fields; the
IS_LABEL_FCOLOR / IS_LABEL_BCOLOR arrays allow per-field color customization.

The label system allows one item to have multiple label variants (different templates for
different customers, or standard vs. promotional labels). IS_LABEL_DFLT = 'Y' selects the
default when no explicit variant is requested.

---

## IS2DBAR — 2D Barcode Field Configuration

**Purpose:** Configures which data fields are encoded in 2D barcodes per item,
and which document types include the barcode.

Used by the DC/handheld barcode scanning system for scan-to-ship and receiving.

Primary key: IS2D_BAR_CODE + IS2D_BAR_ITEM + IS2D_BAR_ORDER

| Offset | Field | Type | Size | Meaning |
|---|---|---|---|---|
| 0 | IS2D_BAR_CODE | STRING | 10 | Barcode format/profile code |
| 10 | IS2D_BAR_ITEM | STRING | 15 | Item code (blank = applies to all items) |
| 25 | IS2D_BAR_ORDER | UBINARY | 2 | Field sequence number within the barcode |
| 27 | IS2D_BAR_CHAR | STRING | 5 | Character set / encoding format |
| 32 | IS2D_BAR_FIELD | STRING | 25 | **Data field name** encoded at this position |
| 57–96 | IS2D_BAR_DOCPR_1..40 | STRING | 1 each | 40 document-print flags — which document types include this barcode field (Y/N per document type) |

**How it works:** For a given item and barcode format, the IS2DBAR rows define which
fields appear in the 2D barcode, in what order, and on which printed documents. The
IS2D_BAR_DOCPR_N flags allow a field to appear on some documents (e.g., packing slips)
but not others (e.g., invoices).

---

## Additional Simple Tables (documented inline)

### BKSOLOCK — SO Record Lock Table (5 fields)

Records which SO record is currently locked by which user. Used to prevent concurrent edits.

| Field | Meaning |
|---|---|
| BKSO_LOCK_REC (10) | Record key of the locked SO |
| BKSO_LOCK_ITEM (25) | Item within the record being locked |
| BKSO_LOCK_DATE | Lock date |
| BKSO_LOCK_TIME | Lock time |
| BKSO_LOCK_WHO (25) | User who holds the lock |

### BKSOHLOT / BKSOHSER — SO History Lot/Serial Tracking (14 fields each, identical structure)

Both tables store lot/serial number history for SO shipments. BKSOHLOT = lot-tracked items;
BKSOHSER = serial-tracked items.

| Field | Meaning |
|---|---|
| BKAR_TXN_SONUM (FLOAT 8) | SO number |
| BKAR_TXN_CODE (15) | Item code |
| BKAR_TXN_DESC (30) | Item description |
| BKAR_TXN_QTY (FLOAT 8) | Quantity |
| BKAR_TXN_LOT (15) | Lot number |
| BKAR_TXN_SERIAL (25) | Serial number |
| BKAR_TXN_DATE | Transaction date |
| BKAR_TXN_STOCK (15) | Stock location |
| BKAR_TXN_LINE (FLOAT 8) | SO line number |
| BKAR_TXN_LOC (10) | Location code |
| BKAR_TXN_TMPSO (40) | Temp SO reference |
| BKAR_TXN_SRNUM (FLOAT 8) | Serial/run number |
| BKAR_TXN_EXTRA (50) | Extra data |
| BKAR_TXN_BIN (15) | Bin location |

---

## BKED* Family — EDI Staging Tables (Pass 106, 2026-06-18)

**Module:** DE-P (Data Exchange → EDI Interface) | **Tables:** 6 | **Status: verified schema**

The BKED* tables form the EDI inbound/outbound staging layer. Inbound EDI purchase orders
(X12 850) land here as staged invoices before conversion to real AR/SO records.
Outbound EDI (810/855/856) reads from BKARINV directly.

### Architecture: clone of BKARINV

BKEDIH and BKEDIL use **identical field names and layout** to BKARINV/BKARINVL.
This is confirmed by the DDF: every field in BKEDIH is `BKAR_INV_*` and every field in
BKEDIL is `BKAR_INVL_*`. The EDI import program (DEP-B) writes EDI orders into these
staging tables as if they were AR invoices; DEP-D then moves them to BKARINV/BKARINVL.

### Family overview

| Table | Fields | Purpose |
|---|---|---|
| BKEDIH | 84 | EDI staged order header — verbatim BKARINV clone |
| BKEDIL | 28 | EDI staged order lines — verbatim BKARINVL clone |
| BKEDIDUN | 7 | Customer DUNS number mapping + per-customer EDI flags |
| BKEDMSTR | 3 | Our company's EDI config (DUNS, import path, counter) |
| BKEDNOTE | 3 | Notes attached to an EDI transaction |
| BKEDPOST | 2 | EDI posting audit trail |

### BKEDIH / BKEDIL — Staged order header + lines

Field layout is **byte-for-byte identical to BKARINV / BKARINVL** — see the BKARINV
documentation for all 84+28 field meanings. Key fields in context:

| BKARINV field | In EDI staging | Notes |
|---|---|---|
| BKAR_INV_NUM | EDI staging record number | Counter from BKEDI_MST_NEXTN |
| BKAR_INV_SONUM | Source SO (0 until DEP-D runs) | Filled when converted |
| BKAR_INV_INVCD | Document type code | Likely 'E' for EDI in staging |
| BKAR_INV_CUSCOD | Customer code | From BKEDIDUN mapping |
| BKAR_INV_CUSORD | Customer's PO number | From EDI 850 BEG04 |
| BKAR_INV_QSTAT | Processing status | Flags: ready/error/posted |

### BKEDIDUN — Customer DUNS mapping (7 fields)

One row per customer, defines their EDI relationship. PK = BKEDI_DUN_CUST.

| Field | Size | Meaning |
|---|---|---|
| BKEDI_DUN_CUST | STRING 10 | Customer code (PK, FK → BKARCUST) |
| BKEDI_DUN_DUNS | STRING 15 | D-U-N-S number for this customer |
| BKEDI_DUN_EDI | STRING 1 | EDI enabled flag (Y/N) |
| BKEDI_DUN_EFFDT | DATE 4 | Effective date for EDI trading relationship |
| BKEDI_DUN_PRODS | STRING 1 | Send 855 (Order Acknowledgment) Y/N |
| BKEDI_DUN_ADVS | STRING 1 | Send 856 (Advance Ship Notice) Y/N |
| BKEDI_DUN_SHPCD | STRING 1 | Shipping code flag |

### BKEDMSTR — Company EDI configuration (3 fields)

Single-row master config for our company's EDI setup.

| Field | Size | Meaning |
|---|---|---|
| BKEDI_MST_NEXTN | FLOAT 8 | Next EDI transaction number (auto-increment counter) |
| BKEDI_MST_DUNS | STRING 15 | Our company's D-U-N-S number (sent in EDI headers) |
| BKEDI_MST_PATH | STRING 66 | File system path for inbound EDI file drop directory |

### BKEDNOTE — EDI transaction notes (3 fields)

| Field | Size | Meaning |
|---|---|---|
| BKEDI_NOTE_EDI | FLOAT 8 | EDI staging record number (FK → BKEDIH) |
| BKEDI_NOTE_SO | FLOAT 8 | Resulting SO/invoice number after DEP-D conversion |
| BKEDI_NOTE_NOTE | STRING 80 | Note text (error messages, transaction details) |

### BKEDPOST — EDI posting audit trail (2 fields)

| Field | Size | Meaning |
|---|---|---|
| BKEDI_POST_INVN | FLOAT 8 | Posted invoice number (FK → BKARINV after conversion) |
| BKEDI_POST_CUST | STRING 10 | Customer code of the posted EDI order |

### EDI pipeline (from BKMENUSU.TXT, DE-P submenu)

| Menu | Program | Action |
|---|---|---|
| DEP-B | T7DEPB | Import EDI Orders — reads X12 files from BKEDI_MST_PATH → writes BKEDIH/BKEDIL |
| DEP-C | T7DEPC | Edit EDI Orders — review/fix BKEDIH/BKEDIL staging records |
| DEP-D | T7DEPD | Convert EDI Orders to Sales Orders — BKEDIH/BKEDIL → BKARINV/BKARINVL + writes BKEDPOST |
| DEP-E | T7DEPE | Export EDI Invoice/Acknowledgement — BKARINV → X12 810 (Invoice) or 855 (Acknowledgment) |
| DEP-F | T7DEPF | Export EDI ASN — BKARINV → X12 856 (Advance Ship Notice) |
| DEP-H | T7DEPH | EDI Error Report — lists errors from import processing |

Inbound transaction set supported: X12 **850** (Purchase Order).
Outbound transaction sets: X12 **810** (Invoice), **855** (Order Acknowledgment), **856** (Advance Ship Notice).

**Confidence: 78/100** — Schema fully confirmed from DDF. Pipeline confirmed from BKMENUSU.TXT
program names and labels. X12 transaction set numbers inferred from program labels (not confirmed
from program source or trading partner docs).

---

## BKES* Family — Estimating/Quoting Tables (Pass 106, 2026-06-18)

**Module:** ES (Estimating) | **Tables:** 3 core + associated ESTSUM/BKMATCST/BKRTCST | **Status: verified schema**

The Estimating module gives manufacturing companies a way to price jobs before committing them
to production. Estimates live in BKESTQT/BKESTQTL (clone of BKARINV architecture) and are
converted to real Sales Orders or Work Orders via ES-E. The module has its own inventory
(MTICMSTR) and cost tables (BKMATCST, BKRTCST) separate from production.

### Architecture: clone of BKARINV

Like the EDI staging tables, BKESTQT and BKESTQTL use **identical field names and layout**
to BKARINV/BKARINVL (all fields are `BKAR_INV_*` and `BKAR_INVL_*`). An estimate record
IS a quote invoice — same structure, different lifecycle.

### Family overview

| Table | Fields | Purpose |
|---|---|---|
| BKESTQT | 84 | Estimate/quote header — verbatim BKARINV clone |
| BKESTQTL | 28 | Estimate line items — verbatim BKARINVL clone |
| BKESTCFG | 13 | Estimating module defaults and configuration |
| ESTSUM | 213 | Estimate cost summary — 10 qty breaks × 18 cost types per quote |
| BKMATCST | 25 | Material cost table — price breaks per material code |
| BKRTCST | 24 | Routing cost table — per-operation setup/labor cost breaks |
| MTICMSTR | 108 | Estimating inventory master (separate from production BKICMSTR) |

### BKESTQT / BKESTQTL — Estimate header + lines

Field layout is **byte-for-byte identical to BKARINV / BKARINVL**. Key fields in estimating context:

| BKARINV field | In estimating | Notes |
|---|---|---|
| BKAR_INV_NUM | Quote number | Auto-incremented from BKEST_CFG_NUM |
| BKAR_INV_SONUM | Resulting SO number | 0 until ES-E converts |
| BKAR_INV_CUSCOD | Prospect/customer | May be blank for speculative quotes |
| BKAR_INV_CUSORD | Customer RFQ number | Customer's quote request reference |
| BKAR_INV_QSTAT | Quote status | Controlled by BKEST_CFG_STAT codes |
| BKAR_INV_INVDTE | Quote date | Set when estimate is entered |
| BKAR_INV_SHIPDT | Estimated ship date | |
| BKAR_INV_SUBTOT | Estimated subtotal | Calculated from BKESTQTL lines |
| BKAR_INV_COGS | Estimated COGS | From BKMATCST/BKRTCST cost rollup |

### BKESTCFG — Estimating defaults (13 fields)

Single-row configuration table for the Estimating module. Edited via ES-J (T7DSEST).

| Field | Type/Size | Meaning |
|---|---|---|
| BKEST_CFG_NUM | FLOAT 8 | Next quote number counter |
| BKEST_CFG_STAT | STRING 1 | Default status code for new estimates |
| BKEST_CFG_CLASS | STRING 4 | Default document class (e.g., product category) |
| BKEST_CFG_FORM | STRING 1 | Default print form type |
| *(gap: offsets 14–53, 40 bytes)* | — | Undocumented/unregistered fields |
| BKEST_CMPY_INFO | STRING 1 | Print company info on quotes (Y/N) |
| BKEST_CFG_DAYS | UBINARY 2 | Default quote validity/expiry in days |
| BKEST_CFG_ENDLN_1..5 | STRING 30 × 5 | Five configurable footer lines printed on quotes |
| BKEST_CFG_SONUM | FLOAT 8 | Last SO number generated from estimate conversion |
| BKEST_CFG_EXTRA | STRING 100 | Spare/expansion |

### ESTSUM — Estimate cost summary (213 fields)

One row per quote. Summarizes all costs across 10 quantity break points for the estimate.
Used by T7ESB (Print Customer Quotes) and T7ESC (Print Cost Rollup).

Primary key: MTESUM_QUOTE (FLOAT 8, quote number).

Structure: 10 × {QTY, MAT, MATMU, LAB, LABMU, SETUP, OP, OPMU, OH, OHMU, MISC, EXTRA,
MEMU, OVALL, TOTAL, PRICE, COST, VOVHD} = 180 cost fields + 14 header fields + 19 scalars.

Key header fields:
| Field | Meaning |
|---|---|
| MTESUM_QUOTE | Quote number (PK) |
| MTESUM_DATE | Quote date |
| MTESUM_EXPDATE | Quote expiry date |
| MTESUM_STATUS | Quote status code |
| MTESUM_CLASS | Document class |
| MTESUM_CODE | Item/product code being estimated |
| MTESUM_DESC | Item description |
| MTESUM_UM | Unit of measure |
| MTESUM_CUSTCODE | Customer code |
| MTESUM_RFQ | RFQ reference number |
| MTESUM_REV | Revision level |
| MTESUM_QTY_1..10 | Ten quantity break points |
| MTESUM_MAT_1..10 | Material cost per unit at each qty break |
| MTESUM_LAB_1..10 | Labor cost per unit at each qty break |

### Estimating workflow (from BKMENUSU.TXT ES menu)

| Menu | Program | Action |
|---|---|---|
| ES-A | T7ESA | Enter Estimates — create/edit BKESTQT/BKESTQTL; opens BOM (BKBMMSTR), items (BKICMSTR), MRP forecast (BKMRPFC) |
| ES-B | T7ESB (213p) | Print Customer Quotes — formatted quote output from BKESTQT |
| ES-C | T7ESC (124p) | Print Estimate Cost Rollup — detailed cost breakdown; uses BKRFQ for vendor pricing |
| ES-D | T7EST (163p) | Quick Estimate — simplified entry path |
| ES-E | T7ESE (194p) | Convert Estimates — BKESTQT → BKARINV (Sales Order) or WORKORD (Work Order) |
| ES-H | T7ESH (60p) | Enter Material Costs — edit BKMATCST price breaks |
| ES-I | T7ESI (94p) | Print Material Costs — report from BKMATCST |
| ES-J | T7DSEST | Estimating Defaults — edit BKESTCFG |
| ES-K | T7IC2EST (6p) | Update Estimating Inventory from Production — copy BKICMSTR → MTICMSTR |
| ES-L | T7ESL | Edit Estimating Inventory — maintain MTICMSTR items |
| ES-M | T7ESM | Estimating Inventory Inquiry — view MTICMSTR |

**Confidence: 78/100** — Schema fully confirmed from DDF. Field meanings confirmed from field
name analysis and cross-reference to BKARINV docs. Program associations confirmed from BKMENUSU.TXT.
ESTSUM cost category semantics inferred from field names (not confirmed by SRC source).
The 40-byte gap in BKESTCFG (offsets 14–53) contains undocumented fields not registered in DDF.
