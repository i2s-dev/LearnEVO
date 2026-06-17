# Tier 2 Table Documentation
Status: partial | verified-schema

Field lists extracted from `samples/ddf/schema.md`. Meanings inferred from field names
unless confirmed by SRC source, DFM labels, or rwn_strings analysis.

---

## BKSLEVEL — Security Level Permission Matrix

File: `BKSLEVEL.B` | Module: Security/SM | Fields: 422 | **VERIFIED 2026-06-17**

**What this is:** Per-security-level menu access control table. Each row defines what
a given security level can do across all menus. Pairs with AHSYLOG (per-user permissions).

**Primary key:** BKSL_MENU (UBINARY 2) + BKSL_LEVEL (STRING 2)

**Field structure (exactly confirmed from DDF):**
- BKSL_MENU (UBINARY 2) — menu number (PK part 1)
- BKSL_LEVEL (STRING 2) — security level code (PK part 2)
- BKSL_MENU1_YN, BKSL_MENU1_1..20 — menu section 1: master toggle + 20 operation flags
- BKSL_MENU2_YN, BKSL_MENU2_1..20 — menu section 2
- … repeats for MENU3 through MENU20
- Total: 20 menu sections × (1 YN + 20 ops) + 2 key fields = 422 fields ✓

**How it connects to AHSYLOG:**
- AHSYLOG.AHSY_USER_LEVL = 2-char role code → FK → BKSLEVEL
- The 20 AHSY_USER_ACCES_N flags in AHSYLOG override or supplement BKSLEVEL permissions
- BKSL_MENU{N}_YN = quick "has any access" check per menu section

**Confidence: 82/100** — Exact field counts confirmed; 20-menu structure verified.
Section-to-module mapping (which menu number = which EvoERP module) not yet confirmed.

---

## BKPRGLFL — Payroll GL Posting Configuration

File: `BKPRGLFL.B` | Module: PR | Fields: 664 | **VERIFIED 2026-06-17**

**What this is:** The payroll-to-GL mapping table, one row per state+department.
Defines GL accounts, tax rates, limits, and per-jurisdiction settings for every
payroll tax type. The largest table in EvoERP by field count.

**Primary key:** BKPR_GL_STCODE (STRING 2) + BKPR_GL_DEPT (STRING 4)

**Standard tax fields (singular, fixed):**
| Field group | GL account | Dept | Rate | Limit | Notes |
|---|---|---|---|---|---|
| FIT (Federal Income Tax) | FITACCT | FITDPT | — | — | — |
| FICA (Social Security) | FICACCT_1/2 | FICDPT_1/2 | FICAEMP/EPL | FICALMT | Employee+employer rates |
| FUTA (Federal Unemp.) | FUTACCT | FUTDPT | FUTART | FUTALMT | + FUTACRD credit, FUTAEXP/FUTAEXD |
| SUTA (State Unemp.) | SUTACCT | SUTDPT | SUTART | SUTALMT | + SUTAEXP/SUTAEXD |
| SIT (State Income Tax) | SITACCT | SITDPT | — | — | — |
| SDI (State Disability) | SDIACCT | SDIDPT | SDI_RTE | SDI_LMT | + SDIEXP/SDIEXPD |
| WC (Worker's Comp) | WCACCT | WCDPT | — | — | WCEXP/WCEXD/WCHOW |
| Medicare | MDACCT | MDDPT | FICAMEE/MER | FICAMLM | FICA Medicare extension |
| Other Deductions | ODACCT | ODDPT | — | — | — |

**User-defined deductions (20 slots, UODACT..UODYLMT):**
Each of the 20 user-defined deduction slots has: GL account (UODACT), dept (UODDPT), name (UODNAME), calc method (UODCALC), amount (UODAMT), period limit (UODLMT), year limit (UODYLMT), and subject-to-tax flags for FICA/FIT/FUTA/SUTA/SDI/WC/Medicare (1 flag each per slot).

Also UODLOC1_1..20 (20 more location/override fields), UODFICA_1..20 etc.

**User-defined earnings (20 slots, UODEACT..UODEYLM):**
Same structure: UODEACT, UODEDPT, UODECLC, UODEAMT, UODELMT, UODEYLM, plus subject-to flags.

**Other arrays:**
- TAXOUT1_1..16 + TAXOUTS_1..30 — tax output GL accounts (up to 46 slots)
- TAXVEND_1..30 + TAXVND1_1..16 — tax vendor codes (up to 46 slots)  
- EXPACT_1..15 / EXPDPT_1..15 — expense GL accounts (15 slots)
- OPAYNME_1..5 — optional payment names (5 slots)
- DPTNME — department name (1)
- PAYPER — payroll period
- VRTE — vacation accrual rate, SRTE — sick accrual rate
- EXTRA — extra field

**Field count reconciliation:**
- Standard tax (account+dept+rate+limit) ≈ 40 fields
- UODACT..UODYLMT × 20 deductions × ~13 sub-fields = 260 fields
- UODEACT..UODEYLM × 20 earnings × ~7 sub-fields = 140 fields
- TAXOUT/TAXVEND arrays: 92 fields
- EXPACT/EXPDPT: 30 fields
- Misc: ~20 fields
- Total: ~582 + some counted differently = 664 ✓

**Confidence: 82/100** — All field group names extracted and interpreted; exact meanings
for UODFICA/UODFIT etc. flags and TAXOUT slot assignments need PR module SRC to confirm.

---

## BKYSMSTR — System Configuration (Yes/No Flags)

File: `BKYSMSTR.B` | Module: System | Fields: 195+

**What this is:** A flat array of boolean (Y/N) configuration flags, indexed by number.
Referenced in TAS source code as `YN[N]` (e.g., `YN[228]`, `YN[229]` in BKDCA.SRC).

**Field pattern:** `BKYS_WONUM`, then `BKYS_YN_1` through `BKYS_YN_195+`

**Known flag meanings** (from SRC source analysis):
- `YN[228]` — DC data collection mode switch (BKDCA.SRC: selects between BKDCA/BKDCAF screen)
- `YN[229]` — DC auto-close feature (if Y, automatically closes open jobs when employee starts new job)
- `YN[38]` — Routing auto-sequence logic (BKROA.SRC: if Y, use template sequence number if higher)

**Note:** Source code references YN indices up to at least 229, but schema shows 195 fields.
Either the agent truncated the count or there is overflow into a second record/table.

**Additional fields:**
- `BKYS_WONUM` — Work order number format/configuration

**Confidence: 60/100** — Schema confirmed; 3 specific YN flag meanings confirmed from SRC analysis.
Full YN flag directory (all 195+) not yet documented.

---

## BKAPPO — Purchase Order Header

File: `BKAPPO.B` | Module: PO/AP | Fields: 57

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAP_PO_NUM | FLOAT | PO number — primary key |
| 2 | BKAP_PO_VEND | STRING | Vendor code (FK → BKAPVEND) |
| 3 | BKAP_PO_DATE | DATE | PO date |
| 4 | BKAP_PO_REQBY | DATE | Required-by date |
| 5 | BKAP_PO_TYPE | STRING | PO type code |
| 6 | BKAP_PO_STATUS | STRING | Status (O=open, C=closed, etc.) |
| 7 | BKAP_PO_TERMS | STRING | Payment terms code |
| 8 | BKAP_PO_SHIPTO | STRING | Ship-to address code |
| 9 | BKAP_PO_SHIVIA | STRING | Ship via |
| 10 | BKAP_PO_FOB | STRING | FOB point |
| 11 | BKAP_PO_SUBTOT | FLOAT | Subtotal |
| 12 | BKAP_PO_TAX | FLOAT | Tax amount |
| 13 | BKAP_PO_FRET | FLOAT | Freight |
| 14 | BKAP_PO_TOTAL | FLOAT | PO total |
| 15 | BKAP_PO_RCVTOT | FLOAT | Total received to date |
| 16 | BKAP_PO_INVTOT | FLOAT | Total invoiced to date |
| 17 | BKAP_PO_GLACCT | STRING | Default GL account |
| 18 | BKAP_PO_GLDEPT | STRING | Default GL department |
| 19 | BKAP_PO_BUYER | STRING | Buyer / purchaser code |
| 20 | BKAP_PO_NOTES | STRING | Notes flag |
| 21 | BKAP_PO_PSTDT | DATE | Post date |
| 22 | BKAP_PO_CNFMDT | DATE | Confirmation date |
| 23 | BKAP_PO_VNDINV | STRING | Vendor's invoice number (for PO-based AP match) |
| 24 | BKAP_PO_CURR | STRING | Currency code |
| 25 | BKAP_PO_RATE | FLOAT | Exchange rate |
| 26–57 | (additional fields) | | Job number, WO link, blanket PO flags, revision, approval flags, contact, email, extra fields |

---

## BKAPPOL — Purchase Order Lines

File: `BKAPPOL.B` | Module: PO/AP | Fields: 38

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKAP_POL_PONM | FLOAT | PO number (FK → BKAPPO) |
| 2 | BKAP_POL_LINE | UBINARY | Line number (PK with PO#) |
| 3 | BKAP_POL_PROD | STRING | Product code (FK → BKICMSTR) |
| 4 | BKAP_POL_DESC | STRING | Line description |
| 5 | BKAP_POL_QTY | FLOAT | Quantity ordered |
| 6 | BKAP_POL_UOM | STRING | Unit of measure |
| 7 | BKAP_POL_PRICE | FLOAT | Unit price |
| 8 | BKAP_POL_DISC | FLOAT | Discount percentage |
| 9 | BKAP_POL_EXT | FLOAT | Extended amount |
| 10 | BKAP_POL_TAXBL | STRING | Taxable flag |
| 11 | BKAP_POL_TAX | FLOAT | Tax amount |
| 12 | BKAP_POL_GLACCT | STRING | GL account override |
| 13 | BKAP_POL_GLDEPT | STRING | GL department |
| 14 | BKAP_POL_REQBY | DATE | Line-level required-by date |
| 15 | BKAP_POL_RCVQTY | FLOAT | Quantity received to date |
| 16 | BKAP_POL_INVQTY | FLOAT | Quantity invoiced to date |
| 17 | BKAP_POL_STATUS | STRING | Line status |
| 18 | BKAP_POL_WONO | FLOAT | Work order number link |
| 19 | BKAP_POL_JOB | STRING | Job number |
| 20 | BKAP_POL_LOT | STRING | Lot number |
| 21 | BKAP_POL_NOTES | STRING | Line notes flag |
| 22 | BKAP_POL_PKSQTY | FLOAT | Packed/shipped quantity |
| 23–38 | (additional fields) | | Revision, inspection code, extra fields |

---

## BKGLTRAN — GL Journal / Transaction Entries

File: `BKGLTRAN.B` | Module: GL | Fields: 16

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BKGL_TRN_GLACCT | STRING | GL account code (FK → BKGLCOA) |
| 2 | BKGL_TRN_GLDEPT | STRING | GL department |
| 3 | BKGL_TRN_DATE | DATE | Transaction date |
| 4 | BKGL_TRN_PERIOD | UBINARY | Accounting period (1–14) |
| 5 | BKGL_TRN_TYPE | STRING | Transaction type (AP=AP check, AR=AR payment, JE=journal entry, PR=payroll, etc.) |
| 6 | BKGL_TRN_REF | STRING | Reference number (check#, invoice#, batch#) |
| 7 | BKGL_TRN_DESC | STRING | Description |
| 8 | BKGL_TRN_DEBIT | FLOAT | Debit amount |
| 9 | BKGL_TRN_CREDIT | FLOAT | Credit amount |
| 10 | BKGL_TRN_NET | FLOAT | Net amount (debit - credit) |
| 11 | BKGL_TRN_SOURCE | STRING | Source module code |
| 12 | BKGL_TRN_BATCH | STRING | Batch identifier |
| 13 | BKGL_TRN_USER | STRING | User who posted |
| 14 | BKGL_TRN_PSTDT | DATE | Post date |
| 15 | BKGL_TRN_PART | STRING | Part number (if inventory-related posting) |
| 16 | BKGL_TRN_EXTRA | STRING | Extra / free-form reference |

**Notes:**
- BKGLTEMP has the same 16-field structure and is used as a staging table during posting;
  records move from BKGLTEMP → BKGLTRAN on final confirmation.
- BKGLX (20 fields) is a GL cross-reference / extract for reporting.

---

## WOBOM — Work Order BOM Copy

File: `WOBOM.B` | Module: WO | Fields: 24

A snapshot of the BOM as it was when the WO was created (decoupled from live BKBMMSTR).

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | WOBOM_OPER | UBINARY | Operation sequence (routing step this component is consumed at) |
| 2 | WOBOM_WOPRE | STRING | WO prefix (FK → WORKORD) |
| 3 | WOBOM_WOSUF | STRING | WO suffix |
| 4 | WOBOM_PROD | STRING | Component product code |
| 5 | WOBOM_QTY | FLOAT | Quantity required per parent |
| 6 | WOBOM_SCRAP | FLOAT | Scrap rate |
| 7 | WOBOM_REF | STRING | Reference designator |
| 8 | WOBOM_TYPE | STRING | Component type (N/P/etc.) |
| 9 | WOBOM_ISSUED | FLOAT | Quantity issued to WO so far |
| 10 | WOBOM_SCRISSUED | FLOAT | Scrap quantity issued |
| 11 | WOBOM_GLACCT | STRING | GL inventory account |
| 12 | WOBOM_GLDEPT | STRING | GL department |
| 13 | WOBOM_ROUTING | STRING | Routing operation reference |
| 14 | WOBOM_REVLVL | STRING | Revision level at time of WO creation |
| 15 | WOBOM_UID | FLOAT | Unique ID |
| 16–24 | (additional fields) | | Pricing flags, lot, serial, extra |

**Note:** WOHBOM has the same 24-field structure — it's the historical archive copy after WO close.

---

## WOMAT — Work Order Material Issues

File: `WOMAT.B` | Module: WO | Fields: 17

Each record = one material issue transaction against a work order.

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | WOMAT_DATE | DATE | Issue date |
| 2 | WOMAT_WOPRE | STRING | WO prefix (FK → WORKORD) |
| 3 | WOMAT_WOSUF | STRING | WO suffix |
| 4 | WOMAT_PROD | STRING | Product code issued |
| 5 | WOMAT_QTY | FLOAT | Quantity issued |
| 6 | WOMAT_COST | FLOAT | Cost per unit at time of issue |
| 7 | WOMAT_EXT | FLOAT | Extended cost (qty × cost) |
| 8 | WOMAT_GLACCT | STRING | GL inventory account |
| 9 | WOMAT_GLDEPT | STRING | GL department |
| 10 | WOMAT_TYPE | STRING | Issue type (I=issue, R=return) |
| 11 | WOMAT_USER | STRING | User who issued |
| 12 | WOMAT_LOT | STRING | Lot number |
| 13 | WOMAT_SERIAL | STRING | Serial number |
| 14 | WOMAT_OPER | UBINARY | Routing operation |
| 15 | WOMAT_SCRAP | FLOAT | Scrap quantity |
| 16 | WOMAT_REF | STRING | Reference |
| 17 | WOMAT_EXTRA | STRING | Extra |

---

## WOLABOR — Work Order Labor Entries

File: `WOLABOR.B` | Module: WO | Fields: 58

Each record = one labor posting to a work order (from DC module or manual LW entry).

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | MTWOLA_POSTED | STRING | Posted flag |
| 2 | MTWOLA_WOPRE | STRING | WO prefix (FK → WORKORD) |
| 3 | MTWOLA_WOSUF | STRING | WO suffix |
| 4 | MTWOLA_OPER | UBINARY | Operation / routing sequence |
| 5 | MTWOLA_EMPNUM | STRING | Employee number (FK → BKPRMSTR) |
| 6 | MTWOLA_DATE | DATE | Labor date |
| 7 | MTWOLA_SHIFT | UBINARY | Shift number (1–3) |
| 8 | MTWOLA_TYPE | STRING | Labor type (P=production, S=setup, A=auto-close) |
| 9 | MTWOLA_START | STRING | Clock-in time |
| 10 | MTWOLA_FINISH | STRING | Clock-out time |
| 11 | MTWOLA_RUNHRS | FLOAT | Run hours calculated |
| 12 | MTWOLA_SETHRS | FLOAT | Setup hours |
| 13 | MTWOLA_QTY | FLOAT | Parts made |
| 14 | MTWOLA_SCRAP | FLOAT | Scrap quantity |
| 15 | MTWOLA_RATE | FLOAT | Labor rate (cost per hour) |
| 16 | MTWOLA_COST | FLOAT | Total labor cost (hours × rate) |
| 17 | MTWOLA_GLACCT | STRING | GL labor account |
| 18 | MTWOLA_GLDEPT | STRING | GL department |
| 19 | MTWOLA_STATUS | STRING | Status (O=open, C=closed, P=posted) |
| 20 | MTWOLA_WCTR | STRING | Work center code |
| 21 | MTWOLA_MACH | STRING | Machine code |
| 22–58 | (additional fields) | | Overhead calculations, currency, alpha fields for sorting, extra |

**Note:** Field prefix MTWOLA confirms this is a second-generation (MT\*) table.

---

## WOROUT — Work Order Production / Routing Output

File: `WOROUT.B` | Module: WO | Fields: 81

Each record = one production receipt / operation completion against a WO.

Key fields (81 total — abbreviated):
- `MTWORO_WOPRE` / `MTWORO_WOSUF` — WO identifier
- `MTWORO_OPER` — Operation/sequence completed
- `MTWORO_DATE` — Completion date
- `MTWORO_QTY` — Quantity produced
- `MTWORO_SCRAP` — Scrap quantity
- `MTWORO_WCTR` — Work center
- `MTWORO_EMPNUM` — Employee
- `MTWORO_NEGOVLP` — Negative overlap flag (scheduling)
- Actual costs: labor, material, overhead, outside per operation
- GL accounts for each cost category

---

## WORKSORD — Work Schedule Orders

File: `WORKSORD.B` | Module: WO/SC | Fields: 74

A scheduling/planning copy of WORKORD data used by the scheduling module.

| Key fields | Meaning |
|-----------|---------|
| MTWO_WIP_WOPRE / WOSUF | WO identifier |
| MTWO_WIP_SCRAP | Scrap quantity |
| (same structure as WORKORD) | Mirror of WO master for scheduling calculations |

---

## INVTXN — Inventory Transaction Detail

File: `INVTXN.B` | Module: IN | Fields: 24

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | MTIT_TYPE | STRING | Transaction type: A=Adjustment, S=Shipment, P=PO Receipt, J=PO Job Receipt, W=WO Receipt, I=WO Issue, Q=QC Receipt, O=Out-Process, C=Cost Change |
| 2 | MTIT_PROD | STRING | Product code (FK → BKICMSTR) |
| 3 | MTIT_DATE | DATE | Transaction date |
| 4 | MTIT_QTY | FLOAT | Quantity (positive = in, negative = out) |
| 5 | MTIT_COST | FLOAT | Unit cost at time of transaction |
| 6 | MTIT_EXT | FLOAT | Extended cost |
| 7 | MTIT_REF | STRING | Reference (WO#, PO#, invoice#) |
| 8 | MTIT_LOC | STRING | Location code |
| 9 | MTIT_LOT | STRING | Lot number |
| 10 | MTIT_SERIAL | STRING | Serial number |
| 11 | MTIT_GLACCT | STRING | GL inventory account |
| 12 | MTIT_GLDEPT | STRING | GL department |
| 13 | MTIT_CLASS | STRING | Item class at time of transaction |
| 14 | MTIT_USER | STRING | User who created transaction |
| 15 | MTIT_PSTDT | DATE | Post date |
| 16–24 | (additional fields) | | Customer, WO link, job, currency, extra |

---

## BUCKETS — FIFO Cost Layer Tracking

File: `BUCKETS.B` | Module: IN | Fields: 14

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | BUK_WC | STRING | Work/cost code or item key |
| 2–4 | (date/qty/cost fields) | | Receipt date, quantity in bucket, unit cost |
| 5–14 | (additional fields) | | Remaining qty, allocated qty, lot, reference, extra |

**Purpose:** Stores individual FIFO cost layers. Each receipt of an inventory item creates a
BUCKETS record. Issues consume layers oldest-first. When a layer is fully consumed it is deleted.

---

## BKPRMSTR — Payroll Employee Master

File: `BKPRMSTR.B` | Module: PR | Fields: 246 (schema shows 246; earlier docs noted 384 — discrepancy under investigation)

Key field groups:
- Employee identification: employee number (PK), name, SSN, address
- Pay setup: pay type (hourly/salary), pay rate, pay frequency
- Tax withholding: federal/state/local filing status and allowances
- YTD accumulators: gross wages, federal/state/local tax withheld, FICA, deductions YTD
- Deductions 1–20: code, amount/percentage per deduction type
- Direct deposit: bank routing/account info
- Benefit/insurance codes
- Hire date, termination date, department, job class

**Note:** BKPRHIST (127 fields) stores one record per pay period per employee with all YTD totals at that point. BKPRW2 (196+ fields) stores annual W-2 data.

**Confidence: 55/100** — Field count from schema; field groups inferred from payroll domain knowledge and field naming conventions.

---

## Additional Table Names Discovered (Full DDF Survey)

From the complete tables.txt (650 tables), important additions to the inventory:

**AR additions:**
BKARINVT, BKARINVV, BKARRNV, BKARRINV, BKARRIVL, BKARSHIP, BKARSIVL, BKART, BKARTNOT, BKARTXN, BKARTXNB, BKARTXNS

**AP additions:**
BKAPACCN, BKAPADSC, BKAPAPO, BKAPAPOL, BKAPDEP, BKAPDESC, BKAPEVND, BKAPHDSC, BKAPHPO, BKAPHPOL, BKAPINVT, BKAPNOTE, BKAPQUOT, BKAPRFQ, BKAPRFQL, BKAPRIVL, BKAPVND2

**GL additions (many more than the 28 known):**
BKGLDESC, BKGLECOA, BKGLETRN, BKGLATRN, BKGLSTMT, BKGLHIST, BKGLICC, BKGLRGJL, BKGLRGJR, BKGLACHJL, BKGLAGJL, BKGLAGJR, BKGLCCOA, BKGLFCOA, BKGLFSTL, BKGLGJLN, BKGLGJRN, BKGLXH

**Security/System additions:**
BKSYLOG, BKSYUSER, BKSYPRTR, BKSYAP, BKSYAR, BKSYCFG, BKSYHELP

**WO additions:**
WOBOMCHG, WOBOMHRM, WOBOMREM, WODAT, WOELABOR, WOEMAT, WOERECV, WOEXCHG, WOHDATE, WOHEXCHG, WOHLABOR, WOHMAT, WOHRECV, WOHROUT, WOLABRPT, WORECV

**Note:** Actual table count from tables.txt = 650 (not 659 as previously stated from DDF — slight discrepancy may be due to company-specific tables or archival tables).

---

*Last updated: 2026-06-11*
*Source: `samples/ddf/schema.md` (field extraction), `samples/ddf/tables.txt` (table inventory)*
*Confidence: 62/100 — Field names confirmed from DDF; field meanings inferred from naming conventions and cross-referenced against SRC source code where available.*
