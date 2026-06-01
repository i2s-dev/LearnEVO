# SD — System Defaults

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → System Defaults (22 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The System Defaults module is the central configuration hub for EvoERP. It contains one defaults screen for each major module in the system, plus two special-purpose programs: SD-Q (the master entry point that links to every sub-screen) and SD-R (which sets auto-incrementing next-numbers for all document types). Settings here are system-wide and take effect immediately without requiring users to exit; however SD-R is an exception that requires all other users to exit the company first. Only one user may be in SD-Q or any of its sub-programs at a time.

---

## Contents

- [SD-A — Company Defaults](#sd-a--company-defaults)
- [SD-B — Work Order Defaults](#sd-b--work-order-defaults)
- [SD-C — Purchase Order Defaults](#sd-c--purchase-order-defaults)
- [SD-D — Material Requirements Defaults](#sd-d--material-requirements-defaults)
- [SD-E — Scheduling Defaults](#sd-e--scheduling-defaults)
- [SD-F — Data Collection Defaults](#sd-f--data-collection-defaults)
- [SD-G — Estimating Defaults](#sd-g--estimating-defaults)
- [SD-H — Inventory Defaults](#sd-h--inventory-defaults)
- [SD-I — Routings Defaults](#sd-i--routings-defaults)
- [SD-J — Bill of Material Defaults](#sd-j--bill-of-material-defaults)
- [SD-K — Lot and Serial Control Defaults](#sd-k--lot-and-serial-control-defaults)
- [SD-L — Features and Options Defaults](#sd-l--features-and-options-defaults)
- [SD-M — Sales Order Defaults](#sd-m--sales-order-defaults)
- [SD-N — Sales Commission Defaults](#sd-n--sales-commission-defaults)
- [SD-O — Contact Manager Defaults](#sd-o--contact-manager-defaults)
- [SD-P — Customer/AR Defaults](#sd-p--customerar-defaults)
- [SD-Q — Master Defaults](#sd-q--master-defaults)
- [SD-R — Assign Next Numbers](#sd-r--assign-next-numbers)
- [SD-S — Warehouse Control Defaults](#sd-s--warehouse-control-defaults)
- [SD-T — Service Repair and RMA Defaults](#sd-t--service-repair-and-rma-defaults)
- [SD-U — Hand Held Defaults](#sd-u--hand-held-defaults)
- [SD-V — International Defaults](#sd-v--international-defaults)
- [Cross-references](#cross-references)

---

## SD-A — Company Defaults

*Source: [sd-a_company_defaults.htm](../../../samples/chm/extracted/sd-a_company_defaults.htm)*

**Purpose.** Enter or change defaults relating to overall company operation rather than any specific module. This is where global system behavior, company identity information, and cross-module security settings are established.

### Configuration Settings

**Configuration Settings** (numeric `0`, `1`, or `2`) — Controls whether selection-screen settings throughout the system can be changed by users. `0` or blank: no user can change settings; program defaults are always used. `1`: a system-wide set of defaults can be established but user-specific workstation settings are not available. `2`: system-wide defaults can be established and individual workstations can also maintain their own overrides.

**Password** — If Configuration Settings is `1` or `2`, this password is required to modify the system-wide defaults. If left blank, any user may change system-wide settings. Individual workstation settings never require this password.

**Alt. Drive for \ISTS\\** — Should always be `C` or blank unless Terminal Services or Citrix is in use. See the *Using Terminal Server and Citrix* help topic if some users connect remotely.

**Multiple Print Dialog Box [Y/N/A]** — After printing an RTM (report template): `Y` re-opens the print dialog so the user can, for example, preview and then email. `N` does not reopen it. `A` asks "Finished Printing?" before deciding.

**Remove EDI SO-IN file** — If `Y`, after importing EDI orders in ED-B the system prompts to clear the import file.

**Enable Del/Make Obsolete in IN-L-O** — If `Y`, the IN-L-O Inactive Items Utility is permitted to mark items Obsolete or delete them based on specified parameters.

**Enable Change/Save Default RTMs** — If `Y`, when a non-default RTM is used for a form or report the user is prompted whether to save it as the new default for that program.

**Maximize Evo Menu Screen on Start** — If blank or `Y`, the main menu is always maximized to full screen on startup. If `N`, the last saved menu size is restored instead.

**Trace Evo File Name** — Leave blank unless instructed by technical support for troubleshooting.

**Enable Evo Notes System** — If `Y`, memo-style free-form Notes are enabled for printing throughout the system. See *Using Evo Notes*.

**Enable Evo Links System** — If `Y`, enables full 256-character path/file name for linked documents and allows links to all master files (not just inventory items). When first enabling, use SM-S Enter Evo Links and click the rightmost toolbar icon (arrow) to convert previously entered inventory links. If the rightmost icon shows eyeglasses, conversion has already been done.

**Enable/Disable/Hide (E/D/H) BCC box?** — Controls whether users sending email can see and control the BCC field. `E` = enabled, `D` = disabled, `H` = hidden.

**Control Ship Via Code (Y/N/R/A)** — Controls use of a validated Ship Via code list (maintained in SM-O Enter Ship Via Codes) on Sales and Purchase Orders. `N` or blank: no checking. `Y`: only listed codes are allowed but the field may be left blank. `R`: code is required and must be from the list. `A`: new codes can be entered on the fly and are added to the list.

**Use Evo Login as Paperless Login** — If `Y`, the employee number in SM-G Enter Employees must match the login ID in PS-A System Users/Passwords. When a user loads HH-I Paperless Shop Floor Tracking they are automatically clocked in and can begin recording labor.

**Permanently Disable DBA Classic** — Works with the password encryption setting below. If passwords are encrypted, DBA Classic must be disabled.

**Permanently Encrypt Passwords** — Once enabled, all user passwords are encrypted in the database and DBA Classic can no longer be used. This change is permanent and cannot be undone. Requires that the ADMIN user exists in PS-A and that no users have blank passwords.

### Company Identity

**Company name** — 25-character alphanumeric field. Appears at the top of master menus and on various reports and forms.

**Address Line 1** — 25-character alphanumeric field.

**Address Line 2** — Additional address information, 25 characters.

**City, State, Zip** — 25-character field. If only one street address line is needed, City/State/Zip can go on Address Line 2 and this field used for phone, fax, or web address.

**If Your License Expires** — If the DBA Classic software license expires, each user logon replaces the name and address fields with a license-expired message. The product remains functional but the license grants no legal right to use. You may temporarily restore the correct name/address for printing purposes, but the expiration message restores itself on each logon. Once an updated license is installed, correct the name/address here.

### Multi-Company and Workflow Settings

**Parent or Subsidiary Company (P/S/N)** — `P` (Parent): IN-B, BM-A, SO-Q-A, AR-A, AP-A, and AM-C are editable and data is pushed down to subsidiaries. `S` (Subsidiary): those programs are view-only; data comes from the parent. `N`: standalone.

**Force Job Tracking (Y/N/R)** — `N` or blank: Job Numbers are optional on all screens. `Y`: Job Number is required on Sales Orders, Purchase Orders, Work Orders, AP Vouchers, and GL Journal Entries, but a new Job Number can be created on the fly. `R`: Job is required and must be selected from the preset list in SM-P-F Enter Jobs.

**Trigger Alerts for Order Entry Programs for New or All (N/A)** — `N`: Alert Notes assigned to Customers, Vendors, or Items pop up only on new order entry. `A`: alerts also pop up when editing existing orders.

**Use Ship Via Code for Customers (N/C/S)** — Requires Control Ship Via Code to be `Y`, `A`, or `R`. Enables use of customer shipping accounts (SM-U Customer Ship Via). `C`: uses accounts for the Billing Customer. `S`: uses accounts for the Ship-To customer.

**Use Ship Via Code for Vendors (Y/N)** — Not currently used.

**Enable USER Specific Settings (Y/N)** — If `Y`, user settings from US-A Customize Settings (Hot Keys, Email settings, etc.) are stored on the server by login name and are accessible from any workstation. If `N` or blank, settings are stored locally and are workstation-specific.

**Archive Dismissed Reminders older than ### days** — If populated, dismissed reminders older than the specified number of days are archived automatically upon login.

**Enable Broadcast Message for Security Level** — If populated, only users with a security level number lower than this value (as assigned in PS-A) may broadcast messages via Tools - Users.

**EDI Path** — If using EDI, enter the path one level above the TRANSFER subfolder where DBASO.IN import files are placed.

**Restrict limited access to license count (Y/N)** — If `Y`, limited-access licenses will not consume a full-access license slot once all limited-access licenses are in use.

---

## SD-B — Work Order Defaults

*Source: [sd-b_work_order_defaults.htm](../../../samples/chm/extracted/sd-b_work_order_defaults.htm)*

**Purpose.** Establishes set-up and processing parameters for the Work Orders module.

### Setup Tab

**Work Order Status Code** — Default status assigned when a work order is created. `S` = Scheduled (no labor or materials allocated). `F` = Firmed (labor and material allocated; most common default). `R` = Released (allocated and released to the shop floor with an actual start date).

**Default Priority Code [1/2/3]** — Priority used for scheduling. Open work orders sort by scheduled finish date within priority code on certain reports. Priority `2` is the most common default.

**Default Class Code** — One-character user-defined classification code for filtering on reports.

**View only in Enter WO Bills of Mat?** — If `Y`, users cannot edit the work order bill of material after creation; view only.

**View only in Enter WO Routings?** — If `Y`, users cannot edit the work order routing after creation; view only.

**Prevent Editing of Desc in WO-A (Y/N)** — If `Y`, the item description in WO-A cannot be modified.

**WO Types that Affect Bus Status** — Indicates whether Status `S` or `I` Work Orders should be included in the Business Status WIP total.

**Allow WO for Make From Items** — Indicates whether Work Orders are allowed for Make-From items.

**Disable Recalc Est Cost in WO-A (Y/N)** — If `Y`, WO-A does not recalculate Estimated cost, always retaining the original estimate.

**Use Material Burden & Burden Item #** — Sets up a Type N part as a placeholder for material burden transactions generated when issuing burdened materials to work orders.

**Show Open or Open/Closed WO in WO-A (O/B)** — `B` or blank: displays all work orders in the WO-A opening list. `O`: limits to open work orders only (note: this slows program load as closed WOs must be filtered).

**Allow Reopen Closed/Canceled WO (Y/N/P)** — `Y` or blank: anybody with access to WO-A can reopen closed or canceled work orders. `N`: cannot be reopened. `P`: a password (entered on the next line) is required.

**Allow Edit of Component Description in WO-G (Y/N)** — If `Y`, WO-G saves an edited description of items issued to work orders (useful for generic part numbers).

**Work Order Default Location** — If populated, Work Orders entered in WO-A are assigned to this location rather than the master Inventory Default Location.

**Calculate Labor from Bill of Material** — If `Y`, the DBA Classic version of Convert Estimate to WO allows BOM Labor items tied to routing sequences to populate routing sequence time.

**WO-B Limit to 1 Work Order** — If `Y`, ranges of work orders cannot be processed in WO-B Release Work Orders.

**WO-K-M Limit Scrap Type to (FMLV)** — If set to `F`, `M`, `L`, or `V`, only Scrap Codes of that type are allowed in WO-K-M Parts Requester.

**WO-K-M Require Reason Code** — If `Y`, WO-K-M Parts Requester requires a Reason (Scrap) Code.

### Processing Tab

**Labor Prompt in Kit Issues?** — `N`: labor type L items are automatically included in kit issues in WO-G and backflushed in WO-I. `Y`: a pop-up window asks whether to include labor on each kit issue, enabling simple labor job costing by routing separately.

**Backflush in Enter Finished Prod? (Y/N/A/B)** — `Y`: a pop-up asks whether to backflush components in WO-I. `N`: no backflushing available. `A`: always backflush without prompting. `B`: always backflush but only the quantity needed to bring the component quantity issued up to what is needed for the assemblies completed (supports mixing manual and backflush issuing).

**Close WO in Enter Finished Prod?** — `Y`: a pop-up offers to close the work order during WO-I Enter Finished Production. `N`: closing is always a separate step in WO-J. Note: if Process WIP Variance in WO-J is `Y`, this setting must be `N`.

**Use Std Cost in Ent Fin Prod?** — `Y`: finished goods always enter inventory at standard cost via WO-I. `N`: actual cost (calculated or manually entered) can be used.

**Use Actual Costs in Labor Entry?** — `Y`: employee-file labor rates are used for job costing in Work Orders and Job Costing modules. `N`: standard labor rates from work centers are used.

**Post Overhead as % of Labor?** — `Y`: overhead rates are a percentage of labor dollars. `N`: overhead rates are hourly rates applied per hour of labor.

**Divide Labor Cost by # Jobs Worked** — `Y`: if an employee works two or more work orders simultaneously, the labor cost is divided among them proportionally. `N`: each work order is charged the full labor rate. Affects WO-F, DC-A, and DC-C.

**Use Lead Time Scheduling (F/B/N)?** — `F`: forward lead time scheduling. `B`: backward lead time scheduling. `N`: use the lead time from the inventory master rather than the calculated lead time. See *How Lead Time Scheduling Works*.

**Backflush by Sequence in Enter Labor?** — `Y`: components tied to routing sequences are backflushed via a pop-up during WO-F Enter Labor, and also when posting via WO-N or DC-H. `N`: do not use this feature.

**Use Projected or Estimate $ and Hours (P/E)?** — `P`: enables WO-K-G Recalculate Projected Hours to recalculate labor hours after labor has been entered. Blank or `E`: this program is not available.

**WO-G Setting for Kit Issues (N,Y,L)** — Pre-defines the Kit Issue setting on the WO-G screen to `N`, `Y`, or `K` (list).

**Check Comps at Finished Production** — `Y`: WO-I and WO-J warn if sufficient components have not been issued to support the assemblies completed. `L`: same warning but labor parts are ignored.

**Specify Comp Loc in WO-G/WO-I** — `Y`: inventory location for components being issued or backflushed can differ from the Work Order Location for each component. `K`: one location can be specified for all components of a kit issue. `N`: components pull from the work order location.

**Check if Qty per Seq > WO Qty (Y/N/W)** — `Y`: prevents entering a quantity complete against a labor sequence greater than the WO quantity. `W`: warns but allows. `N`: no check.

**Reduce WO balance by FP Scrap (Y/N)** — If `Y`, scrap entered in WO-I also adds to the Work Order Quantity Completed, reducing the balance to be completed (as used by MRP, Inventory Inquiry, etc.).

**Allow WO Dates to update SO (Y/N)** — If `Y`, when a WO finish date changes in WO-A or a scheduling program, the user is prompted to also update the corresponding Sales Order Estimated Ship Date.

**Process FP Scrap Serial Number in WO-I (Y/N)** — Indicates whether finished production items scrapped in WO-I should be assigned a serial number.

**Reduce WO Balance by Lab scrap in WO-F (Y/N)** — Indicates whether the net quantity to be made on the work order should be reduced when a part is scrapped in WO-F.

**Process WIP Variance in WO-J** — If `Y`, when closing work orders in WO-J, any variance posting distributes to on-hand inventory up to the work order quantity; residual cost posts to WIP Variance. If `Y`, Close WO at Enter Finished Production is forced to `N`.

**Divide Overhead by Number of Jobs Worked** — If `Y`, overhead cost is divided by number of simultaneously worked jobs.

**Divide Setup by Number of Jobs Worked** — If `Y`, setup cost is divided by number of simultaneously worked jobs.

**Include FP Scrap in cost of good parts (Y/N/A)** — `Y`: scrap assembly cost is amortized among good parts. `N`: a separate transaction posts for scrap. `A`: asks each time. In all cases a Receipt record with a scrap code is generated; if backflushing is on, materials for scrapped assemblies are pulled.

**Remove Scrap $ in WO-F (Y/N)** — Indicates whether the cost of an item scrapped in WO-F should be removed from the Work Order or retained to roll into the eventual cost of the good parts.

**Process Paperless in Seq/Batch** — Indicates whether labor and test reporting in HH-I Paperless Shop Floor Tracking is tracked by Work Order and Sequence only, or by smaller batches within a work order.

**Enter Reg/OT hours together in WO-F** — Indicates whether WO-F will enter both Regular and Overtime hours in a single entry.

**Use WO Number as Lot Number in WO-P (Y/N/A)** — `N` or blank: Lot Number must be manually entered. `Y`: Work Order Number is automatically used as Lot Number without prompting. `A`: prompts but suggests the WO number as the default.

**Allow Dec Entry # Jobs Worked** — If `Y`, the Number of Jobs worked can be entered as a decimal to allocate costs disproportionally among simultaneous jobs.

**Control Over-Issues in WO-G (Y/N/A)** — `Y`: prevents issuing more of a component than the BOM requires. `N` or blank: over-issues allowed. `A`: asks when more than required is being issued.

**Use Markup to Calculate Scrap %** — `Y`: scrap percentage in BM-A is used as a markup (percent of base quantity needed). Blank or `N`: uses a margin calculation (percent of total needed). Example: 100-piece requirement with 20% scrap — Markup = 20 extra pieces; Margin = 25 extra pieces.

**Display Base Price in WO-I (Y/N)** — If `Y`, the base price of the item being manufactured is displayed as a reference in WO-I.

### Processing II Tab

**Display WO Number when Saving New WO (Y/N)** — If `Y`, the assigned work order number is displayed when saving a new work order in WO-A.

**Check Quantities per Sequence (Y/N)** — If `Y`, labor reporting compares the sequence start quantity with the quantity reported as complete.

**Prevent WO-G from taking Inventory negative (Y/N)** — If `Y`, the actual issue quantity will not take inventory negative regardless of what is entered on screen.

**Apply full overhead to team labor (Y/N)** — If `Y`, WO-F applies the full work center overhead to each member of a team when team-based labor is reported.

**Link Work Center Dept to GL Dept (Y/N)** — If `Y`, Absorbed Labor and Overhead postings in WO-F or Data Collection post to the GL Account and Department based on the Work Center Department.

**Pull Comps from Dflt Location regardless of WO Loc (Y/N/S)** — Blank or `N`: components pull from the Work Order Location. `Y`: components pull from the Default Location regardless of WO Location. `S`: only Service/Repair work orders pull from the Default Location.

**Prompt for user password in WO-F (Y/N)** — If `Y`, users must re-enter their password to enter labor.

**Prevent re-using Serial Number for the same item in WO-I (Y/N)** — If `Y`, the same serial number cannot be entered more than once for an item even if current on-hand is zero.

**AutoGen of Serial Numbers in WO-S and process in WO-I (Y/N)** — If `Y`, WO-S Label printing generates serial numbers for finished items when labels are printed, and WO-I uses those serial numbers for finished production.

**Process FP Scrap Lot No in WO-I, WO-F, DC-H (Y/N)** — If `Y`, Lot Controlled items scrapped in WO-I, WO-F, and DC require assignment of a Lot number.

**Allow Holiday Hours for regular WO in WO-F (Y/N)** — If `Y`, Holiday Labor can be entered against a Released Work Order (not only an Indirect Work Order).

**Limit Num of Decimal Places for WO-F (0,1,2)** — Enter the number of decimal places for hours entered in WO-F.

**Allow More QTY than needed in QWO (Y,N,W)** — `N`: Quick Work Order prevents creating a WO that would put more parts into stock than are on Sales Order. `W`: warns. Blank or `Y`: no check.

**Finished Production to post Standard Labor for Employee #** — If an employee number is entered, WO-I uses that employee number, the Routing time standard, and the quantity complete to post labor and overhead to the work order.

**Limit WO-J to closing 1 Work Order** — If `Y`, WO-J Close/Cancel Orders cannot be run for a range of work orders.

**WO-A Prevent WO Qty < Vendor Min Qty for O/P Oper (Y/N/A)** — `Y`: prevents creating a work order in WO-A for a quantity less than any vendor minimum for outside process operation. `A`: warns and asks whether to continue.

**Round to next Int Qty for Comps with same MR-D setting** — If `Y`, kit issues and backflushing of components with "Round MRP Quantities to the next whole number" also round up material issues to the next integer quantity.

**Enable Stock Room Management for Posting Part Request** — If `Y`, pulling components using WO-K-I Kitting System requires a separate supervisor review and posting using DE-K Import & Post Material Issues. Blank or `N`: saving in WO-K-I posts the material issue transactions immediately.

**WO-I Prevent Changing Actual Unit Cost (Y/N/W)** — `Y`: operator cannot modify the calculated unit cost generated by WO-I. `W`: warns but allows change. `N` or blank: no check.

**WOF/WOKK/WOM Update WO Actual Start Date (Y/N/W/A)** — `Y`: if labor is entered with a date prior to the WO Actual Start Date, the Actual Start Date is updated to match. `W`: warning only. `A`: asks whether to make the change.

**Track Lot/Serial or Both for Serialized parents** — `S`: serialized components can be mapped to specific serialized parent serial numbers. `L`: Lot Controlled components can be mapped to serialized parents. `B`: both. Requires preassigning parent serial numbers using WO-S Print Work Order Labels; mapping performed in WO-K-O and WO-K-P.

**WO-I Create BKARTXNS records to assign Serial # to SO** — If `Y`, WO-I assigns the serial numbers produced to the Sales Order line associated with the Work Order, eliminating re-entry of serial numbers when releasing for invoicing.

**Prevent WO-I and WO-P from posting negative unit cost** — If `Y`, when the final receipt for a work order would result in a negative unit cost, the cost is recalculated as total actual cost divided by total quantity made. Closing the work order then makes a WIP Variance posting for the difference.

**Disable Kit program from double validating part numbers** — If `Y`, WO-K-I Kitting System only requires a single scan of component part numbers rather than both a pick-list validation scan and a bin scan.

**Save in the Kit program will also post material issues** — If `Y`, WO-K-I posts material issues on save rather than requiring a separate review and posting in DE-K.

**WOI/WOP Backflush Prevent OH Negative** — If `Y`, backflushing components halts the finished production process if there is insufficient stock on hand.

**WOF/DCA/DCB Backflush Prevent OH Negative** — If `Y`, when backflushing components a warning pops up if there is insufficient stock and the component will not be issued.

**WOM Autopost Labor Records** — `Y`: saving a record in WO-M Batch Labor Entry posts immediately. `A`: user is prompted. Blank or `N`: does not autopost.

### Printing Tab

**Print BOM Remarks? - Traveler** — If `Y`, bill of material component remarks print on the shop traveler below each component.

**Print BOM Comments? - Traveler** — If `Y`, comments added to the work order bill of material print on the shop traveler below each component.

**Print Job Schedule? - Traveler** — If `Y`, related work orders sharing the same prefix are listed in the header of the shop traveler.

**Print Short Form? - Traveler** — `Y`: short format traveler. `N`: long format traveler.

**Print Bill of Mat? - Traveler** — If `N`, the bill of materials section is omitted from the shop traveler.

**Print Mat in Seqs? - Traveler** — If `Y`, BOM components tied to specific routing sequences print within those sequences on the traveler.

**Print Machine and Tool - Traveler** — If `Y`, machine and tool assignments print on shop travelers.

**Print Inspection Fields - Traveler** — If `Y`, optional inspection sign-off fields print on the traveler (quantity, first article, last article, accepted, rejected).

**Print Multi Routings? - Traveler** — If `Y`, sequences designated to print on different routing numbers produce multiple routings within the same work order when the traveler is printed.

**Print Routing Seqs Order (A/D)** — `A` (ascending) or `D` (descending) sequence order on graphical travelers. Descending is used when the traveler is to serve as a tear-off labor ticket.

**Print Short Header on Travelers** — If `Y`, multi-page travelers have an abbreviated heading section on pages after the first.

---

## SD-C — Purchase Order Defaults

*Source: [sd-c_purchase_order_defaults.htm](../../../samples/chm/extracted/sd-c_purchase_order_defaults.htm)*

**Purpose.** Controls setup and processing behavior for the Purchase Orders module.

### Setup Tab

**Default Entered by** — Default initials for the person who generates most purchase orders. Can be overridden per order.

**Default Ship Via** — Default shipping method. Can be overridden per order.

**Allow Service POs?** — `N`: no prompt appears in PO-A; all POs are Purchase type. `Y`: a window asks whether each PO is Purchase or Service type.

**Track PO Taxes using Tax Groups?** — `N`: all taxable POs use the default PO Tax rate (see next field) posted to the default account in AD-A. `Y`: vendors are assigned to Tax Groups and PO taxes are tracked and posted accordingly using SM-E Enter Tax Codes. US customers generally use `N`.

**Default PO Tax Rate** — Default percentage for tax on taxable POs when Tax Groups is `N`.

**Copy in customer PO's from Work Orders as comment lines?** — If `Y` and a work order number is specified on a PO line, the system asks whether to copy the customer's PO number from the work order to a comment line as a cross-reference.

**Allow Entry to Location / GL Department (Y/N/Require)** — Controls whether entry of an inventory Location or GL Department is required, optional, or prohibited on PO lines.

**Allow Closed PO's to be Reopened?** — If `Y`, PO-D View PO Receivers can reopen a closed PO.

**Rep Code for V.P. Report** — If a code is entered, the PO-I-H Vendor Performance Report can save vendor ratings as History records.

**Prevent Editing of Desc in PO-A (Y/N)** — If `Y`, the item description in PO-A cannot be modified.

**Enable Auto Line Numbers in PO-A** — If `Y`, purchase order lines are automatically numbered.

**Allow PO to Edit GL Acct (A,D,B,N)** — `A`: PO-A can edit the GL Account the line will post to. `D`: only the GL Department can be edited. `B`: both account and department can be edited. `N`: neither can be edited.

**Item Types for GL Edit** — Specifies which inventory types allow GL information editing. Typically type `N` (Non-Inventory) only.

**Enable APC Frt & Tax Distribution (Y/N)** — If `Y`, AP-C will redistribute tax and freight among the GL Accounts of the items purchased rather than posting to default Tax and Freight accounts.

**Item Types for Distrib** — Specifies which inventory types allow freight and tax cost distribution.

**Ask for Book Date when editing PO** — Indicates whether changes to a PO should be saved with a date other than the current system date for Business Status Booked Orders totals.

**Track Changes to Purchase Orders** — If `Y`, changes to Purchase Orders are tracked.

**Print Inventory Label after Receiving PO (Y/N/A)** — `Y`: labels for received items print automatically. `A`: prompts whether to print.

**Update PO Rev & Date when saving PO** — If `Y`, the incremental revision counter and change date are updated each time a PO is saved.

**AP-C Price Change update PO Price (Y/N/A)** — Indicates whether a price change in AP-C should update the PO line item price (Yes/No/Ask).

**PO-A Enter Digital Signature (Y/N/A)** — `Y`: prompted to enter digital signature authorization when saving a PO in PO-A. `A`: asked if you want to enter authorization. `N` or blank: no approval available in PO-A.

**PO-A to use Std, Last, Min Price (S/L/M/N)** — `S`: PO-A pulls in Standard cost. `L`: Last Cost. `M`: looks back 6 months and pulls the minimum price.

**Disable Delete Button in PO-A (Y/N)** — If `Y`, the ability to delete POs in PO-A is disabled.

**Allow Edit of Vendor Start Date in AP-A (Y/N)** — If `N`, manual editing of Vendor Start Date is prohibited.

**PO-Q Allow Entry to Price (Y/N)** — If `Y`, users with access to PO-Q Maintain PO Delivery Dates can also edit PO prices.

**PO-A Prevent Creating Vendors (Y/N)** — If `Y`, a user in PO-A cannot create a new vendor on the fly.

**Invoice PO Receipts through AP (Y/N)** — `Y`: PO Invoices are matched to PO Receipts as invoices are entered using AP-C Enter Purchase Order Invoices. `N`: POs close upon final receipt.

**AP-C/PO-K Save original PO when closing PO (Y/N)** — If `Y`, when a PO is closed and deleted from the Open PO file, an archive copy of the original PO is saved.

**PO-A to use Vendor pricing for type R & M items [Y/N/A]** — `Y`: PO-A is required to use Vendor pricing; if no Vendor Pricing exists, the PO line is not allowed. `N` or blank: Vendor pricing is used if it exists but is not required. `A`: asks.

**PO-Q Allow Entry to Quantity** — If `Y`, PO-Q Edit Receipt Dates can also edit line quantities.

### Processing Tab

**Require Pack Slip Info?** — Sets the default for the pack slip number requirement in PO-C Receive Purchase Orders. `Y`: pack slip number required for all receipts. `N`: optional.

**Receive Into** — Sets the default for receiving destination in PO-C: directly into Inventory or into QC Inspection.

**Receive all Lines?** — Sets the default for the "receive all lines" prompt in PO-C.

**Display Comment Lines?** — Sets the default for comment line display in PO-C.

**Display Fully Rec'd Lines?** — Sets the default for fully received line display in PO-C.

**Force PO to use approved vendors?** — Sets the default behavior for vendor approval checking in PO-A and in IN-B. Three options: X in "Do not check vendor approval status" (no restriction); X in "Warn if unapproved but allow use"; X in "Prohibit use of unapproved vendors". Item-level override available in IN-B.

**Require entry of Scrap Code** — Determines whether items rejected in PO-J-C Enter Inspection Buyoffs require a scrap code.

**Require entry of QC Code** — Determines whether items accepted "Use as Is" in PO-J-C require a QC Code.

**Access to Prices on Receivers** — Three levels: `0` or blank: view and change prices. `1`: view only. `2`: unit price field removed from the receiving screen.

**Percentage of Over Receipts Allowed** — If a PO line is received more than this percentage over quantity, a warning message is presented.

**Update Vendor Last Cost in PO-C** — If `Y`, PO-C updates Vendor Pricing (as seen in PO-H Enter Vendor Prices) with the PO price unless a record with quantity break pricing already exists. If no record exists, one is created; existing records without quantity breaks are updated.

**Check Stock Receiving Make From Comps** — `I`: Ignore (do not check on-hand for Make-From components). `W`: warn but allow the receipt. `P`: prevent the receipt if component stock would go negative.

**PO-C to Print QC Traveler** — `N` or blank: never print. `Y`: always chain to PO-J-A Print Receipt Travelers. `A`: prompts whether to print the traveler when parts are received to QC.

**Update Last Cost if Cost is $0.00** — `N`: PO-C does not update Last Cost for items received at $0.00 (such as vendor samples).

**Receive Non-Inventory Items at PO Price** — If `Y` and costing is Standard, Non-Inventory items (such as supplies) are received at PO price rather than standard cost (no PPV posted). Can be overridden at the item level.

**PO-C to Update Primary Vendor** — If `Y`, the Primary Vendor for items is updated to the vendor on the PO whenever a PO is received in PO-C.

**PO-C to Display Receiver Number on Save** — If `Y`, the receiver number is displayed whenever a PO receipt is saved.

**PO-A Default for Change Dates** — Default answer (`Y` or `N`) to "change all lines on a PO with a date" prompt.

**PO-A Disable Price Check for Qty Changes** — If `Y`, changing a quantity on a PO line does not recheck for quantity break pricing.

**PO-C to issue WO Comps for Service POs (Y/N/A)** — `Y`: components associated with the Work Order Sequence on a Service PO are issued to the work order when the PO is received. `A`: prompts. Blank or `N`: no issue.

**PO-C Update Unit Cost if Cost is $0** — `N`: Last Cost is not changed by a receipt at $0.

**PO-C Update Unit Cost and Vendor if less $** — If `Y`, receiving at a cost lower than Last Cost updates Last Cost and changes the Primary Vendor to the vendor on the PO.

**PO-A Recal Vendor Price for item on multi line (Y,N,A)** — If `Y`, vendor pricing for a blanket PO takes the total quantity across all lines into account.

**Enable PO-A Entry Security** — If `Y`, security levels can be used to prevent buyers from editing another buyer's PO.

**PO-C Auto-Generate Serial Numbers when receiving** — If `Y` and serial generation parameters are defined in SC-G Enter Serial Generation Parameters, PO Receiving automatically generates needed serial numbers.

**PO-C Auto-Generate Lot Numbers when receiving** — If `Y`, PO Receiving automatically generates lot numbers using the PO Number and an incremental counter per item.

**PO-A Warn if PO Due Date > WO Due Date** — If `Y` and a Work Order number is specified on the PO line, the program compares the PO Line Est Receipt date with the WO due date and warns if the PO will not arrive in time.

**PO-C 'E' Status Items Receive at PO Price if STDC=0** — If costing method is Standard and a part with Active Status `E` and zero Standard Cost is received, the PO Price is used as the cost of the receipt.

### Processing II Tab

**PO-C Default Item Receiving Bin** — If populated, all PO Receipts default to this bin (e.g., a staging area) and can then be transferred to final bin when moved to the stockroom.

**PO-C Print Lot Labels Upon Receipt** — `Y`: labels for Lot Controlled items print when received. `A`: user is prompted to print.

**PO-A Use Shop Calendar for Due Date** — If `Y`, the Shop Calendar is used to prevent a Due Date falling on a weekend or holiday.

**PO-E Use for Purchase Requisition** — If `Y`, PO-E Enter/Print RFQs pulls in part pricing the same as PO-A so the document can serve as an internal requisition form rather than a vendor RFQ.

**PO-B, E Separately email Multiple PO/RFQs** — If `Y`, multiple items emailed to a vendor simultaneously are separated into multiple PDFs rather than a single multi-page PDF.

**PO-A Risk Assessment Screen Access** — If `Y`, when saving a PO in PO-A a screen opens for entry of risk assessment information pertaining to the PO and its items.

**PO-C/HH-G Prevent PO Receipt X days** — If populated, PO Receipt is not allowed more than the specified number of days early based on the line Estimated Receipt date.

**PO-A Prior Due Days to flag PO as Expedite** — If populated, PO lines with a receipt date greater than this number of days past the WO due date are flagged "Rush"; lines late but within this threshold are flagged "Expedite". Rush/Expedite designations print in PO-B and are color-coded in PO-I-G.

**PO-C Freight Distribution Item Number** — If populated, PO-C allows entry of a freight vendor and amount; the freight amount is distributed to received lines proportioned by weight and a PO to the freight vendor is created so the freight invoice can be applied using AP-C.

**PO-C to Print Inventory in QC (Y/N/A)** — `Y` or `A`: when items are received to QC, PO-J-B Print Inventory in QC is called to print a list.

**PO-C to Print Receiving Report (Y/N/A)** — `Y` or `A`: when items are received to stock, PO-I-E Print Receiving Report is called.

**PO-A/IN-D Promise date for Unconfirmed PO** — Uses the specified date (e.g., several years in the future) as the Promise date when POs are created in PO-A or IN-D, making it obvious they have not been vendor-confirmed.

**PO-A Suppress prompt for multiple Mfg** — If `Y`, all approved manufacturers pull into the PO without prompting.

**PO-A Chg Due Dates without new Approvals** — If `Y`, the electronic signature on a PO is not cleared if only dates are changed.

**PO-A Prevent for Vend with Expired Review** — If `Y`, a PO cannot be entered for a vendor whose Quality Review date has passed.

### Printing Tab

**Print Co. Name/Address on forms?** — If `Y`, company name and address from SD-A prints in the upper left of POs and RFQs.

**RFQ Print Format Number** — Lookup to select from available RFQ print formats.

**Print Title on RFQ?** — Controls whether the title "REQUEST FOR QUOTE" prints on the form.

**PO Print Format Number** — Lookup to select from four graphical formats. Formats 1 and 3 are condensed (one line per line item, small font); Formats 2 and 4 print two lines per item with a larger, more readable font.

**Print Title on PO?** — Controls whether the title "PURCHASE ORDER" prints.

**Print PO Ending Lines?** — If `Y`, up to 5 ending lines (defined below) can print in the lower left corner of purchase orders.

**PO Ending lines** — Up to 5 description lines that appear at the end of a PO when ending lines are enabled.

**Max No Lines in Body of PO** — Number of lines in the PO body before a page feed. Used only for pre-printed forms with footer information on all pages.

**Prevent Printing PO not Digitally Signed** — If PO Digital Signature is enabled and this is `Y`, printing unsigned POs is completely prevented.

---

## SD-D — Material Requirements Defaults

*Source: [sd-d_material_requirements_defaults.htm](../../../samples/chm/extracted/sd-d_material_requirements_defaults.htm)*

**Purpose.** Controls the behavior of the Material Requirements Planning (MRP) module.

**MRP Gen POs in STDPK sizes** — Determines whether Purchase Orders generated by MR-J Generate Purchase Orders round up to the next increment of Standard Pack as defined in IN-B.

**Include in MRP Generation?** — If `Y`, new inventory items created in IN-B will have their "Include in MRP Generation?" switch set to `Y` by default, meaning they will be included in MR-F Generate Material Requirements calculations. Almost always set to `Y`. Individual items can be excluded in MR-D Enter MRP Parameters.

**Expedite Buffer (Days)** — Controls the EXPEDITE message in MRP. An EXPEDITE message is issued when enough material is on order but scheduled to arrive after it is needed. This buffer is the number of days within which an order can arrive and still be considered late (as opposed to being pegged to a later requirement).

**Expedite Sensitivity (Days)** — Reduces unnecessary EXPEDITE messages by suppressing them when the number of days late is equal to or less than this value. Useful because most MRP dates are loosely planned.

**Delay Buffer (Days)** — Controls the DELAY message in MRP. A DELAY message is issued when material on order is scheduled to arrive earlier than needed. This buffer is the number of days beyond which an early arrival receives a DELAY message.

**Delay Sensitivity (Days)** — Controls printing of DELAY messages. Set equal to the number of days an item can arrive early before it needs attention.

**Round MRP Quantities to the next whole number (Y/N)?** — If `Y`, MRP always rounds suggested order quantities to the next whole number. Useful for items (such as full sheets of material) that cannot be ordered fractionally.

**Lead time for WO Start Date** — If populated, MR-F adds this number of days to the lead time of manufactured items to determine the start date of planned work orders.

**Include Forecast in Stock Status** — If `Y`, the "Available" quantity in IN-A Inventory Inquiry reflects Forecast as entered in MR-A Enter Forecast.

**Combine items within { } Days up to ${ }** — If populated, multiple BUY requirements for the same item within the specified number of days and up to the specified dollar limit are combined to a single BUY order on the date of the first requirement.

**Use Sequence Start Date as Need Date in MR-F** — If `Y`, for BOM Components linked to routing sequences, the MR-F need date is the sequence start date rather than the Work Order start date.

---

## SD-E — Scheduling Defaults

*Source: [sd-e_scheduling_defaults.htm](../../../samples/chm/extracted/sd-e_scheduling_defaults.htm)*

**Purpose.** Configures the finite and infinite scheduling behavior used by the Scheduling module.

**Use Lead Time Scheduling (F/B/N)?** — `F`: forward Lead Time Scheduling. `B`: backward Lead Time Scheduling. `N`: use the lead time from the inventory master rather than the calculated lead time when creating work orders. See *How Lead Time Scheduling Works*.

**Calculate Lead Time Hours in SH-N** — `N` or blank: SH-N rounds each routing sequence up to the next full day when generating lead times. `Y`: each sequence calculates minutes and then the total rounds up to the next day.

**Should PO entry and receipt [PO-A, PO-C], labor entry [WO-F], and Data Collection update the actual start/finish date of sequences?** — If `Y` (used with finite scheduling), those programs ask "Is this sequence now complete?" when making entries, enabling the finite scheduling program to know which sequences are finished. Set to `N` if not using finite scheduling.

**Allow entry to overlap settings in routings?** — Applies to finite scheduling only. If `Y`, the *forward OVERLAP* field is available when entering routings. This field allows specification of extra non-production hours before the next sequence can begin (e.g., 24 hours of drying time after a painting operation).

**Display Machine prompt in Enter Labor?** — Applies to infinite or manual scheduling (set to `N` if using finite scheduling). If `Y`, during WO-F Enter Labor the default machine assigned to the routing is shown in a pop-up and can be overridden if the work was performed on a different machine. Keeps machine tracking accurate without requiring manual changes via SH-D.

---

## SD-F — Data Collection Defaults

*Source: [sd-f_data_collection_defaults.htm](../../../samples/chm/extracted/sd-f_data_collection_defaults.htm)*

**Purpose.** Configures the Data Collection module used for shop floor labor and production reporting.

**Allow dec entry # of Jobs Worked (Y/N)** — If `Y`, labor entry allows a decimal number of jobs worked to force disproportionate allocation of labor cost among multiple simultaneous jobs.

**Allow clocking in/out on multiple jobs?** — If `Y`, employees can work on two or more routing sequences simultaneously. If `N`, they must clock out of one sequence before clocking into another. Also configurable at the individual employee level in SM-G Enter Employees. Note: on each clock-in/out, all open sequences are automatically clocked out and back in so labor cost can be distributed accurately across each time segment. Parts produced are reported only to the last transaction.

**Use full screen?** — `Y`: all transactions for an employee's shift are displayed in the lower portion of the screen (WO number, sequence, start/finish time, posting status, parts produced/scrapped, run time). `N`: program prompts are confined to a two-line area in the center; no other information displayed. Full screen recommended unless monitor limitations exist.

**Enable Employee Shift Start/Stop?** — If `Y`, when an employee clocks in for the first time each morning a shift transaction is opened. At end of day, clocking out of the shift also clocks out all open work orders. Enables a single shift record for the day for payroll purposes and eliminates Indirect work orders for non-productive time. Shift data can be printed in DC-D, exported for Checkmark or payroll services, or transferred to PR-K Print/Post Time Cards.

**AutoPost Reported Labor DCA (Q,B,N) (Evo-ERP only)** — Blank or `N`: all labor and quantity complete reported in DC-A, B, and C must be posted using DC-H Post Labor Transactions. `Q`: quantity complete posts automatically on clock-out; labor time and cost still require DC-H. `B`: both labor and quantity complete post automatically.

**Rework Operation Number for DCA** — Enter the sequence number (999 recommended) for the Rework operation automatically added to the routing when parts are sent to Rework during quantity complete reporting in DC-A or DC-B. Both this and the next field must be populated for the Rework option to be available.

**Rework Work Center** — Enter the Work Center to use when automatically creating Rework Operations.

**Print Production Trans Label (Y/N/A)** — `Y`: a transfer label indicating the next operation prints when quantity complete is reported in DC-A or DC-B. `A`: prompts whether to print. Blank or `N`: no label printing.

**Print Rework Trans Label (Y/N/A)** — `Y`: a transfer label prints when rework quantity is reported. `A`: prompts. Blank or `N`: no label printing.

**Qty Complete WO Qty in DC (W/N/S)** — `W`: Work Order Start Quantity is suggested as the quantity complete in DC-A or DC-B. `S`: Sequence Start Quantity is suggested. Blank or `N`: no suggestion.

**Disable Auto-finish of seq if Qty is >= Start Qty in DC-A?** — If `Y`, reporting quantity complete in DC-A does not automatically mark the sequence as complete, so scheduling programs must calculate remaining quantity to complete.

**Enter Scrap Codes in DC-A (YNM)?** — `Y`: prompts for a scrap code when scrap is reported. `M`: allows entry of multiple codes when scrap quantity greater than one is entered.

**Rework to add back Qty to original Operation?** — If `Y`, reporting quantity complete against a Rework operation adds that quantity back to the Start Quantity of the operation they came from.

**Prompt for Run/Setup when clicking in in DC-A?** — If `Y`, users are asked for Run vs Setup time when clocking in rather than clocking out.

**Prevent Clock In if Start Qty=Completed Qty in DC-A?** — If `Y`, clocking into an operation is prevented if the operation Quantity Complete equals the operation Start Quantity.

**Check if QTY per SEQ > WO QTY (N, Y, W, Q) in DC-A?** — `Y`: quantity reported against a sequence cannot exceed the Work Order quantity. `W`: warning only. `Q`: uses the operation start quantity rather than the WO start quantity for comparison.

**Prevent Blank Machine Number in DC-A (Y/N)?** — If `Y`, users must indicate a machine when clocking in.

**Allow Setup to Enter Parts & Scrap (Y/N)?** — If `Y`, complete and scrap part quantities can be reported when reporting Setup Labor.

**Allow Backflush of Lot/Serial Comps in DC-H (L/S/B/N)?** — Controls whether Lot or Serial controlled components linked to routing sequences are backflushed when labor is posted. `L`: Lot only. `S`: Serial only. `B`: both. `N` or blank: neither.

**Use Calendar days for Jobs clocked into multi days (Y/N)?** — If `Y`, if an employee clocks out on a different date than they clocked in, the program assumes they worked all intervening time (as defined by shift hours and the Shop Calendar).

**Round Shift Start/Stop by X minutes in DC-A/DC-C** — If populated, clock-in rounds forward and clock-out rounds backward to the nearest specified minute increment of an hour. Example: a value of `10` rounds a 7:54 clock-in to 8:00 and a 3:12 clock-out to 3:10. Intermediate clock-ins (causing automatic clock-out of prior job) do not round.

**Limit Shift Rounding to Shift Start/Stop in DC-A/DC-C** — If `Y`, the rounding above applies only to shift start/stop entries, not individual job clock-ins/outs.

**Synchronize WS to Server Date & Time** — If `Y`, the workstation date/time is reset to match the server.

**Disable Scrap Quantity in DC-A** — If `Y`, DC-A cannot enter scrap quantity.

**Check if Qty per seq > WO Qty (N,Y,W,Q,P)** — When production is reported against a sequence: `Y`: cannot exceed WO Start Quantity. `W`: warn. `Q`: uses operation start qty for comparison. `P`: password required to exceed.

**DC-A Allow WO Qty Update Password** — If a password is entered, DC-A production greater than the WO Start Quantity can update the WO Start Qty when this password is entered.

**Enter Rework Codes in DC-A (YNM)** — `Y`: rework codes can be entered. `N`: cannot. `M`: allows multiple codes for rework quantity greater than one.

**DC-A To Enter Fin Prod for the last Oper [Y/N]** — If `Y`, entering a quantity complete on the last operation of a work order automatically posts Finished Production for that quantity to stock.

**Prevent Deduction Breaks from Total Shift Hours** — If `Y`, all breaks are deducted from Work Order time but only the Lunch break is deducted from total Shift hours.

**DC-A/B Prevent Reporting Qty Greater Than Previous Sequence** — If `Y`, an operation cannot report a quantity complete greater than the quantity complete reported against the prior sequence.

**DC-B Clear Employee Number after Processing** — If `Y`, the employee number is cleared after each record and must be re-entered.

**DC-A Warning for WO with Active Status E Item** — `Y`: a warning pops up when logging into a work order whose parent part has Active Status `E`. `S`: warning pops up only when clocking into Setup. `I`: warning is a bold full-screen message.

### Processing Tab

**Enter QC Codes for parts into Rework** — If `Y`, sending parts into Rework prompts for QC codes rather than prompting when Rework is complete.

**DC-A/B allow access to view and modify the WC (YN)** — If `Y`, the operator can edit the Work Center for the operation.

**DC-A/B HH-F Prompt for Sequence Complete (YN)** — If `Y`, the operator is prompted to indicate whether the sequence is complete when clocking out.

**DC-L Period Start Date** — Defines the Pay Period Start Date for use in DC-L Shift Clock In/Out to show hours-to-date for the current period.

**DC-L Period Frequency** — Defines the number of days in the pay period for use in DC-L Shift Clock In/Out.

**DC-M Include Last Clock In for all employees** — If `Y`, DC-M Employee Dashboard lists all active employees including the last clock in/out record for employees not currently clocked in.

**DCA/B Backflush Prevent Autopost Taking OH Negative** — If `Y`, when backflushing components a warning pops up if there is insufficient stock and the component will not be issued.

**DCA/B Disable NCR Entry** — If `Y`, the NCR field is not available in DC-A or DC-B.

**DCA/B Force Restart every hour** — If `Y`, the DC-A/B station forces a restart of Evo-ERP approximately every hour when the screen is not actively processing data (nobody is clocking in or out).

### Shift Tab

Accessed via the **Shift Schedule** button. Defines labor shifts so that DC-A and DC-C correctly calculate actual working time and overtime.

Employees are assigned to a shift in SM-G Enter Employees; they do not designate their own shift at the data collection terminal.

For each shift, enter the **Shift Name** and description (up to three shifts). Define a **Buffer** period (when buffer begins and when the actual shift starts) to prevent crowding at terminals at shift start/end. Define **breaks** and **lunch times** so the data collection programs automatically stop posting time for those periods. All times are entered in military time (e.g., `15:30:00` for 3:30 PM; midnight is `00:00:00`; do not exceed `23:59:59`). Define an end-of-shift buffer for clocking out; if an employee clocks out after the buffer period, all buffer time is counted as working time.

**Shift 2 & 3 Threshold Time** — If populated, when labor is posted on second or third shift prior to this time, the posting program populates an additional date field (Effective Shift Start Date) as the day prior to the actual work date, since the shift started before midnight but the employee is working after midnight.

---

## SD-G — Estimating Defaults

*Source: [sd-g_estimating_defaults.htm](../../../samples/chm/extracted/sd-g_estimating_defaults.htm)*

**Purpose.** Sets defaults for the Estimating (ES) module used to enter customer quotations.

**Use Contact Master for Estimates** — If `Y`, ES-A Enter Estimates uses the Contact Manager database rather than the customer database, eliminating the need to add a prospect to the customer database until they actually place an order.

**Default Status Code** — All quotes are assigned a status code. `A` = Active, `C` = Converted, `I` = Inactive, `X` = Canceled. Normally set to `A`.

**Default Class Code** — Optional 4-character alphanumeric classification code to categorize estimates for reporting and retrieval.

**Cust Quote Print Format Number** — Lookup to select from available customer quote print formats.

**Print Co. Name/Address on Quote?** — If `Y`, company name and address print in the upper left corner of the universal quote form.

**Print Title on Quote?** — Controls whether the title "QUOTATION" prints on the form. Suppressing allows pre-printed titles.

**Num Days to Expiration Date** — Default number of days the customer quote is valid. The estimate program adds this value to the quotation date to calculate the expiration date.

**Material Margin** — Default profit margin (not markup) for the material portion of the estimate.

**Labor Margin** — Default profit margin for the labor and setup portion.

**Outs Proc Margin** — Default profit margin for the outside processing portion.

**Overhead Margin** — Default profit margin for the overhead portion.

**Total Margin** — Default profit margin applied to all preceding costs and margins. Not applied to miscellaneous and extra costs.

**Stop Freight/Duty from pulling into Estimates** — If `Y`, freight and duty components of standard cost are not included in estimate costs.

---

## SD-H — Inventory Defaults

*Source: [sd-h_inventory_defaults.htm](../../../samples/chm/extracted/sd-h_inventory_defaults.htm)*

**Purpose.** Controls core inventory behavior, costing method, and item creation policies.

### Setup Tab

**Default Inventory Location** — The name of the default inventory location (plant or warehouse). Good practice to name it even if only one location is used.

**Average, FIFO, LIFO or Standard Costing? [A,F,L,S]** — Determines how inventory cost is calculated when inventory is increased (purchase receipt or adjustment) and what cost is used when inventory is issued or sold. `A`: weighted running average. `F`: FIFO. `L`: LIFO. `S`: Standard Cost (all transactions at Standard Cost; variances post to accounts in AD-A). Consult your accountant. Once transactions have been entered, the method can only be changed using IN-L-I Change Costing Method.

**Allow Access to Std Cost in IN-B** — If `N`, the standard cost field in IN-B is not accessible for editing.

**Multi Company Transfer Co.** — If using IN-L-R Intercompany Inventory Transfer, specify the company code to be used as the intermediate In Transit company (the designation includes the letter B plus the company code).

**Enable UPC Numbers** — If the UPC add-on is installed, enter `Y` and then enter the next available UPC number to be assigned.

**Warranty Designation by Item (Evo-ERP only)** — If `Y`, when a serialized item is saved in IN-B a prompt appears to enter the number of days for standard and extended warranty. When saving a Sales Order with serialized items, a prompt asks whether standard or extended warranty applies; the invoice posting saves the warranty expiration date to the SERIAL file.

**Enable Del/Make Obsolete in IN-L-O** — If `Y`, IN-L-O Inactive Items Utility can make items Obsolete or delete them based on specified parameters.

**IN-B Use Tools Lookup and Validation as Setup in RO-E** — If `Y`, a Tool can be assigned to an item in IN-B using validation from the list entered in RO-E Enter Tools.

**IN-K Allow edit to Transaction Date** — If `Y`, the date field in IN-K Adjust Physical Levels is editable, allowing the transaction date to be changed.

**INC/INK Allow 0 Quantity Adjustments** — If `Y`, a 0-quantity adjustment can be made to document that an item was counted and the count was correct. The Last Count Date in the item master is also updated.

**IN-A Classic view replace customer with User Defined** — If `Y`, the Customer field in the classic IN-A view is replaced by the User Defined field.

**IN-C/INK Prevent Taking Inventory Negative** — If `Y`, adjustments that would take on-hand stock negative are not allowed.

**IN-P/IN-A Use Calendar/Fiscal Year for Usage Calc (C/F)** — `C` or blank: Usage calculation uses a calendar year. `F`: uses the Fiscal Year.

### Processing Tab

**Prevent Item Creation from SO-A / SO-P-A / PO-A / WO-A / ES-A / BM-A / PI-C** — For each of these programs, if the setting is blank or `Y` (or just `Y` for PO-A, ES-A, BM-A, PI-C), the program cannot automatically chain to IN-B to create a new item number. If `N`, on-the-fly item creation is allowed.

**Use long weight in calculations (Y/N)** — `Y`: weight calculations use an expanded field (up to 999,999,999.999999). `N`: standard field (up to 9999.999999).

**Use ECO for Drawing and Revision (Y/N)** — If `Y`, the Drawing field in IN-B gives access to a list of drawings and revisions with effective dates documenting the item's change history. SO-A, PO-A, and WO-A allow entry of Revision information to track the version of an item when made, bought, and sold.

**Use ITP Numbers for Work Orders (Y/N)** — Indicates whether entry of an ITP (Inspection & Test Procedure) field is required in WO-A Enter Work Orders.

**Allow Entry of Base Price in IN-B?** — Indicates whether Base Price can be entered or edited in IN-B.

**Control Category Code (Y/N/R/A)** — Controls whether the Inventory Category field in IN-B must come from the validated list in SM-P Enter Categories. `Y`: only listed values allowed. `N`: no control. `R`: required (cannot be blank). `A`: new values can be added on the fly.

**Control User Defined (Y/N/R/A)** — Same control options for the User Defined field in IN-B, using the list from SM-Q Enter User Defined.

**Chk Item Type in Std Cost Rollup?** — If `Y`, when a part is type `A` (Make) with a BOM but then changed to type `R` (purchased), the standard cost rollup ignores the BOM components. If changed back to `A`, the rollup ignores the manually entered "This Level Material" cost.

**Use Inventory Master for Tools?** — If `Y`, entry of a new sequence in RO-A Enter Routings uses the inventory master for the tool lookup. If the selected item is not in the TOOL file, it is automatically added so usage can be tracked.

**Allow Add Lot/Serial Control with UOH? (Y/N/A)** — `N`: a part cannot be changed to require Lot or Serial control if there is on-hand inventory. `A`: a warning asks whether to proceed despite on-hand stock. Blank or `N`: no check. (Note: the help text has an inconsistency; `A` means warn and ask.)

**IN-B/SO-Q-A Disable Base Price passdown to subsidiary Co?** — If `Y`, changes to base price in a parent company do not pass down to subsidiary companies.

**IN-A Disable Rebuild Stock Status?** — If `Y`, IN-A does not recalculate stock status from order detail.

**IN-C Control Access to COGS GL Account?** — If `Y`, adjustments in IN-C can be directed to a different expense account than COGS per the item class.

**INA,BMA,SOA,POA,WOA Disp Dialog Box for Act Status N** — If `Y`, the listed programs warn when an item with Active Status `N` is entered.

**IN-B/NCR Quality Location** — If a location is specified, when Active Status of an item is changed to `P`, `Q`, or `S` in IN-B, or if an NCR is generated in QC-F-A and Segregate Inventory is selected, any on-hand stock is transferred to this location. If a Note type `QCH` is defined in SM-N-A Enter Note Types, the Notes screen opens to document why the item has been placed on Quality Hold.

**IN-B Prevent inventory transfer when status change to P/S** — If `Y`, Active Status change to `P` or `S` does not transfer stock to the Quality Location.

**INA, Include MRP Data when Viewing Forecast Data** — If `Y`, MRP requirements derived from Planned and Scheduled Work Orders are included in the Forecast quantity displayed.

**INB, QC Good Buyoff Counter to Reset to QC** — If set to a non-zero number, when an item flagged for QC receipt has that number of consecutive good receipts, the flag is reset to `N`.

---

## SD-I — Routings Defaults

*Source: [sd-i_routings_defaults.htm](../../../samples/chm/extracted/sd-i_routings_defaults.htm)*

**Purpose.** Sets defaults for the Routings (RO) module.

**Multiply or Divide by Num Processes [M,D]** — Sets the default for the Multiply/Divide prompt within the #Proc window in all three routings entry programs. See RO-A Enter Routings for a detailed explanation of how the number of processes interacts with processes/hour.

**Use Standard Time [Y,N]** — Sets the *Std Time?* default in routings entry. If `Y`, the system applies standard time to units reported through WO-F Enter Labor rather than requiring actual time entry.

**Make Seq equal Template Number [Y,N]** — If `Y` and operation templates are copied into routings, the routing sequence is assigned the same number as the template wherever possible. Useful for aligning sequence and operation numbering.

**Default Seq increment** — Default increment for sequence numbers when copying multiple operation templates into routings. Example: `10` produces sequences 10, 20, 30; `1` produces 1, 2, 3.

**Display Long Time Prompt** — If `Y`, an optional decimal time field displays in a pop-up window during routings entry. Allows entry of up to 9,999 hours with seven decimal places. Useful for very long or very short operations where standard HH:MM:SS precision is insufficient.

**Sync Template Settings to RO-A (Y/N/A)** — If `Y`, changes to time standards in operation templates automatically update master routings. If `A`, asks whether to update master routings.

**Traveler Printing to print Routing Template Notes Type** — If populated with a Note Type, WO-C Print Travelers includes notes of that type associated with Routing Templates, allowing a single master Template note to be edited once and applied to all items using that operation template.

**Primary Routing Note Type** — Enter a Note type used as the primary note type for Routings. RO-A Enter Routings defaults to this type. Configure WO-C Print Travelers to print only this type.

**ROA Enter Setup Time as Decimal** — If `Y`, Setup Time is entered as decimal hours rather than HH:MM:SS format.

**ROB Print Fixed and Variable Overhead as %** — If `Y`, overhead values print as a percentage of labor rather than as dollar-per-hour amounts.

---

## SD-J — Bill of Material Defaults

*Source: [sd-j_bill_of_material_defaults.htm](../../../samples/chm/extracted/sd-j_bill_of_material_defaults.htm)*

**Purpose.** Sets defaults for the Bills of Material (BM) module. All defaults pertain to the *Seq* field within BM-A Enter Bills of Material, which ties components to specific routing sequences.

Components tied to routing sequences serve two purposes: (1) materials can optionally print on the shop traveler within the sequence they are used; (2) backflushing of components can be tied to routing sequences as production is recorded in WO-F, allowing inventory to be backflushed as the work order progresses rather than all at once when finished goods are completed. If neither feature is used, set all these defaults to `N`.

**Require Sequence Entry - Type N (Non Inventory)?** — If `Y`, the *Seq* field is mandatory for type N items in BM-A.

**Require Sequence Entry - Type L (Labor)?** — If `Y`, the *Seq* field is mandatory for type L items.

**Require Sequence Entry - Type T (Out Process)?** — If `Y`, the *Seq* field is mandatory for type T (outside processing) items.

**Require Sequence Entry - Type R, M, F, A?** — If `Y`, the *Seq* field is mandatory for types R (purchased), M (make-from), F (finished goods), and A (subassemblies).

**Prompt for BOM Remarks when in BOM Component** — If `Y`, every component saved prompts for remark entry.

**Include BM-G in Inventory Audit Tracking** — If `N`, the Inventory Master Audit files are not updated when BM-G is run.

**Allow BOM for Type R Parts for Engineering Purposes (Y/N)** — If `Y`, type R (purchased) parts may have a BOM. When this is enabled, SD-H "Check Item Type in Standard Cost Rollup" should also be set to `Y`.

**BM-G Ignore Standard Cost Date for Parts less than $** — Enter a threshold amount that causes BM-G Print/Rollup Standard Costs to ignore the rollup cost date for components valued below this amount when determining the oldest component standard cost.

---

## SD-K — Lot and Serial Control Defaults

*Source: [sd-k_lot_and_serial_control_defaults.htm](../../../samples/chm/extracted/sd-k_lot_and_serial_control_defaults.htm)*

**Purpose.** Sets global defaults for lot and serial number printing on shipping documents.

**Print Lot Listing after Invoices/Packing Slips?** — If `Y`, any graphical format packing slip or invoice containing items with lot control includes a listing of lot numbers. For text formats, the user is asked whether to print a lot number listing; if yes, a follow-up page repeating the order header section with item numbers, quantities, and lot numbers is printed.

**Print Serial Listing after Invoices/Packing Slips?** — If `Y`, any graphical format packing slip or invoice containing serialized items includes a listing of serial numbers. For text formats, the user is asked; if yes, a follow-up page with item numbers and corresponding serial numbers is printed.

---

## SD-L — Features and Options Defaults

*Source: [sd-l_features_and_options_defaults.htm](../../../samples/chm/extracted/sd-l_features_and_options_defaults.htm)*

**Purpose.** Sets defaults for the Features and Options (product configuration) module.

**Mandatory Feature?** — If `Y`, features are mandatory by default.

**Display Duplicate Option prompt?** — If `Y`, a *Duplicate Option* prompt is displayed presenting three rules for handling duplicate options (e.g., when selecting a color, whether subsequent features with the same color should reuse that selection). If duplicate options are not a factor, set to `N`.

**Duplicate Option Code?** — Default code for handling duplicate options: `1` = Display options regardless of duplicates. `2` = Do not display; add duplicate to order. `3` = Do not display; do not add duplicate to order. See the *Features & Options* help topic for detailed explanations.

**Manufactured or Kit type?** — `M`: options are manufactured and passed to the work order system. `K`: kit types that are not passed to the work order system.

**Include in cost rollup?** — If `Y`, options are included in Print/Rollup Standard Costs. Generally set to `N` because only one out of each group of options would normally be included.

**Use std customer pricing?** — `Y`: option prices are maintained in the standard price code and contract price files. `N`: option prices are feature-specific and maintained within the options bills of material.

**Add price to parent product?** — `N`: option prices are itemized on the sales order. `Y`: option prices are added to the price of the parent product.

**Percentage pricing?** — If `Y`, option prices default to a percentage of the parent product's price.

**Display Option Code prompt?** — Planned for a future version; currently has no use. Set to `N`.

**Suppress Option Comments?** — If `Y`, the comment lines "Options selected:" and "Suboptions" that appear during SO-A order entry are suppressed to save order lines.

---

## SD-M — Sales Order Defaults

*Source: [sd-m_sales_order_defaults.htm](../../../samples/chm/extracted/sd-m_sales_order_defaults.htm)*

**Purpose.** Controls the comprehensive behavior of the Sales Orders, Invoicing, and related shipping modules.

### Setup 1 Tab

**Ready to Ship Default** — Sets the *Rdy?* flag default in the sales order header. When `Y`, items with on-hand inventory can generate instant invoices without using SO-E Release Sales Orders. Can be overridden per order.

**Entered by** — Default name/initials of the primary order entry person.

**Default Ship Via** — Default shipping method. Overridden by the Ship Via in AR-A Enter Customers.

**Default FOB** — Default FOB designation. Overridden by the FOB in AR-A Enter Customers.

**Turn the Credit Limit Message off?** — `Y`: suppresses the credit limit/hold warning during sales order entry. `N`: message is displayed when the Bill To customer is entered (credit hold) or when each line is entered (credit limit check).

**Prompt for Taxable Line Item Amt?** — `Y`: in industries like construction where tax may not apply to the full line item amount, a pop-up window displays the taxable amount and allows override. Most industries use `N`.

**Prompt for Itemized Sales Tax?** — `Y`: when a sales order is saved, asks whether to itemize sales tax. If no, the tax is included in the line item price; when posted, the sales amount is reduced by the tax amount and the tax posts to the default sales tax GL account and tax authority file.

**Prompt for Retention Billing?** — `Y`: when releasing a sales order in SO-E, asks whether to bill for retention. If yes, asks for a percentage; creates a separate retention sales order and handles all GL postings. Common in construction.

**Retention Part No** — Part number (Type N non-inventory item) used on the retention invoice when Retention Billing is enabled.

**Suppress Non-Tax Warning Message?** — `Y`: suppresses the warning that appears when no Tax Group is entered on a sales order. Useful for manufacturing companies that do not process sales taxes.

**Allow Entry to Location** — Controls whether Locations (warehouses) can be entered in SO-A. Recommended setting is `R` (required).

**Allow Entry to Department** — Controls GL Department entry in SO-A. `N`: no Department field access. `Y`: field accessible but optional. `R`: required.

**Attach Notes from ARA** — `N`: disables pulling customer notes from AR-A into sales orders. Blank or `Y`: feature enabled.

**Sales Document Printing** — `N`: disables printing of sales documents (Acknowledgement, Invoice, Packing Slip) from within SO-A. Blank or `Y`: feature enabled.

**Calc BO on Available to Ship** — If `Y`, the determination of whether an item goes to Backorder in SO-A considers Units On Hand less Units already on Sales Order and Backorder from other orders (prevents multiple orders from thinking sufficient stock exists when only enough exists for the first). Also applies to SO-S Mass Release. `W`: warning only in SO-A but still allows entry without backordering.

**Check for Existing PO in SOA** — `N`: turns off checking for duplicate customer PO numbers when entering sales orders.

**Use Ship-To code for FOB in SO-A** — If `Y`, SO-A pulls FOB information from the Ship-To customer record rather than the Bill-To customer.

**Track Changes to Sales Orders (Y/N)** — If `Y`, changes to Sales Order lines (quantity, price, discount, ship or due dates) are tracked and viewable via the HIST button in SO-A, in the Bookings Report in SA-A, or in SO-O-M Print Changes to Sales Orders.

**Prevent Editing of Desc in SO-A (Y/N)** — If `Y`, the item description in SO-A cannot be modified.

**Enable Up Charges in Discounts (Y/N)** — If `Y`, a third digit in the line item discount percentage allows entry of a minus sign for a negative discount (upcharge).

**Round Prices (U)p or (N)earest 0-4 Decimals** — If enabled, discounted prices in SO-A round either up or to the nearest number of specified decimal places.

**Prevent Deleting of Sales Order in SO-A (Y/N)** — If `Y`, the Delete SO button in SO-A is removed.

**Allow 00/00/00 Ship Dates in SO-A (Y/N)** — If `Y`, SO-A allows blank estimated ship dates. SO-N requires a date at conversion time; MRP ignores Sales Order lines with blank dates. Designed for blanket orders with unknown shipping schedules.

**Reopen Closed SO in SO-A (Y/N/P/V)** — Blank or `Y`: a closed SO is reopened when accessed. `N`: closed SOs cannot be viewed. `V`: can be viewed but not reopened. `P`: password required to reopen.

**Prevent Copying of Sales Order & Quotes (Y/N)** — If `Y`, the Copy button in SO-A and SO-P-A is not available.

**Allow entry of prices in SO-A (Y/N)** — If `N`, SO-A skips over price and discount fields, preventing order entry staff from changing prices from the standard pricing.

**Control Ship to based on Bill To** — If `Y`, once a Bill To customer is entered in SO-A, the Ship To lookup is limited to Ship-To addresses assigned to that Bill To in AR-A. If only Ship To is known, leaving Bill To blank and entering the Ship To code pulls in the Bill To information.

**Force Job Tracking in SO/PO/WO (Y/N)** — If `Y`, all SO, WO, and PO require a Job number. Blank or `N`: optional.

**Allow editing of Line Locations in SO-A (Y/N)** — `Y`: warehouse location can be edited by line in SO-A. `S`: location can be edited when shipping in SO-E. `B`: editing allowed in both programs. `N` or blank: no editing.

**Force Order Description in SO/PO (Y/N)** — If `Y`, the Order Description field cannot be left blank.

**Sales Order Default Location** — If populated, Sales Orders default to this location rather than the master Inventory Default Location.

### Setup 2 Tab

**Prompt for Specifications in SO-A?** — If `N`, item specifications are not pulled into Sales Orders.

**Ask for Book Date when editing SO-A** — If `Y`, when a change is made to a sales order, the user is prompted for the effective date of the change, which appears on the Business Status and Changes to Sales Orders reports.

**Prevent Add new cust in order entry?** — If `Y`, SO-A cannot create a new customer.

**Enable add'l SO Class Discount** — `Y`: SO-A recalculates the applicable discount per line based on value breaks in SO-Q-F Enter Discount Codes applied to the order subtotal per item class when the order is saved. `A`: asks when saving. `N` or blank: no recalculation.

**Set new SO Ent by to Username (Evo-ERP only)** — If `Y`, SO-A pulls in the first 5 characters of the entering user's username into the "Entered By" field on new sales orders.

**Exclude Cust X-Ref in SO-A** — If `Y`, the Customer Cross Reference number does not pull into Sales Orders as a comment line.

**SO-A Open or Open/Closed SO (O/B)** — `O`: the opening list in SO-A displays only Open Sales Orders. Blank or `B`: includes both open and closed orders.

**Enable Ready to Post in SO-P-I** — If `Y`, if an invoice number has already been assigned to a sales order, SO-P-I Enter Freight & Tracking # has the option to set the invoice as ready to post.

**Check for Open Invoice in SO-A greater than XXX days** — If a number is entered, SO-A pops up a warning when entering a new order for a customer with any open invoices older than that number of days.

**Default Salesperson** — Default salesperson number (must be set up in CS-A Enter Salespersons). Override is possible per order or by customer assignment in AR-A.

**Use Ship-To for Price and Discount Code** — If `Y`, Price Code and Discount Codes assigned to a Ship-To customer override those of the Bill To customer.

**Prevent Duplicate SO Lines (Y/N/W)** — `Y`: prevents entering two identical lines (same part, quantity, price, delivery date) in the same order. `W`: warns but allows. `N` or blank: no check.

**Item No for Itemized Disc (Type N)** — Part number used in Sales Orders when a Discount Code is defined as an Itemized Discount (included as a separate negative line item).

**SO-A Alt Item - Cust X-Ref (123N)** — If the item number entered in SO-A is not found in inventory, this enables a search on the Customer Cross Reference number. Enter `1`, `2`, or `3` to designate search priority order among the three alternate lookup options; `N` to exclude this lookup.

**SO-A Alt Item - User Defined (123N)** — Same, using the User Defined Field in IN-B as an alternate item number lookup.

**SO-A Alt Item - UPC (123N)** — Same, using the UPC number in IN-B as an alternate item number lookup.

**Maximum Freight Amount $9,999.99 (Y/N)** — If `Y`, freight amounts greater than $9,999.99 are not allowed, preventing costly data entry errors that cannot be undone once the invoice is posted.

**Ask for Lot info when adding SO Lines (Y/N/A/R) (Evo-ERP only)** — `Y`: Lot information can be entered in SO-A when lines are added. `N`: prevented. `A`: asked. `R`: required.

**Ask for Serial info when adding SO Lines (Y/N/A/R) (Evo-ERP only)** — Same for Serial Number information in SO-A.

**Prevent Edit of SLSP in SO-A** — If `Y`, the Sales Rep assigned to the order cannot be changed by order entry.

**SO-A Check for Open-late Inv > XXX days per terms** — If set to a number of days, SO-A warns if any open invoice is past due by more than that number of days per terms.

**Prevent Deletion of SO Lines with Work Orders in SO-A** — If `Y`, Sales Order lines that have been converted to Work Orders cannot be deleted.

**Use UCC** — If a number is entered, it becomes the incremental counter for UCC codes for shipments.

**Item Number for Medical Excise Tax** — Enter a Non-Inventory part number here to enable the calculation of Medical Excise Tax.

**Medical Excise Tax Rate** — The applicable rate (as a percentage).

**Ask for Lot info when releasing SO Lines (Y/N/A/R)** — `Y`: Lot Control information can be entered in SO-E Release Sales Orders. `N`: cannot. `A`: asked. `R`: required.

**Ask for Serial info when releasing SO Lines (Y/N/A/R)** — Same for Serial Control information in SO-E.

**SO-A Set Default to True when changing all line dates (Y/N)** — If `Y`, the default answer to "Do you want to change all lines with this date?" is `Y`.

**SOC/SOF Always use Standard Pack (Y/N)** — If `Y`, SO-C Print Packing Slips and SO-F Print Invoices show the line quantity based on Standard Pack with the invoice price multiplied out accordingly.

**Enable Auto Line Numbers in SO-A (Y/N)** — If `Y`, lines in Sales Orders are automatically numbered.

**SO-A Auto Line Number Starting Number** — Starting number for auto line numbering if different from 1.

**SO-A Auto Line Number Increment** — Increment for auto line numbering if different from 1.

### Setup III Tab

**Prevent Order if it Exceeds Credit Limit** — If `Y`, entering an order that puts a customer over their credit limit is prevented entirely rather than just displaying a warning.

**Always use Today as Ship Date in SO-E** — If `Y`, SO-E Release Sales Orders uses the local system date as Ship Date and the user cannot change it.

**SO-E/HH-D Default Shipping Bin** — If populated, SO-E and HH-D use this bin as the default for all items.

**SO-B,C,F,PB Separately email** — If `Y`, all emailed sales documents are sent as separate PDFs rather than grouped into a single PDF per customer.

**SO-A Use Standard Pack to Enter Quantity** — If `Y`, orders must be entered in an even multiple of Standard Pack. `W`: warns but allows non-standard quantities.

**Archive Sales Orders when they are marked closed** — If `Y`, the final invoice posting of an order archives the order.

**SO-A Use Shipping Lead Time to update other SO Lines** — If `Y`, the longest shipping lead time on an order controls the estimated ship date of all lines.

**SO-A/SOPC Use Shop Calendar for Ship Lead Time** — If `Y`, non-work days in the shop calendar are taken into account when calculating the Est Ship Date using the item Ship Lead Time.

**SO-A Suppress commission popup when changing reps** — If `Y`, changing a rep on an order does not pop up the message to change line commissions.

**Enable SO-A Entry Security** — If `Y`, security levels can be used to prevent users from editing another user's Sales Order.

**SO-A Display Line item Cost, Profit % by line and Total** — If `Y`, line and total profit and margin percentage are displayed during order entry based on item standard cost.

**SO-A Pull in Line User-Defined Info (Y/N/Desc)** — `Y`: the item User Defined field pulls into the order as a comment line. `Desc`: preceded by "UD:".

**SO-A/P-A Warn if Gross Profit is Below Margin (Y/N/K)** — `Y`: warns when a line is entered with a margin below the value in the next setting. `K`: uses Markup rather than Margin for the calculation.

**SO-A/SO-P-A Gross Profit Margin/Markup %** — Enter the threshold value (e.g., `25` for 25%).

**SO-P-B Prompt for Win Likelihood** — If `Y`, printing a Quote prompts for a Win Likelihood on a scale of 1-9 (1 = unlikely, 9 = likely) for use as the Quote Status in CM-C Opportunity Dashboard.

**Enable Avalara Tax System** — If `Y`, requires an Avalara account; enter Account Number, Key, and default Item Tax Code.

**SO-E Retain Original Ship Via Code** — If `Y`, changing a Ship Via Code when releasing an order applies only to the current shipment and does not change the order for subsequent shipments.

**SO-A Autonumber Lines after Inserting SO Lines** — If `Y`, inserting lines in an order renumbers subsequent lines.

**SO-E Move all unshipped lines to Backorder** — If `Y`, when a partial order is released for shipment, all remaining lines are moved to backorder.

**SO-A Prevent Access to Released Orders** — If `Y`, once an order has been released it cannot be edited without unreleasing it.

### Processing Tab

**Release Qtys > On Hand** — Three levels of control for SO-E: `0`: no restrictions on release quantities. `1`: warns if insufficient on-hand stock. `2`: prohibits releasing with insufficient stock.

**Increment WO Suffix in SO-N by** — When work orders are generated from sales orders using SO-N Convert Sales Orders to Work Orders, each SO line gets a different WO suffix. If generating multi-level work orders, using an increment other than 1 allows grouping of lower-level work orders with the same parent.

**Enter Ship Tracking Number in SO-E** — Controls whether a window pops up in SO-E for entry of a shipment tracking number and freight carrier.

**Set Pack Slip Same as Invoice** — If `Y`, when releasing sales orders in SO-E, the same number (Next Invoice Number) is assigned for both Invoice and Pack Slip. Enables reprinting a pack slip after invoice posting since it is a one-to-one relationship.

**Warn if Pack Slip has been printed (Y/N)** — If `Y`, SO-C sets a "Printed" flag on a pack slip; reprinting warns of potential duplicate shipment. Flag clears when the invoice for the shipment is posted.

**Enable Pick Tickets in SO-C (Y/N)** — If `Y`, SO-C prompts whether to print a Pick Ticket or Packing Slip. A Pick Ticket lists all order lines but does not assign or save a Pack Slip number; it is used to pull parts prior to the final packing slip.

**Track On Time Shipping (Y/N)** — If `Y`, as invoices are posted, actual vs. Estimated Ship Date and Customer Due Date data is stored in a file accessible via SO-O-N On Time Delivery Report.

**Allow SO Dates to update WO (Y/N)** — If `Y`, when a SO ship date is changed in SO-A, the user is prompted to also update the corresponding Work Order Estimated Finish Date for work orders converted from sales orders.

**Warn at ship if pmt is required SO-C / SO-E / SO-F (Y/N)** — If `Y`, when a packing slip (SO-C), release (SO-E), or invoice (SO-F) is processed for a Sales Order with a payment term requiring immediate payment (Max Days Til Due = 0), a reminder pops up.

**Allow Changing Invoice # in SO-E** — If `Y`, the invoice number to be assigned when releasing can be manually changed. Manually assigned numbers are still verified against previously used invoice numbers.

**Create 0 Qty SO Lines during post** — If `Y`, fully backordered lines post a record to the Invoice Line item file.

**Treat 99.99% discount as 100%** — If `Y`, a 99.99% Sales Order discount calculates as 100% and posts a $0 price.

**SO-A Pull in Kit Comp Prices** — If `Y`, kit components are priced individually rather than as a single price at the parent kit level.

**SO-Q-A Disable Base Price Passdown to Subsidiary (Y/N)** — If `Y`, changes to Base Price do not pass down to subsidiary companies and Base Price can be entered at the subsidiary level.

**Use Order, Current date for Pricing** — `O`: uses the Order Date to determine effective pricing. `C`: uses the current calendar date.

**SO-N Multi-Yield Part Number** — If populated, SO-N has an option to create a Multi-Yield Work Order combining all order items into a single work order for simultaneous manufacturing. WO-I processes as a Multi-Yield Work Order and completes items based on the SO Lines.

**Automatically update Surcharge prices in SO-E (Y/N/A)?** — `Y`: Sales Order items defined as "Surcharge" in IN-B have their unit cost updated to match current Base Price when released in SO-E. `A`: prompted to reprice. `N`: no changes.

**Prevent SO-N for items with Active Status E (Y/N)?** — If `Y`, prevents converting Sales Orders to Work Orders for items with Active Status `E` (Engineering).

**Enter Additional SO Info (Header/Line/Both)?** — `H`: one screen of additional information per Sales Order. `L`: one screen per line. `B`: both. The additional info screen allows up to 20 additional alpha fields and 5 dates per item.

**Disable Option to Delete Quote in SO-P-C?** — If `Y`, SO-P-C Convert Sales Quotations does not have the option to delete the quote after converting to a sales order.

**New Sales Order Consume Existing Forecasting for the month** — If `Y`, Sales Orders consume forecast in the same month as the Estimated Ship Date until the monthly forecast reaches 0.

**Posting Invoices Consumes Forecasting?** — If `Y`, Sales Invoice Posting consumes Forecast, oldest first. Mutually exclusive with the Sales Order forecast consumption setting above.

**SO-A Prevent SO Qty < Vendor Min Qty for OP Operation** — If `Y`, orders cannot be entered for a quantity less than the Vendor minimum quantity for outside process operations.

**SO-A Auto-Create type XXXXXX-XXXXXX Items** — If `Y`, entering a part number in the format `STRING-STRING` in SO-A that does not exist in inventory but whose two component strings each exist as separate parts automatically creates a new item, copying the inventory record, BOM, and Routing from the first string's item and using the second item's description as the second description line.

**SO-A Add Evo Note for Date Change** — If `Y`, when editing an existing order and changing the ship date, a prompt appears to enter a note explaining the reason.

**Enable Bill of Lading in SO-C?** — If `Y`, SO-C Print Packing Slips prompts whether to print a Bill of Lading.

**SO-E Disable Generate Serials Button** — If `Y`, SO-E Release Sales Orders does not allow auto-generation of Serial Numbers.

### Printing Tab

**Acknowledgment Print Format No.** — Lookup to select the print format for order acknowledgments.

**Packing Slip Print Format Number** — Lookup to select the print format for packing slips.

**Invoice Print Format Number** — Lookup to select the print format for invoices.

**Sales Quote Print Format Number** — Lookup to select the print format for sales quotations.

**Print Co. Name & Address on Forms?** — If `Y`, company name and address (from SD-A) prints in the upper left corner of acknowledgments, invoices, packing slips, and sales quotations.

**Print Discount Column on Forms?** — If `Y`, the Discount heading and column print on forms. If `N`, the discount column is suppressed.

**Decimalized Quantities on Forms?** — If `N`, decimal places are suppressed on all quantity fields on order documents.

**Print Title on:** — Controls whether the form title (Acknowledgment, Packing Slip, Invoice, or Sales Quotation) prints in the upper right corner of each form. Useful for distinguishing pre-printed multi-copy forms.

**Max No Lines in Body of Ack, Pack Slip, Invoices** — Number of lines in the form body before a page feed. Only used for pre-printed forms with footer information on all pages.

**Alternate Title for Invoice** — If populated, this text replaces the word "INVOICE" on printed sales invoices.

**SO-C Cert of Compliance RTM** — If populated, SO-C prints a second copy as a Certificate of Compliance using the specified RTM (report template).

**Print Ending Lines?** — If `Y`, up to 5 ending lines (defined below) can print in the lower left corner of invoices, acknowledgments, and quotations.

**Sales Order Ending Lines** — Up to 5 description lines to include at the end of sales orders/invoices.

**Sales Quote Ending Lines** — Up to 5 description lines to include at the end of sales quotations.

**Print Medical Excise Tax as a Tax Code in SO-F?** — If `Y` and the Medical Excise Tax item is defined, the tax amount prints in the Sales Tax region of the invoice rather than as a line item.

**SO-E Print SO/WO Labels after Releasing?** — If `Y`, after releasing Sales Orders a prompt appears to print labels for the order.

---

## SD-N — Sales Commission Defaults

*Source: [sd-n_sales_commission_defaults.htm](../../../samples/chm/extracted/sd-n_sales_commission_defaults.htm)*

**Purpose.** Controls how commissions are entered, tracked, and reported in the Sales Commissions (CS) module.

**Enter Commissions at Sales Order Entry?** — If `Y`, the commission percentage for salesperson 1 (and salesperson 2 if applicable) is displayed in a pop-up window during sales order header entry. The system defaults to salesperson(s) assigned to the Ship-To, then Bill To address. Commissions and percentages can be accepted or overridden. If `N`, salesperson numbers can be changed but the percentage window is not displayed; percentages come from the customer level or from CS-A Enter Salespersons.

**Enter Commissions at Line Item Entry?** — If `Y`, as each line item is entered, the default commission is shown in a pop-up for both salespersons. Line item commissions can automatically override header defaults on an exception basis if defined in CS-K Enter Price Code Commissions, CS-M Enter Contract Commissions, or if an item is excluded from commissions in IN-B. If `N`, commissions from those programs are used automatically without display.

**Enter Commissions for 2 Salespersons?** — If `N`, only one salesperson field is used. If `Y`, two salesperson fields are displayed; the second does not have to be used.

**Have CS-D print a report of Employee Commissions?** — If not using the internal payroll, the Commission Transfer can print an Employee payroll report for entry into an external payroll system.

**Enable Extended Commissions?** — If `Y`, commissions are based on information in CS-G Enter Sales Rep Links. See *Extended Commissions* for details. Requires no orders released but not yet invoiced when enabled. Orders cannot be released using SO-A when Extended Commissions is active.

**Save Zero dollar value Commissions?** — If `Y`, the Commission file is updated for $0 commissions when a rep is assigned to a customer or item so that sales reports can track sales by rep even when commissions are not paid. Requires Extended Commission System.

**Use COGS Department for GL Expense?** — If `Y`, the Department on the Item Class COGS account is also used for the GL posting of commission expense.

**Enable Overage with Extended Commissions?** — If `Y`, saving an order brings up a screen to enter an Overage amount and commission percentage for each rep assigned to the order.

**Prevent SO-A Access to Released Orders?** — If `Y`, once an order is released for shipment, editing using SO-A Enter Sales Orders is prevented.

---

## SD-O — Contact Manager Defaults

*Source: [sd-o_contact_manager_defaults.htm](../../../samples/chm/extracted/sd-o_contact_manager_defaults.htm)*

**Purpose.** Configures the Contact Manager (CM) module behavior relative to other modules.

**Contact Manager for Quotes** — If `Y`, the Contact Manager is used when entering Sales Quotes in SO-P-A Enter Sales Quotations, so prospects do not need to be added to the Customer file until an actual order is placed.

**Allow CM-A to Make Customer** — If `N`, the "Make Customer" button in CM-A Enter Contact Accounts is disabled.

---

## SD-P — Customer/AR Defaults

*Source: [sd-p_customer_ar_defaults.htm](../../../samples/chm/extracted/sd-p_customer_ar_defaults.htm)*

**Purpose.** Sets defaults for new customer records and controls Accounts Receivable behavior.

### Customer Tab

Provides default values for the following fields in AR-A Enter Customers for new customer records: **Class**, **Price Code**, **Discount Code**, **Salesperson #1**, **Terms**, and **Taxable**. A new customer record defaults to these values when saved unless overridden.

**Allow editing of Start Date in AR-A** — If `N`, the Customer Start Date cannot be edited.

**Make Territory Mandatory in AR-A** — If `Y`, customers must have a Territory assigned.

**Recycle Fee Item Number** — If populated and SM-P-E defines a Fee Quantity in MTIC.PROD.SUBST[2], SO-A adds a line to any sales order for the total Fee Quantity of all order items, using this Non-Inventory part number at Base Price.

### Accounts Receivable Tab

**Credit Card Processing Path** — Path to the X-Charge or Pi Payment Server data folder for credit card processing in AR-C and AR-N. If blank, credit card processing is disabled.

**Default Search Key in AR-A Opening List** — Controls the sort order of customers on the AR-A opening list. Use the Lookup to choose the desired index.

**Edit Credit Card Info (C/A/B/N)** — Controls which screens have full access to customer credit card information. `C`: CM-A only. `A`: AR-A only. `B`: both. `N`: neither (the last 4 digits and expiration date remain visible in any case so staff can confirm a card is on file without seeing full details). AR-T always has access regardless of this setting.

**Pop-up in AR-C for Cr. Hold** — `Y`: AR-C presents a message when payment is received from a customer on Credit Hold, prompting to remove the hold. `V`: the AR clerk is advised but cannot change the status. `N` or blank: no message.

**Pop-up in AR-C for Comm** — `Y`: AR-C can edit commission amounts when processing payments. `C`: editing limited to when credits are applied to invoices. `N` or blank: no editing. Also indicates whether editing applies to sales rep 1, 2, or both.

**Prevent Order Entry for CR Hold** — If `Y`, SO-A prevents order entry for customers on credit hold rather than just displaying a warning.

**Statement Print Format Number** — Lookup to select from three print formats for customer statements.

**Print Co. Name/Addr on Statements?** — If `Y`, company name and address print in the upper left corner of statements.

**Print Title on Statements?** — Controls whether the title "STATEMENT" prints on the form.

**Interest Rate on Overdue Accounts** — Monthly interest rate percentage charged on overdue receivables in AR-D Charge Interest on Invoices. Example: 1.5 = 1.5% per month (18% per year).

**#Days Past Due before Interest is Charged** — Number of days an invoice must be past due (per terms) before interest is charged.

**How should Statements calculate the Age of an Invoice?** — Choose either "Number of days since invoice date" or "Number of days past due per terms."

**User ID for X-Charge / Password for X-Charge** — Credentials for X-Charge credit card processing.

**User ID for PI Payment / Password for PI Payment** — Credentials for PIPay credit card processing.

**Aging Periods** — Up to five aging period thresholds used in AR-F Print Aging and AR-E Print Statements. The first aging period should always be set to 0 days to include all invoices. Defaults can be changed on the fly when printing aging reports.

**AR-C Days to Pay Calculation method** — `U`: unweighted average. `S`: skewed toward more recent payments.

**Remove Freight and Tax from Discounts** — If `Y`, AR-C Record Payments excludes tax and freight from the invoice total when calculating terms discounts.

---

## SD-Q — Master Defaults

*Source: [sd-q_master_defaults.htm](../../../samples/chm/extracted/sd-q_master_defaults.htm)*

**Purpose.** The master entry point for all System Defaults sub-programs. Only one user at a time may be in SD-Q or any of its sub-programs. Users do not need to exit the system for defaults changes to take effect; they are applied immediately. This program contains links to all module defaults screens listed in this document, as well as to AD-A General Ledger Defaults, AD-B Checking Account Defaults, and AD-C Accounts Payable Defaults.

---

## SD-R — Assign Next Numbers

*Source: [sd-r_assign_next_numbers.htm](../../../samples/chm/extracted/sd-r_assign_next_numbers.htm)*

**Purpose.** Sets the "Next" auto-increment number for numbered documents and entries across all modules (e.g., next work order number, next purchase order number, next invoice number, etc.).

**Important:** Other users must exit the system (not just this program) before these settings can be changed. As long as a user has this program open in a company, other users trying to switch to that company are blocked until this program is exited.

---

## SD-S — Warehouse Control Defaults

*Source: [sd-s_warehouse_control_defaults.htm](../../../samples/chm/extracted/sd-s_warehouse_control_defaults.htm)*

**Purpose.** Controls whether and how multi-bin Warehouse Control is used for inventory storage.

**Enable Warehouse Control (Y/N/Q)** — `Y`: enables assignment of multiple Bin Locations per item. `Q`: enables multiple bins per item and also tracks on-hand quantity by bin. The feature can also be enabled/disabled at the item level, but must be enabled here for any item to use it. When first enabled as `Y` or `Q`, the Bin Location in IN-B is set as the default Bin for each item (and for `Q`, the current on-hand quantity is assigned to that bin). Use WC-C Assign Bin Locations to Items to add or import additional bin locations.

**Use Controlled Bin Locations (Y/N)** — Once Warehouse Control is enabled: `N` (note: the help text says "N" but means "free form"): users can create new Bin Locations on the fly in PO-C and WO-I. `Y` (note: the help text says "N" means controlled): users can only assign items to pre-existing Bin Locations defined in WC-A Enter Warehouse Bin Locations. (The help source has a typo; the field is logically `Y` = controlled, `N` = free-form.)

**Allow Blank Bin Location (Y/N)** — `N`: all items coded for Warehouse Control require a named bin location. `Y`: a blank Bin Location is allowed even with Warehouse Control enabled.

**Blank Bin Name** — The system uses "NO BIN LOC" as the default name for unassigned items; this field allows renaming it.

**Delete Zero Qty Bins (Y/N)?** — If `Y`, once on-hand in a bin reaches 0, that bin assignment is deleted for the particular item. The master Bin Location entry in WC-A is still available for other items.

**Prompt for Bins for EFP Backflush (Y/N)?** — `Y`: components processed by backflushing at WO-I Enter Finished Production prompt for the specific bin when posting bin transactions. `N`: uses the default bin.

---

## SD-T — Service Repair and RMA Defaults

*Source: [sd-t_service_repair_and_rma_defaults.htm](../../../samples/chm/extracted/sd-t_service_repair_and_rma_defaults.htm)*

**Purpose.** Controls behavior of the Service/Repair (SR) and Return Merchandise Authorization (RM) modules.

**Show BOM In Release Serv/Repair** — Controls whether the Work Order BOM is visible when releasing a Service/Repair order for shipping, allowing cost calculation and identification of which components would appear itemized on the invoice.

**Service/Repair Location** — Default inventory Location for Service/Repair orders. If this Location is designated a Service Location in IN-L-B Enter/Assign Locations, stock status and inventory inquiry ignore inventory in this Location when calculating available stock.

**Add Misc. information in SR-A & E?** — If `Y`, SR-A and SR-E open an additional user-defined fields screen when saving. Field descriptions on the screen can be defined using SM-R Multi Language Maintenance.

**Allow RMA info changes in RM-C** — Indicates whether RMA receiving can also modify fields such as Reason for Return and Warranty Status.

**Control RMA Return Codes** — `Y`: reason must be on the list in RM-E Enter RMA Return Codes. `N`: any reason can be entered. `A`: any reason can be added to the list on the fly. `R`: a Reason for Return is required.

**RMA Restock Item Number** — Type N item number used for Restocking Charge on returns.

**RMA Restock Flat Charge or %** — `F`: flat charge. `P`: percentage of the return value.

**RMA Restock charge or % Amt** — Default amount or percentage to charge for restocking.

**RMA Credit Item Number** — Type N item number used for customer credit sales orders on returns of defective items.

**Enter Ship Tracking # in SR-E** — If `Y`, entry of the freight carrier tracking number is allowed in SR-E Release S/R Order.

**Generate S/R WO in SR-A (Y/N/A)** — `Y`: Work Orders are automatically generated when saving a Service/Repair order. `A`: prompts whether to generate.

**Allow Upd RMA Reasons after Disp** — If `Y`, RMA Reason for Return can be changed after the RMA disposition has been entered.

**Convert RMA to S/R Quote (Y/N/A)** — `Y`: RMA converts to a Service/Repair Quote when Repair Disposition is selected. `N`: converts to S/R Order. `A`: asks at the time of conversion.

**S/R Generate WO with Standard BOM & Routing** — `Y`: uses Standard BOM & Routing on S/R Order. `N`: uses blank. `A`: asks.

**RM-D Autopost Credit Memo (Y/N/A)** — `Y`: a credit memo is automatically posted when so dispositioned in RM-D Disposition RMA. `A`: asks whether to post.

---

## SD-U — Hand Held Defaults

*Source: [sd-u_hand_held_defaults.htm](../../../samples/chm/extracted/sd-u_hand_held_defaults.htm)*

**Purpose.** Controls the behavior of the Hand Held (HH) module programs used for scanner-based shop floor and warehouse operations.

**Use WO# as Lot # in HH-WOI** — Indicates whether the Work Order number is automatically used as the Lot Number when processing Finished Production via the hand-held interface.

**Inventory Labels in HHWOP** — Blank or `N`: never print labels from HH-D. `Y`: always chains to the label printing program. `A`: prompts whether to print labels for each work order.

**Allow Qty Entry in HH Pack/Ship** — `Y`: a quantity can be entered when releasing Sales Orders for shipment using HH-A Scan & Ship. `N` or blank: each unit is scanned individually with a quantity of 1.

**Release all Lines in HH Pack/Ship** — If `Y`, all lines (including fully backordered lines) are included on the printed invoice for orders released via HH-A Scan & Ship.

**Process Paperless in Seq/Batch** — Indicates whether labor and test reporting in HH-I Paperless Shop Floor Tracking is tracked by Work Order and Sequence only, or by smaller batches within a work order.

**Prevent Exceeding Ship Qty in Pack/Ship (Y/N/A)** — Indicates whether the Sales Order line quantity can be exceeded when packing an order: Yes/No/Ask.

**Prevent Inventory from going negative in Pack/Ship (Y/N/A)** — Indicates whether inventory can be released in excess of current on-hand quantity when packing an order: Yes/No/Ask.

**Prevent Creating new Lot in Pack/Ship (Y/N/A)** — Indicates whether a new Lot Number can be created on the fly when packing an order: Yes/No/Ask.

**Prevent Creating new Serial in Pack/Ship (Y/N/A)** — Indicates whether a new Serial Number can be created on the fly when packing an order: Yes/No/Ask.

**HHG: Allow selection of Line for Multiple Line PO (Y/N)** — If `Y`, a multi-line PO for the same part number is not treated as a blanket order; the user selects which specific line to receive rather than auto-receiving the next line.

**HHC: Allow Kit Issue Material (Y/N/A)** — `Y`: HH-C Issue Materials issues as kits. `N`: issues individual components. `A`: asks when the program starts.

**HHC: Prevent Over-Issue Password** — If a value is entered, this password is required to issue more than the BOM Quantity in HH-C Issue Materials.

**HHC: Prevent adding Non-BOM Components (Y/N/A/P)** — If a component not on the WO BOM is scanned: `Y`: it is issued. `N`: it is not. `A`: user is asked. `P`: password required.

**SO-E/HH-D Default Shipping Bin** — If populated, SO-E and HH-D use this bin as the default for all items (same setting as in SD-M).

**HHD: Close WO at HH Enter Finished Production** — If `N`, even if the master Work Order default for "Close WO at Enter Finished Production" is `Y`, using HH-D does not close the Work Order.

**HHG/POC Prevent PO Receipt prior to X days before ERD** — If populated, purchase orders cannot be received more than this number of days prior to the Estimated Receipt Date.

**HHK Transit Location and HHK Inspection Location** — If both fields are populated, HH-K Transfer Inventory defaults the "to" location to the Inspection Location when the "from" location is the Transit Location and the part being transferred has an ITP assigned. Otherwise defaults to the Default Location.

---

## SD-V — International Defaults

*Source: [sd-v_international_defaults.htm](../../../samples/chm/extracted/sd-v_international_defaults.htm)*

**Purpose.** Enables and configures international features including multi-tax forms, excise tax, multi-currency processing, and landed costs.

**Multi-Tax Forms** — `Y`: if multiple tax codes apply to a sales or purchase order, each tax code is separately itemized and printed in the bottom section of the invoice. `N`: only a single total for all taxes prints.

**Excise Tax** — If `Y`, enables excise tax processing where the tax is embedded in the item's selling or purchase price.

**Multi-Currency** — If `Y`, enables multi-currency processing. Be aware that enabling this switches the multi-currency system on and certain programs will not run until the multi-currency setup is completed. See *Multiple Currency Startup* for details. If forms should print with different currency symbols, Multi-Tax Forms must also be `Y`.

**Pay** — Controls how currency gains or losses are handled on payments (vendor payments and customer receipts). `Y`: currency gain/loss is recognized at the time of each transaction. `N`: currency adjustments are recognized at month-end (required in some countries such as Canada).

**Landed Costs** — If `Y`, enables landed cost processing.

**Auto-Tax Calc** — If `Y`, enables sales tax processing within AP-B Enter Vouchers and AR-B Enter Vouchers. Processed sales tax is posted to the GL and to the sales tax file for transfer to the appropriate tax authorities.

---

## Cross-references

SD contains one defaults screen per EvoERP module. The table below maps each SD sub-program to the module it configures.

| SD Screen | Module |
|-----------|--------|
| SD-A | Company-wide / System Manager (SM) |
| SD-B | Work Orders (WO) |
| SD-C | Purchase Orders (PO) / Accounts Payable (AP) |
| SD-D | Material Requirements / MRP (MR) |
| SD-E | Scheduling (SH) |
| SD-F | Data Collection (DC) |
| SD-G | Estimating (ES) |
| SD-H | Inventory (IN) |
| SD-I | Routings (RO) |
| SD-J | Bills of Material (BM) |
| SD-K | Lot and Serial Control (SC / IN) |
| SD-L | Features and Options (FO / SO) |
| SD-M | Sales Orders (SO) / Shipping |
| SD-N | Sales Commissions (CS) |
| SD-O | Contact Manager (CM) |
| SD-P | Customers / Accounts Receivable (AR) |
| SD-Q | Master entry point (links to all) |
| SD-R | Auto-numbers for all modules |
| SD-S | Warehouse Control (WC) |
| SD-T | Service/Repair (SR) / RMA (RM) |
| SD-U | Hand Held / Scanner (HH) |
| SD-V | International (multi-currency, multi-tax, landed costs) |

Note that the General Ledger Defaults (AD-A), Checking Account Defaults (AD-B), and Accounts Payable Defaults (AD-C) are accessible from SD-Q but are documented under the AD (Accounting Defaults) module, not the SD module. See the AD module documentation for those settings.
