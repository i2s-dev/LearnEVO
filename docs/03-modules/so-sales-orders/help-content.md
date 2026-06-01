# SO — Sales Orders

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Sales Orders (51 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Sales Orders module is the primary customer-facing transaction engine in EvoERP. It handles the complete order-to-cash cycle: entering customer orders, printing acknowledgments and shipping documents, releasing line items to shipping, printing and posting invoices, managing recurring orders, converting orders to work orders, handling quotations, maintaining the pricing database (base prices, price codes, discount codes, and contract prices), and voiding posted invoices. Multiple invoices can be generated from a single sales order; backorders are tracked automatically. The module integrates tightly with AR (accounts receivable), IN (inventory), WO (work orders), PO (purchase orders), and the CS (commissions) subsystem.

---

## Contents

- [SO-A — Enter Sales Orders](#so-a--enter-sales-orders)
- [SO-B — Print Acknowledgments](#so-b--print-acknowledgments)
- [SO-C — Print Packing Slips](#so-c--print-packing-slips)
- [SO-D — Print Shipping Labels](#so-d--print-shipping-labels)
- [SO-E — Release Sales Orders](#so-e--release-sales-orders)
- [SO-F — Print Invoices](#so-f--print-invoices)
- [SO-G — Post Invoices](#so-g--post-invoices)
- [SO-H — Display Invoice History](#so-h--display-invoice-history)
- [SO-I — Customer Service Inquiry](#so-i--customer-service-inquiry)
- [SO-J — Enter Recurring Sales Orders](#so-j--enter-recurring-sales-orders)
- [SO-K — Generate Recurring Sales Orders](#so-k--generate-recurring-sales-orders)
- [SO-N — Convert Sales Orders to Work Orders](#so-n--convert-sales-orders-to-work-orders)
- [SO-O-A — Print Open Sales Order Listing](#so-o-a--print-open-sales-order-listing)
- [SO-O-B — Print Backorder Listing](#so-o-b--print-backorder-listing)
- [SO-O-C — Reprint Invoice](#so-o-c--reprint-invoice)
- [SO-O-D — Print Commissions by Sales Order](#so-o-d--print-commissions-by-sales-order)
- [SO-O-E — Print Shipping Schedule](#so-o-e--print-shipping-schedule)
- [SO-O-F — Print Available to Ship](#so-o-f--print-available-to-ship)
- [SO-O-G — Print Sales Order/Work Order Schedule](#so-o-g--print-sales-orderwork-order-schedule)
- [SO-O-H — Print Invoice Listing](#so-o-h--print-invoice-listing)
- [SO-O-I — Print Released Sales Orders](#so-o-i--print-released-sales-orders)
- [SO-O-J — Print User-Defined Detail](#so-o-j--print-user-defined-detail)
- [SO-O-K — Print User Defined Summary](#so-o-k--print-user-defined-summary)
- [SO-O-M — Print Changes to Sales Orders](#so-o-m--print-changes-to-sales-orders)
- [SO-O-N — Print OnTime Shipping Report](#so-o-n--print-ontime-shipping-report)
- [SO-P-A — Enter Sales Quotations](#so-p-a--enter-sales-quotations)
- [SO-P-B — Print Sales Quotations](#so-p-b--print-sales-quotations)
- [SO-P-C — Convert Sales Quotations](#so-p-c--convert-sales-quotations)
- [SO-P-D — Sales Quotation Detail Report](#so-p-d--sales-quotation-detail-report)
- [SO-P-E — Sales Quotation Summary Report](#so-p-e--sales-quotation-summary-report)
- [SO-P-F — Release Blanket Order](#so-p-f--release-blanket-order)
- [SO-P-I — Enter Freight & Tracking #](#so-p-i--enter-freight--tracking-)
- [SO-P-J — Post Shipped Items](#so-p-j--post-shipped-items)
- [SO-P-K — Edit Posted Invoice](#so-p-k--edit-posted-invoice)
- [SO-P-L — Print Changes to Quotes](#so-p-l--print-changes-to-quotes)
- [SO-P-M — Converted Quote Report](#so-p-m--converted-quote-report)
- [SO-P-N — Convert SO to PO](#so-p-n--convert-so-to-po)
- [SO-P-P — Edit Estimated Ship Dates](#so-p-p--edit-estimated-ship-dates)
- [SO-Q-A — Enter Base Prices](#so-q-a--enter-base-prices)
- [SO-Q-B — Print Base Prices](#so-q-b--print-base-prices)
- [SO-Q-C — Global Price Change](#so-q-c--global-price-change)
- [SO-Q-D — Enter Price Codes](#so-q-d--enter-price-codes)
- [SO-Q-E — Print Price Codes](#so-q-e--print-price-codes)
- [SO-Q-F — Enter Discount Codes](#so-q-f--enter-discount-codes)
- [SO-Q-G — Print Discount Codes](#so-q-g--print-discount-codes)
- [SO-Q-H — Enter Contract Prices](#so-q-h--enter-contract-prices)
- [SO-Q-I — Print Contract Prices](#so-q-i--print-contract-prices)
- [SO-Q-J — Generate Base Prices](#so-q-j--generate-base-prices)
- [SO-R — Void Invoice](#so-r--void-invoice)
- [SO-S — Mass Release Sales Orders](#so-s--mass-release-sales-orders)
- [SO-T — View Sales Orders](#so-t--view-sales-orders)

---

## SO-A — Enter Sales Orders

*Source: [so-a_enter_sales_orders.htm](../../../samples/chm/extracted/so-a_enter_sales_orders.htm)*

**Purpose.** Use this program to enter and modify sales order records for customers. A sales order can include both regular and non-inventory items. All shipping documents and invoices are printed from the information entered here. The program can optionally check stock and automatically track backorders. Multiple invoices can be generated from a single sales order.

### Header Screen Fields

**SO No. (Required)** — The sales order number. Normally left blank; the program assigns the next number (stored in DEF-R Assign Next Numbers) when the order is saved. You may enter a number manually; you will be asked whether to reset the system SO# counter. If a number already in use is entered, you are advised to choose another. Existing orders appear in a lookup window at startup (if enabled in US-A Customize Settings); use the **Find** button or press F2 to locate a specific order; use **Add** (or Insert) to create a new one.

**SO Date** — Defaults to today's date; can be overridden.

**Last Invoice** — Memo field showing the last invoice processed against this order. Read-only.

**Entered by** — 5-character alphanumeric. Defaults from SD-M Sales Order Defaults (can be set to the login ID of the entering user).

**Customer (Required)** — Bill-to customer code. Press F2 or click the lookup icon to select. On entry the program checks credit hold status; if on hold a message is presented (suppressible in SD-M). You can also configure warnings for open invoices older than a specified number of days or past-due amounts. If an unknown customer code is entered, the AR-A Enter Customers screen opens for on-the-fly setup.

**Name, Address, City, St, Zip, Country** — Default from the customer master record (AR-A); can be overridden for this order without affecting the master.

**Attention** — Person from the bill-to account; defaults from *Contact 1* in the customer master.

**Ship to** — If different from bill-to, enter here. After the bill-to customer is entered, bill-to information pre-fills the Ship to area as a convenience. If a default Ship-to Code is defined in AR-A for this customer, that account's information auto-fills. Press F2 to select an alternate ship-to. If *Control Ship To based on Bill To* is set to Y in SD-M, the lookup shows only ship-to customers assigned to the current bill-to customer. Multiple ship-to records are maintained by creating multiple customer records in AR-A.

**Attention (Ship to)** — Contact at the ship-to address; defaults from *Contact 1* in the ship-to customer record. Prints on shipping labels.

**Ord Desc** — General description for this order (optional, 30 characters). Prints on reports and customer statements. If blank the system prints a default cross-reference to the invoice and SO numbers.

**Cust PO** — Customer purchase order number (25 characters). Prints on shipping labels and appears on reports. A duplicate PO warning can be enabled; orders with PO = `VERBAL` are excluded from the duplicate check.

**Location** — If using multiple inventory locations (set up in IN-L-B), enter the location here. Press F2 to select. See "How to Use Multiple Locations" for details. Can also be overridden at the line item level if enabled in SD-M.

**Terms Cd (Required)** — Payment terms code; defaults from the customer master. Up to 20 terms codes are defined in SM-D Enter Terms Table. Press F2 to select.

**FOB** — Freight On Board designation; prints on sales order documents. Defaults first from AR-A Enter Customers, then from SD-M Sales Order Defaults.

**Job No** — Master job number used as a report filter across sales orders, purchase orders, and work orders that belong to a common project.

**GL Dept** — Optional GL department code. Posts income/expense to a specific department in the chart of accounts. Does not affect balance sheet accounts (e.g., AR). If entered, any Item Class or system-default GL account with a blank department will be posted using this department; non-blank departments in Item Class or system defaults are not overridden. Access and whether entry is required are controlled in SD-M.

**Price Cd** — Default price code from the customer master (AR-A). Can be overridden for this order.

**Discnt Cd** — Default discount code from the customer master. Can be overridden for this order. Press F2 to select. Applies to base prices, price code prices, and manually entered prices; does not apply to contract prices. A negative discount acts as a surcharge/upcharge; to enter more than 9.99% negative, enable *Enable Up Charges in Discounts* in SD-M.

**Slsp1** — First salesperson code (4-digit numeric). Defaults from the customer master (bill-to, then ship-to if defined). Priority logic: default salesperson from SD-M → bill-to customer salesperson (AR-A) → ship-to customer salesperson (if any). If SD-N Sales Commissions Defaults allows it, a commission percentage displays to the right; defaults from the customer master or from CS-A Enter Salespersons. Up to two salespeople may be designated per order.

**Slsp2** — Second salesperson, same logic as Slsp1. Commission percentage shows if SD-N permits.

**Ship Via** — Method of shipment (15 characters). Defaults first from AR-A, then from SD-M.

**Taxable** — Defaults from AR-A. If `Y`, the customer's *Tax Group* auto-fills the **By** field and the rate fills the **Rate** field. If `N`, no tax rate is shown. If some lines are taxable and others are not, enter `Y` here and control taxability at the line level. Can also be set to `H` to put the order on hold, preventing release in SO-E.

**By** — Tax group applied to this order. Defaults from the ship-to customer's master record (because the ship-to destination determines tax liability). Press F2 to select. Even for non-taxable orders a tax authority can be assigned for Sales Tax report inclusion. The tax authority message can be suppressed in SD-M.

**Rate** — Tax rate for the tax group in the *By* field. Calculated automatically; cannot be overridden.

**Currency** — If multi-currency processing is enabled (IM-A International Configuration), defaults from the currency code in AR-A. Can be overridden for this order.

**Drop Shipment** — Flag indicating the order ships to a customer different from the ordering customer.

**Ready to Invoice?** — Controls stock checking and instant invoicing. `Y`: the program checks stock as line items are entered and inserts on-hand units in **Ship Qty**; excess units go to **Backord Qty**; **Release?** is set to `Y` automatically, allowing invoicing without running SO-E. `N`: stock checking is suppressed; quantities can be entered freely; **Release?** is set to `N`, requiring SO-E to release. `H`: places the order on hold, preventing release in SO-E. Default controlled by SD-M. If *Calc BO on Available to Ship?* is set to `Y` in SD-M, the program will backorder any quantity exceeding on-hand less existing on-SO and on-BO quantities, regardless of the Ready to Invoice? setting.

**Subtotal** — Sum of line item extensions before tax and freight (11 digits, 2 decimal).

**Tax** — Calculated sales tax (computed when the order is saved).

**Freight** — Freight charge. Prompted each time the order is saved; can also be entered later in SO-E or SO-P-I.

**Total** — Subtotal + Tax + Freight.

### Import Lines

Before advancing to the line item screen, a green-circle import button is available. Click it to import lines from a CSV file. You are prompted for the file name, date format, and which columns map to Item Number, Description, Quantity, Price, and Estimated Receipt Date. Price and description are pulled from the item master and customer pricing if not included in the import.

### Line Items Screen

Accessed by clicking **Line Item Screen** (or PgDn), or by advancing past the *Ready to Invoice?* field. Navigation buttons: **Display Lines** (F2) — shows all lines in a lookup; **First** (F5), **Last** (F6), **Next** (F8), **Prev** (F7) — move through lines; **Add** (End) — clears for a new entry. Current line number shows in the **Line #** field.

### Line Item Entry Fields

**Lin** — Optional 3-character alphanumeric line code. Used to reference a customer PO line number (common with government contracts) or to designate kit components (`K`) and manufactured options (`M`) for the Features & Options module.

**Item number** — Inventory item number (set up in IN-B). Press F2 or click Lookup to select. On entry the product description displays and can be overridden for this order without affecting the master. Pressing Enter through a blank item number creates a **comment line** allowing free-form description text but no quantity or price. Inventory stock status (on SO, on BO, on PO, in QC, on WO, allocated) can be viewed by clicking **Stock Status** while in the item number lookup, or while in the Ship Qty or Backord Qty fields.

**Description** — From IN-B; can be overridden for this order.

**Location** — Editable at the line item level if enabled in SD-M.

**Ship Qty** — Number of units to ship. If *Ready to Invoice?* is `Y`, cannot exceed on-hand units. If `N`, any quantity is allowed. If *Calc BO on Available to Ship?* is `Y` in SD-M, excess quantity is automatically backordered. Default display: 1.00 (11 characters, 2 decimal).

**Backord Qty** — Units not available to ship. Auto-filled if *Ready to Invoice?* is `Y` and ordered quantity exceeds on-hand. In SO-E mode, unshipped units from released orders move here automatically.

**Price** — Unit price. Can be: price code price, base price from the inventory master, contract price, or a manually entered price (12 characters, 4 decimal). Per-thousand pricing uses `M` in the Price UM; per-hundred uses `C` or `H`. `LOT` or `MIN` designates a lot or minimum charge (unit price not multiplied by quantity). Access to this field can be locked in SD-M. After quantity entry, price may change if quantity price breaks apply; press F2 while in Price to see the price structure.

**UM** — Price unit of measure from the inventory master (`M` = per thousand, `C`/`H` = per hundred, `LOT`/`MIN` = lot/minimum charge).

**Disc** — Discount percentage from the discount code assigned to the customer. Based on item class and dollar amount. Discounts do not apply to contract prices. Can be manually entered or overridden. 4-digit numeric, 2 decimal (10% = `10.00`). Negative entry applies a surcharge; for more than 9.99% negative, enable *Enable Up Charges in Discounts* in SD-M.

**Tax?** — Per-line taxability flag. Available if the order header *Taxable?* is `Y`. Defaults from the *Taxable?* field in IN-B for this item. Always `N` if the header is `N`.

**Release?** — Per-line ready-to-ship flag. If header *Ready to Invoice?* is `Y`, auto-set to `Y` for any line with a Ship Qty. Otherwise set to `N` until released via SO-E. Resets to `N` after posting.

**Est Shp** — Estimated ship date for this line. Defaults to today; whatever date is entered on the first line repeats on subsequent lines. Used by the Material Requirements module for production planning, by SO-N to determine WO finish dates, and as a filter/sort key in reports. If a prior date is entered a warning is presented. Use the **Duplicate** button (F7) to repeat a line item with different quantities and dates (for blanket/scheduled orders).

**Cust Due Date** — Customer-committed delivery date. May differ from the Estimated Ship Date. If *Ship Time* is defined for the customer in AR-A, the program skips the Est Ship date and calculates it by working backward from the Customer Due Date.

**Status** — Entering `B` designates this as the master line of a Blanket Order, which can later be released into multiple shipments using SO-P-F Release Blanket Order.

**ECO Info** — Button enabled if *Use ECO* is set to `Y` in SD-H Inventory Defaults. Allows specifying a revision level for this SO line; optionally prints on Invoice and Acknowledgment.

### General Program Operation

**Entering a New Order:** Click **Add** (or Insert). The blue banner reads *Add New Sales Order*. Leave SO No. blank to auto-assign. Enter the customer code; defaults populate the header. Advance to line item entry via **Line Item Screen** (PgDn) or by tabbing past *Ready to Invoice?*.

**On-the-fly customer setup:** If you enter an unknown customer code, AR-A opens automatically; after saving the new customer record you are returned to SO-A.

**Line item entry details:** Enter item number, quantity, verify price (may adjust for quantity breaks), discount, tax flag, Release? flag, and estimated ship dates. Comment lines (blank item number) allow free-form text or blank separators. Specifications from the inventory master are optionally pulled in as comment lines. Customer cross-references (IN-L-C) auto-insert the customer's own item number as comment lines following the item.

**Changing a line:** Use Display Lines (F2) or navigation buttons to bring the line into the entry area. Change any field except Item number (to change the item, delete the line and add a new one). If the Estimated Ship Date is changed, you are prompted to apply the new date to all lines with the same old date.

**Deleting a line:** Bring the line into the entry area and click **Delete** (F4). Comment/specification lines associated with the item are not auto-deleted; delete them individually.

**Inserting a line:** Bring the line you want to insert in *front of* into the entry area and click **Insert** (F3). Associated specs, cross-references, kit components, and Features & Options selections are included in the insert.

**Duplicating lines (blanket/scheduled orders):** After entering a line and any following comment lines, click **Duplicate** (F7). The line is duplicated with cursor at the Est Shp field for a new date. Option to duplicate comment lines.

**Sales Order Notes:** Press **SO Notes** (Home) from anywhere on the header or line item screen. Up to 99 lines of free-form text. Can be marked as Hidden (internal only, not printed on customer documents). Individual note lines can each be toggled hidden/visible. Notes can be inserted from the Bill-to or Ship-to customer's AR-A notes on save.

**Saving the order:** Click **Save SO** (F10). You are prompted for freight. On save, inventory *units on sales order* and *units on backorder* are updated in the inventory master and location files. If *Sales Document printing* is enabled in SD-M, you are prompted to print acknowledgment, packing slip, and/or invoice.

**All-backordered with Ready to Invoice? = Y:** Prompted whether to release as freight-only invoice, or to reset Ready to Invoice? to `N`.

**Editing an existing order:** Orders editable as long as unposted items remain. Once fully invoiced and posted (SO-G), the order is marked closed and is subject to purging via SM-J-J. Cannot edit a sales order marked as printed until the invoice is un-marked (reprint via SO-F and answer N to the mark-as-printed prompt). Closed orders can be reopened (controlled by DEF-M).

**Deleting a sales order:** From the opening screen, highlight the order and click **Delete** (F4). Reverses inventory updates made on save.

**Reopening a closed order:** Select the closed order (marked `C`). Prompted to reopen. After editing and saving, if no unbilled quantities remain, prompted to close it again.

**Credit memos:** Enter negative quantities. Invoices with a negative total print as *CREDIT MEMO*. If inventory return is intended, use the actual item number; for non-inventory credits use a non-inventory item. Use SO credit memos (not AR-B vouchers) when the transaction affects inventory or commissions.

**Features & Options:** Options-based bill-of-material module. During line item entry, option windows appear for selection; selected options are inserted as child lines after the parent. Options can be itemized or added to the parent price. After the order is saved it can be converted to a work order via SO-N.

**Absorbed sales tax:** For industries where tax is built into prices, set *Prompt for Itemized Sales Tax?* to `Y` in SD-M. On save, you choose whether to itemize tax on the invoice. When non-itemized tax is posted, each line's sales GL account is credited net of tax, and the sales tax GL account is credited separately.

---

## SO-B — Print Acknowledgments

*Source: [so-b_print_acknowledgments.htm](../../../samples/chm/extracted/so-b_print_acknowledgments.htm)*

**Purpose.** Print a sales order acknowledgment to send to customers as verification of their orders, or use as an internal file copy. Can be printed on the universal form or on plain paper (format defined in SD-M). The acknowledgment shows the SO header information plus item number, description, unit price, unit of measure, discount, extension, and estimated ship date.

**Operation.** Enter a from/thru range of SO numbers or select from a lookup. If no limits are entered, all open and unpurged closed SOs are printed. Options include: whether to print hidden SO notes; whether to print Features & Options selections; whether to include sales tax and freight; whether to include linked documents.

**Configuration saving:** If SD-A Company Defaults allows configuration changes (setting 1 or 2), a **Save Settings** button appears after all Y/N options are completed. System-level changes may require a password. User-level settings are saved to the workstation.

---

## SO-C — Print Packing Slips

*Source: [so-c_print_packing_slips.htm](../../../samples/chm/extracted/so-c_print_packing_slips.htm)*

**Purpose.** Print shipping documents that accompany merchandise. A copy is returned for invoicing. Can be printed on the universal form or plain paper (format from SD-M). Shows quantity ordered, quantity available to ship, bin location, backorder quantities (or single-quantity format showing only ship qty). Fields for freight/insurance charges, total weight, and cubic feet. Dated and numbered with a shipper number for tracking.

**Operation.**

- Choose to print new packing slips or reprint from a previously posted invoice.
- Limit by sales order range. No limits = all open SOs.
- **Use existing SO Ship Dates:** If `Y` and no ship date was entered in SO-E, uses the Estimated Ship Date from the first line.
- **Print order:** Line Number, Item Number, or Bin Location order (default: Line Item; press F2 to change).
- **Print Non-released Lines?:** `Y` = include all items; `N` = only released items.
- **Date range for blanket orders:** Restrict by *Include only Ship Dates From/Thru* for blanket-order line filtering.
- **Single quantity format:** Choose between showing only Ship Qty (`N` to *Include BO's in Qty this Shipment?*) or Ship Qty + Backord Qty combined (`Y`).
- Options for printing SO notes, selling kit components, comments after shipped items, and Features & Options selections (with or without option quantities).
- Lot Control / Serial Control: optionally print lot/serial listings.
- Linked documents: option to include.
- Warehouse Control options: list all bin locations or only the default; print multiple packing slips by warehouse location.
- **Use Standard Pack:** divides Ship Qty by item Standard Pack to show carton count.
- **Print Consolidated:** combines multiple instances of the same item into a single line.
- **One Kit per page:** splits Selling Kits onto separate pages.

---

## SO-D — Print Shipping Labels

*Source: [so-d_print_shipping_labels.htm](../../../samples/chm/extracted/so-d_print_shipping_labels.htm)*

**Purpose.** Print ship-to information on standard 3 x 5 shipping labels for orders not yet posted or for previously posted invoices. Both Header and Detail label formats are available as graphical forms editable in TA-M Forms Editor.

- **Header label** includes: ship-to name/address, phone, fax, attention line, customer PO number, Job Number, Order Description, FOB, Ship Via.
- **Detail label** includes: item number (text and barcode), description, invoice number, quantity, price.

**Operation.** Enter a range of SO numbers or ship dates. No limits = all open SOs (or all released orders if non-released lines excluded). Specify the number of labels per invoice and choose Header or Detail. Option to include linked documents.

---

## SO-E — Release Sales Orders

*Source: [so-e_release_sales_orders.htm](../../../samples/chm/extracted/so-e_release_sales_orders.htm)*

**Purpose.** Release individual sales order line items for invoicing or for selective printing on packing slips. The program checks stock and automatically backordered items not available to ship. Quantities and backorder quantities can be overridden. When items are released, the *Ready to Invoice?* flag is set to `Y` in the header and each released line's *Release?* flag is set to `Y`.

**Key GL/inventory impact:** SO-E itself does not post to GL. It is a preparatory step. Actual GL impact occurs in SO-G Post Invoices.

**Operation:**

1. Enter the SO number or press F2 to choose from open SOs. The header displays. A **Ship To** button allows reviewing and editing the ship-to address (useful when an order has multiple shipments to different destinations).
2. **Release all Lines?** — If Yes, cursor advances to *Include Backorders?* (whether to move BO quantities into Ship Qty) and *Release thru Est Date* (release lines up through a specific Estimated Ship Date — useful for blanket/scheduled orders).
3. **Display Comment Lines?** — Whether comment lines appear in the display and entry area.
4. **Auto Release Comments?** — Automatically release comment lines following each released line item.
5. **Display Shipped Lines?** — Whether completely shipped lines appear.
6. Click **Release** to display the line items.
7. In the line item area, check the **Release?** box for lines to release. To change quantities, highlight the line and click **Edit**: enter the Ship Qty; remaining units go to Backorder. The *Release Qtys Greater than On Hand* setting in SD-M controls whether the system warns or prohibits over-release. Save each line, then click **Save** when all lines are correct.

**Entering Shipping Information (after line item save):**

- **Ship Via** — Update if changed since order entry.
- **Shipper Number** — Auto-assigned by the system; can be overridden. Next shipper number set in SD-R Assign Next Numbers. If *Set Invoice same as Pack Slip* = `Y` in SD-M, invoice number and shipper number are set equal.
- **Ship Date** — Optional. If blank, invoices are assigned a ship date when printed via SO-F.
- **Freight** — Enter freight charge if applicable.
- **Tracking #** — If *Enter Ship Tracking # in SO-E?* = `Y` in SD-M, prompted for tracking number (up to 40 characters) and freight carrier; prints on pack slip and invoice.

**Features & Options:** When releasing a partial quantity on a parent product, you are asked whether to change all option quantities proportionately.

**Selling Kits:** Same proportionate release logic applies to kit components.

**Retention Billing:** Enabled when *Prompt for Retention Billing?* = `Y` in SD-M and a retention item number is configured.
- After releasing and saving, you are asked *Do you wish to bill for retention?*
- If Yes, enter a retention percentage (e.g., `15.00` for 15%).
- Choose whether to invoice the retention immediately (Ready to Invoice? = `Y`) or defer (Ready to Invoice? = `N`).
- The originating invoice prints *Less Retention* in the totals section, deducting the retention amount from the invoice.
- A new SO is created for the retention amount using the configured retention item number, with a comment line cross-referencing the originating invoice number.
- **GL postings on originating invoice post:** AR is credited by the retention amount; the Retention GL account (from the retention item's item class) is debited.
- **GL postings on retention invoice post:** AR is debited; the Retention GL account is credited (bringing it back to zero).

---

## SO-F — Print Invoices

*Source: [so-f_print_invoices.htm](../../../samples/chm/extracted/so-f_print_invoices.htm)*

**Purpose.** Print invoices for released sales order items (screen, printer, email, or file). An invoice must be printed (and marked as printed) before it can be posted in SO-G. Until posted, the invoice can be reprinted and new items can be added to the original SO. Print format is set in SD-M. Only line items with ship quantities and `Release? = Y` print; backordered and unreleased items do not print.

After printing you are asked *Mark these Invoices as Printed?* If `Y`, the invoices are marked and are ready for SO-G. Once marked, no changes can be made to the SO until the invoice is either posted or un-marked.

**To un-mark (reopen for editing):** Reprint the invoice (even just to screen) and answer `N` to *Mark these Invoices as Printed?*

**Operation:**

1. Choose **new (unposted) invoices** or **reprint previously posted invoices**.
2. **Print Invoice Date same as Ship Date?** — If `Y`, invoice date = ship date from SO-E (or from SO-C if entered there; if neither, uses the Estimated Ship Date from the first line). If `N`, enter Invoice Date and Ship Date separately.
3. **Print all SO's not yet Printed?** — `Y` = batch-print all released unprinted SOs. `N` = specify a range of SO numbers.
4. Options for printing kit components, comments after shipped items, SO notes, Features & Options, and linked documents.
5. Output destination: screen, printer, email, or file.
6. **Deposits:** If a deposit is linked (AR-N Enter/Print Sales Order Deposits), you are prompted to apply the available deposit amount.

**Reprinting posted invoices:** Enter invoice number range. Choose whether to include kit components, comments, notes, options. Choose among SO invoices, AR vouchers, and finance charges. Note: lines with 0 ship quantity are not saved in the posted invoice file unless *Create 0 Qty SO Lines during Post?* = `Y` in DEF-M Sales Order Defaults.

---

## SO-G — Post Invoices

*Source: [so-g_post_invoices.htm](../../../samples/chm/extracted/so-g_post_invoices.htm)*

**Purpose.** Post invoices that have been marked as printed in SO-F. This is the transaction that creates all permanent GL, inventory, AR, and commission records.

**GL and data impacts on posting:**
- Customer outstanding invoice balance updated (AR).
- Inventory: units on SO, units on hand, and last sale date updated in both the inventory master and inventory location records.
- Sales taxes posted to the appropriate tax codes.
- Salesperson records updated: gross sales, COGS, and commissions due.
- A copy of the invoice saved in the invoice history file.
- If payment terms are a cash type, the check register is updated.

**Multi-currency:** If a foreign currency code was entered in the SO header, each line's revenue and cost are converted from source currency to base currency using the closest historical exchange rates to the invoice date. Inventory, Sales, COGS, and Sales Tax Payable GL accounts receive base-currency postings; the currency's AR Control account receives source-currency postings. The difference is posted to the F/E Transactions account (set up in IM-B Enter Multiple Currencies).

**Operation:**

1. **Post all Printed Invoices?** — `Y` = post all unposted marked-as-printed invoices. `N` = specify a range of SO numbers and/or invoice numbers.
2. Before posting starts, you can optionally run a COGS report and a sales commission report to review figures before final commit.
3. The invoice date printed on the invoice is the posting date.

**Inventory Record Locks:** If another user has an inventory record locked during posting, the data is saved in a temporary file. After posting completes, you are prompted to retry. If still locked, use SO-P-J Post Shipped Items, IN-L-S Rebuild Stock Status, or IN-A Inventory Inquiry to manually process.

---

## SO-H — Display Invoice History

*Source: [so-h_display_invoice_history.htm](../../../samples/chm/extracted/so-h_display_invoice_history.htm)*

**Purpose.** View posted invoices one at a time, or reactivate a posted invoice back into a live sales order.

**Operation.** Enter an invoice number or press F2 to choose from a lookup of posted invoices. All fields are read-only. Click **Lines** to view line items; click **Header** to return. Click **Notes** to display associated notes. Two print options are available to get a printed simulation.

**Converting a history invoice to a live sales order:** Click **Copy**. Either enter a specific SO number or let the system assign the next available number. Press Enter to process. Note: all dates on the copied order retain the original invoice dates — edit them in SO-A after conversion.

---

## SO-I — Customer Service Inquiry

*Source: [so-i_customer_service_inquiry.htm](../../../samples/chm/extracted/so-i_customer_service_inquiry.htm)*

**Purpose.** All-purpose inquiry into the order status of a particular customer. With one set of selection criteria you can check open sales orders, recent shipments, open work orders, and inventory status.

**Operation.** The main screen starts with either a **Customer** selection or an **Item (Stock Check)** selection. Each selection opens a new tab so multiple customers and items can be viewed simultaneously.

**Customer tab:** Find by any combination of Customer Code, Name, Telephone Number, Email Address, PO Number, or Invoice Number. Click **Find Customer**. If unique match, data populates. If multiple matches, a selection list appears. Bottom tabs: **Orders**, **Invoices**, **Payments**, **Work Orders**, **RMA**. The RMA tab also allows creating an RMA number for the customer.

**Stock Check (Item) tab:** Click a check-stock tab to open a list of items by Item and Description. Click Description column to search by description. On item selection, a window shows current stock status (on hand, on SO, on BO, on PO, in QC, on WO, allocated) and a list of open sales orders. The right side shows item links; bottom tabs show open Work Orders, Purchase Orders, and Allocations.

---

## SO-J — Enter Recurring Sales Orders

*Source: [so-j_enter_recurring_sales_orders.htm](../../../samples/chm/extracted/so-j_enter_recurring_sales_orders.htm)*

**Purpose.** Enter a template for periodic customer transactions (e.g., monthly service calls, rentals, leases) without re-entering the full order each cycle. SO-K Generate Recurring Sales Orders uses these templates to create live sales orders on schedule.

Recurring SO numbers are assigned from the *Next Recurring SO Num* sequence in DEF-R. When generated via SO-K, they receive the next regular SO number and appear in the open sales order file as released orders ready for invoicing.

**Additional fields unique to recurring orders:**

| Field | Description |
|---|---|
| **Select Cd** | One-letter selection code (optional) used as a memory aid and to filter during SO-K generation. Examples: `S` for service, `M` for monthly. |
| **Frequency** | Times per year the transaction recurs (e.g., `52` = weekly, `12` = monthly). Used to calculate the next transaction date. Required. |
| **Limit** | Maximum number of times this transaction may be posted. When this count is reached, SO-K skips the record. Required. |
| **Next Inv** | Next scheduled invoice date, calculated from the initial date and frequency. |

All other fields are identical to SO-A Enter Sales Orders.

---

## SO-K — Generate Recurring Sales Orders

*Source: [so-k_generate_recurring_sales_order.htm](../../../samples/chm/extracted/so-k_generate_recurring_sales_order.htm)*

**Purpose.** On a regular basis, post the recurring items from SO-J to the open Sales Order file so they can be processed as invoices.

**Operation.** A list of recurring orders is presented for tagging (selection). The list can be sorted by Next Invoice Date, Customer Code, or Selection Code. Once desired orders are tagged, click **Post** and the items are placed in the sales order file, ready for printing and posting like any other invoice. A report listing the generated orders can be printed after transfer.

---

## SO-N — Convert Sales Orders to Work Orders

*Source: [so-n_convers_sales_orders_to_work_orders.htm](../../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm)*

**Purpose.** Generate work orders automatically from SO-A line items, eliminating double entry of both a sales order and a work order. Work orders are created for inventory items of type `F` (finished good) and `A` (assembly).

**Operation prompts (in order):**

| Prompt | Behavior |
|---|---|
| **Create a Multi-Yield Work Order?** | Only if a Multi-Yield placeholder part number is configured in SD-M. If `Y`, all SO lines (regardless of part number) are combined into a single WO for the placeholder. Components from all lines are added to the WO BOM; WO-I will present the SO items during multi-yield processing. |
| **Sales order number** | Enter or F2 lookup. |
| **Combine Duplicate Items into Single Work Orders?** | `Y` = consolidate same-item lines with different due dates into one WO with multiple delivery dates. `N` = separate WO per estimated ship date. |
| **Prompt for Work Order Quantity?** | If checked, a popup for each item shows inventory status (on hand, on SO, on BO, on PO, allocated, in WIP) and allows overriding the quantity. Enter `0` to skip an item. |
| **Use Inventory Lead Time for Start Date?** | If `Y`, uses inventory lead time to determine start date. If Lead Time Scheduling is enabled in SD-B (F or B), backward scheduling from the SO line's due date is always used. |
| **Use Shop Calendar to Determine Start Date?** | If `Y`, start date is moved back to a valid shop calendar day. Always `Y` if using Lead Time Scheduling. |
| **Create Work Orders for Kit Components?** | If `Y`, type-A and type-F components of Selling Kits get WOs generated. |
| **Include Non-Inventory Items?** | Controls whether type-N items receive WOs. |
| **Create Multi-Assembly Orders?** | If `Y`, automatically calls WO-K-D Create Multi-Assy Work Orders for lower-level BOM assemblies. |
| **Generate WO for SO Lines not yet generated?** | If `Y`, only newly added SO lines (not previously converted) receive WOs. |
| **Match WO Suffix to SO Line Number?** | If `Y`, WO suffix matches the SO line number. Conflicts with Create Multi-Assembly Orders; do not enable both. If a WO with the matching number already exists, the line is skipped. |
| **Use Cust Due Date or Est Ship Date as WO Due Date?** | `C` = Customer Due Date; `E` = Estimated Ship Date. |
| **Increment Work Order Suffix by {n}?** | Increment value for WO suffix numbering per SO line. Allows grouping (e.g., suffixes 1–19 = SO line 1 and its subassemblies, 20–39 = line 2, etc.). Default set in SD-M. |
| **Work Order Status for S/R WOs?** | If called by the Service/Repair module, allows a different default WO status. |
| **Include Back Order Qty (Y/N/O)?** | Y = include backordered items, N = exclude, O = only backordered items. |
| **Offset Finish Date by Days?** | Number of days before the Estimated Ship Date to set the WO Estimated Finish Date. |

**WO numbering:** The SO number becomes the WO prefix; the first line item gets suffix `-001`, subsequent lines increment by the specified amount. All WOs sharing a prefix optionally print a *Job Schedule* section on the shop traveler.

---

## SO-O-A — Print Open Sales Order Listing

*Source: [so-o-a_print_open_sales_order_listing.htm](../../../samples/chm/extracted/so-o-a_print_open_sales_order_listing.htm)*

**Purpose.** Print a listing of open sales orders. Can be sorted by customer code, item number, or sales order number.

**Header-level data shown:** Customer code, item number, sales order number, sales order description, order date.

**Line item detail (optional):** Item number and description; quantity ordered, backordered, and shipped; cost per item, discount, and extended price; estimated ship date; ready-to-ship flag.

**Filters:** From/thru ranges for SO number, customer code, customer PO, job number, and estimated ship date. Summary or detail format; option to include comments and backorder amounts.

**Estimated monthly shipments:** Optional section showing projected monthly sales by item or customer, plus company grand totals, based on estimated ship dates. Not available when sorted by SO number. Option to print grand totals only.

**Multi-currency:** If enabled, a `Currency [Base/Src]` field allows reporting in base currency (converting source-currency orders at current exchange rates) or source currency.

---

## SO-O-B — Print Backorder Listing

*Source: [so-o-b_print_backorder_listing.htm](../../../samples/chm/extracted/so-o-b_print_backorder_listing.htm)*

**Purpose.** Print a list of items currently on backorder. Sortable by shipping date (to see all products due to ship) or by item number (to see total backorder quantity by item).

**Operation.** Enter from/thru limits for item number, job number, and estimated ship date (blank = all). After entering filters, a popup asks for sort order: item number or estimated ship date.

---

## SO-O-C — Reprint Invoice

*Source: [so-o-c_reprint_invoice.htm](../../../samples/chm/extracted/so-o-c_reprint_invoice.htm)*

**Purpose.** Reprint a previously posted invoice.

**Operation.** Enter a from/thru range of invoice numbers, Customer Code or Class, Ship Date, and Sales Rep (or use F2 lookup). Options to include kit components, comments following shipped items, and SO notes. Functionally equivalent to the reprint mode in SO-F Print Invoices.

---

## SO-O-D — Print Commissions by Sales Order

*Source: [so-o-d_print_commissions_by_sales_order.htm](../../../samples/chm/extracted/so-o-d_print_commissions_by_sales_order.htm)*

**Purpose.** List commissions by line item on open sales orders. Allows review of commissions for accuracy before posting invoices.

**Operation.** Enter from/thru ranges of sales orders, customer codes, or customer PO numbers.

---

## SO-O-E — Print Shipping Schedule

*Source: [so-o-e_print_shipping_schedule.htm](../../../samples/chm/extracted/so-o-e_print_shipping_schedule.htm)*

**Purpose.** List scheduled shipments. Sortable by estimated ship date, customer, or item number. Option to include or exclude customers on credit hold.

**Operation.** Choose sort order (estimated ship date, customer, or item number). Specify whether to include subtotals and whether to include credit-hold customers. Limit by from/thru ranges of customer code, SO number, job number, item number, location, item class and category, and estimated ship date. Option to exclude Released Lines (`Y`) or only exclude released lines that have had Packing Lists printed (`P`).

---

## SO-O-F — Print Available to Ship

*Source: [so-o-f_print_available_to_ship.htm](../../../samples/chm/extracted/so-o-f_print_available_to_ship.htm)*

**Purpose.** Plan daily shipments. Lists available inventory for open sales order line items.

**Operation.** Limit by from/thru ranges of item numbers, SO numbers, job numbers, customer codes, location, item class and category, and estimated ship dates. Option to include/exclude credit-hold customers.

**Ship-complete filter:** If `Y` to *Print only items that can ship complete?*, indicate whether to require complete lines or complete orders. When partial supply is available, priority is assigned to lines with the oldest estimated ship dates.

---

## SO-O-G — Print Sales Order/Work Order Schedule

*Source: [so-o-g_print_sales_order_work_order_schedule.htm](../../../samples/chm/extracted/so-o-g_print_sales_order_work_order_schedule.htm)*

**Purpose.** Compare estimated ship dates on open sales orders with scheduled finish dates on corresponding work orders. Helps keep production dates synchronized with shipping schedules.

**Operation.** Limit by from/thru ranges of customer codes, item numbers, SO numbers, job numbers, SO estimated ship dates, WO numbers, and WO finish dates.

---

## SO-O-H — Print Invoice Listing

*Source: [so-o-h_print_invoice_listing.htm](../../../samples/chm/extracted/so-o-h_print_invoice_listing.htm)*

**Purpose.** List invoices within any date range. Separate columns for sales, tax, freight, and invoice totals.

**Operation.** Limit by from/thru ranges of invoice dates, invoice numbers, SO numbers, and customer codes.

**Multi-currency:** If enabled, `Currency [Base/Src]` allows printing in base currency using exchange rates in effect on the invoice posting date, or in source currency.

---

## SO-O-I — Print Released Sales Orders

*Source: [so-o-i_print_released_sales_orders.htm](../../../samples/chm/extracted/so-o-i_print_released_sales_orders.htm)*

**Purpose.** List sales orders that have been released for shipping/invoicing but have not yet been posted. SOs are released via SO-A or SO-E.

**Operation.** Sort by customer, item number, or SO. Options to include line item detail, options, kit components, comments, and base or source currency. Limit by from/thru ranges of customers, customer PO numbers, item numbers, estimated shipping dates, SO numbers, and currencies.

**Multi-currency:** Base-currency reporting converts source-currency orders using the exchange rate in effect on the date of the first invoice (or current rates if no invoice posted yet).

---

## SO-O-J — Print User-Defined Detail

*Source: [so-o-j_print_user_defined_detail.htm](../../../samples/chm/extracted/so-o-j_print_user_defined_detail.htm)*

**Purpose.** User-defined open SO report generator providing wide filtering and sorting options, detail-level data (similar to other detail reports). For summary data, see SO-O-K.

**Operation.** Give the report a **Report Name** (settings are saved and recalled by name). Choose Text Format, Export (ASCII without headers/page breaks), or a graphical Report Format (default `T6SOOJ1.RTM`; can be copied and customized via TA-M Modify Forms). Give the report a title and sort parameter: pre-defined (Customer, Customer Class, Salesperson, Item, Item Class) or User Defined (click **User Defined** button to define sort indexes and subtotal breaks). Enter from/thru selection fields across two screens. The primary sort is by Order Date — specify an Order Date range even when filtering by SO number to avoid full-file scans. After completing all fields, choose whether to save settings, whether to print now, and whether to include tax in the price.

**Multi-currency:** If enabled, `Currency [Base/Src]` converts orders using the closest historical exchange rate to today's date.

---

## SO-O-K — Print User Defined Summary

*Source: [so-o-k_print_user_defined_summary.htm](../../../samples/chm/extracted/so-o-k_print_user_defined_summary.htm)*

**Purpose.** User-defined open SO report generator, summary version (one line per sales order). For detail data listing each shipment, see SO-O-J.

**Operation.** Identical to SO-O-J except the default Report Format is `T6SOOK1.RTM` and totals optionally include taxes and freight. The primary sort is Order Date.

---

## SO-O-M — Print Changes to Sales Orders

*Source: [so-o-m_print_changes_to_sales_orders.htm](../../../samples/chm/extracted/so-o-m_print_changes_to_sales_orders.htm)*

**Purpose.** Print a list of changes to Sales Order lines. An audit trail of modifications.

**Operation.** Choose sort order: Sales Order Number or Change Date. Limit by from/thru ranges of customer, item number, job number, change date, and SO number. Indicate which kinds of changes to include.

---

## SO-O-N — Print OnTime Shipping Report

*Source: [so-o-n_print_ontime_shipping_report.htm](../../../samples/chm/extracted/so-o-n_print_ontime_shipping_report.htm)*

**Purpose.** Print a list of on-time delivery performance.

**Operation.** Choose sort order: Invoice Number or Post Date. Limit by from/thru ranges of customer, item number, job number, post date, SO number, and invoice number.

---

## SO-P-A — Enter Sales Quotations

*Source: [so-p-a_enter_sales_quotations.htm](../../../samples/chm/extracted/so-p-a_enter_sales_quotations.htm)*

**Purpose.** Prepare customer quotations using the standard pricing database from the Inventory module. The program is identical to SO-A Enter Sales Orders, except that a sales quotation is not a real order and does not create requirements against inventory. Quotations can also be used as template sales orders for certain products, groups, or customers, and can be converted repeatedly to live sales orders via SO-P-C.

**Operation.** Enter a quotation exactly as you would enter a sales order (see SO-A). Features & Options module is supported. To print, use SO-P-B.

---

## SO-P-B — Print Sales Quotations

*Source: [so-p-b_print_sales_quotations.htm](../../../samples/chm/extracted/so-p-b_print_sales_quotations.htm)*

**Purpose.** Print sales quotations entered via SO-P-A. Designed to print on the universal form.

**Operation.** Enter a from/thru range of quotation numbers. Indicate whether to print notes and linked documents, and whether to print Features & Options selections.

---

## SO-P-C — Convert Sales Quotations

*Source: [so-p-c_convert_sales_quotations.htm](../../../samples/chm/extracted/so-p-c_convert_sales_quotations.htm)*

**Purpose.** Convert sales quotations to live sales orders. Option to keep the quotation on file for future use/reference or delete it after conversion.

**Operation.**

1. Enter a from/thru range of quotation numbers or select via F2 lookup.
2. If the quote was entered against a Contact Manager prospect not yet in the customer file, the program creates a customer record as part of conversion.
3. For a range, choose whether to be prompted for changes to Dates, Location, and Customer PO number for each quotation as it converts.
4. Accept or override the next available SO number.
5. Enter an estimated ship date (all lines get this date; edit individual dates afterward in SO-A).
6. Enter the customer PO number and the ship-from location.
7. Indicate whether to keep the quote on file.
8. Indicate whether to close the quote after conversion.
9. Indicate whether to pass the quote number to the Sales Order as the Job Number, Order Description, or not at all.

---

## SO-P-D — Sales Quotation Detail Report

*Source: [so-p-d_sales_quotation_detail_report.htm](../../../samples/chm/extracted/so-p-d_sales_quotation_detail_report.htm)*

**Purpose.** User-defined report generator for sales quotation data, detail version (similar to SO-O-J for open SOs). For summary data, see SO-P-E.

**Operation.** Give the report a **Report Name** (settings saved by name). Choose Text Format, Export, or Report Format (default `T6SOPD1.RTM`; customizable). Assign a title and sort parameter (pre-defined or User Defined). Enter from/thru selection fields across two screens. The primary sort is Quote Date — also specify a Quote Date range when filtering by quote number to avoid full-file scans. Choose whether to save settings, print now, and whether to include tax in the price.

**Multi-currency:** Converts using the closest historical exchange rate to today's date.

---

## SO-P-E — Sales Quotation Summary Report

*Source: [so-p-e_sales_quotation_summary_report.htm](../../../samples/chm/extracted/so-p-e_sales_quotation_summary_report.htm)*

**Purpose.** User-defined report generator for sales quotation data, summary version (one line per quote). For detail data listing each item, see SO-P-D.

**Operation.** Identical to SO-P-D except the default Report Format is `T6SOPE1.RTM` and totals optionally include taxes and freight. Primary sort is Quote Date.

---

## SO-P-F — Release Blanket Order

*Source: [so-p-f_release_blanket_order.htm](../../../samples/chm/extracted/so-p-f_release_blanket_order.htm)*

**Purpose.** Split off release quantities from a lump-sum blanket order line, generating new SO lines reflecting specific release ship dates. The blanket line quantity is reduced. Released lines become available for conversion to work orders or for MRP near-term demand pickup.

**Setup:** A blanket SO has a single part number with a single line for the total blanket quantity, a far-future ship date (so it does not generate MRP demand), and a `B` in the Status field on the SO line item entry screen.

**Operation.** Enter the blanket SO number. Enter one or more release quantities and ship dates; click **Save** after each to populate the release list. When all release dates have been entered, click **Process**. The program reduces the first blanket line quantity and creates new SO lines for each release quantity and date.

---

## SO-P-I — Enter Freight & Tracking #

*Source: [so-p-i_enter_freight_tracking_number.htm](../../../samples/chm/extracted/so-p-i_enter_freight_tracking_number.htm)*

**Purpose.** Enter shipper tracking information and freight charges on released orders without returning to SO-E Release Sales Orders.

**Operation.** Enter the SO Number, Freight Charge, Tracking Number, and Carrier. Only released orders can be updated with this program.

---

## SO-P-J — Post Shipped Items

*Source: [so-p-j_post_shipped_items.htm](../../../samples/chm/extracted/so-p-j_post_shipped_items.htm)*

**Purpose.** Post items from the temporary file where they are stored when a record lock is encountered on an inventory item during SO-G Post Invoices.

**Operation.** Click **Process**. The program reports either that all items posted successfully or that record locks still exist (try again later). See also IN-L-S Rebuild Stock Status and IN-A Inventory Inquiry, which perform the same rebuild.

---

## SO-P-K — Edit Posted Invoice

*Source: [so-p-k_edit_posted_invoice.htm](../../../samples/chm/extracted/so-p-k_edit_posted_invoice.htm)*

**Purpose.** Edit non-transactional data on posted invoices without voiding and reprocessing.

**Operation.** Enter or look up the invoice number. Editable fields include Bill-to and Ship-to addresses, payment terms, and line item descriptions. Any data that would change financial or inventory transactions cannot be edited.

---

## SO-P-L — Print Changes to Quotes

*Source: [so-p-l_print_changes_to_quotes.htm](../../../samples/chm/extracted/so-p-l_print_changes_to_quotes.htm)*

**Purpose.** Print a list of changes to Sales Quote lines. Audit trail for quotation modifications.

**Operation.** Choose sort order: Sales Quote Number or Change Date. Limit by from/thru ranges of customer, item number, job number, change date, and sales quote number. Indicate which kinds of changes to include.

---

## SO-P-M — Converted Quote Report

*Source: [so-p-m_converted_quote_report.htm](../../../samples/chm/extracted/so-p-m_converted_quote_report.htm)*

**Purpose.** Print a list of sales quotes filtered by customer, date, and whether or not they have been converted to orders.

**Operation.** Select the desired filters and print.

---

## SO-P-N — Convert SO to PO

*Source: [so-p-n_convert_so_to_po.htm](../../../samples/chm/extracted/so-p-n_convert_so_to_po.htm)*

**Purpose.** Generate Purchase Orders for type `R` (purchased) items on a Sales Order or range of Sales Orders, eliminating re-entry of drop-ship or buy-to-order line items.

**Operation.** Filter by SO number, customer, date, and optionally primary vendor. PO date defaults to today. If Est Receipt Date is left blank, it maps to the SO line's Estimated Ship Date minus the number of days in the Offset field. **Auto Generate** creates PO lines only for items with a primary vendor assigned. **Review** mode allows vendor assignment and quantity editing. Choose to purchase the total SO line quantity or only the backorder quantity.

---

## SO-P-P — Edit Estimated Ship Dates

*Source: [so-p-p_edit_estimated_ship_dat.htm](../../../samples/chm/extracted/so-p-p_edit_estimated_ship_dat.htm)*

**Purpose.** Update the Estimated Ship Date of a number of Sales Orders for a single customer in bulk, without opening each order individually.

**Operation.** Enter the customer, the range of orders and existing Ship Dates to be updated, enter the new Ship Date, and click **Process**.

---

## SO-Q-A — Enter Base Prices

*Source: [so-q-a_enter_base_prices.htm](../../../samples/chm/extracted/so-q-a_enter_base_prices.htm)*

**Purpose.** Maintain base prices (list/reference prices) per item. The base price is used by the price code and contract price files as a comparison reference. When no price code or contract price exists, sales order entry uses the base price.

**Operation.** Enter or look up the item number. Enter the **Base Price**. Save the record. Base prices can also be generated in bulk via SO-Q-J.

---

## SO-Q-B — Print Base Prices

*Source: [so-q-b_print_base_price.htm](../../../samples/chm/extracted/so-q-b_print_base_price.htm)*

**Purpose.** Price list report showing base price, last cost, and gross margin percentage.

**Operation.** Filter by from/thru ranges for item numbers, categories, and item classes.

---

## SO-Q-C — Global Price Change

*Source: [so-q-c_global_price_change.htm](../../../samples/chm/extracted/so-q-c_global_price_change.htm)*

**Purpose.** Globally change a range of base prices (and optionally price code prices and contract prices) rather than changing each individually.

**Warning:** Back up files before running this program.

**Operation.**

1. Choose **Increase Prices** or **Decrease Prices**.
2. Choose **Percentage Change** or **Flat Dollar Amount Change**.
3. Enter from/thru ranges for Items, Category, Class, and Customers.
4. Enter the **Amount of price change** (10% = `10.0000`).
5. Answer: how many decimal places of precision (1–4)?
6. Answer: update price code prices that are tied to base price by percentage?
7. Answer: update contract prices that are tied to base price by percentage?
8. Click **Process**.

---

## SO-Q-D — Enter Price Codes

*Source: [so-q-d_enter_price_codes.htm](../../../samples/chm/extracted/so-q-d_enter_price_codes.htm)*

**Purpose.** Establish up to 999 separate price codes (price lists). Each customer is assigned a price code in AR-A. Examples: code 1 = retail, code 2 = dealer, code 3 = distributor, code 4 = OEM. Up to ten quantity price breaks per item per price code.

**Operation.** Enter the item number. The description and base price (if defined) display. A base (list) price must be entered — if no list prices are used, enter the first-level price as the base.

For each price break: enter the **quantity** (the upper bound for that break range) and the **price** (discount from base auto-calculates) or enter the **discount percentage** (price auto-calculates). Price breaks are cumulative: if break 1 is quantity 50 at no discount (base price), and break 2 is 75 at a reduced price, the reduced price applies to quantities 50–74. Up to 10 breaks per item; if only one is entered it applies to all quantities. Save with F10.

---

## SO-Q-E — Print Price Codes

*Source: [so-q-e_print_price_codes.htm](../../../samples/chm/extracted/so-q-e_print_price_codes.htm)*

**Purpose.** List price codes and quantity breaks.

**Operation.** Filter by from/thru ranges for item numbers and price codes. F2 lookup available.

---

## SO-Q-F — Enter Discount Codes

*Source: [so-q-f_enter_discount_codes.htm](../../../samples/chm/extracted/so-q-f_enter_discount_codes.htm)*

**Purpose.** Establish discount tables by item class. Each customer is assigned a discount code in AR-A. A discount code can mix different discount percentages for different item classes (e.g., DEALER code: 50% off complete systems, 35% off system elements, 25% off spare parts). A discount code can also be defined as **SO Total Discount** — applied to the entire order dollar amount regardless of item class, with volume breaks based on the total order amount. Discounts apply on top of price code prices (i.e., to the result of price code + quantity break). Up to 10 dollar-amount breaks per item class per code.

**Operation.** Enter the **Discount Code** (10-character alphanumeric). Enter the item class (or set SO Total Discount to `Y`). Enter an optional Start Date and End Date. Enter dollar quantity breaks and corresponding discount percentages. Example: break $100 at 25% = all amounts $0–$100 receive 25%; break $150 at 35% = amounts $101–$150 receive 35%. Save with F10. Add more item classes for the same discount code by repeating the entry with a different class.

---

## SO-Q-G — Print Discount Codes

*Source: [so-q-g_print_discount_codes.htm](../../../samples/chm/extracted/so-q-g_print_discount_codes.htm)*

**Purpose.** List discount codes and tables.

**Operation.** Filter by from/thru ranges for discount codes and item classes. F2 lookup available.

---

## SO-Q-H — Enter Contract Prices

*Source: [so-q-h_enter_contract_prices.htm](../../../samples/chm/extracted/so-q-h_enter_contract_prices.htm)*

**Purpose.** Establish special prices on specific items for individual customers. Contract prices take priority over price code prices in sales order entry (no price code price or discount is applied when a contract price exists). An expiration date can be set to time-limit the contract.

**Operation.** Enter or look up the customer code; the customer name displays. Enter or look up the item number; the description and base price (for reference) display. Enter a start date and optional expiration date. Enter up to 10 quantity price breaks: enter the **quantity** and **price** (discount from base auto-calculates) or enter the **discount** (price auto-calculates). Quantity break ranges work the same as price codes (break 1 covers quantities 0 through break-1 quantity; break 2 covers quantities break-1+1 through break-2 quantity). Save with F10.

---

## SO-Q-I — Print Contract Prices

*Source: [so-q-i_print_contract_prices.htm](../../../samples/chm/extracted/so-q-i_print_contract_prices.htm)*

**Purpose.** List contract prices by customer. Expiration date is shown for review.

**Operation.** Filter by from/thru ranges for item numbers, customer codes, item class, and category. Choose sort order: by customer or by item. Option to include the retail (base) price as a reference column.

---

## SO-Q-J — Generate Base Prices

*Source: [so-q-j_generate_base_prices.htm](../../../samples/chm/extracted/so-q-j_generate_base_prices.htm)*

**Purpose.** Generate base prices automatically based on a percentage markup over cost. Optionally cascade the change into price code prices and contract prices that are expressed as percentage discounts from the base.

**Operation.**

1. Choose cost basis: **Average Cost**, **Last Cost**, or **Standard Cost**.
2. Enter markup percentage (10% = `10.0000`).
3. Answer:
   - Generate prices for items with zero/negative cost or zero base price?
   - How many decimal places of precision (1–4)?
   - Update price code prices tied by percentage to base price?
   - Update contract prices tied by percentage to base price?
4. Filter by from/thru ranges of item numbers, categories, and item classes.
5. Confirm and process. After completion, prices can be edited individually in SO-Q-A.

---

## SO-R — Void Invoice

*Source: [so-r_void_invoice.htm](../../../samples/chm/extracted/so-r_void_invoice.htm)*

**Purpose.** Reverse a posted invoice that was processed in error. The program first returns all line items to the original sales order (reopening it if closed). If the original SO has been purged, a new SO is created with the original header and line item information. After restoring the SO, the program posts a full reversal to all files that SO-G Post Invoices updates. A complete audit trail is maintained: both the original and reversal postings are preserved.

**Operation.**

1. Enter the invoice number in **Inv#** (or press F2). Header information fills in automatically to confirm the correct invoice.
2. Enter the **Void Date** (date of all reverse postings to GL and related files).
3. Confirm: *Are you sure you want to void this invoice?* Enter `Y` to proceed.
4. The reversed items are returned to the original (or a newly created) SO.
5. The reverse invoice is posted to all files updated by SO-G.
6. A hard copy of the reversal can be printed via SO-F Print Invoices in reprint mode.

**Tip:** Use SO-R (not AR-B vouchers) whenever the reversal affects inventory quantities or salesperson commissions.

---

## SO-S — Mass Release Sales Orders

*Source: [so-s-mass_release_sales_orders.htm](../../../samples/chm/extracted/so-s-mass_release_sales_orders.htm)*

**Purpose.** Release a block of sales orders at once rather than using SO-E to release them one at a time.

**Operation.** Click **Config** to set: Release All Lines, Include Backorders, Auto Release Comments. These settings are saved for subsequent runs. Enter from/thru ranges of SO numbers, Customer Codes, Order Dates, and Item Numbers. Click to process. Ship Date defaults to today's date.

---

## SO-T — View Sales Orders

*Source: [so-t_view_sales_orders.htm](../../../samples/chm/extracted/so-t_view_sales_orders.htm)*

**Purpose.** View sales orders in read-only mode without the ability to make changes.

**Operation.** Operates identically to SO-A Enter Sales Orders except saving is not available. Useful for users who need visibility into orders without edit access.

---

## Cross-references

| Related module | Relationship |
|---|---|
| **AR — Accounts Receivable** | SO-G posts to AR (customer invoices, AR balance). SO-F can reprint AR vouchers and finance charges. AR-A Enter Customers provides bill-to/ship-to defaults, terms, price code, discount code, salesperson, tax group, credit limit, currency. AR-N manages sales order deposits applied during SO-F. |
| **IN — Inventory** | Inventory master (IN-B) provides item descriptions, prices, units of measure, taxability, stock status. SO-A, SO-G update on-SO, on-BO, and on-hand quantities. IN-L-B supplies multi-location data. IN-L-C provides customer cross-reference mappings. IN-L-S Rebuild Stock Status can be used to recover from SO-G lock failures. |
| **WO — Work Orders** | SO-N Convert Sales Orders to Work Orders creates WOs from SO line items. The SO estimated ship date becomes the WO finish date. The SO number becomes the WO prefix. Features & Options selections from SO-A are carried into the WO BOM. SO-O-G prints the SO/WO schedule to compare ship dates with WO finish dates. |
| **PO — Purchase Orders** | SO-P-N Convert SO to PO generates POs for type-R items on a sales order. |
| **CS — Commissions** | Salesperson records (CS-A / CS-B) provide default commission rates. SD-N Sales Commission Defaults controls how commissions are entered and calculated. SO-G updates salesperson gross sales, COGS, and commissions due. SO-O-D and SO-G's pre-posting commission report allow review before posting. |
| **MR — Material Requirements** | SO line estimated ship dates are used by the MRP module as demand target dates for production planning. Blanket order lines with a far-future date are excluded from near-term MRP demand; released lines from SO-P-F are picked up as near-term demand. |
| **SH / Shipping** | SO-C, SO-D generate packing slips and shipping labels. SO-E assigns shipper numbers, ship dates, and tracking numbers. Shipper numbers are tracked per released invoice. |
| **GL — General Ledger** | SO-G posts to Sales GL accounts, COGS accounts, Inventory accounts, Sales Tax Payable, AR Control, and (for retention billing) Retention accounts. GL Dept on the SO header can route income/expense to specific department segments. |
| **SD-M — Sales Order Defaults** | Central control point for SO module behavior: form formats, Ready to Invoice? default, credit limit messaging, duplicate PO warnings, backordering rules, commission entry mode, retention billing, itemized sales tax, price/discount field access control, next number defaults, blanket order settings, and many more. |
| **DEF-R — Assign Next Numbers** | Stores and increments the next SO number, next shipper number, and next recurring SO number. |
| **SM-J-J — Purge Closed Sales Orders** | Archives and removes closed (fully invoiced and posted) sales orders from the live file. Closed orders can be reopened in SO-A before purging if needed. |
| **IM-A / IM-B — Multi-currency** | When enabled, SO header accepts a foreign currency code; SO-G converts to base currency at posting using historical exchange rates; SO reports offer Base/Source currency options. |
