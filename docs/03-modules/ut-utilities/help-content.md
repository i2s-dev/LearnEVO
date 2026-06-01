# UT — Utilities

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → Utilities (12 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Utilities module (UT) groups a set of low-level, administrative programs that operate directly on the EvoERP data files and system configuration. Most of these tools bypass the normal transaction workflow and write directly to the underlying Btrieve (.B) data files. Several of them are genuinely destructive if misused — the UT-K sub-menu in particular contains programs that clear data, globally replace field values, and recalculate derived totals. All UT-K programs carry a mandatory "make a backup first / get everyone off the system" requirement. The non-K programs (UT-A, UT-C, UT-D, UT-H, UT-I) are system-configuration tools intended primarily for initial setup or support-assisted maintenance.

---

## Contents

- [UT-A — Run a TAS Program](#ut-a--run-a-tas-program)
- [UT-C — Re-Index File](#ut-c--re-index-file)
- [UT-D — Edit Data Location File](#ut-d--edit-data-location-file)
- [UT-H — Print File Layouts](#ut-h--print-file-layouts)
- [UT-I — Create/Delete Company](#ut-i--createdelete-company)
- [UT-K-A — Clear Data](#ut-k-a--clear-data)
- [UT-K-B — Global Field Replace](#ut-k-b--global-field-replace)
- [UT-K-D — Recalc GL Chart of Accounts](#ut-k-d--recalc-gl-chart-of-accounts)
- [UT-K-E — Consolidate Inventory Locations](#ut-k-e--consolidate-inventory-locations)
- [UT-K-F — Set Avg and Last Cost to Std Cost](#ut-k-f--set-avg-and-last-cost-to-std-cost)
- [UT-K-G — Recalc Inventory Book Value](#ut-k-g--recalc-inventory-book-value)
- [UT-K-I — Fix Binary Zeroes](#ut-k-i--fix-binary-zeroes)
- [Cross-references](#cross-references)

---

## UT-A — Run a TAS Program

*Source: [ut-a_run_a_tas_program.htm](../../../samples/chm/extracted/ut-a_run_a_tas_program.htm)*

**Purpose.** This option allows you to run Evo-ERP programs that are not included on the standard menus and would normally not be run without assistance from technical support.

**Operation.** Enter the name of the program with or without the file extension. Evo-ERP programs may have a `.RWN` or `.RUN` extension. After entering the program name, press `<Enter>` to launch it.

**Use case.** Support-assisted execution of off-menu programs — diagnostic tools, one-time conversion utilities, or custom programs deployed outside the standard menu tree.

---

## UT-C — Re-Index File

*Source: [ut-c_reindex_file.htm](../../../samples/chm/extracted/ut-c_reindex_file.htm)*

**Purpose.** Rebuild the key structure (index) of a Btrieve data file when it has become corrupted.

**When to use.** Re-indexing is the appropriate response to:

- A data file whose key structure is corrupted due to static discharge, power failure, or physical disk damage.
- An entry program returning wrong descriptions for a given item number, or appearing to lose data.
- A **BTrieve Status 2 Error** (key/index error) on a specific file.

**Operation.** Enter the file name for the file to be re-indexed. For a listing of file names, see the File Names reference in the help system.

**Warnings (both stated as ALL-CAPS in source):**

- **DO NOT REINDEX A FILE WHILE OTHER USERS ARE ON THE SYSTEM.** If the re-index process is interrupted, the file will not be recoverable.
- **MAKE A BACKUP OF ANY FILE BEFORE REINDEXING** so it can be restored if necessary.

---

## UT-D — Edit Data Location File

*Source: [ut-d_edit_data_location_file.htm](../../../samples/chm/extracted/ut-d_edit_data_location_file.htm)*

**Purpose.** Change or add location (path) information for each data file in EvoERP's data dictionary. Used to tell the system the subdirectory containing a given company's files, or to register a new custom file.

**Background — how EvoERP organizes data files:**

- The default company's data files live in a folder named `DEFAULT`, one level below the main `EVOERP` folder; they carry the extension `.B`.
- Each additional company keeps its files in a separate subfolder one level below `EVOERP`. Those files carry an extension of `B` followed by the company code — e.g., company 99 uses `.B99`.
- Data dictionary schema files (all files beginning with `FILE*.*`) are shared across all companies and reside in the main `EVOERP` folder.

**Fields:**

- **File Name** — the name of the data file being registered or updated.
- **Extension** — the company extension, always starting with `B` then the company number (blank for the default company).
- **Layout** — if the file is a schema file (shares another file's layout), enter the name of the primary file it is based on. For non-schema files, **File Name** and **Layout** are identical. When maintaining an existing file, **Layout** auto-fills after **File Name** is entered.
- **Type** — defaults to `T`, indicating a TAS file.
- **Location** — the path where the files are located, relative to the EVOERP folder. Example: `COMPANY2\` means the file is in a folder named `COMPANY2` one level down from the EVOERP directory. No drive letter prefix is required.
- **Description** — human-readable description of the file; can be modified.

**Changing all file locations at once.** Click the **Chg All Locations** button (or press `<Home>`) to enter:

- **New Location** — the path to assign to all files.
- **Comp Code** — the company code (always starts with `B` then the company number).

The program then reassigns all file locations as specified.

**NOTE:** Do not use this program without help from Technical Support. It is generally only used during initial system setup or when adding new custom programs.

---

## UT-H — Print File Layouts

*Source: [ut-h_print_file_layouts.htm](../../../samples/chm/extracted/ut-h_print_file_layouts.htm)*

**Purpose.** Print a listing of field specifications (field names, types, sizes) within one or more EvoERP data files. Used primarily in conjunction with third-party report writers and with DE-A SQL Query Export, where knowing a file's exact field structure is necessary.

**Operation.** Enter a from/thru range of file names. The report lists field specifications for all files within that range. For a listing of file names organized by module, see the File Names reference in the help system.

---

## UT-I — Create/Delete Company

*Source: [ut-i_create_delete_company.htm](../../../samples/chm/extracted/ut-i_create_delete_company.htm)*

**Purpose.** Create additional companies or delete an existing company. The program can copy all files from a source company to the new target company, or create a complete set of empty initialized data files.

**Important notes before using:**

- If using both Evo-ERP and DBA Classic, always use Evo-ERP to create and delete companies so that both sets of data dictionaries are updated.
- If only one company is needed, no action is required — the system ships with empty data files for the default company already installed. Use UT-K-A Clear Data to initialize (clear) any data files in the default company instead.

### Creating a New Company

1. Enter `C` in the first field to indicate Create.
2. **Company Code** — a two-character alphanumeric code for the new company (e.g., `2`, `88`).
3. **Copy from another company?** — enter `Y` to copy data from an existing company. Useful when the new company will share the same GL chart of accounts; you can copy the files and then use UT-K-A Clear Data to remove transaction detail while keeping master files.
4. **Copy from** — if copying, enter the one or two character company code of the source company.
5. **Company Name** — the name that will appear in the Change Company selection window on master menus, in SD-A Company Defaults, and on printed forms such as invoices.
6. **Path** — the subdirectory path for the new company's files, relative to the EVOERP folder. The program auto-inserts a path using the company code as the subfolder name (e.g., `88\` for company code 88). The name can be changed. No drive letter is required.
7. Press `<Enter>` to begin processing.

### Processing (Create)

- The program creates the subdirectory specified.
- If copying from another company, it copies all files from the source to the target, appending the new company code as file extensions.
- If not copying, it creates a full set of initialized (empty) data files with no default settings.
- In all cases, the program finishes by inserting the new company name in SD-A Company Defaults so it appears on master menus and reports.

### Deleting a Company

1. Enter `D` in the first field to indicate Delete.
2. **Company Code** — enter the code of the company to delete.
3. A warning is displayed that data files will be erased; confirm to proceed.
4. All files in the company's subdirectory are erased and all data file locations for the company are removed from the data dictionary location file.

### Special Processing (F-key options)

- **F3** before processing — update the data dictionary only, without actually creating or deleting the data files. Allows adding or removing company entries from the data dictionary independently.
- **F4** before processing — create missing data files only, without adding a company entry to the data dictionary.

---

## UT-K-A — Clear Data

*Source: [ut-k-a_clear_data.htm](../../../samples/chm/extracted/ut-k-a_clear_data.htm)*

**Purpose.** Selectively clear various sets of data files — either transaction data only (leaving master file data intact) or all data entirely. Typically used during system startup or when setting up a second company.

**Typical use cases:**

1. Single company, installing into the default company: clear out any pre-existing GL accounts or test data entered before implementation, starting with completely clean files.
2. Multi-company, sharing master data: copy the default company to a second company using UT-I, then use Clear Data in the second company to remove transaction detail while keeping shared master files (e.g., GL chart of accounts), eliminating double-entry.

**Operation.** An entry screen presents six data categories (file groupings). For each category, enter one of three codes:

| Code | Action |
|------|--------|
| `C` | Keep master file data; clear all transaction detail (GL entries, aging detail, sales history, open orders, etc.) |
| `D` | Delete all data completely (both master and transaction) |
| `N` | Leave this data category untouched |

**Data categories available:**

- General Ledger Chart of Accounts
- Accounts Receivable Customers
- Accounts Payable Vendors
- Inventory Items
- Payroll Employees
- Manufacturing Systems

**Note:** The Clear Data program can take considerable time to run depending on the sizes of the files being cleared.

---

## UT-K-B — Global Field Replace

*Source: [ut-k-b_global_field_replace.htm](../../../samples/chm/extracted/ut-k-b_global_field_replace.htm)*

**Purpose.** Globally change the value of a field across all records in a file, adjust a numeric field by a flat amount or percentage, or delete entire records — all filtered by up to 6 conditions on fields within the same file.

**Prerequisites (stated explicitly in source):**

- **MAKE A BACKUP FIRST.** This program affects many data records; a backup allows restoration if results are unexpected.
- **GET EVERYONE OFF THE SYSTEM** before running.

**Operation:**

1. **File Name** — enter the file to operate on, or click **Display Files** (or press `F2`) to select from a lookup. See the File Names reference for a listing of file names and descriptions.

2. **Action** — choose one of three actions:
   - `Replace` — update a field to a new value.
   - `Adjust` — increment a numeric field by a flat amount or percentage.
   - `Delete` — delete the entire record (not just clear a field value).

3. **Field name** — if Replace or Adjust is chosen, a lookup window automatically displays all available fields in the file. Select the field to change.

4. **Array element number** — if the selected field is an array (indicated by a number in brackets to the right of the field name in the lookup), enter the element number to change. Example: in the Item master file (`MTICMSTR`), the standard cost field `MTIC.PROD.RCOST` is an array of 15 elements representing the various components of standard cost.

5. **For REPLACE action:** Enter the new value in the **Replace with value** field.

6. **For ADJUST action:** Enter the adjustment value.

7. **Filters** — enter up to 6 filters controlling which records are affected. Each filter specifies a field, an operator, and a comparison value. Available operators: `=`, `<`, `<=`, `>`, `>=`, `All`, and `$` (contains substring). When entering fewer than 6 filters, fully complete the last filter and position the cursor on the next blank line before pressing `F10`.

8. Press `F10` to begin processing. On completion, the number of records affected is reported.

---

## UT-K-D — Recalc GL Chart of Accounts

*Source: [ut-k-d_recalc_gl_chart_of_accounts.htm](../../../samples/chm/extracted/ut-k-d_recalc_gl_chart_of_accounts.htm)*

**Purpose.** Rebuild from scratch the "bucketed" (summarized) amounts in the GL Chart of Accounts files (`BKGLCOA` and `ISGLCOA`) from the raw entries in the GL Transactions file (`BKGLTRAN`). The bucketed amounts are the period/year totals visible in GL-A View Chart of Accounts.

**When to use.** Normally only run if `BKGLCOA` becomes corrupted or is incompletely posted due to a power failure or other interruption.

**Prerequisites:**

- **MAKE A BACKUP OF `BKGLCOA` AND `BKGLTRAN` FIRST.**
- Ensure no other user is posting transactions in GL-O.

**Operation:**

1. Confirm that you want to proceed.
2. **Orphan transaction report** — optionally print a report of orphan transactions (transactions whose associated Chart of Accounts entry no longer exists).
3. **Suspense account** — enter the GL account to which orphan transactions will be moved.
4. **Fiscal year start dates** — verify the start dates for the current fiscal year and the prior 6 years. The program needs these dates to correctly calculate beginning balances for each year.
5. **From/Thru GL account range** — enter a range of GL accounts to rebuild, or press `<Enter>` through both fields to include all GL accounts.
6. Confirm the suspense account; processing begins.

**Orphan transactions.** When the program encounters a transaction with no matching Chart of Accounts entry, it examines the transactions for that account:

- If any `YE` (year-end) journal type transactions exist, the account is presumed to have been an income or expense account. Transactions are moved to the same account number but with department `EXP` (an expense account), so that Retained Earnings recalculation will include their effect.
- Otherwise, the account is presumed to have been a balance sheet account, and transactions are moved to the specified suspense account.

---

## UT-K-E — Consolidate Inventory Locations

*Source: [ut-k-e_consolidate_inventory_locations.htm](../../../samples/chm/extracted/ut-k-e_consolidate_inventory_locations.htm)*

**Purpose.** Eliminate unwanted warehouse Locations and combine all inventory records assigned to those unwanted Locations into a single, specified Location.

**Prerequisites:**

- **MAKE A COMPLETE BACKUP FIRST.**
- **GET EVERYONE OFF THE SYSTEM** before running.

**Operation:**

1. A list of existing Locations is presented. Select the Location(s) to keep. Note: a blank Location will not be allowed — all warehouse Locations must be named (due to binary zero problems that arise from blank Locations).
2. Click **Go** once desired Locations are selected.
3. **Special case — only existing Location is blank:** the selection screen is skipped because the blank Location must be replaced. The name `DEFAULT` is suggested for the new Location but can be changed.
4. **Location** — enter the name of the main Location that will replace all deleted Locations.
5. **GL Account** — specify the existing GL Account to use for posting for the specified Location if it does not already exist.

**Post-processing step.** If a new Default Location was created, go to IN-L-B Enter/Assign Locations and enter a name and address for the new location so that the information pulls into the Ship To field for that Location on Purchase Orders.

---

## UT-K-F — Set Avg and Last Cost to Std Cost

*Source: [ut-k-f_set_avg_and_last_cost_to_std_cost.htm](../../../samples/chm/extracted/ut-k-f_set_avg_and_last_cost_to_std_cost.htm)*

**Purpose.** Replace the **Average Cost** and **Last Cost** fields on a range of inventory items with the item's **Standard Cost** value.

**When to use.** This program is used when Average Cost and Last Cost values are meaningless or inaccurate. This can occur:

- During system startup when transactions are made before costs have been established or accumulated through product structures.
- When poor manufacturing controls (negative on-hand quantities, incomplete work order costing) have resulted in badly skewed average costs.

Standard Cost represents a "best guess" cost that provides a good starting point for these two cost fields. This program is also called by IN-L-I Change Costing Method to revalue inventory when changing from Average, LIFO, or FIFO to the Standard Costing method.

**Prerequisites:**

- **MAKE A BACKUP FIRST.**
- **GET EVERYONE OFF THE SYSTEM** before running.

**Operation.**

- Optionally limit processing to a range of **Item numbers** and **Item classes**.
- Optionally limit processing to selected inventory **Type** codes.
- Whether inactive parts are included can also be controlled.
- After making selections, confirm that you want to begin processing.

---

## UT-K-G — Recalc Inventory Book Value

*Source: [ut-k-g_recalc_inventory_book_value.htm](../../../samples/chm/extracted/ut-k-g_recalc_inventory_book_value.htm)*

**Purpose.** Recalculate the **Book Value** field in the inventory master record for a user-defined range of item numbers.

**Background.** The Book Value field is normally maintained incrementally as inventory transactions occur, keeping it synchronized with the Inventory GL account(s) specified in each item's item class — so that Book Value totals in IN-F (Print Inventory Value) tie to the corresponding Inventory GL accounts in the General Ledger.

**Recalculation formula.** Book Value is recalculated as:

```
Book Value = unit average cost × units on-hand
```

**When to use.** Run this program when Book Values have become inaccurate.

**Operation.**

- Limit the items processed by clearing or marking each inventory **Type** with an `X`.
- Enter ranges of **item numbers**, **item classes**, and **GL asset accounts**.
- Specify whether inactive parts are to be included.
- On completion, a report is produced showing the old Book Value, the new Book Value, and the change for each item.

**Important accounting note.** This program makes no accounting entries. If the GL Inventory account(s) were in balance with total Book Value before running the program, a manual journal entry to the Inventory GL account(s) must be made to reflect any changes so that the GL stays in balance.

---

## UT-K-I — Fix Binary Zeroes

*Source: [ut-k-i_fix_binary_zeroes.htm](../../../samples/chm/extracted/ut-k-i_fix_binary_zeroes.htm)*

**Purpose.** Automatically remove binary zero characters from data records across selected data files. Binary zeroes cause posting failures in various areas, including posting of sales orders, receiving purchase orders, and processing payroll checks.

**Background.** Binary zeroes are null bytes (`\x00`) that can creep into field values — most commonly department codes and Location codes. Because binary zero is visually indistinguishable from a space character (neither on-screen nor via Maintain Database can the difference be detected), GL account lookups fail silently: posting amounts are routed to the Clearing Account or go missing entirely.

**Operation.**

1. The program presents a list of all data files in the current company.
2. Click the checkbox next to each file to tag it for processing.
3. Click **Process Tagged** to begin.
4. If the program encounters a record lock (another user has a record open in one of the tagged files), it is safe to stop and re-run later. To avoid record locks, run this program when other users are not in the system.

---

## Cross-references

### UT-K sub-menu — dangerous data-manipulation utilities

The following programs make irreversible bulk changes to live data files. All of them require a full backup and exclusive system access before running. Do not run them in a production environment without explicit authorization and a verified backup.

| Program | Affects | Module cross-link |
|---------|---------|-------------------|
| [UT-K-A Clear Data](#ut-k-a--clear-data) | All six major data categories (GL, AR, AP, IN, PR, MFG) | GL, AR, AP, IN, PR, SM |
| [UT-K-B Global Field Replace](#ut-k-b--global-field-replace) | Any field in any data file | All modules |
| [UT-K-D Recalc GL Chart of Accounts](#ut-k-d--recalc-gl-chart-of-accounts) | `BKGLCOA`, `ISGLCOA` (rebuilds from `BKGLTRAN`) | GL |
| [UT-K-E Consolidate Inventory Locations](#ut-k-e--consolidate-inventory-locations) | Inventory location records; affects IN-L-B and PO ship-to | IN |
| [UT-K-F Set Avg/Last Cost to Std Cost](#ut-k-f--set-avg-and-last-cost-to-std-cost) | Inventory item master cost fields; called by IN-L-I | IN |
| [UT-K-G Recalc Inventory Book Value](#ut-k-g--recalc-inventory-book-value) | Inventory master Book Value; GL Inventory accounts may need a journal entry afterward | IN, GL |
| [UT-K-I Fix Binary Zeroes](#ut-k-i--fix-binary-zeroes) | Any tagged data file; symptoms appear in SO, PO, PR, GL | SO, PO, PR, GL |

### Related programs outside the UT module

- **GL-A View Chart of Accounts** — displays the bucketed amounts that UT-K-D rebuilds.
- **GL-O** (GL posting) — must be idle before running UT-K-D.
- **IN-F Print Inventory Value** — displays Book Value totals that UT-K-G recalculates.
- **IN-L-B Enter/Assign Locations** — must be updated after UT-K-E creates a new Default Location.
- **IN-L-I Change Costing Method** — calls UT-K-F internally when switching to Standard Costing.
- **SD-A Company Defaults** — updated by UT-I when a company is created.
- **DE-A SQL Query Export** — UT-H Print File Layouts is the companion tool for identifying field names before writing SQL queries.
- **UT-K-A** references **UT-I** for the multi-company setup workflow.
