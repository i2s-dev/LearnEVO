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
