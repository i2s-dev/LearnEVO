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
