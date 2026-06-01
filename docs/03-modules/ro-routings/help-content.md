# RO — Routings

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Items → Routings (22 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

---

## Contents

- [RO-A — Enter Routings](#ro-a--enter-routings)
- [RO-B — Print/Rollup Routing Costs](#ro-b--printrollup-routing-costs)
- [RO-C — Enter Work Centers](#ro-c--enter-work-centers)
- [RO-D — Enter Machines](#ro-d--enter-machines)
- [RO-E — Enter Tools](#ro-e--enter-tools)
- [RO-F — Enter QC Codes](#ro-f--enter-qc-codes)
- [RO-G — Enter Scrap Codes](#ro-g--enter-scrap-codes)
- [RO-H — Enter Departments](#ro-h--enter-departments)
- [RO-I — Enter Operation Templates](#ro-i--enter-operation-templates)
- [RO-J-A — Print Routings](#ro-j-a--print-routings)
- [RO-J-B — Print Work Centers](#ro-j-b--print-work-centers)
- [RO-J-C — Print Machines](#ro-j-c--print-machines)
- [RO-J-D — Print Tools](#ro-j-d--print-tools)
- [RO-J-E — Print QC Codes](#ro-j-e--print-qc-codes)
- [RO-J-F — Print Scrap Codes](#ro-j-f--print-scrap-codes)
- [RO-J-G — Print Departments](#ro-j-g--print-departments)
- [RO-J-H — Print Operation Templates](#ro-j-h--print-operation-templates)
- [RO-K — Enter Specification Templates](#ro-k--enter-specification-templates)
- [RO-L — Enter Sequence Print Control](#ro-l--enter-sequence-print-control)
- [RO-M — Enter Testing Method](#ro-m--enter-testing-method)
- [RO-N — Enter Test Requirements](#ro-n--enter-test-requirements)
- [RO-P — Update Processing Cost Standard](#ro-p--update-processing-cost-standard)
- [Cross-references](#cross-references)

---

## RO-A — Enter Routings

*Source: [ro-a_enter_routings.htm](../../../samples/chm/extracted/ro-a_enter_routings.htm)*

**Purpose.** Use this program to define how and where a finished good or assembly is manufactured. Each finished good or assembly is broken down into specific sequences (operations), which can be for direct labor or for outside processing. The information in the routing file is copied to the work order routing file when a work order is firmed in the Work Orders module. From there the information prints on the shop traveler. Routings can be used for costing purposes, or — if work centers are defined with $0 labor and overhead rates — as a written work instruction (e.g. for ISO 9000 certification) and for scheduling and capacity planning while labor costs are captured via a type L part number.

### Header Fields

| Field | Description |
|---|---|
| **Item number** | Inventory item number of the finished good or subassembly to be manufactured. Must be a valid item in the inventory file; should be inventory type `F` (finished good) or `A` (subassembly). |
| **Description** | Displays automatically from the inventory file. Cannot be edited. |
| **Lot** | Typical lot size (quantity) per production run. Used to convert setup cost (a flat dollar amount) and vendor minimum charges for outside processing into a per-unit cost for standard costing. A lot size of zero is treated as 1, so every piece will be charged the full setup time if no lot size is established. |

### Sequence (Line) Fields

| Field | Description |
|---|---|
| **Seq** | Routing sequence number. Three-character numeric field. Many users number sequences 10, 20, 30, etc. to leave room for insertions. Sequences print in numeric order on the shop traveler. |
| **Op** | Operation number of the labor process or outside processing at this sequence. If using operation templates (RO-I), the template number can serve as the operation number. An operation can occur more than once in a routing. If not using templates, the sequence and operation can share the same number. |
| **T** | Operation type. `L` = direct labor (in-house, default); `P` = outside processing (vendor service such as plating, painting, galvanizing); `A` = alternate operation (non-standard alternative — e.g., normally painted in-house but could be sent out if the plant is busy). The Print/Rollup Routings Costs program bypasses alternate operations in cost calculations. |
| **Description** | Short 30-character description of the operation. Shown on the shop traveler and various reports. |
| **Sequence Type** | Enter `R` if the sequence is always Run Time only; `S` if always Setup only; leave blank if either Run or Setup time may be reported against it. |
| **WC** | Work center code where this operation is to be performed. All sequences — including outside processing — must reference a valid work center. |
| **Rt#** | Routing number for shop traveler printing. Default is `1`. Multiple routing numbers allow multiple separate shop travelers to print from a single work order (e.g., breaking an assembly into three separate manufacturing processes). All sequences still belong to one logical routing; only the printed traveler is split. |
| **Time Type & Lines/Comp** | Controlled by SD-I Routings Defaults "Enable Template Time Types" setting. Leave blank or enter `F` for flat time per part. Enter `L` if sequence time is determined by the number of BOM line items (e.g., a stockroom kitting operation) — enter the number of line items in Lines/Comp and the program saves the calculated time as Setup time. Enter `C` if sequence time is a function of the number of components being processed (e.g., a soldering operation) — enter component count in Lines/Comp and the program saves the result as Run time. |
| **#Proc** | Number of processes within this operation (e.g., three bends = three processes; a nine-cavity mold = nine processes). Default is 1. If any value other than 1 is entered, a pop-up window appears for Time/Process, Processes/Hr, and Multiply or Divide by #Processes. |
| **Time/Process** | Time each individual process takes, in decimal hours (e.g., 3 minutes = `.0500` hours). Can be left blank if Processes/Hr is entered instead. |
| **Processes/Hr** | Standard processes per hour rate for this operation. Auto-calculated if Time/Process is entered; otherwise enter directly. |
| **Multiply or Divide by #Processes [M, D]** | `D` = divide processes/hr by the number of processes to get finished parts/hr (e.g., three bends at 120/hr ÷ 3 = 40 parts/hr). `M` = multiply processes/hr by the number of processes to get finished parts/hr (e.g., 10 shots/hr × 9 cavities = 90 parts/hr). |
| **Time/Pt & Decimal Time** | Time required to manufacture each piece. Can be entered in hours:minutes:seconds or as decimal time (allows values exceeding 99 hours or sub-second precision). Auto-calculated from Parts/Hr if that field is entered instead. |
| **Parts/Hr** | Number of finished parts per hour expected for this operation. Auto-calculated from Time/Pt if that is entered. Changing any one of Time/Pt, Decimal Time, or Parts/Hr recalculates the others. |
| **Setup** | Time required to set up this operation, entered in hours:minutes:seconds. The Print/Rollup Routings Costs program divides total setup cost by the lot size to compute a per-unit standard setup cost. |
| **Overlap - Forward** | Used by SH-E Finite Scheduling and SH-P Lead Time Scheduling. Entered in hours. After the sequence completes, parts do not move to the next sequence until this many hours have elapsed (e.g., waiting for paint to dry). |
| **Overlap - Backward** | Used by SH-E Finite Scheduling and SH-P Lead Time Scheduling. Entered in units of parts. Once this many parts have been completed in the current sequence, the next sequence can begin using those parts even though the current sequence is not yet finished — allowing sequences to overlap in time. |
| **Std Time?** | `Y` = standard time is automatically applied when production is reported, rather than requiring the operator to enter actual time. Used for operations impossible to track individually (e.g., one person simultaneously running 20 work orders on automatic machines). WO-F Enter Labor, DC-B Enter Production Only, and WO-M Batch Labor Entry all honor this flag. |
| **#Persons** | Number of persons required for this sequence. Allows two decimal places (e.g., `0.50` for one person running two work orders simultaneously). Print/Rollup Routing Costs multiplies the work center labor rate by this value to calculate standard labor cost. |
| **Mach** | Specific machine required for this operation, if any. Must be a valid entry from the machine file (RO-D). Description displays automatically. May be left blank. |
| **Tool** | Specific tool, die, mold, or fixture required for this operation. Must be a valid entry from the tool file (RO-E). Description displays automatically. May be left blank. |
| **Vend** | Vendor code for outside processing operations. Must be a valid vendor in the vendor file. If the vendor is not known in advance, a generic vendor (e.g., "Plating Vendor") can be created to signal the purchasing department at PO time. Leave blank if no specific vendor is pre-assigned. |
| **Cost** | Standard per-unit cost for the outside processing operation. Used by the standard costing system. If the work center has a Cost/lb default, the program prompts for a weight, multiplies it by that cost, and inserts the result here (overridable). |
| **Min Charge** | Minimum charge for an outside processing operation. Print/Rollup Standard Costs uses the greater of (lot size × cost) or the minimum charge. Estimating uses the greater of (quantity × cost) or the minimum charge. If the work center has a Minimum default, it auto-populates here (overridable). |
| **LT** | Lead time (days) for outside processing — the typical number of days between sending parts out and receiving them back. Copies in automatically from the work center's Lead Time field; may be overridden. Used by scheduling programs. |
| **Notes** | Free-form text, unlimited lines. Describes how the sequence is to be performed. Prints on the shop traveler. For outside processing sequences, notes can also pass through to the purchase order to the vendor. |
| **Specs** | Structured specification fields with predetermined headings, distinct from free-form notes. Used to capture die settings, temperatures, inspection fields, and other industry-specific parameters. Note: for columns in specs to align on the graphical traveler, the RTM font for that section must be set to a non-proportional font (e.g., Courier New) using the Report Editor (TA-M). |

### General Program Operation

Enter the item number of the finished good or subassembly. If no routing exists yet, the program prompts: "A Routing has not yet been set up for this part. Would you like to use the Routing Generator to quickly accomplish this?" Answering `Y` displays a list of operation templates from RO-I. Select templates in sequence order, click Save, and a complete routing is generated automatically. The sequence numbering increment (1, 2, 3, etc. or 10, 20, 30, etc.) is preset in SD-I Routings Defaults.

If `N` is chosen, sequences are entered manually. In the Seq field, press F2 (or click Display Lines) to view existing sequences. In the Op field, press F2 (or click Operation Templates) to copy individual templates from RO-I. Once templates are copied in, they can be moved into the entry area and edited.

**Outside processing sequences:** Enter the vendor code, lead time (auto-populates from the work center), standard unit cost, and optional minimum charge. Notes can be entered to pass instructions through to the purchase order. For outside processing operations, the remaining direct-labor fields (time/pt, setup, machine, tool) are not applicable and cannot be entered.

**Direct labor sequences:** After entering the Rt#, the cursor moves to the #Proc field. Enter number of processes; if more than one, a pop-up window collects Time/Process, Processes/Hr, and M/D setting. Enter Time/Pt or Parts/Hr to establish the standard production rate. Enter Setup time if applicable (always establish a Lot size when using setup time). Set Std Time? to `Y` for operations where actual time tracking is impractical.

**Using Specification Templates:** Click the Enter Specs button to access the specifications screen. Click Copy Spec Templates to select a pre-defined template from RO-K. The template's fields populate the screen; fill in the specific values for this routing sequence.

**Copying Sequences from another Item Number:** With the cursor on the Description field, click Copy Routing and enter the source item number. Answering yes copies all sequences to the new routing, which then displays on screen ready for editing. This is faster than re-entering when many products share the same basic routing.

**Editing existing sequences:** From the Seq field, press F2 to display existing sequences in a window. Highlight and press Enter to move the sequence into the entry area. Edit as needed, then press F10 or click Save.

**Alternate operations** copy into the work order routing when a work order is firmed. If they should not print on the shop traveler, they must be deleted from the work order routing manually, or suppressed using RO-L.

---

## RO-B — Print/Rollup Routing Costs

*Source: [ro-b_print_rollup_routing_costs.htm](../../../samples/chm/extracted/ro-b_print_rollup_routing_costs.htm)*

**Purpose.** Use this program to calculate standard costs for each routing sequence and produce a total standard cost for all sequences, broken out into setup, outside processing, labor, fixed overhead, and variable overhead. The program updates all routing sequences with current work center standard rates for labor and overhead. The resulting total standard costs are passed over to each item's inventory record and may be viewed in IN-B Enter Inventory or IN-L-A Enter Standard Costs. This program is an integral part of the inventory standard cost system.

This program is also incorporated within BM-G Print/Rollup Standard Costs. If doing a complete cost rollup for both routings and bills of material, BM-G can handle both and this program does not need to be run separately.

### General Program Operation

Enter a from/thru range of item numbers for the routings to roll up and print. Use F2 or the Lookup button to select from a pop-up window. Pressing Enter through both fields selects all routings.

If only the cost update is needed and printing a potentially long report is not desired, the report can be directed to the screen. The newly calculated standard costs are passed to each item's inventory record at the same time the report runs, regardless of whether it is printed or sent to screen.

---

## RO-C — Enter Work Centers

*Source: [ro-c_enter_work_centers.htm](../../../samples/chm/extracted/ro-c_enter_work_centers.htm)*

**Purpose.** Use this program to organize the factory into work centers for costing and scheduling purposes. At least one work center must be set up to use Routings. Each routing sequence is assigned to a work center. Work centers can be in-house (with standard rates for setup, labor, fixed overhead, and variable overhead) or for outside processing (with lead time, cost-per-unit-weight/area, and minimum charge defaults).

When the Work Orders Defaults (SD-B) setting "Use Actual Costs in Labor Entry?" is set to `N`, the work center standard rates are charged to work orders as labor is reported. Work center loads can be compared to capacity using SH-I Print Work Center Schedule and SH-R Work Center Scheduler.

### Parent-Child Work Centers (Finite Scheduling Only)

When using finite scheduling, identical machines or workstations within a work center can each be set up as their own child work center. A parent work center is then created to represent all its children. Routings normally assign sequences to the parent work center (exceptions allowed for operations requiring a specific child). When the finite scheduling program schedules a sequence assigned to a parent, it looks across the children and assigns the sequence to the child with the lowest contention (least waiting time).

For infinite, lead time, or manual scheduling, interchangeable machines should be combined into a single work center (e.g., five machines × 8 hours = 40 total hours/day in one work center). Parent-child work centers are not supported by these scheduling methods.

### Field Explanations

| Field | Description |
|---|---|
| **Work Center** | Code for the work center. 12 characters, alphanumeric, upper case only. Can be a sequential number, a short word, or a phrase. Can represent a department, a machine, an area, an employee, or an entire plant. |
| **WC Description** | 30-character description for the work center. Appears on reports and screens. |
| **Department** | Department code this work center is assigned to. 4 characters, alphanumeric, upper case only. Optional. Must be a valid entry from the department file (RO-H). Departments group work centers for reporting. |
| **Description** | Department description. Auto-populates from the department file. |
| **Is this a parent WC?** | `Y` if this is a parent work center (finite scheduling only). |
| **Parent WC** | If this is a child work center, enter the parent work center code here. Only used with finite scheduling. Leave blank if not using finite scheduling. |
| **Is this an outside processing WC?** | `Y` if this work center handles outside processing (vendor services). |
| **Use finite scheduling with this WC?** | Set to `N` for work centers (e.g., inspection) where capacity should not constrain the schedule. SH-E Finite Scheduling will treat this work center as having unlimited capacity. Also set to `N` if not using finite scheduling. |
| **Total Hours/Day** | Total production hours per day available in this work center (e.g., 5 people × 8 hours = 40 hours/day). Not used for outside processing work centers. For a parent work center, set to the average of its children, not the total. |
| **Total Shift Hrs** | Shift hours per day available for production (1 shift = 8 hrs, 2 shifts = 16 hrs, etc.). Used by SH-M Lead Time Estimator and SH-P Lead Time Scheduling to determine how many hours per day are available to routing sequences for a single work order (avoids allocating the entire work center capacity to one job). Cannot exceed 24. For child work centers, Total Shift Hrs must equal Total Hours/Day. |
| **% Utilization** | Percentage of total hours truly available, accounting for maintenance downtime, stoppages, etc. Entered as a number (e.g., `90.00` for 90%). Used by SH-E Finite Scheduling and SH-P Lead Time Scheduling to allocate run time. |
| **Setup Rate** | Standard setup rate ($/hour) charged for all setup time in this work center. |
| **Labor Rate** | Standard labor rate ($/hour) charged for all direct labor in this work center. |
| **Fixed OH** | Standard fixed overhead rate ($/hour) for all work in this work center. Applies to all direct labor and setup hours. If SD-B "Post overhead as % of Labor?" is `Y`, the rate is posted as a percentage of labor rather than a flat rate — the system displays the computed percentage next to this field (e.g., $25/hr overhead with $10/hr labor = 250.00% displayed). Both fixed and variable overhead rates are offered; some companies use only one. |
| **Variable OH** | Standard variable overhead rate ($/hour). Behaves identically to Fixed OH. Most companies that use a single rate use variable overhead. |
| **Estimating Fixed OH** | Fixed overhead rate used only in the Estimating module. Allows the estimating overhead rate to differ from the accounting overhead rate. |
| **Estimating Variable OH** | Variable overhead rate used only in the Estimating module. |
| **Lead Time** | Default lead time (days) for outside processing in this work center. Represents the typical number of days between sending items out and receiving them back. Copies into routing sequences assigned to this work center. |
| **Cost/lb/in/ft** | Default cost per pound, per inch, or per foot for outside processing work centers with weight- or surface-based pricing (e.g., plating, heat treating). Multiplied by the manufactured item's Weight or Foot Factor field (depending on Surface or Wt?) to calculate the routing Cost field. |
| **Minimum** | Default minimum charge for this outside processing work center. Populates the Min Charge field in routings assigned to this work center. |
| **Surface or Wt?** | Determines whether the outside processing cost formula uses the item's Weight field (`W`) or Foot Factor field (`S` for surface area). Inches or feet can be entered in the inventory Foot Factor field. |
| **Queue Times** | Button opens fields for Average, Priority 1, Priority 2, and Priority 3 queue times. Used by SH-M Lead Time Estimator, SH-N Generate Lead Times, and SH-P Lead Time Scheduling. Represents the typical number of days a work order waits upon arriving in a work center before production can begin, due to other work orders already in the queue. |

### General Program Operation

The opening screen lists existing work centers. Click a work center to edit it, or click Add (or press Insert) to create a new one. Enter a Work Center code, then a Description. Optionally assign to a Department (must exist in RO-H; select with F2).

If this is a parent work center, enter `Y` in Is this a parent WC?. If this is a child, enter the parent code in Parent WC. Parent-child relationships are only used with finite scheduling.

If this is an outside processing work center, enter `Y` in Is this an outside processing WC?. The cursor moves to the OUTSIDE PROCESSING section for Lead Time, Cost/lb/in/ft, Minimum, and Surface or Wt? defaults. When saving a work center where outside processing fields have changed, the system prompts to update all standard routings and operation templates, and all work order routings (e.g., to propagate a new lead time to all affected routing records).

For in-house work centers, enter Total Hours/Day, Total Shift Hours, and % Utilization. Then enter the standard rates (Setup Rate, Labor Rate, Fixed OH, Variable OH). If using the Estimating module, enter the Estimating Fixed OH and Estimating Variable OH rates. To enter queue times, click the Queue Times button.

Save with Alt-S or the Save button; the opening screen is returned to for additional entries. Exit with Alt-X.

---

## RO-D — Enter Machines

*Source: [ro-d_enter_machines.htm](../../../samples/chm/extracted/ro-d_enter_machines.htm)*

**Purpose.** Use this program to set up machines in a database file. Scheduled maintenance intervals can be established by specifying the number of machine hours between services. The system automatically logs machine hours via the Work Orders module (WO-F Enter Labor, WO-M Batch Labor Entry, or Data Collection), and free-form notes can be maintained for service history.

### General Program Operation

Enter a machine number (4 characters, alphanumeric). For existing machines, type the code or use the Lookup icon (F2) — the description auto-populates. For new machines:

1. Enter a 30-character description.
2. Specify the work center where this machine is located (the work center and machine can be the same entity in some cases).
3. If using scheduled maintenance, enter the number of hours planned between servicing.
4. Enter the date of last service if known.
5. Leave Hours Used to Date blank unless known — the system increments this automatically as machine hours are reported through WO-F, WO-M, or Data Collection.
6. Enter any notes (service records, specifications, etc.).

Save from any point by clicking Save.

---

## RO-E — Enter Tools

*Source: [ro-e_enter_tools.htm](../../../samples/chm/extracted/ro-e_enter_tools.htm)*

**Purpose.** Use this program to set up tools, molds, dies, fixtures, etc. in a database file. A preventive maintenance program can be established by specifying how many parts should be produced between maintenance cycles. The system automatically tracks production parts through WO-F Enter Labor and can report how many parts have been produced since the last maintenance.

### General Program Operation

Enter a Tool Number (15 characters, alphanumeric, upper case only). Often users use the item number of the item being produced as the tool number. For existing tools, type the code or use Lookup (F2) — description auto-populates. For new tools:

1. Enter a 30-character description.
2. Enter the number of parts to produce between scheduled maintenance (optional).
3. Enter the date of last maintenance if known.
4. Leave Parts Produced to Date blank — the system increments this automatically as production is reported through WO-F, WO-M, or Data Collection.
5. Enter any notes.

Save with the Save button.

**Extra Fields:** Clicking the Extra Fields button opens a screen listing various additional fields that may apply to different types of tools, as well as the machine the tool may be used on.

---

## RO-F — Enter QC Codes

*Source: [ro-f_enter_qc_codes.htm](../../../samples/chm/extracted/ro-f_enter_qc_codes.htm)*

**Purpose.** QC codes are user-defined codes used to track rework labor in WO-F Enter Labor, WO-M Batch Labor Entry, and Data Collection, and to track purchased parts accepted as "Use as is" in PO-J-C Enter Inspection Buyoffs. These codes are a valuable element of an overall quality assurance program.

### General Program Operation

Enter a QC Code (2 characters, alphanumeric, upper case only). The code is user-defined. Codes can be created to categorize rework labor by cause: operator error, machine error, tooling error, etc. For existing codes, type the code or use Lookup (F2) — description auto-populates. For new codes, enter a 30-character description. The program then prompts to save.

---

## RO-G — Enter Scrap Codes

*Source: [ro-g_enter_scrap_codes.htm](../../../samples/chm/extracted/ro-g_enter_scrap_codes.htm)*

**Purpose.** Scrap codes are user-defined codes used to track unplanned scrap of assemblies through WO-F Enter Labor, WO-M Batch Labor Entry, or Data Collection; unplanned scrap of components through WO-G Issue Materials; and parts returned to vendor as rejected in PO-J-C Enter Inspection Buyoffs. These codes are a valuable element of an overall quality assurance program.

### General Program Operation

Enter a Scrap Code (2 characters, alphanumeric, upper case only). The code is user-defined. Codes can be created to categorize scrap by cause: operator error, machine error, tooling error, bad material, etc. For existing codes, type the code or use Lookup (F2) — description auto-populates. For new codes, enter a 30-character description. The program then prompts to save.

---

## RO-H — Enter Departments

*Source: [ro-h_enter_departments.htm](../../../samples/chm/extracted/ro-h_enter_departments.htm)*

**Purpose.** Use this program to set up a department database file. Work centers may be assigned to departments for broader groupings. Departments are currently used only as selection criteria on reports.

### General Program Operation

Enter a Department Code (4 characters, alphanumeric, upper case only). For existing departments, type the code or use Lookup (F2) — description auto-populates. For new departments, enter a 30-character description. The program then prompts to save.

---

## RO-I — Enter Operation Templates

*Source: [ro-i_enter_operation_templates.htm](../../../samples/chm/extracted/ro-i_enter_operation_templates.htm)*

**Purpose.** Use this program to set up templates for commonly used manufacturing operations. The template record is structurally identical to the routing sequence record, allowing default values to be pre-set for all possible fields. Templates can be copied into routings individually (by pressing F2 in the Op field of RO-A) or as a group in sequence order using the Routing Generator (invoked automatically when a new routing is created in RO-A). See RO-A for details on how templates are copied into sequences.

### General Program Operation

Enter a template number in the Template No field — this represents the standard operation number for this operation. Select an operation Type from a pop-up window: `A` (Alternate Operation), `L` (Labor), or `P` (Outside Processing).

Optionally enter a user-defined **Class** code to group similar templates together. The Class code is used as a filter on operation template lookups, making it faster to find the right template among many.

Set up the template exactly as a routing sequence would be set up. The difference is that a template is not for a specific item but for a generic operation usable on many products. See RO-A field explanations for all fields.

Click the Notes button to enter free-form instructions for this operation. Click Prev (or PgUp) from the Notes screen to return to the main template screen.

### Time Types

Controlled by SD-I Routings Defaults "Enable Template Time Types" setting.

| Time Type | Meaning |
|---|---|
| Blank or `F` | Flat time per part Run time plus possible Setup time. Standard behavior. |
| `L` | Time determined by the number of BOM line items, independent of work order quantity (e.g., stockroom kitting). Enter time per line item in the decimal time/part field. When this template is copied into RO-A, the operator enters the number of line items, and the program multiplies by this factor and saves the result as Setup time. |
| `C` | Time is a function of the number of components processed (e.g., a soldering operation). Enter time per component in the decimal time field. When copied into RO-A, the operator enters the component count, and the program multiplies by this factor and saves the result as Run time. |

---

## RO-J-A — Print Routings

*Source: [ro-j-a_print_routings.htm](../../../samples/chm/extracted/ro-j-a_print_routings.htm)*

**Purpose.** Use this program to produce a listing of all or a range of routings and all their associated data fields.

### General Program Operation

Enter a from/thru range of item numbers by typing or using F2/Lookup. Pressing Enter through both fields selects all routings. The report shows all data field values in the routing file for the selected item numbers.

---

## RO-J-B — Print Work Centers

*Source: [ro-j-b_print_work_centers.htm](../../../samples/chm/extracted/ro-j-b_print_work_centers.htm)*

**Purpose.** Use this program to print a list of work centers and all their associated data field values.

### General Program Operation

Enter a from/thru range of work center codes (type or use F2/Lookup). Optionally enter a from/thru range of department codes to restrict the report to work centers in specific departments. Pressing Enter through all fields selects all work centers and departments.

---

## RO-J-C — Print Machines

*Source: [ro-j-c_print_machines.htm](../../../samples/chm/extracted/ro-j-c_print_machines.htm)*

**Purpose.** Use this program to produce a listing of machines and the data field values associated with each machine record.

### General Program Operation

Enter from/thru ranges of machine numbers (type or use F10/Save button to select). Optionally restrict the report to a range of last maintenance dates. To include all dates up to a specified date, enter `01/01/30` as the starting date. Running this report on a regularly scheduled basis, combined with machine-time tracking through the work order system, supports a true preventive maintenance program.

---

## RO-J-D — Print Tools

*Source: [ro-j-d_print_tools.htm](../../../samples/chm/extracted/ro-j-d_print_tools.htm)*

**Purpose.** Use this program to print a listing of tools and the data field values associated with each tool record.

### General Program Operation

Enter a from/thru range of tool numbers (type or use F2/Lookup). Optionally limit the report to a range of last maintenance dates. To include all dates up to a specified date, enter `01/01/30` as the starting date. Running this report regularly, combined with parts-produced tracking through the work order system, supports a true preventive maintenance program for tooling.

---

## RO-J-E — Print QC Codes

*Source: [ro-j-e_print_qc_codes.htm](../../../samples/chm/extracted/ro-j-e_print_qc_codes.htm)*

**Purpose.** Use this program to produce a listing of QC codes and their descriptions.

### General Program Operation

Enter a from/thru range of QC codes (type or use F2/Lookup). Pressing Enter through both fields selects all codes.

---

## RO-J-F — Print Scrap Codes

*Source: [ro-j-f_print_scrap_codes.htm](../../../samples/chm/extracted/ro-j-f_print_scrap_codes.htm)*

**Purpose.** Use this program to produce a listing of scrap codes and their descriptions.

### General Program Operation

Enter a from/thru range of scrap codes (type or use F2/Lookup). Pressing Enter through both fields selects all codes.

---

## RO-J-G — Print Departments

*Source: [ro-j-g_print_departments.htm](../../../samples/chm/extracted/ro-j-g_print_departments.htm)*

**Purpose.** Use this program to produce a listing of departments and their descriptions.

### General Program Operation

Enter a from/thru range of department codes (type or use F2/Lookup). Pressing Enter through both fields selects all departments.

---

## RO-J-H — Print Operation Templates

*Source: [ro-j-h_print_operation_templates.htm](../../../samples/chm/extracted/ro-j-h_print_operation_templates.htm)*

**Purpose.** Use this program to produce a listing of operation templates and their associated field values. This report is valuable to production planners who use templates heavily in routing setup.

### General Program Operation

Enter from/thru ranges for template numbers (type or use F2/Lookup). Optionally limit the report to templates within specific work centers by entering a from/thru range of work center codes (type or use F2/Lookup). Optionally limit by operation type: `A` (alternate), `L` (direct labor), `P` (outside processing).

---

## RO-K — Enter Specification Templates

*Source: [ro-k_enter_specification_templates.htm](../../../samples/chm/extracted/ro-k_enter_specification_templates.htm)*

**Purpose.** Use this program to create templates for specification blocks that are included in routings and shop travelers. A specifications block supplements the free-form notes that can be attached to each routing sequence. Within a specifications block, custom fields, column headings, and text can be defined. Different industries use these templates to hold informational fields not in the standard database — set-up parameters, temperature settings, inspection procedures, and so on. An unlimited number of specifications templates can be created.

### General Program Operation

Enter a template number (user-defined code, 15 characters, alphanumeric). This is the code used to identify the template when copying it into a routing through RO-A.

The template is built line by line. Up to four fields can be placed horizontally across each line. Current Line and Total Lines are displayed at the top. Fields can be used as column headings, or typed continuously across columns to create a continuous line of text, or used one column at a time with a row heading per line. Dashes or equal signs can simulate underlines to give the appearance of a printed form. With four horizontal columns and unlimited rows, templates can visually resemble actual forms or inspection documents.

While entering templates, Insert Lines (F3) inserts a new row and Delete (F4) removes a row.

### Using Specification Templates

During routing entry in RO-A, click the Specs button to access the Specifications screen. Then click Copy Specs Templates to select a pre-defined template. Highlight the desired template and press Enter — the template's pre-defined fields populate the screen. Fill in the specific values for this routing sequence.

Note: for specification columns to align on the graphical shop traveler, the relevant RTM section must use a non-proportional font (e.g., Courier New) via the Report Editor (TA-M Forms Editor).

---

## RO-L — Enter Sequence Print Control

*Source: [ro-l_enter_sequence_print_control.htm](../../../samples/chm/extracted/ro-l_enter_sequence_print_control.htm)*

**Purpose.** Use this program to suppress selected routing sequences from printing on shop travelers. Some sequences are included in routings for estimating cost calculations but are not relevant to the production process. These sequences must remain in the routing for cost recalculation purposes, but should not appear on the shop traveler printed for the shop floor.

### General Program Operation

Press F2 (or click Lookup) and enter the routing's parent item number. All sequences for that item are displayed. Highlight the desired sequence and press Enter or click it. The parent item number, description, sequence, and operation description appear. Enter `N` in the **Print on Shop Traveler?** field and save the record. That sequence will no longer print on shop travelers.

---

## RO-M — Enter Testing Method

*Source: [ro-m_enter_testing_method.htm](../../../samples/chm/extracted/ro-m_enter_testing_method.htm)*

**Purpose.** Use this program to enter testing methods and instructions for testing to be performed and recorded using HH-I Paperless Shop Floor Tracking.

### General Program Operation

Enter a Test Code or select an existing one. For a new code, the revision defaults to `1` and today's date. Enter a 2-line description. Then either click **Notes** to type the testing instructions directly, or click **Links** if the instructions reside in an external document (such as a PDF).

---

## RO-N — Enter Test Requirements

*Source: [ro-n_enter_test_requirements.htm](../../../samples/chm/extracted/ro-n_enter_test_requirements.htm)*

**Purpose.** Use this program to enter testing result requirements for testing to be performed and recorded using HH-I Paperless Shop Floor Tracking.

### General Program Operation

Enter the following:

- **Item Number** — the item being manufactured.
- **Routing Sequence** — the sequence number where testing is to be performed.
- **Test Number** — a user-defined identifier for this test requirement.
- **Test Method Code** — references a test method entered in RO-M.
- **Per item or Sample** — indicate whether testing is performed on each individual item, or on a sample that approves a batch of parts.
- **Pass/Fail or Numeric** — indicate whether the test records a simple pass/fail result or a numeric measurement. If Numeric, enter the upper and lower limits allowed.
- **Batch size** — if batch testing, indicate how many parts are approved by a single passing test result.

---

## RO-P — Update Processing Cost Standard

*Source: [ro-p_update_processing_cost_st.htm](../../../samples/chm/extracted/ro-p_update_processing_cost_st.htm)*

**Purpose.** Use this program to update the outside processing cost on Routings (used in standard cost rollup) by using the most recent Service PO receipt. This allows routing outside processing costs to stay current with actual vendor pricing without manually editing each routing record.

### General Program Operation

Enter the following selection criteria:

- **Receipt date range** — limits the update to receipts within a specified period.
- **Item range** — limits the update to a range of item numbers.
- **Specific sequence** — optionally limit to a particular routing sequence number.
- **Update Vendor, Cost, or Both** — controls which fields are updated: the vendor code, the outside processing cost per unit, or both fields simultaneously.

---

## Cross-references

| Related Module | Relationship |
|---|---|
| **WO — Work Orders** | Routing sequences copy into the work order routing file when a work order is firmed (WO-B Firm Work Orders). Labor is reported against routing sequences through WO-F Enter Labor and WO-M Batch Labor Entry. Machine hours and tool production counts are automatically updated as labor is posted. |
| **SH — Scheduling** | Work center capacity fields (Total Hours/Day, Total Shift Hrs, % Utilization, Queue Times) directly drive all scheduling programs: SH-E Finite Scheduling, SH-P Lead Time Scheduling, SH-M Lead Time Estimator, SH-N Generate Lead Times, SH-I Print Work Center Schedule, and SH-R Work Center Scheduler. Forward Overlap and Backward Overlap fields in routing sequences are used by SH-E and SH-P. |
| **BM — Bills of Material** | BM-G Print/Rollup Standard Costs incorporates the RO-B routing cost rollup, enabling a single combined rollup of both material and routing costs. |
| **IN — Inventory** | Rolled-up routing costs are passed to each item's inventory record. Standard costs (labor, setup, outside processing, fixed OH, variable OH) are viewable in IN-B Enter Inventory and IN-L-A Enter Standard Costs. |
| **PO — Purchase Orders** | For outside processing sequences, routing notes pass to the purchase order sent to the vendor. RO-F QC Codes and RO-G Scrap Codes are used in PO-J-C Enter Inspection Buyoffs when parts are accepted as "use as is" or returned as rejected. RO-P uses Service PO receipts to update outside processing cost standards on routings. |
| **DC — Data Collection** | DC-B Enter Production Only honors the Std Time? flag on routing sequences to auto-apply standard time when production is reported. |
| **HH — Paperless Shop Floor** | RO-M Enter Testing Method and RO-N Enter Test Requirements define tests that are executed and recorded in HH-I Paperless Shop Floor Tracking. |
| **SD — System Defaults** | SD-I Routings Defaults controls the sequence numbering increment for the Routing Generator and the "Enable Template Time Types" flag that activates the Time Type field in RO-A and RO-I. SD-B Work Orders Defaults controls whether actual or standard rates are used when posting labor and overhead. |
| **TA — Tools & Administration** | TA-M Forms Editor (Report Builder) is used to set non-proportional fonts on the shop traveler RTM for specifications block column alignment. |
