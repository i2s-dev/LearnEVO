# EvoERP Data Dictionary — Tier 5 Tables

Status: partial — extracted from Pervasive DDF schema 2026-06-17.

---

## ISUSAGE — Item Usage History

**Purpose:** 26-period rolling quantity/amount history per item per type, plus 5 prior years.
Used by MRP, purchasing analysis, and forecasting to compute average demand.

Primary key: ISTS_USE_CODE + ISTS_USE_TYPE
Fields: 246

| Field group | Count | Meaning |
|---|---|---|
| ISTS_USE_CODE | 1 (STRING 15) | Item/part code (PK part 1) |
| ISTS_USE_TYPE | 1 (STRING 1) | Usage type code — distinguishes issue/sale/etc. (PK part 2) |
| ISTS_USE_QTY_1..26 | 26 (FLOAT 8 each) | Quantity issued/sold per period (26 rolling periods) |
| ISTS_USE_AMT_1..26 | 26 (FLOAT 8 each) | Dollar amount per period |
| ISTS_USE_QTYY1..QTYY5 | 13 each × 5 (= 65) | Qty per period for prior years 1–5 (13 periods/year) |
| ISTS_USE_AMTY1..AMTY5 | 13 each × 5 (= 65) | Amount per period for prior years 1–5 |
| ISTS_USE_DATEY1..DATEY5 | 2 each × 5 (= 10) | Period start/end dates for each prior year |
| ISTS_USE_TOTUSE | 1 (FLOAT 8) | Cumulative total usage quantity |
| ISTS_USE_ALPHA_1..10 | 10 | Alpha sort / category codes |
| ISTS_USE_FLAGS_1..15 | 15 (STRING 1 each) | 15 configurable flag bits |
| ISTS_USE_GDATE_1..10 | 10 (DATE each) | 10 general-purpose dates |
| ISTS_USE_LSTCAL_1..5 | 5 (DATE each) | Last-calculated dates for each year block |
| ISTS_USE_NUM_1..5 | 5 (FLOAT 8 each) | General numeric fields |
| ISTS_USE_WHO_1..5 | 5 (STRING each) | Who last updated each year block |
| ISTS_USE_EXTRA | 1 | Extra field |

**Coverage:** 26 current periods + 5 × 13 = 65 prior-period slots = 91 total period slots.
With monthly periods, this holds 2+ years rolling + 5 years history = ~7 years of data.

---

## ISAPAINL — AP Invoice Line Archive (IS Extension)

**Purpose:** Extended AP invoice line archive storing up to 75 GL distribution lines per invoice.
The active AP invoice table (BKAPINV/BKARINVL) has far fewer GL slots; this IS extension is the
full audit trail or "invoice expansion" used by the AP module for multi-cost-center allocation.

Primary key: BKAP_INVL_CODE + BKAP_INVL_NUM
Fields: 390

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKAP_INVL_CODE | STRING | 10 | Vendor code (PK part 1) |
| BKAP_INVL_NUM | STRING | 10 | Invoice number (PK part 2) |
| BKAP_INVL_DATE | DATE | 4 | Invoice date |
| BKAP_INVL_DESC | STRING | 25 | Invoice description |
| BKAP_INVL_TERMD | STRING | 10 | Terms description |
| BKAP_INVL_TERMN | UBINARY | 2 | Terms net days |
| BKAP_INVL_TYPED | STRING | 10 | Invoice type description |
| BKAP_INVL_TYPEN | UBINARY | 2 | Invoice type number |
| BKAP_INVL_TAMT | FLOAT | 8 | Invoice total amount |
| BKAP_INVL_TDC | STRING | 1 | Debit/credit indicator |
| BKAP_INVL_ISCUR | STRING | 1 | Is currency (multi-currency flag) |
| BKAP_INVL_JOB | STRING | ? | Job code reference |
| BKAP_INVL_CHK | STRING | ? | Check number |
| BKAP_INVL_APDPT | STRING | ? | AP department code |
| BKAP_INVL_EXTRA | STRING | ? | Extra/notes field |

Then 75 × 5 = 375 GL distribution fields:

| Group | Count | Meaning |
|---|---|---|
| BKAP_INVL_GLACT_1..75 | 75 (STRING 10 each) | GL account number for distribution line N |
| BKAP_INVL_DAMT_1..75 | 75 (FLOAT 8 each) | Distribution amount for line N |
| BKAP_INVL_DC_1..75 | 75 (STRING 1 each) | Debit/credit flag for line N |
| BKAP_INVL_GLD_1..75 | 75 (FLOAT 8 each) | GL distribution ledger amount |
| BKAP_INVL_GLDPT_1..75 | 75 (STRING 4 each) | GL department for distribution line N |

**Key insight:** 75 GL distribution lines far exceeds what a typical AP invoice needs.
EvoERP supports splitting one AP invoice across 75 separate GL accounts and departments.
This is the IS-layer archive for the full AP allocation detail.

---

## ISALINKS / ISLINKS — Document Link Attachment Tables

**Purpose:** Attach external documents, URLs, or file paths to any EvoERP record.
Uses the same 48-char composite UID key as ISNOTES — same entity-tagging system.

ISALINKS = archived links, ISLINKS = active links (identical schema, 311 fields each).

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_LNK_UID | STRING | 48 | Composite key — identifies the EvoERP entity (same format as ISNOTES) |
| IS_LNK_LINK | STRING | 256 | The link content — file path, URL, or document reference |
| IS_LNK_APP | STRING | 10 | Application/module code that owns this link |
| IS_LNK_ATYPE | STRING | 1 | Attachment type code |
| IS_LNK_DATE | DATE | 4 | Date link was created |
| IS_LNK_WHO | STRING | ? | User who created the link |
| IS_LNK_SORT | STRING | ? | Sort order within linked entity |
| IS_LNK_PRIVATE | STRING | 1 | Private flag — visible only to creating user |
| IS_LNK_GLOBAL | STRING | 1 | Global flag — visible to all users/companies |
| IS_LNK_OPENWITH | STRING | ? | Application to open the link with (e.g., "ACROBAT") |
| IS_LNK_EXTRA | STRING | ? | Extra/notes |
| IS_LNK_TYPES_1..100 | STRING 1 × 100 | 100 type/category flag slots |
| IS_LNK_DEF_1..100 | STRING × 100 | 100 definition fields (extra metadata per slot) |
| IS_LNK_PCB_1..100 | STRING × 100 | 100 PCB/config field slots |

**Key insight:** Each link can be tagged with up to 100 type flags (IS_LNK_TYPES) allowing
filtering by link category. IS_LNK_LINK holds the actual URL/path (256 chars max).
This is the EvoERP document management / "Files" attachment system.

---

## ISESTASM — MT Estimating Assembly (Quote Master)

**Purpose:** Master table for production estimates/quotes in the ES (Estimating) module.
Stores complete quote header plus all cost components at up to 10 quantity breakpoints.

Primary key: MTESUM_QUOTE
Fields: 213

| Field | Type | Meaning |
|---|---|---|
| MTESUM_QUOTE | FLOAT 8 | Quote number (PK) |
| MTESUM_DATE | DATE | Quote date |
| MTESUM_EXPDATE | DATE | Expiry date |
| MTESUM_FIN_DATE | DATE | Final/approval date |
| MTESUM_CDATE | DATE | Created date |
| MTESUM_STATUS | STRING 1 | Status code (open/won/lost/expired) |
| MTESUM_CLASS | STRING 4 | Product class |
| MTESUM_CODE | STRING 15 | Item/part code being quoted |
| MTESUM_DESC | STRING 30 | Description |
| MTESUM_UM | STRING 3 | Unit of measure |
| MTESUM_CUSTCODE | STRING 10 | Customer code |
| MTESUM_NAME | STRING 30 | Customer name |
| MTESUM_ATTN | STRING 30 | Attention / contact |
| MTESUM_RFQ | STRING 15 | Linked RFQ number (from RF module) |
| MTESUM_REV | STRING 4 | Revision level |
| MTESUM_PROJ | STRING 15 | Project code |
| MTESUM_ENTBY | STRING ? | Entered by |
| MTESUM_LEADTIME | STRING ? | Lead time |
| MTESUM_LEAD_SRC | STRING ? | Lead source (CRM integration) |
| MTESUM_LOC | STRING ? | Location |
| MTESUM_BOM_FLAG | STRING 1 | BOM generated flag |
| MTESUM_RT_FLAG | STRING 1 | Routing generated flag |
| MTESUM_EX_FLAG | STRING 1 | Exported flag |
| MTESUM_OPPTYPE | STRING ? | Opportunity type |
| MTESUM_SLSP_NUM_1/2 | FLOAT 8 × 2 | Salesperson numbers (2 slots) |
| MTESUM_COMM_RTE_1/2 | FLOAT ? × 2 | Commission rates |
| MTESUM_TEMP_NUM | FLOAT ? | Temporary reference number |
| MTESUM_QTREV | STRING ? | Quote revision |
| MTESUM_L_O_CODE | STRING ? | Lost/order code |
| MTESUM_L_O_DATE | DATE ? | Lost/order date |
| MTESUM_EXTRA2 | STRING ? | Extra field |

Per-quantity-break arrays (10 slots each):

| Group | Meaning |
|---|---|
| MTESUM_QTY_1..10 | Quantity break points |
| MTESUM_MAT_1..10 | Material cost at each qty break |
| MTESUM_MATMU_1..10 | Material markup |
| MTESUM_LAB_1..10 | Labor cost |
| MTESUM_LABMU_1..10 | Labor markup |
| MTESUM_SETUP_1..10 | Setup cost |
| MTESUM_OH_1..10 | Overhead cost |
| MTESUM_OHMU_1..10 | Overhead markup |
| MTESUM_OP_1..10 | Outside processing cost |
| MTESUM_OPMU_1..10 | Outside processing markup |
| MTESUM_MISC_1..10 | Miscellaneous cost |
| MTESUM_VOVHD_1..10 | Variable overhead cost |
| MTESUM_OVALL_1..10 | Overall total at each qty break |
| MTESUM_PRICE_1..10 | Selling price at each qty break |
| MTESUM_COST_1..10 | Total cost at each qty break |
| MTESUM_TOTAL_1..10 | Grand total at each qty break |
| MTESUM_NOTES_1..10 | Notes per qty break |
| MTESUM_EXTRA_1..10 | Extra fields per qty break |

**Key insight:** A single estimate stores all cost breakdowns (material/labor/setup/overhead/
outside processing) across 10 price points. When a quote is won, MTESUM_BOM_FLAG and
MTESUM_RT_FLAG indicate whether the BOM and routing were generated. The RF module
creates vendor RFQs from MTESUM data via ISESADTL.

---

## ISESADTL — IS Estimating Detail

**Purpose:** Line-level component detail for estimates. Each row = one component/operation
within an estimate, with qty and cost data at all 10 quantity breakpoints.

Primary key: IS_EST_NUM + IS_EST_PART + IS_EST_LINE
Fields: 203

| Field | Meaning |
|---|---|
| IS_EST_NUM (FLOAT 8) | Estimate number (FK to ISESTASM.MTESUM_QUOTE) |
| IS_EST_PART (STRING 15) | Component part code |
| IS_EST_LINE (FLOAT 8) | Line sequence number |
| IS_EST_QTY_1..10 (FLOAT 8 each) | Component qty per estimate quantity break |
| IS_EST_MAT_1..10 | Material cost per break |
| IS_EST_MATMU_1..10 | Material markup per break |
| + more cost arrays | (same pattern: LAB, SETUP, OH, OP, MISC, TOTAL per 10 breaks) |

---

## ISMICADT / ISMICESA / ISMICEST — MT Inventory Costing Snapshots

**Purpose:** Three identical-schema tables (108 fields each), exact copies of MTICMSTR.
Store inventory master snapshots for costing: ADT = actual-cost detail, ESA = estimated
standard average, EST = estimated standard.

**Confirmed:** All three tables share 100% identical field names with MTICMSTR (zero difference).

| Table | Likely meaning |
|---|---|
| ISMICADT | IS MT Inventory Costing — Actual Detail |
| ISMICESA | IS MT Inventory Costing — Estimated Standard (Average) |
| ISMICEST | IS MT Inventory Costing — Estimated Standard |

These support EvoERP's standard vs. actual costing mode: the JC (Job Costing) module
compares actual transaction costs against these snapshot values to compute variances.

See [tier3-tables.md](tier3-tables.md) for full MTICMSTR/ISMICADT field listing.

---

## ISTAXGRP — Tax Group Definition

**Purpose:** Groups up to 9 tax codes into a single "tax group" that can be applied to
customers or transactions. Tracks collection totals monthly.

Primary key: ISIS_TXG_NAME
Fields: 105

| Field group | Count | Meaning |
|---|---|---|
| ISIS_TXG_NAME | 1 (STRING 10) | Tax group name (PK) — assigned to customers |
| ISIS_TXG_DESC | 1 | Tax group description |
| ISIS_TXG_CODE_1..9 | 9 (STRING 10 each) | Up to 9 tax codes in this group |
| ISIS_TXG_TAXON_1..9 | 9 (STRING 1 each) | "Taxable" flag per code slot (Y/N) |
| ISIS_TXG_TAXBLE_1..12 | 12 (FLOAT each) | Taxable sales amount per month (12-month rolling) |
| ISIS_TXG_NONTAX_1..12 | 12 (FLOAT each) | Non-taxable sales amount per month |
| ISIS_TXG_COLECT_1..12 | 12 (FLOAT each) | Tax collected per month (12-month rolling) |
| ISIS_TXG_DESCF_1..9 | 9 (STRING each) | Description per code slot (for tax filing) |
| ISIS_TXG_PERCC_1..9 | 9 (FLOAT each) | Tax percentage rate per code slot |
| ISIS_TXG_PID_1..9 | 9 (STRING 1 each) | Product ID / product class taxable flag |
| ISIS_TXG_FRGT_1..9 | 9 (STRING 1 each) | "Tax freight" flag per code (Y/N) |
| ISIS_TXG_IDC_1..9 | 9 (STRING 1 each) | Indirect/direct code flag |
| ISIS_TXG_FREIGT | 1 | Global freight taxable flag |
| ISIS_TXG_OUTSTD | 1 | Outstanding balance flag |
| ISIS_TXG_TOTPER | 1 | Total per period |
| ISIS_TXG_TOFPER | 1 | To/from period reference |

**Key insight:** COLECT_1..12 stores 12 months of collected tax — used to generate state/
local tax remittance reports. A group can combine state + county + city tax codes (PERCC
= rate per jurisdiction), with separate freight-taxable flags per jurisdiction.

---

## ISPRMSTR — IS Payroll Employee Master (Extended)

**Purpose:** Extended payroll employee master. 384 fields — same prefix (BKPR_EMP_*)
as BKPRMSTR. Likely the IS-generation version with more deduction/earning buckets.

Primary key: BKPR_EMP_NUM
Fields: 384

**Selected key fields:**

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKPR_EMP_NUM | UBINARY | 2 | Employee number (PK) |
| BKPR_EMP_FNMI | STRING | 25 | First name + middle initial |
| BKPR_EMP_LNME | STRING | 25 | Last name |
| BKPR_EMP_ADD | STRING | 30 | Address |
| BKPR_EMP_CSZ | STRING | 25 | City/state/zip combined |
| BKPR_EMP_ST | STRING | 2 | State |
| BKPR_EMP_ZIP | STRING | 10 | Zip code |
| BKPR_EMP_PHONE | STRING | 15 | Phone |
| BKPR_EMP_SSN | STRING | 11 | Social security number |
| BKPR_EMP_SDATE | DATE | 4 | Start/hire date |
| BKPR_EMP_TERM | STRING | 1 | Terminated flag |
| BKPR_EMP_MS | STRING | 1 | Marital status |
| BKPR_EMP_FEDEXM | UBINARY | 2 | Federal tax exemptions |
| BKPR_EMP_STEXM | UBINARY | 2 | State tax exemptions |
| BKPR_EMP_PAYTYP | STRING | 1 | Pay type (S=salary, H=hourly, etc.) |
| BKPR_EMP_PAYAMT_1..5 | FLOAT 8 × 5 | Pay rates (5 slots — regular/OT/etc.) |

**Extended deduction/earning arrays** (inferred from field names):
- BKPR_EMP_OAQTD_1..N, OAYTD_1..N — other adjustments QTD/YTD
- BKPR_EMP_EXPACT_1..N, EXPDPT_1..N — expense GL accounts and departments (19 slots each)
- BKPR_EMP_UODQTD_1..19, UODYTD_1..19 — user-defined deduction QTD/YTD (19 deductions)
- BKPR_EMP_UDEQTD_1..N, UDEYTD_1..N — user-defined earnings QTD/YTD
- BKPR_EMP_UODAMT_1..19 — user-defined deduction amounts
- BKPR_EMP_UODYLM_1..19 — user-defined deduction year-limit
- BKPR_EMP_UODLMT_1..19 — user-defined deduction limit per period
- BKPR_EMP_UDEAMT_1..19, UDELMT_1..19, UDEYLM_1..19 — same for earnings
- BKPR_EMP_VCAP — vacation accrual cap
- BKPR_EMP_LSTPR — last payroll date
- BKPR_EMP_SHQTD — shift differential QTD
- BKPR_EMP_QTR — current quarter
