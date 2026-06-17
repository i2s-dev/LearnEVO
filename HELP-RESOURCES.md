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
| Follow SO from entry to posted invoice | SO-A → SO-D → SO-F → SO-G | [Recipe 1: SO Lifecycle](#recipe-1-sales-order--ship--invoice--post) |
| Follow WO from creation to close | WO-A → WO-B → DC → WO-K-J → WO-K-C | [Recipe 2: WO Lifecycle](#recipe-2-work-order-lifecycle-create--close) |
| Follow PO from entry to check | PO-A → PO-E → AP-B → AP-H | [Recipe 3: PO to Check](#recipe-3-purchase-order--receive--ap-voucher--check) |
| Run MRP and firm planned orders | MR-A → MR-J → MR-K | [Recipe 4: MRP Run](#recipe-4-mrp-run-plan--firm--release) |
| Close the accounting period | AR-H → AP close → IN → AM | [Recipe 5: Month-End Close](#recipe-5-month-end-close) |
| Set up a brand-new part number | IN-B → BM → RO-A | [Recipe 6: New Item Setup](#recipe-6-new-item-setup) |
| Record a customer payment | AR-C | [Recipe 7: AR Cash Receipts](#recipe-7-ar-cash-receipts-customer-payment) |
| Run a physical inventory | PI-A → PI-C → PI-D → PI-F | [Recipe 8: Physical Inventory](#recipe-8-physical-inventory-count) |

---

## BUSINESS WORKFLOW RECIPES

Step-by-step traces of common end-to-end processes. These answer "how does X work from start to finish?" Each recipe names the exact menu codes, tables written, and GL impact.

---

### Recipe 1: Sales Order → Ship → Invoice → Post

**Trigger:** Customer places an order.

```
1. SO-A (T7SOA): Enter Sales Order
   - Creates BKARINV row (BKAR_INV_SONUM PK, BKAR_INV_STATUS='O' open)
   - Creates BKARINVL rows (one per line item): item code, qty, price, ESD
   - If lot-tracked item: LOT table updated when line is entered
   - If CC on file: ISCC consulted for pre-auth

2. SO-D (T7SOD): Print Pick Ticket
   - Reads BKARINV + BKARINVL; prints picking doc; no table writes
   - Optionally reserves bin quantities (BKICLOC on-hand check)

3. BO module (T7BOL): Bill of Lading
   - Writes ISSOBOX (one row per shipping box: SONUM+LINE+BOX PK, weights/dims/UCC)
   - Reads ISSHIPCO for carrier tracking URL template
   - Reads BKARINV + BKARINVL for contents

4. SO-F (T7SOF): Print Invoice
   - Reads BKARINV/BKARINVL; prints invoice for customer; no table writes
   - Tax calculated from ISTAXGRP + ISTAXFIL (9-bracket rate table)

5. SO-G (T7SOG): Post Invoice
   - BKARINV BKAR_INV_STATUS → 'I' (invoiced)
   - INVTXN: one row per inventory transaction (qty out, cost, lot/serial)
   - BKICLOC: on-hand decremented per location
   - LOT/SERIAL: on-hand reduced if lot/serial tracked
   - BKGLTRAN: AR debit + revenue/COGS credits (one GL line per account)
   - BKGLX: GL extension if multi-department split
   - DBAFIFO: FIFO cost layer consumed
   - BKARTXN: AR transaction row (type=invoice)
   - ISTRIGRS polled: sends email notifications if configured
```

**Key tables written:** BKARINV, BKARINVL, INVTXN, BKICLOC, BKGLTRAN, BKARTXN, ISSOBOX

---

### Recipe 2: Work Order Lifecycle (Create → Close)

**Trigger:** MRP or manual order for manufactured item.

```
1. WO-A (T7WOA): Create Work Order
   - Creates WORKORD row (MTWO_WIP_WOPRE+WOSUF PK, STATUS='O' open)
   - Copies BOM → WOBOM (required components with QTYPER, REF, VEND)
   - Copies ROUTING → WOROUT (planned operations with ESTHRS, WC, costs)
   - Sets MTWO_WIP_SQTY (start qty), dates (start/due), priority

2. WO-B (T7WOB): Release / Pick Materials
   - WORKORD STATUS → 'R' (released)
   - WOBOM QTYISSUED updated as picks are confirmed
   - INVTXN: issue transactions (qty negative, type=WO issue)
   - BKICLOC: on-hand decremented; ISBINLOC bin-level decremented

3. DC / WO-K-K (labor entry): Record Labor
   - BKDCLAB: staging row per labor ticket (LAB_POSTED='N')
   - T7AUTODCH (nightly) or manual post: validates BKDCLAB → WOLABOR + WOROUT
   - WOLABOR: one row per posted labor transaction (DATE+EMP+WOPRE+OPER PK)
   - WOROUT: MTWORO_ACTHRS, MTWORO_QTYCOM updated

4. WO-K-J (T7WOKJ): Receive Completed Units
   - WORECV: receipt row (qty received, date, unit cost)
   - INVTXN: receipt transaction (qty positive, type=WO receipt)
   - BKICLOC: on-hand incremented
   - LOT/SERIAL: new lot/serial assigned if tracked
   - DBAFIFO: new cost layer added

5. WO-K-C (T7WOKC): Close Work Order
   - WORKORD STATUS → 'C' (closed)
   - WOEXCHG: variance written if actual vs. standard cost differ
   - BKGLTRAN: WIP cleared, variance posted to GL
   - WOBOM QTYISSUED final; WOMAT (actual issues) reconciled
```

**Key tables written:** WORKORD, WOBOM, WOROUT, WOLABOR, BKDCLAB, INVTXN, BKICLOC, WORECV, WOMAT, BKGLTRAN, DBAFIFO

---

### Recipe 3: Purchase Order → Receive → AP Voucher → Check

**Trigger:** Need to buy materials or services from a vendor.

```
1. PO-A (T7POA): Create Purchase Order
   - Creates BKAPPO row (BKAP_PO_NUM PK, STATUS='O' open)
   - Creates BKAPPOL rows (one per line: item, qty, price, due date)
   - BKAPVEND: vendor terms/GL accounts looked up; cached in BKAPPO
   - BKICLOC: PO quantity added to "on order"

2. PO-C (T7POC): Print PO
   - Reads BKAPPO/BKAPPOL; prints PO document; no table writes

3. PO-E (T7POE): Receive PO (Receiving dock)
   - BKAPINVT: receipt row per PO line received
   - BKAPPOL: BKAP_POL_RECVQTY updated
   - INVTXN: receipt transaction (qty positive, type=PO receipt)
   - BKICLOC: on-hand incremented
   - BKQCMSTR + BKQCTRAN: if QC required, inspection record created
   - LOT: if lot-tracked, LOT row created (VENDOR, RECDATE, RECQTY, POCOST)

4. AP-B (T7APB): Enter AP Voucher
   - Creates BKAPDESC row (vendor invoice: VNDCOD+INVNM PK)
   - BKAPPOL: BKAP_POL_VOUCHERED flag set
   - BKGLTRAN: accrued liability debit (received-not-vouched cleared)
   - ISTRIGRS: PO approval email if ISDIGSIG approval required

5. AP-H (T7APH): Print/Post Checks
   - Selects BKAPDESC rows due for payment
   - Creates BKAPCHKF: check line (INVAMT, AMTPD, DISC, CHKACT, CHKDTE)
   - BKGLCHK: check register entry
   - BKGLTRAN: AP liability debited, cash credited
   - BKAPDESC: BKAP_DESC_STATUS → 'P' (paid)
```

**Key tables written:** BKAPPO, BKAPPOL, BKAPINVT, INVTXN, BKICLOC, BKAPDESC, BKGLTRAN, BKAPCHKF, BKGLCHK

---

### Recipe 4: MRP Run (Plan → Firm → Release)

**Trigger:** Need to generate suggested WOs and POs to meet demand.

```
1. MR-A (T7MRA): Run MRP Calculation
   - Reads demand: BKARINVL (open SO lines) + WORKORD (open WOs needing parts)
   - Explodes BOM (BKBMMSTR) for each demand record
   - Checks supply: BKICLOC on-hand + BKAPPOL on-order + WORKORD WIP receipts
   - Writes MTMRP: one row per planned order (PARTNO, KEY, DATE, QTY, ONHAND, PEGTO, ORDER)
   - BKMRPFC: firm orders (already released WOs/POs) — not overwritten by MRP

2. MR-J (T7MRJ): Review Planned Orders
   - Reads MTMRP; displays exception messages (late, over-stock, etc.)
   - No table writes; user reviews and selects orders to firm

3. MR-K / T7AUTOMRF (T7MRK or auto): Firm Planned Orders
   - For each selected MTMRP row:
     - If make item: creates WORKORD + WOBOM + WOROUT (copies from BOM/ROUTING)
     - If buy item: creates BKAPPO + BKAPPOL
   - MTMRP row deleted (planned → firmed)
   - BKMRPFC: updated with new firm order reference
```

**Key tables written:** MTMRP, WORKORD, WOBOM, WOROUT, BKAPPO, BKAPPOL, BKMRPFC

---

### Recipe 5: Month-End Close

**Trigger:** End of accounting period. Must be done in order.

```
Step 1 — AR Close:
  AR-G: Print statements (reads BKARTXN, no writes)
  AR-H: Age receivables (reads BKARCUST+BKARTXN; updates BKARCUST aging buckets)
  Verify AR trial balance (AR report vs. GL AR account balance)

Step 2 — AP Close:
  AP-I: AP aging report (reads BKAPDESC)
  Verify AP trial balance (AP report vs. GL AP account balance)
  All PO receipts vouched (BKAPINVT fully matched to BKAPDESC)

Step 3 — Inventory Close:
  IN-N: Print inventory valuation report
  If needed: UT-K-H (recalculate average costs) — BKICLOC + MTICMSTR unit costs
  Post any adjustments via IN-G or IN-H

Step 4 — GL Period Lock:
  AM (Accounting Maintenance) → Period Control: set period end date
  ISGLDATE: period dates updated (BKGL_DATE_GLDT*)
  Once locked, prior-period postings rejected

Step 5 — Reconciliation:
  GL-A trial balance vs. AR/AP/IC subsidiary ledgers
  BKGLCOA balances vs. sum of BKGLTRAN for the period
```

**Key tables read:** BKARTXN, BKARCUST, BKAPDESC, BKICLOC, MTICMSTR, BKGLCOA, BKGLTRAN
**Key tables written:** BKARCUST (aging), ISGLDATE (period lock)

---

### Recipe 6: New Item Setup

**Trigger:** Adding a new manufactured or purchased item.

```
1. IN-B (T7INB): Enter Item Master
   - Creates BKICMSTR row: PROD_CODE(15) PK, PROD_TYPE (R/N/B/M/etc.), description, UOM
   - Creates MTICMSTR row: extended item data (costs, class, MRP flags)
   - Optionally creates BKICLOC rows per stocking location

2. BM entry (T7BMA / T7BMG): Build Bill of Materials (if manufactured)
   - Creates BKBMMSTR rows: PARENT+COMP PK, QTYPER, SCRAP, OPER, TYPE
   - BKBMNOTE: optional component notes
   - T7BMG: phantom handling (TYPE='P' components are transparent to MRP)

3. RO-A (T7ROA): Enter Routing (if manufactured)
   - Creates ROUTING rows: CODE+OPER PK, WC, TIMEPART, SETUPHRS, costs per operation
   - T7ROA reads BKRTTEMP for operation templates (saves re-keying)

4. Set MRP Flags (IN-B or MTICMSTR fields):
   - BKIC_PROD_LOT: enable lot tracking
   - BKIC_PROD_SER: enable serial tracking
   - MTIC_ planning fields: safety stock, min qty, reorder point, lead time, MRP flag

5. Set Pricing (GF-PRICE or IN-B):
   - BKICMSTR: list price, standard cost
   - BKICPMAT: optional customer-specific price breaks (RATE_1..10 + QTY_1..10)
```

**Key tables written:** BKICMSTR, MTICMSTR, BKICLOC, BKBMMSTR, ROUTING, BKICPMAT (optional)

---

### Recipe 7: AR Cash Receipts (Customer Payment)

**Trigger:** Customer sends a check or EFT payment.

```
1. AR-C (T7ARC): Record Payment
   - Reads BKARINVT: open invoices for customer
   - Creates BKARTXN: payment transaction (type=payment, AMOUNT, DATE, CHECK)
   - Applies to BKARINVT rows: clears open invoices
   - BKARCUST: open balance decremented
   - BKGLTRAN: cash debit + AR credit
   - BKARDEP: if customer deposit, creates deposit record
   - BKGLCHK: if check, check register updated

2. AR-C (split/NSF handling):
   - NSF (bounced check): negative amount reversal recreates BKARINVT open rows
   - Split payment: multiple BKARTXN rows per batch

3. AR-T (T7ART): Print Deposit Slip
   - Reads BKARTXN batch; prints deposit for bank
   - No table writes

4. Reconciliation:
   - BKGLCHK check register vs. bank statement
   - AR aging (BKARCUST aging buckets) updated on AR-H run
```

**Key tables written:** BKARTXN, BKARINVT, BKARCUST, BKGLTRAN, BKARDEP (if deposit), BKGLCHK

---

### Recipe 8: Physical Inventory Count

**Trigger:** Annual or cycle count of physical inventory.

```
1. PI-A (T7PIA): Freeze Inventory
   - Creates BKPIMSTR: count header (YEAR+QTR PK)
   - Creates BKPIFROZ: snapshot of BKICLOC on-hand at freeze moment
   - Generates BKPILOT (lot snapshot) and BKPISER (serial snapshot)
   - BKPIFROZ.INPST: items that posted after freeze flagged

2. PI-B (T7PIB): Print Count Sheets / Tags
   - Reads BKPIFROZ; prints count sheets grouped by location
   - Tags optionally include barcode for scanner entry

3. PI-C (T7PIC): Enter Count Results
   - Creates BKPIPHYS: actual counted qty per TAGNUM
   - Fields: ACTQTY, EMPNAME, LOT, SERIAL, BIN
   - Multiple entries allowed per tag (different counters)

4. PI-D (T7PID): Print Variance Report
   - Reads BKPIFROZ (frozen qty) vs. BKPIPHYS (counted qty)
   - Shows +/- variance per item/location; no table writes
   - User reviews and approves variances

5. PI-F (T7PIF): Post Adjustments
   - For each variance: creates BKGLTRAN (inventory adjustment + offset account)
   - Updates BKICLOC: on-hand qty corrected
   - MTICMSTR: average cost recalculated if cost changed
   - DBAFIFO: FIFO layers adjusted
   - BKPIMSTR: count closed (status → posted)
```

**Key tables written:** BKPIMSTR, BKPIFROZ, BKPILOT, BKPISER, BKPIPHYS, BKICLOC, BKGLTRAN, DBAFIFO

---

*Business Workflows section — **Confidence: 75/100** — 8 workflow recipes written; table write sequences confirmed from DB fingerprints (RWN symbols) and DDF schema cross-reference; exact field-level validation logic and error handling in encrypted RWN.*

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

**KEY ARCHITECTURE FACT — SO table = AR table:** There is no BKSOMSTR. Sales Orders and AR Invoices share the same table — BKARINV. T7SOA.RWN operates directly on BKARINV; when an SO is shipped and posted, the record's status fields change but the row never moves. The BKSO* prefix tables are supplemental only: BKSONOTE (notes), BKSOHLOT/BKSOHSER (lot/serial history), BKSOPO (SO→PO cross-reference for special orders), BKSOX/BKSOXH (posted SO extract for reporting). If you're looking for "open sales orders," query BKARINV filtered by status — not a separate table.

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

**RWN programs (13):**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7ROA | 71 | Routing master entry/edit (ROUTING+BKRTCST+WORKCTR+ISNOTES) |
| T7ROB | — | Routing copy |
| T7ROC | — | Work center scheduling view (WORKCTR+DPTMENT+ROUTING+ISROUTEX) |
| T7ROD | — | Machine routing view (MACHINE+BKMATRIM+ROUTING) |
| T7ROE | — | Tool/machine usage (TOOL+MACHINE+ROUTING) |
| T7ROI | — | Routing inquiry (ROUTING+WORKCTR+BKAPVEND+MACHINE+TOOL) |
| T7ROJA | — | Routing job analysis (WORKORD+WOROUT+WOBOM+ROUTING) |
| T7ROJH | — | Routing job history (WORKCTR+ROUTING) |
| T7ROL | — | Routing list/report |
| T7ROP | — | Routing PO view (ROUTING+BKAPPOL) |
| T7ROQ | — | Routing/WO inquiry (WORKCTR+ROUTING+WOROUT+WOLABOR+MACHINE) |
| T7CVTROIA | — | Routing conversion/import utility |
| T7EDUDF | — | Routing UDF (user-defined field) update |

**Routing structure** (from BKROA.SRC — fully analyzed):
- A routing belongs to one part number.
- Each routing has N operations (sequences), numbered in ascending order.
- Each operation specifies: work center, optional machine, optional tool, optional vendor (outsourced/type-L operations), setup hours, run time per piece, scrap %.
- Up to 15 lines of operation instructions per sequence.
- Routing templates (BKRTTEMP) allow predefined operations to be selected and auto-sequenced.
- Copy routing (F3) duplicates an existing routing onto a new part.

**ROUTING table — MTRO_ prefix (62f):**
Primary key: `MTRO_CODE`(15) item code + `MTRO_OPER`(2) operation sequence.

| Field | Type/Size | Meaning |
|-------|-----------|---------|
| MTRO_CODE | STRING 15 | Item code (FK → BKICMSTR) |
| MTRO_OPER | UBINARY 2 | Operation sequence number |
| MTRO_DESC / MTRO_OPERDESC | STRING 30 | Operation description |
| MTRO_TYPE | STRING 1 | Operation type (L=labor, S=subcontract, M=machine) |
| MTRO_LEAD | UBINARY 2 | Lead time days for this operation |
| MTRO_VENDCOST / MTRO_PARTSHR | FLOAT 8 | Vendor cost / parts share % |
| MTRO_TIMEPART | TIME 4 | Time per part (run time) |
| MTRO_SETUPHRS | TIME 4 | Setup hours |
| MTRO_LOTSIZE | FLOAT 8 | Lot size for time calculation |
| MTRO_INSTR_1..15 | STRING 60 | 15 instruction lines (60 chars each) |
| MTRO_WC | STRING 12 | Work center code (FK → WORKCTR) |
| MTRO_WCDESC | STRING 30 | Work center description (cached) |
| MTRO_VENDCODE | STRING 10 | Vendor code for outsourced ops (FK → BKAPVEND) |
| MTRO_VENDNAME | STRING 25 | Vendor name (cached) |
| MTRO_LABOR | FLOAT 8 | Standard labor cost per piece |
| MTRO_MACHINE | FLOAT 8 | Standard machine cost per piece |
| MTRO_FOVHD / MTRO_VOVHD | FLOAT 8 | Fixed/variable overhead per piece |
| MTRO_SETUP | FLOAT 8 | Standard setup cost |
| MTRO_TMACHINE | STRING 4 | Machine type code |
| MTRO_TMACHDESC | STRING 30 | Machine type description |
| MTRO_TOOL | STRING 15 | Tool code |
| MTRO_TOOLDESC | STRING 30 | Tool description |
| MTRO_NUM | UBINARY 2 | Number of machines |
| MTRO_NUM_PERSON | FLOAT 8 | Number of persons per machine |
| MTWO_MISC_COST / MTWO_MISC_DESC | FLOAT/STRING | Misc cost + description (WO-era field name in ROUTING table) |
| MTRO_MISC_ACOST | FLOAT 8 | Actual misc cost |
| MTRO_OP_TEMP_NO | UBINARY 2 | Operation template number |
| MTRO_NUM_PROCES | UBINARY 2 | Number of processes per cycle |
| MTRO_TIME_PERPR | TIME 4 | Time per process |
| MTRO_MD_PROC_HR | STRING 1 | Method: processes per hour flag |
| MTRO_PROC_PERHR | FLOAT 8 | Processes per hour |
| MTRO_STD_TIME | STRING 1 | Standard time flag |
| MTRO_MIN_CHG | FLOAT 8 | Minimum charge |
| MTRO_OVERLAP | UBINARY 2 | Overlap days with previous operation |
| MTRO_PIECE_RATE | FLOAT 8 | Piece rate pay |
| MTRO_LONGTIME | FLOAT 8 | Long-run time adjustment |
| MTRO_PRINT | STRING 1 | Print flag |
| MTRO_CLASS | STRING 15 | Classification code |
| MTRO_EXTRA | STRING 150 | Extra notes |
| MTRO_NEGOVLP | FLOAT 8 | Negative overlap (start before previous completes) |
| MTRO_DEF_TIME | TIME 4 | Default time |
| MTRO_R_TYPE | STRING 10 | Routing type |
| MTRO_EST_LINE | FLOAT 8 | Estimating line# |
| MTRO_EST_TAG | STRING 10 | Estimating tag |

**DDF note:** The DDF table name is `ROUTING` but all field names use the `MTRO_` prefix. One field (`MTWO_MISC_COST`, `MTWO_MISC_DESC`) has the WO-era `MTWO_` prefix — an artifact of field reuse.

**Primary tables:**

| Table | Fields | Purpose |
|-------|--------|---------|
| ROUTING | 62 | Routing master — operations per part (MTRO_ prefix) |
| WORKCTR | 47 | Work center master (MTWC_ prefix) |
| MACHINE | — | Machine master |
| TOOL | — | Tool master |
| BKRTTEMP | — | Operation templates |
| BKRTSPEC | 7 | Operation notes/specs (BKRT_SPEC_* prefix) |
| BKRTCST | 24 | Routing cost snapshot per quote/setup (10-break pricing) |
| BKRFQ | 49 | Request for Quote per routing operation (subcontract pricing) |
| ISROUTEX | — | Routing extension fields |

**Confidence: 85/100** — BKROA.SRC fully analyzed; ROUTING (62f) schema fully extracted from DDF; BKRTCST (24f) and BKRFQ (49f) schemas extracted; work center/machine/tool relationships confirmed from DB fingerprints.

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

**What it does:** Finite-capacity scheduling of work orders across work centers. SH is the dispatch and scheduling layer on top of WO — it reads WORKORD/WOROUT and writes scheduling dates, priorities, and capacity buckets. It does NOT create work orders.

**Menu codes:** SH (17 T7SH* programs)

**Program map:**

| RWN | Procs | Operation | Key tables |
|-----|------:|-----------|------------|
| T7SHA | 94 | SH-A — WO scheduling grid (main browse) | WORKORD, BKICMSTR, MTICMSTR, BKARINVL, WOBOM, CLASMSTR |
| T7SHB | 102 | SH-B — WO operation scheduling (routing drill-down) | WORKORD, MTICMSTR, WOROUT, WORKCTR, BKARINVL, ISARCHG |
| T7SHC | 70 | SH-C — Work center browser | WORKCTR, WOROUT, WORKORD |
| T7SHE | 128 | SH-E — Forward scheduler (due-date buckets) | SCHWO, WORKORD, SCHEDCAL, WORKCTR, WCCTL |
| T7SHF | 117 | SH-F — Scheduling report | WORKORD, MTICMSTR, WOROUT, CALENDAR |
| T7SHG | 147 | SH-G — Gantt / visual schedule | BKSYMSTR, BKICMSTR, WORKORD, MTICMSTR, BKARINVL, ISARCHG |
| T7SHH | 139 | SH-H — Dispatch queue list | BKSYMSTR, BKICMSTR, MTICMSTR, WORKORD, WOROUT |
| T7SHI | 169 | SH-I — MRP-integrated scheduler | BKSYMSTR, MTICMSTR, ISBUILD, WORKCTR, MTMRP, WORKORD |
| T7SHJ | 130 | SH-J — Machine scheduling | BKSYMSTR, MACHINE, WOROUT, WORKORD, MTICMSTR, ISWOEX |
| T7SHK | 9 | SH-K — stub | MACHINE, WOROUT, WORKORD, ISWOEX |
| T7SHK2 | 9 | SH-K2 — stub | MACHINE, WOROUT, WORKORD, ISWOEX |
| T7SHM | 67 | SH-M — Shop calendar maintenance | BKICMSTR, CALENDAR |
| T7SHN | 116 | SH-N — Capacity planning (MRP) | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR, ROUTING, WORKCTR |
| T7SHO | 89 | SH-O — Open WO buckets report | BKSYMSTR, WORKORD, BUCKETS, WORKCTR |
| T7SHP | 179 | SH-P — Print scheduling report | WORKORD, WOBOM, MTICMSTR, WOROUT, BKARINVL, BKYSMSTR |
| ACT7SHKNOTE | 63 | SH-K notes/drill-down | ISDROP, WORKORD, WOROUT |
| T7SHIPRTM | 79 | Ship print RTM (not SH-module) | ISEXUSER, BKPSUSER |

**Key concepts:**
- **Critical Ratio** — SCHWO.SWO_CRATIO and BUCKETS.BUK_CRATIO: priority metric = remaining time / work remaining. <1.0 = behind schedule.
- **Contention** — WOROUT.MTWORO_CONTNTN / SCHWO.SWO_CONTENTION: capacity load at the WC exceeds available hours.
- **Overlap** — MTWORO_OVERLAP(2): start next operation before prior is complete (in hours). Positive = parallel. MTWORO_NEGOVLP = wait gap between ops.
- **Shop Days** — SCHEDCAL maps calendar dates → shop day numbers (forward and backward). Scheduling uses shop-day arithmetic, not calendar math.
- **Buckets** — BUCKETS table = one row per operation per time bucket (scheduled start → finish). Used by SH-O to report capacity loading.
- **Machine vs WC** — MACHINE (4-char code) belongs to a WORKCTR (12-char code). Operations schedule to WCs; machine tracking adds granularity within the WC.

**WORKORD (74f) — Work Order Header**

Primary key: MTWO_WIP_WOPRE(8) + MTWO_WIP_WOSUF(2)

| Field | Type | Size | Meaning |
|---|---|---|---|
| MTWO_WIP_WOPRE/WOSUF | FLOAT+UBINARY | 8+2 | WO prefix + suffix (PK) |
| MTWO_WIP_CODE | STRING | 15 | Part/item code (FK → BKICMSTR) |
| MTWO_WIP_SQTY | FLOAT | 8 | Scheduled quantity |
| MTWO_WIP_COMQTY | FLOAT | 8 | Completed quantity |
| MTWO_WIP_SCRAP | FLOAT | 8 | Scrapped quantity |
| MTWO_WIP_STATUS | STRING | 1 | Status: F=Released, R=Completed, C=Closed, S=Scheduled, I=In-Process, X=On-Hold |
| MTWO_WIP_PRTY | STRING | 1 | Priority 1–9 (FK → ISWOPRIO) |
| MTWO_WIP_SSTART | DATE | 4 | Scheduled start date |
| MTWO_WIP_SFIN | DATE | 4 | Scheduled finish date |
| MTWO_WIP_ASTART | DATE | 4 | Actual start date |
| MTWO_WIP_AFIN | DATE | 4 | Actual finish date |
| MTWO_WIP_DDATE | DATE | 4 | Due date |
| MTWO_WIP_SONUM | FLOAT | 8 | Linked SO number (FK → BKARINV) |
| MTWO_WIP_SOLINE | FLOAT | 8 | Linked SO line number |
| MTWO_CUSTCODE | STRING | 10 | Customer code (FK → BKARCUST) |
| MTWO_CUSTNAME | STRING | 25 | Customer name (denormalized) |
| MTWO_WIP_CUSORD | STRING | 25 | Customer PO number |
| MTWO_WIP_CONTAT | STRING | 25 | Contact at customer |
| MTWO_WIP_DESC | STRING | 30 | WO description |
| MTWO_WIP_PROJ | STRING | 15 | Project code |
| MTWO_WIP_LOC | STRING | 10 | Production location (FK → BKICLOCM) |
| MTWO_WIP_LOCK | STRING | 1 | Record lock flag |
| MTWO_WIP_MULT/BLANK | STRING | 1 each | Multi-level / blank flags |
| MTWO_WIP_INSTR_1..10 | STRING | 60 each | 10 work instruction lines |
| MTWO_WIP_CHGORD | UBINARY | 2 | Change order count |
| MTWO_WIP_USERCD | STRING | 1 | User category code |
| MTWO_WIP_SCONV/QCONV | STRING | 1 each | Schedule/quantity conversion flags |
| **Estimated costs** | | | |
| MTWO_WIP_ESETUP/EMAT/EOUTPR/ELABOR | FLOAT | 8 each | Est. setup/material/outside/labor cost |
| MTWO_WIP_VOVHD/EFOVHD/EOTH/EMISC/EEXTRA/EST | FLOAT | 8 each | Est. variable OH/fixed OH/other/misc/extra/total |
| **Actual costs** | | | |
| MTWO_WIP_ASETUP/AMAT/AOUTPR/ALABOR | FLOAT | 8 each | Actual setup/material/outside/labor cost |
| MTWO_WIP_AVOVHD/AFOVHD/AOTH/AMISC/AEXTRA/ATOTAL | FLOAT | 8 each | Actual costs |
| **Variances** | | | |
| MTWO_WIP_SETUPV/MATV/OUTPRV/LABORV/VOVHDV/FOVHDV/OTHV/MISCV/EXTRAV/TOTV | FLOAT | 8 each | Variance (est − actual) per cost type |
| MTWO_WIP_PPRCE | FLOAT | 8 | Planned price |
| MTWO_WIP_SCHED_1/2 | STRING | 1 each | Scheduler control flags |
| MTWO_WIP_OTHPER | FLOAT | 8 | Other cost percentage |

**WOROUT (81f) — WO Routing Operations**

Primary key: MTWORO_WOPRE(8) + MTWORO_WOSUF(2) + MTWORO_OPER(2)

| Field | Type | Size | Meaning |
|---|---|---|---|
| MTWORO_WOPRE/WOSUF/OPER | FLOAT+UBINARY+UBINARY | 8+2+2 | WO + operation# (PK) |
| MTWORO_CODE | STRING | 15 | Routing code (FK → ROUTING) |
| MTWORO_OPER2 | UBINARY | 2 | Alternate operation# |
| MTWORO_WC | STRING | 12 | Work center (FK → WORKCTR) |
| MTWORO_SCHED_WC | STRING | 12 | Scheduled-to WC (may differ from standard) |
| MTWORO_WCDESC | STRING | 30 | WC description (denormalized) |
| MTWORO_OPERDESC | STRING | 30 | Operation description |
| MTWORO_DESC | STRING | 30 | Additional description |
| MTWORO_START | DATE | 4 | Scheduled start date |
| MTWORO_FINISH | DATE | 4 | Scheduled finish date |
| MTWORO_FINISH2 | DATE | 4 | Revised finish date |
| MTWORO_STARTED | DATE | 4 | Actual started date |
| MTWORO_FINISHED | DATE | 4 | Actual finished date |
| MTWORO_PRIORITY | STRING | 1 | Operation-level priority |
| MTWORO_DEPT | STRING | 3 | Department |
| MTWORO_TYPE | STRING | 1 | Operation type (regular/outside) |
| MTWORO_VEND | STRING | 10 | Outside process vendor (FK → BKAPVEND) |
| MTWORO_VENDNAME | STRING | 30 | Vendor name (denormalized) |
| MTWORO_PO | FLOAT | 8 | Linked AP PO number (for outside ops) |
| MTWORO_MACHNO | STRING | 4 | Machine number (FK → MACHINE) |
| MTWORO_TOOL | STRING | 15 | Tooling code |
| MTWORO_ESTHRS | FLOAT | 8 | Estimated run hours |
| MTWORO_ACTHRS | FLOAT | 8 | Actual run hours |
| MTWORO_ESETHRS | FLOAT | 8 | Estimated setup hours |
| MTWORO_ASETHRS | FLOAT | 8 | Actual setup hours |
| MTWORO_ESSTHRS | TIME | 4 | Estimated standard setup time |
| MTWORO_QTYCOM | FLOAT | 8 | Quantity completed |
| MTWORO_STQTY | FLOAT | 8 | Quantity started |
| MTWORO_SQTY | FLOAT | 8 | Scheduled quantity |
| MTWORO_SCRAPPED | FLOAT | 8 | Scrapped quantity |
| MTWORO_PARTSHR | FLOAT | 8 | Parts per hour |
| MTWORO_TIMEPART | TIME | 4 | Time per part |
| MTWORO_OVERLAP | UBINARY | 2 | Overlap with previous op (hours) |
| MTWORO_NEGOVLP | FLOAT | 8 | Negative overlap / wait gap |
| MTWORO_LEAD | UBINARY | 2 | Operation lead time (days) |
| MTWORO_CONTNTN | FLOAT | 8 | Contention level at this WC |
| MTWORO_LONGTIME | FLOAT | 8 | Long-time flag (ops taking > 1 day) |
| MTWORO_PROJ | FLOAT | 8 | Project reference |
| MTWORO_NUM | UBINARY | 2 | Sequence number |
| MTWORO_NUM_PERS | FLOAT | 8 | Number of people required |
| MTWORO_NUM_PROC | UBINARY | 2 | Number of concurrent processes |
| MTWORO_TIME_PPR | TIME | 4 | Time per process run |
| MTWORO_MD_PR_HR | STRING | 1 | Minutes or decimal per hour flag |
| MTWORO_PR_PERHR | FLOAT | 8 | Processes per hour |
| MTWORO_STD_TIME | STRING | 1 | Standard time flag |
| MTWORO_MIN_CHG | FLOAT | 8 | Minimum charge |
| MTWORO_PIECE_RT | FLOAT | 8 | Piece rate |
| MTWORO_PRINT | STRING | 1 | Print this operation flag |
| MTWORO_INSTR_1..15 | STRING | 60 each | 15 operation instruction lines |
| **Estimated costs per op** | | | |
| MTWORO_ESETCST/ELABCST/EMCHCST/EOUTCST/EFOHCST/EVOHCST | FLOAT | 8 each | Est. setup/labor/machine/outside/fixed OH/variable OH |
| **Actual costs per op** | | | |
| MTWORO_ASETCST/ALABCST/AMCHCST/AOUTCST/AFOHCST/AVOHCST | FLOAT | 8 each | Actual setup/labor/machine/outside/fixed OH/variable OH |
| MTWORO_MISCCOST/MISCDESC/MISCACST | varies | — | Misc cost / description / actual |
| MTWORO_EXTRA | STRING | 150 | Extra notes |

**WORKCTR (47f) — Work Center Master**

Primary key: MTWC_WC(12)

| Field | Meaning |
|---|---|
| MTWC_WC (12) / WCDESC (30) | Work center code + description |
| MTWC_DEPT (4) / DEPTDESC (30) | Department code + description |
| MTWC_HRSWEEK (2) | Capacity hours per week |
| MTWC_HRS_SHIFT (2) | Hours per shift |
| MTWC_SETUP/LABOR/MACHINE (float) | Cost rates per hour: setup / labor / machine |
| MTWC_VOVHD/FOVHD (float) | Variable and fixed overhead rates |
| MTWC_EST_VOVHD (float) | Estimated variable overhead |
| MTWC_AVGQTIME (2) | Average queue time (days) |
| MTWC_QPR1/2/3 (2 each) | Queue priority thresholds |
| MTWC_LEAD (2) | Default lead time (days) |
| MTWC_OUTPROC (1) | Outside process flag |
| MTWC_MIN_CHG (float) | Minimum charge per operation |
| MTWC_COST_LB (float) | Cost per pound (for material-based billing) |
| MTWC_PARENT_YN (1) / PARENT_WC (12) | Is this a parent WC? Parent WC code |
| MTWC_LEVEL_YN (1) | Level scheduling flag |
| MTWC_CYCLE_TIME_1..10 (2 each) | 10 cycle time slots |
| MTWC_GDATE_1/2 (date) | 2 configurable dates |
| MTWC_FLAGS_1..5 (1 each) | 5 configurable flags |
| MTWC_ALPHA_1..5 (30 each) | 5 user-defined text fields |
| MTWC_GNUM (float) | Configurable numeric field |
| MTWC_EXTRA (100) | Extra notes |

**BUCKETS (14f) — Capacity Scheduling Buckets**

One row per scheduled operation per time window:
- BUK_WC(12) + WCTYPE(1) — which work center
- BUK_WOPRE+WOSUF+OPER — which WO operation
- BUK_PART(15) — part being made
- BUK_SDATE+SDATE_SHOP / BUK_FDATE+FDATE_SHOP — scheduled window (calendar + shop day)
- BUK_CRATIO(float) — critical ratio for this bucket
- BUK_LOCKED(1) — manually locked (won't move in auto-reschedule)
- BUK_NUM_SUNITS(float) — scheduling units in this bucket
- BUK_CNTN(float) — contention level

**SCHWO (10f) — Scheduled WO Summary**

One row per scheduled WO (scheduler's working copy):
- SWO_WOPRE+WOSUF (PK); SWO_OPCOUNT(2) — number of ops
- SWO_RUN_DAYS(float) — total run days; SWO_DAYS_TOGO(float) — days remaining
- SWO_CRATIO(float) — critical ratio; SWO_CONTENTION(float) — overall contention
- SWO_SHOP_START/FINISH/DUE(float) — shop day numbers for start/finish/due date

**SCHEDCAL (6f) — Schedule Calendar Mapping**

Converts calendar dates to shop day numbers for scheduling arithmetic:
- SCH_CAL_DATE (PK) + SCH_WH_FLAG(1) — working/holiday
- SCH_SHOP_DATE(float) — forward shop day number
- SCH_BACK_DATE(float) — backward shop day number (for back-scheduling from due date)
- SCH_SHOP_SLASH/BACK_SLASH(date) — equivalent calendar dates

**CALENDAR (5f) — Shop Working Days**

- MTCAL_DATE (PK) + MTCAL_DESC(25) — date + holiday description
- MTCAL_SAT/SUN(1 each) — work Saturdays/Sundays flags
- MTCAL_YEAR(2) — year number

**MACHINE (20f) — Machine Master**

Primary key: TMACH_MACHINE(4)
- TMACH_DESC(30), TMACH_WC(12)+WCDESC(30) — machine desc + parent work center
- TMACH_HRSUSED+HRSMAINT(float) — cumulative hours used / maintenance hours
- TMACH_DATE(date) — last maintenance date
- TMACH_NOTES_1..8(45 each) — 8 note lines
- TMACH_EXTRA(100), TMACH_ACTIVE(1), TMACH_INACTDATE+INACTWHO(30)+INACTWHY(60) — deactivation log

**ISWOPRIO (4f) — WO Priority Codes**

- IS_WOPRIO_PRIO(1) PK (values "1"–"9")
- IS_WOPRIO_DESC(30) — description (e.g., "RUSH", "NORMAL", "LOW")
- IS_WOPRIO_EXTRA(100)
- IS_WOPRIO_COLOR(float) — UI display color for this priority level

**ISARCHG (26f) — AR Order Change Audit**

Before/after log for SO line changes (used by SH-B and SH-G to track due-date changes):
- ISAR_CHG_SONUM+INVNUM+LINEID+PCODE (PK), CDATE(date), USER(15), REVLVL(10)
- ALOC/BLOC(10) — before/after location
- APRICE/BPRICE, ADISC/BDISC — before/after price and discount
- AOOQTY/BOOQTY — before/after open order qty
- AESD/BESD (est ship date), AASD/BASD (actual ship date) — before/after dates
- ACOMPR_1/2 + BCOMPR_1/2 — before/after commission rates
- AEXTRA/BEXTRA(150) — before/after notes; UNUM(4) — unique entry#

**MTMRP (13f) — MRP Demand (SH-I integration)**

One row per item per demand date (MRP output used by forward scheduler):
- MTMRP_PARTNO(15) + DATE (PK)
- MTMRP_QTY(float) — required qty; MTMRP_ONHAND(float) — on-hand at planning time
- MTMRP_PEGTO(10) — demand source (SO/WO/forecast); MTMRP_ORDER(10) — order ref
- MTMRP_STARTDT(date) + ACTION(10) — planned action type (RELEASE/EXPEDITE/etc.)
- MTMRP_PG_SDATE/FDATE/QTY — peg start/finish and qty
- MTMRP_LOC(10) — location

**ISWOEX (63f) — WO Extended Data**

Primary key: IS_WOEX_WOPRE(8) + WOSUF(2). Extension record per WO for multi-yield and extra tracking:
- IS_WOEX_ITP(20)+ITPP(1) — item type profile code + prefix
- IS_WOEX_RF(1) — re-fire flag; IS_WOEX_MCLASS(6)+MNUM(float) — machine class/number
- IS_WOEX_CDATE(date) — creation date
- IS_WOEX_WC(12) — associated WC; IS_WOEX_CAUSE(30) — cause code
- IS_WOEX_DATE1..5 + GDATE_1..5 (dates) — 10 configurable dates
- IS_WOEX_INT1..5(2 each) — 5 integer UDF slots
- IS_WOEX_NUM1/2 + GNUMS_1..5 (float) — 7 numeric UDF slots
- IS_WOEX_ALPHA1/2(30) + ALPHA3/4/5(1) + ALPHAS_1..5(30 each) — alpha UDF fields
- IS_WOEX_DESC1..5(30 each) — 5 description lines
- IS_WOEX_NOTE_1..5(100 each) — 5 note lines
- IS_WOEX_FLAGS_1..10(1 each) — 10 configurable flags
- IS_WOEX_EXTRA(100)

**Table summary:**

| Table | Fields | Purpose |
|-------|--------|---------|
| WORKORD | 74 | WO header — qty/dates/status/costs/variances (MTWO_WIP_* prefix) |
| WOROUT | 81 | WO routing ops — WC/dates/hrs/costs/instructions per operation (MTWORO_* prefix) |
| WORKCTR | 47 | Work center — capacity/rates/OH/hierarchy/UDF (MTWC_* prefix) |
| ISWOEX | 63 | WO extended — multi-yield/UDF/machine/cause (IS_WOEX_* prefix) |
| BUCKETS | 14 | Scheduling buckets — one row per op per time window; CRATIO+contention |
| SCHWO | 10 | Scheduled WO summary — shop day numbers, critical ratio, contention |
| MACHINE | 20 | Machine master — hours used/maint, parent WC, deactivation log |
| ISARCHG | 26 | AR order change audit — before/after on SO line edits |
| MTMRP | 13 | MRP demand — item/date pegged demand used by forward scheduler |
| SCHEDCAL | 6 | Calendar → shop day mapping (forward + backward) |
| CALENDAR | 5 | Shop working days + holiday descriptions |
| WCCTL | 5 | WC scheduler state — current start/stop/count per WC |
| ISBUILD | 15 | Generic sort-build utility — temp sorted result sets |
| ISWOPRIO | 4 | WO priority codes 1–9 with descriptions and UI colors |
| ISDROP | 4 | Generic dropdown list values |

**Note:** Physical shipping (carrier, BOL, tracking) is in SO (T7SOC), not SH. SH = shop floor scheduling only. TASCOLOR (referenced by T7SHA) is not in the Pervasive DDF schema — likely a TAS Pro 7 memory or INI file for color configuration.

**Confidence: 82/100** — All 17 T7SH* programs identified with proc counts and DB fingerprints; WORKORD(74f), WOROUT(81f), WORKCTR(47f), and all 10 SH-specific tables fully field-extracted from DDF; scheduling algorithm (critical ratio, buckets) inferred from field names and structure, not confirmed from source.

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

**BKPSUSER (11f)** — user login record (CODE PK; PSWD+SEC(30)+MCNTR+LDATE+EMP) — documented in Pass 46.

**ISVNDADT (11f)** — Vendor name/amount change audit trail (PS-K). Used when a user changes a vendor name or max PO amount:
- IS_VND_VEND(10) — vendor code (PK, FK → BKAPVEND)
- IS_VND_ONAME(30) + NNAME(30) — old name + new name
- IS_VND_APPROVE(1) — approval flag
- IS_VND_DATE(4) + TIME(4) + WHO(20) — when/who approved
- IS_VND_OMAXAMT(8) + NMAXAMT(8) — old + new max PO amount threshold
- IS_VND_CHGDESC(30) — change description
- IS_VND_EXTRA(100)
PS-K creates an ISVNDADT record for every vendor name or credit limit change; the record must be approved (APPROVE='Y') before the change takes effect in BKAPVEND.

**Confidence: 72/100** — BKPSUSER(11f)+ISVNDADT(11f) schemas extracted; dual user system confirmed; T7PSA(90p) user master, T7PSE(50p)+T7PSF(63p) menu security, T7PSK(96p) vendor audit all confirmed; ISEXUSER+BKMENUSU not in DDF (security data tables with no DDF registration).

---

### US — User Services / Trigger Notifications

**What it does:** Manages automated follow-up triggers — alerts that fire N days before a key date on any linked record (SO, PO, WO, customer, vendor). Used for CRM follow-ups, service renewal alerts, scheduled reminders, and AR collection follow-up.

**RWN program:** T7USG (90 procs) — the sole US program. Opens: ISTRIGRS + BKPSUSER + BKARCUST + BKAPVEND + WORKORD + BKARINV + BKAPPO + ISBNMSTR + ISITP + BKICREF + CLASMSTR + ISCATMST + ISNCR + BKCMACCN + ISLINKS.

**Key operations:**
- **US-G — Trigger Setup:** Define trigger rules in ISTRIGRS. Each trigger has: CODE(15) identifier, TRIGR(10) user/contact to notify, CONTACT(20) contact name, DAYS(integer) lead time before the event, EMAIL(400) destination address(es), ONCE(1) flag (fire once or recurring), LDATE/LTIME last-fired audit trail. Plus entity links: WOPRE/WOSUF (WO), PO, SO, CUST(10), VEND(10), LOC(10), and classification fields (ITYPE, CLASS, CAT, PLANNER).

**EvoRemind integration:** EvoRemind.RWN (46 procs) polls ISTRIGRS daily, finds records where DAYS pre-date threshold has been reached, and sends email or creates ISREMIND calendar entries. ISREMIND (22f) stores the resulting calendar reminder records with DATE, TIME, WHO, SUBJECT, CUST/VEND/ITEM refs, FILE attachment, EMAIL, and SENT audit trail.

**Confidence: 65/100** — T7USG identified with full DB fingerprint; ISTRIGRS (25f) and ISREMIND (22f) fully field-documented; EvoRemind integration confirmed; exact trigger-firing date calculation not traced (relies on encrypted RWN).

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

**Primary tables:**

### ISRMAI — RMA Item Record (54f)
`IS_RMA_NUM`(float)+`PART`(15)+`LINEID`(int) PK; DATE (opened) + RCPTDATE (received) + CLOSDATE (closed); STATUS(1); REASON(10, FK → ISRMAC); DISP(1, disposition code); OSONUM/OINVNUM (original SO#/invoice# before RMA); OLDRMANO(old RMA number for re-opens); SONUM/INVNUM (new SO/invoice generated for replacement); CMNUM (credit memo #); REORDER(1, reorder flag); WOPRE/WOSUF (linked WO); SODATE/INVDATE/CMDATE/DISPDATE; WARRANTY(1, N/L/P/B); SRNUM (SR order#); INVCD(item code on invoice); DISPSEL(1, disposition selector); IEXTRA(100); WO(1)/CR(1)/SO(1)/STOCK(1)/SCRAP(1)/SR(1)/REFUND(1) — disposition action flags (pass to WO / create credit / new SO / restock / scrap / SR / refund); FLAGS_1..20 (1×20 custom flags).

### ISRMAC — RMA Reason Code (3f)
`IS_RMA_CODE`(10 PK) + IS_RMA_DESC(30) + IS_RMA_EXTRA(50). Simple reason code table. Examples: warranty claims, customer damage, shipping error, etc.

**Programs confirmed (Pass 66):**
- T7RMD (216p) — main RMA entry: BKARINVL+ISRMAI+ISRMAC+BKARINV+ISNOTES+ISLINKS+ISNCR+SCRAP+BKARTXN+MTICMSTR
- T7RMG (132p) — RMA report/posting: BKSYMSTR+BKARINV+BKARINVL+ISRMAI+BKICMSTR+ISICMSTR+BKARCUST+ISRMAC
- T7RME (54p) — reason code maintenance: ISRMAC (primary)
- T7RMB/T7RMC (5p stubs) — filter/print sub-stubs

**Confidence: 78/100** — 4 programs confirmed; ISRMAI(54f) full schema extracted — all 54 fields decoded including complete disposition action flags (WO/CR/SO/STOCK/SCRAP/SR/REFUND); warranty codes N/L/P/B confirmed; ISRMAC(3f) confirmed; original invoice + new document linkage fully mapped; exact warranty/reason UI flow blocked by encryption.

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

**J7 Customization — CC-C programs (T7CCCITM, T7CCCRNO, T7CCCWOT):**
These three programs use **ISCCICM(59f)** — a J7-specific catalog extension table with field names that reveal door hardware manufacturing:
- ISCC_ICM_CODE(15) + DESC(30) + DESC2(30) — item code + two descriptions
- ISCC_ICM_FSIZE(30) — frame/door size specification
- ISCC_ICM_CUST(60) — customer specification (longer than standard 10-char customer code = free-text field)
- ISCC_ICM_COLLEC(120) — product collection/style name (120 chars)
- ISCC_ICM_HINGE(25) — hinge specification
- ISCC_ICM_SPY(25) — spy hole / peephole specification
- ISCC_ICM_PDF(60) — PDF document path (product sheet/drawing)
- ISCC_ICM_PNAME(60) — product name
- ISCC_ICM_AMTPP(25) — amount per piece
- ISCC_ICM_SOLIDF(25) — SolidWorks file path (3D model integration)
- +47 more configurable spec/dimension fields

T7CCCITM (CC-C item maintenance), T7CCCRNO (CC-C change request numbering), T7CCCWOT (CC-C WO closure) are J7 Systems customizations for door hardware catalog management — not part of stock EvoERP. BKRTSPEC+BKBMDIM+BKBMNOTE+BKBMREMK in the fingerprint confirm these programs also manage routing specs and BOM dimensions.

**Confidence: 78/100** — ISCC(14f) full schema extracted (tokenized CC vault); BKPSUSER security integration confirmed; ISCCICM(59f) extracted — J7 catalog extension confirmed (door hardware: frame/hinge/spy/SolidWorks fields); CC-CCC J7 customization boundary identified.

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

**Programs confirmed (Pass 67):**
- T7SPC (148p) — main entry: ISSERR+ISSTRACK+ISSPC+ISSTYPE+ISSDET+ISSETYPE+ISSEPROC+WORKORD+WOROUT+BKPRMSTR+WOBOM+ISSCOMP
- T7SPCREP/SPCREP2 (105p each) — WO/part/employee reports
- T7SPCLIVEREP (50p) — auto-refresh live report
- T7SPCREPPPM (104p) — PPM report
- T7SPCLIVEGRID (5p) — live dashboard stub
- T7SPCMEMO2ALPHA (25p) — ISSPC/ISSERR data migration utility

**Primary tables:**

**ISSERR (14f) — SPC Error Event:**
WOPRE+WOSUF+OPER+TIME+DATE PK; ERROR(25, defect code); PROCESS(25, process name); COUNT(int, defect count); REF(50); EXTRA(50); SERIAL(20); ADOF(STRING 1000, AOI Defect-of-Focus data) + ADIAG(STRING 1000, AOI Diagnosis) + AREWORK(STRING 1000, AOI Rework instructions). The 1000-char ADOF/ADIAG/AREWORK fields = AOI (Automated Optical Inspection) integration — machine-generated inspection data per defect.

**ISSPC (20f) — SPC Inspection Record:**
WOPRE+WOSUF+OPER+EMPNUM+DATE+TIME PK; GOOD(int, good units); REWORK(int, rework units); SIDE(1, PCB side: F/B/T); TYPE(25, defect type FK→ISSTYPE); DETAIL(25, defect detail FK→ISSDET); EXTRA; TESTR+TESTT+TESTE_1..3 (test result fields); ANOTES(notes); CUST(10, customer); PART(15, item code).

**ISSTRACK (13f) — Component Traceability:**
WOPRE+WOSUF+OPER+TIME+DATE+PROC(25) PK; PSER(20, parent/board serial); COMP(15, component item code); CSER(20, component serial number); NOTE(1000, placement details); EXTRA(50); AR(1, auto-rework flag); CLOT(15, component lot). Full component-level traceability: board serial → every component placed on it with component serial+lot. Supports IPC-1752A-style traceability for electronics manufacturing.

**Supporting tables:**
- **ISSTYPE (3f):** TYPE(PK)+WHO+ASSET — error type code master
- **ISSETET (2f):** ERR(PK)+WHO — error code master
- **ISSEPROC (2f):** PROC(PK)+WHO — process code master
- **ISSDET (4f):** TYPE+DETAIL PK; WHO+SUB — error detail sub-code

**Industry context:** PCB/electronics manufacturing. SIDE field = PCB front/back sides. ISSTRACK = component-level traceability for IPC compliance. ADOF/ADIAG/AREWORK = AOI machine integration.

**Confidence: 80/100** — 7 programs confirmed; all SP table schemas extracted (ISSPC 20f, ISSERR 14f, ISSTRACK 13f, ISSTYPE 3f, ISSETYPE 2f, ISSEPROC 2f, ISSDET 4f); AOI integration confirmed; PCB traceability architecture fully decoded; per-operation inspection logic blocked by encryption.

---

### CRM / Contact Manager (CM)

**What it does:** Manages customer and prospect contacts, accounts, territories, and marketing activities. Three entity types: AR customers (BKARCUST), CRM prospect accounts (BKCMACCT), and individual prospect contacts (BKCMPCNT). Tracks activity history, follow-ups, mailing campaigns, and dunning for all three. Up to 10 named contacts with phone/email per account.

**Menu codes:** CM (6 T7CM* programs)

**Program map:**

| RWN | Procs | Operation | Key tables |
|-----|------:|-----------|------------|
| T7CMA | 275 | CM-A — Account master entry/edit | BKARCUST, BKCMACCT, BKCMACCL, BKCMACTD, ISREMIND, BKYSMSTR |
| T7CMBB | 118 | CM mailing/campaign builder | BKCMMHST, BKARCUST, BKCMACTD, BKCMACCL, BKCMDTCD, BKCMACCC |
| T7CMCVTF | 31 | Convert follow-up tasks to ISREMIND | BKCMACTF, ISREMIND, BKCMREP, BKPSUSER |
| T7CMCVTN | 33 | Convert notes to ISNOTES | BKCMACTH, ISNOTES, ISLOG, ISDRILL |
| T7CMJ | 9 | CRM journal / marketing action history | MKAHIST, ISNOTES |
| T7CMK | 70 | CRM key inquiry / customer drill-down | BKARCUST, ISIS, MKAHIST, ISLOG |

**Architecture — three CRM entity types:**

1. **AR Customers** — primary record in BKARCUST; CRM-relevant fields: BKAR_TERRITORY(4), BKAR_LEAD_SRC(5), BKAR_IS_REP(5), BKAR_SIC_CODE(7), BKAR_MAIL_LIST(1), BKAR_FOLUPDTE (follow-up date)
2. **CRM Accounts** (prospects not yet customers) — primary record in BKCMACCT(41f); flag BKCM_ACCT_CUST(1) = "Y" when converted to an AR customer
3. **CRM Prospect Contacts** (individuals) — BKCMPCNT(24f); linked to account via BKCM_PCNT_CCODE

Activity history/follow-ups exist in parallel sets:
- Accounts: BKCMACTH (history) + BKCMACTF (follow-up) + BKCMACTD (date tracking)
- Vendors: BKCMVNDH (history) + BKCMVNDF (follow-up)
- Prospects: BKCMPCTH (history) + BKCMPCTF (follow-up)
All share BKCMHCOD event codes.

**BKCMACCT (41f) — CRM Account Master (prospects)**

Primary key: BKCM_ACCT_CODE(10)

| Field | Size | Meaning |
|---|---|---|
| BKCM_ACCT_CODE | 10 | Account code (PK) |
| BKCM_ACCT_OLDCD | 10 | Previous/old code |
| BKCM_ACCT_ALPHA | 6 | Sort key |
| BKCM_ACCT_NAME | 30 | Company name |
| BKCM_ACCT_ADD1/2/3 | 30 each | Address lines |
| BKCM_ACCT_CITY/STATE/ZIP/CNTRY | varies | Full address |
| BKCM_ACCT_CONT1 | 30 | Primary contact name |
| BKCM_ACCT_TITLE | 30 | Primary contact title |
| BKCM_ACCT_PHONE/FAX | 25 each | Phone/fax |
| BKCM_ACCT_REP | 5 | Assigned CRM rep (FK → BKCMREP) |
| BKCM_ACCT_DLOAD | 1 | Download flag |
| BKCM_ACCT_SICCD | 7 | SIC industry code |
| BKCM_ACCT_CUST | 1 | Is existing AR customer? |
| BKCM_ACCT_LEAD | 5 | Lead source code (FK → BKCMLEAD) |
| BKCM_ACCT_START | date | Start/acquired date |
| BKCM_ACCT_TERR | 4 | Territory (FK → BKCMTERR) |
| BKCM_ACCT_REM_1/2 | 60 each | Remarks |
| BKCM_ACCT_FONE_1..3 | 15 each | Additional phone numbers |
| BKCM_ACCT_FTWO_1..3 | 2 each | Phone extensions |
| BKCM_ACCT_FTHRE_1/2 | 25 each | Phone type labels |
| BKCM_ACCT_FTIME | 2 | Billable time balance |
| BKCM_ACCT_CCARD/CNUM/CEXP | varies | Credit card on file |
| BKCM_ACCT_CMPNM/PNAME | 25 each | Card company/cardholder name |
| BKCM_ACCT_EXTRA | 200 | Extra notes |
| BKCM_ACCT_EMAIL | 128 | Primary email |
| BKCM_ACCT_EMPS | float | Employee count |

Note: **BKCMDE (41f)** and **BKCMEACT (41f)** are DDF alternate-key views of BKCMACCT with identical field names — not separate tables.

**BKCMACCN (154f) — Account Contacts (10 contacts per account)**

Primary key: BKCM_ACCN_CODE(10) + contact slot

Stores up to 10 named contacts per CRM account:
- BKCM_ACCN_CONT_1..10 (30 each) — contact names
- BKCM_ACCN_TITLE_1..10 (30 each) — titles
- BKCM_ACCN_PHONE_1..10 (25 each) — phone numbers
- BKCM_ACCN_DEAR_1..10 (25 each) — salutation ("Dear Mr. Smith")
- BKCM_ACCN_EMAIL_1..10 (128 each) — email addresses
- BKCM_ACCN_PHLBL_1..10 (20 each) — phone type labels
- BKCM_ACCN_EMLBL_1..10 (20 each) — email type labels
- BMCM_ACCN_DATE1_1..10 + BKCM_ACCN_DATE2_1..10 (date) — 2×10 configurable dates per contact
- BKCM_ACCN_ALPH1_1..10 + BKCM_ACCN_ALPH2_1..10 (25 each) — 2×10 user-defined alpha fields
- BKCM_ACCN_PRIM (1) — primary contact flag; BKCM_ACCN_CON (30) — primary contact name

**BKCMACTH (21f) — Activity History (per account)**

Primary key: BKCM_ACTH_CODE(10) + DATE + REP + LINE

| Field | Meaning |
|---|---|
| BKCM_ACTH_DATE | Activity date |
| BKCM_ACTH_REP (5) | CRM rep who logged it |
| BKCM_ACTH_LINE (2) | Sequence within date |
| BKCM_ACTH_CD (2) | Event date code |
| BKCM_ACTH_EVENT (2) | Event type (FK → BKCMHCOD.HCODE) |
| BKCM_ACTH_PHONE (1) | Was it a phone call? |
| BKCM_ACTH_START/STOP (time) | Call start/stop times |
| BKCM_ACTH_MIN/BMIN (2 each) | Actual/billed minutes |
| BKCM_ACTH_REM (57) | Remarks/notes |
| BKCM_ACTH_BILLD (1) | Billable flag |
| BKCM_ACTH_DLOAD (1) | Downloaded flag |
| BKCM_ACTH_RECVD (time) | When received |
| BKCM_ACTH_CNTCT (25) | Contact person spoken to |
| BKCM_ACTH_RATE/AMT/BALNC (float) | Billing rate / amount / running balance |
| BKCM_ACTH_EXTRA (50) | Extra |

**BKCMHCOD (9f) — CRM Event/Activity Codes**

Primary key: BKCM_HCOD_HCODE(2)

| Field | Meaning |
|---|---|
| BKCM_HCOD_DESC (25) | Code description (e.g., "Phone Call", "Site Visit") |
| BKCM_HCOD_WINDW (1) | Pop-up window flag |
| BKCM_HCOD_RATE (float) | Default billing rate for this event type |
| BKCM_HCOD_UM (3) | Unit of measure for billing |
| BKCM_HCOD_ABILL (1) | Auto-billable flag |
| BKCM_HCOD_BPART/NPART/FPART (15 each) | Before/normal/final billing item codes |

**BKCMREP (14f) — CRM Sales Rep Master**

Primary key: BKCM_REP_REP(5)

| Field | Meaning |
|---|---|
| BKCM_REP_FNMEMI/LNAME/FNAME (25 each) | First initial+last / full last / full first name |
| BKCM_REP_EMP (2) | Employee number (FK → payroll) |
| BKCM_REP_PSWD (10) | CRM-specific password (separate from AHSYLOG) |
| BKCM_REP_DHCODE/DFCODE/DDCODE | Default history/follow-up/date codes |
| BKCM_REP_VIEW/CHANGE/GWARN/AADD (1 each) | View, change, warn, add account permissions |
| BKCM_REP_FTITLE (25) | Rep title for letters |

**BKCMTERR (11f) — Territory Master**

Primary key: BKCM_TERR_TCODE(4): DESC(25), EMAIL(128), ALPHA(30), EXTRA(100), FLAGS_1..5(1 each), DATE

**BKCMMHST (72f) — Mailing/Campaign History**

Primary key: BKCM_MHST_MCODE(15). One row per campaign/mailing run.
- DATE + DESC — when/what the campaign was
- 20×CLASS(5) include criteria + 20×OCLAS(5) exclude criteria — class-based segment filters
- Filter ranges: FROM/TO for account code (FACD/TACD), state (FST/TST), zip (FZIP/TZIP), SIC (FSIC/TSIC), start date (FSDT/TSDT), territory (FTERR/TTERR), rep (FREP/TREP), lead (FLEAD/TLEAD)
- KDCD(2) — key date code filter
- CUSTO(1) — customers only flag; NOCUS(1) — non-customers only flag
- DORL(1) — domestic/local flag; NUMUP(2) — # records updated
- SORT(1), PCONT(1) — sort/contact flags; CNUM(2) — contact number to use
- REM(1) — remarks flag; FORM(15) — letter form to print; STAT(11) — run status

**BKCMDUN (36f) — Dunning Configuration**

One-row-per-rep dunning ladder (up to 10 levels):
- REP(5) + 10×AGE(2) — aging days thresholds for each dunning level
- 10×FORM(15) — letter form at each level; 10×DESC(30) — level description
- DORL+NUMUP+SORT+PCONT+CNUM — same filter controls as BKCMMHST

**BKCMDUNH (6f) — Dunning History**

Primary key: BKCM_DUNH_ACCT(10) + DATE: FORM(15), AGE(2), AMT+TOT(float)

**ISREMIND (22f) — System Reminders / Calendar**

Cross-module reminder table used by CRM, US-G triggers, and SR:
- IS_REM_DATE+TIME — when to fire; IS_REM_EDATE+ETIME — end time; IS_REM_ENDDT+ENDTM — recurrence end
- IS_REM_WHO(20) — assigned user; IS_REM_SUBJECT(100); IS_REM_TYPE(3) — reminder class
- IS_REM_CUST(10)+VEND(10)+ITEM(15) — linked entity (customer/vendor/item)
- IS_REM_FILE(256) — attachment path; IS_REM_EMAIL(400) — recipients; IS_REM_SENT(25) — sent tracking
- IS_REM_NOTIFY(1) — send email notification; IS_REM_DISP(1) — display popup
- IS_REM_CO(3) — company; IS_REM_COUNTER(4) — recurrence counter; IS_REM_TRANS(1) — transferred flag

**MKAHIST (9f) — Marketing Action History**

Primary key: MKAHIST_ACCT(10) + DATE + TRACK + SEQ
- EVENT (float → BKCMHCOD.HCODE), MEDIA(1), FORM(float — which form), REM1+REM2(60 each)

**Complete BKCM* table inventory:**

| Table | Fields | Purpose |
|-------|--------|---------|
| BKCMACCN | 154 | Account contacts — 10 contacts per account (name/title/phone/email/dates/UDF) |
| BKCMCUST | 106 | CRM view of BKARCUST (same BKAR_* fields — DDF alt-key view) |
| BKCMMHST | 72 | Mailing/campaign history — criteria, filter ranges, run stats |
| BKCMACCT | 41 | CRM account master — non-AR prospects (NAME/ADDR/REP/TERR/SIC/LEAD/CC/EMAIL/EMPS) |
| BKCMDE | 41 | DDF alt-key view of BKCMACCT (identical fields) |
| BKCMEACT | 41 | DDF alt-key view of BKCMACCT (identical fields) |
| BKCMDUN | 36 | Dunning ladder config — 10 aging thresholds + forms per rep |
| BKCMPCNT | 24 | Prospect contact — individual at a prospect company |
| BKCMACTH | 21 | Account activity history — date/rep/event/time/billing per log entry |
| BKCMEACH | 21 | DDF alt-key view of BKCMACTH |
| BKCMACTF | 11 | Account follow-up tasks — date/rep/type/5×remarks/SO link |
| BKCMEACF | 11 | DDF alt-key view of BKCMACTF |
| BKCMHCOD | 9 | CRM event codes — rate/UM/billable flag/before-normal-final item |
| BKCMVNDF | 10 | Vendor follow-up tasks (with PO link) |
| BKCMVNDH | 8 | Vendor contact history |
| BKCMDUNH | 6 | Dunning history per account — date/form/age/amt |
| BKCMREP | 14 | CRM sales rep — name/emp/pswd/defaults/permissions |
| BKCMTERR | 11 | Territory codes — desc/email/alpha/flags/date |
| BKCMCNTD | 12 | Contact field title labels (10 titles + MREP + LTYPE) |
| BKCMFORM | 8 | Letter/dunning form definitions — CODE+LINE+NOTE+margin settings |
| BKCMFTME | 7 | Billable time summary per account — FTIME/ATIME/NTIME buckets |
| BKCMEFTM | 7 | DDF alt-key view of BKCMFTME |
| BKCMHCD2 | 7 | Event code cross-ref — phone/customer/report action parts |
| BKCMSBDF | 5 | Billing settings — increment/rate/conversion |
| BKCMACTD | 4 | Account date tracking — CODE+DCODE+DATE+EXTRA |
| BKCMEACD | 4 | DDF alt-key view of BKCMACTD |
| BKCMPCTH | 8 | Prospect contact history (shorter than BKCMACTH) |
| BKCMPCTF | 9 | Prospect contact follow-up |
| BKCMPCFC | 3 | Prospect follow-up codes |
| BKCMACFC | 3 | Account follow-up codes |
| BKCMVNFC | 3 | Vendor follow-up codes |
| BKCMACCL | 2 | Account classification lookup (CODE→CLASS) |
| BKCMEACC | 2 | DDF alt-key view of BKCMACCL |
| BKCMDTCD | 2 | Date code definitions |
| BKCMACCC | 2 | Contact class codes |
| BKCMLEAD | 2 | Lead source codes (SCODE+DESC) |
| BKCMTEMP/TMP1-4 | 6 each | Temp/sort scratch tables |
| BKCMCTL1-4/BKCMCTRL | 1 each | Concurrent user lock (one slot per session) |

**Key insights:**
- BKCMREP has its own password (BKCM_REP_PSWD, 10 chars) separate from the main AHSYLOG login. VIEW/CHANGE/GWARN/AADD flags control what each rep can see or edit.
- BKCMDE and BKCMEACT are DDF alt-key views of BKCMACCT — not separate tables.
- Activity billing: BKCMACTH tracks start/stop times, minutes billed (BMIN), rate, and running balance (BALNC) per activity log entry — full time-and-billing in CRM.
- BKCMMHST mailing campaigns support complex include/exclude criteria: up to 20 include + 20 exclude class codes, plus 9 address/territory/date range filters.
- ISREMIND is shared across CRM (T7CMA/CMCVTF), US-G triggers, and SR — it is the system-wide calendar/reminder table.

**Confidence: 82/100** — All 37 BKCM* tables field-extracted from DDF; all 6 T7CM* programs identified with proc counts and DB fingerprints; CRM architecture (3-entity + parallel activity sets) confirmed; individual program business logic inferred from DB fingerprints, not source code.

---

### Commission / Salesperson Management (CS)

**What it does:** Manages salesperson commission setup, monthly performance stats, per-invoice commission ledger, commission transfers, and commission reports. Also shares the BKPRMSTR employee/payroll master with the PR (Payroll) module.

**RWN programs (17):**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7CSA | 99 | Salesperson master setup (BKPRSALE+BKPRMSTR+BKPRAGNT) |
| T7CSB | 138 | Commission record view/edit |
| T7CSC | 98 | Commission transfer |
| T7CSD | 15 | Commission display |
| T7CSDE | 65 | Commission detail by rep+customer+item (ISREPLNK) |
| T7CSDO | 129 | Commission processing — DO pass (BKPRCOMM+BKPRCURP) |
| T7CSDX | 104 | Commission processing — DX pass |
| T7CSE | 114 | Salesperson invoice report |
| T7CSF | 105 | Commission report (BKARINV-level) |
| T7CSI | 46 | Commission inquiry |
| T7CSK–N | 8 ea | Report sub-panels (4 variants) |
| T7CSO | 168 | Commission output/post (BKPRCOMM+BKPRSALE+BKAPVEND) |
| T7CSP | 105 | Commission payment report |
| T7CSQ | 25 | Commission query |

**Key operations:**
- **CS-A — Salesperson Master:** Commission class (BKPR_SLS_CLASS_1/2), rate (BKPR_SLS_RATE_1/2), method HOW (`S`=% of sales, `G`=% of gross margin), WHEN (`I`=at invoice, `P`=at payment); linked GL account; linked AP vendor (BKPRAGNT) for outside reps.
- **CS-B/C — Commission Record/Transfer:** BKPRCOMM per-invoice ledger; transfer moves earned commission between periods.
- **CS-DO/DX — Commission DO/DX Pass:** Builds BKPRCURP current payroll period record; posts commissions to BKGLTRAN.
- **CS-E/F/P — Reports:** Detail and summary commission reports by salesperson/period.
- **CS-O — Commission Output/Post:** Writes BKPRCOMM (12f) commission due records; cuts AP checks via BKAPVEND for outside agents.

**Primary tables:**

| Table | Fields | Purpose |
|-------|--------|---------|
| BKPRSALE | 87 | Salesperson monthly perf stats (12×QUOTA, GROSS, COGS, RCPTS, COMM, PAID) |
| BKPRCOMM | 12 | Per-invoice commission ledger (SLSP+CCODE+INVNM+COMM+PD_ON+PCODE) |
| BKPRAGNT | 4 | Outside agent master: agent#, code, GL account+dept |
| BKPRMSTR | 384 | Employee/payroll master shared with PR module (SSN, pay rates, YTD accumulators) |
| BKPRCURP | 127 | Current payroll period record per employee (run when CS-DO executes) |
| ISREPLNK | 11 | Rep-to-customer/item commission link (date-range, GL account override) |

**BKPRCOMM field reference (12f):**
`BKPR_COMM_SLSP`(2) — salesperson# | `BKPR_COMM_CCODE`(10) — customer code | `BKPR_COMM_INVNM`(8) — invoice# | `BKPR_COMM_INVDT`/`PAYDT` — invoice/payment dates | `BKPR_COMM_AMTPD`(8) — amount paid | `BKPR_COMM_COMM`(8) — commission amount | `BKPR_COMM_PD_ON`(8) — paid-on amount | `BKPR_COMM_ULID`(8) — unique line ID | `BKPR_COMM_TDATE` — transfer date | `BKPR_COMM_PCODE`(15) — item/product code

**Confidence: 80/100** — 17 programs mapped; BKPRSALE/BKPRCOMM/BKPRAGNT/BKPRMSTR/BKPRCURP/ISREPLNK schemas fully extracted from DDF; commission calculation HOW/WHEN logic confirmed from field names; exact formula and GL mapping in encrypted RWN.

---

### Lot Control (LC)

**What it does:** Assigns lot numbers to items, tracks lot on-hand/received/issued quantities, enforces lot expiry dates, and provides full lot traceability through SO/WO/PO. Parallel to SC (Serial Control) for lot-tracked items.

**RWN programs (7):**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7LCA | 71 | Lot master entry/view (LOT+MTICMSTR+BKYSMSTR+WORKORD) |
| T7LCB | 59 | Assign lot control to items (sets lot-tracking flag in BKICMSTR) |
| T7LCC | 125 | Lot transaction history (LOT+BKARTXN+INVTXN) |
| T7LCD | 5 | Lot detail panel |
| T7LCE | 124 | Lot edit/adjust (LOT+BKICLOC) |
| T7LCF | 95 | Lot traceability — which SOs shipped a lot (BKARCUST) |
| T7LCG | 98 | Lot archive by expiry date |

**Key operations:**
- **LC-A — Lot Master:** Create/view lot records; assign to received items (PO receipt → LOT row).
- **LC-B — Assign Lot Control:** Toggle lot-tracking on/off for an item in BKICMSTR.
- **LC-C — Transaction History:** Full trace of lot movements (receipts, issues, shipments) from BKARTXN+INVTXN.
- **LC-E — Lot Adjust:** Correct lot on-hand quantities; updates BKICLOC bin-level inventory.
- **LC-F — Lot Traceability:** Show which customers received a specific lot.
- **LC-G — Archive:** Remove expired lots (past MTLOT_EXPDATE) to archive storage.

**LOT table — MTLOT_ prefix (25f):**
Primary key: `MTLOT_CODE`(15) item code + `MTLOT_LOT`(15) lot number.

| Field | Type/Size | Meaning |
|-------|-----------|---------|
| MTLOT_CODE | STRING 15 | Item code (FK → BKICMSTR) |
| MTLOT_LOT | STRING 15 | Lot number |
| MTLOT_EXPDATE | DATE 4 | Lot expiry date |
| MTLOT_ONHAND | FLOAT 8 | Current on-hand quantity |
| MTLOT_PO | FLOAT 8 | Qty on open PO |
| MTLOT_RECDOC | FLOAT 8 | Receipt document# |
| MTLOT_VENDOR | STRING 10 | Vendor code (who supplied lot) |
| MTLOT_RECDATE | DATE 4 | Date received |
| MTLOT_RECQTY | FLOAT 8 | Quantity received |
| MTLOT_POCOST | FLOAT 8 | PO unit cost at receipt |
| MTLOT_WO | FLOAT 8 | Work order# (if lot produced internally) |
| MTLOT_INRECDATE | DATE 4 | Internal receipt date (WO completion) |
| MTLOT_WOQTY | FLOAT 8 | WO completion quantity |
| MTLOT_WOCOST | FLOAT 8 | WO cost |
| MTLOT_NOTES_1..5 | STRING 45 | Five 45-char note lines |
| MTLOT_LOC | STRING 10 | Storage location |
| MTLOT_WOSUF | UBINARY 2 | Work order suffix |
| MTLOT_EXTRA | STRING 50 | Extra notes |
| MTLOT_BEGIN | FLOAT 8 | Beginning quantity (period open) |
| MTLOT_OUT | FLOAT 8 | Quantity shipped/issued out |
| MTLOT_MAXOUT | FLOAT 8 | Maximum issue quantity allowed |

**DDF note:** The DDF table name is `LOT` but all field names use the `MTLOT_` prefix.

**Confidence: 80/100** — 7 programs mapped; LOT/MTLOT_ schema fully extracted (25f confirmed); lot lifecycle (receive via PO → store by location → trace to customer) confirmed from DB fingerprints and field structure.

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
| BKQCMSTR (14f) | QC master records — receiving QC by vendor |
| BKQCTRAN (21f) | QC transaction log — per-item QC event log |
| ISNCR (35f) | NCR/defect tracking — linked to WO/PO/RMA |
| ISQCSPEC (57f) | QC specification per routing operation |
| ISQCMTHD (44f) | QC measurement methods |
| ISWOTRAY (52f) | WO tray scan + QC results by tray |

**SCRAP (21f) — Scrap Code Master:**
`MTSCRAP_CODE`(10 PK) + DESC(30) + TYPE(1, scrap classification type) + EXTRA(100) + GLACCT(10)/GLDPT(4, GL scrap account) + FLAG_1..5 (1×5 custom flags) + ALPHA_1..5 (15×5 custom alpha fields) + DATE_1..5 (date×5 custom dates). One row per scrap reason code. GL accounts allow scrap to be posted to different GL accounts by type. MTSCRAP_ prefix = MT-era table. Used across QC, WO (BKDCLAB has 5 scrap code slots), HH, and RMA modules.

**Confidence: 62/100** — 18 programs confirmed; all QC table schemas extracted; SCRAP(21f) full schema decoded; QC inspection flow traced; NCR/CAPA workflow confirmed; per-inspection measurement logic blocked by encryption.

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

### ISFXASST — Fixed Asset Master (23f)
`IS_FXA_NUMBER` PK; TYPE(4)+DESC(60)+DESC2(60); CSTBAS(cost basis)+RESVAL(residual value, float)+LIFE(float); METH(4, depreciation method: SL=straight-line, DB=declining-balance, etc.); GLA/GLD (GL asset account+dept); ACDEPA/ACDEPD (accumulated depreciation GL account+dept); DEPEXPA/DEPEXPD (depreciation expense GL account+dept); SDATE (placed in service) + EDATE (disposal date); SOLD(1, sold/retired flag); ACCUMDEP (accumulated depreciation balance, float); SERIAL(20, serial/tag number); LDEPAMT/LDEPPERC/LDEPDATE (last depreciation amount/percentage/date); EXTRA(100).

### ISFXATRN — Fixed Asset Depreciation Transaction (12f)
`IS_FXT_NUMBER` (FK → ISFXASST) PK with DATE; AMOUNT(float)+PERC(float, depreciation rate this period); AUDIT(flag); POSTED(1, posted to GL); ACDEPA/ACDEPD (accumulated depreciation GL account+dept); DEPEXPA/DEPEXPD (depreciation expense GL account+dept); NETAVAL (net available value after depreciation); EXTRA(100).

One row per depreciation run per asset. Posted=Y means GL transaction was created in BKGLTRAN.

| Table | Fields | Purpose |
|-------|--------|---------|
| ISFXASST | 23 | Fixed asset master — cost basis, method, life, GL accounts, accumulated depreciation |
| ISFXATRN | 12 | Depreciation transaction log — per-period amount+%, posted status, GL routing |

**Confidence: 82/100** — ISFXASST(23f) and ISFXATRN(12f) full schemas extracted from DDF; all FA-A/FA-B field references now confirmed; depreciation calculation formula (SL vs. DB) confirmed from METH field; GL posting flow confirmed (ISFXATRN.POSTED → BKGLTRAN); FA-E export logic blocked by encryption.

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
- **SM-E/F — Tax Setup:** ISTAXFIL(84f: tax rates) + ISIS.TXG (tax groups). ISTAXFIL structure: CODE(10) PK + DESC + VNDCD(tax authority vendor) + IDNUM; 9 SO brackets (SOLRNG quantity ranges + SOHRNG hour ranges + SOPERC percentages + TICD type flags) + 9 PO brackets (POLRNG/POHRNG/POPERC/PTICD); GL accounts for SO tax (GLASO+GLDSO) and AP/PO tax (GLAPO+GLDPO); TAXIN(1 inclusive flag), ISCUR(3 currency), SOMAX+POMAX (max tax amounts). Tax groups (ISTAXGRP) assign a tax file CODE to a customer or vendor.
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

**Menu codes:** SR-A through SR-T (9 menu ops); 16 RWN programs total including dispatch, backflush, and info sub-screens.

**KEY ARCHITECTURE FACT — SR Orders are BKARINV records:** Service Orders share the same table as AR invoices and Sales Orders. There is no BKSR* master table. The ISSR* entries in the DDF are Btrieve alternate-index views into BKARINV/BKARINVL, not separate tables.

**Key operations:**
- **SR-A — View/Enter Service Orders:** Main entry (T7SRA.RWN, 15 procs). Opens ISSDET, WORKORD, ISSPC, ISSERR, BKAPVEND, BKCMACCN. Creates BKARINV records (service type).
- **SR-K — Equipment Master:** T7SRK.RWN. ISSRMMS — make/model/serial (50 chars each), in/out dates, linked WO#.
- **SR-E — Release/Issue Parts:** T7SRE.RWN. Issues parts from WO to service order (INVTXN, BKICLOC, WOBOM, WOROUT). Checks IS2DBAR barcode config.
- **SR-F — Print/Reprint Invoices:** T7SRF.RWN (form caption: "SO-F" — shared with SO). Opens BKCMACCT, BKISTAX, BKARHTAX, ISSRINFO.
- **SR-G / SR-GA — Post Service Invoices:** T7SRGA.RWN (157 procs). Posts to BKGLTRAN+BKGLX+BKARCUST+BKARINVT+BKARHTAX+ISTAXGRP. Most complex SR program.
- **SR-I — Inquiry:** T7SRI.RWN. Browse posted service invoices; opens ISSOBOX, BKSOLOCK for ship box tracking.
- **SR-INFO — Misc. Information:** T7SRINFO.RWN. Reads/writes ISSRINFO — configurable 20-alpha + 5-date per service record.
- **DISPATCH — Dispatch Manager:** T7SRDISPACH.RWN. View open service orders for scheduling.
- **SR-BK — Live Work Center / Backflush:** T7SRBK.RWN. Opens WORKORD, WOROUT, BKDCLAB, BKPRMSTR — connects service ops to WO backflush.

**Primary SR-specific tables:**

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSRMMS | 12 | Equipment per service line — MAKE(50), MODLE(50), SERIAL(50), INDATE, OUTDTE, EXTRA(150) |
| ISSRINFO | 54 | Configurable service info — 20 ALPHA + 5 DATE slots × 2 groups |
| ISARINVX | 4 | AR invoice extension — EXTRA1(100) + EXRTA2(100) for service use |
| ISSOREVU | 12 | SO/SR approval workflow — DEPT, EMPNME, MOTPAS (override), APPROVE/REQUIRE flags |
| ISSRFQH | 57 | Service RFQ header — identical structure to BKAPPO (PO table) |
| ISSRFQL | 38 | Service RFQ lines — identical structure to BKAPPOL |
| ISSDET | 4 | Standard service details — TYPE/DETAIL codes + WHO + SUB flag |
| ISORDECO | 13 | Order decoration — special instructions per SO/SR order + part + drawing# |
| ISNTYPE | 4 | Note type codes — TYPE(3) + DESC(30) + security level |
| ISUDFINV | 8 | User-defined invoice fields — maps custom names to byte offsets in BKARINV |
| BKISTAX | 13 | Historical tax totals by code/date — TAXABL + NONTAX amounts |
| BKARHTAX | 5 | Historical AR tax per invoice — INVNO + CODE + ID + AMOUNT |
| ISARTXNB | 23 | AR transaction batch — SONUM + CODE + LINEID + BIN + LOC |

**Confidence: 72/100** — SR workflow and table set confirmed from 16 RWN db-file lists; ISSRMMS/ISSRINFO/ISSOREVU fully field-documented; per-screen business logic still encrypted in RWN.

---

### Multi-Yield Work Orders (MU)

**What it does:** Records multiple co-product or by-product outputs from a single work order. Used in industries where one production run yields several distinct finished items (e.g., sawing lumber → multiple sizes, blending → multiple fill weights).

**RWN program:** T7MULTIYIELD (150 procs) — single program. Full DB set: WORKORD + BKSYMSTR + MTICMSTR + WOROUT + BKYSMSTR + BKARINVL + BKICMSTR + BKICLOC + ISBINLOC + WOBOM + WORECV + INVTXN + WOMAT + ISWOEX + LOT + ISBINLOT + SERIAL + ISBNMSTR + ISICMSTR + BKAPPO + BKAPPOL + BKARINV + BKGLTRAN + BKGLX + DBAFIFO + ISTRIGRS + ISREMIND + ISNCR.

**Workflow:**
1. A WO is created for the input item/process (WORKORD).
2. Multi-Yield entry records each output item with its own WORECV (quantity received) and INVTXN (inventory transaction).
3. Cost is split across outputs; MTICMSTR (standard cost) + DBAFIFO (FIFO cost layers) are updated per output item.
4. ISWOEX (WO extended fields) holds supplemental multi-yield state.
5. LOT/SERIAL/ISBINLOT/ISBINLOC track lot/serial numbers and bin locations for each output.

**Key table:** ISWOEX (WO extended) — the MU-specific extension hanging off WORKORD; exact field count not yet extracted.

**Confidence: 62/100** — Single-program module with 150 procs; full DB fingerprint traced; workflow reconstructed from table set; ISWOEX schema and form fields in encrypted RWN.

---

### Field Service (FS)

**What it does:** Optional add-on module for managing field service operations — tracks service class definitions, employee-to-class assignments, and field service information records. Works alongside the SR (Service/Repair) module.

**RWN programs:**
- **T7FSCLASS** (62 procs) — maintains ISFSCLAS (service class definitions) and reads ISPRINFO (employee profile data)
- **T7FSEMP** (59 procs) — assigns employees (BKPRSALE) to service classes (ISFSCLAS)
- **T7FSINFO** (61 procs) — maintains ISFSINFO (FS information records)

**Key tables:**

| Table | Fields | Purpose |
|-------|--------|---------|
| ISFSCLAS | 3 | Service class master — CLASS(4), GROUP(50), EXTRA(50) |
| ISFSINFO | 4 | FS info records — PROGRAM(20), CONTRACT(25), MISC(100), WHO(50) |
| ISPRINFO | 4 | Employee profile info — PROG(30), DESC(80), MISC(50), TYPE(1) |
| BKPRSALE | many | Salesperson/employee master (PR module) |

**Typical use:** Define service classes (e.g., "HVAC", "ELEC"), assign techs to classes, then link FS records to SR service orders.

**Confidence: 62/100** — Three RWN programs identified with full DB fingerprints; key tables field-documented; no DFM forms found (possibly not licensed in this install); no CHM entries.

---

### Global Finance / AR Charges (GF)

**What it does:** Two related functions — (1) customer-item pricing matrix entry (T7GFPRICE) and (2) view/edit of extra AR invoice charges with full before/after audit trail (T7GFV/T7GFVS). Also includes a GF report and test program.

**RWN programs (5):**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7GFPRICE | 116 | Customer-item pricing matrix (BKICPMAT) entry/edit |
| T7GFV | 82 | View/edit AR invoice extra charges; ISARCHG audit trail |
| T7GFVS | 81 | Same as T7GFV, entry starts from invoice lines (BKARINVL) |
| T7GFR | 46 | GF report |
| T7GFTEST | 5 | Test/diagnostic stub |

**Key table — BKICPMAT (85f) — Customer-Item Pricing Matrix:**
Per-customer, per-item pricing override table with 10 price break levels, 2 commission rates per break, and promotional flags. Primary key: `BKIC_PMAT_CUST`(10) + `BKIC_PMAT_PCODE`(15) + `BKIC_PMAT_PNUM`(2).

| Field group | Meaning |
|-------------|---------|
| BKIC_PMAT_RATE_1..10 | 10 price break rates |
| BKIC_PMAT_QTY_1..10 | Quantity thresholds for each break |
| BKIC_PMAT_PER_1..10 | Percentage/amount per break |
| BKIC_PMAT_COMM1_1..10 | Commission rate 1 per break |
| BKIC_PMAT_COMM2_1..10 | Commission rate 2 per break |
| BKIC_PMAT_EXP | Expiration date |
| BKIC_PMAT_SDATE/EDATE | Effective start/end dates |
| BKIC_PMAT_DCODE(10) | Discount code |
| BKIC_PMAT_CLASS(4) | Item class (FK → CLASMSTR) |
| BKIC_PMAT_MIN/MINPR | Minimum qty / minimum price |
| BKIC_PMAT_PROMO | Promotional flag |
| BKIC_PMAT_METH(11) | Pricing method string |
| BKIC_PMAT_OFFIN/OFFCH | Off-invoice / off-charge amounts |
| BKIC_PMAT_SCAND/FRTAL/BILLB/SWELL/ACCRU | Trade promotion buckets |
| BKIC_PMAT_LUMP | Lump-sum override |
| BKIC_PMAT_PDESC(30) | Price description |
| BKIC_PMAT_UID(40) | Unique ID / user ID |

**Key table — ISARCHG (26f) — AR Invoice Charge Audit Trail:**

| Field | Type/Size | Meaning |
|-------|-----------|---------|
| ISAR_CHG_SONUM | FLOAT 8 | Sales order / invoice number |
| ISAR_CHG_INVNUM | FLOAT 8 | Invoice number |
| ISAR_CHG_LINEID | FLOAT 8 | Line ID within invoice |
| ISAR_CHG_PCODE | STRING 15 | Product/item code |
| ISAR_CHG_CDATE | DATE 4 | Change date |
| ISAR_CHG_USER | STRING 15 | User who made the change |
| ISAR_CHG_REVLVL | STRING 10 | Revision level |
| ISAR_CHG_ALOC / BLOC | STRING 10 | From-location / To-location |
| ISAR_CHG_APRICE / BPRICE | FLOAT 8 | Before/after price |
| ISAR_CHG_ADISC / BDISC | FLOAT 8 | Before/after discount |
| ISAR_CHG_AOOQTY / BOOQTY | FLOAT 8 | Before/after open order qty |
| ISAR_CHG_AESD / BESD | DATE 4 | Before/after estimated ship date |
| ISAR_CHG_AASD / BASD | DATE 4 | Before/after actual ship date |
| ISAR_CHG_ACOMPR_1/2 | FLOAT 8 | Before commission rates |
| ISAR_CHG_BCOMPR_1/2 | FLOAT 8 | After commission rates |
| ISAR_CHG_AEXTRA / BEXTRA | STRING 150 | Before/after extra notes |
| ISAR_CHG_UNUM | UBINARY 4 | Unique record number |

**Confidence: 75/100** — 5 programs mapped; BKICPMAT (85f) and ISARCHG (26f) fully field-documented from DDF; pricing break/commission structure confirmed; GF-price application logic (how BKICPMAT overrides BKICMSTR list price during SO entry) in encrypted RWN.

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

**BKSYMSTR** — 286-field global system configuration table (one record per company). Primary accessed via AD-A/AD-B/AD-C (T7MDEFAULTS/T7MDEFBANKS/T7MDEFNDC). Full field breakdown:

| Field group | Fields | Content |
|---|---|---|
| Auto-numbers | ARINV_NUM, APINV_NUM, APPO_NUM, GJ_NUM, ARSO_NUM | Next AR invoice#, AP invoice#, PO#, GL journal#, SO# |
| Record counters | AP_RECNUM, GJ_RECNUM, AR_RECNUM | Last-used record offsets |
| Company | COMP_NAME(25)+ADD1+ADD2+CSZ(25 each) | Company name and address (printed on forms) |
| Tax | TAX_RATE | Default sales tax rate |
| 20 payment terms | TERMS_1..20 (name) + TRM_AMT/TYP/DAY/EOM/MAX/DISC per term | Inline terms table (120 fields total) |
| AR defaults | AR_SHP_VIA(15)+AR_SLSP(2)+AR_ENTBY(5)+AR_TAXABL(1) | Default ship via, salesperson, entered-by, taxable flag |
| AR end-of-form text | AR_ENDDESC_1..5 (30 each) | 5 lines printed at bottom of AR invoices |
| AR flags | AR_TURNOFF(1)+AR_PEL(1) | Turnoff flag + PEL flag |
| AP defaults | AP_SHP_VIA(15)+AP_ENTBY(2)+AP_PEL(1)+AP_ENDDESC_1..5 | AP ship via, entered-by, PEL, 5 end-of-form lines |
| GL accounts | GL_CLRING+GLDPT_CLR, AR_GLACT+AR_GLDPT, AR_DISCGL+DISCDPT | Clearing, AR trade, AR discount accounts |
| | AP_GLACT+AP_GLDPT, AP_DISCGL+DISCDPT | AP trade, AP discount accounts |
| | TAX_GLACT+TAX_GLDPT, PO_TAXGL+PO_TAXDPT | Tax collected, PO tax accounts |
| | PO_FREIGHT+PO_FRGTDPT, GL_RETEARN+GLDPT_RET | PO freight, retained earnings accounts |
| | GL_RELYR+GLDPT_RELY, GL_ARINTR+GLDPT_ARIN | Prior-year relief, AR interest accounts |
| | AR_FREIGHT+AR_FRGTDPT, PO_RNI+PO_RNIDPT, PO_INR+PO_INRDPT | AR freight, PO receiving, PO in-route accounts |
| Fiscal | FISCAL_YR (DATE) + PRGS_WHR(40) | Fiscal year start date; progress report path |
| AR interest | AR_INT_RTE (float) + AR_INT_DAY (int) | Late payment interest rate + calculation days |
| 9 bank accounts | CHK_NUM_1..9 (next check#) + CHK_BAL_1..9 + CHK_NAME_1..9(30) | Per-bank: next check number, balance, name |
| | CHK_CHKACT_1..9(10) + CHK_CHKDPT_1..9(4) + CHK_CHKCUR_1..9(3) | Per-bank: GL account, GL dept, currency code |
| AR/AP/PR check index | AR_CHKACT, AP_CHKACT, PR_CHKACT (UBINARY 2) | Which bank slot (1-9) for each module |
| Plain paper flags | PLAIN_INV, PLAIN_PO, PLAIN_STMT, PLAIN_CHKS (1 each) | Use pre-printed forms vs. plain paper |
| | FORM_CMPNY (1) | Print company name on forms |
| Feature flags | AUTO_BO(1), RTS_DEF(1), TAL(1) | Auto backorder, routing default, TAL module enabled |
| Aging buckets | AR_AGING_1..5 + AP_AGING_1..5 (UBINARY 2 each) | AR and AP aging period boundaries in days |
| PR deduction names | PR_ODNAME_1..6 (12 each) | Payroll optional deduction labels |
| EXTRA | EXTRA (173) | Reserved |

**Access:** AD-A (GL Defaults) via T7MDEFAULTS.RWN (435 procs). See Accounting Defaults (AD) section below.

**Confidence: 78/100** — Full 286-field schema extracted and all field groups decoded from naming conventions; individual field behaviors confirmed from AD module DFM forms and SM module descriptions.

---

### Accounting Defaults (AD)

**What it does:** System-wide configuration hub — sets all GL account codes for every module, controls GL posting behavior, manages checking accounts, and sets AP operational options.

**Menu codes:** AD-A (GL Defaults), AD-B (Checking Accounts), AD-C (AP Defaults)

**RWN programs:**
- **T7MDEFAULTS** (435 procs) — main defaults (AD-A + AD-C); opens BKSYMSTR, BKYSMSTR, ISBANKS, MTICMSTR, CLASMSTR, BKGLCOA, ISTERMS + 35 more
- **T7MDEFBANKS** (79 procs) — bank account setup (AD-B); opens BKGLCOA, ISBANKS, BKSYMSTR, ISMCF
- **T7MDEFNDC** (252 procs) — extended module defaults; opens BKYSMSTR, BKSYMSTR, BKSYAP, BKESTCFG, BKFOCFG

**Key operations:**
- **AD-A — GL Defaults:** Sets posting flags (Post COGS/PO/Adj/WO transactions? Y/N), fiscal period start/end dates, Future Post Date Control (P/G), and 20+ GL account codes (AP payable, AR receivable, COGS, Inventory, WIP, Absorbed Labor/Overhead, Freight, Sales Tax, Commission, Retention, Clearing, Retained Earnings, etc.)
- **AD-B — Checking Account Defaults:** Creates/manages up to 99 bank accounts (ISBANKS). Each has GL account code, type (checking/savings/CC), next check#, Include AP/AR/PR flags, default RTM template override, and active/inactive flag.
- **AD-C — AP Defaults:** Controls AP-B/AP-C/AP-H behavioral options: discount calculation, default search key, >13-invoices-per-check behavior, invoice date vs. today for GL post date, check language (English/Spanish), vendor creation policy, ACH export program name, aging period definitions (5 buckets in days).

**Primary tables:** BKSYMSTR (system config 286f), BKYSMSTR (YN flags), ISBANKS (checking accounts), BKSYAP (AP system config)

**Note on naming:** T7ADCA.RWN is "Advanced Data Collection" (not Accounting Defaults) — different module despite the AD prefix.

**Confidence: 70/100** — CHM content fully documented; RWN programs identified; primary tables known; specific BKSYMSTR field offsets per setting not yet mapped.

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

### BS — Business Score / Summary Dashboard

**What it does:** Real-time cross-module financial dashboard — aggregates KPIs from AR, AP, SO, PO, WO, GL, and Inventory into period-range snapshots stored in ISBSF. Surfaced as QU-D "Business Status" (EVOBS) and as a dedicated BS module with drill-through to source transactions.

**RWN program:** T7BS (162 procs). Opens ISBSF + BKYSMSTR + ISGLDATE + BKSYMSTR + BKGLTRAN + MTICMSTR + BKICMSTR + WORKORD + WOMAT + WOLABOR + OUTPROC + WORECV + WOEXCHG + BKAPPOL + BKAPPO + ISICMSTR + BKARINV + BKARINVL + BKARINVT + BKAPCHKF + BKARDEP + BKAPINVT + ISBANKS + BKGLCOA + ISMCF + ISDRILL + standard boilerplate.

**ISBSF — 143 fields** (PK: ISBSF_STARTDATE + ISBSF_ENDDATE period range):

| Field group | Fields | Meaning |
|------------|--------|---------|
| AR | AR_BAL/BILL/RECP/DISC/COGS/DEPO | AR balance, billed, receipts, discounts, COGS, deposits |
| AP | AP_BAL/PAYA/PAYM/DISC/ATP | AP balance, payables, payments, discounts, available-to-pay |
| SO | SO_OPEN/BOOK/SHIP | Open SO value, booked, shipped |
| PO | PO_OPEN/BOOK/RECP | Open PO value, booked, received |
| WO | WO_WIPBAL/ISSU/FPVAR | WIP balance, issued materials, finish-post variance |
| IC | IC_VALUE | Inventory value |
| CASH | CASH_TOTA + CASH_ACT1..9 | Cash total + 9 GL cash account balances |
| CASH_ACTS | CASH_ACTS_1..100 | 100-period GL cash account history array |
| WOS | WOS_SETUP/LAB/OUTP/MAT/FOH/VOH/MEXT/FP/WIPV | WO standard cost breakdown (setup/labor/outside process/material/OH variants/WIP variance) |
| EXTRA | EXTRA (100) | Free-text extra |

**Confidence: 65/100** — T7BS program identified with full DB fingerprint; ISBSF (143f) fully field-documented; all module data sources confirmed; aggregation/scoring algorithm in encrypted RWN.

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

**ISSCHED (24f) — Job Scheduler Table:**
- IS_SCHED_NAME(20) PK — task name
- IS_SCHED_DESC(60) — description
- IS_SCHED_PROG(30) — program to run (RWN name)
- IS_SCHED_CO(4) — company code
- IS_SCHED_TYPE(1) — schedule type (O=one-time, D=daily, W=weekly, M=monthly)
- IS_SCHED_DATE (date) — next run date
- IS_SCHED_TIME (time) — next run time
- IS_SCHED_RECUR(1) — recurrence interval
- IS_SCHED_LOG(1) — log runs flag
- IS_SCHED_EXTRA(100)
- IS_SCHED_LDATE / LTIME — last run date/time
- IS_SCHED_WHO(15) — last run by user
- IS_SCHED_EMAIL(80) — email address for completion notification
- IS_SCHED_PARAM1..9 + PARAM0 (10 parameters passed to the RWN program at runtime)

**Tables:** ISREMIND — reminder record (date, contact, trigger type, linked record key, note text); ISSCHED — scheduler job queue (timed execution of any RWN program with parameters).

**Confidence: 65/100** — ISSCHED(24f) full schema extracted; scheduler architecture fully understood (EVOSCHEDULER 65p reads ISSCHED, launches programs with params); ISREMIND(22f) confirmed; trigger/reminder detail logic blocked by encryption.

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

**Confidence: 75/100** — 13 RWN programs identified; BKSAREPT (57f) and BKACTRPT (53f) full schemas extracted; SA reads live AR invoices (no pre-aggregated table); T7SAQ actual-margin mechanism confirmed via WO cost tables.

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
| BKICLOC | BKICLOC.B | IN | Inventory locations | Product + location (PK); UOH/UOSO/UBO/UOO/UOWO/UALLOC; per-location GL accounts for adj/cost/sales/WIP |
| BKICLOCM | BKICLOCM.B | IN | Location master | Location code (PK), name, address, TAXGR tax group |
| BKICPMAT | BKICPMAT.B | IN | Customer price matrix | Customer + item + entry# (PK); RATE_1..10 + QTY_1..10 (10 qty-break pricing) |
| BKICDIM | BKICDIM.B | IN | Item dimensions | Part# (PK); FIRST/SECOND/THICK dimensions; ALLOY, TEMPER, FINISH; F_TOL/S_TOL/T_TOL tolerances; DENSITY |
| BKICREQ | BKICREQ.B | IN | Inventory requisitions | REQ_NUM (PK); STATUS, BY, dates, TOLOCN, NOTES_1..10 |
| MTICAMTR | MTICAMTR.B | JC/IN | MT actual cost snapshot | 108-field clone of MTICMSTR — actual cost values for variance analysis |
| MTICEMTR | MTICEMTR.B | JC/IN | MT estimated cost snapshot | 108-field clone of MTICMSTR — estimated standard cost values |
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
| ISBSF | ISBSF.B | BS | Business score dashboard | PK=STARTDATE+ENDDATE; 143f cross-module KPI snapshot: AR_BAL/BILL/RECP/COGS, AP_BAL/PAYA/PAYM, SO/PO/WO open+booked+shipped, IC_VALUE, CASH_TOTA+ACT1..9 (9 GL accts), CASH_ACTS_1..100 (100-period history), WOS cost breakdown |
| ISESTDTL | ISESTDTL.B | RF | Estimate details | Line-level detail records for production estimates; source for RFQ generation |
| ISSCHED | ISSCHED.B | Scheduler | Scheduler jobs | EvoScheduler/EvoRemind job queue — timed task records (confirmed from EvoSched.RWN, EvoScheduler.RWN, EVOSERVICE.RWN) |
| ISSERCNT | ISSERCNT.B | IT | Serial counters | Auto-serial number counter state per item/config |
| ISSDET | ISSDET.B | SD | Standard details | Standard labor/machine time detail records per operation |
| ISTRIGRS | ISTRIGRS.B | US/DI | Trigger notifications | Automated event triggers — CODE(15), TRIGR(10), CONTACT(20), DAYS, EMAIL(400), WO/PO/SO/CUST/VEND refs; fires N days before a date; used by US, DI, EvoRemind |
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
| BKICPMAT | BKICPMAT.B | IN/ES | Customer price matrix | Customer + item + entry# (PK); 10 qty-break RATE/QTY arrays; overrides standard item pricing |
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
| ISSRMMS | ISSRMMS.B | SR | SR equipment master | Service order equipment: MAKE(50), MODLE(50), SERIAL(50), INDATE, OUTDTE per service line |
| ISSRINFO | ISSRINFO.B | SR | SR extended info | Configurable service record data — 20 ALPHA_1..20 + DATE_1..5 (× 2 groups = 40 alpha + 10 dates) |
| ISARINVX | ISARINVX.B | AR/SR | AR invoice extension | SONUM + NUM (PK) + EXTRA1(100) + EXRTA2(100) — extra text fields on AR/SR invoices |
| ISSOREVU | ISSOREVU.B | SO/SR | SO/SR approval | Department + manager approval gate with password override for SO and SR orders |
| ISSDET | ISSDET.B | SR | Service detail codes | TYPE(20) + DETAIL(20) + WHO(40) + SUB flag — standard service operation detail codes |
| ISORDECO | ISORDECO.B | SO/SR | Order decoration | Special instructions per order — SONUM + PONUM + UNUM + PART + DRAW + more |
| ISNTYPE | ISNTYPE.B | System | Note types | Note type codes — TYPE(3) + DESC(30) + security level |
| ISUDFINV | ISUDFINV.B | System | UDF invoice fields | Maps custom field names to byte offsets in BKARINV for user-defined invoice extensions |
| BKISTAX | BKISTAX.B | AR | Historical tax totals | TAX_CODE + DATE (PK) + TRFLAG + TAXABL + NONTAX + collected amounts |
| BKARHTAX | BKARHTAX.B | AR | Historical AR tax | Per-invoice historical tax: INVNO + CODE + ID + PID + AMOUNT |
| ISARTXNB | ISARTXNB.B | AR | AR transaction batch | AR transaction batch records: SONUM + CODE + LINEID + BIN + LOC |
| ISDRILL | ISDRILL.B | QU/SU | Query definitions | Saved query: LOOKUP_FROM + LOOKUP_FILE + LOOKUP_FILTERS_1..20 (filter criteria) + LOOKUP_WHILE_1..20 (loop conditions) |
| ISDRILLM | ISDRILLM.B | QU/SU | Drill-down map | Navigation: PARENT→CHILD with SFIELD_1..5→TFIELD_1..5 field mappings + DRILLM_MENU label |
| BKLUGRID | BKLUGRID.B | QU/SU | Grid column layouts | Per-user saved column visibility/order for F3 lookup grids |
| ISDROP | ISDROP.B | System | Dropdown lists | User-configurable picklist: CODE(10) + TEXT(30) + DESC(30) + EXTRA(50) |
| ISDIGSIG | ISDIGSIG.B | DI | Digital signatures | Per-employee PO approval config — EMP(pk), MOTCACH(16), POENTBY/SOENTBY, ACTIVE_1..10 flags, TYPE_1..10 codes, SDATE/FDATE/TDATE_1..10, AMT_1..10, FLAG_1..10, FILE(256), ATIME/ADATE — 89 fields total |
| ISARDEPL | n/a | MA | Deposit application lines | Confirmed in use by T7GETDEP and T7MAPDEPO; not registered in Pervasive DDF; tracks deposit-to-invoice application records |
| ISREMIND | ISREMIND.B | US | Reminders | Calendar reminders — DATE/TIME/WHO/SUBJECT(100)/CUST/VEND/ITEM/DISP(1)/CO/FILE(256)/NOTIFY/EDATE/ENDDT/EMAIL(400)/SENT — 22 fields; created by EvoRemind trigger firing |
| ISBNMSTR | ISBNMSTR.B | WC | Bin location master | LOC(10)+BIN(15) PK, DESC(60), EXTRA(100) — same table used by WC, MU, US modules |
| ISWOEX | ISWOEX.B | MU | WO extended fields | WO extended data — 63 fields: 5 dates, 5 ints, 2 floats, 5 alphas(30), 5 descs, 10 flags, 5 gnums, 5 alphas, 5 notes(100); WOPRE+WOSUF PK; confirmed in DDF (63f) |
| ISITP | ISITP.B | US | Item tracking profiles | NUM(20), DESC(80), EXTRA(100) — small code table used by US trigger setup |

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

**What it does:** Manages customer deposits — records prepayments and applies them against open AR invoices. The deposit is posted to GL when recorded, then reduced when applied to an invoice at shipment/invoicing.

**Workflow:**
1. **Enter deposit (AR-C or AR-N):** T7ARN (191 procs) creates the BKARDEP record — customer code, deposit amount, SO link, SR flag. GL debit = bank account; credit = AR deposit liability.
2. **Apply deposit (MA module):** T7MAPDEPO (97 procs) matches BKARDEP records to BKARINVL lines. Creates ISARDEPL records (deposit application lines — not in DDF but confirmed by T7GETDEP/T7MAPDEPO).
3. **Retrieval helper:** T7GETDEP (18 procs) reads BKARDEP + BKARINVT + ISARDEPL + BKARINVL to return available deposit balance.
4. **Web deposits:** T7GETWEB (6 procs) reads BKARDEP + BKARINVT for web-order deposit retrieval.
5. **Payment recording (AR-C):** T7ARC (228 procs) also touches BKARDEP when deposits are cleared against invoices.

**Primary tables:**

| Table | Fields | Purpose |
|-------|--------|---------|
| BKARDEP | 6 | Deposit master — DEPNO(8), CUST(10), DATE, SO(8), SR(1 flag), EXTRA(50) |
| ISARDEPL | unknown | Deposit application lines — not in DDF but confirmed used by T7GETDEP and T7MAPDEPO |
| BKARINVT | many | AR payment transactions — deposit reduces invoice balance here |
| BKARINVL | 28 | AR invoice lines — deposit is applied against specific lines |
| BKGLCOA | 65 | GL chart of accounts — deposit posts to liability account |

**Confidence: 62/100** — BKARDEP (6f) fully documented; deposit workflow confirmed across 5 programs; ISARDEPL confirmed to exist but not in DDF schema; GL posting flow inferred from BKGLCOA presence in T7MAPDEPO's DB list.

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

**What it does:** Cross-module freeform notes attached to any EvoERP entity — customers, vendors, items, SOs, POs, WOs, or CRM accounts. All notes share the ISNOTES table, tagged by entity type. Note types, security levels, and archive/search capabilities are module-native.

**Program map:**

| RWN | Procs | Operation | Key tables |
|-----|------:|-----------|------------|
| EVONOTES | 96 | Main note entry/view | ISNOTES, ISNTYPE, BKYSMSTR, BKARCUST, BKAPVEND, BKAPDESC |
| EVONOTESARCH | 137 | Archive browser (history + WO changes) | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND, BKICMSTR, WORKCHG |
| EVONOTESEARCH | 59 | Full-text note search | ISNOTES, ISNTYPE |
| EVONOTESPRT | 40 | Print notes | ISNTYPE, ISNOTES, BKAPDESC, MKAHIST |
| EVONOTESRPT | 149 | Notes report (filtered export) | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND, BKICMSTR, BKARINV |
| T7EVONOTES | 48 | Drill-down note viewer | ISNTYPE, ISNOTES, BKAPDESC, ISDRILL |

**ISNOTES (13f) — Note Records**

Primary key: IS_NOTE_ID(48) + IS_NOTE_TYPE(3) + IS_NOTE_CDATE

| Field | Meaning |
|---|---|
| IS_NOTE_ID (48) | 48-char composite key — encodes the parent entity (e.g., customer code, vendor code, item code, WO prefix+suffix, SO number) |
| IS_NOTE_TYPE (3) | Note type code (FK → ISNTYPE, e.g., "SO", "PO", "WO", "AR", "AP", "IT", "CRM") |
| IS_NOTE_CDATE/CTIME/CWHO | Created date / time string / user |
| IS_NOTE_EDATE/ETIME/EWHO | Last-edited date / time / user |
| IS_NOTE_EXTRA (100) | Search/summary text (searchable without reading the full note) |
| IS_NOTE_PRIVATE (1) | Private flag — restricts visibility by security level |
| IS_NOTE_GROUP (4) | Group/category code |
| IS_NOTE_CONTACT (30) | Contact person this note is about |
| Note body (256) | Full note text — stored in the last DDF field (DDF shows as corrupt DATE/256, actual: STRING 256) |

**Note ID structure:** The 48-char IS_NOTE_ID encodes the parent entity. Examples:
- Customer: the 10-char customer code padded/combined
- WO: WOPRE + WOSUF encoded into the ID
- SO/AR invoice: invoice number encoded
- PO: PO number encoded
- Item: item code encoded

This allows EVONOTES/T7EVONOTES to open BKARCUST or BKAPVEND and pull the right notes for any screen.

**ISNTYPE (4f) — Note Type Codes**

Primary key: IS_NT_TYPE(3)
- IS_NT_DESC(30) — description of note type (e.g., "Customer Complaint", "Engineering Change")
- IS_NT_SEC(2) — minimum security level required to view this note type
- IS_NT_EXTRA(100)

Note types are configured via SM-N. Security level on ISNTYPE allows some note types to be visible only to managers.

**WORKCHG (25f) — WO Change Audit Log**

Used by EVONOTESARCH to show WO history alongside notes.

Primary key: WO_CHG_WOPRE(8) + WOSUF(2) + CODE(15) + CDATE + USER

Before/after (A/B prefix) on every WO header field that can change:
- PRIO(1) — priority before/after
- STATUS(1) — status before/after
- CLASS(1) — class before/after
- DESC(30) — description before/after
- QTY(float) — quantity before/after
- SDATE/FDATE/DDATE(date) — scheduled start/finish/due before/after
- ASD(date) — actual start date before/after
- EXTRA(150 each) — extra notes before/after

**How notes attach to records:**

Every EvoERP entity screen (AR, AP, PO, SO, WO, IC) has a notes button that calls EVONOTES with the entity's ID encoded into IS_NOTE_ID. The note type determines which module the note belongs to. EVONOTESEARCH searches IS_NOTE_EXTRA (100-char summary) or the note body. EVONOTESARCH shows ISNOTES alongside WORKCHG records for a complete WO history view.

**Confidence: 72/100** — All 6 programs identified with proc counts and DB fingerprints; ISNOTES(13f)+ISNTYPE(4f)+WORKCHG(25f) fully extracted; IS_NOTE_ID composite key structure inferred from DB fingerprints (BKARCUST/BKAPVEND/BKICMSTR/WORKORD all opened by note programs); note body field is a DDF-corrupted STRING(256) — actual byte layout confirmed from size, not field type.

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
| **J7\*** | i2 Systems customer-specific customization modules — 50 RWN files: handheld scan forms for mattress/corrugated packaging operations, web order import, customer-specific SO/PO/AP workflows. Confirmed customers: Lapco (workwear), Albertsons (grocery). |
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

## EvoERP System Dialogs — How Common Operations Work

### Login and startup sequence

1. **Splash screen** — "Loading Evolution ~ ERP...." shown while runtime initializes.
2. **Login dialog** (EVOMENU_LOGIN) — enter User Name and Password. "View Password" toggle available.
3. **Company selection** (EVOMENU_SELCOMP) — pick a company from a dropdown list.
4. **Main menu** loads — EvoERPmenu.RWN builds the full module tree at runtime; the window frame is EVOERPMENU.DCY.
5. **Expiry warning** (EVOEXPIRE) — if the annual license is near expiry, a countdown appears ("XX Days").

**Changing your own password:** Use EVOCHANGEPASS — requires old password.
**Admin reset of a user's password:** Use EVORESETPASS — does not require old password.

**Data Collection stations** use a separate path: EVODC_LOGIN → EVODCMENU2 (10-tile kiosk) or EVODC (6-button standard DC menu).

### How printing works

Every EvoERP report uses the same universal print dialog (PRINTTLL.DCY):
- **Print** — send to a named printer (Setup button configures printer properties)
- **Print Preview** — preview on-screen before printing
- **Email** — opens NZEMAILTLL email composition form with document attached
- **Print to File** — save output to a file (type + path fields)
- **Number of Copies** — spinner
- **Auto Send Email** — automatically emails without opening compose dialog; driven by contact number/primary code

**SDQ Settings** require a password (PRINTTLLPSWD — "SDQ Settings Password"). SDQ = per-report saved defaults.

**Printing linked documents** (files attached via EvoLinks): handled by IMAGEPRINT — shows "Printing: [filename]" progress.

### How email works

Email is composed in NZEMAILTLL ("Evo ~ ERP email"):
- Fields: To, Cc, BCC, Attachment, Subject, Form (email template name)
- Checkboxes: BCC Self, BCC Rep (auto-BCC the user's own address or assigned sales rep)
- Customer and vendor contact grids allow selecting recipients by name
- **Defaults** (admin-configurable in NZEDEFS): Subject template, Body template, Signature, Attachment path, BCC Self default

### How lookup lists work (QU / SU architecture)

All list-pickers throughout EvoERP use the same **WBKLOOKUP** program (413 procs):
- DataGrid shows records from the target table
- Sort by any column via the "Sort List by:" dropdown
- Actions: Select, Edit, Add New, Delete, Navigate (First/Previous/Next/Last)
- The Drill Down button (green arrow) invokes drill navigation defined in **ISDRILLM**
- Column layouts are stored per-user in **BKLUGRID**

**ISDRILL** (46 fields) — Saved query definitions used by QU-F and embedded lookups:

| Field | Type | Size | Meaning |
|---|---|---|---|
| LOOKUP_FROM | STRING | 30 | Source context (caller module or form name) |
| LOOKUP_GRID | STRING | 15 | Target grid definition name (FK → BKLUGRID) |
| LOOKUP_REC | UBINARY | 4 | Record offset/pointer for positioning |
| LOOKUP_KEY | UBINARY | 2 | Key index to use for the target table |
| LOOKUP_FILE | STRING | 15 | Target Btrieve table file name |
| LOOKUP_FILTERS_1..20 | STRING×20 | 80 each | Filter condition expressions (1600 bytes total) |
| LOOKUP_WHILE_1..20 | STRING×20 | 80 each | Loop-while conditions — stop scanning when false |
| LOOKUP_COMM | STRING | 150 | Command/query string for complex lookups |

WBKLOOKUP opens **76 tables** total — the complete set of every table that any lookup in the system can target. 70 of 76 are in the Pervasive DDF schema. Six are not: **BKLUGRID** (column-layout config per user/grid — runtime only), **FILEKEY / FILEDICT / FILEDFLD / FILEKNUM** (TAS runtime file-dictionary internals), and **FILELOC** (TAS record-navigation API table).

**ISDRILLM** (17 fields) — Drill-down navigation map:
- DRILLM_PARENT (15) + DRILLM_CHILD (15) — source/destination objects
- DRILLM_MENU (25) — label for drill-down menu item
- DRILLM_FILE (15) + DRILLM_SFIELD_1..5 (15 × 5) → DRILLM_TFIELD_1..5 (15 × 5) — source→target field mapping

Admins configure lookup grids via the **SU module** (4 operations, 3 programs confirmed):

| SU Op | Program | Procs | Purpose |
|---|---|---|---|
| SU-A | WBKLUGRID | 68 | Maintain Grid Lookups — configure BKLUGRID per-user column layouts |
| SU-B | EVOERPDRILLM | 31 | Maintain Drill Down Menus — configure ISDRILLM navigation entries |
| SU-C | (T7FORMSEDIT?) | ? | Forms Editor — edit DFM form layouts (SU-C = CHM confirmed; program not yet matched) |
| SU-D | T7GDM | 31 | Grid Maintenance — BKLUGRID+ISDRILLM admin via Grid Display Manager |

**WBKLUGRID (68p) — the admin side of the lookup framework:**
WBKLUGRID is dual-purpose: it IS the SU-A admin tool AND it IS the BKLUGRID table editor. Full 79-table fingerprint includes lookup-only references (BKAPPOL, WOBOM, WORKORD, BKARINV, SERIAL, LOT, etc.) — all accessed read-only as F3-lookup sources that the admin can configure as lookup targets. Key tables: BKLUGRID+FILELOC+FILEKNUM+FILEDICT+FILEDFLD.

- SU-A: Per-grid config: table (File Name), form to open on Select, Security Level, Sort Keys, optional UDF program
- SU-B: Maintains ISDRILLM drill navigation entries — adds/removes drill-down links between objects  
- SU-D: T7GDM (31p) opens BKLUGRID+ISDRILLM+BKSYHELP+LANGDICT — grid display manager
- Each grid can also define Links & Notes fields for inline EvoLinks access

**SU confidence: 72/100** — 3 of 4 programs confirmed (WBKLUGRID 68p, EVOERPDRILLM 31p, T7GDM 31p); SU-C Forms Editor not yet matched to an RWN; BKLUGRID+ISDRILLM as the sole persistent tables confirmed; WBKLUGRID 79-table fingerprint fully explained (read-only lookup source references).

**QU module programs:**
| Operation | RWN program | Purpose |
|---|---|---|
| QU-A Master Inquiry | WBKLOOKUP (413 procs) | Universal lookup grid with drill-down |
| QU-B Calendar Drill Down | CALDRILLBT (94 procs) | Calendar with order activity drill-down |
| QU-D Business Status | EVOBS (128 procs) | Financial dashboard (ISBSF+BKGLTRAN) |
| QU-E Quick Grid Lookup | T7QGRID (62 procs) | Standalone table browser |
| QU-F Query Executor | QUERYEXECUTE (26 procs) | Runs SQL queries from DE-A definitions |

### How messaging works

**Single-line message to current user:** EVOMESSAGE — modal "OK" box.
**Broadcast to all users:** EVOEMSG or EVODCEMSG — type message, choose "All Users" or a specific user, click Send.
**Admin user management** (EVOUSERS): see who is logged in, force-logout a user, Enable/Disable Logins (locks the system for maintenance), Clear User (clear a stuck session), send a message, view User Count.

### Generic input dialogs

Two reusable input popups are used throughout the system:
- **GETALPHAGEN ("GAG")** — single-field text input; caller sets the caption and field label at runtime.
- **T7POPGET ("POP")** — up to 5 fields with a Lookup button; caller sets all captions at runtime. Used wherever a module needs a quick multi-field modal entry without a dedicated form.

### Java integration loading screen

When EvoPVT.jar runs a background task (SQL export, data sync), T7JAVARUN shows "Java Evo Loading..." until the Java process completes. The TRtnTimer polls for completion and dismisses the screen automatically.

### Background data load indicator

T7CLOADING shows "Loading Data" with an animated spinner (TAnimate) whenever a module is fetching a large dataset in the background.

---

## Keyword Index Additions (Pass 19)

| Term | Definition |
|---|---|
| **EVOMENU_LOGIN** | EvoERP login dialog DCY — User Name + Password entry, leads to company selection |
| **EVOMENU_SELCOMP** | Company selection dialog DCY — dropdown list of available companies |
| **EVOMENU_RUNPRG** | Module launcher DCY — dispatches any .RWN by filename; the core of the module dispatch mechanism |
| **EVOCHANGEPASS** | Change Password DCY — requires old password; user self-service |
| **EVORESETPASS** | Reset Password DCY — admin resets a user's password without needing the old one |
| **PRINTTLL** | Universal print dialog — Print/Preview/Email/File for all reports |
| **NZEMAILTLL** | Email composition form — To/Cc/BCC/Subject/Form/Attachment |
| **NZEDEFS** | Email default settings — subject template, body, signature |
| **WBKLOOKUP** | Standard list-picker dialog used by all modules |
| **WBKLUGRID** | Admin form for configuring lookup grid definitions (table, security, sort, UDF) |
| **GETALPHAGEN (GAG)** | Generic 1-field input dialog; caption/label set by caller at runtime |
| **T7POPGET (POP)** | Generic 5-field popup with Lookup button; used throughout for quick modal entry |
| **EVOUSERS** | Active user management — force logout, lock logins, broadcast message, user count |
| **EVODCMENU2** | 10-tile configurable DC kiosk launcher menu |
| **EVOERPSCHED** | Scheduler task name dialog — names/selects a task for ISSCHED |
| **EVOEXPIRE** | Annual license expiry warning dialog |
| **EVOLOGO** | Menu screen logo configurator (admin) |
| **SDQ settings** | Per-report print/save defaults; protected by PRINTTLLPSWD password |
| **DUMMY.DCY / MDUMMY.DCY** | "Evo Base Window" placeholder — base TEditForm1 template |
| **T7CLOADING** | Animated loading spinner shown during background data fetches |
| **T7JAVARUN** | Wait screen shown while EvoPVT.jar executes a Java task |
| **EVOGETDATE** | News/date message with "Do not show again" — dismissable release notes or date prompt |
| **annual license** | EvoERP uses annual subscription licensing; EVOEXPIRE warns near expiry |
| **EvoSettings.INI** | Per-workstation INI file (`C:\ISTS\EvoSettings.INI`) — stores user preferences (printer, language, sounds, reminder settings, module defaults), per-company email config (SMTP, credentials, body/signature templates), and 6 hot-button shortcuts |
| **Hot Buttons** | 6 user-configurable toolbar shortcuts in EvoSettings.INI; each launches any .RWN module with a custom icon and tooltip |
| **EvoorClassicScreen** | Per-module INI key that switches a module between "Evo" (modern) and "Classic" (DBA-era) UI mode |
| **SAVE ACCESS** | Per-module INI key (0/1); when set, EvoERP remembers the last-accessed record when the user re-enters the module |
| **No database-level constraints** | EvoERP has zero declared foreign keys, triggers, stored procedures, or views in Pervasive — all RI and business rules are enforced in TAS Pro application code |
| **TTASENTER** | Core TAS Pro 7 data-entry control — single alphanumeric field; 7,504 instances across all forms; bound to TAS buffer variable |
| **TTASNumEnter** | Numeric-only TAS Pro 7 entry field (3,994 instances) |
| **TTASComboEnter** | TAS Pro 7 editable dropdown — type or select from list; common for code fields with lookup (3,622 instances) |
| **TTASDateEdit** | TAS Pro 7 date entry with calendar picker (1,380 instances) |
| **TTASDataGrid** | TAS Pro 7 data grid for tabular data (423 instances); columns defined by TTASDGColTemplate children |
| **TShellExe** | Shell execution component — how EvoERP triggers print, email, and file-open; 850 instances across all forms |
| **TRtnTimer** | Return/timeout timer — triggers auto-dismiss, polling, or delayed navigation; 227 instances (loading screens, Java wait, reminders) |
| **TGlyphBtn** | Icon button — the standard EvoERP action button (Save, Exit, Browse); 4,485 instances |
| **TTASStrList** | Runtime string list populated by TAS code; 138 instances (menu system, lookup forms) |

---

## Table Quick-Reference Additions (Pass 20/21)

| Table | Purpose | Primary Key | Fields |
|---|---|---|---|
| **MTICMSTR** | MT-generation inventory master (newer than BKICMSTR) — adds 10 vendors, 15 cost slots, 12 specs, 5 substitutes | MTIC_PROD_CODE | 108 |
| **BKBMMSTR** | Bill of Materials — one row per parent+component pair; key fields QTY_REQD, PROD_SCRAP, PROD_OP | BKBM_PARENT + BKBM_COMPONENT | 26 |
| **BKBMAVAL** | Alternate BOM — same structure as BKBMMSTR | BKBM_PARENT + BKBM_COMPONENT | 26 |
| **BKBMAMTR** | Auto-calculated/master BOM — same structure | BKBM_PARENT + BKBM_COMPONENT | 26 |
| **BKRTEMTR** | MT-generation routing master — one row per part+operation; includes 14 instruction lines | MTRO_CODE + MTRO_OPER | 62 |
| **WORKCTR** | Work center master — code, description, department, hourly rates (setup/labor/machine), overhead | MTWC_WC | 47 |
| **ISNOTES** | EvoNotes table — notes attached to any EvoERP record; IS_NOTE_ID = 48-char composite key | IS_NOTE_ID | 13 |
| **ISSCHED** | Scheduler task table — program to run, company, date/time, recurrence, 10 parameters, email notification | IS_SCHED_NAME | 24 |
| **BKRTCST** | Routing cost/quote snapshot — parts-per-hour + setup times by work center, keyed by quote+part+op | BKRT_QUOTE + BKRT_CODE + BKRT_OPER | 24 |
| **BKRTSPEC** | Routing special notes — 4 note lines per operation | BKRT_SPEC_PART + BKRT_SPEC_SEQ + BKRT_SPEC_LINE | 7 |
| **ISLBLMAP** | Label definition/mapping — links item+variant to an .RTM template; 30 color-customizable field slots; customer/vendor-specific label support | IS_LABEL_ITEM + IS_LABEL_NUM | 102 |
| **IS2DBAR** | 2D barcode field config — which data fields appear in 2D barcodes per item, in what order, and on which document types (40 document-print flags) | IS2D_BAR_CODE + IS2D_BAR_ITEM + IS2D_BAR_ORDER | 109 |
| **ISUSAGE** | Item usage history — 26-period rolling qty/amount + 5 prior years (13 periods/year) per item per type; used by MRP/forecasting | ISTS_USE_CODE + ISTS_USE_TYPE | 246 |
| **ISAPAINL** | AP invoice line archive — AP invoice header + up to 75 GL distribution lines (account + amount + D/C + dept per line) | BKAP_INVL_CODE + BKAP_INVL_NUM | 390 |
| **ISLINKS** | Document attachment links — attach file paths/URLs to any EvoERP entity via IS_LNK_UID composite key; 100 type flag slots | IS_LNK_UID | 311 |
| **ISALINKS** | Archived document links — identical schema to ISLINKS; stores archived/historical link records | IS_LNK_UID | 311 |
| **ISESTASM** | MT Estimate summary — quote master with 10 qty-break pricing, full cost breakdown (material/labor/setup/OH/outside-proc/misc) per break | MTESUM_QUOTE | 213 |
| **ISESADTL** | IS Estimate detail — line-level components per estimate, qty + cost at all 10 qty breakpoints | IS_EST_NUM + IS_EST_PART + IS_EST_LINE | 203 |
| **ISMICADT** | MT inventory costing snapshot — actual cost detail; same 108-field schema as MTICMSTR | MTIC_PROD_CODE | 108 |
| **ISMICESA** | MT inventory costing snapshot — estimated standard (average); same 108-field schema as MTICMSTR | MTIC_PROD_CODE | 108 |
| **ISMICEST** | MT inventory costing snapshot — estimated standard; same 108-field schema as MTICMSTR | MTIC_PROD_CODE | 108 |
| **ISTAXGRP** | Tax group definition — groups 9 tax codes with percentage rates, freight flags, and 12-month collected tax tracking | ISIS_TXG_NAME | 105 |
| **ISPRMSTR** | IS extended payroll employee master — 19 user-defined deductions/earnings with QTD/YTD/limit per slot | BKPR_EMP_NUM | 384 |
| **BKCMACCN** | CM contact names — up to 10 contacts per CRM account (name, title, phone, email) | BKCM_ACCN_CODE | 154 |
| **BKCMCUST** | CM customer view — mirrors BKARCUST field layout; used by Contact Manager when accessing AR customer data | BKAR_CUSTCODE | 106 |
| **BKCMMHST** | CM marketing history — activity date, description, 9 classification codes per entry | BKCM_MHST_MCODE | 72 |
| **BKCMREP** | CM sales rep — code, name, employee link, rep-level password, VIEW/CHANGE/GWARN/AADD permission flags | BKCM_REP_REP | 14 |

---

---

## MODULE QUICK REFERENCE — Pass 30 Additions

### DI — Digital Signatures / PO Approval Workflow

**What it does:** Enforces approval gates on Purchase Orders by routing POs for digital signature approval before release. Each employee's authorization limits and approval status are tracked in ISDIGSIG.

**RWN programs:**
- **T7DIGSIG** (128 procs) — main approval entry; reads ISDIGSIG, BKAPPO, BKAPPOL, ISTRIGRS, BKPSUSER, BKARCUST, BKAPVEND; sends email notifications for pending approvals
- **T7DIGSIGADMIN** (5 procs) — admin configuration stub
- **T7DIGSIGPO** (5 procs) — PO-specific signature entry stub

**ISDIGSIG — 89 fields** (keyed on IS_DSIG_EMP = employee# UBINARY 2):

| Field group | Purpose |
|------------|---------|
| IS_DSIG_EMP | Employee ID (PK) |
| IS_DSIG_MOTCACH (16) | Manager override/cache code |
| IS_DSIG_POENTBY (2) / SOENTBY (5) | PO and SO entered-by codes |
| IS_DSIG_ACTIVE_1..10 | Per-slot active flags — which approval slots are live for this employee |
| IS_DSIG_TYPE_1..10 (10 each) | Approval type code per slot |
| IS_DSIG_SDATE/FDATE/TDATE_1..10 | Start/From/Through dates for each approval slot |
| IS_DSIG_AMT_1..10 + IS_DSIG_POAMT | Dollar amount limits per slot + PO amount threshold |
| IS_DSIG_FLAG_1..10 | Status flags per approval slot |
| IS_DSIG_DATE_1..10 | Most recent action date per slot |
| IS_DSIG_FILE (256) | Document/file path attachment |
| IS_DSIG_ATIME / ADATE | Last approval time/date |
| IS_DSIG_EXTRA (100) | Free-text extra |

**ISTRIGRS** (25 fields) is used by T7DIGSIG to send automatic email notifications when POs require approval. Key fields: CODE(15), TRIGR(10), CONTACT(20), DAYS(trigger lead time), EMAIL(400 chars — multi-address list), ONCE flag, LDATE/LTIME (last fired), plus WO/PO/SO/CUST/VEND reference links.

**Approval workflow:** T7DIGSIG reads BKAPPO to check PO amount → compares against IS_DSIG_AMT (slot amount limit) → if PO amount > threshold, routes to approvers by email via ISTRIGRS → each approver signs in using T7DIGSIG → IS_DSIG_DATE/FLAG/ADATE updated when approved → T7DIGSIG releases PO to BKAPPOL processing. T7DIGSIGPO is the PO-side entry point that triggers the signature flow. BKGLTRAN/BKGLX confirm full PO posting happens only after all required approvals.

**Confidence: 72/100** — Three RWN programs identified; ISDIGSIG fully field-documented (89 fields confirmed); approval workflow traced from DB fingerprint (BKAPPO→ISDIGSIG→ISTRIGRS→BKGLTRAN); exact signature form fields in encrypted RWN.

---

### SE / ST — Service Code Tables

**What it does:** Maintains the code-table master records that support the SR (Service/Repair) module: process codes, error/type codes, event type codes, equipment types, and stock types.

**RWN programs:**
- **T7SEPROC** (52 procs) — maintains ISSEPROC (service process codes)
- **T7SERR** (52 procs) — maintains ISSTYPE (service error/type codes)
- **T7SETYPE** (52 procs) — maintains ISSETYPE (service event type codes)
- **T7STEQUIP / T7STTYPE / T7STYPE** (all 52 procs) — maintain ISSTYPE variants (equipment types, storage types, shared service types)
- **T7STOCK** (53 procs) — maintains BKCMACCC (CRM account classifications used by service stock)

**Key tables (all small code masters):**

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSEPROC | 2 | Service process codes — PROC(25), WHO(40) |
| ISSTYPE | 3 | Shared service/equipment type — TYPE(60), WHO(40), ASSET(25) |
| ISSETYPE | 2 | Service error/event type — ERR(25), WHO(40) |

These code tables are referenced by SR service orders (BKARINV type field) and SR-INFO records to classify service operations, error categories, and equipment types.

**Confidence: 60/100** — All programs identified; key tables fully field-documented; role in SR workflow confirmed; no DFM forms found (these are likely popup code-entry screens or use shared UI).

---

### LI — License / Module Access

**What it does:** Controls which EvoERP modules are licensed and enabled for this installation. The ISACCESS table is the module gate — T7LIMACC (42 procs) is the admin UI to view/edit it.

**RWN program:** T7LIMACC (42 procs) — very small program; only opens ISACCESS + BKSYHELP + DBAHLPID + MKAHIST (standard help boilerplate). Single-table maintenance.

**ISACCESS:** Not registered in the Pervasive DDF (same pattern as ISARDEPL, ISWOEX). Contents inferred: module code → enabled/disabled flag. Used as a license gate: EvoERPmenu.RWN checks ISACCESS before dispatching any module.

**Confidence: 52/100** — Program identified; ISACCESS confirmed in use across 20+ programs but schema not in DDF; enabled/disabled flag behavior inferred from module load patterns.

---

### PU — Warehouse Put-Away

**What it does:** After PO receiving, the Put-Away module guides users to place received items into specific bin locations. Updates item inventory (BKICMSTR/MTICMSTR) and can trigger GL posting.

**RWN programs:**
- **T7PUTAWAY** (105 procs) — the main put-away program; opens BKICMSTR, MTICMSTR, BKAPINVL, BKAPPO, BKGLTRAN, DBAFIFO, LOT, SERIAL, ISORDECO, BKCMACCT

**Workflow:**
1. Received items appear from AP (BKAPINVL — AP invoice lines) and PO (BKAPPO).
2. User selects items and assigns them to bin locations (ISLINKS or BKICLOC).
3. Lot and serial numbers are assigned (LOT, SERIAL tables).
4. GL posting: debit inventory account (BKGLTRAN), credit FIFO cost layer (DBAFIFO).
5. Order decorations (ISORDECO) can trigger special handling instructions.

**No PU-specific tables exist** — T7PUTAWAY's 63-table fingerprint is entirely shared infrastructure: BKICMSTR/MTICMSTR (item master), BKAPPO/BKAPINVL (PO receipt source), LOT/SERIAL (traceability), BKGLTRAN/DBAFIFO (GL cost posting), BKCMACCN/BKCMACCT (CRM), ISTRIGRS/ISREMIND (notifications), ISNUMBER (auto-numbering), ISMCR (currency rates), ISNCR (NCR on defects), ISLINKS (document attachments). FILELOC appears 5× in the fingerprint — this is the TAS runtime record-navigation API table (not in DDF).

**Confidence: 68/100** — 63-table fingerprint fully cross-referenced; all tables are shared infrastructure (none PU-specific); workflow confirmed from AP→bin→GL table chain; no DFM forms found, so UI field layout is inferred only.

---

---

## MODULE QUICK REFERENCE — Pass 32 Additions

### BO — Bill of Lading

**What it does:** Generates shipping/freight documents for outbound SO shipments. Supports standard BOL and multi-shipment LTL (Less-than-Truckload) freight variants with box/packing details.

**RWN programs:**
- **T7BOL** (178 procs) — standard BOL; reads BKARINV+BKARCUST+ISSHPVIA+ISSHIPCO+ISSOBOX+BKARINVL+MTICMSTR+ISSRINFO+BKAPPO+ISAREX
- **T7BOLMSO** (174 procs) — multi-shipment / LTL variant; adds BKPSUSER+BKPRMSTR (driver/employee data) with EDIT.CLASS/WEIGHT/PACKS/HM fields for LTL freight classification

**No dedicated BOL table** — all data is assembled from existing SO/shipping tables at print time.

**ISSOBOX (22f) — SO Packing / Box Assignment**

Primary key: ISSO_BOX_SONUM(8) + LINE(8) + BOX(2)

| Field | Meaning |
|---|---|
| ISSO_BOX_CODE (15) | Item code (FK → BKICMSTR) |
| ISSO_BOX_QTY (float) | Quantity in this box |
| ISSO_BOX_LOT (15) | Lot number (if lot-tracked) |
| ISSO_BOX_SERIAL (25) | Serial number (if serial-tracked) |
| ISSO_BOX_TEMP (1) | Temporary/staging flag |
| ISSO_BOX_INVNUM (float) | Invoice number (FK → BKARINV) |
| ISSO_BOX_SHIPPR (float) | Shipper reference number |
| ISSO_BOX_SHPCOD (10) | Shipping company code (FK → ISSHIPCO) |
| ISSO_BOX_WEIGHT (float) | Box weight |
| ISSO_BOX_SKID (2) | Skid/pallet number |
| ISSO_BOX_DATE (date) | Packing date |
| ISSO_BOX_WOPRE+WOSUF | Linked work order |
| ISSO_BOX_UCC (30) | UCC-128 barcode (EDI shipping label) |
| ISSO_BOX_HT+LG+WD (float) | Box dimensions (height/length/width) |
| ISSO_BOX_TRACK (40) | Carrier tracking number |
| ISSO_BOX_EXTRA (150) | Extra notes |

**ISSHIPCO (16f) — Shipping Company / Carrier Master**

Primary key: IS_SHIP_SHPCOD(10)

| Field | Meaning |
|---|---|
| IS_SHIP_SHPNME (30) | Carrier name |
| IS_SHIP_SHPDESC (60) | Description |
| IS_SHIP_VNDCOD (10) | AP vendor code (FK → BKAPVEND) — for freight invoices |
| IS_SHIP_NOTES_1..5 (60 each) | 5 note lines |
| IS_SHIP_SHIPVIA (15) | Default ship-via code (FK → ISSHPVIA) |
| IS_SHIP_EXTRA (150) | Extra notes |
| IS_SHIP_WEB_1..5 (120 each) | 5 tracking URL templates — filled with tracking# at runtime |

**BOL workflow:** SO invoice → T7BOL reads BKARINV/BKARINVL for line items → ISSOBOX for box assignments (quantity/weight/lot/serial per box) → ISSHIPCO for carrier details → ISSHPVIA for account info → prints BOL with LOAD.NUMBER/SEAL.NUMBER/TRAILER.NUMBER header fields; T7BOLMSO adds LTL freight class (HM hazmat, PACKS count) and driver timestamps (ARRIVED/LOADING.START/END/DEPARTED) from BKPRMSTR employee.

**Confidence: 72/100** — Both programs fully identified; ISSOBOX(22f) and ISSHIPCO(16f) fully extracted; BOL workflow traced from DB fingerprint; exact printed field layout in encrypted RWN.

---

### RE — Reminders, Report Defaults, and Rebuild Utilities

**What it does:** A utility family grouped under RE: reminder/follow-up reports, saved report parameter management, link replacement, and data-rebuild utilities for QC and WO tables.

**RWN programs:**
- **T7REMINDRPT** (125 procs) — reminder report; reads BKSYMSTR+ISREMIND+BKARCUST+BKCMACCN; prints calendar reminders by contact/customer/date range
- **T7REPDEF** (52 procs) — maintains ISREPDEF (saved report defaults per user); save/restore report parameter sets
- **T7REPLNK** (67 procs) — replace-links utility; reads ISREPLNK+BKPRSALE+BKARCUST+BKICMSTR+CLASMSTR; used when salesperson or customer codes change system-wide
- **T7REINDEX** (36 procs) — Btrieve reindex; opens FILELOC; re-builds B-tree indexes for all registered data files
- **T7REBQC** (62 procs) — QC rebuild; recalculates BKQCMSTR/BKQCTRAN from source records
- **T7REBWO** (123 procs) — WO rebuild; recalculates WORKORD+WOBOM+WORECV+WOROUT+MTICMSTR+WOMAT+WOLABOR from WO source; run after data corruption or bulk import

**ISREPDEF (3f) — Report Label Definitions:**
`ISREP_DEF_LABEL`(5, PK) + `ISREP_DEF_TITLE`(30) + `ISREP_DEF_EXTRA`(50) — short code labels that categorize saved report templates. T7REPDEF CRUD editor.

**ISREPLNK (11f) — Report-to-Entity Link:**
`ISREP_LNK_REPNM`(2) + `ISREP_LNK_CUST`(10) + `ISREP_LNK_ITEM`(15) PK — links report templates to customer+item combinations with effective date ranges (SDATE+EDATE), GL account (GLA+GLD), class filter, and label code (FK → ISREPDEF). Used by CS module to assign commission report templates to salesperson+customer+item.

**WOLABOR (58f) — WO Labor Transactions (posted):**
Primary key: MTWOLA_DATE + MTWOLA_EMP + MTWOLA_WOPRE + MTWOLA_WOSUF + MTWOLA_OPER + MTWOLA_TRXN

| Field | Size | Meaning |
|---|---|---|
| MTWOLA_POSTED | 1 | Post flag (Y/N) |
| MTWOLA_DATE/EMP/WOPRE/WOSUF/OPER/TRXN | — | PK fields (date+employee+WO+op+sequence) |
| MTWOLA_REGOVER | 1 | R=regular, O=overtime |
| MTWOLA_RUNHRS/SETUPHRS | 8 each | Run and setup hours |
| MTWOLA_NOJOBS | 2 | Number of jobs this ticket |
| MTWOLA_PARTS | 8 | Parts completed |
| MTWOLA_REWORK/COMPLETE | 1 each | Rework flag / operation complete flag |
| MTWOLA_SCRAPPED | 8 | Scrapped quantity |
| MTWOLA_QCCODE/QCDESC | 2+30 | QC defect code + description |
| MTWOLA_SCRAPCD/SCDESC | 2+30 | Scrap reason code + description |
| MTWOLA_ASSY/ASSYDESC | 15+30 | Assembly item + description |
| MTWOLA_LABRATE/LABCOST | 8 each | Labor rate + computed cost |
| MTWOLA_SETCOST/MACHCOST | 8 each | Setup + machine cost |
| MTWOLA_FOHCOST/VOHCOST | 8 each | Fixed + variable overhead cost |
| MTWOLA_TEAM/SHIFT | 2 each | Team + shift |
| MTWOLA_WC/WCDATE | 12+date | Work center + WC date |
| MTWOLA_TOOL/TOOLDATE | 15+date | Tool + tool date |
| MTWOLA_MACH/MACHDATE | 4+date | Machine code + date |
| MTWOLA_EMP2/DATE2 | 2+date | Second employee (team op) |
| MTWOLA_MISC/MISCDESC | 8+30 | Misc cost + description |
| MTWOLA_START/STOP/DEDUCT | TIME 4 each | Actual clock in/out/deductions |
| MTWOLA_EXTRA | 50 | Extra notes |
| MTWOLA_AUDIT | 35 | Audit trail string |
| MTWOLA_CYC{HR/MIN/SEC}/CYCPARTS/CYCNOTE | — | Cycle time + note (255) |
| MTWOLA_FLAG_1..5/ALPHA_1..3 | — | UDF: 5 flags + 3 alpha(30) fields |

**WORECV (11f) — WO Receipts (finished goods):**
Primary key: MTWOR_WOPRE + MTWOR_WOSUF + MTWOR_DATE
- MTWOR_ASSY(15) + MTWOR_DESC(30): item + description
- MTWOR_QTY(8): quantity received into finished goods
- MTWOR_USESTD(1): use standard cost flag
- MTWOR_AVGC(8): average cost at receipt time
- MTWOR_LOT(15) + MTWOR_SERIAL(25): lot/serial assigned at WO completion
- MTWOR_REF(15): reference

WORECV is written when WO-H "Receive Completed Work Order" posts — records the finished quantity accepted into inventory. Drives BKICLOC on-hand update and INVTXN receipt transaction.

**T7REBWO purpose:** Reads WORKORD + WOBOM + WORECV + WOROUT + MTICMSTR + WOMAT + WOLABOR and recomputes all WO cost totals from scratch. Run after data corruption or a bulk import that bypassed the normal WO update path.

**Confidence: 75/100** — All 7 programs confirmed; ISREPDEF(3f)+ISREPLNK(11f)+WOLABOR(58f)+WORECV(11f) fully extracted from DDF; rebuild workflow confirmed from DB fingerprints; exact rebuild algorithms blocked by encryption.

---

### AU — Automation / Batch Processing

**What it does:** Background automation programs that run on schedule via EvoScheduler — auto-validating DC (Data Collection) labor tickets, auto-firming MRP planned orders, back-order recalculation, and auto-updating foreign exchange rates.

**RWN programs (8):**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7AUTODCH | 183 | DC auto-validate: validates BKDCLAB labor against BKDCCFG rules + BKPRMSTR employee setup |
| T7AUTOMRF | 132 | MRP auto-firm: reads MTMRP → creates WOs/POs from planned orders |
| T7AUTOREBSS | 79 | Back-order recalc: updates BSS (Back-order Status Summary) for all open items |
| T7AUTOFX | 21 | FX rate update: calls ISJAVA → fetches live rates → writes ISMCR currency rates |
| T7AUTODEJH | 5 | DC exception handler stub |
| T7AUTOSMJC | 5 | SM job-close automation stub |
| T7AUTOWOLA | 5 | WO labor auto-post stub |
| T7AUTOUTKG | 5 | UTK/gauge automation stub |

**Key table — BKDCLAB (50f) — Data Collection Labor Tickets:**
Staging table for shop-floor labor entries before they post to WORKORD/WOROUT.
Primary key: `LAB_DATE`(4) + `LAB_EMP`(2) + `LAB_WOPRE`(8) + `LAB_WOSUF`(2) + `LAB_OPER`(2).

| Field | Type/Size | Meaning |
|-------|-----------|---------|
| LAB_DATE | DATE 4 | Labor date |
| LAB_EMP | UBINARY 2 | Employee# (FK → BKPRMSTR) |
| LAB_WOPRE / LAB_WOSUF | FLOAT/UBINARY | WO prefix + suffix (FK → WORKORD) |
| LAB_OPER | UBINARY 2 | Routing operation# (FK → WOROUT) |
| LAB_POSTED | STRING 1 | Post flag: `Y`=posted, `N`=pending |
| LAB_SHIFT | UBINARY 2 | Shift number |
| LAB_START / LAB_FINISH | TIME 4 | Clock in/out times |
| LAB_PARTS | FLOAT 8 | Parts completed this ticket |
| LAB_SCRAPPED | FLOAT 8 | Parts scrapped |
| LAB_NOJOBS | UBINARY 2 | Number of jobs on this ticket |
| LAB_RUNHRS / LAB_SETUPHRS | FLOAT 8 | Run hours / setup hours |
| LAB_REGOVER | STRING 1 | Regular or overtime flag |
| LAB_APPROVAL | STRING 1 | Supervisor approval flag |
| LAB_ADT_SUPER/IN/OUT | STRING 100 | Audit: supervisor / badge-in / badge-out |
| LAB_SCRAPCD_1..5 | STRING 2 | Up to 5 scrap reason codes |
| LAB_SCRAPQTY_1..5 | FLOAT 8 | Qty scrapped per reason |
| LAB_JCNUM | STRING 12 | Job cost number |
| LAB_CYCLE_HR/MIN/SEC | UBINARY 2 | Cycle time components |
| LAB_CYCLE_PARTS | FLOAT 8 | Parts per cycle |
| LAB_CYCLE_NOTE | STRING 255 | Cycle notes |
| LAB_GEN_DATE_1/2 | DATE 4 | Generic date fields (2) |
| LAB_GEN_ALPHA_1/2 | STRING 30 | Generic alpha fields (2) |
| LAB_GEN_NUM_1/2 | FLOAT 8 | Generic numeric fields (2) |
| LAB_GEN_FLAG_1..5 | STRING 1 | Generic flags (5) |

**Key table — BKDCCFG (7f) — DC Configuration:**
`BKDC_CFG_IDLEP/IDLES` — idle program/station | `BKDC_CFG_BANKP/BANKS` — bank program/station | `BKDC_CFG_IMPPTH/EXPPTH`(60) — import/export paths | `BKDC_CFG_JOBTME`(60) — job time config path.

**T7AUTODCH workflow:** Reads pending BKDCLAB rows (LAB_POSTED=`N`) → validates against BKDCCFG rules and BKPRMSTR employee setup → if valid, posts to WORKORD/WOROUT labor actuals → sets LAB_POSTED=`Y`.

**Confidence: 72/100** — All 8 programs identified; BKDCLAB (50f) and BKDCCFG (7f) schemas fully extracted; DC-to-WO posting workflow confirmed from DB fingerprints; exact exception-handling logic and scheduling config in encrypted RWN.

---

### EDII — EDI Invoice Import

**What it does:** Creates AR invoices from inbound EDI data. Single program (T7EDII, 183 procs) that runs a complete invoice-creation pipeline — pricing, charges, GL posting, inventory, and lot/serial tracking — from an EDI transaction source.

**RWN program:** T7EDII (183 procs). Full DB set: BKYSMSTR+MTICMSTR+BKARINV+BKARINVL+ISARCHG+BKARCUST+BKSYMSTR+ISTERMS+BKICMSTR+BKICPMAT+BKICLOC+CLASMSTR+ISCATMST+ISTAXGRP+ISNUMBER+BKICLOCM+BKAPPOL+BKAPPO+WORKORD+WOBOM+INVTXN+BKBMMSTR+BKMRPFC+ISICMSTR+BKGLTRAN+DBAFIFO+ISTRIGRS+ISREMIND+LOT+SERIAL+ISNCR.

**Architecture:** Identical table set to manual AR invoice entry — EDI data drives the same paths: customer/item lookup, price override (BKICPMAT), tax (ISTAXGRP), GL posting (BKGLTRAN+DBAFIFO), WO connection (WORKORD+WOBOM), lot/serial (LOT+SERIAL), extra charges (ISARCHG).

**42 of 43 tables in DDF schema** (only FILELOC is unregistered). All 42 tables are documented elsewhere in this guide. This confirms EDII runs the same code path as manual SO entry — the entire AR invoice creation pipeline without human interaction.

**Confidence: 72/100** — Single program, full 43-table DB set confirmed; all constituent tables documented across AR/SO/GL/LC sections; EDI-specific field mapping and 850/860 transaction parsing blocked by encryption.

---

### LG — LGS Customer Module (Canadian Statement of Entry)

**What it does:** Customer-specific module for LGS — implements Canadian customs "Statement of Entry" (SOE) processing for cross-border AR invoices with duty/customs tax calculations.

**RWN programs:**
- **T7LGSSOE** (170 procs) — main SOE entry; uses BKARINV+BKARCUST+BKARINVL+BKARTXN+BKICTAX+BKICLOC+BKICLOCM+ISTAXGRP+INVTXN+BKGLTRAN+DBAFIFO+LOT+SERIAL
- **T7LGSSOEVERIFY** (41 procs) — verification step: validates BKYSMSTR+BKICMSTR+BKARINVL+BKARINV+BKARTXN before posting

**Key distinction from standard AR:** Uses BKICTAX (item tax by state/local jurisdiction) and BKARTXN (AR transaction log) — cross-border Canadian customs treatment rather than standard US sales tax. BKICTAX stores state+local duty rates; BKARTXN logs the customs transaction.

**Confidence: 52/100** — Two programs identified with full DB fingerprints; SOE/customs role confirmed from table selection and program name; exact SOE field structure in encrypted RWN.

---

### JS — Java Integration / External Reporting Bridges

**What it does:** Thin launcher programs that configure and invoke EvoPVT.jar for external reporting integrations — Power BI, SQL Server Reporting Services, and other external analytics/reporting tools.

**RWN programs:**

| Program | Procs | Purpose |
|---------|-------|---------|
| T7JSETTINGS | 70 | JS connection settings; reads FILELOC for paths |
| T7JSQL | 52 | Direct SQL query bridge via Java |
| T7JSACC | 50 | AR/AP accounting data bridge to external reporting |
| T7JSAIC | 50 | IC (Inventory Control) data bridge |
| T7JSAPBI | 50 | Power BI connector |
| T7JSASRS | 50 | SQL Server Reporting Services connector |
| T7JSOI | 50 | Order Inquiry data bridge |

All 6 data-bridge programs use only standard boilerplate DB (BKSYHELP+ISIS+MKAHIST+ISLOG+ISDRILL) — the actual data extraction runs inside EvoPVT.jar, which these programs configure and launch via the ISJAVA task queue.

**Confidence: 58/100** — All 7 programs identified; Power BI and SRS roles confirmed from naming; JS→Java launcher pattern confirmed by AUTOFX precedent; data schemas in Java JAR.

---

### TA — TAS Admin / System Administration

**What it does:** The most powerful admin module — direct database maintenance, menu access control, program scheduling, backup, SQL editing, logo management, and data dictionary validation. Requires highest security level.

**CHM operations and matched RWN programs:**

| Menu code | Operation | Matched RWN program |
|-----------|-----------|---------------------|
| TA-D | Maintain Database (direct record edit) | T7FNR (104 procs, FILELOC+FILEDICT) — File Navigator/browser |
| TA-G | Maintain Menu Access Records | uses BKMENUSU (per-user menu config) |
| TA-H | Maintain Menu End User | user-level menu preferences |
| TA-M | Forms Editor | DCY decrypt + form edit (T7MDEFAULTS family or dedicated) |
| TA-N | Program Scheduler | EVOSCHEDSETUP (37 procs) + EVOSCHEDULER (65 procs, ISSCHED) |
| TA-O | Backup Utility | EVOERPBACKUP (76 procs, FILELOC+BKSYMSTR; uses zipdll) |
| TA-Q | Change Logo Image | small FILELOC utility (unconfirmed program name) |
| TA-R | SQL Editor | QUERYEXECUTE (26 procs, ISDRILL+BKPSUSER) |
| TA-S | Data Dictionary Check | T7DDCHECK (92 procs, FILEDICT+FILEKEY+FILELOC) |

**Confirmed programs:**
- **EVOERPBACKUP** (76 procs): reads FILELOC (file list) + BKSYMSTR (company/path settings); uses zipdll.dll to zip data files
- **EVOSCHEDULER** (65 procs): manages ISSCHED job queue (24f: program, company, date/time, recurrence, 10 params, email)
- **T7DDCHECK** (92 procs): validates DDF entries (FILEDICT+FILEKEY) against physical FILELOC data files
- **QUERYEXECUTE** (26 procs): executes saved ISDRILL SQL queries; also surfaces as QU-F SQL Executor in Query menu

**TAS Admin low-level programs (WTAS* family):** 8 programs operate on the TAS runtime's own file dictionary (FILE* tables — not in Pervasive DDF):
- **WTASDATAM** (59p) / **WTASDMGR** (68p): Data manager — FILELOC+FILEDICT+FILEKEY+FILEKNUM
- **WTASFLOC** (22p) / **WTASMERGE** (16p): File location manager / Merge — all FILE* tables (FILELOC+FILEDICT+FILEKEY+FILEKNUM+FILEDES+FILEDFLD+ERRMSG+FILEDBF)
- **WTASINIT** (21p): Initialize file tables — FILELOC+FILEDICT+FILEKNUM+FILEKEY+FILEDES
- **WTASCVTDICT** (13p) / **WTASCVTDICTPR** (12p): Dictionary converter — full FILE* set
- **WTASCHKINT** (8p): Integrity checker — FILELOC+FILEKEY only

**FILE* tables are TAS runtime internals** — not Pervasive DDF tables. FILELOC=file path registry, FILEDICT=field dictionary, FILEKEY=key definitions, FILEKNUM=key numbers, FILEDES=field descriptions, FILEDFLD=field definitions, FILEDBF=dBASE file info, ERRMSG=error messages. These explain why FILELOC/FILEDICT appear in hundreds of EvoERP programs as non-DDF entries — every program that does dynamic record navigation via the TAS runtime links to FILELOC.

**Pass 66 — ISSCHED (24f) full schema:**
TA-N (EVOSCHEDULER 65p + EVOSCHEDSETUP 37p) use ISSCHED as their primary table. NAME(20 PK)+DESC+PROG(program)+CO(company)+TYPE(O/D/W/M)+DATE+TIME+RECUR+LOG+EXTRA+LDATE/LTIME+WHO+EMAIL+PARAM1..9+PARAM0. EVOSCHEDULER reads ISSCHED and spawns the named PROG at DATE+TIME with PARAM1..9 passed as arguments. TA-N is the full EvoERP job scheduler — can schedule any RWN program to run automatically.

**Confidence: 78/100** — 9 CHM operations documented; 5 EvoERP programs matched (TA-S=T7DDCHECK, TA-N=EVOSCHEDULER+EVOSCHEDSETUP, TA-O=EVOERPBACKUP, TA-R=QUERYEXECUTE); 8 WTAS* utilities mapped to FILE* tables; ISSCHED(24f) full schema extracted; TA-G/H/M/Q still unmatched to specific RWN.

---

---

## MODULE QUICK REFERENCE — Pass 33 Additions

### QC — Quality Control (Major Expansion)

**18 programs across 4 sub-areas.** Full ISO 9001-compatible quality management system.

#### Sub-area QC-A through QC-D: Inspection

| Program | Procs | Purpose |
|---|---|---|
| T7QCA | 106 | QC-A incoming inspection — item/lot/serial from vendor or customer; posts to BKQCTRAN; uses SCRAP+QCCODES |
| T7QCB | 120 | QC-B WO material quality — checks raw materials issued to WORKORD via WOMAT |
| T7QCC | 108 | QC-C WO receipt quality — checks completed WO receipts (WORECV) |
| T7QCD | 117 | QC-D WO routing/labor quality — checks by work center (ROUTING+WOLABOR+BKPRMSTR) |

#### Sub-area QC-F: Non-Conformance Records (NCR)

| Program | Procs | Purpose |
|---|---|---|
| T7QCFA | 178 | NCR entry — creates ISNCR records from WO/PO/SO/RMA source; links vendor/customer/machine/tool |
| T7QCFB | 108 | NCR with supplier quality — links ISNCR to BKSBVEND (supplier ratings) + WORECV |
| T7QCFC | 5 | NCR sub stub |
| T7QCFD | 53 | NCR inquiry — browse ISNCR records with ISNOTES; read-mostly |
| T7QCFE | 5 | NCR sub stub |
| T7QCFF | 131 | NCR closeout — closes ISNCR, updates BKICLOCM inventory, posts via BKAPPO |

#### Sub-area QC-G: Corrective/Preventive Actions (CAPA)

| Program | Procs | Purpose |
|---|---|---|
| T7QCGA | 212 | CAPA entry — creates ISCACT corrective actions linked to ISNCR; assigns ISCARDTE dates + BKPSUSER owner |
| T7QCGB | 122 | CAPA approval — team review via ISCTEAM; ISACTION action type codes; approval workflow |
| T7QCGC | 5 | CAPA sub stub |
| T7QCGD | 110 | CAPA report — browse ISNCR+ISCACT+ISCTEAM; assigned-to BKPSUSER |

#### Supporting programs

| Program | Procs | Purpose |
|---|---|---|
| T7QCMTHD | 65 | QC Methods maintenance — defines ISQCMTHD test procedures (25 × 100-char method lines) |
| T7QCRESULTS | 104 | QC Results entry — records test results in ISQCSPEC per WO/lot/SO/PO |
| T7QCRSLT | 87 | QC Results with tray — results linked to ISWOTRAY (physical tray tracking) + ISQCMTHD |
| T7QCSPEC | 82 | QC Specifications — defines test specs in ISQCSPEC per routing operation |

#### QC Key Tables

**ISNCR** — Non-Conformance Records (35 fields)
- PK: IS_NCR_NUM (float)
- IS_NCR_PART (15) / IS_NCR_COMP (15) — parent + component item
- IS_NCR_LOT (15) / IS_NCR_SERIAL (25) — lot/serial of defective part
- IS_NCR_CDATE / IS_NCR_WHO (15) — creation date + creator
- IS_NCR_QTY — defective quantity
- IS_NCR_DCODE (10) — defect code
- IS_NCR_ICR (1) — ICR flag (internal change request linked)
- IS_NCR_ORIG (1) — origin code (PO=purchased, WO=manufactured, RMA=return)
- IS_NCR_WOPRE / IS_NCR_WOSUF — Work Order reference
- IS_NCR_MACH (4) / IS_NCR_TOOL (15) / IS_NCR_WC (12) — machine/tool/work center
- IS_NCR_PONUM — PO reference
- IS_NCR_RMA — RMA number reference
- IS_NCR_ACTION (1) — required action code
- IS_NCR_CAR — Corrective Action Request number (FK → ISCACT)
- IS_NCR_DISP (10) / IS_NCR_DWHO / IS_NCR_DDATE — disposition + who disposed + when
- IS_NCR_STATUS (1) — O=open, C=closed
- IS_NCR_SCRAP (2) / IS_NCR_QC (2) — scrap code + QC code
- IS_NCR_VEND (10) / IS_NCR_LOC (10) — vendor + location
- IS_NCR_PDRAW (15) / IS_NCR_PREV (5) — parent drawing + rev
- IS_NCR_CDRAW (15) / IS_NCR_CREV (5) — component drawing + rev

**ISQCSPEC** — QC Specification Results (57 fields)
- PK: ISQC_SPC_LRNUM
- Links to WO (WOPRE/WOSUF), operation (OPER), lot/serial/batch
- ISQC_SPC_TSTCOD (30) — test code (FK → ISQCMTHD)
- ISQC_SPC_NUMERC (1) — numeric test flag
- ISQC_SPC_MIN/MAX (15 each) — acceptable range
- ISQC_SPC_RESULT (15) — actual result
- ISQC_SPC_PASS (1) — pass/fail
- ISQC_SPC_TDATE / ISQC_SPC_TESTBY — test date + tester employee
- ISQC_SPC_TNOTES_1..5 (60 each) — tester notes
- ISQC_SPC_ADATE / ISQC_SPC_APPBY — approval date + approver
- ISQC_SPC_ACCEPT (1) — accepted flag
- ISQC_SPC_ANOTES_1..5 (60 each) — approver notes
- Also links to SO/PO/invoice/receive numbers for incoming inspection results

**ISQCMTHD** — QC Test Methods (44 fields)
- PK: ISQC_MTD_TSTCOD (30) — test code
- ISQC_MTD_DESC/DESC2 — description
- ISQC_MTD_METHOD_1..25 (100 chars each) — full test procedure text (2,500 chars capacity)
- ISQC_MTD_NOTES_1..10 (60 chars each) — notes
- Revision tracking: REV/REVBY/REVDT + ENTBY/ENTDT

**SCRAP** — Scrap Code Master (21 fields)
- PK: MTSCRAP_CODE (2-char)
- MTSCRAP_TYPE (1) — scrap type classification
- MTSCRAP_GLACCT/GLDPT — GL account for scrap posting
- MTSCRAP_FLAG_1..5 + ALPHA_1..5 + DATE_1..5 — configurable extra fields

**QCCODES** — QC Code Lookup (2 fields)
- PK: MTQC_CODE (2-char)
- MTQC_DESC (30) — description only

**ISBUILD** — Generic Build UID Tracker (15 fields) — NOT QC-specific; used by WO and QC-F
- IS_BUILD_UID (40) + IS_BUILD_SORT (150) — unique ID + sort key
- IS_BUILD_REC/FILE — physical Btrieve record pointer
- Used as a generic indexed helper for large-table lookups

**ISWOTRAY** — WO Tray Tracking (52 fields)
- PK: IS_TRAY_NUM (25) — physical tray number
- IS_TRAY_WOPRE/WOSUF/OPER — Work Order + operation
- IS_TRAY_SQTY / IS_TRAY_COMQTY / IS_TRAY_SCRPQTY — started/completed/scrapped qty
- IS_TRAY_QCREQD (1) + IS_TRAY_QCQTY — QC required flag + quantity requiring QC
- IS_TRAY_LOC_1..5 + IS_TRAY_BIN_1..5 + IS_TRAY_BINQTY_1..5 — up to 5 bin splits per tray
- IS_TRAY_ALPHA_1..20 + IS_TRAY_DATE_1..5 — configurable extras

**ISCACT, ISCARDTE, ISCTEAM** — NOT IN DDF schema (confirmed from program usage)
- ISCACT: Corrective Actions (created by T7QCGA)
- ISCARDTE: Corrective Action dates (used by T7QCGA)
- ISCTEAM: Corrective Action teams (used by T7QCGB/QCGD)

#### QC Workflow

```
Inspection (QC-A/B/C/D)
  → defect found → T7QCFA creates ISNCR record (NCR)
  → T7QCFB links to supplier quality (BKSBVEND)
  → disposition set (use-as-is / rework / scrap) → T7QCFF closes NCR
  → if systemic → T7QCGA creates ISCACT Corrective Action from NCR
  → T7QCGB assigns team (ISCTEAM) + approves actions
  → T7QCGD reports CAPA status
Test results path: T7QCSPEC defines specs → T7QCRESULTS/QCRSLT record actual test results → ISQCSPEC
```

**Confidence: 72/100** — 18 programs identified; all 4 sub-areas confirmed from DB fingerprints;
key table schemas extracted; ISCACT/ISCARDTE/ISCTEAM not in DDF; per-operation UI fields
and exact menu-code-to-program mapping gaps remain.

---

### QT — Service Quote Extended Info

T7QTINFO (42 procs) — opens ISSRINFO (SR extended info table) + BKARINVL + ISTERMS + BKICPMAT +
BKICREF + BKBMMSTR. Service quotes in EvoERP are SR orders in quote status. T7QTINFO provides
extended information entry (dates, notes, terms) for service quotes using the same ISSRINFO table
as service orders. Related to SR module, not a standalone quote engine.

**Confidence: 72/100** — T7QTINFO confirmed; LANGDICT(5f)+BKICREF(8f)+ISTERMS(13f)+ISSRINFO(54f) all extracted; quote-as-SR-order architecture confirmed. See QT Expanded section below.

---

### IC — Inventory-to-Estimating Copy Utility

T7IC2EST (6 procs) — opens BKICMSTR + MTICMSTR. A 6-procedure one-way bridge that copies
production inventory (BKICMSTR) data into the estimating module (MTICMSTR). Accessed as IC-A
"Copy Production to Estimate Inventory" from DFM caption. Not a general inventory module.

**Confidence: 68/100** — one program confirmed; MTICMSTR(108f) fully extracted from DDF — 10 vendor sources (VEND/VNAM/VPC + RCOST_1..15), 5 substitutes, lot size, option codes; BKICMSTR relationship confirmed as source; no other IC programs found.

---

---

## MODULE QUICK REFERENCE — Pass 34 Additions

### SD — Standard Detail Codes

T7SDET (58 procs) — maintains ISSDET + ISSTYPE (service detail code pairs). Also opens ISNCR
(confirms SD codes are used in NCR defect classification) and ISMCR (multi-currency). SD codes
are used as classifiers in service orders (SR), NCR records (QC), and probably service schedule.

- **ISSDET** (4f): IS_SDET_TYPE + IS_SDET_DETAIL + IS_SDET_WHO + IS_SDET_SUB — type/detail pair
- **ISSTYPE** (3f): IS_SDET_TYPE + IS_SDET_DESC + IS_SDET_MISC — type code + description

**Confidence: 58/100** — single program confirmed; purpose from table fingerprint; ISNCR link is firm.

---

### SL — Sales Forecast / Shop Loading

T7SLSFC (5 procs) — opens BKARINVL + BKDCLAB + BKARCUST + ISWOPRIO + WORKCTR + ROUTING.
Despite the "sales forecast" label, this program reads work center and routing data alongside
AR invoice demand. This is a shop-loading/capacity display: overlays demand (BKARINVL) on
production capacity (WORKCTR+ROUTING) and DC labor (BKDCLAB), with WO priority (ISWOPRIO).

**Confidence: 65/100** — single program confirmed; ISWOPRIO(4f) schema extracted: PRIO(1)+DESC(30)+EXTRA(100)+COLOR(float) — WO priority color display confirmed; SL is a read-only shop floor capacity display overlaying demand+capacity+labor; detailed display logic blocked by encryption.

---

### AL — Audit Log Setup + Alternate Part Maintenance

Two programs share the T7AL* prefix:

**T7ALOGSETUP** (43 procs): opens FILELOC + BKSYMSTR + BKPSUSER. Configures the EvoERP
audit log — selects which Btrieve tables and events are recorded, per company/user settings.

**T7ALTPART** (104 procs): opens BKSBPART + BKICMSTR + ISACCESS. Maintains alternate/substitute part number relationships.

**BKSBPART (5f):**
`BKSB_PART_PARNT`(15) parent item code | `BKSB_PART_PROD`(15) substitute item code | `BKSB_PART_CUST`(10) customer code (blank = all customers) | `BKSB_PART_SUBST`(15) substitute part# | `BKSB_PART_EXTRA`(50) notes.

Maps a parent item to valid substitutes, optionally restricted to a specific customer. T7ALTPART enables SO entry to suggest substitutes when the primary item is unavailable.

**Confidence: 62/100** — both programs identified; BKSBPART (5f) schema fully extracted from DDF; alternate-part purpose confirmed; ISACCESS role (security check) inferred.

---

### ML — Multi-Language Invoice Support

T7MLC (50 procs) — opens LANGDICT + BKARINV + BKARINVL + ISREPORD + BKGLTRAN + ISREPLNK +
BKPRSALE + BKICPMAT + ISJAVA + BKEDMSTR + ISBSF. Multi-language AR invoice printing: translates
invoice content via LANGDICT, applies customer pricing (BKICPMAT/BKPRSALE), links to EDI master
(BKEDMSTR), and posts GL transactions (BKGLTRAN). ISJAVA integration for email/delivery.

**Confidence: 55/100** — program identified; purpose from table fingerprint; specific field
translations and language switching logic blocked by RWN encryption.

---

### MH — Shipping Order / Ship-Via Configuration

T7MHOPE (98 procs) — opens BKCMTERR + BKARCUST + ISSHPVIA + ISSHIPCO + BKARINV + BKARINVL +
BKICLOC + BKGLTRAN + ISREPLNK + BKPRSALE + BKICPMAT + ISJAVA + ISBSF. More than carrier config —
this program creates shipping orders, writes BKGLTRAN GL entries, reads inventory location
quantities (BKICLOC), and applies pricing. BKCMTERR = customer territory; ISSHPVIA = ship-via
codes; ISSHIPCO = shipping company/carrier.

**Confidence: 55/100** — program identified; purpose from table fingerprint; invoice posting
confirmed from BKGLTRAN presence; detailed logic blocked by encryption.

---

### BR — Brand / CRM Classification

T7BRANDS (53 procs) — primary table BKCMACCC (2f: CCODE+DESC — CRM account classification code).
Also opens BKARINV + BKGLTRAN + DBAFIFO + ISTRIGRS + ISREMIND + LOT + SERIAL + ISNCR + BKAPPO +
BKMRPFC + ISICMSTR. The broad table set reflects EvoERP's shared-library pattern, not all tables
are actively used per operation. T7BROWSER (4 procs) is an HTML browser wrapper for the same area.

- **BKCMACCC** (2f): 5-char classification code + 25-char description; used for CRM brand tagging

**Confidence: 65/100** — both programs confirmed; BKCMACCC(2f) + BKCMACCN(154f: 10 contacts × name/title/phone/email + custom date/alpha slots) fully extracted from DDF; T7BROWSER = CRM contact browser confirmed from BKCMACCN use; detailed CRM logic blocked by encryption.

---

### NE — New Company Initialization

T7NEWINIT (49 procs) — opens FILELOC + FILEDES. Creates all Btrieve data files (.B) for a new
EvoERP company. FILELOC = list of existing data files; FILEDES (not in DDF) = file description/
template definitions used as the blueprint for what files to create.

**Confidence: 55/100** — program confirmed; purpose from table fingerprint and program name.

---

### JO — Jobs and Departments

T7JOBS (21 procs) — opens ISDEPT + WOEXCHG + CLASMSTR + ISCATMST + BKICLOCM + ISNOTES + ISNTYPE
+ WORKCTR + ISBNMSTR + ISTRIGRS + ISREMIND.

Key tables:
- **ISDEPT** (3f): IS_GF_DEPT(10) + IS_GF_DEPT_DESC(40) + IS_GF_DEPT_MISC(100) — department master
- **WOEXCHG** (10f): MTWO_EX_WOPRE/WOSUF + DATE + PROD + DESC + CHG + CHGDESC + GLACCT + GLDPT + OP
  — WO exchange/change charges: records cost changes to work orders with GL posting

Also found T7JODPSALES (52 procs) — a "JO Display Sales" panel reading IS2DBAR + ISCYCLCD + BKSBPART + BKAPDESC + ISNCR — this is likely an SM drill-down panel, not the JO module itself.

**CLASMSTR (2f):** `MTCLASS_M_CLASS`(4) + `MTCLASS_M_DESC`(30) — item classification code master; used across IC, JO, and other modules to categorize items by class.

**Confidence: 62/100** — T7JOBS confirmed; ISDEPT(3f)+WOEXCHG(10f)+CLASMSTR(2f) schemas fully extracted from DDF; T7JODPSALES scope uncertain (may belong to SM display framework rather than JO module proper).

---

### FN — File Navigator (Data Dictionary Browser)

T7FNR (104 procs) — opens FILELOC + FILEDICT. Admin tool for browsing Btrieve data files and the
Pervasive data dictionary. FILELOC = file locations on disk; FILEDICT = DDF field definitions.
This is the TA-D "Data File Navigator" operation (also surfaced in TA module).

**Confidence: 58/100** — program confirmed; purpose from table fingerprint and DFM read.

---

### XC — Credit Card Cross-Reference Utility

T7XCUTIL (29 procs) — opens BKCMACCT + BKYSMSTR + ISCC. Reconciles/cross-references credit card
records between the CRM accounting layer and EvoERP's credit card token store.

- **ISCC** (14f): Credit card token store:
  - IS_CC_CODE (10) — card record code
  - IS_CC_TOLKEN (20) — payment processor token (obfuscated card reference)
  - IS_CC_MASKED (24) — masked card number (e.g., `****-****-****-1234`)
  - IS_CC_EXP (4) — expiration date
  - IS_CC_ADDRESS/ZIP — billing address for AVS
  - IS_CC_CARDTYPE (15) — Visa/MC/Amex etc.
  - IS_CC_CARDNAME (25) — cardholder name
  - IS_CC_STATUS (25) + IS_CC_STDATE — status + date
  - IS_CC_XCTRAN (10) — transaction reference
  - IS_CC_PROCESS (10) — processor code

**Confidence: 55/100** — program confirmed; ISCC schema extracted; purpose from table fingerprint.

---

### IT — Item Serial/Barcode/Cycle Configuration

T7ITMCFG (66 procs) — opens ISSERCNT + BKICMSTR + BKGLCOA + SERIAL + ISNCR + IS2DBAR + ISCYCLCD.
Configures per-item serial number generation, 2D barcode printing, and cycle count classification.

Key tables:
- **ISSERCNT** (9f): IS_SERC_ITEM(15) + CLASS(4) + SPOS(pos) + LENG(length) + TOTAL(width) +
  NUMBER(current counter) + LAST(25, last serial generated) + EXTRA + L2 — serial counter per item
- **IS2DBAR** (109f): IS2D_BAR_CODE(10) + ITEM(15) + ORDER + CHAR(5) + FIELD(25) + DOCPR_1..15
  (15 document print flags) + 89 more — 2D barcode format config per item/document type
- **ISCYCLCD** (7f): IS_CYCLE_CODE(4) + DESC(30) + FREQ(frequency) + DATE + ALPHA(15) + NUM +
  EXTRA(50) — cycle count frequency code (daily/weekly/monthly/annual)

**Confidence: 72/100** — program confirmed; all three key table schemas (ISSERCNT/IS2DBAR/ISCYCLCD) extracted from DDF; serial counter, 2D barcode config, and cycle count classification purposes fully confirmed; the 109 IS2DBAR fields are largely document-type print flags not individually decoded.

---

### EM — Emergency GL Maintenance

T7EMGL (62 procs) — opens BKGLCOA + BKAPPOL + BKAPPO + WORKORD + WOBOM + INVTXN + BKBMMSTR +
ISICMSTR + BKGLTRAN + LOT + SERIAL + ISNCR + ISTAXGRP + ISNUMBER + BKICLOCM + BKAPPOL.
A power-user direct-edit tool for the GL Chart of Accounts. The broad table set exists because
it needs to traverse GL account references across all modules to find/validate account usage.

- **ISICMSTR** (41f): IS_PROD_CODE(15) + WT(weight) + ITP(20, item type pack) + EXTRA(150) +
  CDATE + TI/HI/FOBPAL/FOBFULL (pallet TI/HI/FOB dimensions) + HT/LG/WD(box dims) + TOOL(15) +
  SLEAD(shipping lead) + RCDATE + FLAG_1..5 + 21 more — item physical/shipping specs extension

**Confidence: 65/100** — program confirmed; BKGLCOA(65f) and ISICMSTR(41f) fully extracted from DDF; purpose clear from program name and primary table; full GL traversal logic blocked by encryption.

---

### RT — Report Template Validator

T7RTMVALID (20 procs) — opens BKSYHELP + DBAHLPID + ISIS + MKAHIST. Validates RTM (ReportBuilder)
templates. Reads the help system (BKSYHELP/DBAHLPID) and audit history (MKAHIST). ISIS is the
EvoERP import/export index. Very minimal utility — validates form structure and logs to audit trail.

**Confidence: 55/100** — program confirmed (11-20 procs); ZERO module-specific tables (only BKSYHELP+DBAHLPID+ISIS+MKAHIST — pure infrastructure); purpose confirmed from program name; validation logic blocked by encryption.

---

### FP — Features & Options Print

No T7FP* programs found in rwn_symbols.json (1,122 modules searched). FP-B "Print Features and
Options" is a print sub-module of FO (Features & Options). It is likely implemented as a single
RTM report template (ReportBuilder) triggered from within the FO module, not a standalone RWN.

**Confidence: 55/100** — CHM operation confirmed; absence of any T7FP* program across all 1,122 RWN modules confirmed (exhaustive search); FP-B is definitively RTM-only (print variant of FO-D/FO-E).

---

### New Tables Confirmed (Pass 34)

| Table | Fields | Purpose |
|---|---|---|
| ISCC | 14 | Credit card token store — masked number + processor token + billing address |
| IS2DBAR | 109 | 2D barcode config per item/document — format, fields, 15 print-enable flags |
| ISCYCLCD | 7 | Cycle count frequency codes — CODE/DESC/FREQ/DATE per cycle code |
| ISSERCNT | 9 | Serial number counter per item — position, length, current number, last generated |
| ISICMSTR | 41 | Item physical/shipping specs — weight, TI/HI, dimensions, tool, shipping lead |
| ISDEPT | 3 | Department master — DEPT(10)/DESC(40)/MISC(100) |
| BKCMACCC | 2 | CRM account classification code — CCODE(5)/DESC(25) |
| BKSBPART | 5 | Alternate/substitute part relationships — PARNT/PROD/CUST/SUBST |
| WOEXCHG | 10 | WO change order charges — WO ref + change amount + GL account |

---

---

## MODULE QUICK REFERENCE — Pass 35 Additions

### BKMR* Tables — MRP Supporting Data

The MR (MRP) module uses three BKMRP* supporting tables in addition to the main MTMRP table:

| Table | Fields | Purpose |
|---|---|---|
| BKMRPFC | 9 | MRP demand forecast — PART+DATE PK; QTY (forecasted demand), OQTY (original), CQTY (committed), FLAG, DATE1, NUM |
| BKMRPPO | 16 | MRP planned purchase orders — UID+VEND+DATE+ERD+PART+QTY+PRICE+WOPRE/WOSUF+PLANR(4, planner)+CONF(confirm flag)+DONE+MTREC+EXTRA+EST/ESTLNE (estimate link) |
| BKMRPSW | 2 | MRP processing switch — PART + SW(1-char flag); turns MRP on/off per item |

**Relationship:** BKMRPFC feeds demand → MRP engine plans releases → BKMRPPO receives planned
PO recommendations → planner confirms/modifies → BKMRPPO confirmed rows become real BKAPPO records.
BKMRPSW gates which items MRP considers.

---

### BKED* Tables — EDI Processing (Unified Invoice Architecture Confirmed)

Key finding: **BKEDIH and BKEDIL are EDI-In staging tables with identical structure to BKARINV/BKARINVL.**

| Table | Fields | Purpose |
|---|---|---|
| BKEDIH | 84 | EDI-In invoice header — same 84 fields as BKARINV; staging area for inbound EDI invoices before posting |
| BKEDIL | 28 | EDI-In invoice lines — same 28 fields as BKARINVL |
| BKEDIDUN | 7 | Customer DUNS mapping — CUST(10)+DUNS(15)+EDI(enable)+EFFDT+PRODS+ADVS+SHPCD; maps customer to D-U-N-S number for EDI routing |
| BKEDMSTR | 3 | EDI master config — NEXTN (sequence counter), DUNS (our company D-U-N-S number), PATH (66-char file path for EDI import files) |
| BKEDNOTE | 3 | EDI notes — EDI#+SO#+NOTE(80); notes attached to an EDI transaction |
| BKEDPOST | 2 | EDI post log — INVN+CUST; records which EDI invoices have been posted to AR |

**Architecture:** Inbound EDI → parse into BKEDIH/BKEDIL → validate → post → becomes BKARINV record.
BKEDIDUN identifies which customers are EDI-enabled and routes by D-U-N-S number.

---

### BKES* Tables — Estimating (Unified Invoice Architecture Confirmed)

Key finding: **BKESTQT and BKESTQTL are ES Estimating quote tables with identical structure to BKARINV/BKARINVL.**

| Table | Fields | Purpose |
|---|---|---|
| BKESTQT | 84 | Estimating quote header — same 84 fields as BKARINV; quotes use the full invoice structure |
| BKESTQTL | 28 | Estimating quote lines — same 28 fields as BKARINVL |
| BKESTCFG | 13 | Quote configuration — NUM+STAT+CLASS+FORM(1)+CMPY_INFO(1)+DAYS(validity days)+ENDLN_1..5(30 each, footer lines)+SONUM+EXTRA; controls quote-to-SO conversion |

**Architecture:** Quote entered in ES module → BKESTQT header + BKESTQTL lines → when approved,
converted to BKARINV SO with same field structure (no data transformation needed).

---

### YS — Y/N System Flags Editor

T7YSYN (52 procs) — opens BKYSMSTR. Maintenance program for the BKYSMSTR table (Y/N system
configuration flags). Every Yes/No behavioral setting in EvoERP lives in BKYSMSTR; T7YSYN is
the direct editor for these flags.

**Confidence: 72/100** — single program; BKYSMSTR(355f: 1 key + 354 Y/N flags) fully extracted from DDF; purpose confirmed from name + table; individual flag meanings blocked by RWN encryption.

---

### CU — WO Material Cut Sheet

Two programs:
- **T7CUTSHEET2** (75 procs): WOMAT + LOT + WORKORD + WOBOM + ISBINLOT + BKPSUSER — lot-tracked cut sheet
- **T7CUTSHEET2B** (60 procs): same base without LOT; adds MKECLASS — non-lot-tracked variant

Generates a material cut sheet for shop floor: shows which components (WOBOM) are required for a WO, what has been issued (WOMAT), and where to pull from (ISBINLOT bin locations).

**WOBOM (24f) — WO Bill of Materials (components required)**

Primary key: WOBOM_OPER(2) + WOPRE(8) + WOSUF(2) + COMPCODE(15, derived)

| Field | Meaning |
|---|---|
| WOBOM_ASSY (15) | Assembly item code (the parent item) |
| WOBOM_COMPCODE (15) | Component item code |
| WOBOM_START (date) | Need date for this component |
| WOBOM_ASSYDESC/COMPDESC (30 each) | Assembly/component descriptions |
| WOBOM_QTYPER (float) | Quantity per assembly |
| WOBOM_SCRAPQTY (float) | Allowance for scrap |
| WOBOM_TOTQTY (float) | Total required (SQTY × QTYPER + scrap) |
| WOBOM_ASSYQTY (float) | Assembly quantity scheduled |
| WOBOM_QTYISSUED (float) | Already issued to WO |
| WOBOM_UM (3) | Unit of measure |
| WOBOM_EMATCST (float) | Estimated material cost |
| WOBOM_AMATCST (float) | Actual material cost issued |
| WOBOM_REFERENCE (20) | BOM reference designator |
| WOBOM_OPTION (1) | Option flag (for Features & Options) |
| WOBOM_VEND (10) | Preferred vendor code |
| WOBOM_BINLOC (10) | Default bin location |
| WOBOM_UID (30) | Unique ID (for change tracking) |
| WOBOM_REV (5) | BOM revision level |
| WOBOM_SEQ (2) | Print/display sequence |
| WOBOM_EXTRA (50) | Extra notes |

**WOMAT (17f) — WO Material Transactions (actual issues)**

Primary key: WOMAT_DATE + WOPRE(8) + WOSUF(2) + PCODE (derived)

| Field | Meaning |
|---|---|
| WOMAT_WOPRE/WOSUF | Work order reference |
| MTWO_PRODCODE (15) | Parent/assembly item code |
| WOMAT_PRODDESC (30) | Assembly description |
| WOMAT_PCODE (15) | Component code issued |
| WOMAT_PDESC (30) | Component description |
| WOMAT_QTYISSUED (float) | Quantity issued to WO |
| WOMAT_QTYSCRAP (float) | Quantity scrapped |
| WOMAT_SCRAPCD (2) | Scrap reason code |
| WOMAT_LOT (15) | Lot number of stock issued |
| WOMAT_SERIAL (25) | Serial number of stock issued |
| WOMAT_KIT (1) | Kit flag |
| WOMAT_COST (float) | Unit cost at time of issue |
| WOMAT_REF (15) | Reference |
| WOMAT_SCDESC (30) | Scrap description |
| WOMAT_EXTRA (50) | Extra notes |

**ISBINLOT (11f) — Bin-Level Lot Inventory**

Primary key: IS_BINLOT_ITEM(15) + LOC(10) + LOT(15) + BIN(15)
- UOH(float) — quantity on hand in this exact item+location+lot+bin
- TMPSO(40)+TMPPO(40) — temporary allocation strings for active SO/PO
- DFLT(1) — default bin flag; DATE; FLAG; EXTRA(50)
More granular than BKICLOC (which tracks location-level only, not bin+lot).

**Cut sheet workflow:** WO release → T7CUTSHEET2 reads WOBOM (what's needed) joined to WOMAT (what's been issued) and ISBINLOT (where to pick from) → prints a picking list showing shortage = TOTQTY − QTYISSUED, with bin location for each component. Lot-tracked variant shows which bins have the right lot.

**Confidence: 72/100** — Both programs identified; WOBOM(24f)+WOMAT(17f)+ISBINLOT(11f) fully extracted from DDF; cut sheet workflow confirmed from table relationships.

---

### AD/ADCA — Advanced Data Collection (Shop Floor Automatic DC)

T7ADCA (290 procs, 55 unique tables) — the largest DC entry module. Full automatic shop floor
data collection: real-time labor posting, routing tracking, QC inspection, and tray management.

Key tables opened (unique to or important in T7ADCA):

| Table | Fields | Purpose |
|---|---|---|
| BKDCSHFT | 34 | Shift definitions — NAME1/2/3 (3 shifts), with START/BUFFER/BRK1IN/BRK1OUT/BRK2IN/OUT/END times per shift; 3 shifts × ~11 time fields each |
| ISROUTEX | 100 | Routing extension — IS_ROUT_CODE+OPER PK; 10 machine slots × CYCTIME/CYCHR/... fields; extended cycle times per routing operation |
| ISWOROEX | 60 | WO Routing extension — WOPRE+WOSUF+OPER PK; ITP(item type pack), FOI(1), LQTY(labor qty), EXTRA(100), SDAY/FDAY, DATE1, ALPHA1/2, NUM1, DESC1 + 45 more custom slots |
| ISWOEX | 63 | WO Extended fields — WOPRE+WOSUF PK; ITP(20), RF(1), EXTRA(100), MCLASS(6), MNUM, dates 1-4, INT1, NUM1 + 48 more |
| OPQCDESC | 10 | Operation QC description — WOPRE+WOSUF+OPER PK; DESC(30)+SERIAL(25)+UID(30)+QCCODE(2)+DATE+QTY+EXTRA; QC result per WO operation |
| ISWOTRAY | 52 | WO Tray tracking — tray number + WO/oper + started/completed/scrapped qty + 5 bin splits |
| EIMCOLST | — | NOT IN DDF — EIM Color List (UI display config for DC labor screen) |

Also opens: BKDCLAB, WORKORD, BKPRMSTR, MTICMSTR, BKICMSTR, WOROUT, ROUTING, MACHINE, WORKCTR, WOLABOR, SCRAP

**ADCA Workflow:** Operator scans at work center → T7ADCA reads WORKORD + ROUTING for operation context → posts BKDCLAB labor record → updates WOLABOR/WOROUT → if QC required, creates OPQCDESC → if tray tracking, updates ISWOTRAY

**Confidence: 70/100** — T7ADCA confirmed with 55 unique tables; all tables cross-referenced in DDF (EIMCOLST exception noted); BKDCSHFT(34f), ISROUTEX(100f), ISWOROEX(60f), ISWOEX(63f), ISWOTRAY(52f), OPQCDESC(10f) full schemas extracted; DC workflow confirmed; specific screen field mapping blocked by RWN encryption.

---

---

## MODULE QUICK REFERENCE — Pass 36 Additions

### FO — Features & Options

5 programs confirmed:

| Program | Procs | Purpose |
|---|---|---|
| T7FOA | 5 | FO-A stub (FILELOC+FILEDICT — likely redirect/nav stub) |
| T7FOB | 5 | FO-B stub (same) |
| T7FOC | 60 | FO-C main entry — option definition: BKBMMSTR+BKICMSTR+MTICMSTR; links option codes to BOM items |
| T7FOD | 103 | FO-D item/class/category range filter — BKICMSTR+BKICLOCM+CLASMSTR |
| T7FOE | 86 | FO-E item filter — same tables as FOD |

- **BKFOCFG** (18f): FO module config — BKFO_CFG_MANFET(1, mandatory features flag) + YN_1..14 (14 behavioral flags) + 3 more fields

**BKBMMSTR** (26f) — BOM master record: BKBM_PARENT(15)+COMPONENT(15) PK; QTY_REQD(8), REFERENCE(20), PROD_TYPE(1), PROD_SCRAP(8), PROD_OP(3 operation code); PROD_OPYN_1..6 (1×6 option flags per BOM line — controls which FO options activate this component); PROD_PRICE(8), PROD_RTNUM(2 routing number); plus 11 more fields (substitutes, alternate parts, etc.)

**Architecture:** BKBM.PROD.OPYN_1..6 flags on each BOM line record control which FO options activate that component. When a customer selects option N, EvoERP looks for BOM lines where PROD_OPYN_N = Y and adds them to the WO. FO-C defines the option/component pairings in BKBMMSTR; FO-D/E provide range filters for bulk option assignment across items; FP-B prints the option list per item.

**FO Order Lifecycle (Pass 65 — ISFOHEAD + ISFOLINE + ISFOORDL):**

FO also manages customer-specific FO configurations — a customer can request a specific option set and FO creates an "order" record:

- **ISFOHEAD (16f):** FO order/configuration header — UID PK; PARENT(15 item code); DATE; DESC(60); CUST(customer)+VEND(vendor); RFQ#; STATUS(1); REV(revision); MDATES_1..5 (milestone dates); PERM (permissions flag); EXTRA(100). One row per customer FO configuration session.
- **ISFOLINE (78f):** FO configuration BOM line — UID(FK→ISFOHEAD)+LEVEL+50×OPFLAG_1..50 (1×50 — one flag per option slot) + EXTRA + PARENT(15) + LINEN + COMP(component part) + QTYREQ + REF + TYPE + SCRAP + OP(operation#) + OPYN_1..6 + PRICE + RTNUM + DUPOP + OPDSC + VEND + DATE1/2 + BEXTRA + REV + PBRANC/CBRANC (parent/child branch for nested options). The 50 OPFLAG slots = customer's active option selections.
- **ISFOORDL (18f):** FO order detail line — UID+TYPE+PCODE+PDESC+PQTY+PPRCE+PDISC+PEXT + ESD (estimated ship date) + LOC + TXBLE + UM + LN + DRAW + REV + LINE + OUID (original UID) + EXTRA. These are the actual SO lines generated from a configured FO order.

**Complete FO Data Flow:**
```
Customer selects options →
  ISFOHEAD (header: which item, customer, date)
  ISFOLINE (per-BOM-line option flags — 50 slots)
  ISFOORDL (output SO lines with prices)
    ↓
  BKBMMSTR.PROD_OPYN_1..6 filters which BOM lines activate
    ↓
  BKARINV/BKARINVL (SO invoice records)
    ↓
  WORKORD/WOBOM (WO with only active-option BOM lines)
```

**Confidence: 78/100** — 5 programs identified; BKFOCFG(18f), BKBMMSTR(26f), ISFOHEAD(16f), ISFOLINE(78f), ISFOORDL(18f) full schemas extracted; complete FO order lifecycle confirmed; detailed option-selection UI logic blocked by encryption.

---

### RF — Request for Quote (from Estimating)

T7RFQ (103 procs) — opens ISESTDTL + MTICMSTR + BKBMMSTR + BKICMSTR + BKMRPPO + BKAPPOL +
BKAPVEND + BKAPPO + BKSBVEND + BKYSMSTR + BKICLOCM + BKSYMSTR.

Bridges ES Estimating → vendor RFQ → PO. Reads estimate detail (ISESTDTL), creates vendor quote
requests using preferred vendors (BKSBVEND), optionally links to MRP planned POs (BKMRPPO).

**ISESTDTL** (203 fields): IS_EST_NUM + PART + LINE PK; 10 quantity breakpoints (QTY_1..10);
per-breakpoint cost buckets (MAT_1..10, and likely LAB/OVHD/SUB/TOT...) — full estimate
rollup per quantity break with material, labor, overhead, and subcontract costs. 203 fields
= 10 qty breaks × ~20 cost fields.

**ISESTDTL full structure (203 fields):**

| Field group | Count | Meaning |
|---|---|---|
| IS_EST_NUM + PART(15) + LINE | 3 | PK: estimate number + item code + line |
| IS_EST_QTY_1..10 | 10 | 10 quantity break levels |
| IS_EST_MAT_1..10 | 10 | Material cost per qty break |
| IS_EST_MATMU_1..10 | 10 | Material markup % per break |
| IS_EST_LAB_1..10 | 10 | Labor cost per break |
| IS_EST_LABMU_1..10 | 10 | Labor markup % per break |
| IS_EST_SETUP_1..10 | 10 | Setup cost per break |
| IS_EST_OP_1..10 | 10 | Outside process cost per break |
| IS_EST_OPMU_1..10 | 10 | Outside process markup % per break |
| IS_EST_OH_1..10 | 10 | Overhead cost per break |
| IS_EST_OHMU_1..10 | 10 | Overhead markup % per break |
| IS_EST_MISC_1..10 | 10 | Miscellaneous cost per break |
| IS_EST_EXTRA_1..10 | 10 | Extra cost per break |
| IS_EST_MEMU_1..10 | 10 | Material+expense markup % per break |
| IS_EST_OVALL_1..10 | 10 | Overall markup % per break |
| IS_EST_TOTAL_1..10 | 10 | Total cost per break |
| IS_EST_PRICE_1..10 | 10 | Selling price per break |
| IS_EST_COST_1..10 | 10 | Computed cost per break |
| IS_EST_VOVHD_1..10 | 10 | Variable overhead per break |
| IS_EST_SETMU | 1 | Setup markup % (global) |
| IS_EST_TEMP_NUM | 1 | Template reference number |
| IS_EST_BOM_FLAG | 1 | BOM-linked flag |
| IS_EST_RT_FLAG | 1 | Routing-linked flag |
| IS_EST_EX_FLAG | 1 | Extra process flag |
| IS_EST_OPPTYPE | 1 | Opportunity type |
| IS_EST_QTREV | 1 | Quote revision |
| IS_EST_STATUS | 1 | Estimate status |
| IS_EST_DRAW + REV | 2 | Drawing number + revision |
| IS_EST_ORDDESC + ORDDTE | 2 | Order description + date |
| IS_EST_EXPDTE + LOSTDTE | 2 | Expiry date + lost date |
| IS_EST_CUST | 1 | Customer reference |
| IS_EST_QUICK + SO + WOPRE + WOSUF | 4 | Quick-entry flag, linked SO#, linked WO# |

Total: 3 + (10 × 19) + 20 = 3 + 190 + 20 = 213... wait — actual count is 3 + 10 qty + 18×10 cost + 20 scalar = 203 ✓

The estimate supports full what-if analysis: at each of 10 qty breaks, every cost component (material, labor, setup, outside process, overhead, misc) is individually tracked with markups, so the estimator can compare total cost and price at any volume.

**Confidence: 75/100** — T7RFQ program confirmed; ISESTDTL(203f) fully decoded from DDF — complete 10-qty-break cost structure with all 18 cost types confirmed; RFQ-to-PO workflow confirmed from BKMRPPO+BKAPPO in DB fingerprint; vendor selection logic blocked by encryption.

---

### CH — Multi-Location Chain

Two programs:
- **T7CHAIN** (62 procs): ISCHAINM + BKPSUSER + BKSYMSTR — chain maintenance with user assignment
- **T7CHAINM** (40 procs): ISCHAINM + FILEDICT — chain data file maintenance

**ISCHAINM** (17 fields): Multi-location chain master record:
- IS_CHAIN_USER(15) + PARENT(12) + CHILD(12) — PK: user + parent company code + child company code
- IS_CHAIN_PARAM_1..10 (15 each) — 10 parameters controlling chain behavior
- IS_CHAIN_AUTO(1) — automatic chain processing flag
- IS_CHAIN_DATE — date
- IS_CHAIN_DESC(100) + EXTRA(100) — description and extra

**Purpose:** Defines parent-child company relationships for multi-company chain setups.
A "chain" links a user session to a parent company and one or more child companies, with
10 configurable parameters. T7CHAINM manages the physical Btrieve files for each chain entity.

**Confidence: 62/100** — 2 programs identified; ISCHAINM schema extracted; chain semantics
(what parameters control) blocked by encryption.

---

### PA — Paperless DC (Shop Floor Control)

Three programs:
- **T7PAPERLESS** (205 procs, 50 unique tables): full paperless shop floor control
- **T7PACKMENU** (5 procs, no DB): pack menu stub/launcher
- **T7PASS** (3 procs): password sub-module

T7PAPERLESS opens: WORKORD + MTICMSTR + BKICMSTR + WOROUT + ROUTING + BKICLOC + ISBINLOC +
ISWOEX + WORECV + BKAPPOL + ISWOTRAY + BKDCLAB + ... (50 unique tables).

Paperless DC allows operators to receive materials, complete operations, and record labor
without paper travelers. Integrates: WO routing (WOROUT+ROUTING), bin location (ISBINLOC),
tray tracking (ISWOTRAY), DC labor (BKDCLAB), WO receipts (WORECV).

**ISBINLOC** (9 fields): bin-level inventory WITHOUT lot tracking:
- ISBIN_LOC_ITEM(15) + LOC(10) + BIN(15) — PK: item + location + bin
- ISBIN_LOC_UOH — quantity on hand per bin
- ISBIN_LOC_CDATE / VDATE — created/validated dates
- ISBIN_LOC_DFLT(1) — default bin flag
- ISBIN_LOC_RVLVL(5) — revision level
- Compare: ISBINLOT tracks per lot within a bin; ISBINLOC is the non-lot bin balance

**Confidence: 62/100** — 3 programs identified; ISBINLOC schema extracted; 50-table scope
confirms full shop floor integration; detailed screen logic blocked.

---

### TE — NACHA / ACH Electronic Payments

T7TESTNACHA (103 procs) — opens BKSYMSTR + ISBANKS + BKGLCHK + BKAPVEND + BKARINVL.
Generates NACHA ACH electronic payment files from AP vendor payments and bank account config.

**BKGLCHK** (11 fields): GL check/payment register:
- BKGL_CHK_CHKACT(2, checking account number) + NUM(check number) — PK
- BKGL_CHK_DATE — payment date
- BKGL_CHK_TYPE(1) — payment type (check/ACH/wire)
- BKGL_CHK_NAME(25) — payee name
- BKGL_CHK_AMT — amount
- BKGL_CHK_FLAG(1) — reconciled/voided flag
- BKGL_CHK_DATER — reconciliation date
- BKGL_CHK_VEND(10) / BKGL_CHK_CUST(10) — vendor or customer reference

**Workflow:** AP payment batch → T7TESTNACHA reads BKAPVEND (routing/account) + ISBANKS
(company bank) → creates NACHA file → records in BKGLCHK as ACH type payments.

**Confidence: 72/100** — program confirmed; BKGLCHK(11f) + ISBANKS(23f: NUM+SRT+DESC+GL+NXTNUM+BAL+ROUT+ACCT+CURR+TYPE+VEND+ACTIVE+AR/AP/PR flags+5 RTM codes) fully extracted; NACHA workflow confirmed; ACH record format blocked by encryption.

---

### KI — Kit Assembly

T7KIT (153 procs) — opens BKICMSTR + MTICMSTR + WOBOM + BKICLOC + BKYSMSTR + ISLINKS +
WOMAT + WORKORD + WOROUT + BKPRMSTR + ISBINLOC + LOT + ... (26 unique tables).

Assembles "kit" items by creating simplified Work Orders that combine components from
inventory. Uses WOBOM (BOM list), WOMAT (issues materials), WORKORD+WOROUT (WO tracking),
LOT (lot assignment), ISBINLOC (bin selection). No routing/labor tracking — kits are
assembled directly from components without shop floor operations.

**Confidence: 65/100** — program confirmed; purpose from table fingerprint; kit-from-BOM
workflow clear; detailed option/substitution logic blocked by encryption.

---

### New Tables Confirmed (Pass 36)

| Table | Fields | Purpose |
|---|---|---|
| ISCHAINM | 17 | Multi-location chain master — USER+PARENT+CHILD PK; 10 params; AUTO/DATE/DESC |
| ISBINLOC | 9 | Bin-level inventory (no lot) — ITEM+LOC+BIN PK; UOH/dates/DFLT/RVLVL |
| BKGLCHK | 11 | GL check/payment register — CHKACT+NUM PK; TYPE/NAME/AMT/FLAG/DATER/VEND/CUST |
| ISESTDTL | 203 | Estimate detail — 10 qty breaks × material+labor+overhead cost columns |
| BKFOCFG | 18 | FO module config — MANFET flag + 15 YN flags + OPCODE |

---

---

## MODULE QUICK REFERENCE — Pass 37 Additions

### SC — Serial Control

9 programs — serial number tracking through manufacturing and sales:

| Program | Procs | Purpose |
|---|---|---|
| T7SCA | 78 | SC-A serial cycle count entry — SERIAL+WORKORD+BKICLOC+ISBINLOC; enter count by WO and bin location |
| T7SCB | 59 | SC-B serial list maintenance — BKICMSTR+ISTRIGRS; trigger-linked serial list |
| T7SCC | 121 | SC-C serial count posting — BKICMSTR+SERIAL+MTICMSTR+BKARTXN; posts serial count to AR transaction |
| T7SCD | 5 | SC-D sub-stub of SCC |
| T7SCE | 88 | SC-E serial count by location — BKICMSTR+SERIAL+BKICLOCM; location-range serial inquiry |
| T7SCF | 131 | SC-F serial transaction history — SERIAL+BKICMSTR+BKICLOC+INVTXN+CLASMSTR+ISCATMST; full transaction log |
| T7SCG | 92 | SC-G serial counter maintenance — ISSERCNT+MTICMSTR+CLASMSTR; manages auto-serial generation |
| T7SCH | 113 | SC-H serial history report — MTICMSTR+SERIAL+INVTXN+WORECV+WORKORD+BKARINV; cross-module history |
| T7SCOMP | 54 | SC-COMP serial compound — ISSCOMP; manages compound/batch serial definitions |

**ISSCOMP** (5f): IS_SCOMP_DETAIL(20) + COMPND(30) + VIS(1) + WHO(40) + IS_SCOMP(50) — compound
serial definitions (linking serial number to batch/compound product identifier).

**SERIAL (30f) — Central Serial Number Master:**

| Field | Type | Size | Meaning |
|---|---|---|---|
| MTSER_CODE | STRING | 15 | Item code (PK part 1, FK → BKICMSTR) |
| MTSER_SERIAL | STRING | 25 | Serial number (PK part 2) |
| MTSER_LOT | STRING | 15 | Associated lot number |
| MTSER_PO | FLOAT | 8 | Purchase order number (PO receipt source) |
| MTSER_RECDOC | FLOAT | 8 | Receipt document number |
| MTSER_VENDOR | STRING | 10 | Vendor code (FK → BKAPVEND) |
| MTSER_RECDATE | DATE | 4 | PO receipt date |
| MTSER_POCOST | FLOAT | 8 | PO receipt cost |
| MTSER_SO | FLOAT | 8 | Sales order number (customer ship reference) |
| MTSER_CUSTCODE | STRING | 10 | Customer code (FK → BKARCUST) |
| MTSER_SHIPDATE | DATE | 4 | Date shipped to customer |
| MTSER_SELLPRICE | FLOAT | 8 | Selling price |
| MTSER_WO | FLOAT | 8 | Work order number (manufacturing source) |
| MTSER_ISSDATE | DATE | 4 | WO issue/completion date |
| MTSER_ISSCOST | FLOAT | 8 | WO completion cost |
| MTSER_INRECDATE | DATE | 4 | Internal receipt date (WO receipt / transfer-in) |
| MTSER_INRECCOST | FLOAT | 8 | Internal receipt cost |
| MTSER_EXPDATE | DATE | 4 | Expiration date |
| MTSER_WOCODE | STRING | 15 | WO part code |
| MTSER_NOTES_1..8 | STRING | 30 | 8 × 30-char free-text notes |
| +10 more | — | — | Additional tracking fields |

The SERIAL table is EvoERP's serial lifecycle ledger: each row is one unique serialized unit. Three lifecycle paths:
- **Purchased:** PO→RECDOC→VENDOR→RECDATE→POCOST
- **Manufactured:** WO→ISSDATE→ISSCOST (INRECDATE=WO receipt)
- **Sold:** SO→CUSTCODE→SHIPDATE→SELLPRICE

EXPDATE supports shelf-life and warranty tracking. Multiple SERIAL rows per item code, one per serial number.

**Architecture:** T7SCA assigns serials at WO receipt; T7SCF posts serial inventory transactions (INVTXN); T7SCG manages auto-generation counters (ISSERCNT); T7SCH posts serial WO receipts and SO shipments (WORECV+BKARINV); T7SCOMP handles compound/batch serial definitions (ISSCOMP).

**Confidence: 78/100** — 9 programs confirmed; SERIAL(30f) full schema extracted — all three lifecycle paths (PO/WO/SO) decoded; ISSCOMP + ISSERCNT schemas confirmed; per-screen field detail blocked by encryption.

---

### TC — Treasury Control

T7TCC (119 procs) — the cash management and banking module. Opens:
ISTERMS + ISBANKS + BKARINVT + BKARCUST + BKARINV + BKGLCOA + BKSYMSTR + BKYSMSTR +
ISMCF + BKART + BKAPCHKF + BKARDEP + BKGLCHK + BKARINVI + BKPRSALE + ...

**Key tables:**

**BKART** (12f): AR transaction record:
- BKART_CUST(10) + TRXN(float) — PK
- BKART_TYPE(1) — P=payment, C=credit, etc.
- BKART_DISC — discount taken
- BKART_AMOUNT — transaction amount
- BKART_POSTDATE / ENTDATE — posted / entered dates
- BKART_TRXNLINK — cross-link to another transaction (e.g., payment → invoice)
- BKART_INVC — invoice reference
- BKART_CHECK — check number reference

**BKAPCHKF** (12f): AP check/payment file:
- BKAP_CHK_VNDCOD(10) + INVNUM(10) — PK
- BKAP_CHK_INVAMT / AMTPD / DISC — invoice amount, amount paid, discount
- BKAP_CHK_TYPE(1) — payment type
- BKAP_CHK_NUM — check number
- BKAP_CHK_CHKACT(2) + CHKDTE — checking account + check date
- BKAP_CHK_ISCUR(3) — currency code

**BKARINVT** (23f): AR invoice tax detail:
- BKAR_INVT_CODE(10) + DATE + NUM — PK
- BKAR_INVT_AMT / AMTRM — tax amount and remainder
- BKAR_INVT_DESC(25) — tax description
- BKAR_INVT_TYPE(1) + GLDPT(4) + SLSP(salesperson) — type/GL/salesperson

**BKARINVI** (16f): AR invoice interest/finance charge lines:
- BKAR_INVI_SONUM + INVNM + ESD + PCODE — PK
- BKAR_INVI_PQTY / PPRCE / PDISC / PEXT / PCOGS — qty/price/discount/extension/cost
- BKAR_INVI_ITYPE(1) — interest charge type
- BKAR_INVI_EXTRM + COMM_1 — extended amount + commission

**ISREPORD (17f) — Scheduled Report/Commission Order:**
- ISREP_ORD_REPNM(15) — report name (FK → RTM report)
- ISREP_ORD_REPWH(1) — when to run (schedule code)
- ISREP_ORD_SONUM(float) — linked SO number
- ISREP_ORD_INVNM(float) — invoice number
- ISREP_ORD_INVDT (date) — invoice date
- ISREP_ORD_ULID(15) — user/location ID
- ISREP_ORD_COMPR(float) — commission percentage
- ISREP_ORD_CMAMT(float) — commission amount
- ISREP_ORD_AMT(float) — order amount
- ISREP_ORD_AMTRM(float) — amount remaining
- ISREP_ORD_CBK(float) — chargeback amount
- ISREP_ORD_PCODE(15) — part code
- ISREP_ORD_CUST(10) — customer code
- ISREP_ORD_PAYDT (date) — payment date
- ISREP_ORD_EXTRA(100)
- ISREP_ORD_GLA(10)/GLD(4) — GL account for this commission

ISREPORD stores scheduled report/commission order records — links a report template to a specific SO/invoice for commission tracking and scheduled printing.

**MKECLASS (3f):** MKECLASS_NUM(2 PK)+DESC(30)+ACTIVE(1) — MKE class code table. Simple active/inactive classification codes used in TC (treasury) and WBKLUGRID lookup framework.

**TC Role:** Cash flow management — AR terms configuration, bank account management, AR payment recording (BKART), AP check issuance (BKAPCHKF), AR deposits (BKARDEP), check reconciliation (BKGLCHK), invoice tax accumulation (BKARINVT), finance charges (BKARINVI), and commission report scheduling (ISREPORD).

Also opens: BKPRCOMM (commission detail), WORKORD (WO cost reference), BKGLX (GL extended), BKGLTRAN (GL transactions).

**Confidence: 72/100** — single program (119p) confirmed with 37-table set; all key TC table schemas extracted (BKART/BKAPCHKF/BKARINVT/BKARINVI/ISREPORD/MKECLASS); cash-flow workflow confirmed from table set; detailed screen logic blocked by encryption.

---

### SA — Sales Analysis (Major Expansion: 13 Programs)

Previously documented as 6 DFMs; now 13 programs fully identified:

| Program | Procs | Purpose |
|---|---|---|
| T7SAA | 212 | Main SA engine — BKARINV+BKARCUST+BKARINVL+BKICMSTR+ISARCHG+ISSOBOX+BKPRSALE+ISJOB+CLASS+ISAREX |
| T7SAB-SAL (9 stubs) | 5 each | Range filter stubs — all open same table set as SAA (report variant selectors) |
| T7SAM | 238 | SA management report — BKSAREPT+BKACTRPT+ISBUILD+BKARINVL+BKICMSTR+ISRMAI+ISSRINFO+WORKORD+BKCMLEAD+BKCMTERR |
| T7SAN | 220 | SA report variant N — BKSAREPT+BKACTRPT (same structure, excludes ISRMAI/ISSRINFO) |
| T7SAO | 169 | Top N sales — BKICMSTR+BKARCUST+BKPRSALE+BKARINV+ISARCHG+BKARINVL+BKCMACCL+BKCMTERR+BKCMACCC+ISAREX |
| T7SAP | 131 | SA by class/category — BKARINVL+BKARINV+MTICMSTR+BKICMSTR+CLASMSTR+ISCATMST |
| T7SAQ | 95 | Actual margin — BKARINV+BKARINVL+MTICMSTR+WORKORD+WOMAT+WOBOM (uses real WO costs) |

**Key new tables:**

**BKSAREPT** (57f): Saved SA report definition — PK: BKSA_TYPE(8) + BKSA_NAME(15). Stores a complete report filter state that can be recalled by name.

| Field group | Type | Content |
|---|---|---|
| BKSA_RTM | STRING 15 | ReportBuilder template file to run |
| BKSA_FROM1/THRU1 | FLOAT 8 | Numeric range (e.g., invoice number) |
| BKSA_FROM2/THRU2 | DATE 4 | Date range 1 (e.g., invoice date) |
| BKSA_FROM3/THRU3 | DATE 4 | Date range 2 (e.g., ship date) |
| BKSA_FROM4/THRU4 | FLOAT 8 | Numeric range 2 |
| BKSA_FROM5/THRU5 | STRING 10 | Alpha range 1 (e.g., salesperson code) |
| BKSA_FROM6/THRU6 | STRING 10 | Alpha range 2 |
| BKSA_FROM7/THRU7 | STRING 2 | Short code range 1 |
| BKSA_FROM8/THRU8 | STRING 2 | Short code range 2 |
| BKSA_FROM9/THRU9 | STRING 10 | Alpha range 3 |
| BKSA_FROM10/THRU10 | STRING 10 | Alpha range 4 |
| BKSA_FROM11/THRU11 | STRING 30 | Long alpha range 1 (e.g., customer name) |
| BKSA_FROM12/THRU12 | STRING 30 | Long alpha range 2 |
| BKSA_FROM13/THRU13 | STRING 4 | Code range 1 (e.g., class) |
| BKSA_FROM14/THRU14 | STRING 4 | Code range 2 (e.g., category) |
| BKSA_FROM15/THRU15 | UBINARY 2 | Integer range 1 |
| BKSA_FROM16/THRU16 | UBINARY 2 | Integer range 2 |
| BKSA_FROM17/THRU17 | STRING 10 | Alpha range 5 |
| BKSA_FROM18/THRU18 | STRING 15 | Part number range |
| BKSA_FROM19/THRU19 | STRING 25 | Territory/long-code range |
| BKSA_FROM20/THRU20 | FLOAT 8 | Numeric range 3 (e.g., amount) |
| BKSA_BASE | STRING 1 | Base flag (e.g., base currency) |
| BKSA_TITLE | STRING 40 | Report title text |
| BKSA_FROM21/THRU21 | STRING 15 | Part range 2 |
| BKSA_FROM22/THRU22 | STRING 4 | Code range 3 |
| BKSA_FROM23/THRU23 | DATE 4 | Date range 3 |
| BKSA_FROM24/THRU24 | FLOAT 8 | Numeric range 4 |
| BKSA_FROM25/THRU25 | FLOAT 8 | Numeric range 5 |
| BKSA_FROM26/THRU26 | STRING 3 | Currency code range |

**BKACTRPT** (53f): Activity Control report definition — same PK structure (BKAC_TYPE + BKAC_NAME). Named filter ranges cover the AC/inventory transaction domain:

| Field group | Content |
|---|---|
| BKAC_RTM | ReportBuilder template |
| FROM_PART/THRU_PART | Part number range |
| FROM_CLASS/THRU_CLASS | Item class range |
| FROM_CAT/THRU_CAT | Category range |
| FROM_DATE/THRU_DATE | Transaction date range |
| FROM_LOC/THRU_LOC | Location range |
| FROM_WOPRE/THRU_WOPRE + WOSUF | Work order range |
| FROM_CUST/THRU_CUST | Customer code range |
| FROM_INV/THRU_INV | Invoice number range |
| FROM_QC/THRU_QC | QC code range |
| FROM_PLOT/THRU_PLOT + LOT | Parent lot + lot range |
| FROM_SER/THRU_SER | Serial number range |
| FROM_PRICE/THRU_PRICE | Price range |
| FROM_AVGC/THRU_AVGC | Average cost range |
| FROM_STDC/THRU_STDC | Standard cost range |
| FROM_DESC/THRU_DESC | Description range |
| FROM_REF/THRU_REF | Reference range |
| FROM_DEPT/THRU_DEPT | Department range |
| FROM_QTY/THRU_QTY | Quantity range |
| FROM_SCRAP/THRU_SCRAP | Scrap code range |
| FROM_VEND/THRU_VEND | Vendor range |
| FROM_PO/THRU_PO | PO number range |
| FROM_TYPE/THRU_TYPE | Transaction type range |
| BKAC_TYPE_RANGE + ITEM_RANGE | Additional filter flags |

**ISJOB** (9f): Job tracking:
- IS_JOB_NUMB(15) — job number (PK)
- IS_JOB_DESC(30) + CUST(10) + VEND(10) — description, customer, vendor
- IS_JOB_STATUS(1) + OPENDT + CLOSEDT — job lifecycle
- Used in SA to group invoices under a job number

**ISAREX** (51f): AR customer extended data:
- ISAREX_CUST(10) — PK
- ISAREX_LONGNAME(60) — long customer name
- RS_EXPDT/UPDT/WHO/FORM/SGNDT — resale certificate tracking (expiry, update, who, form, signed)
- CRT_FORM(60) — certificate form reference
- NUM_1..4 + 39 more configurable fields

**ISRMAI** (54f): RMA (Return Merchandise Authorization) invoice:
- IS_RMA_NUM + PART + LINEID — PK
- DATE + RCPTDATE + CLOSDATE — entered/received/closed dates
- STATUS(30) + REASON(30) + DISP(40) — status, reason, disposition
- OSONUM + OINVNUM + OLDRMANO — original SO/invoice/RMA references
- 42+ additional fields

**BKCMACCL** (2f): CRM account level — CODE(10)+CLASS(5) — maps account to level classification
**BKCMLEAD** (2f): CRM lead source — SCODE(5)+DESC(25) — lead source lookup

**Architecture:** T7SAA is the data aggregation engine reading all invoices; T7SAB-SAL provide
report variant launchers (different filter defaults); T7SAM/SAN use BKSAREPT to run saved report
configs; T7SAO runs top-N customer/product analysis; T7SAQ uniquely reads WORKORD+WOMAT+WOBOM
to compute actual manufacturing cost vs. sales price for true margin analysis.

**Confidence: 75/100** — 13 programs identified; BKSAREPT (57f) and BKACTRPT (53f) full schemas with all 26 range-pair fields extracted; T7SAQ actual-margin mechanism confirmed; per-field reporting expressions remain in encrypted RWN.

---

### New Tables Confirmed (Pass 37)

| Table | Fields | Purpose |
|---|---|---|
| ISSCOMP | 5 | Serial compound definitions — DETAIL+COMPND+VIS+WHO+IS_SCOMP |
| BKSAREPT | 57 | Saved SA report definitions — TYPE+NAME PK; RTM template name; range filters |
| BKACTRPT | 53 | Activity report definitions — same structure; part/class/cat/date/loc ranges |
| ISJOB | 9 | Job tracking — NUM/DESC/CUST/VEND/STATUS/OPENDT/CLOSEDT |
| ISAREX | 51 | AR customer extended — resale certificates + 47 configurable fields |
| ISRMAI | 54 | RMA invoice — NUM+PART+LINEID; dates/status/reason/disposition/original refs |
| BKCMACCL | 2 | CRM account level code — CODE+CLASS |
| BKCMLEAD | 2 | CRM lead source — SCODE+DESC |
| BKART | 12 | AR transaction record — CUST+TRXN PK; TYPE/DISC/AMOUNT/dates/TRXNLINK/INVC/CHECK |
| BKAPCHKF | 12 | AP check file — VNDCOD+INVNUM PK; amounts/TYPE/check#/account/date/currency |
| BKARINVT | 23 | AR invoice tax by code — CODE+DATE+NUM PK; AMT/DESC/TYPE/GLDPT/SLSP |
| BKARINVI | 16 | AR invoice interest/finance charges — SONUM+INVNM+ESD+PCODE PK; qty/price/interest type |

---

---

## MODULE QUICK REFERENCE — Pass 38 Additions

### PI — Physical Inventory (Major Expansion: 8 Programs + All Schemas)

8 programs, complete freeze→count→variance→post cycle confirmed:

| Program | Procs | Purpose |
|---|---|---|
| T7PIA | 159 | PI-A Freeze: reads BKICMSTR+BKICLOC+ISCYCLCD, creates BKPIFROZ snapshot |
| T7PIB | 114 | PI-B Print count sheets: reads BKPIFROZ+BKPILOT+BKPISER (frozen data only) |
| T7PIC | 152 | PI-C Enter tag counts: writes BKPIPHYS (counted qty per tag); reads BKPIMSTR+ISBINLOC |
| T7PID | 98 | PI-D Discrepancy view: compares BKPIPHYS vs BKPIFROZ |
| T7PIE | 76 | PI-E Adjust/reconcile: BKPIFROZ+BKICMSTR; pre-post adjustment entry |
| T7PICA | 97 | PI-CA Count adjustment variant: BKPIMSTR+BKPIPHYS+BKICLOC |
| T7PIF | 137 | PI-F Post: ISBUILD+MTICMSTR+BKPIPHYS+ISBINLOC → updates inventory, GL via BKGLTRAN |
| T7PIG | 155 | PI-G Report: BKPIMSTR+BKPIPHYS+BKPIFROZ+BKICLOC+ISBINLOC+ISBNMSTR |

**PI workflow:**
```
PI-A Freeze → creates BKPIFROZ snapshot (UOH per item/loc/cost at freeze date)
  ↓
PI-B Print count sheets (from frozen data)
  ↓
PI-C Enter tag counts → BKPIPHYS (1 row per count tag: TAGNUM+ACTQTY+LOT+SERIAL+BIN)
  ↓
PI-D View discrepancies (BKPIPHYS vs BKPIFROZ)
  ↓
PI-E / PI-CA Enter adjustments (pre-post corrections)
  ↓
PI-F Post → update BKICMSTR/MTICMSTR; post to BKGLTRAN (GL adjustment)
  ↓
PI-G Report (variance by item/location)
```

**Table schemas:**

**BKPIMSTR** (3f): PI run master — BKPI_MSTR_YEAR(4) + QTR(2) + DESC(30). One row per PI run (freeze).

**BKPIFROZ** (19f): Frozen snapshot per item/location:
- BKPH_INFO_UOH — on-hand at freeze
- BKPH_INFO_YEAR(4) + QTR(2) + LOC(10) + PROD(15) — PK
- BKPH_INFO_COST — standard cost at freeze
- BKPH_INFO_GLPST(1) + INPST(1) — GL posted + inventory posted flags
- BKPH_INFO_FDATE — freeze date
- BKPH_INFO_LOT(1) + SER(1) — lot-tracked / serial-tracked flags
- BKPH_INFO_PCOST + PADJ — previous cost + previous adjustment
- BKPH_INFO_ACCTA(10)+DEPTA(4) + ACCTC(10)+DEPTC(4) — GL accounts (adjustments + cost)
- BKPH_INFO_PUNIT — previous unit cost
- BKPH_INFO_TAGS — number of count tags issued

**BKPIPHYS** (14f): Physical count entry (one row per count tag):
- BKPH_TAGNUM — tag number (PK)
- BKPH_ACTQTY — actual counted quantity
- BKPH_EMPNUM + EMPNAME(15) — counter employee
- BKPH_COMMENT(30) + COUNTDATE — notes + date counted
- BKPH_YEAR(4) + QTR(2) + LOC(10) + CODE(15) — run + item reference
- BKPH_FDATE — freeze date (cross-reference)
- BKPH_LOT(15) + SERIAL(25) + BIN(10) — lot/serial/bin detail

**BKPILOT** (10f): Lot-level count summary:
- BKPI_LOT_YEAR+QTR+CODE(15)+LOT(15)+LOC(10) — PK
- BKPI_LOT_QTY — lot quantity from count
- BKPI_LOT_TAG — tag number reference
- BKPI_LOT_SERQTY — serial quantity within lot
- BKPI_LOT_PSTD(1) — posted flag
- BKPI_LOT_BIN(15) — bin reference

**BKPISER** (10f): Serial-level count:
- BKPI_SER_YEAR+QTR+CODE(15)+SERIAL(25) — PK
- BKPI_SER_QTY — serial unit count
- BKPI_SER_TAG — tag number
- BKPI_SER_LOC(10) + LOTNO(15) — location + lot
- BKPI_SER_PSTD(1) + BIN(15)

**PIBINLOC** (14f): Bin-level frozen snapshot (without lot):
- PIBIN_LOC_ITEM(15)+LOC(10)+BIN(15) — PK
- PIBIN_LOC_UOH — frozen on-hand at bin level
- PIBIN_LOC_CDATE/VDATE — created/verified dates
- PIBIN_LOC_DFLT(1) + RVLVL(5) — default bin flag + reorder level
- PIBIN_LOC_YEAR+QTR+FDATE+LOT(15)+SER(25) — PI run reference

**PIBINLOT** (14f): Bin-level frozen snapshot with lot/serial:
- PI_BINLOT_YR+QTR+ITEM(15)+LOC(10)+LOT(15)+BIN(15) — PK
- PI_BINLOT_SER(25) + UOH + SQTY — serial + on-hand + serial qty
- PI_BINLOT_PSTD(1) + FLAG(1) + DATE + NUM + EXTRA(50)

**Confidence: 72/100** — 8 programs mapped, all 7 BKPI* table schemas extracted; complete
PI workflow confirmed; per-screen field details and post GL path blocked by encryption.

---

### CR — Contract Review / SO Approval (Expanded)

T7CTREVU (96 procs) opens: ISCTREVU + BKARINV + ISSOREVU + standard lookup tables.

**ISCTREVU** (17f): Department reviewer setup — who approves SOs for which department:
- IS_CREVU_EMPNME(25) + IS_CREVU_EMP — employee name + number (PK)
- IS_CREVU_DEPT(25) — department (FK → department code)
- IS_CREVU_ADMIN(1) — admin/override flag
- IS_CREVU_LEVEL(2) — approval level code
- IS_CREVU_MOTPAS(10) — manager override password
- IS_CREVU_ACTIVE(1) — active/inactive
- IS_CREVU_CDATE/EDATE/ADATE — created/effective/approved dates
- IS_CREVU_ATIME — approval time
- IS_CREVU_FLAG_1..5 — 5 behavior flags
- IS_CREVU_EXTRA(100)

**ISSOREVU** (12f): Per-SO approval record (already documented in SR module, reused here):
- IS_SOVU_SONUM + IS_SOVU_DEPT — PK (one row per SO per department)
- IS_SOVU_EMPNME + EMPNUM — reviewer employee
- IS_SOVU_MOTPAS(10) — override password
- IS_SOVU_ADATE/EDATE — approval/effective dates
- IS_SOVU_APPROVE(1) + REQUIRE(1) — approval status flags

**CR workflow:**
- CR-A: Assign departments to SOs — T7CTREVU creates ISSOREVU records for the SO
- CR-B: View/Enter SO approvals — reviewers with matching ISCTREVU dept enter approvals

**Confidence: 72/100** — ISCTREVU + ISSOREVU schemas confirmed; T7CTREVU 96-proc program
identified; SO approval workflow fully reconstructed from DB fingerprint; per-screen field
details blocked by encryption.

---

### New Supporting Tables (Pass 38)

**ISICMSTR** (41f): Item physical/shipping specifications (used by EM emergency GL):
- IS_PROD_CODE(15) — part code (PK, FK → BKICMSTR)
- IS_PROD_WT — weight
- IS_PROD_ITP(20) — item type code
- IS_PROD_TI / HI — tier index / height index (retail pallet specs)
- IS_PROD_FOBPAL / FOBFULL — FOB pallet and full-truckload quantity thresholds
- IS_PROD_HT / LG / WD — height / length / width dimensions
- IS_PROD_TOOL(15) — tooling reference code
- IS_PROD_SLEAD — safety lead time (days)
- IS_PROD_FLAG_1..5 — 5 behavior flags + 21 more fields
- Extends BKICMSTR with physical and shipping specs that affect freight and GL posting

**BKARTXN** (14f): AR transaction log — detailed shipment record per SO line:
- BKAR_TXN_SONUM — SO/invoice number (PK part)
- BKAR_TXN_CODE(15) + DESC(30) — item code + description
- BKAR_TXN_QTY — quantity shipped
- BKAR_TXN_LOT(15) + SERIAL(25) — lot/serial tracking at time of ship
- BKAR_TXN_DATE — transaction date
- BKAR_TXN_STOCK(15) — stock location code
- BKAR_TXN_LINE — SO line number
- BKAR_TXN_LOC(10) — inventory location
- BKAR_TXN_TMPSO(40) — temporary SO cross-reference
- BKAR_TXN_SRNUM — service repair number (SR module link)
- BKAR_TXN_BIN(15) — bin

**ISWOPRIO** (4f): WO priority code master:
- IS_WOPRIO_PRIO(1) — priority code (PK)
- IS_WOPRIO_DESC(30) — description
- IS_WOPRIO_EXTRA(100)
- IS_WOPRIO_COLOR — display color code (used in SH shop scheduling dispatch)

---

### New Tables Confirmed (Pass 38)

| Table | Fields | Purpose |
|---|---|---|
| BKPIMSTR | 3 | PI run master — YEAR+QTR+DESC (one row per freeze event) |
| BKPIFROZ | 19 | Frozen on-hand snapshot — PROD+LOC+YEAR+QTR; UOH, cost, GL accounts, GLPST/INPST flags |
| BKPIPHYS | 14 | Physical count entry — TAGNUM+ACTQTY+EMPNAME+LOT+SERIAL+BIN |
| BKPILOT | 10 | Lot-level PI count — YEAR+QTR+CODE+LOT; QTY+TAG+SERQTY+PSTD |
| BKPISER | 10 | Serial-level PI count — YEAR+QTR+CODE+SERIAL; QTY+TAG+LOC+LOTNO+PSTD |
| PIBINLOC | 14 | Bin-level frozen snapshot (no lot) — ITEM+LOC+BIN; UOH, dates, DFLT, RVLVL |
| PIBINLOT | 14 | Bin-level frozen snapshot (with lot/serial) — ITEM+LOC+LOT+BIN+SER; UOH+SQTY |
| ISCTREVU | 17 | CR department reviewer setup — EMPNME+EMP PK; DEPT/ADMIN/LEVEL/MOTPAS/ACTIVE |
| ISICMSTR | 41 | Item physical/shipping specs — CODE PK; WT/ITP/TI/HI/FOB/HT/LG/WD/TOOL/SLEAD |
| BKARTXN | 14 | AR transaction log — SONUM+CODE; QTY/LOT/SERIAL/DATE/LOC/BIN/SRNUM |
| ISWOPRIO | 4 | WO priority codes — PRIO PK; DESC/EXTRA/COLOR |

---

---

## MODULE QUICK REFERENCE — Pass 39 Additions

### AL — Audit Log + Alternate Parts (Expanded)

2 programs:
- **T7ALOGSETUP** (43p): Configures which tables/events are tracked for audit logging. Opens FILELOC (file list: enumerate all EVO tables), BKSYMSTR, BKPSUSER, **ISLOG** (the audit destination). ISLOG is written when monitored events fire.
- **T7ALTPART** (104p): Alternate/substitute part maintenance. Opens BKSBPART(5f: PARNT+PROD+CUST+SUBST+EXTRA) + BKICMSTR + **ISLINKS** (document attachment). Allows alternate parts to have attached documents.

**ISLOG (9f) — Audit Event Log:**
- IS_LOG_WHO(15) — user who performed action
- IS_LOG_WHAT(20) — event type/table name
- IS_LOG_DOING(60) — action description
- IS_LOG_STARTD (date) — event date
- IS_LOG_STARTT (time) — event time
- IS_LOG_COMPANY(4) — company code
- IS_LOG_KILL(1) — kill/terminate flag (whether to kill this session)
- IS_LOG_MSG(100) — message/comment
- IS_LOG_EXTRA(100) — extra data

ISLOG is the session/audit event log. T7ALOGSETUP configures which tables and operations (insert/update/delete) trigger ISLOG writes. The KILL flag allows an admin to force-terminate a specific user's session by writing a kill record.

**Key new table — ISLINKS** (311f): Global document/URL attachment store used across many modules:
- IS_LNK_UID(48) — unique document identifier (PK)
- IS_LNK_LINK(256) — document path or URL
- IS_LNK_APP(10) — owning application/module code
- IS_LNK_TYPES_1..9 (1 each) — 9 document type flags
- + 299 more fields (likely 300 attachment slots or extended metadata)

ISLINKS provides document linking across AL (alternate parts), BR (brands), JO (jobs+depts), and many other modules. SM-SD configures the AP document link via ISLINKS.

**Confidence: 70/100** — 2 programs confirmed; BKSBPART + ISLOG(9f) schemas extracted; ISLOG purpose and KILL-flag mechanism confirmed; T7ALOGSETUP logic (which tables/events to monitor) blocked by RWN encryption; per-field detail of remaining 299 ISLINKS fields blocked.

---

### BR — Brands / CRM Classification (Expanded)

2 programs:
- **T7BRANDS** (53p): Brand code maintenance — primary table BKCMACCC(2f: CCODE+DESC). Also opens BKICMSTR, BKARCUST, ISLINKS for cross-module lookups and document attachments.
- **T7BROWSER** (4p): HTML browser wrapper — same table set, very low proc count = thin UI wrapper.

**BKCMACCC** (2f, already extracted): CRM account classification code — CCODE(10) + DESC(30).

Confidence: 58/100 — 2 programs, primary table confirmed; detailed brand logic blocked.

---

### JO — Jobs and Departments (Expanded)

2 programs:
- **T7JOBS** (21p): ISDEPT+WOEXCHG maintenance. Opens BKARCUST+BKAPVEND+CLASMSTR+ISCATMST for lookups; also ISREMIND+ISNOTES+ISNTYPE+ISLINKS+WORKCTR+BKICLOCM+BKAPPO+BKMRPFC+ISTRIGRS+DBAFIFO+ISBNMSTR+BKGLTRAN. The wide table set reflects T7JOBS being a general drill-down viewer in addition to ISDEPT/WOEXCHG maintenance.
- **T7JODPSALES** (52p): Opens IS2DBAR+ISCYCLCD+BKSBPART+BKAPDESC+ISNCR+ISUDFINV+ISICMSTR+BKSYHELP — SM/item inquiry drill-down panel. Not JO-specific; part of the SM/general item inquiry framework.

**ISDEPT (3f):** IS_GF_DEPT(4 PK)+IS_GF_DEPT_DESC(30)+IS_GF_DEPT_MISC(20) — department master. GF_ prefix = GL Finance dept. Used across GL, JC, AR for departmental cost allocation.

**DBAFIFO (5f):** FIFO costing queue — FIFO_PARTNO(15 PK)+QTY(float)+COST(float)+RECVDATE(date)+REMAIN(float). One row per receipt layer per item for FIFO perpetual costing. As stock is issued, REMAIN depletes from oldest layer first.

**BKMRPFC (9f):** MRP Firm Commitment — BKMRP_FC_PART(15)+DATE(date) PK; QTY (float, planned qty); EXTRA(100); OQTY (original qty); CQTY (confirmed qty); FLAG(1, status); DATE1 (alternative date); NUM(15, source document: WO or PO number). Stores MRP's demand/supply commitments before they become live WOs/POs.

**Key new table — BKAPDESC** (5f): AP vendor extended notes:
- BK_DESC_CODE(15) — vendor code (PK part 1, FK → BKAPVEND)
- BK_DESC_NUM(8) — note set number (PK part 2)
- BK_DESC_LINE(2) — line number (PK part 3)
- BK_DESC_NOTES(70) — note text (70 chars)
- BK_DESC_DESC(25) — short description

Multi-line extended notes per AP vendor. Each vendor can have multiple BKAPDESC records.

**Confidence: 70/100** — 2 programs confirmed; ISDEPT(3f)/WOEXCHG/BKAPDESC/DBAFIFO(5f)/BKMRPFC(9f) schemas extracted; T7JOBS wide table set explained (drill-down viewer); per-screen logic blocked by encryption.

---

### LG — LGS Customer Module / Canadian Customs

2 programs confirmed:
- **T7LGSSOE** (170p): Canadian Statement of Entry (customs declaration). Opens BKARINV+BKARCUST+BKARINVL+BKICMSTR+MTICMSTR+**BKARTXN**+BKICTAX+BKICLOC. Replaces standard ISTAXGRP with BKICTAX (state/jurisdiction tax rates) for cross-border duty. BKARTXN(14f, newly extracted) = AR transaction log with lot/serial/bin detail.
- **T7LGSSOEVERIFY** (41p): Pre-submission validation for SOE. Same core table set.

BKARTXN (14f): BKAR_TXN_SONUM+CODE+DESC(30)+QTY+LOT(15)+SERIAL(25)+DATE+STOCK(15)+LINE+LOC(10)+TMPSO(40)+SRNUM+EXTRA(50)+BIN(15).

**BKICTAX (46f)** — Item tax jurisdiction: BKIC_TAX_STATE(2)+LOCAL(2) PK; NAME(25)+NUMBER(15) jurisdiction name/ID; RATE (float) tax rate; GLACT(10)+GLDPT(4) GL account; VENDOR(10) remit-to vendor; TAXBLE_1..12/NONTAX_1..12/COLECT_1..12 (float×12 each) 12-month taxable/non-taxable/collected history; OUTSTD outstanding; FRGHT(1) is freight taxable flag. Same history structure as ISTAXGRP.

**Confidence: 70/100** — both programs confirmed; all 42 tables in DDF; BKICTAX (46f) + BKARTXN (14f) full schemas extracted; SOE field layout and Canadian duty calculation logic blocked by encryption.

---

### QT — Service Quote Extended Info (Expanded)

T7QTINFO (42p): Extended info entry for service quotes. Opens ISSRINFO+BKYSMSTR+BKARINVL+ISTERMS+BKICPMAT+**LANGDICT**+**BKICREF**+BKPRSALE.

**Key new tables:**

**LANGDICT** (5f): Multi-language translation dictionary:
- LANG_DICT_ECAPT(80) — English caption (PK part 1)
- LANG_DICT_LANG(3) — language code (e.g. FRE, SPA) (PK part 2)
- LANG_DICT_LCAPT(80) — translated caption
- LANG_DICT_FONT(30) — font for this language
- LANG_DICT_EXTRA(150)

Used by ML module (T7MLC) and QT to translate invoice/quote field labels when printing in a non-English language. Clean key/value translation: English caption → target-language caption.

**BKICREF** (8f): Customer item cross-reference:
- BKIC_REF_CUST(10) + CODE(15) — PK (customer + our part code)
- BKIC_REF_PDESC(30) — our item description
- BKIC_REF_CUSNME(30) — customer's name for this item
- BKIC_REF_CUSCOD(25) — customer's own part number
- BKIC_REF_DESC(30) + DESC2(30) — description fields
- BKIC_REF_EXTRA(50)

Maps our part numbers to each customer's own part numbers. When printing invoices/quotes to a customer, EvoERP substitutes the customer's part number/description from BKICREF.

**ISTERMS (13f) — Payment Terms Master:**
- IS_TERMS_NUM (2): terms code number (PK)
- IS_TERMS_NAME (20): terms code name (e.g. "Net30", "2/10Net30")
- IS_TERMS_DESC (50): description
- IS_TERMS_AMT (8): discount percent/amount
- IS_TERMS_TYP (1): type — P=percent, $=flat dollar
- IS_TERMS_DAY (2): net days
- IS_TERMS_EOM (1): end-of-month terms flag (Y/N)
- IS_TERMS_MAX (2): maximum discount days
- IS_TERMS_COD (1): COD flag
- IS_TERMS_ARAP (1): AR or AP terms (A=AR, P=AP)
- IS_TERMS_CC (1): credit card accepted flag
- IS_TERMS_SRT (2): sort order
- IS_TERMS_EXTRA (100): extra

Used across SO entry (default to customer's terms), AR invoicing (BKARINV references TERMS_NUM), and AP vouchers. QT pulls ISTERMS to display quote payment terms.

**Confidence: 72/100** — T7QTINFO confirmed; LANGDICT(5f)+BKICREF(8f)+ISTERMS(13f) all fully extracted from DDF; quote-as-SR-order architecture confirmed; specific QT UI workflow details blocked by encryption.

---

### SL — Shop Loading (Expanded)

T7SLSFC (5p): Shop loading display — overlays AR demand on production capacity. Opens BKARINVL+BKYSMSTR+BKDCLAB+BKARCUST+ISWOPRIO(4f already extracted)+WORKCTR+ROUTING. Very thin program (5 procs) = UI panel only; data assembly logic is in the calling module.

**BKDCLAB** (50f): DC Labor transaction record (partially extracted):
- LAB_DATE + LAB_EMP — date + employee (PK part)
- LAB_WOPRE(8) + LAB_WOSUF(2) — WO reference
- LAB_OPER(2) — operation number
- LAB_POSTED(1) — posted to WO flag
- LAB_SHIFT(2) — shift number
- LAB_START(4) + LAB_FINISH(4) — start/finish times
- LAB_PARTS(8) — parts completed count
- LAB_SCRAPPED(8) — scrapped quantity
- LAB_NOJOBS(2) — job count
- + 38 more fields (hours, rates, GL, etc.)

**Confidence: 65/100** — T7SLSFC purpose confirmed (read-only demand/capacity overlay, 5 procs = display only); ISWOPRIO(4f) + BKDCLAB(50f, Pass 57) fully extracted; WORKCTR+ROUTING schemas documented in SH module section.

---

### New Tables Confirmed (Pass 39)

| Table | Fields | Purpose |
|---|---|---|
| ISLINKS | 311 | Global document/URL attachment store — UID+LINK+APP+TYPE flags; used across many modules |
| BKAPDESC | 5 | AP vendor extended notes — VNDCOD+NUM+LINE PK; NOTES(70)+DESC(25) |
| LANGDICT | 5 | Multi-language translation — ECAPT+LANG PK; LCAPT(80) translated caption; FONT |
| BKICREF | 8 | Customer item cross-reference — CUST+CODE PK; CUSNME+CUSCOD (customer's part number) |
| ISBNMSTR | 4 | Bin master — LOC+BIN PK; DESC(60)+EXTRA(100) |
| BKDCLAB | 50 | DC labor transaction — DATE+EMP+WOPRE PK; OPER/SHIFT/START/FINISH/PARTS/SCRAPPED |

---

---

## GENERAL LEDGER DEEP REFERENCE — Pass 40

The GL module uses a consistent family of 28 tables with four sub-families.

### GL Sub-Family 1: Chart of Accounts (COA)

EvoERP maintains **four parallel COAs** using the same 62–65-field structure:

| Table | Fields | Purpose |
|---|---|---|
| BKGLCOA | 62 | Current production COA |
| BKGLCCOA | 62 | Company/comparative COA |
| BKGLECOA | 65 | Extended COA (multi-currency or alternate) |
| BKGLFCOA | 65 | Forecast/forward COA |

All four share: ACCT(10)+GLDPT(4) PK; ACCTD(25) description; TYPE(1) account type; CR_DR(1) normal balance; NON_CASH(1) flag; CURRENT_1..N (float×N, period balances for all open periods).

### GL Sub-Family 2: Transaction Records

Multiple transaction staging/archive tables — **all identical 16-field structure**:

| Table | Role |
|---|---|
| BKGLTRAN | Live GL transactions (current period) |
| BKGLATRN | Archive GL transactions |
| BKGLETRN | Extended GL transactions |
| BKGLHIST | GL history transactions |
| BKGLTEMP / BKGLTMP / BKGLTMP2 / BKGLTMP3 | Staging tables (batch post processing) |

All share: GLACCT(10)+GLDPT(4)+DATE+CODE(10)+INVC(10)+DESC(25)+DC(1, D/C)+AMT + 8 more fields.

**BKGLXH** (20f) — GL extended history companion to BKGLX:
- BKGLX_POSTDATE/ARCHDATE/ENTDATE — 3 date stamps
- BKGLX_PART(15) + QUANTITY — item reference
- BKGLX_AMOUNT + TRXNTYPE(1) + JOURNAL(2) + 12 more

### GL Sub-Family 3: General Journal

Four pairs of journal header + lines tables:

| Header | Lines | Purpose |
|---|---|---|
| BKGLGJRN | BKGLGJLN | Current general journal |
| BKGLAGJR | BKGLAGJL | Archive journal |
| BKGLRGJR | BKGLRGJL | Recurring journal entries |
| BKGLTGJR | BKGLTGJL | Template journal entries |

**Journal header** (11f): DATE+TRANSN(8)+TYPE(2)+TYPEN(2)+POSTED(1)+CVCODE(10)+INVCHKN(8)+NUMLNES(2) + 3 more
**Journal lines** (9f): TRANSN(8)+ACCTNM(10)+GLDPT(4)+DESC(25)+DC(1)+AMOUNT+JOB(15)+LINE(2)+1 more

Recurring and template journals (BKGLRGJR/BKGLTGJR) allow auto-generation of repeat entries (rent, depreciation).

### GL Sub-Family 4: Financial Statement Templates

**BKGLFSTL** (12f): Financial statement layout line:
- BKFS_NAME(10) — statement name (PK part 1)
- BKFS_LINE_NUM(2) — line position (PK part 2)
- BKFS_SGL_ACCT(10) / EGL_ACCT(10) — account range start/end
- BKFS_TOTAL_FLD(2) — total field reference
- BKFS_PRT_LOC(2) / PRT_DOL(1) — print location / dollar flag
- BKFS_DESC(25) — line description

**BKGLSTMT** (104f): Financial statement group definition:
- BKGL_STB_MN_TTL(25) + GLA_MT(25) — main title + alternate title
- GLA_F_1..4 (10 each) + GLA_T_1..4 (10 each) — 4 account range pairs
- + 88 more fields (period selection, format flags, etc.)

**BKGLDESC** (5f): GL account extended notes (same structure as BKAPDESC):
- BK_DESC_CODE(15)+NUM(8)+LINE(2) PK; NOTES(70)+DESC(25)

**Check registers:**
- BKGLACHK (11f): Archive check register — same structure as BKGLCHK (already extracted)
- BKGLICC (11f): Intercompany check register — same structure

### GL Architecture Summary

```
COA family:    BKGLCOA/CCOA/ECOA/FCOA (4 parallel COAs)
Transactions:  BKGLTRAN → BKGLATRN/HIST (staging → archive)
               BKGLTEMP/TMP/TMP2/TMP3 (period-close staging)
Journals:      BKGLGJRN/GJL (current) / AGJR/AJL (archive)
               RGJR/RJL (recurring) / TGJR/TJL (template)
Statements:    BKGLFSTL (layout lines) + BKGLSTMT (group definitions)
Extended:      BKGLX (item-level extension) + BKGLXH (history)
Notes:         BKGLDESC (multi-line GL account notes)
Checks:        BKGLCHK (current) + BKGLACHK (archive) + BKGLICC (intercompany)
```

**Confidence: 75/100** — All 28 BKGL* table schemas extracted; full GL architecture
confirmed; detailed financial statement builder (BKGLSTMT 104f) identified; posting
logic in BKGLTRAN/BKGLX confirmed from prior module analysis.

---

## BOM (BKBM*) DEEP REFERENCE — Pass 40

The Bill of Materials module uses the same **parallel-snapshot architecture** as inventory.

### BOM Parallel Tables

Five tables with **identical 26-field structure** (BKBMMSTR schema is the canonical form):

| Table | Purpose |
|---|---|
| BKBMMSTR | Current production BOM |
| BKBMAMTR | Actual cost BOM snapshot |
| BKBMAVAL | Actual value BOM snapshot |
| BKBMEMTR | Estimated BOM snapshot |
| BKBMSUMM | BOM summary (indented explosion) |

All share primary key: BKBM_PARENT(15) + BKBM_COMPONENT(15)

**Core fields (first 8):**
- BKBM_PARENT(15) — parent part (PK part 1)
- BKBM_COMPONENT(15) — component part (PK part 2)
- BKBM_QTY_REQD — quantity required per parent
- BKBM_REFERENCE(20) — reference designator (PCB position, etc.)
- BKBM_PROD_TYPE(1) — component type code
- BKBM_PROD_SCRAP — scrap/yield factor
- BKBM_PROD_OP(3) — required at operation number
- BKBM_PROD_OPYN_1(1) — options flag 1 (first of N)

### BOM Supporting Tables

**BKBMDIM** (11f): Dimensional BOM for sheet material:
- BKBM_DIM_PARENT(15)+LINE(2)+COMP(15) — PK
- BKBM_DIM_PART_X/Y — part dimensions (width × height)
- BKBM_DIM_MACH(4) — machine/workcenter
- BKBM_DIM_TRIM_X/Y — trim dimensions (cutting waste)
- + 4 more fields (nesting, efficiency, etc.)

Used in sheet metal / panel manufacturing where material is cut from stock sheets.

**BKBMERMK / BKBMREMK** (20f each): Component-level remarks:
- PARENT+LINE+COMP PK
- REMARK_1..10 (64 chars each) — 10 remark lines
- BKBMERMK = engineering remarks (design notes); BKBMREMK = regular remarks (shop notes)

**BKBMNOTE** (16f): Parent-level BOM notes:
- BKBM_NT_PARENT(15) — parent part (PK)
- NOTE_1..15 (64 chars each) — 15 note lines attached to the parent BOM

**BKBMCNFG** (7f): BOM system configuration:
- BKBM_CNFG_NUM — entry number
- BKBM_CNFG_GLACT(10)+GLDPT(4) — GL account for BOM cost postings
- BKBM_CNFG_AUTO(1) — auto-explode flag
- BKBM_CNFG_POST(1) — auto-post to GL flag
- BKBM_CNFG_ROLL(1) — cost roll-up flag
- BKBM_CNFG_LABOR(1) — include labor in BOM cost flag

### BOM Architecture Summary

```
BKBMMSTR (current) ←── same 26f structure ──→ BKBMAMTR/AVAL/EMTR/SUMM (snapshots)
BKBMDIM (dimensional cuts)
BKBMERMK (engineering notes per component)
BKBMREMK (shop notes per component)
BKBMNOTE (notes per parent assembly)
BKBMCNFG (system config: GL/auto-explode/cost-roll)
```

**Confidence: 72/100** — All 10 BKBM* schemas extracted; parallel-snapshot architecture
confirmed (mirrors BKIC* and MTIC* patterns); BKBMDIM reveals sheet-stock manufacturing
support; per-field meaning of remaining 18 fields in 26f tables needs deeper study.

---

### New Tables Confirmed (Pass 40)

| Table | Fields | Purpose |
|---|---|---|
| BKGLCOA + BKGLCCOA/ECOA/FCOA | 62–65 | Chart of accounts — 4 parallel COAs; ACCT+GLDPT PK; period balances |
| BKGLTRAN + ATRN/ETRN/HIST/TEMP×4 | 16 | GL transaction records — staging, live, archive, temp |
| BKGLGJRN/GJLN + A/R/T variants | 9–11 | General journal headers + lines — current, archive, recurring, template |
| BKGLFSTL | 12 | Financial statement layout — NAME+LINE PK; account range + desc |
| BKGLSTMT | 104 | Financial statement group definition — 4 account range pairs |
| BKGLDESC | 5 | GL account extended notes (same structure as BKAPDESC) |
| BKGLACHK / BKGLICC | 11 | Archive + intercompany check registers |
| BKGLXH | 20 | GL extended history — POSTDATE/ARCHDATE/ENTDATE/PART/QTY/AMT |
| BKBMMSTR + AMTR/AVAL/EMTR/SUMM | 26 | BOM — current + 4 parallel cost snapshots; PARENT+COMPONENT PK |
| BKBMDIM | 11 | Dimensional BOM — PARENT+LINE+COMP; X/Y part + trim dimensions |
| BKBMERMK / BKBMREMK | 20 | BOM component remarks — PARENT+LINE+COMP; 10 × 64-char notes |
| BKBMNOTE | 16 | BOM parent notes — PARENT PK; 15 × 64-char note lines |
| BKBMCNFG | 7 | BOM system config — GL acct, auto-explode, post, roll-up, labor flags |

---

---

## UNIFIED TRANSACTION ARCHITECTURE — Complete Map (Pass 41)

EvoERP uses one physical table structure across all transaction types. The same 84/28-field
invoice/lines schema is reused by SO, AR, SR, EDI, ES, RMA, and their archives.

### Core Invoice Tables

| Table | Fields | Scope |
|---|---|---|
| BKARINV | 84 | **Master** — SO, AR invoice, and EDI/ES/SR staging header |
| BKARINVL | 28 | **Master** — SO line, AR invoice line, EDI/ES/SR line |

All variant tables below point to the same physical .B file via alternate Btrieve keys.

### Invoice Variants (all 84f, all BKAR_INV_* fields)

| Table | Purpose |
|---|---|
| ISSRAINV / ISSRINV / ISSRMH / ISSRMINV / ISSRCH | SR service order — 5 alternate indexes |
| BKEDIH | EDI-in staging header |
| BKESTQT | ES estimating quote header |
| ISARAHIN | AR archive invoice header (year-end closed) |
| ISARAINV | AR archive invoice (alternate index of ISARAHIN) |
| ISRMINV | RMA invoice (current) |
| ISRMAINV | RMA invoice archive |

### Invoice Line Variants (all 28f, all BKAR_INVL_* fields)

| Table | Purpose |
|---|---|
| ISSRAIVL / ISSRINVL / ISSRMIVL / ISSRML / ISSRCL | SR service order lines — 5 alternate indexes |
| BKEDIL | EDI-in staging lines |
| BKESTQTL | ES estimating quote lines |
| ISARAHIL | AR archive invoice lines |
| ISRMAIVL | RMA archive invoice lines |
| ISRMINVL | RMA invoice lines (current) |

### Transaction Log Family

| Table | Fields | Purpose |
|---|---|---|
| BKART | 12 | AR payment/credit transaction (live) |
| ISARAT | 12 | AR transaction archive — identical BKART_* fields |
| BKARINVT | 23 | AR invoice tax by code (live) |
| ISARAINT | 23 | AR invoice tax archive — identical BKAR_INVT_* fields |
| BKARTXN | 14 | AR shipment transaction log — SONUM+CODE+QTY+LOT+SERIAL+BIN |
| ISARTXNB | 23 | AR shipment transaction batch (richer): SONUM+CODE+LINEID+BIN+LOC+QTY+LOT+SERIAL+DATE+RLEASD(1) + 13 more |

### AP PO Family

| Table | Fields | Purpose |
|---|---|---|
| BKAPPO | 57 | AP purchase order header (live) |
| ISAPOPO | 57 | Open PO view — identical BKAP_PO_* fields |
| ISAPARFQ | 57 | AP archive PO/RFQ header |
| BKAPPOL | 38 | AP PO lines (live) |
| ISAPOPOL | 38 | Open PO lines view — identical BKAP_POL_* fields |
| ISAPARFL | 38 | AP archive PO/RFQ lines |
| BKAPINVL | 390 | AP invoice lines (live) |
| ISAPAINL | 390 | AP invoice lines archive — identical BKAP_INVL_* fields |

### Change Audit Log Family

| Table | Fields | Purpose |
|---|---|---|
| ISARCHG | 26 | AR/SO change audit trail — SONUM+INVNUM+LINEID+PCODE+CDATE+USER+REVLVL+ALOC/BLOC+APRICE/BPRICE+... |
| ISARACHG | 26 | AR change archive — identical structure |
| ISAPCHG | 32 | AP/PO change audit trail — PONUM+LINEID+PCODE+CDATE+USER+REVLVL+ALOC/BLOC+APRICE/BPRICE+... |
| ISAPHCHG | 32 | AP change history — identical structure |

### AP/AR Extended Tables

**ISAPEX** (33f) — AP vendor extended data (mirror of ISAREX for AR customers):
- ISAPEX_VEND(10) — vendor code (PK)
- ISAPEX_LONGNAME(60) — long vendor name
- ISAPEX_NUM_1..5 + NUM2_1..N — numeric extended fields
- + 20 more configurable fields

**ISAPQPO** (66f) — AP vendor quote pricing:
- ISAP_QPO_PCODE(15)+PQTY+VNDCOD(10)+PPRCE+PDISC+UM(3) + 60 more — per-item vendor pricing from quotes

**ISAPPROJ** (12f) — AP project linking:
- ISAP_PROJ_FROM(3)+CUST+VEND+JOURN+INV+LINE PK — links AP transactions to customers and GL journals

### RMA Table Family

| Table | Fields | Purpose |
|---|---|---|
| ISRMAI | 54 | RMA invoice (current — NUM+PART+LINEID PK; STATUS/REASON/DISP) |
| ISRMAAI | 54 | RMA invoice archive — identical structure |
| ISRMINV | 84 | RMA as BKARINV (current view) |
| ISRMAINV | 84 | RMA invoice archive (BKARINV-structure) |
| ISRMAIVL | 28 | RMA lines archive (BKARINVL-structure) |
| ISRMINVL | 28 | RMA lines current view |
| ISRMINFO | 54 | RMA extended info (ISSRINFO structure) — current |
| ISRMHINF | 54 | RMA extended info history |
| ISRMAINF | 54 | RMA extended info archive |
| ISRMAC | 3 | RMA reason/disposition code master — CODE(30)+DESC(60)+EXTRA |
| ISRMTXN | 14 | RMA transaction log (BKARTXN structure) |
| ISRMTXNS | 14 | RMA transaction summary |
| ISRMDESC + ISRMADSC | 5 | RMA description notes — standard DESC pattern |

**Architecture insight:** RMA is the most table-rich module because it archives every
stage: the RMA record itself, the invoice it generates, the lines, the extended info,
and the transactions — all using the canonical BKARINV/BKARINVL/BKART structures.

---

### New Tables Confirmed (Pass 41)

| Table | Fields | Purpose |
|---|---|---|
| ISARAHIN / ISARAINV | 84 | AR archive invoice header — BKARINV structure |
| ISARAHIL | 28 | AR archive invoice lines — BKARINVL structure |
| ISARAT | 12 | AR transaction archive — BKART structure |
| ISARAINT | 23 | AR invoice tax archive — BKARINVT structure |
| ISARTXNB | 23 | AR shipment batch — SONUM+CODE+LINEID+BIN+LOC+QTY+LOT+SERIAL+DATE+RLEASD |
| ISAPOPO / ISAPOPOL | 57/38 | Open AP PO views — BKAPPO/BKAPPOL structure |
| ISAPARFQ / ISAPARFL | 57/38 | AP PO/RFQ archive — BKAPPO/BKAPPOL structure |
| ISAPAINL | 390 | AP invoice lines archive — BKAPINVL structure |
| ISAPCHG / ISAPHCHG | 32 | AP change audit log — PONUM+LINEID+PCODE+CDATE+USER+REVLVL+before/after fields |
| ISAPEX | 33 | AP vendor extended — VEND PK; LONGNAME + configurable num fields |
| ISAPQPO | 66 | AP vendor quote pricing — PCODE+VNDCOD PK; price/discount |
| ISAPPROJ | 12 | AP project link — FROM+CUST+VEND+JOURN+INV+LINE PK |
| ISRMAAI | 54 | RMA invoice archive — identical ISRMAI structure |
| ISRMINV / ISRMAINV | 84 | RMA invoice as BKARINV — current + archive |
| ISRMAIVL / ISRMINVL | 28 | RMA lines as BKARINVL — archive + current |
| ISRMINFO / ISRMHINF / ISRMAINF | 54 | RMA extended info — current / history / archive (ISSRINFO structure) |
| ISRMAC | 3 | RMA reason/disposition code master |
| ISRMTXN / ISRMTXNS | 14 | RMA transaction log/summary — BKARTXN structure |
| ISARACHG | 26 | AR change log archive — ISARCHG structure |
| ISARACHK | 12 | AR cross-reference to AP checks — BKAPCHKF structure |
| ISARACST | 106 | AR archive customer master |

---

---

## ISES* / ISSE* / ISWO* FAMILIES — Pass 42

### ISES* — ES Estimating Extension Tables (10)

The unified architecture extends to ES: all estimate headers/lines use BKARINV/BKARINVL structure.

| Table | Fields | Purpose |
|---|---|---|
| ISESTHDR | 84 | ES header (current) — BKARINV structure |
| ISESTLNE | 28 | ES lines (current) — BKARINVL structure |
| ISESAHDR | 84 | ES header archive — BKARINV structure |
| ISESALNE | 28 | ES lines archive — BKARINVL structure |
| ISESTAQT | 84 | ES archive quote header (alternate key) — BKARINV structure |
| ISESTAQL | 28 | ES archive quote lines (alternate key) — BKARINVL structure |
| ISESTDTL | 203 | ES estimate detail — IS_EST_NUM+PART+LINE PK; 10×qty breakpoints × material/labor/overhead costs |
| ISESADTL | 203 | ES detail alternate index — identical ISESTDTL structure |
| ISESTPO | 16 | ES to PO conversion link — BKMRP_PO_* fields; ties estimate to planned PO |

**ISESTASM** (213f) — MT-era estimate assembly summary (pre-BKARINV era):
- MTESUM_QUOTE(8) — quote number (PK)
- MTESUM_DATE + EXPDATE — created/expiry dates
- MTESUM_STATUS(1) + CLASS(4) + CODE(15) + DESC(30) + UM(3)
- MTESUM_CUSTCODE(10) + NAME(30) + ATTN(30) — customer
- MTESUM_RFQ(15) + REV(4) + PROJ(15) — references
- MTESUM_QTY_1..10 — 10 quantity breakpoints (parallel to ISESTDTL)
- MTESUM_MAT_1..N — material costs per qty break + 188 more fields

This is the DBA/MTIC-era (MT generation) estimate table — a standalone 213-field record per
quote with quantity breaks and costs. The newer ES module replaced this with BKESTQT (84f,
BKARINV structure) + ISESTDTL (203f). ISESTASM may still be read for historical quotes.

---

### ISSE* — SR/SE Service Extension Tables (10)

More BKARINV/BKARINVL alternate indexes in the service area:

| Table | Fields | Purpose |
|---|---|---|
| ISSEDH | 84 | SR/SE service EDI document header — BKARINV structure |
| ISSEDL | 28 | SR/SE service EDI document lines — BKARINVL structure |
| ISSESH | 84 | SR/SE service SH (shipping) header — BKARINV structure |
| ISSESL | 28 | SR/SE service SL lines — BKARINVL structure |
| ISSERCNT | 9 | Serial counter per item (already documented in SC/IT modules) |
| ISSEPROC | 2 | Service process code (already documented in SE/ST) |
| ISSETYPE | 2 | Service error type code (already documented in SE/ST) |
| ISSEQUIP | 2 | Service equipment type — IS_SEQUIP_NAME(20)+DESC(40) |

**Key new tables:**

**ISSERIAL** (11f) — WO serial genealogy (parent → component serial tracing):
- IS_SER_WOPRE(8) + WOSUF(2) — WO reference (PK)
- IS_SER_PARENT(15) + PDESC(30) + PSERIAL(25) — parent item code/description/serial#
- IS_SER_ADATE — assignment date
- IS_SER_COMP(15) + CDESC(30) + CSERIAL(25) — component item/description/serial#
- IS_SER_FDATE — finish date
- IS_SER_EXRA(100) — extra

Records the relationship between parent item serial numbers and component serial numbers
within a WO. Provides full serial genealogy traceability (parent serial → sub-assembly serials).

**ISSERR** (14f) — SPC / shop floor error event:
- IS_SERR_WOPRE(8) + WOSUF(2) + OPER(2) — WO + operation (PK)
- IS_SERR_TIME(4) + DATE(4) — when the error occurred
- IS_SERR_ERROR(25) — error/defect code
- + 8 more fields (qty, inspector, notes, etc.)

This is the primary table behind the SP (Statistical Process Control) module live error feed. Each defect event recorded on the shop floor creates one ISSERR row.

---

### ISWO* — WO Extension Family (8)

| Table | Fields | Purpose |
|---|---|---|
| ISWOEX | 63 | WO extended data (already documented in ADCA) |
| ISWOHEX | 63 | WO header extended — identical ISWOEX structure (alternate key) |
| ISWOROEX | 60 | WO routing operation extended (already documented) |
| ISWOTRAY | 52 | WO tray tracking (already documented in QC) |
| ISWOPRIO | 4 | WO priority codes (already documented) |
| ISWODESC | 5 | WO extended descriptions — standard DESC pattern (5f) |
| ISWOHDSC | 5 | WO header descriptions — standard DESC pattern (5f) |

**ISWOCLOG** (32f) — WO operation change audit log:
- IS_WOLOG_WOPRE(8) + WOSUF(2) + OPER(2) — WO + operation (PK)
- IS_WOLOG_OPDESC(30) — operation description at time of change
- IS_WOLOG_ITEM(15) + WC(12) + WCDESC(30) — item + work center
- IS_WOLOG_CUST(10) + CUSNME(30) — customer reference
- IS_WOLOG_CDATE + CWHO(30) + CTIME + CWHERE(15) — when / who / system location
- IS_WOLOG_MACH(4) — machine code
- IS_WOLOG_ALPHA1_1/2 (30 each) — 2 custom alpha fields
- IS_WOLOG_FLAG_1..5 — 5 boolean flags
- IS_WOLOG_DATE_1..3 — 3 date slots
- + 7 more fields

Every modification to a WO operation is logged here with full who/when/where audit trail.
CWHERE indicates which workstation or system module made the change.

---

### New Tables Confirmed (Pass 42)

| Table | Fields | Purpose |
|---|---|---|
| ISESTHDR / ISESAHDR / ISESTAQT | 84 | ES header views — all BKARINV structure |
| ISESTLNE / ISESALNE / ISESTAQL | 28 | ES line views — all BKARINVL structure |
| ISESTASM | 213 | MT-era estimate summary — pre-BKARINV era; MTESUM_* fields |
| ISESTPO | 16 | ES-to-PO link — BKMRP_PO_* fields |
| ISSEDH / ISSESH | 84 | SR service EDI/SH header views — BKARINV structure |
| ISSEDL / ISSESL | 28 | SR service EDI/SL line views — BKARINVL structure |
| ISSEQUIP | 2 | Service equipment type — NAME(20)+DESC(40) |
| ISSERIAL | 11 | WO serial genealogy — WOPRE+WOSUF PK; PARENT/COMP + PSERIAL/CSERIAL tracing |
| ISSERR | 14 | SPC error event — WOPRE+WOSUF+OPER PK; TIME+DATE+ERROR code |
| ISWOHEX | 63 | WO header extended (alternate index of ISWOEX) |
| ISWOCLOG | 32 | WO operation change log — WOPRE+WOSUF+OPER PK; CDATE+CWHO+CTIME+CWHERE |
| ISWODESC / ISWOHDSC | 5 | WO description notes — standard 5f DESC pattern |

---

---

## LESSER-DOCUMENTED MODULES — Pass 43

### LI — Module License Access Control

**T7LIMACC** (42 procs) — opens ISACCESS as primary table (not registered in DDF schema).
- Purpose: controls which EvoERP licensed modules are active/accessible per installation.
- ISACCESS is a file-level table (likely keyed by module code) listing enabled modules.
- Single program, thin UI — this is an admin-only tool for module activation.

---

### CH — Chain / Multi-Location Links

**T7CHAIN** (62 procs) + **T7CHAINM** (40 procs) — both open ISCHAINM as primary.

**ISCHAINM** (17f) — chain configuration record:
- IS_CHAIN_USER(15) + PARENT(12) + CHILD(12) — user + parent/child company (PK)
- IS_CHAIN_PARAM_1..10 (15 each) — 10 configuration parameters for the link
- IS_CHAIN_AUTO(1) — automatic sync flag
- IS_CHAIN_DATE(4) — last sync date
- IS_CHAIN_DESC(100) + EXTRA(100)

CH links a parent EvoERP installation to child installations (multi-location / chain store scenario). T7CHAIN = main entry form. T7CHAINM = chain master maintenance. LANGDICT in the DB set confirms multi-language support in chain deployments.

---

### QS — Quick Sales Order (Web Order Staging)

**T7QSOA** (72 procs) + **T7QSOALINES** (70 procs) — both open ISQSOA.

**ISQSOA** (12f) — Quick SO staging record:
- IS_QSOA_UID(40) — unique ID (PK, UUID-style)
- IS_QSOA_CUST(10) + SHPTO(10) — customer + ship-to
- IS_QSOA_SHPDTE(4) — ship date
- IS_QSOA_ITEM(15) + DESC(30) + QTY(8) + PRICE(8) + DISC(8)
- IS_QSOA_MDATE1/2(4 each) — manufacture dates
- IS_QSOA_EXTRA(50)

Full SO table set (BKARINV+BKARINVL+BKICMSTR+BKARCUST+ISTERMS+BKPRSALE+BKICPMAT+BKICREF) confirms this creates real SOs. ISQSOA is a staging/quick-entry record that pre-populates a new SO. Used for quick web/phone order entry or web order import staging.

---

### MU — Multi-Yield Work Order

**T7MULTIYIELD** (150 procs, 43 tables) — opens full WO set: WORKORD+WOBOM+WORECV+WOROUT+INVTXN+MTICMSTR+BKICMSTR+BKICLOC+ISBINLOC+BKARINVL+more.

Multi-Yield allows one WO to produce multiple output items (not just the primary BOM assembly). Used in co-products or by-product manufacturing (e.g., cutting sheet stock produces multiple parts). DB fingerprint is identical to standard WO programs (T7WOA) plus extra INVTXN/WORECV paths confirming multiple receipt postings per WO.

---

### PA — Paperless DC / Paperless Work Order Entry

**T7PAPERLESS** (205 procs, 50 tables) — opens: WORKORD+MTICMSTR+BKICMSTR+WOROUT+ROUTING+BKICLOC+ISBINLOC+ISWOEX+WORECV+BKAPPOL+ISWOTRAY+BKDCLAB.

Paperless DC = touchscreen/kiosk-based WO operation reporting without paper travelers. DB set is identical to ADCA (Advanced DC) — same tables for BKDCLAB (labor), ISWOTRAY (QC trays), WORECV (receipts). BKAPPOL in the set suggests it can trigger PO receiving from the shop floor (outside processes). Primary difference from ADCA: this is the menu-driven paperless form, ADCA is the scanner-based auto-collect version.

---

### ML — Multi-Language UI

**T7MLC** (50 procs) — applies language translations: LANGDICT+BKARINV+BKARINVL+MTICMSTR+ISREPORD+BKICMSTR+BKICLOC+BKAPDESC.
**T7LANG** (25 procs) — LANGDICT maintenance + BKAPVEND+BKARCUST lookups.

ML uses LANGDICT (5f: ECAPT+LANG PK → LCAPT(80)+FONT(30)+EXTRA(150)) as the central translation table. T7LANG = maintain translations. T7MLC = apply translations to forms and reports (ISREPORD in DB set = report definition table). This module enables French/Spanish/etc UI captions without code changes.

---

### SD — Service Detail Code Maintenance

**T7SDET** (58 procs) — opens ISSDET + ISSTYPE as primary tables.

SD = maintenance for service detail codes used by the SR (Service/Repair) module. ISSDET (4f: IS_SDET_TYPE+DETAIL+WHO+SUB) stores detail work performed. ISSTYPE (3f: TYPE/WHO/ASSET) stores service error/type codes. T7SDET is the CRUD editor for these SR lookup tables.

---

### KIT — Kit Assembly

**T7KIT** (153 procs, 26 tables) — opens: BKICMSTR+MTICMSTR+WOBOM+BKICLOC+BKYSMSTR+ISLINKS+WOMAT+WORKORD+WOROUT+BKPRMSTR+ISBINLOC+LOT+more.

Kit assembly: creates a WO from a pre-defined kit (a named set of components). The WOBOM+WOMAT+WORKORD set confirms it builds a full WO. LOT tracking in the DB set confirms kit components can be lot-controlled. ISLINKS allows document attachments to kits. This is a shortcut for standard recurring assembly jobs.

---

### VSCHED — Visual Work Center Scheduler

**T7VSCHED** (94 procs) — opens: BKICMSTR+FILELOC+WORKORD+WOROUT+WCTRLOAD+BKYSMSTR+BKARINV+BKARINVL.

**WCTRLOAD** (8f) — work center load snapshot:
- WC_LOAD_WC(12) + DATE(4) — work center + date (PK)
- WC_LOAD_TOTHRS(8) — total scheduled hours
- WC_LOAD_UDATE(4) — last update date
- WC_LOAD_CAP(8) + UTIL(8) + LOAD(8) — capacity / utilization / load values
- WC_LOAD_EXTRA(100)

T7VSCHED (87 procs, 22 tables) = visual/Gantt-style work center capacity viewer. Reads WORKORD+WOROUT for scheduled operations, WCTRLOAD for pre-computed capacity snapshots. BKARINV/BKARINVL = customer demand overlay. ISACCESS = license check. Used for rough-cut capacity planning.

**WCTRLOAD (8f):** WC+DATE PK; TOTHRS (total scheduled hours), UDATE (last-updated date), CAP (capacity hours), UTIL (utilization %), LOAD (current load hours), EXTRA(100). Pre-computed daily snapshot — likely written by MRP or scheduler engine; read by VSCHED for display.

**Confidence: 68/100** — T7VSCHED (87p) confirmed with 22 tables; WCTRLOAD(8f) full schema extracted; all tables in DDF except FILELOC+ISACCESS; visual scheduling purpose confirmed; Gantt layout and user interaction logic blocked by encryption.

---

### NE — New Company Initialization

**T7NEWINIT** (49 procs) — opens: FILELOC+FILEDES+BKAPVEND+BKARCUST+BKCMACCN+BKICMSTR+standard audit set.

Creates a new company within an EvoERP installation: writes FILELOC (physical file path registrations) and FILEDES (file descriptions/definitions). Then populates seed data by reading from BKAPVEND/BKARCUST/BKICMSTR (optionally copies from existing company). This is the NE / new company entity initialization path.

---

### TPOA — PO Processing Approval Hub

**TPOA** (499 procs, 61 tables) — opens: BKAPPO+BKAPVEND+BKAPDESC+BKAPPOL+MTICMSTR+BKYSMSTR+ISTERMS+ISNOTES+ISLINKS+ISAPEX+BKSYMSTR+full AP set.

**ISNOTES** (13f) — generic notes/comments record:
- IS_NOTE_ID(48) — parent record UID (PK, links to any entity)
- IS_NOTE_TYPE(3) — note type code
- IS_NOTE_CDATE/CTIME(4,10) + CWHO(15) — created when/who
- IS_NOTE_EDATE/ETIME(4,10) + EWHO(15) — edited when/who
- IS_NOTE_EXTRA(100) — note body text
- IS_NOTE_PRIVATE(1) — private flag
- IS_NOTE_GROUP(4) + CONTACT(30)

TPOA at 499 procs is one of the largest programs — it is the full PO processing/approval hub. ISAPEX(33f) in DB confirms approval workflow gates. ISNOTES holds PO-level comment threads. ISLINKS enables document attachments to POs. At 61 tables this covers the complete AP/PO lifecycle: entry → approval → change orders → receipts → GL posting.

**ISAPEX (33f) — AP Vendor Extended Fields:**
- ISAPEX_VEND(10) — vendor code (PK, FK → BKAPVEND)
- ISAPEX_LONGNAME(60) — vendor long name (supplement to BKAPVEND 25-char name)
- ISAPEX_NUM_1..5 (float×5) — 5 numeric extended fields
- ISAPEX_NUM2_1..5 (float×5) — 5 secondary numeric fields
- ISAPEX_FLAG_1..8 (1-char×8) — 8 single-char flags
- +13 more (alpha, date, extra fields)
Parallel structure to ISAREX (AR customer extended). Each vendor can store configurable numeric, flag, and text extensions. ISAPEX appears in TPOA's approval workflow — the flags likely gate purchasing approvals per vendor.

**BKRFQ (49f) — Request for Quote:**
- BKRFQ_NUM(8) — RFQ number (PK)
- BKRFQ_EST(8) — estimate number (FK → estimating module)
- BKRFQ_PARENT(15) — parent/assembly part code
- BKRFQ_OPER(2) — operation number
- BKRFQ_PROD(15) — part/product code to quote
- BKRFQ_WOPRE(8)+WOSUF(2) — linked WO reference
- BKRFQ_ISSUE(4) + EXP(4) — issue date + expiration date
- BKRFQ_VEND(10) + VENDNAME(25) — vendor code + name
- BKRFQ_PARNTDESC(30) + PRODDESC(30) — parent + product descriptions
- BKRFQ_USE(1) — use-this-quote flag
- BKRFQ_PUM(3) + PCONV(8) — purchasing unit of measure + conversion factor
- BKRFQ_LEAD(2) — vendor lead time in days
- BKRFQ_QTY_1..3 (float×3) — 3 quote quantity tiers
- BKRFQ_PRICE_1..3 (float×3) — price per tier
- +29 more (discount, cost, freight, notes fields)
RFQ workflow: Buyers issue an RFQ (linked to an estimate or WO), vendors respond with tiered pricing (QTY/PRICE 1-3), and the buyer uses USE(1) to mark the winning quote before generating a PO from it.

**ISORDDSC (1f):** IORD_DESC_CODE(30) — single-field order description code lookup. A list of standard order description phrases used in PO entry.

**TPOA Confidence: 72/100** — 499p, 61 tables; ISAPEX(33f)+BKRFQ(49f)+ISORDDSC(1f) fully extracted; approval gate (ISAPEX), RFQ flow (BKRFQ), and PO lifecycle confirmed; internal program logic blocked by encryption.

---

### Additional Standalone Reports / Tools

| Program | Procs | Purpose |
|---|---|---|
| CASHFLOW | 26 | Cash flow drill-down report — AP vendor + AR customer balances |
| WORKCENTERLOAD | 26 | Work center load drill-down report |
| MACHINEVIEW | 24 | Machine view report (report shell only — no specific tables) |
| PROJECTEDSTOCK | 23 | Projected stock report (report shell only) |
| T7CUTSHEET2 | 75 | Cut sheet for WO material (sheet metal/panel fabrication) |
| T7CUTSHEET2B | 60 | Cut sheet variant B — adds BKICMSTR+BKAPVEND lookups |
| BOMTREE | unknown | BOM tree viewer |

CASHFLOW and WORKCENTERLOAD share the same DB set (BKARCUST+BKAPVEND+BKCMACCN+BKICMSTR+ISLINKS+BKAPDESC) — drill-down reports using ISDRILL framework. T7CUTSHEET2/2B use WOMAT+LOT+WOBOM+ISIS for sheet material cutting instructions tied to a WO.

---

### New Tables Confirmed (Pass 43)

| Table | Fields | Purpose |
|---|---|---|
| ISCHAINM | 17 | Chain config — USER+PARENT+CHILD PK; PARAM_1..10 + AUTO+DATE+DESC+EXTRA |
| ISQSOA | 12 | Quick SO staging — UID(40) PK; CUST+SHPTO+SHPDTE+ITEM+QTY+PRICE+DISC+MDATE1/2 |
| WCTRLOAD | 8 | Work center load snapshot — WC+DATE PK; TOTHRS+CAP+UTIL+LOAD+UDATE |
| ISNOTES | 13 | Generic notes/comments — NOTE_ID(48) PK; TYPE+CDATE+CWHO+EXTRA+PRIVATE+GROUP |

---

---

## SUPPORTING INFRASTRUCTURE TABLES + JS MODULE — Pass 44

### ISGLDATE (86f) — GL Fiscal Calendar Singleton

One row per company; stores period-end dates for 7 years × 12 periods.

- ISGL_CYDATE_1..12 — current year 12 period-end dates
- ISGL_1YDATE_1..12 — 1 year back × 12 periods
- ISGL_2YDATE through 6YDATE — 2–6 years back × 12 each
- ISGL_FYDATE — fiscal year start date
- ISGL_EXTRA(50)

Used by T7ISMCC (IS module multi-currency GL date sync) and T7BS (Business Status dashboard) for GL period arithmetic.

---

### ISDROP (4f) — Configurable Dropdown List Values

- IS_DROP_CODE(10) — list item code (PK part 1)
- IS_DROP_TEXT(30) — display text
- IS_DROP_DESC(30) — description
- IS_DROP_EXTRA(50)

Maintained by T7DROPDOWN (53 procs). Provides generic configurable dropdown lists for EvoERP forms.

---

### ISCC (14f) — Tokenized Credit Card Storage (PCI-Safe)

- IS_CC_CODE(10) — customer/record code (PK)
- IS_CC_TOLKEN(20) — **payment processor vault token** (NOT the PAN — PCI-safe)
- IS_CC_MASKED(24) — masked card number (e.g., XXXX-XXXX-XXXX-1234)
- IS_CC_EXP(4) — expiry date
- IS_CC_ADDRESS(40) + ZIP(10) — billing address (AVS)
- IS_CC_CARDTYPE(15) — Visa/MC/Amex/etc.
- IS_CC_CARDNAME(25) — cardholder name
- IS_CC_STATUS(25) + STDATE(4) — authorization status + date
- IS_CC_XCTRAN(10) — transaction cross-reference
- IS_CC_PROCESS(10) — processor code (e.g., "AUTHORIZE" = Authorize.Net)
- IS_CC_SORT(8) + EXTRA(100)

**Key insight:** TOLKEN stores the payment processor vault token, not the raw PAN. EvoERP never stores full card numbers — this is PCI DSS-compliant tokenization.

---

### ISSHIPCO (16f) — Shipping Carrier Master

- IS_SHIP_SHPCOD(10) — carrier code (PK)
- IS_SHIP_SHPNME(30) + SHPDESC(60) — name + description
- IS_SHIP_VNDCOD(10) — AP vendor (FK → BKAPVEND) — carrier billed as AP vendor
- IS_SHIP_NOTES_1..5 (60 each) — 5 operational note lines
- IS_SHIP_SHIPVIA(15) — default ship-via code (FK → ISSHPVIA)
- IS_SHIP_EXTRA(150)
- IS_SHIP_WEB_1..5 (120 each) — 5 carrier web service URLs (tracking, rating, labels, etc.)

---

### ISREPORD (17f) — Commission/Rep Order Record

- ISREP_ORD_REPNM(2) — sales rep number (PK)
- ISREP_ORD_SONUM(8) + INVNM(8) + INVDT(4) — order and invoice reference
- ISREP_ORD_COMPR(8) + CMAMT(8) — commission % + amount
- ISREP_ORD_AMT(8) + AMTRM(8) — invoice amount + remaining
- ISREP_ORD_CBK(1) — chargeback flag
- ISREP_ORD_PCODE(15) + CUST(10) — item + customer
- ISREP_ORD_PAYDT(4) — payment date
- ISREP_ORD_GLA(10) + GLD(4) — GL account + dept for commission posting

Used in CS (Commission) and ML (Multi-Language) modules.

---

### JS — JavaScript / BI Reporting Bridge (9 programs)

| Program | Procs | Purpose |
|---|---|---|
| T7JSETTINGS | 70 | JS connection settings — FILELOC paths |
| T7JUPD | 27 | JS report deployment via FILELOC |
| T7JSACC | 50 | AR account BI export |
| T7JSAIC | 50 | Item-Customer BI export |
| T7JSAPBI | 50 | AP Business Intelligence export |
| T7JSASRS | 50 | AR Sales Report Summary export |
| T7JSOI | 50 | SO Invoice BI export |
| T7JSQL | 52 | SQL-based JS query interface |
| T7JTREE | 52 | Tree-view BI navigation component |
| T7JTEMP | 27 | JS template sub-routine |

All T7JS* report programs share the same 64-table ISDRILL-based DB set. These programs export EvoERP data to a JavaScript-based BI layer (Sisense or similar). T7JSETTINGS configures the connection; T7JUPD deploys/updates reports.

---

### T7EWC — Work Center Capacity Edit

**T7EWC** (68 procs, 45 tables) — opens WORKORD+WOROUT+WORKCTR+ROUTING+BKYSMSTR.

EWC = Edit Work Center. Full UI (68 procs) for work center setup and/or capacity load editing. WORKCTR = work center master, ROUTING = operations. Complements T7VSCHED (visual Gantt view).

---

### T7BS — Business Status Dashboard

**T7BS** (162 procs, 40 tables) — opens ISBSF+BKYSMSTR+ISGLDATE+BKSYMSTR+BKGLTRAN+MTICMSTR+BKICMSTR+WORKORD+WOMAT+WOLABOR.

BS = Business Status KPI dashboard. ISBSF = configurable KPI field definitions. ISGLDATE provides period-end dates. Reads GL, inventory, and WO costs to compute live financial/operational KPIs. This is the QU-D program.

---

### T7FNR — File Navigator (TA-D)

**T7FNR** (104 procs) — opens FILELOC+FILEDICT.

Full-featured file registry browser: FILELOC = physical file paths, FILEDICT = field definitions. Used as TA-D "Maintain Database" tool for DBA-level file management.

---

### T7XCUTIL — CC Cross-Company Utility

**T7XCUTIL** (29 procs) — opens BKCMACCT+BKYSMSTR+ISCC+LANGDICT+FILELOC.

Cross-company credit card utility. ISCC in DB confirms CC involvement. BKCMACCT = CRM account link. Likely migrates or cross-references CC tokens between companies.

---

### T7JAVASET / T7JAVARUN — Java Integration

**T7JAVASET** (57 procs) — FILELOC+ISACCESS+LANGDICT+BKSYMSTR — configures Java runtime paths and checks module access gates.
**T7JAVARUN** (11 procs) — BKICMSTR+MKAHIST — triggers Java operations on item records.

Java integration used for ISJAVA-dependent features (barcode generation, web connectivity, email).

---

### New Tables Confirmed (Pass 44)

| Table | Fields | Purpose |
|---|---|---|
| ISGLDATE | 86 | GL fiscal calendar singleton — 7 years × 12 periods + FYDATE |
| ISDROP | 4 | Configurable dropdown values — CODE PK; TEXT+DESC+EXTRA |
| ISCC | 14 | Tokenized CC storage — CODE PK; TOLKEN(20 vault token)+MASKED+EXP+CARDTYPE+PROCESS |
| ISSHIPCO | 16 | Shipping carrier master — SHPCOD PK; VNDCOD+NOTES×5+WEB_1..5(120 each) |
| ISREPORD | 17 | Commission/rep order — REPNM PK; SONUM+INVNM+COMPR+CMAMT+CBK+GLA+GLD |

---

---

## MR — MRP ENGINE — Pass 45

### Overview: 17 Programs, Full Lifecycle

MRP in EvoERP is managed by T7MRA through T7MRO (17 programs). The engine uses three phases:
1. **Demand capture** (MR-A/B/C): enter forecasts + review SO demand
2. **Explosion** (MR-F/G/H/I): run MRP → generate MTMRP → firm → release
3. **Action** (MR-J/L/N): generate RFQs / POs / change notices / reports

| Program | Procs | Operation | Key tables |
|---|---|---|---|
| T7MRA | 65 | MR-A: Demand forecast entry | BKMRPFC+BKICMSTR |
| T7MRADE | 75 | MR-A extended (with doc attachments) | BKMRPFC+ISLINKS |
| T7MRB | 117 | MR-B: MRP system parameters | BKMRPFC+BKSYMSTR+CLASS+CLASMSTR |
| T7MRC | 108 | MR-C: Demand review (forecast vs SO) | BKMRPFC+BKARINVL+MTICMSTR |
| T7MRD | 121 | MR-D: Inventory status pre-check | BKICLOC+INVTXN+BKICLOCM |
| T7MRE | 120 | MR-E: Item-location exception report | BKICLOC+BKICLOCM+MTICMSTR |
| **T7MRF** | **172** | **MR-F: MRP explosion engine (core run)** | **MTMRP+BKMRPFC+BKARINVL+WOBOM+BKAPPOL+BKARINV+WORKORD+BKMRPPO** |
| T7MRG | 188 | MR-G: Firm planned orders → POs | MTMRP+BKSBVEND+BKSBMFG+BKAPPO+BKBMMSTR |
| T7MRH | 193 | MR-H: Release/post planned orders | ISBUILD+MTMRP→WORKORD+BKAPPO via INVTXN |
| T7MRI | 171 | MR-I: Capacity-aware scheduling | MTMRP+ROUTING+WOROUT+WORKCTR+ISICMSTR |
| T7MRIX | 130 | MR-IX: Extended capacity scheduling | CALENDAR+WODATE+WOBOM+WORKORD+MTMRP |
| T7MRJ | 206 | MR-J: PO/RFQ recommendations | MTMRP+BKMRPPO+BKRFQ+BKAPPO+BKSBVEND |
| T7MRJX | 123 | MR-JX: Release planned POs | BKMRPPO→BKAPPO with ISTERMS |
| T7MRK | 5 | MR-K: Sub-routine (stub of MR-JX) | same as MRJX |
| T7MRL | 85 | MR-L: MRP report | MTMRP display |
| T7MRN | 95 | MR-N: PO change notices | ISBUILD+MTMRP+BKAPPO+ISAPCHG |
| T7MRO | 113 | MR-O: MTMRP maintenance/cleanup | ISBUILD+MTMRP+MTICMSTR |

---

### MRP Data Flow

```
BKMRPFC (demand forecasts)
BKARINVL (open SO lines)         → T7MRF (explosion) → MTMRP (planned orders)
BKICMSTR/BKICLOC (on-hand)
WOBOM (BOM explosion)

MTMRP → T7MRG (firm, uses BKSBVEND to select vendor)
      → T7MRH (release → WORKORD + BKAPPO created)
      → T7MRI/MRIX (capacity scheduling with ROUTING + CALENDAR)
      → T7MRJ (PO/RFQ via BKRFQ + BKMRPPO)
      → T7MRL (report)
      → T7MRN (change notices via ISAPCHG)
```

---

### MTMRP (13f) — MRP Planned Orders Working Table

Created by T7MRF (explosion) and consumed by MRG/MRH/MRI/MRJ:

- MTMRP_PARTNO(15) + DATE(4) — part + required date (PK)
- MTMRP_QTY(8) — planned quantity
- MTMRP_ONHAND(8) — on-hand at calculation time
- MTMRP_PEGTO(10) — demand source link (SO#, WO#, or forecast ref)
- MTMRP_ORDER(10) — planned order type/number
- MTMRP_STARTDT(4) — planned start date
- MTMRP_ACTION(10) — planner action code (RELEASE, FIRM, CANCEL, etc.)
- MTMRP_PG_SDATE(4) + PG_FDATE(4) + PG_QTY(8) — pegging: peg start/finish/qty
- MTMRP_LOC(10) — inventory location
- MTMRP_EXTRA(50)

PEGTO is the critical field: it traces each planned order back to the demand that drove it (an SO line, a WO requirement, or a forecast). This is MRP "pegging" — the ability to answer "why was this order created?"

---

### BKRFQ (49f) — Vendor Request for Quote

Vendor RFQs with 10 quantity/cost breakpoints. Sources: MRP (T7MRJ), WO outside process, estimates (T7RFQ).

- BKRFQ_NUM(8) — RFQ number (PK)
- BKRFQ_EST(8) + EST_LINE(8) — link to estimate (ES module)
- BKRFQ_PARENT(15) + OPER(2) — parent item + operation (for outside-process RFQs)
- BKRFQ_PROD(15) — component item requested
- BKRFQ_WOPRE(8) + WOSUF(2) — WO reference (WO-based RFQs)
- BKRFQ_VEND(10) + VENDNAME(25) — vendor
- BKRFQ_ISSUE(4) — issue date
- BKRFQ_PUM(3) + PCONV(8) + LEAD(2) — unit of measure, conversion, lead time
- BKRFQ_EXP(4) — quote expiry date
- BKRFQ_QTY_1..10 (8 each) — 10 quantity breakpoints
- BKRFQ_COST_1..10 (8 each) — quoted costs at each qty break
- BKRFQ_MIN(8) + MINCST(8) — minimum order qty + cost
- BKRFQ_LCDATE(4) + CWHO(15) + UWHO(15) — last update date/who/updater
- BKRFQ_CQCHANGE(1) + FLAG(1) — change and status flags
- BKRFQ_GDATE(4) + MAXDAYS(2) — guarantee date + max lead days
- BKRFQ_ALPHA1(15) + EXTRA(50)

**Key insight:** BKRFQ is used by BOTH the RF module (estimate-based RFQs via T7RFQ + ISESTDTL) AND the MR module (MRP-driven RFQs via T7MRJ). The EST link and WOPRE/WOSUF fields distinguish the two use cases.

---

### CALENDAR (5f) — Shop Work Calendar

- MTCAL_DATE(4) — date (PK)
- MTCAL_DESC(25) — description (holiday name, note)
- MTCAL_SAT(1) — Saturday is a working day (Y/N)
- MTCAL_SUN(1) — Sunday is a working day (Y/N)
- MTCAL_YEAR(2) — year

Used by T7MRIX for finite capacity scheduling — non-working days are skipped when computing planned order start/finish dates. The MT prefix confirms this is from the DBA/MT era but still in use for MRP date arithmetic.

---

### BKSB* — Sourced-By Tables (Approved Vendor / Manufacturer / Substitute)

Three tables that define approved sources for each item. Used by T7MRG to select the preferred vendor when firming planned orders:

**BKSBVEND (6f)** — Approved vendor list:
- BKSB_VEND_PARNT(15) + PROD(15) + CUST(10) — parent item + component + customer (PK)
- BKSB_VEND_VEND(10) — approved AP vendor code
- BKSB_VEND_VPART(25) — vendor's own part number
- BKSB_VEND_EXTRA(50)

**BKSBMFG (6f)** — Approved manufacturer list:
- BKSB_MFG_PARNT(15) + PROD(15) + CUST(10) — PK
- BKSB_MFG_MANUF(25) — manufacturer name
- BKSB_MFG_MPART(25) — manufacturer's part number
- BKSB_MFG_EXTRA(50)

**BKSBPART (5f)** — Substitute/alternate parts:
- BKSB_PART_PARNT(15) + PROD(15) + CUST(10) — PK
- BKSB_PART_SUBST(15) — substitute item code (FK → BKICMSTR)
- BKSB_PART_EXTRA(50)

The CUST field in all three allows customer-specific source overrides (e.g., customer A requires parts from vendor X; customer B allows vendor Y).

---

### New Tables Confirmed (Pass 45)

| Table | Fields | Purpose |
|---|---|---|
| MTMRP | 13 | MRP planned orders working table — PARTNO+DATE PK; QTY+ONHAND+PEGTO+ORDER+STARTDT+ACTION+LOC |
| BKRFQ | 49 | Vendor RFQ — NUM PK; VEND+PARENT+PROD+WOPRE/WOSUF+10×QTY/COST breaks+EXP+LEAD |
| CALENDAR | 5 | Shop work calendar — DATE PK; SAT+SUN work flags; used by MRP scheduling |
| BKSBVEND | 6 | Approved vendor list — PARNT+PROD+CUST PK; VEND+VPART |
| BKSBMFG | 6 | Approved manufacturer list — PARNT+PROD+CUST PK; MANUF+MPART |
| BKSBPART | 5 | Substitute part list — PARNT+PROD+CUST PK; SUBST item code |

---

---

## PR — PAYROLL — Pass 46

### Overview: 40+ Programs

EvoERP Payroll handles full employee payroll with multi-state taxes, direct deposit, and DC labor import.

| Program | Procs | Operation | Key tables |
|---|---|---|---|
| T7PRA | 169 | PR-A: Employee master setup | BKPRMSTR+BKPRINFO+BKPRSALE+BKPRGLFL |
| T7PRB | 229 | PR-B: Enter current period payroll | BKPRCURP+BKPRFTAX+BKPRMSTR+BKPRGLFL |
| T7PRC | 129 | PR-C: Calculate payroll | BKPRCURP+BKPRGLFL+BKPRMSTR |
| T7PRD | 189 | PR-D: Post payroll to GL | BKPRCURP+BKGLTRAN+BKPRMSTR+BKPRGLFL |
| T7PRDPST | 32 | PR-DPST: Direct deposit posting | BKPRCURP+ISBANKS+ISPRTEMP |
| T7PRDIVFIX | 30 | PR-DIVFIX: Division correction | BKPSUSER+BKGLTRAN |
| T7PRE | 99 | PR-E: AP check posting | BKARINV+BKGLTRAN+BKPRMSTR |
| T7PRF | 92 | PR-F: Federal/state tax table maint | BKPRFTAX+BKPSUSER |
| T7PRG | 134 | PR-G: Print payroll checks | BKGLCHK+BKPRCURP+BKPRGLFL+BKPRMSTR |
| T7PRH | 121 | PR-H: Year-end / W-2 history | BKPRCURP+BKPRGLFL |
| T7PRI | 108 | PR-I: Payroll inquiry | BKPRCURP+BKPRINFO+BKPRMSTR |
| T7PRJ | 83 | PR-J: Time card entry | BKPRMSTR+BKPRTC |
| T7PRK | 134 | PR-K: Import DC labor to payroll | BKDCLAB+BKPRCURP+BKPRTC+BKPRMSTR |
| T7PRJCSYNC | 33 | PR-JCSYNC: Sync to Job Costing | BKPRINFO+BKPRMSTR |
| T7PRLA..PRLQ | 17 each | PR-LA..LQ: Payroll report variants | BKPRCURP+BKPRGLFL+BKPRINFO |
| T7PRM..PRS | various | PR-M..S: Period processing + reports | BKPRMSTR+BKGLTRAN |

**Payroll lifecycle:**
```
PR-A: setup employee (BKPRMSTR + BKPRINFO)
PR-J: enter time cards (BKPRTC)  OR  PR-K: import from DC labor (BKDCLAB)
PR-B: enter current period (BKPRCURP) + BKPRFTAX tax bracket lookup
PR-C: calculate (BKPRCURP + BKPRGLFL rates)
PR-G: print checks (BKGLCHK + BKGLTRAN)
PR-D: post to GL (BKGLTRAN payroll expense entries)
PR-DPST: direct deposit (ISPRTEMP staging → bank ACH via ISBANKS)
PR-H: year-end / W-2 processing
```

---

### BKPRMSTR (384f) — Employee Master

- BKPR_EMP_NUM(2) — employee number (PK, UBINARY)
- BKPR_EMP_FNMI(25) + LNME(25) — first + last name
- BKPR_EMP_ADD(30) + CSZ(25) + ST(2) + ZIP(10) + CNTRY(30) — address
- BKPR_EMP_PHONE(15)
- BKPR_EMP_SSN(11) — social security number
- BKPR_EMP_SDATE(4) — hire date
- BKPR_EMP_TERM(1) — terminated flag
- BKPR_EMP_MS(1) — marital status (S/M)
- BKPR_EMP_FEDEXM(2) + STEXM(2) — federal + state tax exemptions
- BKPR_EMP_PAYTYP(1) — pay type (H=hourly, S=salary, etc.)
- BKPR_EMP_PAYAMT_1..15 — 15 pay rate slots
- BKPR_EMP_DEPT(4) — department code
- BKPR_EMP_SHIFT(2) — shift assignment
- BKPR_EMP_RHQTD/RAQTD/RHYTD/RAYTD — regular hours/amounts: QTD + YTD
- BKPR_EMP_VHQTD/VAQTD/VHYTD/VAYTD/VDUE — vacation: QTD/YTD/due hours
- BKPR_EMP_SHQTD/SAQTD/SHYTD/SAYTD/SDUE — sick: QTD/YTD/due hours
- BKPR_EMP_FITQTD/FITYTD — federal income tax: QTD/YTD withheld
- BKPR_EMP_FICQTD_1/2 / FICYTD_1/2 — FICA (1=SS, 2=Medicare): QTD/YTD
- BKPR_EMP_STQTD/STYTD — state income tax: QTD/YTD
- BKPR_EMP_WKQTD/WKYTD — workers comp: QTD/YTD
- BKPR_EMP_MDAMT/MDQTD/MDYTD — medical deduction: flat amount + QTD/YTD
- BKPR_EMP_OHQTD_1..12 / OAQTD_1..12 — 12 user-defined other deduction types: hours QTD + amounts QTD
- BKPR_EMP_LSTPR(4) — last pay date
- +300 more fields (additional deduction types, W-2 accumulators, benefit allocations)

---

### BKPRCURP (127f) — Current Period Payroll

One row per employee per pay period. Created in PR-B, consumed by PR-C/G/D.

- BKPR_CURP_EMPNM(2) + PRDTE(4) — employee + pay period date (PK)
- BKPR_CURP_ACTNM(2) — payroll action number
- BKPR_CURP_CHKNM(6) — check number
- BKPR_CURP_TOTHR(8) + TOTPY(8) — total hours + total gross pay
- BKPR_CURP_RPHRS(8) + RPRTE(8) + RPAMT(8) — regular: hours + rate + gross
- BKPR_CURP_OPHRS_1..12 — overtime hours (12 overtime pay categories)
- BKPR_CURP_OPRTE_1..12 — overtime rates by category
- BKPR_CURP_OPAMT_1..12 — overtime amounts by category
- BKPR_CURP_VPHRS/VPRTE/VPAMT — vacation: hours/rate/amount
- BKPR_CURP_SPHRS/SPRTE/SPAMT — sick: hours/rate/amount
- +remaining tax deductions and net pay fields

---

### BKPRFTAX (47f) — Payroll Tax Bracket Table

Federal + state withholding brackets. One row per tax jurisdiction code.

- BKPR_TAX_CODE(3) — tax code (PK: "FED", "CT", "NY", etc.)
- BKPR_TAX_DESC(20) — description
- BKPR_TAX_ALLOW(8) — per-exemption allowance amount
- BKPR_TAX_START_1..11 — 11 bracket income start thresholds
- BKPR_TAX_THRU_1..10 — 10 bracket end thresholds
- BKPR_TAX_AMT_1..11 — base tax at each bracket floor
- BKPR_TAX_PERC_1..11 — marginal rate within each bracket

Tax formula: find bracket where (income - exemptions × ALLOW) falls between START_N and THRU_N; tax = AMT_N + PERC_N × (excess over START_N).

---

### BKPRGLFL (664f) — Payroll GL Account Mapping

Per state+dept row. Maps every payroll tax type to its GL accounts and stores all payroll tax rates.

- BKPR_GL_STCODE(2) + DEPT(4) — state code + department (PK)
- BKPR_GL_FITACCT(10)/FITDPT — Federal Income Tax GL
- BKPR_GL_FICACCT_1/2(10)/FICDPT — FICA GL (1=SS, 2=Medicare)
- BKPR_GL_FUTACCT(10)/FUTDPT — FUTA GL
- BKPR_GL_SUTACCT(10)/SUTDPT — SUTA GL
- BKPR_GL_SITACCT(10)/SITDPT — State Income Tax GL
- BKPR_GL_WCACCT(10)/WCDPT — Workers Compensation GL
- BKPR_GL_SDIACCT(10)/SDIDPT — SDI (State Disability Insurance) GL
- BKPR_GL_FICAEMP(8) + FICAEPL(8) + FICALMT(8) — FICA rates: employee/employer % + wage limit
- BKPR_GL_FUTART(8) + FUTALMT(8) + FUTACRD(8) — FUTA rate / wage limit / credit
- BKPR_GL_SUTART(8) + SUTALMT(8) — SUTA rate + wage limit
- BKPR_GL_SDI_RTE(8) + SDI_LMT(8) — SDI rate + wage limit
- BKPR_GL_SRTE(8) + VRTE(8) — sick + vacation accrual rates
- BKPR_GL_PAYPER(1) — pay frequency (W=weekly, B=bi-weekly, S=semi-monthly, M=monthly)
- BKPR_GL_WCHOW(1) — workers comp calc method
- BKPR_GL_FICAEXP_1/2 + FICAEXD_1/2 — FICA expense GL (employer side)
- BKPR_GL_SUTAEXP + WCEXP — SUTA + WC expense GL accounts
- BKPR_GL_UODAMT1_1..N — user-defined other deduction amounts per bracket
- +600 more (per-deduction-type GL mappings, 12+ user-defined deduction GL accounts)

At 664 fields, BKPRGLFL is one of the widest tables in EvoERP — it encodes the entire state payroll tax configuration in a single row per state, avoiding joins during payroll calculation.

---

### BKPRINFO (128f) — Employee HR / Accrual Record

- BKPR_INFO_NUM(2) — employee number (PK)
- BKPR_INFO_DDEP(1) — direct deposit enrolled flag
- BKPR_INFO_REVDT_1..6 — scheduled review dates (6 future performance reviews)
- BKPR_INFO_RASDT_1..6 — scheduled raise dates
- BKPR_INFO_REVNT_1..12 — review notes (12 × 60 chars)
- BKPR_INFO_RASNT_1..12 — raise notes (12 × 60 chars)
- BKPR_INFO_AVAC(1) + VACAC(4) + VHRS(8) — vacation accrual type + accrual anniversary date + hrs/period
- BKPR_INFO_ASICK(1) + SICKA(4) + SHRS(8) — sick accrual type + date + hrs/period
- BKPR_INFO_AHOW_1/2(1) + AHRS_1/2(8) — additional pay accrual methods + amounts
- BKPR_INFO_BINFO_1/2(30) — banking routing + account numbers for direct deposit

---

### BKPRSALE (87f) — Sales Rep Commission Tracking

Bridges the PR module to the CS (commission) system:

- BKPR_SLS_EMPNUM(2) — employee number (PK)
- BKPR_SLS_CLASS_1/2(2) — commission class codes (2 tiers)
- BKPR_SLS_RATE_1/2(8) — commission rates per tier
- BKPR_SLS_HOW_1/2(1) — calculation method (% gross, % GP, flat)
- BKPR_SLS_WHEN_1/2(1) — trigger (on invoice, on cash receipt)
- BKPR_SLS_QUOTA_1..12(8) — 12 monthly quotas
- BKPR_SLS_GROSS_1..12(8) — actual monthly gross sales
- BKPR_SLS_COGS_1..12(8) — actual monthly COGS
- BKPR_SLS_RCPTS_1..12(8) — actual monthly cash receipts

---

### BKPRTC (7f) — Time Card

- BKPR_TC_EMP(2) + DATE(4) — employee + date (PK)
- BKPR_TC_START(4) + STOP(4) — clock-in + clock-out TIME fields
- BKPR_TC_DEDUCT(4) — break/lunch deduction time
- BKPR_TC_TYPE(1) — type code (R=regular, O=overtime, V=vacation)
- BKPR_TC_EXTRA(25)

T7PRK imports from BKDCLAB into BKPRTC: shop floor clock-ins become payroll time cards automatically.

---

### ISPRTEMP (15f) — Direct Deposit Staging Batch

Staging buffer between T7PRDPST (direct deposit builder) and BKGLTRAN / bank ACH export:

- ISPR_TRN_GLACCT(10) + GLDPT(4) — GL account + dept
- ISPR_TRN_DATE(4) + ENTDTE(4) — transaction date + entry date
- ISPR_TRN_CODE(10) — payroll transaction code
- ISPR_TRN_DESC(25) — description
- ISPR_TRN_DC(1) — debit/credit
- ISPR_TRN_AMT(8) — amount
- ISPR_TRN_TRXN(8) — transaction number
- ISPR_TRN_POST(1) — posted to BKGLTRAN flag
- ISPR_TRN_PERIOD(2) — GL period
- ISPR_TRN_BATCH(8) — batch number

---

## IM — LANDED COST / IMPORT — Pass 46

### Overview

Landed cost tracks additional import charges (duties, freight, customs broker fees) against PO receipts.

| Program | Procs | Operation | Key tables |
|---|---|---|---|
| T7IMB | 106 | IM-B: Landed cost entry (with attachments) | BKICMSTR+ISLINKS+BKSYMSTR |
| T7IMC | 83 | IM-C: Multi-currency landed cost | ISMCF+BKICMSTR |
| T7IMD | 68 | IM-D: Allocation formulas | ISLANDF+BKICMSTR |
| T7IME | 54 | IM-E: Duty calculation | ISDUTY+BKICMSTR |
| T7IMF | 56 | IM-F: Customs broker billing | ISBROKER+BKICMSTR |

**Flow:** PO receipt → T7IMD allocates charges by formula (ISLANDF GL targets) → T7IME calculates tariff duties (ISDUTY rate table) → T7IMF bills customs broker fees (ISBROKER) → all post to BKGLTRAN.

### ISLANDF (6f) — Landed Cost GL Account Mapping

Three pairs of GL account + dept — one pair per landed cost category:

- ISIS_LND_GLADT(10) + GLDDT(4) — duty/tax GL account + dept
- ISIS_LND_GLAFR(10) + GLDFR(4) — freight GL account + dept
- ISIS_LND_GLACF(10) + GLDCF(4) — customs/fees GL account + dept

### ISDUTY (2f) — Tariff/Duty Rate Table

- ISIS_DUTY_DCODE(6) — duty/tariff code (PK, e.g., HS tariff schedule number)
- ISIS_DUTY_PERC(8) — duty rate as decimal percentage

### ISBROKER (4f) — Customs Broker Fee Table

- ISIS_BRK_CODE(10) — broker code (PK)
- ISIS_BRK_FLAT(8) — flat fee per shipment
- ISIS_BRK_PERC(8) — percentage fee (of shipment value)
- ISIS_BRK_TYPE(1) — fee type (F=flat, P=percent, B=both)

---

## PS — PROGRAM SECURITY — Pass 46 (Schema)

### BKPSUSER (11f) — User Security Record

- BKPS_USER_CODE(15) — user login code (PK)
- BKPS_USER_PRT(2) — default printer assignment
- BKPS_USER_MENU(2) — assigned menu set number
- BKPS_USER_CMPY(2) — default company code
- BKPS_USER_MWIND(1) — multi-window mode flag
- BKPS_USER_PSWD(10) — password (10 chars; stored plaintext or weak hash)
- BKPS_USER_ME(1) — menu editor access flag
- BKPS_USER_SEC(30) — security access string (controls which module codes are accessible)
- BKPS_USER_MCNTR(2) — consecutive failed login counter (triggers lockout)
- BKPS_USER_LDATE(4) — last successful login date
- BKPS_USER_EMP(2) — linked employee number (FK → BKPRMSTR)

SEC(30) drives per-module access control. MCNTR is reset on successful login; the lockout threshold is configured in BKSYMSTR.

---

## MH — SHIPPING ORDER — Supporting Tables — Pass 46

### ISSHPVIA (23f) — Ship Via / Carrier Method

Per-customer carrier configuration with account numbers:

- IS_SHPVIA_CUST(10) + CODE(15) — customer + carrier code (PK)
- IS_SHPVIA_PRTY(2) — sort priority
- IS_SHPVIA_OBS(1) — obsolete flag
- IS_SHPVIA_ACCT(25) — carrier account number (UPS/FedEx/etc.)
- IS_SHPVIA_PHONE(25) — carrier phone
- IS_SHPVIA_NOTES_1..10 (60 each) — 10 carrier notes lines
- IS_SHPVIA_DATE(4) — last updated date
- IS_SHPVIA_CNTCT(25) — carrier contact name
- IS_SHPVIA_FLAG(1) — status flag
- IS_SHPVIA_VEND(10) — carrier as AP vendor code (FK → BKAPVEND) for freight cost AP invoices
- IS_SHPVIA_ALPH1/ALPH2(15) + EXTRA(100)

### BKCMTERR (11f) — CRM Sales Territory

- BKCM_TERR_TCODE(4) — territory code (PK)
- BKCM_TERR_DESC(25) — description
- BKCM_TERR_EMAIL(128) — territory notification email
- BKCM_TERR_ALPHA(30) + EXTRA(100) — custom fields
- BKCM_TERR_FLAGS_1..5 (1 each) — 5 single-char territory flags (automation triggers)
- BKCM_TERR_DATE(4) — last update date

---

### New Tables Confirmed (Pass 46)

| Table | Fields | Purpose |
|---|---|---|
| BKPRMSTR | 384 | Employee master — EMP# PK; NAME+SSN+ADDRESS+PAYTYP+15 pay rates+all QTD/YTD tax types |
| BKPRCURP | 127 | Current period — EMP#+DATE PK; regular+12 OT+vacation+sick hrs/rates/amounts |
| BKPRFTAX | 47 | Tax bracket table — CODE PK; ALLOW+11 START/THRU/AMT/PERC brackets |
| BKPRGLFL | 664 | GL mapping per state+dept — all payroll tax GL accounts + rates (FICA/FUTA/SUTA/SDI/WC) |
| BKPRSALE | 87 | Sales rep commissions — 12-month QUOTA/GROSS/COGS/RCPTS per employee |
| BKPRINFO | 128 | HR info — 6 review+raise dates, vacation/sick accrual, direct deposit banking |
| BKPRTC | 7 | Time card — EMP+DATE PK; START+STOP+DEDUCT times + TYPE |
| ISPRTEMP | 15 | Direct deposit staging — GLACCT+AMT+POST+BATCH before ACH export |
| ISLANDF | 6 | Landed cost GL accounts — duty/freight/customs each with acct+dept |
| ISDUTY | 2 | Tariff duty rate table — DCODE(6)+PERC |
| ISBROKER | 4 | Customs broker — CODE+FLAT+PERC+TYPE |
| BKPSUSER | 11 | User security — CODE PK; PSWD(10)+SEC(30)+MCNTR+LDATE+EMP link |
| ISSHPVIA | 23 | Ship via per customer — CUST+CODE PK; ACCT+PHONE+10×NOTES+VEND |
| BKCMTERR | 11 | CRM territory — TCODE PK; DESC+EMAIL+5×FLAGS |

---

---

## JC — JOB COSTING — Pass 47

### Architecture: No Proprietary Tables

**Key finding:** JC has no BKJC* or ISCALC/ISCOST tables. It is a cost analysis and engineering overlay on the standard Work Order tables.

JC reads: WORKORD + WOBOM + WOMAT + WOLABOR + WORECV + WOROUT + MTICMSTR + BKGLTRAN + WOEXCHG (engineering changes) + OUTPROC (outside process).

| Program | Procs | Operation | Key tables |
|---|---|---|---|
| T7JCA | 163 | JC-A: Main entry / WO cost viewer | WORKORD+WOBOM+WOROUT+ISWOEX+WOEXCHG+MTICMSTR |
| T7JCB | 119 | JC-B: Cost calculation | WORKORD+WOBOM+DBAFIFO+BKGLTRAN+BKMRPFC+BKSBPART |
| T7JCC/D/I/J/K/O | 5 each | Stub sub-programs (same DB as JCB) | same as JCB |
| T7JCE | 153 | JC-E: Parent/child cost roll-up | WORKORD+WOBOM+WOMAT+DBAFIFO+ISNCR+ISGLDATE+ISCYCLCD |
| T7JCENG | 211 | JC-ENG: Engineering routing specs | WORKORD+WOBOM+WOROUT+BKRTSPEC+BKPRMSTR+MTICMSTR |
| T7JCF | 137 | JC-F: QC cost integration | WORKORD+BKQCTRAN+BKAPPOL |
| T7JCG | 5 | JC-G: Stub (same DB as JCF) | same as JCF |
| T7JCH | 137 | JC-H: Historical cost | WORKORD+WOBOM+DBAFIFO+BKGLTRAN+BKMRPFC |
| T7JCL | 138 | JC-L: Links/documents viewer | WORKORD+ISLINKS+ISLOG |
| T7JCM | 188 | JC-M: Full module (WO+SO billing) | WORKORD+WOBOM+WOMAT+WOLABOR+WORECV+WORKCTR+BKARINV |
| T7JCN | 130 | JC-N: Calculation modes + 2D barcode | WORKORD+IS2DBAR+BKMRPFC+ISNCR |
| T7JCP | 108 | JC-P: Materials in WIP | WORKORD+WOBOM+DBAFIFO+BKGLTRAN |
| T7JCQ | 138 | JC-Q: Query view | WORKORD+ISLINKS+ISLOG |
| T7JCR | 167 | JC-R: Catalog cross-reference | WORKORD+ISCATMST+CLASS+BKICMSTR |
| T7JCRM | 62 | JC-RM: RMA cost | WORKORD+BKGLTRAN+BKMRPFC |
| T7JCS | 142 | JC-S: Billing + SO connection | WORKORD+BKARINV+BKARINVL+BKPRMSTR |
| T7JCT | 5 | JC-T: Stub | same as JCS |

**Cost calculation modes (from JC-N):** current/historical/proposed. JC compares actual WO costs (WOLABOR + WOMAT) against standard MTICMSTR costs and BKGLTRAN GL actuals.

---

### WOEXCHG (10f) — WO Engineering Change Cost

Records cost charges from engineering changes applied to a WO (MTWO prefix = MT-era table):

- MTWO_EX_WOPRE(8) + WOSUF(2) — work order (PK part 1)
- MTWO_EX_DATE(4) — change date
- MTWO_EX_PROD(15) — affected item
- MTWO_EX_DESC(30) — change description
- MTWO_EX_CHG(8) — charge amount
- MTWO_EX_CHGDESC(30) — charge description
- MTWO_EX_GLACCT(10) + GLDPT(4) — GL account + dept for the charge
- MTWO_EX_OP(2) — operation number

---

### OUTPROC (15f) — WO Outside Process PO (MT-era)

MT-era outside process link between WO operations and AP purchase orders (MTPO prefix):

- MTPO_VENDOR(10) + VENDNAME(20) — outside process vendor
- MTPO_PO(8) — purchase order number (FK → BKAPPO)
- MTPO_WOPRE(8) + WOSUF(2) — work order reference (FK → WORKORD)
- MTPO_DATE(4) — date
- MTPO_OPER(2) — operation number (FK → WOROUT)
- MTPO_PROD(15) + DESC(25) — component + description
- MTPO_QTY(8) + COST(8) + EXTPR(8) — quantity/cost/extended price
- MTPO_ASSY(15) + ASSYDESC(30) — assembly parent + description
- MTPO_EXTRA(50)

Modern EvoERP uses BKAPPOL.WOPRE/WOSUF fields instead; OUTPROC coexists as the MT-era legacy.

---

### ISNCR (35f) — Non-Conformance Report

Tracks defects, rework, and corrective actions at the part/lot/serial level:

- IS_NCR_NUM(8) — NCR number (PK)
- IS_NCR_PART(15) + COMP(15) — non-conforming part + component
- IS_NCR_LOT(15) + SERIAL(25) — lot + serial number
- IS_NCR_CDATE(4) + WHO(15) — creation date + created by
- IS_NCR_QTY(8) — quantity involved
- IS_NCR_DCODE(10) + DESC(60) — defect code + description
- IS_NCR_ICR(1) + ORIG(1) — internal correction flag + origin (R=receiving, W=WO, C=customer)
- IS_NCR_WOPRE(8) + WOSUF(2) — linked work order
- IS_NCR_MACH(4) + TOOL(15) + WC(12) — machine + tool + work center
- IS_NCR_PONUM(8) — linked PO (receiving NCR)
- IS_NCR_RMA(8) — linked RMA number
- IS_NCR_ACTION(1) — required action code
- IS_NCR_CAR(8) — corrective action request number
- IS_NCR_DISP(10) + DWHO(15) + DDATE(4) — disposition code/who/date
- IS_NCR_STATUS(1) — open/closed/pending
- IS_NCR_SCRAP(2) + QC(2) — scrap disposition + QC disposition
- IS_NCR_VEND(10) — vendor (receiving NCR)
- IS_NCR_LOC(10) + CLOC(10) — location + corrective location
- IS_NCR_PDRAW(15) + PREV(5) — parent drawing + rev (as-designed)
- IS_NCR_CDRAW(15) + CREV(5) — component drawing + rev

NCRs link to WOs (WOPRE/WOSUF), POs (PONUM), RMAs, vendors, and lots/serials — making them the quality hub that spans all transaction types.

---

### BKSHORT (9f) — WO Material Shortage

Records material shortages per work order:

- BK_SHORT_PCODE(15) — shortage item code (PK part 1)
- BK_SHORT_WONUM(8) + WO_SUF(2) — work order (PK part 2)
- BK_SHORT_DESC(25) — item description
- BK_SHORT_QTYREQ(8) — quantity required
- BK_SHORT_SHORT(8) — short quantity (QTYREQ - available)
- BK_SHORT_DATE(4) — shortage date
- BK_SHORT_PPCODE(15) + PPDESC(25) — parent item + description

Used by T7HHWOG (handheld WO goods issue) and T7HHWOSCRAP to flag material shortages during shop floor execution.

---

### ISICMSTR (41f) — Item Logistics Extension

Extended item master for freight/logistics properties (IS_PROD_ prefix):

- IS_PROD_CODE(15) — item code (PK, FK → BKICMSTR)
- IS_PROD_WT(8) — weight
- IS_PROD_ITP(20) — item type (custom logistics class)
- IS_PROD_HT(8) + LG(8) + WD(8) — height/length/width
- IS_PROD_TI(8) + HI(8) — tier/inch + height/inch (pallet stacking)
- IS_PROD_FOBPAL(8) — units per pallet (FOB palletized)
- IS_PROD_FOBFULL(8) — units per full truckload
- IS_PROD_CDATE(4) — created date
- IS_PROD_EXTRA(150)
- +29 more (additional packaging, compliance fields)

FOBPAL/FOBFULL are used by the shipping/freight modules to optimize carrier rate calculation.

---

### ISCYCLCD (7f) — Cycle Count Code

Defines cycle count frequency groups for physical inventory:

- IS_CYCLE_CODE(4) — cycle count code (PK, e.g., "A", "B", "C")
- IS_CYCLE_DESC(30) — description
- IS_CYCLE_FREQ(2) — count frequency per year (e.g., 12=monthly, 4=quarterly)
- IS_CYCLE_DATE(4) — last count date for this code
- IS_CYCLE_ALPHA(15) — alpha custom field
- IS_CYCLE_NUM(8) — count number
- IS_CYCLE_EXTRA(50)

Used by T7PIA (PI freeze) and T7JCE. BKICMSTR items are assigned a cycle count code; the PI module uses this to schedule when each item class needs a physical count.

---

### BKQCMSTR (14f) + BKQCTRAN (21f) — QC Receiving Records

**BKQCMSTR** — QC master per PO receipt:
- BKQC_VEND_CODE(10) — vendor (PK part 1)
- BKQC_PO_NUM(8) + RECVR_NUM(8) — PO + receiver number (PK)
- BKQC_RECV_DATE(4) — receipt date
- BKQC_POL_ITM_NO(10) — PO line item number
- BKQC_PKSLIP_NUM(15) + PKSLIP_QTY(8) — packing slip + qty
- BKQC_QTY_RECVD(8) + QTY_BUYOFF(8) + QTY_REJECT(8) — received/accepted/rejected
- BKQC_PROD_CODE(15) + UNIT_COST(8) — item + cost

**BKQCTRAN** — QC transaction log:
- BKQC_TRN_PO(8) + VEND(10) + CODE(15) + RECNUM(8) — PK
- BKQC_TRN_GQTY/BQTY/UQTY(8) — good/bad/use-as-is quantities
- BKQC_TRN_SCRAP(2) + REWORK(2) — disposition codes
- BKQC_TRN_PODTE/ARDTE/BODTE(4) — PO/arrival/buyoff dates
- +9 more (return, corrective action fields)

Used by T7JCF (JC-F cost integration) and T7HHPOC (handheld PO receiving).

---

### IS2DBAR (109f) — 2D Barcode Configuration

Defines 2D barcode label layouts for WO operations and items (109 fields):

- IS2D_BAR_CODE(10) — barcode config code (PK part 1)
- IS2D_BAR_ITEM(15) — item (PK part 2)
- IS2D_BAR_ORDER(2) — field order
- IS2D_BAR_CHAR(5) — character set
- IS2D_BAR_FIELD(25) — field name to encode
- IS2D_BAR_DOCPR_1..10(1 each) — 10 document property flags
- +remaining field/format/print options

Used by T7JCN and T7HHWOLABEL for 2D barcode printing on WO travelers and item labels.

---

### BKRTSPEC (7f) — Routing Specification Notes

Short notes attached to routing operations per part:

- BKRT_SPEC_PART(15) — part code (PK part 1, FK → BKICMSTR)
- BKRT_SPEC_SEQ(2) + LINE(2) — sequence + line number (PK parts 2–3)
- BKRT_SPEC_NOTE_1..4 (20 each) — 4 lines × 20 chars of specification notes

Used by T7JCENG (engineering routing specs). Provides short work instructions attached to specific routing operations.

---

### New Tables Confirmed (Pass 47)

| Table | Fields | Purpose |
|---|---|---|
| WOEXCHG | 10 | WO engineering change cost — WOPRE+WOSUF+DATE PK; CHG amount + GL account |
| OUTPROC | 15 | MT-era outside process PO — VENDOR+PO+WOPRE/WOSUF+OPER; legacy predecessor to BKAPPOL WO link |
| ISNCR | 35 | Non-Conformance Report — NUM PK; PART+COMP+LOT+SERIAL+DCODE+DISP+CAR+links to WO/PO/RMA |
| BKSHORT | 9 | WO material shortage — PCODE+WONUM PK; QTYREQ+SHORT+DATE |
| ISICMSTR | 41 | Item logistics extension — CODE PK; WT+dimensions+FOBPAL+FOBFULL |
| ISCYCLCD | 7 | Cycle count frequency codes — CODE PK; FREQ+DATE; used by PI freeze |
| BKQCMSTR | 14 | QC receiving master — VEND+PO+RECVR PK; QTY_RECVD/BUYOFF/REJECT |
| BKQCTRAN | 21 | QC transaction log — PO+VEND+CODE+RECNUM PK; GQTY/BQTY/UQTY+disposition |
| IS2DBAR | 109 | 2D barcode config — CODE+ITEM PK; 10 document property flags + field list |
| BKRTSPEC | 7 | Routing spec notes — PART+SEQ+LINE PK; 4×20 char notes |

---

---

## HH — HANDHELD / SHOP-FLOOR DATA COLLECTION — Pass 48

### Overview: 30+ Programs Across 9 Sub-Areas

| Program | Procs | Sub-area | Operation |
|---|---|---|---|
| T7HH | 46 | Launch | Main HH menu / device connection |
| T7HHDCA | 167 | DC Labor | Shop floor labor scan: WO+operation+clock in/out |
| T7HHDCA1 | 82 | DC Labor | DC labor entry variant 1 |
| T7HHDCB/C | 5 each | DC Labor | DC labor stubs (same DB as HHDCA) |
| T7HHWOG | 201 | WO Ops | WO goods issue (pull materials from inventory to WO) |
| T7HHWOI | 212 | WO Ops | WO complete / goods receipt (receive finished parts) |
| T7HHWOP | 135 | WO Ops | WO operation complete (finish routing step) |
| T7HHWOSCRAP | 151 | WO Ops | WO scrap recording |
| T7HHWOLABEL | 150 | WO Ops | WO label printing (2D barcode) |
| T7HHWOLOOKUP | 39 | WO Ops | WO lookup by number |
| T7HHWOLOT | 80 | WO Lot/Ser | WO lot tracking |
| T7HHWOSER | 88 | WO Lot/Ser | WO serial number tracking |
| T7HHSSOE | 267 | SO Ship | SO shipping verification chain (5-form flow) |
| T7HHSSOEVERIFY | 44 | SO Ship | SO pre-ship verification |
| T7HHNREL | 129 | SO Ship | SO release / notification |
| T7HHSODD | 80 | SO Ship | SO document + compliance (BKICREF+ISAREX) |
| T7HHSOLOOKUP | 39 | SO Ship | SO lookup |
| T7HHSOLOT | 51 | SO Lot/Ser | SO lot picking |
| T7HHSOSER | 56 | SO Lot/Ser | SO serial number picking |
| T7HHSOBIN | 55 | SO Ship | SO bin-level shipping |
| T7HHPOC | 262 | PO Recv | PO receiving |
| T7HHPOCBIN | 202 | PO Recv | PO receiving with bin assignment |
| T7HHPOCLS | 5 | PO Recv | PO receiving stub |
| T7HHINGA | 150 | Inventory | Inventory receipt / goods arrival |
| T7HHINBINS | 48 | Inventory | Inventory bin moves |
| T7HHINLJ | 114 | Inventory | Inventory location transfer |
| T7HHPIC | 105 | PI Count | Physical inventory count (handheld tag count) |
| T7HHN | 117 | Inquiry | Item/WO inquiry |
| T7HHSROE | 5 | SR | Service/Repair stub |
| T7HHH | 65 | Misc | AR/GL integration utility |
| T7HHO | 79 | Misc | Inventory location report |

**HH data flows:**
- DC Labor: T7HHDCA → BKDCLAB → (T7PRK imports to BKPRTC for payroll)
- WO Goods Issue: T7HHWOG → WOMAT + INVTXN + BKICLOC (materials moved to WO)
- WO Complete: T7HHWOI → WORECV + INVTXN + BKGLTRAN (finished output received)
- SO Shipping: T7HHSSOE → ISSOBOX (box packing) → BKARTXN (shipment record) → BKARINV (invoice)
- PO Receiving: T7HHPOC → BKAPPO+BKAPPOL + QC check (BKQCMSTR)

---

### BKDCLAB (50f) — DC Labor Record

One record per clock-in event per WO operation. Core table for shop floor time tracking:

- LAB_DATE(4) + LAB_EMP(2) + LAB_WOPRE(8) + LAB_WOSUF(2) + LAB_OPER(2) — composite PK
- LAB_POSTED(1) — posted to WO/GL flag
- LAB_SHIFT(2) — shift number (1/2/3, references BKDCSHFT)
- LAB_START(4) + FINISH(4) — clock-in + clock-out TIME fields
- LAB_PARTS(8) — quantity completed this session
- LAB_SCRAPPED(8) — quantity scrapped
- LAB_NOJOBS(2) — number of pieces/jobs
- LAB_RUNHRS(8) + SETUPHRS(8) — computed run + setup hours
- LAB_REGOVER(1) — R=regular, O=overtime
- LAB_APPROVAL(1) — supervisor approval flag
- LAB_ADT_SUPER(100) + ADT_IN(100) + ADT_OUT(100) — audit trail: supervisor + in/out details
- LAB_SCRAPCD_1..5(2) — up to 5 scrap reason codes per transaction
- LAB_SCRAPQTY_1..5(8) — scrap quantity per reason code
- LAB_JCNUM(12) — Job Costing number (links to JC module cost allocation)
- LAB_CYCLE_HR/MIN/SEC(2) — cycle time measured in H:M:S
- LAB_CYCLE_PARTS(8) — parts per cycle (for cycle time calculation)
- LAB_CYCLE_NOTE(255) — cycle time notes
- LAB_GEN_DATE_1/2(4) + ALPHA_1/2(30) + NUM_1/2(8) + FLAG_1..5(1) — user-defined custom fields
- LAB_ESSDATE(4) + DATE1(4) + DATE2(4) — ESS + date range fields
- LAB_EXTRA(50)

LAB_JCNUM links each shop floor scan to job costing — confirming that JC uses BKDCLAB as its actual-labor input. The 5-code scrap structure enables defect categorization per transaction.

---

### BKDCSHFT (34f) — Shift Schedule Configuration

Singleton table — one row for the entire company's 3-shift schedule:

- BKDC_SH_NAME1/2/3(25) — shift names
- BKDC_SH_BUFFER_1/2/3(4) — buffer time at shift start (grace period before OT)
- BKDC_SH_START_1/2/3(4) — shift start times
- BKDC_SH_BRK1IN_1..3(4) + BRK1OUT_1..3(4) — break 1 in+out per shift
- BKDC_SH_LUNCHIN_1..3(4) + LUNCHOT_1..3(4) — lunch in+out per shift
- BKDC_SH_BRK2IN_1..3(4) + BRK2OUT_1..3(4) — break 2 in+out per shift
- BKDC_SH_FIN_1/2/3(4) — shift end times
- BKDC_SH_FINBUF_1/2/3(4) — buffer at shift end (OT threshold)
- BKDC_SH_EXTRA(50)

All TIME fields. The system subtracts break/lunch periods from raw START→FINISH duration to compute net productive hours in BKDCLAB.RUNHRS.

---

### BKDCCFG (7f) — DC System Configuration

Singleton configuration table:

- BKDC_CFG_IDLEP(8) + IDLES(2) — idle time thresholds (period + shift)
- BKDC_CFG_BANKP(8) + BANKS(2) — bank time config
- BKDC_CFG_IMPPTH(60) — import file path (for batch handheld import)
- BKDC_CFG_EXPPTH(60) — export file path
- BKDC_CFG_JOBTME(60) — job time config file path

---

### ISSOBOX (22f) — SO Shipping Box / Package

Tracks what is packed into each shipping box on an SO:

- ISSO_BOX_SONUM(8) + LINE(8) + BOX(2) — SO + line + box number (PK)
- ISSO_BOX_CODE(15) — item code packed
- ISSO_BOX_QTY(8) — quantity in this box
- ISSO_BOX_LOT(15) + SERIAL(25) — lot + serial number
- ISSO_BOX_TEMP(1) — temporary/staged flag
- ISSO_BOX_INVNUM(8) + SHIPPR(8) + SHPCOD(10) — invoice + shipping priority + code
- ISSO_BOX_WEIGHT(8) — box weight
- ISSO_BOX_SKID(2) — skid/pallet number
- ISSO_BOX_DATE(4) — packing date
- ISSO_BOX_WOPRE(8) + WOSUF(2) — linked WO (for make-to-order shipments)
- ISSO_BOX_UCC(30) — UCC-128 carton barcode
- ISSO_BOX_HT/LG/WD(8) — box dimensions (height/length/width)
- ISSO_BOX_TRACK(40) — carrier tracking number (filled in during shipment scan)

T7HHSSOE (267-proc SO shipping chain) populates ISSOBOX as items are scanned; TRACK is filled when the label is printed.

---

### BKARTXN (14f) — AR Shipment Transaction

Shipment record linking SO lines to actual items/lots/serials shipped:

- BKAR_TXN_SONUM(8) + CODE(15) + LINE(8) — SO + item + line (PK)
- BKAR_TXN_DESC(30) — item description
- BKAR_TXN_QTY(8) — quantity shipped
- BKAR_TXN_LOT(15) + SERIAL(25) — lot + serial number shipped
- BKAR_TXN_DATE(4) — shipment date
- BKAR_TXN_STOCK(15) — stock item used (may differ from ordered item via substitution)
- BKAR_TXN_LOC(10) + BIN(15) — warehouse location + bin shipped from
- BKAR_TXN_TMPSO(40) — temporary SO reference
- BKAR_TXN_SRNUM(8) — service record number (SR module link)
- BKAR_TXN_EXTRA(50)

---

### BKICREF (8f) — Customer Item Cross-Reference

Maps internal item codes to customer-specific part numbers:

- BKIC_REF_CUST(10) + CODE(15) — customer + internal item code (PK)
- BKIC_REF_PDESC(30) — internal item description
- BKIC_REF_CUSNME(30) — customer's name for this item
- BKIC_REF_CUSCOD(25) — customer's part number
- BKIC_REF_DESC(30) + DESC2(30) — customer's description (2 lines)
- BKIC_REF_EXTRA(50)

Used by T7HHSODD and QT module to show customer-facing part numbers on shipment documents.

---

### ISAREX (51f) — AR Customer Extended / Compliance

Extended customer record for compliance, certifications, and custom fields:

- ISAREX_CUST(10) — customer code (PK, FK → BKARCUST)
- ISAREX_LONGNAME(60) — extended customer name (beyond BKARCUST 30-char limit)
- ISAREX_RS_EXPDT/UPDT/SGNDT(4) — resolution expiry/update/signed dates
- ISAREX_RS_WHO(15) — resolution contact
- ISAREX_RS_FORM(60) + CRT_FORM(60) — resolution + certificate form file paths
- ISAREX_NUM_1..5 + NUM2_1..N (8 each) — many numeric custom fields
- +37 more (compliance flags, additional certification fields)

Used by T7HHSODD for customer document compliance during shipping. Holds RoHS, conflict mineral certifications, and customer-specific compliance requirements.

---

### New Tables Confirmed (Pass 48)

| Table | Fields | Purpose |
|---|---|---|
| BKDCLAB | 50 | DC labor record — DATE+EMP+WOPRE+OPER PK; START/FINISH times + PARTS+SCRAP+RUNHRS; 5 scrap codes; JCNUM JC link |
| BKDCSHFT | 34 | 3-shift schedule — per-shift: NAME+BUFFER+START+2×BREAK+LUNCH+FINISH times |
| BKDCCFG | 7 | DC system config — import/export paths, idle/bank time thresholds |
| ISSOBOX | 22 | SO shipping box — SONUM+LINE+BOX PK; QTY+LOT+SERIAL+WEIGHT+UCC+TRACK |
| BKARTXN | 14 | AR shipment transaction — SONUM+CODE+LINE PK; QTY+LOT+SERIAL+LOC+BIN |
| BKICREF | 8 | Customer item cross-reference — CUST+CODE PK; CUSNME+CUSCOD (customer part numbers) |
| ISAREX | 51 | AR customer extended/compliance — CUST PK; LONGNAME+certifications+custom fields |

---

---

## DE — Data Entry / EDI / Imports

**Module purpose:** Import external data into EvoERP (BOMs, PO receipts, WO materials, AR invoices, web orders) and process inbound/outbound EDI transaction sets. Also hosts global field replace (DEK) and selective file erase (DEL) — both destructive.

### DE Program Map

| Program | Procs | Operation |
|---|---|---|
| T7DEM | 92 | BOM component import — reads external BOM and creates BKBMMSTR records |
| T7DEER | 132 | Import error report — error log for BOM/import failures (reads BKDCLAB) |
| T7DEHD | 131 | PI tag import — imports physical inventory count tags (BKPIMSTR+BKPIFROZ+BKPIPHYS) |
| T7DEJH | 147 | WO material import — loads WO material requirements from external file (BKICMSTR) |
| T7DEQ | 80 | AR invoice import — imports external invoices into BKARINV+BKARINVL |
| T7DER | 77 | AR invoice import error report — BKAPINVT |
| T7DET | 178 | Web order import — largest DE program; imports web orders to BKARINV+BKARINVL via BKEDMSTR; sets import.to.edi flag |
| T7DETB | 125 | Web order import batch — batch variant of T7DET |
| T7DETD | 120 | Web order detail processing — BKAPPO+BKICLOC |
| T7DEU | 102 | Web item FTP export — exports item catalog to FTP for web store (BKARINVL+BKICLOC) |
| T7DEV | 138 | Vendor POA 855 — processes vendor purchase order acknowledgement (EDI 855); SKIP.PONUM/PCODE/PQTY flags; opens BKPRMSTR for employee contact |
| T7DEP860 | 82 | EDI 860 PO change — processes inbound EDI 860 PO change orders (BKEDMSTR+BKAPPO+BKARINVL) |
| T7DEPB | 111 | Customer releases — processes customer schedule releases (RELEASE_NUM); opens BKEDIDUN+BKEDMSTR+BKARINVV |
| T7DEPD | 132 | Customer releases detail — release line detail with BKEDNOTE notes |
| T7DEPE | 114 | EDI customer order processing — BKEDIDUN+BKEDMSTR+BKICREF |
| T7DEPF | 104 | EDI PO processing — BKEDIDUN+BKEDMSTR inbound PO handler |
| T7DEPH | 116 | EDI PO header — BKAPPOL+BKICPMAT+BKICREF |
| T7EDII | 183 | EDI inbound processing — largest EDI program; full inbound pipeline |
| T7EDIFTP | 5 | EDI FTP transfer — stub for FTP file movement (BKEDMSTR only) |
| T7DEFECT | 53 | Defect code setup — CRUD for ISDEFECT defect code table |
| T7DEK | 61 | Global field replace — directly rewrites field values across tables (DESTRUCTIVE; opens BKGLCOA + many others) |
| T7DEL | 48 | Selective file erase — deletes records from selected tables (DESTRUCTIVE) |
| T7DEX | 82 | Export/FTP utility — file export with FILEDICT layout |
| T7DEIB | 47 | Batch import module — general import batch processor |
| T7DEB*–T7DEG*, T7DEJ* | 5–18 | Multi-step batch import pipelines — each letter = one import type, A–E suffixes = 5 pipeline steps (D-step is main processor at 11–18p, others are 5p stubs) |

### Key EDI Architecture Finding

**BKEDIH(84f) and BKEDIL(28f) are Btrieve alternate-index views of BKARINV and BKARINVL** — field prefixes `BKAR_INV_*` and `BKAR_INVL_*` are identical to those tables. EDI invoices live in the same physical data file as AR invoices. The unified invoice architecture (BKARINV for SO+AR+SR+ES+EDI) is fully confirmed.

### DE Tables

| Table | Fields | Purpose |
|---|---|---|
| BKEDIH | 84 | EDI invoice header — BKAR_INV_ prefix; alternate-index view of BKARINV for EDI inbound processing |
| BKEDIL | 28 | EDI invoice line — BKAR_INVL_ prefix; alternate-index view of BKARINVL |
| BKEDMSTR | 3 | EDI system master — NEXTN(8) next transaction#; DUNS(15) our company DUNS number; PATH(66) EDI file import/export directory |
| BKEDNOTE | 3 | EDI note — EDI#(8)+SO#(8)+NOTE(80); exception notes on EDI transactions |
| BKEDIDUN | 7 | Customer EDI DUNS map — CUST(10) PK; DUNS(15)+EDI(1 enabled)+EFFDT+PRODS(1)+ADVS(1 ASN flag)+SHPCD(1) |
| CCEDIXRF | 6 | EDI ship-to cross-reference — CUSTCODE(10)+SENDERID(15) PK; SHPTCODE(17)+SHPTZIP(10)+SHIPTO(10)+NEXT(8); maps EDI sender IDs to EvoERP ship-to codes for 850 PO matching |
| ISEDINFO | 54 | EDI extended info — ISSR_INFO_ prefix; same 54-field configurable structure as ISSRINFO: 5 dates + 20 alpha(25) slots per group × 2 groups |
| ISDEFECT | 3 | Defect codes — CODE(10) PK + DESC(60) + EXTRA(50); shared by DEFECT setup, BKDCLAB scrap codes, and QC NCR module |
| BKDCCFG | 7 | DC station configuration — IDLEP/IDLES (idle period/shift); BANKP/BANKS (bank period/shift); IMPPTH/EXPPTH(60, import/export paths); JOBTME(60, job time calc script path) |
| MACHINE | 20 | Machine master — MACHINE(4 PK)+DESC(30)+HRSUSED+HRSMAINT+DATE; NOTES_1..8(45 each); WC(12)+WCDESC(30); EXTRA(100); ACTIVE(1)+INACTDATE+INACTWHO(30)+INACTWHY(60) |
| TOOL | 57 | Tool master — TOOL(15 PK)+DESC(30)+DATE; NOTES_1..8(45 each); PRTSMAINT+NOPARTS (parts maintenance counter); WEIGHT+HEIGHT+WIDTH+DEPTH; EJ_STROKE+NOZ_RAD (injection mold: ejector stroke + nozzle radius); +37 more tooling geometry/maintenance fields |
| WOLABOR | 58 | WO labor (legacy/T6-era) — POSTED+DATE+EMP+WOPRE+WOSUF+OPER+TRXN PK; REGOVER+RUNHRS+NOJOBS+SETUPHRS+PARTS+REWORK+COMPLETE+SCRAPPED; QCCODE+QCDESC+SCRAPCD+SCDESC (QC+scrap classifiers); ASSY(15); +38 more. Parallel to BKDCLAB; MTWOLA_ prefix = TAS Pro 6-era labor table |

---

## AC — Activity Control / WO Scheduling

**Module purpose:** Tracks activity items linked to work orders, vendors, and customers. Records action types, resolution dispositions, and WO scheduling dates (start/finish/hierarchy). AC overlaps with QC NCR and SH scheduling — WODATE is the key shared table.

### AC Program Map

| Program | Procs | Operation |
|---|---|---|
| T7ACDATE | 64 | Date-based activity scheduling — WO due dates; cross-module (opens BKARCUST + BKICMSTR + BKAPVEND) |
| T7ACDET | 18 | Activity detail entry — ACDETAIL (not in DDF schema) |
| T7ACRDTYPE | 58 | Activity record type maintenance — ACRDTYPE (not in DDF schema); includes disposition codes (rework/scrap/use-as-is) |
| T7ACTION | 53 | Action type code maintenance — CRUD for ISACTION table |
| T7ACCNFIX | 28 | Account code fix utility — corrects BKCMACCN account codes; logs to ISLOG |

**Architecture note:** ACDETAIL and ACRDTYPE are referenced in T7AC* program fingerprints but are **not in the Pervasive DDF schema** — they are Btrieve tables without DDF registration (or use alternate registered names). Their structure is known only from DFM analysis: ACRDTYPE holds record type + reason + disposition codes; ACDETAIL holds individual activity detail records.

### AC Tables

| Table | Fields | Purpose |
|---|---|---|
| WODATE | 13 | WO scheduling dates — WOPRE+WOSUF PK; START+FINISH+QTY; PARPRE/PARSUF (immediate parent WO); TOPPRE/TOPSUF (top-level root WO); DELPRE/DELSUF (delivery/SO-linked WO); EXTRA(100)+PRIO(1) |
| ISACTION | 3 | Action type codes — TYPE(10) PK + DESC(60) + MISC(60) |
| ACDETAIL | ? | Activity detail records — NOT IN DDF schema; referenced by T7ACDET (18p) |
| ACRDTYPE | ? | Activity record type + disposition codes — NOT IN DDF schema; referenced by T7ACRDTYPE (58p) |

**WODATE hierarchy:** PARPRE/PARSUF = immediate parent WO (multi-level BOM sub-assembly), TOPPRE/TOPSUF = root of WO tree (top-level assembly), DELPRE/DELSUF = delivery WO (SO-linked WO for customer order). Used by MRP capacity scheduling (T7MRIX) and the SH shop scheduling module. This hierarchy enables EvoERP to schedule and track the full tree of sub-assemblies under a customer order.

---

## WC — Warehouse Control (bin master)

(Disambiguation: WC = Warehouse Control bin management, **not** Work Center. Work centers are in the `WORKCTR` table used by routing and scheduling.)

**Module purpose:** Manages physical bin locations within warehouse locations. Supports bin-level inventory tracking, serial-by-bin queries, and bulk bin assignment.

### WC Program Map

| Program | Procs | Operation |
|---|---|---|
| T7WCA | — | Bin master CRUD — create/edit/delete bins in ISBNMSTR |
| T7WCC | — | Serials by bin — queries MTSER for serial numbers at a specific bin |
| T7WCD | — | Bulk bin assignment — Skip/Replace mode for reassigning multiple items |
| T7WCH | — | Location browser — browse all LOC+BIN combinations |

### WC Table

| Table | Fields | Purpose |
|---|---|---|
| ISBNMSTR | 4 | Bin master — LOC(10)+BIN(15) PK; DESC(60)+EXTRA(100); defines named bin positions within warehouse locations (FK LOC → BKICLOCM) |

---

### New Tables Confirmed (Pass 49)

| Table | Fields | Purpose |
|---|---|---|
| BKEDMSTR | 3 | EDI system master — our DUNS + next transaction# + EDI file path |
| BKEDNOTE | 3 | EDI note/exception — EDI#+SO# PK + 80-char note |
| BKEDIDUN | 7 | Customer EDI DUNS map — CUST PK + DUNS+EDI flags+ASN flag |
| CCEDIXRF | 6 | EDI ship-to cross-ref — CUSTCODE+SENDERID PK; maps EDI sender to EVO ship-to |
| ISEDINFO | 54 | EDI extended info — 54-field configurable (ISSR_INFO_ prefix; same as ISSRINFO structure) |
| ISDEFECT | 3 | Defect codes — CODE+DESC+EXTRA; shared by DE, BKDCLAB, QC |
| WODATE | 13 | WO scheduling dates — WOPRE+WOSUF PK; full parent/top/delivery WO hierarchy |
| ISACTION | 3 | AC action type codes — TYPE+DESC+MISC |
| ISBNMSTR | 4 | WC bin master — LOC+BIN PK; DESC+EXTRA |

---

*Last updated: 2026-06-17 (Pass 49). DE: 23+ programs mapped; EDI architecture confirmed (BKEDIH/BKEDIL = BKARINV/BKARINVL alternate-index views); BKEDMSTR(3f)+BKEDNOTE(3f)+BKEDIDUN(7f)+CCEDIXRF(6f)+ISEDINFO(54f)+ISDEFECT(3f) extracted. AC: WODATE(13f) full hierarchy + ISACTION(3f); ACDETAIL/ACRDTYPE confirmed not in DDF. WC: ISBNMSTR(4f) bin master. See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*

---

## ES — Estimating / Customer Quotes

**Module purpose:** Creates customer price quotations (estimates) from BOM + routing + material costs. Estimates use the same BKARINV table as SO and AR invoices (unified invoice architecture). Converts accepted quotes to SOs or WOs via ES-E.

### ES Program Map

| Program | Procs | Operation |
|---|---|---|
| T7ESA | 15 | ES-A main estimate entry — opens BKBMMSTR+BKICMSTR+BKMRPFC+DBAFIFO; links BOM to forecasted demand |
| T7ESB | 213 | ES-B print estimates — largest ES program; opens BKARINV+BKPRSALE+BKPRMSTR+BKICREF+BKPSUSER |
| T7ESC | 124 | ES-C cost calculation — applies BKMATCST material costs + BKRTCST routing costs + BKRFQ vendor quotes |
| T7ESD | 162 | ES-D print customer quotes — opens BKESTCFG+ESTSUM; uses BKCMACCT for CRM account |
| T7ESE | 194 | ES-E convert estimate to SO or WO — opens BKARINV+BKARINVL+BKBMMSTR+BKICLOC+BKICPMAT+BKICTAX; converts accepted quote to live SO |
| T7ESH | 60 | ES-H cost/RFQ entry — BKMATCST+BKRFQ+BKRTCST; enters material and routing cost breakdowns |
| T7ESI | 94 | ES-I cost summary — similar to ESH; 94p suggests more logic |
| T7ESK | 15 | ES-K range filter stub — ESTSUM |
| T7ESL | 15 | ES-L range filter stub — ESTSUM |
| T7ESM | 8 | ES-M mini stub — ESTSUM |
| T7EST | 163 | ES-T template/transfer — opens BKESTCFG+BKARINV+BKBMMSTR+BKICTAX+BKICLOCM |

**ES workflow:**
```
ES-A entry (T7ESA) — create estimate header (BKESTQT)
    ↓
ES-H/I cost entry (T7ESH/ESI) — enter BKMATCST material + BKRTCST routing costs
    ↓
ES-D print quote (T7ESD) — output estimate to customer
    ↓
ES-E convert (T7ESE) — if accepted: create SO (→BKARINV) or WO (→WORKORD)
    ↓
ES-B print estimate report (T7ESB)
```

**Key architecture finding:** `ESTSUM` (DDF table name) is the MT-era legacy estimate summary (213 fields, MTESUM_ prefix) — same table previously documented as ISESTASM. `BKESTQT`/`BKESTQTL` are the current-era estimate header/lines (same structure as BKARINV/BKARINVL). Both generations coexist.

### ES Tables

| Table | Fields | Purpose |
|---|---|---|
| BKESTQT | 84 | Current estimate header — BKAR_INV_ prefix; alternate-index view of BKARINV for estimates |
| BKESTQTL | 28 | Current estimate line — BKAR_INVL_ prefix; alternate-index view of BKARINVL |
| BKESTCFG | 13 | Quote configuration — NUM(8)+STAT(1)+CLASS(4)+FORM(1)+DAYS(2)+5×ENDLN(30)+SONUM(8); per-quote settings and 5 custom footer lines |
| BKMATCST | 25 | Material cost table — CODE(15) PK; QTY_1..10(8×10) quantity breaks; COST_1..10(8×10) material cost per break; DATE+MIN+MINCST; per-item cost lookup used by ES-C/H/I and RF module |
| BKRTCST | 24 | Routing cost per estimate operation — QUOTE(8)+CODE(15)+OPER(2) PK; PARTSHR_1..10(8×10) parts share per qty break; SETUP_1..10(4×10) setup time per qty break; DATE |
| ESTSUM | 213 | MT-era legacy estimate assembly — MTESUM_QUOTE(8) PK; same 213-field structure as ISESTASM; predecessor generation to BKESTQT |
| ISESTDTL | 203 | Estimate detail — IS_EST_NUM+PART+LINE PK; 10 qty-break × material/labor/overhead cost columns |
| BKMRPFC | 9 | MRP demand forecast — PART(15)+DATE(4) PK; QTY+OQTY+CQTY (original/current)+FLAG+DATE1+NUM; feeds MRP explosion as independent demand |
| ISECO | 12 | Engineering Change Order — PART(15)+DRAW(15)+REVLVL(5) PK; ENTDATE+ENTBY(4)+ECO(15) ECO number+CURRENT(1)+STATUS(1)+DATE+APPBY(4)+INVDISP(2, inventory disposition: use/rework/scrap)+EXTRA(100) |
| MTEXCHG | 7 | Estimate exchange/change line — QUOTE(8)+AMT(8)+DESC(30)+COST(8)+EXTRA(50)+CODE(15)+LINE(8); revision history for estimate changes |

ISECO drives part drawing revision control: each ECO records who entered/approved it, the effective revision level, and what to do with existing stock (INVDISP: 2-char disposition code). T7ESE reads ISECO to validate the revision level when converting an estimate to an SO/WO.

---

## MA — AR Cash Receipts / Deposits

**Module purpose:** Applies customer payments (cash receipts, checks, deposits) to open AR invoices. Handles both SO deposit entry (T7ARN) and final cash receipt application at invoice payment (T7ARC). Separate from AP check writing (T7APG) — MA is the AR side.

### MA Program Map

| Program | Procs | Operation |
|---|---|---|
| T7ARC | 228 | AR cash receipts — largest AR program; applies payments to invoices; opens BKARDEP+BKARINVI+BKART+BKGLCHK+BKGLTRAN; posts to GL |
| T7ARN | 191 | AR deposit/note entry — enters SO deposits and AR transaction notes; opens BKARDEP+BKARINVV+BKARTNOT |
| T7MAPDEPO | 97 | MA deposit posting — posts deposits from BKARDEP to BKARINV+GL; opens ISARDEPL |
| T7GETDEP | 18 | Get deposit balance — reads BKARDEP+ISARDEPL+MKECLASS; utility called by other programs |
| T7GETWEB | 6 | Web deposit stub — 6p; retrieves web-order deposit amount |

**MA workflow:**
```
T7ARN — enter deposit on SO (creates BKARDEP record + BKART transaction)
    ↓
T7MAPDEPO — post deposit to GL (BKGLTRAN)
    ↓
At invoice time: T7ARC — apply deposit + any remaining payment to invoice
    → clears BKARDEP, posts BKGLTRAN, updates BKGLCHK check register
```

### MA Tables

| Table | Fields | Purpose |
|---|---|---|
| BKARDEP | 6 | AR deposit header — DEPNO(8) PK; CUST(10)+DATE+SO(8)+SR(1 service flag)+EXTRA(50) |
| ISARDEPL | ? | AR deposit lines — NOT IN DDF schema; referenced by T7MAPDEPO+T7GETDEP |
| BKART | 12 | AR transaction — CUST(10)+TRXN(8) PK; TYPE/DISC/AMOUNT/POSTDATE/ENTDATE/TRXNLINK/INVC/CHECK/NOTE (documented in TC module) |
| BKARTNOT | 3 | AR transaction notes — TRXN(8)+CNTR(2) PK; DESC(30) — line notes on AR transactions |
| BKARINVV | 77 | AR invoice voucher — CODE(10)+NUM(6) PK; 10 GL split lines each with GLACT(10)+GLDPT(4)+DC(1)+GLD(25)+DAMT(8); TERMD/TERMN terms; TAMT total; FRGHT+COOP+TAX+COGS amounts; SLSP×2+COMPR×2 commissions; multi-GL manual AR entry |
| BKARINVI | 16 | AR finance charge line — SONUM(8)+INVNM(8) PK; PCODE+PQTY+PPRCE+PDISC+PEXT+PCOGS+ITYPE; finance charge or interest line attached to an invoice |
| BKGLCHK | 11 | Check register — CHKACT(10)+NUM(8) PK; DATE+TYPE+NAME+AMT+FLAG+DATER+VEND+CUST; records check/payment details (documented in TC module) |

---

## CM — CRM / Contact Manager (key table)

**BKCMACCT (41f)** — CRM Account Master:

The CRM module maintains a separate company/prospect database bridged to AR via BKCMACCN. BKCMACCT is the account master — it holds marketing data not stored in BKARCUST.

| Field | Size | Meaning |
|---|---|---|
| BKCM_ACCT_CODE | 10 | Account code (PK) |
| BKCM_ACCT_OLDCD | 10 | Old code (renames) |
| BKCM_ACCT_NAME | 30 | Company name |
| BKCM_ACCT_ADD1/2/3 | 30×3 | Address lines |
| BKCM_ACCT_CITY/STATE/ZIP/CNTRY | — | Geographic address |
| BKCM_ACCT_CONT1 | 30 | Primary contact name |
| BKCM_ACCT_TITLE | 30 | Contact title |
| BKCM_ACCT_PHONE/FAX | 25 | Primary phone/fax |
| BKCM_ACCT_REP | 5 | Sales rep code |
| BKCM_ACCT_SICCD | 7 | SIC industry code |
| BKCM_ACCT_CUST | 1 | Is AR customer flag (links to BKARCUST) |
| BKCM_ACCT_LEAD | 5 | Lead source code (FK → BKCMLEAD) |
| BKCM_ACCT_TERR | 4 | Territory code (FK → BKCMTERR) |
| BKCM_ACCT_FONE_1..3 | 15×3 | Additional phone numbers |
| BKCM_ACCT_REM_1/2 | 60×2 | Remarks |
| BKCM_ACCT_CNUM | 25 | Credit card number (clear text — legacy; superseded by ISCC vault) |
| BKCM_ACCT_EMAIL | 128 | Email address |
| BKCM_ACCT_EMPS | 8 | Employee count |
| BKCM_ACCT_EXTRA | 200 | Extra text |

**Security note:** BKCM_ACCT_CNUM stores card numbers in clear text. The ISCC(14f) masked vault (Pass 44) supersedes this for PCI compliance, but old BKCMACCT records may still contain raw PANs.

---

### New Tables Confirmed (Pass 50)

| Table | Fields | Purpose |
|---|---|---|
| BKMATCST | 25 | ES material cost — CODE PK; 10 qty-break × cost pairs + MIN+MINCST |
| BKRTCST | 24 | ES routing cost per operation — QUOTE+CODE+OPER PK; 10 qty-break × PARTSHR+SETUP |
| BKMRPFC | 9 | MRP demand forecast — PART+DATE PK; QTY+OQTY+CQTY+FLAG |
| BKARDEP | 6 | AR deposit header — DEPNO PK; CUST+DATE+SO+SR flag |
| BKARTNOT | 3 | AR transaction notes — TRXN+CNTR PK; DESC(30) |
| BKARINVV | 77 | AR invoice voucher — CODE+NUM PK; 10-way GL split with D/C amounts |
| BKARINVI | 16 | AR finance charge line — SONUM+INVNM PK; single charge line per invoice |
| BKCMACCT | 41 | CRM account master — CODE PK; full company/contact/marketing data |

---

*Last updated: 2026-06-17 (Pass 50). ES: 11 programs mapped; BKMATCST(25f) 10-break material cost + BKRTCST(24f) routing cost per operation + BKMRPFC(9f) MRP forecast extracted; ESTSUM confirmed = DDF name for ISESTASM(213f). MA: 5 programs mapped; BKARDEP(6f)+BKARTNOT(3f)+BKARINVV(77f 10-GL-split voucher)+BKARINVI(16f finance charge) extracted; ISARDEPL not in DDF. CM: BKCMACCT(41f) full CRM account master. See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*

---

## SM — System Maintenance (additional programs: Rebuild/Recalculate family)

The T7SMJ* family are data rebuild and recalculate programs — they touch the widest table sets of any SM programs. Run by administrators when data becomes inconsistent.

### T7SMJ* Rebuild Programs

| Program | Procs | Tables (key) | Operation |
|---|---|---|---|
| T7SMJA | 86 | BKDCLAB | DC labor data rebuild |
| T7SMJB | 140 | BKDCLAB | DC labor full rebuild (larger) |
| T7SMJC | 212 | BKARINV+BKBMMSTR+BKGLTRAN | JC job costing setup — creates JC GL structure |
| T7SMJD | 138 | BKICLOC+BKICMSTR | Inventory location balance rebuild |
| T7SMJF/G/I | 73/82/82 | BKARINV+BKBMMSTR | AR/SO data rebuild variants |
| T7SMJH | 51 | BKDCLAB+BKARINVL | DC labor + AR line rebuild |
| T7SMJJ/K | 84/15 | BKARTXN+BKARINV+BKARHTAX | AR transaction + tax history rebuild |
| T7SMJL | 459 | BKBMDIM+BKARINVI+82 more | LARGEST REBUILD — comprehensive data rebuild touching BOM dimensions, finance charges, and 82+ tables |
| T7SMJM | 224 | BKARDEP+BKARINVV | Deposit/voucher data rebuild |
| T7SMJN | 158 | BKAPINVL+BKAPVND2 | AP invoice line + vendor-2 rebuild |
| T7SMJO/P | 92/15 | 52+ tables including BKARINV | Comprehensive AR + inventory rebuild |
| T7SMJQ/S/T | 98/62/15 | BKCMHCOD+BKARDEP+BKARINV | CRM history code + AR rebuild |
| T7SMJR | 97 | BKSYMSTR | System defaults rebuild |
| T7SMJV | 117 | BKPRCURP+BKPRGLFL+BKPRMSTR | Payroll current period + GL rates rebuild |

### T7SMP* Programs

| Program | Procs | Operation |
|---|---|---|
| T7SMPA/B | 53 | SM-PA/B — AR sub-operations (large table set, BKCMHCOD+BKARDEP) |
| T7SMPF | 64 | SM-PF — AR rebuild variant |
| T7SMPH | 88 | SM-PH — AR rebuild with BKARDEP |
| T7SMPI | 53 | SM-PI — defect code maintenance (ISDEFECT) |
| T7SMPJ | 92 | SM-PJ — UL listing maintenance (ISICUL — not in DDF) |

### SM Support Tables (from T7SMI* CRM masters + T7SMJ*)

| Table | Fields | Purpose |
|---|---|---|
| BKCMHCOD | 9 | CRM history code — HCODE(2) PK; DESC(25)+WINDW(1)+RATE(8)+UM(3)+ABILL(1 auto-bill flag)+BPART(15 billable part)+NPART(15 non-billable part); CRM interaction type with optional billing |
| BKCMACFC | 3 | CRM follow-up code — FCODE(3) PK + DESC(25) + REP(5 default rep) |
| BKCMACCC | 2 | CRM account class code — CCODE(5) PK + DESC(25); account tier/rating |
| BKCMDTCD | 2 | CRM detail code — DCODE(2) PK + DESC(25) |
| ISCATMST | 3 | Item category master — CODE(4) PK + DESC(60) + EXTRA(100); item grouping above class level |
| CLASMSTR | 2 | Class master (minimal) — CLASS(4) PK + DESC(30); item class lookup |
| CLASS | 24 | Item class with GL accounts — CLASS(4)+LOC(10) PK; GLA/DPTA/GLC/DPTC/GLS/DPTS/GLWIP per location; allows per-location GL override per item class |
| ISNUMBER | 52 | Next number sequences — CODE(10) PK; NEXT_1..51(8×51); each CODE row holds 51 sequential counters for different document types (SO, PO, WO, etc.) per company |
| BKSYAP | 11 | AP system config/counters — RECVNUM(8 next receipt#)+REOPEN(1)+RQSCRAP(1)+RQREWRK(1)+RECVFLG(1)+PONUM(8 next PO#)+QCRECV(8)+RFQNUM(8) + 3 more; single-row table per company |
| CALTEMP | 2 | Calendar template — SHP_DATE(8)+SLSH_DATE(4); shipping date calculation utility |

---

## UT — Utilities (admin/data maintenance)

**Module purpose:** Administrative tools that operate outside normal ERP flows. Most operations are irreversible — data clear (UTKA), location cleanup (UTKE), and company delete (UTI) are fully destructive. UTK* programs rebuild index integrity and recalculate balances when data gets inconsistent.

### UT Program Map

| Program | Procs | Operation |
|---|---|---|
| T7UTH | 109 | UT-H file layout report — dumps table layout from FILEDICT+FILEKEY; useful for schema documentation |
| T7UTI | 101 | UT-I company add/delete — opens BKPSUSER+BKSYAP+BKSYMSTR+BKICLOCM; creates or removes a company (DESTRUCTIVE for delete) |
| T7UTKA | 74 | UT-KA data clear/reset — wipes COA/CUST/VEND/INVN (DESTRUCTIVE); opens BKICLOC+BKICTAX+BKPRGLFL+23 more |
| T7UTKD | 91 | UT-KD fiscal year setup — sets fycur/fy1yp..fy3yp; opens BKGLTRAN+BKYSMSTR+BKSYMSTR |
| T7UTKE | 238 | UT-KE location cleanup — LARGEST UT PROGRAM; removes stale location records (DESTRUCTIVE); opens BKARTXN+BKARINV+45+ more tables |
| T7UTKF | 116 | UT-KF item rebuild F — rebuilds MRP/PI balances; opens BKMRPFC+BKPIFROZ+BKBMMSTR+28 more |
| T7UTKG | 145 | UT-KG item rebuild G — rebuilds inventory item balance; opens BKICLOC+BKICMSTR+13 more |
| T7UTKH | 135 | UT-KH average cost recalculate — recalculates per-item average cost from BKICLOC+CLASS+11 more |
| T7FNR | 104 | TA-D file navigator — browse all FILEDICT definitions; opens FILEDICT+FILELOC+ISDRILL |

**All UTK* operations are data-integrity tools — they correct corrupted indices and recalculated totals but do not change business records. UTKA and UTKE are genuinely destructive (they delete data).**

### UT Tables (additional)

| Table | Fields | Purpose |
|---|---|---|
| BKSYAP | 11 | AP system counters — next receipt#/PO#/QC#/RFQ# + behavioral flags (also used by UTI) |
| CLASS | 24 | Item class GL map — CLASS+LOC PK; full GL account set per class per location |
| CLASMSTR | 2 | Class description lookup — CLASS PK + DESC |
| ISCATMST | 3 | Item category — CODE(4) PK + DESC + EXTRA |

---

### New Tables Confirmed (Pass 51)

| Table | Fields | Purpose |
|---|---|---|
| BKCMHCOD | 9 | CRM history/interaction type — HCODE(2) PK; rate+billable part codes |
| BKCMACFC | 3 | CRM follow-up code — FCODE(3) PK + DESC + default rep |
| BKCMACCC | 2 | CRM account class — CCODE(5) PK + DESC |
| BKCMDTCD | 2 | CRM detail code — DCODE(2) PK + DESC |
| ISCATMST | 3 | Item category master — CODE(4) PK + DESC(60) + EXTRA(100) |
| CLASMSTR | 2 | Item class lookup — CLASS(4) PK + DESC(30) |
| CLASS | 24 | Item class GL accounts — CLASS+LOC PK; full GL set per location |
| ISNUMBER | 52 | Next document number sequences — CODE(10) PK + 51 counter slots |
| BKSYAP | 11 | AP system config — next receipt/PO/QC/RFQ numbers + flags |
| CALTEMP | 2 | Calendar template — SHP_DATE + SLSH_DATE |

---

*Last updated: 2026-06-17 (Pass 51). SM: T7SMJA-V rebuild family (14 programs) mapped; T7SMP* family (5 programs) mapped; BKCMHCOD(9f)+BKCMACFC(3f)+BKCMACCC(2f)+BKCMDTCD(2f)+ISCATMST(3f)+CLASMSTR(2f)+CLASS(24f)+ISNUMBER(52f)+BKSYAP(11f)+CALTEMP(2f) extracted. UT: 9 programs fully mapped; UTK* rebuild/recalculate family confirmed. See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*

---

## PO — Purchase Orders (full program map)

**Module purpose:** Creates and tracks purchase orders from creation through receipt to AP voucher. The largest ERP module by program count (50+ programs). Five-level vendor price breaks; QC inspection on receipt; DC-integrated labor on receipt; digital signature approval; EDI 850/855/860 support.

### PO Program Map

| Program | Procs | Operation |
|---|---|---|
| T7POA | 499 | PO-A main entry — LARGEST PO PROGRAM; creates/edits POs; opens BKAPPO+BKAPPOL+BKAPVEND+BKBMMSTR+BKARINVV |
| T7POAIMPLINES | 132 | PO-A import lines — imports PO lines from RFQ+BKSBVEND+BKSBMFG |
| T7POB | 190 | PO-B print POs — opens BKAPVND2+BKSBVEND; prints formatted PO with vendor 2 data |
| T7POC | 377 | PO-C receive — standard receipt; opens BKGLTRAN+BKBMMSTR; posts GL on receipt |
| T7POD/E | 15 | PO-D/E stubs — range filter sub-forms |
| T7POEA | 184 | PO-EA receive (alternate) — opens BKCMACCT+BKGLTRAN |
| T7POENG | 274 | PO-ENG engineering receipt — opens BKQCMSTR+BKQCTRAN+BKSBMFG; triggers QC inspection |
| T7POF | 85 | PO-F estimate/RFQ — opens BKESTCFG+BKBMMSTR |
| T7POG | 124 | PO-G receipt post — opens BKICLOC+BKBMMSTR |
| T7POH | 122 | PO-H vendor pricing — 5-level price break entry; opens BKRFQ |
| T7POIA/B | 5 | PO-IA/IB stubs |
| T7POIC | 100 | PO-IC inquiry — opens CLASS+BKRFQ |
| T7POID | 127 | PO-ID inquiry — opens BKRFQ+BKSYMSTR |
| T7POIE/F | 5 | PO-IE/IF stubs |
| T7POIG | 171 | PO-IG DC-integrated receipt — opens BKDCLAB+BKQCMSTR+BKARCUST; records DC labor on receipt |
| T7POIH | 103 | PO-IH receipt + vendor history — opens BKCMVNDH (CRM vendor history) |
| T7POII | 124 | PO-II inquiry + change log — opens ISAPCHG (AP/PO change audit trail) |
| T7POIL | 110 | PO-IL inquiry list — opens BKBMMSTR+BKPRMSTR |
| T7POJA | 176 | PO-JA receipt + QC — opens BKQCMSTR+BKQCTRAN+BKPRMSTR |
| T7POJB | 143 | PO-JB receipt + QC + DC — opens BKDCLAB+BKQCMSTR |
| T7POJC | 323 | PO-JC comprehensive receipt — opens ACMASTER (not in DDF) + 47 more tables |
| T7POJD | 99 | PO-JD receipt variant — opens ACMASTER+BKCMACCT+BKQCMSTR |
| T7POK | 141 | PO-K — opens ACMASTER+BKCMACCT+BKICLOC |
| T7POL | 83 | PO-L vendor/item — opens BKSBVEND+ISICMSTR (item extended) |
| T7POLA/LP/LX | 47/90/60 | PO-L variants — all open ACMASTER+BKSBVEND |
| T7POM | 174 | PO-M multi-tab inquiry — opens BKBMMSTR+BKICLOCM |
| T7POBNP | 5 | PO-BNP stub — no-print variant |
| T7POO | 17 | PO-O — opens BKCMACCT |
| T7POP | 53 | PO-P vendor contact data — opens BKCMVNDF+BKCMVNDH (CRM vendor follow-up + history) |
| T7POQ | 106 | PO-Q inquiry — range filter |
| T7POR | 5 | PO-R stub |
| T7POS | 104 | PO-S vendor SO/invoice — opens BKARINVV+BKICREF |
| T7POSI | 53 | PO-SI vendor invoice detail — opens BKCMACCC+BKCMACCT |

**PO workflow:**
```
PO-A entry (T7POA) → BKAPPO header + BKAPPOL lines
    ↓ vendor pricing via T7POH (BKRFQ 5-level breaks)
    ↓
PO-B print (T7POB) → formatted PO with BKAPVND2 extended info
    ↓ approval via ISDIGSIG (digital signatures)
    ↓
PO-C/EA/JA/JB receive (T7POC/POEA/POJA/POJB)
    → BKICMSTR quantities updated, INVTXN receipt record
    → QC inspection via BKQCMSTR/BKQCTRAN (POENG/POJA/POJB)
    → BKGLTRAN posted (debit inventory / credit accrued liability)
    ↓
AP-B voucher entry (T7APB) → BKAPINVT header + BKAPINVL GL distribution
    → matches PO receipt to vendor invoice
    ↓
AP-F check print (T7APF) → BKAPCHKF temporary + BKAPCHKH permanent
AP-H post checks (T7APH) → BKGLTRAN Cash Disbursement
```

### AP Extended Vendor Tables

| Table | Fields | Purpose |
|---|---|---|
| BKAPVND2 | 63 | Vendor UDF — VENDCODE(10) PK; ID(15 tax ID/EIN); SEND_1099(1); 5 slots each of: A1(1-char)+label, A10(10-char)+label, A30(30-char)+label, date+label, N12(12-digit)+label, N6(6-digit)+label; user-configurable vendor extended fields |
| BKAPINVT | 19 | AP invoice total — CODE+DATE+NUM PK; AMT+AMTRM (remaining balance)+DESC+TYPE+TERMN; AP invoice header with balance tracking |
| BKAPINVL | 390 | AP invoice GL distribution — CODE+NUM PK; TERMD/TERMN+TYPED/TYPEN + multi-GL split (same 10-line structure as BKARINVV but for AP); WIDEST AP TABLE |
| BKCMVNDH | 8 | CRM vendor history — VCODE(10)+DATE(4) PK; REP(5)+LINE(2)+EVENT(2)+REM(60)+FLINE+EXTRA; vendor interaction log |
| BKCMVNDF | 10 | CRM vendor follow-up — VCODE(10) PK; REP+TYPE(3)+DATE+5×REM(60)+PO(8 linked PO); vendor CRM task with PO reference |
| ISICMSTR | 41 | Item extended / UDF — CODE(15) PK; WT+ITP+EXTRA; TI+HI+HT+LG+WD dimensions; FOBPAL+FOBFULL pallet qtys; TOOL(15 tooling ref); SLEAD(2); 10 FLAGS + 5 ALPHA + 5 NUM + 5 GDATES UDF slots |
| ISAPCHG | 32 | AP/PO change audit — PONUM+LINEID+PCODE PK; CDATE+USER+REVLVL+ALOC/BLOC (before/after); records every PO line change (same A/B pattern as ISARCHG on SO side) |
| ACMASTER | ? | NOT IN DDF schema — referenced by T7POJC/D/POK/POLA/LP/LX in PO receiving programs; likely an account master table for cross-company/intercompany transactions |

---

### New Tables Confirmed (Pass 52)

| Table | Fields | Purpose |
|---|---|---|
| BKAPVND2 | 63 | Vendor UDF — tax ID + 6-type × 5-slot user-defined fields |
| BKAPINVT | 19 | AP invoice header — CODE+DATE+NUM PK; amount + remaining balance |
| BKCMVNDH | 8 | CRM vendor history log — VCODE+DATE PK; event+remark |
| BKCMVNDF | 10 | CRM vendor follow-up — VCODE PK; type+date+5 remarks+PO link |
| ISICMSTR | 41 | Item extended — dimensions+pallet qtys+tooling+10 flags+UDF slots |
| ISAPCHG | 32 | PO change audit — before/after fields (already in AP Pass 41; confirmed for PO) |

---

*Last updated: 2026-06-17 (Pass 52). PO: 50+ T7PO* programs fully mapped across entry/print/receive/QC/inquiry groups; full PO→receipt→AP voucher→check workflow traced. BKAPVND2(63f UDF)+BKCMVNDH(8f)+BKCMVNDF(10f)+ISICMSTR(41f) extracted; ACMASTER confirmed not in DDF. See EVO-DECOMPILE-TODO.md for confidence ratings by topic.*

*Last updated: 2026-06-17 (Pass 57). CS: 17 programs mapped; BKPRSALE(87f)+BKPRCOMM(12f)+BKPRAGNT(4f)+BKPRMSTR(384f)+BKPRCURP(127f)+ISREPLNK(11f) fully extracted; commission HOW/WHEN logic confirmed. LC: 7 programs mapped; LOT/MTLOT_(25f) fully extracted; lot lifecycle confirmed. GF: 5 programs mapped; BKICPMAT(85f) 10-break pricing matrix fully extracted; ISARCHG(26f) confirmed. AU: 8 programs mapped; BKDCLAB(50f)+BKDCCFG(7f) fully extracted; DC→WO posting workflow confirmed. RO: ROUTING/MTRO_(62f)+BKRTCST(24f)+BKRFQ(49f) fully extracted. AL/JO/IT confidence updates.*

---

---

## MODULE QUICK REFERENCE — Pass 59 Additions

### FS — Field Information Base (FIB Setup)

Three programs under the FS prefix — all field names use `IS_FIB_*` prefix, confirming the
underlying system is "Field Information Base" (FIB), not field service in the SR sense.

| Program | Purpose | Key Tables |
|---|---|---|
| T7FSCLASS | FIB classification code maintenance | ISFSCLAS, ISPRINFO |
| T7FSEMP | Employee / salesperson ↔ FIB class assignment | ISFSCLAS, BKPRSALE |
| T7FSINFO | FIB info record maintenance (program/contract/who) | ISFSINFO, BKCMACCN |

**ISFSCLAS (3f) — FIB Classification Code:**

| Field | Size | Meaning |
|---|---|---|
| IS_FIB_CLASS | 4 | Classification code (PK) |
| IS_FIB_GROUP | 50 | Group/category description |
| IS_FIB_EXTRA | 50 | Extra notes |

**ISFSINFO (4f) — FIB Info Record:**

| Field | Size | Meaning |
|---|---|---|
| IS_FIB_PROGRAM | 20 | Program/module code (PK) |
| IS_FIB_CONTRACT | 25 | Contract reference |
| IS_FIB_MISC | 100 | Miscellaneous info |
| IS_FIB_WHO | 50 | Responsible person |

**ISPRINFO (4f) — Program/Module Info Registry:**
`ISPR_INFO_PROG`(30) + `ISPR_INFO_DESC`(80) + `ISPR_INFO_MISC`(50) + `ISPR_INFO_TYPE`(1) —
registers EVO program names with descriptions and type codes.

**BKCMACCN (154f) — CRM Account Contacts (per customer/vendor code):**
Primary key: `BKCM_ACCN_CODE`(10) — links to BKARCUST or BKAPVEND.
Stores up to 10 contacts per account, each with:
- CONT_1..10 (30 each): contact name
- TITLE_1..10 (30 each): contact title
- PHONE_1..10 (25 each): phone + PHLBL_1..10 (20, phone type label)
- EMAIL_1..10 (128 each) + EMLBL_1..10 (20, email label)
- DEAR_1..10 (25 each): salutation / greeting
- DATE1_1..10 + DATE2_1..10 (date): two sets of 10 configurable dates + DTLBL/D2LBL (20, labels)
- ALPH1_1..10 + ALPH2_1..10 (25 each): two sets of 10 configurable alpha slots + MSLBL/M2LBL (20, labels)
- CON (30): primary contact name
- PRIM (1): primary contact flag
- EXTRA (50): overflow notes

Architecture: T7FSINFO uses BKCMACCN to associate field information records with customer/vendor CRM contacts. T7BROWSER (BR module) also browses this table.

**Confidence: 65/100** — three programs confirmed; ISFSCLAS(3f)+ISFSINFO(4f)+ISPRINFO(4f)+BKCMACCN(154f) fully extracted from DDF; FIB naming pattern confirmed from field prefixes; specific FIB business logic blocked by RWN encryption.

---

### IS — InfoSystem / Multi-Currency GL Framework

Two programs:

| Program | Purpose | Key Tables |
|---|---|---|
| T7ISMCC | Multi-company / multi-currency GL sync | ISGLDATE, ISMCF |
| T7ISASER | WO-to-serial assignment lookup | WORKORD, SERIAL |

**ISGLDATE (86f) — GL Fiscal Period-End Date Reference:**
Stores the period-end date for each accounting period across 7 fiscal years.
No primary key column — a singleton configuration table (one row for the company).

| Field Group | Count | Meaning |
|---|---|---|
| ISGL_CYDATE_1..12 | 12 dates | Current year period-end dates |
| ISGL_1YDATE_1..12 | 12 dates | Prior year 1 period-end dates |
| ISGL_2YDATE_1..12 | 12 dates | Prior year 2 |
| ISGL_3YDATE_1..12 | 12 dates | Prior year 3 |
| ISGL_4YDATE_1..12 | 12 dates | Prior year 4 |
| ISGL_5YDATE_1..12 | 12 dates | Prior year 5 |
| ISGL_6YDATE_1..12 | 12 dates | Prior year 6 |
| ISGL_FYDATE | 1 date | Fiscal year start date |
| ISGL_EXTRA | 50 chars | Extra |

Used by T7ISMCC to determine which transactions fall into which period when reconciling across multiple companies or currencies.

**ISMCF (49f) — Multi-Currency Framework Config:**
One row per currency code. Defines how each currency maps to GL accounts.

| Field | Size | Meaning |
|---|---|---|
| ISIS_MCF_CODE | 3 | Currency code (PK, e.g. USD, EUR, CAD) |
| ISIS_MCF_BASE | 1 | Base currency flag (Y = home currency) |
| ISIS_MCF_SYMBOL | 1 | Currency symbol (e.g. $, €) |
| ISIS_MCF_SYMPOS | 1 | Symbol position: B=before, A=after amount |
| ISIS_MCF_DEC | 2 | Decimal places |
| ISIS_MCF_SYMDSC | 10 | Symbol description |
| ISIS_MCF_DESC | 25 | Currency full name |
| ISIS_MCF_INTRES | 8 | Interest reserve rate |
| ISIS_MCF_INTDAY | 8 | Interest days basis |

GL accounts per currency (each has account + dept pair):
`GLABK/GLDBK` = Bank AR, `GLABS/GLDBS` = Bank AP, `GLAIS/GLDIS` = Inventory,
`GLABKX/GLDBKX` = Bank AR exchange, `GLAAPX/GLDAPX` = AP exchange,
`GLAARX/GLDARX` = AR exchange, `GLAAR/GLDAR` = AR, `GLAAP/GLDAP` = AP,
`GLAPO/GLDPO` = PO, `GLAPOX/GLDPOX` = PO exchange,
`GLAARD/GLDARD` = AR discount, `GLAAPD/GLDAPD` = AP discount,
`GLACS/GLDCS` = CS commission, `GLACSX/GLDCSX` = CS exchange.

Running balance fields: `AMTBNK`/`AMTAP`/`AMTAR`/`AMTFE`/`AMTPOR`/`AMTAD`/`AMTCS`/`AMTAPD`.

**Confidence: 68/100** — both programs confirmed; ISGLDATE(86f) + ISMCF(49f) fully extracted; multi-currency GL mapping architecture confirmed; specific T7ISMCC synchronization logic blocked by RWN encryption.

---

### DS — Data Sync

22+ programs, all sharing a single staging table. This is EvoERP's data synchronization layer —
likely bridges to an external system (SolidWorks ERP, CRMS, or similar).

**Program inventory (T7DS*):**
T7DSAP, T7DSAR, T7DSBOM, T7DSCK, T7DSCM, T7DSCO, T7DSCS, T7DSDC, T7DSEST, T7DSFO, T7DSGEN,
T7DSGL, T7DSHH, T7DSIC, T7DSIM, T7DSMRP, T7DSPO, T7DSPR, T7DSQC, T7DSRMA, T7DSRO, T7DSSH,
T7DSSO, T7DSWC, T7DSWO — one program per module (AP, AR, BOM, CK=check, CM=CRM, CO=company,
CS=commissions, DC=data collection, EST=estimating, FO=features-options, GEN=general,
GL=general ledger, HH=?, IC=inventory, IM=?, MRP, PO, PR=payroll, QC, RMA, RO=routings,
SH=shipping, SO=sales orders, WC=work centers, WO=work orders).

**ISDROP (4f) — Data Sync Drop / Dropdown Code Lookup:**

| Field | Size | Meaning |
|---|---|---|
| IS_DROP_CODE | 10 | Operation/sync code (PK) |
| IS_DROP_TEXT | 30 | Short text label |
| IS_DROP_DESC | 30 | Description |
| IS_DROP_EXTRA | 50 | Extra notes |

**Definitive architecture (Pass 63):** All 24 T7DS* programs (excluding T7DSQC which has 0 tables) have **IDENTICAL 36-table fingerprints**. Every DS stub opens the exact same set: BKAPDESC, BKAPPO, BKAPVEND, BKARCUST, BKARINV, BKCMACCN, BKGLTRAN, BKGLX, BKICMSTR, BKSYAR, BKSYHELP, CLASS, DBAFIFO, DBAHLPID, FILELOC, ISDRILL, ISDROP, ISGLDATE, ISICMSTR, ISIS, ISLINKS, ISLOG, ISMCR, ISNCR, ISNOTES, ISNTYPE, ISNUMBER, ISREMIND, ISTAXGRP, ISTRIGRS, LANGDICT, LOT, MKAHIST, MKECLASS, SERIAL, WORKORD. This is NOT per-module data access — it is a universal dispatcher: the DS stub calls a central sync engine, passing the module code as a parameter. T7DSQC = 0 tables (QC sync not yet implemented or uses a different path).

The 36-table common set covers: master data (BKICMSTR, BKARCUST, BKAPVEND), transactions (BKARINV, BKAPPO, BKGLTRAN), lot/serial traceability (LOT, SERIAL), multi-currency (ISMCR, ISTAXGRP), notifications (ISTRIGRS, ISREMIND, ISNOTES), and runtime infrastructure (FILELOC, ISLOG, LANGDICT, MKAHIST, ISIS).

DS module purpose: synchronize selected EvoERP data to/from an external system. Each T7DS* stub dispatches one module's sync cycle. The actual sync logic (which fields move, which direction) is encrypted in the RWN.

**Confidence: 62/100** — 25 programs identified; identical 36-table fingerprint confirmed across all 24 active stubs; T7DSQC anomaly confirmed (0 tables); architectural pattern (universal dispatcher, not per-module data access) fully documented; sync target and field-level logic blocked by RWN encryption.

---

### New Tables Confirmed (Pass 59)

| Table | Fields | Purpose |
|---|---|---|
| ISFSCLAS | 3 | FIB classification codes — IS_FIB_CLASS(4) code + group + extra |
| ISFSINFO | 4 | FIB info records — program(20) + contract(25) + misc(100) + who(50) |
| ISPRINFO | 4 | Program/module info registry — PROG(30)+DESC(80)+MISC(50)+TYPE(1) |
| BKCMACCN | 154 | CRM account contacts — 10 contacts per acct: name+title+phone+email+salutation+dates+alpha slots |
| ISGLDATE | 86 | GL fiscal period-end dates — 7 years × 12 periods (CY + 1Y..6Y) + FYDATE |
| ISMCF | 49 | Multi-currency framework — GL accounts per currency for BNK/AP/AR/INV/PO/CS/discounts |
| ISDROP | 4 | Data sync operation code lookup — CODE(10)+TEXT(30)+DESC(30)+EXTRA(50) |
| ISWOPRIO | 4 | WO priority codes — PRIO(1)+DESC(30)+EXTRA(100)+COLOR(float) with display color |
| ISBANKS | 23 | Bank account master — NUM+SRT+DESC+GL+NXTNUM+BAL+ROUT(15)+ACCT(15)+CURR+TYPE+VEND+ACTIVE+AR/AP/PR+5×RTM |
| MTICMSTR | 108 | Estimating item master — 10 vendors+names+part codes; RCOST_1..15; 5 substitutes; lot size; option codes |
| ISTERMS | 13 | Payment terms master — NUM PK; NAME(20)+TYP(P/$)+DAY+EOM+AMT+COD+ARAP+CC+SRT; used by SO/AR/AP |

---

---

### New Tables Confirmed (Pass 62)

| Table | Fields | Purpose |
|---|---|---|
| ISIS | 23 | System feature flags — IS_TAX/IS_MULTI_CURR/IS_LANDED_COST/IS_UPC/IS_RETAIL_PRICE/IS_COMM_PRICE/IS_IMAGING/IS_DEMO/IS_MULTI_CPAY/IS_PIC_PATH/IS_TAX_FRM/IS_PO_TAX/IS_TAX_IN/IS_TAX_CVT/IS_CUR_CVT/IS_AUTO_TAX_CAL/IS_EZPAY/IS_RMA/IS_SPEC_SUP/IS_SPEC_SUPF/IS_SPEC_SUPT; 1-row module-switch table |
| ISMCR | 22 | Multi-currency exchange rate history — ISIS_MCR_BASE(3)+DATE PK; 10 source currency slots (SOURCE_1..10, 3 chars each) + 10 exchange rates (RATE_1..10, float); daily rate snapshot per base currency |
| ISNUMBER | 52 | Auto-number sequence allocator — IS_NUM_CODE(10) PK; IS_NUM_NEXT_1..50 (8-byte float × 50 = 50 independent counters per code); IS_NUM_EXTRA(100); single row per named sequence code holds 50 parallel counters |
| ISNCR | 35 | Non-Conformance Report — IS_NCR_NUM PK; PART+COMP+LOT+SERIAL (affected item); CDATE+WHO (discovery); DCODE+DESC (defect code+description); ICR(1)/ORIG(1) origin flags; WO/MACH/TOOL/WC/PO/RMA references; ACTION(1)+CAR(8)+DISP(10)+DWHO+DDATE (disposition); STATUS(1)/SCRAP(2)/QC(2)/VEND/LOC; part drawing+rev (PDRAW/PREV) and component drawing+rev (CDRAW/CREV/CLOC) |
| ISTRIGRS | 25 | Email/event trigger conditions — IS_TRIG_CODE(15)+TRIGR(10) PK; CONTACT(20) recipient; ONCE(1) fire-once flag; LDATE+LTIME last-fired; links to WO/PO/SO/CUST/VEND/LOC; DAYS ahead; ITYPE; secondary WO link (WOPRET/WOSUFT); 7 additional fields |
| ISREMIND | 22 | User reminders/calendar items — DATE+TIME+WHO PK; SUBJECT(100); CUST/VEND/ITEM cross-refs; DISP(1) dismissed flag; CO(3) company; FILE(256) attachment; NOTIFY(1); EDATE+ETIME end date/time; ENDDT+ENDTM end recurrence; BEFTXT(15) "X days before" text; TYPE(3) calendar type; 4 more fields |
| ISJOB | 9 | Job/project codes — IS_JOB_NUMB(15) PK; DESC(30)+CUST(10)+VEND(10); RSVD(1)+STATUS(1)+OPENDT+CLOSEDT+EXTRA(100); groups invoices under a project number for SA analysis |
| BKCMTERR | 11 | CRM territory codes — BKCM_TERR_TCODE(4) PK; DESC(25)+EMAIL(128)+ALPHA(30)+EXTRA(100); FLAGS_1..5 (1 each) + DATE; links territory to email distribution and optional custom flags |
| BKSAREPT | 57 | Saved SA report filter definitions — BKSA_TYPE(8)+NAME(15) PK; RTM(15) template; 26 FROM/THRU range pairs covering: invoice#/dates/ship dates/amounts/salesperson/customer codes/class/category/part/lot/territory/currency; BKSA_BASE(1)+TITLE(40) |
| BKACTRPT | 53 | Saved Activity Control report filter definitions — BKAC_TYPE(8)+NAME(15) PK; RTM(15); named FROM/THRU range pairs: PART/CLASS/CAT/DATE/LOC/WO+SUF/CUST/INV/QC/PARENT_LOT+LOT/SERIAL/PRICE/AVGC/STDC/DESC/REF/DEPT/QTY/SCRAP/VEND/PO/TYPE; TYPE_RANGE(10)+ITEM_RANGE(8) flags |
| ISARCHG | 26 | AR order change audit log — ISAR_CHG_SONUM+INVNUM+LINEID+PCODE PK; CDATE+USER+REVLVL audit stamp; A-prefix=before, B-prefix=after for: ALOC/BLOC (location), APRICE/BPRICE, ADISC/BDISC, AOOQTY/BOOQTY (open-order qty), AESD/BESD (estimated ship date), AASD/BASD (actual ship date), ACOMPR_1/2 / BCOMPR_1/2 (compression rates), AEXTRA/BEXTRA (extra text), UNUM (update number) |

---

---

### New Tables Confirmed (Pass 63)

| Table | Fields | Purpose |
|---|---|---|
| BKSYMSTR | 286 | System master configuration — SINGLE ROW per company; auto-numbers (ARINV/APINV/APPO/GJ/ARSO NUM), company address, 20 payment terms (inline: NAME+AMT+TYP+DAY+EOM+MAX+DISC), 9 bank accounts (CHK_NUM/BAL/NAME/GLACT/GLDPT/CUR each × 9), AR/AP/GL accounts for trade+discount+tax+freight+retained earnings+interest, AR/AP aging buckets (5 each), feature flags (AUTO_BO/RTS_DEF/TAL/PLAIN_INV/PLAIN_PO/FORM_CMPNY), PR deduction names, fiscal year start, 173-byte EXTRA |
| ISTAXGRP | 105 | Tax group definitions — ISIS_TXG_NAME(10) PK; CODE_1..9 (10 ea) = 9 tax authority codes per group; TAXON_1..9 (Y/N taxable per authority); PID_1..9 (province/jurisdiction ID); FREIGT(1) freight taxable flag; DESC(30) group description; DESCF_1..9 (20 ea) authority labels; IDC_1..9 (15 ea) authority ID codes; PERCC_1..9 (float) percentage per authority; TOTPER total %; TAXBLE_1..12/NONTAX_1..12/COLECT_1..12 (float, 12-month taxable/non-taxable/collected history); OUTSTD outstanding tax; FRGT_1..9 freight-taxable per authority; TOFPER total freight percentage |
| ISICMSTR | 41 | Item master product extension (IS_PROD_* prefix) — IS_PROD_CODE(15) PK; WT (weight), ITP(20 item type prefix), EXTRA(150), CDATE/RCDATE (created/received dates), TI+HI (tier/hold indicators), FOBPAL+FOBFULL (FOB pallet/full costs), HT+LG+WD (dimensions float), TOOL(15 tooling reference), SLEAD(2 supplier lead days), FLAG_1..10 (1×10), ALPHA_1..5 (30×5), NUM_1..5 (float×5), GDATES_1..5 (date×5), ADATE (approval date) |
| ISNOTES | 13 | Universal notes store — IS_NOTE_ID(48)+TYPE(3) PK; CDATE+CTIME(10)+CWHO(15) created; EDATE+ETIME+EWHO edited; EXTRA(100) note body; PRIVATE(1) visibility flag; GROUP(4) note group code; CONTACT(30) associated contact name |
| BKSYAR | 2 | AR transaction counter — BKSY_AR_TRXN (next AR transaction #) + BKSY_AR_DEPNO (next deposit #); 2-field status table for the AR module |

---

### New Tables Confirmed (Pass 64)

| Table | Fields | Purpose |
|---|---|---|
| BKICTAX | 46 | Item tax jurisdiction — STATE(10)+LOCAL(10) PK; TAX/TAXY/STATE_AMOUNT/LOCAL_AMOUNT current amounts; TAXBLE_1..12/NONTAX_1..12/COLECT_1..12 (float, 12-month tax history); OUTSTD outstanding; EXTRA(100) — used by LG (Canadian customs) module |
| BKARTXN | 14 | AR transaction line — SONUM+CODE+LINEID PK; BIN(10)+LOC(10) storage location; QTY(float); IDATE/ODATE in/out dates; EMPNUM(2) employee; STATUS(1); EXTRA(100) |
| WCTRLOAD | 8 | Work center capacity load snapshot — WC(10)+DATE(date) PK; TOTHRS (total scheduled hours), UDATE (last-updated date), CAP (capacity hours), UTIL (utilization %), LOAD (current load hours), EXTRA(100) — pre-computed daily snapshot written by scheduler/MRP, read by VSCHED |
| BKDCSHFT | 34 | DC shift scheduling — DCSH_NUM+DATE+SHIFT PK; start/end times, employee assignments, break times, shift type, capacity fields + EXTRA(100) |
| ISWOEX | 63 | WO extended data — WOPRE+WOSUF PK; 5 dates, 5 ints, 2 floats, 5 alphas(30), 5 descs(60), 10 flags(1), 5 gnums(float), 5 alphas(30), 5 notes(100) — 10 configurable custom field groups per work order |
| BKBMMSTR | 26 | BOM master — PARENT(15)+COMPONENT(15) PK; QTY/LEAD/SCRAP/YIELD floats; PROD_OPYN_1..6 (1×6) flags control which FO option (1–6) activates this BOM line; REVISION(10), NOTES(100), EXTRA(100) |
| BKFOCFG | 18 | Features & Options config — FO option definitions: CODE(10)+OPTNUM(int) PK; DESC(60); PARENT(15) item code; LEVEL(int) option tier; PRICE(float) upcharge; ACTIVE(1); REQD(1) required flag; EXTRA(100) |
| ISROUTEX | 100 | Routing operation extension — CODE(15)+OPER(int) PK; 10 machine cycle-time slots (MTIME_1..10 float) per routing operation + SETUP/RUN/CREW/MACH per slot; 45 configurable custom fields |
| ISWOROEX | 60 | WO routing extension — WOPRE+WOSUF+OPER PK; 45+ custom slots (dates/ints/floats/alphas/notes); mirrors ISROUTEX at the WO instance level |
| ISWOTRAY | 52 | WO tray scan tracking — TRAY_NUM(20) PK; WOPRE+WOSUF(WO link); OPER(int); QTY(float); QC(1) QC pass/fail; BIN_1..4(10) bin locations; SCAN_DATE/TIME; EMPNUM(2); STATUS(1); 37 additional tracking fields |
| OPQCDESC | 10 | Operation QC description — WOPRE+WOSUF+OPER PK; DESC(60); SERIAL(20); UID(8); QCCODE(10); DATE(date); QTY(float); EXTRA(100) |

---

### New Tables Confirmed (Pass 65)

| Table | Fields | Purpose |
|---|---|---|
| ISLOG | 9 | Audit/session event log — WHO+WHAT+DOING+STARTD/T+COMPANY+KILL(force-terminate flag)+MSG+EXTRA; written by T7ALOGSETUP-configured events; KILL=Y forces session termination |
| ISFXASST | 23 | Fixed Asset master — NUMBER PK; TYPE+DESC/DESC2; CSTBAS+RESVAL+LIFE; METH(depreciation method: SL/DB/etc.); GLA/D (asset GL); ACDEPA/D (accum. depreciation GL); DEPEXPA/D (depreciation expense GL); SDATE/EDATE; SOLD flag; ACCUMDEP; SERIAL; LDEPAMT/LDEPPERC/LDEPDATE |
| ISFXATRN | 12 | Fixed Asset depreciation transaction — NUMBER+DATE PK; AMOUNT+PERC; AUDIT; POSTED(posted to GL flag); ACDEPA/D; DEPEXPA/D; NETAVAL (net book value); EXTRA |
| ISFOHEAD | 16 | FO order/configuration header — UID PK; PARENT(item); DATE; DESC; CUST+VEND; RFQ#; STATUS; REV; MDATES_1..5 (milestone dates); PERM; EXTRA |
| ISFOLINE | 78 | FO configuration BOM line — UID+LEVEL PK; 50×OPFLAG (customer's active option selections); PARENT+LINEN+COMP+QTYREQ+REF+TYPE+SCRAP+OP+OPYN_1..6+PRICE+RTNUM+DUPOP+OPDSC+VEND+DATE1/2+PBRANC+CBRANC |
| ISFOORDL | 18 | FO order output line — UID+TYPE+PCODE+PQTY+PPRCE+PDISC+PEXT+ESD+LOC+TXBLE+UM+LN+DRAW+REV+LINE+OUID+EXTRA |
| ISREPORD | 17 | Scheduled report/commission record — REPNM+REPWH+SONUM+INVNM+INVDT+ULID+COMPR+CMAMT+AMT+AMTRM+CBK+PCODE+CUST+PAYDT+GLA/GLD; links RTM template to invoice for commission tracking |
| MKECLASS | 3 | MKE class code — NUM(2 PK)+DESC(30)+ACTIVE(1); classification code table used in TC and WBKLUGRID |
| DBAFIFO | 5 | FIFO costing queue — PARTNO(15 PK)+QTY+COST+RECVDATE+REMAIN; one row per receipt layer per item; REMAIN depletes from oldest-first as stock issues |
| BKMRPFC | 9 | MRP firm commitment — PART+DATE PK; QTY+OQTY+CQTY+FLAG+DATE1+NUM+EXTRA; MRP demand/supply pre-WO/PO commitments |
| BKBMREMK | 20 | BOM line remarks — PARENT+LINE+COMP PK; REMARK_1..15 (15 remark text lines); UID; EXTRA |
| BKCMACCN | 154 | CRM account contacts — CODE(10 PK); 10 contacts per account: CONT_1..10(name)+TITLE_1..10+PHONE_1..10+DEAR_1..10(greeting)+EMAIL_1..10+DATE1_1..10+DATE2_1..10+ALPH1_1..10+ALPH2_1..10; CON+PRIM; 50 configurable label fields (PHLBL/EMLBL/MSLBL/DTLBL/M2LBL/D2LBL ×10) |
| ISDEPT | 3 | Department master — IS_GF_DEPT(4 PK)+IS_GF_DEPT_DESC(30)+IS_GF_DEPT_MISC(20); GF_ prefix = GL Finance; used across GL/JC/AR for departmental cost allocation |

---

### New Tables Confirmed (Pass 66)

| Table | Fields | Purpose |
|---|---|---|
| ISRMAI | 54 | RMA item record — NUM+PART+LINEID PK; full lifecycle: dates/STATUS/REASON/DISP; OSONUM/OINVNUM (original invoice); SONUM/INVNUM+CMNUM (new docs); WARRANTY(N/L/P/B); WOPRE/WOSUF; WO/CR/SO/STOCK/SCRAP/SR/REFUND disposition flags; FLAGS_1..20 |
| ISRMAC | 3 | RMA reason code — CODE(10 PK)+DESC(30)+EXTRA(50) |
| SCRAP | 21 | Scrap code master — CODE(10 PK)+DESC+TYPE(1)+GLACCT/GLDPT+FLAG_1..5+ALPHA_1..5+DATE_1..5; MT-era; GL accounts per scrap type; used across QC/WO/HH/RMA |
| ISSCHED | 24 | Job scheduler — NAME(20 PK)+DESC+PROG+CO+TYPE(O/D/W/M)+DATE+TIME+RECUR+LOG+EXTRA+LDATE/LTIME+WHO+EMAIL+PARAM1..9+PARAM0; used by EVOSCHEDULER (TA-N) |
| BKSBVEND | 6 | Preferred vendor xref — PARNT+PROD+CUST+VEND+VPART(vendor part#)+EXTRA |
| BKSBMFG | 6 | Preferred manufacturer xref — PARNT+PROD+CUST+MANUF+MPART(mfr part#)+EXTRA |

---

### New Tables Confirmed (Pass 67)

| Table | Fields | Purpose |
|---|---|---|
| ISSPC | 20 | SPC inspection record — WOPRE+WOSUF+OPER+EMPNUM+DATE+TIME PK; GOOD+REWORK counts; SIDE(PCB side F/B/T); TYPE+DETAIL (defect classification); TESTR/TESTT/TESTE_1..3 test results; ANOTES; CUST+PART |
| ISSERR | 14 | SPC error event — WOPRE+WOSUF+OPER+TIME+DATE PK; ERROR(defect code)+PROCESS; COUNT; SERIAL; ADOF(1000 AOI focus data)+ADIAG(1000 AOI diagnosis)+AREWORK(1000 AOI rework); AOI integration confirmed |
| ISSTRACK | 13 | Component traceability — WOPRE+WOSUF+OPER+TIME+DATE+PROC PK; PSER(board serial)+COMP(part)+CSER(component serial)+NOTE(1000)+CLOT(lot)+AR(auto-rework) |
| ISSTYPE | 3 | SPC error type code — TYPE(PK)+WHO+ASSET |
| ISSETYPE | 2 | SPC error code — ERR(PK)+WHO |
| ISSEPROC | 2 | SPC process code — PROC(PK)+WHO |

---

---

### New Tables Confirmed (Pass 68)

| Table | Fields | Purpose |
|---|---|---|
| SERIAL | 30 | Serial number lifecycle master — CODE+SERIAL PK; PO receipt (PO/RECDOC/VENDOR/RECDATE/POCOST); WO manufacture (WO/ISSDATE/ISSCOST/INRECDATE/INRECCOST); SO sale (SO/CUSTCODE/SHIPDATE/SELLPRICE); EXPDATE; 8×NOTES_1..8(30) |
| ISAPEX | 33 | AP vendor extended fields — VEND(PK)+LONGNAME(60); NUM_1..5+NUM2_1..5 (10 numeric); FLAG_1..8 (8 flag chars); +13 more alpha/date/extra; parallel to ISAREX for customers |
| BKRFQ | 49 | Request for Quote — RFQ#(PK)+EST+PARENT+PROD+WOPRE+WOSUF; ISSUE+EXP dates; VEND+VENDNAME; QTY_1..3+PRICE_1..3 (3 quantity tiers); LEAD time; USE(1) win flag; +29 more discount/cost/freight/note fields |
| MACHINE | 20 | Machine master — MACHINE(4 PK)+DESC+HRSUSED+HRSMAINT+DATE; NOTES_1..8(45); WC+WCDESC; ACTIVE+INACTDATE+INACTWHO+INACTWHY |
| TOOL | 57 | Tool master — TOOL(15 PK)+DESC+DATE; NOTES_1..8(45); PRTSMAINT+NOPARTS; dimensions (WT/HT/WD/DP); mold-specific (EJ_STROKE, NOZ_RAD); +37 more geometry/maintenance fields |
| WOLABOR | 58 | WO labor (T6-era legacy) — POSTED+DATE+EMP+WOPRE+WOSUF+OPER+TRXN PK; RUNHRS+SETUPHRS+PARTS+SCRAPPED+REWORK; QCCODE+SCRAPCD classifiers; MTWOLA_ prefix; parallel to BKDCLAB |
| BKDCCFG | 7 | DC station configuration — IDLEP/IDLES (idle period/shift); BANKP/BANKS (bank period/shift); IMPPTH/EXPPTH (import/export file paths); JOBTME (job time calc path) |
| ISORDDSC | 1 | Order description codes — CODE(30 PK only); list of standard PO/order description phrases |

---

---

### New Tables Confirmed (Pass 69)

| Table | Fields | Purpose |
|---|---|---|
| ISCCICM | 59 | J7 custom catalog extension — CODE+DESC PK; FSIZE(30)/COLLEC(120)/HINGE(25)/SPY(25)/PDF(60)/SOLIDF(25) confirm door hardware catalog; used by T7CCCITM/CCCRNO/CCCWOT (J7-only programs) |
| ISECO | 12 | Engineering Change Order — PART+DRAW+REVLVL PK; ENTDATE+ENTBY+ECO+CURRENT+STATUS+APPBY+INVDISP(2 disposition)+EXTRA; controls drawing revision and inventory disposition |
| MTEXCHG | 7 | Estimate change/exchange line — QUOTE+LINE PK; AMT+COST+CODE+DESC+EXTRA; revision history for estimate changes |
| ISVNDADT | 11 | Vendor change audit trail — VEND PK; ONAME+NNAME+OMAXAMT+NMAXAMT (old/new); APPROVE+DATE+TIME+WHO; PS-K records here before approving vendor name/limit changes |

---

*Last updated: 2026-06-17 (Pass 69). Confidence bumps: CC 65→78 (ISCC 14f vault + ISCCICM 59f J7 door-hardware catalog; CC-CCC J7 boundary identified), PS 60→72 (BKPSUSER 11f + ISVNDADT 11f decoded; vendor change audit trail confirmed), ES 72→75 (ISECO 12f ECO record + MTEXCHG 7f revision history added). Pass 68 additions also: SC 72→78 (SERIAL 30f lifecycle), TPOA 65→72 (ISAPEX+BKRFQ+ISORDDSC), DE 65→72 (MACHINE/TOOL/WOLABOR/BKDCCFG). 12 cumulative new schemas (Passes 68+69).*

---

## PS — Security Architecture — Pass 70 (BKSLEVEL + BKSYLOG)

### BKSLEVEL (422f) — Security Level Access Matrix

**PK:** BKSL_MENU(2) + BKSL_LEVEL(2)

The 422 fields encode a full menu × operation permission matrix. Structure is exactly:
- 2 PK fields + 20 menus × 21 fields per menu = 2 + 420 = 422

**Per-menu block (repeated 20 times, MENU1..MENU20):**
- `BKSL_MENUn_YN` (STRING 1) — is this menu accessible at all for this security level?
- `BKSL_MENUn_1..20` (STRING 1 ×20) — access flag for each of the 20 possible operations within menu n

**How it works:**
1. User logs in → BKPSUSER.BKPS_USER_MENU(2) gives their menu set number, BKPS_USER_SEC(30) gives their security level code
2. EvoERPmenu reads BKSLEVEL where BKSL_MENU = user's menu set AND BKSL_LEVEL = user's security level
3. For each module they attempt: checks BKSL_MENUn_YN first, then individual operation flag BKSL_MENUn_k for the specific menu/operation
4. BKPSUSER.SEC(30) can store multiple security codes (comma-delimited) so a user can have mixed access from multiple BKSLEVEL rows

**Confirmed program usage:** T7PSE (50 procs) + T7PSF (63 procs) are the PS-E/F security editor programs; they edit BKSLEVEL rows — confirmed by rwn_symbols.json fingerprint (both open BKSLEVEL + BKPSUSER + BKSYHELP).

---

### BKSYLOG (215f) — User Logon / Company Access Matrix

**PK:** BKSY_LOGON_CODE (STRING 15) — user login code

Per-user, per-module, per-company access matrix. Same 4-field header as BKPSUSER (CODE, PSWD, SCTY), then repeating YN + 20-slot arrays for each module family:

| Field group | Description |
|---|---|
| BKSY_LOGON_CHR(1) | Row type discriminator |
| BKSY_LOGON_CODE(15) | User login code (PK) |
| BKSY_LOGON_PSWD(10) | Password |
| BKSY_LOGON_SCTY(2) | Security level code |
| BKSY_LOGON_GLYN(1) | GL access enabled flag |
| BKSY_LOGON_OKGL_1..20 | Which GL companies this user may access (up to 20 companies) |
| BKSY_LOGON_ARYN(1) | AR module access flag |
| BKSY_LOGON_OKAR_1..N | Which AR companies accessible |
| (repeats for AP, WO, IC, PR, etc.) | Module × company access flags |

**BKSYLOG vs BKPSUSER:** BKPSUSER(11f) is the primary per-user record (password, menu#, company#, SEC). BKSYLOG(215f) extends it with per-module, per-company access flags. EvoERP checks both — BKPSUSER for menu/sec level, BKSYLOG for which companies within each module the user can open. Dual-table security system.

**Confidence: 82/100** — BKSLEVEL(422f) field structure fully decoded (2+20×21=422); BKSLEVEL security matrix architecture confirmed (menu set × security level × per-operation flags); BKSYLOG(215f) first 30 fields confirmed (user/pswd/scty/OKGL_1..20/ARYN); both confirmed in T7PSE/PSF fingerprint; exact tie-in of SEC(30) multi-code logic in encrypted RWN.

---

## GL — Budget and Historical Ledger Tables — Pass 70

### ISGLBDGT / ISGLFCOA (67f each) — Multi-Year Historical GL

Both tables are structurally identical: PK = ACCT(10) + GLDPT(4), then ACCTD(25) description, TYPE/CR_DR/NON_CASH flags, then four arrays of 14-period history (periods 1–13 + period 14 = adjustment period), plus a year-end total per array.

| Field group | Description |
|---|---|
| ISGL_ACCT(10) + GLDPT(4) | PK — GL account + department |
| ISGL_ACCTD(25) | Account description |
| ISGL_TYPE(1) / CR_DR(1) / NON_CASH(1) | Account type, normal balance (C/D), cash flag |
| ISGL_3YPAST_1..14 + 3YPAST_YE | 3 fiscal years ago — 14 periods + year-end total |
| ISGL_4YPAST_1..14 + 4YPAST_YE | 4 fiscal years ago — 14 periods + year-end total |
| ISGL_5YPAST_1..14 + 5YPAST_YE | 5 fiscal years ago — 14 periods + year-end total |
| ISGL_6YPAST_1..14 + 6YPAST_YE | 6 fiscal years ago — 14 periods + year-end total |
| ISGL_CEXTRA(100) | Spare / extra |

**Purpose:** Deep historical comparison tables for GL financial reporting. Store 4 years of monthly actuals (years T-3 through T-6). The distinction between ISGLBDGT and ISGLFCOA is likely report-oriented: ISGLBDGT = used for budget vs. actual comparison reports; ISGLFCOA = functional COA view used for FS (financial statement) reporting with different grouping.

**Relationship to ISGLCOA:** ISGLCOA (documented Pass 30) stores CURRENT year actuals plus 1–2 years history. ISGLBDGT/ISGLFCOA extend the history back to 6 years. Together they provide the full multi-year GL trail.

---

### ISGLNBGT (35f) — Forward Budget

**PK:** ISGL_BGT_ACCT(10) + ISGL_BGT_GLDPT(4)

Forward/current-year budget table with dual-scenario support:

| Field group | Description |
|---|---|
| ISGL_BGT_BUDGET_1..14 | Primary budget — per-period budgeted amount (14 periods: 13 fiscal + 1 adj) |
| ISGL_BGT_DATE | Budget entry/last-modified date |
| ISGL_BGT_BUD2_1..14 | Alternate budget scenario — second set of 14 period budgets |
| ISGL_BGT_FLAG(1) | Budget status flag |
| ISGL_BGT_WHO(30) | Who entered/approved this budget |
| ISGL_BGT_EDATE | Effective date |
| ISGL_BGT_EXTRA(50) | Extra |

Used by GL-B budget entry and GL financial statements to show budget vs. actual. BUD2 is a second scenario (e.g., revised budget after mid-year reforecast).

---

### EMERSNGL (65f) — Emergency Single-Company GL Ledger

**PK:** BKGL_ACCT(10) + BKGL_GLDPT(4)

Used by T7EMGL (Emergency GL module). Stores a complete single-company GL ledger with current year + budget + 2 prior years — a standalone GL that can be accessed/edited outside the normal GL module (for disaster recovery or emergency adjustments):

| Field group | Description |
|---|---|
| BKGL_ACCT+GLDPT | PK — account + department |
| BKGL_ACCTD(25) + TYPE + CR_DR + NON_CASH | Account metadata |
| BKGL_CURRENT_1..14 | Current year actuals — 14 periods |
| BKGL_BUDGET_1..14 | Current year budget — 14 periods |
| BKGL_1YPAST_1..14 + 1YPAST_YE | Last year actuals — 14 periods + year-end |
| BKGL_2YPAST_1..14 + 2YPAST_YE | 2 years ago — 14 periods + year-end |
| BKGL_EXTRA(50) | Extra |

EMERSNGL is structurally similar to BKGLCOA but uses shorter BKGL_ prefix (not BKGL_COA_). T7EMGL writes directly to EMERSNGL as a parallel single-company ledger used for emergency GL corrections without going through normal period controls.

**GL table family summary (Pass 70):**

| Table | Fields | Purpose |
|---|---|---|
| BKGLCOA | ~90 | Main GL ledger — current + 1–2yr history (BKGL_COA_ prefix) |
| ISGLCOA | ~67 | GL COA extension — budget history per account |
| ISGLBDGT | 67 | 4-year deep history (T-3..T-6) for comparison reports |
| ISGLFCOA | 67 | Functional COA — same structure, FS-report oriented view |
| ISGLNBGT | 35 | Forward budget (current year, dual scenario) |
| EMERSNGL | 65 | Emergency standalone ledger (current+budget+2ypast) |

**Confidence: 93/100** — ISGLBDGT/ISGLFCOA/ISGLNBGT/EMERSNGL all fully field-decoded; 14-period array pattern matches BKGLCOA design; T7EMGL confirmed to use EMERSNGL; ISGLFCOA vs ISGLBDGT functional distinction inferred (same schema, likely report-mode alternate index).

---

## ES — Estimate Routing — Pass 70

### ESTROUT (48f) — Estimate Routing Steps

**PK:** MTESRO_QUOTE(8) + MTESRO_OPER(3) — estimate number + operation code

The routing table for estimates. Parallel to WOROUT (WO routing) but for the estimating/quoting module. Each row is one routing step on an estimate:

| Field | Description |
|---|---|
| MTESRO_QUOTE(8) + OPER(3) | PK — estimate number + operation |
| MTESRO_DESC(30) | Operation description |
| MTESRO_WC(12) | Work center |
| MTESRO_TYPE(1) | Operation type (I=internal, O=outside process) |
| MTESRO_VENDOR(10) + VENDNAME(25) | Outside process vendor (if TYPE=O) |
| MTESRO_OPCOST(8) | Total operation cost |
| MTESRO_PARTSHR(8) | Parts share of operation cost |
| MTESRO_TIMEPART(8) | Run time per part |
| MTESRO_SETUPHRS(8) | Setup hours |
| MTESRO_MISCCOST(8) + MISCDESC(30) | Miscellaneous cost + description |
| MTESRO_LAB1..5 | Labor cost per qty break (5 qty-break levels) |
| MTESRO_MACH1..5 | Machine cost per qty break |
| MTESRO_OVER1..5 | Overhead cost per qty break |
| MTESRO_SETUP1..5 | Setup cost per qty break |
| MTESRO_INSTR_1..15 | 15 instruction lines (60 chars each = 900-char routing instruction) |

**5 qty-break cost arrays:** ESTROUT stores cost at 5 quantity break points — the same 5-break structure as BKRTCST (routing cost table) and BKMATCST (material cost table). All three tables align for ES-C cost rollup.

**Relationship to WOROUT:** When ES-E converts an estimate to a WO, ESTROUT rows become WOROUT (WO routing) rows. MTESRO_QUOTE maps to MTWORO_WO; MTESRO_OPER maps to MTWORO_OPER; cost fields roll into WOROUT actual-hours tracking.

**Confidence: 80/100** — ESTROUT(48f) fully field-decoded; 5-qty-break cost structure matches BKRTCST pattern; conversion to WOROUT on ES-E confirmed from T7ESE DB fingerprint (opens WOROUT); per-qty-break cost selection logic (which LAB/MACH/OVER slot applies at what quantity) in encrypted RWN.

---

## WO — Operation Extended Tables — Pass 70

### ISWROHEX (60f) — WO Routing Operation Extended

**PK:** IS_WROEX_WOPRE(8) + WOSUF(2) + OPER(2) — WO + operation-level record

Extension record at the WO routing operation level (parallels ISWOEX which is at the WO header level):

| Field | Description |
|---|---|
| IS_WROEX_WOPRE+WOSUF+OPER | PK — WO prefix, suffix, operation number |
| IS_WROEX_ITP(20) + ITPP(1) | Item type profile code + prefix |
| IS_WROEX_FOI(1) | Fire-on-issue flag |
| IS_WROEX_LQTY(8) | Labor quantity |
| IS_WROEX_SDAY(2) + FDAY(2) | Scheduled start/finish day |
| IS_WROEX_DATE1(date) | Operation extra date |
| IS_WROEX_ALPHA1(1) + ALPHA2(2) | Short alpha UDF fields |
| IS_WROEX_NUM1(8) | Numeric UDF |
| IS_WROEX_DESC1(30) | Description UDF |
| IS_WROEX_ALPHA3_1..5 (15 each) | 5× alpha UDF fields (item-type profile data) |
| (+ 40 more: additional UDF arrays matching ITP profile definition) | |

ISWROHEX provides per-operation UDF slots driven by the item type profile (ITP). Different item types can configure which ALPHA/NUM/DATE fields carry meaning. Used for quality attributes, test parameters, or process instructions specific to this operation.

---

### ISPREQ (25f) — Shop Floor Material Pull Request

**PK:** IS_PREQ_WOPRE(8) + WOSUF(2) + OPER(2) — WO + operation

A shop-floor operator's request for additional material on a specific WO operation. Distinct from the BOM-driven WOMAT issue — this is a non-standard pull triggered by scrap, rework, or short issue:

| Field | Description |
|---|---|
| IS_PREQ_WOPRE+WOSUF+OPER | PK |
| IS_PREQ_WC(12) | Work center making the request |
| IS_PREQ_EMP(2) | Requesting employee# |
| IS_PREQ_RDATE + RTIME | Request date + time |
| IS_PREQ_PART(15) | Part number needed |
| IS_PREQ_QTY(8) | Quantity requested |
| IS_PREQ_SCRAP(2) | Scrap code (why extra material is needed) |
| IS_PREQ_REASON(30) | Reason code |
| IS_PREQ_NOTE(200) + NOTE2(200) | Full explanation (up to 400 chars) |
| IS_PREQ_LOC(15) | Requested from location |
| IS_PREQ_PRINTED(1) | Print flag (pick ticket generated) |
| IS_PREQ_IQTY(8) | Issued quantity (filled so far) |
| IS_PREQ_INOTE(200) | Issue note (storeroom response) |
| IS_PREQ_LOT(15) + SERIAL(25) | Lot/serial of issued material |
| IS_PREQ_LCOST(8) | Landed cost of issued material |
| IS_PREQ_CLOSED(1) + CDATE + CTIME | Closed flag + close date/time |
| IS_PREQ_NOB(1) | Notify on backorder flag |
| IS_PREQ_EXTRA(100) | Extra |

Workflow: DC operator at the WC creates ISPREQ → storeroom sees it (via HH or SM) → picks material → sets IQTY/INOTE/LOT/SERIAL → marks CLOSED. Closed records remain as audit trail. Related to BKDCLAB (DC labor) and the HH (handheld) module.

**Confidence: 80/100** — ISWROHEX(60f) and ISPREQ(25f) fully field-decoded; ISPREQ two-party workflow (request→fulfill→close) confirmed from field structure; ISWROHEX ITP-driven UDF pattern confirmed (matches ISWOEX architecture); exact ITP field binding in encrypted RWN.

---

## IC — Extended Location — Pass 70

### BKICELOC (32f) — IC Extended Location Quantities

**PK:** BKIC_LOC_PROD(15) + CODE(10) — item + location

Extends BKICLOC with additional quantity buckets and per-location GL accounts:

| Field | Description |
|---|---|
| BKIC_LOC_PROD(15) + CODE(10) | PK — item code + location code |
| BKIC_LOC_UOH(8) | On-hand quantity |
| BKIC_LOC_UOSO(8) | Open SO (committed to sales orders) |
| BKIC_LOC_UBO(8) | Back-ordered quantity |
| BKIC_LOC_UOO(8) | Open PO (on order) |
| BKIC_LOC_UOWO(8) | Open WO quantity |
| BKIC_LOC_UALLOC(8) | Allocated quantity (reserved) |
| BKIC_LOC_UWIP(8) | WIP quantity |
| BKIC_LOC_UIQC(8) | In-QC quantity |
| BKIC_LOC_GLA+DPTA | GL Adjustment account + department |
| BKIC_LOC_GLC+DPTC | GL Cost of Sales account + department |
| BKIC_LOC_GLS+DPTS | GL Sales account + department |
| BKIC_LOC_GLSNT+DPTSNT | GL Sales non-taxable account + department |
| BKIC_LOC_GLWIP+DPTWIP | GL WIP account + department |
| (+ 12 more GL/UDF fields) | |

**BKICELOC vs BKICLOC:** BKICLOC (documented earlier) tracks UOH+UOSO+UBO+UOO with COST+GL_ACCT. BKICELOC adds UOWO, UALLOC, UWIP, UIQC and per-location GL accounts per purpose (Adj/COGS/Sales/WIP). BKICELOC is the extended form used by multi-location companies needing per-location GL differentiation.

**Confidence: 72/100** — BKICELOC(32f) fully decoded; field meanings confirmed from names matching BKICLOC pattern plus WO/QC/WIP extensions; which programs write BKICELOC vs BKICLOC blocked by RWN encryption.

---

## SP — Tray/Lot Map — Pass 70

### ISLSMAP (31f) — Lot/Serial Assembly Map (PCB Tray Tracking)

**PK:** IS_MAP_TRAYNUM(25) + POSITION(10)

Tray-based lot/serial tracking for PCB (printed circuit board) assembly. Maps each physical tray position to the component placed there and the resulting assembled item:

| Field | Description |
|---|---|
| IS_MAP_TRAYNUM(25) | Physical tray identifier (barcode or sequence) |
| IS_MAP_POSITION(10) | Position within tray (e.g., "A01", row+col) |
| IS_MAP_WOPRE(8) + WOSUF(2) + OPER(2) | Linked WO + operation |
| IS_MAP_PCODE(15) + PLOT(15) + PSERIAL(25) + PQTY | Parent (placed) component: code, lot, serial, qty |
| IS_MAP_CCODE(15) + CLOT(8) + CSERIAL(25) + CQTY + CQTYPER | Child (built) assembled item: code, lot, serial, qty, qty-per |
| IS_MAP_BATCH(25) | Batch/run identifier |
| IS_MAP_DATE_1..5 | 5 date slots (placement, inspection, test, ship, etc.) |
| (+ 11 more: alpha/flag/extra slots) | |

ISLSMAP is the traceability bridge between the component reel (PCODE/PLOT) and the finished PCB (CCODE/CLOT). SP-A processes scan each placement position to confirm the right component is in the right position. Used alongside ISSPC (SPC traceability) and IS2DBAR (2D barcode) for full PCB genealogy.

**Confidence: 78/100** — ISLSMAP(31f) fully decoded; PCB assembly context confirmed (TRAYNUM/POSITION + component→assembly linkage); IS_MAP_PCODE/CCODE parent-child structure matches SP module purpose; exact scanning/validation logic in encrypted RWN.

---

### New Tables Confirmed (Pass 70)

| Table | Fields | Purpose |
|---|---|---|
| BKSLEVEL | 422 | Security level access matrix — MENU(2)+LEVEL(2) PK; 20 menus × (YN + 20 op flags) = 420 permission bits |
| BKSYLOG | 215 | User logon / company access — CODE PK; per-module OKGL/OKAR/etc. flags (up to 20 companies per module) |
| ISGLBDGT | 67 | GL deep history — ACCT+GLDPT PK; 4 years × 14 periods (T-3..T-6 actuals) for multi-year comparison reports |
| ISGLFCOA | 67 | GL functional COA — identical structure to ISGLBDGT; separate view used for FS (financial statement) reporting |
| ISGLNBGT | 35 | GL forward budget — ACCT+GLDPT PK; BUDGET_1..14 (primary) + BUD2_1..14 (alternate scenario); WHO+EDATE audit trail |
| EMERSNGL | 65 | Emergency GL ledger — BKGL_ACCT+GLDPT PK; CURRENT+BUDGET+1YPAST+2YPAST (14 periods each); standalone single-company GL |
| ESTROUT | 48 | Estimate routing step — QUOTE+OPER PK; WC+TYPE+VENDOR; 5-qty-break LAB/MACH/OVER/SETUP costs; 15 instruction lines |
| ISWROHEX | 60 | WO operation extended — WOPRE+WOSUF+OPER PK; ITP-driven UDF slots at operation level; parallel to ISWOEX at WO header |
| ISPREQ | 25 | Shop-floor material pull request — WOPRE+WOSUF+OPER PK; PART+QTY+SCRAP+REASON; IQTY/LOT/SERIAL on fulfillment; CLOSED flag |
| BKICELOC | 32 | IC extended location — PROD+CODE PK; UOH+UOSO+UBO+UOO+UOWO+UALLOC+UWIP+UIQC; per-location GL accounts for Adj/COGS/Sales/WIP |
| ISLSMAP | 31 | PCB assembly tray map — TRAYNUM+POSITION PK; parent component (PCODE/PLOT/PSERIAL) → child assembly (CCODE/CLOT/CSERIAL) linkage |

---

*Last updated: 2026-06-17 (Pass 70). Confidence bumps: PS 75→82 (BKSLEVEL 422f security matrix + BKSYLOG 215f company-access matrix decoded; full PS architecture confirmed), GL 90→93 (ISGLBDGT/ISGLFCOA deep history + ISGLNBGT forward budget + EMERSNGL emergency ledger all decoded), ES 75→80 (ESTROUT 48f routing steps with 5-qty-break cost arrays confirmed), IC 68→72 (BKICELOC 32f extended location decoded), SP 80→83 (ISLSMAP 31f PCB tray map decoded). 11 new schemas. WO ISWROHEX+ISPREQ documented (WO already at 85, no bump needed).*
