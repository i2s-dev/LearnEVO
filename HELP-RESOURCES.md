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
| Analyze WO job costs vs. estimates | JC-A | [Job Costing](#job-costing-jc) |
| See materials still open in WIP | JC-P | [Job Costing](#job-costing-jc) |
| Track a serialized item | SC-A | [Serial Control](#serial-control-sc) |
| Enable serial tracking on an item | SC-B | [Serial Control](#serial-control-sc) |
| Schedule WOs across work centers | SH-A / SH-B | [Shop Scheduling](#shop-scheduling-sh) |
| Print a WO dispatch report | SH-I | [Shop Scheduling](#shop-scheduling-sh) |
| Run a Top N Customers report | SA-O | [Sales Analysis](#sales-analysis-sa) |
| Report on actual profit margin by ship date | SA-Q | [Sales Analysis](#sales-analysis-sa) |
| Analyze sales by product class/category | SA-P | [Sales Analysis](#sales-analysis-sa) |
| Enter a customer credit card on file | CC-P | [Credit Card Processing](#credit-card-processing-cc) |
| Reconcile CC charges to invoices | CC Invoice List (ccr1) | [Credit Card Processing](#credit-card-processing-cc) |
| Record inspection errors on a WO | SP/SPC main entry | [Statistical Process Control](#statistical-process-control-sp--spc) |
| View real-time defect rate dashboard | SPC Live Grid | [Statistical Process Control](#statistical-process-control-sp--spc) |
| Receive a PO via barcode scanner | HH → Receive PO | [Handheld](#handheld--shop-floor-data-collection-hh) |
| Issue materials to a WO from scanner | HH → Issue Material | [Handheld](#handheld--shop-floor-data-collection-hh) |
| Pick and ship an SO from handheld | HH → Shipping (SSOE) | [Handheld](#handheld--shop-floor-data-collection-hh) |
| Add a new company to EVO | UT → Company Add/Delete | [Utilities](#utilities-adminddata-maintenance-ut) |
| Recalculate average inventory costs | UT-K-H | [Utilities](#utilities-adminddata-maintenance-ut) |
| Set up currency exchange rates | IM module (IMC) | [Import Management / Landed Cost](#im--import-management--landed-cost) |
| Set up duty rates for imported goods | IM module (IME) | [Import Management / Landed Cost](#im--import-management--landed-cost) |
| Set up customs broker fees | IM module (IMF) | [Import Management / Landed Cost](#im--import-management--landed-cost) |
| Create/edit a user account | PS-A | [Program Security](#ps--program-security--user-access) |
| View which programs a user can access | PS-E / PSEITM | [Program Security](#ps--program-security--user-access) |
| Set up automated CRM follow-up alerts | US-G | [User Services / Triggers](#us--user-services--trigger-notifications) |
| Create an RFQ from an estimate | RF module | [RF — Request for Quote](#rf--request-for-quote-rfq-from-estimating) |
| Import BOM components from CSV | DE module | [DE — Data Entry / EDI](#de--data-entry--edi--imports) |
| Import web orders into EVO | DE-T (Web Import) | [DE — Data Entry / EDI](#de--data-entry--edi--imports) |
| Process inbound EDI 860 PO changes | DE-P-860 | [DE — Data Entry / EDI](#de--data-entry--edi--imports) |
| Create a customer RMA | RM-D | [Return Material Authorization](#rm--return-material-authorization-rma) |
| Process RMA disposition (restock/job) | RM-D-Ask | [Return Material Authorization](#rm--return-material-authorization-rma) |
| Set up product configuration options | FO module | [Features & Options](#fo--features--options) |

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
- `BKIC_PROD_CODE` — Part number (primary key, offset 0, 15 chars)
- `BKIC_PROD_DESC` — Description (offset 15, 30 chars)
- `BKIC_PROD_TYPE` — Item type code (offset 45, 1 char) — **confirmed codes (live IN-A screen + SRC files):**
  - `R` = Raw/purchased inventory — tracked, UOH maintained, posts to inventory on SO ship
  - `N` = Non-stock — not tracked, UOH always 0, no inventory decrement on ship; still posts to AR
  - `F` = Finished goods (manufactured, sellable end item)
  - `A` = Assembly (manufactured from components)
  - `M` = Manufactured / Miscellaneous
  - `K` = Kit (sell as bundle; pulls components)
  - `B` = Phantom (virtual BOM node — zero on-hand, skipped in MRP on-hand calc)
  - `L` = Labor charge (non-inventory service line)
  - `T` = Tool/fixture (tracked separately, non-inventory)
  - `O` = Outside service (sent to vendor for processing; no routings allowed)
  - Source: confirmed R and N from live IN-A screen (2026-06-17); others from BKMRF.SRC + BKROA.SRC analysis
  - Items with invalid type for routings (BKROA.SRC): B, K, R, O, M
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

**SO-G — Post Invoices (T7SAG.RWN):**
Module opens BKARINV, BKARINVL, BKICMSTR. Posts open SO invoice lines to AR.
- Checks `BKIC_PROD_TYPE` on each line item (via BKICMSTR lookup)
- Per-line release gate: `BKAR_INVL_RTS` (offset 117, 1 char) — likely "Release To Ship"; if N, SO-G skips the line
- Per-header: `BKAR_INV_RTS` (offset 621, 1 char) — same flag at header level
- "Create 0 Qty SO Lines during post" system setting: location in BKSYCFG/BKSYAR not confirmed (those tables are too small); likely in encrypted T7SAG.RWN

**Why items might not post on SO-G:**
1. `BKAR_INVL_RTS = 'N'` — line is on hold / not released to ship. Check the Release column on the SO Detail screen.
2. Line qty = 0 and system setting "Create 0 Qty SO Lines" = N
3. Already posted (BKARINV record already has POSTDATE set)
4. Item type exclusion (L=labor, B=phantom, etc.) — but R and N types DO post to AR

**SO data flow:** BKARINV (open invoice header, keyed by BKAR_INV_NUM) → BKARINVL (lines, keyed by INVNM+CNTR) → posted → BKSOX/BKSOXH (posted SO invoice extract). BKARINVI is the SO-to-invoice staging cross-reference (keyed by SONUM+INVNM).

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKARINV | Open SO invoice header — 46+ fields: invoice#, SO#, INVCD (type flag), date, customer, ship-to, terms, subtotal, tax, total, NL (# lines), RTS (release flag) |
| BKARINVL | Open SO invoice lines — 28 fields: INVNM, CNTR, ESD, PCODE (part#), PDESC, PQTY, PPRCE, PDISC, PEXT, PCOGS, ITYPE (item type), TXBLE, UBO, USTD, RTS (release flag), LOC, ABQTY |
| BKARINVI | SO→invoice staging table — SONUM+INVNM cross-ref with ITYPE, qty, price, disc, ext |
| BKSOX | Posted SO invoice extract — 25 fields (company, invoice#, date, customer, totals, SO#, terms, ship date) |
| BKSOXH | Posted SO invoice history — same 25-field structure |
| BKSONOTE | SO notes |
| BKSOPO | SO → PO cross-reference |

**Confidence: 68/100** — Table schemas from DDF; T7SAG identified as SO-G posting module with confirmed table opens; RTS flag inferred from field existence in schema; exact posting exclusion logic is in encrypted T7SAG.RWN.

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

### Job Costing (JC)

**What it does:** Reporting and analysis module that compares estimated vs. actual costs for work
orders. Reads WO labor/operation data; creates no records of its own.

**Menu codes:** JC-A through JC-S (14 report forms + shared engine)

**Key operations:**
- **JC-A — Print Job Cost Report:** Cost variance by WO. Filter by WO range, status (Firmed/Released/
  Closed/Cancelled/Indirect), item range, customer range, job range. Options: G&A Cost%,
  Summary vs. Detail, Composite (roll up sub-WOs), Include Component Descriptions, Include WO Notes.
- **JC-E — Parent/Child Cost Roll-up:** Filters by Parent Item range for multi-level WO cost
  analysis. Supports both Active and Archived WOs.
- **JC-N — Cost Calculation Options:** Chooses the cost basis — Current Month, Historical, or
  Proposed (what-if). Also controls cost breakout detail (`ISCOST.BREAKOUT`).
- **JC-P — Print Materials in WIP:** Lists all material issued to WOs that are not yet closed.
  Used to verify WIP inventory balance.

**JC Engine (T7JCENG.DFM):** All JC reports share a common engine dialog. Parameters: Report
Type, Sort/Subtotal By, Level of Detail, WO Status, WO Source (Active/Archived), Labor Type
(Regular/OT/Doubletime/Sick/Vacation/Holiday), Shift (1st/2nd/3rd), Include Run+Setup or Both,
Multiple Setup (Include Once). Ranges: WO, Work Center, Item, Tool, Employee, Machine, Labor Date,
Job, Sequence, Scrap Code, QC Code, Rework Code, Department, WO Actual Finish Date.

**Primary tables:** WORKORD, WO labor/operation tables (WOPROC, WOSCRAP, WOREMATR),
ISCALC.* (cost calculation config), ISCOST.* (cost breakout config)

**Confidence: 68/100** — All 14 DFM files read; form purposes confirmed; cost formula logic inaccessible (in RWN).

---

### Serial Control (SC)

**What it does:** Manages serial number assignment, tracking, and lifecycle for serialized inventory
items. Distinct from Lot Control (LC) — serial tracking is one-unit-per-serial.

**Menu codes:** SC-A through SC-H (9 forms)

**Key operations:**
- **SC-A — Edit Serial Numbers:** View/edit individual serial records. Fields: Serial Number,
  On-Hand, Date Received, WO#, Exp Date, Location, Cost, SO#, Bin, Invoice#, Customer, Ship Date.
  Primary table: MTSER.
- **SC-B — Assign Serial Control:** Configure which inventory items are serial-tracked by setting
  the MTIC.PROD.SER flag. Shows item type, description, and note.
- **SC-C / SC-C2 — Serial Browse / Print Availability:** Browse/report serial inventory; SC-C2 has
  option to include zero-on-hand serials (ISPRT.ZEROS).
- **SC-E — Archive/Unarchive:** Archive or restore serial records by item and serial number range.
- **SC-F — Serial Control Exceptions:** Shows serials with anomalous state.
- **SC-G — Serial Format Setup:** Defines the serial numbering scheme per item or item class:
  Total Length, Starting Position of Numeric portion, Last Number Used. Tables: IS.SERC.*.
- **T7SCOMP — Compound Serials:** Manages compound/composite serial structures where one finished
  serial is composed of multiple component serials. Tables: IS.SCOMP.DETAIL, IS.SCOMP.COMPND.

**Primary tables:** MTSER (serial master — one record per serial unit), MTIC.PROD.SER (item-level
serial flag), IS.SERC.* (serial format configuration), IS.SCOMP.* (compound serial definitions)

**Confidence: 72/100** — All 9 DFM files read from network share; all form purposes confirmed from captions and field names.

---

### Shop Scheduling (SH)

**What it does:** Finite-capacity scheduling of work orders across work centers on the shop floor.
This module is the dispatch and scheduling layer on top of WO — it does NOT create work orders,
it schedules and monitors their execution.

**Menu codes:** SH-A through SH-P (15 forms)

**Key operations:**
- **SH-A — WO Scheduling Grid:** Main WIP work order browse. Shows WO#, Item, Description,
  Customer, Scheduled Start, Scheduled Finish, Due Date, Priority, Class, Lead Time. Filter by
  Status (Scheduled/Firmed/Released), Priority (1/2/3), Item Class/Category range. Table: MTWO.WIP.*
- **SH-B — WO Operation Scheduling:** Drill-down to individual routing operations. Fields:
  Operation, Work Center, Assigned WC (may differ from standard WC), Start/Finish dates, Status,
  Qty Started, Qty Complete, Contention, Overlap Hours, Negative Overlap, Queue, Labor Type
  (Regular/Outside Process), Vendor (for outside ops), Lead Time. Table: MTWORO.*
- **SH-C — Work Center Browser:** View work centers with Dept, Dept Description, Outside Process
  flag, and Hours/Week capacity. Table: MTWC.*
- **SH-E — Change Due Date:** Quick edit of WO due date and priority from the scheduling view.
- **SH-I — Dispatch Report:** Comprehensive scheduling report with color coding. Options: WO
  status/class/priority filters, work center range, start/finish date range, customer range,
  planner code range, starting weekly date, Recalculate Time Remaining, Limit to WOs with All
  Available Components, Print BOM Components (type FRAM), Print Purchase Orders (SPAN/ASIS).
  Color-codes elapsed start dates and priority changes.
- **SH-P — Report Color Setup:** Configures colors for the SH-I dispatch report.

**Key concepts:**
- WO statuses in SH: Scheduled, Firmed, Released (same as WO module statuses)
- Contention field (MTWORO.CONTNTN): flags operations where work center is over-capacity
- Overlap / Negative Overlap: SH supports operation overlapping (starting an op before the prior
  finishes) and negative overlap (gap between ops). These are scheduling efficiency parameters.
- Planner Code: allows routing WOs to different schedulers/planners by range

**Primary tables:** MTWO.WIP.* (WIP work order header data), MTWORO.* (WO routing operations),
MTWC.* (work center master: capacity, department, outside-process flag)

**Note:** Physical carrier shipping (carrier selection, BOL, tracking) is part of the SO module
(T7SOC hub form), not SH. SH = Shop floor scheduling only.

**Confidence: 72/100** — All 15 DFM files read; MTWO/MTWORO/MTWC table access confirmed; scheduling algorithm inaccessible (in RWN).

---

### IM — Import Management / Landed Cost

**What it does:** Manages foreign currency setup and landed cost configuration. Used by companies that import goods and need to calculate the true delivered cost including import duties, freight, and customs broker fees.

**Key operations:**
- **Currency Factor Setup (IM-B):** Define currencies — code, description, base currency flag, and symbol. ISIS.MCF.* is the master list of all currencies EvoERP knows about.
- **Exchange Rate Entry (IM-C):** Enter dated exchange rates. ISIS.MCR.SOURCE[1..n] allows multiple rate sources per date (bank rate, spot rate, etc.). Rates are date-keyed for historical accuracy.
- **Landed Cost GL Accounts (IM-D):** Configure which GL accounts receive duty charges (ISIS.LND.GLADT), deferred duty (ISIS.LND.GLDDT), freight (ISIS.LND.GLAFR), and deferred freight (ISIS.LND.GLDFR).
- **Duty Rate Codes (IM-E):** Assign duty percentages by vendor-keyed code. The first 3 characters of the duty code = the vendor code, enabling per-vendor duty rate assignments.
- **Customs Broker Setup (IM-F):** Define customs brokers — code, flat fee, percentage rate, and type. Multiple brokers supported.

**Primary tables:** ISIS.MCF.* (currency factors), ISIS.MCR.* (exchange rates), ISIS.LND.* (landed cost GL), ISIS.DUTY.* (duty codes), ISIS.BRK.* (broker fees)

**Note:** The ISIS prefix is shared with SM module (ISIS.TXF/TXG = tax codes). "ISIS" = IS International System — the EvoERP namespace for all international compliance and currency tables.

**Confidence: 70/100** — All 5 DFMs read; full landed cost schema confirmed; PO/receiving integration for applying landed cost to receipts not decoded.

---

### PS — Program Security / User Access

**What it does:** Manages user accounts and program-level access control. Separate from the AHSYLOG system login table — PS provides granular, per-program permission assignments with named security codes.

**Key operations:**
- **PS-A — User Setup:** Create or edit a user account. Fields: User Name (BKPS.USER.CODE), Security Level, Security Code [A/P/1/2/C/V/U/E] (8 named access tiers), Default Start Company, Employee/Rep linkage. The seccode controls what parts of EVO the user can access.
- **PS-E — User Security Report:** Print the security assignments for a user name range. Used for security audits.
- **Program Access List (PSEITM):** The list of programs (menu operations) a specific user is allowed to run. PROGRAM_NUM, PROGRAM_NME = each EVO menu operation identified by number and name.
- **PS-F — Access-to-Program Report:** Print all users who have access to a specific program name. Inverse of PS-E.
- **PS-K — Approve Vendor:** Authorize an AP vendor — ap.vend, bkap.vendname. Access to vendor approval may require PS security level.

**Dual user system:** EvoERP has two user tables:
1. **AHSYLOG** — system-level: login, 20 module-access flags (AHSY_USER_ACCES_1..20), starting menu
2. **BKPS.USER.*** — program-level: per-operation whitelist controlled by PS module

**Primary tables:** BKPS.USER.* (user accounts), program access list (BKPS.PROG.* or similar)

**Confidence: 60/100** — All 6 DFMs read; dual user system confirmed; security code [A/P/1/2/C/V/U/E] exact values not decoded; program number mapping not decoded (in RWN).

---

### US — User Services / Trigger Notifications

**What it does:** Manages automated follow-up triggers — alerts that fire a notification to a user or contact N days before a key date. Used for CRM follow-ups, service renewal alerts, and scheduled reminders.

**Key operations:**
- **US-G — Trigger Setup:** Define a trigger — Trigger Code, User to Trigger (internal user), Last Date/Time fired (audit trail), Days Pre (how many days before the reference date to fire). Notification target: IS.TRIG.CONTACT (contact name), IS.TRIG.EMAIL (email), IS.TRIG.EFLAG (whether to send email vs. in-app alert).

**Integration:** IS.TRIG.CONTACT and EMAIL suggest triggers are linked to CRM contacts (BKCM.ACCN.*) or SR service records. "Days Pre" + CRM key dates (BKCM.ACTD.*) = automated follow-up scheduling (e.g., "alert sales rep 14 days before contract expiry").

**Primary tables:** IS.TRIG.* (trigger records — code/contact/email/days/last-fired)

**Confidence: 45/100** — 1 DFM read; trigger mechanism confirmed; full integration points and trigger type taxonomy not decoded.

---

### DE — Data Entry / EDI / Imports

**What it does:** The EvoERP integration gateway — handles all data imports, EDI transactions, and data exports. Covers BOM component import, Physical Inventory tag import, WO material import, web order import, vendor POA (855) acknowledgments, customer EDI-860 PO changes, and web item catalog export. Also contains two dangerous admin utilities.

**Key workflows:**

- **BOM Component Import:** DE-M imports BOM components from CSV. DE-ER validates the import and reports errors. Filter: import to Estimating or Production BOM; allow 0 qty components.
- **Physical Inventory Tag Import (DE-HD):** Import PI count tags from a CSV. Skip or replace existing tag numbers. Field position mapping (FIELD.NUMBER[1..n]) configures which CSV column maps to which PI field (tag#, location, item#, qty).
- **WO Material Import (DE-J-H):** Import WO component/material lines. Fields: WO prefix/suffix (WO#), product code, description.
- **Web Order Import (DE-T):** Import customer orders from a web source. `import.to.edi` flag routes to EDI module first or direct to open SO. Bank/payment data included in header.
- **Vendor POA Import (DE-V):** Import EDI 855 Purchase Order Acknowledgments from vendors. SKIP flags allow partial imports (skip by PO#, product, qty).
- **EDI-860 PO Changes (DE-P-860):** Process inbound customer EDI 860 (Purchase Order Change) transactions. References RELEASE_NUM for blanket PO releases.
- **Customer Release Import (DE-P-B/E/H):** Import customer blanket PO releases. Filter by customer, SO#, invoice#, release number.
- **Web Item Catalog Export (DE-U):** Export item catalog via FTP (ftp.FileName). Filter by item range.
- **Global Field Replace (DE-K) ⚠️:** Find-and-replace a specific field value across any EVO data file. Irreversible — no undo.
- **Selective File Erase (DE-L) ⚠️:** Erase Inventory, BOM, Customer, and/or Routing files in bulk. Irreversible.
- **Defect Code Setup (DE-FECT):** Maintain the IS.DEF.CODE/DESC master list used by QC and SPC modules.

**Primary tables:** IS.DEF.* (defect codes), WOMAT.* (WO materials), BKAR.INV.*/BKAR.INVL.* (invoice import target)

**Confidence: 68/100** — All 20 DFMs read; EDI flows and import targets confirmed; web order bank integration and exact DE-P sub-form scope not fully decoded.

---

### RM — Return Material Authorization (RMA)

**What it does:** Manages customer returns — creating RMA numbers against original invoices, recording warranty status and reason, and routing returned items to restocking, credit, or WO rework.

**Key operations:**
- **RM-D — RMA Entry:** Create an RMA against an original invoice (Original Inv Num) and SO. Record the returned item, reason for return, and warranty status. Warranty codes: N=Not covered, L=Limited, P=Parts only, B=Both parts & labor.
- **RM-D-Ask — Disposition:** Specify where returned items go — to a bin Location, or passed to a WO Job for rework (Pass RMA# to: D=Description, J=Job, N=None). Enter a Restock Charge if applicable.
- **RMA Status (T7RMAWHY):** View RMA number, line#, status (is.rma.status), and original SO/invoice line reference.
- **RMA Reason Codes (RM-E):** Maintain IS.RMA.CODE/DESC — the master list of return reason codes.
- **RMA Report (RM-G):** Customer/item range report of open or historical RMAs.

**Primary tables:** IS.RMA.* (RMA records — status/warranty/code), BKAR.INV.*/BKAR.INVL.* (original invoice), IS.RMA.CODE/DESC (reason codes)

**Confidence: 68/100** — All 5 DFMs read; RMA lifecycle traced; IS.RMA.* table confirmed; full field schema and exact warranty code values inferred from pattern.

---

### FO — Features & Options

**What it does:** Product configurator extension to the BOM module. Lets manufactured products have selectable features and options. Each option sets a Y/N flag (BKBM.PROD.OPYN[1..N]) on the BOM item. When a customer orders a configurable product, option selections drive which BOM components are included.

**Key operations:**
- **FO-C — Option Configuration:** Configure the option flags for a product. PAR.DESC = parent/assembly, COMP.DESC = the option component. BKBM.PROD.OPYN[5] = option flag index 5 (at least 5 options supported per product).
- **FO-D — Range Operation:** Item/category/class range filter — likely a bulk assignment or report operation.
- **FO-E — Item Select:** Filter features/options by item number range.

**Primary tables:** BKBM.* (BOM — PROD.OPYN flags), BKICMSTR (item master)

**Confidence: 50/100** — 3 DFMs read; option flag mechanism confirmed; SO→option trigger and exact OPYN slot count not decoded (in RWN).

---

### Handheld / Shop-Floor Data Collection (HH)

**What it does:** Provides a scanner-optimized interface for shop-floor terminals and handheld barcode devices. Supports PO receiving, WO material issue and completion, SO picking and shipping, inventory bin transfers, DC labor scanning, and physical inventory counts — all via barcode scan entry.

**DFM count:** 44 forms

**Key workflows:**

- **PO Receiving** — Scan item barcodes to receive against a PO. Assign received qty to bin location (HHPOCBIN), lot (HHPOCLot), or serial (HHPOCSER). Vendor/item alerts popup if configured. RCVD_QTY auto-increments with each scan.
- **Issue Materials to WO** (t7hhwog) — Scan components to issue against a WO. Option to print component labels at issue time (RTM_NAME, prt.per.comp, Label.qty). Lot (HHWOLOT) and serial (hhwoser) sub-forms handle tracked items.
- **Finish Production** (t7hhwop) — Report WO completion. Prompts for issue date, filters by WO status (FRXI = Released/Completed/In-Process/On-Hold), confirms final quantity.
- **Scrap Reporting** (HHWOSCRAP) — Record WO scrap quantities from scanner; prints scrap labels immediately.
- **SO Picking/Shipping** (T7HHSSOE) — Scan items into boxes (curr.boxnum tracks current carton). 5-step verification chain: SSOE → ssoeLabels → ssoeLverify → SSOEVerify → SSOESVerify before release. Bin/Lot/Serial variants handle tracked SO lines.
- **Bin Transfer** (t7hhinlj) — Move inventory from one bin (from.loc) to another (to.loc). Lot and serial variants update MTLOT/MTSER records in parallel.
- **Physical Count** (T7HHPIC / t7hhpictags) — Enter PI tag counts from handheld. Same tag structure as desktop PI-C: CountDate, qtr, year, location. Tag detail captures countqty + lotno + serialno.
- **DC Labor Scan** (T7HHDCA) — Clock in/out at a work center operation: scan WO# (scan.wo), employee ID (scan.emp), and operation code (OPER).

**Large Screen Lookups mode** — Every major HH form has a `large.lookups` flag that switches to a larger-font, touch-friendly layout for kiosk screens.

**Item type filter codes** (HH-N picking): RFAMNLBTKO = Raw, Finished, Assembly, Manufactured, Non-stock, Labor, Bought, Tool, Kit, Other.

**Credit hold enforcement** — HH-N SO picking filter includes `incl.crhold` flag, so the handheld can refuse to show SOs for customers on credit hold.

**Primary tables:** BKAR.INV.* (SO), BKWOMSTR/BKWODTL (WO), BKRECV/BKRECVLN (PO receiving), MTLOT.* (lots), MTSER.* (serials), ISBN.MSTR (bins), BKPH.* (PI count tags)

**Confidence: 68/100** — 20 of 44 DFMs read; all functional areas identified; offline sync mechanism and exact WO join keys not decoded.

---

### Utilities — Admin/Data Maintenance (UT)

**What it does:** Administrative toolkit for EvoERP system maintenance. Covers adding/removing companies, bulk data clear/reset (for initial setup), fiscal year configuration, unused-record cleanup, and inventory cost recalculation. **Most operations are permanent and irreversible.**

**Menu codes:** UT (20 operations in menu)

**Key operations:**
- **Company Add/Delete (t7uti):** Add a new company to EvoERP's multi-company setup. Specify company_code, company_name, path. copy.file initializes by copying an existing company's file structure. The cdelete flag removes a company entirely.
- **Data Clear/Reset (UT-K-A):** Selective module-by-module data wipe. Flags: CLR.COA (chart of accounts), CLR.CUST (customers), CLR.VEND (vendors), CLR.INVN (inventory). Option: delete ALL data ("D") or transactions only ("C"). Caption explicitly warns this clears "General Ledger (and BKSYMSTR)". Used for: new company setup from a template, end-of-demo cleanup.
- **Fiscal Year Setup (UT-K-D):** Configure fiscal year start dates for up to 5 periods: fycur (current), fy1yp (last year), fy2yp, fy3yp, fy4yp. Must be correct before any period-end GL close.
- **Location Cleanup (UT-K-E):** Deletes all warehouse bin/location codes not currently tagged as active. Reassigns orphaned inventory records to a new master location code (new.code). Caption: "not reversable... may take a long time." Run after a bin master reorganization.
- **Item Utilities F & G (UT-K-F, UT-K-G):** Two item-range rebuild passes filtered by item number and class. Likely rebuild on-hand quantities or cost layers (exact operation not confirmed from form alone).
- **Average Cost Recalculate (UT-K-H):** Recalculates Average Cost in inventory records. Filtered by inventory type flags (inc.type[1-4] = by item type) and item/class range. Run after physical inventory adjustments or initial data load when cost layers are out of sync.
- **File Layout Report (UT-H):** Prints the data file structure (field names, types, sizes) for a range of EVO data files (from.file to thru.file). Useful for data export/mapping work.

**Primary tables:** BKSYMSTR (company/global settings), BKYSMSTR (YN flags), BKARCUST/BKAPVEND/BKICMSTR (cleared by UTKA), BKIC.LOCM/ISBN.MSTR (location cleanup), BKICOST (cost layers)

**Confidence: 60/100** — All 8 DFMs read; destructive operations documented; UT-K-F/G exact purpose not confirmed; full 20-operation menu scope not decoded.

---

### Sales Analysis (SA)

**What it does:** Produces sales performance reports and margin analysis across customers, items, salespersons, product classes, and currencies. Uses a dedicated BKSA.* aggregation table (separate from live AR invoice data).

**Menu codes:** SA (13 operations in menu)

**Key operations:**
- **SA-A — Currency Analysis:** Filter and analyze sales by currency pair. Fields: from_cur, thru_cur, inc.change (include currency exchange difference). Used for multi-currency revenue reporting.
- **SA-M / SA-N — Salesperson Reports:** Analyze sales by salesperson/rep. Reads BKSA.NAME, BKSA.TITLE, BASE — pre-summarized salesperson performance data.
- **SA-O — Top N Sales Report:** Ranks customers by sales volume. Filter by customer range and date range. Classic "top 10 customers" report.
- **SA-P — Class/Category Analysis:** Analyze sales by item product class (from.class/thru.class) and category (from.cat). Useful for product line performance analysis.
- **SA-Q — Actual Margin Report:** Profit/loss analysis by ship date range (from.shipdt/thru.shipdt) and actual WO finish date (thru.afin). The WO actual-finish integration means margin is tied to completed job costs, not just invoiced amounts.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKSA.* | Sales analysis aggregation — pre-summarized performance data with NAME, TITLE, BASE fields |
| BKARINV | AR Invoice header — source data for SA calculations |
| BKARCUST | Customer master — customer name/class lookup |

**Important distinction:** SA uses a dedicated BKSA.* table, not just a live query on BKARINV. This means SA data must be refreshed/rebuilt from AR history — there is likely a "build SA data" operation that populates BKSA from invoice history before reports are run.

**Confidence: 55/100** — All 6 DFMs read; BKSA.* table confirmed; SA-O "Top N" and SA-Q "Actual Margin" verified by caption; aggregation/rebuild trigger unknown; BKSA field schema not decoded.

---

### Credit Card Processing (CC)

**What it does:** Stores customer credit card information (masked), records CC charges against invoices and purchase orders, imports CC transaction files from CSV, and produces CC invoice reconciliation reports.

**Menu codes:** CC (6 operations confirmed from DFM count)

**Key operations:**
- **CC-P — Credit Card Entry:** Enter or view a customer's credit card. Stores masked card number (IS.CC.MASKED), cardholder name (IS.CC.CARDNAME), expiry date (IS.CC.EXP in MMYY format), billing ZIP (IS.CC.ZIP), and charge amount. Displays "* Expired *" flag for expired cards.
- **CC-PO — CC Charges on POs:** Link credit card payments to purchase orders (ccnum, ccamount, CCYY, CCMM). Vendors can be paid by credit card through the PO workflow.
- **CC Invoice List (ccr1) — Reconciliation Report:** List all credit card invoices by date range and payment terms range. Used for statement reconciliation.
- **CC Import (CC-DE) — CSV Import:** Import CC transactions from a CSV file (bank statement download). Fields: file.name, COMMA.FIXED.STR (fixed vs. comma-delimited flag), FIELD.NUMBER2[1-2] (field position mapping).
- **CC Item/WO Range Filters:** CC charges can be analyzed by item number range or Work Order/location, enabling cost allocation to specific jobs.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| IS.CC.* | Credit card records — masked card #, cardholder name, expiry, billing ZIP |

**Security note:** IS.CC.MASKED stores only the masked (tokenized) card number, not the raw PAN. Compliance-aware storage.

**Confidence: 65/100** — All 6 DFMs read; CC data model confirmed; masked storage architecture confirmed; IS.CC field count and AR/PO integration join keys not decoded.

---

### Statistical Process Control (SP / SPC)

**What it does:** Records quality inspection errors during manufacturing (by inspector, WO, item, drawing), provides a real-time error dashboard, and produces defect-rate reports including PPM (Parts Per Million) analysis.

**Menu codes:** SP (6 forms confirmed from DFM count)

**Key operations:**
- **SPC Main Entry (T7SPC) — Scan/Inspection Record:** Inspector enters defects found during WO inspection. Fields: Inspector #, Employee (SCAN.EMP), Work Order (SCAN.WO), Work Order Item, Work Order Qty, Customer, Drawing number, error type (IS.SERR.ERROR), and process (IS.SERR.PROCESS). The SORTKEY field suggests inspection records are sequenced.
- **SPC Live Grid — Real-Time Error Dashboard:** Caption='Top Real Time Errors'. Grid columns: ATYPE (error type), ADETAIL (error detail), ACODE (error code), ACOUNT (count). Live view of current defect rates across active WOs.
- **SPC Live Report — Auto-Refresh Report:** Filter by error type, detail, and date range. "Refresh Every" field = configurable auto-refresh interval (seconds). Designed for shop-floor monitor display.
- **SPC Report (SPCREP/SPCREP2) — WO Inspection Report:** Filter by WO range, parent part range, employee range, and date range. Standard after-the-fact quality analysis.
- **SPC PPM Report (SPCREPPPM) — Parts Per Million Defect Rate:** WO/part/date range with "Sides From/Thru" range. PPM = (defects / opportunities) × 1,000,000. The "Sides" field is specific to PCB/electronics manufacturing (front side, back side of a circuit board).

**Primary tables:**

| Table | Purpose |
|-------|---------|
| IS.SERR.* | Scan/inspection error records — error type, process, WO, employee, qty |

**Industry context:** The "Sides" field in the PPM report (PCB front/back) strongly indicates i2 Systems is an electronics/PCB manufacturer. SPC PPM measurement by board side is standard in electronics contract manufacturing.

**Confidence: 60/100** — All 6 DFMs read; IS.SERR.* table confirmed; real-time dashboard and PPM report verified by caption; IS.SERR field schema and process taxonomy not decoded; menu code placement not confirmed.

---

### CRM / Contact Manager (CM)

**What it does:** Manages customer and prospect contacts, accounts, territories, and marketing activities. Bridges AR (customers) and a dedicated CRM account database. Up to 9 email addresses per contact, account classes, territories, SIC/lead-source codes.

**Menu codes:** CM (6 forms confirmed)

**Key operations:**
- **CM-A — CRM Account Master (T7CMA):** Create/edit CRM accounts. Fields: account name, address, territory (BKCMTERR), SIC code, lead source, account class, key contacts with EMAIL[1..9].
- **CRM-AR Bridge:** CRM accounts link to AR customers via BKCMACCN. Same account can exist in both systems; changes sync through T7CMCVTN/T7CMCVTF conversion forms.
- **Contact merge (T7CMBB):** Merge duplicate CRM contact records.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKCMACCN | CRM Account — company name, address, key fields |
| BKCMACCC | CRM Account Class — A/B/C/custom classification |
| BKCMACCT | CRM Account Type |
| BKCMLEAD | CRM Lead Source codes |
| BKCMTERR | CRM Territory codes |

**Confidence: 65/100** — T7CMA + 4 sub-forms read; CRM-AR bridge confirmed; 9-email field, territory, and SIC confirmed; full BKCM* table family (46 tables) not exhaustively cataloged.

---

### Commission / Salesperson Management (CS)

**What it does:** Tracks salesperson setup (rates, commission method, GL accounts), commission due and paid per invoice, transfers, and commission reports.

**Menu codes:** CS (12 forms confirmed)

**Key operations:**
- **CS-A — Salesperson Master:** Fields: BKPR.SLS.RATE (commission %), BKPR.SLS.HOW (calculation method), BKPR.SLS.WHEN (when earned: invoice/payment), BKPR.SLS.CLASS, BKPR.SLS.GL (GL account), BKPR.SLS.AGENT (linked AP vendor for outside reps).
- **CS-B — Commission Record:** Tracks BKPR.COMM.QUOTA, BKPR.COMM.COGS (cost of goods), commission due, and commission paid[1-7] (7 payment buckets).
- **CS-D — Transfer Commissions:** Moves earned commissions between periods. Fields: BKPR.COMM.SLSP, BKPR.COMM.CCODE, BKPR.COMM.INVNM, BKPR.COMM.INVDT.
- **CS-E/F — Reports:** Detail and summary commission reports by period.
- **Outside agents** are linked to AP vendors (BKPR.SLS.AGENT → BKAPVEND) for check payment.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKPRSALE | Salesperson/commission master |
| BKPRAGNT | Outside agent (AP vendor link) |

**Confidence: 70/100** — All 12 DFMs read; commission calculation method, outside agent link, and 7-payment-bucket structure confirmed; commission calculation formula details in encrypted RWN.

---

### Lot Control (LC)

**What it does:** Assigns lot numbers to items, tracks lot usage through SO/WO/PO, and provides lot-level traceability. Parallel to SC (Serial Control) for lot-tracked items.

**Menu codes:** LC (7 forms found)

**Key operations:**
- **LC-A — Lot Master (T7LCA):** View and edit MTLOT lot records.
- **LC-B — Assign Lot Control:** Sets MTIC.PROD.LOT flag on item master — marks item as lot-tracked.
- **LC-G — Archive:** Archive expired lots by expiry date range.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| MTLOT | Lot master — lot numbers, item, qty, dates |
| MTIC.PROD.LOT | Flag in item master enabling lot tracking |

**Confidence: 72/100** — All 6 found DFMs read; LC-A/B/G workflow confirmed; lot lifecycle (receive→track→ship→close) not fully traced.

---

### Quality Control (QC)

**What it does:** Records incoming inspection results (pass/fail/scrap) on PO receipts and WO outputs. Tracks QC/scrap codes per vendor range.

**Menu codes:** QC (18 files in RWN analysis)

**Key operations:**
- **QC-A — Main Entry:** QC code + scrap code dual-classification; vendor range filter for incoming inspection.
- **QC-B/C/D — Reports:** Parent item roll-up reports across QC/scrap records.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKQCMSTR | QC master records |
| BKQCTRAN | QC transaction log |

**Confidence: 52/100** — 4 DFM files read; QC/scrap dual-code and vendor-range confirmed; QC-B/C/D form logic not deeply decoded.

---

### Warehouse Control (WC)

**What it does:** Manages bin/shelf locations, bulk bin assignment, and browsing items by physical bin. Note: WC = Warehouse Control, NOT Work Centers.

**Menu codes:** WC (8 forms read)

**Key operations:**
- **WC-A — Bin Master (CRUD):** Create/edit bin records in ISBN.MSTR (bin master table).
- **WC-C — Serials by Bin:** View serial numbers currently in a specific bin (MTSER table).
- **WC-D — Bulk Bin Assignment:** Mass-assign items to bins (Skip/Replace mode for existing).
- **WC-H — Location Browser:** Browse all bin assignments.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| ISBN.MSTR | Bin master — bin code, description, location |
| BKIC.LOCM | Item-to-bin assignment |
| MTSER | Serial numbers by bin (also used by SC module) |

**Confidence: 72/100** — All 8 DFMs read; bin CRUD, serial-by-bin, bulk assign confirmed; multi-bin/zone hierarchy not traced.

---

### Accounting Maintenance (AM)

**What it does:** GL period control, account history, account entry, department copy/delete, and financial statement format management. Note: AM = Accounting Maintenance, NOT Asset Management.

**Menu codes:** AM (15 files in RWN analysis)

**Key operations:**
- **GL Period Control:** Open/close accounting periods; sets the fiscal year calendar.
- **Account History View/Edit:** Browse GL account balance history across periods.
- **Department Copy/Delete:** Mass-copy or delete department-level GL configurations.
- **Financial Statement Format:** Defines how accounts group into income statement / balance sheet formats.

**Primary tables:** BKGLCOA (GL Chart of Accounts), ISGLDATE (GL date per company/module), ISGLCOA (GL COA extension — multi-year history and budget).

**Confidence: 75/100** — 5 forms read; period control, account history, dept copy/delete confirmed; financial statement format structure details in encrypted RWN.

---

### Fixed Assets (FA)

**What it does:** Tracks fixed assets (equipment, property) with depreciation schedules and GL posting.

**Menu codes:** FA (3 forms confirmed)

**Key operations:**
- **FA-A — Asset Master (T7FAA):** IS.FXA.* fields: asset cost, residual value, useful life, depreciation method (SL/DB/etc.), GL accounts (asset account, accumulated depreciation, depreciation expense).
- **FA-B — Post Depreciation (T7FAB):** IS.FXT.* fields: posts calculated depreciation with a "Ready-to-Post" approval flag before GL entry.
- **FA-E — Export (T7FAE):** Exports asset register.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| IS.FXA.* | Fixed asset master — cost, method, life, GL accounts |
| IS.FXT.* | Depreciation transactions — period amounts, posting status |

**Confidence: 75/100** — All 3 DFMs read; cost/residual/life/method/GL fields confirmed; depreciation calculation formula (SL vs. declining-balance) details in RWN.

---

### Activity Control / NCR (AC)

**What it does:** Non-Conformance Report (NCR) tracking — records manufacturing defects, assigns disposition codes (rework/scrap/use-as-is), and tracks corrective actions linked to work orders.

**Menu codes:** AC (4 RWN modules confirmed)

**Key operations:**
- **T7ACRDTYPE — Disposition Codes:** AC.RD.TYPE (type code), AC.RD.REASON (reason text), AC.RD.DISPO (disposition: rework/scrap/use-as-is), EXTRA1/EXTRA2 (user-defined fields).
- **T7ACTION — Action Items:** IS.ACTION.TYPE/DESC/MISC — action item tracking for corrective actions.
- **T7ACDET — NCR Detail Records:** AC.DET.ID, AC.DET.LINE, AC.DET.PART — detail lines per NCR.
- **T7ACDATE — WO Date Hierarchy:** WODATE.START/FINISH/QTY, PARPRE/PARSUF/TOPPRE/TOPSUF (parent/top WO hierarchy prefixes/suffixes), DELPRE (cascade delete prefix). Links NCRs to specific WO operations.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| WODATE | WO operation dates — start/finish/qty per operation |
| ISACTION | Action items — type, description, misc |
| ACRDTYPE | Disposition code master — type/reason/dispo codes |
| ACDETAIL | NCR detail lines |

**Confidence: 60/100** — 3 DFMs + 4 RWN modules decoded; WO hierarchy (parent/top prefix) and disposition codes confirmed; NCR full lifecycle not traced.

---

### System Maintenance (SM)

**What it does:** The largest maintenance module (34 operations). Configures system-wide settings: user preferences, tax rates, ship-via methods, payment terms, job numbers, company setup, CRM masters, and SMT/PCB machine configuration.

**Menu codes:** SM (34 ops — 3rd largest module)

**Key operations:**
- **SM-K — User Preferences:** Writes to EvoSettings.INI and ISNUMBER (number format preference).
- **SM-E/F — Tax Setup:** ISIS.TXF (tax rates) + ISIS.TXG (tax groups).
- **SM-O — Ship Via:** ISSHPVIA with carrier tracking URL field.
- **SM-D — Payment Terms:** IS.TERMS (standard payment terms like Net30, 2/10Net30).
- **SM-PF — Job Number:** ISJOB (next job cost number counter).
- **SM-PH — Cycle Codes:** IS.CYCLE (production cycle codes).
- **SM sub-modules:**
  - T7SMI* (CRM masters): BKCMLEAD, BKCMTERR, BKCMACFC, BKCMACCC, BKCMDTCD
  - T7SMP* (catalog/UDF/job): ISCATMST, ISUDMSTR, ISJOB
  - T7SMTEND/T7SMTSET (SMT/PCB integration): ISSMTCFG, MACHINE, ISSERIAL, WOBOM — configures surface mount technology placement machines

**Primary tables:** BKSYMSTR, BKYSMSTR, ISSHPVIA, ISIS.TXF/TXG, IS.TERMS, ISJOB, IS.CYCLE, ISSMTCFG, MACHINE

**Confidence: 80/100** — 23+ forms + full T7SM* sub-module family decoded; SMT/PCB integration confirmed; BKSYMSTR/BKYSMSTR not exhaustively decoded.

---

### Service / Repair (SR)

**What it does:** Manages service and repair jobs — equipment master, service quotes, work order linkage, and AR invoicing for service work.

**Menu codes:** SR (13 files in RWN analysis)

**Key operations:**
- **SR-K — Equipment Master:** ISSR.MMS.* fields: make, model, serial number, IN/OUT dates, motor data, linked WO#.
- **SR-I — AR Invoice Browse:** Browse AR invoices linked to service records.
- **SR-E — Invoice Address Edit:** BKAR.INV.* fields — billing address adjustments for service jobs.
- **Service quotes:** QT module (T7QTINFO: ISSR.INFO.DATE[1..5] milestone dates) links to SR.

**Primary tables:**

| Table | Purpose |
|-------|---------|
| ISSR.MMS.* | Service equipment master — make/model/serial/dates/WO link |
| IS.SERR.* | SPC/inspection error records (shared with SP module) |

**Confidence: 58/100** — 7 DFM files read; equipment master, AR invoice link, and service quote date milestones confirmed; main SR-A form not found on share.

---

### Multi-Yield Work Orders (MU)

**What it does:** Records multiple output part numbers from a single work order (co-products and by-products). 150 procs — significant manufacturing-cost module.

**Key operation:** T7MULTIYIELD opens WORKORD + WOROUT + WOBOM + WORECV + INVTXN + ISBINLOC + BKARINVL. One WO produces multiple different finished items; each is received as a separate WORECV/INVTXN entry.

**Primary tables:** WORKORD, WOROUT, WOBOM, WORECV, INVTXN, ISBINLOC, MTICMSTR, BKARINVL

**Confidence: 45/100** — DB fingerprint confirmed; full multi-yield entry form details in encrypted RWN.

---

### Field Service (FS)

**What it does:** Optional Field Service add-on module — tracks service classes, field service information records, and assigns employees to service classes.

**Key tables:** ISFSCLAS (class master), ISFSINFO (FS info records), ISPRINFO (PR employee profile data), BKPRSALE (salesperson/employee)

**Confidence: 45/100** — DB fingerprint confirmed; no DFM forms found for this module; no CHM entries = possibly not licensed in this installation.

---

### Global Finance / AR Charges (GF)

**What it does:** Applies extra charges to AR invoices beyond standard line items (e.g., freight charges, service fees, surcharges). Includes customer-item pricing matrix entry and invoice charge viewer.

**Key tables:** ISARCHG (IS AR extra charges), BKICPMAT (IC pricing matrix), BKARCUST, BKARINV, BKARINVL

**Confidence: 45/100** — DB fingerprint confirmed; no DFM forms found; charge structure details in encrypted RWN.

---

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

### BS — Business Score / Customer Scoring

Tracks customer profitability and scoring metrics. Primary table: **ISBSF** (business score fields). Accessed via T7BSA/T7BSB/T7BSC/T7BSD modules (4 program files = 4 menu code variants). Scores are likely computed from AR transaction history and stored for reporting.

**Use case:** Identify highest-value or most-at-risk customers based on revenue, payment history, or custom scoring criteria.

**Confidence: 42/100** — Module identified by DB fingerprint; table confirmed; scoring algorithm and UI fields not decoded.

---

### AD — Advanced DC / Advanced Data Collection

Extended Data Collection module (builds on DC shop-floor labor entry). Primary tables: **BKSYUSER** (system user extensions), **ISTRIGRS** (trigger actions for automated events). Uses T7ADA/T7ADB/T7ADC modules (3 files). Likely adds automated triggers, badge-reader integration, or advanced scheduling to standard DC labor posting.

**Use case:** Set up automated triggers for labor posting, barcode/badge-reader data entry rules, or shift-based collection rules.

**Confidence: 48/100** — Module identified by DB fingerprint; tables confirmed; trigger logic and UI not decoded.

---

### IT — Item Serial Number Configuration

Extended serial number configuration module. Primary table: **ISSERCNT** (serial counter tracking). Works with existing SERIAL and ISSERIAL tables. T7ITA module (1 file found in rwn_symbols.json). Likely provides serialization rules (auto-generate serial numbers, prefix/suffix, sequence ranges) per item.

**Use case:** Configure auto-serial numbering for manufactured items or purchased serialized goods.

**Confidence: 40/100** — Module identified by DB fingerprint; ISSERCNT confirmed; config fields and UI not decoded.

---

### SD — Standard Detail / Estimate Details

Stores standard production detail records. Primary table: **ISSDET** (standard detail). T7SDET module (58 procs confirmed). Works alongside ISSTYPE. Likely stores labor/machine time standards per operation for estimating and quoting.

**Confidence: 42/100** — Module and table confirmed; field meanings partially inferred from naming.

---

### RF — RFQ from Estimates

Generates Request-for-Quote (purchasing) directly from production estimates. Tables: **ISESTDTL** (estimate details), **BKMRPPO** (MRP planned POs), **BKSBVEND** (sub-vendor/RFQ vendor records). T7RFQ module (103 procs). Links the estimating workflow to vendor quoting, allowing estimate line items to generate vendor quote requests.

**Use case:** From an estimate for a customer job, automatically generate RFQs to vendors for materials or outside processes needed.

**Confidence: 50/100** — Module and tables confirmed; full workflow sequence not traced from source.

---

### EM — Emergency GL Entry

Manual/emergency GL journal entry module. Table: **BKGLTRAN** (standard GL transactions). T7EMA module found in rwn_symbols.json. Allows posting of manual adjusting journal entries outside the normal AR/AP/PR posting cycle — for corrections, period-end adjustments, or inter-company entries.

**Use case:** Post a manual GL entry to correct a balance or record a transaction that has no source document (e.g., depreciation, accruals outside payroll).

**Confidence: 38/100** — Module identified; uses standard GL table; exact form fields not decoded.

---

### EvoRemind — Reminder System

Automated reminder and follow-up system. Primary tables: **ISREMIND** (reminder records), **ISSCHED** (scheduler job queue). EvoRemind.RWN has 116 procs; also used by EvoService and EvoScheduler. Reminders are date/time triggered and can be linked to AR customers, AP vendors, CRM contacts, or free-form notes.

**Use case:** Schedule a follow-up call with a customer, set a payment reminder for an overdue invoice, or create a recurring task for a maintenance schedule.

**Tables:** ISREMIND — reminder record (date, contact, trigger type, linked record key, note text); ISSCHED — scheduler job queue (timed execution of EvoRemind checks).

**Confidence: 52/100** — Tables confirmed from DB fingerprint; reminder record structure partially inferred; trigger mechanism not fully decoded.

---

### GT — Lookup Grid / Grid Templates

Stores user-configured lookup grid layouts. Primary table: **BKLUGRID** (lookup grid definitions). Module T7GT found in rwn_symbols.json. Allows users to define and save custom column layouts for data-entry lookup dialogs (e.g., item lookup, customer lookup) so they see preferred columns.

**Use case:** Customize which columns appear when you press F3 (lookup) in a data entry screen.

**Confidence: 40/100** — Table confirmed; UI customization purpose inferred from table name; config fields not decoded.

---

### JA — Java Integration Setup

Configuration interface for the EvoERP Java integration layer (EvoPVT.jar). Uses **ISJAVA** task queue table. T7JAA/T7JAB modules found. Provides setup UI for the Java bridge that enables SQL reporting and external data export (e.g., Crystal Reports via Pervasive JDBC, or web-facing dashboards).

**Use case:** Configure the Java SQL helper service, set up JDBC connection parameters, or troubleshoot EvoPVT.jar task queue processing.

**Confidence: 45/100** — Module identified; ISJAVA table documented from prior analysis; setup UI fields not decoded.

---

### PI — Physical Inventory

Periodic physical inventory process. Three phases: freeze → count → post.

**Phase 1 — Freeze:** Lock current inventory quantities into BKPIFROZ/PIBINLOC/PIBINLOT snapshot. Creates a BKPIMSTR record for this PI run.

**Phase 2 — Count:** Enter counted quantities into:
- BKPIPHYS — per item per location
- BKPILOT — per lot
- BKPISER — per serial number
Hand-held device entry via T7DEHD opens the same PI tables.

**Phase 3 — Post:** T7PIB/T7PICA compares counts to the frozen snapshot, calculates variances, posts adjustment transactions to BKGLTRAN (GL) and INVTXN (inventory).

**Use case examples:**
- "How do I start a physical inventory count?" → PI-A (main form), freeze inventory, print count tags, enter counts, post.
- "How do I handle a partial count (cycle count)?" → Use bin/location filter in the count entry form.
- "What GL account gets the inventory adjustment?" → Configured in system defaults (BKSYMSTR) as the inventory adjustment GL account.

**Confidence: 52/100** — Module family confirmed from DB fingerprints; 7 PI tables confirmed; phase sequence inferred from table roles; exact form fields not decoded.

---

### JC — Job Cost

Tracks detailed cost against customer jobs, separate from standard WO cost tracking. Used for project-based manufacturing and service jobs.

**Key sub-modules:**
- T7JCA — Job Cost admin/setup
- T7JCENG — Engineering/routing: attaches routing specs (BKRTSPEC) and labor standards to the job
- T7JCM — Job Cost master entry: main data-entry form (customer, item, labor, materials)
- T7JCB/E/N/P — Cost detail sub-screens (material projections, sub-contract, WIP)
- T7JCF — QC integration: links quality transactions to job cost
- T7JCL/Q/R — Job cost list, query, reports

**Key tables:** BKSBPART (sub-contracted parts), BKSBMFG (sub-contracted manufacturing), BKPRMSTR (payroll/employee for labor cost), BKQCTRAN (QC results per job)

**Use case examples:**
- "How do I create a job cost estimate?" → JC-A sets up the job; JC-E enters cost roll-up.
- "How do I link a WO to a Job Cost record?" → Job number field on WO entry (ISJOB table).
- "How do I view sub-contract costs for a job?" → BKSBPART/BKSBMFG records accessed via T7JCB.

**Confidence: 68/100** — DFM forms read + DB fingerprints confirmed; detailed field semantics from DFM analysis.

---

### ES — Estimating / Quoting

Creates cost estimates for customer RFQs. Estimates can be converted to Sales Orders or Work Orders.

**Key sub-modules:**
- T7ESD — Estimate defaults (BKESTCFG: markup percentages, numbering)
- T7ESB / T7ESE — Main estimate entry forms (customer, items, qty, customer PO#)
- T7ESC / T7ESH / T7ESI — Cost detail: BKMATCST (material), BKRFQ (vendor quotes), BKRTCST (routing/labor cost)
- T7EST — Estimate templates (create standard estimates)

**Estimate → Order conversion:** From a completed estimate, the user can generate a SO (converts to BKARINV/BKARINVL) or a WO (converts to WORKORD/WOBOM). The ISESTDTL table holds estimate detail lines; ESTSUM holds rolled-up totals.

**Use case examples:**
- "How do I create a quote for a customer?" → ES-B (main entry), add line items with part numbers, costs auto-populate from BKICMSTR/BKRTCST.
- "How do I convert an estimate to a Sales Order?" → From the estimate form, use the SO conversion function.
- "How do I get vendor pricing into an estimate?" → RF module (RFQ from Estimates) generates vendor RFQs that feed back into BKRFQ.

**Confidence: 58/100** — DFM forms + DB fingerprints; conversion workflow inferred; exact BKESTCFG fields not decoded.

---

### SA — Sales Analysis

Reporting and analysis of sales performance. Separate from standard AR invoicing — uses aggregated/summarized data (BKSAREPT saved templates).

**Key sub-modules:**
- T7SAM / T7SAN — Main sales analysis reports with currency filter (from_cur/thru_cur)
- T7SAO — Top-N Sales Report
- Additional variants for: actual margin, salesperson performance, customer ranking, class/category filters

**Integration:** Uses BKARCUST, BKARINV, BKARINVL (AR invoice data), BKPRSALE (salesperson), BKCMLEAD/BKCMTERR (CRM territory/lead), ISRMAI (RMA auto-invoices for return deductions), ISMCF/ISMCR (multi-currency conversion).

**Use case examples:**
- "What are my top 10 customers by sales?" → SA-O (Top N Report)
- "What is the actual margin on shipped orders?" → SA-Q (Actual Margin Report: from/thru ship date)
- "How do I see sales by territory?" → BKCMTERR filter in SA reports.

**Confidence: 58/100** — DFM forms read in prior passes + DB fingerprints; aggregation method (live AR query vs. pre-built BKSA.* summary table) not fully confirmed.

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
| ACDETAIL | ACDETAIL.B | AC | NCR detail lines | AC.DET.ID, AC.DET.LINE, AC.DET.PART |
| ACRDTYPE | ACRDTYPE.B | AC | NCR disposition codes | TYPE, REASON, DISPO (rework/scrap/use-as-is), EXTRA1/2 |
| BKARTXN | BKARTXN.B | AR | AR transaction log | AR activity/posting history |
| BKCMACCC | BKCMACCC.B | CM | CRM account classifications | A/B/C/custom classification codes |
| BKCMACCN | BKCMACCN.B | CM | CRM account master | Company, address, territory, contacts, EMAIL[1..9] |
| BKCMLEAD | BKCMLEAD.B | CM | CRM lead sources | Lead source codes and descriptions |
| BKCMTERR | BKCMTERR.B | CM | CRM territories | Territory codes and names |
| BKICTAX | BKICTAX.B | IN | IC tax codes | Item-level tax classification for invoicing |
| BKPRSALE | BKPRSALE.B | CS | Salesperson master | Commission rate, method, GL account, agent-vendor link |
| FILEDES | FILEDES.B | System | File descriptions | Purpose strings for each registered Btrieve file |
| ISBINLOC | ISBINLOC.B | WC | Bin locations | Bin location master (distinct from BKICLOC item bins) |
| ISBINLOT | ISBINLOT.B | IN/WO | Bin-lot cross-ref | Which lot numbers are in which bins |
| ISBUILD | ISBUILD.B | BM | Build records | Kit/BOM build operation records |
| ISACCESS | ISACCESS.B | Security | Module access | License/module access control — which modules are enabled |
| ISACTION | ISACTION.B | AC | Action items | Corrective action tracking (type/desc/misc) |
| ISAPCHG | ISAPCHG.B | AP | AP extra charges | Additional charges on AP invoices (parallel to ISARCHG) |
| ISARCHG | ISARCHG.B | AR | AR extra charges | Additional charges added to AR invoices beyond line items |
| ISDEPT | ISDEPT.B | HR | Departments | Department master — codes, names, GL accounts |
| ISFSINFO | ISFSINFO.B | FS | Field service info | Field service call/information records |
| ISFSCLAS | ISFSCLAS.B | FS | FS class master | Field service class definitions |
| ISGLCOA | ISGLCOA.B | GL | GL COA extension | Multi-year history + budget data per GL account |
| ISGLDATE | ISGLDATE.B | GL | GL period dates | Current GL period dates per company and module |
| ISICMSTR | ISICMSTR.B | IN | IS item master | Secondary/extension item master (alternate item config) |
| ISMCF | ISMCF.B | IM | Multi-currency config | Foreign exchange configuration (base currency, conversion rules) |
| ISMCR | ISMCR.B | IM | Exchange rates | Currency exchange rate history by date |
| ISREMIND | ISREMIND.B | CRM | Reminders | Reminder/follow-up records — date, contact, trigger type |
| ISREPDEF | ISREPDEF.B | Reports | Report defaults | Saved report parameter defaults per user/report |
| ISREPORD | ISREPORD.B | AR | Repeat orders | Standing/recurring AR order records |
| ISREPLNK | ISREPLNK.B | System | Replace links | Record-link replacement tracking |
| ISSEPROC | ISSEPROC.B | SR | SE process codes | Service error process codes (SR module support) |
| ISSERIAL | ISSERIAL.B | SC | Active serials | Active serial number tracking (complement to SERIAL master) |
| ISSHIPCO | ISSHIPCO.B | SM | Shipping carriers | Shipping company/carrier master — codes, names, contacts |
| ISSMTCFG | ISSMTCFG.B | SM | SMT machine config | Surface mount technology machine configuration (PCB assembly) |
| ISSETYPE | ISSETYPE.B | SR | SE type codes | Service error category/type codes |
| ISSTYPE | ISSTYPE.B | SR | Shared type codes | Shared service/storage/equipment type code table |
| ISPRINFO | ISPRINFO.B | PR | Employee PR info | Payroll employee profile/additional info records |
| WODATE | WODATE.B | WO | WO operation dates | Operation dates per WO — START/FINISH/QTY, parent/top hierarchy |
| BKLUGRID | BKLUGRID.B | GT | Lookup grid config | User-saved column layout definitions for F3 lookup dialogs |
| BKMRPPO | BKMRPPO.B | RF/MR | MRP planned POs | Planned purchase orders generated by MRP or RFQ-from-estimates |
| BKSBVEND | BKSBVEND.B | RF | Sub-vendor / RFQ vendors | Vendor records specific to RFQ / sub-contracting workflow |
| BKSYUSER | BKSYUSER.B | AD | System user extensions | Extended user configuration for Advanced DC module |
| EIMCOLST | EIMCOLST.B | AD | EIM column state | Column visibility/state tracking for Advanced DC forms |
| ISBSF | ISBSF.B | BS | Business score fields | Customer scoring/profitability metrics (BS module) |
| ISESTDTL | ISESTDTL.B | RF | Estimate details | Line-level detail records for production estimates; source for RFQ generation |
| ISSCHED | ISSCHED.B | Scheduler | Scheduler jobs | EvoScheduler/EvoRemind job queue — timed task records (confirmed from EvoSched.RWN, EvoScheduler.RWN, EVOSERVICE.RWN) |
| ISSERCNT | ISSERCNT.B | IT | Serial counters | Auto-serial number counter state per item/config |
| ISSDET | ISSDET.B | SD | Standard details | Standard labor/machine time detail records per operation |
| ISTRIGRS | ISTRIGRS.B | AD | Trigger actions | Automated trigger rules for Advanced DC events |
| SCHEDCAL | SCHEDCAL.B | Scheduler | Scheduler calendar | Schedule calendar used by T7SHE (shop scheduling due-date changes) and T7SMH |
| ISLINKS | ISLINKS.B | System | EvoLinks attachments | Document attachment cross-reference — record key → linked document path/filename (EvoLinks.RWN, 156 procs) |
| BKPIMSTR | BKPIMSTR.B | PI | PI run master | Physical inventory run/session master — one record per PI freeze cycle |
| BKPILOT | BKPILOT.B | PI | PI lot counts | Physical inventory lot count records (lot, location, counted qty) |
| BKPIPHYS | BKPIPHYS.B | PI | PI physical counts | Physical count records (item, location, count qty) |
| BKPISER | BKPISER.B | PI | PI serial counts | Physical inventory serial number count records (found/missing status) |
| BKPIFROZ | BKPIFROZ.B | PI | PI frozen snapshot | Inventory snapshot taken at PI freeze time — baseline for variance calculation |
| PIBINLOC | PIBINLOC.B | PI | PI bin location | Frozen bin-location records at PI start |
| PIBINLOT | PIBINLOT.B | PI | PI bin lot | Frozen bin-lot records at PI start |
| BKESTCFG | BKESTCFG.B | ES | Estimate config | Estimate module settings (method, markup defaults, numbering) |
| BKMATCST | BKMATCST.B | ES | Material cost | Estimate line-level material cost + pricing detail records |
| BKRFQ | BKRFQ.B | ES/RF | RFQ master | Request for Quote master — vendor RFQ records tied to estimates |
| BKRTCST | BKRTCST.B | ES | Routing cost | Routing cost detail per estimate operation (labor/machine rates) |
| ESTSUM | ESTSUM.B | ES | Estimate summary | Rolled-up cost/price totals per estimate |
| BKICPMAT | BKICPMAT.B | IN/ES | IC purchase material | Item-level purchase material category/config |
| BKICREF | BKICREF.B | IN | IC cross-reference | Item cross-reference (alternate part numbers, customer/vendor part#) |
| BKSBPART | BKSBPART.B | JC/PO | Sub-contract parts | Components sourced from outside-process / sub-contract vendors |
| BKSBMFG | BKSBMFG.B | JC/MR | Sub-contract mfg | Sub-contracted manufacturing operation records |
| BKMENUSU | BKMENUSU.B | PS | Menu user settings | Per-user menu/toolbar layout and saved configuration |
| BKPSUSER | BKPSUSER.B | PS | PS user settings | Per-user personal settings (printer preferences, column layouts) |
| BKSAREPT | BKSAREPT.B | SA | SA report templates | Sales analysis saved report template definitions |
| ISAREX | ISAREX.B | AR/SA | AR extras | Extended AR customer/invoice additional information |
| ISRMAC | ISRMAC.B | RM | RMA credit | RMA credit note records (return merchandise credit authorizations) |
| ISRMAI | ISRMAI.B | RM/SA | RMA invoice | RMA auto-invoice/return material invoice records |
| ISFOHEAD | ISFOHEAD.B | FO | FO header | Field/forecast order header (order#, customer, dates, status) |
| ISFOLINE | ISFOLINE.B | FO | FO lines | Field/forecast order line items (product, qty, price) |
| ISFOORDL | ISFOORDL.B | FO | FO order list | Multi-field/forecast order management list |
| ISBANKS | ISBANKS.B | System | Bank accounts | Bank account master (account codes, bank names, GL accounts) |
| ISNUMBER | ISNUMBER.B | System | Number sequences | Auto-increment number sequence definitions (counters per entity type) |
| BKDCCFG | BKDCCFG.B | DC | DC configuration | Data collection terminal/station configuration settings |
| BKDCLAB | BKDCLAB.B | DC | DC labor records | Data collection labor entry records from DC terminals |
| BKEDMSTR | BKEDMSTR.B | EDI | EDI master | EDI trading partner / transaction set master |
| BKGLX | BKGLX.B | GL | GL extended | GL extended transaction data (supplemental GL fields) |
| BKGLGJRN | BKGLGJRN.B | GL | GL journal header | GL general journal header records |
| BKGLGJLN | BKGLGJLN.B | GL | GL journal lines | GL general journal line entries |
| BKBMNOTE | BKBMNOTE.B | BM | BOM notes | Text notes attached to BOM components |
| BKBMREMK | BKBMREMK.B | BM | BOM remarks | Structured remarks on BOM components |
| BKQCMSTR | BKQCMSTR.B | QC | QC master | QC test/inspection master records |
| BKQCTRAN | BKQCTRAN.B | QC | QC transactions | QC inspection transaction records (pass/fail per inspection) |
| WORECV | WORECV.B | WO | WO receipts | WO production receipt records (parts received/completed per op) |
| WOBOMREM | WOBOMREM.B | WO | WO BOM remarks | Remarks attached to WO BOM components |
| OUTPROC | OUTPROC.B | WO/RO | Outside process | Outside processing operation records (WO ops sent to external vendors) |
| ISNCR | ISNCR.B | QC/AC | NCR records | Non-conformance report records linked to QC/AC module |
| ISTAXGRP | ISTAXGRP.B | System | Tax groups | Tax group/nexus definitions (state, county, city tax combinations) |
| ISTERMS | ISTERMS.B | System | Payment terms | Payment terms definitions (net-days, discount %, EOM flag) |
| ISSOBOX | ISSOBOX.B | SO | SO box | SO packing/box assignments for multi-box shipments |
| ISUSAGE | ISUSAGE.B | IN | Usage tracking | Item usage tracking (consumption history by customer/period) |
| BKSHORT | BKSHORT.B | WO/SO | Short supply | Short supply records — items insufficient for open WO/SO orders |
| LANGDICT | LANGDICT.B | System | Language dict | Multi-language UI label translations (ML module) |
| BKGLSTMT | BKGLSTMT.B | GL | GL statement templates | Named financial report layouts (P&L, Balance Sheet, custom) |
| BKGLFSTL | BKGLFSTL.B | GL | Financial stmt lines | User-defined row format definitions for BKGLSTMT reports |
| BKGLGJRN | BKGLGJRN.B | GL | GL journal headers | Batch/journal header records for manual general journal entries |
| BKGLGJLN | BKGLGJLN.B | GL | GL journal lines | Individual debit/credit lines within a GL journal entry |
| BKPRCURP | BKPRCURP.B | PR | PR current period | YTD and current-period payroll amounts per employee |
| BKPRFTAX | BKPRFTAX.B | PR | PR federal tax tables | Federal and state withholding rate schedules |
| BKPRGLFL | BKPRGLFL.B | PR | PR GL flags | Maps each payroll expense type to its target GL account |
| BKPRINFO | BKPRINFO.B | PR | PR employee extra | Supplemental employee fields beyond the main BKPRMSTR record |
| BKPRTC | BKPRTC.B | PR | PR time cards | Individual time-card entries (employee × job × operation) |
| BKARINVI | BKARINVI.B | AR | AR inv-inventory link | Links AR invoices to the inventory transaction records they generated |
| BKART | BKART.B | AR/TC | AR transaction log | Condensed AR/AP transaction short log for rapid lookup |
| ISCHAINM | ISCHAINM.B | CH | Chain master | Multi-location chain master — codes, names, relationships |
| ISDROP | ISDROP.B | DR | Dropdown lists | User-configurable picklist options for configurable fields |
| ISCTREVU | ISCTREVU.B | CR | Contract review | SO approval workflow state (department/password/status records) |

---

## MODULE QUICK REFERENCE — Pass 12 Additions

### SC — Cycle Count / Serial Control
**What it does:** Performs partial physical inventory by location, category, or item class — without shutting down the full warehouse. Complement to the PI module for continuous accuracy.

**When to use SC vs. PI:**
- SC = regular spot-counts by location or class (ongoing)
- PI = full warehouse freeze, blind count, and post (annual or semi-annual)

**Key tables:** BKICLOC (inventory by location), BKICLOCM (location master), ISBINLOC (bin assignments), ISCATMST (category master), INVTXN (inventory transaction postings)

**Menu path:** Look for **SC** codes in the Inventory or Warehouse menus.

**Files:** T7SCF (main count entry), T7SCC (with AR adjustment), T7SCH (count history), T7SCA (adjustments), T7SCG (by category), T7SCOMP (company-level)

---

### GL Sub-Modules
**How GL is organized — each screen is a separate RWN:**

| Sub-module | Function | Key tables |
|-----------|---------|-----------|
| **T7GLB** (GL-B) | General journal entry — manual debit/credit batches | BKGLGJRN, BKGLGJLN |
| **T7GLE** (GL-E) | Direct transaction posting | BKGLTRAN, BKGLCOA |
| **T7GLF** (GL-F) | Financial statements — generate P&L, Balance Sheet | BKGLSTMT, BKGLCOA |
| **T7GLN** (GL-N) | Budget maintenance — define budget by account/period | BKGLFSTL, BKGLCOA |
| **T7GLL** (GL-L) | Check listing — AP check register posted to GL | BKAPCHKF, BKGLCHK |
| **T7GLC** (GL-C) | Period close — close accounting period | BKGLTRAN, BKGLCOA |
| **T7GLT** (GL-T) | Trial balance — all accounts with debit/credit totals | BKGLCHK, BKGLTRAN |
| **T7GLESPEED** | Speed / fast GL entry — abbreviated posting for high-volume shops | BKGLTRAN, BKGLCOA |

**Tip:** GL financial statements (T7GLF) use BKGLSTMT (layout templates) which reference BKGLFSTL (line definitions). You define the format once, then run it for any period.

---

### PR Extended Tables
**Additional tables confirmed in Pass 12:**

| Table | Purpose |
|-------|---------|
| BKPRCURP | Current-period employee accumulators (YTD gross, taxes, deductions) |
| BKPRFTAX | Federal/state tax rate tables — updated annually per IRS Pub 15 |
| BKPRGLFL | GL account mapping for each payroll expense type |
| BKPRINFO | Extra employee demographics (emergency contact, notes) |
| BKPRTC | Time card entries — import path from DC terminal to payroll |
| BKPRAGNT | Payroll agency/garnishment records (union dues, child support, levies) |

---

### TC — Treasury Control (T7TCC)
**What it does:** Bank reconciliation and cash management — handles AP check posting (BKAPCHKF), AR deposit application (BKARDEP), AR invoice matching (BKARINVI), and the resulting GL check transactions (BKGLCHK). The module that clears checks and marks deposits as applied.

---

### KI — Kit Assembly (T7KIT)
**What it does:** Builds a kit item from its components. Pulls components from BKICLOC (by location), builds the parent kit item, and posts the inventory adjustment. Uses BKPRMSTR for labor if the kit build includes labor operations.

---

### MA — AR Deposit Application (T7MAPDEPO)
**What it does:** Maps/applies customer deposits to open AR invoices. Uses BKARDEP (deposit master), BKARINV (invoice header), BKARINVL (invoice lines), BKARINVT (invoice tax). This is the "apply cash receipts" step after deposits are entered.

---

### TE — NACHA/ACH Testing (T7TESTNACHA)
**What it does:** Generates and validates NACHA-format ACH files for electronic payment (direct deposit or AR collection). Uses ISBANKS (bank account master) and BKGLCHK (check history). A utility module for testing ACH transmission before live payroll or customer payment runs.

---

### CH — Multi-Location Chain (T7CHAIN / T7CHAINM)
**What it does:** Manages multi-location chain relationships. ISCHAINM holds the chain master — location codes, names, and which locations share customer/vendor data. Used in companies running EVO across multiple sites.

---

### DD — Data Dictionary Check (T7DDCHECK)
**What it does:** Admin utility that validates the Pervasive Btrieve data dictionary (FILEDICT, FILEKEY) for consistency. Checks that DDF file/field/key definitions match the actual `.B` data files. Run after any schema change or data migration.

---

## MODULE QUICK REFERENCE — Pass 13 Additions

### SM — System Maintenance + Item Inquiry Hub (58 files)
SM is the largest module family and serves two distinct purposes:

**1. Setup and Maintenance screens** — cross-module code table entry:

| Sub-module | What it maintains |
|-----------|-----------------|
| SM-C (T7SMCA/B/C) | Item class codes and location assignments |
| SM-D (T7SMD) | Payment terms |
| SM-E/F (T7SME/F) | Tax codes, tax groups, tax files, GL accounts |
| SM-G/GA (T7SMG/GA) | Employee ↔ work center assignments (PR ↔ WC) |
| SM-H (T7SMH) | Shop scheduling calendar (work days, shifts per work center) |
| SM-IA/B/C/D/E/F | CRM code tables: lead types, territories, action codes, contact codes, discount codes, categories |
| SM-N/NA/NF (T7SMN) | Notes type master — categories of notes |
| SM-O (T7SMO) | Outside process + shipping company master |
| SM-PA/B/F/H/I/J | Item code assignments: category, user-defined, GL job, cycle count, defect, count unit-level |
| SM-SC/SD | Access control by class/category |
| SM-T/U (T7SMT/U) | Ship-via codes + comprehensive receipt/shipping setup |
| SM-TEND/TSET | Smart Terminal (machine/barcode terminal) configuration |
| SM-W (T7SMW) | Order description codes |

**2. Item Inquiry (SM-J series)** — enter an item number, see all its data across every module:
- T7SMJL (459 procs) = **main panel** — complete item overview
- T7SMJC = On-hand by location
- T7SMJB = Open work orders using this item
- T7SMJD = Inventory transaction history
- T7SMJF = Open purchase orders
- T7SMJG = QC records
- T7SMJI = Estimates and sales order history
- T7SMJJ = AR invoice detail
- T7SMJN = Vendor information
- T7SMJO = AP checks and AR deposits
- T7SMJQ/JS/JT = Lot, serial, QC detail

**How to use Item Inquiry:** Go to the SM module, enter an item number, and use the tabs/sub-screens to drill into any related transaction or document.

---

### FO — Features & Options (4 EVO modules)
**What it does:** Allows configurable product options to be defined at the BOM level and selected by customers at order entry. Example: a customer orders a pump — they can choose Color (Red/Blue/Green) and Seal Type (Standard/High-temp). Each option choice drives different component requirements.

**How the flow works:**
1. Define option sets in **EVOFNO** (ISFOHEAD + ISFOLINE) — like a mini-BOM per option
2. When entering an SO, EvoFNOSO shows the option menu and records choices in ISFOORDL
3. When a WO is created, EvoFNOWO adds the chosen components to the WO BOM automatically
4. POs for option-specific components use EvoFNOPO

**Key tables:** ISFOHEAD (option set header), ISFOLINE (option component lines), ISFOORDL (per-order selections), ISFOHIST (history)

---

### Notes System (EVONOTES family)
**What it does:** Cross-module freeform notes attached to any entity — an item, a sales order, a purchase order, or a work order. All notes share the ISNOTES table, tagged by entity type.

- **EVONOTES**: Enter and view notes on any record
- **EVONOTESRPT**: Print/export notes filtered by entity, date range, or note type
- **EVONOTESARCH**: Browse archived notes including work order change history (WORKCHG)

**Note types** are configured in SM-N (ISNTYPE) — e.g. "Customer complaint," "Engineering change," "Follow-up."

---

### MR — MRP Planning Engine (17 files)
**Critical distinction:** BM module = define BOM structures; MR module = run MRP calculations.

**What MRP does:** Takes open demand (SO lines + build targets), subtracts supply (on-hand, open POs, open WOs), explodes through the BOM, and generates *recommendations* for what to buy and make.

**MRP Workflow:**
1. Demand from SO lines (BKARINVL) + ISBUILD build targets
2. Supply: on-hand (BKICLOC) + open PO receipts (BKAPPOL) + open WO completions (WORKORD)
3. BOM explosion: BKBMMSTR components resolved recursively
4. Output stored in **MTMRP** (planned order recommendations)
5. User reviews via T7MRG/H/I/O (browse MTMRP by item, class, location)
6. User firms changes via T7MRADE → **BKMRPFC** (firmed = won't regenerate next run)
7. Release planned POs: T7MRJX converts **BKMRPPO** → **BKAPPO** (actual purchase order)
8. Release planned WOs: T7MRIX links to WORKORD (via WO module)

| Table | Purpose |
|-------|---------|
| MTMRP | Calculated planned order output — what MRP recommends to buy/make |
| MTICMSTR | MRP snapshot of item master (used during calculation) |
| BKMRPFC | User-firmed changes — overrides that survive MRP regeneration |
| BKMRPPO | Planned PO records — buy recommendations not yet released as real POs |
| ISBUILD | Manual build schedule targets (demand source alongside SOs) |

**How to use:** Run from the MRP menu. After regenerating, review T7MRG (planned orders), firm/edit as needed, then release to purchasing (T7MRJX → creates actual POs).

---

### GE — Generic Import / Utility Tools
- **T7GENIMP**: Schema-aware generic importer — uses Pervasive DDF (FILEDICT, ISFIELDS) to import data into any table dynamically. Admin tool for bulk data loads.
- **T7GENAED / T7GENGET**: Generic add/edit/delete and lookup for service/type code tables (ISSTYPE).
- **T7GETDEP**: AR deposit detail retrieval — fetches ISARDEPL deposit lines for a given deposit.
- **T7GETWEB**: Web-facing deposit retrieval wrapper (thin, 6 procs).

---

## TABLE QUICK REFERENCE — Pass 13 Additions

| Table | File | Module | One-line purpose |
|-------|------|--------|-----------------|
| MTMRP | MTMRP.B | MR | MRP output — planned order recommendations (qty, date, item) |
| MTICMSTR | MTICMSTR.B | MR | MRP shadow item master — item data snapshot for MRP run |
| BKMRPFC | BKMRPFC.B | MR | MRP firm changes — user-locked planned order overrides |
| BKMRPPO | BKMRPPO.B | MR | MRP planned POs — unconfirmed buy recommendations |
| ISBUILD | ISBUILD.B | MR | Build schedule — manual production targets fed into MRP |
| ISICMSTR | ISICMSTR.B | MR | IS item config master — extended item data for multi-location MRP |
| ISARDEPL | ISARDEPL.B | AR | AR deposit lines — line-level payment application within a deposit |
| MKAHIST | MKAHIST.B | Infra | MKA audit history — system-wide change/event log (universal) |
| ISLOG | ISLOG.B | Infra | IS activity log — user action audit trail (universal) |
| ISIS | ISIS.B | Infra | IS image/icon system — UI icon lookup table (universal) |
| BKCMACCN | BKCMACCN.B | Infra | CM account number cross-reference (universal) |
| BKAPDESC | BKAPDESC.B | Infra | AP/AR description text lookup (universal) |

---

### KEYWORD / TERM GLOSSARY

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
| **MRP** | Material Requirements Planning — calculates what to buy/make and when (MR module) |
| **MRP firm change** | A user-locked planned order (BKMRPFC) that survives MRP regeneration |
| **planned order** | MRP's buy/make recommendation before it's released as a real PO or WO |
| **build schedule** | Manually-entered production targets (ISBUILD) that feed MRP demand |
| **MTMRP** | MRP output table — planned order recommendations generated by MRP run |
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

*Last updated: 2026-06-17. Built from SRC analysis, schema extraction, CHM decompilation,
DFM parsing, and RWN symbol extraction (rwn_symbols.json — 1,122 modules). See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*
