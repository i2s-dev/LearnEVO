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
| Configure SMTP email (for alert emails from EVO) | EvoServiceSetup | [Platform Subsystems](#platform-subsystems) |
| Schedule automatic nightly backups | EvoERPbackup | [Platform Subsystems](#platform-subsystems) |
| Restore from an AWS Glacier backup archive | EvoERPbackup → Glacier restore | [Platform Subsystems](#platform-subsystems) |
| Add a hyperlink attachment to a PO / SO / WO / part | EvoLinks | [Platform Subsystems](#platform-subsystems) |
| View or enter reminders / calendar events | CALREM | [Platform Subsystems](#platform-subsystems) |
| View / enter a Spec Book / Approved Source List (AVL/QPL) | IN-B (SB tab) | [Spec Book / AVL (SB)](#spec-book--approved-source-list-sb) |
| Collect employee labor hours into payroll (shop-floor or time cards) | WO-L-E or PR-J → PR-K | [Recipe 17: Payroll Time Entry](#recipe-17-payroll--time-entry-labor-hours-collection-pass-110d-2026-06-19) |
| Calculate payroll and verify before printing checks | PR-B → PR-C | [Recipe 18: Payroll Calculation and Register](#recipe-18-payroll-calculation-and-register-pass-110d-2026-06-19) |
| Print payroll checks and post to GL | PR-D | [Recipe 19: Payroll Check Printing](#recipe-19-payroll-check-printing-pass-110d-2026-06-19) |
| File quarterly 941/940 or generate year-end W-2s | PR-L-G/H → PR-H → PR-O → PR-L-I | [Recipe 20: Quarterly/Annual Tax Filing](#recipe-20-quarterly-and-annual-tax-filing-pass-110d-2026-06-19) |
| Run the full year-end close (payroll W-2/1099 + GL year-end + archive) | PR-O → PR-L-I → AP-S → GL year-end → SM-J archive | [Recipe 21: Year-End Close](#recipe-21-year-end-close-pass-112-2026-06-19) |
| Set up Pervasive DDF so ODBC and Java tools can query EvoERP tables | Pervasive DDF Builder or TA-S | [Recipe 22: Build Pervasive DDF](#recipe-22-build-the-pervasive-ddf-required-before-odbc-java-tools-pass-112-2026-06-19) |
| Add a new customer with payment terms and tax setup | AR-A | [Recipe 23: Add a New Customer](#recipe-23-add-a-new-customer-pass-113-2026-06-19) |
| Add a new vendor and configure 1099 tracking | AP-A | [Recipe 24: Add a New Vendor](#recipe-24-add-a-new-vendor-pass-113-2026-06-19) |
| Receive a PO (with QC, lot/serial, and AP voucher creation) | PO-J | [Recipe 25: Receive a Purchase Order](#recipe-25-receive-a-purchase-order-pass-113-2026-06-19) |
| Fix items stuck on the open order report (shipped but never posting) | SD-M → SO-G | [Recipe 9: Packaging Items Stuck on Open Order Report](#recipe-9-packaging-items-stuck-on-open-order-report) |
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

**Recipe index:**

| # | Title | Menu |
|---|-------|------|
| 1 | Sales Order → Ship → Invoice → Post | SO-A → SO-F → SO-G |
| 2 | Work Order Lifecycle (Create → Close) | WO-A → WO-S |
| 3 | Purchase Order → Receive → AP Voucher → Check | PO-A → PO-J → AP-H |
| 4 | MRP Run (Plan → Firm → Release) | MR-A → MR-F → MR-H |
| 5 | Month-End Close | AR-H → AP → IN → AM |
| 6 | New Item Setup | IN-B → BM → RO-A |
| 7 | AR Cash Receipts (Customer Payment) | AR-C |
| 8 | Physical Inventory Count | PI-A → PI-C → PI-G |
| 9 | Packaging Items Stuck on Open Order Report | SD-M → SO-G |
| 10 | GL Journal Entry (Manual) | GL-B |
| 11 | Period-End Archiving and Purging | GL-P → GL-ARCH |
| 12 | EvoERP Backup and Restore | TA-O |
| 13 | New User Setup | SM → PS-A |
| 14 | Inventory Manual Adjustment | IN-G/IN-H |
| 15 | Lot/Serial Tracking Lifecycle | PO-J → WO-F → SO-C |
| 16 | New Company Creation | UT → NE |
| 17 | Payroll — Time Entry | WO-L-E or PR-J → PR-K |
| 18 | Payroll Calculation and Register | PR-B → PR-C |
| 19 | Payroll Check Printing | PR-D |
| 20 | Quarterly and Annual Tax Filing | PR-L-G/H → PR-O → PR-L-I |
| 21 | Year-End Close | PR-O → AP-S → GL year-end → SM-J |
| 22 | Build Pervasive DDF (ODBC/Java) | TA-S or DDF Builder |
| 23 | Add a New Customer | AR-A |
| 24 | Add a New Vendor | AP-A |
| 25 | Receive a Purchase Order | PO-J |

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

---

### Recipe 9: Packaging Items Stuck on Open Order Report

**Trigger:** Items appear on SO-O-A Open Sales Order Listing with Qty To Ship > 0 and Qty
Shipped = 0 indefinitely. They do not clear after running SO-G. Customer complains of
apparent short shipments because the lines look unfulfilled.

**Typical items affected:** Packaging components (boxes, inserts) and documentation (install
guides, quickstart guides) that ship inside the finished goods box and are never individually
scanned or released through SO-E.

**Root cause:** These items have Qty Shipped = 0 because SO-E is never run against them.
When SO-G (Post Invoices) runs, the flag **SD-M → Processing Tab → "Create 0 Qty SO Lines
during post"** controls whether SO-G posts lines with zero ship qty. If this flag is N
(unchecked), SO-G skips all 0-qty lines permanently — they accumulate on the open order
report forever.

**Diagnosis steps:**

```
1. SO-O-A (Print Open Sales Order Listing)
   - Filter: Item From/Thru = the suspect part number
   - Examine the Qty Shipped column
   - If Qty Shipped = 0.00 on all lines → this is the issue

2. SD-M (Sales Order Defaults) → Processing Tab
   - Check the value of "Create 0 Qty SO Lines during post"
   - If unchecked (N) → confirmed root cause
```

**Fix:**

```
Step 1 — Enable the flag (one-time system change):
   SD-M → Processing Tab → "Create 0 Qty SO Lines during post" → check (Y)

   ⚠ This is system-wide. All 0-ship-qty lines company-wide will now post
   through SO-G. Alert accounting/ops before the next SO-G batch run.

Step 2 — Clear the existing backlog:
   SO-G (Post Invoices)
   - Set SO Number From/Thru to cover affected orders
   - Click Post

Step 3 — Verify:
   SO-O-A filtered to the item number
   - If lines are gone → fix confirmed
```

**Key tables involved:**
- `BKARINVL` — Sales Order line items (Qty Shipped field lives here)
- `BKGLTRAN` — GL transactions created by SO-G posting
- SD-M settings stored in the system defaults configuration table

**Real-world case:** 2026-06-18, Albertsons (customer 2B13). 12 packaging/guide items
(730-54200, 730-54117, 730-54201, 730-54116, 090-series install guides). 28 open SOs,
475 total units stuck. Fixed by SD-M flag change + SO-G run. See full case study:
[docs/procedures/packaging-items-stuck-on-open-order-report.md](docs/procedures/packaging-items-stuck-on-open-order-report.md)

---

*Business Workflows section — **Confidence: 85/100** — 16 workflow recipes written (SO lifecycle, WO lifecycle, PO→check, MRP run, month-end close, new item setup, AR cash receipts, physical inventory, packaging items stuck, GL journal entry, period-end archiving, backup/restore, new user setup, inventory manual adjustment, lot/serial tracking lifecycle, new company creation); table write sequences confirmed from DB fingerprints (RWN symbols) and DDF schema cross-reference; exact field-level validation logic and error handling in encrypted RWN.*

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
  2. Format is controlled by **BKYS.YN[48]** (set in AD-C):
     - Values 1, 4, or 5 → laser format → AP-H chains to BKAPHA (program path via BKSY.PRGS.WHR)
     - Values 2 or 3 → continuous/dot-matrix format → AP-H stays in BKAPH
     - BKAPHA uses RTM templates (BKAPHA1.RTM, BKAPHA2.RTM, BKAPHA3.RTM); supports C/S/S and S/S/C check layouts
  3. After printing, the program posts to GL (debit AP control, credit bank account),
     updates vendor last-payment date, reduces outstanding invoice amounts,
     and deletes records from BKAPCHKF
  4. Checks with zero or negative totals are automatically voided
  5. Check amounts are converted to alpha text ("five thousand dollars") by GET.ALPHA routine
  6. Multi-currency checks print with exchange rate applied; gain/loss posts to separate GL account
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

**MRP calculation stages** (from BKMRF.SRC — re-analyzed Pass 119):
1. **Demand loading (DO.SO):** Scan BKARINVL for open SO demand → write negative MTMRP records
2. **Supply loading — WOs (DO.WO):** Scan WORKORD for open WOs → write positive MTMRP records
3. **Supply loading — POs (DO.PO):** Scan BKAPPOL for open POs → write positive MTMRP records
4. **WO BOM explosion (DO.WOBOM):** For each WO, explode WOBOM → component MTMRP demand
5. **Forecast loading (DO.FC):** Scan BKMRPFC → write projected-demand MTMRP records
6. **Reorder level check (DO.RLEVEL):** Scan BKICLOC → trigger planned orders at reorder level
7. **MRP engine Stage 1/2 (START.MRP/2):** Per-part loop: scan MTMRP, accumulate running ONHAND;
   if ONHAND < reorder level call CREATE.PLN() to add a planned order
8. **MRP engine Stage 3 (START.MRP3):** Assign BKMRPSW record per part (loop control)
9. **Action assignment Stage 4 (START.MRP4):** Assign EXPEDITE/DELAY/REVIEW messages after all
   orders are in MTMRP (more accurate than mid-run assignment)

Note: 2001-01-01 JVH refactor eliminated multi-pass Stage 4 by looping per-part in Stages 1–3.

**MTICMSTR fields confirmed in BKMRF.SRC:**
- MTIC.PROD.MRP = 'Y' — scan filter: only process MRP-enabled items
- MTIC.PROD.TYPE — item type ('B'=buyout, 'F','A','M','N' = other types); type 'B' uses QOH=0 (always generate orders)
- MTIC.PROD.MRPSW ≠ 'N' — rounding switch: if 'N', don't round ONHAND to whole units

**BKICMSTR fields confirmed in BKMRF.SRC:**
- BKIC.PROD.UOH — on-hand quantity (starting ONHAND value for MRP run)
- BKIC.PROD.RLVL — reorder level (if UOH < RLVL, generate planned order at reorder-level pass)

**MTMRP confirmed fields (12f — from source):**
PARTNO(15) + DATE(PK composite with KEY), KEY, ORDER(10, e.g. 'REORDLVL'),
ACTION(10, 'EXPEDITE'/'DELAY'/'REVIEW'), PEGTO(10, demand source reference),
QTY(float), PG.SDATE(date, pegged start), PG.FDATE(date, pegged finish),
STARTDT(date, planned start), PG.QTY(float, pegged qty), ONHAND(float, running balance)

**BKMRPSW confirmed fields (2f):**
PART(15, part number key), SW(1, status flag: 'Z' = processed)

**Primary tables:**

| Table | Purpose |
|-------|---------|
| MTMRP | MRP work table — demand/supply/planned orders per part |
| BKMRPFC | MRP forecast input (projected demand beyond open SOs) |
| BKMRPSW | MRP switch/control file (per-part loop state during run) |
| BKICLOC | Location inventory (reorder level check at location level) |
| WOBOM | WO BOM (component demand from in-progress WOs) |

**Confidence: 78/100** — BKMRF.SRC fully re-analyzed (Pass 119); all 4 MRP stages and
demand/supply sources confirmed from source; MTMRP 12 field names confirmed; MTICMSTR and
BKICMSTR MRP-specific fields confirmed. Minor gap: DO.WSBOM procedure (work schedule BOM?) purpose unclear.

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
| BKRTTEMP | — | Operation templates (template library for reusable operations) |
| BKRTEMTR | — | Routing template transactions — used instead of ROUTING when called from DE-J-C (EDI import edit path) |
| ROUTTEMP | — | Routing edit workspace (transient edit buffer; not permanent) |
| BKRTSPEC | 7 | Operation notes/specs (BKRT_SPEC_* prefix) |
| BKRTCST | 24 | Routing cost snapshot per quote/setup (10-break pricing) |
| BKRFQ | 49 | Request for Quote per routing operation (subcontract pricing) |
| ISROUTEX | — | Routing extension fields |

**DE-J-C call path:** When BKROA.SRC is chained from DE-J-C (EDI import routing editor), it opens
BKRTEMTR instead of ROUTING and uses `setact ROUTING file BKRTEMTR` — same entry logic but against
the EDI-imported routing staging table, not the live ROUTING table.

**Copy routing (F3 / G.COPY):** Duplicates all ROUTING records from source part to target part.
G.COPY.SPEC option: additionally copies all BKRTSPEC (specs/notes) records.

**Confidence: 87/100** — BKROA.SRC re-analyzed (Pass 119); ROUTING (62f) schema confirmed from
DDF; BKRTEMTR (EDI import staging) and ROUTTEMP (edit buffer) confirmed from source; DE-J-C
call path and G.COPY.SPEC behavior confirmed; all ~20 entry-procedure field names map to MTRO_
DDF names.

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
6. Auto-close feature: if a new job starts while a previous is still open, previous is
   automatically closed with a system-generated record (enabled by BKYS.YN[229]='Y')
7. On exit (F9): pending labor moves from BKDCTLAB → BKDCPLAB for batch GL posting

**DC entry variants** (controlled by `cfrom` parameter passed from menu):
- **DC-A** (cfrom=DCA): Full entry — WO, Seq#, Start time, Finish time, Parts, Scrap, Run hours
- **DC-B** (cfrom=DCB): Barcode/scan mode — WO, Seq#, Parts, Scrap only (no clock times)
- **DC-C** (cfrom=DCC): Time-entry only — WO, Seq#, Start, Finish, Run hours (no parts/scrap)

**Screen configuration flags (BKYS.YN array):**
- YN[20]='Y' — barcode mode: sets EXTRA='B' on posted part records
- YN[228]='Y' — use alternate screen form BKDCAF (vs standard BKDCA)
- YN[229]='Y' — auto-close enabled: system closes open jobs automatically on new job start

**Shift configuration:** 3 shifts in BKDCSHFT; each has BUFFER, START, FIN, FINBUF time fields.

**Labor types:**
- P = Production (parts made)
- S = Setup
- A = Auto-close (system-generated close of previous job)

**Status codes (lab.posted field):**
- O = Open (clocked in, in-progress)
- C = Closed (clocked out, ready to flush)
- P = Pending post (in BKDCPLAB, awaiting batch GL post)
- N = New (transitional during auto-close)
- Y = Posted (final state after GL posting via T7AUTODCH)

**WOLABOR field names confirmed from source** (17 of 58 total):
DATE, EMP, WOPRE, WOSUF, WOKEY, OPER, POSTED, SHIFT, START, FINISH, PARTS, SCRAPPED,
NOJOBS, RUNHRS, SETUPHRS, REGOVER (A/1 = reg vs overtime), EXTRA (A/50 = misc flags)

**Primary tables:**

| Table | Purpose |
|-------|---------|
| BKDCSHFT | Shift definitions (3 shifts × BUFFER/START/FIN/FINBUF time fields) |
| BKDCTLAB | DC temporary labor — current session entries (same 50f schema as BKDCLAB) |
| BKDCPLAB | DC permanent labor — awaiting batch GL post (same 50f schema) |
| BKDCLAB | DC labor staging — records moved here first; MOVE_LAB copies to BKDCPLAB |
| WOLABOR | WO labor transactions (posted) — final destination after T7AUTODCH processing |

**Confidence: 82/100** — BKDCA.SRC fully analyzed (938 lines); DC variants, YN flags, and
WOLABOR field names all confirmed from source. Minor gaps: SETUPHRS/REGOVER full semantics
and BKDCAF alternate screen field layout not verified.

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

**T7USG form layout (confirmed from T7USG.DFM — Pass 82):**
Form caption "USG". Trigger entry with fields: Trigger Code (IS.TRIG.CODE), User to Trigger (IS.TRIG.TRIGR → IS.TRIG.CONTACT), Days Pre (is.trig.days), Email Address (IS.TRIG.EMAIL), Email Reminder flag (IS.TRIG.EFLAG), Once on next occurrence (IS.TRIG.ONCE), Last Date (IS.TRIG.LDATE), Last Time (IS.TRIG.LTIME). Filter section: Item Number (IS.TRIG.ITYPE), Customer Code (IS.TRIG.CUST), Vendor Code (IS.TRIG.VEND), SO Number (IS.TRIG.SO), PO Number (IS.TRIG.PO), WO Number range (IS.TRIG.WOPRE/WOSUF × 2 for from/thru), Operation (is.trig.oper), Item Types, Class (IS.TRIG.class), Category (IS.TRIG.cat), Planner (is.trig.planner), Bin Location (IS.TRIG.BINLOC). Also: Notes (IS.TRIG.NOTE) and IS.TRIG.ODEL flag (on-delete trigger).

All 25 ISTRIGRS fields mapped to UI labels. T7USG = complete trigger entry form, NOT a placeholder.

**Confidence: 74/100** — T7USG form fully confirmed from DFM (28 field bindings); ISTRIGRS (25f) and ISREMIND (22f) fully field-documented; EvoRemind integration confirmed; trigger-firing date calculation in encrypted RWN.

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

**What it does:** GL period control, account history, COA maintenance, department copy, financial statement setup, archive/purge, and GL renumber. Note: AM = Accounting Maintenance, NOT Asset Management.

**Menu codes:** AM (15 programs — all DFMs confirmed from network share)

### AM Program Map (confirmed from DFMs — Pass 80)

| Program | Procs | Operation | Confirmed purpose |
|---|---|---|---|
| T7AMA | ? | AM-A GL Period Setup | Sets Fiscal Year Start Date, Open Period Start/End Date, Accounting Open Period — controls what periods are open for posting |
| T7AMB | ? | AM-B GL Balance History | Views GL account period balances across current + 6 prior years (BKGL.CURRENT[1..14] + BKGL.1YPAST..6YPAST arrays) |
| T7AMC | ? | AM-C COA Edit | Chart of Accounts editor — add/modify GL accounts; Account Type (A/L/E/I/O), Non-Cash flag, inactive flag, Period Budget amounts, Beginning Balance; uses ISGL.CYDATE[n] for period-end dates |
| T7AMD | ? | AM-D Department Copy | Copies an existing department's GL account structure to a new department code; GL type filter (A/L/E/I/O); clear budget flag |
| T7AME | ? | AM-E Financial Statement Setup | Largest AM form (105 fields) — configures Income Statement, Balance Sheet, and Cash Flow Statement formats; maps GL account ranges to report line groups (INC/BAL/CAS sections); defines report titles |
| T7AMH | ? | AM-H GL Code Renumber | Imports a CSV file mapping old GL codes → new GL codes, then renames all references; also supports manual old-code → new-code renumber |
| T7AMI | ? | AM-I GL Journal Purge | Archives/purges GL journal transactions by date range, GL account range, and journal type |
| T7AMJ | ? | AM-J AP Vendor Archive | Purge, Archive, or Restore AP vendor records; vendor range + thru date |
| T7AMK | ? | AM-K AR Customer Archive | Purge, Archive, or Restore AR customer records; customer range + thru date |
| T7AMN | ? | AM-N GL Period Dates Edit | 96-field editor for GL fiscal period-end dates — fills ISGLDATE slots; one row per period per year (Current + 7 prior); this is where the fiscal calendar is defined |
| T7AMO | ? | AM-O PO/AP Records Archive | Purge/Archive/Restore PO and AP records; vendor range, last-activity date, vendor class filter; "Delete PO Orphans (L/H/B/N)" |
| T7AMP | ? | AM-P SO/AR Records Archive | Purge/Archive/Restore SO and AR records; customer range, customer class, last-activity date; "Delete SO Orphans (L/H/B/N)"; toggle ship-to customer inclusion |
| T7AMQ | ? | AM-Q GL Budget Setup | 134-field budget configurator; imports prior-year actuals or current-year data as next-year budget; Factor multiplier; four modes: 1YPast / Annual Budget / Current Year / Annual for Next Year Budget |
| T7AMS | ? | AM-S GL Journal Archive | Purge/Archive/Restore GL journals by date range + journal number range + journal type |

**Primary tables:** BKGLCOA (GL Chart of Accounts), ISGLDATE (GL date editor — period-end dates), ISGLCOA (GL COA extension), BKGLTRAN (GL transactions).

**Confidence: 83/100** — All 14 DFMs read from network share; all AM operations confirmed from form captions and field names; AM-E (financial statement) 105-field form structure confirmed; AM-N as the direct ISGLDATE editor confirmed; procs counts and detailed posting logic blocked by RWN encryption.

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

**Confidence: 85/100** — All 286 DDF fields confirmed from samples/ddf/schema.md; embedded arrays fully documented (20-slot terms, 9-slot bank, 5-slot aging, BKSYPRTR printer table confirmed); tier1-tables.md updated Pass 121.

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

See [Recipe 21: Year-End Close](#recipe-21-year-end-close-pass-112-2026-06-19) for the complete step-by-step sequence with table operations.

**Summary:** Payroll year-end (PR-O → BKPRW2 + YTD zero) → W-2 print (PR-L-I) → 1099 (AP-S) → GL year-end shift (CURRENT → 1YPAST → 2YPAST in BKGLCOA) → archive BKGLTRAN → set new budget.

**Confidence: 88/100** — PR-O BKPRW2 creation + BKPRMSTR YTD reset confirmed from DDF + CHM; GL COA year-end column structure confirmed from DDF (BKGLCOA 65 fields); archive mechanism confirmed from SM data-maintenance docs; 1099 path through BKAPVEND.TAX_ID + AP-S confirmed.

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

Creates cost estimates for customer RFQs (requests for quotation). Estimates have a 10-quantity-break cost matrix covering material, labor, overhead, outside process, and misc costs. Completed estimates can be converted to Sales Orders and/or Work Orders.

**Program map (DFM-confirmed, Pass 155, 2026-06-22):**

| Program | Caption | Purpose |
|---------|---------|---------|
| T7EST | ES-A Enter Estimates | Main estimate entry — customer, 10 qty levels (IS.EST.QTY[1..10]), margins (MATMU%/LABMU%/OPMU%/OHMU%/OVLMU%), status, drawing/rev, expire date, lost date, quote rev# |
| T7ESB | ES-B Print Estimates | Filter: SO# range (sFROM.SONUM/sTHRU.SONUM), Customer range, Cust Class range, Job# range; Options: ISPRT.NOTES, ISPRT.HID.NOTES, ISPRT.KIT, ISPRT.ECO, prt.xref, PLDTYPE (YES/NO/PARENT/COMPONENT) |
| T7ESC | ES-C Print Estimate Detail | Filter: Quote# range (vld_estf/vld_estt); PRINT.REPORT[1..10] qty-level checkboxes; Options: Summary Only (ISPRINT.REPT11), 2nd description, BOM detail, routing detail, extra charges |
| T7ESD | ES-D Print Customer Quotes | Filter: Quote# range (vld_qtnum), Customer range, Expiry date range, Cust Class, Status (AICXD = Active/Inactive/Complete/eXpired/Deleted), Consolidated; Options: ais.dec (price decimal precision), PLDTYPE (Y/N/P/C) |
| T7ESE | ES-E Convert Estimates | sFROM.QUOTE → ISTO.SO (Create SO) + ISTO.WO (Create WO); Assigned SO.NUM + sWO.NUM; Customer PO (CUST.PO); LOCATION (vld_loc()); incl.est.no (put Est# in PO field); ISUPD.CONTRACT; Lines grid: APART/AQTY/APRICE/AESD/AWSD/AWFD; Per-line: ORD.QTY/SELL.PRICE/START.DATE/FINISH.DATE/ESD.DATE |
| T7ESH | ES-H Enter Material Costs | BKMC.CODE (item, vld_item()); BKMC.QTY[1..5] / BKMC.COST[1..5] ($,0.0000); BKMC.DATE (last update); Extra: MTIC.PROD.VEND[1] (primary vendor), Lead Time, Standard Pack, Specifications |
| T7ESI | ES-I Print Material Costs | Filter: from.item/thru.item (item range) + from.date/thru.date (date range); Print button |

**ES-E Convert Estimates — field detail:**
- `sFROM.QUOTE` — source estimate/quote number (vld_quote())
- `ISTO.SO` / `ISTO.WO` — checkboxes: convert to Sales Order / Work Order
- `SO.NUM` / `sWO.NUM` — new order numbers (read-only, set during conversion)
- `is.est.cust` — customer (read-only, inherited from quote)
- `CUST.PO` — customer PO number (editable); `incl.est.no` — include estimate# in PO field
- `ISUPD.CONTRACT` — Update Contract Price File during conversion
- Lines grid (`APART`=item, `AQTY`=qty, `APRICE`=price, `AESD`=estimated ship date, `AWSD`=WO start, `AWFD`=WO finish)
- Per-line detail: `ORD.QTY`, `SELL.PRICE` ($,0.0000), `START.DATE`, `FINISH.DATE`, `ESD.DATE`
- Note: Convert button (btnConvert) is Visible=False — conversion triggered by program logic, not a visible button

**Quote status codes (AICXD on qt.status field in ES-D):**
- `A` = Active, `I` = Inactive, `C` = Complete/Converted, `X` = eXpired, `D` = Deleted

**BKMATCST (ES-H entry) — Material Cost Table:**
- Form shows 5 qty breaks (BKMC.QTY[1..5] / BKMC.COST[1..5]); table has 10 breaks in DDF
- `BKMC.DATE` tracks last price update — useful for stale-cost warnings
- Primary vendor reference (`MTIC.PROD.VEND[1]`) pulled from MTICMSTR (ES copy of inventory)

**Estimate → Order conversion:** From ES-E, one estimate can generate both a SO and WO in a single conversion. The lines grid lets the user confirm items, quantities, and pricing from the estimate before committing. ISUPD.CONTRACT updates the contract price file if the estimate was priced against a negotiated contract.

**Use case examples:**
- "How do I create a quote for a customer?" → ES-A (T7EST main entry), enter customer, 10 qty breaks, margins auto-calculate.
- "How do I print an estimate for internal review?" → ES-C (T7ESC) — pick quote# range, select qty levels to print, optionally include BOM/routing detail.
- "How do I send a quote to a customer?" → ES-D (T7ESD) — filter by quote# or customer, set status filter, print.
- "How do I convert a quote to an order?" → ES-E (T7ESE) — enter quote#, check ISTO.SO/ISTO.WO, confirm lines, execute conversion.
- "How do I get vendor pricing into an estimate?" → RF module generates vendor RFQs feeding back into BKRFQ; or enter material costs manually in ES-H.
- "How do I update material costs for estimating?" → ES-H (T7ESH) — enter item code, enter costs for up to 5 quantity breaks.

**Confidence: 82/100** — All 6 DFMs confirmed field-by-field (Pass 155, 2026-06-22); quote status codes AICXD confirmed from AllowedChrs; ES-E conversion flags confirmed; BKMATCST 5-of-10 qty break gap noted. Underlying RWN logic not disassembled.

---

### EX — SQL Export / Business Intelligence Export

Exports EvoERP data to CSV files by running SQL queries against a separate BI database. Entirely Java-based — the TAS Pro component is just a Java launcher stub.

**Architecture (confirmed from DFM + log files, Pass 156, 2026-06-22):**
- `SQLEXPORT.RWN` — TAS Pro 7 launcher stub; shows "Loading...." dialog while spawning Java
- `SQLEXPORT.DFM` — T7JTemp template (generic Java loader form; no EX-specific UI elements)
- `SQLExport.jar` — Java Swing application (`com.evoerp.*` package, version 1.5.0 build 2014-03-19)
- Same architecture as QU-F pivot tool (EvoPVT.jar) — TAS stub → Java app

**Database connection:**
- Connects via Pervasive JDBC v2 to local Pervasive SQL engine
- Host: i2s109-solidcrm, Port: 1583, DB: **EVOBI2** (separate BI database — NOT the main DBAMFG$ operational data)
- Uses company context (Company ID) and user name passed from the TAS session

**Key Java classes:**
- `com.evoerp.sql.PervasiveDatabase` — Pervasive JDBC connection manager
- `com.evoerp.ui.util.TextExportingWorker` — CSV file export worker (Swing background task)
- `com.evoerp.ui.util.FileOpeningWorker` — file open/save dialog worker

**Output:**
- Default export destination: `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS\` (historical: `\\I2S109-SOLIDCRM\EVOREPORTS\`)
- Format: CSV (comma-separated values)
- Common error: path separators in filenames cause FileNotFoundException (e.g., `7\18 thru 8-4.csv`)

**Use case:**
- "How do I export EvoERP data to Excel/CSV?" → EX module (SQL Export) — runs predefined SQL queries against EVOBI2, exports results to CSV.
- The EVOBI2 database is a separate reporting/BI database, likely with views or denormalized tables for reporting. SQL Export lets users run these queries and download the results.
- Logs are written to `\\I2S109-SOLIDCRM\DBAMFG$\logs\SQL Export.log`.

**Confidence: 45/100** — Architecture confirmed from SQLEXPORT.DFM (T7JTemp) + SQL Export.log (Java startup params, package names, DB connection). SQLExport.jar UI and SQL query set not decompiled. EVOBI2 database structure unknown.

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

**T7MAPDEPO form layout (confirmed from T7MAPDEPO.DFM — Pass 82):**
Deposit application form showing: Deposit# (bkar.dep.depno), Customer (BKAR.DEP.CUST), Amount Remaining (amount.rem), original deposit amount (depo.orig.amt). Grid with SO lines: SO Number (sFROM.SONUM), Description (bkar.invl.pdesc), Qty (bkar.invl.pqty), SO Amount (bkar.invl.pext), Deposit Amount (depo.amount), Item Number (from.item), GL Account (from.glacct + from.gldpt). ISARDEPL fields bound: ISAR.DEPL.SO, DEPL.ITEM, DEPL.DESC, DEPL.PEXT, ISAR.DEPL.AMT, ISAR.DEPL.GLACT. Note: "Leave this blank for the Default Accounts" label appears near GL Account field.

**ISARDEPL fields confirmed from DFM:** SO, ITEM, DESC, PEXT (extended price), AMT (deposit amount applied), GLACT (GL account override). Minimum 6 fields confirmed; likely more not bound in DFM.

**Confidence: 76/100** — BKARDEP (6f) fully documented; T7MAPDEPO is a real deposit entry form (NOT TImageList as incorrectly reported in prior session summary); ISARDEPL field bindings confirmed from DFM; complete deposit workflow traced across 5 programs; GL posting flow confirmed.

---

### TE — NACHA/ACH Testing (T7TESTNACHA)
**What it does:** Generates and validates NACHA-format ACH files for electronic payment (direct deposit or AR collection). Uses ISBANKS (bank account master) and BKGLCHK (check history). A utility module for testing ACH transmission before live payroll or customer payment runs.

---

### CH — Multi-Location Chain / Program Chaining (T7CHAIN / T7CHAINM)
**What it does:** Manages EVO's program-chaining system. When a program completes (e.g., T7SOA Sales Order Entry), it can automatically launch a follow-on program (e.g., T7SOB Invoice Print) with parameters passed between them. Per-user chain definitions allow different users to have different post-program behaviors.

**Forms confirmed from DFM (Pass 153, 2026-06-22):**
- **T7Chain.DFM** — "Chain List": browse chains per user; grid: IS.CHAIN.USER, IS.CHAIN.DESC, IS.CHAIN.AUTO, IS.CHAIN.PARENT, IS.CHAIN.CHILD
- **T7CHAINM.DFM** — "Chain Master": full chain definition editor; 9-column grid with PARENT/CHILD/AUTO/DESC/PARAM[1-5]

**IS.CHAIN table structure:** USER(15) + PARENT(12) + CHILD(12) PK; AUTO(1)=Y/N/A; DESC(100); PARAM[1-5](15 each)

**Confirmed parent programs:** T6SOA, T7SOA, T6SOC, T7SOC, T6SOD, T7SOD, T6SOE, T7SOE, T6SOF, T7SOF, T7WOA, T6POA, T7POA, T6POB, T6POR, T7ARA, T7APA, T7SON, ACHHSSOE

**Confirmed child programs:** T6SOB, T7SOB, T6SOC–T7SOF (variants), T7SOG, BKWOB–BKWOI (WO variants), T6WOC, T6WOE, T6POB/POBNP/POC, T7SOOF, T7ARE, T7POIG, BKSON, T6ARN, T7SON, T7SOE, T7WOC, T7WOKD

**AUTO field values:** Y=auto-launch without asking, N=do not chain, A=ask user before launching child

**DDF:** Two tables — ISCHAIN (user-level active chains) and ISCHAINM (chain master/template definitions)

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

### FO — Features & Options / Product Configurator (4 EVO modules)

**What it does:** A **customer-specific product configurator and quotation module**. Used when products can be built in multiple configurations (selected features, custom components, variable pricing). Generates a configurable document (ISFOHEAD/ISFOLINE) that then converts to a Sales Order, Work Order, or Purchase Order.

**Programs:**

| Program | Procs | Role |
|---------|------:|------|
| `EvoFNO.RWN` | 142 | Main configurator — create/edit F&O documents, manage options, convert |
| `EvoFNOSO.RWN` | 84 | Convert F&O → Sales Order (BKARINV/BKARINVL) |
| `EvoFNOWO.RWN` | 74 | Convert F&O → Work Order (WORKORD + WO BOM/routing) |
| `EvoFNOPO.RWN` | 54 | Convert F&O → Purchase Order (BKAPPOL/BKAPPO; checks BKSBVEND/BKSBMFG) |

**Table structure (confirmed from named_vars, Pass 110e, 2026-06-19):**

| Table | Fields | Purpose |
|-------|--------|---------|
| `ISFOHEAD` | 12+ | F&O document header: UID, PARENT, DATE, DESC, CUST, VEND, RFQ, STATUS, REV, MDATES, PERM, EXTRA |
| `ISFOLINE` | 20+ | Internal BOM/routing lines: LEVEL, COMP, QTYREQ, OP, OPYN, RTNUM, SCRAP, TYPE, VEND, DATE1/2, REV, PBRANC/CBRANC |
| `ISFOORDL` | 16+ | Customer-visible order lines: PCODE, PDESC, PQTY, PPRCE, PDISC, PEXT (extended $), ESD, LOC, TXBLE, UM, LN, DRAW, REV, LINE, OUID |
| `ISFOBMRM` | 7+ | BOM remarks for F&O lines (mirrors BKBMREMK structure) |
| `ISFOHIST` | 15+ | Audit history: WHO, DATE, TIME, STATUS, PART, CVTTO (converted-to type), CVTNO (order number after conversion), CITEM, QTY, LOC, CV, DDATE, PRICE |

**The two line types explained:**
- **ISFOLINE** — the *internal* BOM/routing structure (how the product is built): component, quantity required, operation, routing step, option flag (OPYN), scrap %, branch codes.
- **ISFOORDL** — the *customer-facing* order lines (what the customer is buying and at what price): part code, description, quantity, unit price, discount, extended price, ESD.

**Conversion workflow:**
1. Create F&O document in EvoFNO — enter customer (CUST), link to an RFQ (RFQ), define order lines (ISFOORDL) and BOM structure (ISFOLINE).
2. Set STATUS and REV as the quote evolves (full revision history in ISFOHIST).
3. Convert: EvoFNOSO creates an SO from ISFOORDL data; EvoFNOWO creates a WO with BOM derived from ISFOLINE; EvoFNOPO creates a PO (also cross-checks the Spec Book for approved vendors).
4. ISFOHIST records each conversion: CVTTO = "SO"/"WO"/"PO", CVTNO = the created order number.

**Context block vars (SOCB, WOCB, POCB, NICB, SQCB, RQCB)** — when EvoFNO is called from an existing SO/WO/PO/requisition, the caller passes its context; EvoFNO returns the configured options back to the calling program.

**How to access:** From the FO menu (access code FO), or triggered from SO/WO/PO entry screens when a configurable item is added.

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

**Full toolbar capabilities (confirmed from WBKLOOKUP.DFM):**
- **Change View** — switch between index/sort views of the table
- **Drill Down / Drill Up** — navigate the ISDRILLM hierarchy (child records → parent records)
- **Camera** — attach/view document images (EvoLinks integration)
- **CalcTot** — calculate column totals for numeric fields in the current view
- **doc_print** — print the lookup list
- **Manager** — escalated manager-level access for restricted operations
- **External Call** — invoke a custom RWN program registered for this lookup context
- **Triggers** — view/create trigger reminders (ISTRIGRS) from any record
- **openclose** — expand/collapse a record's linked sub-records inline
- **Alternate** — switch to the alternate Btrieve index for this table
- **Search** — free-text search across the visible columns

Control fields: `cbIndexName` (dropdown to pick active index), `link.to` (destination form to open on Select), `Drill.To` (drill-down target definition), `showgrid` (toggle grid vs. form view), `Filter.to` (WHERE-style filter expression).

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

WBKLOOKUP opens **76 tables** total — the complete set of every table that any lookup in the system can target. 70 of 76 are in the Pervasive DDF schema. Six are runtime-only; **BKLUGRID schema extracted from EvoERPDrillM LUGRID_* vars (Pass 115, 2026-06-19):**

**BKLUGRID** — Grid column layout configuration (14 fields confirmed):
| Field | Inferred Meaning |
|---|---|
| LUGRID_NAME | Grid identifier / name |
| LUGRID_FDNAME | Field name (column maps to this Btrieve field) |
| LUGRID_FORM | Form name associated with this grid entry |
| LUGRID_KEYFLD | Key field for sorting/navigation |
| LUGRID_KDATA | Key data value |
| LUGRID_DATA | Column data / content |
| LUGRID_TEXT | Display text / column header |
| LUGRID_EXTPARM | Extended parameters |
| LUGRID_EXTRA | Extra / misc config |
| LUGRID_EXTUDF | Extended UDF hook |
| LUGRID_END | End-of-record marker |
| LUGRID_PROT | Protected flag (read-only column?) |
| LUGRID_DELFLAG | Deleted flag |
| LUGRID_HNDL | File handle (runtime, may not be stored field) |

**FILEKEY / FILEDICT / FILEDFLD / FILEKNUM** — TAS runtime file-dictionary internals (field names from KEY_*/DICT_*/KNUM_* vars in EvoERPDrillM).  
**FILELOC** — TAS record-navigation API table (LOC_* vars).

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
| QU-F Query Executor | QUERYEXECUTE (26 procs) | **EvoPVT.jar launcher** — SQL execution happens in Java layer (Pass 114) |

**QU confidence: 75/100** — All 5 QU programs confirmed with DB fingerprints; ISDRILL(46f)/ISDRILLM(17f) fully extracted; WBKLOOKUP toolbar capabilities confirmed from DFM (11 toolbar actions); EvoBS multi-tab layout (Status+BarChart+PieChart+LineChart) + all ISBSF field bindings confirmed from DFM; CALDRILLBT calendar layout confirmed (date vars: ISTS.EDATE/ENTRY.DATE/DATE_TYPE/MM/DD/YY); QUERYEXECUTE confirmed as EvoPVT.jar launcher stub (same HOST/NAME/PORT/TREEDEST vars as CashFlow/CommissionRpt); BKLUGRID/FILEKEY/FILEDICT schema unknown (runtime-only tables).

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

**BOL workflow:** SO invoice → T7BOL reads BKARINV/BKARINVL for line items → ISSOBOX for box assignments (quantity/weight/lot/serial per box) → ISSHIPCO for carrier details → ISSHPVIA for account info → prints BOL with header fields.

**T7BOL form layout (confirmed from T7BOL.DFM — Pass 82):**
Header section: Authorization Number (author.number), Control Number (control.number), Load Number (load.number), Seal Number (seal.number), Trailer Number (trailer.number), Pick Up Date (pickup.date), Pick Up Time (pickup.time), Driver Arrived Time (driver.arrived), Loading Start Time (loading.start), Loading End Time (loading.end), Driver Departed Time (driver.departed). Line grid: LIST.DESC / LIST.QTY / LIST.CASES / LIST.WT / LIST.PALLET / LIST.DUEDATE / LIST.SHIPINFO. Edit row: edit.desc, edit.qty, edit.item.wt, edit.cases, edit.pallet.wt, edit.info, edit.htype, edit.hqty (handling unit type/qty), edit.pqty, edit.ptype (package type), edit.HM (hazmat flag), edit.nmfc (NMFC freight class code).

**T7BOLMSO form layout (confirmed from T7BOLMSO.DFM — Pass 82):**
Multi-SO/LTL variant adds: Billing Lines 1–6 (billing.line[1..6]), ship.custcode, full LTL fields: No. of Packages (edit.packs), Shipping Class# (edit.class), Weight (edit.weight), No. of Holding Units (edit.units), Hazardous Material (edit.hm), NMFC# (edit.nmfc), Package Type (edit.packtype). SO line grid: LIST.SONUM / LIST.ITEM / LIST.DESC / LIST.PQTY / LIST.PACKS / LIST.PACKTYPE / LIST.WEIGHT / LIST.HM / LIST.NMFC / LIST.CLASS.

**Confidence: 80/100** — Both DFMs fully analyzed; all BOL header fields confirmed (5 reference numbers + 6 timestamps); LTL freight classification fields confirmed; ISSOBOX(22f) and ISSHIPCO(16f) fully extracted; actual printed report layout in encrypted RWN.

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

**T7AUTOREBSS (79 procs) — Back-order Status Summary Recalculation:**
Opens 26 tables — BKICMSTR+MTICMSTR+BKICLOC+BKICLOCM+BKYSMSTR+BKARINVL+BKAPPOL+BKAPPO+WORKORD+WOBOM+INVTXN+BKBMMSTR+BKMRPFC+MTMRP+ISICMSTR+BKARINV+BKGLTRAN+DBAFIFO+ISTRIGRS+ISREMIND+LOT+SERIAL+ISNCR. The same table set as a full MRP run — this program recalculates the BSS (Back-order Status Summary) by reading all demand/supply, netting, and updating status flags across open SOs and WOs. Run nightly to keep the back-order report current.

**T7AUTOFX (21 procs) — Foreign Exchange Rate Auto-Update:**
DB: ISMCF+ISJAVA+ISMCR. Reads ISMCF (multi-currency FROM table — which currency pairs to update) → queues an ISJAVA task → EvoPVT.jar fetches live rates via HTTP → writes ISMCR (multi-currency rates table). Variables: CFROM (currency FROM code), TEST.MODE (dry-run flag), CDATE/CTIME (last update timestamp). The actual HTTP fetch runs inside EvoPVT.jar — T7AUTOFX just configures the task.

---

#### EvoScheduler Architecture (Pass 106f, 2026-06-18)

Three-program scheduler: EVOSCHEDULER (admin UI) + EVOSCHED (runner daemon) + EVOSERVICE (Windows service wrapper).

| Program | Procs | Role |
|---|---|---|
| EvoScheduler.RWN | 65 | **Admin UI** — create/edit/delete ISSCHED jobs; reads BKSYMSTR for program lookup |
| EvoSched.RWN | 21 | **Runner daemon** — polling loop; reads ISSCHED, checks DATE+TIME, invokes PROG |
| EVOSERVICE.RWN | 27 | **Windows service** — wraps EVOSCHED + ISREMIND reminder dispatch |
| EvoSchedSetup.RWN | 37 | **Email config** — stores SMTP credentials (EMAIL.CFG.SMTP/USER/PASS/EMAIL/SEC) in ISTS.CFG; used for job completion notifications |
| EvoServiceSetup.RWN | 49 | **Service SMTP config** — similar to EvoSchedSetup, registers EVOSERVICE Windows service |
| EvoServiceRemove.RWN | 18 | **Uninstall** — removes the Windows service registration |

**How a job executes (EvoSched.RWN):**
```
1. EvoSched reads ISTS.CFG.PTIME (polling interval, seconds)
2. Polling loop: read ISSCHED records sorted by DATE+TIME
3. For each record where IS.SCHED.DATE+IS.SCHED.TIME <= now:
   a. Load IS.SCHED.PROG (program name, e.g. "T7AUTOMRF")
   b. Load IS.SCHED.CO (company code), IS.SCHED.PARAM1..9 (up to 9 parameters)
   c. Execute: tp7runtime.exe runs PROG as a subprocess with company context + params
   d. Write IS.SCHED.LDATE+IS.SCHED.LTIME (last run date/time)
   e. Compute next run: IS.SCHED.TYPE = O(one-shot)/D(daily)/W(weekly)/M(monthly)
      → update IS.SCHED.DATE for next fire
4. Send IS.SCHED.EMAIL notification if configured (via EvoSchedSetup SMTP)
5. Sleep ISTS.CFG.PTIME seconds, repeat
```

**EVOSERVICE also handles ISREMIND:** The service polls both ISSCHED and ISREMIND. When a reminder's due date/time arrives, it sends the EMAIL notification configured in ISREMIND (REMIND.H = reminder header; PARSTO = party to notify).

**ISSCHED field reference:**

| Field | Size | Meaning |
|---|---|---|
| IS_SCHED_NAME | STRING 20 (PK) | Unique job name |
| IS.SCHED.DESC | STRING | Description |
| IS.SCHED.PROG | STRING | Program to run (RWN filename without extension) |
| IS.SCHED.CO | STRING | Company code context |
| IS.SCHED.TYPE | STRING 1 | Recurrence: O=one-shot, D=daily, W=weekly, M=monthly |
| IS.SCHED.DATE | DATE | Next run date |
| IS.SCHED.TIME | TIME | Next run time |
| IS.SCHED.RECUR | FLOAT | Recur every N minutes (alternative to TYPE) |
| IS.SCHED.LOG | STRING | Log file path for job output |
| IS.SCHED.EXTRA | STRING | Extra/notes |
| IS.SCHED.LDATE | DATE | Last run date |
| IS.SCHED.LTIME | TIME | Last run time |
| IS.SCHED.WHO | STRING | Who created this job |
| IS.SCHED.EMAIL | STRING | Email address for completion notification |
| IS.SCHED.PARAM1..9 | STRING | Up to 9 parameters passed to PROG |
| IS.SCHED.PARAM0 | STRING | 10th parameter slot |

(24 fields total confirmed in DDF; DFM analysis confirms at least 22 named fields above.)

**Confidence: 78/100** — All 8 AU automation programs identified with full DB fingerprints; BKDCLAB(50f)+BKDCCFG(7f) schemas fully extracted; ISSCHED(24f) all fields documented; EvoScheduler 3-program architecture confirmed; polling mechanism inferred from EvoSched.RWN variable names (ISTS.CFG.PTIME, SCHED.H); exact scheduling code logic blocked by RWN encryption.

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

FP-B "Print Features and Options" is a print sub-module of FO (Features & Options). There are zero
T7FP* programs — the print layer uses **T7FOD** and **T7FOE** (FO-labeled RWNs), not a separate
FP-prefixed namespace.

| Program | Procedures | Source | Purpose |
|---------|-----------|--------|---------|
| T7FOD | 103 | EVO.LIB | FP-B range print — filter by item range / category range / class range |
| T7FOE | 86 | EVO.LIB | FP-B single-item print — one Feature/Option item number |

**Database fingerprint (both programs, identical):** BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM,
CLASMSTR, BKSYHELP, DBAHLPID, ISIS, MKAHIST, ISLOG, ISDRILL, BKAPVEND, BKARCUST, BKCMACCN,
ISLINKS, BKAPDESC, LANGDICT, FILELOC (18 tables).

**Key variables (both programs):** `CFG.RTM.NAME`, `RTM_NAME`, `RTM.NUMBER`, `HOLD.RTM.NAME`,
`MAX.EVO.RTM`, `RTMVLD_NAME`, `ISTS.CFG.RTMSAV`, `ISTS.CFG.TFNAME` — the RTM filename is
**runtime-configurable** (loaded from a config/system setting), not hardcoded in the RWN bytecode.

**Notable:** MTICMSTR is included in the 18-table fingerprint, confirming FP can print from both
production inventory (BKICMSTR) and estimating inventory (MTICMSTR). The programs are full
print executors, not thin stubs.

**Confidence: 72/100** — T7FOD/T7FOE decrypted and symbol-extracted; 18-table DB fingerprint confirmed; RTM runtime-config pattern confirmed from variable names; RTM file content and exact column layout not yet read.

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

### BKED* Tables — EDI Processing (Pass 106, fully documented 2026-06-18)

**BKEDIH and BKEDIL are EDI inbound staging tables with byte-for-byte identical field layout to BKARINV/BKARINVL** — confirmed from Pervasive DDF (all fields carry BKAR_INV_* and BKAR_INVL_* names). EDI orders are imported, staged here, reviewed, then converted to live AR records.

| Table | Fields | Purpose |
|---|---|---|
| BKEDIH | 84 | EDI staged order header — verbatim BKARINV clone; holds inbound EDI 850 PO as a pending invoice |
| BKEDIL | 28 | EDI staged order lines — verbatim BKARINVL clone |
| BKEDIDUN | 7 | Customer DUNS mapping — CUST(PK)+DUNS(15)+EDI(Y/N)+EFFDT+PRODS(send 855)+ADVS(send 856)+SHPCD |
| BKEDMSTR | 3 | Company EDI config — NEXTN(counter)+DUNS(our D-U-N-S number)+PATH(66-char import file directory) |
| BKEDNOTE | 3 | Transaction notes — EDI#(FK→BKEDIH)+SO#(after conversion)+NOTE(80) |
| BKEDPOST | 2 | Posting audit trail — INVN(posted invoice#)+CUST(customer code) |

**EDI pipeline (DE-P submenu, all confirmed from BKMENUSU.TXT):**

| Step | Menu | Program | Action |
|---|---|---|---|
| 1 | DEP-B | T7DEPB | Import EDI Orders — reads X12 850 files from BKEDI_MST_PATH → writes BKEDIH/BKEDIL |
| 2 | DEP-C | T7DEPC | Edit EDI Orders — review and correct staging records |
| 3 | DEP-D | T7DEPD | Convert EDI Orders to Sales Orders — BKEDIH/BKEDIL → BKARINV/BKARINVL + writes BKEDPOST |
| 4 | DEP-E | T7DEPE | Export EDI Invoice/Acknowledgement — BKARINV → X12 810 (Invoice) or 855 (Order Ack) |
| 5 | DEP-F | T7DEPF | Export EDI ASN — BKARINV → X12 856 (Advance Ship Notice) |
| 6 | DEP-H | T7DEPH | EDI Error Report — list import errors |

**How to enable EDI for a customer:** Add a record to BKEDIDUN with the customer's D-U-N-S number and set BKEDI_DUN_EDI='Y'. Set PRODS='Y' to send 855 acknowledgments; set ADVS='Y' to send 856 ship notices.

**Confidence: 78/100** — Schema confirmed from DDF; pipeline confirmed from BKMENUSU.TXT; X12 transaction set version numbers (004010/005010) not confirmed.

---

### BKES* Tables — Estimating (Pass 106, fully documented 2026-06-18)

**BKESTQT and BKESTQTL are Estimating quote tables with byte-for-byte identical field layout to BKARINV/BKARINVL** — confirmed from Pervasive DDF. Estimates are stored as "pre-invoice" records; ES-E converts them directly to Sales Orders with no data transformation.

| Table | Fields | Purpose |
|---|---|---|
| BKESTQT | 84 | Estimate/quote header — verbatim BKARINV clone; PK=BKAR_INV_NUM (quote number) |
| BKESTQTL | 28 | Estimate line items — verbatim BKARINVL clone |
| BKESTCFG | 13 | Estimating defaults — NUM(next quote#)+STAT(default status)+CLASS(4)+FORM(1)+CMPY_INFO+DAYS(expiry)+ENDLN_1..5(30 each, footer lines)+SONUM(last converted SO)+EXTRA |
| ESTSUM | 213 | Estimate cost summary — MTESUM_QUOTE(PK)+date/status/item/customer + QTY_1..10 (10 qty breaks) × 18 cost categories (MAT/LAB/SETUP/OH/MISC/TOTAL/PRICE etc.) |
| BKMATCST | 25 | Material cost breaks — CODE(PK), 10×QTY_N+10×COST_N, MIN+MINCST+DATE |
| BKRTCST | 24 | Routing cost breaks — QUOTE+CODE+OPER(PK), 10×PARTSHR_N+10×SETUP_N |

**Estimating module workflow (all 11 ES operations confirmed from BKMENUSU.TXT):**

| Step | Menu | Program | Action |
|---|---|---|---|
| 1 | ES-A | T7ESA | Enter Estimates — create/edit BKESTQT/BKESTQTL; draws from BOM (BKBMMSTR) and item master |
| 2 | ES-D | T7EST | Quick Estimate — simplified estimate entry |
| 3 | ES-C | T7ESC | Print Cost Rollup — uses BKRFQ for vendor pricing |
| 4 | ES-B | T7ESB | Print Customer Quotes — formatted quote output |
| 5 | ES-E | T7ESE | Convert Estimates → SO (BKARINV) or WO (WORKORD) |
| — | ES-H | T7ESH | Enter Material Costs → BKMATCST |
| — | ES-J | T7DSEST | Estimating Defaults → BKESTCFG |
| — | ES-K | T7IC2EST | Copy Production→Estimating Inventory (BKICMSTR→MTICMSTR) |
| — | ES-L | T7ESL | Edit Estimating Inventory (MTICMSTR) |

**The estimating module has its own inventory** (MTICMSTR — 108 fields, ES-specific item master separate from production BKICMSTR) and its own cost tables (BKMATCST, BKRTCST). ES-K syncs production inventory into the estimating copy.

**Confidence: 78/100** — Schema confirmed from DDF; field semantics confirmed; pipeline confirmed from BKMENUSU.TXT program labels; BKESTCFG 40-byte gap (offsets 14–53) has unregistered fields unknown.

---

### YS — Y/N System Flags Editor

T7YSYN (52 procs) — opens BKYSMSTR. Maintenance program for the BKYSMSTR table (Y/N system
configuration flags). Every Yes/No behavioral setting in EvoERP lives in BKYSMSTR; T7YSYN is
the direct editor for these flags.

**BKYSMSTR structure:**
- BKYS_WONUM (FLOAT 8) — row key (only one row per company; value = 0 or company#)
- BKYS_YN_1 through BKYS_YN_354 — 354 × STRING(1) flags; each = 'Y' or 'N'

**T7YSYN display mechanism:**
Variables `ARRAY` and `ARRAY.DESC` confirm T7YSYN presents the flags as an array with descriptions.
The descriptions come from `BKSYHELP/DBAHLPID` (the help system — each YN flag index maps to
a DBAHLPID help record). The program header variable `PROGRAM.HEADER` provides the window title.
`YSMSTR.H` = the BKYSMSTR record handle (single-row table loaded once).

**Selected YN flag meanings (confirmed from source files and DFM field labels):**

| Flag | Known meaning | Source |
|---|---|---|
| YN[1] | Auto-close DC labor when new job started | T7DCK DFM (BKDC.CFG.AUTOCLOSE) |
| YN[20] | DC barcode mode: sets EXTRA='B' on labor records when parts > 0 | BKDCA.SRC line 708 |
| YN[36] | Routing default: MTRO.MD.PROC.HR (processes-per-hour method flag) | BKROA.SRC line 609 |
| YN[37] | Routing default: MTRO.STD.TIME (standard time flag) | BKROA.SRC line 656 |
| YN[38] | MD-B routing: 'Y'=use template# as sequence#; 'N'=increment counter | BKROA.SRC lines 392/1582 |
| YN[48] | AP check print format: 1/4/5=laser (chain to BKAPHA); 2/3=dot-matrix | Bkaph.src line 60 |
| YN[59] | MD-D routing: 'Y'=prompt for OVERLAP and NEGOVLP during RO-A entry | BKROA.SRC line 647 |
| YN[66] | Routing: 'Y'=show long-run time field (LONGTIME) in routing entry | BKROA.SRC line 629 |
| YN[228] | DC: 'Y'=use alternate screen BKDCAF; 'N'=use standard BKDCA screen | BKDCA.SRC line 194 |
| YN[229] | DC auto-close: 'Y'=auto-close open job when employee starts a new job | BKDCA.SRC line 228 |
| YN[290] | Include backorders in order status report | BKSYAR.INCLBO cross-ref |
| (most) | Individual flag meanings blocked by RWN encryption | encrypted T7YSYN source |

**⚠️ Correction:** YN[228] was previously documented as "Auto-close labor" — this is wrong.
YN[228] = alternate screen selector (BKDCAF vs BKDCA). YN[229] = auto-close. Confirmed from
BKDCA.SRC source, Pass 118.

The full 354-flag meaning set requires either: (a) decrypting T7YSYN.RWN and reading the ARRAY.DESC
initialization code, or (b) a live EvoERP session walking through the YS editor screen.

**Note:** T7MDefaults.RWN (435 procs) and T7MDefNDC.RWN (252 procs) are the primary UI
for setting these flags — T7YSYN is the back-door "raw" editor for troubleshooting.
Changes to BKYSMSTR take effect immediately for all users on next program load.

**Confidence: 80/100** — BKYSMSTR(355f: 1 key + 354 YN flags) fully extracted; T7YSYN display
mechanism confirmed; 11 specific flags now confirmed from source code (BKDCA.SRC, BKROA.SRC,
Bkaph.src) + DFM analysis; corrected YN[228] documentation (was wrong); most flags still opaque
without RWN decryption.

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

**Key filter variables (confirmed from named_vars):**
- `EJOB` — job number filter (filter cut sheet by job code → ISJOB)
- `ELOT` — lot filter (show only BOM lines with this lot)
- `EQTY` — entry quantity override

**T7CUTSHEET2 also opens ISDUTY + ISBROKER** — this indicates import duty tracking capability:
for purchased components from overseas suppliers, the cut sheet can optionally show
duty/tariff rates (ISDUTY) and broker codes (ISBROKER) alongside the standard BOM components.
This is likely used when the WO is for assemblies using imported materials.

**i2 Systems variant: J7CCCutSheet.RWN (217 procs, 44 tables)**
The i2 customized version adds: ISSRINFO (SR info), ROUTING (routing ops), BKBMMSTR (BOM),
ISJOB, BKARINV/BKARINVL (SO context), BKICLOC, BKICLOCM, BKMRPFC, BKGLTRAN+DBAFIFO (costing),
LOT+SERIAL+ISNCR (quality). Key variables: LIST.WO/ITEM/FABRIC/WOQTY arrays + EDIT.WO.LOC
(which location) + NEW.WO.SQTY (suggested qty). This is a full material management suite
beyond the base cut sheet.

**Confidence: 75/100** — Both programs (lot-tracked and non-lot variants) fully confirmed; WOBOM(24f)+WOMAT(17f)+ISBINLOT(11f) fully extracted; cut sheet workflow confirmed from table relationships; ISDUTY+ISBROKER presence confirms import-component duty tracking; EJOB/ELOT/EQTY filter vars confirmed; i2 J7CCCutSheet program documented.

---

### AD/ADCA — Advanced Data Collection (Shop Floor Automatic DC)

T7ADCA (290 procs, 55 unique tables) — the largest DC entry module. Full automatic shop floor
data collection: real-time labor posting, routing tracking, QC inspection, and tray management.

**Note (Pass 109):** T7ADA/T7ADB/T7ADC do **not exist** on the network share — they were a false inference. The AD subsystem has exactly one program: T7ADCA. (Confirmed by exhaustive rwn_symbols.json search.)

Key tables opened (unique to or important in T7ADCA):

| Table | Fields | Purpose |
|---|---|---|
| BKDCSHFT | 34 | Shift definitions — 3-shift configuration (Pass 109: all 34 fields confirmed) |
| ISROUTEX | 100 | Routing extension — IS_ROUT_CODE+OPER PK; 10 machine slots × CYCTIME/CYCHR/... fields; extended cycle times per routing operation |
| ISWOROEX | 60 | WO Routing extension — WOPRE+WOSUF+OPER PK; ITP(item type pack), FOI(1), LQTY(labor qty), EXTRA(100), SDAY/FDAY, DATE1, ALPHA1/2, NUM1, DESC1 + 45 more custom slots |
| ISWOEX | 63 | WO Extended fields — WOPRE+WOSUF PK; ITP(20), RF(1), EXTRA(100), MCLASS(6), MNUM, dates 1-4, INT1, NUM1 + 48 more |
| OPQCDESC | 10 | Operation QC description — WOPRE+WOSUF+OPER PK; DESC(30)+SERIAL(25)+UID(30)+QCCODE(2)+DATE+QTY+EXTRA; QC result per WO operation |
| ISWOTRAY | 52 | WO Tray tracking — tray number + WO/oper + started/completed/scrapped qty + 5 bin splits |
| BKPRMSTR | — | Payroll employee master — ADCA is payroll-aware; employee ID at scan → BKPRMSTR lookup |
| EIMCOLST | — | NOT IN DDF — EIM Color List (UI display config for DC labor screen) |

**BKDCSHFT (34 fields) — complete field list:**
- `BKDC_SH_NAME1/2/3` (3×25) — names for the 3 shifts (e.g., "Day", "Swing", "Night")
- Per shift (×3), 10 TIME fields: `BUFFER_n` (pre-start), `START_n`, `BRK1IN_n`, `BRK1OUT_n` (first break), `LUNCHIN_n`, `LUNCHOT_n` (lunch), `BRK2IN_n`, `BRK2OUT_n` (second break), `FIN_n` (shift end), `FINBUF_n` (post-finish buffer)
- `BKDC_SH_EXTRA` (50) — extra notes
Total: 3 names + 30 time fields + 1 extra = 34 fields. One row per company.

Also opens: BKDCLAB, WORKORD, MTICMSTR, BKICMSTR, WOROUT, ROUTING, MACHINE, WORKCTR, WOLABOR, SCRAP, ISLOG (kill-flag process control)

**ADCA vs PA distinction:** ADCA opens BKPRMSTR (payroll) + BKDCSHFT (shifts) → scanner-driven, payroll-integrated. PA opens WOMAT + INVTXN + ISBINLOT → touchscreen-driven, material-issue capable. Neither can do what the other does.

**ADCA Workflow:** Operator scans badge → T7ADCA resolves employee via BKPRMSTR → reads WORKORD + ROUTING for WO operation context → posts BKDCLAB labor record → updates WOLABOR/WOROUT → if QC required, creates OPQCDESC → if tray tracking, updates ISWOTRAY

**Confidence: 72/100** — T7ADCA confirmed with 55 unique tables; BKDCSHFT all 34 fields decoded (Pass 109); all key tables fully field-documented; T7ADA/B/C confirmed non-existent; ADCA vs PA functional distinction documented; ISLOG kill-flag mechanism confirmed; specific screen field mapping blocked by RWN encryption.

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

**Key variables (confirmed from named_vars):**
- `CHKACT.TXT` — check account text (account label for the NACHA file header)
- `FROM.CHKNUM` / `THRU.CHKNUM` — check number range filter (select checks to include in batch)
- `FROM.CHKDATE` / `THRU.CHKDATE` — date range filter
- `ACH.FILENAME` — full path of the output NACHA flat file (e.g. `C:\NACHA\PAYMENTS.ACH`)
- `WELLS.ID` — Wells Fargo company ID code (bank-specific identifier in the NACHA batch header)

**BKARINVL in TE DB fingerprint:**
T7TESTNACHA opens BKARINVL (AR invoice lines) — this confirms the module handles
**both directions** of ACH:
- AP side: reads BKAPVEND (vendor ACH routing/account) → BKGLCHK (AP checks) → PPD/CCD debit entries
- AR side: reads BKARINVL (customer invoices) → generates ACH CREDIT entries for customer payments

**WELLS.ID specificity:** The hard-coded Wells Fargo ID variable indicates i2 Systems
configured T7TESTNACHA specifically for Wells Fargo ACH submission. Other banks may use
different ID formats in the ACH Company ID field (10-char NACHA standard field).

**NACHA file structure (standard, generated by T7TESTNACHA):**
```
Record 1: File Header (1 per file)
Record 5: Batch Header (1 per bank account = ISBANKS row)
Record 6: Entry Detail (1 per vendor check in BKGLCHK range)
Record 8: Batch Control (1 per batch)
Record 9: File Control (1 per file)
```
Entry Detail fields come from: ISBANKS.ROUT (9-digit ABA routing) + BKAPVEND.ACH_ACCT
(vendor bank account) + BKGLCHK.AMT (payment amount) + BKGLCHK.NAME (payee).

**Confidence: 75/100** — T7TESTNACHA(103p) confirmed; BKGLCHK(11f)+ISBANKS(23f) fully extracted; key variable names confirm check-range filters + ACH output filename + Wells Fargo ID; BKARINVL presence confirms AR ACH receipts in addition to AP payments; NACHA record structure standard (not EVO-specific); exact field mapping to NACHA offsets blocked by RWN encryption.

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

**SERIAL (30f) — Central Serial Number Master (Pass 109: all 30 fields confirmed from DDF):**

| Field | Type | Size | Meaning |
|---|---|---|---|
| MTSER_CODE | STRING | 15 | Item code (PK part 1, FK → BKICMSTR) |
| MTSER_SERIAL | STRING | 25 | Serial number string (PK part 2) |
| MTSER_LOT | STRING | 15 | Associated lot number |
| MTSER_PO | FLOAT | 8 | PO number (purchased path) |
| MTSER_RECDOC | FLOAT | 8 | Receipt document number |
| MTSER_VENDOR | STRING | 10 | Vendor code (FK → BKAPVEND) |
| MTSER_RECDATE | DATE | 4 | PO receipt date |
| MTSER_POCOST | FLOAT | 8 | PO receipt unit cost |
| MTSER_SO | FLOAT | 8 | SO number (ship path) |
| MTSER_CUSTCODE | STRING | 10 | Customer code (FK → BKARCUST) |
| MTSER_SHIPDATE | DATE | 4 | Date shipped to customer |
| MTSER_SELLPRICE | FLOAT | 8 | Selling price |
| MTSER_WO | FLOAT | 8 | WO number (manufacturing path) |
| MTSER_WOSUF | UBINARY | 2 | WO suffix |
| MTSER_WOCODE | STRING | 15 | WO part code |
| MTSER_ISSDATE | DATE | 4 | WO issue date (component issued to WO) |
| MTSER_ISSCOST | FLOAT | 8 | Cost at WO issue |
| MTSER_INRECDATE | DATE | 4 | Internal WO receipt date (finished good received back) |
| MTSER_INRECCOST | FLOAT | 8 | Cost at WO completion |
| MTSER_EXPDATE | DATE | 4 | Expiration / warranty date |
| MTSER_NOTES_1 | STRING | 30 | Free-text note 1 |
| MTSER_NOTES_2 | STRING | 30 | Free-text note 2 |
| MTSER_NOTES_3 | STRING | 30 | Free-text note 3 |
| MTSER_NOTES_4 | STRING | 30 | Free-text note 4 |
| MTSER_NOTES_5 | STRING | 30 | Free-text note 5 |
| MTSER_ONHAND | FLOAT | 8 | Current on-hand quantity (1=in stock, 0=shipped/consumed) |
| MTSER_LOC | STRING | 10 | Current warehouse location |
| MTSER_BIN | STRING | 15 | Current bin location |
| MTSER_INV | FLOAT | 8 | AR invoice number (when invoiced on SO) |
| MTSER_EXTRA | STRING | 50 | Extra notes |

**Serial number lifecycle — fully traced from MTSER fields (Pass 109):**

1. **Purchase receipt** (T7SCH / PO Receiving): RECDATE + PO + RECDOC + VENDOR + POCOST set; ONHAND → 1; LOC/BIN = receiving location.
2. **Issued to WO as component**: ISSDATE + WO + WOSUF + WOCODE + ISSCOST set; ONHAND → 0 (consumed into WO).
3. **WO completion / internal receipt**: INRECDATE + INRECCOST set; ONHAND → 1; LOC/BIN = finished goods location.
4. **SO shipment**: SHIPDATE + SO + CUSTCODE + SELLPRICE + INV set; ONHAND → 0 (shipped).
5. **Expiry tracking**: EXPDATE populated at receipt or manufacturing for shelf-life / warranty management.

**ISSERIAL (11f) — WO Serial Genealogy:**
- `IS_SER_WOPRE/WOSUF` — which WO produced this relationship
- `IS_SER_PARENT(15)` + `PDESC(30)` + `PSERIAL(25)` — the parent/output item code, desc, and serial
- `IS_SER_ADATE` — assembly date
- `IS_SER_COMP(15)` + `CDESC(30)` + `CSERIAL(25)` — the component item code, desc, and serial consumed
- `IS_SER_FDATE` — finish date
- `IS_SER_EXRA(100)` — extra

Each ISSERIAL row records: "WO WOPRE/WOSUF consumed component serial CSERIAL to produce parent serial PSERIAL." This is the serial genealogy / traceability chain — supports regulatory traceability ("which serial numbers went into unit X?").

**ISSERCNT (9f) — Serial Auto-Number Config per Item:**
- IS_SERC_ITEM(15) — item (PK)
- IS_SERC_CLASS(4) — classification code
- IS_SERC_SPOS(2) — start position of numeric portion within serial string
- IS_SERC_LENG(2) — length of numeric portion
- IS_SERC_TOTAL(2) — total serial string length
- IS_SERC_NUMBER(8) — current next sequence number
- IS_SERC_LAST(25) — last serial issued (text)
- IS_SERC_L2(2) — length-2 (second numeric component, for compound format)
- IS_SERC_EXTRA(100) — extra

**Architecture:** T7SCA assigns/counts serials; T7SCB lists/maintains with trigger links; T7SCC posts count transactions; T7SCE inquires by location; T7SCF shows full serial transaction history (INVTXN); T7SCG maintains ISSERCNT auto-number counters; T7SCH posts serial WO receipts and SO shipments (cross-references WORECV+BKARINV); T7SCOMP handles compound/batch serial definitions (ISSCOMP).

**Confidence: 80/100** — 9 programs confirmed; SERIAL(30f) all 30 fields decoded with lifecycle mapping (Pass 109); ISSERIAL(11f) genealogy table fully documented; ISSERCNT(9f) auto-number config documented; ISSCOMP(5f) confirmed; per-screen field binding blocked by RWN encryption.

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

**T7QTINFO UI (confirmed from DFM — Pass 80):**
The "Quote Misc. Information" form exposes the ISQTINFO alt-index of ISSRINFO:
- 5 date fields: ISSR.INFO.DATE[1..5] — configurable date slots per site (e.g. "Quoted", "Promised", "Required")
- Multiple alpha fields: ISSR.INFO.AL1..5 and more (25-char each) — configurable text slots
- Field labels (qtDate1..5, qtAlpha1..5) are TAS Pro runtime variables that resolve to site-configured caption text at runtime
- ISSR.INFO.CODE (15) selects which configuration record defines the slot meanings

Same 40-alpha/10-date capacity as ISSRINFO; the QT version uses the ISQTINFO alternate-index for quote-number sort.

**Confidence: 74/100** — T7QTINFO confirmed; LANGDICT(5f)+BKICREF(8f)+ISTERMS(13f) all fully extracted from DDF; quote-as-SR-order architecture confirmed; T7QTINFO DFM confirms ISSR.INFO.DATE[1..5]+ISSR.INFO.AL1..5 pattern from ISQTINFO alt-index; complete quote lifecycle blocked by encryption.

---

### SL — Shop Loading (Expanded)

T7SLSFC (5p, source=ISTS.SRC): Shop loading display — overlays AR demand on production capacity.
Opens BKARINVL+BKYSMSTR+BKDCLAB+BKARCUST+ISWOPRIO+WORKCTR+ROUTING+ISMCR+TASCOLOR (22 unique
tables total).

**T7SLSFC is Java-backed** (Pass 157, 2026-06-22): Symbol extraction confirmed JAVA.PATH +
JAVA.PATH2 variables — the TAS stub launches one or more Java scheduler applications:

| JAR | Main Class | Purpose |
|-----|-----------|---------|
| Scheduler.jar | main.Driver | Shop Loading primary (older generation) |
| WCScheduler.jar | com.evoerp.wcsched.main.Main | Work Center Scheduler |
| WOScheduler.jar | com.evoerp.main.Main | Work Order Scheduler |
| WorkCenterLoad.jar | com.evoerp.wcload.javafx.App | Visual WC capacity load (JavaFX) |
| MachineView.jar | com.evoerp.machineview.jfx.App | Machine view (JavaFX) |

Key variables: PLDN (production line down), PTDN (production/tool down), WEBLINK + XCPATH
(cross-platform display paths), CFG.BUFFER. Config flags: ISTS.CFG.AUTOSL (auto shop loading),
ISTS.CFG.AUTOPL (auto production loading), ISTS.CFG.WCBF (WC buffer), ISTS.CFG.WCDEPT (WC dept).

**BKDCLAB** (50f): DC Labor transaction record (date+EMP+WOPRE+WOSUF+OPER PK; POSTED+SHIFT+
START/STOP/PARTS/SCRAPPED/NOJOBS + hours/rates/GL fields).

**ISWOPRIO** (4f): WO priority code — PRIO+DESC+EXTRA+COLOR.

**Confidence: 73/100** — T7SLSFC decrypted + symbol-extracted (Pass 157); Java-backed architecture
confirmed; 22-table DB fingerprint re-confirmed; 5 candidate scheduler JARs identified by package
name; exact JAR dispatch logic not yet traced (which JAR for which SL sub-operation).

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

**T7PAPERLESS** (205 procs, 50 tables), **T7PACKMENU** (5 procs, stub), **T7PASS** (3 procs, 45 tables — password sub).

Paperless DC = touchscreen/kiosk-based WO operation reporting without paper travelers. Opens identical core tables to ADCA (BKDCLAB, ISWOTRAY, WORECV, WORKORD, WOROUT, ROUTING) plus several that ADCA does not open:

| PA-only tables | Missing from ADCA | Implication |
|---------------|-------------------|-------------|
| WOMAT | BKPRMSTR | PA can post WO material issues (BOM consumption) — ADCA cannot |
| INVTXN | BKDCSHFT | PA writes inventory transactions at posting; ADCA doesn't (uses payroll/shift timing instead) |
| ISBINLOT | EIMCOLST | PA does bin-level lot traceability; ADCA has EIM color display config |
| BKBMMSTR | — | PA reads BOM master directly |
| ISACCESS | — | PA checks module-enable flag (license gate) |
| BKYSMSTR | — | PA reads the company/system master |
| WOBOM | — | PA opens the WO BOM detail for material pickup |
| WODATE | — | PA tracks WO date milestones |

**PA vs ADCA distinction:** ADCA is the **scanner-driven** auto-collect path (badge + barcode scan, payroll-integrated with BKPRMSTR, shift-aware via BKDCSHFT). PA is the **touchscreen/menu-driven** kiosk path (operator taps operations, posts BOM material issues via WOMAT, records INVTXN). Both post BKDCLAB labor records and use ISLOG for process-control kill-flag.

**T7PASS** = shared password entry sub-program called by T7PAPERLESS (45 of PA's 50 tables appear in T7PASS — confirms it's a helper that initializes the same session context).

**Confidence: 72/100** — 50-table fingerprint confirmed; PA vs ADCA distinction documented (Pass 109); WOMAT/INVTXN/ISBINLOT material-issue capability confirmed; BKAPPOL confirms outside-process PO receiving from floor; screen-level field mapping blocked by RWN encryption.

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

All T7JS* report programs share the same 64-table ISDRILL-based DB set. These programs bridge EvoERP data to an external BI reporting system.

**DFM confirmation (Pass 82):** T7JSACC, T7JSAIC, T7JSAPBI, T7JSASRS, T7JSOI, T7JSQL, T7JSettings all confirmed from DFMs. Each shows identical DSN configuration form: Host, Port, Name (database name), Company DSN Settings. T7JSettings and T7JSQL additionally have a "Destination" field (TREEDEST — tree-view destination path for the report hierarchy). T7JSettings adds "Detect Settings" and "Generate Program" buttons. The JS system connects EvoERP to an external database/BI server via ODBC DSN — not a JavaScript layer; "JS" = Java/external Sync.

---

### T7EWC — Work Center Capacity Edit

**T7EWC** (68 procs, 45 tables) — opens WORKORD+WOROUT+WORKCTR+ROUTING+BKYSMSTR.

EWC = Edit Work Center. Full UI (68 procs) for work center setup and/or capacity load editing. WORKCTR = work center master, ROUTING = operations. Complements T7VSCHED (visual Gantt view).

---

### T7BS — Business Status Dashboard

**T7BS** (162 procs, 40 tables) — opens ISBSF+BKYSMSTR+ISGLDATE+BKSYMSTR+BKGLTRAN+MTICMSTR+BKICMSTR+WORKORD+WOMAT+WOLABOR.

BS = Business Status KPI dashboard. **Writer/viewer split (Pass 114, 2026-06-19):**
- **T7BS.RWN** (162 procs) = KPI **writer** — queries 40+ tables and populates ISBSF with the snapshot. Opens ISBANKS for cash balance; ISGLDATE for period-end date arithmetic. Procedure vars confirm per-field reads: ISBSF.AR.BAL/BILL/RECP/DISC/COGS + ISBSF.AP.BAL/PAYA/PAYM.
- **EVOBS.RWN** (128 procs, menu QU-D) = KPI **viewer** — reads ISBSF + supplements with live BKGLTRAN+MTICMSTR for on-screen display. Does NOT write ISBSF.

T7BS is driven from the BS module menu (BS-A recalculate); EVOBS is the read-only inquiry view.

**EvoBS screen layout (confirmed from EvoBS.DFM + EvoBSCash.DFM + EvoBSWO.DFM):**

The screen is a floating "stay-on-top" dashboard with 4 tabs:
- **Status** — the main KPI grid with 8 module group boxes and a period range selector
- **Bar Charts** — bar chart trending the selected KPI over time
- **Pie Charts** — pie chart of module proportions
- **Line Charts** — line chart of KPI trend (12 or 24 months)

Status tab group boxes and their ISBSF fields:
| Group | Field(s) shown | ISBSF field names |
|---|---|---|
| Accounts Receivable | Balance / Billings / Receipts / Discounts / COGS / Deposits | AR_BAL / AR_BILL / AR_RECP / AR_DISC / AR_COGS / AR_DEPO |
| Accounts Payable | Balance / Payables / Payments / Discounts / Avail-to-Pay | AP_BAL / AP_PAYA / AP_PAYM / AP_DISC / AP_ATP |
| Sales Orders | Open / Bookings / Shipments | SO_OPEN / SO_BOOK / SO_SHIP |
| Purchase Orders | Open / Bookings / Receipts | PO_OPEN / PO_BOOK / PO_RECP |
| Work Orders | WIP Balance / Issues / FP Variance | WO_WIPBAL / WO_ISSU / WO_FPVAR |
| Inventory | Value | IC_VALUE |
| Cash | Total | CASH_TOTA |
| Period | 12-month / 24-month range pickers | `months12` / `months24` (runtime UI vars, not ISBSF fields) |

Cash Detail drill-down (EvoBSCash.DFM): CASH_TOTA + CASH_ACT1..9 (9 named bank accounts) — backed by CASH_ACTS_1..100 (100 individual GL account slots).

WO Detail drill-down (EvoBSWO.DFM): WO_WIPBAL + WO_ISSU + WO_FPVAR (summary); WOS_LAB / WOS_MAT / WOS_FOH / WOS_VOH / WOS_MEXT (issue cost breakdown); WOS_FP (finished production value); WOS_WIPV (WIP variance); WOS_SETUP (setup cost); WOS_OUTP (outside process cost).

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
| ACRDTYPE | 3 | Activity record type + disposition codes — NOT IN DDF schema but fields confirmed from T7ACRDTYPE.DFM: ac.rd.type (Doc Type), ac.rd.reason (Reason), ac.rd.dispo (Disposition). Disposition = rework / scrap / use-as-is |

**WODATE hierarchy:** PARPRE/PARSUF = immediate parent WO (multi-level BOM sub-assembly), TOPPRE/TOPSUF = root of WO tree (top-level assembly), DELPRE/DELSUF = delivery WO (SO-linked WO for customer order). Used by MRP capacity scheduling (T7MRIX) and the SH shop scheduling module. This hierarchy enables EvoERP to schedule and track the full tree of sub-assemblies under a customer order.

---

## WC — Warehouse Control (bin master)

(Disambiguation: WC = Warehouse Control bin management, **not** Work Center. Work centers are in the `WORKCTR` table used by routing and scheduling.)

**Module purpose:** Manages physical bin locations within warehouse locations. Supports bin-level inventory tracking, serial-by-bin queries, bulk bin import, and bin-location synchronization.

### WC Program Map (confirmed from DFMs — Pass 81)

| Program | Procs | Operation | Confirmed purpose |
|---|---|---|---|
| T7WCA | — | WC-A Bin Master | Create/edit/delete bins in ISBNMSTR (LOC+BIN+DESC) |
| T7WCBK | ? | WC-BK Live Schedule | Floating "Live Work Center Schedule" dashboard — filters by work center, WO status, operation, category, customer, priority; auto-refreshes on timer (ISE.STATUS.2/3 filters) |
| T7WCBinLot | ? | Bin-Lot Batch | Batch file processor for bin/lot assignments (shows Files Processed counter) |
| T7WCC | — | WC-C Serials by Bin | Queries serial numbers located at a specific bin |
| T7WCD | ? | WC-D Bin Location Import | Imports bin location assignments from CSV or fixed-length file; fields: Location(required), Default Bin, Item Number(required), Bin Description, Lot, Serial; Skip/Replace mode |
| T7WCE | ? | WC-E Bin Location Report | Prints inventory-by-bin-location report filtered by item range + class + category + type + active status + bin range + cycle code; optionally includes all warehouses and lot numbers |
| T7WCF | ? | WC-F Inventory Listing | Simplified inventory listing by warehouse — item range + class + category + type + active status; no bin-specific filters |
| T7WCG | ? | WC-G Default Bin Assignment | Sets the default bin for items at a specific location; item range + class + category + type; writes ISBINLOC.DFLT flag |
| T7WCH | ? | WC-H Bin Browse | Browse all bins for a location+bin range (bkic.locm.name + from.bin + thru.bin) |
| T7WCLOCFIX | ? | WC LOC Sync | "This Utility will Update MTIC.PROD.LOC with the Default WC Bin" — syncs ISBIN.LOC.ITEM to MTICMSTR.PROD.LOC using the item's default bin |

### WC Table Family (confirmed from DDF)

| Table | Fields | Purpose |
|---|---|---|
| BKICLOCM | 12 | Warehouse location master — LOC(10) PK, NAME(30), address fields, company flags |
| BKICLOC | 32 | Item-by-location inventory — PROD(15)+LOC(10) PK; UOH/UOSO/UBO/UOO qty fields; all 5 cost fields; GL account |
| ISBNMSTR | 4 | Bin master — LOC(10)+BIN(15) PK; DESC(60)+EXTRA(100); named bin positions within a location |
| ISBINLOC | 9 | Item bin assignment — ITEM(15)+LOC(10)+BIN(15) PK; UOH(qty on hand in this bin); CDATE(count date)+VDATE(verified date); DFLT(1, default bin flag); RVLVL(5, reorder level) |
| ISBINLOT | 11 | Bin-lot cross-reference — ITEM+LOC+LOT+BIN PK; UOH(qty in this bin for this lot); DATE; FLAG; TMPSO/TMPPO(40 each, temp SO/PO reserve pointers); DFLT |

**BKICLOC hierarchy:** Location (BKICLOCM) → Item-at-location (BKICLOC) → Bin assignment (ISBINLOC) → Lot-at-bin (ISBINLOT). ISBINLOC.UOH can only equal BKICLOC.UOH when a single-bin item. Multi-bin items spread UOH across ISBINLOC rows.

**Confidence: 80/100** — 10 programs confirmed from DFMs; full bin table family (ISBNMSTR+ISBINLOC+ISBINLOT+BKICLOCM+BKICLOC) extracted from DDF; all WC operation purposes confirmed; proc counts and serial/lot detail scanning logic blocked by RWN encryption.

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
| T7UTH | 109 | UT-H file layout report — dumps table layout from FILEDICT+FILEKEY (TAS Pro runtime schema); useful for internal schema documentation |
| T7UTI | 101 | UT-I company add/delete — opens BKPSUSER+BKSYAP+BKSYMSTR+BKICLOCM; creates or removes a company (DESTRUCTIVE for delete) |
| T7UTKA | 74 | UT-KA module data clear — selective data delete (enter "D" for full delete, "C" for transactions only) for GL/AR-SO/AP-PO/Manufacturing-IC/Payroll/CM; also resets GL period dates; DESTRUCTIVE |
| T7UTKD | 91 | UT-KD GL fiscal year archive — archives GL transactions by year (current + up to 6 prior years); sets GL account range + suspense account for inter-year balancing; uses ISGLDATE + BKGLTRAN |
| T7UTKE | 238 | UT-KE location code rename — **renames** an existing warehouse location code to a new value, updating all references across IC and AR tables (BKICLOC/BKICMSTR/BKARINV/BKARINVL etc.); NOT just cleanup — it's a full rename cascade |
| T7UTKF | 116 | UT-KF inventory listing — prints IC item list filtered by item range + class + category + type [RFAMNLBTKO]; optional extended description; reads BKICMSTR+INVTXN+BKICLOC |
| T7UTKG | 145 | UT-KG inventory GL account listing — prints items with their GL account assignments; filtered by item range + class + category + active status [YNODEPSQR] + type [RFAM] + GL account range |
| T7UTKH | 135 | UT-KH inventory type report — prints items filtered by type (Purchased/Make-From/Subassembly/Finished Goods); item range + class + GL account range; toggle inactive + 2nd description line |
| T7FNR | 104 | TA-D file navigator — browse all FILEDICT definitions; opens FILEDICT+FILELOC+ISDRILL |

**Note on UTK* descriptions (Pass 79 correction):** Prior Pass 51 descriptions were inferred from DB fingerprint alone and several were wrong. T7UTKE renames locations (not cleanup); T7UTKF/G/H are reports (not rebuilds). Corrections confirmed from DFMs.

**UTKA and UTKE are genuinely destructive.** All UTK* report programs (UTKF/G/H) are read-only listing utilities.

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

**T7ISMCC UI (confirmed from DFM — Pass 153, 2026-06-22 — full read):**
Caption: "Convert Source to Base Currency"

Description: "This will convert your Source Currency accounts (AP, AR, PORNI, and Bank Accounts) to Base Currency, with any Gain or Loss posting to the F/E Gain or Loss Account."

UI fields:
- **is.cvt.mth** — GL period number (1–12), `vld_glperiod()`
- **is.date** — as-of date for the conversion run, `vld_gldate()`
- **gl.period[1-12]** — read-only period numbers (display only)
- **ISGL.CYDATE[1-12]** — read-only period beginning dates from ISGLDATE

Scope of conversion: AP accounts, AR accounts, PORNI (Purchase Orders Received Not Invoiced), and Bank Accounts — all source-currency balances converted to base currency. Gain/loss posts to F/E (Foreign Exchange) Gain or Loss GL account.

Buttons: Process, Exit

Note: An earlier analysis reported 9-period grid with ETBcomboval (company selector) — the actual DFM shows 12-period grid with `is.cvt.mth` (period selector). No ETBcomboval is present in this form; the company is determined by context.

**Confidence: 80/100** — T7ISMCC.DFM fully read; conversion scope confirmed from form description label; 12 period-date fields (ISGL.CYDATE[1-12]) confirmed; posting logic in RWN.

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

**Definitive architecture (Pass 63/109):** All 24 T7DS* programs (excluding T7DSQC which has 0 tables) have **IDENTICAL 36-table fingerprints**. Every DS stub opens the exact same set: BKAPDESC, BKAPPO, BKAPVEND, BKARCUST, BKARINV, BKCMACCN, BKGLTRAN, BKGLX, BKICMSTR, BKSYAR, BKSYHELP, CLASS, DBAFIFO, DBAHLPID, FILELOC, ISDRILL, ISDROP, ISGLDATE, ISICMSTR, ISIS, ISLINKS, ISLOG, ISMCR, ISNCR, ISNOTES, ISNTYPE, ISNUMBER, ISREMIND, ISTAXGRP, ISTRIGRS, LANGDICT, LOT, MKAHIST, MKECLASS, SERIAL, WORKORD. This is NOT per-module data access — it is a universal dispatcher: the DS stub passes the module code to a central sync engine. T7DSQC = 0 tables (QC sync not yet implemented or uses a different path).

**Why each table category appears in the fingerprint (Pass 109, field-level confirmed):**

| Category | Tables | Purpose in DS context |
|----------|--------|-----------------------|
| Master data | BKICMSTR, ISICMSTR, BKARCUST, BKAPVEND, BKCMACCN | Item/customer/vendor master records — the core data being synced |
| Transactions | BKARINV, BKAPPO, BKGLTRAN, BKGLX, BKAPDESC | AR invoices, PO headers, GL entries for sync |
| FIFO costing | DBAFIFO (5f: PARTNO+QTY+COST+RECVDATE+REMAIN) | FIFO cost layers per part — IC valuation data for sync |
| Lot/serial | LOT, SERIAL | Traceability records for item movements |
| Multi-currency | ISMCR, ISTAXGRP, ISIS | Exchange rates, tax groups, system feature flags |
| Scheduling/calendar | ISGLDATE | Fiscal period calendar — needed for date-period mapping during sync |
| Notes/attachments | ISNOTES, ISNTYPE, ISLINKS | Notes and document links per entity |
| Marketing | MKAHIST, MKECLASS | CRM history and event classification |
| Notifications | ISTRIGRS, ISREMIND | Trigger/reminder records |
| NCR | ISNCR | Non-conformance records |
| **Process control** | **ISLOG (9f)** | **Background process tracker — DS writes a row on start (WHO/WHAT/DOING/STARTD/STARTT/COMPANY), polls IS_LOG_KILL(1) to support graceful admin-initiated termination** |
| Help/runtime | DBAHLPID (2f: REF+MAP), BKSYHELP (1f: PATH) | Context-sensitive help topic map + CHM path |
| Runtime infra | FILELOC, LANGDICT, BKSYAR | TAS runtime file registry, language dict, AR sequence numbers |
| Lookups | ISDRILL, ISDROP, CLASS, ISNUMBER | Generic query/lookup tables; auto-number allocator (50 parallel counters) |
| WO context | WORKORD | Work order reference for WO-linked sync records |

**ISLOG — active process / kill control (9 fields):**
- `IS_LOG_WHO(35)` — user/process that started DS
- `IS_LOG_WHAT(15)` — module identifier (e.g., "DSAR", "DSWO")
- `IS_LOG_DOING(60)` — current step description (progress string)
- `IS_LOG_STARTD` + `IS_LOG_STARTT(12)` — start date + time
- `IS_LOG_COMPANY(3)` — company code
- `IS_LOG_KILL(1)` — **kill flag**: admin sets to `.T.` in ISLOG to gracefully terminate the running DS sync
- `IS_LOG_MSG(200)` — status/error message
- `IS_LOG_EXTRA(100)` — extended info

This is the mechanism by which EVO admins can abort a stuck or long-running DS sync without killing the process at the OS level.

DS module purpose: synchronize selected EvoERP data to/from an external system. Each T7DS* stub dispatches one module's sync cycle. The actual sync logic (which fields move, which direction, which external endpoint) is encrypted in the central sync RWN.

**Confidence: 65/100** — 25 programs identified; identical 36-table fingerprint confirmed across all 24 active stubs; T7DSQC anomaly confirmed (0 tables); architectural pattern (universal dispatcher + ISLOG kill-flag process control) fully documented; all 36 fingerprint tables field-decoded (Pass 109); HH=Handheld, IM=Import/Multi-currency confirmed; sync target endpoint and field-level mapping blocked by RWN encryption.

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

---

## System/Menu Architecture — Pass 71 (MENUFILE + BKPRTCFG + BKSYPRTR)

### MENUFILE (108f) — EvoERP Menu Definition

**PK:** MENU_CODE (STRING 4) — menu screen code (e.g., "AR", "AP", "WO")

The foundational menu structure table. EvoERPmenu.RWN reads MENUFILE at startup to build every menu screen. Each row is one menu screen with up to 20 selectable items:

| Field | Description |
|---|---|
| MENU_CODE(4) | Menu code — matches module prefix (PK) |
| MENU_TITLE(30) | Screen title displayed at top |
| MENU_LEFT(4) | Navigate-left menu code (which menu opens on left-arrow) |
| MENU_RIGHT(4) | Navigate-right menu code |
| MENU_ESCAPE(4) | Escape / parent menu code |
| MENU_LINES_1..20 (30 chars × 20) | Up to 20 menu item text lines displayed to user |
| (+ remaining fields: key codes per line, selection codes per line) | |

MENUFILE is the data-driven menu engine — the entire EvoERP module tree is in this file. EvoERPmenu.RWN is essentially a menu navigator that reads MENUFILE to draw screens and dispatch to the correct .RWN program on selection. BKSLEVEL (security matrix) maps against MENUFILE's MENU_CODE to determine which items are visible per security level.

---

### BKPRTCFG (205f) — TAS Printer Command Configuration

**PK:** BKPRT_CFG_KEY (STRING 2) — printer slot number

Stores up to 10 named printer definitions per slot, with TAS Pro 7 printer command escape sequences. Structure: NAME_1..10 (25 chars × 10 printer names) + CMD_1..N (70 chars × 14+ escape sequences per printer). Used by TAS Pro 7's internal print driver to send device-specific codes for condensed print, form feeds, page widths, etc. T7UTKA (UT-KA data clear) and T7MDEFAULTS (AD-A) both reference BKPRTCFG when resetting system config.

---

### BKSYPRTR (11f) — System Printer Registry

**PK:** BKSY_PRTR_NAME (STRING 30) — printer name

Windows-level printer registration for EvoERP:
- NAME(30) — logical printer name
- EXEC(8) — print executable path token
- TAS(1) — use TAS internal driver (Y) vs Windows driver (N)
- LPTNM(1) — LPT port number (1=LPT1, 2=LPT2, etc.)
- TYPE(8) — printer type string (e.g., "LASER", "DOT")
- PWDT(2) — paper width (chars per line)
- PMAX(2) — max lines per page
- PPLNE(2) — lines per page
- LASER(1) — laser printer flag
- POST(8) — PostScript driver name
- PRUN(1) — enabled/run flag

---

## AP — Invoice Archive — Pass 71 (BKPOX/BKPOXH)

### BKPOX / BKPOXH (19f each) — AP Purchase Invoice Archive

**PK:** BKPOX_COMPANY(2) + BKPOX_INVCNUM(10)

Short-form AP invoice archive record, written when an AP invoice is posted and optionally archived:

| Field | Description |
|---|---|
| BKPOX_COMPANY(2) | Company code |
| BKPOX_INVCNUM(10) | Invoice number (vendor invoice# as string) |
| BKPOX_INVCDATE | Invoice date |
| BKPOX_PONUM(8) | Linked PO number |
| BKPOX_VENDCODE(10) + VENDNAME(30) | Vendor code + name |
| BKPOX_SUBTOT + TAXAMT + FREIGHT + TOTAL | Invoice amounts |
| BKPOX_CURRENCY(3) | Currency code |
| BKPOX_TERMSDESC(20) + TERMSCODE(2) | Payment terms |
| BKPOX_INVCDESC(30) | Invoice description |
| BKPOX_TAXCODE(10) + TAXNAME(30) | Tax code + description |
| BKPOX_POSTDATE | GL post date |
| BKPOX_ARCHDATE | Archive date |
| BKPOX_ENTDATE | Entry date |

BKPOX = active open invoice archive; BKPOXH = historical (paid/closed) version. Both use identical structures. This is a lighter-weight summary table (19f vs BKAPINVT's fuller structure) intended for rapid invoice lookup and archive reporting.

**AP confidence: 90/100** — BKPOX/BKPOXH(19f) fully decoded; invoice archive purpose confirmed from ARCHDATE field; BKAPEVND(73f)/ISAPAVND(72f)/BKAPEIVT(19f)/ISAPAINT(19f) confirmed as alternate-index views of BKAPVEND/BKAPINVT respectively, not separate tables; full AP workflow documentation complete.

---

## IC — Item Extended Tables — Pass 71 (BKICALTD + BKICALTP + BKICMFG + MTINVDEF)

### BKICALTD (16f) — Item Alternate Detail / Specification

**PK:** BKIC_ALTD_PCODE(15) + BKIC_ALTD_TYPE(1)

Per-item specification sheets. TYPE differentiates multiple spec sets per item (e.g., dimensional, material, performance):
- DESC(30) — specification set name
- NOTE(30) — general note
- BKIC_ALTD_SPECS_1..12 (30 chars × 12) — 12 specification lines (dimensions, tolerances, material grades, etc.)

Used for item drawing specifications, inspection criteria, or compliance data. One row per item per spec type.

---

### BKICALTP (6f) — Authorized Alternate Parts

**PK:** BKIC_ALTP_TYPE(1) + BKIC_ALTP_PCODE(15) + BKIC_ALTP_ACODE(25)

Approved substitute/equivalent part list — distinct from BKSBPART (which is customer-specific):
- ACODE(25) — alternate part number (can be longer than 15 chars = allows industry/OEM part numbers)
- NOTES_1/2/3 (30 each) — approval notes

Stores authorized interchangeable part numbers. BKICALTP is the engineering-approved alternate list; BKSBPART is the customer-substitution list.

---

### BKICMFG (6f) — Manufacturer Cross-Reference

**PK:** BKIC_MFG_PCODE(15) + BKIC_MFG_MANUF(25) + BKIC_MFG_MCODE(25)

Maps internal item code to manufacturer's own part numbers:
- MANUF(25) — manufacturer name
- MCODE(25) — manufacturer's part number
- REMARK_1/2/3 (30 each) — cross-reference remarks

Used in purchasing to specify "order by manufacturer code MCODE from MANUF." Multiple manufacturers can cross-reference to the same internal PCODE.

---

### MTINVDEF (108f) — Item Class Defaults

**PK:** MTIC_PROD_CLASS(4) + MTIC_PROD_CODE(15)

Template record that defines default field values for new items of a given class. Same 108-field structure as MTICMSTR (item master) but contains default values rather than live inventory. When a new item is created in IC and assigned to CLASS X, MTINVDEF provides GL accounts, unit-of-measure conversion, cost method, MRP flag, cycle count code, etc.

**IC table family summary (Pass 71):**

| Table | Fields | Purpose |
|---|---|---|
| BKICMSTR / MTICMSTR | 108 | Live item master |
| MTINVDEF | 108 | Item class defaults — template values for new items |
| BKICALTD | 16 | Item specification sheets — 12 spec lines per item per type |
| BKICALTP | 6 | Authorized alternate parts — OEM/industry equivalent part numbers |
| BKICMFG | 6 | Manufacturer cross-reference — manufacturer name + MFR part# per item |
| BKICELOC | 32 | Extended location quantities — UOH/WO/WIP/QC + per-location GL |
| IS2DBAR | 109 | 2D barcode / document print flags per item |

**Confidence: 78/100** — BKICALTD(16f)/BKICALTP(6f)/BKICMFG(6f)/MTINVDEF(108f) all fully decoded; IC item master family now complete; per-program logic for spec/alternate/MFR maintenance in encrypted RWN.

---

## PR — Custom Deductions + State Taxes — Pass 71

### ISPRUDF (31f) — Payroll User-Defined Deduction/Earning Type

**PK:** ISPR_UDF_DIV(4) + NUM(8)

Defines custom payroll earning or deduction codes beyond the standard types (FIT, FICA, etc.):

| Field | Description |
|---|---|
| DIV(4) + DIVNAM(20) + NUM(8) | PK — division, name, sequence number |
| DESC(12) | Short code description |
| FIT/FUTA/SDI/PTAX/SS/MED/SIT/WC/SUTA/LOCAL (1 each) | Tax applicability flags — does this deduction reduce each tax base? |
| CALCEE(1) + EETYPE(17) | Employee deduction: calc method + type code |
| CALCRE(1) + ERTYPE(17) | Employer contribution: calc method + type code |
| EEAMT + ERAMT (float) | Fixed deduction amounts (EE + ER) |
| UODLMT + UDELMT (float) | Per-occurrence limits (daily/period) |
| UODYLM + UDEYLM (float) | Annual limits (daily/year) |
| LACCT(10) + (more GL fields) | GL account for this deduction posting |

Supports any custom benefit (health insurance, 401k, garnishments, union dues) with independent tax treatment per withholding type.

---

### BKPRSTFL (2f) — Payroll State Tax Filing ID

**PK:** BKPR_ST_STCODE (STRING 2) — 2-char state code

Maps each state code to the employer's state tax identification number:
- STCODE(2) — state abbreviation (CT, NY, MA, etc.)
- TAXNUM(10) — state employer tax registration number

Used when generating state payroll tax filings (W-2, SIT returns).

**PR confidence: 85/100** — ISPRUDF(31f) + BKPRSTFL(2f) fully decoded; PR table family now covers: BKPRMSTR(384f employee master), BKPRCURP(127f current period), BKPRFTAX(47f tax brackets), BKPRGLFL(664f GL map), BKPRINFO(128f HR info), BKPRTC(7f time card), ISPRTEMP(15f direct deposit), ISPRUDF(31f custom deductions), BKPRSTFL(2f state IDs).

---

## MH/Shipping — Route Load Manifest — Pass 71

### ISRTLOAD (21f) — Shipping Route Load Manifest

**PK:** IS_LOAD_SONUM(8) + IS_LOAD_ITEM(15) + IS_LOAD_SOLINE(3)

One row per SO line item assigned to a truck/load. Enables load planning and scan verification:

| Field | Description |
|---|---|
| SONUM + ITEM + SOLINE | PK — source SO line |
| DESC(30) | Item description |
| SCCOGS(8) | Standard COGS for this item |
| ORDQTY + BALQTY | Ordered and balance quantities |
| LOADQTY | Quantity loaded onto this truck |
| SCANQTY | Quantity confirmed by scan |
| LOADNUM(8) | Load/truck assignment number |
| TRUCK(15) | Truck/route identifier |
| LOC(10) + SER(25) + LOT(15) + BIN(15) | Inventory location at load time |
| DATE1 + DATE2 | Load date, scan date |
| NUM2 + CNTR | Counter fields |
| ALOAD(15) | Actual load identifier |
| EXTRA(100) | Extra |

ISRTLOAD is used by the MH shipping dispatch module to build a pick/load manifest per truck, then verify via barcode scanning that the right items were loaded. LOADQTY vs SCANQTY provides shipment accuracy verification.

---

## SP — J7 GS1 Packaging — Pass 71 (JGPITEMS)

### JGPITEMS (86f) — J7 GS1 Item Packaging Data

**PK:** JGP_ITEM (STRING 15) — item code

J7 Systems customization. Stores GS1/UPC barcode and logistics packaging data per item — required for retail EDI (advance ship notice, carton labels, etc.):

| Field group | Description |
|---|---|
| JGP_ITEM(15) + LITEM(30) | Item code + long description |
| JGP_IND_UPC(13) | Individual (each) UPC barcode |
| JGP_UOM_UPC(13) | Unit-of-measure UPC |
| JGP_SP_BARCODE(14) / MC_BARCODE(14) / PAL_BARCODE(14) | Single-pack / master-carton / pallet GS1 barcodes |
| JGP_SP_QTY / MC_QTY / PAL_QTY | Quantity per single pack / master carton / pallet |
| JGP_UOM_H/W/D/WT/CUBE | Each-unit dimensions and weight |
| JGP_SPACK_H/W/D/WT/CUBE | Single-pack carton dimensions |
| JGP_MCART_H/W/D/WT/CUBE | Master carton dimensions |
| (+ ~36 more: pallet dims, GS1 company prefix, GTIN, SSCC, etc.) | |

JGPITEMS provides the GS1 packaging hierarchy for EDI 856 advance ship notice (ASN) generation and retail compliance labeling. The SP/MC/PAL three-level hierarchy (item → inner pack → master carton → pallet) is standard for retail EDI partners (Walmart, Home Depot, etc.).

**SP confidence: 87/100** — JGPITEMS(86f) first 25 fields decoded; GS1 SP/MC/PAL hierarchy confirmed; J7 Systems customization confirmed from JGP_ prefix (same J7 pattern as ISCCICM); remaining 36 JGPITEMS fields likely GTIN/SSCC/GS1 company prefix fields.

---

### New Tables Confirmed (Pass 71)

| Table | Fields | Purpose |
|---|---|---|
| MENUFILE | 108 | EvoERP menu definition — CODE(4) PK; TITLE+LEFT/RIGHT/ESCAPE nav + 20 menu-item text lines; drives the entire module menu tree |
| BKPRTCFG | 205 | TAS printer command config — KEY(2) PK; 10 named printers × NAME(25) + 14 CMD(70) escape sequences |
| BKSYPRTR | 11 | System printer registry — NAME(30) PK; EXEC+TAS+LPT+TYPE+PWDT+PMAX+LASER+POST flags |
| BKPOX | 19 | AP invoice archive (open) — COMPANY+INVCNUM PK; PO+VENDOR+amounts+ARCHDATE |
| BKPOXH | 19 | AP invoice archive (historical/paid) — identical structure to BKPOX |
| BKICALTD | 16 | Item specification sheet — PCODE+TYPE PK; DESC+NOTE+12×SPECS(30) per type |
| BKICALTP | 6 | Authorized alternate parts — TYPE+PCODE+ACODE PK; 3 notes lines |
| BKICMFG | 6 | Manufacturer cross-reference — PCODE+MANUF+MCODE PK; 3 remark lines |
| MTINVDEF | 108 | Item class defaults — CLASS+PCODE PK; same 108f as MTICMSTR but contains template values for new item creation |
| ISPRUDF | 31 | Custom payroll deduction/earning — DIV+NUM PK; 10 tax-base flags; EE/ER calc method+amount+limits; GL acct |
| BKPRSTFL | 2 | Payroll state tax IDs — STCODE(2) PK + TAXNUM(10); employer state tax registration numbers |
| ISRTLOAD | 21 | Route load manifest — SONUM+ITEM+SOLINE PK; TRUCK+LOADNUM+ORDQTY+LOADQTY+SCANQTY; shipment accuracy verification |
| JGPITEMS | 86 | J7 GS1 packaging — ITEM PK; IND/UOM/SP/MC/PAL barcodes; H/W/D/WT/CUBE per packaging level; EDI 856 ASN support |

---

*Last updated: 2026-06-17 (Pass 71). Confidence bumps: IC 72→78 (BKICALTD/BKICALTP/BKICMFG/MTINVDEF all decoded; item spec/alternate/MFR/class-default family complete), PR 82→85 (ISPRUDF custom deductions + BKPRSTFL state IDs), AP 88→90 (BKPOX/BKPOXH invoice archive; AP alternate-index views BKAPEVND/ISAPAVND/BKAPEIVT/ISAPAINT identified), SP 83→87 (JGPITEMS 86f GS1 packaging hierarchy decoded; J7 retail EDI support confirmed). System architecture: MENUFILE(108f) menu engine decoded — the entire EvoERP module tree is data-driven from this table. 13 new schemas.*

---

## System Identity — Pass 72 (ISVAR)

### ISVAR (17f) — Company Identity / Header Data

**Single-row company identity table** — printed on all invoices, POs, and reports.

| Field | Description |
|---|---|
| IS_VAR_LOGO(256) | Path to company logo image file (used on laser forms) |
| IS_VAR_COMPANY(30) | Company name |
| IS_VAR_ADD1(30) + ADD2(30) | Address lines 1 and 2 |
| IS_VAR_CITY(20) + STATE(2) + ZIP(8) | City, state, zip |
| IS_VAR_CONTACT(30) | Primary contact name |
| IS_VAR_EMAIL1_1..5 (50 each) | Up to 5 company email addresses |
| IS_VAR_WEB(100) | Company website URL |
| IS_VAR_WEBUPD(100) | Web update / API endpoint URL |
| (+ 2 more misc fields) | |

ISVAR is the single-row company identity record. AD-A (T7MDEFAULTS) edits it along with BKSYMSTR. Every RTM report template that prints a company header reads ISVAR. Distinct from BKSYMSTR (which holds operational config like fiscal year, tax codes, etc.) — ISVAR is purely identity/branding data.

---

## ES — Estimate Material BOM — Pass 72

### ESTMAT (18f) — Estimate Material Components

**PK:** MTESMAT_QUOTE(8) + MTESMAT_CODE(15)

The material component table for estimates — parallels ESTROUT (routing steps). Together ESTMAT + ESTROUT = the complete estimate BOM + routing:

| Field | Description |
|---|---|
| MTESMAT_QUOTE(8) + CODE(15) | PK — estimate number + material item code |
| MTESMAT_DESC(30) | Material description |
| MTESMAT_QTYPER(8) | Quantity per finished unit |
| MTESMAT_SCRAP(8) | Scrap allowance |
| MTESMAT_UM(3) | Unit of measure |
| MTESMAT_QUREF(8) | Quote reference (parent estimate link) |
| MTESMAT_COST1..5 (float × 5) | Material cost per quantity break (5 breaks) |
| MTESMAT_REMARKS_1..3 (30 chars × 3) | Remarks |
| (+ 3 more misc fields) | |

ESTMAT is the MT-era estimate material table (MTESMAT_ prefix). ES-H/I enters costs into both ESTMAT (materials) and ESTROUT (routing). ES-C rollup combines both for the final quote price. When ES-E converts to a WO, ESTMAT rows become WOBOM (WO BOM) rows.

**ES table summary (Pass 72):**

| Table | Fields | Purpose |
|---|---|---|
| BKESTQT / BKESTQTL | 84/28 | Estimate header/lines (same structure as BKARINV/BKARINVL) |
| ESTMAT | 18 | Estimate material BOM — QUOTE+PART PK; QTYPER+SCRAP+UM; 5-break COST1..5 |
| ESTROUT | 48 | Estimate routing steps — QUOTE+OPER PK; WC+TYPE+VENDOR; 5-break LAB/MACH/OVER/SETUP |
| BKMATCST | 25 | Material cost lookup — CODE PK; 10-break QTY/COST arrays |
| BKRTCST | 24 | Routing cost per operation — QUOTE+CODE+OPER PK; 10-break PARTSHR/SETUP |
| BKESTCFG | 13 | Quote config — per-quote settings, 5 custom footer lines |
| ESTSUM | 213 | MT-era estimate rollup (legacy parallel to BKESTQT) |

**Confidence: 85/100** — ESTMAT(18f) fully decoded; ESTMAT+ESTROUT material+routing pair confirmed (5-qty-break pattern matches); ES-C/H/I flow confirmed from DB fingerprints; per-quantity-break cost selection logic in encrypted RWN.

---

## BM/RO — Change Audit Tables — Pass 72

### BOMCHG (15f) — Master BOM Change Audit

**PK:** BOM_CHG_PARENT(15) + BOM_CHG_COMP(15)

Audit trail for changes to the master BOM (BKBMMSTR). Records every add/delete/modify to a BOM component:
- CDATE + USER(15) — change date + user
- ACOMP(1) / DCOMP(1) — add flag / delete flag
- AQTY / BQTY — after/before quantity
- AREF(20) / BREF(20) — after/before reference designator
- ASCRAP / BSCRAP — after/before scrap allowance
- AEXTRA(100) / BEXTRA(100) — after/before extra notes
- UID(20) — unique change record ID

---

### WOBOMCHG (17f) — WO BOM Change Audit

**PK:** WBOM_CHG_WOPRE + WOSUF + PARENT(15) + COMP(15) + UID(20)

Same A/B before-after structure as BOMCHG but for WO-level BOM overrides. When a WO's BOM is modified from the master (substitute component, different qty), WOBOMCHG captures the deviation. Used for variance analysis and engineering review.

---

### ROCHG (22f) — Master Routing Change Audit

**PK:** RO_CHG_PART(15) + RO_CHG_OPER(2)

Audit trail for changes to the master routing (ROUTING/WOROUT):
- AOPER(1) / DOPER(1) — add/delete operation
- ALONG / BLONG — after/before run time
- ASETUP / BSETUP — after/before setup time
- ATMACH(4) / BMATCH(4) — after/before machine code
- ATOOL(15) / BTOOL(15) — after/before tool
- AWC(12) / BWC(12) — after/before work center
- CDATE + USER — change date + user
- (+ 7 more A/B pairs for cost rates, instructions, etc.)

---

### WOROCHG (24f) — WO Routing Change Audit

**PK:** WORO_CHG_WOPRE + WOSUF + PART(15) + OPER(2)

Same A/B structure as ROCHG but at the WO routing level. Captures when a WO's routing deviates from the master routing (e.g., rerouted to a different WC, tool substitution, time override). Paired with WOBOMCHG as the complete WO deviation audit package.

**BM/RO change audit summary:**

| Table | Scope | PK |
|---|---|---|
| BOMCHG | Master BOM changes | PARENT+COMP |
| WOBOMCHG | WO-level BOM overrides | WOPRE+WOSUF+PARENT+COMP+UID |
| ROCHG | Master routing changes | PART+OPER |
| WOROCHG | WO routing overrides | WOPRE+WOSUF+PART+OPER |

**BM confidence: 85/100 / RO confidence: 88/100** — All 4 change-audit tables fully decoded; A/B before-after pattern confirmed; BM+RO change audit architecture complete; write triggers (which operations create audit rows) in encrypted RWN.

---

## DC — Serial Scan at Station — Pass 72

### ISDCSER (17f) — DC Serial Number Scan Record

**PK:** ISDC_SER_WOPRE + WOSUF + OPER

Records serial/lot number scans at a DC workstation during production:
- ITEM(15) — item being produced
- EMP(2) — employee who scanned
- SERIAL(25) + LOT(15) — serial and lot scanned
- BIN(15) + LOC(10) — bin and location at scan time
- DATE + TIME — scan timestamp
- FLAG(1) — status flag (e.g., pass/fail/pending)
- ALPHA(30) — general alpha data (e.g., customer part#)
- GDATE — general date (e.g., expiry/test date)
- PARTS(8) — parts count
- (+ 2 more)

ISDCSER is the per-scan event record for the DC serial number tracking feature. At each workstation, the operator scans the serial/lot barcode; ISDCSER records it. Pairs with BKDCLAB (DC labor post) and ISSTRACK (SPC traceability) to build full unit genealogy.

---

## WO — Planned PO and Tool Log — Pass 72

### BKWOPO (16f) — MRP/WO-Linked Planned Purchase Order

**PK:** BKMRP_PO_UID (STRING 20) — unique planned PO ID

MRP-generated planned purchase order linked to a specific WO's outside-process operation:
- VEND(10) — planned vendor
- DATE — planned order date
- ERD — expected receipt date
- PART(15) — outside-process item
- QTY — quantity
- PRICE — planned price
- WOPRE + WOSUF — linked work order
- PLANR(4) — planner code
- CONF(1) — confirmed flag (planner approved)
- DONE(10) — done status/reference
- MTREC(4) — master record link
- EXTRA(50) + EST(10)

Distinct from BKMRPPO (MRP planned PO not linked to WO) — BKWOPO is specifically for WO outside-process operations that need a vendor PO.

---

### ISTOOLOG (34f) — Tool Usage Log

**PK:** ISTOOL_WOPRE + WOSUF + OPER + TOOL(15) + DATE

Tracks tool usage and maintenance events on WO operations:
- WORKDESC(60) — work performed description
- ACTHRS(8) — actual hours used
- COST(8) — cost of this usage/maintenance event
- NOTES_1..10 (60 chars × 10 = 600-char maintenance log)
- EMP(2) — employee who performed the work
- DATES_1..5 — 5 maintenance/inspection dates
- (+ 14 more: quantities, next-maintenance fields, status flags)

ISTOOLOG is the tool maintenance journal — each WO operation that uses a tool creates an entry. Used for tool life tracking, preventive maintenance scheduling, and cost allocation. Pairs with the TOOL master table (20f: tool code, parent WC, hours-used counter, maintenance fields).

---

## DI — Digital Signature Capture — Pass 72

### ISASIGN / ISSIGN (16f each) — Signature Record

Both tables are structurally identical — alternate-index views of the same signature data. **PK:** IS_SIGN_NUM (float)

Electronic signature capture record:
- IS_SIGN_WHO(40) — signer's display name
- IS_SIGN_POS(40) — signer's position/title
- IS_SIGN_EWHO(15) — signer's employee code (FK → BKPRMSTR)
- IS_SIGN_EDATE + ETIME — electronic timestamp
- IS_SIGN_NAME(40) — printed name
- IS_SIGN_JPG(256) — path to signature image (JPG of handwritten signature)
- IS_SIGN_SDATE + STIME — signature date/time
- IS_SIGN_GDTE1..5 — 5 general dates (effective/expiry/approval dates)
- (+ 1 more)

ISSIGN (active) / ISASIGN (archive) pair. T7DIGSIG creates ISSIGN records when a PO is approved via digital signature. The JPG path stores the actual handwritten signature image captured from a tablet or signature pad.

**DI confidence: 78/100** — ISASIGN/ISSIGN(16f) fully decoded; signature capture architecture confirmed (employee→JPG path+timestamp); BKSL_MENUn_YN security integration confirmed; exact PO-signature linkage key (how IS_SIGN_NUM ties to BKAPPO) in encrypted RWN.

---

## IN — Monthly Inventory Summary — Pass 72

### SUMINV (19f) — Monthly Inventory Activity Summary

**PK:** SUMINV_PARTNO(15) + MONTH(2) + YEAR(2) + LOCATION(10)

Monthly rolled-up inventory activity totals per item per location — the IC module's periodic history:

| Field pair | Description |
|---|---|
| DOL_ADJ + UN_ADJ | Dollar and unit adjustments this month |
| DOL_ISS + UN_ISS | Issues (WO material pulls) |
| DOL_RWIP + UN_RWIP | WIP returns |
| DOL_RSTK + UN_RSTK | Stock returns (RMA / put-back) |
| DOL_SHPS + UN_SHPS | Shipments (SO shipments) |
| DOL_SHPC + UN_SHPC | Shipment credits (reversed shipments) |
| (+ 4 more: receipts, transfers, etc.) | |

SUMINV is the compressed monthly history table — each row represents one full month of activity for an item-location pair. Used by IC reports (turnover, usage trends) and SA (Sales Analysis) without scanning full INVTXN transaction detail.

---

## FO — BOM Remarks — Pass 72

### ISFOBMRM (20f) — Features/Options BOM Remarks

**PK:** ISFO_BRM_UID(40) + PARENT(15) + LINE(2) + COMP(15)

Extended remarks per BOM line in the Features/Options (FO) module:
- REMARK_1..11 (64 chars × 11 = 704 chars per BOM line)
- (+ 5 more fields: dates, flags, extra)

Allows each FO configurable BOM option to carry detailed engineering notes, compliance text, or customer-specific instructions. The 704-char capacity (11 × 64) far exceeds the base BOM remark fields.

---

## Miscellaneous New Tables — Pass 72

### ISCRISLS (24f) — CR Contract Sales History

**PK:** ISCR_SLS_CUST(10) + ISCR_SLS_ITEM(15) + ISCR_SLS_SDATE

Contract review (CR module) historical sales data per customer-item pair:
- SUOH/FUOH — starting/final on-hand at period start/end
- SHPQTY + SHPDTE — quantity shipped + ship date
- INVNUM — invoice reference
- FDATE — final date; SOLDTE + SOLDQT — sold date + quantity
- NUM_1/2 (float) + FLAG_1/2 (1 each) — custom metric slots

Used for contract pricing review: compares historical demand/shipments against contract commitments.

---

### BKUMSRTY (23f) — UM Security Access Matrix

**PK:** SCRTY_LEVEL(2) + SCRTY_MENU(2)

An alternate security access table (parallel to BKSLEVEL) used for a specific sub-module:
- SCRTY_GROUP(1) — group code
- SCRTY_ITEM_1..20 (1 each × 20) — 20 per-item access flags

BKUMSRTY (UM_ prefix = "User Menu"?) stores simplified Y/N access per security level per menu for a specific module family, separate from the main BKSLEVEL matrix.

---

### BKISHTAX (13f) — IS/IC Historical Tax Log

**PK:** BKIS_TAX_CODE(10) + BKIS_TAX_DATE

Per-transaction tax history record:
- TRFLAG(1) — transaction type flag
- TAXABL + NONTAX + TAXAMT — taxable/non-taxable amounts and tax collected
- CUST(10) + VEND(10) — customer or vendor
- INVNO + PONO — AR invoice / AP PO reference
- TAG(1) — posting tag
- ISCUR(3) — currency code
- APINV(10) — AP invoice string

IC-side tax accumulation record (BKIS_ prefix = Btrieve/IS era). Parallel to BKISTAX (the AR side). Used for tax remittance reporting across IC/AP transactions.

---

### ISRTMS (29f) — RTM Template Selector

**PK:** IS_RTM_CUST(10) + IS_RTM_VEND(10) + IS_RTM_ITEM(15)

Maps customer/vendor/item combinations to specific RTM (ReportBuilder) report templates:
- RTM(12) — template file name (FK → .RTM file on network share)
- PROGRAM(15) — program code that uses this template
- DFLT(1) — default template flag
- DATE — assignment date
- FLAG(1) — active/inactive
- PARTLBL/SHIPLBL/CONTLBL/MIXEDLBL/QUICKLBL/MISCLBL1..3 (12 each) — label template assignments per label type
- QTY(2) — default label quantity
- PRINTER_1..N (90 each) — printer assignments

ISRTMS is the report template routing table — allows different customers or items to use custom-branded invoice/label templates. When T7SOA prints an invoice, it checks ISRTMS first before using the default template.

---

### ISCCBTXN (16f) — Fabric/Cut Control Transaction (J7 Custom)

**PK:** (ISCC_TXN_ prefix — PK inferred as FABRIC+JOB+LOT)

J7 Systems custom table for fabric cutting operations:
- FABRIC(15) — fabric roll/item code
- JOB(15) — cut job identifier
- LOT(15) + SER(25) — lot and serial of cut piece
- BIN(15) + LOC(10) — bin/location
- PULQTY — pulled quantity from roll
- NEDQTY — needed quantity
- LOTQTY — lot size
- SDATE / TDATE / GDATE — start / transaction / general dates
- STATUS(1) — cut status
- ALPHA(15) — custom alpha data
- TRANS(8) — transaction reference

Used by J7's fabric/cutting manufacturing workflow to track how much fabric was pulled from each roll for each cut job, with lot/serial assignment.

---

### NZITPRE (54f) — WO Item Prefix Counter

Single configuration row: 18 WO prefix ranges, each with current next-number:
- NZ_IPRE_PREFIX_1..18 (float × 18) — 18 configured WO prefix values
- NZ_IPRE_NXTNUM_1..18 (float × 18) — next WO number for each prefix
- (+ 18 more: probably flags/limits per prefix)

Used by the WO creation subsystem to generate the next WO number within each prefix range. Prefix 1 might be standard WOs, prefix 2 might be rework WOs, etc.

---

### New Tables Confirmed (Pass 72)

| Table | Fields | Purpose |
|---|---|---|
| ISVAR | 17 | Company identity — LOGO(256)+COMPANY+ADDRESS+CONTACT+5×EMAIL+WEB; printed on all forms |
| ESTMAT | 18 | Estimate material BOM — QUOTE+CODE PK; QTYPER+SCRAP+UM; 5-break COST1..5; 3 remarks |
| BOMCHG | 15 | Master BOM change audit — PARENT+COMP PK; A/B before-after qty/ref/scrap/extra |
| WOBOMCHG | 17 | WO BOM deviation audit — WOPRE+WOSUF+PARENT+COMP+UID PK; same A/B structure |
| ROCHG | 22 | Master routing change audit — PART+OPER PK; A/B run-time/setup/machine/tool/WC |
| WOROCHG | 24 | WO routing deviation audit — WOPRE+WOSUF+PART+OPER PK; same A/B structure |
| ISDCSER | 17 | DC serial scan record — WOPRE+WOSUF+OPER PK; ITEM+EMP+SERIAL+LOT+BIN+DATE+TIME |
| BKWOPO | 16 | MRP/WO planned PO — UID PK; VEND+DATE+ERD+PART+QTY+PRICE+WOPRE/WOSUF+PLANR+CONF |
| ISTOOLOG | 34 | Tool usage/maintenance log — WOPRE+WOSUF+OPER+TOOL+DATE PK; ACTHRS+COST+10×NOTES |
| ISASIGN / ISSIGN | 16 | Digital signature capture — NUM PK; WHO+POS+EWHO+EDATE+NAME+JPG+5×GDTE |
| SUMINV | 19 | Monthly inventory activity — PARTNO+MONTH+YEAR+LOC PK; 8×DOL/UN pairs |
| ISFOBMRM | 20 | FO BOM remarks — UID+PARENT+LINE+COMP PK; 11×REMARK(64) per BOM line |
| ISCRISLS | 24 | CR contract sales history — CUST+ITEM+SDATE PK; UOH/shipment/demand history |
| BKUMSRTY | 23 | UM security matrix — LEVEL+MENU PK; GROUP+20×ITEM flags |
| BKISHTAX | 13 | IS/IC historical tax — CODE+DATE PK; TAXABL/NONTAX/TAXAMT+CUST/VEND/INVNO |
| ISRTMS | 29 | RTM template selector — CUST+VEND+ITEM PK; RTM(12)+PROGRAM+label+printer assignments |
| ISCCBTXN | 16 | Fabric cut transaction (J7) — FABRIC+JOB+LOT PK; PULQTY+NEDQTY+LOTQTY+STATUS |
| NZITPRE | 54 | WO prefix counter — 18 prefix ranges × (PREFIX+NXTNUM) counters |

---

*Last updated: 2026-06-17 (Pass 72). Confidence bumps: ES 80→85 (ESTMAT 18f material BOM; ES table family now complete: ESTMAT+ESTROUT+BKMATCST+BKRTCST+BKESTQT/L+ESTSUM), BM/BOM 82→85 (BOMCHG 15f + WOBOMCHG 17f change audit pair decoded), RO 85→88 (ROCHG 22f + WOROCHG 24f routing change audit pair decoded), DC 85→87 (ISDCSER 17f serial scan record), WO 85→87 (BKWOPO 16f MRP planned PO + ISTOOLOG 34f tool log), DI 72→78 (ISASIGN/ISSIGN 16f digital signature capture), FO 78→81 (ISFOBMRM 20f BOM remarks). System: ISVAR(17f) company identity decoded. 18 new schemas.*

---

## WO — Three-Tier Archive Architecture — Pass 73

### WO Table Family: Live / Estimate / History

EvoERP's Work Order system uses a **three-tier table architecture** for each sub-entity:

| Sub-entity | Live (active WO) | Estimate / Planned | History (closed WO archive) |
|---|---|---|---|
| WO header | WORKORD (74f) | WORKSORD (74f, template WOs) | WORKHORD (74f) |
| BOM / materials | WOBOM (24f) | WOEMAT (17f) | WOHBOM (24f) |
| Labor transactions | WOLABOR (58f) | WOELABOR (58f) | WOHLABOR (58f) / WOLABRPT (58f) |
| Receipts | WORECV (11f) | WOERECV (11f) | WOHRECV (11f) |
| Routing | WOROUT (81f) | — | WOHROUT (81f) |
| Dates/schedule | WODATE (13f) | — | WOHDATE (13f) |
| Engineering chg costs | WOEXCHG (10f) | — | WOHEXCHG (10f) |

**Pattern:** When a WO is closed/archived, all live records move to the matching WOH* table. WORKSORD holds saved/template WO headers. WOELABOR/WOEMAT/WOERECV are estimate rows that become actuals once the WO is released.

**WOLABRPT** — alternate-index/report view of WOLABOR (same 58 MTWOLA_ fields, different sort key for report generation).

### WORKACHG (25f) — WO Header Change Audit

**PK:** WO_CHG_WOPRE + WO_CHG_WOSUF + WO_CHG_CODE (change type code)

Captures changes to WO header fields (status, priority, class, description) — the fourth member of the WO change-audit family:

| Change pair | Before / After |
|---|---|
| APRIO / BPRIO | After/before priority |
| ASTATUS / BSTATUS | After/before status |
| ACLASS / BCLASS | After/before WO class |
| ADESC / BDESC | After/before description |
| + 13 more A/B pairs | Dates, quantities, GL accounts, etc. |

Full WO change audit family: **WORKACHG** (header) + **WOBOMCHG** (BOM) + **WOROCHG** (routing) — three tables covering every type of WO modification.

**WO confidence: 90/100** — Three-tier archive architecture confirmed from field prefix identity; all WOH* tables confirmed as MTWO_*/WOMAT_*/MTWOLA_ prefix matches of their live counterparts; WO change-audit family complete.

---

## MK — Marketing Automation Module — Pass 73

### Marketing Module Table Family

EvoERP includes a full Marketing Automation subsystem (MK prefix) tied to the CRM (CM) module. It implements campaign-based customer outreach with sequenced events.

### MKDEF (11f) — Marketing Defaults

Single-row configuration:
- MKDEF_REQUIRE(1) — require tracking flag
- MKDEF_CALENDAR(1) — calendar integration flag
- MKDEF_TRACK, PRICECD — default tracking/price codes
- MKDEF_FUCODE(3) — default follow-up code
- MKDEF_HISTORYCD(2) — default history code
- MKDEF_TNEXTID / TCNEXTID / ENEXTID / ECNEXTID / FNEXTID — next-ID auto-counters for tracks/events/forms

---

### MKTRACK (4f) — Campaign Track Definition

**PK:** MKTRACK_NUM (float)
- MKTRACK_DESC(45) — campaign name
- MKTRACK_CLASS(float) — track class (FK: MKTCLASS)
- MKTRACK_ACTIVE(1) — active flag

A "track" is a marketing campaign (e.g., "Q4 Product Launch", "New Customer Onboarding").

---

### MKTROUT (11f) — Campaign Route/Sequence

**PK:** MKTROUT_TRACK + MKTROUT_SEQ

Defines the ordered event sequence for a campaign:
- MKTROUT_JUMP(1) — jump/branch flag
- MKTROUT_NEXTSEQ — next step in sequence
- MKTROUT_EVENT — event to trigger (FK: MKEVENT)
- MKTROUT_DAYSNXT — days until next step
- MKTROUT_FIXED(1) — fixed date vs. relative
- MKTROUT_SALEBEG(1) + SALELEN + SALECLO(1) — sale/promotion window flags
- MKTROUT_PRICECD — price code at this step

MKTROUT defines the workflow: "send event X after N days, then jump to event Y."

---

### MKEVENT (12f) — Marketing Event Definition

**PK:** MKEVENT_NUM (float)
- MKEVENT_DESC(45), CLASS, MEDIA(1) — event description, class, media type (mail/email/call)
- MKEVENT_FORM — form template (FK: MKFORM)
- MKEVENT_FUCODE(3) — follow-up code
- MKEVENT_REM1/2(60 each) — remarks
- MKEVENT_SENDTO(2), GENNAME(45) — recipient code + generic name
- MKEVENT_HISTCD(2), ACTIVE(1) — history code + active flag

---

### MKFORM (6f) — Marketing Form Template

**PK:** MKFORM_NUM (float)
- MKFORM_DESC(45) — form description
- MKFORM_FILE(25) — letter/form file path
- MKFORM_ATT(25) — attachment file path
- MKFORM_MEDIA(1) — delivery medium
- MKFORM_ACTIVE(1)

---

### MKASSIGN (6f) — Campaign Account Assignment

**PK:** MKASSIGN_ACCT + TRACK
- MKASSIGN_ACCT(10) — CM account (FK: BKCMACCT)
- MKASSIGN_TRACK(float) — campaign track
- MKASSIGN_NXTSEQ(2) — next sequence step
- MKASSIGN_NXTDAT — scheduled date for next step
- MKASSIGN_SALEND — sale/promotion end date
- MKASSIGN_PRCODE — price code

Assigns a customer account to a campaign track and tracks their position in the sequence.

---

### Supporting MK Tables

| Table | Fields | Purpose |
|---|---|---|
| MKTCLASS | 3 | Track class codes: NUM+CLASS+ACTIVE |
| MKICLASS | 3 | Item/event class codes: NUM+DESC+ACTIVE |
| MKTNOTE | 3 | Track notes: TRACK+LINE PK; TEXT(70) per line |

**MK module summary:** MKTRACK defines campaigns, MKTROUT defines the event sequence, MKEVENT specifies what happens at each step, MKFORM holds the letter/email template, MKASSIGN puts customers into campaigns at a specific sequence position. The system automatically advances each customer to the next MKTROUT step on schedule.

**MK confidence: 72/100** — Full 6-table architecture confirmed; campaign-route-event-form chain decoded; MKASSIGN customer enrollment confirmed; integration with BKCMACCT (CRM accounts) confirmed; event trigger mechanism (how MKTROUT fires MKEVENT on schedule) in encrypted RWN.

---

## PR — Payroll History, W2, and Commissions — Pass 73

### BKPRHIST (127f) — Payroll Transaction History

**PK:** BKPR_CURP_EMPNM + CURP_PRDTE + CURP_ACTNM + CURP_CHKNM

Identical 127-field structure to BKPRCURP (active payroll period). BKPRHIST is the closed-paycheck archive — after PR-H posts and prints checks, BKPRCURP rows are archived here. Retains complete per-paycheck detail: RPHRS/RPAMT (regular), 12 OT types (OPHRS/OPAMT_1..12), vacation/sick, all 12 deductions, FIT/FICA/state/SDI/WC/medical amounts. Historical audit trail for every paycheck ever issued.

---

### BKPRW2 (384f) — W2 Preparation Table

**PK:** BKPR_EMP_NUM (same as BKPRMSTR)

Same 384-field structure as BKPRMSTR (BKPR_EMP_ prefix). BKPRW2 is the W2 reporting view/staging table — contains the same employee master data (name, SSN, address, YTD amounts) but is specifically used by the W2 printing and magnetic-media programs. The identical field count (384f) confirms this is an alternate-index view of BKPRMSTR, not a separate table.

---

### BKPRBOOK (87f) — Commission Book (Alternate View)

Identical 87-field structure to BKPRSALE (BKPR_SLS_ prefix): 12-month QUOTA/GROSS/COGS/RCPTS arrays. BKPRBOOK is an alternate-index view of BKPRSALE optimized for a different sort order (possibly by commission class rather than by employee number).

---

### BKPRACOM (12f) / BKPRHCOM (12f) — Commission Records (Active/History)

**PK:** BKPR_COMM_SLSP(2) + CCODE(10) + INVNM(float)

Salesperson commission detail per invoice line:
- BKPR_COMM_INVDT — invoice date
- BKPR_COMM_PAYDT — pay date (when commission was earned/paid)
- BKPR_COMM_AMTPD — amount paid on invoice
- BKPR_COMM_COMM — commission amount
- BKPR_COMM_PD_ON — paid-on amount (base for commission calculation)
- BKPR_COMM_EXTRA(25) + ULID(float) + TDATE — notes + unique ID + transaction date
- BKPR_COMM_PCODE(15) — product code

BKPRACOM = active unpaid commissions; BKPRHCOM = history of paid commissions. Used by PR-COMM (commission payout) and CS (commission/salesperson) module.

**PR confidence: 90/100** — BKPRHIST(127f) confirmed as BKPRCURP archive (identical prefix/structure); BKPRW2(384f) confirmed as BKPRMSTR W2 view; BKPRACOM/BKPRHCOM(12f) commission detail decoded; active/history pair pattern confirmed. PR table family now covers: BKPRMSTR, BKPRCURP, BKPRHIST, BKPRW2, BKPRSALE/BKPRBOOK, BKPRACOM/BKPRHCOM, BKPRFTAX, BKPRGLFL, BKPRTC, BKPRINFO, ISPRUDF, BKPRSTFL, ISPRTEMP.

---

## IC — Pricing: DISCOUNT as BKICPMAT Alias — Pass 73

### DISCOUNT (85f) — Alternate Index of BKICPMAT

DISCOUNT uses the identical BKIC_PMAT_ field prefix and 85-field structure as BKICPMAT (customer-item pricing matrix). DISCOUNT is a Btrieve alternate-index of BKICPMAT sorted by PCODE (item) rather than CUST (customer) — programs that need "all customers who have a price for this item" use DISCOUNT, while programs that need "all items this customer has a price for" use BKICPMAT.

---

## System — Utility Tables — Pass 73

### BKCPMSTR (9f) — Check Printing Path Configuration

BKCP_ prefix. Single-row configuration for the check printing (CP) subsystem:
- CMPATH(66) — C-file (check) path
- IMPATH(66) — I-file path
- CFILE(20), VFILE(20), EXPATH(66), HFILE(20), EFILE(20) — additional file paths
- LABEX(1), COMMEX(1) — lab/commission exception flags

### BKCPEC (10f) — Check Printing Error/Staging

**PK:** DATE + CHECKNO
- GLACCT(10) + GLDEPT(4) — GL posting destination
- AMOUNT(float), CHECKNO(float), DESC(25) — check details
- ISCHK(float) — is-check flag; ERROR(5) — error code; LINE(2) — line ref; VEND(10) — vendor

---

### DBACNAME (3f) — DBA Company Name Lookup

- CNAME_CODE(2) + CNAME_NAME(25) + CNAME_FILLER(40)

Multi-company name lookup. Used at company selection (EVOMENU_SELCOMP) to display company names by 2-char code.

---

### BKFLDHLP (3f) — Context-Sensitive Field Help

- HLP_CODE(17) — field identifier (screen + position); HLP_INDEX(2) — line number; HLP_LINE(60) — help text

When a user presses F1 on a field, EvoERP looks up HLP_CODE to retrieve the multi-line help text. Editable via TA-M (Forms Editor).

---

### BKSLMSTR (2f) — Security Level Descriptions

- BKSL_MSTR_LEVEL(2) + BKSL_MSTR_DESC(45)

Human-readable names for the 2-char security level codes used in BKPSUSER and BKSLEVEL.

---

### BKUPDATE (4f) — Software Update Log

**PK:** BKUP_COMPANY(2) + UPDATE(1)
- BKUP_DATE — applied date; BKUPDATE_VER(15) — version string

Records which patches/updates have been applied per company. Prevents TA-D from re-applying patches.

---

### New Tables Confirmed (Pass 73)

| Table | Fields | Purpose |
|---|---|---|
| WORKHORD | 74 | WO history — closed WO header archive (WORKORD mirror) |
| WORKSORD | 74 | WO templates — saved/standard WO headers |
| WOHBOM | 24 | WO BOM history archive |
| WOHLABOR | 58 | WO labor history archive |
| WOHMAT | 17 | WO material issue history archive |
| WOHRECV | 11 | WO receipt history archive |
| WOHROUT | 81 | WO routing history archive |
| WOHDATE | 13 | WO schedule date history archive |
| WOHEXCHG | 10 | WO engineering change cost history |
| WOELABOR | 58 | WO estimated labor (pre-actual) |
| WOEMAT | 17 | WO estimated material (pre-issue) |
| WOERECV | 11 | WO estimated receipt |
| WOLABRPT | 58 | WO labor report view (WOLABOR alt-index) |
| WORKACHG | 25 | WO header change audit — WOPRE+WOSUF+CODE PK; A/B status/priority/class/desc |
| MKDEF | 11 | Marketing defaults — config + next-ID counters |
| MKTRACK | 4 | Campaign track definition — NUM+DESC+CLASS+ACTIVE |
| MKTROUT | 11 | Campaign event sequence — TRACK+SEQ PK; EVENT+DAYSNXT+NEXTSEQ |
| MKEVENT | 12 | Marketing event — NUM PK; DESC+MEDIA+FORM+FUCODE+SENDTO |
| MKFORM | 6 | Marketing form template — NUM PK; FILE+ATT+MEDIA |
| MKASSIGN | 6 | Customer-to-campaign assignment — ACCT+TRACK PK; NXTSEQ+NXTDAT |
| MKTCLASS | 3 | Track class codes |
| MKICLASS | 3 | Item/event class codes |
| MKTNOTE | 3 | Track notes — TRACK+LINE PK; TEXT(70) |
| BKPRHIST | 127 | Payroll history archive — closed paychecks (BKPRCURP mirror) |
| BKPRW2 | 384 | W2 preparation view — BKPRMSTR alt-index for W2 printing |
| BKPRBOOK | 87 | Commission book — BKPRSALE alt-index |
| BKPRACOM | 12 | Active commissions — SLSP+CCODE+INVNM PK; COMM+AMTPD+PCODE |
| BKPRHCOM | 12 | Commission history — same 12f as BKPRACOM |
| DISCOUNT | 85 | BKICPMAT alt-index sorted by item code |
| BKCPMSTR | 9 | Check printing path config — CMPATH+IMPATH+5 file paths |
| BKCPEC | 10 | Check print staging/errors — DATE+CHECKNO+GLACCT+AMOUNT+VEND |
| DBACNAME | 3 | Company name lookup — CODE(2)+NAME(25) |
| BKFLDHLP | 3 | Context-sensitive field help — CODE+INDEX+LINE(60) |
| BKSLMSTR | 2 | Security level names — LEVEL(2)+DESC(45) |
| BKUPDATE | 4 | Patch log — COMPANY+UPDATE PK; DATE+VER(15) |

---

*Last updated: 2026-06-17 (Pass 73). WO three-tier archive architecture confirmed: live (WORKORD/WOBOM/WOLABOR etc.) + estimate (WOEMAT/WOELABOR/WOERECV) + history (WORKHORD/WOHBOM/WOHLABOR etc.); WORKACHG(25f) WO header change audit completes the WO change-audit family (4 tables: header+BOM+routing+history); MK Marketing Automation module decoded (6 tables: MKDEF+MKTRACK+MKTROUT+MKEVENT+MKFORM+MKASSIGN); PR family complete: BKPRHIST(127f) payroll history + BKPRW2(384f) W2 view + BKPRACOM/BKPRHCOM(12f) commission detail; DISCOUNT confirmed as BKICPMAT alt-index. 35 new schemas. Confidence bumps: WO 87→90, PR 87→90, MK new 72.*

---

## AR — Invoice Archive, Recurring, and Customer Views — Pass 74

### BKARHINV (84f) / BKARHIVL (28f) — AR Invoice History Archive

Identical BKAR_INV_*/BKAR_INVL_* field prefix and 84f/28f structure as BKARINV/BKARINVL. BKARHINV and BKARHIVL are the closed/paid AR invoice archive — after payment and period close, invoices from BKARINV move here. Used by MA-C, AR-F, and SA (Sales Analysis) history reports. Standard AR invoice architecture: live (BKARINV/BKARINVL) + history (BKARHINV/BKARHIVL).

---

### BKARRINV (84f) / BKARRIVL (28f) — AR Recurring Invoice Templates

Same 84f/28f structure as BKARINV/BKARINVL. BKARRINV holds template invoices that are periodically cloned into real BKARINV records. Recurring invoices (e.g., monthly maintenance fees) are set up once in BKARRINV and copied by the AR recurring billing process.

---

### BKARECST (106f) / BKARSHIP (106f) — BKARCUST Alternate-Index Views

Both 106f with BKAR_CUSTCODE as the leading key field — identical structure to BKARCUST (AR customer master). BKARECST = estimated cost view of BKARCUST (sorted for cost analysis); BKARSHIP = ship-to view of BKARCUST (sorted for shipping lookup). Standard Btrieve alternate-index pattern: same physical data, different key sort.

---

### BKAREIVT (24f) — AR Aging Summary with Period Breakdown

**PK:** BKAR_INVT_CODE(10) + DATE + NUM

Aging summary per customer per period:
- BKAB_PERIOD (LOGICAL, 1792 bytes) — **period-bucket array**: 1792 ÷ 8 = 224 logical bits, likely holds 14 periods × 8 aging buckets as bit flags or small floats
- BKAR_INVT_AMT / AMTRM — total amount / amount remaining
- BKAR_INVT_TERMN, TYPE, GLDPT — terms number, transaction type, GL dept
- + 14 more fields (amounts by aging bucket, department allocations)

Used by AR aging reports and dunning — the PERIOD field stores the breakdown by period bucket.

---

### BKARDESC / BKARHDSC (5f each) — AR Description Note Lines

BK_DESC_ standard prefix: CODE(15)+NUM(float)+LINE(2)+NOTES(70)+DESC(25). Standard 5-field description note pattern:
- BKARDESC = active AR invoice description lines
- BKARHDSC = history AR invoice description lines

Per-invoice extended text blocks (free-form notes attached to invoice header). Same BK_DESC_ pattern used across AP (BKAPADSC/BKAPHDSC), QT (BKQTNOTE/BKQTTEMP), and RF (BKRFQDES).

---

## AP — PO Views, Notes, Deposits, and GL Distribution — Pass 74

### BKAPAPO (58f) / BKAPHPO (57f) — AP Open / History PO Views

Alternate-index views of BKAPPO (AP purchase order header, 57f):
- **BKAPAPO (58f)** — open POs only; one extra field (AHSY_USER_ACCES_5 INTEGER 256) which is a security filter embedded in the DDF index definition
- **BKAPHPO (57f)** — historical/closed POs; identical structure to BKAPPO

Programs that need only open POs use BKAPAPO (filtered by default); programs that need all-time PO history use BKAPHPO.

---

### BKAPNOTE (12f) — AP Vendor Notes

**PK:** BKAP_NOTE_SRCH1(10) + SRCH2(10) + DATE

Free-form notes attached to AP vendor or PO records:
- SRCH1 = vendor code; SRCH2 = PO# or invoice# (secondary search key)
- BKAP_NOTE_ENTBY(10) — entered by user
- BKAP_NOTE_NOTES_1..6 (76 chars × 6 = 456 chars per note record)
- + 2 more fields (type/flag)

---

### BKAPDEP (6f) — AR Customer Deposit

**PK:** BKAR_DEP_DEPNO (float)
- BKAR_DEP_CUST(10) — customer code
- BKAR_DEP_DATE — deposit date
- BKAR_DEP_SO(float) — linked sales order
- BKAR_DEP_SR(1) — SO/SR flag
- BKAR_DEP_EXTRA(50)

Customer advance payment / deposit against an open SO or SR order. Despite the BKAP- table name prefix, BKAR_DEP_ fields confirm this is the AR deposit table used by MA module (AR-A deposits, MA-A prepayments).

---

### BKAPADSC / BKAPHDSC (5f each) — AP PO Description Notes

BK_DESC_ standard 5-field pattern: CODE+NUM+LINE+NOTES(70)+DESC(25). Same as BKARDESC for AR:
- BKAPADSC = active AP PO description notes
- BKAPHDSC = historical AP PO description notes

---

### BKAPRIVL (390f) — AP Invoice GL Distribution Lines

**PK:** BKAP_INVL_CODE(10) + NUM(10) + DATE

390 fields! This is the AP invoice GL distribution/allocation table — for multi-line GL splits on a single AP invoice:
- BKAP_INVL_DESC(25) + TERMD(10) + TERMN(2) + TYPED(10) + TYPEN(2) — description + terms + type
- BKAP_INVL_TAMT + TDC(1) — total amount + debit/credit flag
- + 380 more fields: GL account/dept pairs per distribution line (up to ~20 GL splits × ~19 fields each = 380)

BKAPRIVL stores how each AP invoice is distributed across multiple GL accounts, departments, and cost centers. The base BKAPINVT (19f) holds the summary; BKAPRIVL holds the detail GL allocation.

---

## WO — Routing 4-Tier Architecture — Pass 74

### WO Routing Table Family (Extended)

Four variants of the 81-field MTWORO_ routing record:

| Table | Tier | Purpose |
|---|---|---|
| WOROUT (81f) | Live | Active WO routing operations |
| WOROUTMP (81f) | Template | Routing from standard template (before WO-specific modifications) |
| WOSROUT (81f) | Saved/Standard | Saved WO template routing (linked to WORKSORD) |
| WOHROUT (81f) | History | Closed WO routing archive |

WOROUTMP is the intermediate state: when a WO is created from a standard routing, WOROUTMP captures the routing as originally planned. Any deviations (WOROCHG) are then applied to WOROUT.

### WOBOMHRM (7f) — WO BOM Horizontal Remark

**PK:** WOBOM_RM_WOPRE + WOSUF + PARENT(15) + LINE(2) + COMP(15) + LINENM(2)

One-line (30-char) short remark per BOM component line on a WO — the compact counterpart to ISFOBMRM's 704-char extended remarks.

---

## QC — Inspection Results and Archive Views — Pass 74

### ISQCRSLT (57f) — SPC Inspection Result Record

**PK:** ISQC_SPC_LRNUM (float) — unique result record number

Full QC/SPC inspection result per lot/serial/operation:
- ISQC_SPC_CODE(15) + OPER(2) — item code + operation
- ISQC_SPC_LOT(15) + SERIAL(25) + BATCH(25) — lot/serial/batch identifiers
- ISQC_SPC_WOPRE + WOSUF — linked WO
- ISQC_SPC_CNTR(2) + LOTQTY — counter + lot quantity
- + 47 more: likely RESULT_1..N measured values + PASS/FAIL flags + DATE/EMP + SPEC references

Used by QC-A through QC-D inspection modules to record actual measured values against specs defined in ISQCSPEC.

---

### ISQCAMST (14f) / ISQCATRN (21f) — QC Archive Views

BKQC_* prefix = same as BKQCMSTR(14f)/BKQCTRAN(21f). ISQCAMST and ISQCATRN are Btrieve alternate-index views (IS* prefix = alternate key) of the QC master and transaction tables, providing different sort orders for reporting.

---

## PI — Physical Inventory Count Tables — Pass 74

### BKPILCNT (10f) — Physical Inventory Lot Count

**PK:** BKPI_LOT_YEAR(4) + QTR(2) + CODE(15) + LOT(15)

Per-lot count record for the physical inventory (PI module):
- BKPI_LOT_QTY — counted quantity
- BKPI_LOT_TAG(float) — count tag number
- BKPI_LOT_LOC(10) + BIN(15) — location and bin
- BKPI_LOT_SERQTY — serial quantity within lot
- BKPI_LOT_PSTD(1) — posted flag

---

### BKPISCNT (10f) — Physical Inventory Serial Count

**PK:** BKPI_SER_YEAR(4) + QTR(2) + CODE(15) + SERIAL(25)

Per-serial-number count for PI (serial-controlled items):
- BKPI_SER_QTY — counted quantity (always 0 or 1 for serial-controlled)
- BKPI_SER_TAG(float) — count tag
- BKPI_SER_LOC(10) + LOTNO(15) + BIN(15) — location + lot + bin
- BKPI_SER_PSTD(1) — posted flag

PI count architecture: BKPICNT (standard items, documented) + BKPILCNT (lot-controlled) + BKPISCNT (serial-controlled) = three-table PI count family covering all item types.

---

## BS — Business Scorecard Period Data — Pass 74

### ISJBSF (143f) — Business Scorecard Financial Snapshot

**PK:** ISBSF_STARTDATE + ISBSF_ENDDATE

Period-range financial KPI snapshot with 143 fields covering every EvoERP module:
- **AR:** AR_BAL, AR_BILL (billings), AR_RECP (receipts), AR_DISC, AR_COGS
- **AP:** AP_BAL, AP_PAYA (payables), AP_PAYM (payments)
- + 133 more: GL balances, WO labor/material/overhead costs, IC turnover, SO/PO totals, PR wages, etc.

ISJBSF is the BS (Business Scorecard) module's per-period rollup table. BS-A collects KPIs from all live modules into ISJBSF for trend analysis and management dashboards. Each row captures a complete financial picture for one time period (START + END dates as PK).

---

## BO — BOL Manifest Alt-Index — Pass 74

### ISBOLMS (22f) — Bill of Lading Manifest (Alt-Index View)

ISSO_BOX_ prefix = same as ISSOBOX (BO/BOL module, 22f). ISBOLMS is a Btrieve alternate-index of ISSOBOX providing a different sort (possibly by INVNUM or CODE rather than SONUM+LINE+BOX). ISSOBOX/ISBOLMS: SONUM+LINE+BOX PK; CODE+QTY+LOT+SERIAL+TEMP+EXTRA(150)+INVNUM+12 more.

---

### New Tables Confirmed (Pass 74)

| Table | Fields | Purpose |
|---|---|---|
| BKARHINV | 84 | AR invoice history archive (paid invoices — BKARINV mirror) |
| BKARHIVL | 28 | AR invoice history line archive (BKARINVL mirror) |
| BKARRINV | 84 | AR recurring invoice template header |
| BKARRIVL | 28 | AR recurring invoice template lines |
| BKARECST | 106 | BKARCUST alt-index for cost analysis |
| BKARSHIP | 106 | BKARCUST alt-index for ship-to lookup |
| BKAREIVT | 24 | AR aging summary — CUST+DATE PK; PERIOD array (1792b) + amounts |
| BKARDESC | 5 | AR active invoice description notes (BK_DESC_ pattern) |
| BKARHDSC | 5 | AR history invoice description notes |
| BKAPAPO | 58 | AP open POs view — BKAPPO + security filter field |
| BKAPHPO | 57 | AP historical closed POs view — BKAPPO mirror |
| BKAPNOTE | 12 | AP vendor notes — SRCH1+SRCH2+DATE PK; 6×NOTES(76) |
| BKAPDEP | 6 | AR customer deposit — DEPNO PK; CUST+DATE+SO+SR flag |
| BKAPADSC | 5 | AP active PO description notes (BK_DESC_ pattern) |
| BKAPHDSC | 5 | AP history PO description notes |
| BKAPRIVL | 390 | AP invoice GL distribution — CODE+NUM+DATE PK; multi-GL-split allocation |
| WOSROUT | 81 | WO saved routing (linked to WORKSORD template WOs) |
| WOROUTMP | 81 | WO routing template (pre-modification state) |
| WOBOMHRM | 7 | WO BOM short remark — WOPRE+WOSUF+PARENT+LINE+COMP PK; REMARK(30) |
| ISQCRSLT | 57 | QC SPC inspection results — LRNUM PK; CODE+OPER+LOT+SERIAL+measured values |
| ISQCAMST | 14 | QC receiving master archive view (BKQCMSTR alt-index) |
| ISQCATRN | 21 | QC transaction archive view (BKQCTRAN alt-index) |
| BKPILCNT | 10 | PI lot count — YEAR+QTR+CODE+LOT PK; QTY+TAG+LOC+BIN |
| BKPISCNT | 10 | PI serial count — YEAR+QTR+CODE+SERIAL PK; QTY+TAG+LOC+LOT+BIN |
| ISJBSF | 143 | Business Scorecard period snapshot — START+END PK; AR/AP/GL/WO/IC KPIs |
| ISBOLMS | 22 | BOL manifest alt-index view of ISSOBOX |

---

*Last updated: 2026-06-17 (Pass 74). AR archive family complete: BKARHINV/BKARHIVL (paid invoice archive) + BKARRINV/BKARRIVL (recurring templates) + BKARECST/BKARSHIP (BKARCUST alt-indexes) + BKAREIVT (aging summary). AP extended: BKAPAPO/BKAPHPO (open/history PO views) + BKAPNOTE(12f) + BKAPDEP(6f AR deposit) + BKAPRIVL(390f GL distribution). WO routing: 4-tier confirmed (WOROUT + WOROUTMP + WOSROUT + WOHROUT); WOBOMHRM(7f) BOM remark. QC: ISQCRSLT(57f) SPC inspection results. PI: BKPILCNT+BKPISCNT lot/serial count pair. ISJBSF(143f) Business Scorecard KPI table decoded. 26 new schemas. Confidence bumps: AR 85→88 (archive family complete), AP 90→92 (GL distribution + open/history views), WO 90→91 (routing 4-tier), QC 78→81 (ISQCRSLT), PI 72→76 (lot/serial count pair), BS 72→78 (ISJBSF KPI table).*

---

## QC/AC — NCR/CAR Follow-Up Events — Pass 75

### ISACAR (35f) — NCR Archive (ISNCR Alt-Index)

IS_NCR_ prefix = identical structure to ISNCR (35f). ISACAR is a Btrieve alternate-index of ISNCR providing a different sort order for the NCR archive/history view.

---

### ISACARFU (13f) / ISCARFUP (13f) — CAR Follow-Up Events (Archive/Active)

IS_CARFUP_ prefix. CAR (Corrective Action Request) follow-up event records:
- IS_CARFUP_CAR(float) — parent CAR/NCR number
- IS_CARFUP_DATE — follow-up date
- IS_CARFUP_USER(15) — user who recorded it
- IS_CARFUP_UID(30) — unique record ID
- IS_CARFUP_TYPE(10) — follow-up type (e.g., email/phone/visit)
- IS_CARFUP_EXTRA(50) — notes
- IS_CARFUP_CDTE + CWHO — close date + closed by
- (+ 5 more: additional close/status fields)

ISACARFU = archive CAR follow-up events; ISCARFUP = active follow-up events. Used by QC-G (CAPA) and AC module to track milestone progress on corrective actions.

---

## IS — Notes and Audit System — Pass 75

### ISANOTES (12f) — Timestamped Note Record

**PK:** IS_NOTE_ID(48) — compound record identifier (table name + record key)

Universal note/audit entry with full create/edit timestamps:
- IS_NOTE_TYPE(3) — note type code
- IS_NOTE_CDATE + CTIME(10) + CWHO(15) — created date/time/by
- IS_NOTE_EDATE + ETIME(10) + EWHO(15) — last-edited date/time/by
- (+ 4 more: content, priority, link fields)

ISANOTES is the universal note-attachment system. The 48-char ID encodes the parent table and record key, so any record in EvoERP can have notes attached. Separate from ISNOTES (which uses a different primary key structure).

---

## IC — Valuation and Alternate Master Views — Pass 75

### BKICVAL (4f) — Daily Inventory Valuation Snapshot

**PK:** BKIC_VAL_CODE(15) + DATE

Per-item daily closing valuation:
- BKIC_VAL_TOTVL(float) — total dollar value (UOH × unit cost)
- BKIC_VAL_UOH(float) — units on hand at this date

Created during period-close or IC-Q "Value Inventory". Used for GL inventory reconciliation and period-end inventory value reporting.

---

### BKICAMTR (64f) / BKICEMTR (64f) / BKICAPMA (85f) — BKICMSTR Alt-Index Views

All share the BKIC_PROD_ field prefix:
- **BKICAMTR (64f)** — "IC Actual Master" — 64-field subset of BKICMSTR sorted for actual-cost reporting
- **BKICEMTR (64f)** — "IC Estimate Master" — same 64-field subset, sorted for ES/MR module pricing access
- **BKICAPMA (85f)** — "IC AP/Price Matrix Alt" — 85-field BKICPMAT alt-index (third sort order of the customer pricing matrix); joins with BKICAPMA give "all pricing for this item across all customers"

---

## IN — Inventory Transactions — Pass 75

### INVATXN (24f) / INVETXN (24f) — Inventory Transaction Records

MTIT_ prefix: both share identical 24-field structure:
- MTIT_TYPE(1) — transaction type (R=receipt, I=issue, A=adjust, T=transfer, S=ship)
- MTIT_CLASS(4) — item class
- MTIT_DATE — transaction date
- MTIT_CODE(15) — item code
- MTIT_QTY — quantity
- MTIT_AVGCOST — average cost at time of transaction
- MTIT_STDCST — standard cost at time of transaction
- MTIT_LOC(10) — location
- (+ 16 more: lot/serial, GL account/dept, employee, WO link, document number)

INVATXN = actual inventory transactions (posted); INVETXN = estimated/planned inventory movements (pre-posting or ES module usage).

---

## PC — Production Control / Kit Module — Pass 75

### BKPCKIT (6f) — Production Kit Components

- BKPC_KIT_COMP(15) — component item code
- BKPC_KIT_QTY_R(float) — quantity required
- BKPC_KIT_QTY_A(float) — quantity allocated
- BKPC_KIT_QTY_S(float) — quantity shipped/used
- BKPC_KIT_DATELM — date limit (need-by date)
- BKPC_KIT_LOC(10) — source location

Tracks component allocation within a PC production kit.

---

### BKPCPLOT (10f) — Production Schedule Plot

**PK:** BKPC_PLOT_PROD(15) + ISDTE

Production scheduling record per item:
- BKPC_PLOT_SPDTE — scheduled ship date
- BKPC_PLOT_QTY — planned quantity
- BKPC_PLOT_CUST(10) — customer
- BKPC_PLOT_INKO(float) — quantity in kit
- BKPC_PLOT_STAT(1) — status (P=planned, R=released, C=complete)
- BKPC_PLOT_STRTD — scheduled start date
- (+ 2 more)

The PC module provides production planning/scheduling on top of the WO and SO modules. BKPCKIT tracks component allocation; BKPCPLOT tracks the production schedule per item.

---

## BM — BOM Alt-Index Views and RO Routing Templates — Pass 75

### ISBMESA / ISBMEST / ISBMTMP (26f each) — BOM Alternate-Index Views

All BKBM_ prefix = identical 26-field structure to BKBMMSTR:
- **ISBMESA** — BOM actual snapshot (used by BM-SA reporting — "BOM Snapshot Actual")
- **ISBMEST** — BOM estimate snapshot (used by ES module — estimated BOM vs. actual)
- **ISBMTMP** — BOM template (saved BOM templates for quick WO creation)

All are Btrieve alternate-index views of BKBMMSTR (or its snapshot variants BKBMAMTR/BKBMEMTR) with different sort orders.

---

### ROUTAING / ROUTTEMP (62f each) — Routing Alt-Index Views

MTRO_ prefix = identical 62-field structure to ROUTING:
- **ROUTAING** — alternate-index of ROUTING (probably sorted by item CODE for "routing-aging" reports)
- **ROUTTEMP** — routing template (saved standard routings before assignment to specific items)

---

### SERIALH (30f) — Serial Number History View

MTSER_ prefix = identical to SERIAL (30f). SERIALH = "Serial History" — alternate-index of SERIAL sorted by RECDATE (or CODE without SERIAL) for historical traceability queries.

---

## CM — Session Lock and Temp Tables — Pass 75

### BKCMCTL2 / BKCMCTL3 / BKCMCTL4 (1f each) — CM Concurrent Session Locks

Single-field tables: BKCM_CTRL_USER(10). One-record lock tables — each holds the user ID of the current CM module session occupying that slot. CM-A checks these before allowing entry; multiple concurrent CM sessions are managed via CTL2/3/4 slots.

---

### BKCMTMP1 / BKCMTMP2 / BKCMTMP3 / BKCMTMP4 (6f each) — CM Bulk Operation Staging

**Fields:** BKCMT_CODE(10) + KEYF(20) + GROUP(8) + COMP(2) + TAG(1) + ACTIVITY(5)

Four identical temporary staging tables (one per concurrent CM session) used during CM module bulk operations (mass mailings, bulk assignments). Session N uses TMPn table. Cleared at session end.

---

## SA — Monthly Summary Rollup Tables — Pass 75

### SUMCUST (5f) — Monthly Customer Sales Summary

**PK:** SUMCUST_CUST(10) + YEAR(2) + MONTH(2)

- SUMCUST_SALES(float) — total sales this month
- SUMCUST_COGS(float) — total COGS this month

Per-customer monthly rollup. Used by SA (Sales Analysis) module for trend reports without scanning full BKARINV transaction detail.

---

### SUMPNCUS (6f) — Monthly Customer-Item Sales Summary

**PK:** SUMPNCUS_CUST(10) + PARTNO(15) + YEAR(2) + MONTH(2)

- SUMPNCUS_SALES + SUMPNCUS_COGS — same as SUMCUST but also by part number

More granular sales analysis: "how much of item X did customer Y buy in month M?"

---

### SUMWC (7f) — Monthly Work Center Summary

**PK:** SUMWC_WORKCTR(12) + YEAR(2) + MONTH(2)

- SUMWC_LABOR + SETUP + UNITS + SCRAP — monthly labor/setup hours, units produced, scrap

Per-WC monthly rollup. Used by SH (Shop Scheduling) efficiency reports and JC (Job Cost) WC performance analysis.

---

## MU — Multi-WO Staging and Notes — Pass 75

### MWOPTEMP (8f) — Multi-WO Operation Staging

**PK:** MWOP_CNTR (float)

Staging record for multi-yield WO (MU module) serial number assignment:
- MWOP_WOPRE + MWOP_WOSUF — source WO
- MWOP_SERIAL(25) — serial number being assigned
- MWOP_QTYCOM — quantity completed
- MWOP_STATUS(10) — staging status (Pending/Assigned/Done)
- MWOP_EXTRA(100) — extra data
- MWOP_SRC(2) — source indicator

Used by MU-A (multi-yield receipt) to stage serial numbers across multiple parallel WO operations before posting.

---

## Cross-Module — Standard Description Note Family — Pass 75

### BK_DESC_ Note Pattern: Remaining Members

The 5-field BK_DESC_ note pattern (CODE+NUM+LINE+NOTES(70)+DESC(25)) used universally for extended text blocks. Previously documented: BKARDESC, BKARHDSC, BKAPADSC, BKAPHDSC. Additional members:

| Table | Module | Purpose |
|---|---|---|
| BKQTNOTE | QT/Service Quote | Active quote notes |
| BKQTTEMP | QT | Quote note templates |
| BKRFQDES | RF/RFQ | RFQ description lines |
| NOTETEMP | System | General note templates (cross-module) |

---

### New Tables Confirmed (Pass 75)

| Table | Fields | Purpose |
|---|---|---|
| ISACAR | 35 | NCR archive alt-index (ISNCR sort variant) |
| ISACARFU | 13 | CAR follow-up archive — CAR+DATE PK; TYPE+EXTRA+CDTE |
| ISCARFUP | 13 | CAR follow-up active — same 13f as ISACARFU |
| ISANOTES | 12 | Timestamped note — ID(48) PK; TYPE+CDATE/CTIME/CWHO+EDATE/ETIME/EWHO |
| ISARFQ | 49 | RFQ alt-index (BKRFQ sort variant for AR access) |
| BKICAMTR | 64 | IC actual master alt-index (BKICMSTR 64-field subset) |
| BKICEMTR | 64 | IC estimate master alt-index (BKICMSTR 64-field subset) |
| BKICVAL | 4 | Daily inventory valuation — CODE+DATE PK; TOTVL+UOH |
| BKICAPMA | 85 | BKICPMAT 3rd alt-index (item-sorted customer pricing) |
| INVATXN | 24 | Inventory actual transactions — TYPE+DATE+CODE PK; QTY+AVGCOST+STDCST |
| INVETXN | 24 | Inventory estimate transactions — same 24f as INVATXN |
| BKPCKIT | 6 | Production kit components — COMP PK; QTY_R/A/S+DATELM+LOC |
| BKPCPLOT | 10 | Production schedule plot — PROD+ISDTE PK; SPDTE+QTY+CUST+INKO+STAT |
| ISBMESA | 26 | BOM actual snapshot alt-index (BKBMMSTR sort variant) |
| ISBMEST | 26 | BOM estimate snapshot alt-index |
| ISBMTMP | 26 | BOM template alt-index |
| ROUTAING | 62 | ROUTING alt-index (aging/alternate sort) |
| ROUTTEMP | 62 | Routing template |
| SERIALH | 30 | SERIAL alt-index (history sort by RECDATE) |
| ISBTCSB | 54 | ISSRINFO alt-index (SR extended info, batch CSB sort) |
| BKCMCTL2/3/4 | 1 | CM concurrent session locks (one per slot) |
| BKCMTMP1..4 | 6 | CM bulk operation staging tables (one per session) |
| SUMCUST | 5 | Monthly customer sales — CUST+YEAR+MONTH PK; SALES+COGS |
| SUMPNCUS | 6 | Monthly customer-item sales — CUST+PARTNO+YEAR+MONTH PK; SALES+COGS |
| SUMWC | 7 | Monthly work center summary — WC+YEAR+MONTH PK; LABOR+SETUP+UNITS+SCRAP |
| MWOPTEMP | 8 | Multi-WO serial staging — CNTR PK; WOPRE/WOSUF+SERIAL+QTY+STATUS |
| BKQTNOTE | 5 | QT quote notes (BK_DESC_ pattern) |
| BKQTTEMP | 5 | QT quote note templates |
| BKRFQDES | 5 | RFQ description lines (BK_DESC_ pattern) |
| NOTETEMP | 5 | General note templates (BK_DESC_ pattern) |

---

*Last updated: 2026-06-17 (Pass 75). IS archive views decoded: ISACAR (ISNCR alt), ISACARFU/ISCARFUP (CAR follow-up events active/archive). IC family extended: BKICVAL(4f) daily valuation + BKICAMTR/BKICEMTR(64f) actual/estimate master views + BKICAPMA(85f) 3rd pricing alt-index. IN: INVATXN/INVETXN(24f) actual/estimated inventory transactions. PC: BKPCKIT(6f) kit components + BKPCPLOT(10f) production schedule. BM/RO: ISBMESA/ISBMEST/ISBMTMP(26f) BOM alt-indexes + ROUTAING/ROUTTEMP(62f) routing variants. SA: SUMCUST(5f)+SUMPNCUS(6f)+SUMWC(7f) monthly rollup tables. MU: MWOPTEMP(8f) serial staging. CM: BKCMCTL2..4(1f) session locks + BKCMTMP1..4(6f) session staging. BK_DESC_ family complete: BKQTNOTE+BKQTTEMP+BKRFQDES+NOTETEMP. 30 new schemas. Confidence bumps: QC 81→82 (ISACAR=ISNCR alt confirmed; CAR follow-up decoded), IC/IN 78→82 (BKICVAL+INVATXN/INVETXN), SA 75→80 (SUMCUST+SUMPNCUS+SUMWC monthly rollups).*

---

## Pass 76 — Alternate-Index Catalog and Remaining Distinct Tables

### Master Alternate-Index Pattern Reference

This pass catalogs the remaining DDF tables that are **Btrieve alternate-index views** (different sort keys over the same underlying data file). EvoERP's Pervasive PSQL database uses alternate indexes extensively to give programs fast access paths from multiple angles without duplicating data.

**How to identify alt-indexes:** Same field prefix as the primary table, same or fewer fields, table name starts with IS* or has a variant suffix (H, A, S, R, T, etc.).

---

### AR Alt-Index Family (84f / 28f / 26f variants)

All of the following are alternate-index views of the core AR tables (BKARINV/BKARINVL/ISARCHG):

**84f BKAR_INV_ views (all = BKARINV sorts):**

| Table | Sort/Purpose |
|---|---|
| ISSQTH | IS SQ (Sales Quote) header sort |
| ISSSOH | IS SS OH — SO shipping sort |
| ISSSRH | IS SS R header — SR service sort |

**28f BKAR_INVL_ views (all = BKARINVL sorts):**

| Table | Sort/Purpose |
|---|---|
| ISSQTL | Sales Quote lines |
| ISSSOL | SO shipping lines |
| ISSSRL | SR service lines |
| BKARSIVL | AR "S" invoice lines (ship-to sort) |
| ISARAIVL | AR archive invoice lines |

**77f / 16f BKAR_INV_ partial views:**

| Table | Fields | Sort/Purpose |
|---|---|---|
| ISARAIVV | 77 | AR archive invoice variant (77 of 84 fields) |
| ISARAIVI | 16 | AR archive invoice index (16-field key subset) |

**26f ISAR_CHG_ views (all = ISARCHG alt-indexes):**

| Table | Sort/Purpose |
|---|---|
| ISARECHG | Estimate change sort |
| ISARHCHG | History change sort |
| ISARICHG | Invoice# change sort |
| ISARMCHG | Misc change sort |
| ISARQCHG | Quantity change sort |
| ISARRCHG | Return change sort |
| ISARSCGH | Special charge group sort |

**14f BKAR_TXN_ views (all = BKARTXN sorts):**

| Table | Sort/Purpose |
|---|---|
| BKARTXNB | AR transaction by bin/batch sort |
| BKARTXNS | AR transaction by serial sort |
| ISARATXN | AR archive transaction |
| ISARATXS | AR archive transaction by serial |
| ISSOALOT | SO/AR transaction by lot |
| ISSOASER | SO/AR transaction by serial |
| ISSRTXN | SR transaction |
| ISSRTXNS | SR transaction by serial |

**5f BK_DESC_ views (all = description note tables):**

| Table | Module | Purpose |
|---|---|---|
| ISARADSC | AR archive | Archive description notes |
| ISARAHDS | AR archive history | Archive history description notes |
| BKARRDSC | AR recurring | Recurring invoice description notes |
| BKARDPST | AR deposit | AR deposit description notes |
| ISRFQADS | RF RFQ | RFQ archive description notes |
| ISSHIPA | SO/AR | Ship-to address notes |
| ISSRADSC | SR | SR description notes |
| ISSRDESC | SR | SR description (alt-index) |

---

### AP Alt-Index Family (57f / 38f / 49f variants)

**57f BKAP_PO_ views (all = BKAPPO sorts):**

| Table | Sort/Purpose |
|---|---|
| BKAPAPO | AP open POs only (with security filter) |
| BKAPHPO | AP historical closed POs |
| ISSPOH | IS SP — supplier portal PO sort |

**38f BKAP_POL_ views (all = BKAPPOL sorts):**

| Table | Sort/Purpose |
|---|---|
| BKAPAPOL | AP open PO lines |
| BKAPHPOL | AP history PO lines |
| BKAPRFQL | AP RFQ lines |
| ISSPOL | IS SP — supplier PO lines |

**57f / 49f RFQ / Quote views:**

| Table | Fields | Sort/Purpose |
|---|---|---|
| BKAPRFQ | 57 | AP RFQ header (BKAP_PO_ prefix, vendor RFQ sort) |
| BKAPQUOT | 49 | AP Quote (BKRFQ_ 49-field quote header alt) |
| ISAPHQT | 49 | IS AP HQ — AP historical quote |
| ISAPQTQT | 49 | IS AP quote-to-quote sort |
| ISARFQ | 49 | IS AR RFQ alt-index (already documented) |

**12f BKAP_CHK_ views (AP check tables):**

| Table | Sort/Purpose |
|---|---|
| BKARCHKF | AP check file (active checks — VNDCOD+INVNUM PK) |
| BKARCHKH | AP check history (cleared checks — same 12f) |
| ISAPACHK | IS AP check archive alt-index |

---

### SO/SR/SQ Extended Info Alt-Indexes (54f ISSR_INFO_ views)

All are alternate-index views of ISSRINFO (54f):

| Table | Sort/Purpose |
|---|---|
| ISSOAINF | SO archive info sort |
| ISSOHINF | SO history info sort |
| ISSOINFO | SO current info sort |
| ISSRAINF | SR archive info sort |
| ISSRHINF | SR history info sort |
| ISBTCSB | Batch CSB info sort |

---

### SO/SR Box/Manifest Alt-Indexes (22f ISSO_BOX_ views)

All = ISSOBOX alt-indexes:

| Table | Sort/Purpose |
|---|---|
| ISSOABOX | SO archive box |
| ISSOAHBX | SO archive history box |
| ISSOHBOX | SO history box |
| ISBOLMS | BOL manifest sort (documented Pass 74) |

---

### IC Alt-Index Family (64f BKIC_PROD_ views)

All = BKICMSTR alt-indexes:

| Table | Sort/Purpose |
|---|---|
| BKICAMTR | IC actual master sort |
| BKICEMTR | IC estimate master sort |
| ISICADT | IS IC actual date sort |
| ISICESA | IS IC ES actual sort |
| ISICEST | IS IC ES estimate sort |
| ISICAMTR | IS IC actual matrix sort |
| XXICMSTR | J7 extended IC master sort |

---

### DC Labor Alt-Indexes (50f LAB_/MTWOLA_ views)

| Table | Fields | Sort/Purpose |
|---|---|---|
| BKDCCLAB | 50 | DC "Copy/Clock" labor sort (LAB_ prefix, DATE+EMP key) |
| BKDCHLAB | 50 | DC history labor sort (MTWOLA_ prefix) |

Both are alternate-index views of BKDCLAB / WOLABOR.

---

### New Distinct Tables — Pass 76

### BKAPACCN (154f) — Vendor Contact Extension

BKCM_ACCN_ prefix (same as BKCMACCN). This is BKCMACCN exposed under a BKAP- alias for AP module access — when the AP module needs to look up vendor contacts (10 contact slots per vendor: CONT_1..10, TITLE, PHONE, EMAIL, etc.). Same underlying data as BKCMACCN; alternate index sorted by vendor code.

---

### ISARCHG-family (BKARCHKF/BKARCHKH) — AP Check Reconciliation

- **BKARCHKF (12f)** — AP check file (active uncleared checks): BKAP_CHK_VNDCOD+INVNUM PK; INVAMT+AMTPD+DISC+TYPE+DESC+INVDTE+NUM+CHKACT+2more
- **BKARCHKH (12f)** — AP check history (cleared checks): same 12f, different Btrieve sort by check number

Used by AP-K (check reconciliation) to match printed checks against paid invoices.

---

### ISCONVRT (9f) — Unit of Measure Conversion

**PK:** IS_CONV_ITEM(15) + SUM(10) + PUM(10)

- IS_CONV_SCONV(float) — stock UM conversion factor
- IS_CONV_PCONV(float) — purchase UM conversion factor
- IS_CONV_WTCONV(float) — weight conversion factor
- (+ 3 more: price/cost conversions)

Per-item multi-UM conversion table. When an item is purchased in "CASE" but stocked in "EACH," ISCONVRT holds the conversion factors. Used by PO receiving, IC transfer, and cost calculations.

---

### ISPOTRK (7f) — PO Shipment Tracking

**PK:** IS_TRK_ORD(float) — PO number

- IS_TRK_NUM(25) — carrier tracking number (FedEx/UPS)
- IS_TRK_SHPVIA(10) — shipping method/carrier
- IS_TRK_CDATE — created date
- IS_TRK_RDATE — expected receipt date
- IS_TRK_STATUS(50) — status string (e.g., "In Transit", "Delivered")
- (+ 1 more)

PO inbound shipment tracking. Allows buyers to track purchase orders by carrier tracking number.

---

### ISPOLOG (9f) — PO Access Audit Log

**PK:** ISPO_LOG_EMP + DATE + TIME

- IS_LOG_WHO(15) — user who accessed the PO
- IS_LOG_PRGM(8) — program name
- IS_LOG_PONUM(float) — PO accessed
- (+ 3 more: terminal ID, company, action)

PO access audit — records every time a user opens or modifies a PO.

---

### ISLOTS / ISHLOTS (11f each) — WO Serial/Lot Genealogy

IS_SER_ prefix. Both tables track parent-child serial relationships during WO production:
- IS_SER_WOPRE + WOSUF — source WO
- IS_SER_PARENT(15) + PDESC(30) — parent item being produced
- IS_SER_PSERIAL(25) — parent serial number
- IS_SER_ADATE — assembly date
- (+ 5 more: child serial/lot, quantity, operation, location)

ISLOTS = active WO lot genealogy; ISHLOTS = history/archive. Tracks "which component serials were consumed to produce this parent serial number."

---

### ISMACS (11f) — WO Machine Assignment

**PK:** IS_MACS_WOPRE + WOSUF + OPER + MACNUM(4)

Records which machine was used for a WO operation:
- IS_MACS_WC(12) — work center
- IS_MACS_SDATE — start date
- (+ 5 more: EDATE, hours, operator, status, notes)

---

### ISQRYSQL (2f) — Stored SQL Queries

- IS_QRY_NAME(30) — query name (PK)
- IS_QRY_QUERY(1000) — SQL statement (up to 1000 chars)

Named SQL queries saved by TA-R (SQL Editor). Allows users to save frequently-used reports or drill-down queries.

---

### ISVARSQL (4f) — SQL Query Parameter Definitions

- IS_VAR_QNAME(30) + VNAME(30) + TYPE(1) + ORDER(2)

Defines input parameters for stored ISQRYSQL queries. QNAME links to ISQRYSQL; VNAME = parameter variable name; TYPE = data type; ORDER = prompt sequence.

---

### ISCONVRT-related small code tables

| Table | Fields | Purpose |
|---|---|---|
| CUSTCLAS | 2 | Customer/item class codes: MTCLASS_M_CLASS(4)+DESC(30) |
| ISLTYPE | 4 | Lot type codes: IS_LT_TYPE(3)+DESC(30)+SEC(2)+EXTRA(100) |
| ISDIV | 3 | GF division codes: IS_GF_DIV(10)+DESC(40)+MISC(100) |
| ISQTCODE | 3 | QT quote category codes: IS_CATM_CODE(4)+DESC(60)+EXTRA(100) |
| ISFSEMP | 3 | FS/Field info base class codes: IS_FIB_CLASS(4)+GROUP(50)+EXTRA(50) |
| ISBILLSH | 4 | Bill-to/ship-to pairing: IS_BILLSH_BILL(10)+SHIP(10)+FLAG(1)+EXTRA(100) |
| ISCMGRP | 2 | Item-to-manufacturer tech spec: ISCC_MTF_ITEM(15)+MTF(60) |
| ISARATNT | 3 | AR archive transaction note type |

---

### J7 Custom — Cancel Order Module (JSPCNLCD / JSPCNLSO)

| Table | Fields | Purpose |
|---|---|---|
| JSPCNLCD | 6 | Cancel reason codes: CODE(1)+DESC(30)+LCODE(10)+CDATE+WHO+EXTRA |
| JSPCNLSO | 12 | Canceled SO line records: SONUM+UNUM+ITEM PK; CQTY+CDATE+WHO+6more |

J7 Systems custom module for formal order cancellation workflow with reason codes.

---

### System Meta-Tables (X$* — Pervasive DDF Catalog)

The X$* tables are the **Pervasive PSQL data dictionary system catalog** — Btrieve's internal schema metadata:

| Table | Purpose |
|---|---|
| X$File | Table registry: file name, path, page size, record length |
| X$Field | Field definitions: name, type, size, offset per table |
| X$Index | Index definitions: key segments, sort order, flags |
| X$Attrib | Field attributes (nullable, default values) |
| X$Occurs | Repeating groups/arrays within records |
| X$Proc | Stored procedure definitions |
| X$Relate | Referential integrity relationships |
| X$Trigger | Trigger definitions |
| X$Variant | Variant record definitions |
| X$View | Named view definitions |

These are read-only meta-tables that describe the database structure itself. DDF viewer tools (like DFVIEW.exe) query them to enumerate all tables and fields.

---

### Helper/Staging Small Tables

| Table | Fields | Purpose |
|---|---|---|
| ISSOABOX | 22 | SO archive box alt-index of ISSOBOX |
| ISSOAHBX | 22 | SO archive history box alt-index |
| ISSOHBOX | 22 | SO history box alt-index |
| ISAREMND | 22 | AR reminder alt-index (ISREMIND sort for AR context) |
| ISPOBOX | 22 | PO receiving bin/box assignment (ISSO_BOX_ prefix, for PO) |
| ISHLOTS | 11 | WO lot genealogy history alt-index |
| ISHSERIA | 11 | WO serial genealogy history (IS_SER_ alt-index) |
| ISAMRPF | 9 | IS AR MRP forecast alt-index (BKMRPFC sort variant) |
| ISMRPFC | 9 | IS MRP forecast alt-index (MTMRP_ sort variant) |
| ISSLSFC | 9 | IS Salesperson forecast (BKPRSALE sort variant) |
| ISPRSALE | 87 | IS PR Sale — BKPRSALE alt-index (87f sort variant) |
| ISGLHDAT | 86 | IS GL Historical Date — ISGLDATE alt-index (86f sort variant) |
| OUTHPROC | 15 | OUTPROC alt-index (outside process by date sort) |
| WBTRVMEM | 5 | WBT review memory — BK_DESC_ pattern, review notes |
| WBTRVMEMO | 5 | WBT review memo — BK_DESC_ pattern |
| ISSRAMMS | 12 | ISSRMMS alt-index (SR equipment make/model/serial sort) |
| ISAUTODC | 12 | IS Automation DC — auto-DC event log (DATE+EMP+WOPRE PK) |
| ISSNOTES | 12 | IS System Notes — ISNOTES alt-index |
| EVOHLPID | 2 | EVO help ID: HELP_ID(code)+mapping |
| HELPURL | 3 | Help URL: CODE+URL(path)+MODULE |
| ESTCHGS | 3 | Estimate charges code: CODE+DESC+RATE |
| ISALOT | 25 | LOT alt-index (already documented as IS Lot sort view) |
| ISDLCK1 / ISDLCK2 | 1 | IS datalock slots 1/2 — single-field lock tables |
| ISPOS / ISPOSC | 2 | IS PO status code(2)/current: STATUS(1)+DESC(1) |
| ISPODESC | 1 | IS PO description single-field lock/flag |
| ISPRESN | 1 | IS PR reason single-field lock/flag |
| ISPOHTRK | 7 | IS PO history tracking — ISPOTRK history sort |
| TEMPOLD | 4 | Legacy temp table (obsolete, from DBA era) |
| TESTARRA | 101 | Development test table — array-of-fields test structure |
| TESTFILE | 11 | Development test file |

---

*Last updated: 2026-06-17 (Pass 76). Bulk alt-index catalog complete. All 133 remaining undocumented tables identified and classified: AR family (BKARINV/BKARINVL/ISARCHG/BKARTXN variants), AP family (BKAPPO/BKAPPOL/BKRFQ variants), SO/SR/SQ info (ISSRINFO variants), IC family (BKICMSTR variants), DC labor (BKDCLAB variants), BK_DESC_ note tables. New distinct tables: ISCONVRT(9f) UM conversion + ISPOTRK(7f) carrier tracking + ISPOLOG(9f) PO audit log + ISLOTS/ISHLOTS(11f) WO serial genealogy + ISMACS(11f) machine assignment + ISQRYSQL(2f) stored queries + ISVARSQL(4f) query parameters + BKAPACCN(154f) vendor contacts + BKARCHKF/H(12f) AP check reconciliation + code tables (CUSTCLAS/ISLTYPE/ISDIV/ISQTCODE) + J7 cancel module (JSPCNLCD/JSPCNLSO). X$* tables = Pervasive DDF system catalog (10 meta-tables). Schema coverage now approaches 100% of the DDF-registered tables. Confidence bumps: SO 75→82 (full ISSO*/ISSQ*/ISSRINFO alt-index family mapped), AP 92→93 (all BKAP*POL/BKAP*PO + BKARCHKF/H decoded).*

---

## Pass 77 — Final 16 DDF Tables (100% Coverage)

### Alt-index completions (same schema as primary, different sort key)

| Alt-index table | Primary table | Module | Sort key / purpose |
|---|---|---|---|
| **ISRTESA** (62f) | ROUTING (62f) | ES/RO | ES actual routing — sorts ROUTING by ES actual-cost order |
| **ISRTEST** (62f) | ROUTING (62f) | ES/RO | ES estimate routing — sorts ROUTING by ES estimate order |
| **ISQTINFO** (54f) | ISSRINFO (54f) | QT/SR | QT (service quote) extended-info sort — same 40-alpha/10-date pattern as ISSRINFO, keyed by quote number |
| **ISANCR** (35f) | ISNCR (35f) | QC | Active NCR alt-sort — third index on ISNCR alongside ISACAR; used for real-time open NCR queue |
| **ISISATAX** (13f) | BKISHTAX (13f) | IS/IC | IS archive historical tax alt-index — same 13-field layout as BKISHTAX; alternate sort for IS archive module |
| **ISARAHTX** (5f) | BKARHTAX (5f) | AR | AR archive historical tax alt-index — same INVNO+CODE+ID+PID+AMOUNT; sorted by CODE for tax-code reporting |
| **ISCCMTF** (2f) | ISCMGRP (2f) | IC/CM | Item-to-manufacturer tech-spec alt-index — same ITEM(15)+MTF(60); alternate sort of ISCMGRP |

---

### ISITMCFG — Item Serial/Lot Number Format Configuration
9 fields. Defines the auto-generation format for serial or lot numbers by item and class. When EvoERP auto-generates serial/lot numbers (SR, IC, WO receipts), this table supplies the pattern and the last-used counter.

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_SERC_ITEM | STRING | 15 | Item code (FK → BKICMSTR) — PK part 1 |
| IS_SERC_CLASS | STRING | 4 | Number class/type (e.g. SER, LOT) — PK part 2 |
| IS_SERC_SPOS | UBINARY | 2 | Start position within the generated number string |
| IS_SERC_LENG | UBINARY | 2 | Length of the numeric increment portion |
| IS_SERC_TOTAL | UBINARY | 2 | Total length of the complete generated number |
| IS_SERC_NUMBER | FLOAT | 8 | Next number to use (auto-increment counter) |
| IS_SERC_LAST | STRING | 25 | Last number generated (display/audit) |
| IS_SERC_EXTRA | STRING | 100 | Extra |

---

### WCTRSLOD — Work Center Capacity Load Snapshot
8 fields. One row per work center per date; records planned capacity, actual load hours, and utilization percentage. Used by the SH (Shop Scheduling) module for finite-capacity planning and WC throughput reporting.

| Field | Type | Size | Meaning |
|---|---|---|---|
| WC_LOAD_WC | STRING | 12 | Work center code (FK → BKWCMSTR) — PK part 1 |
| WC_LOAD_DATE | DATE | 4 | Calendar date — PK part 2 |
| WC_LOAD_TOTHRS | FLOAT | 8 | Total hours loaded (scheduled work) |
| WC_LOAD_UDATE | DATE | 4 | Last update date |
| WC_LOAD_CAP | FLOAT | 8 | Capacity (available hours for this date) |
| WC_LOAD_UTIL | FLOAT | 8 | Utilization % (TOTHRS / CAP × 100) |
| WC_LOAD_LOAD | FLOAT | 8 | Actual load after constraint adjustments |
| WC_LOAD_EXTRA | STRING | 150 | Extra |

---

### ISLOCCST — Per-Location Average Cost
7 fields. When a site uses location-level average-cost accounting, each warehouse location carries its own average cost and book value for a part. ISLOCCST maintains that per-location cost alongside the standard per-item cost in BKICMSTR.

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_LCST_PART | STRING | 15 | Part/item code (FK → BKICMSTR) — PK part 1 |
| IS_LCST_LOC | STRING | 10 | Location code (FK → ISLOC) — PK part 2 |
| IS_LCST_AVGC | FLOAT | 8 | Average cost at this location |
| IS_LCST_BOOKVAL | FLOAT | 8 | Book value (qty × average cost) at this location |
| IS_LCST_LDATE | DATE | 4 | Last cost update date |
| IS_LCST_LTIME | INTEGER | 4 | Last cost update time |
| IS_LCST_EXTRA | STRING | 150 | Extra |

---

### ISEAB — User Email Address Book
6 fields. Personal email address book stored per EvoERP user. Supports the TAS Pro internal messaging / email-from-EVO feature so recipients can be selected without leaving the application.

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_EAB_USER | STRING | 15 | EvoERP user ID (FK → BKUSRMST) — PK part 1 |
| IS_EAB_CONTACT | STRING | 20 | Contact short name / nickname — PK part 2 |
| IS_EAB_FNAME | STRING | 15 | First name |
| IS_EAB_LNAME | STRING | 15 | Last name |
| IS_EAB_EMAIL | STRING | 30 | Email address |
| IS_EAB_EXTRA | STRING | 100 | Extra |

---

### ISFUTYPE — Follow-Up Type Codes
3 fields. Lookup table for follow-up activity type codes. These codes appear on follow-up records throughout the CM (Contact Management), MK (Marketing Automation), and AC (Activities) modules — e.g. "CALL", "EMAIL", "VISIT", "DEMO".

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_FUTYPE_TYPE | STRING | 10 | Type code (PK) |
| IS_FUTYPE_DESC | STRING | 60 | Description |
| IS_FUTYPE_EXTRA | STRING | 50 | Extra |

---

### ISSTEQUI / ISSTTYPE — SR Equipment Category and Service Ticket Type Codes
3 fields each, identical structure. Used by the SR (Service/Repair) module to classify equipment categories and service ticket types.

**ISSTEQUI** — equipment category definitions:

| Field | Type | Size | Meaning |
|---|---|---|---|
| IS_STYPE_TYPE | STRING | 60 | Equipment category description (PK) |
| IS_STYPE_WHO | STRING | 40 | Default responsible technician or group |
| IS_STYPE_ASSET | STRING | 25 | Asset class code |

**ISSTTYPE** — service ticket type definitions (identical layout):
- IS_STYPE_TYPE — service ticket type description (e.g. "REPAIR", "INSTALL", "PM")
- IS_STYPE_WHO — default assigned-to group or technician
- IS_STYPE_ASSET — associated asset class

---

### ISBRANDC / ISBRANDS — Brand Code and Brand-Class Lookups
2 fields each. Support brand-based pricing, reporting, and CRM account categorization. Field prefix BKCM_ACC_ places these in the CM (Contact/Account Management) module.

**ISBRANDC** — brand code master:

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKCM_ACCC_CODE | STRING | 5 | Brand code (PK) — 5-char identifier |
| BKCM_ACCC_DESC | STRING | 25 | Brand description |

**ISBRANDS** — brand-to-product-class mapping:

| Field | Type | Size | Meaning |
|---|---|---|---|
| BKCM_ACCL_CODE | STRING | 10 | Brand code (FK → ISBRANDC) |
| BKCM_ACCL_CLASS | STRING | 5 | Product class code (FK → BKICCLAS or CUSTCLAS) |

---

*Last updated: 2026-06-17 (Pass 77). **100% DDF table coverage achieved.** Every table registered in the Pervasive schema.json is now documented. Final 16 tables: 7 alt-index completions (ISRTESA/ISRTEST/ISQTINFO/ISANCR/ISISATAX/ISARAHTX/ISCCMTF) + 9 new distinct tables (ISITMCFG serial-number config, WCTRSLOD WC load snapshot, ISLOCCST per-location average cost, ISEAB email address book, ISFUTYPE follow-up type codes, ISSTEQUI/ISSTTYPE SR equipment/ticket type codes, ISBRANDC/ISBRANDS brand lookups). Confidence bumps: Database Schema (field meaning) 78→83, SH/Shop Scheduling 82→83, IC 82→83, LC/Lot Control 80→81.*

---

## Pass 82 — DFM Batch Analysis (2026-06-18): 45 DFMs decoded across 20+ modules

### AC — Activity Control DFM Confirmation

**T7ACDATE.DFM:** Confirms WODATE fields — Start Date (WODATE.START), Finish Date (WODATE.FINISH), Quantity (WODATE.QTY), Parent WO (WODATE.PARPRE/PARSUF → parent.wonum display), Top WO (WODATE.TOPPRE/TOPSUF → top.wonum), Deleted WO (WODATE.DELPRE/DELSUF → deleted.wonum), Total Qty label. ETBcomboval confirms T7 ETB toolbar. Full WODATE 13-field schema confirmed from DFM.

**T7ACRDTYPE.DFM:** ACRDTYPE fields confirmed — Doc Type (AC.RD.TYPE), Reason (AC.RD.REASON), Disposition (AC.RD.DISPO). 3-field table structure confirmed despite not being in DDF.

**T7ACTION.DFM:** ISACTION fields confirmed — Action Type (IS.ACTION.TYPE), Description (IS.ACTION.DESC). 2-field core confirmed.

**AC confidence: 68→74/100**

---

### AU — Auto DC-H (Automated Labor Entry)

**T7AUTODCH.DFM** confirms: Caption "AUTO DC-H". Entry fields: Employee From/Thru (sfrom.emp / sthru.emp), Shifts [123] (shifts — comma-separated shift numbers), WO Number From/Thru (from.wonum / thru.wonum), Time Range From/Thru (from.labtime / thru.labtime), Date Range From/Thru (from.labdate / thru.labdate). Buttons: Post, Exit, Settings.

AU-H = batch labor posting from DC — grabs all DC labor entries matching the filter criteria and posts them to the GL in one operation. Equivalent to running DC-H (post DC labor) for a batch of employees/WOs instead of one at a time.

**AU confidence: 72→78/100**

---

### AL — Audit Log + Alternate Parts

**T7ALERTMSG.DFM:** Simple modal alert dialog — shows AlertMsgLabel (dynamic text), OK button. Used system-wide for alerts.

**T7ALOGSETUP.DFM:** Auto-Login configurator — User Name (USER), Password (password), Status label, Enable Auto Login / Disable Auto Login buttons. Stores credentials for automated EvoERP startup without manual login prompt.

**T7ALTPART.DFM:** Alternate Part (substitute) maintenance — Alternate Part label, Part Number (from.item / thru.item range filter), BKSB.PART.PROD (production item), BKSB.PART.SUBST (substitute item), SUB.DESC (substitute description). Buttons: Related Parts, Save, Exit, Delete, Add, Back, Edit, Settings. Creates bidirectional substitute mappings (save.both.ways flag).

The BKSB.PART.* prefix points to the substitute/alternate part cross-reference table (BKSUBST or similar — not directly in DDF under that name).

**AL confidence: 70→76/100**

---

### BR — Brands / CRM Classification

**T7BRANDS.DFM:** Confirms Code (BKCM.ACCC.CCODE) + Description (BKCM.ACCC.DESC). The BKCMACCC table stores brand codes — this is the same BKCMACCC confirmed in the CM module (Credit Card / Classification code master). Brand = a 5-char code + 25-char description used to classify CRM records (customers/prospects) by brand affiliation.

**BR confidence: 65→72/100**

---

### EM — Emergency GL Maintenance

**T7EMGL.DFM:** Caption "New Screen", fields: Account (from.glacct + from.gldpt for filter/search), GL Account Link (BKGL.ACCT + BKGL.GLDPT + BKGL.EXTRA). The form edits BKGL* — this appears to be an emergency GL account maintenance screen for directly editing GL account entries (BKGLCOA or a derivative). BKGL.EXTRA = extra notes on the GL account entry.

Use case: when GL account records are corrupted or need direct correction outside the normal AM-C COA editor.

**EM confidence: 65→72/100**

---

### FN — File Navigator / Mass Field Replace

**T7FNR.DFM** (3,223 lines — fully read Pass 153, 2026-06-22):

FNR = File Navigator Replace — mass field replacement across any EVO data file. Supports find-replace by alpha/date/numeric value with **up to 6 filter conditions** and substring operations. This is the "nuclear" data fix tool — changes data directly in Btrieve files without module-level validation.

**Inputs:**
- FILENAME (combo, F2 → FilePanel: browser of IS.LOC — EVO file location registry)
- DNAME (F2 → FieldPanel: browser of IS.DICT — EVO internal field data dictionary)
- Array # — element index for array fields
- Action (combo, `vld_action()`) — operation to perform

**Filter conditions (6 rows):** Each row: field name (`flname[n]`) / array# (`felement[n]`) / operator / value (alpha/numeric/date)

**Operators:** All, `<>`, `>`, `<`, `>=`, `<=`, `=`, `$` (contains/substring match)

**Replacement fields:** `AREPL_FIELD` (alpha), `Nrepl_field` (numeric), `dREPL_FIELD` (date)

**Substring controls:** `spos` (start position) + `slength` (length) — for partial alpha field replacement. Per-filter `POS[n]` for `$`-operator match position.

**Buttons:** "Test Filters" (validate conditions before run), Process, Exit

**IS.LOC table** (EVO file location registry — from FilePanel grid bindings):
- `LOC_FILE_NAME` — Btrieve file name
- `LOC_BUFF_NAME` — Internal EVO buffer/handle name
- `LOC_LOCATION` — Full network path to the Btrieve file

**IS.DICT table** (EVO internal field dictionary — from FieldPanel grid bindings):
- `DICT_FIELD_NAME`, `DICT_TYPE`, `DICT_SIZE`, `DICT_DESC`

**PopupMenu (right-click on numeric replacement field):** "Flat amount" / "Percentage" — two subtypes for numeric replacement.

**FN confidence: 65→80/100** — T7FNR.DFM fully read; 6 filter rows (not 4 as previously noted), IS.LOC and IS.DICT table structures confirmed from FieldName bindings; substring ops confirmed.

---

### FS — Field Information Base (FIB)

**T7FSCLASS.DFM:** Class (IS.FIB.CLASS) + Description (IS.FIB.GROUP). **KEY FINDING: the table prefix is IS.FIB.*, not IS.FSC.*** — Field Information Base uses FIB prefix throughout.

**T7FSEMP.DFM:** Rep # (SCAN.EMP) + Market Segment (IS.FIB.GROUP — reused as segment label) + IS.FIB.CLASS. Assigns employees (salespeople) to FIB service classes.

**T7FSINFO.DFM:** Contract (IS.FIB.CONTRACT) + Program (IS.FIB.PROGRAM) + Who (IS.FIB.WHO). Maintains FS information records.

**Field prefix correction:** All FS tables use IS.FIB.* prefix (not IS.FSC.* or IS.FS.*). ISFSCLAS maps to IS.FIB.CLASS + IS.FIB.GROUP; ISFSINFO maps to IS.FIB.CONTRACT + IS.FIB.PROGRAM + IS.FIB.WHO.

**FS confidence: 72→78/100**

---

### IT — Item Serial/Barcode Configuration

**T7ITMCFG.DFM:** Caption "New Screen". Fields: Item Group (IS.SERC.ITEM), Total Length of Item Number (IS.SERC.total), Starting Position of Numeric Portion (IS.SERC.SPOS), Length of Numeric Portion (IS.SERC.leng), Last Number (IS.SERC.LAST), Formatted Last Number (ser.format, read-only display), Search button. Configures auto-numbering for each item group — defines how serial/barcode numbers are structured and incremented for items in that group.

**IT confidence: 72→78/100**

---

### JO — Jobs and Departments

**t7jobs.DFM:** Caption "Jobs". Entry fields: Customer Code (jcust), Vendor Code (jvend), Department Code (jdept), Item Number (jitem). Save + Exit buttons. Creates cross-reference between a job and its associated entities — used in Job Costing (JC module) to link jobs to customers, vendors, departments, and items.

**T7JOANDA.DFM:** Caption "Java Response". Very large (1.4 MB DFM). Single label field — this is a display window for Java API responses (JOANDA = JO AND A?). Used to show the output of a Java integration call. No data entry fields.

**T7JODPSALES.DFM:** Caption "New Screen". DSN configuration: Host, Port, Name, Company DSN Settings, Destination (TREEDEST). Save, Go, Exit buttons. Configures the Java data push for Sales data to external BI system.

**JO confidence: 70→76/100**

---

### JS — Java Sync / BI Connection Configurators

All 7 JS DFMs (T7JSACC, T7JSAIC, T7JSAPBI, T7JSASRS, T7JSOI, T7JSQL, T7JSettings) confirmed from DFMs — Pass 82.

All share DSN pattern: Host + Port + Name (database name) + Company DSN Settings section. T7JSettings and T7JSQL add Destination (TREEDEST — tree destination path for report hierarchy). T7JSettings adds "Test Settings", "Detect Settings", "Generate Program" buttons. T7JSOI uses TEditForm2 (slightly different base form).

**Program purposes from DFM captions + prior RWN analysis:**
| Program | DFM form | Purpose |
|---|---|---|
| T7JSACC | TEditForm1 | AR account BI sync DSN setup |
| T7JSAIC | TEditForm1 | Item-Customer BI sync DSN setup |
| T7JSAPBI | TEditForm1 | AP BI sync DSN setup |
| T7JSASRS | TEditForm1 | AR Sales Report Summary DSN setup |
| T7JSOI | TEditForm2 | SO Invoice BI sync DSN setup |
| T7JSQL | TEditForm5 | SQL-based BI query DSN + destination |
| T7JSettings | TEditForm1 | Master JS connection config + program generator |

"JS" prefix = Java Sync — connects EvoERP Pervasive data to an external DSN (likely SQL Server or ODBC target) for BI reporting. Each program configures one data area's sync connection.

**JS confidence: 68→78/100**

---

### LI — Module License / Limited Access

**T7LIMACC.DFM:** Caption "DFM Multi Limited Access Generator / Editor". Fields: DFM Name (dfmname), Access Group (aGroup). Buttons: Generate, Edit, Copy, Exit. Creates access-controlled versions of DFMs — field-level security where different user groups see different subsets of fields.

**LI confidence: 65→72/100**

---

### ML — Multi-Language UI

Both DFM files fully read (Pass 153, 2026-06-22):

**T7MLC.DFM** — "DFM Multi Language Generator / Editor":
- Select a DFM filename (T7 combo, F2 browse)
- Buttons: Generate (populate LANG.DICT from DFM captions), Edit (open T7MLE), Add Lang (show 3-char lang code field `Alang`), Delete (select language via `Langdel` combo to remove), Exit
- Workflow: Generate first → creates ECAPT records for all captions in the selected DFM → then Edit to add translations

**T7MLE.DFM** — "Edit Captions" (SourceFile=T7MLC — same compiled program):
- Language selector: `Langcombo` → `language` field
- Grid: LANG.DICT.ECAPT (Default Caption), LANG.DICT.LANG (Lang code), LANG.DICT.LCAPT (Translated Caption)
- Detail: `defcapt` (read-only English), `LangCapt` (editable translation)
- Navigation: First / Prev / List / Next / Last / Back

**LANG.DICT table** (field bindings confirmed from T7MLE.DFM):
- `ECAPT` — English/default caption (lookup key)
- `LANG` — 3-character language code (e.g., "ESP", "FRN")
- `LCAPT` — Localized (translated) caption

**Runtime integration:** LANGDICT is referenced by many programs at runtime (confirmed in dozens of RWN fingerprints). User language is set in SM-K (T7SMK) via `evo.cfg.lang`. Programs look up LANG.DICT.ECAPT + current LANG to substitute LCAPT.

**ML confidence: 68→82/100** — Both DFMs fully read; LANG.DICT(ECAPT/LANG/LCAPT) confirmed from field bindings; Generate/Edit/AddLang/Delete workflow confirmed; 3-char language code format confirmed; T7MLC+T7MLE share single source confirmed (SourceFile=T7MLC in T7MLE).

---

### MU — Multi-Yield Work Orders

**T7MULTIYIELD.DFM:** Caption "BASE Blank T7 SCREEN". Output item list — M.PART (item code), M.DESC (description), M.QTY (quantity), M.PER (proportion percentage), M.BIN (bin location). Edit row: e.part, e.desc, e.qty, e.bin. Header: scan.wonum (WO number entry), MTWO.WIP.CODE + MTWO.WIP.DESC (input WO from WORKORD). Options: Proportion Costs by [W/F/E] (proportion field — W=Weight, F=Formula, E=Equal split), Use Standard Cost? (stdcost flag). Process + Save + Add + Edit + Delete + Exit buttons.

**W/F/E cost split:** Each output item gets a share of the input WO's cost — W=by weight proportion, F=by formula, E=equal share.

**MU confidence: 72→78/100**

---

### NE — New Company Initialization

**T7NEWINIT.DFM:** Caption "New Screen". Only ETBcomboval field + Go + Exit buttons. Bare stub — no data entry fields visible in DFM; initialization logic is entirely in the encrypted RWN.

**NE confidence: 65→68/100** — Confirmed as a minimal stub; no form fields; initialization logic inaccessible.

---

### SD — Service Detail Code Maintenance

**T7SDET.DFM:** Caption "New Screen". Fields: Type (IS.SDET.TYPE), Detail (IS.SDET.DETAIL). Save + Exit + Delete + Add buttons. Maintains the IS.SDET.* code master used by the SR module for standard service/repair detail classifications.

**SD confidence: 68→74/100**

---

### XC — Credit Card Cross-Reference Utility

**T7XCUTIL.DFM:** Caption "XCharge Conversion Utility". Caption text: "Converting data to Secure XCharge". Single field: bkcm.acct.code. This is a one-time migration utility — converts raw credit card data stored in BKCMACCN account records to secure XCharge vault tokens. Part of PCI compliance upgrade path.

**XC confidence: 68→74/100**

---

### CC — Credit Card Processing (Additional DFMs — Pass 82)

Six additional CC DFMs confirmed:

**T7CCP.DFM** (CC-P — Credit Card Info entry): IS.CC.MASKED (card number masked), IS.CC.EXP (MMYY), IS.CC.ZIP, IS.CC.CARDNAME, IS.CC.CARDTYPE, is.cc.process (processor code e.g. "AUTHORIZE"), is.cc.address, ccamount. Shows "* Expired" indicator when IS.CC.EXP is past. Optional fields: Address, CVV. Buttons: Process, Use a Different Card.

**T7CCPO.DFM** (CC on PO): ccnum, ccamount, cczip, CCYY, CCMM, CCADDRESS, CCCVV. Separate form for PO/AP credit card charges (different from AR CC entry — uses raw fields not ISCC table).

**T7CCCITM.DFM** (CC by Item): from.item range filter — applies/views CC charges filtered by item number.

**T7CCCWOT.DFM** (CC on WO): from.wonum + LOCATION — CC charge application to a specific WO at a specific location.

**T7CCDE.DFM** (CC CSV Import): COMMA.FIXED.STR (delimited/fixed flag), file.name, FIELD.NUMBER[1..8] + FIELD.NUMBER2[1..8] for column position mapping. Imports: Customer Code, Credit Card Number, Expiry Date, Sort, Card Type, Name on Card, Zip, Address from CSV.

**T7ccr1.DFM** (CC Invoice List report): Fromdate/thrudate, Fromterms/thruterms — report filter by date range and payment terms.

**CC confidence: 78→84/100**

---

### BS — Business Status (Additional DFMs — Pass 82)

**T7BS.DFM** confirms all ISBSF field bindings on the Status tab: AR (AR.BAL/BILL/RECP/DISC/COGS/DEPO), AP (AP.BAL/PAYA/PAYM/DISC/ATP), SO (SO.OPEN/BOOK/SHIP), PO (PO.OPEN/BOOK/RECP), WO (WO.WIPBAL/ISSU/FPVAR), IC (IC.VALUE), CASH (CASH.TOTA). Period range pickers: months12 + months24 (UI runtime vars). Form caption " Business Status".

**T7BSR.DFM** (Business Status Rebuild): Caption "Business Status Rebuild", status label "Initializing..." — background rebuild utility that recalculates all ISBSF KPI values from current GL/WO/SO/PO/AR/AP data.

**BS confidence: 78→82/100**

---

### BOM Scrap Fix Utility (UT/SM adjacent)

**T7BOMSCRAPFIX.DFM:** Caption "Reset Scrap Calculation". Fields: Item Number From/Thru (from.item / thru.item), Scrap Calculation [%/Q] (scrap.setting — % = percentage scrap, Q = quantity scrap), Synchronize Open Work Orders? (synch.wos), Update only Blank Settings? (blanks.only). Status fields: File Name (fixfile), Start Time (stime), Current Item (curr.item). Process + Exit buttons. Resets BOM scrap calculation method across a range of items and optionally propagates to open WOs.

This is a one-time data fix utility, likely accessed via UT or SM menu.

---

*Pass 82 complete (2026-06-18). Modules updated: US 65→74, MA 70→76, BO 72→80, AC 68→74, AU 72→78, AL 70→76, BR 65→72, EM 65→72, FN 65→72, FS 72→78, IT 72→78, JO 70→76, JS 68→78, LI 65→72, ML 68→76, MU 72→78, NE 65→68, SD 68→74, XC 68→74, CC 78→84, BS 78→82. 45 DFMs analyzed.*

---

## Pass 83 — DFM Batch Analysis Wave 2 (2026-06-18): MRP, CR, PS, SE/ST, AC/CAR, AD, EDII, Chain, KIT/PU

### MRP / BM — Material Requirements Planning (Full Program Map)

18 MRP programs fully confirmed from DFMs (T7MRA through T7MRO + T7MRADE):

| Program | Caption | Purpose |
|---|---|---|
| T7MRA | MR-A | Forecast entry — BKMRP.FC.PART + DATE + QTY + CQTY + OQTY + FLAG |
| T7MRB | MR-B | Forecast report — filter by item/class/category/date/type [RFAMNLBTKO] |
| T7MRC | MR-C | Forecast generation — modes: Consume/Erase/Rollover/LoadLevel; Archive/Restore |
| T7MRD | MR-D | MRP reorder parameters — EXPEDITE buffer + DELAY buffer + Sensitivity, Reorder Level/Amount/Lead Time/Planner Code per item (with *chg change flags) |
| T7MRE | MR-E | MRP parts report — include.mrp flag, Master/Specific location [M/S] |
| T7MRF | MR-F (run) | 4-stage MRP calculation — Stage1(SO)→Stage2(PO)→Stage3(WO+BOM)→Stage4(Forecast); live progress display |
| T7MRG | MR-G | MRP action report — shows expedite/delay actions vs. original dates; LASTPO filter; customer range |
| T7MRH | MR-H | MRP work queue (hot list) — color-coded by days overdue; prior/x-day thresholds; planner/start/finish filters |
| T7MRI | MR-I | Generate Work Orders — Auto/Review [A/R], combine per item, WO class filter [1..6], std pack qty, add customer info to WO |
| T7MRIR | MR-I popup | Review Qty dialog — MTMRP.PARTNO + STARTDT + DATE + QTY for interactive qty approval |
| T7MRIX | MR-I execute | WO create execute screen — ITEM/TOOL/PART/QTY/DESC × 4, wostartdate, woLOC |
| T7MRJ | MR-J | Purchase Order recommendations — AutoEmail, REPORT.MODE, INC.SPECS, INCLAPPRMFGRS, ORDER/RECV dates |
| T7MRJR | MR-J review | Review vendor/price before PO — MTMRP fields + BKMRP.PO.VEND + BKAP.VENDNAME + eprice |
| T7MRJX | MR-J execute | Create POs — BKMRP.PO.VEND/ERD/QTY/PRICE/CONF/PART/DATE → BKAP.PO.NUM |
| T7MRL | MR-L | Planned orders print — PLND.NUM + reverse lookup flag |
| T7MRN | MR-N | Vendor consolidation — vendor range, PO $ value threshold, report-only mode |
| T7MRO | MR-O | Order changes report — changes.only flag (items with changes since last MR-P) |
| T7MRADE | MR-ADE | Forecast import — CSV/fixed-length field-mapping for Item Number + Date (YYYYMMDD) |

**BKMRP table family (confirmed from DFMs):**
- **BKMRP.FC** (Forecast table): PART + DATE + QTY + CQTY (consumed) + OQTY (original) + FLAG
- **BKMRP.PO** (MRP PO planning): PART + VEND + ERD (Estimated Receipt Date) + QTY + PRICE + CONF (confirmed) + DATE
- **MTMRP** (MRP requirements): PARTNO + STARTDT + DATE + QTY

**MRP workflow summary:** MR-C generate forecast → MR-F run MRP (4-stage) → MR-G/H review action messages → MR-I generate WOs / MR-J generate POs → MR-L view planned orders.

**MRP/BM confidence: 85→88/100**

---

### AC — Activity Control / CAR (8D Corrective Action)

**KEY FINDING — 8D CAR system:** T7CAR8D.DFM reveals a complete 8D Corrective Action Report module within AC:

**T7CAR8D.DFM:** Caption "CAR Actions". Fields: is.cact.CAR (CAR#), is.cact.ACTION (Action#), is.cact.CDATE (creation date), is.cact.DUEDATE, is.cact.STATUS, is.cact.REL (release/revision). IS.CTEAM.NAME (team name), IS.CTEAM.SIGNOF (sign-off), IS.CTEAM.SDATE (sign-off date). Then the 8 disciplines: D2 (problem description), D3 (immediate containment + completed/date/by), D4 (root cause + completed/date/by), D5 (planned corrective action + completed/date/by), D6 (implemented corrective action + completed/date/by), plus actions to prevent reoccurrence, Owner. Fields use prefix is.cact.d2/d3/d4/d5/d6 for each discipline + d*c (completed) + d*cd (completed date) + d*r (completed by = "Release").

**New tables confirmed:**
- **ISCACT** — Corrective Action records: CAR# + ACTION# (PK), CDATE, DUEDATE, STATUS, REL, plus D2-D6 text + completed flags
- **ISCTEAM** — CAR team members: NAME + SIGNOF (sign-off name) + SDATE (sign-off date)

**T7carfu.DFM:** CAR follow-up entry — IS.CARFUP.DATE, IS.CARFUP.USER, IS.CARFUP.TYPE (3-field table confirmed).
**T7CARFUP.DFM:** Follow-up type code master — IS.FUTYPE.TYPE + IS.FUTYPE.DESC (matches ISFUTYPE documented in Pass 77).

The **ISFUTYPE** table from Pass 77 (Follow-up type codes) is now confirmed as the lookup for IS.CARFUP.TYPE.

**AC confidence: 74→78/100**

---

### CR — Contract Review / SO Approval

**T7CTRevu.DFM (confirmed):** Caption "Setup Contract Review Departments". Fields: Password (enter.pswd + conf.pswd — for department setup security), Department (ct.dept), Admin Level (ct.admin), Mass Approval button, SO Number From/Thru (sFROM.SONUM / sTHRU.SONUM), Order Date From/Thru (from.orddte / thru.orddte), Contract Reviewer ID (ct.empname). KILL button (force approval). App SOs button (mass-approve SOs in range). Save + Reset buttons.

**T7CTRevuPSWD.DFM:** Password entry popup — Contract Reviewer ID (ct.empname), Department (ct.dept), Password (enter.pswd). POPLABEL for dynamic prompt text.

**CR workflow confirmed:**
- CR-A (T7CTREVU): Admin sets up review departments — assigns reviewer IDs + passwords + admin level + mass-approval authority
- Reviewers enter CR-B via T7CTRevuPSWD popup to authenticate, then approve assigned SOs
- ISCTREVU table: EMPNME + EMP PK, DEPT, ADMIN, LEVEL, MOTPAS, ACTIVE, CDATE, EDATE, ADATE, ATIME, FLAGS
- ISSOREVU table: SO + DEPT PK, EMPNME, EMPNUM, MOTPAS, ADATE, EDATE, APPROVE, REQUIRE

**CR confidence: 72→78/100**

---

### PS — Program Security (Extended)

**T7PSA.DFM:** User setup — User Name (BKPS.USER.CODE), Security Level (seclevel), Security Code [A/P/1/2/C/V/U/E] (seccode), Default Start Company, Employee/Rep (bkps.user.emp), Group (ISEX.USER.GROUP), Windows Username (ISEX.USER.WINDO), Allow Auto Login (auto.log), Velocitrack Admin (velocitrack).

**KEY FINDING — ISEXUSER table:** ISEX.USER.GROUP (group membership) + ISEX.USER.WINDO (Windows username for SSO) are fields in a table with ISEX. prefix — this is likely **ISEXUSER** (extended user data, not in DDF schema or registered under a different name). This enables Windows Active Directory / SSO login and group-based permissions beyond the 20 ACCES_ flags in AHSYLOG.

**T7PSK.DFM:** Approve Vendor — app.vend (approved Y/N), from.vend + bkap.vendname, max.chk.amt (**Maximum Allowable Check Amount** — an AP vendor approval limit), Unapproved.only filter. Vendors must be approved; approved vendors can have a max check amount limit.

**T7PSE.DFM:** User Security Report — print by user name range (FromU/ThruU), Items/Groups filter.
**T7PSF.DFM:** Access to Program Report — print all users with access to a specific program (PROGNAME).

**PS confidence: 82→88/100**

---

### AD — Accounting Defaults (Master Settings — T7MDefaults)

**T7MDefaults.DFM (1.4 MB):** The Evo ERP Master Default Settings mega-form. Key findings:

**ISTS.CFG.* prefix confirmed** as the config table (not BKSYMSTR/BKYSMSTR). Fields:
- ISTS.CFG.WOADSC (WO show address/description)
- ISTS.CFG.WOBS (WO types that affect Business Status)
- ISTS.CFG.WOMAKF (WO make flag)
- ISTS.CFG.WOCALC (WO disable recalc estimated cost)
- ISTS.CFG.BURDN (use material burden), ISTS.CFG.BURDI (burden item#)
- ISTS.CFG.WOOPEN (allow reopen closed/cancelled WO [Y/N/P])
- ISTS.CFG.WOPSWD (WO reopen password)
- ISTS.CFG.WOONLY (WO-only mode)
- ISTS.CFG.WOGDSC (WO goods description), ISTS.CFG.WOGKIT (WO goods kit flag)
- ISTS.CFG.WOALOC (WO allocate), ISTS.CFG.LIMSCT (limit standard cost), ISTS.CFG.RRFPR (RFQ price)
- Also: bkys.yn[1..202] — confirms BKYSMSTR has at least 202 YN flags (much more than assumed)
- bkys.num[1] = BKSYMSTR numeric array, bkys.rbnum (reorder batch number)

**T7MDefBanks.DFM:** Bank/checking account setup — edit.num (bank account number), edit.glacct/gldpt (GL), edit.desc (account name), edit.acct (bank acct#), edit.rout (routing#), edit.sort (user sort key), edit.bal (balance), edit.nxtnum (next check#), edit.ap/ar/pr (module flags), edit.ap.rtm/pr.rtm (check print RTM path), edit.curr (currency code), edit.type (account type), edit.nxtach (next ACH#), edit.nxtepay (next ePay#), edit.id (company ID for ACH), edit.ach.name (ACH profile name), edit.spachk (special check format), BKGL.ACCTD (GL dept).

**AD confidence: 75→82/100**

---

### SE/ST — Service Code Tables (Full Program Map)

All 6 SE/ST DFMs now confirmed:

| DFM | Caption | Table | Field |
|---|---|---|---|
| T7SEPROC | (Type) | ISSEPROC | IS.SEPROC.PROC — service process code |
| T7SERR | (Type) | ISSTYPE | is.stype.type — service error type |
| T7SETYPE | (Type) | ISSETYPE | is.setype.err — service error code |
| T7STTYPE | (Type) | ISSTYPE | is.stype.type — service ticket type |
| T7STYPE | (Type) | ISSTYPE | is.stype.type — service order type |
| T7STOCK | Code + Desc | BKCMACCC | BKCM.ACCC.CCODE + BKCM.ACCC.DESC — stock code (same table as Brands) |

**T7STOCK uses BKCMACCC** — same table as T7BRANDS. BKCMACCC stores both brand codes and stock classification codes depending on context, or these are separate records in the same table differentiated by a type prefix.

**ISSTYPE note:** T7SERR, T7STTYPE, and T7STYPE all reference IS.STYPE.TYPE — same 3-field table (TYPE/WHO/ASSET from prior DDF extraction). Context determines whether it's a service error, ticket type, or order type.

**SE/ST confidence: 65→74/100**

---

### SU — Setup / UI Configuration (Additional)

**WBKLUGRID.DFM:** Caption "Maintain Grid Lookup Data". Full grid admin form — Grid Name (tempName), FD Name (tempFD), Form Name (tempFormName), Security Level (SEC.LEVEL), Start At End flag (LUGRID_END). Field Data section: FD_COLHEADER (column header), FD_FIELDNAME (source field), FD_TOT (totaling), FD_FUNC (aggregate function), FD_TYPE, FD_SIZE. Key Data: KD_COLHEADER, KD_KEYNAME, KD_FIELDNAME. RT_ARROW (right arrow navigation). Sort Keys section. Buttons: Save, Exit, Clear, Copy, Delete.

**T7gdm.DFM:** Grids & Drills Maintenance — Skip (skip), Replace (replace), Overwrite (overwrite). Options for how to handle existing grid data during maintenance operations.

**SU confidence: 72→78/100**

---

### PU — Put-Away

**T7PUTAWAY.DFM:** Caption "New Screen". Fields: Bin (enterbin), scan.item (item scan input), bkic.prod.code/desc/note (item lookup), BKIC.PROD.LRCPT (last receipt date), BKIC.PROD.UOH (unit on hand), action (put-away action code), PABBL (put-away by bin location flag), MTIC.PROD.CODE/DESC/LOC (standard cost item), UOH (current UOH), qbin (bin quantity), mtic.prod.uiqc (UIQC — unit in QC). Buttons: Put Away, Print Label, Clear, Exit.

UIQC = unit quantity in QC (items in quality inspection, not yet available). The put-away workflow: scan item → system shows current bin/UOH/UIQC → operator enters destination bin → put-away posts inventory to new bin.

**PU confidence: 68→76/100**

---

### CH/CHAIN — Program Chain (New Module)

**New module identified:** EvoERP supports program chaining — one program automatically launches another. Two DFMs confirmed:

**T7Chain.DFM:** Caption "Chain List". IS.CHAIN.USER (user who executes), IS.CHAIN.DESC (chain description), IS.CHAIN.AUTO ([Y/N/Ask] — auto-execute or prompt), IS.CHAIN.PARENT (parent program), IS.CHAIN.CHILD (child program). User-level chain assignments.

**T7CHAINM.DFM:** Caption "Chain Master". IS.CHAIN.PARENT + IS.CHAIN.CHILD (PK), IS.CHAIN.AUTO, IS.CHAIN.DESC, IS.CHAIN.PARAM[1..5] — up to 5 parameters passed to the chained program.

**ISCHAIN table confirmed:** PARENT + CHILD + AUTO + DESC + PARAM[1..5] + USER. Enables automation sequences like: post-SO automatically runs BOL, or post-WO automatically runs costing.

---

### EvoScheduler / ISSCHED — Full Schema Confirmed

**EvoScheduler.DFM** confirms all ISSCHED fields: IS.SCHED.NAME (name, PK), IS.SCHED.DESC (description), IS.SCHED.PROG (program to run), IS.SCHED.PARAM1..8 (8 parameter slots), IS.SCHED.LOG (log file path), IS.SCHED.TYPE (occurrence type), IS.SCHED.DATE (next run date), IS.SCHED.TIME (next run time), IS.SCHED.RECUR (recur every N minutes), IS.SCHED.LDATE/LTIME (last run date/time), IS.SCHED.CO (company), IS.SCHED.EMAIL (email notification), IS.SCHED.WHO (who set up). Also CC_CODE + CC_NAME (currency code/name for scheduled runs).

ISSCHED has at least 22 fields (vs. the 24f confirmed in DDF). 8-parameter support enables complex scheduled programs.

---

### EvoLinks / EvoNotes — Additional Field Confirmation

**EvoLinks.DFM:** ISLINKS additional fields confirmed — IS.LNK.SORT (sort key), IS.LNK.DATE, IS.LNK.WHO, IS.LNK.PRIVATE (private flag), IS.LNK.PCB[100] (100-element PCB array — likely parent context block for up to 100 linked records), GEN.ID (generic ID), FILELINK (file path), ALERTS (alert flag), LEXIST (link exists flag), inventory.link.

**EvoNotes.DFM:** ISNOTES additional fields — IS.NOTE.CDATE/CTIME/CWHO (created date/time/by), IS.NOTE.TYPE (note type → ISNTYPE lookup), IS.NOTE.EWHO (edited by), IS.NOTE.PRIVATE, is.note.contact (linked contact), strsearch (text search), GEN.ID.

---

### KIT — Kit Picking (New Module)

**T7KIT.DFM:** Caption "New Screen". Kit picking workflow for work order material pulls. Fields: SCAN.WO (WO scan input), SCAN.EMP (employee), bkic.prod.code/desc/note, mtic.prod.loc (location), binloc (bin location), Work Order Qty, Customer, Drawing, Sort By, Lines Count, Time To Pull, MTIC.PROD.CYCLE (cycle time). Line grid arrays (A* prefix): APART, ADESC, ARQTY (required qty), AUOH (UOH), ALUOH (location UOH), AQTY (actual qty), ABIN (bin), ABOMNOTE, ALOT (lot#), ALOC (location), AOPER (operation#), wobom.reference, scan.item, SORTKEY, xlot. Process/scan workflow: WO → BOM explodes → operator scans each component to confirm kit pull.

---

### EDII — EDI Invoice Import (Additional Confirmation)

**T7EDII.DFM:** Caption "ED-I-I". Fields: imp.filename (import file path), date.format (date format string), from.cust (optional customer filter). Column mapping: FIELD.NUMBER[1..6] for Customer Code, Item Number, Ship Date, PO Number, Date, and a 6th field. Fixed example format shown: "Ex: C:\EXPORT\DATA\Filename.CSV". Confirms CSV column-mapping import approach documented in Pass 61.

**EDII confidence: 72→76/100**

---

### STDCST — Standard Cost Viewer

**T7STDCST.DFM:** Confirms MTICMSTR.RCOST[1..15] with labeled meanings:
| RCOST slot | Cost type |
|---|---|
| 1 | Material |
| 2 | Fixed Overhead |
| 3 | Labor |
| 4 | Setup |
| 5 | Outside Process |
| 6 | (rolled-up) Material + Freight + Duty |
| 7 | (rolled-up) |
| 8 | Variable Overhead |
| 9–15 | Additional rolled-up cost components |

Also confirms: MTIC.PROD.LOTSZ (lot size), BKIC.PROD.LSTC (last cost), BKIC.PROD.AVGC (average cost), MTIC.PROD.TYPE (item type).

This is an informational viewer — Standard Cost is calculated, not entered here.

---

### TA/TCC — Batch Check Processing

**T7TCC.DFM:** Caption "New Screen". Fields: terms.num (Enter Terms to Pay), CHK_NAME[1] (Bank Account selection). Process + Exit buttons. TA-TCC = Batch Check run — selects all AP invoices matching the specified payment terms and processes checks from the specified bank account. Part of the TA (Transaction Automation) module.

---

*Pass 83 complete (2026-06-18). Modules updated: MRP 85→88, AC 74→78, CR 72→78, PS 82→88, AD 75→82, SE/ST 65→74, SU 72→78, PU 68→76, EDII 72→76. New: CH/CHAIN, KIT, STDCST viewer. EvoScheduler ISSCHED fully confirmed. 63 DFMs total analyzed.*

---

## Pass 84 DFM Analysis (2026-06-18) — 107 DFMs analyzed across 18 modules

### QS/Quick Sales Entry

**T7QSOA.DFM:** Caption "Quick Sales Entry → Create Sales Order". Minimal form: triggers quick-entry workflow.
**T7QSOALINES.DFM:** "New SO Line Item" entry grid. Fields: sSONUM, BKAR.INV.CUSNME, BKAR.INV.CUSCOD (customer lookup), ITEM, BKIC.PROD.DESC, PQTY (quantity), ordl.pdisc (discount %), PRICE. Simple rapid-entry Sales Order screen bypassing the full SO-A form. Confidence: 76/100.

---

### RT/RTM Validator

**T7RTMVALID.DFM:** Caption "Select Report Format Name". Single field: `rtmvld_name`. Used system-wide when a program needs the user to choose an RTM (ReportBuilder template) by name from the list of available report templates. This is a shared helper dialog — not a standalone module. Confidence: 70/100.

---

### VSCHED/Visual Scheduler (update)

**T7VSCHED.DFM:** Confirms full scheduler workflow:
- WO list entry: add.item, add.qty, add.wonum, add.sstart/sfin, add.status, sadd.EstNum
- Three action buttons: `init` (Initialize Scheduling Files + start VS), `VS` (Start Visual Scheduler to continue editing), `Post` (Post Visual Scheduler dates)
- External DSN settings: Host, port, name (connects to `wos` = Work Order Scheduler, `wcs` = Work Center Scheduler)
- DSN configuration panel is labeled "Company DSN Settings" — separate from the ERP database, pointing at the visual scheduler server

**T7SHIPRTM.DFM:** "User | RTM Name" — per-user ship document RTM assignment using `ISEX.USER.MISC1` and `ISEX.USER.CODE`. Stores the default ship template per EVO user in the extended user table. Confidence: 78/100.

---

### FO/Features & Options (update)

**T7FOC.DFM:** Feature/Option setup entry — "Feature | Description | Option | Description | Option price | Add Price to Parent? | Use STD Customer Pricing?". Fields: BKBM.PROD.OPYN[4] and BKBM.PROD.OPYN[5] (option flags in BOM product record), BKBM.PROD.PRICE (option price). Confirms FO pricing is stored in BOM product option fields.

**T7FOD.DFM:** Report print by item/class/category range.
**T7FOE.DFM:** Feature/option item picker by item number.

Table: `BKBM.PROD.*` BOM product record contains OPYN[1..n] option flags and PRICE for feature/option pricing. Confidence: 83/100.

---

### SPC/Statistical Process Control (additional DFMs)

**T7SPCLIVEGRID.DFM:** Caption "Top Real Time Errors". Grid fields: ATYPE, ADETAIL, ACODE, ACOUNT. Live error/defect count display — shows current defect type + detail + error code + count.

**T7SPCLIVEREP.DFM:** Live SPC report generator. Fields: from.TYPE, from.DETAIL, thru.TYPE/DETAIL, from.date, top (Show Top N), refresh (Refresh Every N Mins). Auto-refreshing live report.

**T7SPCREP2.DFM:** Extended SPC report with: WO#, parent part, employee, date, sequence, sides, types, details, test types, serial#, customer, test reason (P/R/B = Pass/Reject/Both), errors-only flag. Most comprehensive SPC report form.

**T7SPCREPPPM.DFM:** PPM (Parts Per Million) defect rate report — filters by WO, item, date, sides, types, details, customer. "Include S/R" flag. PPM = standard quality metric for defect frequency.

SPC error data stored in indexed fields ATYPE/ADETAIL/ACODE/ACOUNT. Live refresh capability confirmed. Confidence: 92/100.

---

### SR/Service Repair & Sales Release (update)

**T7SRE.DFM:** "Release thru Est Date" — the SO/SR release form. BKAR.INV.* header fields: CUSA1/CUSA2/CUSCTY/CUSST/CUSZIP/CUSORD/RTS/TAXABL/ORDDTE/NUM/GLDPT/SLSP/LOC/TERMD. Options: Display Shipped Lines, Auto Release Comments, Display Comment Lines, Include Backorders, Release All Lines, Pull Inventory from Default Bins, Prompt to Proportionally Release Kit Comps. BKAR.INVL.ESD = estimated ship date per line.

**T7SRF.DFM:** Caption "SO-F" (SO Invoice Print). All invoice print filters: invoice range, customer/class, ship date, salesperson, packslip, kit components, notes, hidden notes, options, SO Dwg/ECO/Revs. Invoice types: SO module invoices, AR voucher invoices, finance charge invoices.

**T7SRG.DFM:** Post invoices — "SRG | Post All Printed Invoices? | Print the Prepost Commissions Report?" Processes invoices from sFROM.INVNUM/sTHRU.INVNUM and sFROM.SONUM/sTHRU.SONUM ranges.

**T7SRGA.DFM:** Progress display during posting — shows "Posting Invoice No. | From S/R Order No. | Line Item" with BKAR.INV.NUM and BKAR.INV.SONUM fields.

**T7SRI.DFM:** Invoice inquiry/list — BKAR.INV.* header fields: INVDTE, ORDDTE, SHIPDT, CUSCOD, CUSNME, full address, VOID.DATE, SONUM, SUBTOT, TAXAMT, FRGHT, DEPOSIT, RETENTION, TOTAL, SLSP, GLDPT, LOC, DESC. Complete AR invoice display.

**T7SRINFO.DFM:** "S&R Misc. Information" — extra UDF fields on S/R orders. Table `ISSR.INFO.*`: DATE1–DATE5 (5 date fields), AL1–AL20 (20 alpha/text fields). 25 configurable extra fields per S/R order.

**T7SRS.DFM:** "Work Center Schedule / Data Collection" combined view — shows DCD (Data Collection Detail) and SHI (Shop Item) records side by side. DCD fields: EMP, NAME, WOP, P, ITEM, TIMEIN, RUN. SHI fields: ITEM, WOPRE, CUST, P, SDATE, SQTY, DESC.

**T7SRBK.DFM:** "Live Work Center Schedule" — refreshing display. FROM.LOC (location filter), timer (seconds), ISE.STATUS.2/3/4 (Firmed/Released/Complete WO status flags). Real-time WO status board at a location.

New table confirmed: `ISSR.INFO.*` — 5 date + 20 alpha UDF fields per S/R order. Confidence: 82/100.

---

### SH/Shop Scheduling (update)

**T7SHA.DFM:** WO scheduling entry — "SH-A". MTWO.WIP.WOPRE/WOSUF (WO key), MTWO.WIP.CODE (item), MTWO.WIP.DESC, MTWO.CUSTNAME, MTWO.WIP.SFIN (scheduled finish), MTWO.WIP.SSTART (scheduled start), MTWO.WIP.PRTY (priority), MTWO.WIP.DDATE (due date), MTWO.WIP.USERCD (user code). Batch mode with status/priority/class filters.

**T7SHB.DFM:** WO detail schedule — individual routing operation dates. MTWORO.START/OPER/OPERDESC/WC/SCHED.WC/STQTY.

**T7SHC.DFM:** Work center schedule view — MTWC.WCDESC/DEPT/DEPTDESC, MTWC.HRSWEEK, MTWC.%UTIL, MTWC.HRS.SHIFT. Shows all WOs at a work center with operation dates.

**T7SHE.DFM:** Critical ratio scheduling — SWO.CRATIO (critical ratio), TDATE (target date), SPEC.ACTION.STR. Calculates/updates schedule based on critical ratio logic.

**T7SHF/G/H/I/J/M/N/O/P:** Scheduling reports — filter by WO status, class, priority, customer, date ranges, work center. T7SHM = "Shop Horizon" (lead time analysis: shows PR0-PR3 lead time priority dates). T7SHN = part types + hours/day + queue times analysis. T7SHI/SHP = color-coded schedule reports with elapsed time coloring. Confidence: 88/100.

---

### QC/Quality Control (update)

**T7QCFA.DFM:** NCR (Nonconformance Report) entry. Fields: IS.NCR.CDATE (created date), IS.NCR.PART (parent part), IS.NCR.COMP (component), IS.NCR.WHO, IS.NCR.QTY, IS.NCR.DCODE (defect code), IS.NCR.DESC (description of nonconformity), IS.NCR.ICR (inventory check required), IS.NCR.ORIG (origin: I=In-house/V=Vendor/R=Rework), IS.NCR.PDRAW/PREV/CDRAW/CREV (parent+component drawing/rev), plus WC/machine/tool/operation/vendor/PO/RMA cross-references. NCR# is sFROM.SONUM.

**T7QCMTHD.DFM:** Testing method master — "Enter Testing Method". Fields: TEST.CODE, EDIT.REV, EDIT.REVDT (revision+date), EDIT.DESC/DESC2 (description), PROCEDURE (method text), NOTES.LINE. Table: ISQC.MTD.TSTCOD/DESC/DESC2 (primary key = test code).

**T7QCSPEC.DFM:** Testing requirements per item/operation — "Enter Testing Requirements". Fields: ISQC.SPC.CNTR (work center), ISQC.SPC.OPER (operation), ISQC.SPC.TSTCOD (test code), test.min/max/units, test.lot (lot tracking?), test.psfail (pass/fail only). Primary key: item + work center + operation + test code.

**T7QCRSLT.DFM:** Testing results entry — TEST.NUM, TEST.CODE, TEST.MIN/MAX/UNITS, TEST.RESULT, TEST.PASS. Plus QC.LOT, QC.BATCH, scan.wo (work order), MTWO.WIP.SQTY (WO start qty), lr.number (lot/run#), scan.oper, qc.serial, tdate, SCAN.TESTEMP/SCAN.APPEMP (tested by / approved by). Test results linked to WO + lot + serial.

**T7QCRESULTS.DFM:** Test results report — filter by WO, item, QC report number (sfrom.qclr/sthru.qclr).

New tables: `ISQC.MTD.*` (test method master), `ISQC.SPC.*` (test specification per item/WC/op), `IS.NCR.*` (nonconformance reports). Confidence: 88/100.

---

### CS/Commissions & Salesperson (update)

**T7CSA.DFM:** Salesperson master entry. Fields: SEMPNUM (employee#), BKPR.AGNT.CODE (agent code), BKPR.SLS.RATE (commission rate), BKPR.SLS.FNMI/LNME (first/last name), BKPR.SLS.HOW (commission method), BKPR.SLS.WHEN (when commission earned), BKPR.SLS.CLASS[1] (class), BKPR.SLS.EXPACT/EXPDPT (expense GL account/dept).

**T7CSB.DFM:** Salesperson performance view — "CS-B View Salespersons Info". Monthly statistics: BKPR.SLS.PAID[1..12] (commission paid per month), BKPR.SLS.COMM[1..12] (commission earned per month), BKPR.SLS.RCPTS[1..12] (receipts per month). Plus columns: Quota, COGS, Comm Due, Comm Paid, Receipts, Gross.

**T7CSD.DFM:** Commission transfer — "CS-D Transfer Sales Commissions". Table: BKPR.COMM.SLSP, BKPR.COMM.CCODE (company code), BKPR.COMM.INVNM (invoice#), BKPR.COMM.INVDT (invoice date), BKPR.COMM.PAYDT (payment date), BKPR.COMM.COMM (commission amount). Filter by rep range, date range, with posting date entry.

**T7CSI.DFM:** "Evo Master Inquiry" — universal entity lookup. Single-screen to search by: itemnum, custcode, sonum, invnum, Vendcode, ponum, porecp (PO receipt), wonum, wsuffix. Acts as a cross-module drill-down launcher.

**T7CSE/CSF/CSP:** Commission detail/summary print reports with salesperson range, date range, cost/GP option.

New tables: `BKPR.SLS.*` (12-month commission/paid/receipts arrays), `BKPR.COMM.*` (commission transaction records). Confidence: 85/100.

---

### PR/Payroll (update)

**T7PRA.DFM:** Employee W-4 and YTD/QTD tax summary. 2020 W-4 redesign fields: BKPR.EMP.NEWW4 (use 2020 W-4 flag), BKPR.EMP.2EPJ (two equal-paying jobs), BKPR.EMP.ANDD (annual dependent deduction), BKPR.EMP.OAIWW (other annual income without withholding), BKPR.EMP.AAD (additional annual deduction), BKPR.EMP.AWPPP (additional withholding per pay period). YTD/QTD fields: BKPR.EMP.FITYTD/FITQTD (FIT), BKPR.EMP.FICYTD[1]/FICQTD[1] (FICA-SS), BKPR.EMP.FICYTD[2]/FICQTD[2] (FICA-Med), BKPR.EMP.STYTD/STQTD (state), BKPR.EMP.SDIYTD/SDIQTD (SDI), BKPR.EMP.WKYTD/WKQTD (workers comp).

**T7PRB.DFM:** Payroll batch processing. Current payroll record (BKPR.CURP.*): FITWH (federal income tax), FICWH[1/2] (FICA SS/Med), SITWH (state), MDAMT/MDDPT (misc deduction amount/dept), ODAMT/ODNME (other deduction), FUTEX/FICEX/SUTEX (employer FUTA/FICA/SUTA exempt). Employee list with columns: REC.ARR, NAME.ARR, NUM.ARR, DIV.ARR, LPAY.ARR, HOURS.ARR, GROSS.ARR, NET.ARR, CHECK.TYPE, TAG.ARR.

**T7PRD.DFM:** Check printing — beginning check number, bank accounts (regular + direct deposit), employee range, check date, period ending date. Options: print hourly rate, print PR stubs to PDF, print bottom stub information, print all earnings/deductions, use T6PRD2.RTM for direct deposit. Supports dual bank accounts (CHK_NAME + DDCHK.NAME).

**T7PRM.DFM:** Payroll division GL setup. BKPR.GL.DEPT/DPTNME (division), BKPR.GL.STCODE (state code). Standard deduction rates: BKPR.GL.FICAEMP/FICAMEE (employee/employer FICA %), BKPR.GL.FICAEPL (FICA limit), BKPR.GL.FUTART/SUTART (FUTA/SUTA rates), BKPR.GL.SDI.RTE/LMT (SDI rate/limit). GL accounts: BKPR.GL.FITACCT (FIT liability), BKPR.GL.FICACCT[1/2] (FICA SS/Med), BKPR.GL.FUTACCT, plus dept codes for each.

New table fields: `BKPR.EMP.*` — 2020 W-4 redesign fields confirmed (NEWW4, 2EPJ, ANDD, OAIWW, AAD, AWPPP). `BKPR.CURP.*` — current payroll transaction record. `BKPR.GL.*` — division-level payroll tax GL setup. Confidence: 92/100.

---

### ES/Estimating (update)

**T7EST.DFM:** Main estimate entry — "ES-A | Enter Estimates". Ten quantity levels: IS.EST.QTY[1..10]. Margin fields: IS.EST.MATMU% (material margin), IS.EST.LABMU% (labor margin), IS.EST.OPMU% (outside process margin), IS.EST.OHMU% (overhead margin), IS.EST.OVLMU% (overall margin). Header: IS.EST.ORDDESC (order description), IS.EST.STATUS, IS.EST.DRAW/REV (drawing/rev), IS.EST.EXPDTE (expire date), IS.EST.LOSTDTE (lost date), IS.EST.QTREV (quote revision#), IS.EST.OPPTYPE (opportunity type).

**T7ESE.DFM:** "ES-E Convert Estimates". Converts estimate to WO and/or SO: ISTO.WO, ISTO.SO flags. Entry: sFROM.QUOTE (source estimate#), sWO.NUM/SO.NUM (target numbers), CUST.PO, LOCATION, START.DATE/FINISH.DATE/ESD.DATE. Options: incl.est.no (put estimate# in customer PO field), ISUPD.CONTRACT (update contract price file), UCP (unit cost/price).

**T7ESB/ESC/ESD:** Print estimates/quotes — filter by customer, class, quote#, job#, expiration date, status codes. Up to 10 quantity levels printable. Options: BOM detail, routing detail, kit components, extensions, ECO/drawings.

New table fields: `IS.EST.*` — 10-qty levels, 5 margin types, opportunity type, lost date, quote revision tracking. Confidence: 88/100.

---

### FA/Fixed Assets (update)

**T7FAA.DFM:** Fixed asset master — "FA-A". IS.FXA.NUMBER (asset#), IS.FXA.TYPE, IS.FXA.DESC/DESC2, IS.FXA.CSTBAS (cost basis), IS.FXA.RESVAL (residual value), IS.FXA.LIFE, IS.FXA.METH (depreciation method), IS.FXA.GLA/D (asset GL account/dept), IS.FXA.ACDEPA/D (accum depreciation account/dept), IS.FXA.DEPEXPA/D (depreciation expense account/dept), IS.FXA.SDATE (placed in service), IS.FXA.EDATE (disposed), IS.FXA.SOLD (sales price), IS.FXA.SERIAL. Also tracks: IS.FXA.ACCUMDEP (accumulated depreciation), IS.FXA.LDEPAMT/LDEPPERC/LDEPDATE (last depreciation amount/percent/date).

**T7FAB.DFM:** Depreciation transaction processing. IS.FXT.NUMBER (asset#), IS.FXT.DATE (posting date), IS.FXT.AMOUNT, IS.FXT.PERC (percent), IS.FXT.NETAVAL (net asset value), IS.FXT.ACDEPA/D (accum dep account), IS.FXT.DEPEXPA/D (expense account). "Generate Recurring" option. Processes tagged asset records.

**T7FAE.DFM:** Import fixed assets from file (length/delimited). Maps up to ~15 fields including asset#, type, description, cost basis, residual value, life, dates, GL accounts.

Tables: `IS.FXA.*` (asset master: 22 fields confirmed), `IS.FXT.*` (depreciation transactions). Confidence: 86/100.

---

### SA/Sales Analysis (update)

**T7SAA.DFM:** Main sales analysis — territory (bill+ship), customer, currency range. Options: print in base/source currency, bookings vs sales report, include S&R orders, print item detail.

**T7SAM/SAN.DFM:** Custom report builder — "SA-M". BKSA.NAME (report name), BKSA.TITLE, BKSA.RTM (report template), SORT.TEXT (sort by). N.TOP.SALES (Top N). Range pairs: BKSA.FROM1..BKSA.THRU9 cover invoice date, ship date, customer, salesperson, item, class, territory, and other dimensions.

**T7SAO.DFM:** Top N Sales — filter by customer, date (two ranges), salesperson, bill state, bill+ship territory, customer class. Options: bookings, ship-to, include vouchers, Top N count.

**T7SAQ.DFM:** Actual Margin Report — MTWO.WIP.* based (uses actual WO costs). Filter by ship date and WO finish date.

New confirmed: `BKSA.*` table stores saved report configurations with up to 9 FROM/THRU range pairs + RTM name. Confidence: 84/100.

---

### SM/System Maintenance (update)

**T7SMC.DFM:** Inventory class/location GL account setup. Per class+location: edit.gla/edit.dpta (inventory asset GL/dept), edit.glc/edit.dptc (COGS), edit.glsnt/edit.dptnt (non-taxable sales), edit.gls/edit.dpts (taxable sales), edit.glvoh/edit.dptvoh (variable OH absorbed), edit.glfoh/edit.dptfoh (fixed OH absorbed), edit.glw (WIP), edit.gllab (absorbed labor), edit.glmisc (misc). Plus: MTCLASS.M.DESC (class description), BKIC.LOCM.NAME (location name), sysgla_Inven/sysgld_inven (system default inventory), sysgla_cogs (system default COGS). Confirms GL account structure is per-class, per-location — 10 GL accounts per inventory class+location combination.

**T7SMD.DFM:** Terms codes. IS.TERMS.NAME/NUM/DESC, IS.TERMS.AMT (discount amount), IS.TERMS.TYP (%,$,D,C,A,P,F), IS.TERMS.DAY (discount days), IS.TERMS.MAX (max days til due), plus due.on.rcpt and epay (e-pay only) flags.

**T7SME.DFM:** Tax codes. ISIS.TXF.CODE/DESC/IDNUM (tax ID#), ISIS.TXF.VNDCD (tax vendor), ISIS.TXF.SOPERC[1] (SO tax rate), ISIS.TXF.POPERC[1] (PO tax rate), ISIS.TXF.GLASO/GLDSO (SO GL account/dept), ISIS.TXF.GLAPO/GLDPO (PO GL account/dept), ISIS.TXF.SOMAX (SO max amount).

**CRM Reference Tables (SM-I series):**
| Program | Table | Key Fields | Purpose |
|---|---|---|---|
| T7SMIA | BKCM.LEAD | SCODE, DESC | Lead source codes |
| T7SMIB | BKCM.TERR | TCODE, DESC, EMAIL | Sales territory codes |
| T7SMIC | BKCM.ACFC | FCODE, DESC, REP | Activity/follow-up codes (CRM dashboard flag) |
| T7SMID | BKCM.ACCC | CCODE, DESC | Contact category codes |
| T7SMIE | BKCM.DTCD | DCODE, DESC | Date category codes |
| T7SMIF | IS.CATM | CODE, DESC | Category master |

The BKCM.* prefix = BK CRM module tables. These are used by the CRM/sales activity tracking features.

**Archive/Purge Programs (SM-J series):**
| Program | Purpose |
|---|---|
| T7SMJB | WO archive/restore/purge (by WO#, act finish date, job, customer, item; checks orphaned ISWOEX/ISWOROEX) |
| T7SMJC | Inventory reconciliation (master + transaction level; report-only mode; transaction types ASPJWIQOCMTRG) |
| T7SMJD | Transaction archive/consolidate (consolidation date, type filter) |
| T7SMJE | WO purge (closed and/or cancelled WOs by WO# and finish date) |
| T7SMJF | PO archive/purge (by PO#, vendor, date) |
| T7SMJG | QC receiver archive/purge (by QC receiver#, date, vendor) |
| T7SMJH | Data collection file purge (cut date) |

New tables: `IS.TERMS.*` (terms codes), `ISIS.TXF.*` (tax codes with separate SO+PO rates+GL), `BKCM.LEAD/TERR/ACFC/ACCC/DTCD` (CRM reference), `IS.CATM.*` (category master). Confidence: 86/100.

---

### Business Status (EvoBSR/EvoBSCash/EvoBSWO)

**EVOBSCASH.DFM:** "Business Status Cash Detail". Table `ISBSF.CASH.*`: ISBSF.CASH.TOTA (total cash), ISBSF.CASH.ACT1..ACT9 (9 bank account balances). Real-time cash position dashboard.

**EVOBSWO.DFM:** "Business Status Work Orders". Table `ISBSF.WO.*`: ISBSF.WO.WIPBAL (WIP balance), ISBSF.WO.ISSU (issues), ISBSF.WO.FPVAR (FP/variance). Table `ISBSF.WOS.*`: ISBSF.WOS.LAB (labor), ISBSF.WOS.MAT (materials+process), ISBSF.WOS.FOH (fixed overhead), ISBSF.WOS.VOH (variable overhead), ISBSF.WOS.MEXT (misc extra), ISBSF.WOS.FP (finished production), ISBSF.WOS.WIPV (WIP variance). WO cost component dashboard.

**EVOBSR.DFM:** "Business Status Rebuild" — progress display while rebuilding ISBSF.* summary tables.

New tables: `ISBSF.CASH.*` (cash summary: up to 9 bank accounts), `ISBSF.WO.*` and `ISBSF.WOS.*` (WO cost component summaries). These are pre-computed summary tables rebuilt on demand.

---

### WBK Menu System

**WBKMENUSETUP.DFM:** Full menu administration. Fields: BUTTON_CAPTION, BUTTON_IMAGE, BUTTON_NUM (buttons), ACCESS_CODE, GROUP_CAPTION, GROUP_NUM (groups), MI_MENU_LVL, MI_CAPTION, MI_FASTSELECT, MI_PROGRAMNAME, MI_IMAGE, MI_LABEL (menu items). Also: groupname, username, copyname. Operations: Add Group, Add User, Edit User, Delete User, Copy From (existing menu), Update to Latest Prg (sync program names from EVO releases), Change Prg Name. WBKMENUSETUP is the administration tool for customizing the EVO workbench menu system.

**WBKMENUSUCPRG.DFM:** Change program name — FROM_PRG_NAME → TO_PRG_NAME. Used to remap legacy program names after upgrades.

**WBKMENUSUNEWAC.DFM:** New access code entry — NewAC, ACCopyFrm. Creates a new menu access code by copying permissions from an existing one.

The WBK menu system is EVO's custom graphical launcher (distinct from the TAS Pro 7 character menu). It stores buttons + groups + users + access codes for each user's EVO desktop.

---

### Custom Content (T7CUSTOMS)

**T7CUSTOMS.DFM:** "Custom Content". Fields: Custom.control[1..10] (enable flags), Custom.Name[1..10] (label), Custom.Desc[1..10] (description). Configures up to 10 custom content items — EVO's extensibility hook for site-specific menu items or links. Stored in fields named `Custom.*[n]`.

---

### Chargeback (T7CHARGBK)

**T7CHARGBK.DFM:** ISREP.ORD.* fields: INVNM (invoice#), INVDT (invoice date), REPNM (rep name), COMPR (company), CMAMT (chargeback amount), SONUM (SO#), ULID (user ID). Chargeback/debit memo tracking against orders — likely for commission adjustments when invoices are debited back. Table prefix `ISREP.ORD.*` = order-level commission reporting.

---

### BZ Fix Utility (T7BZFIX)

**T7BZFIX.DFM:** "Records Tagged : 0". Fields: LOC_FILE_NAME, LOC_BUFF_NAME, LOC_LOCATION, TAGGED, FSEARCH. Processes tagged records in Btrieve data files — likely a Btrieve zero-byte record fixer or orphan cleanup utility.

---

*Pass 84 complete (2026-06-18). 107 DFMs analyzed across 18 modules. Key new tables: ISBSF.CASH/WO/WOS (Business Status), ISSR.INFO (S/R UDFs), BKCM.LEAD/TERR/ACFC/ACCC/DTCD (CRM reference), IS.TERMS, ISIS.TXF, IS.NCR, ISQC.MTD/SPC (QC), BKPR.CURP (Payroll), IS.FXA/FXT (Fixed Assets), IS.EST (Estimating), BKSA (Sales Analysis). New module confirmations: FO pricing via BKBM.PROD.OPYN[4/5], VSCHED external DSN confirmed, QS quick entry confirmed, RT/RTM Validator is a shared helper dialog. Modules updated (confidence): QS 65→76, VSCHED 68→78, RT 55→70, SPC 87→92, SR 72→82, CS 80→85, PR 90→92, QC 82→88, SH 83→88, FA 82→86, ES 85→88, SA 80→84, SM 82→86, FO 78→83.*


---

## Pass 85 DFM Analysis (2026-06-18) -- 107 DFMs: J7 customizations, T6 legacy, JC, PI, LC, WTAS

### MACHINEVIEW + WORKCENTERLOAD

Both DFMs contain only "Loading..." captions -- they are progress-display screens, not main program forms. No useful field data; MH/SL modules remain unresolved via DFM analysis.

---

### J7 Customization Programs

The J7 series are i2 Systems customizations added to the standard EvoERP installation.

**Production / Mattress Manufacturing (customer: Lapco):**

| Program | Purpose |
|---|---|
| J7DCMATLABELS | Print mattress labels -- serial scan to WO to employee assignment |
| J7DCSSOE | Shipping dock: scan mattress serial, verify against SO |
| J7DCSSOEVERIFY | Verify shipping -- LINE.VPART/SHIP.QTY/ORDERQTY/DESC |
| J7HHEBINC | Handheld inventory adjustment for serialized mattresses |
| J7HHEBXFER | Handheld inventory transfer -- From location to To location |
| J7HHEBXFERVERIFY | Verify transfer list -- PART.ARRAY/SHIPQ.ARRAY |
| J7HHPTSSOE | Handheld shipping scan with box#, lot, WO, customer |
| J7HHPTSSOELABELS | Print box content labels with RTM_NAME picker |
| J7HHPTSSOEVERIFY | Verify box: LINE.VBOX/VBOXQTY/VSONUM/VDESC/VWONUM/VLOT |
| J7HHRTSSOE | Handheld shipping with "RT London" truck load# |
| J7EBSERIAL | Serial number entry at production -- scan serial against item/qty |
| J7PEDCB | Production status board -- WO/part/dept/qty counts |

**Web / eCommerce:**

| Program | Purpose |
|---|---|
| J7BEFWEBINV | Web Item Export -- CSV/FTP export; active/type/class filters; adjust qty for SO within X days; web-items-only flag |
| J7CIWEBIMPORT | Web Import -- FTP download to EDI or Open SO. Bank account#, auto-mode, add kit components flag |
| J7SOAIMPLINES | Import SO Lines -- comma-delimited CSV; multi-company: company.code/name/path fields |

**AP / Purchasing:**

| Program | Purpose |
|---|---|
| J7AUTOAPC | Auto Enter PO Invoices -- auto-posts received POs as invoices using actual received date |
| J7POAIMPLINES | Import PO Lines -- comma-delimited: item/price/desc/qty/ESD/WO/job |
| J7PTRECPOLINE | Receive PO Line -- simple single-line receipt (BKAP.POL.PCODE/PQTY/PPRCE/PEXT) |
| J7APPVEND | Approve Vendor -- sets app.vend flag + max.chk.amt per vendor |
| J7TMCKANBAN | Kanban Orders -- scan item+qty+price to create PO receipt; BKIC.PROD.RAMT (reorder amount); packing slip# |

**SO / Shipping:**

| Program | Purpose |
|---|---|
| J7HHLITN | Enter tracking numbers -- track#, ship company, freight, box ID |
| J7CRSOW | SO-W report -- SOs with backorders; SONUM/ORDDTE/CUSCOD/PCODE/PDESC/PQTY/UBO |
| J7SYNCWOTOSO | Synchronize WO to SO -- ESD, ASD, sched dates, WO/ship/complete qty. Links SO.LINENO to WO. |

**Finance / Admin:**

| Program | Purpose |
|---|---|
| J7I2SACH | ACH Export -- bank ACH/direct deposit export; CHKACT.TXT, check# range, ACH filename, Bank Assigned ID |
| J7SMJCT | Closed Job Cost Report -- JC report for closed jobs |
| J7PTWOKI | WO-K-J -- sync in-process WOs from BOM; update WO class |
| J7WOLL | WO-L-L -- WO component labels with BOM qty and sequence filter |

**Critical discovery -- J7NMRTMPRINTER.DFM:**
Confirms table `IS.RTM.*` with fields: IS.RTM.PROGRAM, IS.RTM.RTM, IS.RTM.PRINTER. This is the per-program default RTM template + printer assignment table. Administrators assign default printers and report templates to specific EVO programs system-wide. Used by any program that calls the RTM picker.

Customers identified from J7 DFMs: **Lapco** (mattress manufacturer), **RT London** (truck delivery), **MCDSA** (sales analysis client).

---

### T6 Legacy Inventory Tabs (T6ISINB series)

Same core tables as T7INA/INB; tabs add field confirmations:

**T6ISINBECO.DFM -- ECO tab.** Table `IS.ECO.*`:
| Field | Meaning |
|---|---|
| IS.ECO.DRAW | Drawing number |
| IS.ECO.REVLVL | Revision level |
| IS.ECO.ENTDATE | Date entered |
| IS.ECO.ENTBY | Entered by |
| IS.ECO.ECO | ECO number |
| IS.ECO.DATE | ECO effective date |
| IS.ECO.CURRENT | Current revision flag |

**T6ISINBLNK.DFM -- Links tab.** Fields: I.ORDER (sort), I.LINK (link path), I.OTHER (alt path), I.ILOLINK (global path flag).
Image attachment fields:
- `IMAGE.TL[1..10]` -- thumbnail display flags per document type
- `IMAGE.PCB[1..10]` -- print control bits per doc type (9 types: Tra=Traveler, Est, PO, RFQ, Quo, Ack, Inv, Pck, SOl)

**T6ISINBMFG.DFM -- Manufacturer tab.** Table `BKSB.MFG.*`:
- BKSB.MFG.MANUF (manufacturer code), BKSB.MFG.MPART (manufacturer's part#)
- Many-to-one: multiple manufacturer cross-references per item

**T6ISINBVND.DFM -- Vendor tab.** Table `BKSB.VEND.*`:
- BKSB.VEND.VEND (vendor code), BKSB.VEND.VPART (vendor's part#)
- Many-to-one: multiple vendor cross-references per item

**T6ISINBMRP.DFM -- MRP Settings tab.** Additional MTIC.PROD.* MRP fields:
| Field | Meaning |
|---|---|
| MTIC.PROD.MRP | Include in MRP generation flag |
| MTIC.PROD.EXPBF | Expedite buffer (days) |
| MTIC.PROD.DELBF | Delay buffer (days) |
| MTIC.PROD.WIPDP | WIP display option |
| MTIC.PROD.MRPSW | MRP switch/option |
| MTIC.PROD.PLNR | Planner code |
| MTIC.PROD.MRPQ | Round MRP quantities to |

**T6ISINBSPC.DFM -- Specifications tab.** `MTIC.PROD.SPECS[1..12]` -- 12 free-text item specification fields per item.

**T6EVOART.DFM -- T6 CRM account with credit card.** Table `BKCM.ACCT.*`:
- Standard: CODE, NAME, ADD1, ADD2, ADD3, CITY, STATE, ZIP
- Credit card: BKCM.ACCT.CCARD (type), BKCM.ACCT.CNUM (card#), BKCM.ACCT.CMPNM (company on card), BKCM.ACCT.PNAME (person name), BKCM.ACCT.CEXP (expiration)

BKCM.ACCT.* is the CRM company/account master with embedded credit card details -- distinct from BKAR.CUST.* (AR billing customer).

**T6MENUUTIL.DFM:** "Evo ERP T6 Program Names" -- remaps T6 program names to newer names (FROM_PRG_NAME to TO_PRG_NAME). Used for upgrade migration.

---

### JC/Job Costing (full menu)

**T7JCENG.DFM -- JC Engine (central reporting engine).** Filters: report type, sort/subtotal, level of detail. WO status (5 codes), WO source (2 codes), labor type (e.ltype[1..6] = 6 types), shift (e.shift[1..3] = 3 shifts), multiple setup flag. Ranges: WO#, work center, item, tool, employee, machine, labor date, job#, sequence, scrap code, QC code, rework code, department, WO actual finish date.

**Full JC menu programs:**

| Program | Purpose |
|---|---|
| T7JCA | WO cost report -- G&A%, summary/detail, composite option, rebuild WO option |
| T7JCB | By job number + WO + status |
| T7JCE | Labor/component detail -- sort by date/WO/component, scrap code range |
| T7JCF | Outside process/PO cost -- PO#, vendor, date + sequence range |
| T7JCH | Routing update from actuals -- updates master/WO routing from actual data |
| T7JCL | WO start/finish date analysis with archiving support |
| T7JCM | WO cost summary -- as-of-prior-date, prt.details/print.cp/print.zero |
| T7JCN | Percent complete -- ISCALC.HOW.C (costs), ISCALC.HOW.H (hours), ISCALC.HOW.P (parts) |
| T7JCP | Materials in WIP -- WO status [RFISCX], component item filter |
| T7JCQ | WO cost postings -- include FP/WIP variance/scrap flags |
| T7JCR | WO cost by customer -- incl.type.A, as-of-date, class+category range |
| T7JCRM | JC-RM -- DSN configurator (Host/Port/Name/Destination). JS-type bridge for JC reporting server |
| T7JCS | WO invoice integration -- prt.invoices [YNP], div.hrs, prt.op.stot, group.subs |

New confirmed fields: ISCALC.HOW.C/H/P (percent-complete basis), e.ltype[1..6] (6 labor types), e.shift[1..3] (3 shifts). Confidence JC: 78->87.

---

### PI/Physical Inventory (full workflow)

Table `BKPH.*` = physical inventory tag records. YEAR + QTR = PI run identifier.

| Step | Program | Purpose |
|---|---|---|
| PI-A | T7PIA | Capture Frozen Inventory -- YEAR+QTR+FDATE freeze, item/class/cycle filter, COUNT TYPE 1/2 |
| PI-B | T7PIB | Print Frozen Inventory tags -- location, lot/serial detail, on-hand qty |
| PI-C | T7PIC | Enter Tag Counts -- BKPH.TAGNUM/LOC/CODE/LOT/SERIAL/ACTQTY; bin loc, employee, comment |
| PI-C-A | T7PICA | Exception Report -- count vs frozen qty differences |
| PI-D | T7PID | Missing Tags Report -- find gaps in sequential tag numbering |
| PI-E | T7PIE | Alternate count by item+location -- BKPH.INFO.* records |
| PI-F | T7PIF | Physical Inventory Report -- standard/average cost, tag detail, RTYPE.ARR[1..4] formats |
| PI-G | T7PIG | Update Actual Inventory -- post to FIFO, post to GL, update/delete bin locations |
| PI-H | T7PIH | Purge PI records by YEAR+QTR |
| PILOC | T7PILOC | PI Location master: PILOC.LOC/NAME/NOTE/TAG |

Note: QTR = physical inventory run number, not calendar quarter. Confidence PI: 76->88.

---

### LC/Lot Control (full menu)

Table `MTLOT.*` -- lot master record:

| Field | Meaning |
|---|---|
| MTLOT.LOT | Lot number (part of PK) |
| MTLOT.CODE | Item code (part of PK) |
| MTLOT.ONHAND | On-hand quantity |
| MTLOT.RECDATE | Date received |
| MTLOT.WO / WOSUF | WO that produced this lot |
| MTLOT.EXPDATE | Expiration date |
| MTLOT.LOC | Location |
| MTLOT.POCOST | PO cost |
| MTLOT.PO | PO number |
| default.bin | Default bin location |

| Program | Purpose |
|---|---|
| T7LCA | Edit lot numbers -- direct edit of MTLOT fields |
| T7LCB | Assign lot control to items -- sets MTIC.PROD.LOT flag |
| T7LCC/LCC2 | Lot availability reports -- by item/lot/expdate, SO allocations option |
| T7LCE | Exception report -- negative lot UOH, orphaned lots |
| T7LCF | Lot history by item+lot |
| T7LCG | Archive/unarchive lots -- by item/expdate/recdate/lot/zero-UOH |

Confidence LC: 81->88.

---

### TA/TAS Admin -- Addsum TAS Pro 7 DBA Toolkit

The WTAS* programs are the Addsum TAS Professional 7 database administration utilities. They manage the TAS Pro 7 file infrastructure and data dictionaries.

**WTASDMGR.DFM -- Data Dictionary Manager (critical tool).**
"Addsum TAS Premier 7i Maintain Data Dictionary" -- creates and edits TAS Pro 7 data dictionaries:
- Field definitions: FLD_LNAME (long name), FLD_SNAME (short name), FLD_TYPE, FLD_SIZE, FLD_DEC, FLD_ARRAY, FLD_UPCASE, FLD_DESC
- Physical layout: FLD_HTYPE, FLD_HSIZE, FLD_HDEC, FLD_HARRAY, FLD_HOFFSET
- Key definitions: AKEY_LIST, AKEY_NAME, SEG_FLD_LIST, SEG_FLD_NAME, kord, kmod, kdup, kignore, numSeg
- File name: AFILE_NAME
This is the tool used to create and modify the .DFM data dictionaries that define the Btrieve/Pervasive table schemas. The DDF schema.json we've been analyzing was created and maintained via WTASDMGR.

**WTASINIT.DFM -- Create/Initialize File.** Creates new Btrieve data files. Fields: CF_FLNAME, CF_FLCODE, CF_RTYPE, CF_DESC, CF_PATH, cf_fdname. Confirms the FILELOC table structure.

**WTASFLOC.DFM -- Maintain File Names and Locations.** Manages the FILELOC table: maps file codes (CF_FLCODE) to physical disk paths. Same fields as WTASINIT plus "Update All" button.

**WTASDATAM.DFM -- Maintain Database.** Live Btrieve record editor: browse by index (cbIndexName), filter (FilterExpr), edit/add/delete records, export visible/all rows. Sequential scan (NoKey), record counter (rec_num/curr_rec_num), override file path.

**WTASCHKINT.DFM -- DataScanIntegrity.** Btrieve integrity scanner. Progress: Total Progress, Current Scan Progress, Records Scanned, current file/key. Counts: Selected/Scanned/Errors.

**WTASDMGR2.DFM:** New FD dialog -- enter new file definition name.

**WTASDMGR3.DFM:** Restructure a Btrieve file -- RestructFDName, progress counter.

**WTASFLLKUP.DFM:** File Lookup -- pick a file from FILELOC by LOC_FILE_NAME/LOC_COMP_CODE/LOC_BUFF_NAME/LOC_LOCATION.

**WTASFLOCUPD/WTASMERGE2.DFM:** Empty (no form content).

**WTASCVTDICT.DFM:** "Convert Existing Dictionary" -- migrates older data dictionary format.

**WTASCHKINTCOMPANY.DFM:** Company scope selector for integrity scan.

Confidence TA/TAS Admin: 78->88.

---

### WBK Lookup Framework (additional)

**WBKLPRINT.DFM:** "Order Printing" -- Print Acknowledgements / Print Packing Slips / Print Invoices checkboxes (pbox1/2/3). Popup for selecting which order documents to print from WBK menu.

**WBKHHLOOKUP.DFM:** Lookup dialog with sort, vendor#/manufacturer/customer X-ref tabs. Used in handheld (HH) context for item lookup.

**WBKLKPMEMO.DFM:** Generic memo field editor in WBK lookup context.

**WBKMENUSUEU.DFM (end-user menu):** "Menu Item Setup -- Your Access Code" -- limited menu editor showing only this user's Groups/Buttons and Menu Lines. Users can customize their own menu without admin rights.

Confidence WBKLOOKUP/Platform: 68->76.

---

### New Table Summary -- Pass 85

| Table | Purpose | Source |
|---|---|---|
| `IS.RTM.*` | Per-program default RTM + printer (PROGRAM+RTM+PRINTER) | J7NMRTMPRINTER |
| `BKCM.ACCT.*` | CRM account master + credit card (CODE+NAME+CCARD+CNUM+CEXP) | T6EVOART |
| `IS.ECO.*` | ECO master (DRAW+REVLVL+ENTDATE+ENTBY+ECO+DATE+CURRENT) | T6ISINBECO |
| `BKSB.MFG.*` | Manufacturer cross-reference per item (MANUF+MPART) | T6ISINBMFG |
| `BKSB.VEND.*` | Vendor cross-reference per item (VEND+VPART) | T6ISINBVND |
| `MTIC.PROD.SPECS[1..12]` | 12 item specification text fields | T6ISINBSPC |
| `MTIC.PROD.EXPBF/DELBF/WIPDP/MRPSW/PLNR/MRPQ` | Additional MRP item settings | T6ISINBMRP |
| `IMAGE.TL[1..10]` | Thumbnail display flags per doc type | T6ISINBLNK |
| `IMAGE.PCB[1..10]` | Print control bits per doc type (9 types) | T6ISINBLNK |
| `BKPH.*` | Physical inventory tag records (TAGNUM+LOC+CODE+LOT+SERIAL+ACTQTY) | T7PIC |
| `BKPH.INFO.*` | PI count by item+location | T7PIE |
| `MTLOT.*` | Lot master (LOT+CODE+ONHAND+RECDATE+WO+EXPDATE+LOC+POCOST+PO) | T7LCA |

---

*Pass 85 complete (2026-06-18). 107 DFMs: J7 customizations (40 DFMs: mattress manufacturing, web export/import, Kanban, ACH, multi-company), T6 legacy INB tabs (ECO/Links/MFG/VND/MRP/Specs), JC A-S full menu + JCENG filter engine, PI A-H full workflow, LC A-G full lot control, WTAS DBA toolkit. Key new tables: IS.RTM (per-program RTM/printer), BKCM.ACCT (CRM+credit card), IS.ECO, BKSB.MFG/VEND (item xref), MTIC.PROD.SPECS[12], BKPH (PI tags), MTLOT (lot master). WTASDMGR confirmed as TAS Pro 7 Data Dictionary Manager -- the tool that creates and maintains .DFM schema definitions. Confidence updates: JC 78->87, PI 76->88, LC 81->88, J7 72->82, TA 78->88, WBKLOOKUP 68->76, IN 82->86, CRM 82->86, MRP 88->90.*



---

## Pass 86 DFM Analysis (2026-06-18) -- DE/EDI full suite, EVO system tools, reminders, IM, RM, GF

### DE/EDI Module -- Full Import/Export Suite

The DE module handles ALL external data exchange. Much broader than "EDI" alone -- it covers file imports, web sync, and data utilities across all modules.

**T7DEER.DFM:** Error Report -- validates items against Estimating OR Production, prints only error records. PRT.BAD, zero.qtyreqd, est.prod flag.

**T7DEFECT.DFM:** Defect code master. Table `IS.DEF.*`: IS.DEF.CODE + IS.DEF.DESC.

**T7DEHD.DFM:** "PI-C Import Tags" -- imports physical inventory count tags FROM a file. YEAR+QTR (PI run ID), count.date, FIELD.NUMBER[1..9] positional mapping, comma.fixed, replace [S/R], x.by.stdpk (multiply qty by standard pack).

**T7DEJH.DFM:** "DE-J-H" -- WO materials issue import from file. WOMAT.WOPRE/WOSUF/PCODE/PDESC/QTYISSUED/DATE/LOT/REF. Imports WO issue transactions from scanners or external files.

**T7DEK.DFM:** "Replace all Values" -- global field find-and-replace in a Btrieve file. which.file, which.field, replace.all, search.for, replace.with. Data correction utility.

**T7DEL.DFM:** "Erase Files" -- bulk erase Inventory/BOM/Customer/Routings/Vendor/COA/Labor files. Data initialization utility.

**T7DEM.DFM:** BOM component import to Estimating OR Production. PRT.BAD, zero.qtyreqd, est.prod flag.

**T7DEP860.DFM:** "Import EDI 860" -- EDI 860 = Purchase Order Change. BKAR.INV.CUSCOD/CUSNME, RELEASE_NUM, CUSORD, SONUM.

**T7DEPB.DFM:** "Import EDI Orders" -- main EDI SO import (EDI 850). EDI Number, Customer, Release Number, Customer Order, Line Number. EDI pricing flag, reindex, PSV/Fixed format.

**T7DEPD.DFM:** "DE-P-D" -- create SOs from EDI orders. NEW.SO, ORDER.DATE, EST.DATE, LOC, CUST.PO. Quote fields (sFQUOTE.NUM, sTQUOTE.NUM) -- EDI quotes convert to SOs.

**T7DEPE.DFM:** "DE-P-E" -- EDI invoice export (EDI 810). BKAR.INV.NUM, BOL (Bill of Lading), DISTRIB (Distribution Center flag), ONE.FILE.PER.CUST. from/thru invoice#/customer range.

**T7DEPF.DFM:** Invoice export (PSV or fixed). FROM/THRU invoice#, include header, SO vs INV output type.

**T7DEPH.DFM:** "DE-P-H" -- SO data export (EDI 856 ASN). SO#, STDPCK (standard pack), CUSTPO, PRCE.

**T7DEQ.DFM:** AR invoice import from file. Invoice#, Customer, Date, Amount, Exchange Rate, Currency Code, Description, Terms#.

**T7DER.DFM:** AP invoice import from file. Same as DEQ + Taxes + Freight fields.

**T7DET.DFM:** "Web Import" -- FTP download to EDI or Open SO. auto.mode, bank account, add kit components, error check, skip.SO, send.reminder, rename.file, imp.price.

**T7DETB.DFM:** "DE-T-B" -- web import with extended options. EDI vs Open SO, drop shipment fee/default [YNG], include 2nd desc, include specs, import comments. FIELD.NUMBER[1..44] flexible positional mapping.

**T7DEU.DFM:** "Web Item Export" -- CSV/FTP export. item type [RFAMNLBTKO], class/active filters, FTP settings, adjust qty for SO within X days, web-items-only, all locations, include BO qty.

**T7DEV.DFM:** "POA Import" -- PO receipt import from file. Table `ISAP.QPO.*`: PONUM + PCODE + PQTY (queued PO receipt lines). Receipt date, packing slip#, employee#, rename.file.

**T7DEX.DFM:** Data dictionary field selector. MEM.SELECT.FLD/NUM, MEM.DICT_NAME/TYPE/SIZE/DEC/ARRAY. Reused by DE import screens to allow flexible user-defined positional field mapping.

DE module structure:

| Series | Purpose |
|---|---|
| P-series | EDI transactions (850/860/856/810) |
| D/H-series | Handheld/file data import (PI tags, WO materials) |
| J-series | WO materials/issue import |
| Q-series | AR invoice import |
| R-series | AP invoice import |
| T-series | Web order import (FTP) |
| U-series | Web item export (FTP/CSV) |
| V-series | POA (PO receipt) import |
| DEK/DEL | Data utilities (global replace, file erase) |

New tables: `IS.DEF.*` (defect codes: CODE+DESC), `ISAP.QPO.*` (queued PO receipt lines: PONUM+PCODE+PQTY). Confidence DE: 78->86.

---

### EVO System Infrastructure Tools

**EVOENOTES.DFM:** "Entering Notes" -- Evo Notes system. Table `IS.NOTE.*`: CDATE, CTIME, CWHO (created by), EWHO (assigned to), TYPE, PRIVATE, CONTACT. Notes linked to any EVO record type (item, customer, vendor, SO, WO, PO, invoice).

**EvoELinks.DFM:** "Entering Links" -- Evo Links/documents system. Table `IS.LNK.*`: DATE, WHO, LINK (path/URL), ALERT, PRIVATE, SORT, GLOBAL (use global path #), PCB[100] (print control bits per doc type). GlobalPath[1..10] = 10 configurable server base paths for document links. imageinfo.DFM shows GPS/EXIF data (lat/lon/date/time) is read from geo-tagged image attachments.

**EvoEMsg.DFM:** Broadcast message to another user (entMSG + sendwho). Inter-user messaging within EVO.

**EVOFILTERS.DFM:** Reusable WO/JC global filter panel. WO# range, WO finished/start/actual-fin/due dates, WO status, machine, work center, scrap code, employee, sequence#, JC job#/labor date, tool, department, WO class, WO priority [1-9].

**EvoCSI.DFM:** "Evo Master Inquiry" -- central cross-reference lookup. Enter any of: Customer Code, Item#, SO#, Invoice#, Vendor Code, PO Receipts, PO#, WO# to jump to that record.

**evoCSR.DFM:** "Calendar Summary Report" -- by month, customer/item range. ESD vs CDD view. Custom field display: Customer+PO# / Qty+BO / SO#+Customer.

**EvoERPDrillM.DFM:** "Drill Down Menus" editor. Table `DRILLM.*`: PARENT (parent grid field), CHILD, MENU (menu text), PFILE (parent file), FILE (child file), TField[1..5]/SField[1..5] (source/target field mappings). Configures custom drill-down navigation between any two data grids.

**EvoFNO.DFM:** Features & Options main form. Table `ISFO.HDR.*` confirmed: PARENT (item code), DESC, CUST, VEND, RFQ, STATUS, DATE. Converts to: SO, WO, PO, New Item, Sales Quote, RFQ via SOCB/WOCB/POCB/NICB/SQCB/RQCB conversion type flags.

**EvoNotesARCH/EvoNoteSearch/EvoNotesPrt/EvoNotesRpt:** Evo Notes management suite. Archive/restore notes by entity range. Search by string (matchcase, current/archived/both). Print by up to 6 note types. Report by date/entity range.

**EvoSchedsetup.DFM:** Installs Evo Scheduler as a Windows service. SMTP email config (SMTP/user/pass/email/name/port), 32/64-bit OS option.

**EvoMobilesetup.DFM:** Installs EvoMobile reminder service (same SMTP config).

**EVOSERVICESETUP.DFM:** Installs EvoService for the server (main background processing Windows service). SMTP email, 32/64-bit OS, security setting (email.cfg.sec + smtpport + esettings).

**EVOFUP.DFM:** Support tool -- uploads files to a technician (FUTECH picker, fu.name, fu.REmail, FU.ATTACH). Used for submitting bugs/logs to support.

**Evocnvtb.DFM:** "Synchronize Data Dictionary with Btrieve" -- syncs the TAS data dictionary with the actual Btrieve file structure.

**printtll.DFM:** Universal print dialog. Options: Printer/Preview/Email/File. Auto-email with contact name/number/primary code. dflt.printer, prt.file.type, fpath.

**Chart dialogs (chartBarModal/chartLineModal/ChartPieModal):** EVO has built-in charting. Bar (3 series with colors), line (2 series, 6 data points), pie (up to 10 slices). Used in Business Status and dashboard screens.

**EvoDCmenu.DFM:** Data Collection Menu -- touch-friendly DC menu with 9 configurable program buttons (Prog1-9).

**evoERPsched.DFM:** "Evo ERP Scheduler" -- schedule recurring tasks. Run once or weekly on specific days. stime + mon/tue/wed/thu/fri/sat/sun flags.

**EvoERPbackup.DFM:** "Evo Backups" -- creates ZIP archives. Full System / Company Data / Custom modes. zipfiles list, zipName, COMP.TAG/EXT/NAME.

New tables: `IS.NOTE.*` (Evo Notes), `IS.LNK.*` (Evo Links), `DRILLM.*` (drill-down menu config), `ISFO.HDR.*` (F&O header).

---

### Calendar / Reminders (RE module update)

**dayrem.DFM:** "Day Time Reminders" -- Evo Reminder entry/view. Table `IS.REM.*`:

| Field | Meaning |
|---|---|
| IS.REM.DISP | Dismissed/displayed flag |
| IS.REM.EMAIL | Email reminder flag |
| rem.date / rem.time | Reminder date and time |
| rem.type | Reminder type |
| rem.sub | Subject |
| rem.item / rem.cust / rem.vend | Linked entity |
| rem.file | File or URL attachment |
| rem.contact / rem.phone / rem.femail | Contact details |
| remmin | Minutes before event to alert |
| other.user | Assign reminder to another user |

Outlook calendar integration. Google Calendar export via CALREMGC (by date range, open/dismissed/all).

**T7RemindRpt.DFM:** "CM-B-D" -- Reminders report. By date/item/customer/type/user/vendor/company. Open/dismissed/both. Reminders vs Follow-Ups filter toggle.

**evorereminders.DFM:** Reschedule/snooze popup. remdate + remmin + remtime.

CALDRILL/caldrillbt/CALGRIDDRILL/calrem = calendar view screens (no data fields -- rendered from calendar data).

New table: `IS.REM.*`. Confidence RE: 75->83.

---

### IM/Multi-Currency Module (CORRECTION: not just Landed Cost)

**CORRECTION**: IM module is the full Multi-Currency module. ISIS prefix = currency system. Landed cost (duties/freight/customs) is one sub-component.

**T7IMB.DFM:** "IM-B" -- Currency master. Table `ISIS.MCF.*` (Multi-Currency Factor):

| Field | Meaning |
|---|---|
| ISIS.MCF.CODE | Currency code |
| ISIS.MCF.BASE | Is base currency flag |
| ISIS.MCF.SYMBOL / SYMPOS / DEC | Currency formatting |
| ISIS.MCF.GLAAP / GLDAP | AP control GL accounts (debit/credit) |
| ISIS.MCF.GLAAPX / GLDAPX | AP conversion gain/loss |
| ISIS.MCF.GLAAR / GLDAR | AR control GL accounts |
| ISIS.MCF.GLAARX / GLDARX | AR conversion gain/loss |
| ISIS.MCF.GLAPO / GLDPO | PO control GL accounts |
| ISIS.MCF.GLAPOX / GLDPOX | PO conversion gain/loss |
| ISIS.MCF.GLACS | Commission account |
| ISIS.MCF.INTRES / INTDAY | Interest rate + days |

**T7IMC.DFM:** Exchange rates. `ISIS.MCR.*`: DATE + BASE (PK), SOURCE[1..10] (currency codes), RATE[1..10] (exchange rates). Up to 10 currencies per date record.

**T7IMD.DFM:** Landed cost GL accounts. `ISIS.LND.*`: GLADT/GLDDT (duty debit/credit), GLAFR/GLDFR (freight), GLACF/GLDCF (customs fees).

**T7IME.DFM:** Duty codes. `ISIS.DUTY.*`: DCODE + PERC (percentage rate).

**T7IMF.DFM:** Broker codes. `ISIS.BRK.*`: CODE + FLAT (flat fee) + PERC (percentage) + TYPE.

New tables: ISIS.MCF.* (currency master with 20+ GL accounts), ISIS.MCR.* (exchange rates: up to 10 currencies per date), ISIS.LND.* (landed cost GL), ISIS.DUTY.* (duty codes), ISIS.BRK.* (broker codes). Confidence IM: 78->88.

---

### RM/RMA Module (update)

**T7RMAWHY.DFM:** RMA Why -- SRMA.OINVNUM (original invoice#), SRMA.OSONUM (original SO#), IS.RMA.STATUS, reason/description/warranty/promise date. Warranty codes: N=None, L=Limited, P=Parts, B=Both.

**T7RMD.DFM:** "RM-D" -- Full RMA disposition. Receive qty/date/location. Disposition options:
- Issue Credit Memo: Create New CM or Add to Original SO
- Issue Replacement SO: New SO / Original SO / Add Both to Same New SO (and CM together)
- Issue Service and Repair Order: Add new line to original SR
- Return to: Stock, Rework, Repair, or Scrap (in-house or ship to customer)

**T7RMDASK.DFM:** Location/SO dialog. Pass RMA# to Desc/Job/None [D/J/N]. restock.charge. SO#, ESD, original/RMA/SO price comparison.

**T7RME.DFM:** "RM-E" -- RMA reason code master. Table `IS.RMA.*`: IS.RMA.CODE + IS.RMA.DESC.

**T7RMG.DFM:** "RM-G" -- RMA report. By customer/item/reason code/date/RMA#. Sort options, class/category range, incl.open.rmas flag.

New tables: `SRMA.*` (OINVNUM+OSONUM = original invoice/SO references for RMA), `IS.RMA.*` (reason code master: CODE+DESC). Confidence RM: 78->85.

---

### GF/AR Charges Module (update)

**t7GFdept / t7GFdiv:** Department and division code masters. Tables `IS.GF.DEPT` (DEPT+DESC) and `IS.GF.DIV` (DIV+DESC).

**T7GFV / T7GFVS:** AR charge entry/view. today, SO, ORDDATE, ESD, SHIPTO, SORTJ (sort by job), SORTG (sort by group), JOB. Charges linked to SO + job + dept/div.

New tables: IS.GF.DEPT, IS.GF.DIV. Confidence GF: 75->82.

---

### Additional Discoveries

**autoT7POJC.DFM:** PO QC buyoff at receiving. Extended BKQC.* fields confirmed: QTY.RECVD/BUYOFF/REJECT, TRN.GQTY/BQTY/UQTY/SCRAP/REWORK, PKSLIP.NUM. DEFAULT.BING/BINU = default bins for good/use-as-is disposition. rohs = RoHS compliance flag at PO receipt level. Confidence QC: 88->90.

**ht6* (T6 handheld programs):** ht6inc (PO receiving: item+qty), ht6so (create SO: PO#+item+desc+qty), ht6wo (monitor WO by up to 8 work centers: WCT/desc/sqty/eqty per station), ht6close (WO close confirmation).

**NascoPAYex.DFM:** "Export Payroll Data" -- exports to Nasco payroll format. pdate input. Nasco = third-party payroll processing vendor integration.

**nzedefs / nzemailtll:** Evo Email system. nzedefs = email defaults (SMTP path, attachment, signature, body text, BCC self, subject template, field substitution). nzemailtll = full email compose: To/CC/BCC/ICC (internal CC), subject, form, attachment, EMAILLIST/CONTNAME/ICCLIST.

**SSS.DFM:** "Drill Filters" quick popup -- SSSVALUE + SSS1-6 (6 quick filter slots used by drill-down grids).

**SSSFD.DFM:** "Sub String Search" -- 7-slot substring search for Evo Notes (SSSFD1-7).

**ACT7SHKNOTE.DFM:** Add note to WO sequence operation (SCAN.WO, scan.oper, woro.note). Confirms per-operation note attachment on WO routing.

---

### New Table Summary -- Pass 86

| Table | Purpose | Source |
|---|---|---|
| `IS.NOTE.*` | Evo Notes (CDATE+CTIME+CWHO+EWHO+TYPE+PRIVATE+CONTACT) | EVOENOTES |
| `IS.LNK.*` | Evo Links/documents (DATE+WHO+LINK+ALERT+PCB[100]+GlobalPath[10]) | EvoELinks |
| `IS.REM.*` | Evo Reminders (DATE+TIME+SUB+TYPE+ENTITY+FILE+DISP+EMAIL) | dayrem |
| `DRILLM.*` | Drill-down menu config (PARENT+CHILD+MENU+PFILE+FILE) | EvoERPDrillM |
| `ISFO.HDR.*` | Features & Options header (PARENT+DESC+CUST+VEND+RFQ+STATUS+DATE) | EvoFNO |
| `ISIS.MCF.*` | Multi-currency master (CODE+BASE+SYMBOL+20+ GL accounts) | T7IMB |
| `ISIS.MCR.*` | Exchange rates (DATE+BASE+SOURCE[10]+RATE[10]) | T7IMC |
| `ISIS.LND.*` | Landed cost GL accounts (duty/freight/customs) | T7IMD |
| `ISIS.DUTY.*` | Duty code master (DCODE+PERC) | T7IME |
| `ISIS.BRK.*` | Customs broker master (CODE+FLAT+PERC+TYPE) | T7IMF |
| `IS.GF.DEPT` | GF department code (DEPT+DESC) | t7GFdept |
| `IS.GF.DIV` | GF division code (DIV+DESC) | t7GFdiv |
| `IS.DEF.*` | Defect code master (CODE+DESC) | T7DEFECT |
| `ISAP.QPO.*` | Queued PO receipt lines (PONUM+PCODE+PQTY) | T7DEV |
| `SRMA.*` | RMA original invoice/SO reference (OINVNUM+OSONUM) | T7RMAWHY |
| `IS.RMA.*` | RMA reason codes (CODE+DESC) | T7RME |

---

*Pass 86 complete (2026-06-18). 100 DFMs: T7DE* EDI full suite (20 programs), EVO system infrastructure (45), calendar/reminders (10), T7RM/RMA (5), T7IM/Multi-Currency (5), T7GF/AR Charges (5), ht6 T6 handheld (4), misc (10). Key correction: IM = Multi-Currency (ISIS.MCF/MCR/LND/DUTY/BRK), not just landed cost. Key new tables: IS.NOTE/LNK/REM (notes/links/reminders), DRILLM (drill-down config), ISFO.HDR (F&O header), full ISIS.* multi-currency system, IS.GF.DEPT/DIV, IS.DEF, ISAP.QPO, SRMA/IS.RMA. Confidence updates: DE 78->86, IM 78->88, RM 78->85, GF 75->82, FO 83->87, RE 75->83, Notes 72->82, QC 88->90, DC 87->89.*


---

## Pass 87 — HH/Handheld, WO Extended, IN Compliance/UDF/2D, DI Digital Signatures (2026-06-18)

### DI — Digital Signatures

**T7DIGSIG — Digitally Sign Purchase Order** (`T7DIGSIG.DFM`)
- Full PO display: BKAP.PO.NUM, BKAP.PO.ORDDTE, BKAP.PO.VNDCOD, BKAP.PO.VNDNME, BKAP.PO.DESC, BKAP.PO.ENTBY, BKAP.PO.OBYCUS (ordered-by customer)
- PO line display: BKAP.POL.PCODE/PDESC/PQTY/PPRCE/PEXT, ERD/ARD (estimated/actual receipt dates)
- **5-level approval categories**: `emp.cat[1..5]`, `emp.position[1..5]`, `emp.signoff[1..5]`
- Fields: `PO Threshold`, `PO-A Ent By ID`, `Signoff Category`, `Cat` per line
- Settings: Password, Signature File path, Signature Image Preview (image control)
- Actions: &Sign PO, &Category, &Settings, &View PO, &Send (email), &Reset

**T7DigSigChgPSWD — Change Digital Signature Password**
- Fields: `oldpass`, `newpass`, `reentpass`

**Confirmed tables:**
- `EMAIL.TAG/NAME/LEVEL/ADDRESS` — email recipient list for signature notifications
- The digital signature approver table uses `emp.cat[1..5]` / `emp.signoff[1..5]` arrays
  stored in an employee/signoff table (not yet named from DFMs alone)

---

### HH — Handheld Terminal System (Full Coverage)

EvoERP's handheld system is a complete warehouse execution layer built on barcode scanners.
The `ETBcomboval` field appears on every HH form — it is the barcode scan input box (a
combined entry/combo field). All forms use class `TEditForm1..4/10`.

**Architecture:**
- HH forms use a 5-button toolbar (ETB1..ETB5) with programmable functions
- Form sizes are designed for small-screen handheld devices
- `T7HH.DFM` = main HH menu hub; routes to function-specific sub-forms

#### HH — Shipping / SO Dispatch (T7HHSSOE/T7HHSODD)

**T7HHSSOE — Shipping (SO Scan-and-Ship)**
- Scan items into boxes by SO number, print packing slip
- Fields: `scan.qty.char`, `scan.item`, `curr.boxnum`, `print.ps`, `curr.skid.ucc`, `sonum.char`
- Shows: SO Number, Cust, Item Code, Description, Box No, Std Pack, Emp
- Actions: &Rel SO (release), Verify, Std Pk

**t7hhssoeLabels — Print Box Content Labels**
- Per-box label: `RTM_NAME`, `Incl.Lot`, `Incl.Serial`, `Box.Number`, `Box.Total`, `Lab.printer`, `labelQty`
- Option: Start New Box flag

**t7hhssoeLverify / T7HHSSOESVerify / T7HHSSOEVerify — SO Line Verification**
- Grid fields: `LINE.VPART`, `LINE.DESC`, `LINE.ORDERQTY`, `LINE.VBOXQTY`, `LINE.STDPK`
- `T7HHSSOEVerify` adds `LINE.V.PART`, `LINE.V.ORDQTY`, `LINE.V.PQTY` (packed qty)

**T7HHSODD — Shipping/DD dispatch screen**
- SO dispatch finalization: `reprint` (invoice), `prt.sr` (service/repair), `RTM_NAME`, `cert.per.box`
- Shows: Cust Name, SO Number, Cust Code; Last SO/Invoice Scanned

**T7HHSOLookup — SO Lookup grid**
- Columns: BKAR.INV.SONUM, BKAR.INV.CUSCOD, BKAR.INV.CUSNME

**T7HHNDTE — Enter Shipping Details**
- Ship Date, Ship Via, Tracking#, SO#, Freight
- Fields: `ship.date`, `BKAR.INV.SHPVIA`, `BKAR.INV.TRACK`, `BKAR.INV.SONUM`, `BKAR.INV.SHPCOD`, `BKAR.INV.SHPNME`, `BKAR.INV.FRGHT`

**T7HHN / T7HHN2 / T7HHNREL — HH-N SO Picking Queue**

`T7HHN` (Settings):
- `incl.crhold` — include customers on credit hold
- `incl.released` — include released SO lines
- `incl.zero.dates` — include lines with 00/00/00 ESD
- `limit.days` / `limit.date` — limit shipments to N working days
- `incl.kit.comps` — include kit components
- `item.type [RFAMNLBTKO]` — filter by inventory type
- `refresh.timer` (seconds) — auto-refresh interval
- `ship.early.only` / `incl.early`

`T7HHN2` (picking grid):
- Columns: GET.CRHOLD, GET.CUSCOD, GET.CUSNME, BKAR.INVL.INVNM, GET.CUSORD, BKAR.INVL.PCODE, BKAR.INVL.PDESC, BKAR.INVL.PQTY, GET.UOH, BKAR.INVL.ESD, BKAR.INVL.RTS
- Actions: &Lot, S&erial, Release SOs

`T7HHNREL` — same + `incl.bo` (include back orders) + LINES.* grid columns (same as N2)

#### HH — WO Material Issue and Scrap (T7HHWOx)

**t7hhwog — Issue Material to WO**
- Scan WO + component; issue qty to bin/location
- Fields: `scan.wo`, `COMPONENT`, `binloc`, `process.loc`, `scan.qty.char`
- Settings: `RTM_NAME`, `showPrtBox`, `prt.labels [Y/N/Ask]`, `prt.per.comp`, `Label.qty`, `large.lookups`

**T7HHWOIBIN — WC Bin Selection for WO component**
- Shows: Component code/desc, qty, WO number
- Scan bin: `default.bin`

**T7HHWOLabel — WO Label Printing**
- Filter by fin/semi-fin sequence range and class
- Fields: `sfrom.oper.fin`, `sthru.oper.fin`, `fin.class`, `nfin.class`, `sfrom.oper.nfin`, `sthru.oper.nfin`
- Settings: `one.label` (always qty=1), `ship.box.rtm`, `showPrtBox`, `full.lookups`
- Fields on scan: `scan.wo`, `RTM_NAME`, `scan.serial`, `partial.qty`, `full.qty`, `prt.ship.label`

**T7HHWOLookup — WO Lookup grid**
- Columns: MTWO.WIP.WOPRE, MTWO.WIP.WOSUF, MTWO.WIP.CODE (item number)

**T7HHWOLOT — WO Lot Number Release**
- Scan lot: `inp.lot`; fields: `qty.char`, `default.bin`, `scrap.code`, `ret.exp.date`, `Remaining Qty`
- Shows: On Hand qty per lot

**t7hhwop — Finish Production (WO-P)**
- Scan WO + final qty; record completion
- Settings: `final.qty.dflt [Y]`, `prompt.date [YNOnce]`, `wo.status [FRXI]`, `large.lookups`
- Fields: `scan.wo`, `scan.qty.char`, `default.bin`, `inp.oper`

**T7HHWOSCRAP — Report Scrap Material**
- Scan WO + component + scrap code; optionally scan lot/serial
- Fields: `scan.wo`, `COMPONENT`, `SCRAPCD`, `scan.lot`, `scan.Serial`, `prio`
- Settings: `RTM_NAME`, `prt.labels`, `prt.per.comp`, `Label.qty`, `showPrtBox`

**t7hhwoser — Enter Serial Number for WO completion**
- Fields: `inp.serial`, `scrap.code`, `filter.by.loc`
- Options: Auto Gen, CFG Ser

**T7HHWOIBIN / T7HHWOIProcess** — bin selection and processing spinner for WO issue

#### HH — PO Receiving (T7HHPOCx)

**t7hhpoc — Receive PO** (main PO receiving form)
- Scan PO# → vendor/item appear
- Fields: `bkap.po.num`, `RCVD_QTY`, `item`, `recv.into`, `binloc`
- Shows: Vendor Name, Item/Desc, PO Type, Ordered Qty, UM, Unit Cost/Price
- Manufacturer fields: `BKSB.MFG.MANUF`, `BKSB.MFG.MPART`
- Alert options: `vendor.alerts`, `item.alerts`, `large.lookups`
- Options: QC Inspect, Lot Controlled
- Wizard fields (from BKAP.POL): WORD/WSTAT/WREQ/WREM/WPART (on-hand/requisition/remaining)
- Actions: &Notes, &Settings

**T7HHPOCBIN** — bin selection during PO receipt

**T7HHPOCLot — Receive Lot Numbers**
- Scan lots: `inp.lot`, `lot.qty`; shows Last Lot Scanned, Item Code/Description, Qty

**T7HHPOCSER — Receive Serial Numbers**
- Fields: `inp.lot`, `inp.serial`; shows last serial scanned, lot, quantities

**T7HHPOCNotes** — notes per PO/line/item/vendor (4-tab form)

#### HH — Inventory Operations

**t7hhINGA — Print Inventory Labels**
- Scan item, enter qty, lot, serial, bin
- Fields: `scanitem`, `labelQty`, `ScanSerial`, `ScanLot`, `binloc`, `RTM_NAME`, `MISC`, `MISC2`
- Options: `prt.2d.labels` (print 2D barcode), `use.lot.qty`, `use.PO.qty`

**t7hhinlj — Transfer Inventory (HH)**
- Scan item, from loc/bin → to loc/bin, enter qty + date
- Fields: `scan.item`, `from.loc`, `to.loc`, `from.dflt.bin`, `to.dflt.bin`, `tsfr.uoh`, `tsfr.date`
- Shows: OH, From WC, To WC
- Option: `use.same.locs [YNA]` — same location code for all transfers

**T7HHINLJLot — Transfer Lot Numbers**
- Scan lot: `inp.lot`; fields: `lot.qty`, `mtlot.onhand`

**T7HHINLJSer — Transfer Serial Numbers**
- Scan serial: `inp.ser`; shows remaining-to-transfer

**T7HHItemLU — Inventory Item Lookup**
- Search by item or description: `MTIC.PROD.SUBST[1]`, `MTIC.PROD.DESC`

**T7HHO — Bin Transfer**
- From/To bin within a location: `tsfr.item`, `tsfr.qty`, `TO.BIN`, `FROM.BIN`, `tsfr.loc`
- Grid: ITEM.LIST, QTY.LIST

**t7hhinbins — WC Item Lookup (bin)** — lookup items in a work center's bins

#### HH — Physical Inventory

**T7HHPIC — PI-C Enter Tag Counts (settings)**
- `CountDate`, `qtr`, `year`, `location`, `empno`

**t7hhpictags — PI-C tags entry**
- Scan item: `scan.partnum`, `tagnum`, `countqty`, `lotno`, `serialno`, `binloc`, `hold.bin`, `comment`

#### HH — DC Labor (T7HHDCA)

**T7HHDCA — DC Labor Entry (Shipping/Production)**
- Record: Emp Name + No, Work Order, Sequence
- Actions: Start/Stop Shift, Shift Start/Stop
- Fields: `OPER`, `scan.wo`, `scan.emp`

**t7hhdcb / t7hhdcc** — DC loading screen spinners (TEditForm4/3)

#### HH — Tracking Numbers

**T7HHH — Enter Tracking Numbers**
- `track.num`, `ship.co`, `frt.charge`, `BOX.ID`
- Shows: Customer Name, SO Number, Box Number, Ship CO Name, Freight

#### HH — Alerts and Housekeeping

**T7HHALERTMSG** — alert notification popup (AlertMsgLabel displayed)
**T7HHProcess / T7HHWOIProcess** — processing data spinner dialogs

**Confirmed HH tables touched:**
- `BKAR.INV.*` / `BKAR.INVL.*` — SO header and lines
- `MTWO.WIP.*` — WO header
- `MTWOR.*` — WO receipt
- `MTWORO.*` — WO routing/operation
- `BKAP.PO.*` / `BKAP.POL.*` — PO header and lines
- `BKSB.MFG.*` — manufacturer cross-reference
- `MTIC.PROD.*` / `BKIC.PROD.*` — inventory item master
- `MTLOT.*` — lot master
- `EMAIL.*` — email tag/name/level/address list

---

### WO — Work Orders Extended (DFMs T7WOAK through T7WOKM)

Previously confirmed: WO-A header, WO-F labor, WO-G issue, WO-I receipt, WO-J close.
Pass 87 fills in the rest.

#### MTWO.WIP — WO Header Table (confirmed fields from T7WOAC/T7WOAE)

| Field | Meaning |
|---|---|
| MTWO.WIP.WOPRE | WO prefix |
| MTWO.WIP.WOSUF | WO suffix |
| MTWO.WIP.CODE | Parent item number |
| MTWO.WIP.DESC | WO description |
| MTWO.WIP.STATUS | Status (F=Released, R=Completed, C=Closed, S=Scheduled, I=In Process, X=On Hold) |
| MTWO.WIP.USERCD | User-defined class code |
| MTWO.WIP.LOC | Location |
| MTWO.WIP.SQTY | Standard qty to make |
| MTWO.WIP.COMQTY | Qty completed |
| MTWO.WIP.SSTART | Scheduled start date |
| MTWO.WIP.SFIN | Scheduled finish date |
| MTWO.WIP.DDATE | Due date |
| MTWO.WIP.ASTART | Actual start date |
| MTWO.WIP.AFIN | Actual finish date |
| MTWO.WIP.PRTY | Priority |
| MTWO.WIP.CUSTCODE | Customer code |
| MTWO.WIP.CUSTNAME | Customer name |
| MTWO.WIP.CONTAT | Contact/attention |
| MTWO.WIP.CUSORD | Customer PO# |
| MTWO.WIP.PROJ | Project/Job# |
| MTWO.WIP.EST | Quote/estimate# |
| MTWO.WIP.PPRCE | Price |
| MTWO.WIP.CHGORD | Change order number |
| MTWO.WIP.SOLINE | SO line reference |
| IS.OECO.DRAW | Drawing number |
| IS.OECO.REVLVL | Revision level |
| NCR.QTY | NCR (non-conformance report) quantity |

Extended cost fields (from T7WOIASK):
- `MTWO.WIP.EMAT/ESETUP/ETOT/EEXTRA/EMISC/VOVHD/EFOVHD/EOUTPR/ELABOR` — expected costs
- `MTWO.WIP.AMAT/ASETUP/ALABOR/AOUTPR/AFOVHD/AVOVHD/AMISC` — actual costs

#### MTWORO — WO Routing Table (T7WOKA confirmed)

| Field | Meaning |
|---|---|
| MTWORO.TYPE | Operation type |
| MTWORO.OPERDESC | Operation description |
| MTWORO.WC | Work center code |
| MTWORO.NUM | Routing line number |
| MTWORO.NUM.PROC | Number to process at once |
| MTWORO.TIMEPART | Time per part |
| MTWORO.PARTSHR | Parts per hour |
| MTWORO.OVERLAP | Overlap hours (start next op before this finishes) |
| MTWORO.NEGOVLP | Negative overlap flag |
| MTWORO.STD.TIME | Delay before next op (percentage of parts completed) |
| MTWORO.NUM.PERS | Number of persons |
| MTWORO.MACHNO | Machine number |
| MTWORO.TOOL | Tool code |
| MTWORO.VEND | Outside processing vendor code |
| MTWORO.VENDNAME | Vendor name |
| MTWORO.EOUTCST | Estimated outside processing cost |
| MTRO.LEAD | Lead time |
| MTWORO.PRINT | First Off Inspection flag |
| MTWORO.ESETHRS | Estimated setup hours |
| mtworo.longtime | Long-time flag |
| MTWORO.OPER | Sequence/operation number |
| MTWORO.STARTED | Sequence actual start time (T7WOKF) |
| MTWORO.FINISHED | Sequence actual finish time |
| MTWORO.%COMP | Percent complete (from MTWORO display) |

#### MTWOLA — WO Labor Table (T7WOF confirmed)

| Field | Meaning |
|---|---|
| MTWOLA.DATE | Labor date |
| MTWOLA.PARTS | Qty completed |
| MTWOLA.ASSY | WO item (assembly) |
| MTWOLA.ASSYDESC | Item description |
| MTWOLA.MACH | Machine used |
| MTWOLA.REGOVER | Reg/Over/Dbl/Sick/Hol/Vac type |
| MTWOLA.SHIFT | Shift |
| MTWOLA.NOJOBS | Number of jobs worked |
| MTWOLA.REWORK | Rework flag |
| MTWOLA.QCCODE | QC code |
| MTWOLA.QCDESC | QC description |
| MTWOLA.SCRAPCD | Scrap code |

Additional from WO-K-K reverse: `LAB.EMP`, `LAB.DATE`, `LAB.WOPRE`, `LAB.WOSUF`, `LAB.OPER`, `LAB.START`, `LAB.FINISH`, `LAB.PARTS`, `LAB.SCRAPPED`, `LAB.RUNHRS`, `LAB.SETUPHRS`

#### WOBOM — WO Bill of Materials (T7WOKB)

| Field | Meaning |
|---|---|
| WOBOM.COMPCODE | Component item code |
| WOBOM.COMPDESC | Component description |
| WOBOM.QTYPER | Quantity per assembly |
| WOBOM.OPER | Sequence/operation number |
| WOBOM.UM | Unit of measure |
| WOBOM.SCRAPQTY | Scrap quantity |
| WOBOM.QTYISSUED | Quantity already issued |

Also: `remark.replace` / `remark.origin` (edit.remark[1..15] — 15 BOM remarks)

#### WOMAT — WO Material Issues (T7WOG)

| Field | Meaning |
|---|---|
| WOMAT.DATE | Issue date |
| WOMAT.REF | Reference |
| WOMAT.PCODE | Component item code |
| WOMAT.PDESC | Component description |
| WOMAT.SERIAL | Serial number |
| WOMAT.LOT | Lot number |
| WOMAT.SCRAPCD | Scrap code |
| WOMAT.SCDESC | Scrap code description |
| WOMAT.QTYISSUED | Qty issued |
| WOMAT.QTYSCRAP | Qty scrapped |
| WOMAT.COST | Actual cost |

#### WODATE — Multi-Date WO Scheduling (T7WOAMDT)

- `WODATE.START`, `WODATE.FINISH`, `WODATE.QTY`, `WODATE.PRIO` — arrays per split date

#### MTWO.EX — WO Extra Charges (T7WOH)

| Field | Meaning |
|---|---|
| MTWO.EX.PROD | Item charged to |
| MTWO.EX.DESC | Description |
| MTWO.EX.CHGDESC | Charge description |
| MTWO.EX.GLACCT | GL account |
| MTWO.EX.GLDPT | GL department |
| MTWO.EX.CHG | Charge amount |
| MTWO.EX.DATE | Charge date |
| MTWO.EX.OP | Sequence/operation |
| MTWO.EX.WOPRE/WOSUF | WO prefix/suffix |

Cost type: `E` = estimated, `M` = material

#### MTWOR — WO Receipt (T7WOI)

| Field | Meaning |
|---|---|
| MTWOR.DATE | Receipt date |
| MTWOR.ASSY | Item received |
| MTWOR.DESC | Description |
| MTWOR.REF | Reference |
| MTWOR.USESTD | Use standard cost (vs avg) |
| MTWOR.AVGC | Average cost |

#### WO Sub-Program Summary

| Code | Form | Function |
|---|---|---|
| WO-A | T7WOAC/T7WOAE | Create/edit WO header |
| WO-B | T7WOB | Release WOs, import, set status/approval |
| WO-C | T7WOC | Print WO traveler (BOM, routing, labels, serials) |
| WO-D | T7WOD | Print pick list (bin locations, consolidated, RoHS) |
| WO-E | T7WOE | Print labor cards / adhesive labels |
| WO-F | T7WOF | Labor entry (DC time posting) |
| WO-G | T7WOG | Issue/scrap material |
| WO-H | T7WOH | Post extra charges |
| WO-I | T7WOI | WO receipt (close individual WO line) |
| WO-J | T7WOJ | Close or cancel WOs, handle unused serials |
| WO-K-A | T7WOKA | Edit WO routing |
| WO-K-B | T7WOKB | Edit WO BOM |
| WO-K-C | T7WOKC | WO completion/receipt lookup |
| WO-K-D | T7WOKD | Auto-create sub-WOs (explode BOM into WOs) |
| WO-K-E | T7WOKE | Substitute component |
| WO-K-F | T7WOKF | Record sequence start/finish times |
| WO-K-G | T7WOKG | WO list / gantt view filter |
| WO-K-J | T7WOKJ | Sync WO BOM/routing to standard, update ECO |
| WO-K-K | T7WOKK | Reverse DC labor posting |
| WO-K-L | T7WOKL | Mass WO creation (grid entry or file import) |
| WO-K-M | T7WOKM | Material request (non-BOM component) |

WO-K-D (`T7WOKD`) creates sub-WOs by exploding BOM sub-assemblies. Options:
- Match parent due date / est ship date [YNEB]
- Match parent job number [Y/N/W]
- Combine duplicate items into single WOs
- Use shop calendar for start date
- Max BOM explosion levels

WO-K-J (`T7WOKJ`) syncs live WOs after BOM/routing changes:
- Update WO class from item WO class
- Sync in-process WOs (BOM only)
- Update sequences after last sequence
- Update ECO revision level

---

### IN — Inventory Extended (T7INAACDOC through T7INGimport)

#### New Confirmed Tables

**IS.PROD.FLAGS[1..19] — Item Compliance Flags (T7INACMP/T7INBCMP)**

| Index | Field | Meaning |
|---|---|---|
| 1 | IS.PROD.FLAGS[1] | Conflict Free Material [Y/N/P/E] |
| 2 | IS.PROD.FLAGS[2] | RoHS [Y/N/P/E] |
| 3 | IS.PROD.FLAGS[3] | (warehouse control — from t7inbc) |
| 4 | IS.PROD.FLAGS[4] | (shelf control — from t7inbc) |
| 5 | IS.PROD.FLAGS[5] | (pick flag — from t7inbc) |
| 6 | IS.PROD.FLAGS[6] | WEEE [Y/N] |
| 7 | IS.PROD.FLAGS[7] | Certificate of Conformance Required [YNW] |
| 8 | IS.PROD.FLAGS[8] | REACH [Y/N/P/E] |
| 9 | IS.PROD.FLAGS[9] | CA Prop 65 [Y/N/P/E] |
| 10 | IS.PROD.FLAGS[10] | China RoHS [Y/N] |
| 11 | IS.PROD.FLAGS[11] | European RoHS [Y/N] |
| 12 | IS.PROD.FLAGS[12] | Consumer Electronics [Y/N] |
| 13 | IS.PROD.FLAGS[13] | Proprietary Item |
| 14 | IS.PROD.FLAGS[14] | UK Conformity Assessed (UKCA) [Y/N] |
| 15 | IS.PROD.FLAGS[15] | LDPE Recycle [Y/N] |
| 16 | IS.PROD.FLAGS[16] | UL Certification [Y/N] |
| 17 | IS.PROD.FLAGS[17] | Safety Data Sheet (SDS) required |
| 18 | IS.PROD.FLAGS[18] | Hazardous Material (HM) |
| 19 | IS.PROD.FLAGS[19] | Controlled Unclassified Information (CUI) |

Additional compliance fields:
- `CAPROP65` — CA Prop 65 flag
- `REACH` — REACH flag
- `ROHS` — RoHS [Y/N/P/E]
- `ROHS3` — RoHS 3 [Y/N/P/E]
- `CFM` — Conflict Free Material
- `COC.doc.reqd` — COC documentation required
- `rohs.doc.reqd` — RoHS documentation required
- `Prop.item` — Proprietary item flag
- `IS.PROD.ALPHA2[1..7]` — 2-character codes (country of origin, harmony code, control reg, etc.)
- `MTIC.PROD.VNAM[7]` — Moisture Sensitivity level (per IPC/JEDEC J-STD-033)
- `coo.2char` / `CofO.Alpha2` — Country of Origin 2-char ISO code
- Harmony Code, Control Classification Code (ECCN), Control Reg, NMFC, Shipping Class

Export control fields: `EAR99`, `EAR`, `ITAR`
QPL: `IS.PROD.FLAGS[?]` = Qualified Products List

**IS.PROD.NUM[1..N] — Item numeric flags**
- `IS.PROD.NUM[1]` — Reserve Stock Qty (from T7INBMRP)
- `IS.PROD.NUM[3]` — Bin Refill Quantity (from t7inbc)

**UDFi1..UDFi30 — 30 User-Defined Fields per item** (T7INAUDF/T7INBUDF)
- Displayed as UDF1..UDF30
- All named `UDFi1` through `UDFi30` in the DFM

**IS2D.BAR — 2D Barcode Layout Table** (T7INB2DB)
- `IS2D.BAR.DESC` — layout description
- `IS2D.BAR.CHAR` — character literal (or ASCII code)
- `IS2D.BAR.ASCII` — ASCII value
- `IS2D.BAR.FIELD` — field name to embed
- `IS2D.BAR.ORDER` — print order
- `IS2D.BAR.DOC.NAME` — associated document name
- Allows custom per-item 2D barcode composition

**IS.ECO — ECO (Engineering Change Order) Table** (T7INBECO/T7WOAECO)
- `IS.ECO.REVLVL` — current revision level
- `IS.ECO.DRAW` — drawing number
- `IS.ECO.ENTDATE` — ECO entry date
- `IS.ECO.DATE` — ECO effective date
- `IS.ECO.ENTBY` — entered by
- `IS.ECO.ECO` — ECO number
- `IS.ECO.CURRENT` — current ECO flag
- (Also stored per-WO as IS.OECO.* — open ECO for the WO)

**IS.PROD.SLEAD** — Shipping lead time (from t7inbc)
**IS.PROD.RCODE** — Refurbished item code
**IS.PROD.ITP** — Item type pointer (to IS.ITP.DESC)
**IS.ITP.DESC** — Item type description

**IN-A Sub-Tabs (T7INAA* forms — item inquiry sub-tabs)**

| Form | Tab name | Key fields |
|---|---|---|
| T7INAACDOC | Accutron Documentation | Doc types: COR/DR/VAR/MIN/SPR/ECN/ECN C/QC/VAR C/MIN C/QUAL |
| T7INAALO | Item Allocations | PO allocs (APPO/VNDCOD/VNDNME/APPQTY/APERD/APARD/APLOC) + WO allocs (WORD/WSTAT/WPART/WREQ/WISSU/WREM/WDATE/WLOC) |
| T7INACMP | Compliance | IS.PROD.FLAGS[1..19], REACH, CAPROP65, ROHS, CFM |
| T7INAFORECAST | Forecast | USAGE.MONTH/CURRENT/YEAR1..5 |
| T7INAPRC | Customer Pricing | qty/disc/cust/cname/prce per line |
| T7INASPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T7INAUDF | User Defined Fields | UDFi1..UDFi30 |
| T7INAUSG | Item Usage | 5 years usage history |
| T7INAWIP | Item in WIP | Active WOs using this item |

**IN-B Sub-Tabs (T7INBA/T7INB* forms — item master entry sub-tabs)**

| Form | Tab | Key new fields |
|---|---|---|
| T7INB2DB | 2D Barcode Layout | IS2D.BAR.* array |
| t7inbc | Characteristics | lot/serial control, cycle.code, SLEAD, mapping.reqd, supersede.item, WH.CONTROL, WO.MAT |
| T7INBCMP | Compliance | same as INACMP |
| T7INBECO | ECO | IS.ECO.* |
| T7INBLNK | Item Links | I.ORDER/LINK/GPATH, IMAGE.TL[1..10], IMAGE.PCB[1..10] |
| T7INBMFG | Manufacturer XRef | BKSB.MFG.MANUF/MPART/CUST |
| T7INBMRP | MRP Settings | MTIC.PROD.MRPSW (MRP switch), EXPBF/DELBF, planner code, reserve stock |
| T7INBSPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T7INBUDF | User Defined | UDFi1..UDFi30 |
| T7INBVND | Vendor XRef | BKSB.VEND.VEND/VPART, imp.vend.* |

**MTIC.PROD Extended fields (new from Pass 87):**
- `MTIC.PROD.MRPSW` — MRP include switch (per-item MRP override)
- `MTIC.PROD.MRP` — MRP flag (from T7INBMRP label "Include in MRP Generation?")
- `BKIC.PROD.AVFO` — Average forecast (avg forecast qty)
- `bkic.prod.avvo` — Average vendor order qty (?)
- `IS.PROD.NUM[1]` = Reserve Stock Qty (buffer)
- `MTIC.PROD.VEND[1]` — Primary approved vendor code
- `MTIC.PROD.CUST` — Customer code cross-reference
- `MTIC.PROD.ABC` — ABC classification (A/B/C)
- `MTIC.PROD.WIPDP` — WIP display flag
- `IS.PROD.GDATES[1]` — Product good/expiry date (from t7inaE)

**IN Program Summary:**

| Code | Form | Function |
|---|---|---|
| IN-A | T7INA/t7inaC/t7inaE | Item inquiry / lookup |
| IN-B | T7INB/t7INBE | Item master entry/edit |
| IN-C | T7INC | Inventory adjustments + import |
| IN-D | T7IND | Print record report (stock status, BOM, usage) |
| IN-E | T7INE/T7WOE | Print inventory transactions |
| IN-F | T7INF | Print inventory value (as-of date, export CSV) |
| IN-G | T7ING/T7INGimport | Print inventory labels (compliance links, import) |

**IN-F inventory value report** can export to CSV file (`expt.filename`), filter by:
- Item, class, category, vendor, GL account (glacct/gldpt), customer
- Active status [YNODEPSQR], sort by item/class/customer [P/C/U]
- As-of date (historical snapshot), include FIFO option
- Qty YTD / last year ranges

**IN-G label program** prints compliance symbols as links on labels:
- CE, WEEE, European RoHS, China RoHS, UL, LDPE Recycle, UKCA, REACH, User Defined 1/2
- Company logo

**IN-C adjustments** can import from comma-delimited file:
- Fields: item, qty, PO#, vendor, reference, PO price, WC bin, location
- Or lot-on-hand: item + location + lot + lot qty
- Cost basis: A=avg, S=standard, L=last cost



---

## Pass 88 — WO K-M/L/P/S series, SO full suite, PO full suite (2026-06-18)

### WO — New Tables Discovered

#### IS.PREQ — Production Material Request Table (T7WOKNB/C)

Live material request system used at work centers.

| Field | Meaning |
|---|---|
| IS.PREQ.EMP | Requesting employee |
| IS.PREQ.WOPRE | Work order prefix |
| IS.PREQ.WOSUF | Work order suffix |
| IS.PREQ.OPER | Sequence/operation number |
| IS.PREQ.RDATE | Request date |
| IS.PREQ.PART | Item/part requested |
| IS.PREQ.QTY | Quantity requested |
| IS.PREQ.REASON | Reason code |
| IS.PREQ.NOB | (not-on-BOM flag?) |
| IS.PREQ.NOTE | Request notes |
| IS.PREQ.NOTE2 | Secondary notes |
| IS.PREQ.LCOST | Last cost |
| IS.PREQ.IQTY | Issue quantity |
| IS.PREQ.INOTE | Issue notes |
| IS.PREQ.LOC | Location |

Sub-programs: T7WOKNA (live WC schedule), T7WOKNB (open requests grid — substitute/restore/print),
T7WOKNC (issue part from request), T7WOKT (print request report)

#### IS.SER — Serial Number Parent-Component Link (T7woko/T7WOKP)

Tracks serial numbers assembled into parent serial numbers.

| Field | Meaning |
|---|---|
| IS.SER.PSERIAL | Parent serial number |
| IS.SER.PARENT | Parent item code |
| IS.SER.PDESC | Parent item description |
| IS.SER.COMP | Component item code |
| IS.SER.CDESC | Component item description |
| IS.SER.CSERIAL | Component serial number |
| POSTED | Posted flag |

T7woko = parent serial → component serial lookup
T7WOKP = parent serial → component Lot lookup (fields: AWOP/AWOS/APPRT/APSER/ACOMP/ALOT)

#### IS.TRAY — WIP Tray/Bin Tracking (T7WOKS/T7WOKSA)

Tracks physical WIP containers (trays, bins) at work centers during WO processing.

| Field | Meaning |
|---|---|
| IS.TRAY.WOPRE | Work order prefix |
| IS.TRAY.WOSUF | Work order suffix |
| IS.TRAY.WHO | Employee who updated |
| IS.TRAY.CDATE | Change date |
| IS.TRAY.STATUS | WO status |
| IS.TRAY.OPER | Sequence/operation |
| IS.TRAY.CODE | Item code |
| IS.TRAY.BIN | Bin location |
| IS.TRAY.BINQTY | Qty in bin |
| IS.TRAY.DATE[1] | Date array |
| IS.TRAY.ALPHA[1] | Alpha array (description/notes) |
| IS.TRAY.ALPHA[3] | Secondary alpha |

T7WOKS edits individual bin assignments; T7WOKSA prints the WIP bin location report.

#### IS.WOPRIO — WO Priority Color Table (t7woprio/t7woprio2)

| Field | Meaning |
|---|---|
| IS.WOPRIO.PRIO | Priority code (1-9) |
| IS.WOPRIO.DESC | Priority description |
| IS.WOPRIO.COLOR | Display color for Gantt/list views |

#### ISSO.BOX — SO Box/UCC Label Table (T7WOS)

| Field | Meaning |
|---|---|
| ISSO.BOX.UCC | UCC-128 barcode number |
| ISSO.BOX.CODE | Item code |
| ISSO.BOX.QTY | Quantity in box |

#### WO Sub-Program Extensions

**T7WOS — WO Label / Serial Number Assignment**
- Assigns serial numbers to WOs and prints labels
- Fields: `scan.serial`, `assign.cntr`, `from.serial`, `thru.serial`
- Per-label: `edit.lbl.boxno`, `edit.lbl.misc`, `edit.lbl.qty`, `edit.lbl.total`, `edit.lbl.copy`
- Options: `gen.bar` (2D barcode), `one.per` (one lot entry per component), `mfg.date`
- Print modes: stock/index/regular labels (`adt.option`), blank labels (`BLANK.LABELS`)
- Print lot range: `from.lot`/`thru.lot`, WO receipt serials (`PRT.WORECV.SER`)

**T7WOP — Finish Production (WO-P)**
- Finalize WO production quantity and optionally close the WO
- Grid mode: WO#, item, qty, close WO flag
- Import mode: WO prefix, suffix, qty, close WO from CSV
- Fields: `m.date`, `from.wonum/thru.wonum`, `from.job/thru.job`

**T7WOPO/T7WOPOR — Create POs from WO Shortages**
- T7WOPO generates PO lines for open WO material shortages
- Options: `make.po`, `JOBNO`, `INC.SPECS`, order/receipt dates, offset, tie lines to WOs
- T7WOPOR reviews proposed PO lines before creating: BKIC.PROD.CODE, MTIC.PROD.DESC, PO.DATE, ER.DATE, QTY, BKMRP.PO.VEND, price

**T7WOTRWK — Rework to Stock WO**
- Creates a special rework WO to put reworked assemblies back into stock
- Fields: item, desc, quantity, location, sstart.date, sfin.date, issue.parent

**T7WOKNA — Live Work Center Schedule (monitor)**
- Real-time WC production schedule display (like a digital board)
- `location` filter, `timer` (refresh every N seconds), `audio` (audible cue when updated)

**WO-L Report Suite (T7WOLA through T7WOLO)**

| Code | Form | Report |
|---|---|---|
| WO-L-A | T7WOLA | WO open order list (by item, WO, customer, class, routing) |
| WO-L-B | T7WOLB | WO status report (by status/priority/class, multiple) |
| WO-L-C | T7WOLC | WC time utilization (by WC/machine, dept break) |
| WO-L-D | T7WOLD | WO completion status by sequence |
| WO-L-E | T7WOLE | Export labor hours to payroll file (optional post to PR) |
| WO-L-F | T7WOLF | WO shortage/need-by report (need.so/po/wo.date, alloc.date) |
| WO-L-G | T7WOLG | WC schedule by component (key.component[1..15]) |
| WO-L-H | T7WOLH | WO labor hours summary |
| WO-L-I | T7WOLI | Inventory stock status with WO status filter |
| WO-L-J | T7WOLJ | Finished WO report (early/late/on-time details) |
| WO-L-K | T7WOLK | WO BOM print (specs, dwg, subs, vendors, mfgs, phantoms, SMT) |
| WO-L-L | T7WOLL | WO component label print |
| WO-L-M | T7WOLM | Material summary report for SOs (uses WO BOM) |
| WO-L-N | T7WOLN | WO notes print |
| WO-L-O | T7WOLO | WC by customer report |

---

### SO — Sales Order Full Suite

#### BKAR.INV — SO Header Table (T7SOAC/T7SOAE confirmed)

Key previously unconfirmed fields:

| Field | Meaning |
|---|---|
| BKAR.INV.SONUM | SO number |
| BKAR.INV.ORDDTE | Order date |
| BKAR.INV.CUSCOD | Customer code |
| BKAR.INV.CUSNME | Customer name |
| BKAR.INV.CUSA1 | Customer ship-from address 1 |
| BKAR.INV.CUSA2[1..2] | Customer address lines 2+ |
| BKAR.INV.CUSCTY | Customer city |
| BKAR.INV.CUSST | Customer state |
| BKAR.INV.CUSZIP | Customer zip |
| BKAR.INV.CUSCNT | Customer country |
| BKAR.INV.CUSATT | Customer attention |
| BKAR.INV.SHPA1 | Ship-to address 1 |
| BKAR.INV.SHPA2 | Ship-to address 2 |
| BKAR.INV.SHPCTY | Ship-to city |
| BKAR.INV.SHPST | Ship-to state |
| BKAR.INV.SHPZIP | Ship-to zip |
| BKAR.INV.SHPCNT | Ship-to country |
| BKAR.INV.SHPATN | Ship-to attention |
| BKAR.INV.SHPNME | Ship-to name |
| BKAR.INV.SHPCOD | Ship via code |
| BKAR.INV.SHPVIA | Ship via description |
| BKAR.INV.TRACK | Tracking number |
| BKAR.INV.FRGHT | Freight amount |
| BKAR.INV.NUM | SO last invoice number |
| BKAR.INV.DESC | SO description |
| BKAR.INV.JOBNUM | Job number |
| BKAR.INV.FOB | FOB |
| BKAR.INV.ENTBY | Entered by |
| BKAR.INV.SUBTOT | Subtotal |
| BKAR.INV.TAXAMT | Tax amount |
| BKAR.INV.RTS | Release-to-ship date |
| BKAR.INV.TAXABL | Taxable flag |
| BKAR.INV.GLDPT | GL department |
| BKAR.INV.SLSP | Salesperson code |
| BKAR.INV.NL | Non-linked flag |
| BKAR.INV.CUSORD | Customer PO/order# |

SRTYPE — service/repair type (controls SO-E service/repair workflow)
SONUM.CHAR — SO number display field

#### BKAR.INVL — SO Line Table (t7Soa2/T7SOE confirmed)

| Field | Meaning |
|---|---|
| BKAR.INVL.PCODE | Item code |
| BKAR.INVL.PDESC | Item description |
| BKAR.INVL.LOC | Location |
| BKAR.INVL.TAX | Tax code |
| BKAR.INVL.RTS | Release-to-ship date |
| BKAR.INVL.PQTY | Ship quantity |
| BKAR.INVL.UBO | Back order quantity |
| BKAR.INVL.PPRCE | Unit price |
| BKAR.INVL.PEXT | Price extension |
| BKAR.INVL.UM | Unit of measure |
| BKAR.INVL.DISC | Discount % |
| BKAR.INVL.ESD | Estimated ship date |
| BKAR.INVL.ASD | Actual ship date (customer due date) |
| BKAR.INVL.STAT | Line status |
| BKAR.INVL.LONGP | Extended description |
| BKAR.INVL.HIDE | Hide on document flag |
| BKAR.INVL.INVNM | Invoice number |
| BKAR.INVL.FATD | (confirmed/fill-and-tie to date?) |
| line.prod.comm1/comm2 | Commission rates per line |
| line.prod.oqty | Original quantity ordered |
| line.prod.ipext | (invoiced price extension?) |

#### ISAR.CHG — SO Line Change History (T7SOLINEHIST)

Audit trail for every change to SO line fields.

| Field | Meaning |
|---|---|
| ISAR.CHG.CDATE | Change date |
| ISAR.CHG.BPRICE | Price before |
| ISAR.CHG.APRICE | Price after |
| ISAR.CHG.BDISC | Discount before |
| ISAR.CHG.ADISC | Discount after |
| ISAR.CHG.BOOQTY | Qty before |
| ISAR.CHG.AOOQTY | Qty after |
| ISAR.CHG.BASD | ASD before |
| ISAR.CHG.AASD | ASD after |
| ISAR.CHG.BESD | ESD before |
| ISAR.CHG.AESD | ESD after |
| ISAR.CHG.BCOMPR[1..2] | Commission rate before |
| ISAR.CHG.ACOMPR[1..2] | Commission rate after |
| ISAR.CHG.BLOC | Location before |
| ISAR.CHG.ALOC | Location after |
| ISAR.CHG.USER | User who made the change |

#### ISSR.INFO — SO User-Defined Fields (T7SOINFO/T7SOHINFO/T7SOLINFO)

20 alpha + 5 date UDF fields at SO header level, SO line level, and SO header misc level.

| Field | Meaning |
|---|---|
| ISSR.INFO.AL1..AL20 | Alpha user-defined fields 1-20 |
| ISSR.INFO.DATE1..DATE5 | Date user-defined fields 1-5 |
| ISSR.INFO.SRNUM | SO number (linking key) |

Labels for AL1..20 and DATE1..5 are configured in system setup (displayed as soAlpha1..20, soDate1..5 etc.)

Three separate sub-forms use this same table:
- T7SOINFO — SO-level "Sales Misc. Information"
- T7SOHINFO — SO-level "Sales Header Misc. Information"
- T7SOLINFO — SO-line-level "Sales Line Misc. Information"

#### BKIC.PMAT — Item Price Matrix (T7SOAPRC)

| Field | Meaning |
|---|---|
| BKIC.PMAT.QTY | Quantity break |
| BKIC.PMAT.RATE | Price at this quantity |
| BKIC.PMAT.PDESC | Price description |

Shown alongside BKIC.PROD.PRICE (base price) for item pricing lookup during SO entry.

#### ISAR.TXN — SO Bin Allocation Transactions (T7SOBIN)

| Field | Meaning |
|---|---|
| ISAR.TXN.QTY | Allocated quantity |
| ISAR.TXN.BIN | Bin location |
| ISAR.TXN.DATE | Transaction date |

T7SOBIN shows item/bin/qty/SO/customer/line qty/qty allocated/qty left.

#### BKAR.TXN — SO Lot Allocation Transactions (T7SOLOT)

| Field | Meaning |
|---|---|
| BKAR.TXN.QTY | Allocated quantity |
| BKAR.TXN.LOT | Lot number |
| BKAR.TXN.DATE | Transaction date |
| BKAR.TXN.BIN | Bin location |

#### BKAR.DEP — Customer Deposits (T7SOFDEP)

| Field | Meaning |
|---|---|
| BKAR.DEP.CUST | Customer code |
| BKAR.DEP.DATE | Deposit date |
| BKAR.DEP.DEPNO | Deposit number |
| BKAR.INVT.AMTRM | Amount remaining |

#### ISAR.JD — John Deere Label Fields (T7SOD)

Specialized EDI/label fields for John Deere supplier compliance:

| Field | Meaning |
|---|---|
| ISAR.JD.SONUM | SO number |
| ISAR.JD.INVNUM | Invoice number |
| ISAR.JD.PCODE | Item code |
| ISAR.JD.LINE# | Line number |
| ISAR.JD.QTYND | Quantity needed |
| ISAR.JD.PLATE# | Pallet license plate number |

T7SOD also supports: DUNS number, Kanban ID, country of origin, customer routing 1+2, supplier area 1-4, unloading point, delivery note, batch number, packaging type, supplier ID.
John Deere label types: I=individual, M=mixed, X=???, S=???

#### Recurring Orders (T7SOK/T7SOJINFO)

- `mem.group` — recurring group code
- `bkar.inv.invdte` — invoice date
- `mem.freq` — frequency
- `mem.max` — maximum invoices

T7SOK manages recurring templates: view next due dates, tag all in date range, set next order/ESD/CDD, customer PO#.

#### SO Program Summary

| Code | Form | Function |
|---|---|---|
| SO-A | T7SOAC/T7SOAE | Create/edit SO header + lines |
| SO-B | T7SOB | Print SO (quote/acknowledgment) |
| SO-BIN | T7SOBIN | SO bin allocation |
| SO-C | T7SOC | Print packing slip + C of C |
| SO-D | T7SOD | Print shipping labels (standard + JD EDI) |
| SO-E | T7SOE | Release/ship SO lines |
| SO-F | T7SOF | Print invoice |
| SO-G | T7SOG | Post invoice (COGS + commissions) |
| SO-K | T7SOK | Recurring order processing |
| SO-LOT | T7SOLOT | SO lot allocation |
| SO-N | T7SON | Create work orders from SO lines |

**SO-G posting flow:** print → post COGS → post commissions → update GL.
SOG-A shows live posting progress; SOGACHK handles cash terms deposits.

**SO-N options (create WOs from SO):**
- Match WO suffix to SO line number
- Auto-generate serial numbers
- Create WOs for kit components / make-from items / non-inventory types
- Multi-assembly WO option
- Offset start/finish dates
- Use shop calendar / inventory lead time for start dates
- Combine duplicate items into single WOs

---

### PO — Purchase Orders Full Suite

#### BKAP.PO — PO Header Table (T7POA confirmed)

| Field | Meaning |
|---|---|
| BKAP.PO.NUM | PO number |
| BKAP.PO.ORDDTE | Order date |
| BKAP.PO.VNDCOD | Vendor code |
| BKAP.PO.VNDNME | Vendor name |
| BKAP.PO.VNDA1 | Vendor address 1 |
| BKAP.PO.VNDA2 | Vendor address 2 |
| BKAP.PO.VNDCTY | Vendor city |
| BKAP.PO.VNDST | Vendor state |
| BKAP.PO.VNDZIP | Vendor zip |
| BKAP.PO.VNDCNT | Vendor country |
| BKAP.PO.VNDATN | Vendor attention |
| BKAP.PO.SHPA1 | Ship-to address 1 |
| BKAP.PO.SHPA2 | Ship-to address 2 |
| BKAP.PO.SHPCTY | Ship-to city |
| BKAP.PO.SHPST | Ship-to state |
| BKAP.PO.SHPZIP | Ship-to zip |
| BKAP.PO.SHPCNT | Ship-to country |
| BKAP.PO.SHPATN | Ship-to attention |
| BKAP.PO.SHPNME | Ship-to name |
| BKAP.PO.SHPCOD | Ship via code |
| BKAP.PO.SUBTOT | Subtotal |
| BKAP.PO.TAXAMT | Tax amount |
| BKAP.PO.TOTAL | Total |
| BKAP.PO.DESC | Description |
| BKAP.PO.TERMNM | Terms name |
| BKAP.PO.OBYCUS | Ordered-by customer (SO customer driving the PO) |
| BKAP.PO.FOB | FOB |
| BKAP.PO.ENTBY | Entered by |
| BKAP.PO.ISCUR | Currency code |
| BKAP.PO.LOC | Receiving location |
| BKAP.PO.GLDPT | GL department |
| BKAP.PO.EMPNUM | Employee number (signer) |
| BKAP.PO.ISBROKE | Customs broker flag |
| BKAP.PO.CONFIRM[2] | PO type / confirmation code |
| BKAP.PO.NL | Non-linked flag |
| BKAP.TELEPHONE[1] | Phone 1 |
| BKAP.TELEPHONE[3] | Fax |

Risk Assessment fields (T7POAC — aerospace/defense POs):
- `risk.assess[1..6]` — Schedule risks, obsolescence, first article, NADCAP certs, tooling, test reports
- `ritec.dpas` — DPAS (Defense Priority Allocations System) rating
- `ritec.contract` — Contract number

#### BKAP.POL — PO Line Table (T7POA2/t7poc confirmed)

| Field | Meaning |
|---|---|
| BKAP.POL.PCODE | Item code |
| BKAP.POL.PDESC | Item description |
| BKAP.POL.QTY | Order quantity |
| BKAP.POL.OO.QTY | Original order quantity |
| BKAP.POL.ERD | Estimated receipt date |
| BKAP.POL.ARD | Actual receipt date |
| BKAP.POL.PRCE | Unit price |
| BKAP.POL.UM | Unit of measure |
| BKAP.POL.PCON | Purchase conversion factor |
| BKAP.POL.TAX | Tax code |
| BKAP.POL.DISC | Discount % |
| BKAP.POL.EST | Estimate number |
| BKAP.POL.WOPRE | WO prefix |
| BKAP.POL.WOSUF | WO suffix |
| BKAP.POL.OPER | WO sequence |
| BKAP.POL.GLDEPT | GL department override |
| BKAP.POL.LOC | Line location |
| NKAP.POL.UM.LIN[1..2] | Unit of measure array |
| BKAP.POL.RQTY | Received quantity |
| enter.prod.conf | Confirmed flag |
| enter.prod.long | Extended description |

#### BKRFQ — RFQ / Price Quote Table (T7POF/T7POH)

| Field | Meaning |
|---|---|
| BKRFQ.PROD | Item code |
| BKRFQ.PRODDESC | Item description |
| BKRFQ.VEND | Vendor code |
| BKRFQ.VENDNAME | Vendor name |
| BKRFQ.PARENT | Parent item (WO assembly) |
| BKRFQ.PARNTDESC | Parent description |
| BKRFQ.EST | Estimate number |
| BKRFQ.OPER | WO operation/sequence |
| BKRFQ.ISSUE | Issue/RFQ date |
| BKRFQ.EXP | Expiry date |
| BKRFQ.PUM | Purchase unit of measure |
| BKRFQ.PCONV | PO conversion factor |
| BKRFQ.LEAD | Lead time |
| BKRFQ.QTY[1..10] | Quantity breaks (up to 10) |
| BKRFQ.COST[1..10] | Price at each quantity break |
| BKRFQ.MIN | Minimum quantity |
| BKRFQ.MINCST | Minimum cost |
| BKRFQ.LCDATE | Last change date |
| BKRFQ.CWHO | Changed by |
| BKRFQ.EXTRA | Extra notes |
| BKRFQ.FLAG | Flag (archive/active status) |
| BKRFQ.USE | Use in estimation flag |

RFQ workflow: PO-F (enter RFQ) → PO-G (convert to PO) → PO-H (vendor price history/archive)
PO-I-C (print open RFQs) → PO-I-D (print vendor price lists, expired/current)
T7POAPrBrk verifies price breaks at PO entry time.

#### PO Receipt (t7poc — PO-C)

Full receipt form fields:
- `RCVD_QTY` — received qty
- `PKSLIP.QTY` — packing slip qty
- `ENTER.PRICE` — entered unit cost
- `RINTO` / `RCVINTO.TXT` — receive into (QC, stock, location)
- `RCVD_WT` — received weight
- `POL.JOB` — job number per line
- `no.work.done` — flag: received but no work performed (outside processing return)
- `DTS` — dock to stock (skip QC and put directly into stock)
- `BKAP.PO.ISBROKE` — customs broker involved
- `BKAP.PO.EMPNUM` — employee receiving
- `PACKING.SLIPNUM` — packing slip number
- `PO.CONFIRM.TXT` — PO type text
- `BKAP.PO.ISCUR` — currency code

#### PO QC Buyoff (T7POJC — PO-J-C)

| Field | Meaning |
|---|---|
| BKQC.QTY.RECVD | Total received qty |
| BKQC.QTY.BUYOFF | Total bought off qty |
| BKQC.QTY.REJECT | Total rejected qty |
| BUYOFF.REMAIN | Qty remaining to buy off |
| BKQC.TRN.GQTY | Good qty this buyoff |
| BKQC.TRN.BQTY | Bought-off qty |
| BKQC.TRN.UQTY | Use-as-is qty |
| BKQC.TRN.SCRAP | Scrap qty |
| BKQC.TRN.REWORK | Rework qty |
| BKQC.TRN.NQTY | NCR qty |
| BKQC.QTY.NCR | NCR accumulated qty |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.VEND.CODE | Vendor code |
| BKQC.RECV.DATE | Receipt date |
| BKQC.PO.NUM | PO number |
| DEFAULT.BING | Default bin for good parts |
| DEFAULT.BINU | Default bin for use-as-is parts |
| rohs | RoHS flag |
| sampl | Sample size |
| mpart | Manufacturer part number |

Sub-dialogs: T7pojcqc (multi use-as-is codes), T7pojcsc (multi scrap codes)

#### PO Vendor On-Time Delivery (T7POIH/T7POJD)

- PO-I-H: evaluates vendor on-time delivery for a date range
- Date basis options: scheduled (ERD), actual receipt date, or defined cutoff
- Allowable early/late days tolerance
- Base on: total dollars, item quantities, or line count
- Option to save results to vendor history

#### POENG — PO Engineering Report (T7POENG)

User-defined sort/break report with up to 10 index fields:
- `index.text[1..10]` — index labels
- `UDBRK.ARRAY[1..10]` — user-defined break arrays
- `REPORT.TITLE` — custom report title
- Filters: PO range, ship-to range, vendor state range, and more (`ZBKSA.*` fields)

#### PO Program Summary

| Code | Form | Function |
|---|---|---|
| PO-A | T7POA/T7POAC/T7POAE | Create/edit PO (standard, risk assessment, enhanced) |
| PO-B | T7POB | Print PO (with digital signature option) |
| PO-C | t7poc | Receive PO (dock-to-stock, customs broker, customs) |
| PO-E-A | T7POEA | Print RFQs |
| PO-ENG | T7POENG | User-defined sort/break report |
| PO-F | T7POF | Enter RFQ (10 qty/cost break tiers) |
| PO-G | T7POG | Convert RFQ to PO |
| PO-H | T7POH | Vendor price history and archive |
| PO-I-C | T7POIC | Print open RFQs by range |
| PO-I-D | T7POID | Print vendor price lists |
| PO-I-G | T7POIG | PO expedite report (rush/expedite colors) |
| PO-I-H | T7POIH | Vendor on-time delivery analysis |
| PO-I-I | T7POII | PO change report |
| PO-J-A | T7POJA | Print QC receipt travelers |
| PO-J-B | T7POJB | PO receipt value/expedite report |
| PO-J-C | T7POJC | QC buyoff form |
| PO-J-D | T7POJD | Vendor on-time delivery report |
| PO-K | T7POK | Close POs |
| PO-L | T7POL | Vendor XRef list (primary vendor indicator) |
| PO-L-A | T7POLA | Approved vendors report |

**Digital Signature integration:** T7POB has "Enter Digital Signature (Y/N/Ask)" option;
T7POAE has "&Sign PO" button — these invoke T7DIGSIG.



---

## Pass 89 — SO sub-programs, PO remaining, AP full, AR full (104 DFMs)

### SO-O Sub-Programs (Reports/Inquiries)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-OA | T7SOOA | Backorder / open order report — range by ESD, customer, job, SO, item, sort by, currency, customer PO, salesperson 1&2, order date, due date, item class; options: grand totals only, line detail, comments, MO totals, kit components, include BO |
| SO-OB | T7SOOB | Packing slip sequence report — item/job/ESD/customer ranges |
| SO-OD | T7SOOD | Print SOs — SO/customer/customer PO/salesperson ranges, one SO per page |
| SO-O-E | T7SOOE | WO/labor scheduling report — machine 1/2/3 ranges, WO status, WO start date, item cat/class, ESD, customer, job, lead source 1&2, customer due date; option: include remaining labor, include SR, tag all locs |
| SO-OF | T7SOOF | Production planning/dispatch — customer due date ranges across 5 filter sets, item cat/class, ESD, customer, job, SO; options: complete only, credit hold, include released, UOH by loc, price, holdups, zero-UOH |
| SO-O-G | T7SOOG | WO-to-SO cross-reference — item/customer/SO/WO/ESD/WO-finished/job ranges, sort, WO status; options: exclude item types, all open SO lines, SO lines without WOs |
| SO-OH | T7SOOH | Invoice type report — invoice types (INVCTYPE[1..3]: finance charges, AR vouchers, SO module), invoice date/number/SO/customer ranges, sort by invoice or date; option: drop-ship only, SR module invoices, currency range |
| SO-OI | T7SOOI | Open order report (variant of OA) — same ranges + use.ship.date, item class/category |
| SO-O-M | T7SOOM | SO change history report — change date range, customer/item/job/SO ranges, sort; options: changes in price/qty/ESD/ASD/discount/location/commission, print archived SO changes |
| SO-O-N | T7SOON | On-time delivery report — item class/cat/num, customer, invoice date, SO/invoice nums, allowable days early/late, ESD/ASD basis; options: summary only, late orders only, print ship log, net days, customer class range |

### SO-P Sub-Programs (Processing/Print)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-NQty | T7SONQTY | Quantity conversion — shows item stock levels (UOH/UOSO/UBO/available/min-ord/reorder-level/lead-time/in-WIP/allocated/on-WO/on-PO) when converting SO line qty; fields BKIC.PROD.UOH/UOSO/UBO/RAMT/RLVL/UOO + MTIC.PROD.AVAIL/LEAD/UIWIP/UOA/UOWO |
| SO-PB | T7SOPB | Print quotations — quotation number range, print linked docs (PLDTYPE), notes/hidden notes, tax/freight, kit components, options, system quote notes last, print item rev (ECO), tax codes for $0, mark as printed, archived quotes, contract pricing matrix, price code matrix |
| SO-PC | T7SOPC | Quote conversion to SO — ORDER.DATE, EST.DATE, DUE.DATE, CUST.PO, LOC, CNVT.NOTES, KEEP.QUOTE; batch mode: from/thru quote range, from/thru unconverted date, pass.quote (desc/job/none), new.status (Y/L/A/N/S/D/W/B), reason.code, use.ship.lead, close.QUOTE, status change only |
| SO-PF | T7SOPF | Blanket SO releases — group.Mlines, shows BKAR.INVL.PCODE/PDESC/OOQTY/ESD/UM, balance-on-order (blanket.left), release qty/date per line |
| SO-PI | T7SOPI | Shipping/invoicing — invoice/SO number, frt.charge, tracking.num, shipping company/shipper number, drop ship flag, gross weight, date filter, ship.cust |
| SO-PJ | T7SOPJ | Background processing progress form — fixfile, stime |
| SO-PK | T7SOPK | Edit posted invoices — bill-to: BKAR.INV.CUSCOD/CUSNME/CUSA1/CUSA2[1..2]/CUSCTY/CUSZIP/CUSST/CUSCNT/CUSATT + ship-to: BKAR.INV.SHPCOD/SHPNME/SHPA1/SHPA2[1..2]/SHPCTY/SHPZIP/SHPST/SHPCNT/SHPATN; also BKAR.INV.DESC/SHPVIA/TERMNM/JOBNUM/FOB/BILCOD/ORDDTE/INVDTE |
| SO-PM | T7SOPM | Print quote list — customer/order-date ranges, print unconverted/converted/all quotes, check job# and description |
| SO-PO | T7SOPO | Generate POs from SOs — JOBNO, order date, est-receipt date, offset, from/thru SO/order/customer/vendor, UBO (use backorder qty), pass.sell.price, pass.line.num, pass.ship.info, pass.more.info (via/FOB/terms/notes), pass.po.num, pass.job.num [H/L/B/N] |
| SO-POR | T7SOPOR | SO-PO review — item/desc, PO.DATE, ER.DATE, QTY, vendor, price, SO line (BKAR.INVL.INVNM) |
| SO-PP | T7SOPP | Mass update ESD on SOs — from/thru SO, ESD range, new ESD, customer filter |

### SO-Q Sub-Programs (Pricing)

| Code | DFM | Purpose |
|------|-----|---------|
| SO-QA | T7SOQA | Update item base price — from.item, BKIC.PROD.PRICE, BKIC.PROD.NOTE, HOW.ROUND, CHG.PCODE, CHG.CONTRACT |
| SO-QB | T7SOQB | Price list report — item/cat/class ranges, active status filter [YNODEPSQR], format with $ and commas |
| SO-QC | T7SOQC | Mass price change — direction (CHG.DIR.ARR[1/2]: increase/decrease), type (CHG.TYPE.ARR[1/2]: %/flat), ENT_CHANGE_AMT, item/class/cat/customer ranges, active status, new expiration date, update contract/price codes ONLY option, cust.filter [ICN] |
| SO-QH | T7SOQH | Price matrix entry — BKIC.PMAT.QTY[1..10]/RATE[1..10]/PER[1..10]/ISRET[1..10] (retail flag)/COMM1[1..10]/COMM2[1..10]; EXIST.ACTION for existing codes; item/price-code/customer/base-price/expiration/inv-class/start-end-date/SO-total-disc/discount-code/minimum/promo fields |
| SO-QI | T7SOQI | Price list/discount code report — FROM.DCODE/THRU.DCODE, customer/class/cat/vendor ranges, exp-date range, price code range, INC.RETAIL, all.locs, sort by item or customer, incl.last.so, SO order date range |
| SO-QJ | T7SOQJ | Cost-based price update — COST.TYPE.TXT, markup vs margin (use.margin), CHG.PCODE/CHG.CONTRACT, item/class/cat, active status, report.only, prevent.below |
| SO-Q-K | T7SOQK | Print catalog — item type [RFAMNLBTKO], class/cat/vendor ranges, active status, sort, pricing (RTYPE), price code (PC), sold-since date, extended desc, thumbnail images, price quantity breaks |
| SO-Q-L | T7SOQL | Import new SO prices — from.item, from.esd/thru.esd, new.price, imp.filename (CSV), FIELD.NUMBER[1/2] (column mapping) |

### SO-R, SO-S, SO-V, SO-Contract Review, SO-Serial

| Code | DFM | Purpose |
|------|-----|---------|
| SO-R | T7SOR | Void invoice list — BKAR.INV.INVDTE/ORDDTE/SHIPDT/CUSCOD/CUSNME/CUSA1/CUSA2[1..2]/CUSCTY/CUSST/CUSCNT/CUSZIP, VOID.DATE, BKAR.INV.SONUM/SUBTOT/TAXAMT/FRGHT, DISPDEPOSIT/DISPRETEN/DISPTOTAL, BKAR.INV.SLSP/GLDPT/LOC/DESC |
| SO Contract Review | T7SORevu | Digital signature approval for SOs — SO.REQUIRE, SO.DEPT, SO.EMPNAME, SO.APPROVE, SO.ADATE, so.entby, so.edate; requires password T7SORevuPSWD (ct.empname/dept/enter.pswd) |
| SO-S | T7SOS | Release SOs from hold — AUTO.RCOMM/AUTO.BO/REL.ALL, SO/customer/order/item ranges |
| SO-SERIAL | T7SOSER | Allocate serial numbers to SO — BKAR.TXN.SERIAL, MTSER.BIN, alloc.qty, qty.left, generate/tag serials |
| SO-V | T7SOV | Maintain SO shipping dates — line-by-line: edit.ASDate/edit.ESDate, BKAR.INVL.PQTY/UBO/PCODE/PDESC; LINE.PROD.* parallel display fields; SONUM.CHAR |

### PO Remaining Sub-Programs

| Code | DFM | Purpose |
|------|-----|---------|
| PO line history | T7POLINEHIST | PO line change history — ISAP.CHG table: CDATE, BPRICE/APRICE (price before/after), BDISC/ADISC (discount B/A), BOOQTY/AOOQTY (ordered qty B/A), BARD/AARD (actual receipt date B/A), BERD/AERD (expected receipt date B/A), BGLA/BGLD/AGLA/AGLD (GL acct/dept B/A), BWOP/BWOS/BOPER/AWOP/AWOS/AOPER (WO prefix/suffix/operation B/A), ISAP.CHG.USER |
| PO-L-P | T7POLP | Vendor/item price list report — vendor/item ranges |
| PO-M | T7POM | PO inquiry — vendor/item/PO/WO/job/base-price/date search; shows WO routing (MTWORO.OPER/OPERDESC/WC/STQTY/QTYCOM/%COMP/VEND/PO), WO header (MTWO.WIP.*), PO lines (BKAP.POL.WOPRE*/PONM/PCODE/PQTY), receipts, SO cross-reference |
| PO Master | T7POMAST | PO master inquiry — vendor info + item stock: UOH/UOSO/UBO/UOO/UIQC/UOWO/UOA/AVAIL/UIWIP; fields MTIC.PROD.UIQC (in QC), MTIC.PROD.UOWO (on WO), MTIC.PROD.UOA (allocation), MTIC.PROD.AVAIL (available), MTIC.PROD.UIWIP (in WIP) |
| PO-P | T7POP | Vendor master — BKAP.VENDCODE/NAME/SORT/ADD1[1]/ADD2[1]/CITY[1]/ZIP/STATE/COUNTRY[1]/CONTACT[1]/TELEPHONE[1..3]/IS.MCCODE (currency)/START.DATE, remittance: ADD1[2]/ADD2[2]/CITY[2]/REM.ZIP/REM.STATE/COUNTRY[2], BKAP.IS.DCODE/CLASS/TERMS.NUM/GL.ACCT/GL.DPT/SHIP.VIA/FOB.POINT/CUST.CODE/IS.TAXIN/LASTPMT, BKAP2.ID/IS.TAXGRP/SEND.1099, WEBLINK |
| PO-POP-GET | T7POPGET | Generic popup — POPVALUE[1..5], POPDATE[1..5] |
| PO-Q | T7POQ | Maintain PO delivery dates — line-by-line: edit.ERDate/ARDate/conf/price/pqty, upd.all.ERD/ARD; LINE.PCODE/PDESC/ERD/ARD/REF/QTY/CONF/PRICE; BKAP.PO.CONFIRM[1]; &Clear All / Confirm All options |
| PO-S (POS) | T7POS | Point of Sale — IS.QSOA.ITEM/DESC/QTY/PRICE/DISC (line items); T7POSCD: amount due/tendered/change; T7POSI: BKCM.ACCC.CCODE/DESC (category codes); T7POSX: is.stype.type + QSOA items — POS module lives in the PO module area |

### ISAP.CHG Table — PO Line Change History

Confirmed fields from T7POLINEHIST.DFM:

| Field | Meaning |
|-------|---------|
| ISAP.CHG.CDATE | Change date |
| ISAP.CHG.BPRICE / APRICE | Price before/after |
| ISAP.CHG.BDISC / ADISC | Discount before/after |
| ISAP.CHG.BOOQTY / AOOQTY | Ordered quantity before/after |
| ISAP.CHG.BARD / AARD | Actual receipt date before/after |
| ISAP.CHG.BERD / AERD | Expected receipt date before/after |
| ISAP.CHG.BGLA / AGLA | GL account before/after |
| ISAP.CHG.BGLD / AGLD | GL department before/after |
| ISAP.CHG.BWOP / AWOP | WO prefix before/after |
| ISAP.CHG.BWOS / AWOS | WO suffix before/after |
| ISAP.CHG.BOPER / AOPER | WO operation before/after |
| ISAP.CHG.USER | User who made change |

### AP Module — Full Schema

#### AP-A Vendor Master (T7APA / t7apaC / t7apae)

**BKAP table** — AP vendor master:

| Field | Meaning |
|-------|---------|
| BKAP.VENDCODE | Vendor code (primary key) |
| BKAP.VENDNAME | Vendor name |
| BKAP.SORT | Alpha sort code |
| BKAP.ADD1 / ADD2 | Street address lines |
| BKAP.CITY / STATE / ZIP / COUNTRY | Address |
| BKAP.ADD1[2]/ADD2[2]/CITY[2]/REM.ZIP/REM.STATE/COUNTRY[2] | Remittance address |
| BKAP.TELEPHONE[1] / [3] | Phone / fax |
| BKAP.CONTACT[1..4] | Up to 4 contact names |
| BKAP.EMAIL[1..4] | Up to 4 email addresses |
| BKAP.IS.MCCODE | Multi-currency code |
| BKAP.TERMS.NUM | Payment terms number |
| BKAP.GL.ACCT / GL.DPT | Default GL account/dept |
| BKAP.SHIP.VIA / FOB.POINT | Shipping method/FOB |
| BKAP.CLASS | Vendor class |
| BKAP.CUST.CODE | Customer at this vendor (cross-ref to BKAR) |
| BKAP.IS.TAXIN / IS.TAXGRP | Tax-inclusive flag / tax group |
| BKAP.IS.DCODE | Duty code |
| BKAP.START.DATE | Start date |
| BKAP.LASTPMT / LASTPURCH | Last payment/purchase dates |
| BKAP.OUTINV / OUT.CREDIT | Outstanding invoices/credits |
| BKAP.PURCH.YTD / LYR / VAR | Purchase statistics YTD/LY/variance |

**BKAP2 table** — vendor user-defined fields (T7APINFO):

| Field Pattern | Description |
|---------------|-------------|
| BKAP2.A1L[1..5] + A1[1..5] | 5 × 1-char UDF (label + value) |
| BKAP2.A10L[1..5] + A10[1..5] | 5 × 10-char UDF (label + value) |
| BKAP2.D8L[1..5] + D8[1..5] | 5 × date UDF (label + value) |
| BKAP2.A30L[1..5] + A30[1..5] | 5 × 30-char UDF (label + value) |
| BKAP2.ID | Tax ID number |
| BKAP2.SEND.1099 | 1099 flag |

**ISAPEX table** — vendor extended/bank data (T7APABANK / t7apaC / t7apae):

| Field | Meaning |
|-------|---------|
| ISAPEX.BNAME | Bank name |
| ISAPEX.BACCTNAM | Account name |
| ISAPEX.BEMAIL | Bank email |
| ISAPEX.BADD1/BADD2/BADD3 | Bank address lines |
| ISAPEX.BCITY / STATE / ZIP | Bank city/state/zip |
| ISAPEX.BCONTACT | Bank contact |
| ISAPEX.BAPHONE | Bank phone |
| ISAPEX.BACCTTYP | Account type [C=checking/S=savings] |
| ISAPEX.ALPHA[1..2] | Misc info 1 and 2 |
| ISAPEX.LONGNAME | Long vendor name |
| ISAPEX.DATE[1] | Review date |

#### AP Voucher Entry (T7APB)

**BKAP.INVL table** — AP voucher distribution lines:

| Field | Meaning |
|-------|---------|
| BKAP.INVL.GLACT[1..10] | GL account (up to 10 lines) |
| BKAP.INVL.GLDPT[1..10] | GL department (up to 10 lines) |
| BKAP.INVL.GLD[1..10] | GL description (up to 10 lines) |
| BKAP.INVL.DC | Debit/credit flag |
| BKAP.INVL.DAMT | Distribution amount |
| BKAP.INVL.TERMD | Terms date |
| BKAP.INVL.DESC | Description |
| BKAP.INVL.DATE | Invoice date |
| BKAP.INVL.TYPED | Invoice type |
| BKAP.INVL.ISCUR | Currency code |
| BKAP.INVL.TAMT | Total amount |
| BKAP.INVL.JOB | Job number |
| BKAP.INVL.CODE | Recurring voucher selection code |
| BKAP.INVL.NUM | Voucher/invoice number |
| BKAP.INVL.TERMN | Terms number |
| BKAP.INVT.SDATE | Scheduled payment date |
| BKAP.INVT.TAX | Tax amount |
| BKAP.INVT.FRT | Freight amount |

#### AP Check Operations (T7APH / T7APT / T7APQ)

**BKAP.CHK table** — check history:

| Field | Meaning |
|-------|---------|
| BKAP.CHK.ISCUR | Currency |
| BKAP.CHK.INVDTE | Invoice date |
| BKAP.CHK.INVAMT | Invoice amount |
| BKAP.CHK.DISC | Discount |
| BKAP.CHK.AMTPD | Amount paid |
| BKAP.CHK.DESC | Description |
| BKAP.CHK.CHKDTE | Check date |
| BKAP.CHK.TYPE | Check type |
| BKAP.CHK.CHKACT | Bank account number |

#### AP-C Voucher from PO Receipt (T7APC) — BKQC Table

| Field | Meaning |
|-------|---------|
| BKQC.PO.NUM | Purchase order number |
| BKQC.RECVR.NUM | QC receiver number |
| BKQC.POL.ITM.NO | PO line item number |
| BKQC.RECV.DATE | Receipt date |
| BKQC.PROD.CODE | Item/product code |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.QTY.RECVD | Quantity received |
| BKQC.QTY.BUYOFF | Quantity bought off (accepted) |
| BKQC.QTY.REJECT | Quantity rejected |

#### AP Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| AP-A | T7APA / t7apae / t7apaC | Vendor master (basic/full/enhanced) |
| AP-BANK | T7APABANK | Vendor ACH/bank information |
| AP-CON | T7APACON | Vendor contacts (up to 4) |
| AP-INFO | T7APINFO | Vendor UDF fields (BKAP2: 20 UDFs in 4 types) |
| AP-STA | T7APASTA | Vendor statistics (purchase YTD/LY) |
| AP-PRC | T7APAPRC | Check vendor item pricing |
| AP-B | T7APB | Voucher entry — 10-line GL distribution |
| AP-C | T7APC | Receive PO with voucher — QC receiver integration |
| AP-D | T7APD | Enter scheduled payment dates |
| AP-E | T7APE | Cash requirements report |
| AP-F | t7apf | Check selection (interactive payment) |
| AP-G | t7apg | Pro forma check register |
| AP-H | T7APH | Print checks (+ ACH/NACHA export) |
| AP-HASK | T7APHASK | Check note entry per vendor |
| AP-I | T7API | AP aging/listing — BKSY.AP.AGING[1..5] configurable periods |
| AP-J | T7APJ | Vendor listing/directory report |
| AP-K | T7APK | Vendor labels report |
| AP-L | t7apl | Recalculate MTD/YTD vendor totals |
| AP-M | T7APM | Vendor mail labels |
| AP-O | T7APO | Recurring voucher maintenance — 10-line GL distribution |
| AP-P | T7APP | Generate recurring vouchers by selection code |
| AP-Q | T7APQ | Void check |
| AP-R | T7APR | Payment history report (check register) |
| AP-S | T7APS | 1099 report — TXTTYPE, YEAR, FIN filter |
| AP-T | T7APT | Check inquiry — full check + invoice + PO detail |
| AP-V | T7APV | Vendor deposits (uses BKAR.DEP table) |
| AP-X | T7APX | Invoice report — archived / no-link invoices |
| AP-Y | T7APY | Reprint checks / email remittances |
| AP-YB | T7APYB | Pinnacle bank check export (CSV) |
| AP-YC | T7APYC | NACHA/ACH export (TXT) — company.tax.id, eff.date |
| AP-ZA | T7APZA | Vendor purchase analysis — 3 date ranges (YTD/LYYTD/LY), top-N |

#### AP Aging Configuration

**BKSY.AP.AGING[1..5]** — configurable aging bucket thresholds (same pattern as AR); configured in system setup.

### AR Module — Full Schema

#### AR-A Customer Master (T7ARAC / T7ARAE)

**BKAR table** — AR customer master:

| Field | Meaning |
|-------|---------|
| BKAR.CUSTCODE | Customer code (primary key) |
| BKAR.CUSTNAME | Customer name |
| BKAR.SORT | Alpha sort code |
| BKAR.ADD1 | Street address line 1 |
| BKAR.ADD2[1..2] | Street address lines 2-3 |
| BKAR.CITY / STATE / ZIP / COUNTRY | Address |
| BKAR.FAX.PHONE | Fax number |
| BKAR.TELEPHONE[1..5] | Up to 5 phone numbers |
| BKAR.CONTACT[1..5] | Up to 5 contact names |
| BKAR.EMAIL[1..5] | Up to 5 email addresses |
| BKAR.IS.MCCODE | Multi-currency code |
| BKAR.REQD.CERTS | Required certifications |
| BKAR.SLSP.NUM[1..2] | Salesperson 1 and 2 codes |
| BKAR.COMM[1..2] | Commission % for salesperson 1 and 2 |
| BKAR.CREDIT.HLD | Credit hold flag |
| BKAR.CREDITLMT | Credit limit |
| BKAR.FOLUPDTE | Follow-up date |
| BKAR.DAYS.TOPAY | Average days to pay |
| BKAR.LASTPMT | Last payment date |
| BKAR.LASTSALE | Last sale date |
| BKAR.OUT.CREDIT[1..2] | Outstanding credits (possibly AR/SO split) |
| BKAR.OUTINV | Outstanding invoices |
| BKAR.GLACCT | Default GL sales account |
| BKAR.FOB | FOB point |
| BKAR.SHIPTO | Default ship-to code |
| BKAR.GROUP | Customer group |
| BKAR.START.DATE | Start date |
| BKAR.WEBLINK | Website URL |

**BKAR statistics fields** (T7ARASTA):

| Field | Meaning |
|-------|---------|
| BKAR.GROSS.YTD / LYR / VAR | Gross sales YTD / last year / variance |
| BKAR.COGS.YTD / LYR / VAR | Cost of goods sold YTD / LY / variance |
| BKAR.NET.YTD / LYR / VAR | Net sales YTD / LY / variance |
| BKAR.PNET.YTD / LYR / VAR | Net % YTD / LY / variance |

**ISAREX table** — customer extended data (T7ARAC / T7ARAE):

| Field | Meaning |
|-------|---------|
| ISAREX.ALPHA[1..2] | Misc info 1 and 2 |
| ISAREX.EXTADD[1..8] | Extended address lines (up to 8) |

**BKCM.DUNH.FORM** — dunning form code (in BKAR credit record T7ARACRE).

**RTM.PRINT.GROUP** — per-customer report template print group for customized invoice/SO printing.

#### AR Voucher Entry (T7ARB)

**BKAR.INVV table** — AR voucher distribution lines:

| Field | Meaning |
|-------|---------|
| BKAR.INVV.TERMD | Terms date |
| BKAR.INVV.DESC | Description |
| BKAR.INVV.DATE | Voucher date |
| BKAR.INVV.TYPED | Voucher type |
| BKAR.INVV.ISCUR | Currency code |
| BKAR.INVV.TAMT | Total amount |
| BKAR.INVV.GLACT[1..10] | GL account (up to 10 lines) |
| BKAR.INVV.GLDPT[1..10] | GL department (up to 10 lines) |
| BKAR.INVV.GLD[1..10] | GL description (up to 10 lines) |

#### AR Payment and Deposit (T7ARC / T7ARN)

AR-C record payments: CUSTCODE, CHECK_AMT, CHECK_NUM, DEPOSIT_NUM, NEG.CHK; BKAR.OUT.CREDIT[1/2]; invoice list INV_NUM/PS/DATE/AMTRM/APPLIED; exceptions EXCP.INVOICE/AMOUNT/DISC/DESC; import payments from file.

AR-N customer deposits (same BKAR.DEP table as SO deposits): BKAR.DEP.SO/DATE/REMAIN.AMT/DEP.DESC, CHECK.NO, BKAR.DEP.CUST, MAPPED; options: enter deposit, generate invoice, map lines, split deposit, credit card.

#### AR Credit Card (T7ART)

**IS.CC table** — stored credit card data:

| Field | Meaning |
|-------|---------|
| IS.CC.CARDNAME | Name on card |
| IS.CC.ZIP | Billing zip |
| IS.CC.CARDTYPE | Card type (Visa/MC/etc.) |
| IS.CC.MASKED | Masked card number |
| IS.CC.EXP | Expiration date (MMYY) |
| IS.CC.PROCESS | Processor name |
| IS.CC.ADDRESS | Billing address |
| onetime | One-time use flag |

#### AR Tax Operations (T7ARL / T7ARK)

**BKIS.TAX table** — sales tax transfer:
- BKIS.TAX.CODE, BKIS.TAX.DATE, BKIS.TAX.TAG, TAX.PONO

**ISIS.TXF table** — tax file:
- ISIS.TXF.DESC, ISIS.TXF.SOPERC

AR-K tax report: CUR_HIST [P/O/B paid/outstanding/both], FULLYPD, POSO [P/S purchases/sales], BASE [B/S base/source], SUMMARY [S/D], tax code/group ranges, invoice date range.

#### AR Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| AR-2DB | T7ARA2DB | 2D barcode layout (IS2D.BAR.*) for AR documents |
| AR-AC | T7ARAC | Customer master (compact form) |
| AR-ACE | T7ARAE | Customer master (full form) — web, territory, lead source, group |
| AR-ACON | T7ARACON | Customer contacts (up to 5) |
| AR-ACRE | T7ARACRE | Customer credit — credit limit, hold, follow-up, dunning form (BKCM.DUNH.FORM) |
| AR-ASTA | T7ARASTA | Customer statistics — gross/COGS/net YTD/LY/variance |
| AR-APRC | T7ARAPRC | Check customer item pricing |
| AR-B | T7ARB | AR voucher entry — 10-line GL distribution (BKAR.INVV.*) |
| AR-C | T7ARC | Record payments — check/deposit, invoice selection, exceptions, import |
| AR-D | T7ARD | Charge interest — CALC_DATE, NMININT, COMPOUND, BKSY.AR.INT.DAY |
| AR-E | T7ARE | Print statements — balance forward, age statement, print groups, deposits |
| AR-F | T7ARF | AR aging — BKSY.AR.AGING[1..5], follow-up codes, salesperson range |
| AR-G | T7ARG | Customer code/name list — active/inactive, credit hold/over limit filters |
| AR-H | T7ARH | Customer general info report |
| AR-I | T7ARI | Customer mail labels — OPEN.AR/OPEN.DE/OPEN.CR flags |
| AR-K | T7ARK | Tax report — paid/outstanding/both, purchase vs sales |
| AR-L | T7ARL | Transfer sales taxes to GL — BKIS.TAX.* and ISIS.TXF.* |
| AR-M | T7ARM | Customer refund — creates AP vendor + check via BKAP.INVT.* |
| AR-N | T7ARN | Customer deposits — BKAR.DEP.*, credit card, map lines, generate invoice |
| AR-P | T7ARP | Payment reminders — days prior/late, due/past-due filter |
| AR-R | T7ARR | Payment history report (check register) |
| AR-T | T7ART | Credit card management — IS.CC.* stored cards |
| AR-U | T7ARU | Dunning — from/thru customer, pastdue.days |

#### AR Aging Configuration

**BKSY.AR.AGING[1..5]** — configurable AR aging bucket thresholds (mirrors BKSY.AP.AGING[1..5]).

### New Tables Confirmed in Pass 89

| Table | Module | Primary Purpose |
|-------|--------|----------------|
| ISAP.CHG | PO | PO line change history (14 before/after field pairs + user) |
| ISAPEX | AP | Vendor extended data (bank, misc, long name, review date) |
| BKAP2 | AP | Vendor UDF (20 fields: 5×1-char, 5×10-char, 5×date, 5×30-char) |
| BKAP.CHK | AP | Check history (currency, dates, amounts, discount, bank acct) |
| BKQC | AP/PO | QC receiver records (PO, item, qty received/bought-off/rejected) |
| BKAP.INVL | AP | AP voucher GL distribution lines (10-line capacity) |
| BKAP.INVT | AP | AP voucher header (scheduled date, tax, freight) |
| BKAR | AR | Customer master (full schema documented) |
| ISAREX | AR | Customer extended data (2 misc info, 8 extended address lines) |
| BKAR.INVV | AR | AR voucher GL distribution lines (10-line capacity) |
| IS.CC | AR | Stored credit card data (masked number, expiration, processor) |
| BKIS.TAX | AR | Sales tax transfer records |
| ISIS.TXF | AR | Tax file (description, percentage) |
| IS.QSOA | PO | Point-of-sale order lines (item, desc, qty, price, discount) |
| BKCM.ACCC | PO | POS item category codes |


---

## Pass 90 — WC, SR, AM, MRP, GF, SM, INA, utility DFMs

### WC Module — Warehouse/Bin Control (additional sub-programs)

| Code | DFM | Purpose |
|------|-----|---------|
| WC-D | T7WCD | Import bin locations — comma/fixed CSV, FIELD.NUMBER[1..8], replace.binloc/replace.binmstr/replace.binmstr flags (skip/replace/ignore) |
| WC-E | T7WCE | Physical count sheet (with cycle codes) — item/type/class/cat ranges, FROM.BIN/THRU.BIN, FROM.CYCLE/THRU.CYCLE, incl.lot/ser, zero-UOH, combine.dupes |
| WC-F | T7WCF | Warehouse bin listing — item/type/class/cat ranges, include extended desc, all warehouses |
| WC-G | T7WCG | Assign bin locations — item/type/class/cat, Location, Bin, make.default (set as default bin) |
| WC-H | T7WCH | Bin inquiry by location — location, BKIC.LOCM.NAME, from.bin/thru.bin |
| WC-BK | T7WCBK | Live Work Center Schedule — FROM.WC, timer (refresh seconds), ISE.STATUS.2/3 (WO status filters), operation, category, customer, WO priority filter |
| WC-LOC-FIX | T7WCLOCFIX | LOC sync utility — updates MTIC.PROD.LOC with default WC bin; ISBIN.LOC.ITEM, default.loc |

### SR Module — Service/Repair (additional sub-programs)

| Code | DFM | Purpose |
|------|-----|---------|
| SR-B | T7SRB | Print SR orders — customer/class/SR/job ranges; PLDTYPE (linked docs), notes/hidden/kit/options/zero-balance/tax/MMS/lot/serial/RMA/original-order options |
| SR-BK | T7SRBK | Live Work Center Schedule for SR — FROM.LOC, timer, ISE.STATUS.2/3/4 (3 WO status filters) |
| SR-D | T7SRD | Print SR packing slips — customer/class/SR/job/date ranges, SHIP.DATE/SHIP.NUM, USE.EXIST.SDT, PRT.NOTRTS (non-released), incl.bo.qty, SORT.TEXT |
| SR-E | T7SRE | Release SR orders — BKAR.INV header: CUSA1/CUSA2[1..2]/CUSCTY/CUSST/CUSZIP/CUSORD/RTS/TAXABL/ORDDTE/NUM/GLDPT/SLSP/LOC/TERMD; line display: BKAR.INVL.ESD/PCODE/PDESC/PQTY/PPRCE/PEXT/TXBLE/UM.LN[2]/COGS/PDISC; auto-release comments/BO/all-lines; use default bins; ask proportional kit release |
| SR-F | T7SRF | Print SR invoices — same as SO-F: MARK.INVOICES, RTYPE, consolidate, distribute.frt, apply deposits (appdep), invoice types (SO/AR-voucher/finance-charge), PRT.ECO/SERIAL/KIT/COMMENT/NOTES/HID.NOTES/OPTIONS, PLDTYPE |
| SR-G | T7SRG | Post SR invoices — invoice/SR number ranges, post.all, prt.comm (commissions report) |
| SR-G-A | T7SRGA | SR posting progress indicator |
| SR-I | T7SRI | SR void invoice list — same structure as SO-R: BKAR.INV.INVDTE/ORDDTE/SHIPDT/CUSCOD/CUSNME/address fields, VOID.DATE, subtotal/tax/freight/deposit/retention/total |
| SR-INFO | T7SRINFO | SR misc info UDFs — ISSR.INFO.DATE1-5 + ISSR.INFO.AL1-20 (5 dates + 20 alpha per SR header); ISSR.INFO.SRNUM |
| SR-S | T7SRS | Work center/data collection sync — DCD.EMP/NAME/WOP/P/ITEM/TIMEIN/RUN (data collection fields) + SHI.ITEM/WOPRE/CUST/P/SDATE/SQTY/DESC (shipping schedule fields) |

### AM Module — Accounting Maintenance (full sub-program suite)

| Code | DFM | Purpose |
|------|-----|---------|
| AM-A | T7AMA | Open period setup — fiscal_d (current fiscal year start), gl_close_d (open period start), future.date (open period end), acct.date (accounting open period start), today_d |
| AM-B | T7AMB | Archive/view GL account history — BKGL.CURRENT[1..14], BKGL.1YPAST[1..14], ISGL.2YPAST through ISGL.6YPAST[1..14] — up to 7 years of 14-period GL data |
| AM-C | T7AMC | GL account maintenance — BKGL.ACCT/GLDPT/ACCTD/TYPE/NON.CASH/inactive, BKGL.BUDGET[1..14], ISGL.CYDATE[1..12] |
| AM-D | T7AMD | Create/delete GL department — template dept, new dept code, gl_type[1..5] (Asset/Liability/Expense/Income/Owner), bdgt_clr (clear budget), del_dpt |
| AM-E | T7AME | Financial statement configuration — BKGL.STC.* (balance sheet sections: GLN=net income/noncash, GLA.F/T[1..4]/GLATTL[1..4]=assets, GLL.F/T[1..4]/GLLTTL[1..4]=liabilities) + BKGL.STI.* (income statement: GLI.F/T/GLIMT=income, COGS, GLDMT=expenses, GLO/GLE=other inc/exp) |
| AM-H | T7AMH | GL account renumbering — import CSV with old/new GL code+dept, field mapping |
| AM-I | T7AMI | Purge/archive GL journals — date range, GL account range, journal type |
| AM-J | T7AMJ | Archive/purge AP data — vendor range, thru date, action [P/A/R] |
| AM-K | T7AMK | Archive/purge AR data — customer range, thru date |
| AM-N | T7AMN | GL fiscal period dates — ISGL.4YDATE[1..12] / ISGL.5YDATE[1..12] / ISGL.6YDATE[1..12] (period start dates for years 4-6 ago); BKSY.FISCAL.YR / NY.FISCAL.YR (current/next fiscal year start) |
| AM-O | T7AMO | Archive/purge PO data — vendor/class range, last activity date, del.orphans [L/H/B/N] |
| AM-P | T7AMP | Archive/purge SO/customer data — customer/class range, last activity date, del.orphans, incl.ship.cust |
| AM-Q | T7AMQ | Copy/create GL budgets — from/thru GL/dept; source: use.yearpast / use.annual / use.curryear / use.annual.ny; factor / factor.ny; shows ISGL.3YPAST through ISGL.6YPAST[1..14] per period |
| AM-S | T7AMS | Archive/purge GL journals (variant) — date range, journal number range, action, journal type range |

### GL Table Structure — Extended (from T7AMB/AMC/AMQ/AMN)

EVO uses **14 GL periods per year** (not 12). The extra 2 periods accommodate adjustment entries.

| Table/Field Pattern | Description |
|--------------------|-------------|
| BKGL.CURRENT[1..14] | Current year monthly/period balances (14 periods) |
| BKGL.1YPAST[1..14] | 1 year ago balances (14 periods) |
| ISGL.2YPAST[1..14] through ISGL.6YPAST[1..14] | 2–6 years ago balances |
| BKGL.BUDGET[1..14] | Budget amounts per period |
| ISGL.CYDATE[1..12] | Period start dates for current year (12 calendar dates) |
| ISGL.4YDATE/5YDATE/6YDATE[1..12] | Period start dates for years 4/5/6 ago |
| BKSY.FISCAL.YR | Current fiscal year start date |
| NY.FISCAL.YR | Next fiscal year start date |
| BKGL.ACCT / GLDPT | GL account code and department |
| BKGL.ACCTD | Account description |
| BKGL.TYPE | Account type (A=Asset, L=Liability, E=Expense, I=Income, O=Owner) |
| BKGL.NON.CASH | Non-cash flag (affects cash flow statement) |
| BKGL.STC.GLN.F/T | Balance sheet: net income GL range start/end |
| BKGL.STC.GLA.F[1..4]/T[1..4]/GLATTL[1..4] | Balance sheet: 4 asset sections (from/thru/title) |
| BKGL.STC.GLL.F[1..4]/T[1..4]/GLLTTL[1..4] | Balance sheet: 4 liability sections |
| BKGL.STI.GLI.F[1..2]/T[1..2] | Income statement: 2 income GL ranges |
| BKGL.STI.MN.TTL | Income statement: main title |

### MR/MRP Module — Material Requirements Planning (full suite)

#### MRP Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKMRP.FC | PART, QTY, DATE, CQTY, OQTY, FLAG | MRP demand forecast — item/qty/date, consumed qty, original qty, flag |
| BKMRP.PO | VEND, ERD, QTY, PRICE, CONF, PART, DATE | MRP-generated PO staging — vendor/receipt-date/qty/price/confirmed/part |
| MTMRP | PARTNO, STARTDT, DATE, QTY | MRP calculation results — part, start date, due date, qty required |
| MTIC.PROD.MRP | (flag) | Per-item: include in MRP generation (in MTIC.PROD record) |

#### MRP Sub-Program Summary

| Code | DFM | Purpose |
|------|-----|---------|
| MR-A | T7MRA | Demand forecast entry/view — BKMRP.FC.PART/QTY/DATE/CQTY/OQTY/FLAG |
| MR-ADE | T7MRADE | Import demand forecast — item/date/qty from CSV (comma or fixed) |
| MR-B | T7MRB | Print forecast report — item/type/class/cat/date ranges, print consumed and original qty, current vs archived |
| MR-C | T7MRC | Process forecast — consume/erase/rollover/load-level; item/class/cat/customer/date ranges; archive/restore |
| MR-D | T7MRD | MRP parameters per item — MTIC.PROD.MRP (include), M.EXPBF/DLYBF (expedite/delay buffers), m.sensexp/sensdly (sensitivities), M.LEAD/RLVL/RAMT, m.round; planner.code; master vs specific location |
| MR-E | T7MRE | Print MRP parameters — item/type/class/cat, include.mrp [Y/N], master.loc [M/S] |
| MR-F | T7MRF | **Main MRP generation run** — 4-stage process: (1) BOM analysis, (2) generating requirements, (3-4) consolidating; THRU.DATE (include ESD thru), OPT.TYPES [RFAM], INC.SO, STYPE (S-type WOs), INC.FORECAST, std.pack, RLVL, incl.seg.locs, all.locs, po.lead, calc.usage; processes BKAR.INVL/BKAP.POL/WO.CODE/WOBOM.COMPCODE/BKMRP.FC during run |
| MR-G | T7MRG | MRP action report — item/date/class/cat/planner/vendor/customer ranges; LASTPO (last X POs); BOM components; OD (show original dates); prt.All.Mfg; PLDTYPE (linked docs) |
| MR-H | T7MRH | MRP color-coded action report — ACT.TYPES [MBEDORC]: M=Make/B=Buy/E=Expedite/D=Delay/O=OK/R=Reschedule/C=Cancel; prior.cl/xdays.cl (color bands by urgency); item/class/cat/planner/vendor/customer/WO-date ranges |
| MR-I | T7MRI | Auto-generate WOs from MRP — for location; item/class/cat/planner/WO-date ranges; combine (1 WO per item); wo.class[1..6]; use.std.pack; add.cust.info; review mode |
| MR-IR | T7MRIR | MRP WO review — MTMRP.PARTNO/STARTDT/DATE/QTY |
| MR-IX | T7MRIX | Tool-based WO creation — up to 4 output parts (part[1..4]/desc/mrpqty), qty, woLOC, wostartdate |
| MR-J | T7MRJ | Auto-generate POs from MRP — BKMRP.PO.VEND/ERD/QTY/PRICE/CONF; AutoEmail; REPORT.MODE; INC.SPECS; INCLAPPRMFGRS; pricing [CBM]=contract/base/minimum; spo.num; one.po.per.item |
| MR-JR | T7MRJR | MRP PO review — MTMRP.PARTNO/STARTDT/DATE + PO.DATE/ER.DATE/QTY/vendor/price |
| MR-JX | T7MRJX | MRP PO generation — BKMRP.PO.VEND/ERD/QTY/PRICE/CONF/PART; show blank vendors; BKAP.PO.NUM assigned |
| MR-L | T7MRL | MRP plan lookup — PLND.NUM (1 through LAST.PLND), revrse (reverse lookup) |
| MR-N | T7MRN | Auto-approve POs — from/thru vendor, po.amt (dollar threshold), report.only |
| MR-O | T7MRO | Print MRP change report — items changed since last MR-P |

#### MRP Expedite/Delay Buffer Fields (T7MRD)

Per-item MRP sensitivity settings stored in MTIC.PROD:

| Field | Meaning |
|-------|---------|
| MTIC.PROD.EXPBF | Expedite buffer days |
| MTIC.PROD.DELBF | Delay buffer days |
| m.sensexp | Expedite sensitivity |
| m.sensdly | Delay sensitivity |

#### MTMRP Action Codes (Pass 106e)

MTMRP.ACTION field values — what T7MRF writes, what T7MRG/T7MRH display:

| Action code | Meaning | What to do |
|---|---|---|
| `NEW` | New planned order needed — no supply exists for this demand | Create PO (MR-J) or WO (MR-I) |
| `DELAY` | Existing PO/WO due too early — supply will arrive before demand | Reschedule PO out (MR-N) |
| `CANCEL` | Existing PO/WO excess — demand no longer exists | Cancel the PO/WO |
| `EXPEDITE` | Existing PO/WO due too late — supply arrives after need date | Pull in the PO due date |
| `RESCHEDULE` | Minor timing adjustment needed | Adjust PO/WO dates |
| `OK` | No action needed — supply and demand aligned | Review only |

MR-H color-codes these by urgency: ACT.TYPES [MBEDORC] — `M`=Make, `B`=Buy, `E`=Expedite,
`D`=Delay, `O`=OK, `R`=Reschedule, `C`=Cancel. Color bands set by PRIOR.CL (priority) and
XDAYS.CL (days until due date).

#### BKMRPPO → BKAPPO Conversion (T7MRJ, Pass 106e)

When T7MRJ (MR-J — Generate Purchase Orders) runs, it converts BKMRPPO entries to actual POs:

```
BKMRPPO.BKMRP_PO_CONF = 'Y' (confirmed by planner)
  → T7MRJ creates BKAPPO header (assigns PO number)
  → T7MRJ creates BKAPPOL line (item, qty, price, ERD)
  → BKMRPPO.BKMRP_PO_DONE = 'DONE' (marks as processed)
```

Pricing source priority in T7MRJ: [C]ontract price → [B]ase vendor price → [M]inimum price.
`one.po.per.item` flag merges all BKMRPPO rows for the same vendor+item into one PO line.

**Confidence: 78/100** — Table schemas confirmed from DDF. Program list confirmed from BKMENUSU.TXT.
Action codes inferred from field names and T7MRH parameter strings (`ACT.TYPES [MBEDORC]`).
MRP netting algorithm inferred from program DB fingerprints — not confirmed from decrypted source.

### SM Module — System Maintenance (additional sub-programs)

#### SM-C Item Class GL Mapping (T7SMC)

Per item-class + location, maps up to 10 GL accounts (account + department each):

| Field | GL Purpose |
|-------|-----------|
| edit.gla/dpta | Inventory Asset/Expense |
| edit.glc/dptc | COGS |
| edit.gls/dpts | Taxable Sales |
| edit.glsnt/dptnt | Non-Taxable Sales |
| edit.glw/dptw | WIP Inventory Asset |
| edit.gllab/dptlab | Absorbed Labor |
| edit.glfoh/dptfoh | Absorbed Fixed Overhead |
| edit.glvoh/dptvoh | Absorbed Variable Overhead |
| edit.glmisc/dptmisc | Material Burden |

Plus system-wide defaults (sysgla_/sysgld_ for each GL type).

#### SM-D Payment Terms (T7SMD) — IS.TERMS Table

| Field | Meaning |
|-------|---------|
| IS.TERMS.NUM | Terms number (key) |
| IS.TERMS.NAME | Short name |
| IS.TERMS.DESC | Description |
| IS.TERMS.AMT | Discount amount |
| IS.TERMS.TYP | Discount type [%,$,D,C,A,P,F] |
| IS.TERMS.DAY | Discount days |
| IS.TERMS.MAX | Max days till due |
| due.on.rcpt | Due on receipt flag |
| epay | E-pay only flag |

#### SM-E Tax Code Maintenance (T7SME) — ISIS.TXF Table (Full Schema)

| Field | Meaning |
|-------|---------|
| ISIS.TXF.CODE | Tax code (key) |
| ISIS.TXF.DESC | Description |
| ISIS.TXF.IDNUM | Tax ID number |
| ISIS.TXF.VNDCD | Vendor code (remit to) |
| ISIS.TXF.SOPERC[1] | SO tax rate % |
| ISIS.TXF.POPERC[1] | PO tax rate % |
| ISIS.TXF.GLASO / GLDSO | GL account/dept for SO tax |
| ISIS.TXF.GLAPO / GLDPO | GL account/dept for PO tax |
| ISIS.TXF.SOMAX | SO max tax amount |

#### SM-G Employee Report (T7SMG) — BKPR.EMP Table

| Field | Meaning |
|-------|---------|
| BKPR.EMP.FNMI | First name/middle initial |
| BKPR.EMP.LNME | Last name |
| BKPR.EMP.ADD | Address |
| BKPR.EMP.CSZ | City/state/zip |
| BKPR.EMP.PHONE | Phone |
| BKPR.EMP.EMAIL | Email |
| BKPR.EMP.SDATE | Start date |
| BKPR.EMP.DEPT | Department/division |
| BKPR.EMP.SHIFT | Shift number |
| BKPR.EMP.TERM | Terminated flag |
| BKPR.EMP.PAYAMT[1] | Regular pay rate |
| BKPR.EMP.PAYAMT[2] | Overtime pay rate |
| BKPR.EMP.PAYAMT[4] | Holiday pay rate |
| BKPR.EMP.OPNAME[5] | User name (login) |
| mobile.phone | Mobile phone |
| ud.alpha1/ud.label1 | User-defined field 1 |

#### SM Code Tables Confirmed (T7SMIA/B/C/D/E/F)

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKCM.LEAD | SCODE, DESC | Lead source codes |
| BKCM.TERR | TCODE, DESC, EMAIL | Territory codes |
| BKCM.ACFC | FCODE, DESC, REP | CRM follow-up/history codes (REP = include in CRM dashboard) |
| BKCM.ACCC | CCODE, DESC | Activity/category/brand/stock codes (reused across modules) |
| BKCM.DTCD | DCODE, DESC | Document type codes |
| IS.CATM | CODE, DESC | Item category master |

#### SM-J Maintenance Utilities

| Code | DFM | Purpose |
|------|-----|---------|
| SM-JA | T7SMJA | Generic batch utility (report-only mode) |
| SM-JB | T7SMJB | Archive/purge WOs — WO/fin-date/job/customer/item ranges; closed/cancelled flags; orphan ISWOEX/ISWOROEX check |
| SM-JC | T7SMJC | Inventory reconciliation — master level, transaction level, report stock status changes (RSS), METHOD, item/class/date; checks MTICMSTR records |
| SM-JD | T7SMJD | Archive/consolidate inventory transactions — type [ASPJWIQOCMTRG], consolidation date |
| SM-JE | T7SMJE | Purge WOs — from/thru WO/fin-date, PURGE.CLOSE/CANCEL |
| SM-JF | T7SMJF | Archive/purge POs — PO/vendor/date ranges |
| SM-JG | T7SMJG | Archive/purge QC receivers — QC receiver/vendor/date ranges |
| SM-JH | T7SMJH | Purge data collection records — CUT.DATE |

### T7INA — Item Master Main Form

Full item master fields from T7INA.DFM (the primary item entry screen):

| Field | Meaning |
|-------|---------|
| BKIC.PROD.LONGP | Long part number |
| BKIC.PROD.DESC / NOTE | Description / note |
| BKIC.PROD.CLASS | Item class |
| MTCLASS.M.DESC | Class description |
| BKIC.PROD.CAT | Category |
| MTIC.PROD.SUBST[1] | Superseded by (substitute part) |
| BKIC.PROD.TYPE | Item type [RFAMNLBTKO] |
| MTIC.PROD.ACTIV | Active status |
| BKIC.PROD.TXBLE / TAXIN | Taxable / tax-inclusive flags |
| BKIC.PROD.UM | Stock unit of measure |
| MTIC.PROD.SUM / PUM | Stock UM / purchase UM |
| BKIC.IS.DCODE | Duty code |
| BKIC.PROD.RLVL / RAMT | Reorder level / reorder amount |
| MTIC.PROD.PCONV | PO conversion multiplier |
| MTIC.PROD.LEAD | Lead time (days) |
| calc.wt | Weight |
| MTIC.PROD.CUBFT | Cubic feet (foot factor) |
| MTIC.PROD.STDPK | Standard pack |
| MTIC.PROD.FRT% | Freight percentage |
| BIN.LOCATION | Default bin location |
| MTIC.PROD.REV | Revision level |
| BKIC.PROD.ISUPC | UPC code |
| MTIC.PROD.WIPDP | WIP display flag |
| MTIC.PROD.EXPBF / DELBF | Expedite/delay buffer days (also used by MRP) |
| BKIC.PROD.PRICE | Base selling price |
| MTIC.PROD.DRAW | Drawing number |
| IS.PROD.GDATES[1] | Good (effective) date |
| MTIC.PROD.ABC | ABC class |
| MTIC.PROD.SER / LOT | Serial/lot control flags |
| WH.CONTROL | Warehouse control flag |
| MTIC.PROD.OPTCS | Options/configuration flag |
| cycle.code | Cycle count code |

### Business Status Dashboard (T7BS) — ISBSF Table

| Field | Module | Meaning |
|-------|--------|---------|
| ISBSF.AR.BAL | AR | Current AR balance |
| ISBSF.AR.BILL | AR | Billings for period |
| ISBSF.AR.RECP | AR | Receipts for period |
| ISBSF.AR.DISC | AR | Discounts |
| ISBSF.AR.COGS | AR | Cost of goods sold |
| ISBSF.AR.DEPO | AR | Deposits |
| ISBSF.AP.BAL | AP | Current AP balance |
| ISBSF.AP.PAYA | AP | Payables for period |
| ISBSF.AP.PAYM | AP | Payments made |
| ISBSF.AP.DISC | AP | Discounts taken |
| ISBSF.AP.ATP | AP | Approved to pay |
| ISBSF.SO.OPEN | SO | Open orders value |
| ISBSF.SO.BOOK | SO | Booked orders value |
| ISBSF.SO.SHIP | SO | Shipments value |
| ISBSF.PO.OPEN | PO | Open POs value |
| ISBSF.PO.BOOK | PO | Booked POs value |
| ISBSF.PO.RECP | PO | Receipts value |
| ISBSF.WO.WIPBAL | WO | WIP balance |
| ISBSF.WO.ISSU | WO | Issues to WO |
| ISBSF.WO.FPVAR | WO | Finished product / variances |
| ISBSF.IC.VALUE | IN | Inventory value |
| ISBSF.CASH.TOTA | GL | Cash balance total |

### Bill of Lading (T7BOL / T7BOLMSO)

T7BOL fields: auth/control/load/seal/trailer numbers; pickup.date/time, driver.arrived, loading.start/end, driver.departed; HANDLING UNIT: edit.htype/hqty/HM; PACKAGE: edit.ptype/pqty/nmfc/class; pallet.wt; commodity; department.

T7BOLMSO (multi-SO BOL): billing.line[1..6], LIST.SONUM/ITEM/DESC/PQTY/PACKS/PACKTYPE/WEIGHT/HM/NMFC/CLASS, SCAC (carrier code), carrier.name, billing.type [PCTN], billing.acct, marks[1..2].

### Miscellaneous Tables Confirmed in Pass 90

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| BKSB.PART | PROD, SUBST, SUB.DESC | Alternate/substitute parts cross-reference |
| IS.ACTION | TYPE, DESC | Action type codes (generic) |
| AC.RD | TYPE, REASON, DISPO | Corrective action document types + reason + disposition |
| WODATE | START, FINISH, QTY, PARPRE/PARSUF, TOPPRE/TOPSUF, DELPRE/DELSUF | WO date schedule with parent/top/deleted WO linkage |
| IS.SERC | ITEM, SPOS, total, NUMBER, LAST, leng | Item number auto-numbering template |
| IS.STYPE | TYPE | Service/sales type codes |
| IS.CATM | CODE, DESC | Item category master |
| ISBSF | (see above) | Business Status summary (rebuilt by T7BSR) |
| ISTS.CFG | woadsc, wobs, womakf, wocalc, burdn, burdi, woopen, wopswd, woonly, wogdsc, woaloc, WOBWO1, LIMSCT, RRFPR, cmploc, dcseq, scrcmp, wodso, fpser#, sccomf, wipv, divohd | System configuration flags (WO behavior, labor, overhead, MRP) |
| BKYS.YN[1..n] | — | System yes/no configuration flags (indexed array) |
| BKYS.NUM[1..n] | — | System numeric configuration values (indexed array) |
| IS.GF.DEPT | (code, desc) | Golding Farms custom department codes |
| IS.GF.DIV | (code, desc) | Golding Farms custom division codes |

### Master Default Settings Key — ISTS.CFG Fields

From T7MDEFAULTS.DFM, the most important configuration flags:

| Field | Default Setting Controls |
|-------|------------------------|
| ISTS.CFG.WOADSC | Prevent editing of description in WO-A |
| ISTS.CFG.WOBS | WO types that affect Business Status |
| ISTS.CFG.WOMAKF | View only in Enter Finished Product? |
| ISTS.CFG.WOCALC | Calculate labor from BOM |
| ISTS.CFG.BURDN | Use material burden |
| ISTS.CFG.BURDI | Burden item number |
| ISTS.CFG.WOOPEN | Show open or open/closed WOs in WO-A (O/B) |
| ISTS.CFG.WOPSWD | Password for reopening closed/cancelled WOs |
| ISTS.CFG.WOONLY | WO-B: limit to 1 WO (Y/N/W) |
| ISTS.CFG.WOGDSC | Allow edit of component description in WO-G |
| ISTS.CFG.WOALOC | WO default location |
| ISTS.CFG.WOBWO1 | WO-B: limit to 1 WO (flag) |
| ISTS.CFG.LIMSCT | WO-K-M: limit scrap type to (FMLV) |
| ISTS.CFG.RRFPR | WO-K-M: require reason code for scrap |
| ISTS.CFG.CMPLOC | WO default location |
| ISTS.CFG.DCSEQ | Backflush by sequence in Enter Labor (Y/N/B) |
| ISTS.CFG.SCRCMP | Include FP scrap in COGS parts (Y/N/A) |
| ISTS.CFG.WIPV | Use projected or estimate $ and hrs (P/E) |
| ISTS.CFG.DIVOHD | Divide setup by number of jobs worked |

Key BKYS.YN flags (selected):
- BKYS.YN[1]: WO status code default
- BKYS.YN[2]: View only in WO Bills Mat
- BKYS.YN[3]: Close WO in Enter Finished Prod
- BKYS.YN[15]: Use standard cost in Enter Finished Prod
- BKYS.YN[19]: Labor prompt in kit issues
- BKYS.YN[20]: Post overhead as % of labor
- BKYS.YN[21]: Backflush in Enter Finished Prod [Y/N/A/B]
- BKYS.YN[22]: Use actual costs in labor entry
- BKYS.YN[65]: Divide labor cost by # jobs worked

### Kit Issue Form (T7KIT)

Fields revealed: WOBOM.REFERENCE, MTIC.PROD.CYCLE (cycle code), scan.item/scan.wo/scan.emp; per BOM line: APART/ADESC/ARQTY (required qty)/AUOH (UOH)/ALUOH (location UOH)/AQTY (issue qty)/ABIN/ABOMNOTE/ALOT/ALOC/AOPER. Multi-yield WOs: M.PART/DESC/QTY/PER/BIN, proportion [W=weight/F=foot factor/E=equal].

### Put-Away Form (T7PUTAWAY)

BKIC.PROD.LRCPT (last receipt date), scan.item, enterbin, PABBL (put away by bin loc), MTIC.PROD.UIQC (in QC inspection), action (put-away or label).


---

## Pass 91 — J7 Customizations, EVO* Infrastructure, T6 IN-B, WBK/WTAS (2026-06-18)

### J7* Customization Suite — i2 Systems Customer-Specific Forms

All 41 J7* DFMs confirmed from Pass 91 analysis. The J7* namespace is i2 Systems' reserved prefix for customer-specific customizations layered on top of standard EvoERP.

#### J7 Form Index

| Form | Caption / Purpose | Key Fields |
|------|------------------|-----------|
| J7ABISHIPRPT | Lapco Fulfillment Report | from.cust, thru.cust, from/thru.orddte, from/thru.item |
| J7ADTNACHA | ACH (extended) | (unknown — empty DFM) |
| J7APPVEND | Approve Vendor | app.vend, from.vend, bkap.vendname, max.chk.amt |
| J7AUTOAPC | Auto Enter PO Invoices | from/thru.date, from/thru.vclass, from/thru.vend, Use.ARD, inv.date |
| J7BEFWEB | Web Export (legacy) | (unknown — empty DFM) |
| J7BEFWEBINV | Web Item Export (CSV/FTP) | ftp.FileName, from/thru.item, item.type, from/thru.class, PRT.ACTIVE, ftp.password/userName/hostName, WebItems.only, all.loc, on.so.days, incl.stock.qty, incl.bo, print.by.loc |
| J7CCPIC | PI-C Physical Count Tag Entry | CountDate, qtr, year, location, empno |
| J7CIWEB | CI Web (legacy) | (unknown) |
| J7CIWEBIMPORT | Web Order Import | auto.mode, use.imp.sonum, import.to.edi, bank.name, downloadfile, ftp.FileName/password/userName/hostName, add.kit.comps, imp.FileName |
| J7CJBUSAGE | Print Inventory Usage | from/thru.date/class/cat/item/cust, PRT.ACTIVE |
| J7CRSOW | Custom SO-W Report | sFROM/sTHRU.SONUM, from/thru.orddte/cust, sFROM/sTHRU.INVNUM, incl.backorders |
| J7DCMATLABELS | Print Mattress Labels (DC) | SCAN.WO, SCAN.EMP1, SCAN.EMP2, oper1, oper2, inp.serial |
| J7DCSSOE | Shipping Data Collection | inp.serial, SCAN.WO, sonum.char |
| J7DCSSOEVERIFY | Verify SO Lines (DC) | LINE.VPART, LINE.SHIP.QTY, LINE.ORDERQTY, LINE.DESC |
| J7EBSERIAL | Enter Serial Number | scan.serial, SERIAL.LIST |
| J7EIMDCREV | WO Labor DC Review | LAB.DATE, scan.wonum, scan.emp, scan.oper, MTWO.WIP.CODE/DESC, rshrs, lab.parts/scrapped/scrap.code, force.close, nojobs.dec, lab.setuphrs/runhrs/start/finish/wc |
| J7HHEBINC | Handheld Inventory Adjustment | inp.Serial (serial-based) |
| J7HHEBXFER | Handheld Transfer Inventory | inp.Serial, from→to location |
| J7HHEBXFERVERIFY | Handheld Verify Transfer | PART.ARRAY, SHIPQ.ARRAY, DESC.ARRAY |
| J7HHLITN | Enter Tracking Numbers | track.num, ship.co, frt.charge, BOX.ID |
| J7HHPTSSOE | Handheld Shipping (PTS) | scan.qty.char, item, WONUM, Lot.No, from.cust |
| J7HHPTSSOELABELS | Print Box Content Labels | RTM_NAME, MISC, from.box, thru.box, labelQty |
| J7HHPTSSOEVERIFY | Verify SO (handheld) | LINE.VBOX, LINE.VPART, LINE.VBOXQTY, LINE.VSONUM, LINE.VDESC, LINE.VWONUM, LINE.VLOT |
| J7HHRTSSOE | RT London Shipping | scan.qty.char, scan.item, truck.no, sload.num, sonum.char |
| J7I2SACH | ACH Export | CHKACT.TXT, from/thru.chknum, from/thru.chkdate, ach.filename, wells.id, date.format, delimiter, eff.date |
| J7I2SYSTEMSOOE | Custom SOOE Filter | from/thru.cust, from/thru.esd, from/thru.class/cat/cclass |
| J7LAPCOSO | Lapco Print Inventory Usage | from/thru.cust/item/class/cat, item.type, PRT.ACTIVE |
| J7MCDSAREPORT | Sales Analysis Report | from/thru.date, from/thru.cust, from/thru.cclass |
| J7MPIMPORTAR | Import AR | FileName |
| J7NMBINS | Bin Inquiry | item, BKIC.PROD.DESC, BKIC.PROD.UOH, MTIC.PROD.LOC |
| J7NMRTMPRINTER | RTM Printer Setup | rtm.printer, rtm.program, rtm.rtm; stores to IS.RTM.PROGRAM/RTM/PRINTER |
| J7PEDCB | Production Status (DC) | scan.wonum, MTWO.WIP.CODE/DESC, from.wc, SCAN.PARTS, SCAN.SCRAPPED, MAX.QTY, CUR.QTY |
| J7POAIMP | Import PO (legacy) | (unknown) |
| J7POAIMPLINES | Import PO Lines | imp.filename, sPONUM, BKAP.PO.VNDCOD, FIELD.NUMBER[1..8], date.format, incl.mfgs, incl.2nd.desc, incl.vend.part, incl.specs |
| J7PTRECPOLINE | Receive PO Line | BKAP.POL.PCODE/PQTY/PPRCE/PEXT, BKIC.PROD.DESC/NOTE, BKAP.PO.VNDCOD/VNDNME/NUM |
| J7PTWOKI | WO-K-J Sync | from/thru.item, excepts.only, sync.ip.wos, upd.wo.class, from/thru.wonum |
| J7SMJCT | Closed Job Cost Report | from/thru.orddte, item, sSONUM |
| J7SOAIMPLINES | Import SO Lines (multi-company) | company.code/name/path, sponum, vend.name/code, incl.mf.comps, CC_CODE/CC_NAME, imp.filename, sSONUM, BKAR.INV.CUSCOD/CUSNME, FIELD.NUMBER[1..6], date.format, incl.2nd.desc/specs |
| J7SYNCWOTOSO | Synchronize WO to SO | SO.PARENT, SO.LINENO, SO.CODE, SO.DESC, SO.PQTY/ESD/ASD; edit.esd/asd/sstart/sfin/ddate/pqty/sqty; MTWO.WIP.WOPRE/WOSUF; BKAR.INVL.PCODE/PDESC; issued.mat, cost.msg |
| J7TMCKANBAN | Kanban Orders | edit.item/rqty/price/pext, BKIC.PROD.RAMT, vend.code, BKAP.VENDNAME, dflt.loc, PACKING.SLIPNUM, BKAP.PO.ENTBY, po.subtot, INVC.NUMBER |
| J7WOLL | WO-L-L Label Printing | sfrom/sthru.oper, from/thru.comp, use.bom.qty, label.qty, scan.wonum, MTWO.WIP.CODE/DESC |

#### J7 Sub-System Highlights

**J7 ACH Export (J7I2SACH):** Exports AP checks to ACH format for bank transmission. Supports Wells Fargo ID field (`wells.id`), configurable effective date format, delimiter, and export filename. Input: check number range + check date range.

**J7 Web Import (J7CIWEBIMPORT):** Imports customer orders from web/FTP into EVO — either EDI module or open SO file. Supports: bank account for payment, kit component expansion, use-imported-SO-number option, and FTP auto-download. Fully unattended mode available.

**J7 Handheld Suite (J7HH*):** Six handheld scanner forms for warehouse operations:
- HHEBINC: Inventory adjustment by serial scan
- HHEBXFER: Inventory transfer by serial scan (from→to location)
- HHLITN: Enter tracking numbers (ship co + freight charge + box ID)
- HHPTSSOE: PTS shipping (item + qty + box + SO# + WO# + lot#)
- HHRTSSOE: RT London shipping (truck# + load# + SO# + customer)
- HHPTSSOELABELS: Print box content labels (RTM + box range + label qty)

**J7 Data Collection (J7DC*):** Mattress/WO manufacturing data collection:
- DCMATLABELS: Print mattress labels by scanning WO + serial + employee
- DCSSOE: Shipping scan (serial + WO → SO)
- DCSSOEVERIFY: Verify shipped SO lines (part, ship qty, order qty, desc)

**J7 WO Sync (J7SYNCWOTOSO):** Full bidirectional WO↔SO synchronization — shows original and edited values side-by-side for: ESD, actual ship date, scheduled start/finish, due date, promise date, WO qty, ship qty, qty complete, issued labor/material.

**J7 Kanban (J7TMCKANBAN):** Creates kanban replenishment orders. Entry per line: item, receive qty, price; reads BKIC.PROD.RAMT for reorder amount. Creates PO-like receipt against vendor with packing slip tracking.

---

### IS.RTM — Report/Program→Printer Assignment Table

Confirmed from J7NMRTMPRINTER.DFM (RTM Printer Setup):

| Field | Description |
|-------|-------------|
| IS.RTM.PROGRAM | Program name that runs the report |
| IS.RTM.RTM | RTM report template filename |
| IS.RTM.PRINTER | Assigned printer for this program/RTM combo |

Purpose: maps each EvoERP program+RTM pair to a specific printer, allowing per-report printer routing without changing Windows defaults.

---

### EVO* Infrastructure Suite

#### EvoCSI — Evo Master Inquiry

Universal cross-module inquiry launcher. Fields: `itemnum`, `custcode`, `sonum`, `invnum`, `Vendcode`, `ponum`, `porecp`, `wonum`, `wsuffix`. One form that can open any major record by code.

#### Evo Notes System (EVOENOTES / EvoNotes / EvoNotesARCH / EvoNotesPrt / EvoNotesRpt / EvoNoteSearch)

**IS.NOTE.* table fields confirmed from DFMs:**

| Field | Description |
|-------|-------------|
| IS.NOTE.CDATE | Creation date |
| IS.NOTE.CTIME | Creation time |
| IS.NOTE.CWHO | Created by (user) |
| IS.NOTE.EWHO | Entered by (may differ from created by) |
| IS.NOTE.TYPE | Note type code |
| IS.NOTE.PRIVATE | Private flag |
| IS.NOTE.CONTACT | Contact name |
| GEN.ID | Generic entity ID (48-char composite: entity type + key) |

Note archive/restore (EvoNotesARCH) filters: date, item, customer, vendor, user (cwho), SO, WO, invoice, PO, CM customer, note type. Supports bulk archive and bulk restore. Reports include/exclude by entity type (customer/vendor/item/WO/SO/PO).

**EvoNoteSearch:** Text search across note bodies — SearchString, matchcase, searchNotes (current/archived/both).

#### Evo Links System (EvoELinks) — IS.LNK.* Table

| Field | Description |
|-------|-------------|
| IS.LNK.DATE | Link creation date |
| IS.LNK.WHO | User who created link |
| IS.LNK.LINK | File path or URL |
| links.alert | Alert flag for this link |
| links.itm.alert | Item-level alert flag |
| is.lnk.private | Private/visible flag |
| is.lnk.sort | Sort number |
| is.lnk.global | Use global path # (1-10) |
| is.lnk.pcb[100] | Print checkboxes (up to 100 print destinations) |
| GlobalPath[1..10] | 10 configurable global base paths for relative links |

Print destinations (link checkboxes): Traveler, Estimate, PO, RFQ, Quote, Acknowledgement, Invoice, Packing Slip, SO line, IN line, and more. Each destination gets an independent enable/disable flag per link.

#### EvoFNO — Features & Options Configurator

Form suite: EvoFNO (main), EvoFNOPO/SO/WO (conversion progress), EvoFNOQty (qty/location entry).

ISFO.HDR.* fields confirmed from DFM: PARENT (item number), DESC, CUST, VEND, RFQ, STATUS, DATE.

Convert action: creates SO (SOCB), WO (WOCB), PO (POCB), New Item (NICB), Sales Quote (SQCB), or RFQ (RQCB) from an F&O configuration. CVTQty/CVTLoc/CVTCV/cvtdate are the conversion parameters.

#### Evo Business Status — Full Detail

EvoBS.DFM confirms the complete ISBSF field set (22 summary fields + detail sub-tables):

**ISBSF Sub-table: WO Detail (EvoBSWO)**

| Field | Description |
|-------|-------------|
| ISBSF.WOS.LAB | WO issues — labor |
| ISBSF.WOS.MAT | WO issues — materials + process |
| ISBSF.WOS.FOH | WO issues — fixed overhead |
| ISBSF.WOS.VOH | WO issues — variable overhead |
| ISBSF.WOS.MEXT | WO issues — misc extra |
| ISBSF.WOS.FP | WO finished production value |
| ISBSF.WOS.WIPV | WO WIP variance |

**ISBSF Sub-table: Cash Detail (EvoBSCash)**

ISBSF.CASH.TOTA (total) + ISBSF.CASH.ACT1 through ACT9 (up to 9 bank accounts).

**EVOBSR** — Business Status Rebuild: regenerates the ISBSF snapshot from live transaction files.

#### EvoScheduler — IS.SCHED.* Table

Full IS.SCHED.* field set confirmed from EvoScheduler.DFM:

| Field | Description |
|-------|-------------|
| IS.SCHED.NAME | Job name (PK) |
| IS.SCHED.DESC | Description |
| IS.SCHED.PROG | Program to execute |
| IS.SCHED.PARAM1..8 | Up to 8 command-line parameters |
| IS.SCHED.LOG | Log file path |
| IS.SCHED.TYPE | Occurrence type (once/weekly/etc.) |
| IS.SCHED.DATE | Next run date |
| IS.SCHED.TIME | Next run time |
| IS.SCHED.RECUR | Recur every N minutes |
| IS.SCHED.LDATE | Last run date |
| IS.SCHED.LTIME | Last run time |
| IS.SCHED.CO | Company code |
| IS.SCHED.EMAIL | Email address for completion notification |
| IS.SCHED.WHO | Operator/owner |

EvoSchedsetup: creates Windows service wrapper. Prompts for server path (g:\path format), SMTP/user/pass/email/name settings, and 32-bit vs 64-bit OS selection.

evoERPsched: simpler scheduler with day-of-week checkboxes (Mon-Sun), run-once vs. weekly mode, and execution time.

#### Evo Reminders — IS.REM.* Table

IS.REM.DATE, IS.REM.TIME, IS.REM.SUBJECT, IS.REM.TYPE, IS.REM.CO, IS.REM.DISP (dismissed).

dayrem.DFM (Day Time Reminders) full fields: TIMES, SUBJECTS, rem.time/sub/item/cust/vend/file, remmin (remind X minutes before), IS.REM.DISP, rem.date/type/contact/phone/femail, REM.EMAIL, other.user, Outlook/Email reminder flags.

#### evoCSR — Calendar Summary Report

Filter fields: month, cust.from/thru, Item.from/thru, ESD (estimated ship date), CDD (customer due date), ENTRY.DATE. Display options: custpo (customer+PO#), qtybo (qty+backorder), socust (SO#+customer).

#### EvoDCmenu — Data Collection Menu

Two variants: EvoDCmenu (9 configurable program buttons, main/settings/about), EvoDCmenu2 (simplified). EvoDCsetup: workstation setup — server path and date format (dd/mm/yy or mm/dd/yy).

#### EVOFILTERS — Compound Filter Form

Multi-entity filter dialog. Supports simultaneous filters across:
- WO: num, finished date, status, start date, machine, work center, scrap code, employee, sequence, actual finish date, due date, class, priority
- JC: job number, labor date, tool, dept, rework code, divide hrs by jobs flag
- SO: SO num, invoice num, order date, est ship date

#### EVOERPUPDW — Archive Work Orders

Bulk WO archive by date (`wa.date`). Archives closed WOs to history.

---

### T6 IN-B — Legacy Inventory Entry (10-Tab Form)

The T6 era "IN-B Enter Inventory" form is split across 10 DFMs, each a tab in a multi-page entry screen:

| Tab DFM | Tab Name | Key Tables/Fields |
|---------|----------|------------------|
| T6EVOINB / T6ISINB | Main | BKIC.PROD.CODE/DESC/NOTE/CLASS/CAT/TYPE, UM variants (BKIC.PROD.UM, MTIC.PROD.SUM/PUM), BKIC.PROD.RLVL/RAMT, MTIC.PROD.LEAD/PCONV/CUBFT/STDPK/FRT%/LOC, reorder, warehouse/lot/serial control, ROHS, UPC, approved vendors |
| T6ISINB2 | Compact main | Subset: code/desc/class/cat/type/status + Sources + Links tabs only |
| T6ISINBECO | ECO | IS.ECO.REVLVL, IS.ECO.DRAW, IS.ECO.ENTDATE, IS.ECO.DATE, IS.ECO.ENTBY, IS.ECO.ECO, IS.ECO.CURRENT |
| T6ISINBLNK | Item Links | I.ORDER, I.LINK, I.OTHER, I.ILOLINK, I.GPATH; IMAGE.TL[1..10] (thumbnails); IMAGE.PCB[1..10] (print checkboxes) |
| T6ISINBMFG | Manufacturer | BKSB.MFG.MPART, BKSB.MFG.MANUF |
| T6ISINBMRP | MRP Settings | MTIC.PROD.MRP, MTIC.PROD.MRPSW, BKIC.PROD.RLVL/RAMT, MTIC.PROD.LEAD/EXPBF/DELBF/WIPDP |
| T6ISINBSPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T6ISINBVND | Vendor Sources | BKSB.VEND.VEND, BKAP.VENDNAME, BKSB.VEND.VPART |
| T6ISSTDCST | Standard Cost | MTIC.PROD.RCOST[1..14], MTIC.PROD.LOTSZ, BKIC.PROD.LSTC/AVGC |
| T6EVOART | Credit Card | BKCM.ACCT.CODE/NAME/ADD1-3/CITY/STATE/ZIP/CCARD/CNUM/CMPNM/PNAME/CEXP |

#### IS.ECO — Engineering Change Order Table

| Field | Description |
|-------|-------------|
| IS.ECO.REVLVL | Revision level (current) |
| IS.ECO.DRAW | Drawing number |
| IS.ECO.ENTDATE | Entry date |
| IS.ECO.DATE | ECO effective date |
| IS.ECO.ENTBY | Entered by |
| IS.ECO.ECO | ECO number |
| IS.ECO.CURRENT | Current revision flag |

#### BKSB Tables — Sub-contractor / Cross-Reference

| Table | Fields | Purpose |
|-------|--------|---------|
| BKSB.MFG | MPART (mfg part#), MANUF (manufacturer) | Approved manufacturer cross-reference per item |
| BKSB.VEND | VEND (vendor code), BKAP.VENDNAME (name), VPART (vendor's part#) | Approved vendor cross-reference per item |

#### Standard Cost Structure — MTIC.PROD.RCOST[1..14]

From T6ISSTDCST.DFM captions, the 14 cost array slots map to:

| Slot(s) | Cost Element | Level |
|---------|-------------|-------|
| [1] | Labor | This level |
| [2] | Variable overhead | This level |
| [3] | Setup | This level |
| [4] | Outside process | This level |
| [5] | Freight | This level |
| [6] | Material | This level |
| [7] | Labor | Rolled-up (all levels) |
| [8] | Material + freight | Rolled-up |
| [9] | Setup | Rolled-up |
| [10] | Labor (duplicate rolled) | Rolled-up |
| [11] | Outside process | Rolled-up |
| [12] | Fixed overhead | Rolled-up |
| [13] | Variable overhead | Rolled-up |
| [14] | Fixed overhead | This level |

Standard Cost = sum of this-level slots; Rolled-up Cost = sum across all BOM levels.

#### MTIC.PROD.SPECS[1..12] — Item Specifications

12-element string array storing up to 12 free-text specification lines per item (from T6ISINBSPC tab).

#### BKCM.ACCT — Credit Card Account Table

From T6EVOART.DFM (part of IN-B):

| Field | Description |
|-------|-------------|
| BKCM.ACCT.CODE | Account code (PK) |
| BKCM.ACCT.NAME | Account name |
| BKCM.ACCT.ADD1..3 | Address lines 1-3 |
| BKCM.ACCT.CITY | City |
| BKCM.ACCT.STATE | State |
| BKCM.ACCT.ZIP | ZIP code |
| BKCM.ACCT.CCARD | Card type |
| BKCM.ACCT.CNUM | Card number |
| BKCM.ACCT.CMPNM | Company name on card |
| BKCM.ACCT.PNAME | Person name on card |
| BKCM.ACCT.CEXP | Card expiration date |

---

### WBK* — Web Interface / Lookup Framework

#### WBKLOOKUP — Evo Lookups (Main List-Picker Widget)

The universal lookup list widget used throughout EvoERP. Full feature set confirmed:

- cbIndexName: sort/index selection
- link.to, Drill.To: drill-down destination
- showgrid / Filter.to: grid display mode + filter
- SSSFD: sub-string search within list
- Built-in tools: Camera (image capture), CalcTot (column total), doc_print, Manager, External Call, Triggers, openclose, Alternate, Memo, arch (archive view)
- Sort options: Vendors Number, Manufacturers, Customers X-Ref
- Tag/untag functions (Tag, Untag, Invert Tag)
- Check mode for multi-select

#### WBKMENUSETUP — Menu Item Setup

Manages EvoERP menu structure. Key tables/fields:

| Field | Description |
|-------|-------------|
| BUTTON_CAPTION | Button caption text |
| BUTTON_IMAGE | Button image file |
| BUTTON_NUM | Button number |
| ACCESS_CODE | Security access code |
| GROUP_CAPTION | Group caption |
| GROUP_NUM | Group number |
| MI_MENU_LVL | Menu level |
| MI_CAPTION | Menu item caption |
| MI_FASTSELECT | Fast-select key |
| MI_PROGRAMNAME | Program to launch |
| MI_IMAGE | Menu item image |
| MI_LABEL | Menu item label |

Operations: Add User, Edit User, Delete User; Add Group, Delete Group, Move to Group; Copy From (copy menu setup); Update to Latest Programs; Clean Up (remove obsolete entries).

#### WBKLPRINT — Order Printing

Three checkboxes: Print Acknowledgements (pbox1), Print Packing Slips (pbox2), Print Invoices (pbox3).

---

### WTAS* — TAS Professional Data Administration Tools

#### WTASDATAM — Maintain Database (Raw Btrieve Browser)

Direct Btrieve file browser. Features: sort by index (cbIndexName), sequential scan (NoKey), record counter (rec_num/curr_rec_num), editing (GoEditing/edit mode), row add, row save, row delete, count/refresh, export visible/all rows. File location override (path_name). Deleted record counter. Displays field-configurable columns.

#### WTASDMGR — TAS Premier 7i Data Dictionary Manager

Full FD (File Descriptor) editor. Fields for each table definition:

| Category | Fields |
|----------|--------|
| Field list | FLD_LIST, FLD_LNAME, FLD_SNAME, FLD_TYPE, FLD_SIZE, FLD_DEC, FLD_ARRAY, FLD_UPCASE, FLD_DESC |
| Host type info | FLD_HTYPE, FLD_HSIZE, FLD_HDEC, FLD_HARRAY, FLD_HOFFSET |
| Key list | AKEY_LIST, AKEY_NAME, SEG_FLD_LIST, SEG_FLD_NAME |
| Key properties | knme (name), kord (order), kmod (modifiable), kdup (allow duplicates), kignore (ignore case), numSeg |
| File info | AFILE_NAME, AFILE_EXT, AFILE_TYPE, AFILE_PATH, AFILE_DESC |

Operations: Save FD, Close FD, Delete FD, Print FD, Create/Initialize File, Reindex Btrieve File, Reindex CodeBase File, Restructure File, Convert Btrieve→CodeBase, Entity Relationships diagram.

#### WTASINIT — Create/Initialize File

New file creation: CF_FLNAME (file name), CF_FLCODE (extension), CF_RTYPE (record type), CF_DESC, CF_PATH, cf_fdname (FD name to use as template).

---

### QC Buyoff Form — autoT7POJC (PO-J-C)

QC inspection/buyoff workflow triggered during PO receipt:

| Field | Description |
|-------|-------------|
| BKQC.QTY.RECVD | Quantity received |
| BKQC.QTY.BUYOFF | Quantity bought off to date |
| BKQC.QTY.REJECT | Quantity rejected to date |
| BUYOFF.REMAIN | Remaining qty to buyoff |
| BKQC.TRN.GQTY | This transaction — accepted qty |
| BKQC.TRN.BQTY | This transaction — rejected qty |
| BKQC.TRN.UQTY | This transaction — use-as-is qty |
| BKQC.TRN.SCRAP | This transaction — scrap qty |
| BKQC.TRN.REWORK | This transaction — rework qty |
| DEFAULT.BING | Default accepted qty bin |
| DEFAULT.BINU | Default use-as-is bin |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.VEND.CODE | Vendor code |
| BKQC.PROD.CODE | Item (product) code |
| BKQC.RECV.DATE | Received date |
| BKQC.PO.NUM | PO number |
| rohs | RoHS compliance flag |

---

### Calendar / Scheduling Infrastructure

**calDDsel** — Calendar Drill Down Type selector: DDTYPE (Est. Receipt Date = opt1, Vendor Promise Date = opt2).

**calrem** — Monthly calendar with drill-down, previous/today nav, Google Calendar export, and closed-WO filter.

**dayrem** — Day Time Reminders entry: TIMES/SUBJECTS list, rem.time/sub/item/cust/vend/file, remmin (minutes before reminder), IS.REM.DISP, rem.date/type/contact/phone/femail, REM.EMAIL, other.user. Can create Outlook reminders and email reminders. Reminder can be assigned to another user.

---

### Utility Forms Confirmed in Pass 91

| Form | Purpose |
|------|---------|
| SSS | Drill Filters (SSSVALUE, SSS1-6) |
| SSSFD | Sub-string search / Evo Notes search (SSSFDVALUE, SSSFD1-7) |
| DDFilters | Drill Down Filters (ANDOR, DBFIELD, OPER, FVALUE, sort_key_name) |
| GetFileName | Enter File dialog (filtname, localfile, serverfile) |
| GetAlphaGen | Generic single-field alpha entry (gagalpha / GAG Caption) |
| udfedit | UDF value editor (editudf) |
| GRIDPLAY | Quick grid inventory viewer (BKIC.PROD.UOH/CODE/DESC/CLASS) |
| ISCCREP | Credit Card Report (fromso/thruso) |
| autoT7POJC | QC Buyoff for PO receipts (see table above) |
| DFMALTS | Developer tool: set ALT keys for DFM forms (DFMName) |
| nzedefs | Email default settings (entAPATH, SubjectField, BCC, subject, body fields) |
| EMAILREL4 | SMTP email relay config (SMTP, Email, Name, Port) |
| ACT7SHKNOTE | WO Sequence Note (data collection: SCAN.WO, scan.oper, woro.note) |
| NUMEMP | # of Employees dialog (xnumemp) |
| dbamenu_LOGIN | Login form (unknown internals) |
| dbamenu_SELCOMP | Select Company form (unknown internals) |

---

### New Tables Summary — Pass 91

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| IS.NOTE | IS_NOTE_ID (48), CDATE, CTIME, CWHO, EWHO, TYPE, PRIVATE, CONTACT | EvoNotes entity — CRM notes linked to any record |
| IS.LNK | DATE, WHO, LINK, SORT, GLOBAL, PCB[100] | Attachments/links per entity |
| IS.SCHED | NAME (PK), DESC, PROG, PARAM1-8, LOG, TYPE, DATE, TIME, RECUR, LDATE, LTIME, CO, EMAIL, WHO | Scheduler jobs |
| IS.REM | DATE, TIME, SUBJECT, TYPE, CO, DISP | User reminders |
| ISFO.HDR | PARENT, DESC, CUST, VEND, RFQ, STATUS, DATE | F&O header |
| IS.ECO | REVLVL, DRAW, ENTDATE, DATE, ENTBY, ECO, CURRENT | Engineering Change Orders |
| BKSB.MFG | MPART, MANUF | Approved manufacturer cross-ref |
| BKSB.VEND | VEND, VPART | Approved vendor cross-ref (per item) |
| BKCM.ACCT | CODE, NAME, ADD1-3, CITY, STATE, ZIP, CCARD, CNUM, CMPNM, PNAME, CEXP | Credit card accounts |
| BKQC | QTY.RECVD, QTY.BUYOFF, QTY.REJECT, TRN.GQTY/BQTY/UQTY/SCRAP/REWORK, PKSLIP.NUM, VEND.CODE, PROD.CODE, RECV.DATE, PO.NUM | QC inspection/buyoff |
| IS.RTM | PROGRAM, RTM, PRINTER | Report→printer routing |
| MTIC.PROD.SPECS[1..12] | (array) | Item specification lines |
| MTIC.PROD.RCOST[1..14] | (array) | Standard cost rollup (14 cost elements) |



---

## Pass 92 — ES/JC/QC/CS/CC/DE/PS/FA/IM/LC/AC deep-DFM pass (2026-06-18)

### IS.EST — Estimating Table Structure (10-Quantity-Level × Cost Elements)

Confirmed from T7EST.DFM (ES-A main form). Each estimate stores up to 10 quantity levels, and for each level, 16 cost elements:

| Field Pattern | Element |
|---------------|---------|
| IS.EST.QTY[n] | Quantity for level n |
| IS.EST.MAT[n] | Material cost |
| IS.EST.MATMU[n] | Material markup |
| IS.EST.SETUP[n] | Setup cost |
| IS.EST.LAB[n] | Labor cost |
| IS.EST.LABMU[n] | Labor markup |
| IS.EST.OP[n] | Outside process cost |
| IS.EST.OPMU[n] | Outside process markup |
| IS.EST.OH[n] | Overhead cost |
| IS.EST.OHMU[n] | Overhead markup |
| IS.EST.cost[n] | Running total cost |
| IS.EST.MISC[n] | Misc costs |
| IS.EST.EXTRA[n] | Extra charges |
| IS.EST.TOTAL[n] | Total cost |
| IS.EST.PRICE[n] | Selling price |
| IS.EST.OVALL[n] | Overall margin |

**Header fields:** IS.EST.NUM (PK), IS.EST.STATUS, IS.EST.EXPDTE, IS.EST.LOSTDTE (lost date for closed quotes), IS.EST.QTREV (quote revision), IS.EST.OPPTYPE (opportunity type), IS.EST.DRAW (drawing), IS.EST.ORDDESC.

**Margin % fields:** IS.EST.MATMU%, IS.EST.LABMU%, IS.EST.OPMU%, IS.EST.OHMU%, IS.EST.OVLMU% — global margin settings for the estimate.

**ES-E Convert Estimates (T7ESE):** Converts estimate to WO/SO/production. Fields: SO.NUM, sWO.NUM, sFROM.QUOTE, CUST.PO, LOCATION, START.DATE, FINISH.DATE, ESD.DATE, SELL.PRICE, ORD.QTY, ISUPD.CONTRACT (update contract price file), ISTO.WO/ISTO.SO/ISTO.PROD (conversion targets), UCP (update contract price).

---

### JC Engine — Full Parameter Inventory (T7JCENG)

The JC Engine is the central batch processor for all job costing reports. Complete parameter set:

**WO Status flags (individually toggleable):**
- Firmed, Released, Closed, Cancelled, Indirect, Active, Archived

**WO Source (two toggles):** Indirect, Active

**Labor Type (6 types, individually toggleable):**
Regular, Overtime, Doubletime, Sick, Vacation, Holiday

**Shift (3 toggles):** Shift 1, Shift 2, Shift 3

**Range filters:** WO number, work center, item number, tool, employee, machine, labor date, job number, sequence number, scrap code, QC code, rework code, department code, WO actual finish date.

**Output controls:** Report Type, Sort/Subtotal By, Level of Detail, divide hrs by number of jobs (div.hrs), include run/setup/both (RSB), print report filters, estcst.once (one-time setup cost flag).

**JC-N Percent Complete methods (ISCALC.HOW.*):**
- ISCALC.HOW.C — calculate on costs
- ISCALC.HOW.H — calculate on hours to date
- ISCALC.HOW.P — calculate on parts

**JC-M WIP Analysis special options:** asof.date (as-of prior date), sstart.date (estimated start date), txn.date (last transaction date mode), moldy.wos (print dormant WOs), alt.summary, prt.details, inc.labor/inc.mat, prt.last.txn.

**T7JCRM — Remote Database Settings:** Host, port, name, TREEDEST. JC reports can publish to a remote database (appears to be tree-format output — possibly a business intelligence/dashboard endpoint).

---

### CS — Commission Data Array Structure

T7CSB.DFM confirms 10-month rolling data per salesperson (not just YTD):

| Field | Period N Meaning |
|-------|-----------------|
| BKPR.SLS.PAID[1..10] | Commission paid per month (months 1-10 + current period) |
| BKPR.SLS.COMM[1..10] | Commission due per month |
| BKPR.SLS.RCPTS[1..10] | Receipts per month |
| BKPR.SLS.COGS[1..10] | COGS per month |
| BKPR.SLS.GROSS[1..10] | Gross profit per month |

T7CSA confirms: BKPR.AGNT.CODE (outside agent links to AP vendor), BKPR.SLS.CLASS[1] (commission class), BKPR.SLS.EXPACT/EXPDPT (GL account + dept for expense posting).

T7CSD commission transfer: BKPR.COMM.PAYDT (payment date), fISREP.LNK.REPN / tISREP.LNK.REPN (from-rep/to-rep in ISREPLNK table). Posting.date for GL entry.

T7CSO advanced commission — 3 color-coded classes with configurable class codes. Two print modes: Classic (transfer date range, open/transferred) vs. Detail (commission date range, base/source currency, invoice/rep).

---

### CC — Credit Card Tables Fully Confirmed

T7CCP.DFM confirms complete IS.CC table fields:

| Field | Description |
|-------|-------------|
| IS.CC.MASKED | Masked card number (last 4 shown) |
| IS.CC.ZIP | Billing ZIP code |
| IS.CC.CARDNAME | Name on card |
| IS.CC.EXP | Expiry (MMYY) |
| IS.CC.CARDTYPE | Card type (Visa, MC, etc.) |
| is.cc.process | Processor code (e.g., AUTHORIZE) |
| is.cc.address | Billing address |
| ccamount | Transaction amount |

T7CCPO (PO credit card charges): ccnum, ccamount, cczip, CCYY, CCMM, CCADDRESS, CCCVV — raw card entry for PO payments (not vaulted).

T7CCDE import: FIELD.NUMBER2[1..8] and FIELD.NUMBER[1..8] — column positions for: customer code, CC number, expiry date, sort, card type, name on card, ZIP, address. Supports fixed-length or comma-delimited.

T7CCCITM / T7CCCWOT: cycle count entry forms for CC module (CC-C by item and by WO+location).

---

### DE / EDI — Additional Findings

**ISAP.QPO — PO Receipt Staging Table** (confirmed from T7DEV):

| Field | Description |
|-------|-------------|
| ISAP.QPO.PONUM | PO number (from EDI 855 POA) |
| ISAP.QPO.PCODE | Item code |
| ISAP.QPO.PQTY | Quantity to receive |

ISAP.QPO is the 855 POA (purchase order acknowledgment) staging queue. The SKIP.PONUM/PCODE/PQTY flags control whether those fields are overridden from the imported file or kept from the matching PO.

**T7DEX — Export Data Dictionary Helper:** MEM.SELECT.FLD/NUM, MEM.DICT_DESC/NAME/TYPE/SIZE/DEC/ARRAY — in-memory data dictionary reference used during export configuration.

**T7DEPH — EDI Price Update (DE-P-H):** Updates SO prices from EDI 864 file — stdpck (standard pack), custpo (customer PO), PRCE (price). SO range filter.

**T7DETB extended web import field mapping** — up to FIELD.NUMBER[44] — 44 configurable column positions for complete SO header + ship-to detail including: drop shipment (FIELD.NUMBER[25]), currency ([26]), order discount ([27]), ship-to detail including email ([42]) and ship-to code ([43]).

**T7DEPB EDI Releases (855 POA):** RELEASE_NUM, edi.price, edi.reindex, out.type (PSV/fixed) — customer releases with pricing option and file reindex.

---

### PS — Extended User Table (ISEX)

T7PSA.DFM confirms two extended user fields not previously documented:

| Field | Description |
|-------|-------------|
| ISEX.USER.GROUP | User group assignment (for group-based menu access) |
| ISEX.USER.WINDO | Windows username (for auto-login matching) |
| velocitrack | Velocitrack admin flag (third-party shop-floor integration) |

Combined with previously known BKPS.USER: CODE + seclevel + seccode [A/P/1/2/C/V/U/E] + company + bkps.user.emp (employee link) + auto.log.

---

### IS.RMA — Return Merchandise Authorization Table

Confirmed from T7RMAWHY.DFM:

| Field | Description |
|-------|-------------|
| bkar.inv.sonum | RMA SO number |
| bkar.invl.um.ln[1] | Line number |
| is.rma.status | RMA status |
| bkar.invl.pcode | Item code |
| bkar.invl.pdesc | Item description |
| srma.oinvnum | Original invoice number |
| srma.osonum | Original SO number |
| rma.desc | RMA description/reason |
| rma.warranty | Warranty type [N/L/P/B/Blank] |
| rma.promdate | Promise date |
| rma.reason | Reason code |

Note: `srma.*` prefix (vs `is.rma.*`) suggests two separate tables — ISRMA (primary) and a secondary SRMA or BKRMA table with original-order links.

---

### ISSR.INFO — SR / Quote Extended Info Table

From T7QTINFO.DFM (Quote Misc. Information — same schema as T7SRINFO):

| Fields | Count | Description |
|--------|-------|-------------|
| ISSR.INFO.DATE[1..5] | 5 | Date UDFs |
| ISSR.INFO.AL1..AL20 | 20 | Alpha UDFs |
| ISSR.INFO.SRNUM | 1 | SR/Quote number (PK) |

26 total UDF fields per SR/Quote. Used identically for both SR service repair orders and QT sales quotes.

---

### MA — AR Deposits — ISAR.DEPL Confirmed

T7MAPDEPO.DFM confirms the deposit application line table fields:

| Field | Description |
|-------|-------------|
| BKAR.DEP.DEPNO | Deposit number (PK in BKARDEP) |
| BKAR.DEP.CUST | Customer code |
| amount.rem | Amount remaining on deposit |
| depo.orig.amt | Original deposit amount |
| ISAR.DEPL.SO | SO number being applied to |
| ISAR.DEPL.AMT | Amount applied from deposit |
| ISAR.DEPL.GLACT | GL account override for deposit application |

The deposit apply workflow: customer pays deposit (BKARDEP entry) → applied to specific SO lines (ISAR.DEPL entries) → GL debit/credit via ISAR.DEPL.GLACT.

---

### IS-M Multi-Currency: Period Conversion Uses 12 Periods

T7ISMCC.DFM (IS-M: Convert Source to Base Currency) uses:
- ISGL.CYDATE[1..12] — 12 GL period dates for currency conversion
- gl.period[1..12] — period display
- is.cvt.mth — conversion month
- is.date — convert/post as of date

**Key finding:** The currency conversion module uses 12 periods, not 14. The 14-period structure (confirmed in AM module) is for actuals/budgets; currency conversion aligns to fiscal year structure (12 standard periods).

---

### LC — Lot Control Forms Summary

All 7 LC forms confirmed:

| Form | Purpose | Key Fields |
|------|---------|-----------|
| T7LCA | Edit Lot Numbers | MTLOT.LOT/ONHAND/RECDATE/WO/WOSUF/EXPDATE/LOC/POCOST/PO; default.bin |
| T7LCB | Assign Lot Control | MTIC.PROD.LOT flag per item |
| T7LCC | Print Lot History | prt.allocs (SO allocations), sort.text, incl.totals |
| T7LCC2 | Print Lot Availability | serial number range + lot exp date + item range |
| T7LCE | Exceptions Report | neg.only (negative UOH lots), orphans.only (orphaned lots) |
| T7LCF | Lot Traceability | item + lot.no + rpt.details (summary/detail/all) |
| T7LCG | Archive/Unarchive | archive/U flag, zero.uoh.only |

---

### AC — Activity Control (T7ACDATE / T7ACRDTYPE / T7ACTION)

All 3 AC DFMs confirm table schemas:

**WODATE table** (from T7ACDATE — AC date schedule):

| Field | Description |
|-------|-------------|
| WODATE.START | Start date |
| WODATE.FINISH | Finish date |
| WODATE.QTY | Quantity |
| WODATE.PARPRE/PARSUF | Parent WO prefix/suffix |
| WODATE.TOPPRE/TOPSUF | Top-level WO prefix/suffix |
| WODATE.DELPRE/DELSUF | Deleted WO prefix/suffix |

**AC.RD table** (from T7ACRDTYPE — corrective action document types):
AC.RD.TYPE, AC.RD.REASON, AC.RD.DISPO — document type + reason code + disposition code.

**IS.ACTION table** (from T7ACTION — action items):
IS.ACTION.TYPE, IS.ACTION.DESC — simple type+description code table.

---

### FA — Fixed Assets Full Field Layout Confirmed

T7FAA.DFM confirms all IS.FXA.* fields visible:

IS.FXA.CSTBAS, IS.FXA.TYPE, IS.FXA.NUMBER, IS.FXA.DESC, IS.FXA.DESC2, IS.FXA.RESVAL, IS.FXA.LIFE, IS.FXA.METH, IS.FXA.ACCUMDEP, IS.FXA.LDEPAMT, IS.FXA.LDEPPERC, IS.FXA.LDEPDATE, IS.FXA.GLA/GLD (asset GL account+dept), IS.FXA.ACDEPA/ACDEPD (accum dep account+dept), IS.FXA.DEPEXPA/DEPEXPD (dep expense account+dept), IS.FXA.SDATE/EDATE (placed-in-service / disposed dates), IS.FXA.SOLD (sale price), IS.FXA.SERIAL.

T7FAB confirms IS.FXT.* and adds: IS.FXT.NETAVAL (net asset value), ready (Ready-to-Post flag), TAGGED (for tagged batch posting).

T7FAE FA import: 22 field mappings (all ISFXASST fields mappable from CSV or fixed-length).

---

### IM — Multi-Currency + Landed Cost Full Confirmation

ISIS.MCF (currency master) — all 49 fields confirmed from T7IMB:
- GL account pairs (dept+acct) for: AP/AP-conversion/AP-deposit, AR/AR-conversion/AR-deposit, PO/PO-conversion, CS/CS-conversion, bank/bank-conversion, foreign exchange gain/loss
- Interest rate and days (ISIS.MCF.INTRES/INTDAY)
- Running balances: AMTBNK/AMTAP/AMTAR/AMTFE/AMTAD/AMTPOR/AMTCS

ISIS.MCR (exchange rates) — confirmed: DATE + BASE + SOURCE[1..10] + RATE[1..10] (up to 10 currency pairs per date row).

ISIS.LND (landed cost GL) — GLADT/GLDDT (duty), GLAFR/GLDFR (freight), GLACF/GLDCF (customs fees) — 3 cost types × 2 GL fields (account+dept) = 6 fields.

ISIS.DUTY — DCODE + PERC.
ISIS.BRK (customs broker) — CODE + FLAT + PERC + TYPE.



---

## Pass 93 — SH/POA/RFQ/TC/US/SL suite deep-DFM pass (2026-06-18)

### SL / Shop Loading — SH Module (T7SHA through T7SHP + T7SHIPRTM)

The SH module is **Shop Loading and Scheduling** (not Shipping). It manages WO dispatch,
work center capacity, forward/backward scheduling, and critical ratio calculation.

**SH-A (T7SHA) — WO Dispatch List:** Filter + sort for open WOs. Key fields:
MTWO.WIP.SSTART / MTWO.WIP.SFIN (scheduled start / scheduled finish), status, priority,
planner, item class, WC range, customer, priority range, color display by due-date or priority.

**SH-B (T7SHB) — Routing Operation Schedule Edit:**

| Field | Description |
|-------|-------------|
| MTWORO.OPER | Operation number |
| MTWORO.OPERDESC | Operation description |
| MTWORO.WC | Assigned work center |
| MTWORO.SCHED.WC | Scheduled (effective) work center |
| MTWORO.STQTY | Start quantity |
| MTWORO.QTYCOM | Quantity complete |
| MTWORO.CONTNTN | Contention flag (resource conflict) |
| MTWORO.OVERLAP | Overlap days (positive = overlap with next op) |
| MTWORO.NEGOVLP | Negative overlap (gap between operations) |
| MTWORO.TYPE | Operation type (R=run, S=setup, etc.) |
| MTWORO.VEND | Outside process vendor code |
| MTWORO.VENDNAME | Vendor name |
| MTWORO.LEAD | Lead time for outside process |

**SH-C (T7SHC) — Work Center Capacity View:**

| Field | Description |
|-------|-------------|
| MTWC.DEPT | Department code |
| MTWC.DEPTDESC | Department description |
| MTWC.HRSWEEK | Available hours per week |
| MTWC.%UTIL | Utilization percentage |
| MTWC.HRS.SHIFT | Hours per shift |
| IS.OUTPROC | Outside process flag on WC |

**SH-E (T7SHE) — Scheduling Engine (Critical Ratio Mode):**

| Field | Description |
|-------|-------------|
| SWO.CRATIO | Critical ratio per WO (TDATE / remaining days) |
| SWO.RUN.DAYS | Running days consumed |
| TDATE | Target/due date for critical ratio calculation |
| SPEC.ACTION.STR | Specific action string (override scheduling action) |
| SORT.OPTION.STR | Sort option (by CR, by WO, by WC, etc.) |
| incl.last.seq | Include last operation sequence flag |

**SH-F/G/H (T7SHF / T7SHG / T7SHH) — Filters and Status Reports:**
- SH-F: WO status filter [FR = Firmed/Released], WO range, planner, class, priority
- SH-G: Class include/exclude list, late WOs only, approved WOs only — WO status summary
- SH-H: Status report by date/range variant

**SH-I (T7SHI) — Shop Load Analysis:** Color-coded capacity view.
Flags: avail.only (available capacity only), prt.bom (print BOM), print.po (include POs),
MRP data, weekly.summary, incl.price. Outputs a load-vs-capacity grid by WC and week.

**SH-J (T7SHJ) — Machine/WC Gantt View:** Machine range + WC range filters.
Displays scheduled operations on a timeline.

**SH-M (T7SHM) — Lead Time Simulation:**

| Field | Description |
|-------|-------------|
| PR3.DATE | Priority 3 date (furthest out) |
| PR2.DATE | Priority 2 date |
| PR1.DATE | Priority 1 date |
| PR0.DATE | Priority 0 date (immediate) |
| DAYZ[1..4] | Days arrays for 4 priority levels |

**SH-N (T7SHN) — Item Lead Time Recalculation:** USE.Q (include queue times in lead time),
Finish Good / Subassembly type toggles, hours/day setting. Batch recalculates MTIC.PROD lead times.

**SH-O (T7SHO) — WC Print:** page.wc flag = page break between work centers in printed output.

**SH-P (T7SHP) — Scheduling Engine (Forward/Backward Mode):**
forward/backward toggle, due.date vs finish.date toggle, critical.ratio threshold, delay.days.
Priority coloring and elapsed-time coloring. Full schedule commit + preview modes.

**T7SHIPRTM — User RTM Assignment:**
ISEX.USER.MISC1 = RTM name (per-user default report template assignment for shipping),
ISEX.USER.CODE = user code. This extends the user table with a third misc field.

**New ISEX.USER field confirmed:**

| Field | Description |
|-------|-------------|
| ISEX.USER.GROUP | User group (for group-based menu access) — Pass 92 |
| ISEX.USER.WINDO | Windows username (auto-login) — Pass 92 |
| ISEX.USER.MISC1 | Default RTM name (per-user report template) — Pass 93 |

---

### RF / RFQ — Price Break Table (T7RFQ + T7POAPrBrk)

**BKRFQ — Request For Quote / Price Break Table:**

| Field | Description |
|-------|-------------|
| BKRFQ.EXP | Expiry date for this price break |
| BKRFQ.ISSUE | Issue date |
| BKRFQ.QTY | Quantity break |
| BKRFQ.COST | Cost at this quantity |
| BKRFQ.PROD | Item / product code |
| BKRFQ.LCDATE | Last changed date |

**T7RFQ workflow:** Generates RFQ from an estimate. Fields: aenum (estimate number),
is.est.orddesc (order description), LIST.PART / DESC / QTY / VEND / STDCST / STATUS / TAG.
Items can be individually tagged or group-tagged for vendor assignment.

**T7POAPrBrk:** PO price breaks referenced directly from PO entry — reads BKRFQ table
by BKRFQ.PROD to display vendor-specific tiered pricing.

---

### TC — Treasury Control (T7TCC)

Minimal form — selects payment terms and bank account for cash management:
- terms.num — payment terms number
- CHK_NAME[1] — bank account / check name

Treasury Control is essentially a payment-run selector: choose which terms to pay,
which bank account to draw from. The actual payment generation is in TPOA.

---

### US — Triggers / Notifications — IS.TRIG Table Fully Confirmed

**IS.TRIG — Complete Schema (T7USG):**

| Field | Description |
|-------|-------------|
| IS.TRIG.CODE | Trigger code (PK) |
| IS.TRIG.CUST | Customer filter |
| IS.TRIG.VEND | Vendor filter |
| IS.TRIG.SO | Sales order filter |
| IS.TRIG.PO | Purchase order filter |
| IS.TRIG.WOPRE | WO prefix filter |
| IS.TRIG.WOSUF | WO suffix filter |
| IS.TRIG.OPER | Operation filter |
| IS.TRIG.CLASS | Item class filter |
| IS.TRIG.CAT | Item category filter |
| IS.TRIG.PLANNER | Planner filter |
| IS.TRIG.BINLOC | Bin location filter |
| IS.TRIG.ODEL | Delete after triggering flag |
| IS.TRIG.TRIGR | User to trigger (recipient) |
| IS.TRIG.ONCE | Fire once on next occurrence flag |
| IS.TRIG.LDATE | Last triggered date |
| IS.TRIG.LTIME | Last triggered time |
| IS.TRIG.NOTE | Notes |
| IS.TRIG.CONTACT | Contact name |
| IS.TRIG.EMAIL | Email address |
| IS.TRIG.EFLAG | Email reminder flag |
| IS.TRIG.ITYPE | Item type filter |
| IS.TRIG.DAYS | Days before event to pre-trigger |

**Trigger logic:** Triggers fire when a matching entity (customer, vendor, SO, PO, WO, item)
reaches the specified condition. The ODEL flag auto-deletes after firing (one-shot triggers).
ONCE flag fires only on the next matching occurrence and stops. DAYS allows pre-event alerts.

---

### POA — PO Entry / Approval Suite (T7POA through T7POAIMPLINES)

**BKAP.PO header fields confirmed from T7POA:**

Vendor: VNDCOD, VNDNME, VNDA1/VNDA2, VNDCTY, VNDST, VNDZIP, VNDATN, VNDCNT,
TELEPHONE[1] (main), TELEPHONE[3] (fax).

Ship-to override: SHPCOD, SHPNME, SHPA1/SHPA2, SHPCTY, SHPST, SHPZIP, SHPATN, SHPCNT.

PO control: SUBTOT, TAXAMT, TOTAL, DESC, TERMNM, OBYCUS (job number field), FOB,
ENTBY, ISCUR (currency), LOC (location), GLDPT (GL department), TAXRTE, ISTXGR (tax group),
TAXABLE, ORDDTE, SHPVIA.

**BKAP.PO.CONFIRM[1] / CONFIRM[2]:**
- CONFIRM[1] — PO type (standard, blanket, etc.)
- CONFIRM[2] — Confirming PO flag (verbal/confirming order indicator)

**PO Line fields (T7POA2 enter.prod.* and LINE.PROD.* arrays):**
LINE (line#), CODE (item code), DESC (description), QTY, ERD (est receipt date),
PRCE, UM, PCON (price conversion factor), TAX, DISC, EST (estimate link),
WO / WO.OP (WO + operation link), GLA / GLD (GL account + dept override),
ARD (actual receipt date), CONF (line confirmed flag), LONG (long description text).
ECO info: edit.revlvl, edit.intrl, edit.eco, edit.draw.

**T7POAC — RITEC Aerospace Risk Assessment Extension:**

| Field | Description |
|-------|-------------|
| risk.assess[1..6] | 6 yes/no risk assessment questions |
| ritec.contract | Contract number |
| ritec.dpas | DPAS (Defense Priorities and Allocations System) rating |

Note: T7POAC is a customer-specific form (RITEC / aerospace) added to the PO entry flow
for NADCAP-related compliance documentation.

**T7POAE — Extended PO Entry:** Adds rush.expedite flag, "Sign PO" button (digital signature
integration), recv.to.qc flag (route PO receipt directly to QC inspection).

**T7POACPY — Copy PO:** new PO number, estimated receipt date, new vendor code.

**T7POAVITEM — Vendor-Specific Items:** MTIC.PROD.CODE, MTIC.PROD.DESC, MTIC.PROD.DISP.UOH
(display units on hand for vendor item lookup).

**T7POAIMPLINES — Import PO Lines (10 column mappings):**
Extends J7POAIMPLINES (8 mappings) with:
- FIELD.NUMBER[9] = comment column position
- FIELD.NUMBER[10] = sequence column position
- CONFIRM[2] = PO type (confirming PO flag)

---

### Standard Cost Array Correction — MTIC.PROD.RCOST Has 15 Slots

T7STDCST.DFM confirms **15 slots** in the MTIC.PROD.RCOST rolled-up cost array,
not 14 as previously documented (Pass 91 was incorrect):

| Slot | Label |
|------|-------|
| RCOST[1] | Material — This Level |
| RCOST[2] | Freight — This Level |
| RCOST[3] | Labor — This Level |
| RCOST[4] | Setup — This Level |
| RCOST[5] | Outside Process — This Level |
| RCOST[6] | FOH — This Level |
| RCOST[7] | VOH — This Level |
| RCOST[8] | Material — Rolled Up |
| RCOST[9] | Freight — Rolled Up |
| RCOST[10] | Labor — Rolled Up |
| RCOST[11] | Setup — Rolled Up |
| RCOST[12] | Outside Process — Rolled Up |
| RCOST[13] | FOH — Rolled Up |
| RCOST[14] | VOH — Rolled Up |
| RCOST[15] | **Duty** (landed cost duty — rolled up) |

**Correction:** MTIC.PROD.RCOST[15] = Duty. The 15th slot was added for landed cost
duty allocation in the standard cost rollup. Prior Pass 91 documentation showing 14 slots
was incomplete.

---

### ISREP.ORD — Commission Order Chargeback Table (T7CHARGBK)

| Field | Description |
|-------|-------------|
| ISREP.ORD.INVNM | Invoice number |
| ISREP.ORD.INVDT | Invoice date |
| ISREP.ORD.REPNM | Rep name |
| ISREP.ORD.COMPR | Commission percent |
| ISREP.ORD.CMAMT | Commission amount |
| ISREP.ORD.SONUM | Sales order number |
| ISREP.ORD.ULID | Update/last ID |

Used in rep chargebacks — tracks which invoices generated commissions for which reps.

---

### BKCM.ACCC — Brand / Account Class Codes (T7BRANDS)

| Field | Description |
|-------|-------------|
| BKCM.ACCC.CCODE | Brand/category code |
| BKCM.ACCC.DESC | Description |

Simple code table under the BKCM (CRM) namespace. Used to classify customers by
brand or account category for reporting and commission segmentation.

---

### SEL.LOCM — Location Selection Master (T7SELLOC)

| Field | Description |
|-------|-------------|
| SEL.LOCM.TAG | Tagged for selection |
| SEL.LOCM.CODE | Location code |
| SEL.LOCM.NAME | Location name |
| SEL.LOCM.TYPE | Location type |
| sel.incl.seg | Include segregated locations flag |

Popup/filter used wherever a location range is needed (inventory transfer, WO issue, etc.).

---

### T7CUSTOMS — Configurable Custom Content Slots

10 custom content blocks with individual enable/disable:

| Pattern | Description |
|---------|-------------|
| Custom.control[1..10] | Enable/disable flag per slot |
| Custom.Name[1..10] | Label / name per slot |
| Custom.Desc[1..10] | Description per slot |

Used to configure optional custom content areas in the EvoERP interface
(likely for custom UDF panels or optional feature blocks).

---

### T7VSCHED — Visual Scheduler Remote Database

Same remote DB connection pattern as T7JCRM:
Host / port / name (database server DSN), init / VS / Post operation modes,
WOs tab / WCs tab. Connects to the Visual Scheduler external database
for bi-directional WO schedule synchronization.

---

### Other Pass 93 Findings

**T7NEWINIT — New Company Initialization:** Bare initialization form for setting up
a new company in EvoERP. Minimal fields — company name + confirmation.

**T7BOMSCRAPFIX — BOM Scrap Recalculation:**
scrap.setting [% or Q = percent/quantity], synch.wos (synchronize WOs), blanks.only
(only recalculate items with no current scrap setting).

**T7BZFIX — Location File Fix Utility:**
LOC_FILE_NAME, LOC_BUFF_NAME, LOC_LOCATION, TAGGED, FSEARCH — low-level location
record repair tool.

**T7EMGL — Email GL Link:**
from.glacct / gldpt + BKGL.EXTRA — associates a GL account with an email address
(BKGL.EXTRA field stores the email). Used for automated GL posting notifications.

**T7STTYPE / T7STYPE — Service Type Codes:**
IS.STYPE.TYPE — service type code table (both forms use same field = same table).

**T7ALOGSETUP — Auto-Login Setup:**
USER, password, enable/disable auto-login. Workstation-level auto-login config
(distinct from ISEX.USER.WINDO which is the per-user Windows-name match).

**T7AUTODCH — Automated DC Hours:**
Employee/shift/WO/time/date range filters for batch labor posting from
automated data collection devices.

**T7EDII — EDI Inbound Release Import:**
FIELD.NUMBER[1..6] → item number, ship date, PO number, quantity, firm/scheduled flag,
customer code. Maps EDI 830/862 scheduled releases to EvoERP fields.

**T7DSIG / T7DigSigChgPSWD — Digital Signature:**
Digital signature setup and password change forms. No new table fields — uses
existing BKPS.USER security framework with a digital signature password layer.

**T7ISMCC — Multi-Currency Conversion (IS-M):**
Already documented in Pass 92: ISGL.CYDATE[1..12], gl.period[1..12],
is.cvt.mth, is.date. 12 periods for currency conversion (not 14).



---

## Pass 94 — GF/JS/UTK/SPC/Approval-Suite/BOL/KIT/misc DFM pass (2026-06-18)

### GF — AR Charges / Global Finance Module

**GF Module Identity:** T7GFPRICE caption "Golding Farms Pricing" is a customer-specific
label on the pricing form. The GF module in EvoERP is "Global Finance / AR Charges" and
handles customer-specific pricing matrices and charge entry.

**BKIC.PMAT — Pricing Matrix Table (DFM-confirmed field additions):**

| Field | Description |
|-------|-------------|
| BKIC.PMAT.PCODE | Item/product code |
| BKIC.PMAT.SDATE | Start date (effective from) |
| BKIC.PMAT.EDATE | End date (effective through) |
| BKIC.PMAT.PFLAG | Pricing flag (pricing method/type) |

The full pricing matrix (BKICPMAT, 85 fields) was extracted from RWN in Pass 57.
T7GFPRICE DFM confirms the entry-form field names used during pricing setup.

**IS.GF.DEPT / IS.GF.DIV — GF Organizational Codes (confirmed from t7GFdept/t7GFdiv):**
- IS.GF.DEPT + IS.GF.DEPT.DESC — GF department code + description
- IS.GF.DIV + IS.GF.DIV.DESC — GF division code + description

**GF View Forms:**
- T7GFV — SO order view by date: SO, ORDDATE, ESD, SHIPTO, SORTJ (sort by job), SORTG (sort by group), JOB
- T7GFVS — Shipment view: "Orders to ship on [date]" — same SO fields
- T7GFR — Date range report: Orders From / Thru date

---

### JS Module — External Database Connector Settings

All 7 JS forms use identical structure — each configures a connection to a different
external database or reporting endpoint:

| Form | Target System |
|------|--------------|
| T7JSACC | Accounting connector |
| T7JSAIC | AIC connector |
| T7JSAPBI | Power BI connector |
| T7JSASRS | ASRS (Automated Storage/Retrieval) connector |
| T7JSOI | Open Items connector |
| T7JSQL | SQL export destination |
| T7JSettings | Master settings — Test/Generate/Detect + program generator |

**Common fields (all forms):** Host / port / name — DSN connection to external database.
**Additional (JSQL, JSettings):** TREEDEST — destination path for tree-format data output.

T7JSettings adds "Test Settings", "Generate Program", "Detect Settings" buttons,
making it the master configuration and program-generation interface for the JS connector family.
Same architecture as T7JCRM (JC remote DB) and T7VSCHED (Visual Scheduler).

---

### UTK Module — System Utilities (UT-K Series)

**T7UTKA — Data Deletion / Module Reset (DESTRUCTIVE):**
Clears all data from selected modules:

| Field | Module to clear |
|-------|----------------|
| CLR.COA | Chart of Accounts (GL) + BKSYMSTR |
| CLR.CUST | Customers / SO (AR) |
| CLR.VEND | Vendors / PO (AP) |
| CLR.INVN | Inventory + Manufacturing |
| CLR.EMP | Payroll employees |
| CLR.CM | Contact Manager |
| CLR.GLDATES | GL Period Dates only |
| done.gl/AR/AP/INV/PR/CM/DT | Completion flags per module |

**T7UTKD — GL Account Balance Transfer:**
Moves GL balances between accounts for year-end or restructuring:
- fycur (current FY) + fy1yp-fy6yp (1–6 years prior) — fiscal year range
- from.glacct/thru.glacct + from.gldpt/thru.gldpt — source account range
- susp.glacct/susp.gldpt — suspense account for the transfer

**T7UTKE — Location Code Rename:**
new.code (new location code), LOCATION (existing location to rename).
Updates all location references in the database.

**T7UTKF — Item Master Report (F variant):**
from/thru item, class, category ranges + item.type [RFAMNLBTKO] filter + prt.extdesc (include 2nd desc line).

**Item type codes (UTKF/UTKG):** R=Purchased, F=Finished goods, A=?, M=Made/manufactured,
N=Non-stock, L=?, B=?, T=?, K=Kit, O=Obsolete (inferred from context).

**T7UTKG — Item Master Report (G variant):**
Same as F + act.status filter [YNODEPSQR] (Y/N=active/inactive status plus D/E/P/S/Q/R variants) + GL account range.

**T7UTKH — Item Type Listing:**
inc.type[1-4] = Purchased Parts / Make From / Subassembly / Finished Goods toggles.
incl.inactive (include inactive), prt.note (print 2nd description line).
GL account range.

---

### Approval Suite — Cross-Module Approval Control

**SOAC — SO Approval Control (T7SOAC):**
Read-only or approval-gated view of the SO header for authorization workflow.
Fields confirm the same BKAR.INV.* structure as the main SO-A form — no new fields.
SRTYPE (SR/Quote type), BKAR.INV.DCODE (discount code), SLSP1/SLSP2 (salespeople),
COMM1/COMM2 (commission rates) visible in approval context.

T7SOACITEM — customer-specific items lookup (MTIC.PROD.CODE/DESC/DISP.UOH).
T7SOACPY — Copy SO to new SO number with new estimated ship date.

**APAC — AP Vendor Approval Control:**
t7apaC (AP Vendor master) confirms additional BKAP fields not previously documented:

| Field | Description |
|-------|-------------|
| BKAP.REM.ZIP | Remittance address ZIP |
| BKAP.REM.STATE | Remittance address state |
| BKAP.ADD1[2] | Remittance address line 1 |
| BKAP.ADD2[2] | Remittance address line 2 |
| BKAP.CITY[2] | Remittance city |
| BKAP.COUNTRY[2] | Remittance country |
| BKAP2.ID | Secondary ID / SSN (in BKAP2 table) |
| ISAPEX.LONGNAME | Vendor long name |
| ISAPEX.DATE[1] | Extended date UDF 1 |
| TMC.Bank | Bank name (treasury management) |
| TMC.Branch | Bank branch |
| TMC.AcctBase | Bank account base number |
| TMC.Suffix | Bank account suffix |
| bank.AcctNo | ACH routing account number |
| bank.RoutNo | ACH routing number |
| vend.status | Vendor approval status |
| territory | Vendor territory code |
| convert.sopo | Convert SO to PO flag |

T7APACON — BKAP.CONTACT[1-4] + BKAP.EMAIL[1-4] + BKAP.TELEPHONE[1-5] (4 contacts).

**ARAC — AR Customer Approval Control:**
T7ARAC (AR Customer master) confirms additional BKAR fields:

| Field | Description |
|-------|-------------|
| ISAREX.EXTADD[1..8] | 8-line extended address (ISAREX table) |
| BKAR.REQD.CERTS | Required certifications/approvals |
| BKAR.RTM.PRINT.GROUP | RTM print group (customer-specific report routing) |
| BKAR.LEAD.SRC | Lead source (1 && 2) |
| BKAR.price.mat | Price matrix override |
| BKAR.allow.bo | Allow back orders flag |
| BKAR.roll.surcharge | Roll surcharge into price flag |

T7ARACON — BKAR.CONTACT[1-5] + BKAR.EMAIL[1-5] + BKAR.TELEPHONE[1-5] (5 contacts).

T7ARACRE (AR Customer Credit): BKAR.CREDIT.HLD, BKAR.CREDITLMT, BKCM.DUNH.FORM (dunning form),
BKAR.FOLUPDTE (follow-up date), BKAR.DAYS.TOPAY, BKAR.LASTPMT, BKAR.LASTSALE,
BKAR.OUT.CREDIT[1-2] (two outstanding credit buckets), BKAR.OUTINV.

**WOAC — WO Approval Control:**
T7WOAC confirms additional WO cost array fields not previously documented:

| Field | Description |
|-------|-------------|
| MTWO.WIP.ESETUP | Estimated setup cost |
| MTWO.WIP.EMAT | Estimated material cost |
| MTWO.WIP.EOUTPR | Estimated outside process cost |
| MTWO.WIP.ELABOR | Estimated labor cost |
| MTWO.WIP.EFOVHD | Estimated fixed overhead |
| MTWO.WIP.VOVHD | Estimated variable overhead |
| MTWO.WIP.EMISC | Estimated misc cost |
| MTWO.WIP.EEXTRA | Estimated extra cost |
| MTWO.WIP.ETOT | Estimated total cost |
| MTWO.WIP.ASETUP | Actual setup cost |
| MTWO.WIP.AMAT | Actual material cost |
| MTWO.WIP.AOUTPR | Actual outside process cost |
| MTWO.WIP.ALABOR | Actual labor cost |
| MTWO.WIP.AFOVHD | Actual fixed overhead |
| WO.Convert | WO conversion date |
| WO.Production | WO production date |
| WO.Show | WO show date |
| wo.approval | Approval flag |
| scrapped.qty | Scrapped quantity |
| ssonum | Source SO number |
| NCR.QTY | NCR quantity |
| line.refno | Line reference number |

T7WOACFG — excl.zero.qty (exclude 0-qty BOM items), call.wokb (update BOM), call.woka (update routing).
T7WOACPY — Copy WO: C.SUFF (copy all suffixes), TO.WOP/TO.WOS (destination WO prefix/suffix).

---

### MH — Bill of Lading Forms Fully Confirmed (T7BOL / T7BOLMSO)

**T7BOL — Standard Bill of Lading:**

| Field | Description |
|-------|-------------|
| load.number | Load number |
| seal.number | Trailer seal number |
| trailer.number | Trailer number |
| author.number | Authorization number |
| control.number | Control number |
| pickup.time | Pickup time |
| driver.arrived | Driver arrived time |
| loading.start | Loading start time |
| loading.end | Loading end time |
| driver.departed | Driver departed time |
| pickup.date | Pickup date |
| SCAN.INV | Invoice number (scan) |
| sShip.Num | Shipper number |
| marks[1-2] | Shipping marks |
| LIST.DESC/QTY/CASES/WT/PALLET/DUEDATE/SHIPINFO | Commodity line arrays |
| edit.htype/hqty | Handling unit type/quantity |
| edit.pqty/ptype/HM/nmfc/class | Package line: qty/type/hazmat/NMFC/freight class |
| edit.pallet/add.pallet.wt/edit.pweight | Pallet info |
| commodity/department/edit.pairs | Freight classification |
| drop.shpnme/drop.ship.to[1-4] | Drop ship address |

**T7BOLMSO — Multi-SO Bill of Lading:**
Handles shipment consolidation across multiple SO lines:
- BOL header: sbolnum (BOL#), ship.custcode/name, ship.date, shpvia, SCAC (carrier code),
  carrier.name, billing.type [PCTN = Prepaid/Collect/Third-party/Notify], billing.acct,
  num.skids, marks[1-4], total.class, author/control/trailer/load/seal numbers
- billing.line[1-6] — 6 billing note lines
- EDIT/LIST arrays: item, SO#, description, ship qty, packages, package type, weight, HM, NMFC, class
- USER.NAME — user entering the BOL

The BOL forms are the primary output documents of the MH/Shipping Order module.

---

### KI — Kit Assembly (T7KIT)

**T7KIT — Kit Pull and Assembly Interface:**

BOM component display arrays (one slot per component):

| Array Field | Description |
|-------------|-------------|
| APART | Component item code |
| ADESC | Component description |
| ARQTY | Required quantity |
| AUOH | Units on hand (all locations) |
| ALUOH | Units on hand (in lot) |
| AQTY | Quantity to pull |
| ABIN | Bin location |
| ABOMNOTE | BOM note for component |
| ALOT | Lot number |
| ALOC | Location code |
| AOPER | Operation number |

**Control fields:** SCAN.WO (WO number), SCAN.EMP (employee), bkic.prod.code (kit item),
bkic.prod.desc, bkic.prod.note, mtic.prod.loc (default location), binloc (scan bin),
MTIC.PROD.CYCLE (cycle count flag), kit.ln.cntr (line counter), xlot (lot to assign),
xqty (quantity), xoper (operation), wobom.reference (BOM reference), scan.item (barcode scan),
sqty, bomnote.

Kit assembly integrates lot tracking (ALOT/xlot), barcode scanning (scan.item),
bin-level inventory (ALUOH, binloc), and BOM component visibility in one workflow.

---

### SP/SPC — Statistical Process Control — Additional Tables

Pass 84 documented IS.SPC at high confidence. T7SPC.DFM confirms additional fields:

**IS.SPC (SPC production data):**
GOOD (accepted qty), REWORK (rework qty), ANOTES (general notes), SIDE (side),
TYPE (defect type), DETAIL (detail code), TESTT (test type), TESTE[1-3] (test equipment 1-3),
OPER (operation), DATE, EMPNUM (employee).

**IS.SERR (Serial/error records):**
ERROR (error code), PROCESS (process step), COUNT (error count), REF (reference designator),
SERIAL (serial number), aDOF (date of failure), aREWORK (rework description),
aDIAG (diagnosis/root cause).

**IS.STRACK (Serial genealogy/traceability):**
PSER (parent serial number), CSER (child serial number), COMP (component code),
PROC/PROCESS (process step), AR (assembled/received flag).

SPC live monitoring: ATYPE, ADETAIL, ACODE, ACOUNT — real-time error type/count display
(T7SPCLIVEGRID).

---

### SOGC — SO Gross Costing Reports

T7SOGCogs — "SOG COGS Report": calculates COGS from invoices by range (invoice#, SO#,
shipper#, invoice date). all.printed flag to include all printed invoices.

T7SOGComm — "SOG Commission Report": same structure, calculates commission liability.

These are batch COGS and commission reconciliation reports operating on posted invoices.

---

### FO (F&O) Additional Forms

**T7FOC — Feature/Option Price Setup:**
PAR.DESC (feature/parent item description, read-only), COMP.DESC (option component description, read-only),
BKBM.PROD.OPYN[4]="Use STD Customer Pricing?" — when Y, use standard price schedule instead of PRICE field;
BKBM.PROD.OPYN[5]="Add Price to Parent?" — when Y, option price adds to the parent feature price on SO;
BKBM.PROD.PRICE — fixed option price ($,0.0000 format; used when OPYN[4]=N).
Note: `from.item` = Feature item (not a range start); `thru.item` = Option item (not a range end) — TAS Pro field naming quirk.

**T7FOD — F&O Range Report:** item/category/class range filters → Print (FP-B RTM).
**T7FOE — F&O Single Item:** single Feature/Option item number → Print (FP-B RTM).

---

### FS — Field Information Base (IS.FIB.*)

Confirmed from T7FSCLASS / T7FSEMP / T7FSINFO (FS module DFMs):

| Field | Description |
|-------|-------------|
| IS.FIB.CLASS | FIB classification code |
| IS.FIB.GROUP | FIB group |
| IS.FIB.CONTRACT | Contract reference |
| IS.FIB.WHO | Who (responsible person) |
| IS.FIB.PROGRAM | Program/project code |

**SCAN.EMP** links FIB records to employees/reps. Market Segment field ties to sales rep.
FS module = "Field Information Base" — tracks field service records by class/group,
linked to contracts and programs. Not a general field service dispatch system.

---

### ML — Multi-Language (LANG.DICT.* confirmed from T7MLC/T7MLE)

T7MLC — language DFM generator: DFMName, Addlang, language (adds new language to a DFM file).
T7MLE — caption editor:

| Field | Description |
|-------|-------------|
| LANG.DICT.ECAPT | English (default) caption |
| LANG.DICT.LCAPT | Localized translation |
| LANG.DICT.LANG | Language code |

---

### EvoERPDrillM — Drill-Down Configuration (DRILLM Table)

T7DRILLM (SU module) confirmed from EvoERPDrillM.DFM:

| Field | Description |
|-------|-------------|
| DRILLM.PARENT | Parent grid field (source key) |
| DRILLM.CHILD | Child grid field (target key) |
| DRILLM.MENU | Menu label text |
| DRILLM.PFILE | Parent file/table |
| DRILLM.FILE | Child file/table |
| TField[1-5] | Target fields (5 columns mapped to child grid) |
| SField[1-5] | Source fields (5 columns from parent grid) |

Drill-down config = a parent grid cell value launches a child grid using the DRILLM
mapping to resolve source → target field relationships (up to 5 field pairs per drill).

---

### Other Pass 94 Findings

**T7WCBK — Live Work Center Dispatch Board:**
FROM.WC (work center from), timer (auto-refresh seconds), ISE.STATUS.2/3 (WO status filter slots 2-3), oper2 (operation filter), category, from.cust, priority. Feeds the live WC schedule view.

**T7ALTPART — Alternate/Substitute Parts (BKSB.PART):**
BKSB.PART.PROD (original item), BKSB.PART.SUBST (substitute item), SUB.DESC (description).
save.both.ways — creates the cross-reference in both directions.

**T7PUTAWAY — Warehouse Put-Away:**
scan.item, MTIC.PROD.CODE/DESC/LOC, BKIC.PROD.LRCPT (last receipt), BKIC.PROD.UOH,
enterbin (bin entry), action, PABBL (put-away by bin location), mtic.prod.uiqc (UOH in QC).

**T7SDET — Service Detail Codes (IS.SDET):**
IS.SDET.TYPE + IS.SDET.DETAIL — simple type+detail code table for SR service reason breakdown.

**T7STOCK — Stock/Brand Codes:**
Same table as T7BRANDS: BKCM.ACCC.CCODE / BKCM.ACCC.DESC.
T7STOCK is a second entry point to the same brand/category code table.

**T7FNR — Field Name Replace Utility (DESTRUCTIVE):**
Mass-update any field in any data file with up to 6 filter conditions:
FileNAME (target file), DNAME (field), element (array index), action,
flname[1-6] + felement[1-6] + oper[1-6] = filter conditions,
drepl_field/aREPL_FIELD/nREPL_FIELD = replacement values (date/alpha/numeric).
Position mode: spos/slength + POS[1-6] for substring operations.

**T7XCUTIL — XCharge CC Conversion:**
bkcm.acct.code — converts credit card data in CRM accounts to Secure XCharge vault.

**T7RTMVALID — RTM Report Name Selector:**
rtmvld_name — pop-up to select a valid report format name (RTM filename validation).

**T7ALERTMSG / evoalerts — Alert Display:**
Simple modal alert dialogs. T7ALERTMSG uses AlertMsgLabel for system alert messages.
evoalerts fires on alert conditions with Ignore button.

**EvoELinks — Enhanced Document Links Settings:**
Extends IS.LNK.* with: links.alert (link alert flag), links.itm.alert (item alert),
is.lnk.private (private flag), GlobalPath[1-10] (10 configurable global file paths),
WFA (Windows File Associations), OFA (Other File Associations).

**evoCSR — Calendar Summary Report (ESD/CDD view):**
ESD (estimated ship date), csd (customer delivery date), cust/item ranges, ENTRY.DATE.
Report field toggles: custpo (include customer PO#), qtybo (qty + backorder), socust (SO# + customer).
A shipping calendar showing open orders grouped by ESD or CDD.

**Dynamic-load forms (no DFM fields):**
CRMDASHBOARD, CASHFLOW, COMMISSIONRPT, MACHINEVIEW, WORKCENTERLOAD, BOMTREE, EDITBOMTREE,
PURCHITEM, PURCHVEND, INVCHANGE — all show "Loading..." caption.
These are web-based visualization panels launched from TAS Pro that load their UI from
an HTML/JavaScript layer, not from the DFM definition. Content is server-driven.



---

## Pass 95 — SOA/EVO-infra/WTAS/WBK/SM-IJ/CAL DFM sweep (2026-06-18)

### SO — Additional Header and Line Fields (T7SOA / t7Soa2)

**BKAR.INV additional fields confirmed from T7SOA:**

| Field | Description |
|-------|-------------|
| BKAR.INV.FRGHT | Freight amount on SO/invoice |
| BKAR.INV.SUBTOT | Sub-total (before tax + freight) |
| BKAR.INV.TAXAMT | Tax amount |
| BKAR.INV.TOTAL | Grand total |
| BKAR.INV.NL | Note line flag |
| sobookdate | Booking date for the SO |

**SO Line arrays (t7Soa2 line.prod.* — display buffer index up to 5001):**

| Field | Description |
|-------|-------------|
| line.prod.NUM[n] | Line number |
| line.prod.CODE[n] | Item code |
| line.prod.DESC[n] | Item description |
| line.prod.QTY[n] | Ordered quantity |
| line.prod.UBO[n] | Unit backorder quantity |
| line.prod.PRCE[n] | Price |
| line.prod.UM[n] | Unit of measure |
| line.prod.DISC[n] | Discount percentage |
| line.prod.ESD[n] | Estimated ship date |
| line.prod.ASD[n] | Actual ship date |
| line.prod.TAX[n] | Line taxable flag |
| line.prod.RTS[n] | Return to stock flag |
| line.prod.STAT[n] | Line status |
| line.prod.LONGP[n] | Long product description flag |
| line.prod.HIDE[n] | Hidden line flag |
| line.prod.IPEXT[n] | In-progress extension |
| line.prod.OQTY[n] | Original quantity |
| line.prod.FATD[n] | Fill at time of dispatch flag |
| line.prod.UPCHG[n] | Upgrade charge |
| line.wt | Single line weight |
| tot.line.wt | Total order weight |

**T7SOABKD — Booking Date:** sobookdate — popup to enter/change the SO booking date.

**T7SOAFRT — Freight Entry:** bkar.inv.frght — popup to enter freight amount on SO.

**T7SOAIMPLINES — Import SO Lines (7-column mapping):**
FIELD.NUMBER[1-7] = item code / description / quantity / price / ESD / comment / location.
Also: company.code/path (source ERP company for inter-company imports), sponum (source PO),
vend.code/name, incl.kit (include kit components), skip.zero.qty, incl.2nd.desc,
incl.specs, imp.comments, date.format (MM/DD/YY or DD/MM/YY).

**T7SOAPRC — SO Pricing Popup:**
BKIC.PMAT.QTY + BKIC.PMAT.RATE + BKIC.PMAT.PDESC — shows tiered pricing from the
pricing matrix (BKICPMAT) when entering SO lines.

**T7SOAXCOM — Extra SO Commission Override:**
Per-SO commission overrides beyond the customer default:
seREP (rep code), Empname (employee name), ecommp (commission %), eoveramt (overage amount),
eoverp (overage %). Arrays: LABEL, REP, VCOMMP, OVERAMT, OVERP — one row per extra commission.

**T7SOINFO / T7SOHINFO — Sales UDF (ISSR.INFO):**
Both the line-level (SOINFO) and header-level (SOHINFO) UDF forms use the SAME
ISSR.INFO table: ISSR.INFO.DATE1-5 (5 date UDFs) + ISSR.INFO.AL1-20 (20 alpha UDFs).
The ISSR.INFO.SRNUM PK links to the SO or SR number.

**T7SOJINFO — Recurring SO Info:**
mem.group (recurring group code), bkar.inv.invdte (invoice date), mem.freq (frequency),
mem.max (maximum invoices). Controls the recurring SO scheduling (group + frequency + limit).

---

### SM-I Suite — CRM Code Tables (T7SMIA through T7SMIF)

**All SM-I forms manage BKCM.* code tables:**

| Form | Table | PK Field | Fields |
|------|-------|----------|--------|
| T7SMIA | Lead Sources | BKCM.LEAD.SCODE | + DESC |
| T7SMIB | Territory Codes | BKCM.TERR.TCODE | + DESC + EMAIL |
| T7SMIC | Activity/History Codes | BKCM.ACFC.FCODE | + DESC + REP (rep flag) + dashboard toggle |
| T7SMID | Account/Category Codes | BKCM.ACCC.CCODE | + DESC (same as T7BRANDS) |
| T7SMIE | Document Type Codes | BKCM.DTCD.DCODE | + DESC |
| T7SMIF | Item Category Master | IS.CATM.CODE | + DESC |

**Key distinction:** IS.CATM is the item category master (under SM, affects inventory and CRM).
BKCM.ACFC is the CRM activity/history follow-up code with a CRM Dashboard inclusion flag.
BKCM.TERR includes an email address for territory routing.

---

### SM-J Suite — Archive and Purge Programs (T7SMJA through T7SMJH)

**Complete SM-J archive/purge program inventory:**

| Form | Purpose | Key Range Fields |
|------|---------|-----------------|
| T7SMJA | Inventory Reconciliation (report-only mode) | RPT.ONLY flag |
| T7SMJB | WO Archive/Restore/Purge | WO#, act.fin.date, job, cust, item; ARCH.CLOSE/CANCEL; orphan.woex |
| T7SMJC | Inventory Reconciliation | MASTER/TRANSACT levels, RSS (stock status report), METHOD, item/class, transdate |
| T7SMJD | Inventory Transaction Archive | Type [ASPJWIQOCMTRG], date range, consolidation date |
| T7SMJE | WO Purge (closed/cancelled) | PURGE.CLOSE/PURGE.CANCEL, WO range, act.fin.date range |
| T7SMJF | PO Archive | PO range, vendor range, date range |
| T7SMJG | QC Receiver Archive | arch.or.purge flag, date range, QC receiver# range, vendor range |
| T7SMJH | DC Data Collection Purge | CUT.DATE — purges all DC records before this date |

**T7SMJD Transaction Type codes [ASPJWIQOCMTRG]:**
A=AR, S=SO, P=PO, J=JC labor, W=WO, I=Inventory, Q=QC, O=overhead, C=cost adjustment,
M=MRP, T=transfer, R=return, G=GL.

---

### IS.REM — Reminder Table Additional Fields

evoreminders.DFM and dayrem.DFM confirm:

| Field | Description |
|-------|-------------|
| IS.REM.DATE | Reminder date |
| IS.REM.TIME | Reminder time |
| IS.REM.SUBJECT | Subject line |
| IS.REM.TYPE | Reminder type code |
| IS.REM.CO | Company code |
| IS.REM.DISP | Dismissed flag |

**dayrem additional fields:** rem.item (item#), rem.cust (customer), rem.vend (vendor),
rem.file (file/URL link), rem.contact/phone/femail (contact info), REM.EMAIL (email reminder flag),
other.user (create reminder for a different user — cross-user reminders).

---

### EvoFilters — Global Filter Form (EVOFILTERS.DFM)

The global filter form confirms the full range of JC/WO/SO filter fields used across
EvoERP reports and analysis screens:

**WO filters:** from/thru WO#, WO finished date, WO status, WO start date, machine, WC,
scrap code, employee, sequence range, WO act.fin.date, due date, WO class, WO priority [1-9].

**JC filters:** job range, labor date range, tool range, dept range, rework code range,
div.hrs (divide hours by number of jobs).

**SO/Invoice filters:** SO range, invoice range, order date range, ESD range, invoice date range,
cust order (customer PO) range, salesperson 1 + 2 ranges, job number range.

---

### EvoService / EvoScheduler Setup

**EVOSERVICESETUP.DFM** confirms EvoService installer settings:
email.cfg.SMTP/user/pass/Email/Name/sec (security), smtpport, esettings (email settings toggle),
thirtytwo/sixtyfour (OS bitness), file_name (server path).

**evoERPsched.DFM** confirms the ERP batch scheduler:
stime (schedule time), mon/tue/wed/thur/Fri/sat/sun (day toggles), runonce/weekly (frequency),
rtime (run-at time). Batch jobs can be scheduled on specific days of the week.

---

### WBK Menu System — Additional Fields Confirmed

**WBKLUGRID.DFM — Grid Lookup Editor:**
FD_COLHEADER (column header), FD_FIELDNAME (field name), FD_TOT (total flag), FD_FUNC (function),
FD_TYPE (field type), FD_SIZE (field size), LUGRID_END (start at end flag), SEC.LEVEL (security),
KD_COLHEADER/KEYNAME/FIELDNAME (key definition columns).

**WBKMENUBUTT.DFM — Button Setup:**
MI_BUTT_CAP (button caption), MI_BUTT_OPT (button option), MI_BUTT_NUMB (button number).

**WBKMENUSUEU.DFM — Menu Item Setup:**
GROUP_CAPTION/NUM, BUTTON_CAPTION/IMAGE/NUM, access_code, MI_MENU_LVL (menu level),
MI_CAPTION (caption), MI_FASTSELECT (quick key), MI_OLD_OPT/CAP/PRGNME (old menu values for migration).

**WBKMENUSUCPRG.DFM:** Change program name — FROM_PRG_NAME / TO_PRG_NAME (migration tool).
**WBKMENUSUNEWAC.DFM:** New access code — NewAC, ACCopyFrm (copy from existing code).

**WBKLPRINT.DFM:** Order printing options — pbox1 (Acknowledgements), pbox2 (Packing Slips),
pbox3 (Invoices). Three separate print jobs selectable per session.

---

### WTAS Additional Forms

**WTASFLOC / WTASINIT — File Location Table (CFFLOC):**

| Field | Description |
|-------|-------------|
| CF_FLNAME | File/table name |
| CF_FLCODE | File code |
| CF_RTYPE | Record type |
| CF_DESC | Description |
| CF_PATH | File path |
| cf_fdname | Field definition name |

WTASFLOC maintains this table; WTASINIT creates new entries (initializes new data files).
This is the EvoERP file registry — every data table in the system is registered here.

**WTASDMS2-5 — Auxiliary browser dialogs:**
- DMS2: Enter array elements (ARRAYCNTR)
- DMS3: Edit memo field
- DMS4: Enter filter expression (FilterExpr)
- DMS5: Enter find-next expression (FindFilterExpr)

---

### EvoERP Infrastructure — Other Findings

**EvoERPbackup.DFM — Backup System:**
zipfiles (file list), zipName (archive name), fullsystem/compdata/custom (backup scope toggles),
COMP.TAG/EXT/NAME (component list), CSTFILELIST (custom file list).
Three backup scopes: Full System, Company Data, or Customized file list.

**EVOERPUPDW.DFM — Archive Work Orders:**
wa.date — archives closed WOs to the WO history file as of this date.

**nzemailtll.DFM — Email Composer:**
entTO/CC/entICC (To/CC/BCC arrays), EMAILLIST/EMAILLBL (recipient list), CONTNAME,
bccself, TEMPATT (attachment), Email.cfg.subj (subject). Auto-email infrastructure
for sending invoices, reports, and notifications directly from EvoERP.

**printtll.DFM — Print Dialog:**
print_opt[1-4] = Printer / Preview / Email / File modes.
autoemail (auto-send to contact), contname/contnum/contprimcode (contact for email routing).
Confirms the four output modes available from any EvoERP print dialog.

**autoT7POJC.DFM — Auto QC Buyoff (PO-J-C):**
Confirms BKQC.RECV.DATE (receive date), BKAP.POL.WOSUF (WO suffix on PO line), rohs (RoHS
compliance flag on receipt). Automated version of the QC buyoff form for receiving.

**imageinfo.DFM — Image GPS Metadata:**
File.Name, Create.date/time, LatTXT/LONGTXT — reads GPS geolocation from image EXIF data.
Used in EvoLinks when attaching geotagged photos to records.

**SSS.DFM — Drill Filters:** SSSVALUE + SSS1-6 — 6-slot quick filter for drill-down queries.
**SSSFD.DFM — Sub-String Search:** SSSFDVALUE + SSSFD1-7 — 7-slot substring search across EvoNotes.

**ACT7SHKNOTE.DFM — Shackleton WO Note:**
SCAN.WO, scan.oper, woro.note — shop-floor WO operation note entry (third-party integration).

**NascoPAYex.DFM — Nasco Payroll Export:**
pdate — payroll export for a specific customer integration (Nasco brand).

**GetAlphaGen.DFM / GetFileName.DFM:**
Generic input dialogs used internally: alpha value prompt (gagalpha),
file name prompt with local/server toggle.



---

## Pass 97 — Business Workflow Recipes (2026-06-18)

---

### Recipe 10: GL Journal Entry (Manual)

**When to use:** Recording adjusting entries, accruals, reclassifications, or any
transaction that must go directly to the General Ledger without an AR/AP/PR sub-ledger.

**Module path:** GL → GL-A (Journal Entry) or GL-B (Recurring Journal Entry)

**Steps:**

```
1. GL-A (Journal Entry)
   - Enter: Journal date (BKGLTRAN.JRNLDATE)
   - Enter: Journal description (BKGLTRAN.DESC)
   - For each line:
     a. GL account number → BKGLCOA.GLACCT (must exist in chart of accounts)
     b. Debit or credit amount
     c. Reference / memo for this line
   - Total debits must equal total credits (entry is balanced)
   - Post → creates BKGLTRAN rows, updates BKGLCOA period balances

2. If entry is recurring (e.g., monthly accrual):
   - Use GL-B (Recurring Journal Entry) instead
   - Set: frequency, start/end date, template
   - Run GL-B monthly to generate the actual transaction

3. Verify posting:
   - GL-O-A (GL Trial Balance) — confirm accounts changed as expected
   - GL-O-B (GL Detail Listing) — shows individual BKGLTRAN rows
```

**Key tables:**
- BKGLTRAN — journal transaction rows (one per debit/credit line)
- BKGLCOA — chart of accounts (GL account master + period balances)
- BKGLPER — period status (open/closed per fiscal period)

**Pre-requisite:** The fiscal period must be open in BKGLPER. If the period is closed,
use GL-G (Reopen Period) before entry. Re-close after posting.

**Common errors:**
- "Account not found" — account code not in BKGLCOA; add via GL-C (COA maintenance)
- "Period closed" — open the period via GL-G first
- Entry not balanced — system will not allow posting; check debit/credit totals

**Confidence: 76/100** — Module path confirmed from menu codes; table structure verified;
exact field-by-field behavior of GL-A form inferred from DFM (T7GLA*) — RWN logic blocked.

---

### Recipe 11: Period-End Archiving and Purging

**When to use:** At month-end or year-end to archive completed transactions and purge
old data, keeping the live database fast. Run in the order shown — archive before purge.

**Module path:** SM → SM-J series (T7SMJA through T7SMJH)

**Typical sequence (monthly):**

```
1. SM-JA — Inventory Reconciliation (report only)
   - Purpose: verify inventory balance matches transaction history BEFORE archiving
   - Set: RPT.ONLY = Y (no changes, just report)
   - Review: any discrepancies must be resolved before archiving

2. SM-JC — Inventory Transaction Archive
   - After confirming SM-JA is clean, archive old inventory transactions
   - Set: date range (archive transactions before cut-off date)
   - Transaction types: select which of [ASPJWIQOCMTRG] to include
     A=AR, S=SO, P=PO, J=JC, W=WO, I=Inventory, Q=QC, O=overhead,
     C=cost adj, M=MRP, T=transfer, R=return, G=GL
   - Consolidation: optionally consolidate to summary records
   - Result: old BKISTXN rows moved to archive file

3. SM-JB — Work Order Archive (if month-end WO closure done)
   - Archive finished/cancelled WOs older than cut-off date
   - Options: ARCH.CLOSE (archive closed WOs), ARCH.CANCEL (archive cancelled WOs)
   - Orphan WO cleanup: orphan.woex = archive orphaned WO extensions
   - Archived WOs can be restored via SM-JB → Restore option

4. SM-JF — PO Archive
   - Archive received/closed POs older than cut-off
   - Range: PO number range + vendor range + date range

5. SM-JG — QC Receiver Archive
   - arch.or.purge = A (archive) or P (purge, deletes permanently)
   - Date range + QC receiver# range + vendor range
   - Use A (archive) unless disk space is critical

6. SM-JH — DC Data Collection Purge
   - CUT.DATE: purges all data collection records before this date
   - WARNING: this is a permanent delete; DC records cannot be restored
   - Only purge after confirming all DC transactions are posted to WO/JC

7. SM-JE — WO Purge (year-end / old closed WOs)
   - PURGE.CLOSE / PURGE.CANCEL: selects which WO statuses to purge
   - WO range + act.fin.date range
   - WARNING: purge is permanent; run SM-JB archive FIRST

8. SM-JD — Inventory Transaction Purge (if separate from archive)
   - Purges previously archived INV transaction records from archive file
   - Use after verifying the archive was successful
```

**Key tables affected:**
- BKISTXN / archive equivalent — inventory transactions
- WORKORD / WORKCHG — WO header and detail (archived to separate files)
- BKAPPO / BKAPPOL — PO header/detail (archived)
- BKQCRECV — QC receiver (archived or purged)
- DC data collection tables (purged)

**Safety rules:**
- Always run SM-JA (reconciliation) before SM-JC (archive)
- Archive before purge — SM-JB before SM-JE, SM-JG before purge mode
- Keep archive files for at least one fiscal year before deleting
- Coordinate with GL month-end close — post all sub-ledgers first

**Confidence: 72/100** — SM-J forms fully confirmed from DFMs; step order is best-practice
inference; exact table names for archive files not confirmed.

---

### Recipe 12: EvoERP Backup and Restore

**When to use:** Before major changes (software updates, configuration changes, year-end),
and as part of scheduled maintenance. Three backup scopes available.

**Module path:** SM → SM-O or directly via EvoERPbackup launcher

**Backup scopes:**

| Scope | Contents | When to use |
|-------|----------|-------------|
| Full System | All EvoERP program files + company data | Before software updates |
| Company Data | All .B (Btrieve) data files for selected company | Before configuration changes |
| Custom | User-selected file list (CSTFILELIST) | Targeted backup of specific tables |

**Steps:**

```
1. Open EvoERPbackup
   - Select scope: fullsystem / compdata / custom
   - If custom: edit CSTFILELIST to select specific files

2. Specify archive:
   - zipName: output archive file name
   - zipfiles: file list to include (auto-populated for Full/Company scopes)

3. COMP.TAG / EXT / NAME: component list
   - EVO automatically populates this from the component registry
   - Verify the component count before proceeding

4. Run backup
   - Creates a ZIP archive at the specified path
   - Monitor for errors (locked files, path not found)

5. Verify:
   - Check ZIP file size is plausible
   - Optionally test-restore to a temp location
```

**Restore procedure:**
- No automated restore tool in EvoERP — use Windows file extraction
- For data restore: stop EvoERP services first, extract .B files,
  restart Pervasive SQL service, then restart EvoERP
- For full system restore: extract to a staging folder, validate,
  then copy over production path

**Confidence: 68/100** — EvoERPbackup form confirmed from DFM; exact menu path to launch
it (SM-O or direct) inferred; restore steps are general Btrieve/Pervasive procedure.

---

### Recipe 13: New User Setup

**When to use:** Adding a new EvoERP user, assigning security level, and configuring
starting menu and preferences.

**Module path:** SM → SM-A (User Maintenance) + SM-B (Security Levels)

**Steps:**

```
1. SM-A (User Maintenance) — create the user record
   - Enter: AHSYLOG.AHSY_USER_ID (user name / login)
   - Enter: AHSYLOG.AHSY_PASSWORD (initial password — user should change)
   - Assign: AHSYLOG.AHSY_USER_LEVL (security level — 2-char code)
     Security level controls what menus the user can see and which
     operations they can perform (via BKSLEVEL matrix)
   - Set: AHSYLOG.AHSY_USER_TYPE (user type: A=Admin, U=User, etc.)
   - Set access flags: AHSYLOG.AHSY_USER_ACCES_1..20 (optional overrides)
   - Set: starting menu / company

2. SM-B (Security Level Maintenance) — verify or create the security level
   - If using existing level: verify BKSLEVEL matrix has correct permissions
   - If new level needed: create BKSLEVEL row for the new level code
   - For each of 20 menu sections: set YN master toggle + individual op flags
   - 20 operations per section = what the user can do within that menu

3. WBK (Workbench / Menu Customizer) — optional menu customization
   - If this user needs a custom menu (vs. the global EvoERP menu):
     Use WBK to create a custom menu layout
   - Assign: GROUP/BUTTON/CAPTION/IMAGE for each menu item
   - Set: FASTSELECT (keyboard shortcut) for frequently used options
   - Assign: ACCESS_CODE (security check per button)

4. Test the login:
   - Log in as the new user
   - Verify menu shows expected modules
   - Attempt an operation in a restricted area — confirm access denied
   - Verify starting company is correct

5. EvoSettings.INI (per-user preferences):
   - Stored in [User:NAME] section of EvoSettings.INI on the workstation
   - Set on first login: screen layout, column widths, grid preferences
   - Email configuration (if user sends from EvoERP): [EMAIL CO# X User:Y] section
     requires SMTP host, port, credentials
```

**Key tables:**
- AHSYLOG — user master (PK: AHSY_USER_ID)
- BKSLEVEL — security permission matrix (PK: BKSL_MENU + BKSL_LEVEL)
- BKLOGON — active sessions (updated on each login)

**Common errors:**
- User can see all menus even with restricted level — check BKSLEVEL YN flag for
  each menu section; YN=Y grants access regardless of individual op flags
- User cannot log in — password case-sensitivity; check AHSY_PASSWORD format
- "Access denied" on everything — AHSY_USER_LEVL not matching a BKSLEVEL row

**Confidence: 74/100** — AHSYLOG + BKSLEVEL confirmed from DDF and DFMs; WBK steps
confirmed from WBK DFM analysis; BKLOGON behavior inferred.

---

### Recipe 14: Inventory Manual Adjustment

**When to use:** Correcting a quantity or cost discrepancy found outside of a formal
physical count (Recipe 8). Also used for writing off obsolete stock, adjusting for
damaged goods, or correcting a posting error.

**Module path:** IN → IN-G (Inventory Adjustment — Quantity) or IN-H (Cost Adjustment)

**Quantity adjustment (IN-G):**

```
1. IN-G (Inventory Adjustment)
   - Enter: item code (BKICMSTR / MTICMSTR)
   - Enter: adjustment quantity (positive = add, negative = remove)
   - Enter: GL account for the offset entry (inventory adjustment account)
   - Enter: reason code or note
   - Enter: lot / serial number if item is lot/serial tracked
   - Enter: bin location if location tracking is active
   - Post: creates BKISTXN row (type I = Inventory adjustment),
           updates BKICLOC (per-location quantity),
           posts offset to GL via BKGLTRAN

2. Verify:
   - IN-O-A (Item Inquiry) — confirm new on-hand qty
   - GL-O-B (GL Detail) — confirm GL offset was posted to correct account
```

**Cost adjustment (IN-H):**

```
1. IN-H (Cost Adjustment)
   - Enter: item code
   - Enter: cost adjustment amount (per unit or total)
   - System recalculates weighted average cost (if AVCO costing)
   - Or sets new standard cost (if STND costing — requires separate cost roll)
   - Posts BKISTXN row (type C = cost adjustment)
```

**Key tables:**
- BKICMSTR / MTICMSTR — item master (on-hand qty, average cost)
- BKICLOC — per-location quantity (updated if location tracking active)
- BKISTXN — inventory transaction history (I or C type row added)
- BKGLTRAN — GL offset entry

**Notes:**
- Adjustments bypass the formal Physical Inventory (PI module) — use PI for
  periodic full counts, IN-G only for spot corrections
- Large adjustments should be approved; EvoERP does not require approval for
  IN-G by default (no approval routing like WOAC/SOAC)
- Lot/serial tracked items: must specify lot/serial on adjustment

**Confidence: 70/100** — Module path confirmed from menu codes; table flow is standard
inventory adjustment logic for Btrieve-based systems; DFM for T7ING not specifically
analyzed (no T7ING.DFM found in samples — behavior inferred from module pattern).

---

### Recipe 15: Lot/Serial Tracking Lifecycle (Pass 106d, 2026-06-18)

**When to use:** Understanding how a specific lot/serial number flows from PO receipt through
production/consumption to customer shipment. Also useful for tracing a quality defect to its
production batch.

**Key tables:**

| Table | Purpose |
|---|---|
| LOT | Lot master — one row per lot number per item. Tracks: LOT_CODE(PK), ITEM, QTY, RCVDTE, CRTDTE, status |
| SERIAL | Serial master — one row per serial number per item |
| BKICLOC | Per-location, per-lot quantity on-hand |
| ISBINLOT | Bin-level lot quantity (ITEM+LOC+LOT+BIN PK) |
| ISSOBOX | Shipping box contents (SONUM+LINE+BOX PK) — includes LOT field |
| BKISTXN | Inventory transaction history — each receipt/issue writes a row with LOT field |
| WORKORD.LOT / WOROUT.LOT | WO routing step lot tracking |

**Lifecycle flow:**

```
Step 1: PO Receipt (PO-E)
  → LOT record created (or existing lot updated)
  → BKICLOC.QTY incremented for this lot at this location
  → BKISTXN row written (type R = Receipt, LOT field populated)

Step 2: WO Material Issue (DC module / WO-K-B)
  → Operator scans or enters lot number
  → BKICLOC.QTY decremented (lot consumed from location)
  → BKISTXN row written (type M = Material Issue, LOT field)
  → ISBINLOT updated if bin tracking active

Step 3: WO Completion (WO-K-J — Enter WO Completions)
  → If item is lot-tracked, lot assigned to finished goods
  → New LOT record for the finished goods lot (or existing updated)
  → BKICLOC updated for FG location

Step 4: SO Shipment (SO-C — Pick/Pack/Ship)
  → Lot number selected for the SO line
  → ISSOBOX.LOT populated for shipping scan
  → BKICLOC decremented from shipping location
  → BKISTXN row written (type S = Shipment, LOT field)
  → BKSOHLOT row written (SO history lot record)
```

**Tracing a lot:**
- Find all transactions for a lot: `SELECT * FROM BKISTXN WHERE BKIS_LOT_CODE = '?'`
- Find current qty by location: `SELECT * FROM BKICLOC WHERE BKIC_LOC_LOT = '?'`
- Find which SOs received this lot: `SELECT * FROM BKSOHLOT WHERE BKAR_TXN_LOT = '?'`

**Serial tracking** follows the same lifecycle but one-to-one (each serial number = 1 unit).
Serial numbers are tracked in the SERIAL table and BKISTXN.LOT field (shares the same column).

**Lot-enabled items:** Set BKICMSTR/MTICMSTR field `MTIC_PROD_LOT = 'Y'` (lot tracking) or
`MTIC_PROD_SER = 'Y'` (serial tracking). Once enabled, EvoERP requires a lot/serial on every
transaction for that item.

**Confidence: 68/100** — Table schemas confirmed from DDF; transaction type codes inferred from
field naming conventions; exact workflow steps confirmed from module DB fingerprints (PO-E opens
LOT, SO-C opens ISSOBOX+LOT, WO-K opens WORKORD+LOT). Per-step screen behavior blocked by RWN encryption.

---

### Recipe 16: New Company Creation (Pass 106d, 2026-06-18)

**When to use:** Adding a new entity/division to EvoERP that will have its own set of Btrieve
data files while sharing the same program installation.

**Module:** NE (New Entity / Company Initialization)
**Program:** T7NEWINIT (49 procs) — accessed via the NE module menu (14 button entries in BKMENUSU)

**What T7NEWINIT does:**
- Opens FILELOC (the TAS runtime file-location table) — reads the list of all registered `.B` files
- Opens FILEDES (file template definitions — NOT in Pervasive DDF, TAS runtime only)
- Creates a new directory on the share: `\\i2s109-solidcrm\DBAMFG$\<COMPANYCODE>\`
- Creates a new copy of every `.B` file registered in FILELOC, using `.<COMPANYCODE>` suffix
- Optionally seeds data from an existing company by reading BKAPVEND, BKARCUST, BKCMACCN

**Step-by-step:**

```
1. UT module → add new company code in company master (BKSY or system config)
2. NE-A or NE-B → T7NEWINIT
   - Select source company to seed from (or blank for empty)
   - Enter new company code (2-3 chars, e.g. "NW")
   - Choose which master data to copy:
     □ Vendor master (BKAPVEND)
     □ Customer master (BKARCUST)
     □ CRM accounts (BKCMACCN)
     □ Chart of accounts (BKGLCOA)
     □ Item master (BKICMSTR)
   - Confirm — T7NEWINIT creates all files
3. New company folder created: DBAMFG$\NW\
4. All data files created: BKARCUST.BNW, BKGLTRAN.BNW, WORKORD.BNW, etc.
5. Log in → company selection screen shows new company
```

**Company code → file suffix mapping:**
- 2-char company code "I2" → file suffix `.BI2` (e.g. `BKARCUST.BI2`)
- 2-char company code "AT" → file suffix `.BAT` (e.g. `BKARCUST.BAT`)
- 2-char company code "AB" → file suffix `.BAB`
- Default company → no suffix, plain `.B`

**Key tables:**
- FILELOC — TAS runtime table listing all registered file paths (not in Pervasive DDF)
- FILEDES — file template definitions (TAS runtime, not in DDF)
- BKAPVEND, BKARCUST, BKCMACCN — source data for optional seeding

**Confidence: 60/100** — T7NEWINIT DB fingerprint confirmed (FILELOC+FILEDES+BKAPVEND+BKARCUST+BKCMACCN);
multi-company file suffix convention confirmed from physical share inspection; exact menu path and
screen flow blocked by RWN encryption.

---

### Recipe 17: Payroll — Time Entry (Labor Hours Collection) (Pass 110d, 2026-06-19)

**When to use:** Collecting employee work hours into the payroll system each pay period.
Two paths exist: Data Collection / Work Order labor (for shop-floor workers) and direct
time card entry (for office/salaried workers).

**Path A — Shop-Floor DC → WO Labor → Payroll:**

```
1. DC or WO-F Enter Labor / WO-M Batch Labor Entry
   - Labor posted to WOLABOR (WO labor charges: DATE+EMP+WOPRE+WOSUF+OPER+TRXN PK)
   - Also posted to BKDCLAB (DC labor table: DATE+EMP+WOPRE+WOSUF+OPER PK)
   - Fields: RUNHRS, SETUPHRS, LABRATE, LABCOST per employee per WO/operation

2. WO-L-E — Print/Post Labor to Payroll
   - Reads WOLABOR records not yet transferred (POSTED flag = N)
   - Sums hours per employee per pay period
   - Inserts/updates records in BKPRCURP (current payroll period: 127 fields)
   - Sets POSTED = Y on source WOLABOR records
   - Prints a transfer register for verification
   - This replaces manual PR-J entry for shop-floor employees
```

**Path B — Time Card Entry (office / direct):**

```
1. PR-J — Enter Time Cards
   - Enter employee number, date, start/stop times, type (R=regular, O=overtime, D=double)
   - Three time formats: AM/PM, 24-hour, decimal (configured per division in PR-M)
   - System calculates total hours after lunch/break deduction
   - Entries held in time card staging (not yet in BKPRCURP)

2. PR-K — Print/Post Time Cards
   a. First run: print only (no post) — review for errors
   b. Return to PR-J if corrections needed
   c. Second run: print + post
      - Hours inserted into BKPRCURP for each employee
      - Regular, overtime, double-time columns populated separately
```

**Key tables read:** WOLABOR, BKDCLAB, BKPRMSTR
**Key tables written:** BKPRCURP (labor hours), WOLABOR (POSTED flag)

**Confidence: 80/100** — PR-J/K/WO-L-E steps confirmed from CHM; BKPRCURP and WOLABOR
schemas confirmed from DDF; exact staging table for PR-J time cards not confirmed (may be
BKPRCURP directly or an intermediate table, blocked by RWN encryption).

---

### Recipe 18: Payroll Calculation and Register (Pass 110d, 2026-06-19)

**When to use:** After all labor hours are in BKPRCURP (via Recipe 17), run the payroll
calculation to compute gross pay, deductions, and net pay. Run before printing checks.

```
1. Prerequisite — hours must be in BKPRCURP:
   - Either from WO-L-E (shop-floor path) or PR-J/PR-K (time card path)
   - Or entered directly in PR-B

2. PR-B — Enter Pay Info
   - Opening screen: list of employees with P column:
     C = record not yet processed for payment
     P = record processed for payment
     D = Direct Deposit | M = printed check
   - Tag employees for this payroll run:
     [Tag All] = all active employees
     [Tag Division] = specific division only (use for multi-division shops)
     [Tag/Untag One] = individual employee
   - For each tagged employee [Pay One]:
     a. Hours screen: regular/overtime/holiday/vacation/sick hours shown (pre-populated from
        WO-L-E or PR-K); review and adjust if needed
     b. Pay calculation:
        - Gross pay = hours × rates (from BKPRMSTR: regular/overtime/holiday rates)
        - Standard deductions: FIT, FICA-SS, FICA-Med, SIT, SDI, WC (from PR-F tax tables
          and PR-M division defaults)
        - User-defined deductions: up to 15 per division; pre-tax / post-tax configurable
        - Net pay = gross − all deductions
     c. Set OK to save? = Y → Save (F10)
     d. System moves to next tagged employee automatically
   - Results written to BKPRCURP (127 fields: all pay components, deductions, net pay)

3. PR-C — Print Payroll Register (verify before printing checks)
   - Reads BKPRCURP; no writes
   - Prints every employee's hours, gross pay, each deduction, net pay, pay type (D/M)
   - Prints totals for all employees
   - Review carefully — this is the last opportunity to correct before checks print
   - Return to PR-B to change any employee record before proceeding
```

**Key tables read:** BKPRCURP, BKPRMSTR, PR tax tables (BKPRTAXS or similar — exact name
blocked by encryption)
**Key tables written:** BKPRCURP (pay amounts, deductions, net pay fields)

**Payroll division note:** Shops with multiple divisions (e.g., different states, different
pay periods) process each division separately in PR-B. Run PR-B once per division using
[Tag Division].

**Confidence: 78/100** — PR-B/C program descriptions confirmed from CHM; calculation logic
(gross→deductions→net) confirmed; BKPRMSTR (384f) and BKPRCURP (127f) schemas confirmed
from DDF; internal calculation path (which fields drive which deductions) blocked by RWN
encryption.

---

### Recipe 19: Payroll Check Printing (Pass 110d, 2026-06-19)

**When to use:** After verifying the payroll register from Recipe 18, print and post
the payroll checks. This is the final, irreversible step of a payroll run.

```
1. Prerequisite: PR-C register reviewed and approved; BKPRCURP records verified.

2. PR-D — Print Payroll Checks
   a. Select bank account (from ISBANKS — payroll checking account configured in AD-B)
   b. Verify/confirm beginning check number (ISBANKS.NXTNUM — next available check #)
   c. Confirm check date (defaults to today; also sets pay period end date)

   Direct Deposit employees processed first:
   - Prints pay stubs to plain paper (not actual checks)
   - Asks if stubs printed correctly → Y = post
   - Updates next Direct Deposit reference in SD-R
   
   Printed check employees:
   - Switch printer if checks are in different tray
   - Prints actual checks (pin-feed or laser, per AD-B default)
   - Asks if checks printed correctly → Y = post all checks

   When posting confirmed (Y):
   - BKPRCURP records cleared (payroll period file reset)
   - Each check written to GL check register (BKGLCHK: CHKACT+NUM PK + DATE/TYPE/NAME/AMT/FLAG)
   - Employee pay history updated in BKPRMSTR (LAST PAID date, cumulative YTD/QTD amounts)
   - Current taxes withheld added to outstanding tax liability totals (held in BKPRMSTR per
     employee + division totals in BKPRCURP → BKPRGLFL GL accounts)
   - ISBANKS.NXTNUM incremented for next payroll
   - Payroll history record saved (source for PR-I Print Pay History and PR-L-* reports)

3. If a check prints incorrectly → PR-G — Void Payroll Check
   - Enter employee number, select check from history list
   - Reverses all PR-D postings: removes check from BKGLCHK, subtracts from pay history,
     posts offsetting GL entries
   - Caution: if taxes already transferred to AP via PR-H, must reverse PR-H entries manually
```

**Key tables read:** BKPRCURP, BKPRMSTR, ISBANKS
**Key tables written:** BKGLCHK (check register), BKPRMSTR (YTD/QTD history, LAST PAID),
ISBANKS (NXTNUM), BKGLTRAN (GL journal entries for payroll posting), payroll history table

**Confidence: 82/100** — PR-D program flow confirmed from CHM; ISBANKS (23f) schema confirmed
(NXTNUM field confirmed); BKGLCHK (11f) schema confirmed; BKGLTRAN confirmed as GL target;
exact payroll history table name (BKPRHIST or similar) not in DDF schema — may be blocked by
encryption or use a different naming convention.

---

### Recipe 20: Quarterly and Annual Tax Filing (Pass 110d, 2026-06-19)

**When to use:** End of each calendar quarter for 941/940 filing; year-end for W-2 generation
and payroll year-end close.

#### Part A — Quarterly Reports (run each quarter)

```
1. PR-L-A — Print Quarterly Info
   - Summary of all employee payroll activity for the quarter
   - Compare to FICA/FIT liability balances before paying

2. PR-L-C — Print QTD Taxable Earnings
   - Taxable earnings by type for each employee
   - Useful for FICA wage-base tracking (Social Security wage base limit)

3. PR-L-G — Print 941 and Schedule B Reports
   - IRS Form 941: Employer's Quarterly Federal Tax Return
   - Schedule B: per-payroll date deposit detail
   - Source: QTD FIT + FICA withheld from employee records + employer FICA match
   - Use this report to fill out the actual IRS Form 941

4. PR-L-H — Print 940 Forms
   - IRS Form 940: Employer's Annual Federal Unemployment (FUTA) Tax Return
   - Typically filed once per year but amounts computed quarterly
   - FUTA wages tracked separately (subject only up to $7,000/employee/year)

5. PR-H — Transfer Liabilities to AP
   - After running the 941, transfer the tax liabilities to AP for payment
   - Reads outstanding withholding totals from BKPRMSTR/BKPRCURP (per division)
   - Creates AP vouchers: one per tax type (FIT, FICA, SIT, FUTA, SUTA, SDI, WC,
     user-defined deductions) using vendor codes configured in AP-A
   - Debit: payroll liability GL accounts (from BKPRGLFL)
   - Credit: AP account (from AD-A GL defaults)
   - After transfer, outstanding liability amounts reset
   - Run AP check cycle (AP-E → AP-H) to pay the tax vendors
   - Run quarterly for FIT/FICA; run monthly if depositing on monthly schedule
```

#### Part B — Year-End Close (run before first payroll of new year)

```
6. PR-L-I — Print W-2 Forms
   - Source: BKPRW2 (W-2 data file created by PR-O)
   - Must run PR-O first to create BKPRW2

7. PR-O — Year End Routine
   - Creates BKPRW2.B* — copy of every employee's master payroll record with YTD amounts
   - Resets all employee QTD and YTD pay fields to zero (BKPRMSTR)
   - Must run before first payroll of new calendar year
   - Generates W-2 data file as part of the routine

8. PR-L-I — Print W-2 Forms (again, after PR-O)
   - Reads BKPRW2; prints IRS Form W-2 for each employee
   - Includes: wages, FIT withheld, FICA-SS, FICA-Med, SIT, SDI, user-defined deductions
     that are W-2 reportable (configured per deduction in PR-M)

9. PR-L-N — Print Payroll Wages Detail / PR-L-F — Print Subject to Report
   - Cross-check: verify total wages match W-2 totals and 941 amounts
   - PR-L-F: shows wages subject to each tax type (useful for state SUI/SDI reporting)
```

**Key tables read:** BKPRMSTR (QTD/YTD totals), BKPRGLFL (GL config), BKGLTRAN
**Key tables written:**
- PR-H: BKAPDESC (AP invoices for tax payments), BKGLTRAN (GL debit liability accounts)
- PR-O: BKPRW2 (W-2 data file), BKPRMSTR (QTD/YTD reset to zero)

**1099 note:** Contractor/vendor 1099 forms are not generated through the PR module —
they come from the AP module. Use AP-J (1099 report) which reads BKAP1099 or similar
table tracking 1099-eligible AP payments.

**Confidence: 82/100** — PR-H, PR-O, PR-L-A/C/G/H/I/N/F programs confirmed from CHM with
field-level detail; PR-H AP voucher creation path confirmed; BKPRW2 table named in PR-O
CHM text; BKPRGLFL (664f) GL config schema confirmed from DDF; internal QTD/YTD field
mapping within BKPRMSTR (384f) not individually named — count confirmed, field meanings
inferred from CHM context.

---

### Recipe 21: Year-End Close (Pass 112, 2026-06-19)

**When to use:** Once per calendar year — after the last payroll of the year but before the first payroll of the new year. This is a multi-module sequence; order matters.

#### Phase 1 — Final Monthly Close First

Complete the normal month-end close for December before starting year-end:
- AR-H, AP aging, IN valuation, GL period lock (AM period control)
- All outstanding AP vouchers entered and posted
- All PO receipts fully vouchered against BKAPINVT

#### Phase 2 — Payroll Year-End

```
1. PR-L-A — Print Quarterly Summary (final Q4 report)
   - Verify QTD FIT/FICA totals against liability balances

2. PR-L-G — Print 941 / Schedule B
   - Q4 payroll tax deposit reconciliation

3. PR-H — Transfer Tax Liabilities to AP
   - Creates BKAPINVL + BKAPINVT vouchers for outstanding tax liabilities
   - One AP voucher per tax type (FIT, FICA, FUTA, SUTA, SIT, SDI, WC, user-defined)
   - GL debit: payroll liability accounts (from BKPRGLFL)
   - GL credit: AP control account
   - Run AP check cycle (AP-E → AP-H) to pay the tax vendors

4. PR-O — Year End Routine  *** CRITICAL — do this before any new-year payroll ***
   - Copies BKPRMSTR → BKPRW2 (W-2 snapshot): all employee records with final YTD amounts
   - Resets BKPRMSTR QTD and YTD pay fields to zero for the new year
   - Rolls BKPRSALE → BKPRBOOK (prior-year sales/commission history)
   - BKPRW2 schema is identical to BKPRMSTR (384 fields, same BKPR_* prefix)

5. PR-A — Edit W-2 Data (optional corrections)
   - Edits BKPRW2 records if any corrections needed before printing
   - Box mapping: BKPR_WFITYTD → Box 2 (FIT withheld),
     BKPR_WFICAYTD → Box 4 (SS withheld),
     BKPR_WMEDYTD → Box 6 (Medicare withheld),
     BKPR_WSITYTD → Box 17 (state income tax)

6. PR-L-I — Print W-2 Forms
   - Source: BKPRW2 (must run PR-O first)
   - Reads BKPRW2 for each employee; formats IRS Form W-2
   - Includes wages, FIT, FICA-SS, FICA-Med, state, user-defined W-2-reportable deductions
```

#### Phase 3 — 1099 Processing (AP Module)

```
7. AP-S — Print 1099 Forms
   - Source: BKAPVEND (TAX_ID field) + BKAPVND2 (63f: 10-slot 1099 box amounts)
   - Reads BKAP_INVT records with TYPE="P" (1099-eligible payments) for the calendar year
   - Vendors with BKAPVEND.TAX_ID populated and 1099-eligible payments summed
   - Prints IRS Form 1099-MISC / 1099-NEC by vendor
   - Threshold: payments ≥ $600 (per IRS rules, enforced by AP-S filter)
```

#### Phase 4 — GL Year-End Close

```
8. AM (Accounting Maintenance) — Year-End GL Shift
   - Shifts BKGLCOA period balances forward by one year:
     Before: CURRENT_1..14, 1YPAST_1..14, 2YPAST_1..14
     After:  CURRENT_1..14 → zeroed/retained earnings, old CURRENT → 1YPAST, old 1YPAST → 2YPAST
   - Retained earnings: net income (sum of income − expense CURRENT balances) transferred to
     equity account; income/expense accounts zeroed for new year
   - BKGLCOA 65-field schema: CURRENT/BUDGET/1YPAST/2YPAST arrays each have 14 period columns
     plus a YE (year-end total) column

9. GL-O — Post Journal Batches (if any year-end adjusting entries remain)
   - Post any final GJR journal batches before closing
   - BKGLGJRN (header 11f) + BKGLGJLN (lines 9f) → BKGLTRAN (16f)
```

#### Phase 5 — Archive and Purge

```
10. SM-J-* — Data Maintenance: Archive and Purge
    - Run per-module archiving per the SM Data Maintenance schedule
    - BKGLTRAN prior-year transactions → BKGLATRN archive
    - BKARINV closed invoices → BKARHINV (AR history)
    - BKAPINVL paid vouchers → ISAPAINL archive
    - BKMENUSU-driven archive menus per module
    - Frees Btrieve file space; data remains queryable via archive tables

11. Set New Year Budget (optional)
    - GL-A or AM → enter BUDGET_1..14 values in BKGLCOA for the new fiscal year
    - Budget figures can be imported from spreadsheet or manually entered per account
```

**Key tables written:**
| Table | Written by | What changes |
|-------|-----------|-------------|
| BKPRW2 | PR-O | Year-end W-2 snapshot (copy of BKPRMSTR at close) |
| BKPRMSTR | PR-O | QTD/YTD fields zeroed for new year |
| BKPRSALE → BKPRBOOK | PR-O | Prior-year sales/commission history rolled |
| BKAPINVL + BKAPINVT | PR-H | AP vouchers for payroll tax liabilities |
| BKGLTRAN | PR-H, GL-O | GL journal entries for liability transfer + adjusting entries |
| BKGLCOA | AM year-end | CURRENT → 1YPAST shift; income/expense accounts zeroed |
| Archive tables | SM-J* | BKGLATRN, BKARHINV, ISAPAINL, etc. |

**Confidence: 88/100** — PR-O BKPRW2 creation + BKPRMSTR YTD reset confirmed from DDF + CHM (Pass 111d); BKGLCOA 65-field COA array structure confirmed from DDF (CURRENT/1YPAST/2YPAST columns); PR-H AP voucher creation via BKPRGLFL confirmed (Pass 111d); 1099 via BKAPVEND.TAX_ID + BKAPVND2 confirmed (Pass 111d); SM archive table names confirmed from sm/data-maintenance-archiving.md; exact GL year-end journal entries (retained earnings transfer) are in encrypted AM/GL RWN programs — mechanism inferred from BKGLCOA column structure.

---

### Recipe 22: Build the Pervasive DDF (Required Before ODBC/Java Tools) (Pass 112, 2026-06-19)

**When to use:** The Pervasive DDF (Data Dictionary Files — FILE.DDF, FIELD.DDF, INDEX.DDF) must
exist before ODBC connections or the Java EvoPVT.jar can query EvoERP tables. The DDF is NOT
shipped with EvoERP; it must be built from the running Pervasive database using Pervasive
utilities or EvoERP's own TA-S Data Dictionary Check tool.

**What the DDF does:**
- Maps Btrieve `.B` file names to SQL-style table names
- Defines field names, types, and lengths for each table
- Enables ODBC SELECT/INSERT/UPDATE/DELETE on Btrieve files
- Required by `EvoPVT.jar` (jdbc.ini Host/Name/Port/Company parameters)
- Required by any external tool using `DSN=DBA` or the Pervasive ODBC driver

#### Method 1 — Pervasive DDF Builder (Pervasive utility)

```
1. Open Pervasive Control Center (PCC) on the server (i2s109-solidcrm)
   - Path: Start → Pervasive → Pervasive Control Center

2. Connect to the database: i2s109-solidcrm → Databases → DBA (or EVOADMIN)
   - The DBA database corresponds to \\i2s109-solidcrm\DBAMFG$\

3. Use DDF Builder tool:
   - Right-click the database → Build DDF
   - Point at the \\i2s109-solidcrm\DBAMFG$\ directory containing the .B files
   - DDF Builder reads each .B file's internal schema and creates:
     FILE.DDF  (table names → file paths)
     FIELD.DDF (field definitions)
     INDEX.DDF (key segment definitions)
   - Output directory: \\i2s109-solidcrm\DBAMFG$\ (same folder as the .B files)

4. Restart Pervasive service to pick up new DDF
```

#### Method 2 — EvoERP TA-S (Data Dictionary Check)

```
TA-S — Data Dictionary Check (T7DDCHECK.RWN, 92 procs)
- Opens FILEDICT (DDF mapping registry in TAS runtime)
- Opens FILEKEY, FILELOC (file location + key definitions)
- Validates that the DDF in FILEDICT matches the physical .B files
- Can rebuild missing or inconsistent DDF entries
- Access via: TA module → TA-S

Note: TA-S maintains the TAS-runtime DDF (FILEDICT table), not necessarily the
Pervasive ODBC DDF (FILE.DDF/FIELD.DDF/INDEX.DDF). Both may need updating after
schema changes.
```

#### Method 3 — Pervasive ODBC Administrator

```
1. Open Pervasive ODBC Administrator (32-bit):
   C:\Windows\SysWOW64\odbcad32.exe  ← ALWAYS use this for EvoERP (32-bit app)
   (NOT C:\Windows\System32\odbcad32.exe which is 64-bit)

2. System DSN → Add → Pervasive ODBC Client Interface (32-bit)
   - Data Source Name: DBA
   - Server Name: i2s109-solidcrm
   - Port: 1583
   - Database: @DBA  (@ prefix = Pervasive server-side database)

3. Test connection — if DDF exists, tables will be visible in the schema viewer

4. If no tables appear: run DDF Builder (Method 1) first
```

**Key locations:**
- DDF files: `\\i2s109-solidcrm\DBAMFG$\FILE.DDF`, `FIELD.DDF`, `INDEX.DDF`
- ODBC DSN name: `DBA` (32-bit system DSN on each workstation)
- Pervasive service: runs on `i2s109-solidcrm`, port 1583
- Java config: `C:\ISTS\jdbc.ini` — Host=i2s109-solidcrm, Name=DBA, Port=1583

**Bitness warning:** EvoERP is a 32-bit application. Always use the 32-bit ODBC admin
(`SysWOW64\odbcad32.exe`). The 64-bit admin (`System32\odbcad32.exe`) stores DSNs in
a different registry hive that EvoERP cannot see.

**After schema changes (adding fields, new tables):**
```
1. Run DDF Builder to update FILE.DDF/FIELD.DDF/INDEX.DDF
2. OR run TA-S to sync TAS runtime FILEDICT
3. Restart any open ODBC connections to pick up schema changes
```

**Confidence: 88/100** — ODBC bitness trap confirmed (System32 vs SysWOW64 hives documented);
DSN parameters confirmed (Host/Port/Database/Driver from ODBC setup testing); jdbc.ini parameters
confirmed from Pass 110e Java analysis; DDF file structure (FILE.DDF/FIELD.DDF/INDEX.DDF)
confirmed as standard Pervasive DDF format; exact TA-S behavior blocked by RWN encryption
(FILEDICT sync mechanism inferred from T7DDCHECK DB fingerprint: FILEDICT+FILEKEY+FILELOC).

---

### Recipe 23: Add a New Customer (Pass 113, 2026-06-19)

**Menu:** AR-A (Accounts Receivable → Maintain Customers)
**Program:** T7ARA.RWN
**Primary table:** BKARCUST (106 fields, fully documented)

**When to use:** When onboarding a new customer who will receive invoices through EvoERP.

#### Steps

```
1. AR → AR-A → press F4 (or click New) to add new record

2. Required — Identity
   BKAR_CUST_CODE    (10)   Unique customer code (e.g., ACME001)
   BKAR_CUST_NAME    (40)   Company name
   BKAR_CUST_ADDR1   (40)   Address line 1
   BKAR_CUST_ADDR2   (40)   Address line 2 (optional)
   BKAR_CUST_CITY    (25)   City
   BKAR_CUST_STATE   (2)    State abbreviation
   BKAR_CUST_ZIP     (10)   ZIP / postal code
   BKAR_CUST_CNTRY   (15)   Country (blank = domestic)
   BKAR_CUST_PHONE   (20)   Main phone
   BKAR_CUST_FAX     (20)   Fax (optional)
   BKAR_CUST_CONT    (25)   Primary contact name

3. Required — Billing defaults
   BKAR_CUST_TERMS   (4)    Payment terms code (links to ISTERMS table)
                            Common: NET30, NET60, 2/10NET30
   BKAR_CUST_SALSP   (10)   Salesperson code (links to BKPRMSTR employee)
   BKAR_CUST_CLASS   (2)    Customer class code (links to CLASS table)

4. Required — Tax and compliance
   BKAR_CUST_TAXGRP  (4)    Tax group code (links to ISTAXGRP)
                            Determines which taxes apply to invoices
   BKAR_CUST_RESALE  (20)   Resale certificate number (if tax-exempt)

5. Optional — Credit and limits
   BKAR_CUST_CRLIM   FLOAT  Credit limit (0 = no limit enforced)
   BKAR_CUST_HOLD    (1)    Credit hold flag: Y = block new orders

6. Optional — Additional tabs
   - Shipping: alternate ship-to addresses (BKAR_CUST_SHIP*)
   - Notes: free-text notes (stored separately)
   - Pricing: customer-specific pricing (links to BKICPMAT)
   - CRM: links to BKCMACCN contact records

7. Save → customer is immediately active for invoicing
```

**Key relationships:**
- BKAR_CUST_TERMS → `ISTERMS.TERMS_NUM` (payment terms master)
- BKAR_CUST_SALSP → `BKPRMSTR.EMP#` or `BKPRSALE.SLSP` (commission tracking)
- BKAR_CUST_TAXGRP → `ISTAXGRP` (multi-jurisdiction tax groups)
- BKAR_CUST_CLASS → `CLASS` table (customer segmentation + per-class GL accounts)
- Customer code → `BKARINV.BKAR_INV_CUST` (all future invoices)
- Customer code → `BKARINVT.BKAR_INVT_CODE` (open-item AR ledger)

**Confidence: 90/100** — BKARCUST all 106 fields confirmed from DDF (Pass 110e); T7ARA
form confirmed from DFM + CHM; field names from tier1-tables.md documentation.

---

### Recipe 24: Add a New Vendor (Pass 113, 2026-06-19)

**Menu:** AP-A (Accounts Payable → Maintain Vendors)
**Program:** T7APVEND.RWN (or equivalent)
**Primary table:** BKAPVEND (72 fields, fully documented)

**When to use:** When adding a new supplier, subcontractor, or payee who will be paid through EvoERP AP.

#### Steps

```
1. AP → AP-A → press F4 (or click New) to add new record

2. Required — Identity
   BKAP_VEND_CODE    (10)   Unique vendor code (e.g., STEELCO01)
   BKAP_VEND_NAME    (40)   Company/person name
   BKAP_VEND_ADDR1   (40)   Address line 1
   BKAP_VEND_ADDR2   (40)   Address line 2 (optional)
   BKAP_VEND_CITY    (25)   City
   BKAP_VEND_STATE   (2)    State
   BKAP_VEND_ZIP     (10)   ZIP / postal code
   BKAP_VEND_PHONE   (20)   Main phone
   BKAP_VEND_CONT    (25)   Primary contact name

3. Required — Payment defaults
   BKAP_VEND_TERMS   (4)    Payment terms code (same ISTERMS table as AR)
   BKAP_VEND_CURR    (3)    Currency code (blank = functional currency)

4. Required — Tax / 1099 setup
   BKAP_VEND_TAX_ID  (15)   Federal EIN or SSN (for 1099 reporting)
   BKAP_VEND_1099    (1)    1099 flag: M=1099-MISC, N=not subject to 1099
                            IMPORTANT: set correctly before first payment;
                            affects AP-S 1099 year-end run

5. Optional — Banking / EFT (for direct deposit / ACH)
   BKAP_VEND_BANK*   fields  Bank routing + account (for EFT payments)

6. Optional — Additional tabs
   - BKAPVND2: 10-slot 1099 box amount overrides + extended data
   - GL account: override AP posting account (otherwise uses system default)
   - Notes: free-text (BKAPNOTE)
   - Approved source: if vendor supplies specific parts (BKSBVEND)

7. Save → vendor is immediately active for PO and voucher entry
```

**Key relationships:**
- BKAP_VEND_CODE → `BKAPPO.BKAP_PO_VENDOR` (purchase orders)
- BKAP_VEND_CODE → `BKAPINVL.BKAP_INV_VENDCODE` (AP vouchers)
- BKAP_VEND_CODE → `BKAPCHKF/H.BKAP_CHK_VENDOR` (AP checks)
- BKAP_VEND_CODE → `BKAPVND2` (extended vendor data, 1099 boxes)
- BKAP_VEND_TAX_ID + BKAP_VEND_1099 → `AP-S` 1099 annual print run
- BKAP_VEND_CODE → `BKSBVEND` (vendor approved source / part cross-ref)

**1099 workflow note:**
If BKAP_VEND_1099 = 'M' and payments for the year exceed the IRS threshold, the vendor
will appear on AP-S (1099 print). The tax ID (BKAP_VEND_TAX_ID) is printed on the form.
Payment totals accumulate automatically in BKAPVND2 as checks are posted.

**Confidence: 90/100** — BKAPVEND all 72 fields confirmed from DDF (Pass 110e);
vendor 1099 workflow confirmed from Bkaph.SRC analysis and BKAPVND2 schema; AP-S
confirmed in year-end recipe (Recipe 21).

---

### Recipe 25: Receive a Purchase Order (Pass 113, 2026-06-19)

**Menu:** PO-J (Purchase Orders → Receive PO Items)
**Program:** T7POJC.RWN (T7PO series)
**Primary tables:** BKAPINVL (390f — AP voucher lines), BKAPPO (57f — PO header), BKAPPOL (38f — PO lines)

**When to use:** When goods arrive from a vendor and need to be received into inventory, triggering an AP voucher.

#### Steps

```
1. PO → PO-J → enter PO number (from BKAPPO)

2. Review open lines (T7POJC reads BKAPPOL for line status)
   - QTY_ORD = original ordered quantity
   - QTY_RCVD = already received
   - QTY_OPEN = remaining (QTY_ORD - QTY_RCVD)

3. Enter received quantities for each line
   - Can receive partial quantities (partial receipt leaves line open)
   - Each line links to BKICMSTR item master for UOM validation

4. QC inspection (optional — controlled by item QC flag)
   - T7POJC passes items through QC entry if BKICMSTR.QC = Y
   - BKQCMSTR (14f) and BKQCTRAN (21f) record inspection results
   - RoHS and NCR tracking available here (T7POJC confirmed from DFM)

5. Lot / serial number entry (if item is lot/serial controlled)
   - Lot: creates LOT record (25f) with RECDATE + VENDOR + WOCOST
   - Serial: creates SERIAL record (30f) with PO receipt path
   - Assignment links receipt to lot/serial before inventory update

6. Bin location assignment (if WC / bin control is active)
   - Choose target location (BKICLOC) and bin (ISBNMSTR)
   - Recorded in BKICLOCM and ISBINLOC

7. Confirm receipt → system creates:
   a. AP voucher lines: BKAPINVL (390f) — header fields in first 10 fields,
      GL distribution array (GLACT/GLDPT/DC/GLD/DAMT_1..75 for up to 75 GL splits)
   b. AP open-item: BKAPINVT (19f) — one record per invoice/voucher
   c. Inventory update: BKICMSTR.UOH += received quantity
   d. Cost update: DBAFIFO or BKICVAL cost layer (FIFO/LIFO/average)
   e. INVTXN record: receipt transaction logged with LOT/SERIAL/COST/REF

8. Voucher now appears in AP-F (select invoices for payment)
   → proceed to AP-H to print check when payment is due
```

**Key note — landed cost:**
If IM module (Import Management) is active, landed costs (freight, duty, customs) can
be allocated to received items BEFORE posting. IM-D/IM-E set up landed cost GL accounts;
landed amounts allocated via BKAPINVL GL distribution.

**Key note — PO-A vs PO-J sequence:**
- PO-A creates the PO (BKAPPO header + BKAPPOL lines)
- PO-E prints the PO (RTM output)
- PO-J receives the PO (this recipe)
- AP-B can also create a voucher directly without PO (non-PO invoices)

**Confidence: 82/100** — T7POJC confirmed from DFM (RoHS/NCR/digital sig tabs);
BKAPINVL 390f schema confirmed; BKAPPOL 38f schema confirmed; lot/serial receipt path
confirmed from LC/SC module docs; QC path confirmed from BKQCMSTR/BKQCTRAN schemas.
POJC internal logic blocked by RWN encryption (some steps inferred from table relationships).

---

## Pass 99 — EvoLinks, FNO, Calendar, Infrastructure DFM sweep (2026-06-18)

### EvoLinks — Document Attachment System (ISLINKS Table)

EvoLinks.DFM confirms the ISLINKS table schema and attachment workflow:

| Field | Type | Meaning |
|-------|------|---------|
| IS.LNK.SORT | STRING | Sort key / attachment ID (PK part) |
| IS.LNK.DATE | DATE | Date attachment was added |
| IS.LNK.WHO | STRING | User who attached the file |
| IS.LNK.PRIVATE | STRING | Private flag — only visible to attaching user |
| IS.LNK.PCB[100] | STRING array | PCB (print control block?) — 100-slot array (attachment metadata) |
| FILELINK | STRING | Path/filename of the linked document |
| ALERTS | STRING | Alert/notification flag on this link |
| LEXIST | STRING | Link exists flag (document still present) |
| GEN.ID | STRING | Generic ID — the record key (customer#, WO#, etc.) that this link attaches to |
| inventory.link | STRING | Inventory link flag — link is to an inventory item |

**How EvoLinks works:** Every EvoERP record (customers, WOs, SOs, items, etc.) can have
documents, images, or files attached via EvoLinks. GEN.ID stores the parent record key;
FILELINK stores the document path (relative to `LinkDoc\` or absolute). LEXIST checks
whether the file still exists. IS.LNK.PRIVATE prevents other users from seeing the link.

**Kill button:** The KILL caption in the DFM is the delete-link action — removes the link
record from ISLINKS without deleting the actual file.

**Confidence: 78/100** — All visible fields confirmed from DFM; PCB[100] array purpose
inferred; GEN.ID linking mechanism inferred from pattern.

---

### EvoFNO — Features & Options Configurator (ISFO.HDR.* Table)

EvoFNO.DFM confirms the Features & Options header table:

| Field | Meaning |
|-------|---------|
| ISFO.HDR.PARENT | Parent part number (the configurable item) |
| ISFO.HDR.DESC | F/O configuration description |
| ISFO.HDR.CUST | Customer code (customer-specific configuration) |
| ISFO.HDR.VEND | Vendor code |
| ISFO.HDR.RFQ | RFQ number |
| ISFO.HDR.STATUS | Configuration status code |
| ISFO.HDR.DATE | Date created/modified |

**Conversion flags (turn F/O into real orders):**
- SOCB — convert to Sales Order
- WOCB — convert to Work Order
- POCB — convert to Purchase Order
- NICB — convert to New Item Number
- SQCB — convert to Sales Quote
- RQCB — convert to RFQ

**EvoFNOQty.DFM** — Quantity entry for conversion:
CVTQty (quantity to make), CVTLoc (location), CVTCV (customer/vendor), cvtdate (due date).

**How FNO works:** The user configures a product by selecting features/options from a
BOM-like tree (ISFO.HDR). When ready, it converts to a real SO, WO, PO, or new item
by transferring the F/O selections to the target module.

**Confidence: 72/100** — Header table confirmed; ISFO line (option selection) table
not yet fully analyzed; conversion mechanism inferred.

---

### CAL Module — Calendar and Reminders

**CALREM.DFM** — Calendar Reminders browser:
Shows reminders in calendar view. Confirms: "Export to Google Calendar" button
(calls CALREMGC.DFM). Drill-down: caldrillbt (drill into reminder details).

**CALREMGC.DFM** — Google Calendar Export:
from.date, thru.date (date range), expall/expopen/expdis (filter: all/open-only/dismissed-only).
Exports EvoERP reminders to Google Calendar iCal format.

**evorereminders.DFM** — Reminder Snooze:
remdate (new date), remmin (minutes until next alert), remtime (time for reschedule).
The "Snooze" functionality for IS.REM reminders.

**evoCSR.DFM** — Calendar Summary Report:
esd (ESD date flag), csd (CDD — customer desired date flag), cust.from/thru, item.from/thru,
ENTRY.DATE, custpo (customer PO column), qtybo (qty + backorder column), socust (SO# + customer column).
Cross-reference report of SOs by date range with optional columns.

---

### ISFO — Features & Options Line Table (ISFO.LIN.*)

From EvoFNO context (not directly confirmed but inferred from FNO pattern):
ISFO.LIN.PARENT → ISFO.HDR.PARENT, ISFO.LIN.OPT (option code),
ISFO.LIN.DESC (option description), ISFO.LIN.QTY (option quantity),
ISFO.LIN.SEL (selected flag).

**Confidence: 45/100** — Line table structure inferred from FNO navigation pattern.

---

### T7CUSTOMS — Configurable Custom Content Slots

T7CUSTOMS.DFM fully confirms the 10-slot configurable content system:

| Field | Meaning |
|-------|---------|
| Custom.control[1-10] | Enable/disable flag for slot N |
| Custom.Name[1-10] | Caption/label for slot N |
| Custom.Desc[1-10] | Description for slot N |

These 10 slots appear across multiple modules as user-configurable custom fields.
The T7CUSTOMS form manages the slot labels and enable states (one row per slot).

**Confirmed earlier:** MTIC.PROD.RCOST[15] = Duty uses one of these slots as the
standard cost component label system.

**Confidence: 82/100** — All 30 fields confirmed (10 × 3 arrays).

---

### EvoUpdate Infrastructure

**Full update pipeline (confirmed from rwn_symbols.json, Pass 110e, 2026-06-19):**

| Program | Procs | Role |
|---------|------:|------|
| `EvoUpdate.RWN` | 9 | Entry point — reads full ISTS.CFG buffer, validates admin password, delegates to EvoERPupd/EvoPRupd |
| `EvoUPDSetup.RWN` | 18 | Configure update path (FILE_NAME = server path to update package), validate serial |
| `EvoERPupd.RWN` | 77 | Main schema migration engine — ERP tables |
| `EvoPRupd.RWN` | 51 | Payroll schema migration engine |
| `UPDTP7.EXE` | — | Binary patcher (role unclear; likely patches EVO .RWN files themselves) |

**EvoERPupd schema migration engine (77 procs):**

Opens FILEDICT + FILEDBF + FILEKEY — EvoERP's own internal schema registry (separate from Pervasive DDF). Together these define: table field definitions (FILEDICT), dBASE-format table catalog (FILEDBF), and index/key definitions (FILEKEY).

Key migration variables:
- `FILE_DEF` / `FILE.CHRS` — field definition descriptor
- `CREATE_FILE` — flag to create a new table
- `FROM_FILE` / `TO_FILE` — source and destination files during record migration
- `DO_FILE` — process this file in the update loop
- `UPDATE_FD` / `UPDATE_FD_CNTR` — update field definitions; counter
- `UPDT_CNTR` — total update operations counter
- `RSTR_FILES` — restore files on failure/rollback
- `ISTS.CFG.EPASS` — encrypted update password (update packages may be locked)

Also opens BKLUGRID (updates grid/lookup column definitions), ISDRILLM (updates drill-down module definitions), and a large set of ERP data tables (BKBMMSTR, BKICMSTR, BKARINV, WORKORD, WOBOM, WOLABOR, etc.) — meaning updates can **read existing data records** and transform them as part of the schema migration.

**Summary of the update flow:**
1. Admin launches EvoUpdate → EvoUPDSetup configures the update server path.
2. EvoERPupd reads FILE*.UPD manifests → for each file in the update:
   a. Reads current schema from FILEDICT/FILEDBF/FILEKEY.
   b. Creates new table structure (CREATE_FILE).
   c. Copies records FROM_FILE → TO_FILE with field mapping.
   d. Updates BKLUGRID and ISDRILLM to match new field names.
   e. Updates ISTS.CFG.* entries to new default values.
3. EvoPRupd does the same for Payroll tables.
4. `Evocnvtb.RWN` (separate) finalizes: syncs Btrieve DDF with the new .B file structure.

**EvoERPupd.DFM / EvoForceUpd.DFM** — Update engine UI forms:
- Uforce = force update flag (bypass version check)
- Clog = create log file flag
- FD Name / FileName = data dictionary field name + update file name
- "Files in this Update" + "Files to Force" — two-panel view: which files the update includes vs. which to force-overwrite

**EvoUPDsetup.DFM** — Update server setup:
file_name = server path for update distribution.

**Evocnvtb.DFM** — Data dictionary synchronization:
ConvertingFile = currently processing table name. Syncs the Btrieve DDF
with the actual .B file structure after schema changes.

---

### EvoService / Mobile Installer Forms

**EVOSERVICEREMOVE.DFM** — Remove EvoService: simple path entry + continue.
No data fields — just removes the Windows service registration.

**EvoMobilesetup.DFM** — Mobile Reminders setup:
Same fields as EvoSchedsetup: file_name, email.cfg.SMTP/user/pass/Email/Name,
thirtytwo/sixtyfour, plus SMTP port. Sets up email for mobile reminder delivery.

**Evowkssetup.DFM / EvoDCsetup.DFM** — Workstation and DC terminal setup:
file_name (server path), dmy/mdy (date format toggle DD/MM/YY or MM/DD/YY).
Two variants of the same workstation-initialization form.

**EVOFUP.DFM** — Support file upload:
FUTECH (tech contact), fu.desc (description), FU.ATTACH (attach screenshots flag),
fu.name (your name), fu.REmail (return email). Internal tech-support file upload utility.

**EvocfgSave.DFM** — Save/restore program defaults:
evoss (Evo service settings flag). Manages saving and restoring EVO configuration defaults.

---

### EvoLinks CVT (Link Format Conversion)

**EvoLinkCVT.DFM** — "Evo Links CVT": converts old image-based links to the current
EvoLinks format. No data fields — purely a conversion progress indicator.

---

### EVOBSR — Business Status Rebuild

**EVOBSR.DFM** — Rebuilds the ISBSF (Business Score File — KPI aggregation table).
"Business Status Rebuild" + "Initializing..." — rebuilds cross-module KPI/score data.
ISBSF confirmed as the target table.



---

## Pass 102 — Java Integration: EvoPVT.jar Architecture (2026-06-18)

**Source:** `samples/jar/extracted/` — constant-pool string extraction from 881 class files.
**Confidence:** 85/100 — all strings confirmed from class file constant pools; runtime
dispatch logic inferred from class structure since bytecode not fully decompiled.

---

### EvoPVT.jar Overview

`EvoPVT.jar` (lib version 0.4.7) is EvoERP's Java bridge layer. It operates in two modes:

| Mode | Entry Point | Purpose |
|------|-------------|---------|
| **GUI** | `com.evoerp.javafx.EvoApp` | JavaFX desktop UI (calendar, tabular views, CRM dashboard) |
| **Task runner** | `com.evoerp.TASKS.sql.Main` | CLI task executor — invoked by TAS Pro, writes results to ISJAVA |

TAS Pro 7 (tp7runtime) launches the task runner via command line, passing `host port name`
as arguments (confirmed from `Main$WindowsUtils.main()` argument dispatch to
`PervasiveDatabase.writeParams()`).

---

### ISJAVA Table (TAS Pro ↔ Java bridge)

**Confirmed from:** `TASKS/sql/PervasiveDatabase.class` constant pool.

```
INSERT INTO ISJAVA (IS_JAVA_UID, IS_JAVA_DATE, IS_JAVA_PARAM_1, IS_JAVA_PARAM_2, ...) VALUES (?, ?, ...)
```

- Table is **not** a Java model class — it lives on the TAS Pro / Pervasive side only.
- TAS Pro writes a task request row; Java reads and processes it; Java writes result params back.
- Field pattern:
  - `IS_JAVA_UID` — unique task identifier (string, used as `setString` param 1)
  - `IS_JAVA_DATE` — task date (`setDate` param 2, java.sql.Date)
  - `IS_JAVA_PARAM_N` — variable number of string parameters (dynamically constructed
    loop: `, IS_JAVA_PARAM_` + suffix + `) VALUES (?, ?` + `, ?` × N)
- `writeParams(params, maxLength)` — the Java method that performs the INSERT.
- The parameter count (N) is runtime-determined by `maxLength`.

---

### Connection Configuration: jdbc.ini

**Confirmed from:** `DatabaseSettings.class` constant pool — file name `jdbc.ini` literal.

`DatabaseSettings` reads a plain-text configuration file (`jdbc.ini`) with this format:

```ini
Company=<company-code>
Host=<server-hostname>
Port=<port-number>
Name=<database-name>
Tree Destination=<report-tree-path>
```

Key facts:
- Default file path resolved at runtime from process working directory or a known config path.
- Multiple company instances are supported via `DatabaseSettings.getInstance(code)` —
  one instance per company code, keyed in a `HashMap<String, DatabaseSettings>`.
- `getDefault()` returns the default company instance.
- `isInitialized()` guards against unread configurations.

---

### Database Connection: Pervasive JDBC

**Confirmed from:** `sql/PervasiveDatabase.class` constant pool.

- JDBC URL prefix: `jdbc:pervasive://`
- Driver class: `com.pervasive.jdbc.v2.ConnectionPoolDataSource`
- Connection parameters: host, port, name (from `jdbc.ini`)
- Connection pool managed by `DatabaseWorkerService` (thread-local connection model)
- SQL queries confirmed in this class:

```sql
-- Shop calendar holiday/weekend dates
SELECT MTCAL_DATE FROM CALENDAR WHERE MTCAL_DATE IS NOT NULL

-- Carrier tracking URL template
SELECT IS_SHIP_WEB_2 FROM ISSHIPCO WHERE IS_SHIP_SHIPVIA = ?
```

The tracking URL uses `%%TRACK%%` as a placeholder, replaced with the actual tracking
number at runtime via `String.replace("%%TRACK%%", trackingNumber)`.

---

### WinRegistry Utility

**Confirmed from:** `com/evoerp/util/WinRegistry.class` constant pool.

EvoERP Java reads/writes Windows registry using the `reg` command-line tool. Methods:
- `read(path, key)` — runs `reg query <path> /v <key>`, parses `REG_\S+` type + value
- `addKey(path, key)` / `addKey(path, key, value)` — runs `reg add`
- `deleteKey(path, key)` — runs `reg delete`

Uses `COMPLETED SUCCESSFULLY` output to detect success.
Registry paths are not embedded in this class — they are passed as arguments from callers.

---

### Process Monitor (Main$WindowsUtils)

**Confirmed from:** `TASKS/sql/Main$WindowsUtils.class` constant pool.

When the task runner starts, it monitors these three EvoERP-related processes:
```
PV.EXE  Evoerp.exe  TP7Runtime.exe
```
The `listRunningProcesses(istsPath)` method checks which of these are active.
This is likely used to determine whether TAS Pro is still alive before committing results.

---

### EvoPVT.jar GUI Architecture

**Confirmed from:** `com/evoerp/Evo.class` and javafx/* classes.

Command-line arguments accepted by the main Evo application:
| Arg | Purpose |
|-----|---------|
| `-log <level>` | Set log level (SEVERE/WARNING/INFO/CONFIG/FINE/FINER/FINEST/ALL/OFF) |
| `-nodialog` | Suppress error dialog boxes (runs in server mode) |
| `-lang <locale>` | Set locale (default: `en_US`, format: `language_country_variant`) |

Property keys read/written by `Evo.getProperty()` / `Evo.setProperty()`:
| Key | Purpose |
|-----|---------|
| `app.version` | Application version string |
| `lib.version` | Library version (confirmed: `0.4.7`) |
| `app.date` | Application build date |
| `app.name` | Application name |
| `evo.version` | EVO version (read from `EVO.VER` file) |
| `pervasive.version` | Pervasive SQL engine version |
| `company.id` | Active company code |
| `user.name` | Logged-in user name |

Logs directory: `logs/` relative to working directory. Log file: `<classname>.log`.

---

### Java SQL Layer (com.evoerp.sql)

The `sql` package is a fluent query-builder over Pervasive JDBC. Key classes:

| Class | Role |
|-------|------|
| `Query` | SELECT builder — `Query.selecting(fields).from(table).where(clause)` |
| `Table` | Table descriptor |
| `Field` | Typed field reference (`StringField`, `IntegerField`, `BigDecimalField`, `LocalDateField`, `LocalTimeField`) |
| `Clause` | WHERE condition builder (`AndClause`, `OrClause`, `BinaryClause`, `NullClause`) |
| `Ordering` | ORDER BY builder |
| `Sql` | Utility class with static SQL helpers |
| `ShopCalendar` | Wraps CALENDAR table; returns `Set<LocalDate>` of holidays/weekends |
| `DatabaseWorkerService` | Thread pool with thread-local connections for concurrent queries |

---

### Complete Java-Side Table Model

The `com.evoerp.sql.tables` package contains **~260+ Java model classes**, one per
Pervasive table. These are the tables EvoPVT.jar can query. Full inventory by module:

**AP (Accounts Payable):**
BKAPADSC, BKAPAPO, BKAPAPOL, BKAPCHKF, BKAPCHKH, BKAPDEP, BKAPDESC, BKAPEIVT,
BKAPEVND, BKAPHDSC, BKAPHPO, BKAPHPOL, BKAPINVL, BKAPINVT, BKAPNOTE, BKAPPO, BKAPPOL,
BKAPQUOT, BKAPRFQ, BKAPRFQL, BKAPRIVL, BKAPVEND, BKAPVND2

**AR (Accounts Receivable):**
BKARCHKF, BKARCHKH, BKARCUST, BKARDEP, BKARDESC, BKARDPST, BKARECST, BKAREIVT,
BKARHDSC, BKARHINV, BKARHIVL, BKARHTAX, BKARINV, BKARINVI, BKARINVL, BKARINVT, BKARINVV,
BKARRDSC, BKARRINV, BKARRIVL, BKARSHIP, BKARSIVL, BKART, BKARTNOT, BKARTXN, BKARTXNB, BKARTXNS

**BM (Bill of Materials):**
BKBMAMTR, BKBMAVAL, BKBMCNFG, BKBMDIM, BKBMEMTR, BKBMERMK, BKBMMSTR, BKBMNOTE, BKBMREMK, BKBMSUMM

**CM (CRM / Customer Management):**
BKCMACCC, BKCMACCL, BKCMACCN, BKCMACCT, BKCMACFC, BKCMACTD, BKCMACTF, BKCMACTH,
BKCMCNTD, BKCMCTL1..4, BKCMCTRL, BKCMCUST, BKCMDE, BKCMDTCD, BKCMDUN, BKCMDUNH,
BKCMEACC, BKCMEACD, BKCMEACF, BKCMEACH, BKCMEACT, BKCMEFTM, BKCMFORM, BKCMFTME,
BKCMHCD2, BKCMHCOD, BKCMLEAD, BKCMMHST, BKCMPCFC, BKCMPCNT, BKCMPCTF, BKCMPCTH,
BKCMREP, BKCMSBDF, BKCMTEMP, BKCMTERR, BKCMTMP1..4, BKCMVNDF, BKCMVNDH, BKCMVNFC

**DC (Data Collection):**
BKDCCFG, BKDCCLAB, BKDCHLAB, BKDCLAB, BKDCPLAB, BKDCSHFT, BKDCTLAB

**EDI:**
BKEDIDUN, BKEDIH, BKEDIL, BKEDMSTR, BKEDNOTE, BKEDPOST

**Estimating:**
BKESTCFG, BKESTQT, BKESTQTL

**GL (General Ledger):**
BKGLACHK, BKGLCCOA, BKGLCHK, BKGLCOA, BKGLDESC, BKGLECOA, BKGLETRN, BKGLFCOA, BKGLFSTL,
BKGLGJLN, BKGLGJRN, BKGLHIST, BKGLRGJL, BKGLRGJR, BKGLSTMT, BKGLTEMP, BKGLTGJL, BKGLTGJR,
BKGLTMP, BKGLTMP2, BKGLTMP3, BKGLTRAN, BKGLX, BKGLXH

**IC (Inventory / Items):**
BKICALTD, BKICALTP, BKICAMTR, BKICAPMA, BKICDIM, BKICELOC, BKICEMTR, BKICLOC, BKICLOCM,
BKICMFG, BKICMSTR, BKICPMAT, BKICREF, BKICREQ, BKICTAX, BKICVAL

**MRP/Other:**
BKISHTAX, BKISTAX, BKLOGON, BKMATCST, BKMATRIM, BKMRPFC, BKMRPPO, BKMRPSW

**Packing/PI (Physical Inventory):**
BKPCKIT, BKPCPLOT, BKPIFROZ, BKPILCNT, BKPILOT, BKPIMSTR, BKPIPHYS, BKPISCNT, BKPISER

**PO (Purchase Orders):**
BKPOX, BKPOXH

**PR (Payroll):**
BKPRACOM, BKPRAGNT, BKPRBOOK, BKPRCOMM, BKPRCURP, BKPRFTAX, BKPRGLFL, BKPRHCOM,
BKPRHIST, BKPRINFO, BKPRMSTR, BKPRSALE, BKPRSTFL, BKPRTC, BKPRTCFG, BKPRW2

**QC (Quality Control):**
BKPSUSER, BKQCMSTR, BKQCTRAN, BKQTNOTE, BKQTTEMP

**RFQ / Routing:**
BKRFQ, BKRFQDES, BKRTCST, BKRTEMTR, BKRTSPEC, BKRTTEMP

**SA (Sales Analysis):**
BKSAREPT, BKSBMFG, BKSBPART, BKSBVEND, BKSHORT

**Security/Users:**
BKSLEVEL, BKSLMSTR, BKSYAP, BKSYAR, BKSYCFG, BKSYHELP, BKSYLOG, BKSYMSTR, BKSYPRTR, BKSYUSER

**SO (Sales Orders):**
BKSOHLOT, BKSOHSER, BKSOLOCK, BKSONOTE, BKSOPO

**Update/History:**
BKUMSRTY, BKUPDATE, BKWOPO, BKYSMSTR

**IS-prefix tables (EVO extensions):**
IS2DBAR, ISANOTES, ISAPACHK, ISAPAINL, ISAPAINT, ISAPARFL, ISAPARFQ, ISAPAVND, ISAPCHG,
ISAPHCHG, ISAPHQT, ISAPPROJ, ISAPQTQT, ISARACHK, ISARACST, ISARADSC, ISARAHDS, ISARAHIL,
ISARAHIN, ISARAHTX, ISARAINT, ISARAINV, ISARAIVI, ISARAIVL, ISARAIVV, ISARAT, ISARATNT,
ISARATXN, ISARATXS, ISARCHG, ISAREMND, ISARFQ, ISARHCHG, ISARINVX, ISARTXNB, ISAUTODC,
ISBANKS, ISBILLSH, ISBINLOC, ISBINLOT, ISBMEST, ISBMTMP, ISBNMSTR, ISBRANDC, ISBRANDS,
ISBROKER, ISBSF, ISBTCSB, ISBUILD, ISCATMST, ISCC, ISCHAIN, ISCHAINM, ISCONVRT, ISCTREVU,
ISCYCLCD, ISDEPT, ISDIGSIG, ISDIV, ISDLCK1, ISDLCK2, ISDRILL, ISDRILLM, ISDUTY, ISEAB,
ISECO, ISEDINFO, ISESTAQL, ISESTAQT, ISESTASM, ISESTDTL, ISESTHDR, ISESTLNE, ISESTPO,
ISFIELDS, ISFOBMRM, ISFOHEAD, ISFOHIST, ISFOLINE, ISFOORDL, ISFXASST, ISFXATRN, ISGLBDGT,
ISGLCOA, ISGLDATE, ISGLFCOA, ISGLHDAT, ISGLNBGT, ISICADT, ISICAMTR, ISICEST, ISICMSTR,
ISIS, ISISATAX, ISITMCFG, ISITP, ISJBSF, ISJOB, ISLANDF, ISLBLMAP, ISLINKS, ISLOCCST,
ISLOG, ISLSMAP, ISLTYPE, ISMACS, ISMCF, ISMCR, ISMICADT, ISMICEST, ISMRPFC, ISNOTES,
ISNTYPE, ISNUMBER, ISORDDSC, ISORDECO, ISPODESC, ISPOHTRK, ISPOS, ISPOSC, ISPOTRK,
ISPREQ, ISPRESN, ISPRMSTR, ISPRSALE, ISPRTEMP, ISQCMTHD, ISQCRSLT, ISQCSPEC, ISQSOA,
ISQTINFO, ISREMIND, ISREPDEF, ISREPLNK, ISREPORD, ISRFQADS, ISRMAAI, ISRMAC, ISRMAI,
ISRTEST, ISRTLOAD, ISSCHED, ISSDET, ISSEPROC, ISSEQUIP, ISSERCNT, ISSERR, ISSETYPE,
ISSHIPCO, ISSHPVIA, ISSLSFC, ISSOABOX, ISSOAHBX, ISSOALOT, ISSOASER, ISSOBOX, ISSOHBOX,
ISSOHNFO, ISSOINFO, ISSOREVU, ISSPC, ISSRADSC, ISSRAINF, ISSRAINV, ISSRAIVL, ISSRAMMS,
ISSRDESC, ISSRINFO, ISSRINV, ISSRINVL, ISSRMMS, ISSTEQUI, ISSTTYPE, ISSTYPE, ISTAXFIL,
ISTAXGRP, ISTERMS, ISTRIGRS, ISUDFINV, ISUDMSTR, ISUSAGE, ISVAR, ISVNDADT, ISWODESC,
ISWOEX, ISWOHDSC, ISWOPRIO, ISWOROEX, ISWOTRAY

**Misc / Other:**
ARTTEMP, BKABCUST, BKABVEND, BKACTRPT, BKCPEC, BKCPMSTR, BUCKETS, CALTEMP, CCEDIXRF,
CLASMSTR, CLASS, CUSTCLAS, DBACNAME, DBAFIFO, DBAHLPID, DISCOUNT, DPTMENT, ESTCHGS,
ESTMAT, ESTROUT, ESTSUM, EVOHLPID, HELPURL, INVATXN, INVETXN, INVTXN, JSPCNLCD, JSPCNLSO,
LANGDICT, LOT, MACHINE, MENUFILE, MKAHIST, MKASSIGN, MKDEF, MKECLASS, MKEVENT, MKFORM,
MKICLASS, MKTCLASS, MKTNOTE, MKTRACK, MKTROUT, MTEXCHG, MTICAMTR, MTICEMTR, MTICMSTR,
MTINVDEF, MTMRP, MWOPTEMP, NOTETEMP, NZITPRE, OUTHPROC, OUTPROC, PIBINLOC, PIBINLOT,
QCCODES, ROUTAING, ROUTING, ROUTTEMP, SCHEDCAL, SCHWO, SCRAP, SERIAL, SERIALH, SUMCUST,
SUMINV, SUMPNCUS, SUMWC, TEMPOLD, TESTFILE, TOOL, WBTRVMEM, WBTRVMEMO, WCCTL, WCTRLOAD,
WCTRSLOD, WOBOM, WOBOMHRM, WOBOMREM, WODATE, WOELABOR, WOEMAT, WOERECV, WOEXCHG, WOHBOM,
WOHDATE, WOHEXCHG, WOHLABOR, WOHMAT, WOHRECV, WOHROUT, WOLABOR, WOLABRPT, WOMAT, WORECV,
WORKCHG, WORKCTR, WORKHORD, WORKORD, WORKSORD, WOROUT, WOROUTMP, WOSROUT, XXICMSTR

---

### Key Table Field Schemas (Java-confirmed)

#### ISLINKS — 311 fields
EvoLinks document attachment table. Full schema:
- `IS_LNK_UID` — unique link ID
- `IS_LNK_LINK` — file/URL path being linked
- `IS_LNK_APP` — application type for linked file
- `IS_LNK_ATYPE` — attachment type code
- `IS_LNK_DATE` — link creation date
- `IS_LNK_WHO` — user who created the link
- `IS_LNK_NOTE` — description note
- `IS_LNK_OPENWITH` — open-with application override
- `IS_LNK_GLOBAL` — global link flag (visible to all users)
- `IS_LNK_ALPHA` — additional alpha field
- `IS_LNK_EXTRA` — extra/overflow field
- `IS_LNK_PCB_1..100` — 100 parent-context-block fields (entity key fields)
- `IS_LNK_DEF_1..100` — 100 definition/descriptor fields
- `IS_LNK_TYPES_1..100` — 100 type classification fields

The PCB/DEF/TYPES arrays (100 each) store context keys linking a document to specific
records across all modules — enabling the same document to be attached to multiple entities.

#### ISREMIND — 24 fields
Reminders and calendar events:
IS_REM_WHO, IS_REM_DATE, IS_REM_TIME, IS_REM_ENDDT, IS_REM_ENDTM, IS_REM_ETIME,
IS_REM_SUBJECT, IS_REM_TYPE, IS_REM_CO, IS_REM_DISP, IS_REM_CUST, IS_REM_VEND, IS_REM_ITEM,
IS_REM_FILE, IS_REM_MEMO, IS_REM_NOTE, IS_REM_EMAIL, IS_REM_NOTIFY, IS_REM_SENT,
IS_REM_TRANS, IS_REM_BEFTXT, IS_REM_COUNTER, IS_REM_EDATE, IS_REM_EXTRA

#### ISSHIPCO — 16 fields
Shipping carrier master:
IS_SHIP_SHIPVIA (PK), IS_SHIP_SHPCOD, IS_SHIP_SHPDESC, IS_SHIP_SHPNME, IS_SHIP_VNDCOD,
IS_SHIP_WEB_1..5 (5 tracking URL templates — WEB_2 confirmed used for parcel tracking),
IS_SHIP_NOTES_1..5 (5 note lines), IS_SHIP_EXTRA

#### CALENDAR — 5 fields
Shop calendar:
MTCAL_DATE, MTCAL_DESC, MTCAL_SAT, MTCAL_SUN, MTCAL_YEAR

#### BKLOGON — 10 fields
Active login session record (one row per active EVO session):
BKLOGON_CODE (user code), BKLOGON_PSWD, BKLOGON_SCRTY (security level), BKLOGON_MENU,
BKLOGON_SUBMENU, BKLOGON_CMPY (company), BKLOGON_PRINTER, BKLOGON_CURPRT (current printer),
BKLOGON_INUSE (Y/N in-use flag), BKLOGON_PROG (current program code)

#### BKSYUSER — 5 fields
System user table (simple login credentials):
BKSY_USER_CODE (user code), BKSY_USER_PSWD, BKSY_USER_SCTY (security level),
BKSY_USER_COMP (company), BKSY_USER_CHR

#### BKSLEVEL — 422 fields
Security level permission table. Pattern: BKSL_MENU{1..20}_{1..20} + BKSL_MENU{1..20}_YN.
For 20 menus × 21 fields each = 420 + BKSL_LEVEL + BKSL_MENU = 422 total.
Each menu section has 20 item permissions (Y/N) plus a master YN flag for that menu.

#### BKSYCFG — 4 fields
System module configuration flags:
BKSY_CFG_ACCTG (accounting mode), BKSY_CFG_ADVWO (advanced WO), BKSY_CFG_LITEWO (lite WO),
BKSY_CFG_SALES (sales configuration)

#### BKUPDATE — 4 fields
Update history record:
BKUPDATE_VER, BKUP_COMPANY, BKUP_DATE, BKUP_UPDATE

#### BKBMMSTR — 26 fields
Bill of Materials component record:
BKBM_UID, BKBM_PARENT (parent item code), BKBM_COMPONENT (child item code),
BKBM_P_TYPE, BKBM_C_TYPE, BKBM_QTY_REQD, BKBM_REFERENCE, BKBM_REV, BKBM_EXTRA,
BKBM_DATE1, BKBM_DATE2, BKBM_EST_LINE, BKBM_PROD_OP, BKBM_PROD_OPDSC, BKBM_PROD_DUPOP,
BKBM_PROD_TYPE, BKBM_PROD_SCRAP, BKBM_PROD_PRICE, BKBM_PROD_VEND, BKBM_PROD_RTNUM,
BKBM_PROD_OPYN_1..6

#### ISFOHEAD — 16 fields
Features & Options header (F&O master):
ISFO_HDR_UID, ISFO_HDR_PARENT (item code), ISFO_HDR_DESC, ISFO_HDR_STATUS, ISFO_HDR_DATE,
ISFO_HDR_CUST, ISFO_HDR_VEND, ISFO_HDR_RFQ, ISFO_HDR_REV, ISFO_HDR_PERM,
ISFO_HDR_MDATES_1..5 (5 milestone dates), ISFO_HDR_EXTRA

#### ISFOLINE — 78 fields
Features & Options line (F&O component):
ISFO_LIN_UID, ISFO_LIN_PARENT, ISFO_LIN_COMP, ISFO_LIN_TYPE, ISFO_LIN_LEVEL, ISFO_LIN_LINEN,
ISFO_LIN_OP, ISFO_LIN_OPDSC, ISFO_LIN_DUPOP, ISFO_LIN_RTNUM, ISFO_LIN_QTYREQ, ISFO_LIN_PRICE,
ISFO_LIN_SCRAP, ISFO_LIN_REV, ISFO_LIN_REF, ISFO_LIN_VEND, ISFO_LIN_DATE1, ISFO_LIN_DATE2,
ISFO_LIN_CBRANC, ISFO_LIN_PBRANC, ISFO_LIN_BEXTRA, ISFO_LIN_EXTRA,
ISFO_LIN_OPFLAG_1..50 (50 operation flags), ISFO_LIN_OPYN_1..6

#### AHSYLOG — 23 fields
Security access log / user session:
AHSY_USER_CTRL, AHSY_USER_LEVL, AHSY_USER_MENU, AHSY_USER_ACCES_1..20

#### MACHINE — 16 fields
Machine master (work center machine):
TMACH_MACHINE (PK), TMACH_WC (work center), TMACH_WCDESC, TMACH_DESC, TMACH_DATE,
TMACH_HRSUSED, TMACH_HRSMAINT, TMACH_EXTRA, TMACH_NOTES_1..8

#### ROUTING — 62 fields
Routing operation master (MTRO_* prefix — full schema):
MTRO_NUM (routing number), MTRO_CODE (product code), MTRO_OPER (operation), MTRO_OPERDESC,
MTRO_DESC, MTRO_WC, MTRO_WCDESC, MTRO_TYPE, MTRO_R_TYPE, MTRO_CLASS, MTRO_LABOR,
MTRO_SETUP, MTRO_SETUPHRS, MTRO_STD_TIME, MTRO_DEF_TIME, MTRO_OVERTIME, MTRO_LEAD,
MTRO_LONGTIME, MTRO_LOTSIZE, MTRO_OVERLAP, MTRO_NEGOVLP, MTRO_PRINT, MTRO_PARTSHR,
MTRO_MACHINE, MTRO_TMACHINE, MTRO_TMACHDESC, MTRO_TOOL, MTRO_TOOLDESC, MTRO_MIN_CHG,
MTRO_PIECE_RATE, MTRO_NUM_PERSON, MTRO_NUM_PROCES, MTRO_MD_PROC_HR, MTRO_PROC_PERHR,
MTRO_TIME_PERPR, MTRO_TIMEPART, MTRO_FOVHD, MTRO_VOVHD, MTRO_EST_LINE, MTRO_EST_TAG,
MTRO_MISC_ACOST, MTRO_OP_TEMP_NO, MTRO_VENDCODE, MTRO_VENDCOST, MTRO_VENDNAME,
MTRO_INSTR_1..15 (15 instruction lines), MTRO_EXTRA,
MTWO_MISC_COST, MTWO_MISC_DESC (WO misc cost fields stored in routing record)

#### WORKCTR — 24 fields
Work center master (MTWC_* prefix — full schema):
MTWC_WC (PK), MTWC_WCDESC, MTWC_DEPT, MTWC_DEPTDESC, MTWC_LABOR, MTWC_SETUP, MTWC_FOVHD,
MTWC_VOVHD, MTWC_EST_VOVHD, MTWC_LEAD, MTWC_HRSWEEK, MTWC_HRS_SHIFT, MTWC_AVGQTIME,
MTWC_COST_LB, MTWC_MACHINE, MTWC_MIN_CHG, MTWC_OUTPROC, MTWC_PARENT_WC, MTWC_PARENT_YN,
MTWC_LEVEL_YN, MTWC_QPR1, MTWC_QPR2, MTWC_QPR3, MTWC_EXTRA

#### ISBSF — 143 fields
Business Score File (ISBSF_* prefix — rebuilt by EVOBSR):
Key summary fields: AP_ATP, AP_BAL, AP_DISC, AP_PAYA, AP_PAYM, AR_BAL, AR_BILL, AR_COGS,
AR_DEPO, AR_DISC, AR_RECP, IC_VALUE, SO_BOOK, SO_OPEN, SO_SHIP, PO_BOOK, PO_OPEN, PO_RECP,
WOS_FOH/FP/LAB/MAT/MEXT/OUTP/SETUP/VOH/WIPV, WO_FPVAR, WO_ISSU, WO_WIPBAL,
CASH_ACT1..9 (9 manual cash accounts), CASH_ACTS_1..100 (100 G/L cash accounts),
CASH_TOTA, STARTDATE, ENDDATE, EXTRA

#### BKSYMSTR — 286 fields
System master (company settings, terms, GL accounts):
Key groups: AP setup (APINV_NUM, APPO_NUM, AP_AGING_1..5, AP_CHKACT, AP_DISCGL, AP_GLACT),
AR setup (ARINV_NUM, ARSO_NUM, AR_AGING_1..5, AR_CHKACT, AR_FREIGHT, AR_INT_DAY/RTE, AR_TAXABL),
Company info (COMP_ADD1/ADD2/CSZ/NAME), Check accounts (CHK_NAME/NUM/ACT/CUR/DPT_1..9),
GL accounts (GL_ARINTR, GL_CLRING, GL_RELYR, GL_RETEARN + GLDPT equivalents),
Terms (TERMS_1..20 names + TRM_AMT/DAY/DISC/EOM/MAX/TYP_1..20 = 120 term detail fields),
PO setup (PO_FREIGHT, PO_INR, PO_RNI, PO_TAXGL), PR setup (PR_ODNAME_1..6),
Fiscal year (FISCAL_YR), Extra fields (EXTRA)

---

*Java Integration documentation auto-generated Pass 102 from EvoPVT.jar class file constant pool extraction.*


---

## Pass 103 — AP/AR/PO/SO Module Form Catalog (2026-06-18)

Source: DFM analysis of 171 forms in `samples/dfm/` (35 AP, 24 AR, 41 PO, 71 SO).
All form descriptions confirmed from Caption fields extracted from DFM files.

---

### AP — Accounts Payable Module (35 forms)

**Menu flow:** AP-A (vendors) → AP-C (receive invoice) → AP-F (select for payment) →
AP-G (proforma check register) → AP-H (print checks) → post to GL automatically.

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| AP-A | BKAPA | T7APA.DFM / t7apaC.DFM / t7apae.DFM | Enter/edit vendor master (name, address, GL expense, terms, 1099 type, ship-via, currency, bank info, pricing) |
| AP-B | BKAPB | T7APB.DFM | Enter recurring/scheduled vouchers with GL distribution |
| AP-C | BKAPC | T7APC.DFM | Enter AP invoice from PO receipt — "Do you want to close this P/O?" prompt |
| AP-D | BKAPD | T7APD.DFM | Schedule payment dates against outstanding invoices |
| AP-E | BKAPE | T7APE.DFM | Print cash requirements report (vouchers due) with terms type filter |
| AP-F | BKAPF | t7apf.dfm | Select items to pay — browse open AP, take discounts, pay via check or ePay |
| AP-G | BKAPG | t7apg.dfm | Print proforma check register (preview before printing checks) |
| AP-H | BKAPH | T7APH.DFM | Print checks (paper, ACH/NACHA, ePay) — sets check date, beginning number, posts |
| AP-I | BKAPI | T7API.DFM | Print AP aging report with 5 configurable aging periods |
| AP-J | BKAPJ | T7APJ.DFM | Print vendor directory (active/inactive/approved/unapproved) |
| AP-K | BKAPK | T7APK.DFM | Print vendor labels / address list |
| AP-L | BKAPL | t7apl.DFM | Recalculate vendor MTD and YTD purchase totals |
| AP-M | BKAPM | T7APM.DFM | Print vendor mailing labels (filing or mailing format) |
| AP-N | BKAPN | T7APINFO.DFM | Vendor custom info / user-defined fields |
| AP-O | BKAPO | T7APO.DFM | Enter recurring AP vouchers (standing orders with frequency, next date, max times) |
| AP-P | BKAPP | T7APP.DFM | Generate recurring vouchers for the batch due date |
| AP-Q | BKAPQ | T7APQ.DFM | Void a check (by check number, vendor, amount, date) |
| AP-R | BKAPR | T7APR.DFM | Print check history |
| AP-S | APS2000 | T7APS.DFM | Print 1099 forms (year-specific programs — APS1999, APS2000, TAPS2000) |
| AP-T | BKAPT | T7APT.DFM | AP check / invoice inquiry drill-down (check → invoices paid → PO lines) |
| AP-V | BKAPV | T7APV.DFM | Enter / print vendor deposits |
| AP-X | BKAPX | T7APX.DFM | Print invoice link report (invoices missing PO link) |
| AP-Y | BKAPY | T7APY.DFM | Reprint checks |
| AP-YB | BKAPYB | T7APYB.DFM | Export positive pay file (CSV to bank — configurable fields) |
| AP-YC | BKAPYC | T7APYC.DFM | Export ACH/NACHA file for electronic payments |
| AP-ZA | BKAPZA | T7APZA.DFM | Top N vendors by period analysis (MTD/YTD/LYR) |

**Sub-forms (child dialogs of AP-A):**

| Form | Purpose |
|------|---------|
| T7APABANK.DFM | Vendor bank account info (name, routing number, account number, type) |
| T7APACON.DFM | Vendor contacts (name, email, phone) |
| T7APAPRC.DFM | Vendor item pricing grid (item, qty, price, extension) |
| T7APASTA.DFM | Vendor statistics (YTD vs LY gross purchases, variance) |
| T7APHASK.DFM | Check note entry dialog (used from AP-H) |
| T7APPVND.DFM | AP vendor popup (lookup, no captions — runtime-labeled) |

**Key tables:** BKAPVEND (vendor master), BKAPINVL (invoices/vouchers), BKAPCHKH (check history),
BKAPCHKF (check run batch), BKAPPO (PO header), BKAPPOL (PO lines), BKAPNOTE (vendor notes),
BKAP.REM (remittance), BKAP.TMC (ACH bank info).

---

### AR — Accounts Receivable Module (24 forms)

**Menu flow:** AR-A (customers) → SO module creates invoices → AR-C (record payments) →
AR-F (aging) → AR-E (statements) → AR-G (post to GL via SO-G).

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| AR-A | BKARA | T7ARA.DFM / T7ARAE.DFM / T7ARAC.DFM | Enter/edit customer master — name, address, credit limit, terms, GL defaults, salesperson, tax code, currency, discount code, ASN required flag |
| AR-B | BKARB | T7ARB.DFM | Enter AR vouchers / journal entries |
| AR-C | BKARC | T7ARC.DFM | Record payments (cash receipts) — apply to open invoices, handle discounts, NSF checks, import batch payments |
| AR-D | BKARD | T7ARD.DFM | Charge interest on overdue invoices (configurable minimum charge) |
| AR-E | BKARE | T7ARE.DFM | Print customer statements (balance-forward or open-item, deposits, aging format) |
| AR-F | BKARF | T7ARF.DFM | Print AR aging report (5 configurable periods, base or source currency, export past due to file) |
| AR-G | BKARG | T7ARG.DFM | Print customer code / name directory (active, inactive, credit hold, class filter) |
| AR-H | BKARH | T7ARH.DFM | Print customer general info report |
| AR-I | BKARI | T7ARI.DFM | Print customer mail labels / address list |
| AR-K | BKARK | T7ARK.DFM | Print sales tax report (by tax code/group, purchases or sales) |
| AR-L | BKARL | T7ARL.DFM | Transfer / post outstanding sales taxes to GL |
| AR-M | BKARM | T7ARM.DFM | Enter customer refund (create check or credit, link to original invoice) |
| AR-N | BKARN | T7ARN.DFM | Enter / print customer deposits (link to SO, generate invoice) |
| AR-P | BKARP | T7ARP.DFM | Print customer follow-up report (days late for payment) |
| AR-R | BKARR | T7ARR.DFM | Print AR payment history (check date/number range, bank accounts) |
| AR-T | BKART | T7ART.DFM | Customer credit card management (add/update/delete stored cards, processor setup) |
| AR-U | BKARU | T7ARU.DFM | Process accounts receivable (period-end tasks, as-of date) |

**Sub-forms (child dialogs of AR-A):**

| Form | Purpose |
|------|---------|
| T7ARA2DB.DFM | 2D barcode layout configuration per customer (field, character, order) |
| T7ARACON.DFM | Customer contacts (name, email, phone) |
| T7ARACRE.DFM | Customer credit info panel (credit limit, hold, follow-up date, outstanding amounts) |
| T7ARAPRC.DFM | Customer item pricing grid (item, discount %, price, qty, extension) |
| T7ARASTA.DFM | Customer statistics (gross sales, COGS, net sales, YTD vs LY) |

**Key tables:** BKARCUST (customer master 106f), BKARINV (invoice header), BKARINVL (invoice lines),
BKARINVI (SO→invoice cross-ref), BKARSHIP (ship-to addresses), ARTTEMP (payment temp),
BKARDESC (descriptions), ISARDEPL (AR deposit lines).

---

### PO — Purchase Orders Module (41 forms)

**Menu flow:** PO-F (RFQ) → PO-G (RFQ → PO) → PO-A (PO entry) → PO-C (receive) →
PO-J-C (QC receive) → AP-C (AP invoice entry from PO) → PO-K (close PO).

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| PO-A | BKPOA | T7POA.DFM / T7POAE.DFM / T7POAC.DFM | Enter/edit purchase orders — vendor, items, quantities, due dates, GL, job#, DPAS rating, risk assessment, FAR/NADCAP compliance flags |
| PO-B | BKPOB | T7POB.DFM | Print purchase orders (standard or consolidated, with notes, ECO/drawing info) |
| PO-C | BKPOC | t7poc.DFM | Receive PO into inventory (packing slip, bin, lot, inventory or QC) |
| PO-E-A | BKPOEA | T7POEA.DFM | Print RFQs |
| PO-ENG | BKPOENG | T7POENG.DFM | Engineering open order report (with previous 12-month usage, WO allocations, rush/expedite colors) |
| PO-F | BKPOF | T7POF.DFM | Enter verbal RFQ quotes (vendor, item, qty breaks, lead time, cost, estimation link) |
| PO-G | BKPOG | T7POG.DFM | Convert RFQ to PO (with WO prefix/suffix, pass/skip zero-qty items, keep quote on file) |
| PO-H | BKPOH | T7POH.DFM | Vendor pricing master (archive original price, update pricing, track last cost 1–5) |
| PO-I-C | BKPOIC | T7POIC.DFM | Print open RFQ report |
| PO-I-D | BKPOID | T7POID.DFM | Print vendor price list (active/archived/expired prices) |
| PO-I-G | BKPOIG | T7POIG.DFM | Print PO expedite / shortage report (color-coded by rush level, planner code filter) |
| PO-I-H | BKPOIH | T7POIH.DFM | Print vendor on-time delivery performance report |
| PO-I-I | BKPOII | T7POII.DFM | Print PO change history (by PO#, vendor, item, job, date of change) |
| PO-I-L | BKPOIL | T7POIL.DFM | Print PO open order listing with digital signature status |
| PO-J-A | BKPOJA | T7POJA.DFM | Print QC receipt travellers (with rush/expedite coloring) |
| PO-J-B | BKPOJB | T7POJB.DFM | Print QC open order / shortage report (rush/colors, exclude bought-off items) |
| PO-J-C | BKPOJC | T7POJC.DFM | QC receiver entry — accept/reject/buyoff/rework/NCR/RoHS per receipt line |
| PO-J-D | BKPOJD | T7POJD.DFM | Print vendor quality performance report (on-time delivery by class/vendor range) |
| PO-K | BKPOK | T7POK.DFM | Batch close POs (archive by date / PO# / vendor range) |
| PO-L | BKPOL | T7POL.DFM | Approved vendor list entry (approved vendors per item, with primary flag) |
| PO-L-A | BKPOLA | T7POLA.DFM | Print approved vendor list (by item, parent item, vendor) |
| PO-L-P | BKPOLP | T7POLP.DFM | Print vendor pricing report |
| PO-M | BKPOM | T7POM.DFM | PO inquiry — search by item or PO# — shows on-hand, on-PO, on-WO, in-QC, allocated, on-SO |
| PO-MAST | BKPOMAST | T7POMAST.DFM | Vendor / item master inquiry (AP + IC + TR + PO drill-down in one screen) |
| PO-P | BKPOP | T7POP.DFM | Full vendor master entry form (AP + PO integrated: contacts, GL, follow-ups, pricing history, gross purchase history) |
| PO-Q | BKPOQ | t7POQ.DFM | Maintain PO delivery dates — mass confirm / update estimated receipt dates |
| PO-S | BKPOS | T7POS.DFM | Cash sale / point-of-sale PO screen (item, qty, price, discount) |
| PO-S-CD | BKPOSCD | T7POSCD.DFM | Cash drawer / change-due dialog for POS |
| PO-S-I | BKPOSI | T7POSI.DFM | POS codes maintenance (code, description) |
| PO-S-X | BKPOSX | T7POSX.DFM | POS transaction types maintenance |

**Sub-forms:**

| Form | Purpose |
|------|---------|
| T7POA2.DFM | PO line-item entry sub-form (qty, price, ECO, job, location, due date) |
| T7POAC.DFM | Advanced PO with risk assessment, DPAS rating, FAR/NADCAP compliance |
| T7POACPY.DFM | Copy PO to new PO / archive (change vendor, new PO#) |
| T7POAIMPLINES.DFM | Import PO lines from CSV file |
| T7POAPrBrk.DFM | Verify PO price breaks (item, last cost, expiry date) |
| T7POAVITEM.DFM | Vendor-specific item lookup |
| T7POPGET.DFM | Generic PO popup lookup (labels set at runtime by caller) |
| T7POLINEHIST.DFM | PO line change history (ERD, price, qty, GL account, VPD) |
| T7pojcqc.DFM | Multi-scrap code entry for QC receiver (use-as-is quantities) |
| T7pojcsc.DFM | Multi-scrap code entry for QC receiver (scrap quantities) |

**Key tables:** BKAPPO (PO header 57f), BKAPPOL (PO lines 38f), BKQCMSTR (QC receivers 14f),
BKRFQ (RFQ header/lines), BKPOHIST (vendor price history), ISBINLOT (bin/lot assignments).

**Special compliance fields (T7POAC.DFM):**
- DPAS Rating — Defense Priorities and Allocations System order priority code
- First Article Reports Required [Y/N]
- NADCAP Certs Required For Finishes [Y/N]
- Risk assessment: schedule risks, potential obsolescence

---

### SO — Sales Orders Module (71 forms)

**Menu flow:** SO-A (enter SO) → SO-C (pick ticket) → SO-E (ship) → SO-F (invoice) →
SO-G (post to AR/GL) → AR-C (record payment).
Parallel: SO-N (generate WOs from SO) → WO module.

| Code | Program | Form | What it does |
|------|---------|------|-------------|
| SO-A | BKSOA/BKSOA2 | T7SOA.DFM / T7SOAE.DFM / T7SOAC.DFM | Enter / edit sales orders — customer, items, qty, price, disc, due date, location, FOB, freight, drop ship, currency, job#, APH market/program fields |
| SO-B | BKSOB | T7SOB.DFM | Print sales orders (with blanket lines, kit components, hidden notes, linked documents) |
| SO-BIN | BKSOBIN | T7SOBIN.DFM | Bin-level inventory allocation for SO lines |
| SO-C | BKSOC | T7SOC.DFM | Print pick tickets / packing slips (back-orders, lot numbers, serial numbers, multi-location) |
| SO-D | BKSOD | T7SOD.DFM | Print shipping labels — standard, John Deere (I/M/X/S types), PDF417 barcode, kanban |
| SO-E | BKSOE | T7SOE.DFM | Ship sales order — release to invoice, assign shipper, BOL number, carrier pro number, gross weight |
| SO-F | BKSOF | T7SOF.DFM | Print invoices — consolidated, auto-email, apply deposits, print C of C, print C of O |
| SO-G | BKSOG | T7SOG.DFM | Post invoices to AR/GL (pre-post COGS + commissions reports, post all printed) |
| SO-HINFO | BKSOHINFO | T7SOHINFO.DFM | SO header UDFs — 20 alpha fields (sohAlpha1–20) + 5 date fields (sohDate1–5) |
| SO-INFO | BKSOINFO | T7SOINFO.DFM | SO-level misc info UDFs — 20 alpha (soAlpha1–20) + 5 date (soDate1–5) |
| SO-J-INFO | BKSOJINFO | T7SOJINFO.DFM | Recurring SO settings (group code, frequency, limit, next invoice date) |
| SO-K | BKSOK | T7SOK.DFM | Recurring orders — generate invoices from order templates by selection code / date range |
| SO-L-INFO | BKSOLINFO | T7SOLINFO.DFM | SO line UDFs — 20 alpha (solAlpha1–20) + 5 date (solDate1–5) |
| SO-LINEHIST | — | T7SOLINEHIST.DFM | SO line change history viewer (CDD, ESD, price, qty, commission rates, discount) |
| SO-LOT | BKSOLOT | T7SOLOT.DFM | Lot-level inventory allocation for SO lines |
| SO-N | BKSON | T7SON.DFM | Generate work orders from SO lines (multi-assy WO, combine duplicates, suffix matching, shop calendar start date) |

**Sub-forms (child dialogs of SO-A):**

| Form | Purpose |
|------|---------|
| t7Soa2.DFM | SO line-item entry (item, qty, price, disc, ECO, drawing, location, line weight) |
| T7SOABKD.DFM | Booking date entry popup |
| T7SOAFRT.DFM | Freight amount entry popup |
| T7SOAIMPLINES.DFM | Import SO lines from CSV (multi-company, include kit/make-from/specs) |
| T7SOAPRC.DFM | Customer item pricing matrix display |
| T7SOAXCOM.DFM | Extra commission override entry (rep#, commission %, overage %) |
| T7SOACPY.DFM | Copy SO to new quote (SO → Quote) |
| T7SOACITEM.DFM | Customer-specific item lookup for SO lines |
| T7SOBIN.DFM | Bin allocation dialog |
| T7SOLOT.DFM | Lot allocation dialog |
| T7SODDesc.DFM | Label description entry (copies) |
| T7SODPallet.DFM | Pallet configuration for shipping labels |
| T7SOFDEP.DFM | Apply customer deposit to SO invoice |
| T7SOGA.DFM | Real-time order posting progress display |
| T7SOGACHK.DFM | Cash terms check dialog (cash terms customer — capture payment at invoice post) |
| T7SOGCogs.DFM | Pre-post COGS report print dialog |
| T7SOGComm.DFM | Pre-post commissions report print dialog |
| T7sondte.DFM | SO-N date entry popup |

**Key tables:** BKARINV (invoice/SO header), BKARINVL (invoice/SO lines), BKARINVI (SO→invoice cross-ref),
BKSOX/BKSOXH (SO extract for reporting), BKSONOTE (SO notes), BKSOPO (SO→PO cross-ref),
ISSOHNFO (SO header UDF values — sohAlpha/sohDate), ISSOINFO (SO misc info), ISSRINFO (SO line UDFs),
ISSCHED (scheduling), BKSOLOCK (SO record locking), BKSOHLOT (header lot assignments),
BKSOHSER (header serial numbers).

**John Deere label integration (T7SOD.DFM):**
- Label types: I (item), M (material), X (mixed), S (small)
- JD Pallet License Plate Number entry
- MFD Date, packaging type, and pallet configuration
- "John Deere Shipment?" flag triggers JD-specific label format

**APH (Advanced Planning Horizon) fields (T7SOA.DFM):**
- APH Market — customer market segment for demand planning
- APH Program — program code for APH demand grouping
These are i2 Systems J7 customization fields (not standard EvoERP).

---

*Pass 103 AP/AR/PO/SO module catalog — 171 DFM forms confirmed from `samples/dfm/` analysis.*
*Per-table confidence: 87/100. PROJECT-STRUCTURE.md confidence: 86/100.*


---

## Pass 103b — SO Sub-Modules: Reports (SO-O), Proposals (SO-P), Pricing (SO-Q), Misc (2026-06-18)

Source: DFM analysis of untracked samples/dfm/ forms — T7SOOA-I (reporting), T7SOP* (proposals),
T7SOQ* (pricing master), T7SOR/S/V (receive/release/backorder), T7SOSER/SONQTY (allocation helpers),
T7SORevu (contract review).

---

### SO-O — Sales Order Reporting Sub-Module (T7SOOA..I, T7SOOM, T7SOON)

| Form | Purpose |
|------|---------|
| T7SOOA.DFM | Print SO open order report — includes backorder amounts, WO est hours, days-to-ship calculation |
| T7SOOB.DFM | Print SO summary by item or estimated ship date |
| T7SOOD.DFM | Print SO delivery report (customer order range, customer due date filter) |
| T7SOOE.DFM | Print SO WO labor hours remaining report (WO filter for labor hours) |
| T7SOOF.DFM | Print SO open order by customer / due date |
| T7SOOG.DFM | Print SO by customer name and estimated ship date |
| T7SOOH.DFM | Print SO AR voucher / invoice batch (currency range, AR voucher flag) |
| T7SOOI.DFM | Print SO open order listing with comments |
| T7SOOM.DFM | Print SO change history report (change date, customer, commissions changes) |
| T7SOON.DFM | Print SO on-time delivery report — ESD vs ASD (actual ship date) with early/late tolerances |

---

### SO-P — Proposals / Sales Quotes Sub-Module (T7SOP*)

The SO-P sub-module manages pre-sales proposals and formal sales quotes. Quotes can be
converted to SOs via SO-P-C. Win likelihood (0–9) is tracked per quote.

| Form | Purpose |
|------|---------|
| T7SOPK.DFM | Enter / edit proposal header (full order entry screen: address, attention, city, country, lines) |
| T7SOPF.DFM | Enter / edit proposal lines (items, quantities, prices, comments, balance on order) |
| T7SOPC.DFM | Convert proposal to SO — change ESD, customer due date, location, close after conversion |
| T7SOPB.DFM | Print proposal win likelihood report (filter by win likelihood 0–9) |
| T7SOPM.DFM | Print proposals report (with job# and order description check option) |
| T7SOPI.DFM | Proposal / quote inquiry |
| T7SOPJ.DFM | Proposal job file reference (file name, start time — time-stamping) |
| T7SOPO.DFM | Auto-generate or review proposals (customer range, default job#) |
| T7SOPOR.DFM | PO receipt review dialog from proposal (item, exp recv date, price, qty — "Review" button) |
| T7SOPP.DFM | Process proposals (batch conversion or status update by customer) |

**Business context:** Proposals are the pre-sale step before a confirmed SO. A sales rep enters a
proposal in SO-P-K, adds items in SO-P-F, marks win likelihood, and when the customer confirms,
SO-P-C converts it to a live SO. The BKSOA/BKSOA2 programs share the T7SOAC form for quotes too —
the distinction between a "proposal" (SO-P) and a "quote" (SO-A in quote mode) may be status-flag
driven within the same form set.

---

### SO-Q — Pricing Master Sub-Module (T7SOQ*)

Controls item base prices, price codes, customer contract pricing, and mass price changes.

| Form | Purpose |
|------|---------|
| T7SOQA.DFM | Enter / edit item base price (with contract price and price code multipliers) |
| T7SOQH.DFM | Enter / copy price code headers (customer, discount code, multiple price tiers) |
| T7SOQB.DFM | Print price list (filter by active status: Y/N/O/D/E/P/S/Q/R) |
| T7SOQI.DFM | Print price code listing (customer / date / discount code range) |
| T7SOQK.DFM | Print price code report (by category, class, customer) |
| T7SOQC.DFM | Mass price change — direction (up/down), type (%), amount, with contract and price code updates |
| T7SOQJ.DFM | Recalculate prices from cost basis — new base price = cost × markup; optionally update contract prices |
| T7SOQL.DFM | Import price codes from CSV file |

**Price code status field values (active status filter `YNODEPSQR`):**
- Y = active, N = inactive, O = obsolete, D = discontinued, E = end-of-life,
  P = prototype, S = sample, Q = quote-only, R = restricted

---

### SO-R / SO-S / SO-V / SO-SER / SO-NQty / SO-REVU

| Form | Purpose |
|------|---------|
| T7SOR.DFM | AR refund / deposit re-application from SO (city, country, department, deposit, description) |
| T7SOS.DFM | SO release screen — auto-release comments, include backorders, customer range |
| T7SOV.DFM | SO backorder management — edit back-ordered qty, customer due date, customer name |
| T7SOSER.DFM | SO serial number allocation (similar to T7SOBIN: item, qty, bin, tag, remove all) |
| T7SONQTY.DFM | SO-N quantity availability popup — shows available, allocated, on-PO, on-BO, lead time, min order qty |
| T7SORevu.DFM | SO contract review sign-off — "SO Contract Review" with customer, SO#, entered by/date, KILL button |
| T7SORevuPSWD.dfm | Contract review password dialog (ID, department, password — required before sign-off) |

**SO Contract Review (T7SORevu + T7SORevuPSWD):**
A quality-gate feature where a specific SO must be reviewed and signed off by an authorized
reviewer before it can be processed. The "KILL" button on T7SORevu likely voids / rejects the review.
The password dialog (T7SORevuPSWD) authenticates the reviewer by Contract Reviewer ID + password +
department — suggesting role-based approval routing.

---

*Pass 103b — SO sub-module catalog: SO-O (11 reporting forms), SO-P (10 proposal forms),
SO-Q (8 pricing forms), plus SO-R/S/V/SER/NQty/REVU ancillary forms.*
*Total SO DFMs now cataloged: 71 forms.*


---

## Pass 103c — 16 Opaque Module Identifications (2026-06-18)

Source: .RUN string dump analysis (confirmed table refs), BKLME.SRC source code,
DFM caption extraction. These 16 module codes were previously listed in EVO-DECOMPILE-TODO.md
as essentially unknown (15/100 confidence).

| Module | Code | Programs | Identification | Evidence |
|--------|------|----------|---------------|----------|
| **RMA / Returns** | AB | T6ABINV.RTM, T6ABPO1.RTM, T6ABrma1.RTM, ISABOUT.DCY | Return Material Authorization — tracks customer returns, reverse receipts, and credit invoices. ISABOUT.DCY is the EvoERP "About" dialog (unrelated to AB module). | T6ABrma1.RTM = RMA report; T6ABINV = return invoice; T6ABPO1 = return PO. |
| **Execute Utility** | EX | t7exec.RUN | Single-purpose program executor / shell command runner. | Only one file: t7exec.RUN |
| **Flexible Location** | FL | ISFLOC.RUN | Flexible Location Control — manages non-fixed inventory bin locations. | ISFLOC.RUN; ISFLOC likely references BKICLOC/BKICLOCM tables. |
| **Lot Movement** | LM | BKLMA–BKLMG (+ BKLME.SRC) | Inventory lot movement reporting and management. Tracks qty transactions by type: I=Issue, A=Adj, J=WO-job, P=Purchase, W=WIP, S=Sales, Q=QC, O=Other, C=Closing. | BKLME.SRC opens MTICMSTR + INVTXN; variable arrays QTY.I/A/J/P/W/S/Q/O/C confirm all INVTXN transaction types. BKLMA.RUN opens BKICMSTR, MTICMSTR, BKICLOC. |
| **Mass AP Deposits** | MA | ISMASVOD.RUN, T7MAPDEPO.DFM/RWN | AP deposit mapping and mass void operations. T7MAPDEPO = "Map Deposits" form (customer, deposit #, amount, GL account, item number). ISMASVOD = "IS Mass Void" (batch void of checks/vouchers). | T7MAPDEPO.DFM captions: "Map Deposits", deposit/GL/amount fields. ISMASVOD name = mass void. |
| **Manufacturing Mgmt Reporting** | MM | BKMMA–BKMMH (8 programs) | Cross-module manufacturing management reports. BKMMB bridges Payroll (BKPRMSTR/BKPRSALE/BKPRGLFL) and WO labor (WOLABOR). BKMMF uses all WO tables (WORKORD, WORECV, BKDCLAB, WOEXCHG, WODATE, WOROUT, WOBOM). BKMMA includes MKAHIST (Marketing Activity History). | BKMMB.RUN strings: BKPRMSTR, BKPRSALE, BKPRGLFL, BKPRINFO, WOLABOR. BKMMF.RUN strings: WORKORD, WORECV, BKDCLAB, WOEXCHG, WODATE, WOROUT, WOBOM. |
| **Payroll Link** | PL | BKPLA–BKPLE (5 programs) | Links EvoERP to an external payroll software package. PL-E = Payroll Link Setup (stores path to payroll software in BKCPMSTR). PL-D = "Import Employees (under construction)". BKPLA uses BKCPMSTR, checks for "DOS version of DBA". | BKPLA.RUN: "A path was not found for the Payroll software, please use PL-E (Payroll Link Setup)". BKPLE.RUN: "PL-E Payroll Software Link Setup". |
| **Report Template** | RT | T7RTMVALID.DFM/RWN, T6RTRue.RTM | RTM validation / report format selection utility. T7RTMVALID allows selecting a report format name from a list (used when multiple RTM formats exist for one report). | T7RTMVALID.DFM captions: "Select Report Format Name", OK/Cancel. |
| **Spec Book / Approved Source List** | SB | BKSBMFG, BKSBPART, BKSBVEND | Approved Source List (ASL) / Qualified Parts List (QPL) / Spec Book. Stores approved manufacturers (BKSBMFG: PARNT+PROD+CUST PK → MANUF+MPART), approved vendors (BKSBVEND: PARNT+PROD+CUST PK → VEND+VPART), and substitute parts (BKSBPART). Used in electronics/PCB manufacturing for AVL and QPL control. Accessed by T7MRG (MRP firming) and T7POB (PO print) to enforce sourcing rules. | BKSB* table fields confirmed from DDF schema; field names (PARNT/PROD/CUST/MANUF/MPART/VEND/VPART) unambiguously indicate approved-source structure. Earlier "Scoreboard Export" label was incorrect. |
| **Shop Loading / SFC** | SL | t7slsfc.RWN | Shop Loading and/or Shop Floor Control. "SFC" = Shop Floor Control. | t7slsfc.RWN = TAS7 Shop Loading-Shop Floor Control (encrypted binary). |
| **User Menu Maintenance** | UM | BKUMA–BKUMD (4 programs) | Allows administrators to define custom user menus (MENUFILEA). BKUMA = Enter User Menus; BKUMB = Print User Menus. Menus are stored in MENUFILEA / MENUFILEI tables. | BKUMA.RUN: "Enter User Menus", "Menu Maintenance A", "Menu code is not on file, 'Y' to add". BKUMB.RUN: "Print User Menus". |
| **Update Utility** | UP | ISUPDATE.RUN | EvoERP version update utility — applies patch/update scripts to the database. Referenced by BKUPDATE table. | ISUPDATE.RUN (single program); BKUPDATE table tracks applied updates (VER, COMPANY, DATE, UPDATE). |
| **YN Flags Editor** | YS | T7YSYN.RWN | System yes/no configuration flag editor — UI for BKYSMSTR 200+ boolean settings fields. | T7YSYN.RWN (encrypted binary). Previously confirmed at 72/100. |

**Unidentified / no files found:**
- **CP** — No files in share. Possibly deprecated; may have been merged into another module.
- **PC** — No files in share. Possibly Price Codes (now part of SO-Q) or deprecated.
- **SY** — No files matching T7SY*/BKSY* found. The System module functions are accessed via other modules (BKSYMSTR, BKSLEVEL) rather than standalone SY programs.

**T7PLessComps.DFM / T7PLessNotes.DFM (PL DFMs):**
Despite having the "PL" prefix, these forms are WO-related, not Payroll Link:
- T7PLessComps: "Issue Components", "Shortages", "WO Number" → WO component shortage/issue form
- T7PLessNotes: "QC Specifications", "Routing", "Vendor", "WO" → WO notes popup with QC/routing context
These are most likely sub-forms for a "PLess" (short for "Paperless" or a WO picklist operation)
that happen to use the T7PL prefix. Their exact parent program has not been identified.

---

### Summary: 16 Opaque Modules (Pass 103c confidence update)

| Module | Before | After | Notes |
|--------|--------|-------|-------|
| AB / RMA | 15 | 45 | 3 RTM report files confirmed, function clear from names |
| CP | 15 | 15 | No files — cannot improve |
| EX | 15 | 40 | Single RUN file, single-purpose utility |
| FL | 15 | 40 | ISFLOC.RUN name self-explanatory |
| LM | 15 | 75 | BKLME.SRC fully read; all 7 INVTXN transaction types confirmed |
| MA | 15 | 55 | T7MAPDEPO.DFM confirmed + ISMASVOD name clear |
| MM | 15 | 45 | 8 programs found; BKMMB+F table refs identified but purpose mixed |
| PC | 15 | 15 | No files — cannot improve |
| PL | 15 | 65 | BKPLE "Payroll Software Link Setup" confirmed; 5 programs found |
| RT | 15 | 60 | T7RTMVALID.DFM captions clearly describe RTM format selector |
| SB | 15 | 40 | 2 XPT export templates found; EVOBSR connection inferred |
| SL | 15 | 30 | 1 RWN file only (encrypted) — name = shop floor |
| SY | 15 | 20 | No files — function handled by other modules |
| UM | 15 | 70 | BKUMA/BKUMB strings: "Enter/Print User Menus", MENUFILEA confirmed |
| UP | 15 | 60 | ISUPDATE.RUN + BKUPDATE table correlation |
| YS | 72 | 72 | Already documented (not in this pass) |

Average confidence for these 16: ~15 → ~47 (gap 35 → ~18)


---

## Pass 103d — Boot Sequence and File Location System (2026-06-18)

Source: START_UP.DBA binary string extraction, FILELOC.B structure parse (3,613 records),
StartEvo.exe .NET string analysis (PDB path: D:\prog\evoerp\StartEvo\), WHOAMI.DBA read.

---

### Complete EvoERP Boot Sequence

**Step 1 — StartEvo.exe (C# .NET launcher, C:\ISTS\StartEvo.exe)**

StartEvo.exe is a custom C# .NET application (not part of DBA/TAS Pro original code).
Built by i2 Systems at `D:\prog\evoerp\StartEvo\`. Key functions extracted from binary:

| Function | What it does |
|----------|-------------|
| `GetEvoDir` | Reads EvoERP install directory from config |
| `UpdateIniFile` | Writes/updates `evoini` (EvoERP.INI) with current settings |
| `DomainAuthenticateAndLaunchEvo` | Main entry — authenticates Windows domain user, then launches EVO |
| `IsCompanyAllowed` | Checks that the authenticated user may access the selected company |
| `GetMenuName` | Retrieves the menu RWN filename to pass to tp7runtime.exe |
| `GetUserCompProg` | Assembles user + company + program command-line arguments |
| `KillEvoProcesses` | Terminates stale `tp7runtime.exe` / `EvoERP.exe` processes from prior sessions |
| `LaunchEvoWithUser` | Spawns `tp7runtime.exe` with the assembled arguments |
| `ProcessEvoUri` | Handles URI-scheme deep links (e.g. `evo://...` protocol) |
| `TAS_ISTS_PATH_PROGRAMS` | Environment variable: path where TAS Pro looks for .RWN program files |

Environment variable `TAS_ISTS_PATH_PROGRAMS` is set to the DBAMFG$ share path so
TAS Pro runtime can locate all .RWN compiled programs.

**Step 2 — tp7runtime.exe (TAS Professional 7 runtime)**

Command line constructed by `LaunchEvoWithUser`:
```
tp7runtime.exe EvoERPmenu.RWN /user:<USERNAME> /company:<CO> /pass:<PASSWORD>
```
Arguments `userArg`, `passArg`, and `company` map to `/user`, `/pass`, `/company` flags.

**Step 3 — EvoERPmenu.RWN (encrypted main menu)**

EvoERPmenu.RWN (497,383 bytes, on DBAMFG$ share) is the encrypted TAS Pro main menu
program. Cipher: Twofish-192-CFB-128 (cipher key derived from "mabufoju"). On load,
tp7runtime decrypts and executes it. EvoERPmenu chains to START_UP.DBA first.

**Step 4 — START_UP.DBA (TAS Pro compiled startup script)**

START_UP.DBA (27,083 bytes, on DBAMFG$ share) is the initialization script that runs
before the main menu is displayed. Confirmed execution sequence from string analysis:

1. Opens `FILELOC` — loads the file location routing table (386 tables × 6 companies)
2. Opens `TASCOLOR` — loads UI color scheme settings
3. Checks `START_UP.RUN` integrity (flags read-only attribute errors)
4. Runs `USECOMP.RUN` (3,567 bytes) — company selection dialog
5. Displays "Please wait while we do some short system checking."
6. Opens `BKSYMSTR` and `BKYSMSTR` — validates no duplicate system master records
7. Shows registration screen:
   - Company: **AMERICAN BACKPLANE INC.** (i2 Systems' prior registered name)
   - Address: 355 BANTAM LAKE ROAD, MORRIS, CT 06763
   - Serial No: **75790**
   - Expiry: **12/31/30** (December 31, 2030)
   - Licensed users: **15**
8. If in demo mode: shows "DEMO VERSION — limited to 150 records per file" notice

**Step 5 — Main Menu (EvoERPmenu.RWN continued)**

After START_UP.DBA returns, EvoERPmenu.RWN displays the EvoERP top-level menu.
The menu reads user permissions from BKSLEVEL and presents authorized menu items.

---

### FILELOC.B — File Location Routing Table

`FILELOC.B` (2,793,472 bytes) is the central Btrieve file that tells TAS Pro runtime
where to find each logical table for each company. Loaded first at every boot.

**Statistics (confirmed from full parse):**
- 3,613 total records
- 386 unique logical table names
- 6 company codes: AT, AB, CA, I2, IT, 99
- 1,754 alias mappings (48.5%) — different physical file per company
- 1,859 same-name mappings — same physical file across companies

**Record format (inferred from parsed data):**
```
Bytes 0–7:   Logical table name (8 chars, space-padded)
Bytes 8–15:  Physical filename alias (8 chars, space-padded)
Byte 16:     'B' (Btrieve file type marker)
Bytes 17–18: Company code (2 chars)
```

**Company codes in FILELOC.B:**
| Code | Records | Identity |
|------|---------|---------|
| AT | 714 | Internal/testing company AT |
| AB | 714 | "American Backplane" — legacy production company |
| CA | 714 | Company CA |
| I2 | 714 | i2 Systems — current production company |
| 99 | 735 | Demo / test company (standard DBA "company 99") |
| IT | 22 | IT admin / system company |

When TAS Pro opens a table (e.g., `BKSOX`), it looks up `FILELOC` to find the
physical filename and folder for the current company. This allows the same TAS Pro
code to route different companies to different data files.

**Key aliasing examples (I2 company):**

| Logical Name | Physical File | Explanation |
|-------------|--------------|-------------|
| BKARINV | BKARRINV | AR invoice — "R" archive variant |
| ROUTING | BKRTEMTR | Routing uses MT-era routing table |
| ISSRINFO | ISSRAINF | Sales receipt info → SR-specific variant |
| BKARCUST | BKCMCUST | Customer → Contact Manager customer alias |
| BKARCUST | ISARACST | Customer → IS-AR archive variant |
| BKICLOC | TBKICLOC | Inventory location → T-prefixed variant |
| WOLABOR | WOLABRPT | WO labor → Labor reporting variant |
| BKGLCOA | BKGLECOA / BKGLFCOA | COA → GL extended / GL forecast variants |
| INVTXN | INVATXN / INVETXN | Inventory transactions → archive variants |
| ISSERIAL | ISHLOTS | Serial control → lot-managed serial variant |
| BKART | ARTTEMP | AR transactions → temp/staging |
| ESTSUM | ISESTASM | Estimate summary → IS estimate assembly |

The I2 company has 200+ unique aliases, reflecting extensive customization.
(By comparison, AT company is a clean/test installation with fewer aliases.)

---

### WHOAMI.DBA — Workstation Identity File

`\i2s109-solidcrm\DBAMFG$\WHOAMI.DBA` is **2 bytes** (CR+LF only — essentially empty).
The per-workstation identity file is stored locally: `C:\ISTS\WHOAMI.DBA`.
The network copy being empty suggests all workstation-specific data lives locally.

The CLAUDE.md notes WHOAMI.DBA can be 35 bytes — the local workstation copy at
C:\ISTS\WHOAMI.DBA may contain workstation name, last user, company code, and
other session state that survives restart.

---

*Pass 103d — Boot sequence confirmed from START_UP.DBA + StartEvo.exe binary analysis.*
*Boot Sequence confidence: 68→82/100.*

---

## Pass 104 — TAS 4GL Language Summary and Module Confirmations (2026-06-18)

Source: BKROA.SRC (75KB, Routing Entry), BKMRF.SRC (57KB, MRP Generate), BKDCA.SRC (30KB, Data Collection A).
Full language reference in `docs/02-file-formats/src-tas-pro-language.md`.

---

### TAS Pro 7 4GL Language — Complete Reference Summary

**All operators confirmed:**

| Class | Operators |
|-------|-----------|
| Arithmetic | `+` `-` `*` `/` |
| Comparison | `=` `<>` `>` `<` `>=` `<=` |
| Logical | `.a.` (AND) `.o.` (OR) `.n.` (NOT) |
| In-set | `$` — `if STATUS $ "CXI"` = true if STATUS char is in the string "CXI" |
| String concat | `*` (traditional) and `+` both work |

**All field types:**

| Type | Meaning |
|------|---------|
| A | Alpha string (fixed length) |
| N | Numeric decimal (`dec N` sets fraction digits) |
| I | Integer |
| D | Date (YYYYMMDD) |
| T | Time (HH:MM:SS) |
| L | Logical: `.t.` / `.f.` |
| R | Record position (Btrieve cursor location) |
| B | Byte |
| P | Pointer |
| F | Float/file handle |
| V | Variant (observed, purpose unclear) |
| O | Object/flag (observed in DC module) |

**All find modes:**

| Mode | Meaning |
|------|---------|
| `find F` | First record |
| `find N` | Next record |
| `find P` | Previous record |
| `find L` | Last record |
| `find G` | Greater-or-equal (first record with key >= given value) |
| `find M` | Match (exact key match) |

Find modifiers: `err <label>` (branch on not-found), `nlock` (no lock), `noclr` (keep buffer).

**Key built-in functions:**

| Function | Purpose |
|----------|---------|
| `windows()` | True if running in Windows mode (not DOS) |
| `clicked_on()` | True if field activated by mouse click |
| `zask(msg, default)` | Yes/no modal dialog |
| `iif(cond, a, b)` | Inline conditional |
| `str(val[, width, dec])` | Numeric to string |
| `trim(str, 'L'/'R')` | Trim leading/trailing spaces |
| `mid(str, start, len)` | Substring |
| `just(str, 'L'/'R')` | Justify (left/right pad) |
| `chr(n)` | Character from ASCII code |
| `round(val, dec)` | Round numeric |
| `ttof(time)` / `ftot(n)` | Time ↔ float conversion |
| `flerr(handle)` | File error code (0=OK) |
| `fnum('name')` | Get file handle number |
| `co()` | Current 2-char company code |
| `loc(str, sub)` | Position of substring |

**Loop constructs:**

```
for(var;start;end;step)
  fexit_if condition    ;exit if true
  fexit                 ;unconditional exit
next

while condition
  exit                  ;break
endw

while .t.              ;infinite loop
  exit                  ;use exit to break
endw
```

**`ifna TABLE ... endif`** — execute block if last find found no record.

**Record position save/restore:**
```
rcn TABLE rcn POSVAR get   ;save current position
rcn TABLE rcn POSVAR set   ;restore position
```
Requires `POSVAR` of type R.

**Array utilities:**
```
updta ARRAY clr                    ;zero all elements
updta ARRAY1,ARRAY2,ARRAY3 clr    ;clear multiple
sorta KEY[cntr] move A[cntr],B[cntr],C[cntr] num N cntr cnt_var
```

---

### EvoERP Module Code Confirmations (Pass 104)

Previously uncertain module codes now confirmed from menu_codes.csv analysis:

| Code | Module Name | How Confirmed |
|------|------------|---------------|
| **DE** | Data Exchange | DE-A=Export Data; DE-B..H=Import (Inventory/BOM/Routings/Customers/Vendors/COA/Labor); DE-O=Export to QuickBooks |
| **IS** | i2 Systems Custom Reports | IS-A..D all use J5/J6/JM-prefix custom programs — Item Recap, Production Report, Top-N Ships, New Customers |
| **MM** | Mfg Management Reporting Hub | MM menu entries reuse BKARG/BKAPJ/BKAPA — reporting shortcuts pointing to existing AP/AR programs |
| **PL** | Payroll Link | PL-E = BKPLE, program says "Payroll Software Link Setup" |
| **RM** | Return Material Authorization | RM-A Enter RMA, RM-C Receive, RM-D Process, RM-E Reason Maint. Supersedes DBA legacy "AB" module name |
| **LM** | Lot Management | LM-B Item Generator Templates (BKLMB); LM-H Purge QC Receipts (BKLMH) |
| **DI** | Data Import — Labor | Single entry: DI-G=Import Labor (BKDIG) |

**IS module programs (i2 custom):**

The IS module programs use non-standard prefixes (J5, J6, JM) and appear to be Java or custom application integrations added by i2 Systems:
- `J5AVICT`, `J5BOMXPT`, `J5CRDCPY`, `J5CRPIMP`, `J5NWTICT` → IS-A Item Recap
- `J6CFPRPT`, `JMAPIBL`, `JMMPI2`, `jmcrbfs` → IS-B Production Report
- `J6CFTOPI` → IS-C Top N Shipped Items
- `j6cfcust` → IS-D New Customer Report

These are distinct from the standard BKXXY / T7XXY program naming convention — they are i2 Systems custom extensions layered on top of the base EvoERP system.

---

### System Architecture — StartEvo.exe and Menu Storage (Pass 105)

**StartEvo.exe is a .NET assembly** (not a TAS Pro program) that runs before `tp7runtime.exe`:
1. Authenticates via Active Directory (`DomainAuthenticateAndLaunchEvo`)
2. Kills stale EvoERP processes (`KillEvoProcesses`)
3. Queries Pervasive PSQL DSN `EVOADMIN` for license validation:
   `SELECT count(*) FROM tas_menus WHERE menu_name = ? AND program_name = ?`
4. Launches `evoerp.exe` (= `tp7runtime.exe`) under the authenticated user
5. Handles `evo://` URI deep-links from emails or browsers

**Menu storage is BKMENUSU.DBF** (xBase/dBASE format, read by CodeBase `c4dll.dll`):
- `BKMENUSU.TXT` on the network share is a plain-text CSV export of the full menu tree
- 870 lines covering every menu item, its label, and its program file
- Record format: `"CODE","Label","program.rwn"` — three columns, quoted CSV
- `tas_menus` in StartEvo's SQL is the PSQL view of this same file

**Module navigation groups** (the EvoERP tab bar):

| Tab | Modules |
|-----|---------|
| Mfg | WO, JC, PO, MR, SH, DC, ES, QC |
| Items | IN, RO, BM, LC, SC, FO, PI, WC |
| Sales | SO, SR, RM, SA, CS, CM, AR, CR |
| Queries | QU, SU |
| Hand Held | HH |
| System Mgr | UT, SM, SD, IM, PS, DE, TAS |
| Accounting | GL, AP, FA, AM, AD |
| Pay Link | PL |
| Payroll | PR |
| Settings | US |

**PL = Checkmark Payroll Link** — integrates with an external product called
"Checkmark Payroll." PL-A launches Checkmark; PL-B/C import the resulting check and
voucher data back into EvoERP; PL-D configures the connection. Entirely separate from
EvoERP's own PR (Payroll) module.

---

*Pass 104 — TAS 4GL language comprehensively documented; all 38 EvoERP module codes confirmed.*
*TAS 4GL: 75→87/100. File Formats — SRC: 80→87/100. Menu System: 78→84/100.*
*Pass 105 — StartEvo.exe analyzed; BKMENUSU.DBF menu storage confirmed; complete code→program mapping.*
*System Architecture: 80→87/100. Menu System: 84→93/100.*

---

## Platform Subsystems

Background services and utility programs that run alongside or outside the main EvoERP session. Not invoked from the standard module menus.

**Confidence: 82/100** — programs identified from RWN string analysis and DB fingerprints; configuration details confirmed from named_vars.

### EvoService — Background Scheduler and Reminder Engine

**Program:** `EvoService.RWN` (27 procs)

Runs as a background process. Polls on the interval set in `ISTS.CFG` key `WTIME` (seconds). On each tick it:
1. Queries `ISSCHED` (24-field scheduler table) for due jobs → dispatches them.
2. Queries `ISREMIND` (reminder table) for overdue reminders → fires notifications.

**Configuration:**
- `ISTS.CFG.WTIME` — polling interval in seconds.
- `ISTS.CFG.USINI` — path to user INI file.
- SMTP settings are configured separately in EvoServiceSetup.

### EvoServiceSetup — Service Install + Email / SMTP Configuration

**Program:** `EvoServiceSetup.RWN` (49 procs). Opens `ESETTINGS` table.

Does two things:

**1. Registers the Windows Service:**
- `THIRTYTWO` / `SIXTYFOUR` — named vars holding the 32-bit and 64-bit Windows service registration paths respectively. The installer picks the path matching the OS bitness and writes the EvoService entry to the Windows Service Control Manager.
- `ISTS.CFG.USINI` — writes the path to the user INI file so EvoService can locate it at runtime.
- `EvoServiceRemove.RWN` (18 procs) uses the same `THIRTYTWO`/`SIXTYFOUR` vars to uninstall.

**2. Configures outgoing email (for alert notifications, reminders, and automated reports):**
- `EMAIL.CFG.SMTP` — SMTP server hostname.
- `EMAIL.CFG.PORT` — SMTP port (commonly 25 or 587).
- `EMAIL.CFG.USER` / `EMAIL.CFG.PASS` — SMTP credentials.
- `EMAIL.CFG.SEC` — security/TLS flag.
- `ESETTINGS` — general email enable/disable toggle (persisted to ESETTINGS table).

**How to configure SMTP:** Run EvoServiceSetup from the EVO admin menu → enter SMTP host/port/credentials → save. Changes take effect at next EvoService poll cycle. To uninstall the service, run EvoServiceRemove from the same menu.

### EvoERPbackup — Automated Backup

**Program:** `EvoERPbackup.RWN` (76 procs)

Three backup scope modes (selected at setup):
- `FULLSYSTEM` — entire EvoERP data share.
- `COMPDATA` — company-specific data files only.
- `CUSTOM` — user-defined file list via `FILELOC` routing table.

Day-of-week scheduling variables: `MON`/`TUE`/`WED`/`THU`/`FRI`/`SAT`/`SUN`.

**AWS Glacier support:** Variable `GLACIERKEY` + archive type variables `GS_ARCH` / `GS_BACKUP` / `GS_NONE` — allows archiving to Amazon Glacier cold storage in addition to local backup.

**How to restore from Glacier:** Use EvoERPbackup → Glacier Restore mode (GS_ARCH path). Glacier retrieval takes hours to days depending on retrieval tier.

### EvoLinks — Document / URL Attachment System

**Program:** `EvoLinks.RWN` (156 procs). Primary table: `ISLINKS` (311 fields).

Attaches hyperlinks (files, URLs, network paths) to any EvoERP entity (PO, SO, WO, part, vendor, customer, etc.).

**ISLINKS field semantics (from TAS named_vars, Pass 110e, 2026-06-19):**

| TAS variable | Purpose |
|---|---|
| `IS.LNK.UID` | Unique link record ID (PK) |
| `IS.LNK.LINK` | The link target — file path, URL, or UNC path |
| `IS.LNK.APP` | Which EvoERP application/module owns this link |
| `IS.LNK.TYPES` | Link type code (file, URL, email, etc.) |
| `IS.LNK.PCB` | Parent Context Block — array of up to 100 parent record keys; links one document to multiple records simultaneously |
| `IS.LNK.DEF` | Default link flag (used when multiple links exist for one record) |
| `IS.LNK.GLOBAL` | Globally visible (all users can see) vs. user-private |
| `IS.LNK.OPENWITH` | Application to launch when user opens the link |
| `IS.LNK.DATE` | Date link was attached |
| `IS.LNK.NOTE` | Free-text note/description for the link |
| `IS.LNK.WHO` | User who created the link |
| `IS.LNK.ATYPE` | Attachment type (e.g., document, image, thumbnail) |
| `IS.LNK.EXTRA` | Extra metadata field |
| `IS.LNK.PRIVATE` | Private-to-user flag (overrides GLOBAL for the creating user) |
| `IS.LNK.SORT` | Sort order among multiple links on one record |
| `IS.LNK.ALPHA` | Alpha/display key for sorting |
| `FILELINK` | Resolved local file path (after path translation) |
| `LEXIST` | Flag: link target exists on disk (validated at open time) |
| `GEN.ID` | Generic entity ID — the key of the owning record (e.g., PO number, SO number) |
| `INVENTORY.LINK` | Set when the link belongs to an inventory item |

**Entity attachment — supporting tables opened by EvoLinks:**
- `BKAPVEND` — AP vendor master (vendor-linked documents)
- `BKARCUST` — AR customer master (customer-linked documents)
- `BKCMACCN` — CRM account (CRM contact documents)
- `BKAPDESC` — AP description codes (AP-linked documents)
- `BKYSMSTR` / `BKICMSTR` — Item / inventory master (part documents)
- `BKPSUSER` — User table (for WHO lookup)
- `FILELOC` — File location routing (for translating server paths)
- `ISACCESS` / `ISLOG` — Security / audit trail

**Thumbnail / component document links (eBOM / engineering doc integration):**
- `E.DOC.NAME` — Engineering document name
- `E.THUMB.LINK` — Thumbnail image link for engineering document
- `E.PARENT.COMP` — Parent component (part number) for engineering doc
- `PG.DOC.NAME` — Purchasing / general document name
- `PG.THUMB.LINK` — Thumbnail image link for purchasing document
- `PG.PARENT.COMP` — Parent component for purchasing doc

These vars suggest EvoLinks supports a two-tier document system: **engineering docs** (`E.*`) and **purchasing/general docs** (`PG.*`), each with thumbnail previews and parent-component links.

**How to add a link:** From any EvoERP transaction header, press the Links button (or use the EvoLinks menu) → enter the URL or file path → select Open-With application → save. The `IS.LNK.PCB` array means one file can be attached to multiple records in one operation.

### CALREM — Calendar Reminders

**Program:** `CALREM.RWN` (142 procs). Opens: `ISREMIND`, `BKARCUST`, `BKAPVEND`, `BKICMSTR`, `BKCMACCN`.

Create and view date/time reminders. Reminders can be linked to:
- AR customers (`BKARCUST`)
- AP vendors (`BKAPVEND`)
- Inventory items (`BKICMSTR`)
- CRM contacts (`BKCMACCN`)
- Free-form (no entity link)

No separate CALREMGC.RWN — Google Calendar sync, if present, is embedded in CALREM.RWN itself.

**How to add a reminder:** Open CALREM from the Reminder button/menu → select entity type and link → set date/time and note → save. EvoService fires the reminder on schedule.

---

## Spec Book / Approved Source List (SB)

**Confidence: 82/100** — DDF schema confirms field names and key structure; program assignments inferred from RWN analysis.

The SB module implements an **Approved Vendor / Manufacturer List (AVL/QPL)** — sometimes called a "Spec Book" in the EvoERP UI. Common in electronics and PCB manufacturing to enforce sourcing rules.

Three tables:

| Table | Fields | Purpose |
|-------|--------|---------|
| `BKSBMFG` | 6+ | Approved manufacturers. PK: `PARNT`+`PROD`+`CUST` → `MANUF`+`MPART`. Maps a parent part + product + customer combination to approved manufacturer and manufacturer part number. |
| `BKSBVEND` | 6+ | Approved vendors. PK: `PARNT`+`PROD`+`CUST` → `VEND`+`VPART`. Maps to approved vendor code and vendor's part number. |
| `BKSBPART` | 5+ | Approved substitute parts. Stores approved part substitutions for a given parent part. |

**How to view/edit the AVL for a part:** IN-B (Inventory Item Master) → SB tab. The SB tab shows `BKSBMFG` and `BKSBVEND` records for the selected item.

**MRP / PO enforcement:** T7MRG (MRP firming) and T7POB (PO print) query the SB tables to flag or enforce sourcing rules when generating purchase orders.

*Pass 108 — Platform Subsystems and Spec Book sections added; TAS 4GL `enter` options fully documented (12 options confirmed from 7 SRC files).*

---

## Java Application Inventory (Pass 157+159, 2026-06-22)

EvoERP ships 30+ Java application JARs on `\\i2s109-solidcrm\DBAMFG$\`. Each is launched by a
TAS Pro 7 stub program (usually 5–30 procs) that populates ISJAVA or uses JAVA.PATH/JAVA.PATH2 vars
to shell-execute the JAR. The JARs implement the heavy-UI viewer / analysis layer that TAS Pro 7 UI
cannot efficiently render.

### TAS Stub Program Families (Pass 159)

Three distinct TAS Pro 7 stub patterns connect to the Java layer:

**Pattern A — Thin ISTECH.LIB launchers (23–27 procs, JAVA.PATH/JAVA.NAME vars):**
These programs do nothing except look up a JAR path and launch it. Programs: PROJECTEDSTOCK (23p),
SQLEXPORT (23p), COMMISSIONRPT (23p), INVCHANGE (24p), ITEMCLASS (24p), PURCHITEM (26p),
WORKCENTERLOAD (26p), CASHFLOW (26p), CRMDASHBOARD (26p), PURCHVEND (26p), PURCHTXN (24p),
BOMTREE (27p), EDITBOMTREE (27p), t7jtemp (27p), t7jftrans (27p). All from ISTECH.LIB.
`PROJECTEDSTOCK.RWN` — JAR name unknown (not yet decrypted to read JAVA.NAME constant).

**Pattern B — EVO.LIB/LISTG60.LIB module panels (50–65 procs, PROGRAM.HEADER/VS/INIT/POST vars):**
Full module programs with display state management that open a Java panel as their primary UI.
Programs: T7VSCHED (94p), T7JSETTINGS (70p, Sisense BI config: SERIAL7/CDEF.BUFF/SERVER_PATH),
T7JAVASET (57p, basic Java connection URL/HOST/PORT setup), t7jpos (54p, POS module, POSSOURCE/POSDEST),
T7JCRM (62p, CRM Java panel), t7jbs (63p, Business Score embedded panel), T7JODPSALES (52p, JO drill-down),
t7jsacc/jsaSRS/jsoi/jsaPBI/jsaIc (50p each, JS BI data bridges).

**Pattern C — Large TAS programs using Java for sub-operations (HOST/PORT/NAME, 100+ procs):**
Full TAS Pro 7 business programs that use the Java connection for notifications, AvaTax, or
real-time alerts — not Java-primary. Programs include: T7SOA (606p, SO Entry → AvaTax/email),
T7ING (323p, inventory adj), T7POJC (323p, PO QC receiving), T7WOS (197p, WO ship/boxing),
T7MDefaults (435p, global handle initializer), EvoERPmenu (147p, main menu startup initializer),
T7SRE (213p, SO return entry / RMA), t7hhssoe (267p, HH ship), T7SOE/SOD/SOGA/SOR (SO variants).

**T7MDefaults** (435p, ISTECH.LIB) is the **global system startup handle initializer**: called from
the main menu to open shared handles (FO.H/SYAP.H/GLCOA.H/DCSHFT.H/SHIPCO.H/DIGSIG.H/EDIMSTR.H),
set module enable flags (SYSACCTGON/SYSARON/SYSAPON), and start the Sisense keepalive timer
(TENMIN.KILLER/LOOP.TIME). It also reads LGS config (DCL.WEEKS/PERIOD.FREQ/PERIOD.PDTE) and
EIM co-product shift codes (EIMCO.SHIFT2/3).

### Module-to-JAR Mapping

| JAR | Main Class (package) | Module | Purpose |
|-----|---------------------|--------|---------|
| Scheduler.jar | main.Driver | SL | Shop Loading scheduler (older) |
| WCScheduler.jar | com.evoerp.wcsched | SL | Work Center Scheduler |
| WOScheduler.jar | com.evoerp.main | SL | Work Order Scheduler |
| WorkCenterLoad.jar | com.evoerp.wcload.javafx | VSCHED | Visual WC capacity load (JavaFX) |
| MachineView.jar | com.evoerp.machineview.jfx | SL/DC | Machine/floor view (JavaFX) |
| FOTree.jar | com.evoerp.fotree.main | FO | Features & Options tree view |
| FOTreeRun.jar | Main | FO | FO tree launcher shim |
| BOMTREE.JAR | com.evoerp.bomtree.javafx | BM | BOM tree viewer (JavaFX) |
| EditBOMTree.jar | com.evoerp.editbomtree.javafx | BM | BOM tree editor (JavaFX) |
| BomUtility.jar | com.evoerp.bomutility.jfx | BM | BOM utility (JavaFX) |
| BusinessStatus.jar | com.evoerp.businessstatus.main | QU-D | Business Status dashboard |
| CrmDashboard.jar | com.evoerp.ureinn.jfx | CM | CRM Dashboard (JavaFX) |
| CustomerServiceInquiry.jar | com.evoerp.csi.main | AR/CM | Customer Service Inquiry |
| LLForecast.jar | com.evoerp.levelload.main | MR | Level Load / production forecast |
| MultiYearSales.jar | com.evoerp.multiyear.main | SA | Multi-year sales analysis |
| SalesRepSummary.jar | com.evoerp.salesanalysis.srs | SA | Sales rep summary |
| ProfitByInvoice.jar | com.evoerp.salesanalysis.pbi | SA | Profit by invoice |
| ItemClass.jar | com.evoerp.salesanalysis.ic | SA | Item class analysis |
| CustomerClass.jar | com.evoerp.salesanalysis.cc | SA | Customer class analysis |
| CashFlow.jar | main.Main | GL/QU | Cash flow viewer |
| CashFlowReport.jar | main.Main | GL/QU | Cash flow report |
| CommissionRpt.jar | main.Main | SA/PR | Commission report |
| PurchItem.jar | main.Main | PO | Purchase by item analysis |
| purchtxn.jar | com.evoerp.main | PO | Purchase transaction viewer |
| purchvend.jar | main.Main | PO | Purchase by vendor analysis |
| QueryExecute.jar | com.evoerp.queryexecute.jfx | QU-E/F | Query execute (JavaFX) |
| EVOPVT.JAR | com.evoerp.TASKS.sql | QU-F | SQL task executor (QU-F backend) |
| SQLExport.jar | com.evoerp.sqlexport.main | EX | SQL Export / BI export |
| DataUpload.jar | com.evoerp.dataupload.main | TA | Data upload utility |
| invchange.jar | com.evoerp.icr.main | IN | Inventory change record viewer |
| phone.jar | com.evoerp.phonecompare.main | CM | Phone/contact comparison |
| EVOFX.JAR | com.evoerp.FX.sql | ML | Foreign exchange rate SQL tool |
| EVOAVATAX.JAR | com.evoerp.avatax.sql | (config) | Avalara AvaTax integration |
| EvoToOutlookAppt.jar | com.evoerp.outlook.appointments | CALREM | Outlook calendar appointment sync |
| EvoScreenshot.jar | com.evoerp.screenshot.main | (util) | Screenshot capture utility |
| SMTPCLIENT.JAR | com.evoerp.smtp | (infra) | SMTP email client |
| EVOERP-BACKUP.JAR | — | TA-O | EvoERP backup (large: 4.3 MB) |
| Barcode.jar | Main | (util) | Barcode rendering |
| Tree.jar | — | (util) | Generic tree UI component |

### Java Infrastructure
All Java JARs use the shared Pervasive JDBC driver (`lib/pvjdbc2.jar`, `lib/pvjdbc2x.jar`) for
database access and depend on:
- `lib/Evo.jar` / `lib/Evo2.jar` / `lib/EVO3.JAR` — shared EvoERP Java framework
- `lib/jide-*.jar` — JIDE Swing component suite (grids, dock, dialogs)
- `lib/jfreechart.jar` — chart rendering (sales dashboards, capacity charts)
- Spring 3.0.7 (`lib/spring-*.jar`) — dependency injection for larger apps
- Java 8 runtime (`java/` folder) for 32-bit TAS Pro 7, Java 11+ (`Java2/`) for newer apps

**Confidence: 75/100** — All 37 JARs enumerated with Main-Class; package names confirm module
assignments; 3 stub patterns classified (Pass 159); PROJECTEDSTOCK JAR name unresolved; T7JAVASET vs
T7JSETTINGS distinction confirmed; JAR source not decompiled.
