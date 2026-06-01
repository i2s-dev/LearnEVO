# SM — System Maintenance

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → System Maintenance (55 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The System Maintenance (SM) module is the central setup and housekeeping hub of EvoERP. It provides programs to create and maintain master records used throughout every other module (customers, vendors, employees, item classes, tax codes, terms, ship-via codes, notes), code-table programs that define pick-list values used in other modules (categories, scrap codes, QC codes, WO priority codes, cycle codes, jobs, user-defined fields), a full suite of data-maintenance routines that archive or purge old records across all transactional modules, and several system-level utilities (shop calendar, multi-language maintenance, Evo Links, Java/JDBC settings, patch downloads, and user-preference settings).

---

## Contents

- [SM-A — Enter Customers](#sm-a--enter-customers)
- [SM-B — Enter Vendors](#sm-b--enter-vendors)
- [SM-C — Enter Item Classes](#sm-c--enter-item-classes)
- [SM-D — Enter Terms Table](#sm-d--enter-terms-table)
- [SM-E — Enter Tax Codes](#sm-e--enter-tax-codes)
- [SM-F — Enter Tax Groups](#sm-f--enter-tax-groups)
- [SM-G — Enter Employees](#sm-g--enter-employees)
- [SM-H — Enter Shop Calendar](#sm-h--enter-shop-calendar)
- [SM-I-A — Enter Lead Source Codes](#sm-i-a--enter-lead-source-codes)
- [SM-I-B — Enter Territory Codes](#sm-i-b--enter-territory-codes)
- [SM-I-D — Enter Reminder Types](#sm-i-d--enter-reminder-types)
- [SM-I-F — Enter Reasons for Loss](#sm-i-f--enter-reasons-for-loss)
- [SM-I-G — Enter Class Codes](#sm-i-g--enter-class-codes)
- [SM-I-H — Enter Key Date Codes](#sm-i-h--enter-key-date-codes)
- [SM-J-A — Work Order File Maintenance](#sm-j-a--work-order-file-maintenance)
- [SM-J-B — Archive Work Orders](#sm-j-b--archive-work-orders)
- [SM-J-C — Reconcile Inventory On-Hand](#sm-j-c--reconcile-inventory-on-hand)
- [SM-J-D — Consolidate Inventory Transactions](#sm-j-d--consolidate-inventory-transactions)
- [SM-J-E — Purge Work Orders](#sm-j-e--purge-work-orders)
- [SM-J-F — Purge Purchase Order History](#sm-j-f--purge-purchase-order-history)
- [SM-J-G — Purge QC Receipts](#sm-j-g--purge-qc-receipts)
- [SM-J-H — Purge Data Collection File](#sm-j-h--purge-data-collection-file)
- [SM-J-I — Purge Estimates](#sm-j-i--purge-estimates)
- [SM-J-J — Archive or Purge Closed Sales Orders](#sm-j-j--archive-or-purge-closed-sales-orders)
- [SM-J-K — Purge or Archive Invoice History](#sm-j-k--purge-or-archive-invoice-history)
- [SM-J-L — Change Part Numbers](#sm-j-l--change-part-numbers)
- [SM-J-M — Change Customer Codes](#sm-j-m--change-customer-codes)
- [SM-J-N — Change Vendor Codes](#sm-j-n--change-vendor-codes)
- [SM-J-O — Rebuild Customer/Vendor Credit Info](#sm-j-o--rebuild-customervendor-credit-info)
- [SM-J-P — Purge/Archive Service/RMA Orders](#sm-j-p--purgearchive-servicerma-orders)
- [SM-J-Q — BOM Recursion Utility](#sm-j-q--bom-recursion-utility)
- [SM-J-R — Archive Purchase Orders](#sm-j-r--archive-purchase-orders)
- [SM-J-S — Purge Inventory Audit Info](#sm-j-s--purge-inventory-audit-info)
- [SM-J-T — Purge or Archive Sales Quotes](#sm-j-t--purge-or-archive-sales-quotes)
- [SM-J-U — Configure Vendor Miscellaneous Info](#sm-j-u--configure-vendor-miscellaneous-info)
- [SM-J-V — Archive Inventory Transactions](#sm-j-v--archive-inventory-transactions)
- [SM-K — Evo User Settings](#sm-k--evo-user-settings)
- [SM-N-A — Enter Note Types](#sm-n-a--enter-note-types)
- [SM-N-B — Enter System Notes](#sm-n-b--enter-system-notes)
- [SM-N-C — Synchronize Classic Notes to Evo](#sm-n-c--synchronize-classic-notes-to-evo)
- [SM-N-D — Synchronize Evo Notes to Classic](#sm-n-d--synchronize-evo-notes-to-classic)
- [SM-O — Enter Ship Via Codes](#sm-o--enter-ship-via-codes)
- [SM-P-A — Enter Categories](#sm-p-a--enter-categories)
- [SM-P-B — Enter User Defined](#sm-p-b--enter-user-defined)
- [SM-P-C — Enter Scrap Codes](#sm-p-c--enter-scrap-codes)
- [SM-P-D — Enter QC Codes](#sm-p-d--enter-qc-codes)
- [SM-P-E — Define Inventory User Defined Fields](#sm-p-e--define-inventory-user-defined-fields)
- [SM-P-F — Enter Jobs](#sm-p-f--enter-jobs)
- [SM-P-G — Enter WO Priority Codes](#sm-p-g--enter-wo-priority-codes)
- [SM-P-H — Enter Cycle Codes](#sm-p-h--enter-cycle-codes)
- [SM-R — Multi Language Maintenance](#sm-r--multi-language-maintenance)
- [SM-S — Enter Evo Links](#sm-s--enter-evo-links)
- [SM-T — Enter Java Settings](#sm-t--enter-java-settings)
- [SM-U — Customer Ship Via](#sm-u--customer-ship-via)
- [SM-V — Check for Updates](#sm-v--check-for-updates)
- [Cross-references](#cross-references)

---

## SM-A — Enter Customers

*Source: [sm-a_enter_customers.htm](../../../samples/chm/extracted/sm-a_enter_customers.htm)*

**Purpose.** This program is identical to AR-A Enter Customers. It is provided as a convenience shortcut within System Maintenance so the user does not have to navigate to the Accounts Receivable module to manage customer master records.

---

## SM-B — Enter Vendors

*Source: [sm-b_enter_vendors.htm](../../../samples/chm/extracted/sm-b_enter_vendors.htm)*

**Purpose.** This program is identical to AP-A Enter Vendors. It is provided as a convenience shortcut within System Maintenance so the user does not have to navigate to the Accounts Payable module to manage vendor master records.

---

## SM-C — Enter Item Classes

*Source: [sm-c_enter_item_classes.htm](../../../samples/chm/extracted/sm-c_enter_item_classes.htm)*

**Purpose.** Item classes organize inventory into meaningful groups for reporting and General Ledger posting. Every inventory item number must be assigned to an item class. Item classes must be set up before creating inventory records.

**GL posting overview.** Nine GL account codes can optionally be assigned to each item class: Asset/Expense, Cost of Goods Sold, Taxable Sales, Non-Taxable Sales, WIP Inventory Asset, Absorbed Labor, Absorbed Fixed Overhead, Absorbed Variable Overhead, and Absorbed Material Burden. Any account left blank uses the system default from AD-A General Ledger Defaults. GL accounts are only accessible if accounting is turned on in AI-B and if "Permit use of Item Class GLs" is set to Y in AD-A.

**Uses of item classes beyond GL posting:**
- IN-F Print Inventory Value subtotals by item class.
- SO-Q-F Enter Discount Codes allows discounts defined by item class.
- IN-N-A Print Month End Inventory Costing subtotals by item class.
- SA-L, SA-M, SA-N provide sales analysis by item class.

**Field explanations:**

- **Item class** — Four-character alphanumeric code, upper case only. Identifies the item class.
- **Description** — Up to 30 characters, alphanumeric, upper and lower case. Used on reports.
- **Location** — For multi-location companies, separate GL accounts can be defined per Location within the same item class. Under Average Costing (set in SD-H), GL Asset/Exp and GL WIP accounts may differ by Location within a class. Under FIFO or LIFO, GL Asset/Exp and GL WIP must be the same for all Locations within a class because the FIFO/LIFO file is company-wide.
- **GL Asset/Exp Acct** — Asset or expense account for all items in the class. Receives cost of units received. Use an expense account (not asset) for non-inventory items such as shop supplies; those items should also be set to type `N` (Non-Inventory) in IN-B.
- **GL COGS Acct** — Cost of goods sold account. Receives COGS postings when invoices are posted and when inventory adjustments are entered in IN-C or IN-K.
- **GL Taxable Sales Acct** — Sales revenue account for taxable sales in this class.
- **GL Non-Taxable Sales** — Sales revenue account for non-taxable sales. May be the same as the taxable account if no distinction is needed.
- **GL WIP Inventory Asset** — WIP asset account for items in this class during manufacturing.
- **GL Absorbed Labor** — Absorbed labor account (normally adjacent to Direct Labor expense accounts). Credited as labor costs are posted via WO-F, DC-H, WO-N, WO-G issues, or WO-I backflushing; debited to the WIP account of the item being manufactured.
- **GL Absorbed Fixed OH** — Absorbed fixed overhead account. Works the same way as Absorbed Labor but for fixed overhead.
- **GL Absorbed Variable OH** — Absorbed variable overhead account. Works the same way as Absorbed Labor but for variable overhead.

**General program operation.** Select an existing class from the opening list or click Add to create a new one. Enter the Class code and Description. If GL posting is off or this class does not need custom GL accounts, no further steps are needed and items can be assigned to this class in IN-B.

To assign GL accounts click the **Item Class GLs** button. Enter the Class Code and, if using multiple Locations, the Location. System defaults display on the right side for reference. Enter only those accounts that differ from system defaults. Leave blank to use the system default.

- **Import GLs** — Copies GL accounts from another existing Item Class/Location.
- **Clear GLs** — Removes all GL entries for the current Class/Location.
- **Reset GLs** — Resets GL accounts to their values before any editing in the current session.
- **Copy to all Locs** — Copies this item class record to all Locations.
- **Copy all Classes** — Copies all item class records to a specified Location.

**Deletion.** To delete a class master for all locations, highlight the class and click Delete on the initial screen. To delete a Class/Location record, highlight the record on the Item Class GLs screen and click Delete. A class master cannot be deleted while items are still assigned to it; reassign those items first.

**FIFO/LIFO warning.** If FIFO or LIFO costing is configured in SD-H, the GL Asset/Exp and GL WIP accounts must be identical for all Locations within the same item class.

---

## SM-D — Enter Terms Table

*Source: [sm-d_enter_terms_table.htm](../../../samples/chm/extracted/sm-d_enter_terms_table.htm)*

**Purpose.** Defines payment terms used when creating vouchers, invoices, purchase orders, and recording payments in both Accounts Receivable and Accounts Payable.

**Field explanations:**

- **Term Num** — Sequential number identifying the terms entry. Up to 99 different terms types. The first position (Term Num 1) is the default used for NSF checks, interest charges, PR tax, and commission transfers; it should be a generic term such as NET 30. NOTE: Sales Orders, Purchase Orders, and AR/AP invoices store only the Terms Number in the database. Once order processing has begun, do not rearrange the order of items on the terms table because existing orders and invoices reference terms by number and will be affected.
- **Description** — Up to 20 characters. Prints in the Terms section on invoices, POs, etc. Also used as the reference on pop-up menus when selecting a terms type.
- **Disc Amt** — Percentage or dollar discount allowed if paid within discount days. Two-digit numeric with 2 decimal places. Enter `2.00` for 2%, not `0.02`.
- **Typ** — Type of terms:
  - `%` — discount is a percentage
  - `$` — discount is a dollar amount
  - `C` — cash terms; SO-G Post Invoices or AR-B Enter Vouchers posts directly to the default AR cash account instead of creating a receivable
  - `A` — ask for the bank account; invoicing programs prompt for a checking account at posting time
  - `P` — promotional term; due on the next occurrence of a specified calendar day (day in the Days field, month in the Max Days til Due field)
  - Cash-type terms post to both the Cash Receipts and Sales Journals and create a check register deposit entry dated the same day as the invoice. For credit card or COD payments, consider posting to a "dummy" bank account (e.g., "Credit Card pending") and using GL-K Transfer Bank Account Funds to move the funds to the operating account when bank confirmation arrives.
- **Days** — Number of discount days allowed (3-character numeric). Also used as the calendar day for a Promotional (type P) term.
- **Max Days till Due** — Maximum days before the invoice is overdue (3-character numeric). Also used as the calendar month for a Promotional (type P) term.

**General program operation.** At least one term must exist for programs requiring a terms type to work properly. Defined terms appear automatically in pop-up windows during any transaction that requires a term designation.

---

## SM-E — Enter Tax Codes

*Source: [sm-e_enter_tax_codes.htm](../../../samples/chm/extracted/sm-e_enter_tax_codes.htm)*

**Purpose.** Creates a tax code for each tax authority to which sales tax (and optionally purchase tax) is owed. Tax codes are then grouped together in SM-F Enter Tax Groups.

**Background — sales tax processing.** In the US, a single rate is usually applied, sometimes with state and local layers. In other countries, multiple taxes (federal, provincial, local, VAT, excise) may apply, sometimes hierarchically (taxes on taxes). The system allows any number of tax codes grouped into tax groups and assigned to customers and vendors.

**Background — purchase tax processing.** In the US, the vendor is responsible for collecting and remitting tax on purchases; set "Track PO taxes using tax groups?" to `N` in SD-C Purchase Orders Defaults. In other countries, purchase taxes may need the same code/group treatment as sales taxes; set the SD-C prompt to `Y`.

**Field explanations:**

- **Tax Code** — Alphanumeric code that identifies the tax authority. Used in SM-F to build tax groups.
- **Description** — Description of the tax code.
- **Tax Identification Number** — Optional governmental ID number. Prints on documents if configured in SM-F to do so.
- **Vendor Code** — A valid vendor code that the system uses to transfer the accumulated tax amount when AR-L Transfer Sales Taxes is processed.
- **Percent %** — The tax rate percentage applied to the sales/purchase order line amount.
- **GL-Account** — GL account to which taxes post. If blank, taxes post to the account defined in AD-A General Ledger Defaults.

**General program operation.** Enter the appropriate information for each tax authority. To process taxes on purchase orders, set "Track PO taxes using tax groups?" to `Y` in SD-C.

---

## SM-F — Enter Tax Groups

*Source: [sm-f_enter_tax_groups.htm](../../../samples/chm/extracted/sm-f_enter_tax_groups.htm)*

**Purpose.** Combines individual tax codes (created in SM-E) into tax groups. A tax group determines the total tax charged to a specific customer or by a specific vendor. A tax group may contain one tax code or up to nine tax codes. Customers are assigned to tax groups via AR-A Enter Customers; vendors via AP-A Enter Vendors.

**Field explanations (group header):**

- **Group** — Code identifying the tax group.
- **Description** — Description of the tax group.

**Field explanations (per tax code line within a group):**

- **Tax Code** — A tax code created in SM-E. Group codes in the order that applies for this tax group.
- **Description** — Auto-filled from the SM-E tax code description.
- **% Rate** — Auto-filled from the SM-E tax code rate.
- **I.D.** — Auto-filled from the SM-E tax identification number.
- **On** — `Y` if this tax is calculated on the preceding tax code's tax amounts (tax on tax); `N` if independent.
- **Freight** — `Y` if tax is calculated on freight charges.
- **Print** — `Y` to print the Tax Code and Identification Number to the left of the tax amount on invoices, acknowledgements, sales quotations, purchase orders, and RFQs. Requires Multi-Tax Forms to be set to `Y` in IM-A International Configuration.

---

## SM-G — Enter Employees

*Source: [sm-g_enter_employees.htm](../../../samples/chm/extracted/sm-g_enter_employees.htm)*

**Purpose.** Enters employees for labor tracking in the Work Orders module, Job Costing, and Data Collection modules. Also used for tracking PO receiving and inspection, PO approval, email addresses, and Sales Rep assignments.

**Fields:** Employee number (4-character numeric), first name, middle initial (optional), last name, street address, city, state, zip, phone, start date, regular pay rate, overtime pay rate, email address (available at the icc button when emailing forms), Division, Shift, flag for whether the employee can clock into multiple work orders simultaneously, exemption from overhead burden (for temporary employees), and an optional link to an employee photograph image file.

**Rate button.** Click Rate and enter a pay rate only when labor is to be charged to work orders using employee rates rather than work center rates.

**Saving.** When entry is complete the system asks to save the record; alternatively click the Save button at any time.

---

## SM-H — Enter Shop Calendar

*Source: [sm-h_enter_shop_calendar.htm](../../../samples/chm/extracted/sm-h_enter_shop_calendar.htm)*

**Purpose.** Defines weekends, holidays, and other non-workdays (planned shutdowns, vacations). Programs such as PO-A Enter Purchase Orders and WO-A Enter Work Orders do not allow entry of dates that fall on non-working days. The program supports marking individual days or date ranges an unlimited number of years into the future.

**Two calendars.** There is a screen calendar for marking non-working days (used by all programs except SH-E Finite Scheduling) and an internal scheduling calendar generated from the screen calendar (required by SH-E Finite Scheduling).

**Marking individual days (Screen 1):**
- Enter the date within the month displayed. Use PgUp/Next Month or PgDn/Previous Month to navigate months.
- **W/H field** — `W` to mark as weekend, `H` to mark as holiday, blank to unmark a previously marked day. Optionally enter a description.
- After marking, the calendar display shows an asterisk for weekends and `H` for holidays.
- To edit an existing date, enter the date or use F2/Lookup.

**Marking a range of days (Screen 2, accessed via Home key):**
- Enter a from/thru date range.
- Enter `M` (mark) or `U` (unmark).
- Enter a description that applies to all days in the range.
- Enter `W` (weekend) or `H` (holiday).
- Answer `Y` to mark/unmark all days in the range, or `N` to specify selected days of the week (Sunday=1, Monday=2, ..., Saturday=7). Run the process again for each additional day of the week if needed.

**Generating the scheduling calendar.** On exit, the program asks whether to generate the scheduling calendar. Required if using SH-E Finite Scheduling. Recommended: mark non-working days at least six months before today and five years into the future. Regenerate the scheduling calendar whenever the screen calendar is changed.

---

## SM-I-A — Enter Lead Source Codes

*Source: [sm-i-a_enter_lead_source_codes.htm](../../../samples/chm/extracted/sm-i-a_enter_lead_source_codes.htm)*

**Purpose.** Creates Lead Source codes and descriptions for use with CM-A Enter Contact Accounts and AR-A Enter Customers. Identifies where a prospect or customer originated (advertisement, referral, direct mail, etc.). Used as a filter on reports and mailing labels.

**Operation.** Enter a code (up to 5 characters, alphanumeric) and a 25-character description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-I-B — Enter Territory Codes

*Source: [sm-i-b_enter_territory_codes.htm](../../../samples/chm/extracted/sm-i-b_enter_territory_codes.htm)*

**Purpose.** Creates Territory codes for use with CM-A Enter Contact Accounts and AR-A Enter Customers. Assigns an account to a sales territory. Used as a filter on reports and mailing labels.

**Operation.** Enter a code (up to 4 characters, alphanumeric) and a 25-character description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-I-D — Enter Reminder Types

*Source: [sm-i-d_enter_reminder_types.htm](../../../samples/chm/extracted/sm-i-d_enter_reminder_types.htm)*

**Purpose.** Creates Account Follow-up codes (Reminder Types) for use with Reminders in CM-A Enter Contact Accounts and AR-A Enter Customers. Defines categories of follow-up activity (telephone follow-up, trade show follow-up, Accounts Receivable follow-up, etc.). Allows follow-up reports to be filtered to specific types.

**Operation.** Enter a code (up to 3 characters, alphanumeric) and a 25-character description. To include the code in the CM-C Opportunity Dashboard panel, set the **CRM Dashboard** column to `Y`. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-I-F — Enter Reasons for Loss

*Source: [sm-i-f_enter_reasons_for_loss.htm](../../../samples/chm/extracted/sm-i-f_enter_reasons_for_loss.htm)*

**Purpose.** Creates Loss Reason codes for use with SO-P-C Convert Sales Quotations when changing a Quote Status to Lost or Abandoned. Allows analysis of why quotes are not converted to orders.

**Operation.** Enter a code (up to 4 characters, alphanumeric) and a description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-I-G — Enter Class Codes

*Source: [sm-i-g_enter_class_codes.htm](../../../samples/chm/extracted/sm-i-g_enter_class_codes.htm)*

**Purpose.** Creates Class codes for use with CM-A Enter Contact Accounts. A user-defined classification code identifying various account characteristics. Used primarily as a filter for lists, reports, and mailing labels.

**Operation.** Enter a code (up to 5 characters, alphanumeric) and a 25-character description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-I-H — Enter Key Date Codes

*Source: [sm-i-h_enter_key_date_codes.htm](../../../samples/chm/extracted/sm-i-h_enter_key_date_codes.htm)*

**Purpose.** Creates Key Date codes for use with CM-A Enter Contact Accounts. A user-defined code identifying a significant type of date for an account (date of first inquiry, first sales appointment, first order, etc.). Used as a filter on reports and mailing labels.

**Operation.** Enter a code (up to 2 characters, alphanumeric) and a 25-character description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-J-A — Work Order File Maintenance

*Source: [sm-j-a_work_order_file_maintenance.htm](../../../samples/chm/extracted/sm-j-a_work_order_file_maintenance.htm)*

**Purpose.** Performs housekeeping on work order-related files, including deleting blank or duplicate records, deleting orphan records, and noting transaction records dated prior to a work order's start date. Supports a report-only mode (preview without changes) and a "for real" mode that actually applies changes.

**Operation.** On first start, a documentation file explaining exactly what SM-J-A does to each file is displayed — it can be read on screen or printed with F10. The program warns that other users should not be processing work order-related data while it runs. After confirming whether to run in report-only mode, a report is generated listing changes made and manual recommendations.

---

## SM-J-B — Archive Work Orders

*Source: [sm-j-b_archive_work_orders.htm](../../../samples/chm/extracted/sm-j-b_archive_work_orders.htm)*

**Purpose.** Removes selected Closed and/or Canceled Work Orders from the active files and transfers them to historical Work Order Archive files. Job Cost reports can be run against either active or archived files. WO-Q Work Order Inquiry can view archived orders; WO-A Enter Work Orders can copy from archived orders. Archiving is the preferred alternative to outright deletion (SM-J-E) because the history is retained.

**Operation:**
1. The program may warn that large disk space is required.
2. A warning notes that it may take a long time; running after hours is suggested.
3. Choose to archive active work orders or to restore archived work orders to the active file.
4. Enter from/thru ranges for: Work Orders, Actual Finish Dates, Job Number, Customer Code, Item Number.
5. Indicate whether to archive Closed, Canceled, or both.
6. An Archive Report lists archived work orders; an Exception Report lists any that could not be archived (likely because another user had the record open).
7. Press F10 or click Archive to begin.

**Disk space recovery.** Archiving removes records logically but disk space is not recovered until the work order files are reindexed with UT-C Re-Index File.

---

## SM-J-C — Reconcile Inventory On-Hand

*Source: [sm-j-c_reconcile_inventory_on_hand.htm](../../../samples/chm/extracted/sm-j-c_reconcile_inventory_on_hand.htm)*

**Purpose.** Reconciles all inventory-related data files so balances agree across files. Also performs housekeeping: deletes blank/duplicate records, corrects mismatching or missing records. Useful as a diagnostic tool — run before and after a suspect program to isolate errors.

**Two reconciliation levels:**

**Master Level Reconciliation** — Synchronizes the main inventory master files with each other and cleans up duplicates and mismatches. Files involved: inventory master (`BKICMSTR.B*`), manufacturing inventory master (`MTICMSTR.B*`), location master (`BKICLOCM.B*`), location detail file (`BKICLOC.B*`), item class master (`CLASMSTR.B*`), class/location file (`CLASS.B*`). Also reconciles order and allocation status against sales order line items (`BKARINVL.B*`), PO line items (`BKAPPOL.B*`), and WO BOM file (`WOBOM.B*`).

**Transaction Level Reconciliation** — Reconciles On-Hand quantities and stock status fields in the inventory master files against the inventory transaction file and open SO/PO/WO files. Stock status fields (on SO, on backorder, on PO, in QC, on WO, allocated, in WIP) are recalculated from scratch from detail files. Files involved: inventory masters (`BKICMSTR.B*`, `MTICMSTR.B*`), location detail (`BKICLOC.B*`), inventory transactions (`INVTXN.B*`), SO line items (`BKARINVL.B*`), PO line items (`BKAPPOL.B*`), WO BOM file (`WOBOM.B*`).

Two methods for transaction level:
- `A` — Force the transaction file to agree with the current On-Hand (creates an adjusting transaction entry). Appropriate after a physical inventory when On-Hand is the most trusted figure.
- `B` — Force On-Hand to agree with the net calculated from actual transactions. Appropriate when transactions are accurate but On-Hand quantities have drifted.

**Operation steps:**
1. Start with documentation display; read on screen or print with F10.
2. Select Master Level (`Y`/`N`) and Transaction Level (`Y`/`N`) reconciliation.
3. Select report-only mode (`Y` = preview, no changes; `N` = apply changes and report what was done).
4. Optionally exclude Stock Status corrections from the report for a cleaner output.
5. If Transaction Level selected, choose method A or B.
6. Optionally limit to from/thru Item Numbers and Item Classes.
7. If running for real, all users must be out of the system. Press any key to begin.

**Recommended sequence:**
1. Run Master Level in report-only mode.
2. Run Master Level for real.
3. Run Transaction Level in report-only mode.
4. Run Transaction Level for real.

**GL impact.** If On-Hand quantities change, the inventory asset account balances on the GL balance sheet are affected. Items marked with `$` on the reconciliation report have GL implications. After running for real, compare IN-F Print Inventory Value against the GL inventory asset accounts and make general journal adjustments via GL-B if needed. Consider running IN-L-S Rebuild Stock Status first to reduce stock status noise on the reconciliation report.

---

## SM-J-D — Consolidate Inventory Transactions

*Source: [sm-j-d_consolicate_invventory_transactions.htm](../../../samples/chm/extracted/sm-j-d_consolicate_invventory_transactions.htm)*

**Purpose.** Selectively purges and consolidates transactions from the inventory transaction file to reduce file size. All inventory transactions throughout the system are captured in the inventory transaction file (`INVTXN.B*`), from which usage, month-end costing, lot control, and serial control reports are derived. Lot and Serial Control items are automatically excluded from consolidation to preserve their history.

**Transaction types that can be consolidated:**

| Code | Type |
|------|------|
| `A` | Adjustments |
| `S` | Shipments |
| `P` | Purchase Receipts to Stock |
| `J` | Purchase Receipts to WIP |
| `W` | Work Order Receipts to Stock |
| `I` | Stock Issues to WIP |
| `Q` | PO Receipts to QC |
| `O` | Outside Processing Service PO Receipt to WIP |
| `C` | Price Change at AP-C |
| `M` | Make From Component Receipt |
| `T` | Location Transfer |
| `G` | Scrap |
| `B` | Bin Transfer within Warehouse |

**Operation.** Specify from/thru item number range, from/thru date range, and transaction types. Enter the date for the final consolidation transaction (the thru date of the range is suggested). Confirm with `Y` to proceed. A balance-forward record per month is created for each consolidated transaction type, rolling up net units and average cost into a single record. This preserves monthly totals needed by SM-J-C reconciliation and IN-A Inventory Inquiry monthly Usage button.

**Audit data warning.** Each inventory transaction has a date/time stamp and User login ID. Consolidation deletes this audit trail detail.

---

## SM-J-E — Purge Work Orders

*Source: [sm-j-e_purge_work_orders.htm](../../../samples/chm/extracted/sm-j-e_purge_work_orders.htm)*

**Purpose.** Permanently deletes (purges) closed and/or canceled work orders. This is a destructive operation — consider using SM-J-B Archive Work Orders instead, which removes records from the active files without deleting them permanently.

**Operation:**
1. Enter from/thru range of Work Order numbers. If the suffix is omitted, all work orders with the entered prefix are included.
2. Enter from/thru range of Finish Dates.
3. Specify whether to include Closed work orders, Canceled work orders, or both.
4. Confirm to proceed with the purge.
5. After scanning and purging, the system asks whether to print a listing of purged work orders.

---

## SM-J-F — Purge Purchase Order History

*Source: [sm-j-f_purge_purchase_order_history.htm](../../../samples/chm/extracted/sm-j-f_purge_purchase_order_history.htm)*

**Purpose.** Clears the closed purchase orders history file. Because PO history contains valuable reference information (it is the source for the Closed PO lookup in IN-A Inventory Inquiry and various PO reports), the help file advises against running this unless clearing very old, no-longer-useful records. SM-J-R Archive Purchase Orders is the preferred alternative.

**Operation.** Purge all items, or limit by vendor and date range. PO information from purged items is displayed on screen as it is being deleted.

---

## SM-J-G — Purge QC Receipts

*Source: [sm-j-f_purge_qc_receipts.htm](../../../samples/chm/extracted/sm-j-f_purge_qc_receipts.htm)*

*(Note: the source filename contains "j-f" but the topic is documented as SM-J-G in the help system.)*

**Purpose.** Clears the QC receivers file for QC receivers that are fully bought off.

**Operation.** Optionally limit the purge to a specific date range. If no range is entered, all fully bought-off QC receivers are purged.

---

## SM-J-H — Purge Data Collection File

*Source: [sm-j-h_purge_data_collection_file.htm](../../../samples/chm/extracted/sm-j-h_purge_data_collection_file.htm)*

**Purpose.** Purges records that have accumulated in the data collection file (`BKDCLAB.B*`). Records are created when DC-H Post Labor Transactions or WO-N Post Labor Batches are run. The file grows rapidly due to high labor transaction volume. Purging is optional — there is no harm in letting the file grow indefinitely except that DC-D Print Labor Status (when reporting on posted transactions) will be slower.

**Safety note.** The BKDCLAB file records have already been posted to work order files; all data except labor start/stop times exists elsewhere. The only report that uses this file is DC-D Print Labor Status (posted transactions). There is little risk in purging.

**Operation.** Enter a date through which records are to be purged. Confirm the deletion when prompted. Records are briefly displayed on screen as they are deleted.

---

## SM-J-I — Purge Estimates

*Source: [sm-j-i_purge_estimates.htm](../../../samples/chm/extracted/sm-j-i_purge_estimates.htm)*

**Purpose.** Periodically purges the estimate file of inactive or older estimates.

**Operation:**
- Enter from/thru ranges of quote numbers, customer codes, expiration dates, and classes.
- **Include Status "I" Estimates?** — `N` purges only status `X` (canceled) estimates. `Y` also includes inactive (`I`) estimates.
- **Purge Inventory, BOM, and Routing Files?** — `Y` additionally purges inventory items associated with the purged estimates that have their Active switch set to `N`.

---

## SM-J-J — Archive or Purge Closed Sales Orders

*Source: [sm-j-j_purge_closed_sales_orders.htm](../../../samples/chm/extracted/sm-j-j_purge_closed_sales_orders.htm)*

**Purpose.** Removes closed sales orders from the open sales orders file, either by permanent deletion (purge) or by moving them to an archive file. A closed sales order is one in which all items have been fully shipped and the order is marked closed. Archiving (recommended) retains orders viewable in SO-T View Sales Orders and allows copying from them in SO-A Enter Sales Orders. Running this program does not affect sales history, which is kept in separate files.

**Operation.** Select Purge, Archive, or Restore from Archive. Enter from/thru ranges of Sales Order number, date, and customer code. Processed items are displayed on screen.

---

## SM-J-K — Purge or Archive Invoice History

*Source: [sm-j-j_purge_or_archive_invoice_history.htm](../../../samples/chm/extracted/sm-j-j_purge_or_archive_invoice_history.htm)*

*(Note: the source filename contains "j-j" but this is SM-J-K per the help system.)*

**Purpose.** Clears the invoice history file by permanently deleting (purge) history or moving it to a separate archive file (recommended). The invoice history file is the source for all Sales Analysis module reports and for Shipments lookups in AR-A, SO-I Customer Service Inquiry, and IN-A Inventory Inquiry. SA-M and SA-N can optionally print from the active or archive invoice file.

**Operation.** Select Purge, Archive, or Restore from Archive. Enter from/thru ranges of invoice number, date, and customer code. Processed items are displayed on screen.

---

## SM-J-L — Change Part Numbers

*Source: [sm-j-l_change_part_numbers.htm](../../../samples/chm/extracted/sm-j-l_change_part_numbers.htm)*

**Purpose.** Changes an item number across all files in the system. Typically used during system start-up when item numbers are subject to revision, as part of an overall renumbering, or to merge history of two items that are actually the same thing. **CAUTION: This program changes history files as well as master files.**

**Manual operation.** Enter the existing item number in **Old Part No** (use F2/Lookup to browse). Enter the new item number in **New Part No**. The program warns that it may take hours depending on data file size. If you proceed, each file name displays in sequence as records are changed.

**Automated option.** For bulk changes, create a comma-delimited CSV file with columns Old Part, New Part (e.g., from Excel). Enter the filename at the top of the screen. When both parts already exist (a merge scenario), the program asks which master information to keep. The program then processes the entire file unattended.

---

## SM-J-M — Change Customer Codes

*Source: [sm-j-m_change_customer_codes.htm](../../../samples/chm/extracted/sm-j-m_change_customer_codes.htm)*

**Purpose.** Changes a customer code across all files in the system. Can also merge customer history when a customer is set up with two codes or one customer acquires another. **CAUTION: This program changes history files as well as master files.**

**Manual operation.** Enter the existing code in **Old Customer Code** (F2/Lookup available). Enter the new code in **New Customer Code**. If the new code already exists, a merge warning is displayed and you can choose which master information (address, contacts, etc.) to keep. The program warns of potentially long run time. Proceeds by displaying each file name as records are changed.

**Automated option.** For bulk changes, create a comma-delimited CSV of Old Code, New Code. Enter the filename at the top of the screen; the program processes the file unattended.

---

## SM-J-N — Change Vendor Codes

*Source: [sm-j-n_change_vendor_code.htm](../../../samples/chm/extracted/sm-j-n_change_vendor_code.htm)*

**Purpose.** Changes a vendor code across all files in the system. Can also merge vendor history when a vendor has two codes or one vendor acquires another. **CAUTION: This program changes history files as well as master files.**

**Manual operation.** Enter the existing code in **Old Vendor Code** (F2/Lookup available). Enter the new code in **New Vendor Code**. The program warns of potentially long run time. Proceeds by displaying each file name as records are changed.

**Automated option.** For bulk changes, create a comma-delimited CSV of Old Code, New Code. Enter the filename at the top of the screen; the program processes the file unattended.

---

## SM-J-O — Rebuild Customer/Vendor Credit Info

*Source: [sm-j-o_rebuild_customer_vendor_credit_info.htm](../../../samples/chm/extracted/sm-j-o_rebuild_customer_vendor_credit_info.htm)*

**Purpose.** Rebuilds the totals for Out Credits, Out Deposits, and Out Inv Amts on the AR-A Enter Customers Credit Info screen, and Outstanding Credits and Outstanding Invoices on the AP-A Enter Vendors screen. Optionally also rebuilds YTD and Last Year totals for customers and vendors.

**Operation:**
- Choose to rebuild customer totals, vendor totals, or both (`Y`/`N`).
- Enter from/thru ranges of customers and vendors (blank = all).
- Indicate whether prior year totals should also be rebuilt. Note: YTD and Last Year amounts are based on calendar year, not fiscal year.
- Enter a date range and choose a method to recalculate customer Days-to-Pay:
  - `1` — Unweighted average of all payments in the date range.
  - `2` — Average skewed toward more recent payments.
  - `3` — Weighted average based on payment amount.

---

## SM-J-P — Purge/Archive Service/RMA Orders

*Source: [sm-j-p_purge_archive_service_rma_orders.htm](../../../samples/chm/extracted/sm-j-p_purge_archive_service_rma_orders.htm)*

**Purpose.** Purges (deletes) or archives closed service and RMA orders from the open orders file. A closed order is one in which all items have been fully shipped and it has been marked closed. Running this program does not affect shipment history, which is kept in separate files.

**Operation.** Select Purge, Archive, or Restore from Archive. Enter from/thru ranges of invoice number, date, and customer code. Processed items are displayed on screen.

---

## SM-J-Q — BOM Recursion Utility

*Source: [sm-j-q_bom_recursion_utility.htm](../../../samples/chm/extracted/sm-j-q_bom_recursion_utility.htm)*

**Purpose.** Checks the BOM structure for "loops" — situations where an item is entered as a component at a lower level of its own Bill of Materials. Such loops can cause the MRP generation and Standard Cost rollup programs to run indefinitely.

**Operation.** Enter from/thru ranges of items and specify types to include. Including nested detail causes the report to show all levels and sub-levels containing the loop. If a problem is detected, the affected BOM is printed on the report. If none are found, only the report heading prints with no entries.

---

## SM-J-R — Archive Purchase Orders

*Source: [sm-j-r-archive_purchase_orders.htm](../../../samples/chm/extracted/sm-j-r-archive_purchase_orders.htm)*

**Purpose.** Removes selected Closed Purchase Orders from the receiver files and transfers them to historical Purchase Order Archive files. Purchasing History reports can be run on either active or archived files. Archiving speeds up active-file reports such as PO-I-F Print Received not Invoiced while retaining historical lookups. Preferred alternative to SM-J-F Purge Purchase Order History.

**Archive files affected:** `BKAPHPO` and `BKAPHPOL`.

**Operation:**
1. A warning about disk space requirements may appear.
2. A warning about run time is displayed; after-hours operation is suggested.
3. Choose to archive active purchase orders or to restore archived purchase orders to the active file.
4. Enter from/thru ranges of Purchase Orders, Vendor Code, and Order Date.
5. Archiving removes data from active files logically; disk space is not recovered until the files are reindexed with UT-C Re-Index File.

---

## SM-J-S — Purge Inventory Audit Info

*Source: [sm-j-s_purge_inventory_audit_i.htm](../../../samples/chm/extracted/sm-j-s_purge_inventory_audit_i.htm)*

**Purpose.** Removes records from the inventory master audit files. These files grow large over time because a record is added every time a change is made to the item master.

**Operation.** Enter a range of items (or leave blank for all). Enter a cutoff date — all records prior to that date will be deleted. Enter the type of audit information to delete (the type corresponds to which program originated the audit record).

---

## SM-J-T — Purge or Archive Sales Quotes

*Source: [sm-j-t_purge_or_archive_sales_.htm](../../../samples/chm/extracted/sm-j-t_purge_or_archive_sales_.htm)*

**Purpose.** Purges (deletes) or archives Sales Quotes from the open Quotes file. Archiving retains quotes for historical review without keeping them in the active file.

**Operation.** Select Purge, Archive, or Restore from Archive. Enter from/thru ranges of Quote number, date, and customer code. Processed items are displayed on screen.

---

## SM-J-U — Configure Vendor Miscellaneous Info

*Source: [sm-j-u_configure_vendor_miscel.htm](../../../samples/chm/extracted/sm-j-u_configure_vendor_miscel.htm)*

**Purpose.** Defines labels and default values for the user-defined fields available at the Info button in AP-A Enter Vendors.

**Available field layout on the Vendor User Defined Info screen:**
- 5 Flags (single-character indicators)
- 5 10-character Code fields
- 5 Date fields
- 5 30-character Data fields
- 5 6-digit integer number fields
- 5 2-decimal-place numeric value fields

**Operation.** Enter labels to define which fields to use and what they represent. Optionally enter default values for Flags, Codes, and Data fields. Fields with no label are not visible on the AP-A screen.

---

## SM-J-V — Archive Inventory Transactions

*Source: [sm-j-v_archive_inventory_trans.htm](../../../samples/chm/extracted/sm-j-v_archive_inventory_trans.htm)*

**Purpose.** Archives inventory transactions older than a specified date. Differs from SM-J-D Consolidate Inventory Transactions in that archiving moves detail records to an archive file (viewable later) rather than collapsing them into a balance-forward record.

**Operation.** Select a fiscal year start date 1 to 6 years past from the drop-down. All inventory transactions older than that date are moved to an archive file. A beginning-balance adjustment entry dated one day before the start date is posted to preserve the net quantity balance. Archived transactions can be viewed in IN-E Print Inventory Transactions and IN-O User Defined Inventory Transactions.

---

## SM-K — Evo User Settings

*Source: [sm-k-evo_user_settings.htm](../../../samples/chm/extracted/sm-k-evo_user_settings.htm)*

**Purpose.** This program is identical to US-A Customize Settings. It is provided as a convenience shortcut within System Maintenance for accessing per-user Evo-ERP preference settings.

---

## SM-N-A — Enter Note Types

*Source: [sm-n-a_enter_note_types.htm](../../../samples/chm/extracted/sm-n-a_enter_note_types.htm)*

**Purpose.** Creates Note Types for use in Evo-ERP Memo Notes. Controls note categories and security access.

**Standard note types (built-in):**

| Code | Description |
|------|-------------|
| `CSN` | Classic Style Note — synchronizes with DBA Classic tables |
| `CSH` | Classic Hidden Note — synchronizes with DBA Classic tables |
| `STD` | Standard Evo note (visible, non-hidden) |
| `HID` | Hidden Evo note |
| `INT` | Internal note — never prints anywhere |
| `PRD` | Paperless Produce Note — used in HH-L Multi-user Paperless Shop Floor; cannot be deleted once created |

**Configuration guidance:**
- If "Use Evo Notes" is set to `N` in SD-A Company Defaults (using T6... RTMs), choose `CSN` type for notes to print.
- If "Use Evo Notes" is set to `Y`, choose a type other than `CSN` to avoid notes printing twice.

**Custom note types.** The Note Types feature supports multiple purpose-specific note types. For example: `SHP` for shipping instructions (defaulted to print on packing slips), `PMT` for wire transfer instructions (defaulted to print on invoices).

**Operation.** Click Add and enter a code (up to 3 characters, alphanumeric), a 25-character description, and a security level. The security level is controlled per user in PS-A System Users/Passwords; users can only see notes whose security number is greater than or equal to their own user login security number. Use security level `999` for notes accessible to all users. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-N-B — Enter System Notes

*Source: [sm-n-b_enter_system_notes.htm](../../../samples/chm/extracted/sm-n-b_enter_system_notes.htm)*

**Purpose.** Enters or views Notes that are not associated with any specific item, customer, or order. These are master-level notes used system-wide.

**Operation.** Click Add, select the Note type, and type the note text. A system note can serve as a master note such as Terms and Conditions for Purchase Orders, Sales Orders, Work Orders, Sales Quotes, RFPs, RMAs, and Service/Repair orders — it prints on every instance without requiring re-entry or assignment to individual records.

---

## SM-N-C — Synchronize Classic Notes to Evo

*Source: [sm-n-c_synchronize_classic_notes_to_evo.htm](../../../samples/chm/extracted/sm-n-c_synchronize_classic_notes_to_evo.htm)*

**Purpose.** Transfers notes entered in DBA Classic to the new Evo Notes file as `CSN` (Classic Synchronized Note) or `CSH` (Classic Synchronized Hidden Note) type. Typically used when Evo Notes are enabled in DEF-A Company Defaults and the company is beginning to use the GUI version of a program that uses Notes.

**Operation.** Select the note type to convert. Available types: Customer, Vendor, Work Order, Sales Order, Purchase Order, GL Journal, Bill of Materials, Routing, Quotes, RFQ, Lot, and Serial.

---

## SM-N-D — Synchronize Evo Notes to Classic

*Source: [sm-n-d_synchronize_evo_notes_to_classic.htm](../../../samples/chm/extracted/sm-n-d_synchronize_evo_notes_to_classic.htm)*

**Purpose.** Copies Evo `CSN` and `CSH` type notes back to the DBA Classic files for Customers, Vendors, Sales Orders, and Work Orders.

**Operation.** Click Go. Notes are copied over and replace any existing Classic notes.

---

## SM-O — Enter Ship Via Codes

*Source: [sm-o-enter_ship_via_codes.htm](../../../samples/chm/extracted/sm-o-enter_ship_via_codes.htm)*

**Purpose.** Creates Ship Via codes for use in Sales and Purchase Orders.

**Fields:** Code (up to 15 characters, alphanumeric), optional company code, Name, description, and associated Vendor Code. Also supports a carrier home page URL and a specific tracking URL for shipment tracking from SO-I Customer Service Inquiry.

**Shipment tracking.** Navigate to the carrier's website and manually track a shipment to get the tracking URL format. Copy the full URL but replace the tracking number with the placeholder `%%TRACK%%`. Example URLs:
- **FedEx:** `https://www.fedex.com/fedextrack/index.html?cntry_code=us&tracknumbers=%%TRACK%%`
- **UPS:** `http://wwwapps.ups.com/WebTracking/processInputRequest?track.x=0&track.y=0&InquiryNumber1=%%TRACK%%`

Once configured, clicking Tracking Info on the SO-I shipments screen opens a browser and tracks the shipment automatically.

---

## SM-P-A — Enter Categories

*Source: [sm-p-a_enter_categories.htm](../../../samples/chm/extracted/sm-p-a_enter_categories.htm)*

**Purpose.** Creates Category codes for use with IN-B Enter Inventory. A user-defined inventory grouping code used as a filter on various reports.

**Operation.** Enter a code (up to 4 characters, alphanumeric) and a 25-character description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-P-B — Enter User Defined

*Source: [sm-p-b_enter_user_defined.htm](../../../samples/chm/extracted/sm-p-b_enter_user_defined.htm)*

**Purpose.** Creates User Defined codes for use with IN-B Enter Inventory. A user-defined code used as a filter on various reports.

**Operation.** Enter a code (up to 25 characters, alphanumeric) and a description. To edit an existing code, enter the code or press F2/Lookup.

---

## SM-P-C — Enter Scrap Codes

*Source: [sm-p-c_enter_scrap_codes.htm](../../../samples/chm/extracted/sm-p-c_enter_scrap_codes.htm)*

**Purpose.** This program is identical to RO-G Enter Scrap Codes. It is provided as a convenience shortcut within System Maintenance.

---

## SM-P-D — Enter QC Codes

*Source: [sm-p-d_enter_qc_codes.htm](../../../samples/chm/extracted/sm-p-d_enter_qc_codes.htm)*

**Purpose.** This program is identical to RO-F Enter QC Codes. It is provided as a convenience shortcut within System Maintenance.

---

## SM-P-E — Define Inventory User Defined Fields

*Source: [sm-p-e_define_inventory_user_define_fields.htm](../../../samples/chm/extracted/sm-p-e_define_inventory_user_define_fields.htm)*

**Purpose.** Defines up to 30 user-defined fields to be assigned to inventory item numbers and displayed in IN-A Inventory Inquiry and IN-B Enter Inventory (User Defined tab, GUI view only). These fields are also available for inclusion in RTM report layouts.

**Technical background.** Fields are defined by specifying a starting position and length within one of four TAS Pro substring fields: `MTIC.PROD.SUBST[2]`, `MTIC.PROD.SUBST[3]`, `MTIC.PROD.SUBST[4]`, or `MTIC.PROD.SUBST[5]`. Each field is 25 characters, giving 100 total characters across all four. A descriptive label and a screen position (1–30) are also defined.

**Screen layout.** Positions 1–30 are arranged in 3 columns of 10. Position 1 is upper-left, position 21 is upper-right, position 30 is lower-right.

**Operation.** On first load, four default fields are auto-created, each using the first 10 characters of one of the available SUBST fields. Edit these to change position, description, or field size; delete any of them; or add more up to the 30 maximum. If all 30 are deleted, the program auto-creates the same four default fields the next time it loads.

---

## SM-P-F — Enter Jobs

*Source: [sm-p-f_enter_jobs.htm](../../../samples/chm/extracted/sm-p-f_enter_jobs.htm)*

**Purpose.** Creates Job codes for use in Sales Orders (SO-A), Purchase Orders (PO-A), and Work Orders (WO-A). When on the Job Number field in those programs, a Lookup lets the user select from this table; entering a new value on the fly offers the option to add it here.

**Operation.** Click Add to add a new Job, Edit to modify, Delete to remove, or Print to list all jobs. The only required field is the Job code itself; all other fields are optional.

---

## SM-P-G — Enter WO Priority Codes

*Source: [sm-p-g_enter_wo_priority_codes.htm](../../../samples/chm/extracted/sm-p-g_enter_wo_priority_codes.htm)*

**Purpose.** Creates Priority Codes for use in Work Orders. Default values are `1`, `2`, and `3` for High, Medium, and Low priority. Supports 9 numeric and 26 alpha characters for custom priority definitions.

**Operation.** Click Add New to add, Edit to modify, or Delete to remove a priority code. A color can be assigned to each priority to differentiate them visually in SH-R Work Center Scheduler.

---

## SM-P-H — Enter Cycle Codes

*Source: [sm-p-h_enter_cycle_codes.htm](../../../samples/chm/extracted/sm-p-h_enter_cycle_codes.htm)*

**Purpose.** Creates Cycle Codes and count frequencies for inventory management. PI-A Capture Frozen Inventory can use these codes to limit items counted to those due for counting based on their last count date and the assigned frequency.

**Operation.** Click Add New to add or Edit to modify. The Cycle code field is 4 characters alphanumeric. Enter a description and a count frequency in days.

---

## SM-R — Multi Language Maintenance

*Source: [sm-r-multi_language_maintenance.htm](../../../samples/chm/extracted/sm-r-multi_language_maintenance.htm)*

**Purpose.** Defines translation tables for Evo-ERP screens. Can be used for different human languages or for redefining field labels using industry-specific terminology.

**Operation:**
1. First create a language: click **Add Language** and enter a 3-character code (e.g., `SPA` for Spanish). To check existing languages, click Edit and use the **Select a Language** drop-down.
2. Once a language exists, select a screen (DFM file) to translate: click the Browser button next to DFM Name and select the desired `.DFM` file. Example: the IN-A Classic view screen is `T7INAC.DFM`. Click **Generate** to populate the translation table.
3. Click Edit and select the language. A table showing the original field descriptions and an empty column for translated values appears. Any untranslated field continues to display its original text.

---

## SM-S — Enter Evo Links

*Source: [sm-s_enter_evo_links.htm](../../../samples/chm/extracted/sm-s_enter_evo_links.htm)*

**Purpose.** Creates master links to external files tied to record types such as SO, PO, or Quotes. These links let external documents (drawings, PDFs, images, etc.) be associated with and printed or viewed alongside EvoERP documents.

**Operation:**
- If previously using Inventory Links and switching to Evo Links, click the rightmost toolbar button (conversion arrow icon) to convert existing Inventory Links to Evo Links. If the rightmost button shows eyeglasses, the conversion has already been done.
- Choose the type of link to create and click Add.
- Enter the file path and choose print and association settings:
  - **Print settings** — control which form the link prints on, whether it appears as a thumbnail or as a link, and (for inventory items) whether the link is active when the item is a parent, a component, or either in the document.
  - Most files open using standard Windows file associations, so no additional association setup is usually needed.

---

## SM-T — Enter Java Settings

*Source: [sm-t_enter_java_settings.htm](../../../samples/chm/extracted/sm-t_enter_java_settings.htm)*

**Purpose.** Configures company-level JDBC connection settings for Evo programs written in Java, including SH-R Work Center Scheduler, BM-N BOM Availability Tree, and GL-R Business Status.

**Fields:**

- **Host** — IP address or server name where Evo is installed.
- **Port** — Default `1583` (Pervasive Relational Engine port); change if redirected.
- **Name** — Name of the Pervasive database created in the Pervasive Control Center on the server, pointing to the company subfolder.
- **Destination** — Folder where Java-generated reports are sent.

**Operation.** Save the settings then click **Test Settings**. If successful, the first 10 items in inventory are displayed. If unsuccessful, an error report is available; the report can be emailed to support@istechsupport.com with company contact information for assistance.

---

## SM-U — Customer Ship Via

*Source: [sm-u_enter_customer_ship_via.htm](../../../samples/chm/extracted/sm-u_enter_customer_ship_via.htm)*

**Purpose.** Stores shipping carrier account information for customers to support third-party freight billing. Allows the customer's billing account numbers to be on file.

**Operation.** Enter the Customer Code and Ship To Code (the Ship To code must already exist in SM-O Enter Ship Via Codes). Enter a priority to set precedence if multiple shipping accounts exist for the same customer. Enter the Billing Account Number, optional Notes, Active/Inactive status flag, and whether insurance is required when using this carrier.

---

## SM-V — Check for Updates

*Source: [sm-v_check_for_updates.htm](../../../samples/chm/extracted/sm-v_check_for_updates.htm)*

**Purpose.** Connects to the internet and downloads available patches for the current version. If a newer numbered version exists, a message indicates that a full update is available.

**Operation.** On load, the program connects to the ISTech website, compares local files to available files, and displays differences. By default, file dates are ignored and all differences are shown. If a pre-release copy of a file has been provided (e.g., for a customization), disable "Ignore File Dates" to prevent a newer local file from being overwritten by an older website version. Click **What's New** to view a list of file changes.

---

## Cross-references

**Master record entry (must be set up early in system configuration):**
- SM-A (= AR-A) and SM-B (= AP-A) create customer and vendor master records used throughout AR, AP, SO, PO, and SA.
- SM-G creates employee records used in WO (labor entry), DC (data collection), PO (receiving/inspection/approval), and commission/sales rep tracking.
- SM-C item classes are required on every IN item record; they drive GL posting for IN, PO, WO, and SO.
- SM-D terms table is required in AR, AP, SO, and PO.
- SM-E/SM-F tax codes and tax groups are assigned to customers (AR-A) and vendors (AP-A) and govern tax calculations in SO and PO.
- SM-H shop calendar gates date entry in PO-A, WO-A, and drives SH-E Finite Scheduling.

**CRM/sales code tables (SM-I-*):**
- SM-I-A Lead Source, SM-I-B Territory, SM-I-D Reminder Types, SM-I-G Class Codes, SM-I-H Key Date Codes all feed CM-A Enter Contact Accounts and AR-A Enter Customers.
- SM-I-F Loss Reasons feed SO-P-C Convert Sales Quotations.

**Archive and purge routines (SM-J-*):**
- SM-J-A housekeeping and SM-J-B archive/SM-J-E purge manage WO data; both interact with WO module files.
- SM-J-C inventory reconciliation is a critical diagnostic for IN module integrity; has GL implications reported via IN-F.
- SM-J-D consolidates the INVTXN file used by IN-A, IN-E, and IN-N-A.
- SM-J-F purges / SM-J-R archives PO history; affects IN-A Closed PO lookup and PO reports.
- SM-J-G purges QC receivers; affects QC module.
- SM-J-H purges BKDCLAB; affects DC-D Print Labor Status.
- SM-J-I purges estimates; interacts with the SO quotation module.
- SM-J-J archives/purges closed SO; does not affect SA history. SM-J-K archives/purges invoice history (SA source).
- SM-J-L/M/N change part numbers, customer codes, vendor codes across all modules (IN, SO, PO, WO, AR, AP, SA, DC, QC).
- SM-J-O rebuilds AR/AP credit totals.
- SM-J-P archives/purges Service/RMA orders.
- SM-J-Q BOM recursion check affects MRP and standard cost rollup (MR module).
- SM-J-S purges inventory audit history from the item master audit files (IN).
- SM-J-T archives/purges sales quotes (SO quotation module).
- SM-J-U configures AP-A vendor user-defined info fields.
- SM-J-V archives INVTXN transactions; archived records viewable in IN-E and IN-O.

**Notes (SM-N-*):**
- SM-N-A note types apply to all modules that support Evo Notes (AR, AP, SO, PO, WO, GL, IN, BM, and more).
- SM-N-B system notes serve as boilerplate text printed on any document type.
- SM-N-C/D handle migration between Classic and Evo note storage systems.

**Code tables (SM-P-*, SM-O):**
- SM-P-A Categories and SM-P-B User Defined codes are assigned to IN items.
- SM-P-C Scrap Codes (= RO-G) and SM-P-D QC Codes (= RO-F) are used in the RO (Routing) and WO (Work Orders) modules.
- SM-P-E inventory user-defined fields extend IN-A and IN-B screens.
- SM-P-F Jobs link SO, PO, and WO orders to job numbers for job costing.
- SM-P-G WO Priority Codes are used in WO-A and displayed in SH-R Work Center Scheduler.
- SM-P-H Cycle Codes feed PI-A Capture Frozen Inventory (physical inventory).
- SM-O Ship Via Codes are used in SO and PO; SM-U adds customer-specific carrier billing accounts.

**System configuration utilities:**
- SM-R Multi Language Maintenance supports translation of `.DFM` screen files.
- SM-S Evo Links manages external file associations for all document types.
- SM-T Java Settings is required before SH-R Work Center Scheduler, BM-N BOM Availability Tree, or GL-R Business Status can connect to the Pervasive database.
- SM-K (= US-A) manages per-user display/behavior preferences.
- SM-V Check for Updates downloads patches from the ISTech website.
