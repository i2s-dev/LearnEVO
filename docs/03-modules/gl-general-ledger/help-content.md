# GL — General Ledger

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Accounting → General Ledger (18 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The General Ledger is the financial backbone of EvoERP. Every accounting module — Accounts Receivable, Accounts Payable, Sales Orders, Purchase Orders, Work Orders, Inventory, and Payroll — posts its transactions through a temporary staging file (BKGLTEMP) and into the permanent GL via GL-O. The GL stores monthly balances for the current year, up to six prior years, and budget amounts for every account in the chart of accounts. Financial statements (income statement, balance sheet, cash flow) are produced from GL data. Bank account reconciliation and credit card reconciliation are also managed here.

---

## Contents

- [GL-A — View Chart of Accounts](#gl-a--view-chart-of-accounts)
- [GL-B — Enter/Post General Journal Transactions](#gl-b--enterpost-general-journal-transactions)
- [GL-C — Print GL Transactions](#gl-c--print-gl-transactions)
- [GL-D — Print Journals](#gl-d--print-journals)
- [GL-E — Print Detailed Trial Balance](#gl-e--print-detailed-trial-balance)
- [GL-F — Print Financial Statements](#gl-f--print-financial-statements)
- [GL-G — Print GL Code and Description](#gl-g--print-gl-code-and-description)
- [GL-H — Print Chart of Accounts](#gl-h--print-chart-of-accounts)
- [GL-I — Print Check Register](#gl-i--print-check-register)
- [GL-J — Reconcile Check Register](#gl-j--reconcile-check-register)
- [GL-K — Transfer Bank Account Funds](#gl-k--transfer-bank-account-funds)
- [GL-L — Credit Card Reconciliation](#gl-l--credit-card-reconciliation)
- [GL-N — Print Custom Financial Statements](#gl-n--print-custom-financial-statements)
- [GL-O — Print/Post General Ledger Batches](#gl-o--printpost-general-ledger-batches)
- [GL-P — Edit General Ledger Batch Entries](#gl-p--edit-general-ledger-batch-entries)
- [GL-Q — Enter Payroll Checks](#gl-q--enter-payroll-checks)
- [GL-R — Business Status](#gl-r--business-status)
- [GL-S — View GL Journal Notes](#gl-s--view-gl-journal-notes)
- [Cross-references](#cross-references)

---

## GL-A — View Chart of Accounts

*Source: [gl-a_view_chart_of_accounts.htm](../../../samples/chm/extracted/gl-a_view_chart_of_accounts.htm)*

**Purpose.** Allows read-only viewing of accounts in the General Ledger chart of accounts, with one editable exception: budget amounts can be changed here to project future performance. New accounts cannot be created and existing account metadata cannot be changed in this program. To create or modify GL accounts, use AM-C Enter General Ledger Accounts. Before changing or deleting a GL account, verify system defaults in AD-A General Ledger Defaults.

### Field Explanations

| Field | Description |
|---|---|
| **Acct Code** | The GL account code or number to view. Press F2 or click Lookup to search. |
| **Dept** | GL department code for the account. Leave blank if not using departments or if the account has no department. |
| **Description** | The account title — filled automatically after entering the account code. Read-only. |
| **Type** | Account type: `A` = Asset, `L` = Liability, `O` = Owner's Equity, `I` = Income, `E` = Expense. Read-only. |
| **Norm Dr/Cr** | Normal balance side: `D` = Debit (asset and expense accounts), `C` = Credit (equity, income, liability accounts). Filled automatically. |
| **Non-Cash** | Flags the account as a non-cash expense. Used for the Changes in Financial Position (Cash Flow) statement in GL-F. Non-cash expense amounts (e.g., depreciation) are added back to net income when calculating ending cash position. |
| **Current** | Monthly amounts posted in the current fiscal year — filled from posting activity. |
| **Budget** | Monthly budget amounts — the only field that can be changed in this program. Used for comparison in financial statements and projections. Entering $100.00 on a credit-normal account stores and displays it as `<$100.00>`; no need to enter as negative. |
| **1 Year Past** | Monthly posted amounts from the previous fiscal year. |
| **2 Years Past** | Monthly posted amounts from two years ago. |
| **Prior Years** | Previous and Next buttons navigate up to 6 years back. |

### Viewing an Account

1. Enter the **Acct Code** and press Enter, or press F2 / click Lookup to search.
2. Account information displays automatically.
3. Press F3 or click **Clear** to clear the screen before entering another account code.
4. Change budget amounts as needed. The **Ending Balance** column recalculates automatically.
5. Click **Save** before leaving — budget changes are not committed until saved.

---

## GL-B — Enter/Post General Journal Transactions

*Source: [gl-b_enter_post_general_journal_trxns.htm](../../../samples/chm/extracted/gl-b_enter_post_general_journal_trxns.htm)*

**Purpose.** Entry point for miscellaneous General Journal transactions that need to reach the GL but do not belong to a specific subsidiary module. Common uses include: month-end and year-end accruals and reversals, recording bank service charges and other checking account expenses, beginning balance entries at system startup, and any adjusting entry that does not touch AR or AP. Entries are batch transactions with up to 999 line items each; the batch net must equal zero before posting. Supports transaction templates for recurring entries and a Reverse function to flip debits and credits.

> **CAUTION:** Do not use GL-B to adjust Accounts Receivable or Accounts Payable GL account balances. Any adjustment to those accounts must be made within the AR or AP modules to keep subsidiary aging reports reconciled with the GL.

### Transaction Types

| Code | Type | Description |
|---|---|---|
| `GJ` | General Journal | Adjusting/correcting entry that does not affect cash accounts. |
| `CR` | Cash Receipts | Entry that posts a Deposit record to the check register. |
| `CD` | Cash Disbursements | Entry that posts a Check record to the check register. |
| `TT` | Transaction Template | Reusable template for recurring or reversing GJ entries. Journal type stored as GJ. |
| `BB` | Beginning Balance | Used to enter fiscal year-end balance sheet amounts at system startup. Journal type stored as GJ. |

### Header Screen Fields

| Field | Description |
|---|---|
| **Transaction Number** | Auto-assigned 6-digit numeric. Starting number set in AD-A (DBA Classic) or SD-R (Evo-ERP). |
| **Transaction Type** | Select from the five types above (F2 or lookup icon for the list). |
| **Transaction Date** | Posting date for all line items in this transaction. Defaults to today. |
| **Bank Account [1-9]** | Required for CR and CD types. References bank accounts defined in AD-B Checking Accounts Defaults. |
| **GJ Transaction Code** | Optional 10-character alphanumeric identifier (e.g., customer number, vendor number, `ME-ADJ-01`). |
| **Deposit/Check Number** | Required for CR and CD types; optional identifier for GJ types. 6-digit numeric. |
| **Job Number** | Optional (or required if SD-A Company Defaults is set to `R`). Suggested for all line items but overridable per line. Job list maintained in SM-P-F Enter Jobs. |

### Line Item Entry Screen Fields

| Field | Description |
|---|---|
| **GL Account** | Account code for this line item. F2 / lookup available. |
| **Line item description** | Defaults to the GL account description but can be overridden with a more specific description (e.g., `Bank Charges 11/1/95`). Both the standard account description and this field print on GL-D and GL-E reports. |
| **Dr/Cr** | `D` = Debit, `C` = Credit. Defaults to the account's normal balance side; can be changed. |
| **Line item amount** | Dollar amount to debit or credit. |
| **Needed to balance** | Running net debit/credit balance of all line items entered so far. Use it to determine the amount and direction of the final balancing entry. |
| **Notes** | Free-text notes attached to this line item. |
| **Job Number** | Inherits from header; can be overridden per line. |

### General Program Operation

**Creating a new transaction:** Click **Add** (or press Insert) on the opening screen to go to the header screen. Complete all header fields and click **Save** to advance to the line item list.

**Adding a line item:** Click **Add** (or press Alt-A) on the line item list. Enter the GL account, accept or override the description, set Dr/Cr, enter the amount, and press through the last field to return to the list. Repeat until the transaction is complete.

**Editing a line item:** Highlight the item, click **Edit**, make changes, click **Save** (F10) or press through the last field.

**Deleting a line item:** Highlight the item, click **Delete**, confirm Yes.

**Saving the transaction:** Click **Save** (F10) from the line item list. An out-of-balance transaction can be saved but cannot be posted. A warning is displayed if saving out of balance.

**Editing an existing transaction:** From the opening screen, highlight the transaction and click **Edit** to access the header, then the line item list.

**Deleting an entire transaction:** Highlight on the opening screen, click **Delete**, confirm Yes.

**Posting a transaction:** Highlight on the opening screen, click **Post Transaction**. The transaction must be in balance. After posting it goes into the BKGLTEMP temporary file; it is not yet in the permanent GL. Final posting to the permanent GL happens via GL-O Print/Post General Ledger Batches.

**Printing a transaction:** Highlight on the opening screen, click **Print transaction**. The standard List/Print/Disk output options are presented.

**Copying or reversing a transaction:** Highlight any transaction (including templates or previously posted transactions), click **Copy** or **Reverse**. Reverse flips all debits to credits and vice versa. The result is a new transaction in the list ready for editing and posting.

**Entering notes:** Click **NOTES**, type the note, click **Save Notes**. Notes flagged as Hidden appear on-screen only and do not print.

---

## GL-C — Print GL Transactions

*Source: [gl-c_print_gl_transactions.htm](../../../samples/chm/extracted/gl-c_print_gl_transactions.htm)*

**Purpose.** Produces a listing of individual GL transactions — posted, unposted, or orphaned (orphans are posted transactions whose GL account has since been deleted from the chart of accounts). Supports extensive filtering for ad hoc analysis or audit work.

### General Program Operation

Set filters before running:

- **Posted / Unposted / Orphan** — select the population to include.
- **Journal type** — limit to a single journal type or leave blank for all.
- **GL account range** — from/thru account codes.
- **Department range** — from/thru department codes.
- **Post date range** — from/thru posting dates.
- **Entry date range** — from/thru entry (creation) dates.
- **C/V/P Code Range** — customer code, vendor code, or item number reference contained in the transaction record.
- **Invoice/Voucher number range** — from/thru invoice or voucher numbers.
- **Batch range** — from/thru posting batch numbers. A batch number is assigned each time transactions are transferred to the GL via GL-O.
- **Description keyword** — search for a word or phrase in the transaction description.
- **Include YE entries** — whether to include Year End journal entries.
- **Include Audit detail** — if yes, adds entry time and User Login ID to each line.

The report lists transactions in GL Account/Department order, subtotaled by account with total debits, total credits, and net transaction per account, plus a grand total debit and credit across all listed transactions.

---

## GL-D — Print Journals

*Source: [gl-d_print_journals.htm](../../../samples/chm/extracted/gl-d_print_journals.htm)*

**Purpose.** Prints a chronological listing of all transactions of a specific journal type within a date range, allowing verification that all activity for a day or period was recorded correctly. Complements GL-E (account-order detail) — together they provide a complete audit trail.

### Available Journal Types

| Journal | Source Transactions |
|---|---|
| **General Journal** | GJ-type adjusting entries from GL-B. |
| **Cash Receipts Journal** | CR entries from GL-B; cash-terms invoice postings from SO-G; AR payment receipts from AR-C; sales order deposits from AR-N. |
| **Cash Disbursements Journal** | AP checks from AP-H; ePayments from AP-F; manual checks from AP-B; COD payments from AP-C; customer refunds from AR-M; CD entries from GL-B. |
| **Sales Journal** | All sales order invoice transactions, AR vouchers/credits from AR-B, interest charges from AR-D. |
| **Purchases Journal** | All non-cash AP and PO transactions, including sales tax, commissions, customer refunds, and payroll tax transfers to AP. |
| **Other Journal** | Inventory value/quantity changes, bank account fund transfers (GL-K), commissions, month-end currency conversions. |
| **Work Orders Journal** | All transactions originating from the Work Orders module. |
| **Year End Journal** | Entries closing Income and Expense accounts to Retained Earnings, generated by AM-B Fiscal Year End Routine and by GL-O when income/expense accounts are posted to in a prior year. |

### General Program Operation

1. Enter **From Posting Date** and **Thru Posting Date** (defaults to today if left blank; Thru defaults to From).
2. Optionally enter an **Entry Date** range to check all entries made on a given day regardless of posting date — useful for verifying daily batches.
3. Select the journal to print from the menu.

The report subtotals each transaction group, provides grand total debits and credits at the end of the transaction listing, and then appends a summary of net debit and credit to each GL account.

---

## GL-E — Print Detailed Trial Balance

*Source: [gl-e_print_detailed_trial_balance.htm](../../../samples/chm/extracted/gl-e_print_detailed_trial_balance.htm)*

**Purpose.** Prints transactions in account code and date order rather than the journal-type order used by GL-D. Together with GL-C and GL-D it forms the audit trail: GL-E shows all transactions per GL account; the journals show related entries per transaction. Date range limited to 6 years before the start of the current fiscal year; for older data use GL-C.

### General Program Operation

1. Enter **from/thru GL accounts**, **from/thru GL departments**, **from/thru posting dates**, and **from/thru entry dates**.
2. Specify whether to include **YE (Year End)** transactions. Balance forward from prior years always includes YE entries.
3. **Print Summary Only?**
   - `N` — full detail listing of all transactions within the range.
   - `Y` — summary mode; then choose:
     - **Net Change** — one line per account showing the net change. Optionally **Subtotal by Journal Type** — gives each account a subtotal per journal type, very helpful for month-end balancing.
     - **Beginning and Ending Balances** — opening and closing balance per account.
4. **Print Customer/Vendor Code or Name (C/N)?** — If Name, customer/vendor names print instead of codes; transaction amount field maximum becomes 99,999,999.99.
5. **Include long check numbers** — yes/no.
6. **Print Header on every page** — yes/no.
7. **Use Fiscal YE data for Beginning Balance** — speeds up the report significantly; only valid when no entry date range is specified, no subtotal by journal type is selected, and all journal types are included.
8. Select **Journal Type** from the list, or select all.
9. If Detail mode: **Summarize all transactions prior to [date] into a balance forward line?**
   - `Y` — prior transactions shown as a lump-sum beginning balance, detail shown for subsequent dates.
   - `N` — detail for all dates within range, no beginning balance brought forward (faster if beginning balance is not needed).

---

## GL-F — Print Financial Statements

*Source: [gl-f_print_financial_statements.htm](../../../samples/chm/extracted/gl-f_print_financial_statements.htm)*

**Purpose.** Prints standard financial statements (Income Statement, Balance Sheet, or Cash Flow / Changes in Financial Position) using the format defined in AM-E Format Standard Financial Statements. Up to four comparative columns can be included. Custom-formatted statements (defined in AM-I) are printed from GL-N instead.

### Statement Types

| Type | Description |
|---|---|
| **Income Statement** | Profit and Loss. Requires beginning and ending month (fiscal period numbers). Supports percentage column. |
| **Balance Sheet** | Asset/Liability/Equity snapshot. Requires a single end-of-month period number. |
| **Cash Flow** | Changes in Financial Position. Uses the Non-Cash flag on GL accounts (see GL-A) to add back non-cash expenses to net income. Requires beginning and ending month. |

If multiple companies have been consolidated using AM-G Consolidate Financials, you are offered the option of printing a consolidated statement.

### Column Fields (up to four columns)

| Field | Description |
|---|---|
| **Which Amounts** | `C` = Current Year, `B` = Budget, `1`–`6` = Prior years 1 through 6. Column 3 also offers `D` = Subtract Col 1 from Col 2 (variance column). |
| **Beg Month** | First fiscal period to include (Income Statement and Cash Flow only). |
| **End Month** | Last fiscal period to include (Income Statement and Cash Flow only). |
| **Print as of end of this Month** | Single period for Balance Sheet — balances as of the last day of that month. |
| **Print %?** | `Y` = print percentages to the right of each account amount (Income Statement only). Note: percentage columns increase report width and may limit the number of columns available. |

### Other Print Options

| Field | Description |
|---|---|
| **Beg Dept Code / End Dept Code** | Limit the report to a range of GL department codes. Leave blank for all departments. |
| **Print Department Detail** | `Y` = show individual department amounts plus account total. `N` = account totals only. |
| **Print Account Codes?** | `Y` = print GL account codes alongside descriptions. `N` = descriptions only. |
| **Print Amounts That are Zero?** | `N` = exclude accounts with no activity in the specified range. `Y` = include all. |

### General Program Operation

1. Choose statement type from the opening window.
2. If multi-company consolidated records exist, choose whether to print consolidated.
3. For each column (up to four), select **Which Amounts**, enter the period range, and set percentage flag (Income Statement).
4. When finished with columns, press Esc/Exit at the **Which Amounts** window to advance to the right-side options.
5. Enter department range, print options, and whether to show account codes.
6. On the second screen, customize the column headings (two lines per heading). Use the left column if percentages are printing; use the right column otherwise.
7. Column 3's **D** option (difference between Col 1 and Col 2) is valuable for current vs. budget or this year vs. last year comparisons.

---

## GL-G — Print GL Code and Description

*Source: [gl-g_print_gl_code_and_description.htm](../../../samples/chm/extracted/gl-g_print_gl_code_and_description.htm)*

**Purpose.** Prints a simple reference list of GL account codes, departments, account types, and descriptions. Useful as a quick-reference lookup sheet or for verifying account setup.

### General Program Operation

Enter from/thru GL account codes and from/thru GL departments to limit the report. If no limits are entered, all account codes, departments, and descriptions are printed. The account type letter (`I` = Income, `E` = Expense, `O` = Owner's Equity, `A` = Asset, `L` = Liability) prints alongside each account.

---

## GL-H — Print Chart of Accounts

*Source: [gl-h_print_chart_of_accounts.htm](../../../samples/chm/extracted/gl-h_print_chart_of_accounts.htm)*

**Purpose.** Prints GL accounts with their monthly dollar amounts. Can include any combination of current year, budget, and up to six prior years of monthly figures. More detailed than GL-G.

### General Program Operation

1. Enter a range of GL account codes and GL departments.
2. Select which monthly amount types to print by entering `Y` in the appropriate fields: Current, Budget, 1 Year Past through 6 Years Past.
3. If no limits are entered, all accounts are printed.

Monthly figures for each account are printed for each amount type selected.

---

## GL-I — Print Check Register

*Source: [gl-i_print_check_register.htm](../../../samples/chm/extracted/gl-i_print_check_register.htm)*

**Purpose.** Prints a copy of all checks and deposits for a specified period and bank account. Most commonly used to prepare for bank statement reconciliation — the printout is compared to the bank statement before running GL-J Reconcile Check Register.

### General Program Operation

1. Enter from/thru **check number** range and from/thru **date** range (optional filters).
2. Select the **Bank Account to Print**.
3. Choose which items to include: **Uncleared Checks Only**, **Cleared Checks Only**, or **Both Types**.
4. Choose **sort order**: by Check Number or by Check Date.
5. Choose transaction type to print: **Checks Only**, **Deposits Only**, or **All Types**.

> **Note:** All transactions that add to the account balance are treated as Deposits (including voided checks); anything that subtracts is treated as a Check.

> **Reconciliation tip:** If you select Uncleared Only, all check numbers and dates, and All Types, the resulting beginning balance should match your last reconciled bank statement ending balance, and the ending balance should match the GL cash account balance visible in GL-A — provided there are no unposted transactions in GL-O for that account.

---

## GL-J — Reconcile Check Register

*Source: [gl-j_reconcile_check_register.htm](../../../samples/chm/extracted/gl-j_reconcile_check_register.htm)*

**Purpose.** The primary bank reconciliation tool. Compares the EvoERP check register to the bank statement by tagging cleared items. Also supports marking cleared items back to uncleared (if not yet archived), and archiving cleared items from the active register. Integrated shortcut buttons launch GL-B, AP-B, or AR-C directly so entries discovered during reconciliation can be posted without exiting.

### Opening Screen

1. Select the **Bank Account** to reconcile.
2. Select **Task to Perform**:
   - **Reconcile to bank statement** — tag items as cleared.
   - **Mark cleared items as uncleared** — reverse a prior clearing.
   - **Archive cleared items** — remove cleared items from the active check register.
3. Optionally filter the list by from/thru date ranges and item numbers (check and deposit numbers).

### Tagging Items

- Enter the **Ending Bank Balance** from your bank statement.
- Optionally change the **Sort Order** from the drop-down (three options available).
- Tag individual items by **double-clicking** or highlighting and clicking **Tag One** (checkmark appears in the Tag column).
- **Tag Group** — tags a group by date range or deposit number; the program reports how many items will be tagged and the total amount. Confirm if it matches the bank statement deposit amount.
- **Tag All** — tags every item on the list.
- **Report** button — prints a report of currently tagged items at any point.
- Running totals display for **Tagged Deposits**, **Tagged Checks**, **Ending Book Balance**, and **Difference to Balance**. When **Difference to Balance** reaches zero, the account is fully reconciled.

### Processing Tagged Items

Click **Save**. Three choices are presented:

1. **Save status for further editing** — saves current tag state; return to complete reconciliation later.
2. **Reconciliation is complete** — prompts for effective date, then clears all tagged items. An optional reconciliation report lists reconciled items, beginning balance, cleared checks and deposits totals, ending balance, bank ending balance, and difference.
3. **Cancel** — discards all changes made in this session.

Once items are cleared, the book bank balance in AD-B Checking Accounts Defaults is updated and items are marked cleared. The **Opening Book Balance** will reflect the new amount on the next reconciliation or check register print.

Cleared items can later be archived by re-entering the program and choosing **Archive cleared items**. If an item was accidentally cleared, it can be uncleared by re-entering the program and choosing **Mark cleared items as uncleared** (only available before archiving).

---

## GL-K — Transfer Bank Account Funds

*Source: [gl-k_transfer_bank_account_funds.htm](../../../samples/chm/extracted/gl-k_transfer_bank_account_funds.htm)*

**Purpose.** Records transfers between two internal checking accounts (e.g., general operating account to payroll account). A completed transfer posts to the Other Journal and to the GL transaction file, and creates both a deposit record and a withdrawal record in the check register for each account.

### Multi-Currency Processing

If multi-currency is enabled (IM-A International Configuration), bank accounts can be held in foreign currencies. GL-K handles base-to-source, source-to-base, and source-to-source currency transfers using current exchange rates from IM-C. The effective exchange rate can be overridden on the transfer entry screen. GL posting remains in source currency; any difference between currency amounts posts as an offsetting entry to the **F/E Gain/Loss-Trxns** account.

### General Program Operation

1. Enter the **Date of Funds Transfer**.
2. Select the **From Bank Account** from the menu.
3. Select the **To Bank Account** from the menu.
4. The **Beginning Balance** for both accounts is displayed (reflects the GL cash account balance; unposted transactions in GL-O are not included).
5. Enter the **Amount of Funds to Transfer**.
6. Optionally edit the **transaction description**.
7. Press Enter through the last field; answer `Y` to save and post the transfer.

---

## GL-L — Credit Card Reconciliation

*Source: [gl-l_reconcile_credit_card_sta.htm](../../../samples/chm/extracted/gl-l_reconcile_credit_card_sta.htm)*

**Purpose.** Enters and reconciles credit card charges against the credit card statement. Credit card accounts must be defined in AD-B Checking Accounts Defaults as type `CC` and assigned to a liability GL account. A vendor can be assigned to represent who the credit card bill is paid to.

### Initial Screen

- Select the **credit card account** from the list.
- Enter the **date range** of the statement being reconciled.

### Editing Screen

- The **top portion** displays any transactions already posted to the selected credit card within the date range (e.g., entries made via AP-C as COD payments, or from prior sessions of this program). These are reference-only — they are already included in the statement total and should not be duplicated.
- The **lower portion** is where new charges are added or imported. Required fields: **date**, **amount**, **GL Account**. Optional: **vendor code** (if entered, posted charges appear in AP Payables history as a manual check; if no vendor code, posted as a Cash Disbursement entry).

### Importing Data

Credit card statement data can be imported if a downloadable file is available from the card provider. Required import fields are date and amount; a description field is also strongly recommended to identify charges and assign the correct GL Account.

### Save Button Options

1. **Save Status for further editing** — saves entries in a temporary file for later editing.
2. **Post** — generates Cash Disbursement entries for charges without a vendor code, and AP Manual check entries for charges with a vendor code. After posting, the credit card bill should be entered as a voucher in AP-B Enter Vouchers (posting to the liability GL account assigned to the card in AD-B). The resulting liability account balance is then reconciled to zero using GL-J Reconcile Check Register.
3. **Exit without saving** — deletes any new entries made in this session.

---

## GL-N — Print Custom Financial Statements

*Source: [gl-n_print_custom_financial_statements.htm](../../../samples/chm/extracted/gl-n_print_custom_financial_statements.htm)*

**Purpose.** Prints user-defined financial statement formats that were created in AM-I Format Custom Financial Statements. Complements GL-F, which handles the three standard statement types. Supports consolidated output if AM-G Consolidate Financials has been run.

### General Program Operation

1. Enter the custom statement format name, or press F2 / click Lookup to choose from the list.
2. Operation is similar to GL-F Print Financial Statements — refer to that section for column, period, and option details.

**Important difference from GL-F:** Because these are user-defined formats, the program does not know whether the format represents a Balance Sheet or an Income Statement, so it always asks for a range of months and whether to include a beginning balance. For a Balance Sheet-type custom statement:
- Answer `Y` to Beginning Balance.
- Make sure the month range covers the entire year-to-date, not just the ending month.

---

## GL-O — Print/Post General Ledger Batches

*Source: [gl-o_print_post_general_ledger_baches.htm](../../../samples/chm/extracted/gl-o_print_post_general_ledger_baches.htm)*

**Purpose.** The central posting gateway for the entire GL. Every program in EvoERP that generates GL entries first posts them to the temporary file **BKGLTEMP**. GL-O reviews the contents of BKGLTEMP in batches, verifies balance and valid account codes, and then posts them permanently to the General Ledger. This program is the mandatory final step in the GL posting workflow — no amounts appear in the permanent GL until GL-O is run.

> **Recommendation:** Run GL-O daily. Daily batches are far easier to review and correct than accumulated backlogs.

### Batch Categories

Batches are organized by these journal types:
`Cash Receipts` | `Cash Disbursements` | `Sales` | `Purchases` | `Payroll` | `Other` | `Work Orders` | `General Journal` | `Year End`

### Batch Status Window

The lower half of the selection screen has two panels:

- **Available** — shows total marked records and total debits/credits per batch type. Indicates whether each type is in balance before selection.
- **Selected** — shows status of batches chosen for printing or posting. **Stat** (status) codes:
  - `O` — Out of Balance (cannot post)
  - `C` — Clearing Account Entries (entries posted to the clearing account due to missing GL account defaults)
  - `B` — Bad GL Account Entries (invalid account codes)

A batch cannot be posted until it is fully in balance and all GL account codes are valid. Bad entries can be corrected via GL-P Edit General Ledger Batch Entries.

### Out-of-Balance Handling

Each time GL-O starts, it marks all current BKGLTEMP entries to distinguish them from new entries arriving while the program runs. If a transaction was being saved at the exact moment of marking, part may be marked and part not, throwing the marked group out of balance.

- **Small number of transactions out of balance (10 or under):** Almost certainly a race condition. Answer `Y` to "Do you wish to exclude these items and post them later?" The few transactions at the end of the file are unmarked and will be included in the next batch.
- **Large number of transactions out of balance:** Indicates a genuine problem in earlier transactions. Answer `N` to work with the entire batch and locate the problem.
- Use the **Out of Bal Report** button to identify out-of-balance items.

### General Program Operation

1. On startup, the program marks BKGLTEMP entries ("Preparing unposted transactions").
2. If marked entries are in balance, the main screen opens.
3. Select batch types: enter `S` in the **(S)elect or (D)eselect** field, optionally enter from/thru **Posting Date** or **Date Entered** ranges, then check **For All Batch Types?** or select individual batch types.
4. Selected batches appear in the **Selected** panel. If no status codes appear in the **Stat** column, click **Post** (Alt-O) to permanently post all selected transactions to the GL.
5. To view or print before posting, click **Print** (Alt-P).
6. If status codes appear, print for review, correct via GL-P, then re-select and re-attempt posting.
7. To deselect specific batch types: enter `D` in the select/deselect field, enter `N` for all batch types except those being deselected (which get `Y`).
8. On exit, you are asked to confirm ending the session. Confirming clears all selections; the next session starts the marking process over.

### Fiscal Year End Behavior

Before the first day of a new fiscal year, run **AM-B Fiscal Year End Routine** to move current-year balances one year back, open balances for the new year, update beginning balances in all Balance Sheet accounts, clear beginning balances in Income and Expense accounts, and create Retained Earnings year-end entries.

Until AM-B is run, new-fiscal-year transactions can be entered throughout the system but cannot be posted via GL-O. GL-O will display: *"The program has detected XXXX records with transaction dates beyond the current fiscal year and cannot post these until you run AM-B."*

> **Important:** AM-B does NOT close the year; it should be run on the first day of the new fiscal year. Do not wait for prior-year accounting entries to be finalized.

---

## GL-P — Edit General Ledger Batch Entries

*Source: [gl-p_edit_general_ledger_batch_entries.htm](../../../samples/chm/extracted/gl-p_edit_general_ledger_batch_entries.htm)*

**Purpose.** Corrects errors in the BKGLTEMP temporary batch file before entries are permanently posted via GL-O. Most commonly used to fix entries that landed in the **Clearing Account** (the system posts there when a required GL account default is not yet configured) by changing the account code to the correct one.

> **Warning:** Be very careful when changing dollar amounts. Most entries are supported by subsidiary reports in AR, AP, inventory, and job costing. It is better to make a reversing entry in the original module than to change dollar amounts here. The program warns before allowing amount changes.

### General Program Operation

**Finding an entry:**
- Click **Lookup** on the GL Account Code field. The list of unposted transactions appears sorted by GL account; sort order can be changed.
- Highlight the desired entry, press Enter, double-click, or click **Select**.

**Editable fields:**

| Field | Notes |
|---|---|
| **GL Account Code** | The primary correction — change from Clearing Account to the correct account. |
| **Department** | Editable. |
| **Post Date** | Editable. |
| **Code** | Customer, vendor, salesperson, or item number codes. Cursor skips this field by default; access with mouse if needed. |
| **Number** | Sales order, invoice, purchase order, or work order number. Cursor skips by default. |
| **Description** | General description. Cursor skips by default. |
| **Debit / Credit** | Selected from a pop-up window. |
| **Amount** | Editable but triggers a warning about subsidiary file impact. Call IS Tech Support if uncertain. |
| **Batch Type** | Determines which batch category the entry belongs to. Selected from a pop-up window. |
| **Entry Date** | The calendar date the entry was created (distinct from Post Date). |

**Deleting a record:** Select the entry as for editing, then press **Delete** on the editing screen. The same warning about subsidiary file consequences is displayed.

**Creating a new entry:** Possible but extremely rare — only warranted if a transaction is missing one side due to equipment failure or a unique system anomaly.

---

## GL-Q — Enter Payroll Checks

*Source: [gl-q_enter_payroll_checks.htm](../../../samples/chm/extracted/gl-q_enter_payroll_checks.htm)*

**Purpose.** An IS Tech Support add-on (demo copy limited to 5 executions for evaluation). Designed for companies that use an outside payroll service. Instead of entering each payroll check as a separate transaction in GL-B, this program allows all payroll check details to be entered on a single screen, generating individual check register entries for each check.

### General Program Operation

Workflow when payroll is processed by an outside service:

1. In GL-B, post the total net check amount of all non-direct-deposit checks to a **payroll clearing GL account**.
2. Run GL-Q. Enter:
   - **Bank Account** the checks are drawn on.
   - **Posting date** of the payroll.
   - **Payroll clearing GL Account**.
   - Optional **reference** to appear on transaction detail.
3. Enter each **check number** and **net check amount**. A running total is maintained for comparison against the payroll clearing account credit from step 1.
4. When all checks are entered, click **Post**. A separate GL entry posts for each check, clearing the payroll clearing account balance, and a corresponding check register entry is created for each check to support bank statement reconciliation.

---

## GL-R — Business Status

*Source: [gl-r_business_status.htm](../../../samples/chm/extracted/gl-r_business_status.htm)*

**Purpose.** An executive dashboard providing a summary view of the company's current financial position. Recalculates current period data from transaction detail each time it loads.

### General Program Operation

**Current period screen shows:**
- Open **Accounts Receivable** balance
- **Customer Deposits** balance
- Open **Accounts Payable** balance
- **Cash** balance (which checking accounts are included is controlled by a setting in AD-B Checking Accounts Defaults)
- Open **Sales Orders** and **Purchase Orders** balances
- **WIP** (Work in Progress) and **Inventory** balances
- **Billings** and **Booked Orders** for the current period (defined by the Period Start and End dates in the lower left of the screen)
- **EOM Projected Cash** — projected end-of-month cash balance calculated as:
  - Current cash balance
  - Minus: AP payables where the Scheduled Payment date (or due date per terms if scheduled date is blank) falls before month end
  - Plus: AR receivables based on invoice date and Customer Average Days to Pay (or invoice due date per terms for new customers)
  - Note: payroll is not factored in

**Navigation and tools:**
- Click any **label** on the screen to drill into the detail behind that balance.
- **Prior periods** can be calculated via Tools → Calculate prior periods.
- Once calculated, prior periods can be viewed by clicking **Previous** or graphed via Tools → Graphs (specify data type and number of periods).

---

## GL-S — View GL Journal Notes

*Source: [gl-s_view_journal_notes.htm](../../../samples/chm/extracted/gl-s_view_journal_notes.htm)*

**Purpose.** Provides a read-only view of notes attached to GL-B General Journal transactions. Notes are entered in GL-B using the NOTES button.

### General Program Operation

- Notes are displayed in **Transaction number order** by default; can be resorted by **Code**.
- Click **Print** to produce a printout filtered by transaction number, code, and/or date.
- The **Date** filter applies to the **entry date of the note**, not the journal transaction date.
- Notes designated as **Hidden** will not print even when the print function is used.

---

## Cross-references

GL is the financial backbone — all EvoERP accounting modules converge here:

- **AM — Accounting Maintenance:** AM-C creates and maintains GL accounts; AM-B runs the Fiscal Year End Routine (required before GL-O can post new-year transactions); AM-E formats standard financial statements (used by GL-F); AM-I formats custom financial statements (used by GL-N); AM-G consolidates charts of accounts across companies (consolidated output available in GL-F and GL-N).
- **AD — Accounting Defaults:** AD-A General Ledger Defaults sets the starting GL transaction number and system-wide default accounts; AD-B Checking Accounts Defaults defines bank accounts (referenced by GL-B, GL-I, GL-J, GL-K, GL-L, GL-Q, GL-R) and credit card accounts (GL-L).
- **AR — Accounts Receivable:** AR postings feed the Sales Journal and Cash Receipts Journal (GL-D). DO NOT adjust AR GL account balances in GL-B; use AR vouchers instead.
- **AP — Accounts Payable:** AP postings feed the Purchases Journal and Cash Disbursements Journal (GL-D). DO NOT adjust AP GL account balances in GL-B; use AP vouchers instead.
- **SO — Sales Orders:** Invoice posting (SO-G) generates Cash Receipts Journal entries.
- **PO — Purchase Orders:** PO invoicing generates Purchases Journal entries.
- **WO — Work Orders:** All WO transactions appear in the Work Orders Journal (GL-D).
- **PR — Payroll:** Payroll transactions feed the Payroll Journal (GL-D). Outside-service payroll check entry handled by GL-Q.
- **IN — Inventory:** Inventory value and quantity adjustments appear in the Other Journal (GL-D).
- **IM — International:** Multi-currency exchange rates (IM-C) used by GL-K bank fund transfers.
- **SD — System Defaults:** SD-A Company Defaults controls whether Job Number is optional or required on GL-B entries; SD-R Assign Next Numbers sets the GL transaction numbering sequence (Evo-ERP).
- **SM — System Maintenance:** SM-P-F Enter Jobs maintains the job list referenced by GL-B when Job Number is required.

**Key posting workflow:**
All modules → BKGLTEMP (temporary) → GL-P (correct errors if needed) → GL-O (review and post permanently to GL) → GL-D / GL-E / GL-C (audit reports) → GL-F / GL-N (financial statements).

**Bank reconciliation workflow:**
GL-I (print register) → GL-J (tag and clear items) → GL-J archive when done.

**Credit card reconciliation workflow:**
GL-L (enter/import charges, post) → AP-B (enter monthly CC bill as AP voucher) → GL-J (reconcile liability account to zero).
