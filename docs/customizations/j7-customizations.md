# J7* — EvoERP Customization Modules (i2 Systems)

Status: partial (DFM forms analyzed; RWN program logic is encrypted and not readable).

*Source: `\\i2s109-solidcrm\DBAMFG$\J7*.*` — copied to [samples/j7-customizations/](../../samples/j7-customizations/).*
*Inventory date: 2026-06-01. Total files: 109 (41 DFM, 63 RWN, 19 RTM/RTX, 1 ZIP).*

---

## Overview

J7* modules are site-specific customizations layered on top of standard EvoERP. The naming convention mirrors the standard TAS Pro 7 module prefix scheme — standard screens use `T7xx`, while customizations use `J7xx`. These modules extend or replace standard EVO screens to support customer-specific workflows, external integrations, data collection on shop-floor and handheld terminals, and specialized reports. Some modules are general i2 Systems infrastructure (usable for any customer); others are hard-coded for a named customer (Lapco Manufacturing, a mattress manufacturer, BEF, TMC, CC, etc.) and are identified as such below.

The prefix characters after `J7` often encode the customer or module category: `CC` = customer CC, `TMC` = customer TMC, `BEF` = customer BEF, `RC` = customer RC, `NM` = customer NM, `SI` = customer SI, `ABI` = customer ABI / Lapco, `PT` = Portable Terminal (handheld series), `HH` = Hand Held, `DC` = Data Collection, `EB` = customer EB (mattress manufacturer group).

---

## Module Inventory by Category

---

### Sales Orders

---

#### J7CRSOW — Batch Close Sales Orders

**Category:** Sales Orders
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Batch close Sales Orders. Provides a filter screen (SO number range, invoice number range, customer range, customer PO number range, order date range) and a grid showing SO#, order date, customer code, item, description, ship qty, and backorder qty. A Y/N flag controls whether only SOs with remaining backorder quantity are closed.
**Key form fields:**
- SO Number From/Thru
- Invoice Number From/Thru
- Customer From/Thru
- Cust PO Number From/Thru
- Order Date From/Thru
- Include SOs with Backorders only [YN]
- SO# (grid)
- Ord Date (grid)
- Cust Code (grid)
- Item (grid)
- Ship Qty (grid)
- BO Qty (grid)

**Related EVO modules:** SO, AR
**Notes:** Caption is `SO-W`. The backorder-only flag (`incl.backorders`, `AllowedChrs='YN'`) determines whether all matching SOs or only those with open backorder balance are closed. Form is stay-on-top with `RememberSize`.

---

#### J7i2SystemSOOE — Custom Open Orders Export (i2 Systems)

**Category:** Sales Orders
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: i2 Systems — the reseller/implementer itself, not an end customer)
**Last modified:** not in recent-activity list
**Purpose:** Custom Open Orders Export (SOOE) filter screen for i2 Systems. Lets the user select a range of open sales order lines to export or process, filtered by estimated ship date, customer ID, customer class, item class, and item category.
**Key form fields:**
- Est Ship Date From/Thru
- Customer ID From/Thru
- Customer Class From/Thru
- Item Class From/Thru
- Item Category From/Thru

**Related EVO modules:** SO, IN
**Notes:** Caption is `Custom SOOE`. `SourceFile` is `J7I2SYSTEMSOOE`; event handlers delegate to `T7SOOE`, indicating it is a custom override of the standard SOOE screen. Includes Print and Settings buttons. Older `RememberSizeDate` (2013).

---

#### J7SOAImpLines — Import SO Lines from CSV

**Category:** Sales Orders
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Import Sales Order lines from a comma-delimited CSV file into an existing SO. The user specifies a company code, target SO number, import filename, date format, and column position numbers for item code, description, quantity, price, estimated ship date, and customer due date. Options to include a second description line, specifications, and make-from components.
**Key form fields:**
- Company Code / Company Name / Company Path (selection grid)
- SO Number
- Customer Code
- Import Filename
- Date Format
- Item Code (column#), Item Description (column#), Quantity (column#), Price (column#), Est Ship Date (column#), Cust Due Date (column#)
- Include Second Description
- Include Specifications
- Include Make From Components

**Related EVO modules:** SO, AR, IN
**Notes:** Two-panel form: a company-selection grid (`CC_CODE`, `CC_NAME`) and an SO lines import panel. A PO panel in the file appears vestigial or alternate (fields reference `sponum`/`vend.code`/`vend.name`), suggesting shared structural code with J7POAImpLines. Comma-delimited import with configurable column positions (`FIELD.NUMBER[1-7]`).

---

#### J7SyncWOtoSO — Synchronize WO Dates and Quantities to SO

**Category:** Sales Orders
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Synchronize Work Order dates and quantities to their parent Sales Order lines. Displays a grid of SO lines linked to WOs showing SO line#, item, description, qty to ship, ship date, and promise date. For each selected line, the user can update the SO estimated ship date, promise date, and ship quantity, and simultaneously update the WO scheduled start/finish date, due date, and WO quantity. Shows original values alongside editable new values for comparison.
**Key form fields:**
- SO Line Number
- WO Number (prefix/suffix)
- Item Number / Description
- Est Ship Date / Promise Date (SO side)
- Sched Start Date / Sched Fin Date / Due Date (WO side)
- Ship Quantity / WO Quantity / Quantity Complete
- Issued L/M

**Related EVO modules:** SO, WO
**Notes:** Caption is `Sychronize WO to SO` (misspelling preserved from original). Form is 920 px wide with two grids (SOGrid 7-column and SOWOGrid 15-column) plus an edit panel. `Issued L/M` hint: L = Labor Issued, M = Material Issued, B = Both. Event handlers reference `T7WODATES`, indicating reuse of a standard WO dates routine.

---

### Accounts Payable

---

#### J7POAIMPLINES — Import PO Lines from CSV

**Category:** Accounts Payable
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Import Purchase Order lines from a comma-delimited CSV file into an existing PO. The user specifies a PO number (vendor code and name auto-populated), import filename, date format, and column positions for item code, description, quantity, price, estimated receipt date, WO prefix, WO suffix, and job number. Options to include second description, vendor items, approved manufacturers, and specifications.
**Key form fields:**
- PO Number / Vend Code / Vend Name
- Import Filename
- Date Format
- Item Code (column#), Item Description (column#), Quantity (column#), Price (column#), Est. Receipt Date (column#), WO Prefix (column#), WO Suffix (column#), Job Number (column#)
- Include Second Description
- Include Vendor Items
- Include Approved Manufacturers
- Include Specifications

**Related EVO modules:** PO, AP, IN, WO
**Notes:** Structurally parallel to J7SOAImpLines but targets PO lines. Eight configurable column-position fields (`FIELD.NUMBER[1-8]`). WO prefix/suffix and job number columns extend beyond SO import, reflecting PO-specific requirements. Action button is labeled `Import` rather than `Process`. Caption is `BASE Blank T7 SCREEN` — the form title was never updated from its template.

---

#### J7AutoAPC — Auto-Enter AP Invoices from Received POs

**Category:** Accounts Payable
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Auto-enter Accounts Payable invoices from received purchase orders. User sets a date range (Received Date From/Thru), vendor range, and vendor class range, then chooses whether to use the PO actual received date or fall back to a manual invoice date. A Process button triggers the automatic AP invoice creation.
**Key form fields:**
- Received Date From/Thru
- Vendor From/Thru
- Vendor Class From/Thru
- Use PO Actual Received (checkbox)
- If not, use Invoice Date / Date as the Invoice Date

**Related EVO modules:** AP, PO
**Notes:** Source handler is `T7APC`. Has a Settings button (`btnCFG`) alongside the Process button, suggesting configurable behavior. The `Use PO Actual Received` checkbox toggles between the PO receipt date and a fallback manual invoice date.

---

#### J7AppVend — Approve Vendor / Set Maximum Check Amount

**Category:** Accounts Payable
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Approve or flag a vendor as an approved vendor and set a maximum allowable check amount for that vendor. User looks up a vendor by code and the vendor name auto-populates. Then sets the Approved Vendor checkbox and a monetary ceiling for AP check writes.
**Key form fields:**
- Vendor Code
- Name (read-only, auto-populated)
- Approved Vendor (checkbox)
- Maximum Allowable Check Amount

**Related EVO modules:** AP
**Notes:** Simple maintenance form. Source handler is `T7APV`. The vendor name field (`bkap.vendname`) is read-only and auto-filled when a vendor code is entered. The max check amount (`max.chk.amt`) is presumably stored on the vendor master record.

---

#### J7MPImportAR — Import AR Data from External File

**Category:** Accounts Payable
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Import Accounts Receivable data from an external file into EvoERP. User provides the full path and filename of the import file and clicks Process. Very minimal UI.
**Key form fields:**
- Name of file to Import (Must include path)
- Import File Name

**Related EVO modules:** AR
**Notes:** Despite the `AP` parent menu inferred from filename prefix `MP`, the form caption says `Import AR` and the source handler is `J7MPI`. The `MP` likely refers to a specific integration or migration project. Extremely lean UI — one text field and a Process button.

---

#### J7PTRecPOLine — Portable Terminal: Receive PO Line

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Receive a single PO line in a portable-terminal or point-of-use context. Displays a read-only summary of the PO (number, vendor code, vendor name, item number, description, item note, receive quantity, item price, extension) with a Clear button and a Process button (initially hidden).
**Key form fields:**
- PO Number
- Vendor Code / Vendor Name
- Item Number / Description / Item Note
- Receive Quantity / Item Price / Extension

**Related EVO modules:** PO, AP, IN
**Notes:** Caption is `Receive PO Line`. The `PT` prefix indicates a Portable Terminal / handheld screen. Nearly all fields are `ReadOnly`; the user sees pre-populated PO line data and confirms receipt via the Process button. `btnProcess` is `Visible=False` at design time — shown conditionally at runtime. The form includes a `TShellExe` component, unusual for a PO receive screen.

---

### Finance / ACH

---

#### J7I2SACH — AP Check ACH Export

**Category:** Finance
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems infrastructure)
**Last modified:** not in recent-activity list
**Purpose:** Export AP check data as an ACH (Automated Clearing House) payment file. User selects a bank account, specifies an output file path and delimiter, filters by check number range and check date range, then clicks Process to produce the export file.
**Key form fields:**
- Bank Account Number / Bank Account Name
- Export FileName
- Check Number From/Thru
- Check Date From/Thru
- Export Field Delimiter
- Effective Date
- Bank Assigned ID

**Related EVO modules:** AP
**Notes:** Module name contains `I2S` indicating i2 Systems-authored infrastructure. Hidden fields (Wells ID, Effective Date, Date Format combo) suggest configurable ACH format variants — one appears to be a Wells Fargo-specific layout. Hint text on the filename field recommends CSV or TXT extension.

---

### Manufacturing

---

#### J7WOLL — Print WO Component Labels (WO-L-L)

**Category:** Manufacturing
**Files:** DFM (form present), RWN (program present — October 2024)
**Customer-specific:** No (general i2 Systems)
**Last modified:** October 2024 (recently active)
**Purpose:** For a given Work Order number, prints labels for BOM components within a sequence number range and/or component item number range. Options to use BOM quantity for label quantity or specify a fixed copy count.
**Key form fields:**
- WO Num
- Parent Item / Description
- Sequence Number From/Thru
- Component Number From/Thru
- Use BOM Qty for Label Qty? (checkbox)
- Copies

**Related EVO modules:** WO, IN
**Notes:** Caption is `WO-L-L`. The WO number header panel is always visible (stay-on-top panel with gradient background); the filter area is below it. WO number entry (`scan.wonum`) accepts digits and hyphens, suggesting barcode scanner input. Includes Print and Settings buttons. DFM and RWN both modified October 2024.

---

#### J7PTWOKI — Portable Terminal WO-K-I (BOM Sync)

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Synchronize or update Work Order item/BOM data in batch. Filters by WO number range and item number range. Options: Print Exceptions Only, Sync In-Process WOs (BOMs only), and Update WO Class from Item WO Class. Action is triggered via a Process button.
**Key form fields:**
- Work Order From/Thru
- Item Number From/Thru
- Print Exceptions Only (checkbox)
- Sync In-Process WOs (Boms only) (checkbox)
- Update WO Class from Item WO Class (checkbox)

**Related EVO modules:** WO, IN
**Notes:** Caption is `WO-K-J` (form caption) though SourceFile is `J7PTWOKI`. Event handlers reference `T7WOKI` (standard WO KI routine). Includes a `TRtnTimer` component (`RTimer`, `Enabled=False`), suggesting auto-refresh or polling at runtime. The `Sync In-Process WOs` checkbox limits BOM sync to WOs already in process.

---

#### J7PEDCB — Production Floor Data Entry (Qty Reporting)

**Category:** Manufacturing
**Files:** DFM (form present), RWN (program present — March 2025)
**Customer-specific:** No (general i2 Systems)
**Last modified:** March 2025 (recently active)
**Purpose:** Production status data entry for work orders — a production floor scan/entry screen. A worker enters a Work Order number (with F2 lookup), and the parent part code, description, department, and work center auto-populate. The worker then records quantities: Qty to Make, Qty Completed, Parts Made, and Parts Scrapped.
**Key form fields:**
- Work Order
- Parent Part / Description
- Department / Work Center
- Qty to Make
- Qty Completed
- Parts Made
- Part Scrapped

**Related EVO modules:** WO, DC
**Notes:** Contains a `TAlarmClock` component in the toolbar (for shift timing / elapsed time display) and a Labor entry button (`btnLabor`), indicating this form may also log labor time against the work order. Field names reference `MTWO` (Manufacturing Work Order) and `MTWC` (Work Center) Btrieve files. Shop-floor data collection form, likely used at a terminal near the production line.

---

#### J7EIMDCRev — Data Collection Reverse / Correction (Labor)

**Category:** Data Collection
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Data collection reverse / correction form for work order labor transactions (EVO menu path IN-H). Allows a user to enter, review, or reverse a labor data collection record. Fields cover date, employee, work order number, operation sequence, run/setup hours toggle, start/finish times, parts produced, scrapped quantity, scrap code, number of jobs, run hours, setup hours, and work center.
**Key form fields:**
- Date / Employee
- Work Order Number
- Sequence (operation)
- Run/Setup Hrs toggle (R/S)
- Time Start / Time Finish
- Parts / Scrapped / Scrap Code
- Number of Jobs
- Run Hours / Setup Hours
- Work Center
- Backflush by Sequence (checkbox)
- Sequence now Complete (checkbox)

**Related EVO modules:** DC, WO
**Notes:** Caption says `IN-H Print Inventory Listing` but form content is entirely labor DC entry/reversal — the caption appears to be a placeholder copied from another form. SourceFile is `J7EIMDCREV`. Assembly (`MTWO.WIP.CODE`) and operation description (`seq.desc`) are displayed read-only as context. `EIM` likely = Employee Input Manufacturing.

---

#### J7TMCKanban — Kanban Order Management

**Category:** Manufacturing
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: TMC — initials, exact name unknown)
**Last modified:** not in recent-activity list
**Purpose:** Kanban order management form. Displays a list of pending kanban replenishment orders in a grid (Item, Description, Quantity, Price, Extension). Header panel allows filtering by vendor range, location, and packing slip number. The edit panel allows entry of a new kanban line: item number, description, reorder amount, receive quantity, item price, and calculated extension.
**Key form fields:**
- Vendor From/Thru
- Location
- Packing Slip Number
- Item Number / Description
- Reorder Amount (display)
- Receive Quantity / Item Price / Extension

**Related EVO modules:** IN, PO
**Notes:** Grid columns are `LINE.ITEM`, `LINE.DESC`, `LINE.RQTY`, `LINE.PRICE`, `LINE.PEXT`. Item note field (`BKIC.PROD.NOTE`) is displayed on the edit panel. CRUD buttons (Add, Edit, Delete) plus Process and Save. TMC prefix indicates a specific customer or plant.

---

### Data Collection / Hand Held — Mattress Manufacturer Group

The following modules form a cohesive workflow for a mattress manufacturer (customer prefix `EB`). All share the serial-number-driven mattress item tracking model and are consistent with each other in field naming and form sizing.

---

#### J7DCMatLabels — Print Mattress Labels (Data Collection)

**Category:** Data Collection
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group)
**Last modified:** not in recent-activity list
**Purpose:** Data Collection barcode-scan form that collects a serial number, a work order number, two employee IDs, and two operation sequence numbers, then prints mattress labels.
**Key form fields:**
- Serial Num (`inp.serial`)
- Matt WO No (`SCAN.WO`)
- Employee 1 (`SCAN.EMP1`) / Employee 2 (`SCAN.EMP2`)
- Sequence 1 (`oper1`) / Sequence 2 (`oper2`)
- Mattress Number / Mattress Description / Mattress WO Num (display)
- Last Item Scanned (display)

**Related EVO modules:** DC, WO
**Notes:** Two-employee entry with F2 lookup on each. Validates WO number with `VLD_WONUM()` and serial with `vld_serial()`. Form stays on top (`fsStayOnTop`). Narrow 224 px handheld form factor. SourceFile: `J7DCMATLABELS`.

---

#### J7DCSSOE — Data Collection Shipping (Mattress)

**Category:** Data Collection
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group)
**Last modified:** not in recent-activity list
**Purpose:** Scans a Sales Order number, then scans serial numbers and WO numbers to record mattress items being shipped against the SO. Buttons: Clear, Verify, Save.
**Key form fields:**
- SO Number (`sonum.char`)
- Serial Number (`inp.serial`)
- Matt WO No (`SCAN.WO`)
- Customer / Mattress Number / Mattress Description / Mattress WO Num / Quantity (display)
- Last Item Scanned (display)

**Related EVO modules:** DC, SO, WO
**Notes:** Verify launches `J7DCSSOEVerify`. Save posts the shipment. Primary SO entry field uses combo-enter with numeric-only allowed chars. Part of a DC → SO shipping workflow.

---

#### J7DCSSOEVerify — Verification Screen for J7DCSSOE

**Category:** Data Collection
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group; SourceFile = J7DCSSOE)
**Last modified:** not in recent-activity list
**Purpose:** Displays a grid of scanned line items (Item, Ship Qty, Ord Qty, Desc) so the operator can review before committing the shipment. Buttons: List, Exit. Grid allows row deletion.
**Key form fields:**
- Item (`LINE.VPART`)
- Ship Qty (`LINE.SHIP.QTY`)
- Ord Qty (`LINE.ORDERQTY`)
- Description (`LINE.DESC`)

**Related EVO modules:** DC, SO
**Notes:** Read-only grid (no insert, row-delete allowed) with 4 columns. SourceFile points back to J7DCSSOE — this is a sub-screen of that workflow. Caption reads `Sales Orders`.

---

#### J7HHEBINC — Hand Held Inventory Adjustment (Incoming)

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group)
**Last modified:** not in recent-activity list
**Purpose:** Scans a serial number to look up a mattress item and records the invoice number and bin/location for the incoming inventory adjustment.
**Key form fields:**
- Serial Num (`inp.Serial`)
- Item Number / Description / Mattress Number / Mattress Description / Inv No / Location (display)
- Last Item Scanned (display)

**Related EVO modules:** HH, IN
**Notes:** Uses `T7HH.OnClose`/`OnStart`/`OnOpenFiles` handlers — standard HH module lifecycle. No save/commit button visible in the form; likely auto-saves on valid scan. 224 px wide handheld form factor.

---

#### J7HHEBXFER — Hand Held Inventory Transfer (Mattress)

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group)
**Last modified:** not in recent-activity list
**Purpose:** Scans serial numbers to transfer mattress items from one warehouse location to another. Shows Transfer: From -> To Location header, item/description, mattress number/description, a running count of items scanned, and buttons: Verify, Save, Clear, Exit.
**Key form fields:**
- Serial Num (`inp.Serial`)
- Transfer (From -> To Location, display)
- Item Number / Description / Mattress Number / Mattress Description (display)
- Num Items Scanned / Last Item Scanned (display)

**Related EVO modules:** HH, IN
**Notes:** Verify button opens `J7HHEBXferVerify`. Running quantity counter on screen. Same 224 px handheld form factor.

---

#### J7HHEBXferVerify — Verification Screen for J7HHEBXFER

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: mattress manufacturer — EB group; SourceFile = J7HHEBXfer)
**Last modified:** not in recent-activity list
**Purpose:** Shows a grid of all scanned items (Item Number, Ship Qty, Description) before committing the transfer. Buttons: Label, List, Exit.
**Key form fields:**
- Item Number (`PART.ARRAY`)
- Ship Qty (`SHIPQ.ARRAY`)
- Description (`DESC.ARRAY`)

**Related EVO modules:** HH, IN
**Notes:** Grid with 3 columns; row deletion allowed. Has a `Label` button — can print transfer labels directly from the verify screen. SourceFile references `J7HHEBXfer`.

---

### Data Collection / Hand Held — General

---

#### J7EBSerial — Serial Number Capture (Data Collection)

**Category:** Data Collection
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Captures serial numbers during data collection (shop floor or receiving). Displays the item being processed, its description, total quantity required, and quantity remaining. User scans or types a serial number; scanned serials accumulate in a grid list.
**Key form fields:**
- Item Code / Item Description
- Qty (required) / Qty Remaining
- Serial Num (scan entry)
- Last Serial Num Scanned (display)
- Serial Number (grid list)

**Related EVO modules:** DC, WO, IN
**Notes:** SourceFile is `T7DCA` (standard Data Collection module). Small narrow form (224x284). Serial numbers stored in `SERIAL.LIST`. Allows row deletion from the grid but not insertion.

---

#### J7HHLITN — Hand Held: Enter Tracking Numbers

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Associates carrier tracking numbers with SO boxes. Operator scans a Box ID, enters the tracking number and shipping company, and records the freight charge. Displays SO number, box number, customer name, and ship company name.
**Key form fields:**
- Box ID Num (`BOX.ID`)
- Track # (`track.num`)
- Ship Co (`ship.co`)
- Freight (`frt.charge`)
- SO Number / Box Number / Customer Name / Ship CO Name (display)

**Related EVO modules:** HH, SO
**Notes:** SourceFile is `T7HHLITN` (standard T7 naming, not J7) — a generic i2 Systems HH module. Validates tracking number with `vld_tracknum()`, shipping company with `vld_shipco()`, and freight with `vld_frt()`. Buttons: Save, Clear, Exit.

---

#### J7CCPIC — Physical Inventory Count Entry (Hand Held)

**Category:** Inventory
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: CC — initials, exact name unknown)
**Last modified:** not in recent-activity list
**Purpose:** Physical inventory count entry form used during cycle counts or full physical inventory. An employee enters their number (validated), selects a year, physical inventory number (PI-C style quarter/number), count date, and warehouse location. A Tags button navigates to tag entry.
**Key form fields:**
- Employee No / Employee Name (display)
- Year
- Phys Inv No
- Count Date
- Location

**Related EVO modules:** IN
**Notes:** `OnClose`/`OnStart` handlers reference `T7HH` (hand-held module framework), confirming this is a hand-held terminal form. Caption: `PI-C Enter Tag Counts` — matches EVO's physical inventory count step C. Form is 224x284 — standard handheld size.

---

### Hand Held — PTS (Pick-Ticket Shipping) Group

---

#### J7HHPTSSOE — Hand Held PTS Shipping Entry

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: identified by `from.cust` field with F2 lookup — customer-specific i2 workflow)
**Last modified:** not in recent-activity list
**Purpose:** Shipping entry form for scanning items against a Sales Order by customer, item, lot number, WO number, and quantity. Wide desktop form (679 px) rather than handheld width, suggesting PTS is used at a PC workstation. Options to use a Print Dialog Box.
**Key form fields:**
- From Customer (`from.cust`)
- Item Number / Lot Number (`Lot.No`) / WO Number (`WONUM`) / Quantity (`scan.qty.char`)
- SO Number / Item Code / Item Description / Quantity / Box No (display)
- Use Print Dialog Box? (checkbox)

**Related EVO modules:** HH, SO, WO, IN
**Notes:** Wider than typical HH forms (679x443 vs 224x284). Label printing is integrated. Verify launches `J7HHPTSSOEVerify`. Lot number and WO number both have F2 lookup buttons.

---

#### J7HHPTSSOELABELS — Print Box Content Labels (PTS)

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: same as J7HHPTSSOE; SourceFile = J7HHPTSSOE)
**Last modified:** not in recent-activity list
**Purpose:** Sub-form of J7HHPTSSOE that prints packing/content labels for a range of boxes. Operator enters label quantity, a misc field, a box range (from/to box number), and an RTM report template name.
**Key form fields:**
- Label Qty (`labelQty`)
- Misc (`MISC`)
- Box (`from.box` to `thru.box`)
- RTM (`RTM_NAME`)

**Related EVO modules:** HH, SO
**Notes:** `RTM_NAME` field directly references a ReportBuilder `.RTM` template name — confirms label printing uses the Nevrona ReportBuilder engine. Box range entry allows batch label printing across multiple boxes.

---

#### J7HHPTSSOEVerify — Verification Screen for J7HHPTSSOE

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: same as J7HHPTSSOE; SourceFile = J7HHPTSSOE)
**Last modified:** not in recent-activity list
**Purpose:** Shows a 7-column grid of all scanned line items (Box#, Item, Box Qty, SO#, Description, WO Number, Lot Number) before the operator commits the shipment. Buttons: List, Label, Exit.
**Key form fields:**
- Box# (`LINE.VBOX`)
- Item (`LINE.VPART`)
- Box Qty (`LINE.VBOXQTY`)
- SO # (`LINE.VSONUM`)
- Description (`LINE.VDESC`)
- WO Number (`LINE.VWONUM`)
- Lot Number (`LINE.VLOT`)

**Related EVO modules:** HH, SO, WO, IN
**Notes:** Most data-rich verify grid in the set — 7 columns. Wide form (624x444). `Label` button links to `J7HHPTSSOELABELS` for printing from the verify screen.

---

#### J7HHRTSSOE — Hand Held Retail/Route Truck Shipping (RTS)

**Category:** Hand Held
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: `RT London` label visible on form — likely a route for a specific retail/distribution customer)
**Last modified:** not in recent-activity list
**Purpose:** Scans items against a Sales Order for route-truck or retail shipment. Operator selects an SO, then scans item and quantity per box. Buttons: Clear, Rel SO (release SO), Reset, Verify, Std Pk (standard pack), Exit.
**Key form fields:**
- SO Number (`sonum.char`)
- Box Num (`truck.no`)
- Item Num (`scan.item`) / Quantity (`scan.qty.char`)
- Load # (`sload.num`, hidden)
- Customer Name / Item Code / Quantity / Box No / Std Pack / UM (display)

**Related EVO modules:** HH, SO, IN
**Notes:** `Rel SO` (Release SO) and `Reset` buttons suggest a two-step release workflow distinct from other shipping forms. `Std Pk` button applies a standard pack quantity. Hidden `Load #` field hints at load/truck manifest tracking. `RT London` label text is italic/underlined and hard-coded — customer/route specific.

---

### Web Integration

---

#### J7BEFWebInv — Web Inventory FTP Export

**Category:** Web Integration
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: BEF — exact name unknown; initials match prefix pattern)
**Last modified:** not in recent-activity list
**Purpose:** Exports inventory data to a CSV file and uploads it via FTP to a web server. Allows filtering by item number range, item type, product class range, active status, and optionally restricts to `Web Inventory` items only. Can adjust exported quantity by open SO demand within a configurable day window and by reserve quantity.
**Key form fields:**
- FTP Host Name / FTP User Name / FTP Password
- Name of CSV File
- Item Number From/Thru
- Item Type [RFAMNLBTKO]
- Class From/Thru
- Active Status Filter [YNODE]
- Report on Only Web Inventory Items (checkbox)
- Include All Locations / Print By Location
- Adjust Qty with SO within X Days
- Adjust Qty by Reserve Qty
- Include BO Quantity for SOs

**Related EVO modules:** IN, SO
**Notes:** SourceFile is `T7DEU` (base data export module, not a J7 file). Tooltip on the `Web Inventory` checkbox references IN-B user-defined fields and SM-P-E setup. Has both Export and Settings buttons. A companion `J7BEFWebInvAuto.RWN` (7 KB) exists for automated/unattended runs.

---

#### J7CIWebImport — Web / EDI Sales Order Import

**Category:** Web Integration
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Imports sales orders from a web/EDI flat file downloaded via FTP. Supports FTP download mode and direct local file import. Orders can be routed to either the EDI staging module or directly into the open Sales Order file. Includes bank account selection, optional unattended (auto) mode, and kit component expansion.
**Key form fields:**
- FTP Host Name / FTP User Name / FTP Password
- Name of File on FTP Site / New Name of FTP file to Save (optional)
- Name of Import File (local)
- Import to EDI Module or Open SO file (E, S)
- Bank Account Number
- Run Unattended (checkbox)
- Use Imported SO Number as actual SO Num (checkbox)
- Add Kit Components to SO for Kit Parents (checkbox)

**Related EVO modules:** SO, AR, EDI
**Notes:** Form has three sub-panels (`CIWebPanel`, `DETPanel`, `ImpFldsPanel`). The `ImpFldsPanel` is a reference layout showing expected flat-file column positions for Order Header (H records, fields 1-21) and Order Line (L records) — effectively documenting the import format within the UI itself. Required fields are shown in red.

---

### Inventory

---

#### J7NMBins — Bin Location Maintenance

**Category:** Inventory
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Maintains bin location assignments for inventory items. User enters an item number; the form displays the item description, on-hand quantity, and current bin location. The bin location field is editable. An image preview panel is present (likely showing a warehouse map or item photo).
**Key form fields:**
- Item / Description / On Hand / Bin Location

**Related EVO modules:** IN
**Notes:** Uses field names `BKIC.PROD.DESC`, `BKIC.PROD.UOH`, `MTIC.PROD.LOC` — confirming direct Btrieve file access to inventory master (BKIC) and item transaction/location (MTIC) tables. `TImage` panel (`ImagePreview`) suggests bin-map or product image display. NM prefix likely stands for the customer or module variant.

---

### Reports

---

#### J7LapcoSO — Lapco Inventory Usage Report

**Category:** Reports
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: Lapco Manufacturing)
**Last modified:** not in recent-activity list (RememberSizeDate 2009 — among earliest customizations)
**Purpose:** Print Inventory Usage report for Lapco Manufacturing. Filters by item number range, item class range, item category range, item type code, active status filter, and customer range.
**Key form fields:**
- Item Number From/Thru
- Class From/Thru
- Category From/Thru
- Item Type [RFAMNLBTKO]
- Active Status Filter [YNODE]
- Customer From/Thru

**Related EVO modules:** SO, IN
**Notes:** Form caption is `Print Inventory Usage`. SourceFile is `J7LAPCOSO`; event handler prefix is `J7LMI`. RememberSizeDate timestamp is 2009 — one of the earliest customizations in the set. Includes Print and Settings buttons.

---

#### J7ABIShipRpt — Lapco Fulfillment Report

**Category:** Reports
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** Yes (customer: Lapco Manufacturing — caption explicit)
**Last modified:** not in recent-activity list
**Purpose:** Customer-specific shipping/fulfillment report that filters by item number range, order date range, and customer range, then prints. The form caption explicitly names `Lapco`.
**Key form fields:**
- Item Number From/Thru
- Order Date From/Thru
- Customer From/Thru

**Related EVO modules:** SO, IN
**Notes:** The filename prefix `ABI` does not match the Lapco caption — `ABI` may be an older customer code or abbreviation that predates a rename, or refers to a parent entity. Source handler is `J7ABI`. Structurally identical to other report-criteria forms in this set.

---

#### J7MCDSAReport — Sales Analysis Report

**Category:** Reports
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Sales Analysis Report — filters by customer code range, customer class range, and a year-to-date date range, then prints the report.
**Key form fields:**
- Customer Code From/Thru
- Customer Class From/Thru
- YTD Date From/Thru

**Related EVO modules:** SO, AR
**Notes:** Source handler is `T7MCD`. `MCDSA` likely means `MCD Sales Analysis`. Standard report-criteria form with no unusual components.

---

#### J7NMRTMPRINTER — RTM Print Routing Configuration

**Category:** System
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems infrastructure)
**Last modified:** not in recent-activity list
**Purpose:** Maintains a table mapping EvoERP program names to specific RTM report template names and printer destinations. Users can Add, Edit, Delete, and Save rows in a grid showing Program Name, RTM Name, and Printer. A separate edit panel allows entry of individual values with F2 lookup and a printer Setup button.
**Key form fields:**
- Program Name (`rtm.program`)
- RTM Name (`rtm.rtm`)
- Printer (`rtm.printer`)

**Related EVO modules:** (none — system-level)
**Notes:** Caption is `BASE Blank T7 SCREEN` — the internal developer label indicating it was built from a blank template. Source handler is `J7NMPRTM`. Grid field names (`IS.RTM.PROGRAM`, `IS.RTM.RTM`, `IS.RTM.PRINTER`) indicate data is stored in a custom `IS` (i2 Systems) Btrieve file, not a standard EvoERP table. This is essentially the print-routing configuration table for the ReportBuilder engine.

---

#### J7SMJCT — Closed Job Cost Report

**Category:** Reports
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Closed Job Cost (JCT) report parameters form. User selects a sales order number (with customer code and name displayed for context), item number (with description lines displayed), and an order date range. Generates a printed cost report for closed work orders linked to sales orders.
**Key form fields:**
- SO Number
- Customer Code / Customer Name (display)
- Item Number / Item Description / Item Description Line 2 (display)
- Order Date From/Thru

**Related EVO modules:** SO, WO, GL
**Notes:** Caption is `Closed Job Cost Report`. SourceFile is `J7SMJCT`. Print and Exit buttons only — purely a report driver form. SM prefix likely indicates Sales/Manufacturing reporting category within the J7 customization set.

---

#### J7CJBUsage — Inventory Usage Report

**Category:** Reports
**Files:** DFM (form present), RWN (program present)
**Customer-specific:** No (general i2 Systems)
**Last modified:** not in recent-activity list
**Purpose:** Prints an inventory usage report filtered by date range, customer range, item number range, product class range, product category range, and active status.
**Key form fields:**
- Date From/Thru
- Customer From/Thru
- Item Number From/Thru
- Product Class From/Thru
- Product Category From/Thru
- Active Status Filter [YNODE]

**Related EVO modules:** IN, SO, AR
**Notes:** Caption is `Print Inventory Usage`. SourceFile is `J7CJBUSAGE`. Print, Settings, and Exit buttons. The customer filter connects this to AR/SO data — usage is likely derived from sales history or issue transactions. CJB prefix is an unknown customer or sub-module designation.

---

## RWN-Only Modules (No DFM — Encrypted; Purpose Inferred from Name)

These modules have compiled `.RWN` program files on the network share but no readable `.DFM` form definition. Purpose is inferred from the filename and file size only; actual logic is not readable.

| Module | Size | Last Modified | Inferred Purpose |
|---|---|---|---|
| J7AIJCG.RWN | 310 KB | — | AII/AIJ customer — likely Job Cost or GL reporting (large = complex) |
| J7AIJCG2.RWN | 313 KB | — | Second variant of J7AIJCG — possibly a revised or alternate version |
| J7AISAN.RWN | 427 KB | — | AIS customer — largest RWN, likely a comprehensive report or data sync |
| J7APCHECK.RWN | 44 KB | — | AP Check printing or validation utility |
| J7BEFWebInvAuto.RWN | 7 KB | — | Automated/unattended companion to J7BEFWebInv (scheduled FTP export) |
| J7CCCutSheet.RWN | 546 KB | — | CC customer — Cut Sheet document (largest file in set; likely PDF/form generation) |
| J7CCFABXFER.RWN | 338 KB | — | CC customer — Fabrication Transfer (inventory or WO transfer for fab shop) |
| J7CCITEMSYNC.RWN | 284 KB | — | CC customer — Item Sync (synchronize item master data) |
| J7CCSHI.RWN | 7 KB | — | CC customer — Shipping (small, likely a launcher or dispatch screen) |
| J7CCSOLABELS.RWN | 353 KB | — | CC customer — SO Labels (print labels for sales orders) |
| J7CCXFER.RTM | 13 KB | — | CC customer — Transfer report template (ReportBuilder RTM, not a program) |
| J7HHNorSSOE.RWN | 7 KB | — | Hand Held — NorS SO Entry (small handheld SO screen, customer NorS) |
| J7NMImport.RWN | 302 KB | — | NM customer — Import (large import routine, likely item or order data) |
| J7NMITEMRTM.RWN | 225 KB | — | NM customer — Item RTM (item label or report template program) |
| J7POC.RWN | 241 KB | — | PO-C (Purchase Order Confirm/Close) — general i2 Systems |
| J7RCConvTable.RWN | 233 KB | — | RC customer — Conversion Table maintenance |
| J7RCPitex.RWN | 284 KB | — | RC customer — Pitex integration or export |
| J7RCSOImport.RWN | 346 KB | — | RC customer — SO Import (large, likely full SO import from external system) |
| J7RITECPOA.RWN | 126 KB | October 2024 | RITEC customer — PO-A (PO entry or acknowledgement) — recently active |
| J7SISALES.RWN | 294 KB | — | SI customer — Sales reporting or sales data export |

---

## Zero-Byte DFM Placeholders

The following `.DFM` files exist on the share but are 0 bytes. The corresponding `.RWN` program may or may not exist. These likely represent modules under development, recently retired, or migrated to a different structure.

| File | Notes |
|---|---|
| J7ADTNACHA.DFM | ACH / NACHA payment export (ADT customer or general AP) — 0-byte placeholder |
| J7BEFWEB.DFM | BEF customer web integration — possibly superseded by J7BEFWebInv |
| J7CIWEB.DFM | CI web import — possibly superseded by J7CIWebImport (separate DFM analyzed above) |
| J7POAIMP.DFM | PO-A Import — 0-byte as of October 2024 (RWN modified same date; under active development) |

---

## Recently Active Modules (2024–2025)

Four modules show file modification dates in 2024-2025, indicating ongoing development or maintenance at the time of inventory:

| Module | Date | What It Suggests |
|---|---|---|
| J7PEDCB.RWN | March 2025 | Shop-floor production data entry (Qty Reporting) is actively maintained — likely in use at a customer site |
| J7RITECPOA.RWN | October 2024 | RITEC customer PO-A screen is active — a named customer engagement ongoing in late 2024 |
| J7POAIMP.DFM | October 2024 | PO line import form is being rebuilt or extended — 0-byte DFM with same-date RWN suggests active development |
| J7WOLL.DFM / J7WOLL.RWN | October 2024 | WO component label printing was recently updated — both form and program touched in the same release window |

---

## Cross-References

- Standard Sales Order module: [docs/03-modules/so-sales-orders/help-content.md](../03-modules/so-sales-orders/help-content.md)
- Standard Work Order module: [docs/03-modules/manufacturing/](../03-modules/manufacturing/)
- Standard Inventory module: [docs/03-modules/inventory/](../03-modules/inventory/)
- Standard AP module: [docs/03-modules/ap-accounts-payable/](../03-modules/ap-accounts-payable/)
- ReportBuilder (.RTM) file format: [docs/file-formats/rtm-reportbuilder.md](../file-formats/rtm-reportbuilder.md)
- Btrieve / Pervasive data files (.B): [docs/file-formats/btrieve-data-files.md](../file-formats/btrieve-data-files.md)
- TAS Pro 7 source / compiled files (.SRC, .RWN): [docs/file-formats/tas-pro-7-files.md](../file-formats/tas-pro-7-files.md)
- EVO file naming conventions: [docs/README.md](../README.md)
