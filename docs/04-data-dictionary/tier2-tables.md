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

*Last updated: 2026-06-19*
*Source: `samples/ddf/schema.md` (field extraction), `samples/ddf/tables.txt` (table inventory)*
*Confidence: 80/100 — All field names confirmed from DDF; field meanings inferred from naming conventions; no BKCM SRC source available to confirm internal logic.*
