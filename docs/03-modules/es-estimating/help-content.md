# ES — Estimating

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Manufacturing → Estimating (10 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

1. [ES-A — Enter Estimates](#es-a--enter-estimates)
2. [ES-B — Print Customer Quote](#es-b--print-customer-quote)
3. [ES-C — Print Internal Estimate Sheet](#es-c--print-internal-estimate-sheet)
4. [ES-D — Quick Estimate](#es-d--quick-estimate)
5. [ES-E — Convert Estimates](#es-e--convert-estimates)
6. [ES-H — Enter Material Costs](#es-h--enter-material-costs)
7. [ES-I — Print Material Costs](#es-i--print-material-costs)
8. [ES-K — Update Inventory from Production](#es-k--update-inventory-from-production)
9. [ES-L — Edit Estimating Inventory](#es-l--edit-estimating-inventory)
10. [ES-M — Estimating Inventory Inquiry](#es-m--estimating-inventory-inquiry)

---

## ES-A — Enter Estimates

*Source: [es-a_enter_estimates.htm](../../../samples/chm/extracted/es-a_enter_estimates.htm)*

**Purpose.** Use this program to enter or revise estimates. The program allows entry of multiple lines per estimate, each with up to 10 estimate quantities.

### General Program Operation

The first part of the program operates the same as SO-A (Enter Sales Orders). Customer information is entered into the header and then the operator advances to the line item screen.

Once an item number is entered (which can be new — if so, it is created and saved only to the Estimating file, not the production inventory file) and the item description is tabbed through, the program opens an Estimating detail screen for that line. Details for using that screen are described under ES-D (Quick Estimate) below. Once the detail screen is saved, the program returns to add an additional line.

### Key behaviors

- New item numbers entered here are written only to the Estimating file, not to the production inventory.
- Each line in the estimate is individually detailed through the ES-D Quick Estimate screen.
- Header entry mirrors the SO-A sales order header (customer, address, job number, etc.).
- Multiple lines are supported per estimate number.

---

## ES-B — Print Customer Quote

*Source: [es-b_print_customer_quotes.htm](../../../samples/chm/extracted/es-b_print_customer_quotes.htm)*

**Purpose.** Use this program to print a customer quote, which can then be mailed, emailed, or faxed to the customer. The form default can be set in SD-G (Estimating Defaults).

### General Program Operation

Print a range of quotes by selecting from/thru ranges of:

- Estimate numbers
- Customer codes
- Customer classes
- Job numbers

To print a single quote, limit the quote number fields to that one quote.

### Print options

| Option | Description |
|---|---|
| **Notes** | Whether to include quote notes on the printed form. |
| **Hidden Notes** | Whether to include hidden notes on the printed form. |
| **Kit Components** | Whether to list kit component details. |
| **Extensions** | Whether to print extended pricing. |
| **Linked Documents** | Whether to include linked document references. |

After making selections, click Print.

---

## ES-C — Print Internal Estimate Sheet

*Source: [es-c_print_internal_estimate_sheet.htm](../../../samples/chm/extracted/es-c_print_internal_estimate_sheet.htm)*

**Purpose.** Use this program to get a detailed printout of estimate costs and margins. This report is for internal use and is generally not sent to prospects or customers.

### Report structure

The report has four sections:

1. **Bill of Material** — component costs, either rolled up to one level or exploded through all product structure levels.
2. **Routings** — labor and machine time costs.
3. **Extra Charges** — any additional charges entered against the estimate.
4. **Summary** — a spreadsheet-format summary page reprinting the data visible on the Summary screen in ES-A. Only one summary page prints regardless of how many quantities are in the estimate.

Sections 1–3 repeat for each estimate quantity that is included in the run. The summary page covers all quantities at once.

Note: only estimate summary information is permanently stored in the estimate file. The estimate detail (BOM, routing, extra charges) is calculated on-the-fly each time this report is run.

### General Program Operation

Specify a range of quote numbers or select estimates from a pop-up window using F2 (Lookup).

**Summary only vs. full detail.** When prompted, answering Yes prints only the summary page. Answering No advances the cursor to the quote quantity section.

**Quantity selection.** Separate detail pages print for each quote quantity specified. On estimates with multiple lines and multiple quantities this can produce a very long report. To restrict output, enter Y only against the quantities for which detail is wanted.

**Multiple levels.** Answering No to the multiple-levels prompt rolls all lower-level costs up into single figures at the first level of the BOM. Answering Yes produces an exploded view showing costs at every level of the product structure.

**BOM remarks and notes.** The operator is prompted whether to include BOM remarks and notes on the report.

---

## ES-D — Quick Estimate

*Source: [es-d_quick_estimate.htm](../../../samples/chm/extracted/es-d_quick_estimate.htm)*

**Purpose.** Use this program to enter or revise estimates for a single item, or to update and edit individual lines of a multi-line estimate originally created in ES-A. For multi-line estimates, initial entry is typically done in ES-A, but subsequent edits to generate the BOM, routing, obtain vendor pricing, and roll up costs are more conveniently done line by line through this program.

### General Program Operation

#### Header fields

When creating a new estimate, the item number is required. After entering the item number (or when called from ES-A), enter:

| Field | Description |
|---|---|
| **Description** | Item description. If an Order Description was entered in the Estimate Header in ES-A, it is used automatically; otherwise enter one here. |
| **Drawing** | Drawing number for the item being estimated. |
| **Revision** | Revision level of the drawing. |
| **Expiration Date** | Date after which the estimate/quote is no longer valid. |
| **Quote Revision** | Optional revision counter for the quote itself. |
| **Opportunity Type** | Optional classification of the sales opportunity. |

#### Quantity breaks

Up to ten quantity breaks can be entered. Margins are pulled from Estimating Defaults (SD-G) but can be edited for the specific estimate.

#### BOM button

Clicking BOM opens BM-A (Enter Bills of Material) configured with a copy option that can copy from either Production BOMs or Estimating BOMs. All saves write to the Estimating file rather than to production.

#### Routing button

Clicking Routing opens RO-A (Enter Routings) configured with a copy option that can copy from either Production Routings or Estimating Routings. All saves write to the Estimating file rather than to production.

#### RFQ button

Once the BOM has been entered, clicking RFQ opens a list of all type-R (purchased) parts at all levels of the bill of material, showing the total quantity of each required per one top-level assembly. The list shows:

- Whether a primary vendor is assigned.
- The Standard Cost (used in the cost rollup if no RFQ or Estimating cost is entered).
- RFQ Status (blank on first entry; populated after RFQs are processed).

The operator can tag groups of items to generate RFQs, then select one or more vendors to send them to. Clicking Process generates the RFQs, which can then be printed and sent using PO-E (Enter/Print RFQs). Once vendors return pricing, the RFQ Prices button is used to enter the returned prices and designate which price for each item will be used in the estimate cost rollup.

#### Extra Charges tab

Used to enter any additional charges (beyond material and labor) that should be included in the estimate.

#### Summary tabs (Summary 1-5 and Summary 6-10)

These tabs calculate the rolled-up cost for each quantity break, add in the margins defined for this estimate, and generate a suggested price. The suggested price can be overridden — for example, to round to an even dollar amount.

#### Saving

Clicking Save stores the estimate detail. If this program was called from ES-A, saving returns to ES-A to add an additional line to the multi-line estimate.

---

## ES-E — Convert Estimates

*Source: [es-e_convert_estimates.htm](../../../samples/chm/extracted/es-e_convert_estimates.htm)*

**Purpose.** Use this program to convert estimates into sales orders and/or work orders. The program also adds any new inventory items associated with the quoted item's product structure into the production inventory file.

### General Program Operation

Enter the Quote Number of the estimate to be converted, or select one using F2 (Lookup). The Item Number displays for reference.

#### Conversion target

Indicate whether to convert to:

- A Sales Order only
- A Work Order only
- Both a Sales Order and a Work Order

The next available sales order and work order numbers are displayed automatically. Custom order numbers can be assigned manually if desired.

#### Prospect handling

If the estimate was originally entered against a Contact Manager prospect who is not yet a customer, the program prompts that it will create a customer file entry as part of the conversion. If the estimate was created in ES-D (Quick Estimate) with no customer attached, a customer can be entered at this point.

#### Additional prompts

| Prompt | Description |
|---|---|
| **Customer PO** | The customer's purchase order number to associate with the new order. |
| **Warehouse Location** | The warehouse location to assign. |
| **Save Estimate Number with Customer PO** | Whether to record the estimate/quote number alongside the customer PO on the converted order. |

#### Line item conversion

All line items from the estimate are displayed. For each line the operator specifies:

- The quantity to convert (does not have to match the original estimate quantity break).
- The price (defaults to the estimate price for the selected quantity break but can be changed).

If converting to a Sales Order, an Estimated Ship Date is required. If converting to a Work Order, an Estimated Start Date and an Estimated Finish Date are required.

After entries are complete, clicking Process creates the orders.

---

## ES-H — Enter Material Costs

*Source: [es-h_enter_material_costs.htm](../../../samples/chm/extracted/es-h_enter_material_costs.htm)*

**Purpose.** Use this program to enter material costs for components that will be used within estimates. Up to five quantity/cost pairs can be entered per item to reflect quantity price breaks.

If no record exists in this file for a component, the estimate entry program falls back to the inventory Total Standard Cost defined in IN-L-A (Enter Standard Costs).

### General Program Operation

Enter the Item Number of the material item to be costed. This file is normally used only for items coded with an inventory type of:

| Type | Meaning |
|---|---|
| **R** | Regular (purchased parts) |
| **L** | Labor — if labor is defined as item numbers and included in BOMs rather than within routings |
| **T** | Outside processing — same condition as L above |

Enter each quantity and its corresponding cost. The first cost field applies from a quantity of zero through the first quantity specified. If there is only one price regardless of quantity, enter a quantity of 1.00 and a single cost. Tab through unused fields.

When saved, the program automatically records today's system date in the Last Update field as a reference for the next time the record is viewed or the material cost file is printed.

---

## ES-I — Print Material Costs

*Source: [es-i_print_material_costs.htm](../../../samples/chm/extracted/es-i_print_material_costs.htm)*

**Purpose.** Use this program to get a printout of material costs entered through ES-H (Enter Material Costs).

### General Program Operation

Specify:

- A from/thru range of item numbers.
- A from/thru range of Last Update dates.

The report can be viewed on screen, sent to a printer, or sent to a disk file.

---

## ES-K — Update Inventory from Production

*Source: [es-k_update_inventoiry_from_pr.htm](../../../samples/chm/extracted/es-k_update_inventoiry_from_pr.htm)*

**Purpose.** Use this program to copy the production inventory items and costs to the Estimating database.

### General Program Operation

Launch the program and click Go to process. All production items are copied. No selection criteria are offered — the copy covers the entire production inventory.

This program is used to synchronize the Estimating inventory database with production when item records or standard costs have changed in the production files.

---

## ES-L — Edit Estimating Inventory

*Source: [es-l_edit_estimating_inventory.htm](../../../samples/chm/extracted/es-l_edit_estimating_inventory.htm)*

**Purpose.** Use this program to edit the Estimating inventory records.

### General Program Operation

This program is identical to IN-B (Enter Inventory) but saves changes to the Estimating inventory database rather than the production inventory database. All fields and behaviors documented for IN-B apply here.

Use this program to add, edit, or delete items in the Estimating inventory that differ from their production counterparts — for example, to create estimate-only phantom items or to adjust cost fields used only in estimating.

---

## ES-M — Estimating Inventory Inquiry

*Source: [es-m__estimating_inventory_inq.htm](../../../samples/chm/extracted/es-m__estimating_inventory_inq.htm)*

**Purpose.** Use this program to view the Estimating inventory records (read-only).

### General Program Operation

This program is identical to IN-A (Inventory Inquiry) but looks at the Estimating inventory database rather than the production inventory database. All display fields and navigation behaviors documented for IN-A apply here.

Use this program to confirm the item data the Estimating module will use during estimate entry and cost rollup without the risk of inadvertently changing records.

---

## Cross-references

| Module | Relationship |
|---|---|
| **SO — Sales Orders** | ES-A header entry mirrors SO-A. ES-E conversion produces sales orders; the SO module then manages shipment and invoicing of the converted order. |
| **WO — Work Orders** | ES-E conversion can produce work orders. Work order start and finish dates are entered during conversion. |
| **BM — Bills of Material** | ES-D launches BM-A in Estimating mode to build the estimate BOM. Estimating BOMs are stored separately from production BOMs and are not visible in the production BM module until the estimate is converted. |
| **RO — Routings** | ES-D launches RO-A in Estimating mode to build the estimate routing. Same isolation pattern as BM above. |
| **IN — Inventory** | ES-K copies production inventory to the Estimating database. ES-L and ES-M provide edit and inquiry access to that shadow database. ES-H provides estimate-specific material costs that override IN standard costs during rollup. |
| **PO — Purchase Orders** | ES-D generates RFQs viewable and printable through PO-E (Enter/Print RFQs). Vendor pricing returned on RFQs feeds back into the estimate cost rollup via the RFQ Prices button. |
| **FO — Features and Options** | Estimates can include option-type items; kit component printing in ES-B controls whether option details appear on the customer-facing quote. |
| **SD — System Defaults** | SD-G (Estimating Defaults) sets the quote form default used by ES-B and supplies default margins loaded into ES-D quantity break screens. |
| **CM — Contact Manager** | Estimates can be entered against prospects (non-customers) in the Contact Manager. ES-E automatically promotes the prospect to a customer record when the estimate is converted. |
