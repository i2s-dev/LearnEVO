# IN — Inventory

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Inventory (38 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [IN-A — Inventory Inquiry](#in-a--inventory-inquiry)
- [IN-B — Enter Inventory](#in-b--enter-inventory)
- [IN-C — Enter Inventory Adjustments](#in-c--enter-inventory-adjustments)
- [IN-D — Print Reorder Report](#in-d--print-reorder-report)
- [IN-E — Print Inventory Transactions](#in-e--print-inventory-transactions)
- [IN-F — Print Inventory Value](#in-f--print-inventory-value)
- [IN-G — Print Inventory Labels](#in-g--print-inventory-labels)
- [IN-H — Print Inventory Listing](#in-h--print-inventory-listing)
- [IN-I — Print Inventory General Information](#in-i--print-inventory-general-information)
- [IN-J — Print Physical Check](#in-j--print-physical-check)
- [IN-K — Adjust Physical Levels](#in-k--adjust-physical-levels)
- [IN-L-A — Enter Standard Costs](#in-l-a--enter-standard-costs)
- [IN-L-B — Enter/Assign Locations](#in-l-b--enterassign-locations)
- [IN-L-C — Enter Customer Cross-Reference](#in-l-c--enter-customer-cross-reference)
- [IN-L-D — Print Customer Cross-Reference](#in-l-d--print-customer-cross-reference)
- [IN-L-E — Update Material Standard Costs](#in-l-e--update-material-standard-costs)
- [IN-L-F — Enter Material Dimensions](#in-l-f--enter-material-dimensions)
- [IN-L-H — Edit FIFO/LIFO Buckets](#in-l-h--edit-fifolifo-buckets)
- [IN-L-I — Change Costing Method](#in-l-i--change-costing-method)
- [IN-L-J — Transfer Inventory](#in-l-j--transfer-inventory)
- [IN-L-K — Inventory Exception Report](#in-l-k--inventory-exception-report)
- [IN-L-L — Inactive BOM Component Report](#in-l-l--inactive-bom-component-report)
- [IN-L-M — Batch Location Transfer](#in-l-m--batch-location-transfer)
- [IN-L-N — Copy Item](#in-l-n--copy-item)
- [IN-L-O — Inactive Inventory Utility](#in-l-o--inactive-inventory-utility)
- [IN-L-Q — Enter Inspection/Test Procedure Codes](#in-l-q--enter-inspectiontest-procedure-codes)
- [IN-L-R — Intercompany Inventory Transfer](#in-l-r--intercompany-inventory-transfer)
- [IN-L-S — Rebuild Stock Status](#in-l-s--rebuild-stock-status)
- [IN-L-T — Reset Cycle Code](#in-l-t--reset-cycle-code)
- [IN-L-U — Item Number Configurator](#in-l-u--item-number-configurator)
- [IN-M — Summary Reorder Report](#in-m--summary-reorder-report)
- [IN-N-A — Print Month End Inventory Costing](#in-n-a--print-month-end-inventory-costing)
- [IN-N-B — Print Shipments Costing](#in-n-b--print-shipments-costing)
- [IN-N-C — Print Closed Work Orders Costing](#in-n-c--print-closed-work-orders-costing)
- [IN-N-D — Print Inventory to GL Exceptions](#in-n-d--print-inventory-to-gl-exceptions)
- [IN-O — User Defined Inventory Transactions](#in-o--user-defined-inventory-transactions)
- [IN-P — Print Inventory Usage](#in-p--print-inventory-usage)
- [IN-Q — Print Labels with Lot/Serial Info](#in-q--print-labels-with-lotserial-info)
- [Cross-references](#cross-references)

---

## IN-A — Inventory Inquiry

*Source: [in-a_inventory_inquiry.htm](../../../samples/chm/extracted/in-a_inventory_inquiry.htm)*

**Purpose.** All-purpose inquiry on a specific inventory item. Displays product type, stock unit of measure, category, item class, last cost, average cost, standard cost, inventory value, base price, selling UM, purchase UM and conversion factor, lead time, reorder level, reorder amount, revision level, drawing number, and stock location. Inventory status is shown for: on hand, on sales order, on back order, on purchase order, on work order, allocated, and in work-in-process quantities.

**Navigation from the inquiry screen.** Buttons allow viewing open and closed sales orders, purchase orders, work orders, and allocations. Additional buttons access Vendors, Manufacturers, Customer cross-reference numbers, Bill of Materials, Where Used (one level in each direction), Routing, transaction history, and monthly usage summary for the past year. Double-clicking an item in a BOM or Where Used result opens another IN-A screen for that item, enabling drill-down or drill-up through the product structure.

**Usage definition.** Usage is the total of type `I` (Issue to Work Order), `J` (Purchase to Work Order), and `S` (Shipment) transactions. Adjustments are not included.

**Multi-location.** A second screen displays inventory status within each warehouse/plant location when multiple locations are active.

**Stock status rebuild.** Pressing `<Enter>` after the item number rebuilds all stock status fields (on sales order, on back order, on PO, on WO, allocated) from scratch directly from the open order files.

**Multi-currency and landed cost notes.** If multi-currency processing is enabled (IM-A), the Last and Average costs of purchased items reflect foreign currency fluctuations that can vary from transaction to transaction. If landed cost processing is in use, Last and Average costs will also be increased by landed costs such as duty charges, brokerage fees, and freight.

**Lookup.** Enter an item number directly or press F2 / click Lookup to search by item number, description, item class, or alternate (vendor or manufacturer item number). The alternate search resolves the vendor/manufacturer cross-reference and pulls in the equivalent internal item number.

---

## IN-B — Enter Inventory

*Source: [in-b_enter_inventory.htm](../../../samples/chm/extracted/in-b_enter_inventory.htm)*

**Purpose.** Create new inventory item records or change information on existing items. This is the master item file maintenance program.

**Audit button.** Displays a list of changes to the part, the login ID of the user making the change, date and time, and which program was used. Columns shown by default include Item Class and Type. Additional columns from the ICAUDIT grid can be added via SU-A Maintain Grid Lookups.

### Field Explanations

**Item number.** 15-character alphanumeric, upper case only. Single/double quotes and commas are not allowed; other characters such as `#` or `-` are allowed.

**Description.** Two 30-character fields, both upper and lower case. The second description line is not used on all reports; place the most important information in the first field. Up to 12 lines of specifications can be entered via the Specifications button to print as comment lines on SO and PO documents. Unlimited Notes can also be attached with different Note types defaulting to print on different documents.

**Class.** Required 4-character alphanumeric (upper case). Item classes define the GL account codes used for inventory accounting and must be set up first in SM-C Enter Item Classes. The class description displays automatically to the right of the code.

**Category.** User-defined 4-character alphanumeric (upper case) for grouping products for reporting. Whether a predefined list is required can be controlled in SD-H Inventory Defaults; the list is maintained in SM-P-A Enter Categories.

**User Defined Sort Field.** An indexed field usable as a filter on many reports. Predefined list behavior controlled in SD-H; list maintained in SM-P-B Enter User Defined.

**Part Type.** Ten part types are supported:

| Code | Name | Description |
|------|------|-------------|
| `N` | Non-Inventory | Engineering charges, shop supplies, etc. No stock balances maintained. Sub-options: Service & Repair item (with Make/Model/Serial#), multi-yield placeholder for WO-I, or Surcharge part for auto-price update at SO-E release. |
| `R` | Regular | Purchased parts used as components or for resale. |
| `M` | Make From | Item that receives an outside process giving it a different item number than its pre-processed form (e.g., plated vs. non-plated). Has a BOM of its raw components. On PO receipt, components are relieved and the Make From item is updated at actual (outside processing cost + component cost). Eliminates need for a work order to handle outside processing. |
| `F` | Finished Good | Top-level manufactured items generally not used in other assemblies. |
| `A` | Subassembly | Manufactured items going into higher-level assemblies; can be sold or issued to higher assemblies. |
| `B` | Phantom Assembly | Never manufactured or stocked. Represents a kit; components are automatically exploded when a WO is created. Cannot have its own work orders. |
| `L` | Labor | Labor categories (welding, setup, assembly, etc.) with standard cost maintained; no on-hand balance kept. |
| `T` | Outside Processing | Services such as plating, painting, heat treating; can appear in BOMs and POs. |
| `K` | Selling Kit | Kit of parts ordered/invoiced via one item number in sales orders; never manufactured or stocked. |
| `O` | Feature | Used by the Features & Options module. Represents a group of options presented as a pop-up during SO entry. Never purchased or manufactured. |

**Active?** Controls inclusion/exclusion in reports and prevents transactions for certain statuses. Allowable values:

| Value | Status | Effect |
|-------|--------|--------|
| `Y` | Active | All activity allowed. |
| `N` | Inactive | All activity allowed; can be excluded from some reports; warning shown in various programs. |
| `O` | Obsolete | Historical reference only. Cannot be bought, sold, made, or have on-hand quantity. Requires zero on-hand, no open orders, before change is allowed. |
| `D` | Discontinued | Can be consumed (shipments, issues to WO allowed) but cannot be replenished (no POs, no WOs to make more). |
| `E` | Engineering | Items under development; orders and transactions allowed but a warning is presented. Access to create/edit E-status items can be limited to users with Security Code E in PS-A. |
| `P` | Production & Purchasing Hold | Prevents WO processing, prevents PO entry, forces PO receipts to a Quality Hold Location. |
| `S` | Shipping Hold | Prevents packing slips, releasing sales orders, and processing invoices. |
| `Q` | Full Quality Hold | Combination of P and S; prevents all activity. |

Changing to status `P`, `S`, or `Q` automatically transfers any on-hand stock to a Quality Hold warehouse location defined in SD-H Inventory Defaults.

**Taxable?** `Y` = taxable by default (can be overridden per transaction); `N` = never taxable on SO or PO.

**Stock UM.** 3-character alphanumeric (upper case). The unit of measure in which the item is stocked (e.g., `EA`, `LBS`, `FT`).

**Price UM.** Unit of measure for selling. Special values: `M` = per 1,000; `C` or `H` = per 100; `LOT` or `MIN` = lot/minimum charge (no extended price calculation by quantity). Other values are reference only and perform no conversion.

**Purch UM.** Unit of measure for purchasing. Special pre-defined values that trigger internal price formula calculations:

| Code | Pricing Formula |
|------|----------------|
| `M` | Per thousand: (PO qty)/1000 × (PO price) |
| `H` or `C` | Per 100: (PO qty)/100 × (PO price) |
| `LOT` | Lot charge (flat fee regardless of quantity) |
| `LB` | Per pound: (PO qty) × (Weight field) × (PO price) |
| `CWT` | Per 100 weight: (PO qty) × (Weight)/100 × (PO price) |
| `SF` | Per sq ft: (PO qty) × (Foot Factor) × (PO price) |
| `MSF` | Per 1,000 sq ft: (PO qty) × (Foot Factor)/1000 × (PO price) |
| `BF` | Per board foot: (PO qty) × (Foot Factor) × (PO price) |
| `MBF` | Per 1,000 board foot: (PO qty) × (Foot Factor)/1000 × (PO price) |
| `LF` | Per linear foot: (PO qty) × (Foot Factor) × (PO price) |
| `CLF` | Per 100 linear feet: (PO qty) × (Foot Factor)/100 × (PO price) |
| `MLF` | Per 1,000 linear feet: (PO qty) × (Foot Factor)/1000 × (PO price) |

If using a non-pre-defined Purch UM that differs from Stock UM, define a PO Conv Mult (see below).

**Duty Code.** 3-character code forming the item-side of the 6-character duty code used in landed cost processing (IM-E). Combined with a 3-character vendor code to determine duty fees.

**RTM Group.** Single character. Assigns items to a custom label format RTM. If RTM Print Group is `A`, the program will use `T6ING1A.RTM` instead of the standard `T6ING1.RTM` when that file exists.

**Base Price.** Default selling price for customers without special pricing. Access can be disabled in SD-H, in which case base prices are entered in SO-Q-A Enter Base Prices.

**Type R Comp Date.** For purchased items (type R): date the standard cost was last entered in IN-L-A or the last purchase receipt date saved by IN-L-E Update Material Standard Costs (whichever is later). For assemblies and Make From parts, it is the earliest standard cost rollup date of purchased components in the BOM. Updated by BM-G Print/Rollup Standard Costs for assemblies.

**BP Last Changed.** Date the Base Price was last changed, either here or in SO-Q-A.

**Primary Vendor.** 10-character vendor code for the primary source of a purchased item. Referenced on the Reorder Report and used as the default vendor by MR-J Generate Purchase Orders. Entering a primary vendor automatically creates a record in the approved vendor file (PO-L).

**Customer.** If this item is made for one customer only, enter the customer code here (for reporting purposes only).

**ITP#.** Inspection and Test Procedure code. Setting Print ITP to Y and enabling the Items default for Use ITP for Work Orders causes the ITP number and description to print on the Shop Traveler. ITP codes are maintained in IN-L-Q.

**Tool.** Primary tool used to make this item (reference field).

**WO Class Code.** If populated, work orders for this item created in WO-A will be assigned this class.

**2D Barcode.** Opens a screen to define a 2D QR bar code for the item (data fields, control characters, plain text). Prints on inventory labels generated by WO-S Print Work Order Labels.

**Reorder Level.** The quantity threshold below which the item needs replenishment. Used as a minimum on-hand by the Material Requirements module.

**Minimum Order Qty.** Minimum quantity for generated purchase orders or work orders. Used by MRP as the minimum quantity for suggested orders.

**PO Conv Mult.** Conversion multiplier from purchase UM to stock UM, applied automatically during PO receiving. Only required if Stock UM and Purch UM differ AND the Purch UM is not one of the pre-defined special values listed above. Example: buy by YD, stock by FT, multiplier = 3.00000.

**Lead Time [days].** Days from order/start date to receipt/finish date. Used by MRP to determine start dates. Calendar days for purchased parts; shop days (per SM-H Shop Calendar) for manufactured parts. For manufactured parts, reflects only the days to make a typical production run quantity at this level of the BOM, assuming all components are available.

**Receive to QC.** Enter `Y` to force this item to be received into QC in PO-C regardless of the receiving operator's choice.

**Reset & Counter.** If the Inventory default for Reset Receive to QC is enabled, the Reset checkbox and a counter specify how many consecutive good receipts must occur before the Receive to QC requirement is waived.

**Weight.** Weight of the item. Used to calculate total packing slip weight. Also used as a conversion factor in PO pricing when Purch UM is `LB` or `CWT`.

**Foot Factor.** Cubic or linear feet of the item. Used as a conversion factor in PO pricing when Purch UM is `SF`, `MSF`, `BF`, `MBF`, `LF`, `CLF`, or `MLF`.

**Std Pack.** Number of items per carton or pack. Can be used as a Purchase Increment by MR-J Generate Purchase Orders if enabled in SD-D Material Requirements Defaults. Should be entered in purchase UM units.

**Freight Percent.** Percentage freight surcharge added to cost on PO receipt to absorb freight into average cost. Example: 20.00 adds 20% to the received cost. Use only on items where freight is a significant cost portion.

**Warehouse Control?** `Y` = multiple bin locations available, quantity by bin not tracked; `Q` = quantity by bin also maintained. Requires global warehouse control turned on in SD-S Warehouse Control Defaults.

**Cycle Code.** User-defined code for cycle counting selection in IN-J Print Physical Check and PI-A Capture Frozen Inventory. Example: code `1` = monthly, `2` = quarterly, `3` = annually.

**Commissions.** Enter `N` to exclude this item from Sales Commission calculations in Sales Orders. Intended for exception items such as tooling or restocking charges.

**Drawing #.** Engineering drawing number. Prints on the shop traveler and is an invisible field on POs (can be made visible). When ECO Tracking is enabled in SD-H, a Lookup icon shows prior revision history and allows entering a new ECO and Revision.

**Revision Level.** Current engineering revision level. Prints on the shop traveler; also an invisible field on POs.

**UPC.** UPC number, displayed if UPC Control is enabled in SD-H.

**Bin Location.** 10-character primary bin location. Prints on packing list, physical inventory count sheet, and work order pick list. When Warehouse Control is on, this is a reference/default bin only.

**Lot Control?** `Y` = item is lot-controlled.

**Serial Control?** `Y` = item is serial-controlled.

**Shipping Lead Time.** If populated, SO-A Enter Sales Orders uses today + this value to generate the Estimated Ship date. For multi-line orders, the greatest lead time applies to all lines.

**Approved Vendors in PO?** Controls vendor enforcement at PO entry: `0` or blank = no restriction; `1` = warning if non-approved vendor; `2` = hard block, non-approved vendor not allowed. A system-wide default can be set in SD-C Purchase Orders Defaults.

**Work Order Material.** `Y` = every PO for this item requires a Work Order number. Used for generic item numbers for one-time purchases that should never carry an on-hand quantity or average cost.

**Refurbished Item #.** Item number of the refurbished version of this item. Used in the Service and Repair module.

### Additional Entry Screens (Buttons)

**Links Button.** Attach external files (PDF drawings, JPG images, Word documents, CAD files, etc.) to the item. A global path can be saved to avoid repeating folder names. A link can be associated with a specific Routing sequence. Files can be designated to print as embedded thumbnails or as linked documents on various RTM-based documents (Shop Traveler, Estimate, PO, RFQ, Quote, Acknowledgement, Invoice, Packing Slip, labels). Supported thumbnail formats include BMP, JPG, GIF, TIFF, PCX, WMF, PSD, and others. When RTM forms are emailed, linked document files (up to 10 per item per RTM) are included as additional email attachments.

**Specs Button (Specifications).** Free-format notepad for extra description or specifications. Prints optionally on acknowledgments, packing lists, invoices, and purchase orders; prints automatically on shop travelers.

**Std Cost Button.** Shortcut to the standard cost entry screen (same as IN-L-A Enter Standard Costs).

**MRP Button.** Shortcut to MRP parameter entry for this item (same as MR-D Enter MRP Parameters).

**Vendors Button.** Shortcut to vendor and vendor item number assignment (same as PO-L Assign Vendors to Items).

**Manufacturers Button.** Shortcut to manufacturer and manufacturer item number assignment (same as BM-L Enter Approved Manufacturers).

**Cmp Button.** Compliance screen for: Conflict-Free Material, RoHS, RoHS3, REACH, CA Prop 65 (each set to Yes/No/Pending/Exempt). Also specifies whether RoHS Documentation and Certificate of Conformance are required.

**U-Def Button.** User-defined fields as defined in SM-P-E Define Inventory User Defined Fields.

### International Fields

Available based on settings in IM-A International Configuration.

**Tax-In.** `Y` = item has an excise tax embedded in its selling or purchase price. On invoice posting or PO receiving, the embedded tax is backed out for GL, sales analysis, and tax reporting. See IM-G Enter Tax-In Codes.

**Duty Code.** 3-character item classification code forming the item-side of the 6-character landed cost duty code used in IM-E Enter Landed Cost Duty Codes.

### General Program Operation

**Adding a record.** Create item classes in SM-C first. Required minimum fields before saving: Item number, Class, Part Type, Stock UM, Price UM, Purch UM. Save with the Save button or Alt-S.

**Deleting a record.** An item cannot be deleted if it has on-hand quantity, open orders, is in a BOM, has a routing, or is part of an active or non-purged physical inventory. Use Lookup/F2 to select the item, press Enter, then click Delete. If deletion is blocked, a list of reasons is presented.

---

## IN-C — Enter Inventory Adjustments

*Source: [in-c_enter_inventory_adjustments.htm](../../../samples/chm/extracted/in-c_enter_inventory_adjustments.htm)*

**Purpose.** Adjust inventory quantities up or down, or make a zero-quantity adjustment to document that a count was verified as correct.

### Field Explanations

**Date.** Defaults to the computer system date; may be overridden.

**Type.** Inventory transaction type. Available values:
- `A` — Adjustment
- `S` — Shipment
- `P` — Purchase Receipt

**Item number.** The item being adjusted. Lookup available via F2.

**Description.** Auto-populated from the item master; not editable here.

**Location.** Warehouse location. Current on-hand for that location is displayed for reference.

**Quantity.** Units to adjust. May be positive (adding) or negative (removing).

**Use Std Cost?** `Y` = insert the item's standard cost into the Act Unit Cost field. Only applicable when adding inventory.

**GL Account.** If the default allows it, enter the GL account and department for the expense side of the adjustment transaction.

**Act Unit Cost.** If Use Std Cost = Y, standard cost is used. If No, average cost is the default. Override is allowed for positive adjustments. For negative adjustments, average cost is used and cannot be changed.

**Reference.** Short notation on the reason for the adjustment (type A). For types S and P, the system records the customer or vendor name here.

**Invoice No.** Invoice number for type S (shipment) transactions.

**Customer Code.** Required for type S transactions. Must be a valid customer. Lookup via F2.

**Customer Name.** Auto-populated from customer record; can be overridden for notation purposes.

**Selling Price.** Sales price of the shipment, applicable only to type S transactions.

**Purch Ord No.** Purchase order number for type P transactions.

**Vendor Code.** Required for type P transactions. Must be a valid vendor. Lookup via F2.

**Vendor Name.** Auto-populated; can be overridden for notation.

**Lot Number.** Required if the item is lot-controlled.

**Serial Number.** Required (one per unit) if the item is serial-controlled.

### General Program Operation

Select a transaction type. Enter the item number. Enter the quantity (positive or negative). For positive adjustments, choose whether to use standard or average cost, or enter an actual cost. For type S (shipments), also enter invoice number, customer code, and selling price. For type P (purchase receipts), enter PO number and vendor code. If lot or serial controlled, enter the lot or serial number before saving.

---

## IN-D — Print Reorder Report

*Source: [in-d_print_reorder_report.htm](../../../samples/chm/extracted/in-d_print_reorder_report.htm)*

**Purpose.** Primary worksheet for determining which inventory items need to be purchased or manufactured. Calculates a theoretical available quantity using on-hand, on sales order, on back order, allocated, on purchase order, and on work order balances. Compares available quantity against the reorder level, shows the over/under amount, and displays a reorder quantity guideline.

**Report options.** Sort by Item, Class, or Vendor. Can be limited to all components of a single top-assembly BOM. Selection filters include from/thru ranges of item number, product type, item class, Category, Primary Vendor, Cycle Code, Planner Code. Can be restricted to items where available quantity has fallen below reorder level. Active status filter available. Can exclude future supply to show immediate shortages only. Options to include second description line, primary vendor, and last cost. Can use warehouse-location-specific reorder levels.

**Detail option.** Includes a list of all open sales orders, purchase orders, work orders, and allocations with dates and quantities. Can make the report very long.

**Stock status rebuild.** Option to rebuild stock status fields from scratch from the actual order files before printing. This can take a long time depending on file sizes. An alternative is to run IN-L-S Rebuild Stock Status or SM-J-C Reconcile Inventory On-Hand periodically as preventive maintenance.

---

## IN-E — Print Inventory Transactions

*Source: [in-e_print_inventory_transactions.htm](../../../samples/chm/extracted/in-e_print_inventory_transactions.htm)*

**Purpose.** History report of inventory movements for one or a range of items. Provides a full audit trail of all transaction types.

**Transaction types available for filtering:**

| Code | Description |
|------|-------------|
| `A` | Adjustments |
| `S` | Shipments |
| `P` | Purchase order receipts to stock |
| `J` | Purchase order receipts to work-in-process |
| `W` | Work order receipts to stock |
| `I` | Stock issues to work-in-process |
| `O` | Outside Processing Receipt to Work Order |
| `Q` | Purchase Receipt to QC |
| `C` | AP Price Change |
| `M` | Make-From component Issue |
| `T` | Transfer between Warehouse Locations |
| `G` | Scrap |
| `R` | Service/Repair return of repaired item to customer |
| `B` | Transfer between Bin Locations in the same Warehouse |

**Filters.** Item number (single or range), item class, Category, Location, and from/thru date range. Press Enter twice with no dates to view all records for the selected item(s).

**Calculated totals at end of report:**
- **Net Unit Chg** — net difference between additions and deductions within the selected ranges (how much on-hand went up or down).
- **Avg Cost (Period)** — average cost of transactions within the selected ranges.
- **Reference values** — current Last, Average, and Standard cost from the inventory master.

---

## IN-F — Print Inventory Value

*Source: [in-f_print_inventory_value.htm](../../../samples/chm/extracted/in-f_print_inventory_value.htm)*

**Purpose.** Inventory valuation report for all or selected items. Can report at actual (average) cost or include both standard and actual cost. Standard costs are broken out into material, setup, labor, outside processing, fixed overhead, and variable overhead. Supports as-of-date reporting: the program takes current on-hand and backs out transactions to calculate value as of the specified prior date.

**Report automatically subtotals by item class when sorted by class.**

**Selection options:**
- All item numbers in range (including zero-value)
- All except zero-value parts
- Include On-Hand with $0 cost (anything with on-hand quantity, even if value is $0)

Under Inventory Types, checkboxes allow including/excluding specific part types. Additional options: Active status filter (Y/N/O/E/D), Include standard costs, Include units in QC, Print Subtotals only, Print 2nd line part description.

**Location filter.** If multiple inventory locations are defined, select which locations to include. Note: GL Book Value is not maintained by location and will only be reported if printing all locations.

**As-of date.** If entered, the report calculates today's inventory value and backs out all transactions back to the specified date. If any transactions encountered are marked "Consolidate Inventory Transactions," the report will note that it may be inaccurate.

**From/thru ranges.** Item numbers, item classes, and GL asset accounts.

---

## IN-G — Print Inventory Labels

*Source: [in-g_print_inventory_labels.htm](../../../samples/chm/extracted/in-g_print_inventory_labels.htm)*

**Purpose.** Print inventory labels for product identification. Optionally prints bar-coded labels.

**Label formats:**
- **1-up** — standard 3-1/2" × 15/16" continuous form labels
- **2-up** — Avery 5161 laser form
- **3-up** — Avery 5160 laser form

**Options.** Enter or look up the item number. Enter optional miscellaneous text to print on the label. Specify whether to print the stock unit of measure. Optionally print a bar code for the item number directly above the printed item number. Specify the number of labels to print and whether to include linked documents. Select the desired label format.

---

## IN-H — Print Inventory Listing

*Source: [in-h_print_inventory_listing.htm](../../../samples/chm/extracted/in-h_print_inventory_listing.htm)*

**Purpose.** Listing of inventory items. Standard report shows item number, description, type, category, class, units of measure, base price, standard cost, last cost, and average cost. The report template `T6INH1.RTM` can be modified via TA-M Forms Editor to add additional columns from the inventory master file.

**Filters.** Choose to report on Active, Archived, or Estimating inventory data. Limit by from/thru ranges of item numbers, types, categories, classes, and primary vendor. Report prints in item number order.

---

## IN-I — Print Inventory General Information

*Source: [in-i_print_inventory_general_information.htm](../../../samples/chm/extracted/in-i_print_inventory_general_information.htm)*

**Purpose.** Full detail listing of all inventory field values — a complete record dump for selected items.

**Filters.** Limit by from/thru ranges of item numbers, types, classes, and categories. If no limits are specified, the program prints general information on all inventory items. This produces a very long report since only two items print per page.

---

## IN-J — Print Physical Check

*Source: [in-j_print_physical_check.htm](../../../samples/chm/extracted/in-j_print_physical_check.htm)*

**Purpose.** Count verification worksheet. Supports a planned system of cycle counts as an alternative to an annual physical inventory. The report provides blank fields for entering new count totals, which can then be entered in IN-C Enter Inventory Adjustments or IN-K Adjust Physical Levels.

**Cycle count example.** Assign Cycle Code `M` = count monthly, `Q` = count quarterly, `Y` = count annually. Use the cycle code as a filter when running this report.

**Selection criteria.** From/thru ranges of item numbers, item categories, item classes, stock locations, cycle count codes, and bin locations. Report can print in part number order or bin location order.

---

## IN-K — Adjust Physical Levels

*Source: [in-k_adjust_physical_levels.htm](../../../samples/chm/extracted/in-k_adjust_physical_levels.htm)*

**Purpose.** Enter beginning stock balances and average costs, or overlay existing on-hand quantities with new physical count results.

**General operation.** Select the item number. The current on-hand and average cost are displayed. The cursor stops at the New Last Cost per Unit field; enter a new Last Cost if applicable. Then optionally change the Average Cost in the New Avg Cost per Unit field. Current inventory status is shown for each Location. Enter a Reference note (reason for adjustment) then enter the new quantity in the New Units column. The system displays how much the GL asset account will go up or down.

**Costing method restrictions.** If the costing method is FIFO or LIFO (set in SD-H), you cannot change Last Cost or Average Cost here — use IN-L-H Edit FIFO/LIFO Buckets instead. If the costing method is Standard or Average, you can only change Average Cost for items with no on-hand quantity. To correct an invalid cost for an item with on-hand quantity, use IN-C to adjust stock to 0 at the incorrect cost, then make a positive adjustment to put stock back in at the correct cost (this maintains the audit trail and preserves book value integrity).

---

## IN-L-A — Enter Standard Costs

*Source: [in-l-a_enter_standard_costs.htm](../../../samples/chm/extracted/in-l-a_enter_standard_costs.htm)*

**Purpose.** Maintain or view standard costs on inventory items.

### Field Explanations

**Part No / Desc.** Item number and auto-displayed description.

**Lot Size.** Typical production run quantity. Used to establish a per-unit setup cost estimate.

**Type.** Inventory type (display only).

**Last Cost.** Auto-maintained by the system (last purchase or manufactured cost). Display only.

**Average Cost.** Auto-maintained by the system, recalculated on every inventory transaction. Display only. Under average costing: running weighted average. Under FIFO or LIFO: recalculated as (sum of each bucket's qty × cost) / total on-hand qty.

**Stock UM.** Reference only; standard costs are in the stocking UM.

### This Level Cost (user-entered)

Standard costs are entered only in the This Level Costs column. Rolled-up costs on the right are calculated by cost rollup programs and cannot be edited.

If using Routings for labor costing: enter only Material, Duty, and Freight on purchased (type R) items and Outside Processing and Freight for Make-From (type M) items. All other costs are maintained in routings.

If using Labor item numbers: also enter Labor, Setup, and Overhead on type L (labor) items, and Outside Processing costs on type T and type M items.

| Field | Applies To |
|-------|-----------|
| **Material** | Type R (purchased) only |
| **Freight** | Type R and type M (Make-From) only |
| **Labor** | Type L (labor) items only |
| **Setup** | Type L (labor) items only |
| **Outside Proc** | Type T (outside processing) and type M (Make-From) only |
| **Fixed Overhead** | Type L (labor) items only — rate per unit of labor |
| **Var Overhead** | Type L (labor) items only — rate per unit of labor |

### Rolled-Up Costs (calculated, display only)

All rolled-up fields (Material & Freight, Labor, Setup, Outside Proc, Fixed Overhead, Var Overhead, Total Standard Cost) are calculated by BM-G Print/Rollup Standard Costs or via the Cost Rollup button on this screen. They represent the accumulation of this level's costs plus all lower levels of the product structure.

**Total Standard Cost.** Grand total of all rolled-up costs. The definitive standard cost for the item.

### General Program Operation

Look up the item by number, then advance through fields and enter costs. Field access is restricted by item type. Upon saving with changes, the system asks if you want the total standard cost updated (triggers a cost rollup on the item). For type F, A, or B items, click the Cost Rollup button to roll up costs for this item and all related subassemblies and components. To roll up a range of items, use BM-G Print/Rollup Standard Costs.

---

## IN-L-B — Enter/Assign Locations

*Source: [in-l-b_enter_assign_locations.htm](../../../samples/chm/extracted/in-l-b_enter_assign_locations.htm)*

**Purpose.** Define warehouse/factory locations (up to 250) and assign inventory items to them. Can also delete locations that are no longer needed. Each inventory item must be explicitly assigned to a location; the program does not assume all items exist at all locations.

GL account codes by item class per location are set up in SM-C Enter Item Classes. On-hand quantities by location are entered via IN-C, IN-K, IN-L-J, or IN-L-M.

### Factory/Warehouse Location Fields

**Code.** 10-character location name. The master (default) location is defined in SD-H Inventory Defaults; all other locations are defined here.

**Loc Type.** Leave blank for standard production/warehouse locations. Enter `S` (Service), `R` (RMA), or `Q` (Quality) for special location types. Stock and on-order quantities at S, R, and Q locations are excluded from stock status calculations for available inventory.

**Name, Add1, Add2, CSZ.** Long name, address lines, and city/state/zip. These pull into Purchase Orders as the Ship To address.

**Warehouse Control Setting.** Default Warehouse Control setting for this warehouse.

**Order to display Location in IN-A.** A number from 1-6 causes this location's on-hand quantity to show on the Stock Status tab in IN-A Inventory Inquiry (Evo view).

**Resale Number, Contact, Phone, Fax.** Reference information only.

### Assigning Items to a Location

**Single Product Entry.** Enter one item number at a time and save.

**Generate Location Records (batch).** Specify from/thru ranges of item numbers, item classes, and inventory types. Press Enter through all fields to assign the entire inventory to the location.

### Deleting a Location

Three-step process:
1. Verify all on-hand, on-order, and allocated quantities for the location are zero (run IN-D Print Reorder Report for the location).
2. Select a range of items and choose Delete rather than Generate. Only item/location records with zero balances will be deleted.
3. Once all item/location records are deleted, click the button to delete the Master Location record.

To remove invalid locations and transfer any stock or orders to the primary default location, use UT-K-E Consolidate Inventory Locations.

---

## IN-L-C — Enter Customer Cross-Reference

*Source: [in-l-c_enter_customer_cross_reference.htm](../../../samples/chm/extracted/in-l-c_enter_customer_cross_reference.htm)*

**Purpose.** Maintain a customer's item number and description as a cross-reference to your internal item number. When a sales order is entered for the item, the customer's item number and description automatically feed into the sales order as comment lines. Ideal for companies supplying other manufacturers who require their own item numbers on order documents. Unlimited cross-references can be entered against any one item number.

**General operation.** Enter your item number and the customer code, then enter the customer's item number and optionally their product description. To edit an existing record, enter your item number and the customer code; their cross-reference number will pull in for editing.

---

## IN-L-D — Print Customer Cross-Reference

*Source: [in-l-d_print_customer_cross_reference.htm](../../../samples/chm/extracted/in-l-d_print_customer_cross_reference.htm)*

**Purpose.** Listing of customer cross-references that have been established.

**Filters.** From/thru ranges of customer codes, item numbers, class, and category. If no limits are specified, the entire file is printed.

---

## IN-L-E — Update Material Standard Costs

*Source: [in-l-e_update_materoal_standard_costs.htm](../../../samples/chm/extracted/in-l-e_update_materoal_standard_costs.htm)*

**Purpose.** Batch update the material standard cost for a range of type R inventory items (purchased parts) with either the Last Cost or Average Cost values. A significant time-saver when revising standard costs.

**General operation.** Limit to from/thru ranges of item numbers, item classes, categories, and Active Status. Specify whether to update using Last Cost (`L`) or Average Cost (`A`). All inventory type R items within the range are updated. The program displays each item as it is updated.

---

## IN-L-F — Enter Material Dimensions

*Source: [in-l-f_enter_material_dimensions.htm](../../../samples/chm/extracted/in-l-f_enter_material_dimensions.htm)*

**Purpose.** Enter material dimensions (length, width, height) on inventory items for use by the Yield Calculator in the Estimating module. The Yield Calculator determines how many parts of a given size can be made from a particular raw material size.

**Generic Item Number.** Multiple raw material item numbers can be tied to a Generic Item number (must be type B — Phantom). When using the Yield Calculator with a generic item number instead of a specific material, the program compares part dimensions against all associated raw materials and selects the one with the lowest estimated cost for the BOM.

**General operation.** Enter the raw material item number, then enter Length, Width, and Thickness. Optionally enter a Generic Part No to link this material to a phantom group. Save with the Save button or F10.

---

## IN-L-H — Edit FIFO/LIFO Buckets

*Source: [in-l-h_edit_fifo_lifo_buckets.htm](../../../samples/chm/extracted/in-l-h_edit_fifo_lifo_buckets.htm)*

**Purpose.** Make changes to the receipt date or cost on existing FIFO or LIFO cost buckets. Quantities within buckets cannot be changed through this program (doing so could create discrepancies between location on-hand quantities and bucket totals; FIFO/LIFO buckets are company-wide and not maintained by location).

### How FIFO Costing Works

Each time inventory is received, a cost bucket is created containing the receipt date, quantity, and cost. When inventory is deducted, it is taken from the oldest bucket first, then the next oldest, and so on. Fully depleted buckets are deleted. There is no limit to the number of buckets. After each inventory transaction, Average Cost is recalculated as: (sum of each bucket's qty × cost) / total on-hand qty.

### How LIFO Costing Works

Identical to FIFO except deductions come from the most recent bucket first, then the next most recent, and so on.

### General Program Operation

Enter the item number. The screen shows Average Cost, Total Quantity (company-wide on-hand), and Last Cost for reference. Existing buckets are listed; select a bucket to change its cost. As the cost is changed, the Average Cost field recalculates on-screen (does not update the master file until saved). When all edits are complete, press F10 / click Save. A message indicates the net value change to the inventory GL asset account. Accepting the prompt debits or credits the GL asset account accordingly.

---

## IN-L-I — Change Costing Method

*Source: [in-l-i_change_costing_method.htm](../../../samples/chm/extracted/in-l-i_change_costing_method.htm)*

**Purpose.** Change from one costing method to another. The costing method is originally set in SD-H Inventory Defaults; once set there it cannot be changed within SD-H — this program must be used to ensure all related files are adjusted correctly.

### Costing Methods

EvoERP supports four costing methods:

| Method | Description |
|--------|-------------|
| **Average** | Running weighted average cost. Recalculated on every inventory transaction. |
| **FIFO** | First-In First-Out. Cost buckets per receipt; oldest bucket consumed first on deductions. Average Cost = weighted average of all buckets. |
| **LIFO** | Last-In First-Out. Cost buckets per receipt; most recent bucket consumed first on deductions. Average Cost = weighted average of all buckets. |
| **Standard** | Inventory valued at predefined standard cost. Variances between actual and standard are isolated. |

### Conversion Behavior

**FIFO or LIFO → Average:** All FIFO or LIFO cost buckets are deleted.

**Average → FIFO or LIFO:** A single beginning cost bucket is created from the current on-hand quantity and average cost. All inventory Locations within a given item class must have identical GL asset accounts (because FIFO/LIFO costs are not maintained by location). If accounts differ, the conversion is blocked until you align the GL accounts in SM-C Enter Item Classes.

**Any method → Standard:** Inventory is revalued at Standard Cost. Any FIFO or LIFO buckets are deleted. Price Change transactions are generated as necessary. Book Value is recalculated. No automatic GL postings — the user must make their own manual GL entry to reset the inventory value.

### General Program Operation

The program runs in single-user mode only; all other users should be out of the system before running. Select the target cost method from the presented window. The program advises running SM-J-C Reconcile Inventory On-Hand first to verify current on-hand totals are correct. After processing completes, a confirmation message is displayed.

---

## IN-L-J — Transfer Inventory

*Source: [in-l-j_transfer_inventory.htm](../../../samples/chm/extracted/in-l-j_transfer_inventory.htm)*

**Purpose.** Transfer inventory from one Location (factory or warehouse) to another, or from one Bin to another within the same warehouse.

**General operation.** Enter a Transfer Date. Enter the Transfer FROM Location and the Transfer TO Location (lookup available). Enter the Transfer Amount. The screen shows current on-hand in each location, units to be transferred, new on-hand after transfer, and which GL accounts will be affected. Enter `Y` to OK the transfer and post it.

**Lot & Serial Controlled Items.** If the item requires Lot and/or Serial Control, a window of available Lots or Serial Numbers and their on-hand quantities is displayed. Select the Lot or Serial Number (for Lot Control, enter the quantity to transfer from that lot). Click Save or F10 to process.

---

## IN-L-K — Inventory Exception Report

*Source: [in-l-k_inventory_exception_report.htm](../../../samples/chm/extracted/in-l-k_inventory_exception_report.htm)*

**Purpose.** Identify inventory items with any combination of problems: negative on-hand quantity, or cost discrepancies between Last, Average, and Standard costs and Book Value.

**General operation.** Select which exception types to include and the percent difference threshold for cost discrepancies. Limit by inventory type, item number range, class range, and GL account range. This program produces a report only — it makes no corrections or GL postings. Items identified require manual follow-up.

---

## IN-L-L — Inactive BOM Component Report

*Source: [in-l-l_incative_bom_component_report.htm](../../../samples/chm/extracted/in-l-l_incative_bom_component_report.htm)*

**Purpose.** Identify inventory items that are either not called out on any BOM, or whose BOM parents have all been designated Inactive. Items identified can then be designated Inactive, moved to a different Item Class, or both.

**General operation.** Specify inventory types and ranges of Item Number, Class, and Category. Indicate whether to include items on no BOM, items with inactive parents, or both. A report is generated. After the report is closed, the user is prompted whether to automatically change the identified items to Inactive and/or move them to a different item class.

---

## IN-L-M — Batch Location Transfer

*Source: [in-l-m_batch_location_transfer.htm](../../../samples/chm/extracted/in-l-m_batch_location_transfer.htm)*

**Purpose.** Transfer a list of multiple inventory items from one Location (factory or warehouse) to another in a single batch, with an optional printed transfer sheet.

**General operation.** Enter the Transfer FROM Location and Transfer TO Location (lookup available). Enter a Transfer Date and indicate whether to print the transfer document. Then enter item numbers and quantities one line at a time (Insert key or Enter on a blank line). As each item is entered, the screen shows current on-hand in each location, units to be transferred, and new on-hand after transfer. Click Done when all items are entered to process the transfer.

**Lot & Serial Controlled Items.** Same behavior as IN-L-J: a window of available Lots or Serial Numbers is displayed; select the lot/serial and quantity, then click Save or F10.

---

## IN-L-N — Copy Item

*Source: [in-l-n_copy_item.htm](../../../samples/chm/extracted/in-l-n_copy_item.htm)*

**Purpose.** Copy an existing item and its Bill of Materials and Routing to a new item number. Useful for creating new items that are similar to existing ones.

**General operation.** Enter the existing item number as the From Item Number and the new item number as the To Item Number.

---

## IN-L-O — Inactive Inventory Utility

*Source: [in-l-o_inactive_inventory_utility.htm](../../../samples/chm/extracted/in-l-o_inactive_inventory_utility.htm)*

**Purpose.** Two functions: (1) identify inactive inventory items (those without transactions within a given date range) and optionally change their Active status to N, O (Obsolete), or Delete them; (2) archive Obsolete items.

### Identify Inactive Inventory

Choose Active/Inactive Status Inventory. Select or create a report filter set (multiple named filter sets can be saved for reuse). Sort/subtotal options: Item Number, Description, Class, Category, or Type.

Include options:
- All item numbers
- Status change only (Active with no transactions → change to Inactive; or Inactive with activity → change to Active)
- Active only / Inactive only / Active plus changed / Obsolete / Delete

Select which transaction types to include. Choose filter print location and date range, class, category, and item type.

A report is generated showing items meeting the criteria with recommended status changes. The program can then automatically apply the recommended changes. Changing to Obsolete or Deleting is only allowed if enabled in SD-H Inventory Defaults and only if the item meets the limiting parameters defined in IN-B Enter Inventory.

### Archive Obsolete Inventory

Choose Archive Obsolete Inventory. Enter a range of item numbers, Class, Category, User Defined, and item type. Option to delete inventory transactions for the selected items or archive them along with the items. All items with status `O` (Obsolete) meeting the filters are archived. Data moved to archive files: inventory master, BOM, Routing, and (optionally) inventory transactions. Restore from Archive is also available.

---

## IN-L-Q — Enter Inspection/Test Procedure Codes

*Source: [in-l-q_enter_inspection_test_procedure_codes.htm](../../../samples/chm/extracted/in-l-q_enter_inspection_test_procedure_codes.htm)*

**Purpose.** Maintain the table of ITP (Inspection and Test Procedure) codes used in IN-B Enter Inventory and WO-A Enter Work Orders. When Print ITP is set to Y on an item and the Items default for Use ITP for Work Orders is enabled, the ITP number and description print on the Shop Traveler.

**General operation.**
- **Adding:** Click ADD, enter a Code and Description.
- **Editing:** Click EDIT, make changes, click Save or F10.
- **Deleting:** Click DELETE and confirm.

---

## IN-L-R — Intercompany Inventory Transfer

*Source: [in-l-r_intercompany_inventory_transfer.htm](../../../samples/chm/extracted/in-l-r_intercompany_inventory_transfer.htm)*

**Purpose.** Transfer inventory between companies in a multi-company EvoERP installation. Uses a common intermediary "In Transit" (Transfer) company. Outgoing transfers move inventory from the sending company into the Transfer company; receipts move it from the Transfer company into the receiving company.

### Initial Setup Requirements

1. Item Classes must be consistent across all companies so GL postings work correctly when items are created in a new company.
2. Create a dedicated Transfer Company (e.g., "TC") for the in-transit staging.
3. In each live company that will make transfers, designate the Transfer Company in SD-H Inventory Defaults.
4. In the Transfer Company, set the GL Account for Inventory in AD-A General Ledger Defaults to the Intercompany Transfer account used by all companies.
5. If multiple currencies are in use: Currency Designations (IM-B) must be consistent across all companies. All companies involved in transfers must have multi-currency set up, and each company's base currency must exist as either Base or Source in all other companies.

### Initiating a Transfer

1. Answer No to receiving a transfer.
2. Enter the destination company.
3. Enter the originating warehouse location, transfer date, and whether to print the transfer document and include image links.
4. Enter item numbers and quantities (use Down Arrow to add more lines).
5. Click Done to process and optionally print the transfer ticket.

### Receiving a Transfer

1. Answer Yes to receiving a transfer.
2. Enter the transfer number (lookup available for pending transfers).
3. Enter the receipt date.
4. Enter the destination warehouse location within the receiving company.
5. Confirm the date and indicate whether to print the confirming document.
6. Review the list of items. If no discrepancies, click Done.

**If discrepancies exist:** Change a quantity to 0 (item missing) or the actual received quantity (quantity mismatch). Add items received but not on the list by pressing Down Arrow on a blank line.

### Transaction Posting

| Direction | Sending Company | Transfer Company | Receiving Company |
|-----------|-----------------|------------------|-------------------|
| Outgoing transfer | Credits inventory (by item class); INVTXN type T, negative qty | Debits Intercompany Transfer account; INVTXN type T, positive qty | — |
| Receipt | — | Credits Intercompany Transfer account; INVTXN type T, negative qty | Debits inventory (by item class); INVTXN type T, positive qty |

No GL postings occur in the Transfer Company. If the base currencies of the two companies differ, inventory is revalued upon receipt using the receiving company's currency conversion table.

---

## IN-L-S — Rebuild Stock Status

*Source: [in-l-s_rebuild_stock_status.htm](../../../samples/chm/extracted/in-l-s_rebuild_stock_status.htm)*

**Purpose.** Stand-alone version of the Rebuild Stock Status routine that also runs within IN-A Inventory Inquiry and optionally within IN-D Print Reorder Report. Recalculates stock status fields (On Sales Order, On Work Order, etc.) from actual order detail for the specified range of items.

**General operation.** Enter from/thru ranges of items, Class, and Category, and specify the item types to include. The program rebuilds all stock status derived fields from the actual open order files.

---

## IN-L-T — Reset Cycle Code

*Source: [in-l-t_reset_cycle_code.htm](../../../samples/chm/extracted/in-l-t_reset_cycle_code.htm)*

**Purpose.** Automatically assign Cycle Codes to inventory items based on usage value for a specified period. Used to maintain an ABC-style cycle counting program where high-value/high-usage items are counted more frequently.

**General operation.** Enter from/thru ranges of usage dates, items, Class, and Category; specify item types. Then enter the cycle code to assign for each usage value threshold. The program assigns cycle codes to items falling within each threshold.

---

## IN-L-U — Item Number Configurator

*Source: [in-l-u_item_number_configurato.htm](../../../samples/chm/extracted/in-l-u_item_number_configurato.htm)*

**Purpose.** Define families of item numbers that will be automatically incremented when the Item Configurator is enabled in SD-H Inventory Defaults. Allows structured, sequential item number generation within defined families.

**General operation.** Click Add. For Item Group, enter the text string that will be the leading character(s) of the family (e.g., `WIDGET-`). Enter the total length of the item number, the starting position and length of the numeric portion, and the last number used. The program generates the formatted last number. When creating new items in IN-B, entering the text string causes the next number in the family to be auto-generated.

---

## IN-M — Summary Reorder Report

*Source: [in-m_summary_reorder_report.htm](../../../samples/chm/extracted/in-m_summary_reorder_report.htm)*

**Purpose.** Monthly supply/demand/ending balance summary for the current month and the next three months. A forward-looking planning view complementary to the detail-oriented IN-D Reorder Report.

**Report content.** For each item: current on-hand quantity; supply (Work Orders and Purchase Orders with estimated receipt/finish dates) through end of current month; demand (Sales Orders and Work Order Allocations with estimated ship dates or WO start dates) through end of current month; expected ending balance. Then the same supply, demand, and ending balance for each of the next three months.

**Filters.** Item number range, item type(s), Class, Category, Primary Vendor, Active Status, Planner Code range. Options to include extended description and to include or limit to RoHS compliant items.

---

## IN-N-A — Print Month End Inventory Costing

*Source: [in-n-a_print_month_end_inventory_costing.htm](../../../samples/chm/extracted/in-n-a_print_month_end_inventory_costing.htm)*

**Purpose.** Assist with month-end inventory accounting for the General Ledger. Used primarily by companies that switch off automatic GL posting (AD-A General Ledger Defaults) and instead make manual journal entries after reviewing monthly activity.

**Transaction categories reported** (both standard and actual cost):
- Adjustments
- Stock Issues to WIP
- Purchase Receipts to WIP
- Purchase Receipts to Stock
- Shipments
- Work Order Receipts to Stock
- Purchase Receipts to QC
- Outside Processing Receipts to WIP
- PO Price Change
- Make From Component Issue
- Transfer
- Service/Repair Shipment
- Scrap

**General operation.** Enter a from/thru date range. Accept or decline each transaction category (default is Y for all). Choose between a detail report (one line per transaction) or a summary report (summarized by transaction type and item class).

---

## IN-N-B — Print Shipments Costing

*Source: [in-n-b_print_shipments_costing.htm](../../../samples/chm/extracted/in-n-b_print_shipments_costing.htm)*

**Purpose.** Listing of all shipments for a period at standard cost. Standard cost is broken into individual columns: material, labor, setup, outside processing, fixed overhead, and variable overhead. Used to analyze the relative cost content for the period.

**Filters.** From/thru date range, item numbers, customers, and item classes.

---

## IN-N-C — Print Closed Work Orders Costing

*Source: [in-n-c_print_closed_work_orders_costing.htm](../../../samples/chm/extracted/in-n-c_print_closed_work_orders_costing.htm)*

**Purpose.** Standard and actual cost comparison for all work orders closed during a period. Shows cost breakdown (material, labor, setup, outside processing, fixed overhead, variable overhead, total) at both standard and actual, with the variance for each. Used by companies that report WIP transactions at standard cost during the month, then adjust inventory and cost-of-goods accounts by the variances shown on this report.

**Filters.** From/thru work order finish date range and item classes.

---

## IN-N-D — Print Inventory to GL Exceptions

*Source: [in-n-d_print_inventory_to_gl_exceptions.htm](../../../samples/chm/extracted/in-n-d_print_inventory_to_gl_exceptions.htm)*

**Purpose.** Identify dates and Journal Types within a date range for a specific GL Account where inventory transactions and GL postings do not show the same amount. Used to locate discrepancies between the inventory sub-ledger and the General Ledger. Once a discrepant date and journal type are identified, detail reports such as GL-C Print GL Transactions and IN-O User Defined Inventory Transactions can be used to find the root cause.

**General operation.** Enter a date range and the Inventory GL Account to examine. Select which Journal types to include. Choose to show only dates with exceptions or all dates. After identifying a date with a difference, re-run for that specific date and answer Y to Print Exception Details to get the transaction-level detail showing where GL and Inventory transactions diverge.

---

## IN-O — User Defined Inventory Transactions

*Source: [in-o_user_defined_inventory_transactions.htm](../../../samples/chm/extracted/in-o_user_defined_inventory_transactions.htm)*

**Purpose.** Flexible, savable transaction history report for one or a range of inventory items. Multiple named report definitions can be saved with different filter combinations for recurring use.

**Transaction types** (same as IN-E, with addition of `B` — Bin transfer and `M` — Make From component Issue noted explicitly):

| Code | Description |
|------|-------------|
| `A` | Adjustments (IN-C, IN-K, or Physical Inventory) |
| `B` | Bin transfer |
| `C` | PO Price Change entered in AP-C |
| `G` | Scrap |
| `I` | Stock issues to work-in-process |
| `J` | Purchase order receipts to work-in-process |
| `O` | Outside Processing (Service) PO Receipt to Work Order |
| `P` | Purchase order receipts to stock |
| `Q` | Purchase Receipt to QC |
| `R` | Service & Repair shipment |
| `S` | Shipments |
| `T` | Location Transfer |
| `W` | Work order receipts to stock |

**Sort orders.** The sort order directly affects report speed and which index is used. Choosing Item Number sort with a specific item/date range is the fastest and most common usage.

**Report modes:**
- Detail and subtotals
- Subtotals only
- Beginning balance with ending total (EvoERP only)

**Filter options.** Item number or range, transaction date range, Class, Category, Item Type, Work Order number range, and others via Next Screen. Including a date range substantially speeds up execution when searching by other criteria such as a work order number.

**Output per item (Detail and Subtotals mode):**
- **Net Units** — net change in on-hand quantity within the selected range.
- **Avg Cost (Period)** — average cost of transactions within the range.
- Current Average, Last, and Standard Cost from the inventory master (reference).

**Audit detail.** Optionally includes the entry date, time, and User Login ID for each transaction.

---

## IN-P — Print Inventory Usage

*Source: [in-p_print_inventory_usage.htm](../../../samples/chm/extracted/in-p_print_inventory_usage.htm)*

**Purpose.** Usage report for inventory items within a date range. Supports detail or summary output and optional exclusion of adjustments.

**General operation.** Select from/thru date range. Filter by item numbers, Class, Category, Item Type. Indicate whether to include adjustments, whether to run summary only, whether to consolidate totals or separate by transaction type, and optionally filter by quantity range to include only transactions of a certain size.

---

## IN-Q — Print Labels with Lot/Serial Info

*Source: [in-q_print_labels_with_lot_serial_info.htm](../../../samples/chm/extracted/in-q_print_labels_with_lot_serial_info.htm)*

**Purpose.** Print inventory labels including Lot and/or Serial number information, driven from an imported list of items. Supports batch printing of multiple label formats in a single run.

**General operation.** Enter the path and file name of the import file. Specify which column of the file contains the Item Number, quantity of labels to print, Lot number, and Serial number. If the same quantity should print for all items, enter that quantity on the screen after defining the import file columns.

This program uses the RTM Print Group assigned to items in IN-B Enter Inventory. Custom label RTM variants (e.g., `T7ING1A.RTM` for Print Group `A`) are automatically selected for items with the matching Print Group setting. Multiple formats can be printed in a single batch as long as all formats use the same size label stock.

---

## Cross-references

The Inventory module is the foundation of the EvoERP item master and interacts with every transaction-processing module.

| Module | Relationship |
|--------|-------------|
| **BM — Bills of Material** | Item types F, A, B, L, T, M are used as parents and components in BOMs. Standard cost rollups (BM-G) flow through BOM structure to IN-L-A standard cost fields. IN-L-L identifies inactive BOM components. IN-L-N copies items with their BOMs. |
| **WO — Work Orders** | Work orders consume inventory (type I — stock issue to WIP) and produce inventory (type W — WO receipt to stock). Cycle codes set in IN-B control PI-A Capture Frozen Inventory. ITP codes (IN-L-Q) print on shop travelers. |
| **PO — Purchase Orders** | PO receiving creates type P transactions (to stock), type J (to WIP), and type Q (to QC). Approved vendor controls in IN-B enforce PO-L Assign Vendors to Items. Purch UM, PO Conv Mult, Weight, and Foot Factor in IN-B all drive PO pricing calculations. IN-L-E updates standard costs from last or average PO receipt costs. |
| **SO — Sales Orders** | Shipments create type S transactions. Customer cross-references (IN-L-C) auto-populate SO comment lines. Base price from IN-B is the default SO price. Shipping Lead Time in IN-B sets estimated ship dates. |
| **GL — General Ledger** | Item classes (set up in SM-C, assigned in IN-B) determine which GL asset accounts are debited/credited for each inventory transaction. IN-N-A supports month-end GL reconciliation. IN-N-D identifies discrepancies between inventory sub-ledger and GL. IN-L-H FIFO/LIFO bucket edits post directly to the GL asset account. IN-L-I Change Costing Method affects GL asset valuation. |
| **MR — Material Requirements** | Reorder Level and Minimum Order Qty from IN-B feed MRP planning. IN-D Reorder Report is the primary reorder worksheet. IN-M Summary Reorder Report provides a 4-month forward view. IN-L-S Rebuild Stock Status ensures MRP uses accurate on-order quantities. |
| **PI — Physical Inventory** | PI-A Capture Frozen Inventory uses Cycle Codes set in IN-B. IN-J Print Physical Check generates count sheets. IN-K Adjust Physical Levels enters count results. IN-L-T Reset Cycle Code maintains the cycle counting program. |
| **IM — International** | Multi-currency affects Last and Average cost displayed in IN-A. Duty Codes on items (IN-B) combine with vendor duty codes for landed cost processing. Tax-In flag causes excise tax backing-out on invoice/receipt posting. |
