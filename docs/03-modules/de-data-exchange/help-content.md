# DE — Data Exchange

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → Data Exchange (15 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Data Exchange module provides all of EvoERP's import and export plumbing. It covers: a SQL-based query/export tool for extracting data to CSV; bulk import wizards for the five core master files (inventory, bills of material, routings, customers, vendors, and chart of accounts); three transactional import-and-post programs for manufacturing data (labor, material issues, work order receipts); import of physical inventory counts; a web-storefront integration pair (download orders, upload stock balances); and two destructive utilities that reset data globally (Global Field Change, Erase Files). Most import programs stage data in temporary files first, allow error review and editing, then transfer to permanent master files.

---

## Contents

- [DE-A — SQL Query/Export (Java Version)](#de-a--sql-queryexport-java-version)
- [DE-B — Import Inventory](#de-b--import-inventory)
- [DE-C — Import Bills of Material](#de-c--import-bills-of-material)
- [DE-D — Import Routings](#de-d--import-routings)
- [DE-E — Import Customers](#de-e--import-customers)
- [DE-F — Import Vendors](#de-f--import-vendors)
- [DE-G — Import Chart of Accounts](#de-g--import-chart-of-accounts)
- [DE-H — Global Field Change](#de-h--global-field-change)
- [DE-I — Erase Files](#de-i--erase-files)
- [DE-J — Import & Post Labor](#de-j--import--post-labor)
- [DE-K — Import & Post Material Issues](#de-k--import--post-material-issues)
- [DE-L — Import & Post Work Order Receipts](#de-l--import--post-work-order-receipts)
- [DE-M — Import Physical Inventory Counts](#de-m--import-physical-inventory-counts)
- [DE-T — Import Web Storefront Orders](#de-t--import-web-storefront-orders)
- [DE-U — Upload Stock Balance to Web Storefront](#de-u--upload-stock-balance-to-web-storefront)
- [Cross-references](#cross-references)

---

## DE-A — SQL Query/Export (Java Version)

*Source: [de-a_sql_query_export.htm](../../../samples/chm/extracted/de-a_sql_query_export.htm)*

**Purpose.** Extract all or selected records and fields from EvoERP data files to a disk file in CSV format. Two paths are provided: direct SQL entry for experienced users, and a Query Wizard for everyone else.

**Direct SQL path.** If you know the EvoERP file and field names and are comfortable with SQL, compose a query in the main text area and click **Execute**. Results are displayed on screen with an option to save to a CSV file. Queries can be saved for future reuse.

**Query Wizard path.** Click **Query Wizard**. The wizard walks through three screens:

1. **File selection** — choose one or more EvoERP data files, then click **Next**.
2. **Field selection** — for each file in the dropdown, select the fields to include. Click **Next** when all files have been configured.
3. **File linking** — link files by a common field (e.g., link `BKAPPO` Purchase Order Header to `BKAPPOL` Purchase Order Lines by Purchase Order Number). If the linking field is not already in the selected field list, click **Show All** to expose every field in both files.
4. **Filters** — enter any desired filter criteria. **Show All** is again available to filter on fields not in the result set.

Click **Finish** to return to the main screen with the SQL query pre-populated, then click **Execute**.

**Default Queries (preset reconciliation queries).** Click **Default Queries** to access a library of predefined reconciliation queries:

- **GLPOINV** — Identifies GL transactions posted to the PO/RNI account from PO Invoicing (AP-C) that have no corresponding line items in the PO Receiver file.
- **GLPORECPT** — Identifies GL transactions posted to the PO/RNI account from PO Receiving (PO-C) that have no corresponding line items in the PO Receiver file.
- **Inv_Txn_no_GL** — Finds Inventory Transaction entries that have no corresponding GL entries.
- **INVGL** — Finds GL Transaction entries to a specified inventory account that have no corresponding Inventory Transaction.
- **INVGLACCT** — Finds Inventory Transactions whose associated GL transactions are not posting to the correct account based on item class and location.
- **Inventory_Non_Asset** — Identifies tangible inventory items that are posting to a GL account that is not an Asset account.
- **Non_Inventory_Asset** — Identifies non-tangible inventory items that are posting to an Asset GL account.

---

## DE-B — Import Inventory

*Source: [de-b_import_inventory.htm](../../../samples/chm/extracted/de-b_import_inventory.htm)*

**Purpose.** Import inventory items from another system or from an ASCII file produced outside of EvoERP. Designed primarily for system startup, but can also be used on an ongoing basis when new item lists arrive from customers or are exported from a CAD/engineering system.

**General operation.** Follow the general import instructions described in the *Importing Master Files* section of the help file. The inventory import has five required fields in addition to the **Item Number** itself:

- **Class** — validated against values in SM-C Enter Item Classes.
- **Type** — validated against the acceptable type list defined in IN-B Enter Inventory.
- **Stock U/M** — stock unit of measure (required).
- **Price U/M** — pricing unit of measure (required).
- **Purch U/M** — purchasing unit of measure (required).

All other inventory fields are optional. Additionally, **Vendor** codes are validated against vendors entered in AP-A Enter Vendors, and **Customer** codes are validated against customers entered in AR-A Enter Customers. Detailed field descriptions are given in IN-B Enter Inventory.

---

## DE-C — Import Bills of Material

*Source: [de-c_import_bills_of_material.htm](../../../samples/chm/extracted/de-c_import_bills_of_material.htm)*

**Purpose.** Import Bills of Material from another system or from an ASCII file. Like the inventory import, this can be used at startup or ongoing when Engineering releases new BOMs from a CAD system.

**General operation.** Follow the general import instructions in *Importing Master Files*. Required fields:

- **Parent Part Number** — validated against the inventory master.
- **Component Part Number** — validated against the inventory master.
- **Component Type** — required and validated.
- **Quantity Per** — must be non-zero.

All other BOM fields are optional.

**Duplicate handling.** The import can be configured to skip or replace existing parent/component pairs, or to allow appending duplicate components during the import to the temporary staging files. However, regardless of this setting, the **Transfer to Permanent Files** step always appends to the existing BOM master file. This means that if you import a BOM for a parent part that already has a BOM in the permanent file, you will end up with duplicated components. Verify existing BOM records before transferring.

---

## DE-D — Import Routings

*Source: [de-d_import_routings.htm](../../../samples/chm/extracted/de-d_import_routings.htm)*

**Purpose.** Import Routings from another system or from an ASCII file produced outside of EvoERP.

**General operation.** Follow the general import instructions in *Importing Master Files*. Required fields:

- **Parent Part Number** — validated against the inventory master.
- **Type** — required and validated.
- **Work Center** — validated against work centers entered in RO-C Enter Work Centers.
- **Sequence** — must be non-zero.
- **Operation** — must be non-zero.

All other routing fields are optional.

**Time entry.** Time per part for each operation is entered as decimal time (e.g., `0.0833` for 5 minutes). When data is transferred to the master files, the program automatically converts decimal time to HH:MM:SS time per part and calculates parts per hour.

---

## DE-E — Import Customers

*Source: [de-e_import_customers.htm](../../../samples/chm/extracted/de-e_import_customers.htm)*

**Purpose.** Import Customer master file information from another system or from an ASCII file.

**General operation.** Follow the general import instructions in *Importing Master Files*. Only two fields are required:

- **Customer Code** — the unique customer identifier.
- **Payment Terms Number** — must be a valid payment terms code.

All other customer fields are optional.

---

## DE-F — Import Vendors

*Source: [de-f_import_vendors.htm](../../../samples/chm/extracted/de-f_import_vendors.htm)*

**Purpose.** Import Vendor master file information from another system or from an ASCII file.

**General operation.** Follow the general import instructions in *Importing Master Files*. Only two fields are required:

- **Vendor Code** — the unique vendor identifier.
- **Payment Terms Number** — must be a valid payment terms code.

All other vendor fields are optional.

---

## DE-G — Import Chart of Accounts

*Source: [de-g_import_chart_of_accounts.htm](../../../samples/chm/extracted/de-g_import_chart_of_accounts.htm)*

**Purpose.** Import Chart of Accounts master file information from another system or from an ASCII file.

**General operation.** Follow the general import instructions in *Importing Master Files*. Two fields are required:

- **Account Code** — the GL account number/code.
- **Type** — required and validated. Valid type values are:
  - `A` — Asset
  - `L` — Liability
  - `O` — Owner's Equity
  - `E` — Expense
  - `I` — Income

All other chart of accounts fields are optional.

---

## DE-H — Global Field Change

*Source: [de-h_global_field_change.htm](../../../samples/chm/extracted/de-h_global_field_change.htm)*

**Purpose.** Globally change a critical field value across many records in a master file without editing records one by one. This is especially useful after an import when codes from the source system do not match EvoERP's expected codes — for example, changing all inventory **Type** `P` (purchased, in the old system) to **Type** `R` (raw material, in EvoERP). The program only operates on the critical fields listed on the error reports.

**General operation.**

1. Select one of the four supported files from the opening list, then press Enter.
2. A window lists the critical fields within that file that can be globally changed. Highlight the desired field and press Enter.
3. **Replace all values?**
   - Answer **Y** to superimpose a single value on every record in the file (e.g., set the selling unit of measure to `EA` for all records). The cursor moves to **Value to replace with?** — enter the new value and press Enter.
   - Answer **N** to replace only records that match a specific value. Enter the **value to search for** (e.g., `P`) and the **value to replace with** (e.g., `R`). The program automatically replaces every matching occurrence.

---

## DE-I — Erase Files

*Source: [de-i_erase_files.htm](../../../samples/chm/extracted/de-i_erase_files.htm)*

**Purpose.** Completely erase imported data from one or more modules so you can restart the import process with empty staging files. Intended for use when an import run has errors that cannot be corrected in place and the entire import needs to be restarted.

**General operation.** Enter `Y` for each module whose data you want to erase, then press Enter or Tab through the remaining fields to begin processing.

**Scope of erasure.** This program erases data only from the **temporary staging files**. It has no effect on the permanent master files with one important exception:

- **Imported Labor** is stored in the same file as unposted labor from Data Collection or WO-M Batch Labor Entry. If you are both importing labor and using Data Collection or Batch Labor Entry concurrently, ensure that all valid labor is posted before running Erase Files on the labor module — otherwise valid unposted labor from those other sources will also be erased.

---

## DE-J — Import & Post Labor

*Source: [de-j-a_import_post_labor.htm](../../../samples/chm/extracted/de-j-a_import_post_labor.htm)*

**Purpose.** Import Work Order labor data collected by an external time clock system, review it for errors, edit it, and post it to Work Order files. This program comprises three sub-programs: Import Labor, Print Labor Errors, and Edit Labor.

### Import Labor

**Purpose.** Load labor records from an external time clock file into EvoERP's unposted labor staging area.

**General operation.** Follow the general import instructions in *Importing Manufacturing Data*. Required fields:

- **Employee Number** — validated against employees in SM-G Enter Employees.
- **Work Order** number — validated against open released work orders.
- **Sequence** number — validated against work order sequences.

If no date is provided in the import file, the program defaults to the **system date (today)**. Note that imported labor is stored in the same staging file as labor entered through Data Collection or WO-M Batch Labor Entry.

### Print Labor Errors

**Purpose.** Print a report of errors in imported labor data before transferring to permanent work order files.

**General operation.** Enter a range of **dates** and **employees** to filter the error report. Error codes on the report:

- `WO` — Invalid Work Order number.
- `RI` — Work Order is not status `R` (Released) or `I` (In Process).
- `SQ` — Invalid sequence number.
- `EM` — Invalid employee number.

Note: each record displays only one error code on the report, but a record may have multiple errors. All errors must be corrected in the Edit Labor program before the record can be saved or posted.

### Edit Labor

**Purpose.** Edit individual imported labor records before posting to Work Order files.

**General operation.** Select the record to edit from the list. All fields can be edited except the **Employee Name** (which is display-only, derived from the employee number). Tab through all fields or press **F10** at any time to save the record. To create new labor entries from scratch (not imported), use WO-M Batch Labor Entry instead.

---

## DE-K — Import & Post Material Issues

*Source: [de-k-a_import_post_material_issues.htm](../../../samples/chm/extracted/de-k-a_import_post_material_issues.htm)*

**Purpose.** Import Work Order Material Issue data collected by an external system (such as a bar code data collection device), edit it, and post it to Work Order files. Comprises two sub-programs: Import Material Issues and Edit & Post Material Issues.

### Import Material Issues

**Purpose.** Load material issue records from an external collection file into EvoERP's staging area.

**General operation.** Follow the general import instructions in *Importing Manufacturing Data*. All fields are required **except** the **Lot Number** for items that are not Lot Controlled. If no date is provided, the program defaults to the **workstation system date (today)**.

**Limitation:** This program does **not** support components that require Serial Control.

### Edit & Post Material Issues

**Purpose.** Review, edit, and post imported material issue transactions to work order files.

**General operation.**
- The program opens with a list of all **unposted transactions**.
- Select any transaction that needs editing.
- Click **REPORT** to print a report of all unposted transactions.
- Once all transactions are correct, click **POST**. You can filter the posting by **Work Order number** and **date range**.
- After posting, a report is generated listing any transactions that were not posted. Possible reasons for non-posting:
  - GL Close Date restriction.
  - Closed Work Order.
  - Invalid Part Number.
  - Lot or Serial Control required.

---

## DE-L — Import & Post Work Order Receipts

*Source: [de-l-a_import_post_work_order_receipts.htm](../../../samples/chm/extracted/de-l-a_import_post_work_order_receipts.htm)*

**Purpose.** Import Work Order Receipt data collected by an external system (such as a bar code data collection device), edit it, and post it to Work Order files. Comprises two sub-programs: Import Work Order Receipts and Edit & Post Work Order Receipts.

### Import Work Order Receipts

**Purpose.** Load work order receipt records from an external collection file into EvoERP's staging area.

**General operation.** Follow the general import instructions in *Importing Master Files*. All fields are required **except** the **Lot Number** for items that are not Lot Controlled. If no date is provided, the program defaults to the **workstation system date (today)**.

**Limitation:** This program does **not** support items that require Serial Control.

### Edit & Post Work Order Receipts

**Purpose.** Review, edit, and post imported Work Order Receipts to work order files.

**General operation.**
- The program opens with a list of all **unposted transactions**.
- Select any transaction that needs editing.
- Click **REPORT** to print a report of unposted transactions.
- Once all transactions are correct, click **POST**. You can filter the posting by **Work Order number** and **date range**.
- Posting behavior follows the defaults established in **SD-B Work Order Defaults**, including:
  - Standard vs. actual costing.
  - Whether to backflush BOM components automatically.
  - Whether to close the Work Order when total quantity complete meets or exceeds the Work Order start quantity.

**Critical warning:** Do **not** use this program with backflushing turned on if any component on the work order bill of material requires Lot or Serial Control — this combination is not supported and will cause problems.

After posting, a report is generated listing transactions that could not be posted. Possible reasons:
- GL Close Date restriction.
- Closed Work Order.
- Lot or Serial Control of the finished item required.

---

## DE-M — Import Physical Inventory Counts

*Source: [de-m_import_physical_inventory_counts.htm](../../../samples/chm/extracted/de-m_import_physical_inventory_counts.htm)*

**Purpose.** Import Physical Inventory Count data obtained from an external collection system such as a bar code data collection device.

**General operation.** Specify the **Year** and **Quarter** of the Physical Inventory and the **count date**. Define the field positions in the import file following the standard data import rules for comma-delimited or fixed-length files (as described in *Importing Manufacturing Data*). Required fields:

- **Tag Number** (or an incremental line counter number).
- **Location**.
- **Part Number**.
- **Quantity Counted**.

Optional fields:
- **Employee Number**.
- **Bin Location**.

Press Enter or Tab through all fields, or press **F10** to process. A report is generated listing all imported items and flagging any exceptions that must be manually entered.

**Limitation:** While manually entered Physical Inventory counts support Serial Control, imported counts do **not** support serialized items.

---

## DE-T — Import Web Storefront Orders

*Source: [de-t_impoer_web_storefront_ord.htm](../../../samples/chm/extracted/de-t_impoer_web_storefront_ord.htm)*

**Purpose.** Import Sales Orders downloaded as a CSV file from a web storefront. Orders can be routed either directly into Sales Orders, or first staged as EDI orders so that error checking can be performed via ED-H Error Report before converting to Sales Orders using ED-D Convert EDI Orders to Sales Orders.

**Program setup.** The main screen must be configured with:

- **FTP login information** for the server where the storefront-generated file is located.
- **Filename** of the import file.
- **Second filename** (optional) — the original file can be renamed to this name to prevent conflicts if a new order is being saved to the file at the same time as the download.
- **Bank account** — which bank account payment records should be posted to.
- **Import target** — whether to import to the **EDI file** or directly to **Sales Orders**.

The import can be triggered manually by clicking the **Import** button, or the settings can be saved and the program scheduled as a recurring task.

**Import file format.** Click the **Imp fields** button to display the required fields. Format is CSV; single and double quotes must not appear within data values (they are reserved as text delimiters only). There are four record types, identified by the first character of each line:

- `C` — **Customer** record. Required only for new customers not yet in EvoERP.
- `H` — **Order Header** record. Required for every order.
- `L` — **Order Line** record. Required for every order line. A single header record can have multiple line records.
- `P` — **Payment** record. Required only if payment processing was performed online.

---

## DE-U — Upload Stock Balance to Web Storefront

*Source: [de-u_upload_stock_balance_to_w.htm](../../../samples/chm/extracted/de-u_upload_stock_balance_to_w.htm)*

**Purpose.** Upload current inventory stock balances to a web storefront so the storefront can display accurate available quantities.

**Program setup.** The main screen must be configured with:

- **FTP login information** for the server where the file will be uploaded.
- **Filename** for the upload file.

**Upload file format.** A two-column CSV containing **Part Number** and **Quantity**. The quantity uploaded represents items available for sale on the website, calculated as:

> On-Hand quantity  
> minus Sales Orders scheduled to ship within a specified number of days  
> minus Reserve Quantity  
> optionally including or excluding backorders (configurable)

**Filtering which items are uploaded.** If you define a User Defined field in SM-P-E Define Inventory User Defined Fields labeled `Web Inventory` as a single-character Y/N flag, and set it to `Y` for the items you want to expose on the web storefront, only those items will be included in the upload. Items without the flag or with the flag set to `N` are excluded.

---

## Cross-references

| DE Program | Touches / Depends On |
|---|---|
| DE-A SQL Query/Export | All modules (read-only query across any EVO data file) |
| DE-B Import Inventory | IN (Inventory), SM-C (Item Classes), AP (Vendors), AR (Customers) |
| DE-C Import Bills of Material | BM/IN (BOM master, inventory master) |
| DE-D Import Routings | RO-C (Work Centers), IN (inventory master) |
| DE-E Import Customers | AR (Accounts Receivable customer master) |
| DE-F Import Vendors | AP (Accounts Payable vendor master) |
| DE-G Import Chart of Accounts | GL (General Ledger chart of accounts) |
| DE-H Global Field Change | IN, AR, AP, GL (whichever of the four supported files is selected) |
| DE-I Erase Files | All import staging areas; shares labor file with WO-M and Data Collection |
| DE-J Import & Post Labor | WO (Work Orders), SM-G (Employees), Data Collection / WO-M |
| DE-K Import & Post Material Issues | WO (Work Orders), IN (Inventory), GL (close date) |
| DE-L Import & Post Work Order Receipts | WO (Work Orders), IN (Inventory), GL (close date), SD-B (WO defaults) |
| DE-M Import Physical Inventory Counts | PI (Physical Inventory), IN (Inventory) |
| DE-T Import Web Storefront Orders | SO/EDI (Sales Orders, ED-H, ED-D), AR (Customers), bank accounts |
| DE-U Upload Stock Balance to Web Storefront | IN (Inventory on-hand), SO (open orders), SM-P-E (UDF definition) |
