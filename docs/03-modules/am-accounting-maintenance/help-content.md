# AM — Accounting Maintenance

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Accounting → Accounting Maintenance (18 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Accounting Maintenance (AM) module is the administrative backbone of EvoERP's accounting stack. It provides tools to control when GL posting is permitted, execute the fiscal year-end rollover, build and restructure the chart of accounts, define departmental sub-ledgers, format financial statements for printing, consolidate multi-company financials, manage GL transaction detail volume, and archive or purge historical data across GL, AP, AR, vendors, and customers. Most AM programs are run infrequently — typically once per period, once per year, or on demand during cleanup — but their settings govern the behaviour of every other accounting module.

---

## Contents

- [AM-A — Reset General Ledger Close Date](#am-a--reset-general-ledger-close-date)
- [AM-B — Fiscal Year End Routine](#am-b--fiscal-year-end-routine)
- [AM-C — Enter General Ledger Accounts](#am-c--enter-general-ledger-accounts)
- [AM-D — Enter General Ledger Departments](#am-d--enter-general-ledger-departments)
- [AM-E — Format Standard Financial Statements](#am-e--format-standard-financial-statements)
- [AM-F — Format Custom Financial Statements](#am-f--format-custom-financial-statements)
- [AM-G — Consolidate Financials](#am-g--consolidate-financials)
- [AM-H — Change GL Account Codes](#am-h--change-gl-account-codes)
- [AM-I — Consolidate General Ledger Detail](#am-i--consolidate-general-ledger-detail)
- [AM-J — Archive/Purge AP History](#am-j--archivepurge-ap-history)
- [AM-K — Archive/Purge AR History](#am-k--archivepurge-ar-history)
- [AM-N — Maintain GL Fiscal Periods](#am-n--maintain-gl-fiscal-periods)
- [AM-O — Archive/Purge Vendor Data](#am-o--archivepurge-vendor-data)
- [AM-P — Archive/Purge Customer Data](#am-p--archivepurge-customer-data)
- [AM-Q — Enter Budget Information](#am-q--enter-budget-information)
- [AM-R — Out of Balance Report](#am-r--out-of-balance-report)
- [AM-S — Archive/Purge GL Journals](#am-s--archivepurge-gl-journals)
- [AM-T — Archive GL Transaction Detail](#am-t--archive-gl-transaction-detail)
- [Cross-references](#cross-references)

---

## AM-A — Reset General Ledger Close Date

*Source: [am-a_reset_general_ledger_close_date.htm](../../../samples/chm/extracted/am-a_reset_general_ledger_close_date.htm)*

**Purpose.** Use this program to reset the *Open Period Start Date* and *Open Period End Date* that gate all GL posting system-wide. GL posting is blocked for any date prior to the Start Date and after the End Date. Setting these dates correctly prevents accidental posting to a closed period caused by date-entry errors. If a deliberate back-period posting is required, change the date, post the transaction, then restore it.

### Fields and Behavior

**GL Close Date (Open Period Start Date).** The first day of the currently open posting period. No module may post a GL transaction dated before this date, except where the Accounting Open Period Start Date override is enabled (see below).

**End Date (Open Period End Date).** The last day of the currently open posting period.

**Day of week display.** After entering a date, the system automatically shows the day of the week so you can confirm the date is correct.

**Confirm (Y/N).** Enter `Y` to apply the new dates.

**Future Posting control.** Two values control what happens to transactions dated after the End Date:

| Value | Meaning |
|-------|---------|
| `P`   | No transactions from any module may be posted later than the Period End Date. |
| `G`   | General Journal entries in GL-B are allowed after the End Date, but transactions originating in other modules are not. |

### Two Open Period Start Dates

There are two distinct Open Period Start Date values in the system:

1. **Open Period Start Date** — controls posting for all modules.
2. **Accounting Open Period Start Date** — an optional override active when the default settings for GL-B (Enter/Post General Journal Trxns), AP-B (Enter Vouchers), and AR-C (Record Payments) are configured to use it. This override allows the Accounting department to continue posting adjusting entries to the prior period while keeping that period locked for all other operational modules.

---

## AM-B — Fiscal Year End Routine

*Source: [am-b_fiscal_year_end_routine.htm](../../../samples/chm/extracted/am-b_fiscal_year_end_routine.htm)*

**Purpose.** This is the critical program run once per year to prepare the General Ledger for the new fiscal year. It is the most consequential routine in the AM module. EVO recommends running it on the first day of the new fiscal year.

### What AM-B Does

When executed, the program performs all of the following in a single pass:

- Moves the current year GL chart-of-accounts balances (as visible in GL-A View Chart of Accounts) one year back.
- Opens balance slots for the new fiscal year.
- Updates beginning balances in all **asset**, **liability**, and **owner's equity** accounts.
- **Clears** beginning balances in all **income** and **expense** accounts (resetting them to zero for the new year).
- Creates year-end journal entries that post the net income/loss to the **Retained Earnings** account.
- After completion, a set of `YE` (year-end) transactions is queued and ready for posting in GL-O Print/Post General Ledger Batches.

### Does Not Permanently "Close" the Year

Running AM-B does not prevent adjusting entries to the prior year. An unlimited number of prior-year adjusting entries may be made at any time during the new fiscal year, subject only to the Open Period Start Date set in AM-A. This is intentional — audit adjustments are expected.

### Changing the Fiscal Year Start Date

If the company's fiscal year start date changes, the procedure is:

1. Run AM-N (Maintain GL Fiscal Periods) to define the period dates for the short year.
2. Run AM-B on the first day of the new fiscal year using the new start date.

### General Program Operation

The program displays a warning if it detects that fewer than 12 months have elapsed since the last fiscal year-end run (which could indicate an accidental double-run). Click *Yes* to proceed past the warning. Processing begins and a screen is presented to confirm or adjust the start dates of the twelve months for the new fiscal year. Once processing is complete, the YE batch is available in GL-O.

---

## AM-C — Enter General Ledger Accounts

*Source: [am-c_enter_general_ledger_accounts.htm](../../../samples/chm/extracted/am-c_enter_general_ledger_accounts.htm)*

**Purpose.** The primary program for creating and maintaining the chart of accounts. Used during initial ERP setup to build the account structure, and on an ongoing basis to add, modify, or delete individual GL accounts. Budget amounts can also be entered here and compared to actuals on financial statements.

### Fields

**Acct Code.** The GL account code. May include a department suffix (four-character code separated by a hyphen — see AM-D). Press F2 or click *Lookup* to browse existing accounts.

**Description.** A 25-character alphanumeric title for the account. Prints on financial statements and trial balances.

**Type.** The account classification. Determines how the account is handled during the fiscal year-end rollover (AM-B) and on financial statements:

| Code | Type |
|------|------|
| `A`  | Asset |
| `L`  | Liability |
| `O`  | Owner's Equity |
| `I`  | Income |
| `E`  | Expense |

**Non-Cash.** Applies only to Expense (`E`) accounts. Used by the Cash Flow statement (GL-F Print Financial Statements) to add back non-cash expense amounts to net income. Enter `Y` for non-cash expenses such as depreciation. Enter `N` for expenses that involve an actual cash payment such as payroll.

**Inactive.** If set, historical data is retained but GL-O will block any new postings to this account. Use instead of deletion when an account must be retired but its history preserved.

**Budget (monthly amounts).** Twelve monthly budget figures that can be compared against actual posted amounts in GL-A View Chart of Accounts and on printed financial statements. These are the planned monthly amounts entered in advance.

### General Program Operation

To create a new account: enter the account code, description, type, and non-cash flag (if Expense). Optionally enter monthly budget amounts. Click *Save* (F10) to write the record.

### Deleting a GL Account

To delete an account: bring it up on screen and click *Delete*. If the account has any transactions posted to it, the system will prompt for a target GL account to which those transactions must be moved before deletion proceeds.

---

## AM-D — Enter General Ledger Departments

*Source: [am-d_enter_general_ledger_departments.htm](../../../samples/chm/extracted/am-d_enter_general_ledger_departments.htm)*

**Purpose.** Departments allow financial performance tracking for sub-groups within the company. The department code is a four-character suffix appended to a GL account code, separated by a hyphen (e.g., `5000-MFGR`). This program auto-generates departmentalized account entries for selected account types, saving the labor of entering each account-department combination individually through AM-C.

### Key Concepts

- Departmental accounting is generally appropriate for **income and expense accounts only**. Asset, liability, and owner's equity accounts are normally not tracked by department because automatic postings to balance sheet accounts only go to a single default account/department — manual journal adjustments would be required to allocate balance sheet activity across departments.
- When a department is created, a new account record is generated for every GL account type selected in the wizard.
- To delete a department that is no longer needed: first journalize out all amounts from its accounts (GL-B), then run AM-I (Consolidate General Ledger Detail) for the department, then delete through this program.

### Fields

**Use which existing department as TEMPLATE.** Enter the code of an existing department whose account structure closely matches the new department to be created. If left blank, the full company chart of accounts is used as the template.

**Code of the NEW department to create.** Enter the four-character code for the new department.

**Clear budget values?** If `Y`, budget values from the template department are not copied to the new department. Use `Y` when the new department requires substantially different budget figures.

**Which account types should be transferred?** A set of yes/no flags for each account type (Assets, Liabilities, Owner's Equity, Income, Expense). Set to `N` for any type that should not receive a departmental extension.

### General Program Operation

After creating the new department, use GL-B (Enter/Print General Journal Trxns) to enter the beginning balances or to transfer existing non-departmental account balances into the new department-based accounts.

For more limited departmental use, a single department extension may be added to one existing account in AM-C without running this program. The original non-departmental account remains; the new departmental account is created alongside it.

---

## AM-E — Format Standard Financial Statements

*Source: [am-e_format_standard_financial_statements.htm](../../../samples/chm/extracted/am-e_format_standard_financial_statements.htm)*

**Purpose.** Defines the account ranges and section headings for the three pre-formatted standard financial statements. This setup must be completed before running the GL-F Print Financial Statements program. The standard format is pre-structured and itemizes all GL accounts individually. If more flexible grouping, summary/detail combinations, or non-sequential account ranges are needed, use AM-F (Format Custom Financial Statements) instead.

### Three Statement Types

| Key | Statement |
|-----|-----------|
| `I` | Income Statement (Profit and Loss) |
| `B` | Balance Sheet (Assets, Liabilities, Owner's Equity at a point in time) |
| `C` | Statement of Changes in Financial Position (Cash Flow) |

### Income Statement Sections

Each section requires a range of GL accounts (**G/L From** and **G/L Thru**) and a 25-character title:

- **Report Title** — prints at the top of the statement.
- **Income Main Title** — division heading for income accounts.
- **Income 1, 2** — income sub-group ranges and titles (e.g., Power Tool Sales and Laundry Equipment Sales as separate subtotals).
- **COGS Main Title** — division heading for cost of goods sold.
- **COGS 1, 2** — cost-of-goods-sold sub-group ranges.
- **Expenses Main Title** — division heading for operating expenses.
- **Expenses 1, 2, 3, 4** — expense sub-group ranges.
- **Other Inc** — other income division.
- **Other Exp** — other expense division.

### Balance Sheet Sections

- **Report Title** — prints at the top of the statement.
- **Assets Main Title / Assets 1, 2, 3, 4** — asset division and sub-groups.
- **Liabilities Main Title / Liabilities 1, 2, 3, 4** — liability division and sub-groups.
- **Owners Equity Main Title / OE 1, 2** — owner's equity division and sub-groups.

### Cash Flow Statement Sections

- **Report Title** — prints at the top.
- **Net Income** — net income division.
- **Non-Cash Exp** — non-cash expense accounts (flagged as Non-Cash in AM-C) to be added back to net income.
- **Assets Main Title / Assets 1, 2, 3, 4** — asset sub-groups to be subtotaled.
- **Liabilities Main Title / Liabilities 1, 2, 3, 4** — liability sub-groups to be subtotaled.

### General Program Operation

Select the statement type (I, B, or C). Enter a main title for each major division. Use sub-groups where you want subtotals within the major total. For example, to subtotal power tools sales separately from laundry equipment sales: enter the power tools account range in *Income 1 G/L From/Thru* with a title "Power Tool Sales", and the laundry range in *Income 2 G/L From/Thru*. Press F2 on any account code field to look up accounts. Click *Save* (F10) when done. The system does not validate that entered account codes exist, so double-check account codes when typed manually.

---

## AM-F — Format Custom Financial Statements

*Source: [am-f_format_custom_financial_statements.htm](../../../samples/chm/extracted/am-f_format_custom_financial_statements.htm)*

**Purpose.** Builds fully customized financial statement formats for printing via GL-N (Print Custom Statements). Custom statements support up to nine column positions, up to 20 named running totals, optional percentage calculations, header and blank-line commands, and grouping of non-sequential account ranges — capabilities not available in the standard AM-E format. Consult your accountant when creating these statements to ensure totals properly reflect the chart of accounts.

### Fields

**Report Name.** A 10-character identifier used to retrieve the saved format. Does not print as a title on the statement.

**Line.** Auto-assigned line number. A pointer marks the current line during editing.

**Op (Operator/Command code).** Chosen from an on-screen pop-up window. The operator determines which other columns are active for data entry on that line. Commands:

| Code | Command | Description |
|------|---------|-------------|
| `tO` | top Of form | Go to the top of the next page. |
| `Mt` | Main title | Statement's main title. Only allowed once; must be line 1. |
| `pH` | print Header | Print a format header line. |
| `Ga` | Get G/L accounts | Read a specific account or range; optionally print and/or total them. |
| `At` | Add to total | Add one total field into another; used for running totals and subtotals. |
| `pS` | print Single line | Print a single dashed line (e.g., `------------`). |
| `pD` | print Double line | Print a double dashed line (e.g., `============`). |
| `pB` | print Blank line | Print blank lines; count specified in column **T**. |
| `pT` | print Total field | Print a previously accumulated total. |
| `Ct` | Clear total field | Reset an assigned total to zero for reuse. |

**G/L From / G/L Thru.** Starting and ending GL account codes. Used only with `Ga`.

**T (Total field number, 1–20).** For `Ga`: the slot (1–20) into which the GL range's total is accumulated. For `pB`: the number of blank lines. For `At`, `pT`, `Ct`: identifies which of the 20 named totals to operate on.

**B (Base field number, 1–20).** Identifies the total field to use as the percentage base when GL-N is run with the *Calculate %'s* option. Also holds the accumulator for `At` (Add to Total) commands — the sum of `T` is added into `B`.

**P (Print flag).** For `Ga` only: `Y` to print the individual account amounts on the statement, `N` to read them into totals without printing each line.

**L (Location, 1–9).** Column position (in increments of 5 character positions) where amounts or headers print. When only one data category is selected for a report, locations are under user control; when multiple categories (e.g., current + prior year) are selected, the program controls the layout.

**$ (Dollar sign).** `Y` or `N` — whether a dollar sign prefix is printed before the amount on the current line.

**D/C (Debit/Credit).** Required for `pT` commands. Declares whether the total being printed is a debit or credit. If the actual sign of the total is opposite the declared D/C, the amount prints in brackets. Confirm with your accountant.

**Description.** Free text for titles, headers, or labels on total lines.

### General Program Operation

Enter a *Report Name* to start a new format or retrieve an existing one (F2 to look up). Line 1 must always be an `Mt` (Main title) command. The `Op` command pop-up appears for each new line. Cursor movement is restricted to the fields relevant to the chosen command. After completing each line, the program prompts to save it. Press the down arrow to move to the next blank line and click *Add* to add a new line. Press Esc (or click *Exit*) when the format is complete — this finalizes the format file.

### Sample Formats — Tutorial

#### Trial Balance (6 lines)

| Line | Op | G/L From | G/L Thru | T | B | P | L | $ | D/C | Description |
|------|----|---------|---------|---|---|---|---|---|-----|-------------|
| 1 | Mt | — | — | — | — | — | — | — | — | Trial Balance Report |
| 2 | pH | — | — | — | — | — | 1 | — | — | TRIAL BALANCE ACCOUNTS: |
| 3 | pB | — | — | 1 | — | — | — | — | — | *(1 blank line)* |
| 4 | Ga | 10000 | 22300 | 1 | 1 | Y | 1 | N | — | *(account descriptions from chart)* |
| 5 | pD | — | — | — | — | — | 1 | — | — | *(double line)* |
| 6 | pT | — | — | 1 | 1 | — | 1 | N | C | Trial Balance Total: |

#### Balance Sheet — Key Technique

Use `Ct` (Clear total) to empty a total field after printing it so it can be reused. Use `At` (Add to total) to accumulate subtotals into a master total. For example: after printing Liabilities subtotals into field 1 and printing them, add field 1 into field 2 (which holds the running Liabilities total), clear field 1, then use field 1 again for Owner's Equity, then add field 1 into field 2, and finally print field 2 as the combined Liabilities + Owner's Equity total.

#### Income Statement — Key Technique

GL account amounts accumulated in multiple total fields (e.g., income in field 1, expenses in field 2) can all be added into a single field 3, which then serves as both the Net Income total and the percentage calculation base. The report engine runs the format twice: once to compute totals (for percentages) and once to print — do not clear the percentage base field between uses.

Note: amounts print in column location 1, subtotals in location 2, and the net total in location 3, creating a visually tiered layout. Dollar sign (`$`) flags can be selectively applied at total lines while suppressing them on detail lines.

---

## AM-G — Consolidate Financials

*Source: [am-g_consolidate_financials.htm](../../../samples/chm/extracted/am-g_consolidate_financials.htm)*

**Purpose.** Generates a combined, read-only chart-of-accounts file from multiple EvoERP companies so that consolidated financial statements can be printed without merging the companies' live data. A single EvoERP installation can serve multiple companies; this program lets you report across them.

### Requirements and Limitations

- The chart-of-accounts structures of the companies being consolidated must be compatible — account numbers must represent the same account type across all companies (e.g., `10000` cannot be an Asset in Company A and a Liability in Company B).
- All companies being consolidated must use the same **base currency**. The Multi-Currency feature does not apply to consolidated financial statements.
- This operation produces an external reporting file only. It does **not** merge or affect the financial data of any individual company.

### Fields

**Consolidation Name.** A named set of companies to consolidate. Multiple consolidation sets can be stored under different names.

**Last Consolidation was on.** Displays the date the selected consolidation set was last run.

**Company Code.** Lists the company codes available for selection.

**Include.** Mark companies to include in the consolidation. An asterisk (`*`) indicates a selected company; pressing Enter on a selected company deselects it.

### General Program Operation

1. Enter or look up a Consolidation Name.
2. Highlight each company to include and press Enter to mark it with an asterisk.
3. Click *Save Consolidation Companies* and confirm.
4. The program creates an independent combined chart-of-accounts file in the `DBAMFG` or `EVOERP` subdirectory, identified by a `.B` file with a company code extension.
5. Go to GL-F (Print Financial Statements) or GL-N (Print Custom Statements) and answer *Yes* to the prompt for consolidated financial information.

---

## AM-H — Change GL Account Codes

*Source: [am-h_change_account_codes.htm](../../../samples/chm/extracted/am-h_change_account_codes.htm)*

**Purpose.** Renames a GL account code across the entire system, moving all transaction history, balances, and references from the old code to the new code. Primarily used when restructuring or renumbering the chart of accounts. Eliminates the need to make journal entries to transfer balances manually. Can also merge two existing accounts by mapping the old account into an existing new account.

### Prerequisite

The "new" account code must already exist in AM-C (Enter General Ledger Accounts) before running this program.

### General Program Operation

Enter the **Old GL Code** and the **New GL Code**. Processing begins immediately and all data associated with the old code is transferred to the new code.

**Important caveat:** If the old account code is referenced in AD-A (General Ledger Defaults) as a system-assigned default account, that reference will **not** be automatically updated by this program. It must be manually corrected in AD-A after the rename.

---

## AM-I — Consolidate General Ledger Detail

*Source: [am-i_consolidate_gl_detail.htm](../../../samples/chm/extracted/am-i_consolidate_gl_detail.htm)*

**Purpose.** Condenses ranges of individual GL transaction records into single summarized records, one per GL account per journal type per fiscal month. Used to reduce file volume in high-transaction accounts (such as payroll) and to manage the size of the GL transaction file (`BKGLTRAN.B*`) over time without permanently losing account-balance information.

**Warning: always make a full system backup before running this program.** Consolidation permanently destroys the transaction-level audit trail (including timestamps and user login IDs) for the affected records.

### Use Cases

1. **High-volume accounts.** Payroll postings, for example, generate multiple GL records per employee per pay run. Consolidation reduces thousands of detail lines to one summary record per account per period.
2. **Aging data management.** If detail beyond two years is no longer needed, run this program to collapse old detail into summary data rather than purging it outright. Account balances are preserved; only the individual transaction lines are lost.

### Consolidation Result

The output is a single record per GL account for each journal type within each fiscal month (as defined in AM-N Maintain GL Fiscal Periods) within the specified date range.

### General Program Operation

Enter:
- **From/Thru date range** — the date span to consolidate.
- **From/Thru GL account range** — the account codes to consolidate.
- **Journal type** (optional) — limit to a specific journal type such as `PR` (Payroll) or `WO` (Work Order).

Processing may take a significant amount of time depending on the number of records involved.

### Audit Data Warning

Each GL transaction is stored with a timestamp and the User login ID of the person who generated it. Consolidation deletes this audit trail for all consolidated records.

---

## AM-J — Archive/Purge AP History

*Source: [am-j_archive_purge_ap_history.htm](../../../samples/chm/extracted/am-j_archive_purge_ap_history.htm)*

**Purpose.** Removes or archives Accounts Payable invoice and payment records for specified vendors and date ranges. Reduces AP file sizes and removes obsolete payables data from the live system.

**Warning: always make a full system backup before running this program.**

### What Is Processed

All payments through the specified ending date that did **not** make partial payments against any invoices, plus all associated invoices and vouchers paid by those payments, are eligible for processing. Records that involved partial payments are excluded because a clear cutoff date cannot be established. Purchase history of items (item purchase records) is not processed.

### General Program Operation

1. Select the operation mode: **Purge** (delete), **Archive** (save to archive database), or **Restore** (restore previously archived records).
2. Optionally enter a range of vendor codes.
3. Enter the ending date cutoff — only fully settled transactions on or before this date are eligible.
4. Confirm and process.

---

## AM-K — Archive/Purge AR History

*Source: [am-k_archive_purge_ar_history.htm](../../../samples/chm/extracted/am-k_archive_purge_ar_history.htm)*

**Purpose.** Removes or archives Accounts Receivable invoice and payment records for specified customers and date ranges. Reduces AR file sizes and clears obsolete receivables data from the live system.

**Warning: always make a full system backup before running this program.**

### What Is Processed

All invoices that are **fully paid** as of the specified date, plus the associated payment, commission, and other Receivables-related transaction records, are eligible. Shipment history of items (shipment records by item) is not processed.

### General Program Operation

1. Select the operation mode: **Purge**, **Archive**, or **Restore**.
2. Optionally enter a range of customer codes.
3. Enter the ending date cutoff — only fully-paid invoices on or before this date are eligible.
4. Confirm and process.

---

## AM-N — Maintain GL Fiscal Periods

*Source: [am-n_maintain_gl_fiscal_periods.htm](../../../samples/chm/extracted/am-n_maintain_gl_fiscal_periods.htm)*

**Purpose.** Defines the start dates of the twelve fiscal periods (months) within each fiscal year. Required during initial system setup and each time AM-B (Fiscal Year End Routine) is run to establish the period dates for the incoming year. Also required if the company changes its fiscal year start date.

### General Program Operation

The program automatically populates the twelve period start dates based on calendar months working backwards from the fiscal year start date. If the company uses non-calendar-month periods, or had a **short stub year** due to a change in fiscal year, enter the desired dates manually.

**Handling a short year example:** If changing from a June 1 fiscal year to a January 1 fiscal year, the short-year dates would be: 6/1; 7/1; 8/1; 9/1; 10/1; 11/1; 12/1 — and then 12/1 repeated for all remaining period slots in that year's table.

The fiscal period dates defined here are also used by AM-I (Consolidate General Ledger Detail) to determine which records fall within a given fiscal month during consolidation.

---

## AM-O — Archive/Purge Vendor Data

*Source: [am-o_archive_purge_vendor_data.htm](../../../samples/chm/extracted/am-o_archive_purge_vendor_data.htm)*

**Purpose.** Removes or archives the complete vendor master record and all associated transaction data (invoices, payments, purchase orders, RFQs) for vendors that are no longer active. Provides a deeper cleanup than AM-J, which only handles AP transaction history.

**Warning: always make a full system backup before running this program.**

### Eligibility Criteria

A vendor is eligible for processing only if it has:
- No open purchase orders.
- No Payables transactions or RFQ activity after the specified ending date.

All associated data is processed: invoices, payments, purchase orders, RFQs, and the vendor master record itself.

### General Program Operation

1. Select the operation mode: **Purge**, **Archive**, or **Restore**.
2. Optionally enter a range of vendor codes.
3. Optionally enter a range of vendor class.
4. Enter the ending date of the activity cutoff.
5. Confirm and process.

---

## AM-P — Archive/Purge Customer Data

*Source: [am-p_archive_purge_customer_data.htm](../../../samples/chm/extracted/am-p_archive_purge_customer_data.htm)*

**Purpose.** Removes or archives the complete customer master record and all associated transaction data (invoices, payments, sales orders, RMAs, service orders, quotes, estimates) for customers that are no longer active. Provides a deeper cleanup than AM-K, which only handles AR transaction history.

**Warning: always make a full system backup before running this program.**

### Eligibility Criteria

A customer is eligible for processing only if it has:
- No open sales orders or RMA/Service and Repair orders.
- No Receivables transactions, Quote, or Estimating activity after the specified ending date.

All associated data is processed: invoices, payments, sales orders, RMA orders, service orders, quotes, estimates, and the customer master record itself.

### General Program Operation

1. Select the operation mode: **Purge**, **Archive**, or **Restore**.
2. Optionally enter a range of customer codes.
3. Optionally enter a range of customer class.
4. Enter the ending date of the activity cutoff.
5. Confirm and process.

---

## AM-Q — Enter Budget Information

*Source: [am-q_enter_budget_information.htm](../../../samples/chm/extracted/am-q_enter_budget_information.htm)*

**Purpose.** Enters or updates budget amounts for a range of GL accounts in bulk. This is the batch complement to the per-account budget entry available in AM-C. Budget amounts can then be compared against actual posted results in GL-A (View Chart of Accounts) and on printed financial statements.

### General Program Operation

1. Select the range of accounts and departments to be updated.
2. Choose the basis for the budget amounts:
   - **Copy from prior-year actuals with a multiplier** — takes the actual amounts from one year ago and scales them by a user-specified factor (e.g., 1.05 for a 5% increase).
   - **Annual amount divided by 12** — during processing, the system prompts for an annual total for each account in the range and divides it equally across the 12 months.

---

## AM-R — Out of Balance Report

*Source: [am-r_out_of_balance_report.htm](../../../samples/chm/extracted/am-r_out_of_balance_report.htm)*

**Purpose.** Identifies GL journal groupings in which the debits and credits do not net to zero. The same diagnostic report is available from within GL-O (Print/Post General Ledger Batches), but running it here allows it to be executed independently without waiting for GL-O to scan all unposted transactions.

### General Program Operation

Enter a date range and select whether to examine **posted** or **unposted** transactions. The report flags any journal grouping (matched by date, journal type, and Cus/Vend Code and Invoice number) where debits and credits do not balance.

**False positives:** The report may flag entries that are genuinely balanced if the two sides of the entry reference different Customer or Vendor codes or different invoice numbers. Such groupings must be manually reviewed and discarded if the underlying transaction is confirmed correct.

---

## AM-S — Archive/Purge GL Journals

*Source: [am-s_purge_or_archive_gl_journ.htm](../../../samples/chm/extracted/am-s_purge_or_archive_gl_journ.htm)*

**Purpose.** Removes or archives the General Ledger journal header records as listed in GL-B (Enter/Post General Journal Trxns). These journal headers are used by GL-B to allow copying or reversing of previously posted entries. Purging or archiving them has **no effect on account balances or posted GL transactions** — it only removes the journal entry "templates" from the GL-B list.

### What Is and Is Not Affected

- **Affected:** Journal entries listed in GL-B that can be used to copy or reverse prior entries.
- **Not affected:** Posted GL transaction detail (account balances, transaction history in GL-C, GL-D). For that, use AM-T.

Only journal entries that are already marked as **Posted** in GL-B are eligible for purge or archive.

### General Program Operation

1. Select the operation mode: **Purge**, **Archive**, or **Restore**.
2. Enter ranges of **Journal Number**, **Date**, or **Journal type** as filters.
3. Process.

---

## AM-T — Archive GL Transaction Detail

*Source: [am-t_archive_gl_transaction_de.htm](../../../samples/chm/extracted/am-t_archive_gl_transaction_de.htm)*

**Purpose.** Archives GL transaction detail entries older than 6 fiscal years past, removing them from the live transaction file and replacing them with a single synthesized beginning-balance transaction per account. This is the standard long-term retention mechanism for the GL transaction file — more targeted than AM-I (which consolidates by date range) and less destructive than a purge.

### Key Behavior

- The cutoff date is **not user-configurable**. It is fixed at the Fiscal Year Start Date that is 6 years in the past, as defined in AM-N (Maintain GL Fiscal Periods).
- There are no other selection criteria. The program processes all accounts for all transactions older than the 6-year mark.
- Once archived, the transactions remain accessible for reporting in GL-C (Print GL Transactions) and GL-D (Print Journals) — they are moved to an archive database, not deleted.

---

## Cross-references

AM is the administrative spine of the EvoERP accounting stack. The relationships between AM and other modules are as follows:

**GL (General Ledger)**
- AM-A controls the posting date window enforced by GL-O and GL-B.
- AM-B generates the YE batch posted through GL-O.
- AM-C and AM-D build the chart of accounts read by GL-A, GL-B, GL-C, GL-D, GL-F, GL-N, and GL-O.
- AM-E and AM-F define the layouts used by GL-F and GL-N respectively.
- AM-G feeds the consolidated file used by GL-F and GL-N in multi-company mode.
- AM-I and AM-T manage the volume of the `BKGLTRAN.B*` file read by GL-C and GL-D.
- AM-N fiscal period dates govern period assignment in GL-O and are referenced by AM-I and AM-T.
- AM-R runs the same out-of-balance check available inside GL-O.
- AM-S manages the GL-B journal entry header list.

**AP (Accounts Payable)**
- AM-J handles transaction-level AP history for individual invoices and payments.
- AM-O performs a deeper purge/archive of entire vendor records including the vendor master.

**AR (Accounts Receivable)**
- AM-K handles transaction-level AR history for individual invoices and payments.
- AM-P performs a deeper purge/archive of entire customer records including the customer master.

**AD (Accounting Defaults)**
- AM-H (Change GL Account Codes) does not update account code references in AD-A (General Ledger Defaults). Those must be manually corrected after an account rename.

**Critical sequencing note:** AM-B (Fiscal Year End Routine) should be run on the first day of the new fiscal year. It depends on AM-N having correct period dates for the new year, and its output (the YE batch) must be posted through GL-O. AM-A should be updated at the same time to advance the Open Period Start Date to the new year.
