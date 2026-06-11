# HELP-RESOURCES.md
# EvoERP Knowledge Base — Searchable Reference

**Purpose:** Answer abstract "how do I…" questions about EvoERP. Intended for users who
know what they want to accomplish but not which menu, table, or file is involved.

**How to use:** Search this file (Ctrl+F) for any keyword — module name, table name,
business concept, or term. Each section links to deeper documentation in `docs/`.

**Confidence ratings** are given per section. See `EVO-DECOMPILE-TODO.md` for the scale.

---

## QUICK LOOKUP — "How do I…"

| I want to… | Go to menu | See section |
|------------|-----------|-------------|
| Add a new customer | AR-A | [Customers](#accounts-receivable-ar) |
| Enter a customer invoice | AR-B (voucher) or SO module | [AR Vouchers](#ar-vouchers) |
| Record a customer payment | AR-C | [AR Payments](#ar-payments) |
| Add a new vendor | AP-A | [Vendors](#accounts-payable-ap) |
| Enter a vendor invoice | AP-B | [AP Vouchers](#ap-vouchers) |
| Print AP checks | AP-H (continuous) or AP-H-A (laser) | [AP Checks](#ap-check-printing) |
| Add a new inventory item | IN-B | [Inventory Items](#inventory-in) |
| Check inventory quantities | IN-A | [Inventory Inquiry](#inventory-in) |
| Create a sales order | SO-A | [Sales Orders](#sales-orders-so) |
| Create a work order | WO-A | [Work Orders](#work-orders-wo) |
| Enter labor / clock in | DC module or LW module | [Labor Entry](#data-collection-dc) |
| Run MRP | MR module | [MRP](#mrp-mr) |
| Close the month | GL / AR / AP / IN sequences | [Month-End](#month-end-close) |
| Set up a new user | SM module → user setup | [Users & Security](#users--security) |
| Print a report | Each module has its own reports | [Reporting](#reporting-engine) |
| Modify a report | RBDsgnr.exe (ReportBuilder) | [Modifying Reports](#modifying-reports) |
| Add a GL account | GL-A | [General Ledger](#general-ledger-gl) |
| Set up a routing | RO-A | [Routing](#routing-ro) |
| Build a BOM | BM module | [Bill of Materials](#bill-of-materials-bm) |
| View system defaults | AD-A (GL Defaults) | [System Defaults](#system-defaults) |

---

## MODULE REFERENCE

### Accounts Receivable (AR)

**What it does:** Manages customer accounts, invoices, payments, statements, and aging.

**Menu codes:** AR-A through AR-S (17 operations)

**Key operations:**
- **AR-A — Enter Customers:** Create or edit a customer record. Fields include customer code
  (10 chars), name, billing/shipping address, default GL sales account, payment terms,
  credit limit, salesperson(s) with commission rates, price code, discount code, tax group,
  backorder policy, and contact manager fields. The customer code is the primary key used
  everywhere else in the system.
- **AR-B — Enter Vouchers:** Enter miscellaneous AR charges, credit memos, cash transactions,
  and beginning balances. Up to 10 GL distribution lines per transaction. Types: A (voucher),
  B (credit memo), C (cash), D/E (beginning balance). Multi-currency supported.
- **AR-C — Record Payments:** Record customer payments, apply to invoices (oldest-first auto
  or manual selection), enter deposits, process NSF reversals (negative amounts), split
  payments across customers. Integrates with X-Charge for credit card processing.
- **AR-D — Charge Interest:** Automatically generates interest charges for past-due customers
  who have "Charge Interest = Y" on their customer record.
- **AR-E — Print Statements:** Aged statements showing open invoices and payments.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKARCUST | Customer master — 106 fields including code, name, address (3 lines + extended), GL sales account, class, salesperson 1/2 with commissions, territory, price/discount codes, terms, taxable status, tax group, credit limit, start date, contact info, website |
| BKARINV | AR Invoice header — 84 fields including invoice#, customer, ship-to, tax, totals, GL accounts, COGS tracking |
| BKARINVL | AR Invoice lines — 28 fields including invoice#, counter, product code, qty, price, tax, freight, GL account |
| ARTTEMP | AR temporary records — 12 fields (used during payment posting) |

**Confidence: 72/100** — Menu ops and primary tables confirmed; full field meanings from DFM + SRC analysis. Payment application logic partially traced.

---

### Accounts Payable (AP)

**What it does:** Manages vendor accounts, purchase invoices, check runs, and 1099 processing.

**Menu codes:** AP-A through AP-U (19 operations)

**Key operations:**
- **AP-A — Enter Vendors:** Create/edit vendor records. Equivalent of AR-A for vendors.
  Primary table: BKAPVEND.
- **AP-B — Enter Vouchers:** Enter vendor invoices. Supports purchase order matching.
  Up to 26 GL distribution accounts per invoice. Primary table: BKAPINVL.
- **AP-E — Print Vouchers Due:** Aging report of unpaid invoices.
- **AP-H / AP-H-A — Print Checks:** The check printing process works as follows:
  1. A check run file (BKAPCHKF) is built first (separate step — select which invoices to pay)
  2. AP-H prints continuous-form checks; AP-H-A prints laser checks using RTM templates
     (BKAPHA1.RTM, BKAPHA2.RTM, BKAPHA3.RTM)
  3. After printing, the program posts to GL (debit AP control, credit bank account),
     updates vendor last-payment date, reduces outstanding invoice amounts,
     and deletes records from BKAPCHKF
  4. Checks with zero or negative totals are automatically voided
  5. Check amounts are converted to alpha text ("five thousand dollars") by GET.ALPHA routine
- **AP-P — Generate Recurring Vouchers:** Batch-create repeating invoices.
- **AP-S — 1099 Forms:** Year-specific programs (APS1999, APS2000, TAPS2000 etc.).

**Multi-currency:** Fully supported in AP. Exchange rates are applied at check print time;
foreign exchange gain/loss is posted to a separate GL account.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKAPVEND | Vendor master — 26+ fields: code, name, address, payment history, purchase metrics |
| BKAPINVL | AP invoice/voucher — 36+ fields: vendor, invoice#, date, description, terms, amount, 26 GL distribution accounts |
| BKAPCHKH | AP check header — 12 fields: vendor, invoice#, amounts, check date, check number |
| BKAPCHKF | Check run file — in-progress batch of checks to print |
| BKAPINVT | AP invoice transactions — updated when checks are posted |
| BKAPPO | Purchase order header |
| BKAPPOL | Purchase order lines |

**Confidence: 72/100** — Full source code (Bkaph.SRC, Bkapha.SRC) analyzed. Check printing logic fully traced. Voucher entry logic not from source.

---

### Inventory (IN)

**What it does:** Manages item master records, on-hand quantities, cost layers (FIFO/LIFO/Average),
location tracking, physical counts, and inventory transactions.

**Menu codes:** IN-A through IN-T (40 operations — largest non-SO module)

**Key operations:**
- **IN-A — Inventory Inquiry:** View current stock, on-hand qty, locations, cost, open orders.
  Form: T7INA.DFM with tabs for Item Number, Type, Main, Characteristics, Controls.
- **IN-B — Enter Inventory:** Create/edit item master records.
- **IN-G — Print Labels:** Inventory labels.
- **IN (physical count area):** Physical inventory is a separate PI module.

**Item master fields (BKICMSTR — 64 fields, key subset):**
- `BKIC_PROD_CODE` — Part number (primary key)
- `BKIC_PROD_DESC` — Description
- `BKIC_PROD_TYPE` — Type code
- `BKIC_PROD_UOM` — Unit of measure (stock)
- `BKIC_PROD_PUOM` — Purchase UOM
- `BKIC_PROD_PRCUOM` — Price UOM
- `BKIC_PROD_CLASS` — Class code
- `BKIC_PROD_CAT` — Category code
- `BKIC_PROD_COST` — Standard/current cost
- `BKIC_PROD_PRICE` — Base price
- `BKIC_PROD_UOH` — Units on hand (quantity)
- `BKIC_PROD_REODR` — Reorder level
- `BKIC_PROD_MINOQ` — Minimum order quantity
- `BKIC_PROD_LTDAYS` — Lead time (days)
- `BKIC_PROD_WEIGHT` — Weight
- `BKIC_PROD_BIN` — Bin location
- `BKIC_PROD_DRAW` — Drawing number
- `BKIC_PROD_MRPSW` — MRP planning switch
- GL accounts for COGS, inventory, variance

**Inventory transaction types (INVTXN):**
- A = Adjustment, S = Shipment (sales), P = PO Receipt, J = PO Job Receipt,
  W = WO Receipt (finished goods), I = WO Issue (material), Q = QC Receipt,
  O = Out-Process, C = Cost Change

**Transaction consolidation** (BKLME.SRC): Rolls up individual transactions by type into
summary records for period-end. Lot/serial tracked items are excluded from consolidation.

**Confidence: 65/100** — Item master fields from schema; BKLME.SRC fully analyzed. FIFO/LIFO bucket logic identified (BUCKETS, DBAFIFO tables) but not fully traced.

---

### Sales Orders (SO)

**What it does:** Manages the full customer order lifecycle — entry, acknowledgment, picking,
shipping, invoicing, and history.

**Menu codes:** SO-A through SO-T (48 operations — most of any module)

**Key operations:**
- **SO-A — View/Enter Sales Orders:** Main order entry form (T7SOA.DFM). Fields: SO#,
  customer, name/address, ship-via, terms, job#, description, line items. Buttons for:
  CC (credit card), Stock inquiry, Info, Recurring, Clock In, Issue Material, Print S/R.
- **SO acknowledgments, packing slips, shipping labels** — SO-B through SO-G area
- **SO invoicing** — Separate step from shipping; generates AR invoice
- **SO quotes** — QU module (quote entry → conversion to SO)

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKSOX | SO extract / invoice — 25 fields: company, invoice#, date, customer code/name, subtotal, tax, freight, deposit, retention, total, currency, SO#, customer PO, terms, ship date, shipper, job#, tax code, dates |
| BKSOXH | SO header variant — same 25-field structure |
| BKSONOTE | SO notes |
| BKSOPO | SO → PO cross-reference |

**Confidence: 62/100** — Menu ops and form confirmed; table field mapping from schema. Business logic (order→ship→invoice chain) not fully traced.

---

### Work Orders (WO)

**What it does:** Manages production work orders from creation through labor entry, material
issues, and close-out.

**Menu codes:** WO-A through WO-T (31 operations)

**Key operations:**
- **WO-A — Enter Work Orders:** Create work orders. Form T7WOA.DFM. Fields: WO number,
  location, part#, description, qty to make, qty completed, start date, finish date, due
  date, class, priority, status. Action buttons: Copy WO, ECO, Material Issues, Labor,
  Outside Processes, Notes, Links.
- **WO-B — Release Work Orders:** Release to shop floor.
- **WO-C — Print Traveler:** Shop traveler document.
- **WO-D — Pick List:** Material pick list.
- **Labor entry:** DC module (BKDCA.SRC) or LW module for manual labor entry.
  Labor flows: Clock-in (type O) → Clock-out (type C) → Batch post to GL.
  Labor types: P (production), S (setup), A (auto-close).
- **WO-K-F — Edit Sequence Dates:** Modify operation start/finish dates.
- **WO close:** Closes WO, calculates variance between estimated and actual costs.

**Work order status codes:**
- S = Scheduled, F = Firmed, R = Released, C = Closed, X = Cancelled

**Work order priority codes:** 1, 2, 3

**Primary tables:**

| Table | Purpose |
|-------|---------|
| WORKORD | WO master — 74 fields: WO prefix/suffix (key), qty to make, priority, class, status, sched/actual start/finish dates, completed qty, estimated costs (labor/material/overhead/outside), actual costs (same), customer order, 10 instruction lines, scrap qty |
| WORKCHG | WO change log — 25 fields: WO ref, change code, change date, user, before/after: priority, status, class, description, qty, dates |
| WOBOM | WO bill of materials |
| WOMAT | WO material issues |
| WOLABOR | WO labor entries |
| WOROUT | WO routing / production output |
| WORKCTR | Work center master |
| MACHINE | Machine master |
| TOOL | Tool master |

**Confidence: 68/100** — BKAWLB.SRC (WO schedule report) + BKDCA.SRC (DC labor) fully analyzed. WO master table fully confirmed. Full lifecycle logic partially traced.

---

### General Ledger (GL)

**What it does:** Chart of accounts, journal entries, period-end balances, budgets, and multi-period reporting.

**Menu codes:** GL-A through GL-P (16 operations)

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKGLCOA | Chart of accounts — 65 fields: account code, department, description, type, CR/DR designation, current balance periods 1–14, budget periods 1–14, prior-year balances, year-end balances |
| BKGLTRAN | GL transactions / journal entries |
| BKGLTEMP | GL posting temporary (used during AP/AR/PR posting) |
| BKGLCHK | GL check history records |

**GL posting** happens automatically when AP checks are printed, AR payments are recorded,
payroll is run, and inventory is transacted. Programs use BKGLTEMP as a staging area,
then move records to BKGLTRAN on confirmation.

**BKGLCOA** stores 14 periods of balance per account (periods 1–14 cover 12 months + 2
adjustment periods). Budget amounts are stored alongside actuals in the same record.

**Confidence: 62/100** — Table structure confirmed from schema. GL posting logic partially traced through AP source code. Journal entry entry/posting workflow not directly analyzed.

---

### Purchase Orders (PO)

**What it does:** Manages vendor purchase orders from creation through receipt and AP matching.

**Menu codes:** 29 operations

**Key workflow:**
1. Create PO (PO-A area) → BKAPPO header + BKAPPOL lines
2. Receive goods (IN module receipt) → creates inventory transaction type P
3. AP matching → creates BKAPINVL voucher matching PO lines

**Primary tables:** BKAPPO (header), BKAPPOL (lines) — shared with AP module.

**Confidence: 55/100** — Tables identified; workflow chain inferred from MRP source code analysis; not directly traced.

---

### MRP / Material Requirements Planning (MR)

**What it does:** Calculates planned purchase orders and work orders based on demand (sales
orders, forecasts) vs. supply (on-hand, open POs, open WOs) across the full BOM structure.

**Menu codes:** 12 operations

**MRP calculation stages** (from BKMRF.SRC — fully analyzed):
1. **Demand loading:** Scan BKARINVL for open SO line items → create negative requirements
2. **Supply loading — POs:** Scan BKAPPOL for open POs → create positive supply records
3. **Supply loading — WOs:** Scan WORKORD for S/F/R status WOs → create supply records
4. **BOM explosion:** For each required parent item, explode BOM (BKBMMSTR) to components.
   Phantom parts (type P) are exploded inline. Scrap/yield factors applied.
5. **Reorder levels:** Check BKICMSTR reorder levels; generate planned orders below minimum.
6. **Action codes:** Assign Expedite/Delay/Review based on planned date vs. need date.

**Key MRP fields in BKICMSTR:**
- `BKIC_PROD_MRPSW` — MRP planning switch ('Y' = include in MRP)
- `BKIC_PROD_REODR` — Reorder level (minimum stock trigger)
- `BKIC_PROD_MINOQ` — Minimum order quantity
- `BKIC_PROD_LTDAYS` — Lead time in days (used for planned order date calculation)

**Primary tables:**

| Table | Purpose |
|-------|---------|
| MTMRP | MRP output — planned order recommendations (type PO or WO) |
| BKMRPFC | MRP forecast input (projected demand beyond open SOs) |
| BKMRPSW | MRP switch file (tracks which run is in progress) |

**Confidence: 72/100** — BKMRF.SRC fully analyzed and documented. Algorithm completely understood. Output table (MTMRP) identified but field-level detail not extracted.

---

### Routing (RO)

**What it does:** Defines the manufacturing process sequence (operations) for each part —
which work centers, machines, tools, and times are required to make the item.

**Menu codes:** 19 operations

**Routing structure** (from BKROA.SRC — fully analyzed):
- A routing belongs to one part number.
- Each routing has N operations (sequences), numbered in ascending order.
- Each operation specifies: work center, optional machine, optional tool, optional vendor
  (for outsourced/type-L operations), setup hours, run time per piece, scrap %.
- Up to 4 lines of operation notes per sequence.
- Routing templates (BKRTTEMP) allow predefined operations to be selected and auto-sequenced.
- Copy routing (F3) duplicates an existing routing onto a new part.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| ROUTING | Routing master — operations per part |
| WORKCTR | Work center master |
| MACHINE | Machine master |
| TOOL | Tool master |
| BKRTTEMP | Operation templates |
| BKRTSPEC | Operation notes/specs |

**Confidence: 75/100** — BKROA.SRC fully analyzed. Table relationships confirmed. Work center / machine / tool masters identified.

---

### Bill of Materials (BM)

**What it does:** Defines the component structure of manufactured items — what parts and
quantities go into each parent assembly.

**BOM structure** (from BKBMMSTR — 26 fields per component row):
- Parent product code + component product code (composite key)
- Quantity required per parent
- Scrap rate
- Operation sequence (which routing operation consumes this component)
- Revision level
- Component type (N=normal, P=phantom, etc.)
- Pricing and costing flags

**Phantoms (type P):** BOM components that are themselves assemblies but not stocked
separately. MRP explodes through phantoms transparently — the phantom's components
become direct requirements of the parent.

**BOM explosion** is used by: MRP (BKMRF.SRC), WO creation (copies BOM to WOBOM),
and the BOM Tree analysis tool (BOMTREE.RWN).

**Confidence: 62/100** — BKBMMSTR schema confirmed; phantom handling confirmed from MRP source. Full BOM explosion logic traced through MRP code.

---

### Data Collection (DC)

**What it does:** Shop-floor labor and production data entry, typically via terminals or
handheld devices. Records employee clock-in/out, parts made, and scrap.

**Key workflow** (from BKDCA.SRC — fully analyzed):
1. Employee enters their employee number (validated against BKPRMSTR)
2. Employee enters work order number and operation sequence
3. Clock-in: creates open (type O) record with start time and shift
4. Clock-out: closes record with finish time, calculates run hours
5. Employee reports parts made and scrapped
6. Auto-close feature: if employee starts a new job while previous is open, previous
   is automatically closed (if YN[228]='Y')
7. On exit (F9): pending labor moves from BKDCTLAB → BKDCPLAB for batch GL posting

**Shift configuration:** 3 shifts defined in BKDCSHFT (start/finish times per shift).

**Labor types:**
- P = Production (parts made)
- S = Setup
- A = Auto-close (system-generated close of previous job)

**Status codes:** O = Open (clocked in), C = Closed (clocked out), P = Posted (GL posted), N = New

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKDCSHFT | Shift definitions (3 shifts × start/finish time) |
| BKDCTLAB | DC temporary labor — in-progress entries (type O = open, C = closed) |
| BKDCPLAB | DC pending labor — awaiting batch GL post |

**Confidence: 78/100** — BKDCA.SRC fully analyzed. Complete workflow documented.

---

### Payroll (PR)

**What it does:** Employee master records, payroll calculation, check printing, direct deposit,
W-2, 1099, and tax filing.

**Menu codes:** 29 operations

**Primary table:** BKPRMSTR — 384 fields (largest practical table in the system). Contains
all employee data: personal info, pay rates, deductions, tax withholding settings,
year-to-date totals for every pay category.

**Confidence: 50/100** — Table identified and field count confirmed; payroll logic not yet traced from source.

---

### Physical Inventory (PI)

**What it does:** Periodic physical count process — freeze inventory, enter counts, calculate
and approve variances, post adjustments.

**Standard cycle:**
1. Freeze inventory (prevents transactions during count)
2. Print count sheets
3. Enter physical counts
4. System calculates variance (counted - system on-hand)
5. Review and approve variances
6. Post adjustments (creates INVTXN type A)

**Primary tables:** BKPI\* (7 tables)

**Confidence: 48/100** — Workflow inferred from CHM help content; tables identified by name but not fully analyzed.

---

### Estimating (ES)

**What it does:** Pre-sales cost estimating for quoted work.

**Primary tables:** BKES\* (3 tables)

**Confidence: 35/100** — Tables identified; no source or DFM analysis done.

---

## SYSTEM & ADMINISTRATION

### Users & Security

**How users are stored:** `AHSYLOG` table. One record per user.

| Field | Size | Purpose |
|-------|------|---------|
| AHSY_USER_LEVL | 2 chars | Role / security level |
| AHSY_USER_MENU | 4 chars | Starting menu code (where user lands after login) |
| AHSY_USER_CTRL | 1 char | Control flag |
| AHSY_USER_ACCES_1 through _20 | 1 char each | Module permission flags (20 modules) |

**Login process:** EvoERPmenu.rwn → EVOMENU_LOGIN.DCY (form) → validates against AHSYLOG
→ EVOMENU_SELCOMP.DCY (company select) → main menu.

**Session tracking:** Active logins stored in BKLOGON (10 fields: code, password, company,
program, printer, in-use flag, security level, menu, submenu, current printer).

**Password storage:** Encrypted via `ENCRYPTSTR` TAS keyword. Algorithm not decoded.

**To add a new user:** SM module (System Maintenance) → user setup function. Creates record
in AHSYLOG with role, starting menu code, and 20 access flags.

**Confidence: 65/100** — AHSYLOG schema confirmed. Login flow traced. Access flag → module mapping not decoded.

---

### System Defaults

**BKSYMSTR** — 286-field global configuration table. One record. Contains:
- AR/AP/PO auto-increment invoice numbers
- Tax rate
- 20 payment terms (each: amounts, type, days, EOM flag, max)
- Check bank accounts, balances, GL account names, GL department codes
- AR/AP/PR check accounts
- AR sales order number counter
- Freight GL accounts
- AR aging bucket definitions (4 buckets: days thresholds)
- PR (payroll) optional deduction settings
- Currency codes

**Access:** AD-A (GL Defaults / Administration defaults)

**Confidence: 68/100** — Field count and major categories confirmed from schema; individual field meanings inferred from naming conventions.

---

### Month-End Close

**Standard sequence (from CHM help):**
1. **AR:** Print aged trial balance; charge interest (AR-D) if applicable; print statements (AR-E)
2. **AP:** Print aged payables; review unposted vouchers
3. **IN:** Run inventory consolidation (BKLME.SRC — consolidates transactions by type); print inventory value report
4. **GL:** Verify all batches posted; run GL trial balance; post any adjusting journal entries
5. **PR:** Payroll period-end (if payroll period ends); run payroll reports
6. **GL Close:** Lock the period in GL to prevent further postings to it
7. **Sales Tax:** Transfer sales tax liability to tax authority (if applicable)

**Confidence: 55/100** — Workflow confirmed from CHM help content; exact GL period-lock mechanism not traced from source.

---

### Year-End Close

**Standard sequence:**
1. Print all year-end reports (AR/AP aging, GL trial balance, payroll YTD)
2. Generate W-2 forms (PR module)
3. Generate 1099 forms (AP-S)
4. Close payroll year
5. GL year-end close (carries forward retained earnings, zeros income/expense accounts)
6. Archive and purge old transaction history (built-in archiving tools)
7. Set new budget figures for next year

**Confidence: 48/100** — Workflow from CHM; specific GL year-end table operations not traced.

---

## REPORTING ENGINE

### How Reports Work

1. A TAS program (`.RWN`) calls `EXEC_RB` (execute ReportBuilder) with `RTM_FN` pointing
   to a `.RTM` file.
2. The program first sets up a data buffer using `SETUP_REPORT_BUFF`, `OUTPUT_REPORT_DATA`,
   and `UPDATE_REPORT_DATA` — these pipe data from the TAS program into the RTM template.
3. The RTM template (Nevrona ReportBuilder, TPF0 binary format) defines the layout:
   bands (header, detail, footer), labels, database text fields bound by name to the
   TAS data buffer, sub-reports, and page/printer settings.
4. ReportBuilder renders and sends to printer, screen, or file based on `USE_PRINTER`,
   `PRINT_TO_FILE`, and related settings.
5. PDF output goes to `C:\ISTS\PDFS\` on the local workstation.

### Modifying Reports

**To edit an existing report:**
1. Open `RBDsgnr.exe` (Nevrona ReportBuilder stand-alone designer, located at `C:\ISTS\`)
2. Open the `.RTM` file from `\\I2S109-SOLIDCRM\DBAMFG$\` (read the file name from the
   calling `.RWN`'s source — if source available — or from the `rtm_callers.csv` index)
3. Add/remove bands, labels, and database text fields
4. Database text fields are bound to the TAS data buffer by field name — use names that
   match what the TAS program puts into the buffer (e.g., `BKAP_CHK_INVNUM`)
5. Save and test

**Confidence for modifying reports: 72/100** — RTM format confirmed; designer tool confirmed; data binding mechanism confirmed from AP source analysis. Full field list per report not yet extracted.

### Known Report Templates

| RTM File | Module | Purpose |
|----------|--------|---------|
| BKAPHA1.RTM | AP | AP check — laser format 1 |
| BKAPHA2.RTM | AP | AP check — laser format 2 |
| BKAPHA3.RTM | AP | AP check — laser format 3 |
| ENARE4.RTM | AR | AR aged statement |
| t7ing1.rtm | IN | IN-G inventory labels |

*(Full RTM cross-reference in `samples/rtm_callers.csv`)*

---

## TABLE QUICK-REFERENCE

One-liner per table. For full field lists see `samples/ddf/schema.md`.

| Table | File | Module | Purpose | Key Fields |
|-------|------|--------|---------|------------|
| AHSYLOG | AHSYLOG.B | Security | User accounts | AHSY_USER_LEVL, AHSY_USER_MENU, AHSY_USER_ACCES_1..20 |
| ARTTEMP | ARTTEMP.B | AR | AR temp transactions | Customer, transaction#, type, amounts |
| BKABCUST | BKABCUST.B | AB | AB module customer | Start/expiry dates, period, warning |
| BKABVEND | BKABVEND.B | AB | AB module vendor | Serial#, registered name |
| BKACTRPT | BKACTRPT.B | AC | AC activity reports | Type, name, RTM template, part/class/cat ranges |
| BKARCUST | BKARCUST.B | AR | Customer master | Code (PK), name, address, GL sales acct, terms, credit limit, salesperson |
| BKARINV | BKARINV.B | AR | AR invoice header | Invoice# (PK), customer, ship-to, subtotal, tax, total, GL accts |
| BKARINVL | BKARINVL.B | AR | AR invoice lines | Invoice#, counter (PK), product, qty, price, tax, GL |
| BKAPVEND | BKAPVEND.B | AP | Vendor master | Vendor code (PK), name, address, payment history |
| BKAPINVL | BKAPINVL.B | AP | AP invoice / voucher | Vendor, invoice# (PK), date, amount, 26 GL distribution accounts |
| BKAPCHKH | BKAPCHKH.B | AP | AP check header | Vendor, invoice#, amounts, check date, check# |
| BKAPCHKF | BKAPCHKF.B | AP | AP check run file | In-progress check batch |
| BKAPINVT | BKAPINVT.B | AP | AP invoice transactions | Updated when checks post |
| BKAPPO | BKAPPO.B | PO | PO header | PO# (PK), vendor, dates, status |
| BKAPPOL | BKAPPOL.B | PO | PO lines | PO#, line# (PK), item, qty, price |
| BKBMMSTR | BKBMMSTR.B | BM | BOM components | Parent product, component (PK), qty required, scrap rate, operation |
| BKDCSHFT | BKDCSHFT.B | DC | Shift definitions | Shift# (PK), start time, finish time |
| BKDCTLAB | BKDCTLAB.B | DC | Temporary labor | Employee, WO, operation, status (O/C) |
| BKDCPLAB | BKDCPLAB.B | DC | Pending labor | Awaiting batch GL post |
| BKGLCOA | BKGLCOA.B | GL | Chart of accounts | Acct code, dept (PK), description, type, balances 1–14, budgets |
| BKGLTRAN | BKGLTRAN.B | GL | GL journal entries | Date, account, dept, debit, credit, reference |
| BKGLTEMP | BKGLTEMP.B | GL | GL posting temp | Used during AP/AR/PR posting |
| BKGLCHK | BKGLCHK.B | GL | GL check history | Posted check records |
| BKICMSTR | BKICMSTR.B | IN | Item master | Product code (PK), description, type, UOM, cost, price, on-hand qty, reorder level, lead time, MRP switch |
| BKICLOC | BKICLOC.B | IN | Inventory locations | Product, location (PK), qty |
| BKLOGON | BKLOGON.B | Security | Active sessions | Code (PK), company, program, printer, in-use flag, security level, menu |
| BKMRPFC | BKMRPFC.B | MR | MRP forecast | Forecasted demand input |
| BKMRPSW | BKMRPSW.B | MR | MRP switch file | Run state tracking |
| BKPRMSTR | BKPRMSTR.B | PR | Payroll master | Employee (PK), all pay/deduction/YTD data — 384 fields |
| BKRTTEMP | BKRTTEMP.B | RO | Routing op templates | Predefined operations for routing entry |
| BKRTSPEC | BKRTSPEC.B | RO | Routing specs/notes | Operation notes (4 lines per op) |
| BKSONOTE | BKSONOTE.B | SO | Sales order notes | SO#, note text |
| BKSOPO | BKSOPO.B | SO | SO → PO link | Cross-reference: which SO generated which PO |
| BKSOX | BKSOX.B | SO | SO invoice extract | Invoice#, customer, subtotal, tax, freight, total, SO#, ship date |
| BKSYMSTR | BKSYMSTR.B | System | Global config | AR/AP/PO counters, tax rate, 20 terms, check accounts, aging buckets — 286 fields |
| BKYSMSTR | BKYSMSTR.B | System | Global config #2 | Second system master (YN flags array) |
| BUCKETS | BUCKETS.B | IN | FIFO cost layers | Cost bucket tracking per item |
| CALENDAR | CALENDAR.B | WO/MR | Shop calendar | Work days and holidays |
| INVTXN | INVTXN.B | IN | Inventory transactions | Item, type (A/S/P/J/W/I/Q/O/C), date, qty, cost |
| ISNOTES | ISNOTES.B | Notes | EvoNotes records | Append-only note text + metadata |
| LOT | LOT.B | IN/WO | Lot master | Lot numbers and attributes |
| MACHINE | MACHINE.B | WO/RO | Machine master | Machine code, description, work center |
| MTMRP | MTMRP.B | MR | MRP planned orders | Planned PO and WO recommendations |
| ROUTING | ROUTING.B | RO | Routing master | Part + operation sequences |
| SCRAP | SCRAP.B | WO | Scrap codes | Scrap reason codes |
| SERIAL | SERIAL.B | IN/WO | Serial number master | Serial numbers and history |
| TOOL | TOOL.B | WO/RO | Tool master | Tool codes and descriptions |
| WOBOM | WOBOM.B | WO | WO BOM copy | BOM snapshot at WO creation |
| WOLABOR | WOLABOR.B | WO | WO labor entries | Employee, hours, operation, date |
| WOMAT | WOMAT.B | WO | WO material issues | Parts issued to WO |
| WORKCTR | WORKCTR.B | WO/RO | Work center master | Work center code, description, capacity |
| WORKCHG | WORKCHG.B | WO | WO change log | Before/after: priority, status, dates, qty |
| WORKORD | WORKORD.B | WO | WO master | WO# (PK), part, qty, dates, status, priority, estimated/actual costs |
| WOROUT | WOROUT.B | WO | WO production output | Parts received/completed per operation |

---

## KEYWORD / TERM GLOSSARY

| Term | Definition |
|------|-----------|
| **Btrieve** | The Pervasive database engine storing all EVO data in `.B` files |
| **BOM** | Bill of Materials — the component list for a manufactured item |
| **Chart of Accounts** | BKGLCOA — the list of GL accounts with balance periods |
| **Class code** | User-defined grouping for items, customers, vendors |
| **Cost layer** | A FIFO/LIFO bucket storing cost at a specific receipt date (BUCKETS table) |
| **DCY** | Data dictionary / compiled schema file — encrypted TAS format |
| **DDF** | Data Definition Files — Pervasive schema files (FILE.DDF, FIELD.DDF, etc.) |
| **DFM** | Delphi Form — the plaintext UI layout file paired with each RWN |
| **ENCRYPTSTR** | TAS keyword that encrypts a string; used for password storage |
| **EXEC_RB** | TAS keyword that executes a ReportBuilder report (calls RTM file) |
| **FIFO** | First-In-First-Out inventory costing method |
| **GL distribution** | Splitting a transaction across multiple GL accounts |
| **ISJAVA** | Task queue table for TAS → Java integration |
| **J7\*** | i2 Systems customer-specific customization modules |
| **lot tracking** | Tracking inventory by lot number (LOT table) |
| **MRP** | Material Requirements Planning — calculates what to buy/make and when |
| **MTMRP** | MRP output table — planned order recommendations |
| **open PO** | A purchase order not yet fully received |
| **outside process** | A WO operation sent to an external vendor (type L routing) |
| **phantom** | BOM component that is an assembly but not stocked (type P) |
| **Pervasive PSQL** | The Btrieve database server |
| **posting** | Moving temporary (staged) transaction records to permanent GL records |
| **RTM** | ReportBuilder template — the layout file for a report |
| **RUN** | TAS Pro 6 compiled program file (partially readable strings) |
| **RWN** | TAS Pro 7 compiled + encrypted program file |
| **scrap rate** | Percentage of component wasted in manufacturing (in BOM) |
| **SRC** | TAS Pro 4GL source code file (plaintext) |
| **standard cost** | Pre-set cost for an inventory item (vs. actual cost) |
| **TAS Pro 7** | The 4GL runtime engine (`tp7runtime.exe`) that runs all EVO programs |
| **TPF0** | The binary format magic bytes of Nevrona ReportBuilder `.RTM` files |
| **tp7runtime.exe** | The TAS Professional 7 interpreter — runs all `.RWN` and `.RUN` programs |
| **UPDTP7.EXE** | EvoUpdate binary patcher |
| **UOM** | Unit of Measure |
| **variance** | Difference between standard cost and actual cost; also between WO estimated vs. actual |
| **voucher** | An AP or AR transaction record (invoice entry) |
| **WHOAMI.DBA** | 35-byte workstation identity token read by tp7runtime.exe |
| **work center** | A production resource (machine group, labor area) with capacity; WORKCTR table |
| **WO** | Work Order — a manufacturing job order |
| **YN flag** | A boolean configuration flag stored in BKYSMSTR (indexed as YN[N]) |

---

*Last updated: 2026-06-11. Built from SRC analysis, schema extraction, CHM decompilation,
and DFM parsing. See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*
