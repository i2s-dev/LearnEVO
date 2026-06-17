# EvoERP Data Dictionary — Tier 6 Tables

Status: partial — extracted from Pervasive DDF schema 2026-06-17.

---

## Key Architecture Finding: Sales Orders Share BKARINV

**Sales Orders in EvoERP are AR Invoices — they use the same table.**

T7SOA.RWN (the main SO entry program) operates on BKARINV, not a separate BKSOMSTR.
The BKSO* prefix tables are only supplemental:
- BKSOLOCK (5 fields) — record lock during editing
- BKSONOTE (5 fields) — SO notes
- BKSOHLOT/BKSOHSER (14 fields each) — lot/serial history for SO shipments
- BKSOPO (16 fields) — SO→PO cross-reference for special orders
- BKSOX/BKSOXH (25 fields each) — SO extract for reporting

The BKARINV table serves as both the SO and the AR invoice. When an SO is invoiced,
the status fields change but the record stays in the same table.

---

## BKICLOC — Inventory Location Quantities

**Purpose:** Per-location inventory balances for each item. The primary source of
on-hand, on-order, committed, and WIP quantities at a specific warehouse/bin location.

Primary key: BKIC_LOC_PROD + BKIC_LOC_CODE
Fields: 32

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKIC_LOC_PROD | STRING | 15 | Item/part code (PK part 1) |
| BKIC_LOC_CODE | STRING | 10 | Location code (PK part 2, FK → BKICLOCM) |
| BKIC_LOC_UOH | FLOAT | 8 | Units on hand at this location |
| BKIC_LOC_UOSO | FLOAT | 8 | Units on sales order (committed to SOs) |
| BKIC_LOC_UBO | FLOAT | 8 | Units back-ordered |
| BKIC_LOC_UOO | FLOAT | 8 | Units on order (purchase orders) |
| BKIC_LOC_GLA | STRING | 10 | GL account — inventory adjustments |
| BKIC_LOC_DPTA | STRING | 4 | GL dept — adjustments |
| BKIC_LOC_GLC | STRING | 10 | GL account — cost of goods |
| BKIC_LOC_DPTC | STRING | 4 | GL dept — cost |
| BKIC_LOC_GLS | STRING | 10 | GL account — sales |
| BKIC_LOC_DPTS | STRING | 4 | GL dept — sales |
| BKIC_LOC_GLSNT | STRING | 10 | GL account — non-taxable sales |
| BKIC_LOC_DPTSNT | STRING | 4 | GL dept — non-taxable sales |
| BKIC_LOC_GLWIP | STRING | 10 | GL account — WIP |
| BKIC_LOC_DPTWIP | STRING | 4 | GL dept — WIP |
| BKIC_LOC_UOWO | FLOAT | 8 | Units on work order (WIP allocated) |
| BKIC_LOC_UALLOC | FLOAT | 8 | Units allocated (reserved but not yet on SO) |
| + 14 more | — | — | Additional quantity/GL fields |

**Key insight:** Each BKICMSTR (item master) can have multiple BKICLOC rows — one per
warehouse location. The total on-hand is the sum of UOH across all location rows.
The GL accounts per location allow different items or locations to post to different accounts.

---

## BKICLOCM — Inventory Location Master

**Purpose:** Defines warehouse/stockroom locations with address and tax group.
One row per physical location code.

Primary key: BKIC_LOCM_CODE
Fields: 12

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKIC_LOCM_CODE | STRING | 10 | Location code (PK) |
| BKIC_LOCM_NAME | STRING | 30 | Location name |
| BKIC_LOCM_ADDR1/2/3 | STRING | 30 each | Address lines |
| BKIC_LOCM_CITY | STRING | 20 | City |
| BKIC_LOCM_STATE | STRING | 2 | State |
| BKIC_LOCM_ZIP | STRING | 10 | Zip code |
| BKIC_LOCM_CNTCT | STRING | 25 | Contact name |
| BKIC_LOCM_PHONE | STRING | 25 | Phone |
| BKIC_LOCM_FAX | STRING | 25 | Fax |
| BKIC_LOCM_TAXGR | STRING | 10 | Tax group code (FK → ISTAXGRP) |

**Confidence: 88/100** — Small table, all fields clear.

---

## BKICPMAT — Customer Item Price Matrix

**Purpose:** Per-customer, per-item pricing with up to 10 quantity breakpoints.
Overrides standard pricing when a customer-specific price is set.

Primary key: BKIC_PMAT_CUST + BKIC_PMAT_PCODE + BKIC_PMAT_PNUM
Fields: 85

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKIC_PMAT_CUST | STRING | 10 | Customer code (PK part 1, FK → BKARCUST) |
| BKIC_PMAT_PCODE | STRING | 15 | Item/part code (PK part 2, FK → BKICMSTR) |
| BKIC_PMAT_PNUM | UBINARY | 2 | Price matrix entry number (PK part 3) |
| BKIC_PMAT_RATE_1..10 | FLOAT 8 × 10 | — | Price/rate at each quantity breakpoint |
| BKIC_PMAT_QTY_1..10 | FLOAT 8 × 10 | — | Quantity breakpoints |
| + 65 more | — | — | Date ranges, discount types, unit types, etc. |

**Key insight:** When a SO line is entered, EvoERP checks BKICPMAT first (customer + item).
If a match exists, RATE values override the standard pricing in BKICMSTR.

**Confidence: 72/100** — First 25 fields confirmed; remaining 65 fields not extracted.

---

## BKICDIM — Item Dimensions / Material Specifications

**Purpose:** Physical specifications for manufactured items: dimensions, alloy, temper,
finish, tolerances, and density. Used primarily in metals/materials manufacturing.

Primary key: BKICDIM_PARTNO
Fields: 47

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKICDIM_PARTNO | STRING | 15 | Part number (PK) |
| BKICDIM_PARENT | STRING | 15 | Parent part (for dimension inheritance) |
| BKICDIM_FIRST | FLOAT | 8 | First dimension (e.g., width) |
| BKICDIM_SECOND | FLOAT | 8 | Second dimension (e.g., length) |
| BKICDIM_GENERIC | STRING | 15 | Generic/base part code (for similar parts) |
| BKICDIM_THICK | FLOAT | 8 | Thickness |
| BKICDIM_ALTDESC | STRING | 30 | Alternate description |
| BKICDIM_ALLOY | STRING | 20 | Material alloy (e.g., "6061-T6") |
| BKICDIM_TEMPER | STRING | 20 | Material temper |
| BKICDIM_FINISH_1/2 | STRING | 20 each | Surface finish specifications |
| BKICDIM_F_TOL_1/2 | FLOAT | 8 each | First dimension tolerance ± |
| BKICDIM_S_TOL_1/2 | FLOAT | 8 each | Second dimension tolerance ± |
| BKICDIM_T_TOL_1/2 | FLOAT | 8 each | Thickness tolerance ± |
| BKICDIM_DENSITY | FLOAT | 8 | Material density |
| + 29 more | — | — | Additional spec fields |

**Confidence: 72/100** — First 18 fields clear; 29 remaining not extracted.

---

## BKICTAX — Item Tax by State/Locality

**Purpose:** Sales tax configuration per state+local jurisdiction, with per-period collection tracking.
Complements ISTAXGRP (tax groups) with state-specific rates and collection history.

Primary key: BKIC_TAX_STATE + BKIC_TAX_LOCAL
Fields: 46

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKIC_TAX_STATE | STRING | 2 | State code (PK part 1) |
| BKIC_TAX_LOCAL | STRING | 2 | Local jurisdiction code (PK part 2) |
| BKIC_TAX_NAME | STRING | 25 | Tax authority name |
| BKIC_TAX_NUMBER | STRING | 15 | Tax authority ID/registration number |
| BKIC_TAX_RATE | FLOAT | 8 | Tax rate (decimal, e.g., 0.065 = 6.5%) |
| BKIC_TAX_GLACT | STRING | 10 | GL account for collected tax |
| BKIC_TAX_GLDPT | STRING | 4 | GL department |
| BKIC_TAX_VENDOR | STRING | 10 | Tax vendor/authority code for remittance |
| BKIC_TAX_TAXBLE_1..10 | FLOAT 8 × 10 | — | Taxable sales per period (10 periods) |
| + 28 more | — | — | NONTAX/COLECT per period, additional fields |

---

## BKICREQ — Inventory Requisitions

**Purpose:** Internal material transfer/requisition requests — not purchase orders,
but internal requests to move or issue inventory.

Primary key: BKIC_REQ_NUM
Fields: 41

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKIC_REQ_STATUS | STRING | 1 | Requisition status |
| BKIC_REQ_BY | UBINARY | 2 | Requested by (employee number) |
| BKIC_REQ_IDATE | DATE | 4 | Issue date |
| BKIC_REQ_NUM | FLOAT | 8 | Requisition number (PK) |
| BKIC_REQ_TYPE | STRING | 1 | Type code |
| BKIC_REQ_TOLOCN | STRING | 10 | Destination location code (FK → BKICLOCM) |
| BKIC_REQ_DDATE | DATE | 4 | Due/needed date |
| BKIC_REQ_DESC | STRING | 30 | Description |
| BKIC_REQ_NOTES_1..10 | STRING 30 × 10 | — | 10 note lines |
| + 23 more | — | — | Additional fields |

---

## MTICAMTR / MTICEMTR — MT Inventory Cost Snapshots (Additional)

**Purpose:** Two more copies of MTICMSTR (same 108 fields) for actual-cost and
estimated-cost snapshots at the MT (second-gen) level. With MTICMSTR (current),
MTICAMTR (actual), and MTICEMTR (estimated), the system maintains 3 parallel
inventory masters for variance analysis.

**Confirmed:** MTICAMTR and MTICEMTR have 100% identical field names to MTICMSTR.

| Table | Fields | Purpose |
|---|---|---|
| MTICMSTR | 108 | MT inventory master — current/standard |
| MTICAMTR | 108 | MT inventory master — actual cost snapshot |
| MTICEMTR | 108 | MT inventory master — estimated cost snapshot |
| BKICMSTR | 64 | BK inventory master — current/standard |
| BKICAMTR | 64 | BK inventory master — actual cost snapshot |
| BKICEMTR | 64 | BK inventory master — estimated cost snapshot |

The AMTR/EMTR tables are updated by the JC (Job Costing) standard cost variance module
when standard/estimated costs are recalculated.

---

## BKSOPO — SO to PO Cross-Reference

**Purpose:** Links special-order Sales Order lines to their corresponding Purchase Orders.
When a customer orders a non-stocked item, EvoERP creates a PO and records the SO↔PO link here.

Fields: 16, first field: BKMRP_PO_UID

| Field | Meaning |
|---|---|
| BKMRP_PO_UID (FLOAT 8) | PO UID (FK → BKAPPOL/BKRPOLS) |
| BKMRP_SO_NUM (FLOAT 8) | SO number (FK → BKARINV) |
| BKMRP_SO_LINE (FLOAT 8) | SO line number |
| BKMRP_QTY (FLOAT 8) | Quantity linked |
| + 12 more | Additional tracking fields |

**Note:** The BKMRP prefix suggests this table is also used by MRP for planned/released orders.
