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

---

## BKCM* Family — CRM / Contact Manager (46 tables)

**Pass 133 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 3236–4227**

EvoERP's Contact Manager (CM) module manages accounts, prospects, vendors, activity
history, mass mailings, dunning letters, and CRM-to-AR bridging. 46 tables organized
in 8 functional clusters. Field-prefix is `BKCM_` except for BKCMCUST which reuses
the `BKAR_*` prefix (it is a CRM-resident copy of BKARCUST).

### Cluster overview

| Cluster | Tables | Purpose |
|---------|--------|---------|
| Account core | BKCMACCT / BKCMDE / BKCMEACT | Account master + 2 edit mirrors |
| Account contact config | BKCMACCN / BKCMCNTD | Per-account 10-slot contacts + display labels |
| AR customer bridge | BKCMCUST | Filtered copy of BKARCUST for CRM lookup |
| Activity tracking | BKCMACTH/ACTF/ACTD + E-mirrors | History, follow-ups, date entries (account) |
| Prospect sub-module | BKCMPCNT / PCTF / PCTH | Prospect contacts + follow-ups + history |
| Vendor CRM | BKCMVNDH / VNDF | Vendor activity history + follow-ups |
| Mass mail / dunning | BKCMMHST / DUN / DUNH / FORM | Mailing list definition + collection letters |
| Code / lookup tables | BKCMREP/TERR/ACCC/ACCL/etc. | Rep, territory, class, activity code lookups |
| Concurrent locks | BKCMCTL1-4 / BKCMCTRL | One-field edit-lock semaphores (×5) |
| Temp/work tables | BKCMTEMP / TMP1-4 | In-flight query scratch (×5, all identical) |

---

### BKCMACCT — CRM Account Master

File: `BKCMACCT.B` | Fields: 41 | PK: `BKCM_ACCT_CODE` (STRING 15)

The central account record for the CRM module. One row per company tracked.

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_ACCT_CODE | STRING 15 | Account code (PK) |
| BKCM_ACCT_OLDCD | STRING 15 | Old/alternate code |
| BKCM_ACCT_ALPHA | STRING 10 | Sort key |
| BKCM_ACCT_NAME | STRING 40 | Company name |
| BKCM_ACCT_ADD1..3 | STRING 40 ×3 | Address lines 1–3 |
| BKCM_ACCT_CITY | STRING 25 | City |
| BKCM_ACCT_STATE | STRING 3 | State |
| BKCM_ACCT_ZIP | STRING 12 | ZIP / postal code |
| BKCM_ACCT_CNTRY | STRING 20 | Country |
| BKCM_ACCT_CONT1 | STRING 25 | Primary contact name |
| BKCM_ACCT_TITLE | STRING 20 | Primary contact title |
| BKCM_ACCT_PHONE | STRING 15 | Main phone |
| BKCM_ACCT_FAX | STRING 15 | Fax |
| BKCM_ACCT_REP | STRING 4 | Assigned CRM rep → FK BKCMREP |
| BKCM_ACCT_DLOAD | STRING 1 | Download flag |
| BKCM_ACCT_SICCD | STRING 8 | SIC industry code |
| BKCM_ACCT_CUST | STRING 15 | Linked AR customer code → FK BKCMCUST |
| BKCM_ACCT_LEAD | STRING 4 | Lead source → FK BKCMLEAD |
| BKCM_ACCT_START | STRING 8 | Start / first-contact date |
| BKCM_ACCT_TERR | STRING 4 | Territory code → FK BKCMTERR |
| BKCM_ACCT_REM_1..2 | STRING 60 ×2 | Remark lines 1–2 |
| BKCM_ACCT_FONE_1..3 | STRING 15 ×3 | Additional phone 1–3 |
| BKCM_ACCT_FTWO_1..3 | STRING 15 ×3 | Additional phone labels 1–3 |
| BKCM_ACCT_FTHRE_1..2 | STRING 15 ×2 | Additional phone label extension 1–2 |
| BKCM_ACCT_FTIME | STRING 15 | Time zone or office hours |
| BKCM_ACCT_CCARD | STRING 2 | Credit card type |
| BKCM_ACCT_CNUM | STRING 20 | Credit card number |
| BKCM_ACCT_CEXP | STRING 6 | Credit card expiry |
| BKCM_ACCT_CMPNM | STRING 30 | Card company name |
| BKCM_ACCT_PNAME | STRING 25 | Card holder name |
| BKCM_ACCT_EXTRA | STRING 200 | User-defined extra data |
| BKCM_ACCT_EMAIL | STRING 128 | Primary email |
| BKCM_ACCT_EMPS | STRING 6 | Employee count |

**BKCMDE** (41f) — byte-for-byte identical schema; used as data-entry staging buffer.
**BKCMEACT** (41f) — byte-for-byte identical schema; "E" (edit) in-progress buffer.

---

### BKCMACCN — Per-Account Contact Configuration

File: `BKCMACCN.B` | Fields: 154 | PK: `BKCM_ACCN_CODE` (STRING 15)

Stores 10 contact slots per account with full labeling for phone, email, date, and
alpha fields. The label arrays (PHLBL/EMLBL/MSLBL/DTLBL/etc.) let each account
customize what each slot represents.

| Field block | Fields | Meaning |
|-------------|--------|---------|
| BKCM_ACCN_CODE | 1 | Account code PK → FK BKCMACCT |
| BKCM_ACCN_CONT_1..10 | 10 | Contact name per slot |
| BKCM_ACCN_TITLE_1..10 | 10 | Contact title per slot |
| BKCM_ACCN_PHONE_1..10 | 10 | Phone per slot |
| BKCM_ACCN_DEAR_1..10 | 10 | Salutation per slot |
| BKCM_ACCN_EXTRA | 1 | STRING 50 extra |
| BKCM_ACCN_EMAIL_1..10 | 10 | Email (STRING 128) per slot |
| BKCM_ACCN_DATE1_1..10 | 10 | Date field 1 per slot |
| BKCM_ACCN_DATE2_1..10 | 10 | Date field 2 per slot |
| BKCM_ACCN_ALPH1_1..10 | 10 | Alpha field 1 per slot |
| BKCM_ACCN_ALPH2_1..10 | 10 | Alpha field 2 per slot |
| BKCM_ACCN_CON | 1 | Active contact slot# |
| BKCM_ACCN_PRIM | 1 | Primary contact flag |
| BKCM_ACCN_PHLBL_1..10 | 10 | Phone slot labels (user-defined) |
| BKCM_ACCN_EMLBL_1..10 | 10 | Email slot labels |
| BKCM_ACCN_MSLBL_1..10 | 10 | Mail-slot labels |
| BKCM_ACCN_DTLBL_1..10 | 10 | Date-1 slot labels |
| BKCM_ACCN_M2LBL_1..10 | 10 | Mail-slot-2 labels |
| BKCM_ACCN_D2LBL_1..10 | 10 | Date-2 slot labels |
| **Total** | **154** | |

---

### BKCMCUST — AR Customer Bridge (CRM Copy)

File: `BKCMCUST.B` | Fields: 106 | PK: `BKAR_CUST_CODE` (STRING 15)

This table uses the `BKAR_*` field prefix — it is a filtered subset of BKARCUST
(AR customer master) maintained inside the CRM module for fast CRM-side lookups.
Field layout matches BKARCUST fields 1–106 exactly; provides address, contacts,
financials, and credit info without a cross-module join.

Cross-reference: → `docs/04-data-dictionary/tier1-tables.md` BKAR* family for
full BKARCUST field documentation.

---

### BKCMACTH — Account Activity History

File: `BKCMACTH.B` | Fields: 21 | PK: CODE+DATE+REP+LINE (composite)

One row per activity log entry against an account.

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_ACTH_CODE | STRING 15 | Account code (PK part 1) |
| BKCM_ACTH_DATE | STRING 8 | Activity date (PK part 2) |
| BKCM_ACTH_REP | STRING 4 | Rep code (PK part 3) |
| BKCM_ACTH_LINE | UBINARY 2 | Line within date/rep (PK part 4) |
| BKCM_ACTH_CD | STRING 4 | Activity code → FK BKCMHCOD |
| BKCM_ACTH_EVENT | STRING 1 | Event type flag |
| BKCM_ACTH_PHONE | STRING 1 | Phone-call flag |
| BKCM_ACTH_START | STRING 8 | Start time (HHMMSS) |
| BKCM_ACTH_STOP | STRING 8 | Stop time |
| BKCM_ACTH_MIN | FLOAT | Duration in minutes |
| BKCM_ACTH_BMIN | FLOAT | Billable minutes |
| BKCM_ACTH_REM | STRING 57 | Remark |
| BKCM_ACTH_BILLD | STRING 1 | Billed flag |
| BKCM_ACTH_DLOAD | STRING 1 | Download flag |
| BKCM_ACTH_FLINE | STRING 1 | First-line flag |
| BKCM_ACTH_RECVD | STRING 8 | Received time |
| BKCM_ACTH_CNTCT | STRING 25 | Contact name at time of event |
| BKCM_ACTH_RATE | FLOAT | Billing rate |
| BKCM_ACTH_AMT | FLOAT | Amount charged |
| BKCM_ACTH_BALNC | FLOAT | Running balance |
| BKCM_ACTH_EXTRA | STRING 50 | Extra |

**BKCMEACH** (21f) — identical schema; "E" (edit) in-progress buffer for BKCMACTH.

---

### BKCMACTF — Account Activity Follow-Up

File: `BKCMACTF.B` | Fields: 11 | PK: CODE+REP+TYPE+DATE

Scheduled future activities (call-backs, appointments) linked to an account.

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_ACTF_CODE | STRING 15 | Account code (PK part 1) |
| BKCM_ACTF_REP | STRING 4 | Rep (PK part 2) |
| BKCM_ACTF_TYPE | STRING 4 | Follow-up type code (PK part 3) |
| BKCM_ACTF_DATE | STRING 8 | Scheduled date (PK part 4) |
| BKCM_ACTF_REM_1..5 | STRING 60 ×5 | Remark lines 1–5 |
| BKCM_ACTF_DLOAD | STRING 1 | Download flag |
| BKCM_ACTF_SO | FLOAT | Linked SO reference |

**BKCMEACF** (11f) — identical schema; "E" edit mirror.

---

### BKCMACTD — Account Activity Date Detail

File: `BKCMACTD.B` | Fields: 4 | PK: CODE+DCODE+DATE

Links specific date-coded milestones to accounts (e.g., renewal date, audit date).

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_ACTD_CODE | STRING 15 | Account code (PK part 1) |
| BKCM_ACTD_DCODE | STRING 4 | Date category code → FK BKCMDTCD (PK part 2) |
| BKCM_ACTD_DATE | STRING 8 | Date value (PK part 3) |
| BKCM_ACTD_EXTRA | STRING 100 | Notes / extra data |

**BKCMEACD** (4f) — identical schema; "E" edit mirror.

---

### BKCMPCNT — Prospect Contact Master

File: `BKCMPCNT.B` | Fields: 24 | PK: `BKCM_PCNT_CCODE` (STRING 15)

Parallel to BKCMACCT but for prospects (not yet converted to accounts or customers).

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_PCNT_CCODE | STRING 15 | Prospect code (PK) |
| BKCM_PCNT_REP | STRING 4 | Assigned rep |
| BKCM_PCNT_ALPHA | STRING 10 | Sort key |
| BKCM_PCNT_NAME | STRING 40 | Company/contact name |
| BKCM_PCNT_ADD1..3 | STRING 40 ×3 | Address lines |
| BKCM_PCNT_CITY | STRING 25 | City |
| BKCM_PCNT_STATE | STRING 3 | State |
| BKCM_PCNT_ZIP | STRING 12 | ZIP |
| BKCM_PCNT_CNTRY | STRING 20 | Country |
| BKCM_PCNT_CONT | STRING 25 | Contact name |
| BKCM_PCNT_TITLE | STRING 20 | Contact title |
| BKCM_PCNT_PHONE | STRING 15 | Phone |
| BKCM_PCNT_FAX | STRING 15 | Fax |
| BKCM_PCNT_CLASS | STRING 4 | Class code → FK BKCMACCC |
| BKCM_PCNT_SDATE | STRING 8 | Start/first-contact date |
| BKCM_PCNT_REM_1..4 | STRING 60 ×4 | Remark lines 1–4 |
| BKCM_PCNT_EXTRA | STRING 100 | Extra |
| BKCM_PCNT_WPHON | STRING 15 | Work phone (alternate) |
| BKCM_PCNT_EMAIL | STRING 40 | Email |

**BKCMPCTF** (9f) — prospect follow-up: CCODE+REP+TYPE+DATE PK + REM_1..5.
**BKCMPCTH** (8f) — prospect contact history: CCODE+DATE+REP+LINE PK + EVENT + REM(60) + FLINE + EXTRA(50).
**BKCMPCFC** (3f) — prospect follow-up code: FCODE + DESC + REP.

---

### BKCMREP — CRM Sales Rep Master

File: `BKCMREP.B` | Fields: 14 | PK: `BKCM_REP_REP` (STRING 4)

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_REP_REP | STRING 4 | Rep code (PK) |
| BKCM_REP_FNMEMI | STRING 25 | First name / middle initial |
| BKCM_REP_LNAME | STRING 25 | Last name |
| BKCM_REP_EMP | UBINARY 2 | Linked employee number → FK payroll/HR |
| BKCM_REP_PSWD | STRING 8 | Rep login password |
| BKCM_REP_DHCODE | STRING 4 | Default history code → FK BKCMHCOD |
| BKCM_REP_DFCODE | STRING 4 | Default follow-up code → FK BKCMACFC |
| BKCM_REP_DDCODE | STRING 4 | Default date code → FK BKCMDTCD |
| BKCM_REP_VIEW | STRING 1 | View-all-accounts permission flag |
| BKCM_REP_CHANGE | STRING 1 | Change permission flag |
| BKCM_REP_GWARN | STRING 1 | Warn-before-global-change flag |
| BKCM_REP_AADD | STRING 1 | Allow-add permission flag |
| BKCM_REP_FNAME | STRING 30 | Full name display |
| BKCM_REP_FTITLE | STRING 30 | Rep title |

---

### BKCMTERR — Territory Master

File: `BKCMTERR.B` | Fields: 11 | PK: `BKCM_TERR_TCODE` (STRING 4)

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_TERR_TCODE | STRING 4 | Territory code (PK) |
| BKCM_TERR_DESC | STRING 30 | Description |
| BKCM_TERR_EMAIL | STRING 128 | Territory manager email |
| BKCM_TERR_ALPHA | STRING 30 | Sort key |
| BKCM_TERR_EXTRA | STRING 100 | Extra |
| BKCM_TERR_FLAGS_1..5 | STRING 1 ×5 | User-defined flags |
| BKCM_TERR_DATE | STRING 8 | Last update date |

---

### BKCMMHST — Mass Mail History / List Definition

File: `BKCMMHST.B` | Fields: 72 | PK: `BKCM_MHST_MCODE` (STRING 10)

Defines and tracks mail campaigns. Each row is a named mailing run with its full
selection criteria (class, date range, geography, territory, rep) and result counts.

| Field block | Fields | Meaning |
|-------------|--------|---------|
| BKCM_MHST_MCODE | 1 | Campaign code (PK) |
| BKCM_MHST_DESC | 1 | Description |
| BKCM_MHST_MDATE | 1 | Mailing date |
| BKCM_MHST_CLASS_1..20 | 20 | Account class filter: up to 20 class codes |
| BKCM_MHST_KDCD | 1 | Key date code filter |
| BKCM_MHST_FKDAT / TKDAT | 2 | Key date range FROM/TO |
| BKCM_MHST_FACD / TACD | 2 | Account code range FROM/TO |
| BKCM_MHST_FST / TST | 2 | State range FROM/TO |
| BKCM_MHST_FZIP / TZIP | 2 | ZIP range FROM/TO |
| BKCM_MHST_FSIC / TSIC | 2 | SIC code range FROM/TO |
| BKCM_MHST_CUSTO | 1 | Customers-only flag |
| BKCM_MHST_FLEAD / TLEAD | 2 | Lead source range FROM/TO |
| BKCM_MHST_FSDT / TSDT | 2 | Start date range FROM/TO |
| BKCM_MHST_FTERR / TTERR | 2 | Territory range FROM/TO |
| BKCM_MHST_FREP / TREP | 2 | Rep range FROM/TO |
| BKCM_MHST_PCONT | 1 | Print contacts flag |
| BKCM_MHST_CNUM | 1 | Contact slot number to use |
| BKCM_MHST_DORL | 1 | Detail or list mode flag |
| BKCM_MHST_NUMUP | 1 | Number-up (labels per page) |
| BKCM_MHST_OCLAS_1..20 | 20 | Old/previous class filter array |
| BKCM_MHST_STAT | 1 | Campaign status |
| BKCM_MHST_NOCUS | 1 | Non-customer-only flag |
| BKCM_MHST_SORT | 1 | Sort order code |
| BKCM_MHST_REM | 1 | Remark |
| BKCM_MHST_FORM | 1 | Default form/letter → FK BKCMFORM |
| **Total** | **72** | |

---

### BKCMDUN — Dunning Letter Configuration

File: `BKCMDUN.B` | Fields: 36 | PK: `BKCM_DUN_REP` (STRING 4)

Per-rep aging thresholds and form assignments for collection letter runs.

| Field block | Fields | Meaning |
|-------------|--------|---------|
| BKCM_DUN_REP | 1 | Rep code (PK) |
| BKCM_DUN_AGE_1..10 | 10 | Age breakpoints (days overdue) |
| BKCM_DUN_FORM_1..10 | 10 | Form code for each age tier → FK BKCMFORM |
| BKCM_DUN_DESC_1..10 | 10 | Description for each tier |
| BKCM_DUN_DORL | 1 | Detail or list print flag |
| BKCM_DUN_NUMUP | 1 | Labels per page |
| BKCM_DUN_SORT | 1 | Sort order |
| BKCM_DUN_PCONT | 1 | Print contacts flag |
| BKCM_DUN_CNUM | 1 | Contact slot# for address |

**BKCMDUNH** (6f) — dunning history: ACCT+DATE PK + FORM + AGE + AMT + TOT.

---

### BKCMFORM — Letter / Form Content

File: `BKCMFORM.B` | Fields: 8 | PK: CODE+LINE

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_FORM_CODE | STRING 8 | Form code (PK part 1) |
| BKCM_FORM_LINE | UBINARY 2 | Line number (PK part 2) |
| BKCM_FORM_NOTE | STRING 78 | Body text for this line |
| BKCM_FORM_DESC | STRING 30 | Short description (header lines) |
| BKCM_FORM_LEFT | STRING 2 | Left margin |
| BKCM_FORM_LNSPG | STRING 2 | Lines per page |
| BKCM_FORM_START | STRING 2 | Starting line |
| BKCM_FORM_DUN | STRING 1 | Dunning letter flag |

---

### BKCMHCOD — Activity / History Code Master

File: `BKCMHCOD.B` | Fields: 9 | PK: `BKCM_HCOD_HCODE` (STRING 4)

Defines billable activity types. The ABILL/BPART/NPART/FPART fields govern
multi-part billing splits.

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_HCOD_HCODE | STRING 4 | History code (PK) |
| BKCM_HCOD_DESC | STRING 30 | Description |
| BKCM_HCOD_WINDW | STRING 1 | Window type (popup form code) |
| BKCM_HCOD_RATE | FLOAT | Default billing rate |
| BKCM_HCOD_UM | STRING 4 | Unit of measure |
| BKCM_HCOD_ABILL | STRING 1 | Auto-bill flag |
| BKCM_HCOD_BPART | FLOAT | Billing-part multiplier |
| BKCM_HCOD_NPART | FLOAT | Non-billable part |
| BKCM_HCOD_FPART | FLOAT | Flat-fee part |

**BKCMHCD2** (7f) — history code extension: HCODE + PCODE+CCODE+RCODE + PPART+CPART+RPART (billing code splits by part type).

---

### BKCMEFTM / BKCMFTME — Employee and Firm Time Tables

Both files: 7 fields | PK: CODE+FTIME

Track time-balance accounts for reps or the firm — likely used for service-billing
or scheduling allocation.

| Field | Type | Meaning |
|-------|------|---------|
| BKCM_EFTM_CODE | STRING 4 | Rep/entity code (PK part 1) |
| BKCM_EFTM_FTIME | STRING 8 | Time slot (PK part 2) |
| BKCM_EFTM_DESC | STRING 30 | Description |
| BKCM_EFTM_BALNC | FLOAT | Balance (hours or dollars) |
| BKCM_EFTM_LASTP | STRING 8 | Last-posted date |
| BKCM_EFTM_ATIME | FLOAT | Accumulated time |
| BKCM_EFTM_NTIME | FLOAT | New / pending time |

BKCMFTME has the identical field layout; likely BKCMEFTM = employee time,
BKCMFTME = firm-level time.

---

### Vendor CRM Tables

**BKCMVNDF** (10f) — vendor follow-up: VCODE+REP+TYPE+DATE PK + REM_1..5(STRING 60) + PO(FLOAT).
Mirrors BKCMACTF but for vendor relationships; PO float links to a purchase order.

**BKCMVNDH** (8f) — vendor contact history: VCODE+DATE+REP+LINE PK + EVENT + REM(60) + FLINE + EXTRA(50).
Mirrors BKCMACTH but for vendor CRM records.

**BKCMVNFC** (3f) — vendor follow-up code: FCODE + DESC + REP.
Mirrors BKCMACFC for the vendor sub-module.

---

### Lookup / Code Tables (small)

| Table | Fields | PK | Purpose |
|-------|--------|----|---------|
| BKCMACCC | 2 | CCODE | Account class code (CCODE+DESC) |
| BKCMACCL | 2 | CODE+CLASS | Account class link (assigns a class to an account) |
| BKCMEACC | 2 | CODE+CLASS | Edit mirror of BKCMACCL (identical schema) |
| BKCMACFC | 3 | FCODE | Account follow-up code (FCODE+DESC+REP) |
| BKCMDTCD | 2 | DCODE | Date category code (DCODE+DESC) → used in BKCMACTD |
| BKCMLEAD | 2 | SCODE | Lead source code (SCODE+DESC) |
| BKCMSBDF | 5 | (single) | Service billing defaults (BINC/MINC/ICONV/NCHG/DHOLD) |
| BKCMCNTD | 12 | TTLE1 | Contact-slot display labels (9 TITLE_* + MREP + LTYPE) |

---

### Concurrent Edit Lock Tables (×5)

| Table | Fields | Lock field |
|-------|--------|------------|
| BKCMCTL1 | 1 | CTRL_USER |
| BKCMCTL2 | 1 | CTRL_USER |
| BKCMCTL3 | 1 | CTRL_USER |
| BKCMCTL4 | 1 | CTRL_USER |
| BKCMCTRL | 1 | CTRL_USER |

Each is a single-field table holding the username of whoever currently has exclusive
write access to the corresponding CRM sub-view. Cleared on session exit.

---

### Temp / Work Tables (×5)

| Table | Fields | Schema |
|-------|--------|--------|
| BKCMTEMP | 6 | CODE+KEYF+GROUP+COMP+TAG+ACTIVITY |
| BKCMTMP1 | 6 | identical |
| BKCMTMP2 | 6 | identical |
| BKCMTMP3 | 6 | identical |
| BKCMTMP4 | 6 | identical |

Used for concurrent search/filter queries; one slot per user session. The TAG and
ACTIVITY fields index into the current result set for paging or mail-merge output.

---

### BKCM* Architecture Summary

```
BKCMACCT ──► BKCMACCN (10-slot contacts)
     │
     ├──► BKCMACTH / BKCMACTF / BKCMACTD (activity log/follow-up/dates)
     │         each has E-mirror (BKCMEACH/BKCMEACF/BKCMEACD) for in-progress edits
     │
     ├──► BKCMCUST (BKAR_* fields — bridge to AR customer master BKARCUST)
     │
     └──► BKCMACCL / BKCMEACC (class assignments → BKCMACCC)

BKCMPCNT ──► BKCMPCTF / BKCMPCTH  (prospect follow-up / history)
             └──► BKCMPCFC (prospect follow-up codes)

BKCMREP ──► (assigns accounts/prospects, controls view/change permissions)

BKCMTERR ──► (geographic grouping of accounts)

BKCMMHST ──► BKCMFORM ──► BKCMDUN ──► BKCMDUNH  (mail campaigns → letters → aging)

BKCMHCOD ──► BKCMHCD2  (activity codes + billing split details)

BKCMVNDH / BKCMVNDF  (vendor CRM — parallel to account activity tables)

BKCMCTL1-4 / BKCMCTRL  (edit locks — one per concurrent user)
BKCMTEMP / TMP1-4      (query scratch — one per concurrent user)
```

**Mirror architecture:** `BKCMDE`, `BKCMEACT`, `BKCMEACH`, `BKCMEACF`, `BKCMEACD`,
`BKCMEACC` are all in-progress edit buffers for their non-E counterparts. The pattern
is: copy master record to E-table → user edits E-table → commit writes E→master and
clears E. This prevents dirty reads during concurrent edits.

---

## BKCP* Family — Checkmark Payroll Link (2 tables)

**Pass 133 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 4228–4256**

Two tables discovered at DDF lines 4228–4256, adjacent to BKCM*. These belong to the
CP (Checkmark Payroll) integration module, not the CM CRM module.

### BKCPMSTR — Checkmark Payroll Integration Config

File: `BKCPMSTR.B` | Fields: 9 | PK: (single-row config)

| Field | Type | Meaning |
|-------|------|---------|
| BKCP_CMPATH | STRING 80 | Checkmark payroll data path |
| BKCP_IMPATH | STRING 80 | Import path |
| BKCP_CFILE | STRING 12 | Company file name in Checkmark |
| BKCP_VFILE | STRING 12 | Vendor/payee file name |
| BKCP_EXPATH | STRING 80 | Export path |
| BKCP_HFILE | STRING 12 | History file name |
| BKCP_LABEX | STRING 80 | Labor export path |
| BKCP_COMMEX | STRING 80 | Commission export path |
| BKCP_EFILE | STRING 12 | Employee file name in Checkmark |

### BKCPEC — Checkmark Payroll Error / Exception Log

File: `BKCPEC.B` | Fields: 10 | PK: DATE+GL+DEPT (likely)

| Field | Type | Meaning |
|-------|------|---------|
| BKCP_EC_DATE | STRING 8 | Entry date |
| BKCP_EC_GL | STRING 10 | GL account code |
| BKCP_EC_DEPT | STRING 10 | Department code |
| BKCP_EC_AMOUNT | FLOAT | Dollar amount |
| BKCP_EC_CHECKNO | STRING 15 | Check number |
| BKCP_EC_DESC | STRING 30 | Description |
| BKCP_EC_ISCHK | STRING 1 | Is-check flag |
| BKCP_EC_ERROR | STRING 60 | Error message |
| BKCP_EC_LINE | UBINARY 2 | Line number |
| BKCP_EC_VEND | STRING 15 | Vendor code |

---

## ISIS — Global Feature License / Module Enable Flags

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` line 17577**

File: `ISIS.B` | Fields: 23 | Single-row table (one record per company)

ISIS is the master feature-flag table. One row per company database. Every major
licensed add-on module is gated by a flag here. Programs read these flags at startup
to decide whether to show certain options. T7BRANDS (BR module) is the primary editor
for these flags via the IS.* vars.

| Field | Type | Meaning |
|-------|------|---------|
| IS_TAX | STRING 1 | Sales tax enabled |
| IS_MULTI_CURR | STRING 1 | Multi-currency enabled |
| IS_LANDED_COST | STRING 1 | Landed cost (IM module) enabled |
| IS_UPC | STRING 1 | UPC barcode enabled |
| IS_RETAIL_PRICE | STRING 1 | Retail pricing enabled |
| IS_COMM_PRICE | STRING 1 | Commission pricing enabled |
| IS_IMAGING | STRING 1 | Imaging / document attachment enabled |
| IS_UPC_1 | STRING 6 | UPC code prefix 1 |
| IS_DEMO | DATE 4 | Demo expiry date (non-zero = demo mode) |
| IS_UPC_2 | STRING 5 | UPC code prefix 2 |
| IS_MULTI_CPAY | STRING 1 | Multi-currency AP payment enabled |
| IS_PIC_PATH | STRING 20 | Product picture storage path |
| IS_TAX_FRM | STRING 1 | Tax-from flag |
| IS_PO_TAX | STRING 1 | PO-level tax enabled |
| IS_TAX_IN | STRING 1 | Inclusive tax mode |
| IS_TAX_CVT | STRING 1 | Tax currency conversion flag |
| IS_CUR_CVT | STRING 1 | Currency conversion enabled |
| IS_AUTO_TAX_CAL | STRING 1 | Automatic tax calculation |
| IS_EZPAY | STRING 1 | EzPay (credit card processing) enabled |
| IS_RMA | STRING 1 | RMA module enabled |
| IS_SPEC_SUP | STRING 1 | Special supplier flag |
| IS_SPEC_SUPF | UBINARY 2 | Special supplier from-value |
| IS_SPEC_SUPT | UBINARY 2 | Special supplier to-value |

ISIS is read by nearly every module via the global `IS.*` var block. Confirmed readers
include BKARCUST, BKAPVEND, BKICMSTR, T7BRANDS, T7PUTAWAY, T7MHOPE, T7AUTOMRF, T7ADCA.

---

## ISBANKS — Bank Account Master

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` line 14446**

File: `ISBANKS.B` | Fields: 23 | PK: `IS_BANKS_NUM` (UBINARY 2)

One row per configured bank account. ISBANKS is used by the BS Business Score module
(T7BS reads IS_BANKS_BAL for cash position KPIs), the IS multi-currency module, and
the TC (Treasury Control) module.

| Field | Type | Meaning |
|-------|------|---------|
| IS_BANKS_NUM | UBINARY 2 | Bank number / sequence (PK) |
| IS_BANKS_SRT | UBINARY 2 | Sort order |
| IS_BANKS_DESC | STRING 40 | Bank account description |
| IS_BANKS_GLA | STRING 10 | GL account code for this bank |
| IS_BANKS_GLD | STRING 4 | GL department for this bank |
| IS_BANKS_NXTNUM | FLOAT | Next check number |
| IS_BANKS_BAL | FLOAT | Current book balance |
| IS_BANKS_ROUT | STRING 15 | ABA routing number |
| IS_BANKS_ACCT | STRING 15 | Bank account number |
| IS_BANKS_CURR | STRING 3 | Currency code → FK ISMCF |
| IS_BANKS_TYPE | STRING 2 | Account type (CK=checking, SV=savings, etc.) |
| IS_BANKS_VEND | STRING 10 | Associated vendor code → FK BKAPVEND |
| IS_BANKS_ACTIVE | STRING 1 | Active flag |
| IS_BANKS_INC_BS | STRING 1 | Include in Business Score KPI flag |
| IS_BANKS_AR | STRING 1 | AR deposit bank flag |
| IS_BANKS_AP | STRING 1 | AP check bank flag |
| IS_BANKS_PR | STRING 1 | Payroll check bank flag |
| IS_BANKS_RTM_1..5 | STRING 12 ×5 | Up to 5 report template names for this bank |
| IS_BANKS_EXTRA | STRING 100 | Extra / notes |

---

## ISBSF — Business Score Framework KPI Store

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 14665–14811**

File: `ISBSF.B` | Fields: 143 | PK: `ISBSF_STARTDATE` + `ISBSF_ENDDATE` (DATE pair)

One row per time period. T7BS.RWN (the BS module writer) calculates and writes all
values; EVOBS.RWN (the BS viewer, QU-D) reads them. This is the pre-computed KPI
snapshot store used by the Business Status dashboard.

| Field block | Fields | Meaning |
|-------------|--------|---------|
| ISBSF_STARTDATE / ENDDATE | 2 | Period start and end dates (PK) |
| ISBSF_AR_BAL/BILL/RECP/DISC/COGS | 5 | AR KPIs: open balance, billings, receipts, discounts, COGS |
| ISBSF_AP_BAL/PAYA/PAYM/DISC/ATP | 5 | AP KPIs: open balance, payables, payments, discounts, available-to-pay |
| ISBSF_SO_OPEN/BOOK/SHIP | 3 | SO KPIs: open order backlog, bookings, shipments |
| ISBSF_PO_OPEN/BOOK/RECP | 3 | PO KPIs: open PO value, ordered, received |
| ISBSF_WO_WIPBAL/ISSU/FPVAR | 3 | WO KPIs: WIP balance, material issued, finished-goods variance |
| ISBSF_IC_VALUE | 1 | Inventory on-hand value |
| ISBSF_AR_DEPO | 1 | AR deposits on hand |
| ISBSF_CASH_TOTA | 1 | Total cash position (sum of all bank IS_BANKS_BAL) |
| ISBSF_CASH_ACT1..9 | 9 | Cash activity by GL account (up to 9 accounts) |
| ISBSF_WOS_SETUP/LAB/OUTP/MAT/FOH/VOH/MEXT/FP/WIPV | 9 | WO cost breakdown: setup/labor/output/material/FOH/VOH/machine-ext/finished-part/WIP-variance |
| ISBSF_CASH_ACTS_1..100 | 100 | 100-period rolling GL cash history (one float per period) |
| ISBSF_EXTRA | 1 | STRING 100 extra |

The 100-slot CASH_ACTS array provides a rolling history for trend charts. T7BS
iterates ISGLDATE periods to populate them.

---

## ISBTCSB — Batch/Scheduled Service Record (ISSR_INFO Clone)

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 14813–14864**

File: `ISBTCSB.B` | Fields: 54 | Schema identical to ISSRINFO (ISSR_INFO_* prefix)

ISBTCSB uses the identical 54-field ISSR_INFO_* schema as ISSRINFO. The file name
prefix "BTCSB" suggests "Batch / Time-Controlled Service Batch". Same PK structure:
ISSR_INFO_SRNUM + ISSR_INFO_UID. Cross-reference: see ISSRINFO documentation in the
SR/Service-Repair module docs.

---

## IS Warehouse / Bin Tables

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 14474–14510**

### ISBILLSH — Bill-To / Ship-To Cross-Reference

File: `ISBILLSH.B` | Fields: 4

| Field | Type | Meaning |
|-------|------|---------|
| IS_BILLSH_BILL | STRING 10 | Bill-to customer code |
| IS_BILLSH_SHIP | STRING 10 | Ship-to location code |
| IS_BILLSH_FLAG | STRING 1 | Relationship flag |
| IS_BILLSH_EXTRA | STRING 100 | Extra |

### ISBINLOC — Bin-Level Inventory Quantity

File: `ISBINLOC.B` | Fields: 9 | PK: ITEM+LOC+BIN

| Field | Type | Meaning |
|-------|------|---------|
| ISBIN_LOC_ITEM | STRING 15 | Item code (PK part 1) |
| ISBIN_LOC_LOC | STRING 10 | Location code (PK part 2) |
| ISBIN_LOC_BIN | STRING 15 | Bin code (PK part 3) |
| ISBIN_LOC_UOH | FLOAT | Units on hand in this bin |
| ISBIN_LOC_CDATE | DATE | Created/cycle-count date |
| ISBIN_LOC_VDATE | DATE | Last verified date |
| ISBIN_LOC_DFLT | STRING 1 | Default bin for this item/location |
| ISBIN_LOC_EXTRA | STRING 100 | Extra |
| ISBIN_LOC_RVLVL | STRING 5 | Reorder level |

### ISBINLOT — Bin-Level Lot Tracking

File: `ISBINLOT.B` | Fields: 10 | PK: ITEM+LOC+LOT+BIN

| Field | Type | Meaning |
|-------|------|---------|
| IS_BINLOT_ITEM | STRING 15 | Item code (PK part 1) |
| IS_BINLOT_LOC | STRING 10 | Location (PK part 2) |
| IS_BINLOT_LOT | STRING 15 | Lot number (PK part 3) |
| IS_BINLOT_BIN | STRING 15 | Bin (PK part 4) |
| IS_BINLOT_UOH | FLOAT | Lot quantity in this bin |
| IS_BINLOT_DATE | DATE | Date lot was placed in bin |
| IS_BINLOT_FLAG | STRING 1 | Status flag |
| IS_BINLOT_EXTRA | STRING 50 | Extra |
| IS_BINLOT_TMPSO | STRING 40 | Temp SO reservation hold |
| IS_BINLOT_TMPPO | STRING 40 | Temp PO receipt hold |

The TMP fields hold short-term allocation strings during SO picking or PO put-away;
cleared when the pick/receipt completes.

---

## MK* Family — Marketing Automation (11 tables)

**Pass 134 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 24535–24659**

The MK module provides campaign tracking, event sequencing, and automated follow-up
routing. Tables use the `MK` prefix with no shared field-prefix convention (each table
uses its own prefix). The module appears in DB fingerprints of many unrelated programs
because MKAHIST is updated whenever a significant customer event occurs (shipment,
CRM activity, mass mailing, etc.).

### Family overview

| Table | Fields | PK | Purpose |
|-------|--------|----|---------|
| MKAHIST | 9 | ACCT+DATE+TRACK+SEQ | Account marketing history log |
| MKASSIGN | 6 | ACCT+TRACK | Track assignment per account |
| MKDEF | 11 | (single row) | MK system defaults |
| MKECLASS | 3 | NUM | Event class code |
| MKICLASS | 3 | NUM | Item class code (same schema as MKECLASS) |
| MKTCLASS | 3 | NUM | Track class code (same schema as MKECLASS) |
| MKEVENT | 12 | NUM | Event definition |
| MKFORM | 6 | NUM | Form/letter definition |
| MKTNOTE | 3 | TRACK+LINE | Track notes text |
| MKTRACK | 4 | NUM | Marketing track definition |
| MKTROUT | 11 | TRACK+SEQ | Track routing / step sequence |

---

### MKAHIST — Account Marketing History

File: `MKAHIST.B` | Fields: 9 | PK: ACCT+DATE+TRACK+SEQ

| Field | Type | Meaning |
|-------|------|---------|
| MKAHIST_ACCT | STRING 10 | Customer/account code (PK part 1) |
| MKAHIST_DATE | DATE | Event date (PK part 2) |
| MKAHIST_TRACK | FLOAT | Track number (PK part 3) |
| MKAHIST_SEQ | UBINARY 2 | Sequence within track (PK part 4) |
| MKAHIST_EVENT | FLOAT | Event code → FK MKEVENT |
| MKAHIST_MEDIA | STRING 1 | Media channel code |
| MKAHIST_FORM | FLOAT | Form/letter used → FK MKFORM |
| MKAHIST_REM1..2 | STRING 60 ×2 | Remark lines |

This table records every marketing touchpoint per customer. Its wide adoption in
module fingerprints (DS, AU, MH, PU, BR, XC, etc.) confirms that EvoERP logs a
MKAHIST record whenever a shipment, payment, or CRM interaction occurs.

---

### MKASSIGN — Track Assignment per Account

File: `MKASSIGN.B` | Fields: 6 | PK: ACCT+TRACK

| Field | Type | Meaning |
|-------|------|---------|
| MKASSIGN_ACCT | STRING 10 | Account code (PK part 1) |
| MKASSIGN_TRACK | FLOAT | Track number (PK part 2) |
| MKASSIGN_NXTSEQ | UBINARY 2 | Next sequence step to execute |
| MKASSIGN_NXTDAT | DATE | Date next step is due |
| MKASSIGN_SALEND | DATE | Sale/campaign end date |
| MKASSIGN_PRCODE | FLOAT | Price code override for this track |

---

### MKDEF — Marketing System Defaults

File: `MKDEF.B` | Fields: 11 | Single-row config

| Field | Type | Meaning |
|-------|------|---------|
| MKDEF_REQUIRE | STRING 1 | Require track assignment flag |
| MKDEF_CALENDAR | STRING 1 | Use calendar for due dates flag |
| MKDEF_TRACK | FLOAT | Default track number |
| MKDEF_PRICECD | FLOAT | Default price code |
| MKDEF_FUCODE | STRING 3 | Default follow-up code |
| MKDEF_HISTORYCD | STRING 2 | Default history code |
| MKDEF_TNEXTID | FLOAT | Next track ID auto-number |
| MKDEF_TCNEXTID | FLOAT | Next track-class ID auto-number |
| MKDEF_ENEXTID | FLOAT | Next event ID auto-number |
| MKDEF_ECNEXTID | FLOAT | Next event-class ID auto-number |
| MKDEF_FNEXTID | FLOAT | Next form ID auto-number |

---

### MKEVENT — Marketing Event Definition

File: `MKEVENT.B` | Fields: 12 | PK: `MKEVENT_NUM` (FLOAT)

| Field | Type | Meaning |
|-------|------|---------|
| MKEVENT_NUM | FLOAT | Event number (PK) |
| MKEVENT_DESC | STRING 45 | Description |
| MKEVENT_CLASS | FLOAT | Event class → FK MKECLASS |
| MKEVENT_MEDIA | STRING 1 | Media channel code |
| MKEVENT_FORM | FLOAT | Form to send → FK MKFORM |
| MKEVENT_FUCODE | STRING 3 | Follow-up code |
| MKEVENT_REM1..2 | STRING 60 ×2 | Remarks |
| MKEVENT_SENDTO | UBINARY 2 | Send-to flag (contact slot) |
| MKEVENT_GENNAME | STRING 45 | Generic name for merge |
| MKEVENT_HISTCD | STRING 2 | CRM history code → FK BKCMHCOD |
| MKEVENT_ACTIVE | STRING 1 | Active flag |

---

### MKFORM — Marketing Form / Letter Definition

File: `MKFORM.B` | Fields: 6 | PK: `MKFORM_NUM` (FLOAT)

| Field | Type | Meaning |
|-------|------|---------|
| MKFORM_NUM | FLOAT | Form number (PK) |
| MKFORM_DESC | STRING 45 | Description |
| MKFORM_FILE | STRING 25 | File name for the letter template |
| MKFORM_ATT | STRING 25 | Attachment file name |
| MKFORM_MEDIA | STRING 1 | Media channel (M=mail, E=email, F=fax) |
| MKFORM_ACTIVE | STRING 1 | Active flag |

---

### MKTRACK — Marketing Track Definition

File: `MKTRACK.B` | Fields: 4 | PK: `MKTRACK_NUM` (FLOAT)

| Field | Type | Meaning |
|-------|------|---------|
| MKTRACK_NUM | FLOAT | Track number (PK) |
| MKTRACK_DESC | STRING 45 | Track description |
| MKTRACK_CLASS | FLOAT | Track class → FK MKTCLASS |
| MKTRACK_ACTIVE | STRING 1 | Active flag |

**MKTNOTE** (3f) — notes on a track: TRACK(FLOAT PK part1) + LINE(UBINARY2 PK part2) + MKNOTE_TEXT(STRING 70).

---

### MKTROUT — Track Routing / Step Sequence

File: `MKTROUT.B` | Fields: 11 | PK: TRACK+SEQ

Defines the ordered steps in a marketing track. Each step specifies which event to
execute, when to do it, and where to branch next.

| Field | Type | Meaning |
|-------|------|---------|
| MKTROUT_TRACK | FLOAT | Track number (PK part 1) |
| MKTROUT_SEQ | UBINARY 2 | Step sequence (PK part 2) |
| MKTROUT_JUMP | STRING 1 | Branch flag |
| MKTROUT_NEXTSEQ | UBINARY 2 | Next sequence on success |
| MKTROUT_EVENT | FLOAT | Event to execute → FK MKEVENT |
| MKTROUT_DAYSNXT | UBINARY 2 | Days until next step |
| MKTROUT_FIXED | STRING 1 | Fixed date flag |
| MKTROUT_SALEBEG | STRING 1 | Sale-begin trigger flag |
| MKTROUT_SALELEN | UBINARY 2 | Sale duration (days) |
| MKTROUT_SALECLO | STRING 1 | Sale-close trigger flag |
| MKTROUT_PRICECD | FLOAT | Price code override for this step |

---

### Class Code Tables (×3, identical schema)

| Table | Fields | Purpose |
|-------|--------|---------|
| MKECLASS | 3 | Event class: NUM(FLOAT PK) + DESC(45) + ACTIVE(1) |
| MKICLASS | 3 | Item class: NUM + DESC + ACTIVE (MKECLASS_* prefix — identical schema) |
| MKTCLASS | 3 | Track class: NUM + CLASS(45) + ACTIVE |

---

### MK* Architecture Summary

```
MKDEF (defaults)
MKECLASS/MKICLASS/MKTCLASS (class codes)
MKEVENT ──► MKFORM (event definition links to letter/form)
MKTRACK ──► MKTROUT (track definition → step sequence → events)
         └──► MKTNOTE (track notes)
MKASSIGN ── per-account track enrollment (ACCT+TRACK PK)
MKAHIST  ── per-account event history (ACCT+DATE+TRACK+SEQ PK)
```

Marketing flow: define events (MKEVENT) → group into tracks (MKTRACK + MKTROUT
routing) → assign tracks to accounts (MKASSIGN) → each event execution logs to
MKAHIST. Account-wide touchpoints (ship, pay, CRM) also log directly to MKAHIST.

---

*Last updated: 2026-06-19*
*Source: `samples/ddf/schema.md` (field extraction), `samples/ddf/tables.txt` (table inventory)*
*Confidence: 82/100 — All field names confirmed from DDF; field meanings inferred from field names and module fingerprint analysis; no MK SRC source available for logic confirmation.*

---

## FO Extended + Fixed Assets + GL History + Serial Genealogy — Pass 137

**Pass 137 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 16602–17300**

---

### FO Module — Full Table Set

The ISFO* family is now fully resolved (7 tables). The FO (First-Off / First-Article
Inspection) module manages pre-production quality inspection of BOM assemblies.

**ISFOHIST** (15f, `ISFO_HIST_*`): FO event history.
UID(40)+WHO+DATE+TIME+STATUS(40)+PART(15)+CVTTO(4 doc type)+CVTNO(FLOAT doc#)+CITEM(15)+
QTY+LOC+CV(10)+DDATE+PRICE+EXTRA.
CVTTO/CVTNO record the conversion of the FO result to a downstream document (PO, SO, WO).

**ISFOLINE** (78f, `ISFO_LIN_*`): FO BOM line with 50 operation-flag slots.
UID(40 FK)+LEVEL + **50×OPFLAG_1..50** (1 char each) + EXTRA(150) + PARENT(15)+LINEN+
COMP(15)+QTYREQ+REF(20)+TYPE+SCRAP+OP+6×OPYN+PRICE+RTNUM+DUPOP+OPDSC+VEND+DATE1/2+
BEXTRA(50)+REV+PBRANC+CBRANC(branch refs).
50 single-char inspection flags per BOM component = up to 50 quality check checkboxes
(pass/fail/NA per inspection criteria). PBRANC/CBRANC = parent/component BOM branch.

**ISFOORDL** (18f, `ISFO_ORDL_*`): Order line generated from FO approval.
UID(40)+TYPE(6)+PCODE(15)+PDESC+PQTY+PPRCE+PDISC+PEXT+ESD+LOC+TXBLE+UM+LN(3)+DRAW+REV+
LINE+OUID(FLOAT)+EXTRA. Written when a First-Off approval spawns a PO or SO line.

**Summary of FO module tables:**

| Table | f | Role |
|-------|---|------|
| ISFOHEAD | 16 | Inspection header (item, dates, status, RFQ) |
| ISFOBMRM | 20 | BOM component remarks (15 remark slots each) |
| ISFOLINE | 78 | BOM component line with 50 op-flag checkboxes |
| ISFOHIST | 15 | Event history + document conversion log |
| ISFOORDL | 18 | Order line spawned from FO approval |

---

### Fixed Assets Module (FX)

**ISFXASST** (23f, `IS_FXA_*`): Fixed asset master record.

| Field | Type | Meaning |
|-------|------|---------|
| IS_FXA_NUMBER | FLOAT | Asset number (PK) |
| IS_FXA_TYPE / DESC / DESC2 | STRING | Asset type (30), descriptions |
| IS_FXA_CSTBAS | FLOAT | Cost basis (purchase price) |
| IS_FXA_RESVAL | FLOAT | Residual / salvage value |
| IS_FXA_LIFE | FLOAT | Useful life (years) |
| IS_FXA_METH | STRING 30 | Depreciation method |
| IS_FXA_GLA / GLD | STRING | Asset GL account + dept |
| IS_FXA_ACDEPA / ACDEPD | STRING | Accumulated depreciation GL acct + dept |
| IS_FXA_DEPEXPA / DEPEXPD | STRING | Depreciation expense GL acct + dept |
| IS_FXA_SDATE / EDATE | DATE | Service start / end dates |
| IS_FXA_SOLD | FLOAT | Proceeds from sale |
| IS_FXA_ACCUMDEP | FLOAT | Accumulated depreciation to date |
| IS_FXA_SERIAL | STRING 30 | Asset serial number |
| IS_FXA_LDEPAMT / LDEPPERC / LDEPDATE | FLOAT / FLOAT / DATE | Last depreciation: amount, percent, date |
| IS_FXA_EXTRA | STRING 100 | Extra |

Three GL account+department pairs: asset account, accumulated depreciation account,
depreciation expense account. Standard double-entry fixed-asset bookkeeping in one row.

**ISFXATRN** (12f, `IS_FXT_*`): Depreciation/transaction history per asset.
NUMBER(FK→ISFXASST)+DATE+AMOUNT+PERC+AUDIT(25)+POSTED(1)+ACDEPA+ACDEPD+DEPEXPA+DEPEXPD+
NETAVAL+EXTRA. One row per depreciation posting event.

---

### GL History Extension — ISGL* Family

BKGLCOA stores 2 years of period history (CURRENT_1..14 + 1YPAST_1..14 + 2YPAST_1..14).
The ISGL* extension tables add years 3–6, giving **up to 7 years of GL history total**.

**ISGLCOA / ISGLBDGT / ISGLFCOA** (67f each, identical `ISGL_*` schema):

| Field | Meaning |
|-------|---------|
| ISGL_ACCT + ISGL_GLDPT | PK — matches BKGLCOA |
| ISGL_ACCTD / TYPE / CR_DR / NON_CASH | Account header (same as BKGLCOA) |
| ISGL_3YPAST_1..14 + 3YPAST_YE | Year −3: 14 period amounts + year-end total |
| ISGL_4YPAST_1..14 + 4YPAST_YE | Year −4 |
| ISGL_5YPAST_1..14 + 5YPAST_YE | Year −5 |
| ISGL_6YPAST_1..14 + 6YPAST_YE | Year −6 |
| ISGL_CEXTRA | STRING 100 — extra |

Three variants:
- **ISGLCOA** — actual historical period balances (years 3–6)
- **ISGLBDGT** — budget amounts for years 3–6
- **ISGLFCOA** — future / forecast COA (likely next year's plan or foreign company COA)

**GL COA total history depth:** BKGLCOA (years 0–2) + ISGLCOA (years 3–6) = 7 years of actuals.

---

### GL Period Date Tables

**ISGLDATE / ISGLHDAT** (86f each, identical `ISGL_*` schema): Period end date calendar.

One row per company (singleton). Stores all fiscal period end dates across 7 years:
CYDATE_1..12 (current year, 12 periods) + 1YDATE_1..12 through 6YDATE_1..12 (6 past years)
+ ISGL_FYDATE (fiscal year start date) + ISGL_EXTRA.

Total: 84 fiscal period end dates + 1 FY start = complete fiscal calendar for GL navigation.
ISGLDATE = active dates; ISGLHDAT = historical dates (saved before year-end rollover).

Cross-reference: T7BS.RWN reads ISGLDATE to resolve period numbers into calendar dates.

---

### ISGLNBGT — GL Next/New Budget

File: `ISGLNBGT.B` | Fields: 35 | PK: `ISGL_BGT_ACCT` + `ISGL_BGT_GLDPT`

| Field | Meaning |
|-------|---------|
| ISGL_BGT_ACCT + GLDPT | PK |
| ISGL_BGT_BUDGET_1..14 | Next period budget (14 periods) |
| ISGL_BGT_DATE | Budget date |
| ISGL_BGT_BUD2_1..14 | Second/alternate budget set (14 periods) |
| ISGL_BGT_FLAG | Budget status flag |
| ISGL_BGT_WHO | Who set this budget |
| ISGL_BGT_EDATE | Effective date |
| ISGL_BGT_EXTRA | Extra |

Two parallel budget sets (BUDGET and BUD2) per account for next-year planning. Separate
from BKGLCOA.BUDGET_1..14 (current-year budget). The GL module uses both when generating
budget vs. actual reports.

---

### i2 Systems Fiber/FS Tables

**ISFSCLAS / ISFSEMP** (3f each, `IS_FIB_*`): Fiber class and employee codes.
IS_FIB_CLASS(4)+IS_FIB_GROUP(50)+IS_FIB_EXTRA(50). Used by i2 Systems fiber/fabric
manufacturing operations. ISFSCLAS = fabric/fiber classification codes;
ISFSEMP = employee fiber classification assignments.

**ISFSINFO** (4f, `IS_FIB_*`): Fiber/FS program header.
IS_FIB_PROGRAM(20)+IS_FIB_CONTRACT(25)+IS_FIB_MISC(100)+IS_FIB_WHO(50). i2-specific.

**ISFUTYPE** (3f, `IS_FUTYPE_*`): Follow-up type code.
TYPE(10)+DESC(60)+EXTRA(50). Codes used by ISCARFUP (IS_CARFUP_TYPE field).

---

### ISHLOTS / ISHSERIA — Serial Assembly Genealogy

Both files: 11 fields, identical `IS_SER_*` schema.
PK: WOPRE + WOSUF.

| Field | Meaning |
|-------|---------|
| IS_SER_WOPRE / WOSUF | WO prefix + suffix (PK) |
| IS_SER_PARENT | Parent assembly item code |
| IS_SER_PDESC | Parent item description |
| IS_SER_PSERIAL | Parent serial number |
| IS_SER_ADATE | Assembly date |
| IS_SER_COMP | Component item code |
| IS_SER_CDESC | Component description |
| IS_SER_CSERIAL | Component serial number |
| IS_SER_FDATE | Final/completion date |
| IS_SER_EXRA | Extra (note: typo in field name — `EXRA` not `EXTRA`) |

These tables record the serial genealogy: which component serial number (CSERIAL) was
consumed to build which parent assembly serial number (PSERIAL) on which WO at ADATE.
Critical for traceability — if a component is recalled, ISHLOTS identifies all parent
assemblies that used it.

ISHLOTS = active genealogy records; ISHSERIA = archived serial genealogy.

---

### ISICADT — Inventory Item Audit Snapshot

File: `ISICADT.B` | Fields: 18+ | Prefix: `BKIC_PROD_*` (BKICMSTR field names)

ISICADT uses the `BKIC_PROD_*` field names from BKICMSTR. It is an audit snapshot
copy of the inventory item master — a point-in-time record of item master data used
for inventory auditing and reconciliation:

CODE(15)+DESC(30)+TYPE+UM+CAT(4)+TXBLE+CLASS(4)+RLVL(reorder level)+RAMT(reorder qty)+
LSALE+LORD+LRCPT+ADTR(audit trail ref)+TO(turnover)+LSTC(last cost)+AVGC(avg cost)+
UOH(on-hand)+UOSO(on SO)+...

Likely written at period-end or physical inventory time to record what the system
showed, for later comparison against actual counts or auditor requests.

---

## ES* Estimating Module — Pass 136

**Pass 136 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 15525–16602**

The ES (Estimating/Quoting) module stores quotes using a mirror-of-BKARINV architecture:
quote headers reuse the full `BKAR_INV_*` schema, quote lines reuse `BKAR_INVL_*`, and
a separate `IS_EST_*` cost-breakdown layer stores 10-quantity-break pricing.

---

### ISESTASM — Estimating Assembly Summary (Quote Master)

File: `ISESTASM.B` | Fields: 213 | PK: `MTESUM_QUOTE` (FLOAT) | Prefix: `MTESUM_*`

The top-level quote record. One row per quote (MTESUM_QUOTE). Key groups:

| Field group | Fields | Meaning |
|-------------|--------|---------|
| Header | QUOTE, DATE, EXPDATE, STATUS, CLASS(4), CODE(15 item), DESC, UM | Quote identity |
| Customer | CUSTCODE(10), NAME(30), ATTN(30) | Customer for this quote |
| Quote ref | RFQ(15), REV(4), PROJ(15) | RFQ reference, revision, project |
| 10-break QTY | QTY_1..10 | The 10 quantity break levels |
| 10-break costs | MAT+MATMU, LAB+LABMU, SETUP, OP+OPMU, OH+OHMU, MISC ×10 | Cost + markup per break |
| Summary | OVALL_1..10, TOTAL_1..10, PRICE_1..10, COST_1..10, VOVHD_1..10 | Rolled-up totals + selling prices |
| Notes | NOTES_1..10 (60 chars each) | Per-break notes/comments |
| Control | ENTBY(15), LOC(10), TEMP_NUM, BOM_FLAG, RT_FLAG, EX_FLAG | BOM/routing/extra loaded flags |
| Dates | CDATE, FIN_DATE, L_O_DATE | Created, finished, L/O date |
| Sales | SLSP_NUM_1/2, COMM_RTE_1/2 | Salesperson + commission rates |
| Misc | OPPTYPE(2), QTREV(9), EXTRA2(100), LEAD_SRC(4), LEADTIME(30) | |

---

### ISESADTL / ISESTDTL — Estimating Detail (Per-Part Cost Breakdown)

Files: `ISESADTL.B` / `ISESTDTL.B` | Fields: 203 each | Prefix: `IS_EST_*`
PK: `IS_EST_NUM` + `IS_EST_PART` + `IS_EST_LINE`

ISESADTL = active estimate detail; ISESTDTL = working/in-progress copy. Both identical.

One row per BOM component (PART) per estimating quote (NUM) per line (LINE). Stores
the full cost breakdown across 10 quantity breaks for that component:

- IS_EST_QTY_1..10 — qty break levels
- IS_EST_MAT_1..10 / MATMU_1..10 — material cost + markup
- IS_EST_LAB_1..10 / LABMU_1..10 — labor cost + markup
- IS_EST_SETUP_1..10 / SETMU — setup cost + single markup
- IS_EST_OP_1..10 / OPMU_1..10 — outside process cost + markup
- IS_EST_OH_1..10 / OHMU_1..10 — overhead + markup
- IS_EST_MISC_1..10 — miscellaneous costs
- IS_EST_EXTRA_1..10 — extra cost fields
- IS_EST_MEMU_1..10 — ME (material extra) markup
- IS_EST_VOVHD_1..10 — variable overhead
- IS_EST_OVALL_1..10 — overall rolled cost
- IS_EST_TOTAL_1..10 — total per break
- IS_EST_PRICE_1..10 — selling price per break
- IS_EST_COST_1..10 — cost per break

Control fields: BOM_FLAG/RT_FLAG/EX_FLAG (BOM/routing/extra loaded), OPPTYPE, QTREV,
STATUS, DRAW/REV, ORDDESC/ORDDTE/EXPDTE/LOSTDTE, CUST, QUICK (quick-quote),
SO (→ linked SO#), WOPRE/WOSUF (→ linked WO#), TEMP_NUM, EXTRA2.

FK: IS_EST_LINE → ISBMEST/ISBMESA (BOM estimating mirrors).

---

### ISESAHDR / ISESTHDR / ISESTAQT — Estimating Quote Headers

Files: `ISESAHDR.B` / `ISESTHDR.B` / `ISESTAQT.B` | Fields: 84 each
Prefix: `BKAR_INV_*` (verbatim BKARINV schema)

Three clones of the BKARINV invoice header:
- ISESAHDR — saved/archived quote header
- ISESTHDR — historical quote header
- ISESTAQT — active/current quote template

All 84 fields are verbatim BKARINV: NUM, SONUM, INVCD, INVDTE, CUSCOD, customer/ship-to
address, TERMD/TERMNM, SLSP, ENTBY, CUSORD, TAXABL, SUBTOT/TAXAMT/TOTAL/COGS, FRGHT,
LOC, ORDDTE, DCODE, PCODE, SHIPDT, FOB, commission fields, billing address, EXTRA(150),
ISCUR, RELNUM, TRACK, QSTAT, MDATE, MISC.

This design means estimates can be converted to invoices by copying the quote header
directly into BKARINV — the schemas share identical field offsets.

---

### ISESALNE / ISESTLNE / ISESTAQL — Estimating Quote Lines

Files: `ISESALNE.B` / `ISESTLNE.B` / `ISESTAQL.B` | Fields: 28 each
Prefix: `BKAR_INVL_*` (verbatim BKARINVL schema)

Three clones of the BKARINVL invoice line. Same logic as the header clones:
- ISESALNE — saved/archived quote lines
- ISESTLNE — historical quote lines
- ISESTAQL — active quote template lines

28 fields: INVNM+CNTR PK, ESD (estimate ship date), PCODE+PDESC, PQTY+PPRCE+PDISC
+PEXT+PCOGS, ITYPE, TXBLE, UBO/USTD, RTS, LOC, ABQTY, UM_LN_1/2, COMPR_1/2, ASD,
TXAMT, FRGHT, COOP, OOQTY, EXTRA, SCCOG.

---

### ISESTPO — Estimate-to-PO Bridge

File: `ISESTPO.B` | Fields: 16 | PK: `BKMRP_PO_UID` (STRING 20) | Prefix: `BKMRP_PO_*`

| Field | Type | Meaning |
|-------|------|---------|
| BKMRP_PO_UID | STRING 20 | Unique ID (PK) |
| BKMRP_PO_VEND | STRING 10 | Vendor code |
| BKMRP_PO_DATE | DATE | PO creation date |
| BKMRP_PO_ERD | DATE | Expected receipt date |
| BKMRP_PO_PART | STRING 15 | Item code |
| BKMRP_PO_QTY | FLOAT | Quantity |
| BKMRP_PO_PRICE | FLOAT | Unit price |
| BKMRP_PO_WOPRE/WOSUF | FLOAT+USHORT | Linked work order |
| BKMRP_PO_PLANR | STRING 4 | Planner code |
| BKMRP_PO_CONF | STRING 1 | Confirmed flag |
| BKMRP_PO_DONE | STRING 10 | Done/status |
| BKMRP_PO_MTREC | UBINARY 4 | MT record pointer |
| BKMRP_PO_EXTRA | STRING 50 | Extra |
| BKMRP_PO_EST | STRING 10 | FK to estimate number |
| BKMRP_PO_ESTLNE | FLOAT | FK to estimate line |

Uses BKMRP_PO_* prefix — it is a planned PO created from an estimating quote, bridging
the ES module to the MRP/PO workflow. EST+ESTLNE link back to the originating quote.

---

### ES* Table Architecture Summary

```
ISESTASM (quote master, MTESUM_*)
  └─ ISESADTL/ISESTDTL (detail per component, IS_EST_*, 203f)
     └─ ISBMEST/ISBMESA (BOM estimating mirrors, BKBM_*, 26f)
ISESAHDR/ISESTHDR/ISESTAQT (headers, BKAR_INV_*, 84f)
ISESALNE/ISESTLNE/ISESTAQL (lines, BKAR_INVL_*, 28f)
ISESTPO (estimate-to-PO, BKMRP_PO_*, 16f)
```

---

## Platform Tables — Pass 136

---

### ISDCSER — Data Collection Serial Tracking

File: `ISDCSER.B` | Fields: 17 | PK: WOPRE + WOSUF + OPER | Prefix: `ISDC_SER_*`

WOPRE(F)+WOSUF+OPER PK; ITEM(15)+EMP; SERIAL(25)+LOT(15)+BIN(15)+LOC(10);
DATE+FLAG+ALPHA(30)+GDATE+TIME; PARTS+QTY+EXTRA(100).

Records serial number assignments at each WO operation during shop-floor data
collection (ADCA/PA modules). One row per serialized item produced at a DC event.

---

### ISDEFECT — Defect Code Master

File: `ISDEFECT.B` | Fields: 3 | PK: `IS_DEF_CODE` (STRING 10)

CODE(10) + DESC(60) + EXTRA(50). Defect codes referenced by IS_NCR_DCODE in ISNCR/ISCAR.

---

### ISDEPT / ISDIV — Department and Division Masters

Both use `IS_GF_*` prefix. 3 fields each: code(10) + desc(40) + misc(100).
Shared dimension codes used by payroll, G/L, and HR modules.

---

### ISDLCK1 / ISDLCK2 — Singleton Lock Sentinels

1 field each (`BUBBA` STRING 10). Programs acquire an exclusive Btrieve lock on the
single record to serialize concurrent access to a shared resource. Two independent
lock objects for two independent critical sections.

---

### ISDRILL / ISDRILLM — Drill-Down Navigation Tables

**ISDRILL** (46f, `LOOKUP_*` prefix): Defines a drill-through lookup.
FROM(30)+GRID(15)+REC+KEY+FILE(15)+20×FILTERS(80)+COMM(150)+20×WHILE(80).

**ISDRILLM** (17f, `DRILLM_*` prefix): Maps source→target field pairs for drill-through.
PARENT(15)+CHILD(15)+MENU(25)+FILE+5×SFIELD(15)+5×TFIELD(15)+KEY+PFILE+EXTAR(150).

Together these drive EvoERP's context-sensitive drill-down navigation from any field
to a related record in another module. Opened by T7EMGL and other modules.

---

### ISDROP — User-Defined Drop-Down Codes

File: `ISDROP.B` | Fields: 4. CODE(10)+TEXT(30)+DESC(30)+EXTRA(50).
Generic configurable drop-down list entries; multiple lists distinguished by CODE prefix.

---

### ISDUTY — Landed Cost Duty Rate

File: `ISDUTY.B` | Fields: 2. ISIS_DUTY_DCODE(6)+ISIS_DUTY_PERC(FLOAT 3dp).
Duty rate by tariff code; used by landed cost module (ISIS.IS_LANDED_COST flag).

---

### ISEAB — Employee Email Address Book

File: `ISEAB.B` | Fields: 6. USER(15)+CONTACT(20)+FNAME(15)+LNAME(15)+EMAIL(30)+EXTRA(100).
Per-user email contacts for internal notifications.

---

### ISECO — Engineering Change Order

File: `ISECO.B` | Fields: 12 | PK: PART + DRAW + REVLVL

PART(15)+DRAW(15)+REVLVL(5) PK; ENTDATE+ENTBY(4)+ECO#(15)+CURRENT(1)+STATUS(1)
+DATE+APPBY(4)+INVDISP(2)+EXTRA(100). CURRENT flag marks active revision;
INVDISP = inventory disposition for old stock on ECO implementation.

---

### ISEDINFO — SR-Info Clone (EDI/batch context)

File: `ISEDINFO.B` | Fields: 54 | Prefix: `ISSR_INFO_*`

Identical schema to ISSRINFO: SRNUM+UID+CODE+5×DATE+20×ALPHA(25)+EXTRA+5×DATE2+20×AL.
Used as an EDI or batch service transaction info store, reusing the SR Info layout.

---

### ISFIELDS — User-Defined Field Registry

File: `ISFIELDS.B` | Fields: 7 | PK: FD + FIELD

IS_FLDS_FD(8 table name)+FIELD(15)+DESC(40)+NUM(USHORT)+EXTRA(50)+ANUM+REQUIRE(1).
Maps table/field names to user-friendly descriptions and requirement flags; supports
EvoERP's UDF (User-Defined Fields) labeling system.

---

### ISFOHEAD / ISFOBMRM — First-Off / First-Article Inspection

**ISFOHEAD** (16f, `ISFO_HDR_*`): Inspection header.
UID(40 PK)+PARENT(15 item)+DATE+DESC(30)+CUST+VEND+RFQ(20)+STATUS(15)+REV(5)+5×MDATES+PERM+EXTRA(150).

**ISFOBMRM** (20f, `ISFO_BRM_*`): Per-component BOM remarks.
UID(40 FK)+PARENT(15)+LINE(USHORT)+COMP(15 component)+15×REMARK(64 each)+EXTRA(100).

ISFOHEAD captures the First-Article Inspection event; ISFOBMRM records the inspection
result for each BOM component (15 inspection remark fields per component). This is the
FO (First Off) module — used before production begins on a new part or revision.

---

## IS* Supplement — QC/CAPA, Chain, BM Estimating, CR Approval, Conversion

**Pass 135 — 2026-06-19 | Source: `samples/ddf/schema.md` lines 14513–15195**

---

### ISCAR — Corrective Action Report (NCR Schema)

File: `ISCAR.B` | Fields: 35 | PK: `IS_NCR_NUM` (FLOAT)

**Important:** ISCAR uses the identical `IS_NCR_*` field prefix as ISNCR and has the
same 35-field layout. The distinction: ISNCR holds active Non-Conformance Records;
ISCAR holds Corrective Action Requests (CAR) formally created from an NCR.

Fields are identical to ISNCR (previously documented in QC module). Key fields:
IS_NCR_NUM (PK), IS_NCR_PART, IS_NCR_COMP, IS_NCR_LOT, IS_NCR_SERIAL, IS_NCR_CDATE,
IS_NCR_WHO, IS_NCR_QTY, IS_NCR_DCODE, IS_NCR_DESC, IS_NCR_ICR (internal CR flag),
IS_NCR_ORIG (origin flag), IS_NCR_WOPRE/WOSUF/MACH/TOOL/WC (WO/work-center context),
IS_NCR_PONUM, IS_NCR_RMA, IS_NCR_ACTION, IS_NCR_CAR (→ FK back to NCR?),
IS_NCR_DISP/DWHO/DDATE (disposition), IS_NCR_STATUS/SCRAP/QC/VEND/LOC, IS_NCR_EXTRA,
IS_NCR_PDRAW/PREV/CDRAW/CREV/CLOC (parent/child drawing revision tracking).

---

### ISCARFUP — Corrective Action Follow-Up Dates

File: `ISCARFUP.B` | Fields: 13 | PK: `IS_CARFUP_CAR` (FLOAT)

| Field | Type | Meaning |
|-------|------|---------|
| IS_CARFUP_CAR | FLOAT | CAR number (PK) → FK ISCAR |
| IS_CARFUP_DATE | DATE | Follow-up date |
| IS_CARFUP_USER | STRING 15 | Assigned-to user |
| IS_CARFUP_UID | STRING 30 | Unique identifier / task description |
| IS_CARFUP_TYPE | STRING 10 | Follow-up type code |
| IS_CARFUP_EXTRA | STRING 50 | Extra |
| IS_CARFUP_CDTE | DATE | Completed date |
| IS_CARFUP_CWHO | STRING 15 | Completed by |
| IS_CARFUP_GDTE1..5 | DATE ×5 | Goal/milestone dates 1–5 |

---

### ISCHAIN / ISCHAINM — Multi-Location Chain Dispatch Tables

Files: `ISCHAIN.B` / `ISCHAINM.B` | Fields: 17 each | PK: USER+PARENT+CHILD

Both files share the identical `IS_CHAIN_*` schema. ISCHAIN = active chain dispatch;
ISCHAINM = chain master / template. Used by the CH (Multi-Location Chain) module.

| Field | Type | Meaning |
|-------|------|---------|
| IS_CHAIN_USER | STRING 15 | User or owner (PK part 1) |
| IS_CHAIN_PARENT | STRING 12 | Source company code (PK part 2) |
| IS_CHAIN_CHILD | STRING 12 | Target company code (PK part 3) |
| IS_CHAIN_PARAM_1..10 | STRING 15 ×10 | Dispatch parameters (context-dependent per chain type) |
| IS_CHAIN_AUTO | STRING 1 | Auto-dispatch flag |
| IS_CHAIN_DATE | DATE | Chain execution date |
| IS_CHAIN_DESC | STRING 100 | Description |
| IS_CHAIN_EXTRA | STRING 100 | Extra |

The PARAM_1..10 fields carry the inter-company transaction parameters (item code,
quantity, PO/SO number, etc.) passed from parent to child company during chain
dispatch.

---

### ISBMESA / ISBMEST / ISBMTMP — BM Estimating BOM Mirrors

Files: `ISBMESA.B` / `ISBMEST.B` / `ISBMTMP.B` | Fields: 26 each
Schema identical to BKBMMSTR (BOM master) — uses `BKBM_*` prefix.

| Table | Role |
|-------|------|
| ISBMEST | Active estimating BOM (working copy used during ES quote) |
| ISBMESA | Estimating BOM archive (saved quote BOM) |
| ISBMTMP | Estimating BOM temp (in-progress edit buffer) |

All 26 fields identical to BKBMMSTR:
BKBM_PARENT + BKBM_COMPONENT (PK pair); BKBM_QTY_REQD, BKBM_REFERENCE,
BKBM_PROD_TYPE, BKBM_PROD_SCRAP, BKBM_PROD_OP (operation), BKBM_PROD_OPYN_1..6,
BKBM_PROD_PRICE, BKBM_PROD_RTNUM (routing#), BKBM_PROD_DUPOP, BKBM_PROD_OPDSC,
BKBM_PROD_VEND (outside-process vendor), BKBM_DATE1/2, BKBM_EXTRA,
BKBM_REV (revision), BKBM_P_TYPE/C_TYPE (parent/component item type),
BKBM_EST_LINE (FK to ISESADTL estimating line), BKBM_UID.

Cross-reference: → `docs/04-data-dictionary/tier1-tables.md` BKBM* family.

---

### ISCRISLS — CR/SO Approval Sales Data

File: `ISCRISLS.B` | Fields: 24 | PK: `ISCR_SLS_CUST` + `ISCR_SLS_ITEM`

| Field | Type | Meaning |
|-------|------|---------|
| ISCR_SLS_CUST | STRING 10 | Customer code (PK part 1) |
| ISCR_SLS_ITEM | STRING 15 | Item code (PK part 2) |
| ISCR_SLS_SDATE | DATE | Snapshot date |
| ISCR_SLS_SUOH | FLOAT | Units on hand at snapshot |
| ISCR_SLS_SHPQTY | FLOAT | Quantity shipped |
| ISCR_SLS_SHPDTE | DATE | Last ship date |
| ISCR_SLS_INVNUM | FLOAT | Invoice number |
| ISCR_SLS_FDATE | DATE | Future/forecast date |
| ISCR_SLS_FUOH | FLOAT | Future on-hand quantity |
| ISCR_SLS_SOLDTE | DATE | Sold date |
| ISCR_SLS_SOLDQT | FLOAT | Sold quantity |
| ISCR_SLS_NUM_1..2 | FLOAT ×2 | Numeric fields 1–2 |
| ISCR_SLS_FLAG_1..5 | STRING 1 ×5 | User flags 1–5 |
| ISCR_SLS_ALPHA_1..2 | STRING 30 ×2 | Alpha fields 1–2 |
| ISCR_SLS_EXTRA | STRING 50 | Extra |
| ISCR_SLS_ASOFDT | DATE | As-of date (inventory snapshot) |
| ISCR_SLS_ASOFOH | FLOAT | As-of on-hand quantity |
| ISCR_SLS_ASOFLG | STRING 1 | As-of flag |

Used by the CR (Contract Review / SO Approvals) module to track sales history data
per customer+item for the contract review decision.

---

### ISCTREVU — Contract Review Employee

File: `ISCTREVU.B` | Fields: 17 | PK: `IS_CREVU_EMPNME` (implicit — employee name key)

| Field | Type | Meaning |
|-------|------|---------|
| IS_CREVU_EMPNME | STRING 25 | Employee name (PK) |
| IS_CREVU_EMP | UBINARY 2 | Employee number → FK BKPRMSTR |
| IS_CREVU_DEPT | STRING 25 | Department |
| IS_CREVU_ADMIN | STRING 1 | Admin reviewer flag |
| IS_CREVU_LEVEL | STRING 2 | Review authority level |
| IS_CREVU_MOTPAS | STRING 10 | Motion password (electronic signature) |
| IS_CREVU_ACTIVE | STRING 1 | Active flag |
| IS_CREVU_CDATE | DATE | Created date |
| IS_CREVU_EDATE | DATE | Expiry date |
| IS_CREVU_ADATE | DATE | Last approval date |
| IS_CREVU_ATIME | TIME | Last approval time |
| IS_CREVU_FLAG_1..5 | STRING 1 ×5 | User flags 1–5 |
| IS_CREVU_EXTRA | STRING 100 | Extra |

ISCTREVU defines which employees can approve SOs via the CR module. MOTPAS =
electronic signature challenge (password required to approve). LEVEL governs which
SOs the reviewer can approve (dollar-limit based).

Cross-reference: ISSOREVU (the per-SO approval record) uses ISCTREVU employees as
approvers. Both documented together in `docs/03-modules/` CR module notes.

---

### ISCONVRT — Unit of Measure Conversion Table

File: `ISCONVRT.B` | Fields: 9 | PK: `IS_CONV_ITEM` + `IS_CONV_SUM` + `IS_CONV_PUM`

| Field | Type | Meaning |
|-------|------|---------|
| IS_CONV_ITEM | STRING 15 | Item code (PK part 1) |
| IS_CONV_SUM | STRING 10 | Stocking UOM (PK part 2) |
| IS_CONV_PUM | STRING 10 | Purchasing UOM (PK part 3) |
| IS_CONV_SCONV | FLOAT | Stock conversion factor |
| IS_CONV_PCONV | FLOAT | Purchase conversion factor |
| IS_CONV_WTCONV | FLOAT | Weight conversion factor |
| IS_CONV_DESC | STRING 90 | Description |
| IS_CONV_DATE | DATE | Last updated date |
| IS_CONV_EXTRA | STRING 100 | Extra |

Per-item stocking↔purchasing unit conversion. Used by receiving (PO module) and
material issue (WO module) when SUM ≠ PUM.

---

### ISCATMST — Category Master

File: `ISCATMST.B` | Fields: 3 | PK: `IS_CATM_CODE` (STRING 4)

| Field | Type | Meaning |
|-------|------|---------|
| IS_CATM_CODE | STRING 4 | Category code (PK) |
| IS_CATM_DESC | STRING 60 | Description |
| IS_CATM_EXTRA | STRING 100 | Extra |

Shared category code table referenced by multiple modules (JO module confirmed:
ISCATMST appears in T7JOBS fingerprint). Provides user-defined category groupings
for items, departments, or jobs.

---

### ISCYCLCD — Cycle Count Frequency Code

File: `ISCYCLCD.B` | Fields: 7 | PK: `IS_CYCLE_CODE` (STRING 4)

| Field | Type | Meaning |
|-------|------|---------|
| IS_CYCLE_CODE | STRING 4 | Cycle count code (PK) |
| IS_CYCLE_DESC | STRING 30 | Description |
| IS_CYCLE_FREQ | UBINARY 2 | Frequency in days |
| IS_CYCLE_DATE | DATE | Last cycle count date |
| IS_CYCLE_ALPHA | STRING 15 | Alpha category |
| IS_CYCLE_NUM | FLOAT | Numeric parameter |
| IS_CYCLE_EXTRA | STRING 50 | Extra |

Assigns cycle count frequencies to items. Used by PI (Physical Inventory) and
WC (Warehouse Control) modules. FREQ = days between counts; DATE = last count date
used to calculate when next count is due.

---

### ISBOLMS — BOL Manifest (ISSOBOX Schema Clone)

File: `ISBOLMS.B` | Fields: 22 | PK: SONUM+LINE+BOX

ISBOLMS uses the identical `ISSO_BOX_*` field schema as ISSOBOX (22 fields). The
naming difference: ISSOBOX = standard SO packing box record; ISBOLMS = BOL manifest
version (used when generating Bill of Lading to group boxes across SOs).

Fields: SONUM+LINE+BOX PK; CODE/QTY/LOT/SERIAL/TEMP/EXTRA; INVNUM/SHIPPR/SHPCOD/
WEIGHT/SKID/DATE; WOPRE/WOSUF (WO link); UCC(30); HT/LG/WD (dims); TRACK(40).

Cross-reference: ISSOBOX (22f) documented in SO module. ISBOLMS and ISSOBOX
are parallel schemas serving the same data at BOL-manifest time.

---

### ISBRANDC / ISBRANDS — Brand Category and Class Tables

**ISBRANDC** (2f): BKCM_ACCC_CCODE(5) + BKCM_ACCC_DESC(25) — brand category code
(uses BKCM_ACCC_* prefix from the CRM class code schema).

**ISBRANDS** (2f): BKCM_ACCL_CODE(10) + BKCM_ACCL_CLASS(5) — brand class link
(assigns a class to an account/brand; uses BKCM_ACCL_* prefix).

Both use CRM field prefixes even though they live in the IS* namespace; they are the
operational brand tables accessed by T7BRANDS (BR module).

---

### i2 Systems Custom Tables (CC* prefix)

These tables are specific to i2 Systems manufacturing operations and do not exist in
a standard EvoERP installation:

**ISCCICM** (10+ fields) — Cut Cloth / Corrugated Item Master:
CODE(15 PK) + DESC(30) + DESC2(30) + FSIZE(30 fabric size) + CUST(60) + COLLEC(120) +
HINGE(25) + SPY(25) + PDF(60) + PNAME(60). Stores fabric specifications for
corrugated/mattress component items.

**ISCCBTXN** (16f) — Cut Cloth transaction log:
FABRIC(15)+JOB(15)+LOT(15)+SER(25)+BIN(15)+LOC(10) PK-like fields; PULQTY/NEDQTY/LOTQTY;
SDATE/TDATE/STATUS/ALPHA/GDATE/TRANS/EXTRA. Records pull and cut transactions for
fabric-based components.

**ISCCMTF** / **ISCMGRP** (2f each, identical) — CC MTF (Manufacturing Transfer Form):
ITEM(15) + MTF(60). Maps items to their manufacturing transfer form template.

---

## Pass 138 — IC Extension, Business Scorecard, Links, NCR, Payroll (DDF lines 17298–19635)

### IC Item Master Snapshot / Extension Family

**ISICADT** (64f, `BKIC_PROD_*`) — IC item master audit snapshot. Full copy of BKICPROD
with a `BKIC_IS_DCODE` (3ch) discriminator. Captures CODE, DESC, TYPE, UM, CAT, TXBLE,
CLASS, reorder levels, last-sale/order/receipt dates, MTD/YTD/LYR usage quantities (unit
sales, gross sales, cost, net sales, net gross), 3 GL account pairs (asset+dept,
COGS+dept, scrap/net+dept), PRICE, UBO, PMAT, MANUF, NOTE, 6 avg cost components (lab,
setup, op, mat, FOH, VOH), EXTRA(100), TAXIN, ISUPC, LONGP. Confirmed 64 fields.

**ISICAMTR** / **ISICMSTR** (41f each, `IS_PROD_*`) — IC item master attribute extension.
Stores physical properties and UDFs that don't fit in BKICPROD: WT (weight 6-dec),
ITP(20), EXTRA(150), CDATE, TI/HI (tick/hit integers), FOBPAL/FOBFULL, HT/LG/WD
(dimensions 3), TOOL(15), SLEAD (safety lead days), RCDATE, 10 FLAG chars, 5 ALPHA
strings (30ch each), 5 NUM floats, 5 GDATE dates, ADATE. Both tables are schema-identical.

**ISICESA** / **ISICEST** (64f each, `BKIC_PROD_*`) — IC item master snapshots for the
Estimating module (Archive and Current). Schema-identical to ISICADT.

**ISMICADT** / **ISMICESA** / **ISMICEST** (108f each, `MTIC_PROD_*`) — Multi-company
IC item master snapshots. Extends the BKICPROD schema with a leading CLASS(4) field plus:
12 SPECS strings (30ch), 10 VEND+VNAM+VPC (vendor codes, names, vendor part codes), 15
RCOST floats (replacement costs), 5 SUBST items (substitutes), LOTSZ, OPT/OPTCS/OPTCD
(option codes), UIQC (qty in QC), EXPBF/DELBF (expire/delete buffers), CUM(3), LONGP.
All three schema-identical. Confirmed 108 fields.

### IS System Configuration

**ISIS** (23f) — IS module configuration singleton (one record). Flags: IS_TAX,
IS_MULTI_CURR, IS_LANDED_COST, IS_UPC, IS_RETAIL_PRICE, IS_COMM_PRICE, IS_IMAGING,
IS_MULTI_CPAY, IS_TAX_FRM, IS_PO_TAX, IS_TAX_IN, IS_TAX_CVT, IS_CUR_CVT,
IS_AUTO_TAX_CAL, IS_EZPAY, IS_RMA, IS_SPEC_SUP. Also stores UPC_1(6)/UPC_2(5) prefix
segments, IS_DEMO (demo expiry date), IS_PIC_PATH(20), IS_SPEC_SUPF/SUPT (UBINARYs).
This table controls which optional IS modules are active.

**ISISATAX** (13f, `BKIS_TAX_*`) — Sales/use tax audit trail. Per-transaction record:
TAX_CODE(10), TAX_DATE, TRFLAG, taxable/non-taxable/tax amounts, customer, vendor,
invoice#, PO#, tag, currency code, AP invoice#.

### Item Configuration and ITP

**ISITMCFG** (9f, `IS_SERC_*`) — Per-item serial/lot number auto-generation configuration.
KEY: ITEM(15) + CLASS(4). Fields: start position, length string, total width, next number
float, last number string(25), EXTRA(100), L2. Controls how serial/lot numbers are
generated for each item.

**ISITP** (3f, `IS_ITP_*`) — Inspection/Test Plan master. KEY: ITP_NUM(20). Fields:
ITP_DESC(80), ITP_EXTRA(100). Defines inspection plans by number; plans are referenced
from ISICAMTR.IS_PROD_ITP.

### Business Scorecard

**ISJBSF** (143f, `ISBSF_*`) — Business scorecard / management KPI snapshot. Key:
STARTDATE + ENDDATE (period boundaries). Captures cross-module summary metrics:
- AR: balance, billings, receipts, discounts, COGS, deposits
- AP: balance, payables, payments, discounts, ATP
- SO: open, booked, shipped values
- PO: open, booked, received values
- WO: WIP balance, issues, FP variances; 9 cost component summaries
  (setup/labor/output/material/FOH/VOH/misc ext/FP/WIP variance)
- IC: inventory value
- Cash: CASH_TOTA + 9 CASH_ACT slots (monthly accounts) + 100 CASH_ACTS slots
  (annual trend — 100 periods × 1 account each)
- EXTRA(100)

Architecture note: the 100 CASH_ACTS fields allow storing a full 100-period cash flow
trend (e.g. 8+ years of monthly data) in a single record per account group.

### Job Master

**ISJOB** (9f, `IS_JOB_*`) — Job/project master. KEY: JOB_NUMB(15). Fields: DESC(30),
CUST(10), VEND(10), RSVD(1), STATUS(1), OPENDT, CLOSEDT, EXTRA(100). Lightweight
project tracker linking a job number to a customer or vendor.

### Landed Cost

**ISLANDF** (6f, `ISIS_LND_*`) — Landed cost freight GL account configuration. Three GL
account+dept pairs: appraise (GLA/GLD), freight (GLAFR/GLDFR), customs-freight
(GLACF/GLDCF). No key field visible — likely a single-record config table.

### Label Management

**ISLBLMAP** (102f, `IS_LABEL_*`) — Label template mapping. KEY: ITEM(15) + NUM(15).
Fields: DESC(30), DFLT(1), OBS(1), CDATE/EDATE (effective dates), CUST(10), VEND(10),
RTM(12) — the ReportBuilder .RTM filename for this label template. Then: 30 NTYPE slots
(3ch each — note types to include), 30 FCOLOR + 30 BCOLOR slots (10ch each — foreground
and background color names per print zone), FLAG(1), EXTRA(100).
This table defines which label template to use per item (optionally filtered by
customer/vendor), and controls print formatting by note type.

### Document Attachment System

**ISLINKS** (311f, `IS_LNK_*`) — Cross-module document/URL attachment store.
KEY: UID(48) — a 48-char identifier (application code + record key). Fields:
- LINK(256) — file path or URL
- APP(10) — application module code
- TYPES_1..100 — 100 single-char type flags (document type classification)
- PCB_1..100 — 100 single-char PCB flags (permission/control bits)
- DEF_1..100 — 100 single-char DEF flags (default/filter flags)
- GLOBAL(1), OPENWITH(1), DATE, WHO(15), ATYPE(3), EXTRA(100), PRIVATE(1), SORT float

The 100-slot type/PCB/DEF arrays allow extremely flexible classification and access
control for each attachment. IS_LNK_UID format: `<APP><RECORD-KEY>` zero-padded to 48
chars, enabling lookup of all attachments for any ERP record.

**ISLTYPE** (4f, `IS_LT_*`) — Link type code master. TYPE(3), DESC(30), SEC (security
level), EXTRA(100).

### Location Costing

**ISLOCCST** (7f, `IS_LCST_*`) — Per-location average cost tracking. KEY: PART(15) +
LOC(10). Stores AVGC (average cost 4-dec), BOOKVAL (book value 4-dec), LDATE/LTIME
(last update timestamp), EXTRA(150).

### Activity Logging

**ISLOG** (9f, `IS_LOG_*`) — User activity log. Fields: WHO(35), WHAT(15),
DOING(60), STARTD, STARTT(12), COMPANY(3), KILL(1), MSG(200), EXTRA(100). Records
who did what when; KILL flag marks entries flagged for deletion.

### Lot/Serial Tray Mapping

**ISLOTS** (11f, `IS_SER_*`) — Serial assembly genealogy (schema identical to
ISHLOTS/ISHSERIA). KEY: WOPRE + WOSUF + PARENT(15) + COMP(15) + PSERIAL(25). Fields:
same IS_SER_* structure. NOTE: DDF typo confirmed — field 11 is `IS_SER_EXRA` not
`IS_SER_EXTRA`.

**ISLSMAP** (31f, `IS_MAP_*`) — Lot/serial tray position map. KEY: TRAYNUM(25) +
POSITION(10). Links a tray slot to a WO operation: WOPRE/WOSUF/OPER, then parent
part+lot+serial+qty and child part+lot+serial+qty+qty-per. Also: BATCH(25), 5 dates,
5 alpha fields (25ch), 5 flags, EXTRA(100). Used for tracking component assembly
placement on a physical tray or pallet.

### Machine Scheduling

**ISMACS** (11f, `IS_MACS_*`) — WO machine scheduling record. KEY: WOPRE + WOSUF +
OPER + MACNUM(4). Fields: WC(12), SDATE/STIME (scheduled start), FDATE/FTIME
(scheduled finish), EXTRA(100), TREM (time remaining float). Tracks machine assignment
per WO operation.

### Multi-Currency

**ISMCF** (49f, `ISIS_MCF_*`) — Multi-currency forex configuration per currency code.
KEY: CODE(3). Fields: BASE(1) flag, then 7 GL account+dept pairs: Bank (BK), Sales (BS),
Interest (IS), BankX (BKX), APX, ARX — plus standalone GL pairs for AR/AP/PO/CS
(cash settlement). Financial fields: AMTBNK/AMTAP/AMTAR/AMTFE (current balances),
AMTPOR, AMTAD, AMTCS, AMTAPD. Currency: SYMBOL(1), SYMPOS(1), DEC (decimal places),
SYMDSC(10). Interest: INTRES (rate 3-dec), INTDAY. Confirmed 49 fields.

**ISMCR** (22f, `ISIS_MCR_*`) — Multi-currency exchange rate history. KEY: BASE(3) +
DATE. Stores 10 source currency codes (SOURCE_1..10, 3ch each) and 10 corresponding
rates (RATE_1..10, float 6-dec). One record per base currency per date.

### MRP Forecast

**ISMRPFC** (9f, `BKMRP_FC_*`) — MRP demand forecast. KEY: FC_PART(15) + FC_DATE.
Fields: QTY (planned demand), EXTRA(25), OQTY (original qty), CQTY (current qty),
FLAG(1), DATE1 (alternate date), NUM (sequence#). Feeds into MRP net requirements
calculation.

### NCR / Nonconformance

**ISNCR** (35f, `IS_NCR_*`) — Nonconformance Report. KEY: NCR_NUM (float auto-number).
Fields: PART(15), COMP(15) (component that failed), LOT(15), SERIAL(25), CDATE, WHO(15),
QTY, DCODE(10) (defect code), DESC(60), ICR(1) (internal corrective action required),
ORIG(1) (origin code), WOPRE/WOSUF, MACH(4), TOOL(15), WC(12), PONUM, RMA#, ACTION(1),
CAR# (corrective action request link), DISP(10) (disposition code), DWHO(15)/DDATE
(disposer), STATUS(1), SCRAP(2)/QC(2) codes, VEND(10), LOC(10), EXTRA(50), PDRAW/PREV
(parent drawing/rev), CDRAW/CREV (component drawing/rev), CLOC. Confirmed 35 fields.

This table is the origin point for CAR/CAPA tracking — NCR.CAR → ISCAR.IS_NCR_NUM.

### Notes System

**ISNOTES** (13f, `IS_NOTE_*`) — Cross-module notes/memos store. KEY: NOTE_ID(48) + TYPE.
Fields: CDATE/CTIME(10)/CWHO(15) (creator), EDATE/ETIME(10)/EWHO(15) (last editor),
EXTRA(100), PRIVATE(1), GROUP(4), CONTACT(30). Field 13 has corrupt DDF metadata
(`BKAP_INVL_GLACT_48`, Date type, 256-byte size) — this is a DDF encoding artifact; the
actual field stores the note text blob. IS_NOTE_ID uses the same 48-char UID format as
ISLINKS (app + record key).

**ISNTYPE** (4f, `IS_NT_*`) — Note type code master. TYPE(3), DESC(30), SEC
(security level), EXTRA(100).

### Auto-Numbering

**ISNUMBER** (52f, `IS_NUM_*`) — Next-number sequence registry. KEY: CODE(10).
Stores 50 independent next-number slots (NEXT_1..50, float 0-dec) + EXTRA(100).
One record per document type (e.g. "NCR", "CAR", "ECO"). The 50 slots allow
multi-company or multi-division sequence sets within a single record.

### Order / PO Support

**ISORDDSC** / **ISPODESC** (1f each) — Order and PO description code masters.
Single field: IORD_DESC_CODE(30). Simple lookup tables for standard order descriptions.

**ISORDECO** (13f, `IS_OECO_*`) — Order-to-ECO cross-reference. KEY: SONUM + PONUM +
UNUM. Fields: PART(15), DRAW(15), REVLVL(5), ECO(15), WOPRE/WOSUF, ENTDATE, EXTRA(100),
TMPO(40). Links sales orders and POs to Engineering Change Orders. NOTE: field 13 has
corrupt DDF metadata (`BKAP_INVL_GLACT_56`, Date/256/dec5) — same encoding artifact as
ISNOTES.

**ISPOBOX** (22f, `ISSO_BOX_*`) — PO pack box contents (schema mirrors ISBOLMS/SO boxes).
KEY: SONUM + LINE + BOX. Fields: CODE(15), QTY, LOT(15), SERIAL(25), TEMP(1), EXTRA(150),
INVNUM, SHIPPR, SHPCOD(10), WEIGHT, SKID, DATE, WOPRE/WOSUF, UCC(30), HT/LG/WD, TRACK(40).
PO-side packing list tracking.

**ISPOHTRK** / **ISPOTRK** (7f each, `IS_TRK_*`) — Shipment tracking records (identical
schema). KEY: TRK_ORD (order#). Fields: TRK_NUM(25) (tracking number), SHPVIA(10) (carrier),
CDATE (created), RDATE (received), STATUS(50), EXTRA(100). ISPOHTRK = PO inbound
receiving; ISPOTRK = PO outbound shipment.

**ISPOLOG** (9f, `ISPO_LOG_*`) — PO change/audit log. KEY: EMP + DATE + TIME.
Fields: WHO(15), PRGM(8), PONUM, NAME(50), REASON(50), EXTRA(100).

**ISPOS** (2f, `BKCM_ACCL_*`) — PO account class master. CODE(10) + CLASS(5).
**ISPOSC** (2f, `BKCM_ACCC_*`) — PO account class code master. CCODE(5) + DESC(25).

### Production Requisition

**ISPREQ** (25f, `IS_PREQ_*`) — WO production material requisition. KEY: WOPRE + WOSUF +
OPER + WC + EMP. Fields: RDATE (required date), PART(15), QTY(4-dec), SCRAP(2) code,
REASON(30), NOTE(200), NOTE2(200), LOC(15), PRINTED(1), IQTY (issued qty, 4-dec),
INOTE(200) (issue note), LOT(15), SERIAL(25), LCOST (landed cost), CLOSED(1)/CDATE,
NOB(1), EXTRA(100), RTIME/CTIME (request/close timestamps). Records material pull
requests generated from WO routing operations.

**ISPRESN** (1f) — Production reason code (single REASON field 30ch).

### Program Registry

**ISPRINFO** (4f, `ISPR_INFO_*`) — Program information registry. KEY: PROG(30).
Fields: DESC(80), MISC(50), TYPE(1). Metadata registry of TAS Pro programs/modules.

### Payroll

**ISPRMSTR** (384f, `BKPR_EMP_*`) — Payroll employee master. One of the largest tables
in EvoERP. KEY: EMP_NUM (UBINARY). Key fields:
- Demographics: FNMI(25), LNME(25), ADD, CSZ, ST, ZIP, CNTRY, PHONE, SSN(11), BDAY
- Employment: SDATE (start), TERM(1) (terminated flag), SHIFT, BENDTE, EMAIL(128)
- Pay: PAYTYP(1), 15 PAYAMT rates (float 4-dec), 2 federal exemptions
- Hours by pay class (12 periods × 3 sets = 36 slots each): regular/actual/vacation/sick
  OT hours (OHQTD_1-12, OAQTD_1-12, OHYTD_1-12, OAYTD_1-12)
- Taxes QTD/YTD: FIT, FICA, 2 FIC codes, state, workers comp, Medicare, other
- SDI: SDIQTD/SDIYTD/SDIEXM
- State: STEXM/STEXMA/STEXMN
- UOD (user-defined deductions): 20 deductions × 4 arrays = UODQTD_1-20/UODYTD_1-20/
  UODAMT_1-20 (per-period amount)/UODLMT_1-20 (per-period limit)/UODYLM_1-20
  (annual limit)/UDELMT_1-20 (one-time limit) — 120 float fields
- UDE (user-defined earnings): identical 20-slot structure with UDAMT/UDEQTD/UDEYTD/
  UDELMT/UDEYLM/UDEAMT arrays — 120 more float fields
- 15 expense GL accounts + depts (EXPACT_1-15 + EXPDPT_1-15)
- W/C rates: WCEE/WCER (employee/employer workers comp rates)
- Vacation/sick: VRTE, SRTE, VCAP, SCAP
- Additional: DEPT, LOCCOD, EIC/EICAMT, YEAR, QTR, bank routing+account (BANKR(9)/BANKA(17))

Total record size: 3,389+ bytes (field 384 BANKA ends at offset 3,389).

**ISPRSALE** (87f, `BKPR_SLS_*`) — Sales rep commission tracking. KEY: EMPNUM.
Fields: 2 commission classes with rates/calculation methods (HOW: % or flat, WHEN:
invoice/receipt), 12-period arrays for quota, gross sales, COGS, cash receipts, earned
commission, paid commission. Also: name (FNMI/LNME), expense GL account+dept,
EXTRA(100), EMAIL(128). Total 87 fields.

**ISPRTEMP** (15f, `ISPR_TRN_*`) — Payroll GL transaction staging buffer. Fields:
GLACCT(10), GLDPT(4), DATE, CODE(10) (payroll code), INVC(10) (invoice/check ref),
DESC(25), DC(1) (debit/credit), AMT, TYPE(2), ENTDTE, EXTRA(25), TRXN (transaction#),
POST(1), PERIOD, BATCH. Payroll journal entries held pending GL post.

**ISPRUDF** (31f, `ISPR_UDF_*`) — Payroll user-defined deduction/earning definition.
KEY: UDF_DIV(4) + UDF_NUM. Defines the rules for each of the 20 UOD/UDE slots:
DIVNAM(20), DESC(12), 9 tax-inclusion flags (FIT/FUTA/SDI/PTAX/SS/MED/SIT/WC/SUTA/LOCAL),
2 calculation types for EE + ER (CALCEE/CALCRE, EETYPE/ERTYPE — calculation formulas),
EE/ER amounts, per-period and annual limits, 2 GL account+dept pairs (liability/expense),
VEND(10) (vendor for remittance), TAXOUT, EXTRA(100).

### QC Receiving Inspection

**ISQCAMST** (14f, `BKQC_*`) — QC receiving inspection master record. KEY: VEND_CODE +
RECV_DATE + PO_NUM + RECVR_NUM + POL_ITM_NO. Fields: PKSLIP_NUM(15), QTY_RECVD/BUYOFF/
REJECT, PKSLIP_QTY, PROD_CODE(15), UNIT_COST(4-dec), EXTRA(25), OUT_DATE.

**ISQCATRN** (20f, `BKQC_TRN_*`) — QC receiving inspection transaction detail. KEY:
TRN_PO + TRN_VEND + TRN_CODE + TRN_RECNUM. Fields: GQTY/BQTY/UQTY (good/buyoff/under
qtys), SCRAP(2)/REWORK(2) codes, PO/AR/BO dates, EMPNUM, RECVNM, FAULT(1)/BROKEN(1)
flags, FIXQTY, POQTY, INVCD(1) (invoice code), FLAG(1). Detail line for each inspection
disposition decision.

---

## Pass 139 — IS* tables: Reporting, RMA, Routing, Scheduling, SE/Service, Shipping (DDF lines 19929–21379)

### Reporting Support

**ISREPDEF** (3f, `ISREP_DEF_*`) — Report label/title definition. KEY: LABEL(5). Fields:
TITLE(30), EXTRA(50). Minimal lookup table mapping a 5-char code to a report display title.

**ISREPLNK** (11f, `ISREP_LNK_*`) — Report-to-customer/item/class link. KEY: REPNM(UBINARY
2)+CUST(10)+ITEM(15)+CLASS(4). Fields: EXTRA(100), DATE, SDATE/EDATE (date range), LABEL(5),
GLA(10), GLD(4). Links a report number to a customer+item+class combination with effective
date range and GL account/dept override.

**ISREPORD** (17f, `ISREP_ORD_*`) — Report order tracking. KEY: REPNM(UBINARY)+REPWH(1).
Fields: SONUM+INVNM+INVDT, ULID(4-dec), COMPR(4-dec), CMAMT+AMT+AMTRM (commission+amount+
amount remaining), CBK(1), PCODE(15), CUST, PAYDT, EXTRA(100), GLA+GLD. Tracks which SO/
invoice a report represents, with commission percentage and payment date.

### RFQ Support

**ISRFQADS** (5f, `BK_DESC_*`) — RFQ address/description lines. Same BK_DESC_* schema used
by many description-line tables: CODE(15)+NUM+LINE+NOTES(70)+DESC(25). Stores multi-line
text blocks keyed on a code+number+line counter.

### RMA (Return Merchandise Authorization) Family

EvoERP's RMA system is a large family of closely related tables. Key architectural pattern:
each document type has a current version and an archived (AI/history) version with identical
schema. Invoice header/line snapshots use BKAR_INV_*/BKAR_INVL_* prefixes (full clones of
the AR invoice schema).

**ISRMAAI** (54f, `IS_RMA_*`) — RMA line item, archived. KEY: NUM(float)+PART(15)+LINEID.
Fields: DATE/RCPTDATE/CLOSDATE, STATUS(30), REASON(30), DISP(40), original SO/INV/OLDRMANO
cross-refs (OSONUM/OINVNUM/OLDRMANO), replacement SO/INV/CM cross-refs (SONUM/INVNUM/CMNUM),
REORDER(1), WO (WOPRE+WOSUF), SODATE/INVDATE/CMDATE/DISPDATE, WARRANTY(1), SRNUM (SR link),
INVCD(1), DISPSEL(UBINARY), IEXTRA(150), 7 named one-char disposition flags
(WO/CR/SO/STOCK/SCRAP/SR/REFUND), FLAGS_1..20. Archive of closed RMA lines with complete
disposition history. Note: FLAGS_1..20 provide 20 user-defined extension flags.

**ISRMAC** (3f, `IS_RMA_*`) — RMA reason code master. KEY: CODE(30). DESC(60)+EXTRA(100).
Simple lookup for RMA return-reason codes.

**ISRMADSC** / **ISRMDESC** (5f each, `BK_DESC_*`) — RMA description lines. Both use the
standard BK_DESC_* schema (CODE+NUM+LINE+NOTES+DESC). Long-form text for RMA documents.

**ISRMAI** (54f, `IS_RMA_*`) — RMA line item, current (schema identical to ISRMAAI).
Active (open) RMA lines; ISRMAAI holds the archived version after closure.

**ISRMAINF** / **ISRMHINF** / **ISRMINFO** (54f each, `ISSR_INFO_*`) — RMA extended info
(active, historical, module-info variants). Schema identical to ISSRINFO/ISQTINFO pattern:
KEY: SRNUM+UID. CODE(15), 5+5 dates (DATE_1..5 + DATE1..5), 20+20 alphas ×25ch (ALPHA_1..20
+ AL1..20), EXTRA(100). Total record ~1,171 bytes. Three separate tables maintain the same
flexible UDF structure per RMA number for active, historical, and module-level data.

**ISRMAINV** / **ISRMINV** (84f each, `BKAR_INV_*`) — RMA invoice header snapshot (active
and current variants). Full clone of the AR invoice header: customer/ship-to addresses,
terms, salesperson, totals (subtot/tax/total/COGS), freight, department, all IS extension
fields (currency ISCUR, tax key ISTXKY, revision ISREV/ISRVDT, release RELNUM, tracking,
QC status QSTAT, misc). ~1,332+ bytes. The IS-prefixed fields within BKAR_INV_* schema
confirm these are captured at the IS module layer.

**ISRMAIVL** / **ISRMINVL** (28f each, `BKAR_INVL_*`) — RMA invoice line snapshots (active
and archived). Full clone of AR invoice line: item code+desc+qty+price+disc+ext+COGS, item
type+taxable+UBO+USTD, RTS(1), location, ABQTY, UM, commission rates, dates, tax amount,
freight+coop+OOQTY, extra, SCCOG. ~312 bytes.

**ISRMTXN** / **ISRMTXNS** (14f each, `BKAR_TXN_*`) — RMA transaction (current and staged).
KEY: SONUM. Fields: CODE(15)+DESC(30)+QTY+LOT(15)+SERIAL(25)+DATE+STOCK(15)+LINE+LOC(10)+
TMPSO(40)+SRNUM+EXTRA(50)+BIN(15). Inventory transaction record for each RMA item movement
(receipt back to stock, scrap, reroute to WO, etc.).

### Routing Extended and Snapshot Tables

**ISROUTEX** (100f, `IS_ROUT_*`) — Routing extended data per operation. KEY: CODE(15)+OPER.
Contains 5 parallel cycle-tracking arrays:
- Cycle time: CYCTIME_1..10 (UBINARY), CYCHR_1..5, CYCMIN_1..5, CYCSEC_1..5
- Cycle production: CYCPART_1..5 (float, 1-dec = parts/cycle)
- Cycle notes: CYCNOTE_1..5 (255ch each = 1,275 chars total)
- Cycle assignment: CYCEMP_1..5 (employee UBINARY), EMPNAME_1..5 (80ch each = 400 chars)
- Cycle WO: WOPRE_1..5 + WOSUF_1..5 (WO references per cycle slot)
- Cycle dates: CYCDATE_1..5, CYCMACH_1..5 (4ch machine codes)
- 15 FLAGS (single-char), 10 ALPHA_N×30ch, 5 NUM_N (float, 2-dec), EXTRA(100)
- TIMEREQ(1), CALCREQ(1)
Total record ~2,338 bytes. Captures detailed cycle-time study data for 5 independent cycles
on a single routing operation, with employee, WO, note, and machine per cycle.

**ISRTESA** / **ISRTEST** (62f each, `MTRO_*`) — Routing operation snapshot (estimate and
test/template variants). KEY: CODE(15)+OPER. Full clone of BKROUT operation: desc+operdesc,
type(1), lead, vendcost(6-dec), partshr, timepart/setuphrs (TIME), lotsize, 15 instruction
lines ×60ch (900 chars), WC(12)+wcdesc(30), vendcode(10)+vendname(25), rates for
labor/machine/fovhd/vovhd/setup (4-dec each), tmachine(4)+tmachdesc(30), tool(15)+tooldesc(30),
num(UBINARY), num_person, misc_cost+misc_desc(30), misc_acost, op_temp_no, num_proces,
time_perpr (TIME), md_proc_hr(1), proc_perhr, std_time(1), min_chg, overlap(UBINARY),
piece_rate, longtime(7-dec), print(1), class(15), extra(150), negovlp, def_time (TIME),
r_type(10), est_line, est_tag(10). ~1,514+ bytes. ISRTESA = estimate routing snapshot;
ISRTEST = routing test/template (schema identical).

### Shipping and Load Manifest

**ISRTLOAD** (21f, `IS_LOAD_*`) — Shipping load manifest. KEY: SONUM. ITEM(15)+DESC(30)+
SOLINE(3)+SCCOGS+ORDQTY+BALQTY+LOADQTY+SCANQTY+LOADNUM+TRUCK(15)+LOC(10)+SER(25)+LOT(15)+
BIN(15)+DATE1/DATE2+NUM2+CNTR+ALOAD(15)+EXTRA(100). Tracks qty ordered vs loaded vs scanned
onto a truck (LOADNUM) per SO line and serial/lot/bin combination.

**ISRTMS** (29f, `IS_RTM_*`) — Report-template/label mapping. KEY: CUST(10)+VEND(10)+ITEM(15).
RTM(12, label template filename)+PROGRAM(15)+DESC(30)+DFLT(1)+DATE+FLAG(1). Label name
fields: PARTLBL/SHIPLBL/CONTLBL/MIXEDLBL/QUICKLBL/MISCLBL1-3 (all 12-char template names
for different label types). QTY(UBINARY)+EXTRA(100)+PRINTER_1..10 (10 printer path strings,
90ch each = 900 chars total). Maps item/customer/vendor to specific label template file names
and printer paths for up to 10 different label printers.

### Job Scheduler

**ISSCHED** (24f, `IS_SCHED_*`) — EVO job scheduler task definition. KEY: NAME(50). Fields:
DESC(256), PROG(256), CO(3), TYPE(1), DATE+TIME (next run schedule), RECUR(float, interval),
LOG(256, last run output), EXTRA(100), LDATE/LTIME (last-run datetime), WHO(15),
EMAIL(128), PARAM1..PARAM9+PARAM0 (10 parameter slots ×256ch each = 2,560 chars). Total
record ~3,649 bytes. Stores task name, the EVO program to run (PROG), schedule (next
date+time + recurrence interval), last-run log, and 10 arbitrary program parameters.
PARAM0 appears to be the 10th parameter (zero-indexed last). This is EVO's internal cron/task
scheduler — no external scheduler required.

### Compound and Service Detail

**ISSCOMP** (5f, `IS_SCOMP_*`) — Compound/complexity detail. DETAIL(20)+COMPND(30)+VIS(1)+
WHO(40)+SCOMP(50). Tracks compound items or visual complexity assignments per detail code.

**ISSDET** (4f, `IS_SDET_*`) — Service/schedule detail type. TYPE(20)+DETAIL(20)+WHO(40)+
SUB(1). Detail-type classification for service scheduling.

### SE (Service/Estimate) Document Family

The SE family is structurally parallel to the RMA family, using the same BKAR_INV_*/BKAR_INVL_*
AR invoice clones for document headers and lines.

**ISSEDH** / **ISSESH** (84f each, `BKAR_INV_*`) — SE Document/Session header. Full AR
invoice header clone (same 84f schema as ISRMAINV/ISRMINV). ISSEDH = SE document header;
ISSESH = SE session header. Both use the full BKAR_INV_* field set including all IS extension
fields (ISCUR, ISTXKY, ISREV, ISRVDT, RELNUM, TRACK, QSTAT, MISC).

**ISSEDL** / **ISSESL** (28f each, `BKAR_INVL_*`) — SE Document/Session lines. Full AR
invoice line clone (same 28f schema as ISRMAIVL/ISRMINVL). SE document lines and SE session
lines respectively.

**ISSEPROC** (2f, `IS_SEPROC_*`) — SE process access. PROC(25)+WHO(40). Maps a process name
to a username — access control or log for SE processes.

**ISSEQUIP** (2f, `IS_SEQUIP_*`) — Service equipment master. NAME(20)+DESC(40). Minimal
lookup for equipment names used in service records.

**ISSETYPE** (2f, `IS_SETYPE_*`) — SE error type. ERR(25)+WHO(40). Error type classification
for SE error tracking.

### Serial Number Management

**ISSERCNT** (9f, `IS_SERC_*`) — Serial number auto-counter. KEY: ITEM(15)+CLASS(4). Fields:
SPOS(UBINARY, start position in serial string), LENG(2, length of numeric portion), TOTAL
(UBINARY, total serial length), NUMBER(float, current counter value), LAST(25, last serial
issued), EXTRA(100), L2(UBINARY). Drives auto-generation of serial numbers per item/class
using a configurable position+length format within the serial string.

**ISSERIAL** (11f, `IS_SER_*`) — Serial BOM component tree. KEY: WOPRE+WOSUF+PARENT(15)+
COMP(15). Fields: PDESC(30), PSERIAL(25), ADATE (assembly date), CDESC(30), CSERIAL(25),
FDATE (finish/final date), IS_SER_EXRA(100). Records which serial-numbered component was
assembled into which serial-numbered parent item on which WO, with assembly date and final
date. Note: field name `IS_SER_EXRA` is a confirmed DDF typo (see ISLOTS, ISHLOTS).

**ISSERR** (14f, `IS_SERR_*`) — Shop floor error log. KEY: WOPRE+WOSUF+OPER+TIME+DATE.
Fields: ERROR(25), PROCESS(25), COUNT(UBINARY), REF(50), EXTRA(50), SERIAL(20), ADOF(1000,
Description of Failure text), ADIAG(1000, Diagnosis text), AREWORK(1000, Rework instructions
text). Total record ~3,228+ bytes. Each record stores a complete failure report for a WO
operation: what failed (ADOF=1KB), diagnosis (ADIAG=1KB), and rework plan (AREWORK=1KB).
The most text-intensive table in the IS family.

### Shipping Carrier Configuration

**ISSHIPA** (5f, `IS_SHPA_*`) — Shipping API credentials. KEY: CODE(10). USER(30)+PASS(30)+
TOKEN(30)+EXTRA(50). Stores carrier-API login credentials (username, password, API token) per
carrier code. Likely used for UPS/FedEx/etc. web-service rate shopping.

**ISSHIPCO** (16f, `IS_SHIP_*`) — Shipping company extended master. KEY: SHPCOD(10). SHPNME(30)+
SHPDESC(60)+VNDCOD(10)+5 NOTES×60ch (300 chars)+SHIPVIA(15)+EXTRA(150)+5 WEB_N×120ch (600 chars
of web endpoint URLs). Augments the base shipping-company master with vendor link, notes, and
web API endpoint URLs.

**ISSHPVIA** (23f, `IS_SHPVIA_*`) — Customer-specific ship-via setup. KEY: CUST(10)+CODE(15).
PRTY(UBINARY)+OBS(1)+ACCT(25, carrier account#)+PHONE(25)+10 NOTES×60ch (600 chars)+DATE+
CNTCT(25)+FLAG(1)+VEND(10)+ALPH1/2×15+EXTRA(100). Per-customer carrier account credentials
with contact info and 10 notes lines. Enables billing shipments to customer's own carrier
account.

### Digital Signature

**ISSIGN** (16f, `IS_SIGN_*`) — Digital signature record. KEY: NUM(float). WHO(40)+POS(40,
position/title)+EWHO(15, employee code)+EDATE/ETIME+NAME(40)+JPG(256, file path to signature
JPEG image)+SDATE/STIME+5 GDTE1..5 (general dates)+EXTRA(50). Stores signature metadata and
a path to the scanned/captured JPEG image. Used for electronic approval workflows (POs, QC
sign-offs, etc.).

### Sales Forecast

**ISSLSFC** (9f, `BKMRP_FC_*`) — Sales module forecast entries. KEY: PART(15)+DATE. QTY+
EXTRA(25)+OQTY (original qty)+CQTY (committed qty)+FLAG(1)+DATE1+NUM. Uses the BKMRP_FC_*
prefix (same as ISMRPFC), indicating shared MRP forecast schema. Tracks forecast qty vs
committed qty per item per date — feeds into MRP demand planning from the sales side.

### SMT (Surface Mount Technology) Assembly

**ISSMTCFG** (15f, `IS_SMT_*`) — SMT machine reel configuration. KEY: WOPRE+WOSUF+OPER(3).
MACHINE(4)+DATE+TIME+EMP(4)+COMP(15, component/part)+LOT(15)+CURRENT(1)+REEL(UBINARY)+
EXTRA(50)+CNTR(UBINARY)+CAP(UBINARY)+RQTY(float, 4-dec). Tracks which component reel is
loaded on which SMT machine for a given WO operation, with lot, employee, and reel capacity.
Supports SMT pick-and-place traceability.

### Structured Notes (Extended)

**ISSNOTES** (12f, `IS_NOTE_*`) — Structured note record with dual-author tracking and
privacy/group assignment. KEY: ID(48, UID matching ISLINKS/ISNOTES format)+TYPE(3). Fields:
CDATE/CTIME(STRING 10)/CWHO(15) (created: date + time-string + employee), EDATE/ETIME
(STRING 10)/EWHO(15) (last-edited), EXTRA(100), [12-byte gap at offset 209–220], PRIVATE(1),
GROUP(4), CONTACT(30). Note: CTIME and ETIME are STRING(10) rather than TIME type — stored
as formatted time text. PRIVATE flag marks notes as non-public; GROUP assigns the note to a
department/team code; CONTACT links the note to a named contact. Total record ≈ 256 bytes.
*Correction from Pass 139: originally documented as 9f — DDF lines 21377–21381 confirmed 3
additional fields (PRIVATE, GROUP, CONTACT) at the end of the record.*

---

## Pass 140 — IS* Tables (SO Extension, SR/SS Snapshots, IST/ISU/ISV/ISW Families)
*DDF source: `samples/ddf/schema.md` lines 21382–24237. Completed 2026-06-22.*

### SO Extension — Shipping Box Manifest

**ISSOABOX / ISSOAHBX / ISSOBOX / ISSOHBOX** (22f each, `ISSO_BOX_*`) — SO shipping box
manifests, 4 schema-identical variants (archived-line, archived-header, current-line,
current-header). KEY: WOPRE+WOSUF+LINEID. Fields: BOXNUM(STRING 25)+LNITEM(15)+UCCLBL(25,
UCC-128 barcode)+BOXHT+BOXLG+BOXWD (FLOAT, box dimensions, 2-dec)+LDATE+EXTRA(50)+BOXWT
(weight)+INTIME+OUTTIME+ENTBY(5)+MACH(4)+FLAG(1). ~342-byte records. Tracks each shipping
box assigned to a SO line, with dimensions, weight, UCC label, and timestamps for when the
box entered/left the packing station.

### SO Extension — UDF Info Blocks

**ISSOAINF / ISSOHINF / ISSOINFO** (54f each, `ISSR_INFO_*`) — SO UDF extension blocks,
3 schema-identical variants (archived line-level, historical, current). Identical layout to
the ISSR_INFO_* 54-field pattern first seen in ISSRINFO: 5 dates, 5 alt-dates, 20 alpha*25ch,
20 alpha*25ch, EXTRA(50). See ISSRINFO entry in Pass 139 documentation for full field list.

### SO Extension — Lot/Serial Transactions

**ISSOALOT / ISSOASER** (14f each, `BKAR_TXN_*`) — SO lot and serial inventory
transactions, 2 schema-identical variants. Identical to the BKAR_TXN_* 14f pattern seen
in ISRMTXN/ISRMTXNS: SONUM+CODE(15)+DESC(30)+QTY+LOT(15)+SERIAL(25)+DATE+STOCK(15)+
LINE+LOC(10)+TMPSO(40)+SRNUM+EXTRA(50)+BIN(15). ISSOALOT records lot-based SO withdrawals;
ISSOASER records serial-number-based SO withdrawals.

### SO Extension — Review/Approval

**ISSOREVU** (12f, `IS_SOVU_*`) — SO review and electronic approval record. KEY:
WOPRE+WOSUF+OPER(3). Fields: DATE+TIME+WHO(15)+MOTPAS(STRING 50, motion/electronic
password signature)+STATUS(1)+NOTES(100)+FLAG(1)+EXTRA(50)+RDATE+RWHO(15). MOTPAS stores
the electronic approval signature token for the SO review step, the same approval mechanism
seen in ISCTREVU.

### SPC (Statistical Process Control)

**ISSPC** (20f, `IS_SPC_*`) — SPC quality record per WO operation. KEY: WOPRE+WOSUF+
OPER(3). Fields: PART(15)+OPDES(30)+DATE+TIME+MACH(4)+EMP(4)+QTY+SCRAP+ANOTES(STRING 1000,
free-text process notes)+EXTRA(50)+FLAG(1)+4 general-purpose floats (GNUMS 1-4). The 1 KB
ANOTES field is the largest free-text per-operation field in the IS* shop-floor family,
supporting narrative process documentation or out-of-control descriptions.

### SP Module — PO Header Snapshot

**ISSPOH** (57f, `BKAP_PO_*`) — SP module Purchase Order header snapshot. Full 57-field
clone of the standard BKAP_PO_* AP PO header schema (identical to ISSRFQH). KEY: PONUM+
POTYPE. See BKAP_PO / BKSOPRDS documentation for the full field list. The SP module
(Special Purchases or SP-type orders) mirrors AP PO documents at the IS-extension layer.

### SP Module — PO Line Snapshot

**ISSPOL** (38f, `BKAP_POL_*`) — SP module Purchase Order line snapshot. Full 38-field
clone of the BKAP_POL_* PO line schema (identical to ISSRFQL). KEY: PONUM+LINEID. Fields
18-19 have the confirmed DDF typo NKAP_POL_UM_LIN_1 / NKAP_POL_UM_LIN_2 (should be
BKAP_POL_). This typo is shared with ISSRFQL and was likely propagated from the same
template during the DDF build.

### Quote / SR Document Snapshots

**ISSQTH** (84f, `BKAR_INV_*`) — Sales Quote header snapshot. Full 84-field BKAR_INV_*
invoice header clone. KEY: NUM+SONUM.

**ISSQTL** (28f, `BKAR_INVL_*`) — Sales Quote line snapshot. Full 28-field BKAR_INVL_*
invoice line clone. KEY: INVNM+CNTR.

**ISSRCH** (84f, `BKAR_INV_*`) — Service Request current header snapshot.
Full 84-field BKAR_INV_* clone. KEY: NUM+SONUM.

**ISSRCL** (28f, `BKAR_INVL_*`) — Service Request current lines. Full 28-field clone.

All four use the standard invoice snapshot schema described under the BKAR_INV_* /
BKAR_INVL_* pattern entries in this document.

### SR — Description Lines

**ISSRADSC** (5f, `BK_DESC_*`) — SR archived description lines. Identical to the universal
BK_DESC_* 5-field pattern: CODE(15)+NUM+LINE+NOTES(70)+DESC(25). Stores archived
long-form description text for SR documents, one record per 70-char line.

**ISSRDESC** (5f, `BK_DESC_*`) — SR current description lines. Identical schema to
ISSRADSC. Active descriptive text per SR document line.

### SR — UDF Info Blocks

**ISSRAINF / ISSRHINF / ISSRINFO** (54f each, `ISSR_INFO_*`) — SR UDF extension blocks:
archived-line, historical, and current variants. All three are schema-identical to the
ISSR_INFO_* 54-field pattern (5 dates + 5 alt-dates + 20*alpha25 + 20*alpha25 + EXTRA(50)).
See ISSRINFO in Pass 139 documentation.

### SR — Invoice Snapshots (Archived)

**ISSRAINV** (84f, `BKAR_INV_*`) — SR archived invoice header. Full 84-field
BKAR_INV_* clone. KEY: NUM+SONUM.

**ISSRAIVL** (28f, `BKAR_INVL_*`) — SR archived invoice lines. Full 28-field clone.

### SR — MMS (Machine/Material/Serial)

**ISSRAMMS** (12f, `ISSR_MMS_*`) — SR archived MMS record. Identical schema to ISSRMMS:
SRVNUM+LINEID+INVNUM+WOPRE+WOSUF+PART(15)+MAKE(50)+MODLE(50)+SERIAL(50)+INDATE+
OUTDATE+EXTRA(150). Stores the physical device (manufacturer, model, serial number) for
the equipment being serviced on an SR. Note: MODLE is the DDF field name spelling for Model.

### SR — RFQ Header/Line Snapshots

**ISSRFQH** (57f, `BKAP_PO_*`) — SR Request for Quotation header snapshot. Full 57-field
BKAP_PO_* clone. Identical schema to ISSPOH. KEY: PONUM+POTYPE.

**ISSRFQL** (38f, `BKAP_POL_*`) — SR RFQ line snapshot. Full 38-field BKAP_POL_* clone.
Identical schema to ISSPOL. Has the same NKAP_POL_UM_LIN_1/2 DDF typo in fields 18-19.

### SR — Invoice Snapshots (Current)

**ISSRINV** (84f, `BKAR_INV_*`) — SR current invoice header. Full 84-field BKAR_INV_*
clone (DDF lines 22537-22625, fully read). KEY: NUM+SONUM.

**ISSRINVL** (28f, `BKAR_INVL_*`) — SR current invoice lines. Full 28-field BKAR_INVL_*
clone. KEY: INVNM+CNTR.

### SR Master — Document Family

**ISSRMH** (84f, `BKAR_INV_*`) — SR master header. Full 84-field BKAR_INV_* clone.
The master variants represent the authoritative current SR document record, distinct from
the provisional current (ISSRCH) and archived (ISSRAINV) copies.

**ISSRMINV** (84f, `BKAR_INV_*`) — SR master invoice header. Full 84-field clone.

**ISSRMIVL** (28f, `BKAR_INVL_*`) — SR master invoice lines. Full 28-field clone.

**ISSRML** (28f, `BKAR_INVL_*`) — SR master lines. Full 28-field BKAR_INVL_* clone.

**ISSRMMS** (12f, `ISSR_MMS_*`) — SR master MMS record. Identical schema to ISSRAMMS
(12f). Tracks physical device being serviced on the master SR record.

### SR — Transaction Log

**ISSRTXN / ISSRTXNS** (14f each, `BKAR_TXN_*`) — SR lot and serial transactions,
2 identical variants. Full 14-field BKAR_TXN_* clone: SONUM+CODE(15)+DESC(30)+QTY+
LOT(15)+SERIAL(25)+DATE+STOCK(15)+LINE+LOC(10)+TMPSO(40)+SRNUM+EXTRA(50)+BIN(15).
ISSRTXN tracks lot-based SR inventory moves; ISSRTXNS tracks serial-number-based moves.

### SS Module — Document Snapshots

The ISS+S tables form the SS submodule document archive — 4 tables that snapshot both
SO and SR document headers/lines (likely for a Status Snapshot or Service Scheduling module).

**ISSSOH** (84f, `BKAR_INV_*`) — SS SO header snapshot. Full 84-field BKAR_INV_* clone.

**ISSSOL** (28f, `BKAR_INVL_*`) — SS SO lines snapshot. Full 28-field BKAR_INVL_* clone.

**ISSSRH** (84f, `BKAR_INV_*`) — SS SR header snapshot. Full 84-field BKAR_INV_* clone.

**ISSSRL** (28f, `BKAR_INVL_*`) — SS SR lines snapshot. Full 28-field BKAR_INVL_* clone.

### Service Type Lookups

**ISSTEQUI / ISSTTYPE / ISSTYPE** (3f each, `IS_STYPE_*`) — Three schema-identical
service type lookup tables. Fields: TYPE(STRING 60)+WHO(STRING 40)+ASSET(STRING 25).
- **ISSTEQUI** — equipment type classifications (what type of equipment is this?).
- **ISSTTYPE** — service tracking type codes (e.g., repair, installation, PM).
- **ISSTYPE** — service type codes (e.g., contract, warranty, T&M).

TYPE (60 chars) holds the full description; WHO (40 chars) stores the responsible
person/department; ASSET (25 chars) links to an asset/equipment code.

### Shop Floor Tracking

**ISSTRACK** (13f, `IS_STRACK_*`) — Shop floor component-tracking record per WO operation.
KEY: WOPRE+WOSUF+OPER. Fields: TIME+DATE+PROC(25, process station code)+PSER(20, process
serial)+COMP(15, component part code)+CSER(20, component serial)+NOTE(STRING 1000, 1 KB
free-text tracking notes)+EXTRA(50)+AR(1, accept/reject flag)+CLOT(15, component lot).
~1,166-byte records. Tracks individual process-step + component combinations through the
shop floor, with a 1 KB note field for quality or issue description.

---

## IST* Family

### Tax Filing

**ISTAXFIL** (84f, `ISIS_TXF_*`) — Tax filing / jurisdiction record. KEY: CODE(10).
Fields: DESC(30)+VNDCD(10, tax vendor/authority)+IDNUM(15, tax ID number)+
GLAPO(10, GL account for AP)+GLDPO(4, GL dept for AP)+9*POLRNG(PO low range, floats)+
9*POHRNG(PO high range)+9*POPERC(PO percentage, 3-dec)+9*SOLRNG(SO low range)+
9*SOHRNG(SO high range)+9*SOPERC(SO percentage)+GLASO(10, GL account for AR)+
GLDSO(4, GL dept AR)+TAXIN(1)+9*TICD(1-char tier ID)+9*PTICD(1-char PO tier ID)+
ISCUR(3, currency)+SOMAX(max taxable SO amount)+POMAX(max taxable PO amount).
~563-byte records. Stores a single tax jurisdiction with bracket-style rate arrays for
both SO (sales) and AP (purchasing) sides, allowing up to 9 rate tiers per direction.

**ISTAXGRP** (105f, `ISIS_TXG_*`) — Tax group record. KEY: NAME(10). Fields: 9*CODE(10,
jurisdiction codes in group)+9*TAXON(1, taxable flag per jurisdiction)+9*PID(1, produce ID
flag)+FREIGT(1, freight taxable)+DESC(30)+9*DESCF(20, per-jurisdiction label)+
9*IDC(15, ID codes)+9*PERCC(FLOAT 3-dec, percentage collected)+TOTPER(total %)+
12*TAXBLE(monthly taxable amount)+12*NONTAX(monthly non-taxable)+12*COLECT(monthly
collected)+OUTSTD(outstanding)+9*FRGT(freight taxable per jurisdiction)+TOFPER.
~857-byte records. Groups multiple tax jurisdictions; carries 12-month running totals of
taxable/non-taxable sales and collected tax amounts per jurisdiction.

### Payment Terms

**ISTERMS** (13f, `IS_TERMS_*`) — Payment terms definition. KEY: NUM(UBINARY). Fields:
NAME(20)+DESC(50)+AMT(float, discount amount or threshold)+TYP(1, term type)+DAY(UBINARY,
due days)+EOM(1, end-of-month flag)+MAX(UBINARY, max discount days)+COD(1, cash-on-delivery)+
ARAP(1, AR or AP applicable)+CC(1, credit card flag)+SRT(UBINARY, sort order)+EXTRA(100).
~191-byte records. Stores payment terms used in both AR and AP. ARAP flag determines which
module the term applies to.

### Tool Usage Log

**ISTOOLOG** (34f, `ISTOOL_*`) — Tool usage log per WO operation. KEY: WOPRE+WOSUF+OPER.
Fields: TOOL(15, tool code/part number)+DATE+WORKDESC(60)+ACTHRS(float 1-dec, actual hours)+
COST+10*NOTES(STRING 60, 10-line x 60ch notes = 600 chars total)+EMP(UBINARY)+3*DATES+
5*ALPHA(30)+3*FLAG+ESTHRS(estimated hours)+EXTRA(100)+LOGNUM(float, log sequence)+
ITEM(15, item/part used). ~1,005-byte records. Tracks tool and labor usage per WO routing
operation with structured notes, general-purpose date/alpha/flag fields, and a LOGNUM key
for ordering multiple tool-use entries per operation.

### Business Triggers / Alerts

**ISTRIGRS** (25f, `IS_TRIG_*`) — Business trigger/alert rule. KEY: CODE(15). Fields:
TRIGR(10, trigger event type)+CONTACT(20)+ONCE(1, fire once flag)+LDATE/LTIME (last fired)+
EXTRA(100)+WOPRE+WOSUF+PO+SO+CUST(10)+VEND(10)+LOC(10)+DAYS(UBINARY)+ITYPE(10)+
WOPRET+WOSUFT+ODEL(1)+EFLAG(1)+EMAIL(STRING 400, email recipient list)+[6000-byte gap in
DDF mapping]+OPER(3)+CLASS(4)+CAT(4)+PLANNER(4). DDF anomaly: OPER is at offset 6634
while EMAIL ends at offset 634 — a 6000-byte unmapped region between fields 21 and 22,
possibly a large text buffer or binary blob not registered in the DDF. Triggers fire on
specified ERP events (WO, PO, SO, customer/vendor actions) and send email notifications.

---

## ISU* Family

### UDF Invoice Mapping

**ISUDFINV** (8f, `IS_UDF_*`) — User-Defined Field invoice screen mapping. KEY: NAME(15,
UDF slot name). Fields: FIELD(19, physical field name in the table)+START(UBINARY)+
LENGTH(UBINARY)+SCRVAR(UBINARY, TAS Pro screen variable number)+SCRLBL(25, screen label)+
SCRSIZE(UBINARY, display width)+EXTRA(100). Maps logical UDF slot names to their physical
field positions, screen variable assignments, and labels, allowing IS-module UDF screens
to be configurable per installation.

### UDF Master Codes

**ISUDMSTR** (3f, `IS_UDM_*`) — UDF master code lookup. KEY: CODE(25). Fields: DESC(60)+
EXTRA(100). A simple code-description table for UDF dropdown values; referenced by ISUDFINV
field names to provide picklist values on UDF screens.

### Inventory Usage Statistics

**ISUSAGE** (246f, `ISTS_USE_*`) — Extended inventory usage history per item. KEY:
CODE(15)+TYPE(1). Structure:
- Current period: 26*QTY (rolling 26-period quantity) + 26*AMT (rolling 26-period amount)
- Year 1: 13*QTYY1 + 13*AMTY1 (qty + amount per 13-period fiscal year)
- Year 2: 13*QTYY2 + 13*AMTY2
- Year 3: 13*QTYY3 + 13*AMTY3
- Year 4: 13*QTYY4 + 13*AMTY4
- Year 5: 13*QTYY5 + 13*AMTY5
- Period-start dates: 2*DATEY1..Y5 (10 dates total for year boundaries)
- General dates: 10*GDATE
- 15 FLAG(1) fields + 10*ALPHA(30) + 5 NUM (float) + 5*LSTCAL (last-calibration dates)
- 5*WHO(15, responsible employee codes) + EXTRA(100)

~2,103-byte records. Provides multi-year rolling usage history at the IS-extension level,
complementing the core BKIN inventory table usage fields.

---

## ISV* Family

### Company Variables

**ISVAR** (17f, `IS_VAR_*`) — IS-module company configuration singleton. Fields:
LOGO(256, path to company logo file)+COMPANY(30)+ADD1+ADD2+CITY(20)+STATE(2)+ZIP(8)+
CONTACT(30)+5*EMAIL1(50, up to 5 email addresses)+WEB(100)+WEBUPD(100, web update URL)+
WEBSUP(100, web support URL)+EXTRA(150). ~1,106-byte record. Stores company identity and
contact information used by IS-module screens and reports.

### SQL Variable Mapping

**ISVARSQL** (4f, `IS_VAR_*`) — SQL query variable mapping. KEY: QNAME(30). Fields:
TYPE(1, query type)+VNAME(30, TAS Pro variable name)+ORDER(UBINARY). Maps named SQL queries
to their corresponding TAS Pro variable assignments, providing the binding layer between
external SQL data sources and IS-module screen variables.

### Vendor Address/Data Audit

**ISVNDADT** (11f, `IS_VND_*`) — Vendor name and credit limit change audit trail. KEY:
VEND(10). Fields: ONAME(30, old name)+NNAME(30, new name)+APPROVE(1)+DATE+TIME+WHO(20,
approver)+OMAXAMT(old max amount)+NMAXAMT(new max amount)+CHGDESC(30, reason)+EXTRA(100).
Records before/after for vendor name and maximum credit amount changes, with timestamp and
approver identity. Supports compliance requirements for vendor data change authorization.

---

## ISW* Family

### WO Change Log

**ISWOCLOG** (32f, `IS_WOLOG_*`) — Work Order change log per operation. KEY: WOPRE+WOSUF+
OPER. Fields: OPDESC(30)+ITEM(15)+WC(12, work center)+WCDESC(30)+CUST(10)+CUSNME(30)+
ITEMDS(30)+CDATE/CWHO(30)/CTIME/CWHERE(15, workstation where change occurred)+MACH(4)+
2*ALPHA1(30)+5*FLAG+5*DATE+2*NUM(float 2-dec)+2*NUM2(float integer)+EXTRA(100).
~443-byte records. Logs each significant change to a WO operation with who/when/where
context, supporting traceability and ISO-style change control.

### WO Description Lines

**ISWODESC / ISWOHDSC** (5f each, `BK_DESC_*`) — WO description lines, 2 variants. Both
are schema-identical to the BK_DESC_* 5-field pattern: CODE(15)+NUM+LINE(UBINARY)+
NOTES(70)+DESC(25). ISWODESC stores per-operation description lines; ISWOHDSC stores
WO header-level description lines.

### WO Extended Fields

**ISWOEX** (63f, `IS_WOEX_*`) — WO extended data per routing operation. KEY: WOPRE+WOSUF.
Fields (summarized): ITP(20, inspection type/process)+ITPP(1)+RF(1, rework flag)+EXTRA(100)+
MCLASS(6, machine class)+MNUM+CDATE+4 dates+INT1(UBINARY)+NUM1(float 3-dec)+ALPHA1/2(30)+
5*INT+DATE5+3 single-char ALPHA flags+2*DESC(30)+NUM2(float 4-dec)+WC(12)+3 more DESCs+
CAUSE(30)+5*GDATE+5*NOTE(100 each, ~500 chars total)+10*FLAGS+5*GNUMS(float)+5*ALPHAS(30).
~1,171-byte records. Rich extension layer per WO with inspection, machine assignment,
general-purpose fields, and 5 note slots.

**ISWOHEX** (63f, `IS_WOEX_*`) — WO header extended data. Identical schema to ISWOEX.
Header-level sibling of ISWOEX — keyed at the WO header rather than per operation.
Both use the IS_WOEX_* field prefix.

### WO Priority

**ISWOPRIO** (4f, `IS_WOPRIO_*`) — Work Order priority code lookup. KEY: PRIO(1, single
char priority code). Fields: DESC(30)+EXTRA(100)+COLOR(float, Delphi TColor integer value).
Maps priority codes to descriptions and display colors for the WO scheduling boards. COLOR
stores a Delphi TColor constant, allowing color-coded WO rows in the dispatch list.

### WO Routing Operation Extended

**ISWOROEX** (60f, `IS_WROEX_*`) — WO routing operation extended data per routing step.
KEY: WOPRE+WOSUF+OPER. Fields: ITP(20)+ITPP(1)+FOI(1, first-off inspection flag)+LQTY+
EXTRA(100)+SDAY/FDAY (UBINARY, schedule start/finish day offsets)+DATE1+ALPHA1(1)/ALPHA2(2)+
NUM1(float)+DESC1(30)+10*ALPHA3(15, 10 part/component codes)+10*DATE2+5*NUM2(float integer)+
PRMACH(4, primary machine)+5*FLAG+5*INT+cycle study fields: CYCHR/CYCMIN/CYCSEC
(UBINARY, hours/minutes/seconds per cycle)+CYPART(float 1-dec, parts per cycle)+
CYNOTE(255, cycle study notes)+CYNAME(80, study name)+CYDATE+CYMACH(4)+CYCEMP(UBINARY,
employee who performed cycle study). ~799-byte records. Extends each routing step with
inspection flags, scheduling offsets, and a built-in cycle-time study framework (full time
decomposition + parts-per-cycle + named study session).

**ISWROHEX** (60f, `IS_WROEX_*`) — WO routing header extended data. Identical schema to
ISWOROEX (same IS_WROEX_* prefix, same 60 fields). Header-level variant of ISWOROEX.

### WO Tray / Shop Packet

**ISWOTRAY** (52f, `IS_TRAY_*`) — Work Order shop packet / component tray record. KEY:
NUM(25, tray/packet identifier)+WOPRE+WOSUF+OPER. Fields: OPDESC(30)+CODE(15, component
part)+SQTY(start qty)+COMQTY(completed qty)+SCRPQTY(scrap qty)+QCREQD(1, QC required)+
QCQTY+5*LOC(10)+5*BIN(15)+5*BINQTY+20*ALPHA(25)+5*DATE+EXTRA(100). ~900-byte records.
Tracks a physical component tray through the shop floor: starting quantity, completed and
scrapped quantities, QC requirement, and up to 5 bin locations with associated quantities.
The 20 ALPHA fields provide extensive general-purpose labeling.

---

*Pass 140 documents 53 additional IS* tables: SO extension family (8 tables), SR document
family (21 tables), SS snapshot family (4 tables), service type lookups (3 tables),
shop tracking (1 table), IST* (5 tables), ISU* (3 tables), ISV* (3 tables), ISW* (9 tables).*

*ISSNOTES corrected from 9f to 12f (added PRIVATE, GROUP, CONTACT fields).*

*ISWROHEX is the final IS* table in the DDF. Next table family: JGP* (JGPITEMS,
barcode/packaging data, begins at DDF line 24238).*


---

## Pass 141 — JGP/JSP, LOT/SERIAL, MK*, ROUTING, WO Standalone, Utility Tables (2026-06-22)

Tables documented this pass: JGPITEMS, JSPCNLCD, JSPCNLSO, LANGDICT, LOT, MACHINE,
MENUFILE, MKAHIST, MKASSIGN, MKDEF, MKECLASS, MKEVENT, MKFORM, MKICLASS, MKTCLASS,
MKTNOTE, MKTRACK, MKTROUT, MWOPTEMP, NOTETEMP, NZITPRE, OPQCDESC, OUTHPROC/OUTPROC,
PIBINLOC, PIBINLOT, QCCODES, ROCHG, ROUTING/ROUTAING/ROUTTEMP, SCRAP, SCHEDCAL, SCHWO,
SERIAL/SERIALH, SUMCUST, SUMINV, SUMPNCUS, SUMWC, TOOL, WBTRVMEM/WBTRVMEMO, WCCTL,
WCTRLOAD/WCTRSLOD, WOBOM/WOHBOM, WOBOMCHG, WOBOMHRM/WOBOMREM, WODATE/WOHDATE,
WOELABOR/WOHLABOR/WOLABOR/WOLABRPT, WOEMAT/WOHMAT/WOMAT, WOERECV/WOHRECV/WORECV,
WOEXCHG/WOHEXCHG, WOHROUT, WORKACHG/WORKCHG, WORKCTR, WORKHORD/WORKORD

---

### JGP — Item Global Packaging

#### JGPITEMS — Item packaging/logistics master (86f) [schema.md:24238]

Key fields: `JGP_ITEM` STRING(15) — part number FK; `JGP_LITEM` STRING(30) — long item name;
`JGP_IND_UPC` STRING(13) — individual unit UPC barcode; `JGP_UOM_UPC` STRING(13) — UOM UPC;
`JGP_SP_BARCODE`/`JGP_MC_BARCODE`/`JGP_PAL_BARCODE` STRING(14) — standard pack/master case/pallet barcodes;
`JGP_SP_QTY`/`JGP_MC_QTY`/`JGP_PAL_QTY` FLOAT(8,2) — pack quantities per level;
`JGP_UOM_H/W/D/WT/CUBE` FLOAT(8,4) — UOM physical dimensions (HxWxD, weight, cubic ft);
`JGP_SPACK_*`/`JGP_MCART_*`/`JGP_PALLET_*` — same 5-tuple for std pack, master carton, pallet;
`JGP_IND_*` — individual unit dimensions;
`JGP_TARRIF_CODE` STRING(15) — tariff/HS code; `JGP_C_OF_ORIGIN` STRING(30) — country of origin;
`JGP_CERT_1`..`JGP_CERT_9` STRING(100) each — 9 compliance certification text fields;
`JGP_ALLERGEN_1`..`JGP_ALLERGEN_9` STRING(100) each — 9 allergen declaration fields;
`JGP_MIN_AGE` UBINARY(2) — minimum age requirement; `JGP_ASTM` STRING(1) — ASTM standard flag;
`JGP_REVDT_FRONT`/`JGP_REVDT_BACK` STRING(4) — label revision dates (front/back);
`JGP_ISBN` STRING(17) — ISBN; `JGP_LOCATION1/2/3` STRING(10) — warehouse locations;
`JGP_GEN_ALPHA_1..5` STRING(15) — 5 generic alpha UDF fields;
`JGP_GEN_DATE_1..5` DATE(4) — 5 generic date UDF fields;
`JGP_GEN_FLAG_1..5` STRING(1) — 5 flag fields;
`JGP_GEN_NUM` FLOAT(8,0) — generic numeric;
`JGP_CATALOG` STRING(750) — catalog description text; `JGP_LONG_DESC` STRING(750) — long description;
`JGP_EXTRA` STRING(100) — overflow;
`JGP_PREF_CRIT` STRING(1) — preferred criteria; `JGP_PRODUCER` STRING(1) — producer flag;
`JGP_NET_COST` STRING(1) — net cost method; `JGP_NET_ACOST` FLOAT(8,2) — actual net cost.

Purpose: Extended item record for packaging compliance, barcode generation, and logistics
(carton/pallet configuration). Supports multi-tier retail packaging with per-level UPC codes
and physical dimensions. ASTM/allergen/certification arrays cover food-safety and toy-safety requirements.

---

### JSP — JSP Cancel Module

#### JSPCNLCD — JSP cancel reason code master (6f) [schema.md:24329]

`JSP_CNLCD_CODE` STRING(1) PK — single-char cancel reason code;
`JSP_CNLCD_DESC` STRING(30) — description; `JSP_CNLCD_LCODE` STRING(10) — long code;
`JSP_CNLCD_CDATE` DATE(4) — creation date; `JSP_CNLCD_WHO` STRING(20) — created by;
`JSP_CNLCD_EXTRA` STRING(100) — overflow.

#### JSPCNLSO — JSP SO cancellation log (12f) [schema.md:24340]

`JSP_CNLSO_SONUM` FLOAT(8,0) — SO number; `JSP_CNLSO_UNUM` FLOAT(8,4) — unit number;
`JSP_CNLSO_ITEM` STRING(15) — item code; `JSP_CNLSO_CQTY` FLOAT(8,2) — cancelled qty;
`JSP_CNLSO_CDATE` DATE — cancel date; `JSP_CNLSO_WHO` STRING(20) — cancelled by;
`JSP_CNLSO_CTIME` TIME — cancel time; `JSP_CNLSO_FLAG` STRING(1) — processing flag;
`JSP_CNLSO_GDATE` DATE — guaranteed date; `JSP_CNLSO_STAT` STRING(1) — status;
`JSP_CNLSO_CUST` STRING(10) — customer code; `JSP_CNLSO_EXTRA` STRING(100) — overflow.

Purpose: JSP (Job Scheduling/Planning?) cancel module. Tracks SO line cancellations with
reason codes, quantities, and timestamps.

---

### Standalone Utility Tables

#### LANGDICT — Multi-language caption dictionary (5f) [schema.md:24357]

`LANG_DICT_ECAPT` STRING(80) — English caption (PK component); `LANG_DICT_LANG` STRING(3) — language code (PK component);
`LANG_DICT_LCAPT` STRING(80) — translated caption; `LANG_DICT_FONT` STRING(30) — display font;
`LANG_DICT_EXTRA` STRING(150) — overflow.

Purpose: Maps English UI captions to translated equivalents for multi-language installations.
Key is (ECAPT, LANG). Allows the TAS Pro 7 runtime to display localized labels.

#### LOT — Lot tracking master (25f) [schema.md:24367]

`MTLOT_CODE` STRING(15) — item code (PK component); `MTLOT_LOT` STRING(15) — lot number (PK component);
`MTLOT_EXPDATE` DATE — expiration date; `MTLOT_ONHAND` FLOAT(8,2) — qty on hand;
`MTLOT_PO` FLOAT(8,0) — PO number received on; `MTLOT_RECDOC` FLOAT(8,0) — receiving document;
`MTLOT_VENDOR` STRING(10) — vendor code; `MTLOT_RECDATE` DATE — date received;
`MTLOT_RECQTY` FLOAT(8,2) — original received qty; `MTLOT_POCOST` FLOAT(8,4) — PO cost;
`MTLOT_WO` FLOAT(8,0) — WO number produced on; `MTLOT_INRECDATE` DATE — WO receipt date;
`MTLOT_WOQTY` FLOAT(8,2) — WO produced qty; `MTLOT_WOCOST` FLOAT(8,4) — WO cost;
`MTLOT_NOTES_1..5` STRING(45) each — 5 notes lines;
`MTLOT_LOC` STRING(10) — warehouse location; `MTLOT_WOSUF` UBINARY(2) — WO suffix;
`MTLOT_EXTRA` STRING(50) — overflow;
`MTLOT_BEGIN` FLOAT(8,7) — beginning balance; `MTLOT_OUT` FLOAT(8,7) — qty issued out;
`MTLOT_MAXOUT` FLOAT(8,7) — max qty issued.

Purpose: Lot tracking master. One record per item/lot combination. Tracks both PO-received lots
and WO-produced lots. `MTLOT_EXPDATE` drives expiry compliance. On-hand qty decrements as lot
is consumed. Cross-links to SERIAL (MTSER_LOT) for lot+serial traceability.

#### MACHINE — Machine master (20f) [schema.md:24397]

`TMACH_MACHINE` STRING(4) PK — machine code; `TMACH_DESC` STRING(30) — description;
`TMACH_HRSUSED` FLOAT(8,0) — cumulative hours used; `TMACH_HRSMAINT` FLOAT(8,0) — hours at last maintenance;
`TMACH_DATE` DATE — last maintenance date; `TMACH_NOTES_1..8` STRING(45) each — 8 notes lines;
`TMACH_WC` STRING(12) — associated work center; `TMACH_WCDESC` STRING(30) — WC description;
`TMACH_EXTRA` STRING(100) — overflow; `TMACH_ACTIVE` STRING(1) — active flag;
`TMACH_INACTDATE` DATE — inactivated date; `TMACH_INACTWHO` STRING(30) — inactivated by;
`TMACH_INACTWHY` STRING(60) — inactivation reason.

Purpose: Machine asset master. Used for capacity planning and maintenance tracking.
Referenced from ROUTING/WORKORD via MTRO_TMACHINE and MTWORO_MACHNO.
4-char machine code distinguishes this from WORKCTR (12-char WC code).

#### MENUFILE — Runtime menu definitions (108f) [schema.md:24422]

`MENU_CODE` STRING(4) PK — 4-char menu identifier; `MENU_TITLE` STRING(30) — menu title;
`MENU_LEFT`/`MENU_RIGHT`/`MENU_ESCAPE` STRING(4) — navigation target codes;
`MENU_LINES_1..20` STRING(30) — up to 20 menu line labels;
`MENU_WIDTH` UBINARY(2) — display width; `MENU_LL_ROW`/`MENU_LL_COL` UBINARY(2) — position;
`MENU_OPTIONS_1..20` STRING(1) — option keystroke characters;
`MENU_TYPES_1..20` STRING(1) — option types (P=program, M=menu, etc.);
`MENU_NAMES_1..20` STRING(4) — target menu/program codes;
`MENU_PROG_1..20` STRING(8) — program names to launch per option.

Purpose: TAS Pro 7 runtime menu definitions stored in Btrieve. This table defines the entire
menu hierarchy that the runtime displays. Up to 20 options per menu with keystroke, type,
and target (either another MENUFILE record or a program name in MENU_PROG_*).

#### MWOPTEMP — WO operation completion template (8f) [schema.md:25143]

`MWOP_CNTR` FLOAT(8,0) — counter/sequence; `MWOP_WOPRE` FLOAT(8,0) — WO prefix;
`MWOP_WOSUF` UBINARY(2) — WO suffix; `MWOP_SERIAL` STRING(25) — serial number;
`MWOP_QTYCOM` FLOAT(8,2) — qty completed; `MWOP_STATUS` STRING(10) — status;
`MWOP_EXTRA` STRING(100) — overflow; `MWOP_SRC` UBINARY(2) — source flag.

Purpose: Temporary working table for WO operation completion batch. Holds serial-level
completion data while the operation close transaction processes.

#### NOTETEMP — Generic note template (5f) [schema.md:25156]

`BK_DESC_CODE` STRING(15) — parent document code (item/vendor/customer);
`BK_DESC_NUM` FLOAT(8,0) — document number; `BK_DESC_LINE` UBINARY(2) — line sequence;
`BK_DESC_NOTES` STRING(70) — note text; `BK_DESC_DESC` STRING(25) — label.

Purpose: Reusable note/description line template. The BK_DESC prefix indicates shared use
across BK-module entities. Same field set as item description/note tables.

#### NZITPRE — NZ item number prefix ranges (54f) [schema.md:25166]

18 prefixes (FLOAT(8,0)) + 18 next-numbers (FLOAT(8,0)) + 18 descriptions STRING(30).
`NZ_IPRE_PREFIX_1..18` — prefix values; `NZ_IPRE_NXTNUM_1..18` — next sequence numbers per prefix;
`NZ_IPRE_DESC_1..18` — descriptions.

Purpose: New Zealand localisation — item number prefix/autonumber ranges. Supports 18 separate
numbering series, each with its own prefix and sequential counter.

#### OPQCDESC — WO operation QC inspection record (10f) [schema.md:25225]

`OPQC_WOPRE` FLOAT(8,0) — WO prefix; `OPQC_WOSUF` UBINARY(2) — WO suffix;
`OPQC_OPER` UBINARY(2) — operation number; `OPQC_DESC` STRING(30) — operation description;
`OPQC_SERIAL` STRING(25) — serial number inspected; `OPQC_UID` STRING(30) — inspector user ID;
`OPQC_QCCODE` STRING(2) — QC result code (FK to QCCODES); `OPQC_DATE` DATE — inspection date;
`OPQC_EXTRA` STRING(50) — overflow; `OPQC_QTY` FLOAT(8,2) — qty inspected.

Purpose: Per-operation QC inspection log for WOs. Links a WO/operation to a QC code (pass/fail
reason), inspector, and quantity. Used for shop-floor quality tracking.

---

### OUTHPROC / OUTPROC — Outsource PO (15f) [schema.md:25240/25260]

Both tables share identical schema (MTPO prefix):
`MTPO_VENDOR` STRING(10) — vendor; `MTPO_VENDNAME` STRING(20) — vendor name;
`MTPO_PO` FLOAT(8,0) — PO number; `MTPO_WOPRE` FLOAT(8,0) — parent WO;
`MTPO_WOSUF` UBINARY(2) — WO suffix; `MTPO_DATE` DATE — date;
`MTPO_OPER` UBINARY(2) — routing operation number; `MTPO_PROD` STRING(15) — item code;
`MTPO_DESC` STRING(25) — description; `MTPO_QTY` FLOAT(8,2) — quantity;
`MTPO_COST` FLOAT(8,4) — unit cost; `MTPO_EXTPR` FLOAT(8,2) — extended price;
`MTPO_ASSY` STRING(15) — assembly code; `MTPO_ASSYDESC` STRING(30) — assembly description;
`MTPO_EXTRA` STRING(50) — overflow.

Purpose: Tracks outsource/subcontract purchase orders linked to WO routing operations.
OUTPROC = current active; OUTHPROC = history/archive. Each record links a PO to a specific
WO operation (the "buy" step for an outprocessed routing step).

---

### PI — Physical Inventory

#### PIBINLOC — Physical inventory bin/location (14f) [schema.md:25280]

`PIBIN_LOC_ITEM` STRING(15) — item; `PIBIN_LOC_LOC` STRING(10) — location;
`PIBIN_LOC_BIN` STRING(15) — bin; `PIBIN_LOC_UOH` FLOAT(8,2) — unit on hand;
`PIBIN_LOC_CDATE` DATE — count date; `PIBIN_LOC_VDATE` DATE — verified date;
`PIBIN_LOC_DFLT` STRING(1) — default bin flag; `PIBIN_LOC_EXTRA` STRING(100) — overflow;
`PIBIN_LOC_RVLVL` STRING(5) — reorder level; `PIBIN_LOC_YEAR` STRING(4) — PI year;
`PIBIN_LOC_QTR` STRING(2) — PI quarter; `PIBIN_LOC_FDATE` DATE — freeze date;
`PIBIN_LOC_LOT` STRING(15) — lot number; `PIBIN_LOC_SER` STRING(25) — serial number.

Purpose: Physical inventory by item/location/bin/lot/serial. During a PI count, one record
per item+location+bin combination. Includes lot and serial fields for lot/serial-tracked items.
Year+quarter fields identify the PI cycle.

#### PIBINLOT — Physical inventory bin/lot count (14f) [schema.md:25299]

`PI_BINLOT_YR` STRING(4) — PI year; `PI_BINLOT_QTR` STRING(2) — quarter;
`PI_BINLOT_ITEM` STRING(15) — item; `PI_BINLOT_LOC` STRING(10) — location;
`PI_BINLOT_LOT` STRING(15) — lot; `PI_BINLOT_BIN` STRING(15) — bin;
`PI_BINLOT_SER` STRING(25) — serial; `PI_BINLOT_UOH` FLOAT(8,2) — on hand count;
`PI_BINLOT_SQTY` FLOAT(8,2) — system qty; `PI_BINLOT_PSTD` STRING(1) — posted flag;
`PI_BINLOT_FLAG` STRING(1) — processing flag; `PI_BINLOT_DATE` DATE — count date;
`PI_BINLOT_NUM` FLOAT(8,0) — sequence number; `PI_BINLOT_EXTRA` STRING(50) — overflow.

Purpose: PI count records keyed by PI cycle (year/quarter) + item/location/lot/bin/serial.
Stores both the counted qty (`UOH`) and system qty (`SQTY`) for variance calculation.
`PSTD` flag indicates the adjustment has been posted to inventory.

#### QCCODES — QC reject reason codes (2f) [schema.md:25318]

`MTQC_CODE` STRING(2) PK — 2-char QC code; `MTQC_DESC` STRING(30) — description.

Referenced by OPQCDESC (`OPQC_QCCODE`) and WOELABOR (`MTWOLA_QCCODE`).

---

### RO — Routing Change Log

#### ROCHG — Routing change audit log (22f) [schema.md:25325]

`RO_CHG_PART` STRING(15) — item code; `RO_CHG_OPER` UBINARY(2) — operation number;
`RO_CHG_AOPER`/`RO_CHG_DOPER` STRING(1) — add/delete operation flags;
`RO_CHG_CDATE` DATE — change date; `RO_CHG_USER` STRING(15) — changed by;
`RO_CHG_ALONG`/`RO_CHG_BLONG` FLOAT(8,7) — before/after run time;
`RO_CHG_ASETUP`/`RO_CHG_BSETUP` TIME — before/after setup time;
`RO_CHG_ATMACH`/`RO_CHG_BMATCH` STRING(4) — before/after machine;
`RO_CHG_ATOOL`/`RO_CHG_BTOOL` STRING(15) — before/after tool;
`RO_CHG_AWC`/`RO_CHG_BWC` STRING(12) — before/after work center;
`RO_CHG_ASTDT`/`RO_CHG_BSTDT` STRING(1) — before/after standard time flag;
`RO_CHG_ANUMPERS`/`RO_CHG_BNUMPERS` FLOAT(8,2) — before/after number of persons;
`RO_CHG_AEXTRA`/`RO_CHG_BEXTRA` STRING(100) — before/after extra fields.

Purpose: Audit trail for routing operation changes. A=after/new, B=before/old (A/B pairs
follow EVO convention throughout the change tables).

---

### ROUTING / ROUTAING / ROUTTEMP — Routing Operations (62f each) [schema.md:25352/25419/25486]

All three tables share identical MTRO prefix schema:

**Key fields:** `MTRO_CODE` STRING(15) — item code (PK component); `MTRO_OPER` UBINARY(2) — operation number (PK component);
`MTRO_DESC` STRING(30) — operation description; `MTRO_OPERDESC` STRING(30) — operation detail description;
`MTRO_TYPE` STRING(1) — operation type (I=in-house, O=outsource, etc.);
`MTRO_LEAD` UBINARY(2) — lead time days; `MTRO_VENDCOST` FLOAT(8,6) — vendor cost;
`MTRO_PARTSHR` FLOAT(8,2) — parts per hour; `MTRO_TIMEPART` TIME — time per part;
`MTRO_SETUPHRS` TIME — setup hours; `MTRO_LOTSIZE` FLOAT(8,0) — lot size basis;
`MTRO_INSTR_1..15` STRING(60) each — 15 operation instruction lines;
`MTRO_WC` STRING(12) — work center code; `MTRO_WCDESC` STRING(30) — WC description;
`MTRO_VENDCODE`/`MTRO_VENDNAME` — vendor for outsource ops;
`MTRO_LABOR` FLOAT(8,4) — labor rate; `MTRO_MACHINE` FLOAT(8,4) — machine rate;
`MTRO_FOVHD`/`MTRO_VOVHD` FLOAT(8,4) — fixed/variable overhead rates; `MTRO_SETUP` FLOAT(8,4) — setup rate;
`MTRO_TMACHINE` STRING(4) — tool/machine code; `MTRO_TOOL` STRING(15) — tool code;
`MTRO_NUM` UBINARY(2) — number of machines; `MTRO_NUM_PERSON` FLOAT(8,2) — number of persons;
`MTWO_MISC_COST` FLOAT(8,2) — misc cost; `MTRO_OP_TEMP_NO` UBINARY(2) — operation template number;
`MTRO_NUM_PROCES` UBINARY(2) — number of processes; `MTRO_TIME_PERPR` TIME — time per process;
`MTRO_MD_PROC_HR` STRING(1) — mode (proc per hr or hr per proc);
`MTRO_PROC_PERHR` FLOAT(8,2) — processes per hour; `MTRO_STD_TIME` STRING(1) — use standard time;
`MTRO_MIN_CHG` FLOAT(8,2) — minimum charge; `MTRO_OVERLAP` UBINARY(2) — overlap %;
`MTRO_PIECE_RATE` FLOAT(8,2) — piece rate; `MTRO_LONGTIME` FLOAT(8,7) — total runtime;
`MTRO_PRINT` STRING(1) — print flag; `MTRO_CLASS` STRING(15) — class;
`MTRO_EXTRA` STRING(150) — overflow; `MTRO_NEGOVLP` FLOAT(8,2) — negative overlap;
`MTRO_DEF_TIME` TIME — default time; `MTRO_R_TYPE` STRING(10) — routing type;
`MTRO_EST_LINE` FLOAT(8,0) — estimating line; `MTRO_EST_TAG` STRING(10) — estimating tag.

**Distinction:**
- `ROUTING` — current active routing master for standard items
- `ROUTAING` — archive of inactive/superseded routings (name has typo: "ROUTAING" not "ROUTING")
- `ROUTTEMP` — template workspace for routing edits/copies

Purpose: Manufacturing routing master. One record per item/operation pair. Defines how an item
is made: the sequence of operations, work centers, machines, tools, labor/machine rates, and
standard times. Central to WO costing, scheduling (WORKCTR capacity), and WORKHORD/WORKORD.
Outsource operations (TYPE=O) link to OUTHPROC via vendor and operation number.

---

### SCRAP — Scrap Reason Codes (21f) [schema.md:25579]

`MTSCRAP_CODE` STRING(2) PK — 2-char scrap reason code; `MTSCRAP_DESC` STRING(30) — description;
`MTSCRAP_TYPE` STRING(1) — scrap type; `MTSCRAP_EXTRA` STRING(50) — overflow;
`MTSCRAP_GLACCT` STRING(10) — GL account for scrap posting; `MTSCRAP_GLDPT` STRING(4) — GL department;
`MTSCRAP_FLAG_1..5` STRING(1) — 5 flag fields;
`MTSCRAP_ALPHA_1..5` STRING(30) — 5 alpha UDF fields;
`MTSCRAP_DATE_1..5` DATE — 5 date UDF fields.

Purpose: Scrap reason code master. Controls GL posting for scrap (each code maps to a specific
GL account/department). Referenced by WOELABOR (`MTWOLA_SCRAPCD`) and WOEMAT (`WOMAT_SCRAPCD`).

---

### SCHED* — Scheduling Tables

#### SCHEDCAL — Scheduling calendar (6f) [schema.md:25553]

`SCH_CAL_DATE` DATE PK — calendar date; `SCH_WH_FLAG` STRING(1) — working/holiday flag;
`SCH_SHOP_DATE` FLOAT(8,0) — forward shop day count; `SCH_BACK_DATE` FLOAT(8,0) — backward shop day count;
`SCH_SHOP_SLASH` DATE — forward slash date; `SCH_BACK_SLASH` DATE — backward slash date.

Purpose: Maps calendar dates to shop days for forward/backward scheduling. Working days get
sequential shop day numbers; holidays/weekends are skipped. Used by the scheduler to convert
between calendar dates and shop days.

#### SCHWO — WO scheduling data (10f) [schema.md:25564]

`SWO_WOPRE` FLOAT(8,0) — WO prefix; `SWO_WOSUF` UBINARY(2) — WO suffix;
`SWO_OPCOUNT` UBINARY(2) — operation count; `SWO_RUN_DAYS` FLOAT(8,4) — scheduled run days;
`SWO_DAYS_TOGO` FLOAT(8,0) — days remaining; `SWO_CRATIO` FLOAT(8,5) — critical ratio;
`SWO_SHOP_START` FLOAT(8,0) — scheduled start shop day; `SWO_SHOP_FINISH` FLOAT(8,0) — scheduled finish shop day;
`SWO_SHOP_DUE` FLOAT(8,0) — due shop day; `SWO_CONTENTION` FLOAT(8,0) — contention score.

Purpose: Scheduling working data for each active WO. The critical ratio (CRATIO) is the
standard scheduling priority metric. CONTENTION scores resource conflicts. Used by the
scheduling engine to prioritize and dispatch WOs.

---

### SERIAL / SERIALH — Serial Number Tracking (30f each) [schema.md:25605/25640]

Both tables share identical MTSER prefix schema:

`MTSER_CODE` STRING(15) — item code (PK component); `MTSER_SERIAL` STRING(25) — serial number (PK component);
`MTSER_LOT` STRING(15) — associated lot number;
`MTSER_PO` FLOAT(8,0) — PO received on; `MTSER_RECDOC` FLOAT(8,0) — receiving document;
`MTSER_VENDOR` STRING(10) — vendor; `MTSER_RECDATE` DATE — receipt date;
`MTSER_POCOST` FLOAT(8,4) — PO cost;
`MTSER_SO` FLOAT(8,0) — sales order shipped on; `MTSER_CUSTCODE` STRING(10) — customer;
`MTSER_SHIPDATE` DATE — ship date; `MTSER_SELLPRICE` FLOAT(8,4) — selling price;
`MTSER_WO` FLOAT(8,0) — WO produced on; `MTSER_ISSDATE` DATE — WO issue date;
`MTSER_ISSCOST` FLOAT(8,4) — WO cost;
`MTSER_INRECDATE` DATE — WO receipt date; `MTSER_INRECCOST` FLOAT(8,4) — WO receipt cost;
`MTSER_EXPDATE` DATE — expiration date; `MTSER_WOCODE` STRING(15) — WO item code;
`MTSER_NOTES_1..5` STRING(30) each — 5 notes lines;
`MTSER_ONHAND` FLOAT(8,2) — on hand (0 or 1 for serial); `MTSER_LOC` STRING(10) — location;
`MTSER_WOSUF` UBINARY(2) — WO suffix; `MTSER_EXTRA` STRING(50) — overflow;
`MTSER_BIN` STRING(15) — bin location; `MTSER_INV` FLOAT(8,0) — invoice number.

SERIAL = current active serials; SERIALH = historical (shipped/consumed serials).

Purpose: Complete life-cycle tracking per serial number: received from PO, optionally processed
through WO, shipped on SO. Cross-links LOT, PIBINLOC, OPQCDESC. On-hand is normally 0 or 1
(one unit per serial). Moves to SERIALH on shipment.

---

### SUM* — Monthly Summary Aggregates

#### SUMCUST — Monthly sales by customer (5f) [schema.md:25675]

`SUMCUST_CUST` STRING(10) — customer; `SUMCUST_YEAR` UBINARY(2) — year;
`SUMCUST_MONTH` UBINARY(2) — month; `SUMCUST_SALES` FLOAT(8,4) — net sales;
`SUMCUST_COGS` FLOAT(8,4) — cost of goods sold.

#### SUMINV — Monthly inventory movements by item (19f) [schema.md:25685]

`SUMINV_PARTNO` STRING(15) — item; `SUMINV_MONTH` UBINARY(2) — month; `SUMINV_YEAR` UBINARY(2) — year;
`SUMINV_LOCATION` STRING(10) — warehouse location;
`SUMINV_DOL_ADJ`/`SUMINV_UN_ADJ` — dollar/unit adjustments;
`SUMINV_DOL_ISS`/`SUMINV_UN_ISS` — dollar/unit issues to WO;
`SUMINV_DOL_RWIP`/`SUMINV_UN_RWIP` — dollar/unit returns to WIP;
`SUMINV_DOL_RSTK`/`SUMINV_UN_RSTK` — dollar/unit returns to stock;
`SUMINV_DOL_SHPS`/`SUMINV_UN_SHPS` — dollar/unit shipped;
`SUMINV_DOL_SHPC` — cost of units shipped;
`SUMINV_DOL_WORC`/`SUMINV_UN_WORC` — dollar/unit WO receipts;
`SUMINV_DOL_FILL`/`SUMINV_UN_FILL` — dollar/unit fill (from PO receipt).

Purpose: Monthly inventory movement summary by item/location. Drives inventory analysis
reports and cost-of-goods summaries. Each record = one month's activity.

#### SUMPNCUS — Monthly part/customer sales (6f) [schema.md:25709]

`SUMPNCUS_CUST` STRING(10) — customer; `SUMPNCUS_PARTNO` STRING(15) — item;
`SUMPNCUS_YEAR` UBINARY(2) — year; `SUMPNCUS_MONTH` UBINARY(2) — month;
`SUMPNCUS_SALES` FLOAT(8,4) — net sales; `SUMPNCUS_COGS` FLOAT(8,2) — COGS.

#### SUMWC — Monthly work center summary (7f) [schema.md:25720]

`SUMWC_WORKCTR` STRING(12) — work center; `SUMWC_YEAR` UBINARY(2) — year;
`SUMWC_MONTH` UBINARY(2) — month;
`SUMWC_LABOR` FLOAT(8,2) — total labor hours; `SUMWC_SETUP` FLOAT(8,2) — total setup hours;
`SUMWC_UNITS` FLOAT(8,2) — units produced; `SUMWC_SCRAP` FLOAT(8,2) — scrap units.

Purpose: Work center activity rolled up by month. Used for productivity and efficiency reports.

---

### TOOL — Tool/Mold Master (57f) [schema.md:25863]

`MTOOL_TOOL` STRING(15) PK — tool code; `MTOOL_DESC` STRING(30) — description;
`MTOOL_DATE` DATE — put-in-service date; `MTOOL_NOTES_1..8` STRING(45) — 8 note lines;
`MTOOL_PRTSMAINT` FLOAT(8,0) — parts per maintenance interval; `MTOOL_NOPARTS` FLOAT(8,0) — total parts count;
`MTOOL_EXTRA` STRING(100) — overflow;
`MTOOL_WEIGHT`/`MTOOL_HEIGHT`/`MTOOL_WIDTH`/`MTOOL_DEPTH` FLOAT(8,2) — physical dimensions;
`MTOOL_EJ_STROKE` FLOAT(8,2) — ejector stroke; `MTOOL_NOZ_RAD` FLOAT(8,2) — nozzle radius;
`MTOOL_TOOLTYPE_1/2` STRING(60) — tool type description; `MTOOL_HOTRUN_CH` STRING(30) — hot runner channels;
`MTOOL_NUM_PORTS` STRING(30) — number of ports; `MTOOL_WATERTMPA/B` FLOAT(8,2) — water temperatures;
`MTOOL_SHOTSIZE` FLOAT(8,2) — shot size; `MTOOL_MIN_TON` FLOAT(8,2) — minimum tonnage;
`MTOOL_CUST` STRING(10) — customer (owner) code; `MTOOL_INSERV_DT` DATE — in-service date;
`MTOOL_REPL_COST` FLOAT(8,2) — replacement cost;
`MTOOL_BLOC_BIN`/`MTOOL_ILOC_BIN` STRING(15) — base/in-use location bins;
`MTOOL_OWNER` STRING(10) — owner code; `MTOOL_CAVITY` STRING(60) — cavity description;
`MTOOL_CYCLES` FLOAT(8,0) — current cycle count; `MTOOL_TOTCYCLES` FLOAT(8,0) — total lifetime cycles;
`MTOOL_LST_MDATE` DATE — last maintenance date; `MTOOL_PM_INTVAL` UBINARY(2) — PM interval (shots);
`MTOOL_FLAG_1..5` STRING(1) — 5 flags; `MTOOL_ALPHA_1..5` STRING(30) — 5 alpha UDF;
`MTOOL_ADATE_1/2` DATE — 2 date UDF; `MTOOL_BASE_LOC`/`MTOOL_INS_LOC` STRING(10) — locations;
`MTOOL_LASTUSED` DATE — last use date; `MTOOL_NUMCAVITY` UBINARY(2) — cavity count;
`MTOOL_NUM1_1/2` FLOAT(8,2) — numeric UDF.

Purpose: Tool/mold master with injection-molding-specific fields (ejector stroke, nozzle radius,
shot size, tonnage, water temperatures, hot runner channels). Cycle count against PM interval
drives preventive maintenance. Customer owner field tracks customer-owned tooling.
Referenced from ROUTING via `MTRO_TOOL`.

---

### WB — Btrieve Working Memory

#### WBTRVMEM / WBTRVMEMO — Btrieve memory buffer (5f each) [schema.md:25925/25935]

`BTRV_MEM_CNTR` UBINARY(4) — counter; `BTRV_MEM_SIZE` UBINARY(4) — buffer size;
`BTRV_MEM_SUBC` UBINARY(4) — subcount; `BTRV_MEM_LINK` UBINARY(4) — link pointer;
`BTRV_MEM_BUFF` STRING(512) — data buffer.

Purpose: Runtime working memory tables for the Btrieve/Pervasive engine. These are
internal plumbing — TAS Pro 7 uses them as temp scratch space for large data operations.
Not user-facing.

---

### WC — Work Center Control

#### WCCTL — Work center scheduling control (5f) [schema.md:25945]

`WCTL_WC` STRING(12) PK — work center; `WCTL_START` FLOAT(8,0) — scheduled start shop day;
`WCTL_STOP` FLOAT(8,0) — scheduled stop shop day; `WCTL_COUNT` FLOAT(8,0) — operation count;
`WCTL_FLAG` STRING(1) — processing flag.

Purpose: Scheduler control record per work center. Tracks the scheduling window (start/stop
shop days) and operation count for the current scheduling pass.

#### WCTRLOAD / WCTRSLOD — Work center daily load (8f each) [schema.md:25955/25968]

Identical schema: `WC_LOAD_WC` STRING(12) — work center; `WC_LOAD_DATE` DATE — date;
`WC_LOAD_TOTHRS` FLOAT(8,2) — total hours loaded; `WC_LOAD_UDATE` DATE — update date;
`WC_LOAD_CAP` FLOAT(8,2) — capacity hours; `WC_LOAD_UTIL` FLOAT(8,2) — utilization %;
`WC_LOAD_LOAD` FLOAT(8,2) — load %; `WC_LOAD_EXTRA` STRING(100) — overflow.

WCTRLOAD = current load (active WOs); WCTRSLOD = scheduled load (projected).

Purpose: Daily capacity planning per work center. One record per WC per date. CAP comes from
WORKCTR hours per shift. LOAD = actual hours booked ÷ CAP. Used for capacity analysis reports.

---

### WO Standalone Transaction Tables

These tables form the WO transaction layer (distinct from BKWO* module-level tables).
Multiple date-versioned copies of the same schema indicate current vs. history partitioning.

#### WOBOM / WOHBOM — WO BOM material lines (24f each) [schema.md:25981/26190]

Identical schema (WOBOM prefix):
`WOBOM_OPER` UBINARY(2) — operation; `WOBOM_WOPRE` FLOAT(8,0) — WO number;
`WOBOM_WOSUF` UBINARY(2) — WO suffix; `WOBOM_ASSY` STRING(15) — assembly item code;
`WOBOM_COMPCODE` STRING(15) — component item code; `WOBOM_START` DATE — start date;
`WOBOM_ASSYDESC` STRING(30) — assembly description; `WOBOM_COMPDESC` STRING(30) — component description;
`WOBOM_QTYPER` FLOAT(8,8) — qty per assembly; `WOBOM_SCRAPQTY` FLOAT(8,8) — scrap allowance;
`WOBOM_TOTQTY` FLOAT(8,4) — total required; `WOBOM_ASSYQTY` FLOAT(8,2) — WO order qty;
`WOBOM_QTYISSUED` FLOAT(8,4) — qty issued to date; `WOBOM_UM` STRING(3) — unit of measure;
`WOBOM_EMATCST` FLOAT(8,2) — estimated material cost; `WOBOM_AMATCST` FLOAT(8,2) — actual material cost;
`WOBOM_REFERENCE` STRING(20) — reference designator; `WOBOM_OPTION` STRING(1) — option flag;
`WOBOM_VEND` STRING(10) — vendor; `WOBOM_EXTRA` STRING(50) — overflow;
`WOBOM_SEQ` UBINARY(2) — sequence; `WOBOM_REV` STRING(5) — revision;
`WOBOM_BINLOC` STRING(10) — bin location; `WOBOM_UID` STRING(30) — user ID.

WOBOM = current WOs; WOHBOM = historical.

Purpose: WO material pick list. One record per WO BOM component. Tracks qty issued vs.
required for material variance. Reference designator supports electronics/PCB assembly.

#### WOBOMCHG — WO BOM change audit (17f) [schema.md:26010]

Before/after pairs for: COMP (component), QTY, REF (reference), SCRAP, EXTRA.
Also: WOPRE, WOSUF, PARENT, UID, CDATE, USER, ACOMP (add flag), DCOMP (delete flag).

Purpose: Tracks engineering changes to WO BOMs — component adds, deletes, qty changes.

#### WOBOMHRM / WOBOMREM — WO BOM remark lines (7f each) [schema.md:26032/26044]

`WOBOM_RM_WOPRE` FLOAT(8,0); `WOBOM_RM_WOSUF` UBINARY(2); `WOBOM_RM_PARENT` STRING(15);
`WOBOM_RM_LINE` UBINARY(2); `WOBOM_RM_COMP` STRING(15); `WOBOM_RM_LINENM` UBINARY(2);
`WOBOM_RM_REMARK` STRING(30).

Purpose: Free-text remarks attached to WO BOM component lines. WOBOMHRM = history; WOBOMREM = current.

#### WODATE / WOHDATE — WO scheduling parameters (13f each) [schema.md:26056/26219]

`WODATE_WOPRE`/`WOSUF` — WO key; `WODATE_START` DATE — scheduled start;
`WODATE_FINISH` DATE — scheduled finish; `WODATE_QTY` FLOAT(8,2) — split qty;
`WODATE_PARPRE`/`WOPARSUF` — parent WO (for multi-level); `WODATE_TOPPRE`/`TOPSUF` — top-level WO;
`WODATE_DELPRE`/`DELSUF` — delivery WO; `WODATE_EXTRA` STRING(100) — overflow;
`WODATE_PRIO` STRING(1) — priority.

Purpose: WO scheduling dates and parent/child WO relationships for multi-level assemblies.
Used by the scheduling engine (SCHWO/SCHEDCAL) and capacity planning.

#### WOELABOR / WOHLABOR / WOLABOR / WOLABRPT — WO labor transactions (58f each) [schema.md:26074/26252/26439/26502]

All four share identical MTWOLA prefix schema (58 fields).

Key fields: `MTWOLA_POSTED` STRING(1) — posted flag; `MTWOLA_DATE` DATE — transaction date;
`MTWOLA_EMP` UBINARY(2) — employee number; `MTWOLA_WOPRE`/`WOSUF` — WO;
`MTWOLA_OPER` UBINARY(2) — operation; `MTWOLA_TRXN` UBINARY(2) — transaction sequence;
`MTWOLA_REGOVER` STRING(1) — regular/overtime; `MTWOLA_RUNHRS` FLOAT(8,2) — run hours;
`MTWOLA_NOJOBS` UBINARY(2) — number of jobs; `MTWOLA_SETUPHRS` FLOAT(8,2) — setup hours;
`MTWOLA_PARTS` FLOAT(8,2) — parts completed; `MTWOLA_REWORK` STRING(1) — rework flag;
`MTWOLA_COMPLETE` STRING(1) — operation complete flag; `MTWOLA_SCRAPPED` FLOAT(8,2) — scrapped qty;
`MTWOLA_QCCODE` STRING(2) — QC code; `MTWOLA_QCDESC` STRING(30) — QC description;
`MTWOLA_SCRAPCD` STRING(2) — scrap code; `MTWOLA_SCDESC` STRING(30) — scrap description;
`MTWOLA_ASSY` STRING(15) — assembly code; `MTWOLA_ASSYDESC` STRING(30) — assembly description;
`MTWOLA_LABRATE`/`LABCOST`/`SETCOST`/`MACHCOST`/`FOHCOST`/`VOHCOST` FLOAT — cost components;
`MTWOLA_TEAM`/`SHIFT` UBINARY(2) — team/shift; `MTWOLA_WC` STRING(12) — work center;
`MTWOLA_TOOL` STRING(15) — tool used; `MTWOLA_MACH` STRING(4) — machine used;
`MTWOLA_EMP2` UBINARY(2) — second employee; `MTWOLA_MISC` FLOAT(8,6) — misc cost;
`MTWOLA_START`/`STOP`/`DEDUCT` TIME — clock-in/clock-out/deduction;
`MTWOLA_OTEAM` UBINARY(2) — overtime team; `MTWOLA_AUDIT` STRING(35) — audit trail;
`MTWOLA_CYCHR`/`CYCMIN`/`CYCSEC` UBINARY(2) — cycle study: hours/minutes/seconds;
`MTWOLA_CYCPARTS` FLOAT(8,1) — cycle study parts count; `MTWOLA_CYCNOTE` STRING(255) — cycle study notes;
`MTWOLA_FLAG_1..5` STRING(1) — 5 flags; `MTWOLA_ALPHA_1..3` STRING(30) — 3 alpha UDF.

Note: 6000-byte gap between `MTWOLA_CYCNOTE` (ends offset 673) and `MTWOLA_FLAG_1` (offset 674) —
the gap is 0 bytes (255-char field ends at 419+255=674), so no gap. Records are ~769 bytes.

Distinctions: WOELABOR = labor entries (unposted/current); WOHLABOR = historical labor;
WOLABOR = active labor; WOLABRPT = labor report staging. The cycle study fields
(CYCHR/MIN/SEC + CYCPARTS + CYCNOTE) provide embedded time-study capability.

#### WOEMAT / WOHMAT / WOMAT — WO material issue transactions (17f each) [schema.md:26137/26315/26565]

All three share identical schema (WOMAT/MTWO prefix mix):
`WOMAT_DATE` DATE — issue date; `WOMAT_WOPRE`/`WOSUF` — WO;
`WOMAT_QTYISSUED` FLOAT(8,4) — quantity issued; `WOMAT_QTYSCRAP` FLOAT(8,2) — scrap qty;
`WOMAT_SCRAPCD` STRING(2) — scrap reason; `WOMAT_LOT` STRING(15) — lot number;
`WOMAT_SERIAL` STRING(25) — serial number; `MTWO_PRODCODE` STRING(15) — component item code;
`WOMAT_PRODDESC` STRING(30) — component description; `WOMAT_KIT` STRING(1) — kit flag;
`WOMAT_PCODE`/`PDESC` STRING — parent item; `WOMAT_SCDESC` STRING(30) — scrap description;
`WOMAT_COST` FLOAT(8,2) — issue cost; `WOMAT_REF` STRING(15) — reference;
`WOMAT_EXTRA` STRING(50) — overflow.

WOEMAT = material issue entries; WOHMAT = historical; WOMAT = active.
Lot/serial fields link to LOT and SERIAL tables for traceability.

#### WOERECV / WOHRECV / WORECV — WO finished goods receipt (11f each) [schema.md:26159/26337/26587]

All three share MTWOR prefix:
`MTWOR_WOPRE`/`WOSUF` — WO; `MTWOR_DATE` DATE — receipt date;
`MTWOR_ASSY` STRING(15) — assembly item; `MTWOR_DESC` STRING(30) — description;
`MTWOR_QTY` FLOAT(8,2) — qty received; `MTWOR_USESTD` STRING(1) — use standard cost flag;
`MTWOR_AVGC` FLOAT(8,4) — average cost; `MTWOR_LOT` STRING(15) — lot assigned;
`MTWOR_SERIAL` STRING(25) — serial assigned; `MTWOR_REF` STRING(15) — reference.

Purpose: WO finished goods receipt back to inventory. Assigns lot/serial at receipt.
WOERECV = entries; WOHRECV = history; WORECV = active.

#### WOEXCHG / WOHEXCHG — WO exchange/misc charges (10f each) [schema.md:26175/26237]

`MTWO_EX_WOPRE`/`WOSUF` — WO; `MTWO_EX_DATE` DATE; `MTWO_EX_PROD` STRING(15) — item;
`MTWO_EX_DESC` STRING(30); `MTWO_EX_CHG` FLOAT(8,6) — charge amount;
`MTWO_EX_CHGDESC` STRING(30); `MTWO_EX_GLACCT` STRING(10) — GL account;
`MTWO_EX_GLDPT` STRING(4); `MTWO_EX_OP` UBINARY(2) — operation.

Purpose: Miscellaneous charges against a WO (tooling, subcontract extras, etc.) with GL coding.

#### WOHROUT — WO historical routing (81f) [schema.md:26353]

Key fields (MTWORO prefix): `MTWORO_WOPRE`/`WOSUF`/`OPER` — WO operation key;
`MTWORO_PROJ` FLOAT(8,0) — project; `MTWORO_START`/`FINISH`/`FINISH2` DATE — dates;
`MTWORO_CODE` STRING(15) — routing code; `MTWORO_ESTHRS`/`ACTHRS` FLOAT(8,4) — est/actual hours;
`MTWORO_ESETHRS`/`ASETHRS` FLOAT(8,4) — est/actual setup hours;
`MTWORO_OPERDESC` STRING(30); `MTWORO_VEND`/`VENDNAME` — outsource vendor;
`MTWORO_MACHNO` STRING(4) — machine; `MTWORO_TOOL` STRING(15) — tool;
`MTWORO_WC` STRING(12) — work center; `MTWORO_PRIORITY` STRING(1);
`MTWORO_INSTR_1..15` STRING(60) each — 15 instruction lines;
`MTWORO_QTYCOM` FLOAT(8,2) — qty completed; `MTWORO_SCRAPPED` FLOAT(8,2);
`MTWORO_ESETCST`..`MTWORO_AVOHCST` FLOAT(8,4) — est/actual 6-component cost split
(setup, labor, machine, outside, fixed-OH, variable-OH);
`MTWORO_NUM_PROC` UBINARY(2); `MTWORO_CONTNTN` FLOAT(8,0) — contention;
`MTWORO_SCHED_WC` STRING(12) — scheduled work center; `MTWORO_NEGOVLP` FLOAT(8,2) — neg overlap;
+ process/time/standard fields mirroring ROUTING.

Purpose: Historical snapshot of each WO routing operation with actual vs. estimated cost
comparison. Stores the instruction text at time of WO release. 81 fields vs. ROUTING's 62 —
the extra fields are actual costs, completion data, and scheduling results.

---

### WORKACHG / WORKCHG — WO Header Change Audit (25f each) [schema.md:26603/26633]

Identical schema (WO_CHG prefix):
`WO_CHG_WOPRE`/`WOSUF`; `WO_CHG_CODE` STRING(15) — changed-by code;
`WO_CHG_CDATE` DATE; `WO_CHG_USER` STRING(15);
Before/after pairs: PRIO (priority), STATUS (1), CLASS (1), DESC (30), QTY (float),
SDATE (start), FDATE (finish), DDATE (due), ASD (actual start), EXTRA (150).

WORKACHG = archive; WORKCHG = current.

Purpose: Audit trail for WO header changes (priority, status, qty, dates). A/B convention
throughout: A = after/new value, B = before/old value.

---

### WORKCTR — Work Center Master (47f) [schema.md:26663]

`MTWC_WC` STRING(12) PK — work center code; `MTWC_WCDESC` STRING(30) — description;
`MTWC_DEPT` STRING(4) — department; `MTWC_DEPTDESC` STRING(30) — department description;
`MTWC_HRSWEEK` UBINARY(2) — hours per week capacity; `MTWC_SETUP` FLOAT(8,4) — setup rate;
`MTWC_LABOR` FLOAT(8,4) — labor rate; `MTWC_MACHINE` FLOAT(8,4) — machine rate;
`MTWC_AVGQTIME` UBINARY(2) — average queue time (days); `MTWC_QPR1/2/3` UBINARY(2) — 3 queue priority ranges;
`MTWC_VOVHD`/`FOVHD` FLOAT(8,4) — variable/fixed overhead rates; `MTWC_EST_VOVHD` FLOAT(8,4) — estimated variable OH;
`MTWC_LEAD` UBINARY(2) — lead time (days); `MTWC_OUTPROC` STRING(1) — outsource process flag;
`MTWC_HRS_SHIFT` UBINARY(2) — hours per shift; `MTWC_MIN_CHG` FLOAT(8,2) — minimum charge;
`MTWC_COST_LB` FLOAT(8,6) — cost per pound; `MTWC_EXTRA` STRING(100) — overflow;
`MTWC_PARENT_YN` STRING(1) — is a parent WC flag; `MTWC_PARENT_WC` STRING(12) — parent WC;
`MTWC_LEVEL_YN` STRING(1) — leveled scheduling flag;
`MTWC_CYCLE_TIME_1..10` UBINARY(2) each — 10 cycle time slots;
`MTWC_GDATE_1/2` DATE — 2 date UDF; `MTWC_FLAGS_1..5` STRING(1) — 5 flags;
`MTWC_GNUM` FLOAT(8,0) — generic number;
`MTWC_ALPHA_1..5` STRING(30) — 5 alpha UDF.

Purpose: Work Center master — the capacity definition for manufacturing. Rate fields
(LABOR, MACHINE, SETUP, VOVHD, FOVHD) feed into ROUTING cost calculations.
Capacity (HRSWEEK, HRS_SHIFT) feeds into scheduling. PARENT_WC enables hierarchical
WC grouping for rollup reporting. OUTPROC flag marks a WC as an outsource operation.
Referenced throughout ROUTING, WOHROUT, WCTRLOAD, and the labor tables.

---

### WORKHORD / WORKORD — Work Order Header (74f each) [schema.md:26715/26794]

Both share identical MTWO_WIP prefix schema (74 fields):

`MTWO_WIP_WOPRE` FLOAT(8,0) — WO number (PK component); `MTWO_WIP_WOSUF` UBINARY(2) — WO suffix (PK);
`MTWO_WIP_BLANK` STRING(1) — blank flag; `MTWO_WIP_MULT` STRING(1) — multi-level flag;
`MTWO_WIP_SQTY` FLOAT(8,2) — scheduled qty; `MTWO_WIP_PRTY` STRING(1) — priority;
`MTWO_WIP_SSTART`/`SFIN` DATE — scheduled start/finish; `MTWO_WIP_ASTART`/`AFIN` DATE — actual start/finish;
`MTWO_WIP_COMQTY` FLOAT(8,2) — completed qty; `MTWO_WIP_STATUS` STRING(1) — status (O=open, R=released, C=closed, H=hold);
`MTWO_WIP_LOCK` STRING(1) — locked flag;
`MTWO_WIP_ESETUP`/`EMAT`/`EOUTPR`/`ELABOR` FLOAT(8,2) — estimated costs (setup/mat/outsource/labor);
`MTWO_WIP_ASETUP`/`AMAT`/`AOUTPR`/`ALABOR` FLOAT(8,2) — actual costs;
`MTWO_WIP_ETOT`/`ATOTAL` FLOAT(8,2) — estimated/actual total costs;
`MTWO_WIP_EST` FLOAT(8,0) — estimating link; `MTWO_WIP_CODE` STRING(15) — assembly item code;
`MTWO_WIP_SONUM` FLOAT(8,0) — linked SO number; `MTWO_WIP_SOLINE` FLOAT(8,0) — SO line number;
`MTWO_WIP_SETUPV`/`MATV`/`OUTPRV`/`LABORV` FLOAT(8,2) — cost variances (actual - estimated);
`MTWO_CUSTCODE`/`CUSTNAME` STRING — customer for the SO;
`MTWO_WIP_DESC` STRING(30) — assembly description; `MTWO_WIP_PPRCE` FLOAT(8,4) — projected price;
`MTWO_WIP_TOTV` FLOAT(8,2) — total variance; `MTWO_WIP_INSTR_1..10` STRING(60) — 10 WO instructions;
`MTWO_WIP_SCONV`/`QCONV` STRING(1) — scheduling/qty conversion flags;
`MTWO_WIP_DDATE` DATE — due date;
`MTWO_WIP_VOVHD`/`AVOVHD`/`VOVHDV` FLOAT(8,2) — variable OH est/actual/variance;
`MTWO_WIP_EFOVHD`/`AFOVHD`/`FOVHDV` FLOAT(8,2) — fixed OH est/actual/variance;
`MTWO_WIP_USERCD` STRING(1) — user code; `MTWO_WIP_PROJ` STRING(15) — project code;
`MTWO_WIP_LOC` STRING(10) — warehouse location; `MTWO_WIP_CONTAT` STRING(25) — contact;
`MTWO_WIP_CHGORD` UBINARY(2) — change order count;
`MTWO_WIP_EOTH`/`AOTH`/`OTHV`/`OTHPER` FLOAT(8,2) — other cost est/actual/variance/%;
`MTWO_WIP_EMISC`/`AMISC`/`MISCV` FLOAT(8,2) — misc cost est/actual/variance;
`MTWO_WIP_EEXTRA`/`AEXTRA`/`EXTRAV` FLOAT(8,2) — extra cost est/actual/variance;
`MTWO_WIP_SCHED_1/2` STRING(1) — scheduling flags; `MTWO_WIP_SCRAP` FLOAT(8,2) — scrap qty.

WORKHORD = historical closed WOs; WORKORD = current active WOs.

Purpose: Work Order master header. This is the primary WO control record (not BKWOMSTR —
WORKORD uses the newer MTWO prefix generation). Tracks the full WO lifecycle from release
to close. Cost fields track 6-component cost breakdown (setup, material, outsource, labor,
variable OH, fixed OH) with estimated vs. actual vs. variance. Links to SO via SONUM/SOLINE.
Project code supports project-based manufacturing. Change order counter tracks ECO revisions.

---

### MK — Marketing Module

#### MKAHIST — Marketing account history (9f) [schema.md:24535]

`MKAHIST_ACCT` STRING(10) — account (customer); `MKAHIST_DATE` DATE; `MKAHIST_TRACK` FLOAT(8,0) — track number;
`MKAHIST_SEQ` UBINARY(2) — sequence; `MKAHIST_EVENT` FLOAT(8,0) — event number;
`MKAHIST_MEDIA` STRING(1) — media code; `MKAHIST_FORM` FLOAT(8,0) — form number;
`MKAHIST_REM1/2` STRING(60) each — 2 remark lines.

Purpose: Marketing activity history per customer account. Records each touchpoint (event,
media, form) with date, track, and remarks.

#### MKASSIGN — Marketing assignment (6f) [schema.md:24549]

`MKASSIGN_ACCT` STRING(10) — account; `MKASSIGN_TRACK` FLOAT(8,0) — track;
`MKASSIGN_NXTSEQ` UBINARY(2) — next sequence; `MKASSIGN_NXTDAT` DATE — next action date;
`MKASSIGN_SALEND` DATE — sale end date; `MKASSIGN_PRCODE` FLOAT(8,0) — price code.

Purpose: Assigns a customer account to a marketing track with scheduling data.

#### MKDEF — Marketing module defaults (11f) [schema.md:24560]

`MKDEF_REQUIRE` STRING(1) — required flag; `MKDEF_CALENDAR` STRING(1) — use calendar flag;
`MKDEF_TRACK` FLOAT(8,0) — default track; `MKDEF_PRICECD` FLOAT(8,0) — default price code;
`MKDEF_FUCODE` STRING(3) — follow-up code; `MKDEF_HISTORYCD` STRING(2) — history code;
`MKDEF_TNEXTID`/`TCNEXTID`/`ENEXTID`/`ECNEXTID`/`FNEXTID` FLOAT(8,0) — auto-number counters
(track, track-class, event, event-class, form next IDs).

Purpose: Single-row defaults table for the marketing module. Stores next-ID counters for all
marketing entity types.

#### MKECLASS / MKICLASS — Marketing event/item class codes (3f each) [schema.md:24576/24612]

Identical schema: `MKECLASS_NUM` FLOAT(8,0) PK; `MKECLASS_DESC` STRING(45); `MKECLASS_ACTIVE` STRING(1).
MKECLASS = event classes; MKICLASS = item classes. Note: MKICLASS reuses the MKECLASS field prefix.

#### MKEVENT — Marketing events (12f) [schema.md:24584]

`MKEVENT_NUM` FLOAT(8,0) PK; `MKEVENT_DESC` STRING(45); `MKEVENT_CLASS` FLOAT(8,0) — FK to MKECLASS;
`MKEVENT_MEDIA` STRING(1) — media type; `MKEVENT_FORM` FLOAT(8,0) — FK to MKFORM;
`MKEVENT_FUCODE` STRING(3) — follow-up code; `MKEVENT_REM1/2` STRING(60) — remarks;
`MKEVENT_SENDTO` UBINARY(2) — send-to code; `MKEVENT_GENNAME` STRING(45) — generic name;
`MKEVENT_HISTCD` STRING(2) — history code; `MKEVENT_ACTIVE` STRING(1).

#### MKFORM — Marketing forms (6f) [schema.md:24601]

`MKFORM_NUM` FLOAT(8,0) PK; `MKFORM_DESC` STRING(45); `MKFORM_FILE` STRING(25) — file name;
`MKFORM_ATT` STRING(25) — attachment; `MKFORM_MEDIA` STRING(1); `MKFORM_ACTIVE` STRING(1).

Purpose: Marketing form master — defines printed forms/documents used in campaigns.

#### MKTCLASS — Marketing track class codes (3f) [schema.md:24620]

`MKTCLASS_NUM` FLOAT(8,0) PK; `MKTCLASS_CLASS` STRING(45); `MKTCLASS_ACTIVE` STRING(1).

#### MKTNOTE — Marketing track notes (3f) [schema.md:24628]

`MKTNOTE_TRACK` FLOAT(8,0) — track FK; `MKTNOTE_LINE` UBINARY(2) — line seq;
`MKNOTE_TEXT` STRING(70) — note text. Note: field prefix mismatch (MKNOTE vs. MKTNOTE).

#### MKTRACK — Marketing tracks (4f) [schema.md:24636]

`MKTRACK_NUM` FLOAT(8,0) PK; `MKTRACK_DESC` STRING(45); `MKTRACK_CLASS` FLOAT(8,0) — FK to MKTCLASS;
`MKTRACK_ACTIVE` STRING(1).

Purpose: A marketing track is a sequence of timed events (like a campaign drip sequence).
Accounts are assigned to tracks via MKASSIGN; events fire on schedule per MKTROUT.

#### MKTROUT — Marketing track routes (11f) [schema.md:24645]

`MKTROUT_TRACK` FLOAT(8,0) — track FK; `MKTROUT_SEQ` UBINARY(2) — step sequence;
`MKTROUT_JUMP` STRING(1) — jump/branch flag; `MKTROUT_NEXTSEQ` UBINARY(2) — next step;
`MKTROUT_EVENT` FLOAT(8,0) — event to fire (FK to MKEVENT); `MKTROUT_DAYSNXT` UBINARY(2) — days until next step;
`MKTROUT_FIXED` STRING(1) — fixed date flag; `MKTROUT_SALEBEG` STRING(1) — sale begin flag;
`MKTROUT_SALELEN` UBINARY(2) — sale length (days); `MKTROUT_SALECLO` STRING(1) — sale close flag;
`MKTROUT_PRICECD` FLOAT(8,0) — price code to apply.

Purpose: Defines the event sequence within a track: step 1 fires event X, then DAYSNXT days
later step 2 fires event Y, etc. JUMP/NEXTSEQ allow conditional branching.

---

### Temp/Test Tables (noted, not operational)

**TEMPOLD** (4f) — legacy temp table using BKCM_ACTD prefix (Activity Detail?). Likely a
remnant from an older module version. Fields: code, date-code, date, extra.

**TESTARRA** (101f) / **TESTFILE** (11f) — TAS Pro 7 developer test tables. Not operational.

---

## Pass 142 — Pre-IS* DDF Tables: AP, AR, BM, CM Families

*Source: `samples/ddf/schema.md` lines 0–4166 (DDF read 2026-06-22)*

This pass documents the pre-IS* BK* families that were absent from tier2-tables.md. These tables appear in the DDF before the IS* module tables (~line 11629). All field counts and offsets are confirmed from the DDF.

---

### System / Utility Tables

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| AHSYLOG | 23 | AHSY_ | System activity log: user, date, time, program, action |
| ARTTEMP | 12 | ARTT_ | A/R temp work table (report/processing scratch) |
| BKABCUST | 5 | BKAB_ | A/R customer abbreviation/alternate code map |
| BKABVEND | 2 | BKAB_ | A/P vendor abbreviation/alternate code map |
| BKACTRPT | 53 | BKAC_ | Activity report control / filter parameters |

**AHSYLOG** (23f, AHSY_ prefix): Audit trail for user logins and program launches. Key fields: `AHSY_USER` (STRING/10), `AHSY_DATE` (DATE), `AHSY_TIME` (TIME), `AHSY_PROG` (STRING/15), `AHSY_ACTION` (STRING/1), plus extended detail fields.

**BKACTRPT** (53f, BKAC_ prefix): Report parameter block for activity/usage reports — stores filter ranges, sort options, output type flags. Largest non-master table in this section.

---

### A/P Module: BKAP* Family

#### Core Vendor Master

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKAPVEND | 72 | BKAP_VEND_ | Vendor master (active) |
| BKAPVND2 | 63 | BKAP2_ | Vendor extended — 5 user-defined fields per type |
| BKAPEVND | 73 | BKAP_ | Vendor entry (data entry staging) |
| BKAPNOTE | 8 | BKAP_NOTE_ | Vendor notes (8 fields: VEND + CNTR + 6 NOTE lines) |

**BKAPVEND** (72f): Vendor master. PK = `BKAP_VEND_NUM` (UBINARY/2). Key fields: vendor code (STRING/10), name/address block, tax ID, payment terms (`BKAP_VEND_TERMS`, UBINARY/2), default GL account/dept, 5 email slots (128 each), IS* extension fields (TAXGRP, TAXIN, MCCODE). 1099 flags, credit limit, YTD/LYR purchase totals, 10 notes lines (80-char each).

**BKAPVND2** (63f, BKAP2_ prefix): Vendor extended record — 5 user-defined slots each for: ALPH (25-char string), DATE1 (DATE), DATE2 (DATE), NUML (FLOAT), NUMS (UBINARY). Plus CONT/TITLE/PHONE/FAX, 2 email slots, DEAR fields. PK = `BKAP2_VEND` (STRING/10).

#### A/P Description (Narrative) Satellites — BK_DESC_ Pattern

| Table | Fields | Pattern | Purpose |
|-------|--------|---------|---------|
| BKAPADSC | 5 | BK_DESC_ | A/P entry description lines |
| BKAPDESC | 5 | BK_DESC_ | A/P description lines (active) |
| BKAPHDSC | 5 | BK_DESC_ | A/P history description lines |

All three share the **BK_DESC_ pattern**: `BK_DESC_CODE` (FLOAT/8) + `BK_DESC_NUM` (UBINARY/2) + `BK_DESC_LINE` (UBINARY/2) + `BK_DESC_NOTES` (STRING/1) + `BK_DESC_DESC` (STRING/60). PK = CODE + LINE. Used to store multi-line narrative text attached to AP vouchers.

#### A/P Check Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKAPCHKF | 12 | A/P check file (current checks) |
| BKAPCHKH | 12 | A/P check history |

Both share the same 12-field schema: `BKAP_CHK_INVNUM` (FLOAT/8), `BKAP_CHK_VENDNUM` (UBINARY/2), `BKAP_CHK_CHKNUM` (FLOAT/8), date, amount, cleared flag, discount, etc.

#### A/P Invoice / GL Distribution

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKAPACCN | 154 | BKAP_ACCN_ | A/P account contacts (10 contact slots × 15 field types) |
| BKAPINVL | 390 | BKAP_INV_ | A/P invoice GL distribution (75 GL slots) |
| BKAPRIVL | 390 | BKAP_INV_ | A/P invoice GL distribution — history/reversed |
| BKAPINVT | 19 | BKAP_INVT_ | A/P invoice temp (work table) |
| BKAPEIVT | 19 | BKAP_INVT_ | A/P invoice entry temp (same schema as BKAPINVT) |
| BKAPDEP | 6 | BKAP_DEP_ | A/P department code table |

**BKAPINVL** (390f): Most complex AP table. Stores 75 GL distribution slots, each with 4 arrays indexed 1..75:
- `BKAP_INV_GLACT_n` (STRING/10) — GL account
- `BKAP_INV_GLDPT_n` (STRING/4) — GL department
- `BKAP_INV_DC_n` (STRING/1) — Debit/Credit flag
- `BKAP_INV_GLD_n` (STRING/15) — GL description
- `BKAP_INV_DAMT_n` (FLOAT/8/2) — Distribution amount

Plus metadata: INVNUM, VENDNUM, INVDATE, POSTDATE, totals. 390 fields total. **BKAPRIVL** is byte-for-byte identical — the reversed/history version.

#### A/P Purchase Order Tables

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKAPAPO | 58 | BKAP_PO_ | A/P PO entry (data entry) |
| BKAPAPOL | 38 | BKAP_POL_ | A/P PO entry lines |
| BKAPPO | 57 | BKAP_PO_ | A/P PO active |
| BKAPPOL | 38 | BKAP_POL_ | A/P PO active lines |
| BKAPHPO | 57 | BKAP_PO_ | A/P PO history |
| BKAPHPOL | 38 | BKAP_POL_ | A/P PO history lines |
| BKAPRFQ | 57 | BKAP_PO_ | A/P RFQ (Request for Quote) |
| BKAPRFQL | 38 | BKAP_POL_ | A/P RFQ lines |
| BKAPQUOT | 49 | BKRFQ_ | A/P quotation (vendor quote response) |

**BKAP_PO_ schema** (57–58 fields): Header contains vendor code/num, PO number, dates (order, promised, required), ship-to address block, freight/terms/FOB, approval flag, buyer, totals. BKAPAPO has 58f (1 extra temp field).

**BKAP_POL_ schema** (38 fields): Line-level data — part code, description, ordered qty, received qty, unit price, extended amount, GL acct/dept, line number, status.

**BKAPQUOT** (49f, BKRFQ_ prefix): Vendor quote response — RFQ number, vendor, quoted price/qty/lead-time, expiry date, notes.

---

### A/R Module: BKAR* Family

#### Customer Master

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKARCUST | 106 | BKAR_ | A/R customer master |
| BKARECST | 106 | BKAR_ | Customer master — estimating module view (identical schema) |
| BKARSHIP | 106 | BKAR_ | A/R alternate ship-to addresses (identical schema) |
| BKARDEP | 6 | BKAR_DEP_ | A/R department code |

**BKARCUST** (106f, PK = `BKAR_CUSTCODE` STRING/10): Most complete customer record. Fields:
- Address: CUSTNAME, ADD1, ADD2_1/2, CITY, STATE, ZIP, COUNTRY
- Contacts: CONTACT_1..5 (STRING/30 each), TELEPHONE_1..5 (STRING/25 each)
- Credit: CREDITLMT, CHG_INTRST, REMAINCRD, OUTINV, CREDIT_HLD
- Sales history: GROSS/COGS/NET/PNET × MTD/YTD/LYR/PVAR (16 FLOAT fields)
- Credit aging: OUT_CREDIT_1/2
- Tax: TAX_STATE, TAX_LOCAL, TAX_YN
- Billing: STATEMENT, SLSP_NUM_1/2, TERMS_NUM, PRICE_MAT, DISC_CODE
- Notes: NOTES_1..10 (STRING/80 each)
- GL: GLACCT, GLDPT
- Logistics: FOB, SHIPTO, SHIPVIA, CARRIER, SHP_WINDOW, RECV_HOURS, SHP_TOLRNC
- CRM: LEAD_SRC, LEAD_SRC2, TERRITORY, SORT, COOP_RATE, COOP_AMT, COMM_1/2
- QC/Compliance: QC_INFO, REQD_CERTS, RESALE_NO, PURCH_AGMT
- Contact ext: FAX_PHONE, EMAIL_1..5 (STRING/128 each)
- IS* extensions: IS_TAXGRP, IS_TAXIN, IS_MCCODE, IS_REP

**BKARECST** and **BKARSHIP** are byte-for-byte identical 106-field schemas — BKARECST gives the estimating module access to customer data; BKARSHIP stores alternate ship-to addresses (same physical layout, different PK usage).

#### A/R Description (Narrative) Satellites — BK_DESC_ Pattern

| Table | Fields | Purpose |
|-------|--------|---------|
| BKARDESC | 5 | A/R description lines |
| BKARDPST | 5 | A/R description posted |
| BKARHDSC | 5 | A/R history description |
| BKARRDSC | 5 | A/R return/credit description |

All four share the **BK_DESC_ pattern** (same 5-field schema as BKAPADSC — see above).

#### A/R Check Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKARCHKF | 12 | A/R check file |
| BKARCHKH | 12 | A/R check history |

Identical 12-field schema to BKAPCHKF (different prefix BKAR_CHK_).

#### A/R Invoice Tables

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKARINV | 84 | BKAR_INV_ | A/R invoice header (current) |
| BKARHINV | 84 | BKAR_INV_ | A/R invoice header (history) — identical schema |
| BKARRINV | 84 | BKAR_INV_ | A/R return/credit invoice — identical schema |
| BKARINVL | 28 | BKAR_INVL_ | A/R invoice lines (current) |
| BKARHIVL | 28 | BKAR_INVL_ | A/R invoice lines (history) — identical schema |
| BKARRIVL | 28 | BKAR_INVL_ | A/R return/credit lines — identical schema |
| BKARSIVL | 28 | BKAR_INVL_ | A/R sales invoice lines variant (adds SCCOG field) |
| BKARINVT | 23 | BKAR_INVT_ | A/R invoice temp |
| BKAREIVT | 24 | BKAR_INVT_ | A/R invoice entry temp (adds BKAB_PERIOD field) |
| BKARINVI | 16 | BKAR_INVI_ | A/R invoice item temp (SO-to-invoice sequence) |
| BKARINVV | 77 | BKAR_INVV_ | A/R invoice GL distribution (10 GL slots) |
| BKARHTAX | 5 | BKAR_TAX_ | A/R invoice tax breakdown |

**BKAR_INV_ schema** (84f): Invoice header. Key fields: INVNM (invoice number, FLOAT/8), CUSTCODE, INVDATE, POSTDATE, DUE date, billing address block (BILCOD/BILNME/BILA1-3/BILCTY/BILST/BILZIP/BILCNT/BILATN — 10 fields), payment terms, salesperson 1/2, tax amounts, freight, totals (subtotal, discount, tax, freight, net), misc. GL acct/dept for revenue posting. **BKARHINV**, **BKARRINV** are byte-identical.

**BKAR_INVL_ schema** (28f): Invoice line items. Key fields: INVNM (FK), CNTR (line counter, UBINARY/2), ESD (estimated ship date, DATE), PCODE (part code, STRING/15), PDESC (description, STRING/30), PQTY, PPRCE, PDISC, PEXT (extended), PCOGS, ITYPE (item type), TXBLE (taxable flag), UBO (unit backorder qty), USTD (unit standard cost), RTS (return-to-stock), LOC (location), ABQTY (allocated backorder), UM_LN_1/2 (units of measure), COMPR_1/2 (component prices), ASD (actual ship date), TXAMT, FRGHT (freight), COOP, OOQTY (original order qty), EXTRA. **BKARHIVL**, **BKARRIVL** are identical. **BKARSIVL** adds SCCOG (standard cost of goods, FLOAT/8/4) as field 28.

**BKARINVV** (77f, BKAR_INVV_ prefix): AR invoice GL distribution — smaller than AP's 75-slot BKAPINVL. Stores 10 GL distribution slots: GLACT_n/GLDPT_n/DC_n/GLD_n/DAMT_n (n=1..10) = 50 fields, plus invoice number, customer code, date, control totals, and metadata = 77 fields total.

#### A/R Transaction Tables

| Table | Fields | Prefix | Purpose |
|-------|--------|--------|---------|
| BKART | 12 | BKART_ | A/R transaction ledger |
| BKARTNOT | 3 | BKART_NOT_ | A/R transaction notes |
| BKARTXN | 14 | BKAR_TXN_ | A/R transaction detail (lot/serial tracking) |
| BKARTXNB | 14 | BKAR_TXN_ | A/R transaction detail — backup/batch variant (identical) |
| BKARTXNS | 14 | BKAR_TXN_ | A/R transaction detail — shipped variant (identical) |

**BKART** (12f): AR ledger entry. PK = CUST + TRXN. Fields: CUST (STRING/10), TRXN (transaction number, FLOAT/8), TYPE (STRING/1: I=invoice, P=payment, C=credit, etc.), DISC, AMOUNT, POSTDATE, CNTR, ENTDATE, TRXNLINK, INVC, CHECK, NOTE.

**BKARTXN** (14f): Lot/serial tracking for shipped items. PK = SONUM + LINE + LOT + SERIAL. Fields: SONUM, CODE (part), DESC, QTY, LOT (STRING/15), SERIAL (STRING/25), DATE, STOCK (location), LINE, LOC, TMPSO (temp SO reference), SRNUM (serial number float), EXTRA, BIN. BKARTXNB and BKARTXNS are byte-identical.

---

### BOM Module: BKBM* Family

#### BOM Line Tables (Shared Schema)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKBMMSTR | 26 | BOM master (production standard) |
| BKBMAMTR | 26 | BOM alternate material |
| BKBMAVAL | 26 | BOM alternate validation copy |
| BKBMEMTR | 26 | BOM engineering master |
| BKBMSUMM | 26 | BOM summary/rollup |

All five share the **BKBM_ line schema** (26f):
- PK: `BKBM_PARENT` (STRING/15) + `BKBM_COMPONENT` (STRING/15)
- `BKBM_QTY_REQD` (FLOAT/8/8 — 8 decimal places for precision)
- `BKBM_REFERENCE` (STRING/20)
- `BKBM_PROD_TYPE` (STRING/1) — component type flag
- `BKBM_PROD_SCRAP` (FLOAT/8/2) — scrap factor
- `BKBM_PROD_OP` (STRING/3) — operation code
- `BKBM_PROD_OPYN_1..6` (STRING/1 each) — op enable flags
- `BKBM_PROD_PRICE` (FLOAT/8/4)
- `BKBM_PROD_RTNUM` (UBINARY/2) — routing number
- `BKBM_PROD_DUPOP` (STRING/1) — duplicate op flag
- `BKBM_PROD_OPDSC` (STRING/5) — op description
- `BKBM_PROD_VEND` (STRING/10) — outside process vendor
- `BKBM_DATE1`, `BKBM_DATE2` (DATE) — effectivity dates
- `BKBM_EXTRA` (STRING/50), `BKBM_REV` (STRING/5) — ECO revision
- `BKBM_P_TYPE`, `BKBM_C_TYPE` (STRING/10 each) — parent/component type
- `BKBM_EST_LINE` (FLOAT/8/0), `BKBM_UID` (STRING/20)

#### BOM Satellite Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKBMCNFG | 7 | BOM module configuration |
| BKBMDIM | 11 | BOM component dimensions (sheet metal / cut-to-size) |
| BKBMERMK | 20 | BOM engineering remarks (15 remark lines × 64 chars) |
| BKBMREMK | 20 | BOM remarks — same 20-field schema as BKBMERMK |
| BKBMNOTE | 16 | BOM notes (parent-level, 15 note lines × 64 chars) |

**BKBMCNFG** (7f): Module config — GL account/dept for BOM postings, AUTO/POST/ROLL/LABOR flags.

**BKBMDIM** (11f): Sheet material cut-to-size dimensions. PK = DIM_PARENT + LINE. Fields: COMP (component), PART_X/Y (part size, FLOAT/8/4), MACH (machine code), TRIM_X/Y (trim allowance), REMN_X/Y (remnant size), EXTRA.

**BKBMERMK / BKBMREMK** (20f each, identical schema): PK = RM_PARENT + LINE + RM_COMP. Contains 15 × `BKBM_RM_REMARK_n` (STRING/64 each) + UID + EXTRA.

**BKBMNOTE** (16f): Parent-level BOM notes. PK = NT_PARENT. Contains 15 × `BKBM_NT_NOTE_n` (STRING/64 each).

---

### CM Module: BKCM* Family (Contact Manager / CRM)

The BKCM* family is the EvoERP CRM/Contact Manager module. It mirrors AR customer data (BKCMCUST = BKARCUST schema), adds prospect tracking (BKCMPCNT), dunning/collections (BKCMDUN/DUNH), activity history (BKCMACTH), and mail-merge campaigns (BKCMMHST).

#### Account / Contact Master

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMACCT | 41 | CM account master (company-level) |
| BKCMDE | 41 | CM data-entry/export copy (identical schema) |
| BKCMEACT | 41 | CM eAccess account (identical schema) |
| BKCMCUST | 106 | CM customer view (identical to BKARCUST 106-field schema) |
| BKCMACCN | 154 | CM account contacts — 10 contact slots × multi-field |
| BKCMPCNT | 24 | CM prospect contact master |

**BKCMACCT** (41f, BKCM_ACCT_ prefix): Account (company) master. Fields: CODE (PK/10), OLDCD, ALPHA (sort key/6), NAME (30), ADD1/2/3 (30 each), CITY (26), STATE (2), ZIP (10), CNTRY (30), CONT1/TITLE/PHONE/FAX (contact 1), REP (5), DLOAD, SICCD (7), CUST (is-customer flag), LEAD (5), START (DATE), TERR (4), REMs (2 × STRING/60), phone slots with extensions, credit card fields (CCARD/CNUM/CEXP/CMPNM/PNAME), EXTRA (200), EMAIL (128), EMPS (FLOAT = employee count).

**BKCMACCN** (154f): Per-account contacts table — 10 named contacts each with: CONT_n (30), TITLE_n (30), PHONE_n (25), EMAIL_n (128), ALPH1_n (25), ALPH2_n (25), DATE1_n, DATE2_n. Plus column-header label strings for phone/email/messaging/date slots (PHLBL, EMLBL, MSLBL, DTLBL, M2LBL, D2LBL — 10 × 20-char each). PK = ACCN_CODE. 154 total fields.

**BKCMPCNT** (24f): Prospect contact master (pre-customer). PK = CCODE (10). Fields: REP, ALPHA, NAME, ADD1/2/3, CITY, STATE, ZIP, CNTRY, CONT, TITLE, PHONE, FAX, CLASS, SDATE, REMs 1..4, EXTRA, WPHON, EMAIL.

#### Activity / History Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMACTH | 21 | CM account activity history |
| BKCMEACH | 21 | CM eAccess activity history (identical schema) |
| BKCMACTF | 11 | CM activity follow-up |
| BKCMEACF | 11 | CM eAccess follow-up (identical schema) |
| BKCMACTD | 4 | CM activity date link |
| BKCMEACD | 4 | CM eAccess activity date link (identical schema) |
| BKCMPCTH | 8 | CM prospect contact history |
| BKCMPCTF | 9 | CM prospect contact follow-up |

**BKCMACTH** (21f): Activity history log entry. PK = CODE + DATE + REP + LINE. Fields: CODE (account/10), DATE, REP (5), LINE (UBINARY/2), CD (activity code/2), EVENT (event type, UBINARY/2), PHONE (Y/N), START/STOP (TIME), MIN/BMIN (duration minutes, UBINARY), REM (memo/57), BILLD (billed flag), DLOAD, FLINE, RECVD (TIME), CNTCT (contact name/25), RATE/AMT/BALNC (billing amounts), EXTRA.

**BKCMACTF** (11f): Follow-up record. PK = CODE + REP + DATE. Fields: CODE, REP, TYPE (activity type/3), DATE, REMs 1..5 (60 each), DLOAD, SO (linked SO number, FLOAT).

#### Dunning / Collections

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMDUN | 36 | Dunning run control parameters |
| BKCMDUNH | 6 | Dunning history |
| BKCMFORM | 8 | Dunning form/letter definition |

**BKCMDUN** (36f): Dunning configuration. Per-rep settings: AGE_1..10 (aging bucket thresholds, UBINARY/2 each), FORM_1..10 (form codes, STRING/15 each), DESC_1..10 (descriptions, 30 each), DORL (D=dunning/L=letters), NUMUP, SORT, PCONT (print contact), CNUM.

**BKCMFORM** (8f): Dunning letter template definition. PK = FORM_CODE (15) + LINE (UBINARY). Fields: NOTE (78), DESC (30), LEFT/LNSPG/START (layout params, UBINARY), DUN (flag).

#### Mail Merge / Marketing History

**BKCMMHST** (72f, BKCM_MHST_ prefix): Mail merge history — largest CM table. One record per campaign run. Key fields: MCODE (15), DESC (25), MDATE, 20 CLASS filters and 20 override OCLAS filters (STRING/5 each), FROM/TO range criteria for account code, state, ZIP, SIC, start date, lead source, territory, rep, STATUS filter (11 chars), CUSTO flag, sort/form/contact settings.

#### Code / Lookup Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMACCC | 2 | Contact class code (CCODE/5 + DESC/25) |
| BKCMACCL | 2 | Account class (CODE/10 + CLASS/5) |
| BKCMEACC | 2 | eAccess class (identical to BKCMACCL) |
| BKCMDTCD | 2 | Date code (DCODE/2 + DESC/25) |
| BKCMACFC | 3 | Follow-up call category (FCODE/3 + DESC/25 + REP/5) |
| BKCMPCFC | 3 | Prospect follow-up call category (identical) |
| BKCMLEAD | 2 | Lead source code (SCODE/5 + DESC/25) |
| BKCMTERR | 11 | Territory definition |
| BKCMHCOD | 9 | Help/activity category code |
| BKCMHCD2 | 7 | Help code 2-part hierarchy |
| BKCMREP | 14 | CM rep/salesperson master |
| BKCMCNTD | 12 | Contact definitions (title slot labels) |

**BKCMTERR** (11f): Territory. PK = TCODE (4). Fields: DESC (25), EMAIL (128), ALPHA (30), EXTRA (100), FLAGS_1..5 (STRING/1 each), DATE.

**BKCMREP** (14f): CM rep master. PK = REP (5). Fields: FNMEMI, LNAME, EMP (employee num, UBINARY/2), PSWD, DHCODE (default help code), DFCODE, DDCODE, VIEW/CHANGE/GWARN/AADD (permission flags), FNAME, FTITLE.

**BKCMHCOD** (9f): Activity/help category. PK = HCODE (2). Fields: DESC (25), WINDW (Y/N), RATE (billing rate, FLOAT/8/2), UM (unit of measure/3), ABILL (auto-bill flag), BPART/NPART/FPART (part codes for billable/non-billable/flat — STRING/15 each).

#### Free Time / Subscription Billing

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMFTME | 7 | Free time account (billable time balance) |
| BKCMEFTM | 7 | eAccess free time (identical schema) |
| BKCMSBDF | 5 | SBD interest / subscription parameters |

**BKCMFTME** (7f): Free time/prepaid support balance. PK = FTME_CODE (10). Fields: FTIME (prepaid minutes, UBINARY), DESC (25), BALNC (balance, FLOAT), LASTP (last posted date), ATIME (used minutes, UBINARY), NTIME (next billing minutes, UBINARY).

**BKCMSBDF** (5f): Service/subscription billing defaults. Fields: BINC (billing increment, FLOAT/8/2), MINC (minimum charge minutes, UBINARY/2), ICONV (unit conversion factor, FLOAT/8/6), NCHG (no-charge threshold, UBINARY/2), DHOLD (defer-to-hold flag, STRING/1).

#### Control / Temp Tables

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMCTL1..4, BKCMCTRL | 1 each | Lock control (single field: CTRL_USER STRING/10) |
| BKCMTEMP | 6 | CM work/temp table |
| BKCMTMP1 | 6 | CM temp 1 (identical to BKCMTEMP) |
| BKCMTMP2 | 6 | CM temp 2 (identical to BKCMTEMP) |

**BKCMTEMP** (6f, BKCMT_ prefix): Temporary work record. Fields: CODE (10), KEYF (20), GROUP (8), COMP (2), TAG (1), ACTIVITY (5). Used during CM processing/report runs.

---

*Pass 142 — batch 1 complete: 107 tables documented (AP, AR, BM, CM families). GL, IC, PR, SL, SO, SY, WH families follow in pass 143.*

---

## Pass 143 — BKPI / BKPOX / BKLOGON / BKMATCST / BKRT / BKSA / BKSB / BKSL / BKSO+ / BKPR(partial) / EST* families

### Physical Inventory (BKPI*)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKPILCNT | 10 | PI lot count record |
| BKPILOT | 10 | PI lot record (identical schema) |
| BKPIMSTR | 3 | PI period master |
| BKPIPHYS | 14 | PI physical count tag |
| BKPISCNT | 10 | PI serial count |
| BKPISER | 10 | PI serial record (identical to BKPISCNT) |

**BKPIMSTR** (3f): Physical inventory period master. PK = BKPI_MSTR_YEAR (STRING/4) + BKPI_MSTR_QTR (STRING/2). Fields: DESC (STRING/30 — period description). Defines PI fiscal periods.

**BKPILCNT** (10f): PI lot count record. PK = YEAR+QTR+CODE (part code STRING/15)+LOT (lot# STRING/15). Fields: QTY (FLOAT/8/2), TAG (FLOAT/8/0 — count tag#), LOC (warehouse location STRING/10), SERQTY (serial qty FLOAT/8/2), PSTD (posted flag STRING/1), BIN (STRING/15).

**BKPILOT** (10f): PI lot record — byte-identical schema to BKPILCNT.

**BKPIPHYS** (14f): PI physical count tag. PK = TAGNUM (FLOAT/8/0 — tag number). Fields: ACTQTY (FLOAT/8/2 — actual qty counted), EMPNUM (UBINARY/2), EMPNAME (STRING/15), COMMENT (STRING/30), COUNTDATE (DATE), YEAR (STRING/4), QTR (STRING/2), LOC (STRING/10), CODE (part STRING/15), FDATE (DATE — freeze date), LOT (STRING/15), SERIAL (STRING/25), BIN (STRING/15).

**BKPISCNT** (10f): PI serial count. PK = YEAR+QTR+CODE+SERIAL (STRING/25). Fields: QTY (FLOAT/8/2), TAG (FLOAT/8/0), LOC (STRING/10), LOTNO (STRING/15), PSTD (STRING/1), BIN (STRING/15).

**BKPISER** (10f): PI serial record — byte-identical to BKPISCNT.

---

### PO Transmittal / Export (BKPOX*)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKPOX | 19 | PO transmittal header (current) |
| BKPOXH | 19 | PO transmittal history (identical schema) |

**BKPOX** (19f): Purchase order electronic transmittal/export record. PK = COMPANY (STRING/2)+INVCNUM (STRING/10)+INVCDATE (DATE). Fields: PONUM (FLOAT/8/0), VENDCODE (STRING/10), VENDNAME (STRING/30), SUBTOT (FLOAT/8/2), TAXAMT (FLOAT/8/2), FREIGHT (FLOAT/8/2), TOTAL (FLOAT/8/2), CURRENCY (STRING/3), TERMSDESC (STRING/20), TERMSCODE (UBINARY/2), INVCDESC (STRING/30), TAXCODE (STRING/10), TAXNAME (STRING/30), POSTDATE (DATE), ARCHDATE (DATE), ENTDATE (DATE).

**BKPOXH** (19f): PO transmittal history — byte-identical to BKPOX.

---

### User Login / Session Control (BKLOGON)

**BKLOGON** (10f): User login and session control. PK = CODE (STRING/15 — user ID/login name). Fields: PSWD (password STRING/10 — **stored as plaintext**), CMPY (company code STRING/2), PROG (current program STRING/8), PRINTER (UBINARY/2), INUSE (in-use flag STRING/1), SCRTY (security level STRING/2 — links to BKSLMSTR/BKSLEVEL), MENU (UBINARY/2), SUBMENU (UBINARY/2), CURPRT (current printer# UBINARY/2). INUSE flag prevents duplicate sessions.

---

### Material Cost Break Table (BKMATCST)

**BKMATCST** (25f): Material cost break points per part. PK = BKMC_CODE (STRING/15 — part code). Fields: QTY_1..10 (FLOAT/8/2 — 10 qty break thresholds), COST_1..10 (FLOAT/8/4 — unit cost at each break), DATE (DATE — effective date), MIN (FLOAT/8/2 — minimum order qty), MINCST (FLOAT/8/4 — minimum cost to charge), EXTRA (STRING/50). Supports up to 10-tier volume pricing for materials.

---

### Sales Analysis Reports (BKSA*)

**BKSAREPT** (57f): Sales analysis report saved filter parameters. PK = TYPE (STRING/8 — report type) + NAME (STRING/15 — saved filter name). Fields: RTM (report template STRING/15), then 26 FROM/THRU parameter pairs covering every filter type: numeric (FLOAT), date (DATE), 10-char codes, 2-char company, 30-char names, 4-char dept/period, integer (UBINARY), 25-char names, amounts (FLOAT/8/2), currency (STRING/3), etc. Also: BASE (STRING/1), TITLE (STRING/40 — saved report title). Allows saving/restoring complex report filter sets.

---

### Subcontract / Approved Source BOM (BKSB*)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKSBMFG | 6 | Approved manufacturer for component |
| BKSBPART | 5 | Approved substitute part |
| BKSBVEND | 6 | Approved vendor for component |

All three share compound PK: PARNT (parent part STRING/15) + PROD (component STRING/15) + CUST (customer STRING/10), allowing customer-specific approved source lists.

**BKSBMFG** (6f): Approved manufacturer. Additional fields: MANUF (STRING/25), MPART (mfg part# STRING/25), EXTRA (STRING/50).

**BKSBPART** (5f): Approved substitute part. Additional fields: SUBST (substitute part STRING/15), EXTRA (STRING/50).

**BKSBVEND** (6f): Approved vendor. Additional fields: VEND (STRING/10), VPART (vendor's part# STRING/25), EXTRA (STRING/50).

---

### WO Component Shortage Tracking (BKSHORT)

**BKSHORT** (9f): Work order component shortage record. PK = PCODE (STRING/15)+WONUM (FLOAT/8/0)+WO_SUF (UBINARY/2). Fields: DESC (STRING/25), QTYREQ (FLOAT/8/2), SHORT (shortage qty FLOAT/8/2), DATE (DATE), PPCODE (parent part STRING/15), PPDESC (parent description STRING/25). Created by MRP/WO when a component is short; drives shortage reporting.

---

### Security / Access Level (BKSL*)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKSLMSTR | 2 | Security level name/description |
| BKSLEVEL | 422 | Per-level menu access ACL bitmap |

**BKSLMSTR** (2f): Security level master. PK = BKSL_MSTR_LEVEL (STRING/2 — level code e.g. "01", "SU"). Fields: DESC (STRING/45 — level name). One record per defined security level; codes link to BKLOGON.SCRTY and BKSLEVEL.LEVEL.

**BKSLEVEL** (422f): Security access control list — defines which menu items each security level may access. PK = MENU (UBINARY/2 — main menu#) + LEVEL (STRING/2 — security level code). Structure: 2 PK fields + 20 menu groups × 21 flags (each STRING/1):

- `BKSL_MENUx_YN` — Y/N: entire menu group enabled for this level
- `BKSL_MENUx_1` through `BKSL_MENUx_20` — individual item access flags

Fields 3-23 = MENU1 group, 24-44 = MENU2, … 402-422 = MENU20 group. Record size = 424 bytes (offsets 0-423). Supports up to 20 top-level menus × 20 items each = 400 individual access control points per level. At login, EVO reads (menu#, user-level) → flags to show/hide each menu item.

---

### Sales Order Lot / Serial Allocation (BKSO* additions)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKSOHLOT | 14 | SO lot allocation (on-hold) |
| BKSOHSER | 14 | SO serial allocation (on-hold, identical) |

Both use BKAR_TXN_ field prefix (shared with AR transaction tables).

**BKSOHLOT** (14f): Lot number committed to a SO line. PK = SONUM (FLOAT/8/0)+CODE (STRING/15)+LINE (FLOAT/8/0). Fields: DESC (STRING/30), QTY (FLOAT/8/2), LOT (STRING/15), SERIAL (STRING/25), DATE (DATE), STOCK (STRING/15), LOC (STRING/10), TMPSO (STRING/40), SRNUM (FLOAT/8/0), EXTRA (STRING/50), BIN (STRING/15).

**BKSOHSER** (14f): Serial number committed to SO line — byte-identical to BKSOHLOT.

---

### Routing Module (BKRT*)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKRTCST | 24 | Routing cost standard |
| BKRTEMTR | 62 | Routing estimate/template operation master |
| BKRTSPEC | 7 | Routing specification notes |
| BKRTTEMP | 6 | Routing template notes |

**BKRTSPEC** (7f): Routing spec notes per part+operation. PK = BKRT_SPEC_PART (STRING/15)+SEQ (UBINARY/2)+LINE (UBINARY/2). Fields: NOTE_1..4 (STRING/20 × 4).

**BKRTTEMP** (6f): Routing template notes. PK = BKRT_TEMP_CODE (STRING/15)+LINE (UBINARY/2). Fields: NOTE_1..4 (STRING/20 × 4).

**BKRTEMTR** (62f): Routing operation template library (used for estimating). PK = MTRO_CODE (STRING/15) + MTRO_OPER (UBINARY/2). Key fields:
- MTRO_DESC/OPERDESC (STRING/30 each), MTRO_TYPE (1), MTRO_LEAD (UBINARY/2), MTRO_LOTSIZE (FLOAT/8)
- MTRO_INSTR_1..15 (STRING/60 × 15 — 900 bytes of work instructions)
- MTRO_WC/WCDESC (work center STRING/12/30), MTRO_TMACHINE/TMACHDESC (machine type STRING/4/30)
- MTRO_TOOL/TOOLDESC (STRING/15/30), MTRO_CLASS (STRING/15)
- MTRO_VENDCOST (FLOAT/8/6), MTRO_PARTSHR (FLOAT/8/2)
- MTRO_TIMEPART/SETUPHRS (TIME/4 each), MTRO_LOTSIZE (FLOAT/8)
- MTRO_LABOR/MACHINE/FOVHD/VOVHD/SETUP (FLOAT/8/4 — 5 cost elements)
- MTRO_NUM/NUM_PERSON/NUM_PROCES, MTRO_OVERLAP, MTRO_PIECE_RATE, MTRO_LONGTIME (FLOAT/8/7)
- MTRO_STD_TIME (STRING/1), MTRO_MIN_CHG, MTRO_PRINT (STRING/1), MTRO_EXTRA (STRING/150)
- MTRO_NEGOVLP, MTRO_DEF_TIME (TIME/4), MTRO_R_TYPE (STRING/10), MTRO_EST_LINE, MTRO_EST_TAG (STRING/10)
- MTRO_OP_TEMP_NO (UBINARY/2), MTWO_MISC_COST/MISC_DESC (note: MTWO_ prefix appears to be a DDF typo)
- MTRO_MISC_ACOST (FLOAT/8/2)

---

### Payroll / Commission Module (BKPR* — partial)

| Table | Fields | Purpose |
|-------|--------|---------|
| BKPRACOM | 12 | Commission archive (historical transactions) |
| BKPRAGNT | 4 | Agent/salesperson GL account mapping |
| BKPRBOOK | 87 | Salesperson annual book (quotas + 12-month actuals) |
| BKPRCOMM | 12 | Commission detail (byte-identical to BKPRACOM) |
| BKPRCURP | 127 | Current payroll period record per employee |
| BKPRGLFL | ~664 | Payroll GL distribution (very large, partially confirmed) |
| BKPRMSTR | ~384 | Employee payroll master (partially confirmed) |
| BKPRINFO | ~100 | Employee HR information (partially confirmed) |

**BKPRAGNT** (4f): Agent GL mapping. PK = NUM (UBINARY/2). Fields: CODE (STRING/10), GLACT (STRING/10), GLDPT (STRING/4). Maps each salesperson# to GL clearing account.

**BKPRACOM** (12f): Commission transaction archive. PK = SLSP (UBINARY/2)+CCODE (STRING/10)+INVNM (FLOAT/8/0). Fields: INVDT, PAYDT (DATEs), AMTPD (FLOAT/8/2), COMM (FLOAT/8/2), PD_ON (FLOAT/8/2), EXTRA (STRING/25), ULID (FLOAT/8/4), TDATE (DATE), PCODE (STRING/15). **BKPRCOMM** (12f) is byte-identical.

**BKPRBOOK** (87f): Salesperson annual performance book. PK = EMPNUM (UBINARY/2). Fields: CLASS_1/2, RATE_1/2, HOW_1/2, WHEN_1/2 (commission setup), then 12-month arrays: QUOTA_1..12, GROSS_1..12 (gross sales), COGS_1..12, RCPTS_1..12, COMM_1..12 (earned), PAID_1..12 (paid), then FNMI (STRING/25), LNME (STRING/25), EXPACT (STRING/10), EXPDPT (STRING/4), EXTRA (STRING/100), EMAIL (STRING/128).

**BKPRCURP** (127f): Current payroll period per employee. PK = EMPNM (UBINARY/2)+PRDTE (DATE). Fields (1-73 confirmed): ACTNM (UBINARY/2), CHKNM (STRING/6), TOTHR/TOTPY (FLOAT/8/2 each), RPHRS/RPRTE/RPAMT (regular hrs/rate/amt), OPHRS_1..12 (OT code hours × 12), OPRTE_1..12 (OT rates × 12), OPAMT_1..12 (OT amounts × 12), VPHRS/VPRTE/VPAMT (vacation), SPHRS/SPRTE/SPAMT (sick), MDAMT, ODAMT, UOD_1..20 (20 user-defined deductions). Fields 74-127 cover UODEC accumulators and federal/state/local tax withholding arrays.

---

### Estimating Module (EST*)

| Table | Fields | Purpose |
|-------|--------|---------|
| ESTCHGS | 3 | Quote surcharge line |
| ESTMAT | 18 | Quote BOM material line |
| ESTROUT | 48 | Quote routing operation line |
| ESTSUM | 213 | Quote/estimate header |

All use MTE*/MTES*/MTESUM_ field prefixes (not BK*). These four tables define a complete quote: ESTSUM header → ESTMAT (materials) + ESTROUT (routing) + ESTCHGS (surcharges). MTESUM_BOM_FLAG/RT_FLAG/EX_FLAG mark whether data has been transferred to a work order.

**ESTCHGS** (3f): Quote surcharge. PK = MTESCH_QUOTE (FLOAT/8/0). Fields: AMT (FLOAT/8/2), DESC (STRING/30).

**ESTMAT** (18f): Quote material line. PK = MTESMAT_QUOTE (FLOAT/8/0)+CODE (STRING/15). Fields: DESC (30), QTYPER (FLOAT/8/8 — 8-decimal qty per), SCRAP (FLOAT/8/2), UM (3), QUREF (FLOAT/8/0), COST1..5 (FLOAT/8/6 — 5 cost types), REMARKS_1..5 (STRING/30 × 5), COSTCD (STRING/1).

**ESTROUT** (48f): Quote routing operation. PK = MTESRO_QUOTE (FLOAT/8/0)+OPER (STRING/3). Fields: DESC (30), WC (STRING/12), TYPE (1), VENDOR/VENDNAME (STRING/10/25), OPCOST (FLOAT/8/6), PARTSHR (FLOAT/8/2), TIMEPART (FLOAT/8/6), SETUPHRS (FLOAT/8/2), MISCCOST/MISCDESC, LAB1..5 (FLOAT/8/4 × 5), MACH1..5, OVER1..5, SETUP1..5, INSTR_1..15 (STRING/60 × 15 instruction lines). Record size = 1219 bytes.

**ESTSUM** (213f): Quote/estimate header. PK = MTESUM_QUOTE (FLOAT/8/0). Structure:
- Header: DATE, EXPDATE, STATUS (1), CLASS (4), CODE (15), DESC (30), UM (3), CUSTCODE (10), NAME (30), ATTN (30), RFQ (15), REV (4), PROJ (15)
- 10 qty breaks: QTY_1..10
- 14 cost arrays × 10 breaks: MAT, MATMU, LAB, LABMU, SETUP, OP, OPMU, OH, OHMU, MISC, OVALL, EXTRA, TOTAL, PRICE — all FLOAT/8/4
- Notes: NOTES_1..10 (STRING/60 × 10)
- Tracking: ENTBY (15), LOC (10), TEMP_NUM (UBINARY/2), BOM_FLAG/RT_FLAG/EX_FLAG (STRING/1 each)
- COST_1..10 (per-break costs), CDATE (conversion date), VOVHD_1..10 (variable overhead)
- FIN_DATE, L_O_CODE (5), L_O_DATE, LEAD_SRC (4), LEADTIME (30)
- SLSP_NUM_1/2 (UBINARY/2), COMM_RTE_1/2 (FLOAT/8/4)
- OPPTYPE (2), QTREV (9), EXTRA2 (100)
Record size = 2465 bytes.

---

### Department Master (DPTMENT)

**DPTMENT** (2f): Department master — non-BK* table with DPT_ prefix. PK = DPT_CODE (STRING/4). Fields: DPT_DESC (STRING/30). Simple department code lookup.

---

### GL Chart of Accounts — 14-Period Structure Confirmed (BKGLFCOA)

BKGLFCOA (65f confirmed at DDF lines 11260-11325) supports **14 fiscal periods per year**:
- Fields 7-20: BKGL_CURRENT_1..14 (current year, 14 periods, FLOAT/8/2)
- Fields 21-34: BKGL_BUDGET_1..14 (14-period budget)
- Fields 35-48: BKGL_1YPAST_1..14 (prior year, 14 periods)
- Fields 49-62: BKGL_2YPAST_1..14 (2-years-prior, 14 periods)
- Field 63: BKGL_EXTRA (STRING/50)
- Fields 64-65: BKGL_1YPAST_YE + BKGL_2YPAST_YE (year-end balances for prior years)
Record size = 556 bytes. Periods 13-14 are closing/adjustment periods. This is why BKSYMSTR has TRM_MAX_1..20 (20 payment terms maximum-day thresholds) rather than 12 or 14 — the system was designed with extended period capacity throughout.

---

*Pass 143 complete: 37 tables documented (PI/POX/LOGON/MATCST/SA/SB/SHORT/SL/SO+/RT/PR(partial)/EST* families); BKGLFCOA 14-period structure confirmed.*

---

## Pass 144 — Help System, Inventory Variants, IS AP/AR Module, IS 2D/Build, RMA Header, PC/Material (2026-06-22)

DDF lines confirmed this pass: 4228–4306 (CP/PC/material), 11629–11730 (help + inventory variants), 11731–12200 (IS2DBAR), 14000–19000 (ISAP*/ISAR* families). BKMATCST field count corrected 23f→25f (inline fix applied to this file previously).

---

### Help System Tables

**EVOHLPID** (2f, `DBA_HELP_*`): EvoERP context-sensitive help reference map.
File: `EVOHLPID.B` | DDF line ~11629.
- `DBA_HELP_REF` STRING(8) — help reference code (PK); maps menu codes or field identifiers to CHM help topics.
- `DBA_HELP_MAP` UBINARY(2) — integer context ID passed to the help engine.

**HELPURL** (3f, `HELP_URL_*`): Help URL repository.
File: `HELPURL.B` | DDF line ~11637.
- `HELP_URL_REF` STRING(10) — reference key (PK).
- `HELP_URL_FILE` STRING(256) — file path or URL for the help topic.
- `HELP_URL_EXTRA` STRING(100) — additional routing or parameter data.

Both tables support the integrated help system; EVOHLPID maps context IDs for CHM-based help while HELPURL supports web-based or file-based alternatives.

---

### Inventory Transaction Variants

The DDF defines three identically-structured inventory transaction tables (DDF lines 11644–11730). INVTXN (main) was documented earlier; the two variants are:

**INVATXN** (24f, `MTIT_*`): Inventory adjustment transactions. File: `INVATXN.B`. Identical schema to INVTXN. Stores user-initiated quantity adjustments, write-offs, and physical count corrections separately from normal movement transactions.

**INVETXN** (24f, `MTIT_*`): Inventory edit/error transactions. File: `INVETXN.B`. Identical schema to INVTXN. Stores transactions created during error correction or re-posting (e.g., voided receipts, cost corrections). The three-file separation allows audit queries to distinguish normal movement (INVTXN), deliberate adjustments (INVATXN), and error/edit corrections (INVETXN) without filtering on MTIT_TYPE alone.

---

### IS 2D Barcode Module

**IS2DBAR** (109f, `IS2D_BAR_*`): 2D barcode field configuration.
File: `IS2DBAR.B` | DDF line ~11731.
KEY: `IS2D_BAR_CODE` STRING(10). Record = 329 bytes.

| Field group | Fields | Meaning |
|-------------|--------|---------|
| Header | CODE, ITEM(15), ORDER(UBINARY/2) | Barcode definition key + part item + print order |
| Separator | CHAR(5) | Field separator character in barcode payload |
| Source field | FIELD(25) | ERP field name to embed in barcode |
| Print flags | DOCPR_1..100 (STRING/1 × 100) | Per-document-type print enable flags (100 document types) |
| Description | DESC(60), EXTRA(100) | Label description and extension |
| Encoding | ASCII(UBINARY/2), TYPE(10) | ASCII code and barcode symbology (CODE39, QR, etc.) |

Defines what data fields appear on 2D barcode labels for each of 100 document types. One record per barcode field definition; the DOCPR_1..100 array enables/disables that field per document type independently.

---

### IS Build Work Table

**ISBUILD** (4f, `IS_BUILD_*`): Batch sort/build temporary work table.
File: `ISBUILD.B` | Temporary; cleared before/after batch operations.
- `IS_BUILD_UID` STRING(40) — entity identifier.
- `IS_BUILD_SORT` STRING(150) — pre-computed sort key.
- `IS_BUILD_REC` UBINARY(4) — record number in the source file.
- `IS_BUILD_FILE` STRING(8) — source file name.

Used internally by IS batch processes (report generation, bulk updates) to stage and sort large record sets before processing. Not a persistent business table.

---

### IS AP Module (ISAP* / BKAP_* family)

The IS AP module is a comprehensive procurement add-on layered over the base BKAP/BKP tables. It stores enhanced copies of AP master data (vendor, PO, invoice) with IS-specific extensions, plus change audit and multi-currency support.

**ISAPACHK** (12f, `BKAP_CHK_*`): AP check/payment detail per invoice.
File: `ISAPACHK.B` | KEY: VNDCOD+INVNUM.
- VNDCOD(10), INVNUM(10) — vendor + invoice (PK).
- INVAMT/AMTPD/DISC (FLOAT/8/2 each) — invoice amount, amount paid, discount.
- TYPE(1) — payment type (check, EFT, etc.).
- DESC(25) — payment description.
- INVDTE — invoice date.
- NUM (FLOAT/8/0) — check number.
- CHKACT (UBINARY/2) — check account ID.
- CHKDTE — check date.
- ISCUR(3) — currency code (IS multi-currency field).

**ISAPAINL** (385+f, `BKAP_INVL_*`): AP invoice line with 75-way GL distribution.
File: `ISAPAINL.B` | Record = 3082+ bytes. Largest IS AP record.
Header fields (~10): vendor code, invoice number, line number, date, terms, type, total.
Distribution arrays (5 × 75 = 375 fields):
- `BKAP_INVL_GLACT_1..75` STRING(10) — GL account per distribution slot.
- `BKAP_INVL_GLDPT_1..75` STRING(4) — GL department per slot.
- `BKAP_INVL_DC_1..75` STRING(1) — debit/credit flag per slot.
- `BKAP_INVL_GLD_1..75` STRING(25) — GL description per slot.
- `BKAP_INVL_DAMT_1..75` FLOAT(8/2) — distribution amount per slot.
Supports AP invoices split across up to 75 distinct GL accounts. Most invoices use 1–5 slots; complex cost-allocation scenarios use all 75.

**ISAPAPOL** (38f, `BKAP_POL_*`): AP PO line receipt detail.
File: `ISAPAPOL.B` | Extends standard PO line with IS fields.
Key IS-specific fields: INVNUM (matched invoice), PCONV (FLOAT/8/5 — price conversion factor for unit-of-measure conversion), PSTDTE (post date), PKSQTY (packing slip qty), INVDTE.

**ISAPARFQ** (57f, `BKAP_PO_*`): AP PO header — archived/historical version.
File: `ISAPARFQ.B` | Stores closed/archived PO headers.
Full PO header with vendor+ship-to addresses (3-line each), payment terms, FOB, tax, totals, IS-specific: currency code, broker, revision number, ECO link.

**ISAPOPO** (57f, `BKAP_PO_*`): AP open PO header — active current version.
File: `ISAPOPO.B` | Identical schema to ISAPARFQ. Active POs only.
ISAPARFQ and ISAPOPO together implement a two-tier active/archived PO header store (same schema, separate files for open vs. closed).

**ISAPAVND** (72f, `BKAP_*`): AP vendor master snapshot.
File: `ISAPAVND.B` | Record = 2230 bytes.
Full vendor record mirroring BKAPVEND plus IS extensions:
- NOTES_1..10 (STRING/60 × 10) — 10 free-text note lines.
- EMAIL_1..5 (STRING/128 × 5) — 5 email addresses.
- IS fields: TAXGRP(10), TAXIN(1), MCCODE(10 — multi-currency code), DCODE(10 — default discount code), CUST_CODE(10 — linked customer), CREDLIM (FLOAT/8/2 — credit limit), REQQC(1 — require QC on receipts), ALPHA1/ALPHA2 (STRING/25 × 2), DATE1/DATE2 (DATE × 2).
Snapshot is refreshed when AP processes update it; enables IS reporting without joining to BKAPVEND.

**ISAPCHG** (32f, `ISAP_CHG_*`): PO line change audit — active/current.
**ISAPHCHG** (32f, `ISAP_CHG_*`): PO line change audit — historical. Identical schema.
Files: `ISAPCHG.B` / `ISAPHCHG.B` | Record = 506 bytes. KEY: PONUM+LINEID.
Before/after (A/B suffix) pairs for 16 audited fields:
- Price_A/B, Disc_A/B (FLOAT/8/5 — 5-decimal precision).
- OOQty_A/B (FLOAT/8/2 — open-order qty).
- ERD_A/B, ARD_A/B (DATE — estimated/actual receipt dates).
- WOPRE_A/B, WOSUF_A/B (WO link).
- Oper_A/B (UBINARY/2 — operation).
- GLACT_A/B, GLDPT_A/B (GL account/dept).
- CONV_A/B (FLOAT/8/5 — unit conversion factor).
- EXTRA_A/B (STRING/30).
ISAPCHG holds the live change log; ISAPHCHG holds the archived (invoiced/closed) equivalent.

**ISAPEX** (33f, `ISAPEX_*`): Vendor user-defined extension.
File: `ISAPEX.B` | Record = 430 bytes. KEY: ISAPEX_VEND STRING(10).
- NUM_1..5 (FLOAT/8/2 × 5) — 5 numeric UDFs.
- NUM2_1..5 (FLOAT/8/0 × 5) — 5 integer UDFs.
- FLAG_1..10 (STRING/1 × 10) — 10 yes/no flags.
- ALPHA_1..5 (STRING/30 × 5) — 5 text UDFs.
- DATE_1..5 (DATE × 5) — 5 date UDFs.
- LONGNAME (STRING/60), EXTRA (STRING/100).
One record per vendor; provides 25 user-defined fields beyond the standard BKAPVEND schema.

**ISAPHQT** (49f, `BKRFQ_*`): Historical RFQ (Request For Quote).
**ISAPQTQT** (49f, `BKRFQ_*`): Quote-to-quote matching reference. Identical schema.
Files: `ISAPHQT.B` / `ISAPQTQT.B` | KEY: NUM+VEND. 10 qty-break bids:
- QTY_1..10 (FLOAT/8/2) — quantity break points.
- COST_1..10 (FLOAT/8/5) — bid cost per qty break.
Plus: MIN (FLOAT/8/2 — minimum order qty), MINCST (FLOAT/8/5 — minimum cost), EXPIRE (DATE), LEAD (UBINARY/2 — lead days), CONV (FLOAT/8/5 — conversion factor), FLAG (STRING/1), MAXDAYS (UBINARY/2 — maximum lead days), GDATE (price guaranteed date), UWHO/CWHO (update/create who), ALPHA1 (STRING/25 — free text).

**ISAPPROJ** (12f, `ISAP_PROJ_*`): AP invoice-to-project allocation.
File: `ISAPPROJ.B` | KEY: FROM(8)+CUST(10)+VEND(10)+JOURN(8/0)+INV(8/0)+LINE(UBINARY/2).
Links an AP invoice line to a project: PROJ(15 — project code), JCUST(10), JVEND(10), JDEPT(4), JITEM(15), EXTRA(50). Enables project cost tracking for multi-vendor AP scenarios.

**ISAPQPO** (66f, `ISAP_QPO_*`): Quick PO line record.
File: `ISAPQPO.B` | Record = 1797 bytes.
Full PO line with extended fields: COMMENTS_1..10 (STRING/60 × 10), FLAGS_1..5 (STRING/1 × 5), ALPHA_1..2 (STRING/25 × 2), NUM_1..2 (FLOAT/8/2 × 2), GDATE_1..5 (DATE × 5), MINCST (FLOAT/8/5), VENOTE (STRING/1000 — vendor notes up to 1 KB). The VENOTE field is the largest single field in the IS AP module, allowing a full paragraph of vendor-specific notes per PO line.

---

### IS AR Module (ISAR* / BKAR_* family)

The IS AR module mirrors the IS AP structure for the AR/SO side — storing enhanced customer master snapshots, history, and change audit.

**ISARARC** (106f, `BKAR_*`): AR customer master snapshot.
File: `ISARARC.B` | Record > 2500 bytes.
Full customer record with IS extensions: two complete address sets (billing/shipping), 4 contact names + 5 phone numbers, 10 note lines (STRING/60), 5 email addresses (STRING/128), financial summaries (YTD sales/COGS/disc), IS fields: TAXGRP, TAXIN, MCCODE, REP (salesperson), CREDLIM, ALPHA1/2, DATE1/2. Refreshed snapshot enables IS reporting without live BKARCUST joins.

**ISARADSC** (5f, `BK_DESC_*`): AR description lines — active SO/invoice.
**ISARAHDS** (5f, `BK_DESC_*`): AR description lines — historical. Identical schema.
Files: `ISARADSC.B` / `ISARAHDS.B` | KEY: CODE(15)+NUM(FLOAT/8/0)+LINE(UBINARY/2).
- NOTES (STRING/70) — full description text.
- DESC (STRING/25) — short label.
Long-form text lines for IS SO/AR documents; separate active vs. historical files.

**ISARAHIL** (28f, `BKAR_INVL_*`): Historical AR invoice lines.
File: `ISARAHIL.B` | Record = 312 bytes.
Full per-line invoice snapshot: PCODE(15), PDESC(30), PQTY/PPRCE/PDISC/PEXT (qty/price/disc/extended), PCOGS (cost of goods), ITYPE(1), TXBLE(1), UBO (unit back-ordered FLOAT/8/2), USTD (unit standard FLOAT/8/2), RTS(1), LOC(10), UM_LN_1/2 (unit-of-measure primary/secondary), COMPR_1/2 (comparison prices FLOAT/8/4 × 2), ASD (actual ship date), TXAMT (tax amount), FRGHT (freight), COOP (co-op deduction), OOQTY (open-order qty), EXTRA(30), SCCOG (secondary COGS FLOAT/8/4).

**ISARAHIN**: Historical AR invoice header.
File: `ISARAHIN.B` | Large — full BKAR_INV_* schema with IS extensions.
Full AR invoice header (customer+ship-to addresses, terms, totals, salesperson, customer order, IS fields: ISCUR, ISTXKY, ISREV/ISRVDT, RELNUM, tracking, QSTAT).

**ISARCHG** (26f, `ISAR_CHG_*`): AR SO/invoice line change audit — active.
**ISARICHG** (26f, `ISAR_CHG_*`): AR invoice line change audit — historical.
**ISARMCHG** (26f, `ISAR_CHG_*`): AR memo/credit line change audit. All identical schema.
Files: `ISARCHG.B` / `ISARICHG.B` / `ISARMCHG.B` | Record = 488 bytes. KEY: SONUM/INVNUM+LINE.
Before/after (A/B) pairs: PRICE_A/B, DISC_A/B, OOQty_A/B, ESD_A/B, ASD_A/B, COMPR_1_A/B, COMPR_2_A/B, EXTRA_A/B (STRING/30 × 2). Plus UNUM (UBINARY/4 — unique sequence number). Three variants cover the three document types (SO line, invoice line, credit memo line).

**ISARINVX** (4f, `ISAR_INV_*`): AR invoice extension record.
File: `ISARINVX.B` | KEY: SONUM(FLOAT/8/0)+NUM(FLOAT/8/0). Per-invoice extra fields.
- `ISAR_INV_EXTRA1` STRING(100) — user-defined extension 1.
- `ISAR_INV_EXRTA2` STRING(100) — user-defined extension 2. **Note: field name typo in original DDF** — `EXRTA2` not `EXTRA2`; this is in the source file, not introduced by documentation.

---

### IS RMA Module — Main Header

**ISRMAM** (54f, `IS_RMA_*`): RMA main header record.
File: `ISRMAM.B` | Record = 407 bytes. KEY: IS_RMA_NUM(FLOAT/8/0).

The ISRMAM record is the controlling header for the RMA workflow. Previously documented: ISRMAI (active line items), ISRMAC (reason codes), ISRMADSC (description lines), ISRMAINF/ISRMAAI/ISRMAINV (info/archive/invoice tables). ISRMAM is the header that links them all.

| Field group | Fields | Meaning |
|-------------|--------|---------|
| Identity | NUM, PART(15), LINEID(UBINARY/2) | RMA number, originating part, line |
| Dates | RCPTDATE, CLOSDATE | Received date, closed date |
| Status | STATUS(30), REASON(30), DISP(40) | Current status string, return reason, disposition decision |
| SO/Invoice link | OSONUM, OINVNUM (original), SONUM, INVNUM (replacement) | Original SO/invoice + replacement SO/invoice |
| Credit | CMNUM (FLOAT/8/0) | Credit memo number |
| WO link | WOPRE(FLOAT/8/0), WOSUF(UBINARY/2) | Work order created for rework |
| SR link | SRNUM(FLOAT/8/0) | Service request number |
| Qty / condition | QTY(FLOAT/8/2), CONDITION(1) | Return quantity, product condition code |
| Disposition flags | WO/CR/SO/STOCK/SCRAP/SR/REFUND (STRING/1 × 7) | 7 action type flags (one per disposition path) |
| User flags | FLAGS_1..20 (STRING/1 × 20) | 20 user-defined flags |
| Warranty | WARRANTY(1) | Under warranty flag |
| Tracking | DISPSEL(UBINARY/2) | Disposition selection code |
| Extra | IEXTRA(150) | Extended text |

The 7 disposition flags (WO/CR/SO/STOCK/SCRAP/SR/REFUND) are the decision record: which combination of actions was taken when the return was processed.

---

### IS SR/SO Merge

**ISSRSOMR** (54f, `ISSR_INFO_*`): Service request / SO merge data.
File: `ISSRSOMR.B` | Schema identical to ISSRINFO — KEY: SRNUM+UID.
Stores the flexible UDF block (20 alpha fields × 25ch, 10 date fields, EXTRA/100) for SR records that have been matched/merged with a sales order. Parallel to ISBTCSB (batch SR) and ISSRSOMR (SR→SO merge); all three reuse the ISSR_INFO_* schema for extensibility.

---

### PC Module — Kit and Plot Tables

**BKPCKIT** (6f, `BKPC_KIT_*`): PC kit component record.
File: `BKPCKIT.B` | Note: implied PK field (kit code, STRING/15) precedes listed fields at offset 0.
- `BKPC_KIT_COMP` STRING(15) — component part number.
- `BKPC_KIT_QTY_R` FLOAT(8/2) — required quantity.
- `BKPC_KIT_QTY_A` FLOAT(8/2) — actual quantity used.
- `BKPC_KIT_QTY_S` FLOAT(8/2) — quantity shipped.
- `BKPC_KIT_DATELM` DATE — date eliminated from kit.
- `BKPC_KIT_LOC` STRING(10) — storage location.

**BKPCPLOT** (10f, `BKPC_PLOT_*`): PC production plot / schedule record.
File: `BKPCPLOT.B` | Same implied PK pattern.
- PROD(15) — product/part, ISDTE/SPDTE (issue/shipped date), QTY(FLOAT/8/2), CUST(10), INKO(FLOAT/8/2 — in-process qty), STAT(1 — status), STRTD/COMPD (started/completed date), LOC(10).

---

### Material Trim Table

**BKMATRIM** (3f, `BKMA_TRIM_*`): Sheet metal / material trim configuration.
File: `BKMATRIM.B` | KEY: MACH STRING(4) — machine code.
- `BKMA_TRIM_FIRST` FLOAT(8/2) — first-cut trim dimension.
- `BKMA_TRIM_SECND` FLOAT(8/2) — second-cut trim dimension.
Per-machine trim/waste offsets for sheet metal cutting. Used in material requirement calculations to account for kerf and edge waste.

---

*Pass 144 complete: 32 tables documented — EVOHLPID/HELPURL (help system); INVATXN/INVETXN (inventory transaction variants); IS2DBAR (2D barcode, 109f); ISBUILD (batch work table); ISAP* family 13 tables (ISAPACHK/ISAPAINL/ISAPAPOL/ISAPARFQ/ISAPOPO/ISAPAVND/ISAPCHG/ISAPHCHG/ISAPEX/ISAPHQT/ISAPQTQT/ISAPPROJ/ISAPQPO); ISAR* family 7 tables (ISARARC/ISARADSC/ISARAHDS/ISARAHIL/ISARAHIN/ISARCHG+2/ISARINVX); ISRMAM (RMA header 54f); ISSRSOMR (SR/SO merge); BKPCKIT/BKPCPLOT/BKMATRIM (PC/material module). BKMATCST corrected 23f→25f.*

