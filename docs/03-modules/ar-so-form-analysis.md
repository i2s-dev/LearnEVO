# AR and SO Module — DFM Form Analysis
Status: partial | verified-from-DFM

Forms read directly from `\\I2S109-SOLIDCRM\DBAMFG$\T7AR*.DFM` and `T7SO*.DFM`.

---

## AR — Accounts Receivable

### Complete AR Workflow

```
Customer master (T7ARA)
    ↓
Invoice creation (T7ARB — manual vouchers; or from SO module)
    ↓
Payment receipt & application (T7ARC)
    ↓
Finance charge calculation (T7ARD — periodic)
    ↓
Reporting: Statements (T7ARE), Aging (T7ARF), Customer lists (T7ARG-I)
```

---

### T7ARA — Customer Master Maintenance (AR-A)
**Purpose:** Enter and maintain customer master records.

**Key fields:**
- Customer Code (`BKAR.CUSTCODE`), Customer Name (`BKAR.CUSTNAME`)
- Address: ADD1, ADD2, City, State, Zip, Country
- Contact: Phone (`BKAR.TELEPHONE`), Fax (`BKAR.FAX.PHONE`), Email (`BKAR.EMAIL`)
- Terms (`BKAR.TERMS.NUM`)
- Up to 2 salesperson/commission slots: `BKAR.SLSP.NUM[1-2]`, `BKAR.COMM[1-2]`
- GL Sales Account (`BKAR.GLACCT`), GL Department (`BKAR.GLDPT`), Territory
- Flags: Send Statement (`BKAR.STATEMENT`), Charge Interest (`BKAR.CHG.INTRST`)
- Ship-To: code, FOB, Ship Via (`BKAR.SHIPTO`, `BKAR.FOB`, `BKAR.SHPVIA`)
- Discount/Price codes, Tax group
- Extended address (up to 8 lines via `ISAREX.EXTADD[1-8]`)

**Primary tables:** BKARCUST (customer master), ISAREX (extended attributes)
**Primary key:** `BKAR_CUSTCODE`

---

### T7ARB — Voucher / Manual Invoice Entry (AR-B)
**Purpose:** Create AR invoices manually (not from SO module).

**Key fields:**
- Customer Code/Name
- Voucher/Check Number (`CHECK.VNUM`)
- Invoice: Number, Type, Date, Description (`BKAR.INVV.VNUM/TYPED/DATE/DESC`)
- Terms (`BKAR.INVV.TERMD`), Currency (`BKAR.INVV.ISCUR`)
- Total Amount (`BKAR.INVV.TAMT`)
- Up to 10 GL distribution lines: `BKAR.INVV.GLACT[1-10]`, `BKAR.INVV.GLDPT[1-10]`,
  `BKAR.INVV.GLD[1-10]` (amounts), `BKAR.INVV.DC[1-10]` (Debit/Credit indicators)
- Job number (`DEFJOB`)

**Primary tables:** BKARINV (invoice header), BKARINVL (invoice lines)
**Primary key:** `BKAR_INV_NUM`

---

### T7ARC — Record Payments / Cash Receipts (AR-C or similar)
**Purpose:** Apply customer payments to outstanding invoices.

**Key fields:**
- Customer Code/Name
- Invoice list: Number, Date, Description, Amount, Terms, Discount, Applied, Balance
  (`dinv_num`, `dinv_date`, `dinv_desc`, `dinv_amtrm`, `ENT_DISC`, `ENT_APPLIED`, `xbal`)
- Payment: Check/Deposit Amount, Check Number, Deposit Number, Payment Date
- Outstanding balances: Credits, Deposits, Invoices (`BKAR.OUT.CREDIT[1-2]`, `BKAR.OUTINV`)
- Customer info: Phone, Last Sale, Last Payment
- Exception handling: Invoice, Amount, Discount, Description (`EXCP.*`)
- NSF check/reversal flags

**Primary tables:** BKARINV (invoice header), payment application tables
**Primary key:** `BKAR_INV_NUM`

**Important:** Credits and deposits are tracked separately (`BKAR.OUT.CREDIT[1-2]`) — this is
the mechanism for applying credits/prepayments before touching open invoices.

---

### T7ARD — Finance Charge Calculation
**Purpose:** Calculate and post finance charges on overdue invoices.

**Key fields:**
- Calculate-as-of date (`CALC_DATE`)
- Minimum charge (`NMININT`)
- Compound interest flag — charge interest on previous finance charges
- Interest rate display (read-only from system settings)
- Grace period in days (`BKSY.AR.INT.DAY`)
- Currency filter

**Primary tables:** BKARINV, BKSYMSTR/BKYSMSTR (interest rate config)

---

### T7ARE — Print Customer Statements
**Purpose:** Generate and print customer account statements.

**Key options:**
- Balance Forward Date, Statement Date
- Show payments for last X days
- Customer Class range, Currency filter
- Overdue / Current / All accounts filter
- Sort by: Code, Name, or Class
- Print Description/Terms/Customer PO option
- Age Statement format, Zero balance accounts
- Show deposits applied vs received

---

### T7ARF — Print AR Aging
**Purpose:** Generate AR aging report with invoice aging buckets (30/60/90/120+ days).

---

### T7ARG — Print Customer Directory
**Purpose:** Print customer code and name listing.

---

### T7ARH — Print Customer General Info
**Purpose:** Customer master report with filter by start date, last sale date, salesperson,
state, and customer class range.

---

### T7ARI — Print Customer Mail Labels
**Purpose:** Mailing labels for customer marketing/communication.

---

## SO — Sales Orders

### Complete SO Workflow

```
Enter SO header + lines (T7SOA)
    ↓
Print/Process SO acknowledgment (T7SOB)
    ↓
Release SO for picking (T7SOE)
    ↓
Execute: pick → pack slip → ship → invoice (T7SOC)
    ↓
Print final invoices (T7SOF)
    ↓
COGS / profitability analysis (T7SOG)
```

---

### T7SOA — Sales Order Header & Line Entry (SO-A)
**Purpose:** Enter and maintain sales order headers and line items.

**Header fields:**
- SO Number (`SONUM.CHAR`)
- Customer: Code, Name, Address (`BKAR.INV.CUSCOD/CUSNME/CUSA1/CUSA2/CUSCTY/CUSST/CUSZIP`)
- Ship-To: Code, Name, Address, Contact (`BKAR.INV.SHPCOD/SHPNME/SHPA1/SHPA2/SHPATN/SHPCNT/SHPST/SHPCTY/SHPZIP`)
- Totals: Subtotal, Tax, Freight, Total (`BKAR.INV.SUBTOT/TAXAMT/FRGHT/TOTAL`)
- Description, Terms, Ship Via, FOB, Job Number
- Entered By, Currency, Location, GL Department
- Tax Group/Key/Taxable flag, Billing Code
- Up to 2 salespersons/commissions
- Customer PO, Price Code

**Line item fields (5,001 element arrays):**
- Location (`line.prod.loc[5001]`), Ordered Qty (`line.prod.oqty[5001]`)
- Product Number, Code, Description
- Qty, ESD (Estimated Ship Date), Price, UOM
- Taxable flag, Discount, ASD (Actual Ship Date), Revision Level
- UBO (Unit Backorder?)
- Weight tracking per line (`line.wt`), total weight (`tot.line.wt`)
- ECO/Drawing references (`IS.OECO.DRAW`, `IS.OECO.REVLVL`)

**Primary tables:** BKSO (SO header), BKSOL (SO lines), BKICMSTR (product), BKARCUST (customer)
**Primary key:** `BKAR_INV_NUM` (invoice number assigned; SO# is `SONUM.CHAR`)

**Note:** Line arrays sized to 5,001 — supports very large SOs. Each SO can have 5,000 line items.

---

### T7SOB — Print/Process SO Reports
**Purpose:** Print SO acknowledgments and control processing.

**Key options:**
- Customer/Class/SO number/Job range filters
- Sort by item flag
- Print options: Notes, Hidden notes, Kit components, ECO, Options, Tax codes, Freight
- Include zero balance lines, Blanket lines flag

---

### T7SOC — Pick / Pack / Ship / Invoice Hub
**Purpose:** The central workflow controller — executes picking, packing slips, shipping,
and invoicing from a single form.

**Key fields:**
- SO/Customer/Class/Job range filters
- Ship date, Ship number
- Print options:
  - Notes, Hidden notes, Kit, Comment, Options, Qty options, Lot, ECO, Serial
  - Multi-location, Bin locations
  - Zero qty, Backorders, Standard pack, Consolidation, Open kit
  - Truck routing, Serial numbers
- Print start date / Use existing start date
- Page break character
- Invoice date range
- Backorder only flag, Surcharge
- RTM templates: `SOCofC.rtm`, `ItemCofC.rtm`, `ShipDoc.rtm`, `coo.rtm`
  (Certificate of Conformance, Certificate of Origin, Shipping Document)
- Posted packing slip, Line COFC, BO report, CoC, Country of Origin, Ship doc flags

**Primary tables:** BKSO, BKSOL, BKSOSH (shipment records), BKARINV (invoices created)

**Key finding:** T7SOC creates invoices — it is where the SO → Invoice transition happens.
The `coo.rtm` (Country of Origin) report integration and `SOCofC.rtm` (Certificate of Conformance)
integration show EVO supports export compliance documentation from the shipping workflow.

---

### T7SOD — SO Line Details / Status Management
**Purpose:** Display and modify SO line-level details and status; handles backorder lines.

---

### T7SOE — SO Release & Shipment Management
**Purpose:** Release SOs for picking/shipping and manage shipment status.

**Key fields:**
- SO Date, Customer/Ship-To address block
- Customer PO, GL Dept, Salesperson, Location, Terms
- Release through Estimated Ship Date
- Tracking Number, Last Invoice
- Release flag
- Display shipped lines option
- Auto-release comments option

**Primary tables:** BKSO (header status), BKSOL (line status)

---

### T7SOF — Print Invoices
**Purpose:** Print customer invoices from shipped SOs.

**Key options:**
- Invoice/Customer/Class/Salesperson/Shipper range filters
- Sort option
- Print linked documents
- Serial numbers option (Y/N/W/I)
- Ship date range
- RTM template selection
- Print options: Kit components, After-invoice packing slip, Tax codes, Freight, Surcharge,
  Line COFC, BO report, CoC, Country of Origin, Ship document, Blankets, Non-inventory items

---

### T7SOG — COGS / Profitability Report
**Purpose:** Sales Order Cost of Goods Sold analysis — shows profit margin per order.
**Caption confirmed:** "SOG COGS Report"

---

## Key Table Relationships

```
BKARCUST (customer) ←→ BKSO (SO header)
BKSO ←→ BKSOL (SO lines)
BKSOL ←→ BKICMSTR (item master — product lookup)
BKSO → BKSOSH (shipment records when T7SOC executed)
BKSO → BKARINV (invoice created by T7SOC/T7SOF)
BKARINV ←→ BKARINVL (invoice lines)
BKARINV → payment application (T7ARC)
```

---

*Last updated: 2026-06-11*
*Confidence: 72/100 — T7ARA through T7ARI and T7SOA through T7SOG all read from network share.
Field-level names confirmed for key forms. Business logic inferred from field names and labels.*
