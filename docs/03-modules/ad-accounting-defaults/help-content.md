# AD — Accounting Defaults

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Accounting → Accounting Defaults (3 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Accounting Defaults (AD) module is the system-wide configuration hub for all financial posting behavior in EvoERP. It establishes which GL accounts receive postings from every other module, controls which transaction types actually generate GL entries, sets the open posting period boundaries, defines every bank/checking account available to AP, AR, and Payroll, and configures AP-specific operational options. Nothing posts to the General Ledger without flowing through defaults established here. AD must be configured during initial system setup and revisited whenever the chart of accounts, fiscal year, or banking arrangements change.

---

## Contents

- [AD-A — General Ledger Defaults](#ad-a--general-ledger-defaults)
  - [GL Posting Defaults (flags)](#gl-posting-defaults)
  - [Period Date Controls](#period-date-controls)
  - [Accounting/Sales GL Account Codes](#accountingsales-gl-account-codes-tab)
  - [Manufacturing GL Defaults](#manufacturing-gl-defaults-tab)
  - [Payroll GL Defaults](#payroll-gl-defaults-tab)
- [AD-B — Checking Account Defaults](#ad-b--checking-account-defaults)
  - [Set Up Banks fields](#field-descriptions--set-up-banks)
  - [Defaults fields](#field-descriptions--defaults)
- [AD-C — Accounts Payable Defaults](#ad-c--accounts-payable-defaults)
- [Cross-references](#cross-references)

---

## AD-A — General Ledger Defaults

*Source: [ad-a_general_ledger_defaults.htm](../../../samples/chm/extracted/ad-a_general_ledger_defaults.htm)*

**Purpose.** Use this program to enter or change system-wide General Ledger default account codes and to set posting controls. Every GL account code field is mandatory — none may be left blank. If a particular account type is not used, substitute the GL Clearing Account number as a placeholder.

> NOTE: All account codes entered may include a department code. Confine department codes to income and expense accounts. See AM-D Enter General Ledger Departments for details.

---

### GL Posting Defaults

These flags control whether the manufacturing side of the system generates actual GL transactions. Regardless of the flag settings, the manufacturing modules track all transactions internally and reports can serve as supporting documents for manual journal entries. When posting is enabled (`Y`), the GL accounts used are the system defaults defined in this program unless Item Class-level overrides are set in SM-C Enter Item Classes.

| Flag | `Y` behavior | `N` behavior |
|---|---|---|
| **Post COGS transactions?** | SO-G Post Invoices generates a GL entry debiting COGS and crediting Inventory for item cost. AR, Sales, Sales Tax Withheld, Commission Expense, and Freight Out always post regardless of this flag. | COGS/Inventory entries suppressed; other invoice GL postings still occur. |
| **Post PO transactions?** | PO-C Receive Purchase Orders posts Debit Inventory/WIP, Credit PO's Received Not Invoiced. AP-C Enter PO Invoices posts Debit PO's Received Not Invoiced + PO Freight In + PO Sales Tax Expense, Credit Accounts Payable. | No GL entries on PO receipt or PO invoice. |
| **Post Inventory Adjustments?** | IN-C Enter Inventory Adjustments and IN-K Adjust Physical Levels post between Inventory and COGS (debit or credit direction determined by whether inventory increases or decreases). | Adjustment transactions not posted to GL. |
| **Post WO transactions?** | All WIP movements generate GL entries: materials issued debit WIP / credit Inventory; labor debits WIP / credits Absorbed Labor and Overhead accounts; finished production credits WIP / debits Inventory; variances post between WIP and WIP Variance. | No GL entries for Work Order activity. |
| **Permit use of Item Class GLs?** | System default GL accounts for Inventory, COGS, Sales, WIP, and Absorbed Labor/Overhead can be overridden per Item Class and Location in SM-C. | All postings use system defaults regardless of SM-C entries. |

---

### Period Date Controls

| Field | Description |
|---|---|
| **Fiscal Year Date** | Start date of the current fiscal year (e.g., `1/01/01` for calendar year). Set once during initial system setup; automatically updated by AM-B Fiscal Year End Routine. **CAUTION: Never manually re-enter this field after initial setup.** |
| **Open Period Start Date** | First day of the current open period; postings before this date are blocked. To make a backdated entry, temporarily move this date back, post, then restore it. |
| **Open Period End Date** | Last day of the current open period; postings after this date are blocked per the Future Post Date Control setting. |
| **Future Post Date Control (P/G)** | `P` — no transactions later than the Period End Date can be posted from any module. `G` — GL-B Enter/Post General Journal Trxns may post beyond the end date, but transactions from other modules cannot. |
| **Accounting Open Period Start Date** | A separate, finer-grained open period start date that applies only to GL-B, AP-B Enter Vouchers, and AR-C Record Payments, based on the per-program flag settings below. Useful when accounting staff need a different cutoff from the operations cutoff. |
| **Use Open Period Start Date in GL-B** | `Y` — GL-B uses the Accounting Open Period Start Date instead of the overall Open Period Start Date. |
| **Use Open Period Start Date in AR-C** | `Y` — AR-C Record Payments uses the Accounting Open Period Start Date instead of the overall Open Period Start Date. |
| **Use Open Period Start Date in AP-B** | `Y` — AP-B Enter Vouchers uses the Accounting Open Period Start Date instead of the overall Open Period Start Date. |

---

### Accounting/Sales GL Account Codes Tab

| Field | Account Type | Description |
|---|---|---|
| **GL Current Earnings** | Owner's Equity | Holds the net income/loss for the current year when printing a Balance Sheet in GL-F Print Financial Statements or GL-N Print Custom Statements. Always a calculated amount — no actual posted entries exist in the GL transaction file for this account. |
| **GL Retained Earnings** | Owner's Equity | Accumulates prior-year net income/loss. AM-B Fiscal Year End Routine posts closing entries that bring each income/expense account to zero and makes a single net entry to this account. Prior-year income/expense postings also auto-generate a closing entry here. Direct transactions (e.g., dividend/profit payments to owners) may also be posted here. |
| **GL Clearing Account** | Owner's Equity (recommended `99999`) | Safety net: receives any GL posting when the target account code is not found. Without this account a missing code puts the ledger out of balance. Recommended account type `O` (Owner's Equity) and a number at the end of the chart of accounts such as `99999`. Cannot be the same as the Suspended Account for Deleted COA Accounts. |
| **AP Accounts Payable** | Liability | Default GL account for Accounts Payable. |
| **AP Discounts Taken** | Expense or Income | Vendor early-payment discounts are posted here when taken. |
| **AP Deposits** | Asset | Advance payments/deposits made to vendors before invoicing. |
| **AR Accounts Receivable** | Asset | Default GL account for Accounts Receivable. |
| **AR Discounts Taken** | Expense or Income | Customer early-payment discounts offered and taken. |
| **AR Interest Charged** | Income | Interest charged to customers on overdue invoices via AR-D Charge Interest on Invoices. |
| **AR Customer Deposits** | Liability | Prepayments received from customers that will later be applied to invoices. Kept separate from AR so they are not mingled. Entered through AR-N Enter/Print Sales Order Deposits or AR-C Record Payments. |
| **SO Taxable Sales** | Revenue | Default revenue account for taxable customer sales. Overridable at Item Class level in SM-C. |
| **SO Non-taxable Sales** | Revenue | Default revenue account for non-taxable customer sales. Overridable at Item Class level in SM-C. |
| **SO Invoice Freight Out** | Income or Expense | Freight charged to customers on invoices. |
| **SO Sales Tax Withheld** | Liability | Default account for sales tax collected on customer invoices. Can be overridden per tax code in SM-E Enter Tax Codes. |
| **SO Retention** | Asset | Temporary holding account for retention billing. When the original invoice posts, the retention amount is credited here; when the retention sales order later posts, the amount is debited from this account and credited to the AR account. Only needed if using the sales order retention billing feature. |
| **CS Agents Comm Payable** | Liability | When invoices or customer payments are posted with agent commissions, the commission amount is credited here (debit goes to CS Agents Comm Expense). When commissions are transferred to AP via CS-D Transfer Sales Commissions, this account is debited and Accounts Payable is credited. |
| **CS Agents Comm Expense** | Expense | Debited for agent commission amounts when invoices or customer payments are posted. |
| **Misc Cost GL Acct for AP-C** | (varies) | Default GL account suggested when entering miscellaneous costs on a Purchase Order in AP-C Enter Purchase Order Invoices. |
| **Susp Acct for Deleted COA Accounts** | Owner's Equity (recommended `99998`) | Receives orphaned transaction history when UT-K-D Recalc GL Chart of Accounts encounters transactions for accounts that no longer exist in the chart. Must differ from the GL Clearing Account. Background: prior to the 2/7/07 update, accounts with activity older than 2 years could be deleted; the 6-year history expansion made this field necessary. |

---

### Manufacturing GL Defaults Tab

| Field | Account Type | Description |
|---|---|---|
| **IN Inventory (Asset)** | Asset | Default account for all on-hand inventory value. Overridable at Item Class level in SM-C. |
| **IN Inventory Cost of Goods Sold** | Expense | Posted when invoices are processed in SO-G Post Invoices or when inventory adjustments are made via IN-C or IN-K. Overridable at Item Class level in SM-C. |
| **IN Absorbed Freight In** | Expense | When the `Freight Pct` field in IN-B Enter Inventory is used to absorb inbound freight into inventory cost, the credit side posts here (debit goes to the item's Asset account). Compare month-end balance against the actual Freight In account to evaluate the accuracy of Freight Pct settings. |
| **PO's Received Not Invoiced** | Liability | Clearing/holding account for POs received but not yet vendor-invoiced. PO-C Receive POs credits this account (debit to asset/expense); AP-C Enter PO Invoices debits this account (credit to AP). Normally located adjacent to the AP account in the chart of accounts. |
| **PO Freight In** | Expense | Freight charges added by vendors to their invoices for shipping to the company. |
| **PO Tax Expense** | Expense | Sales or use tax charged on purchase orders. |
| **PO Purchase Price Variance** | Expense | Under Standard Costing, any difference between the standard cost and actual PO price posts here. |
| **WO Extra Costs** | Expense (accrual) | Credit-side account when extra costs are entered in WO-H Enter Misc/Extra Costs; offset debit posts to the WIP account of the item being manufactured. Washed out when the corresponding vendor invoice is received. Extra costs apply to the work order as a whole. |
| **WO Miscellaneous Costs** | Expense (accrual) | Same mechanics as WO Extra Costs, but miscellaneous costs are tied to specific routing sequences rather than the whole work order. |
| **WO Absorbed Labor** | Expense | Labor costs are credited here and debited to WIP as transactions are entered via WO-F Enter Labor, DC-H Post Labor Transactions, WO-N Post Labor Batches, WO-G Issue Materials (Type L parts), or WO-I Enter Finished Production (backflushing). Overridable at Item Class level in SM-C. |
| **WO Absorbed Fixed Overhead** | Expense | Fixed overhead costs credited here and debited to WIP through the same labor-entry programs. Overridable at Item Class level in SM-C. |
| **WO Absorbed Variable Overhead** | Expense | Variable overhead costs credited here and debited to WIP through the same labor-entry programs. Overridable at Item Class level in SM-C. |
| **WO WIP Inventory** | Asset | GL asset account for Work In Process inventory. Overridable at Item Class level in SM-C. |
| **WO WIP Variance** | Expense (adj. to COGS) | Receives residual WIP cost when a Work Order is closed in WO-I or WO-J Close/Cancel Work Orders and actual costs in do not equal finished production out. Also receives cost differences when AP-C makes cost changes to a work order already closed. Normally adjacent to the COGS account. |

---

### Payroll GL Defaults Tab

| Field | Account Type | Description |
|---|---|---|
| **PR Vac/Sick Accrual (Liability)** | Liability | Credited when vacation or sick time is accrued; debited when vacation or sick time is taken in PR-D Print Payroll Checks. If left blank, accrual posting does not occur and the employee's assigned expense account is debited directly when time is taken. |

---

## AD-B — Checking Account Defaults

*Source: [ad-b_checking_account_defaults.htm](../../../samples/chm/extracted/ad-b_checking_account_defaults.htm)*

**Purpose.** Use this program to define and manage all checking accounts used by the system. Up to 99 accounts may be created. Accounts are designated as defaults for Accounts Receivable, Accounts Payable, and Payroll. The term "checking account" here is broad: any account through which money is collected (AR), disbursed (AP, Payroll), or for which a check register is desired qualifies — including petty cash, salesperson credit cards, and pending credit card charge accounts.

The program has two areas: a **Defaults** screen (shown on first open) and a **Set Up Banks** screen (accessed via a button).

**General operation:** Define accounts in Set Up Banks first, then designate defaults for each module.

---

### Field Descriptions — Set Up Banks

| Field | Description |
|---|---|
| **Default Bank Account Numbers (1-99)** | Auto-incremented internal counter. Links cash transaction records in AP, AR, and GL to the correct account. If an account is closed, mark it Inactive rather than deleting or reusing the number. Numbers must never be reused — reuse corrupts check register and payment history reports. |
| **Account Name** | Descriptive label for the account; the GL account description is suggested but may be overridden. This name appears in pop-up account-selection windows throughout the system. |
| **Account Number** | The actual account number at the bank. Required only for automated ACH payments. |
| **Routing Number** | The bank's ABA routing number. Required only for automated ACH payments. |
| **GL Account-Dept** | The GL account code for this checking account. Generally an asset account; may be a liability if tracking Accounts Payable credit card payments. |
| **Balance** | Period-ending balance of the account. Updated by GL-J Reconcile Check Register; should match the most recently reconciled bank statement balance. |
| **Type** | Account type: checking, savings, petty cash, or credit card (`CC`). An account must be type `CC` to be reconciled using GL-L Credit Card Reconciliation. |
| **Next Ck #** | Next available check number. May be set to a starting value greater than 1 during initial setup; incremented automatically on each check print. |
| **CC Vendor** | The vendor associated with a Credit Card type account — the entity that is paid to settle the credit card balance. |
| **User Defined Sort #** | Controls the display order of accounts in selection pop-ups. Use this field (not the Bank Account Number) to reorder accounts after setup has begun, because the Bank Account Number is stored in check register and payment history records and must not change. |
| **Include AP (Y/N)** | `Y` — account is available for selection in Accounts Payable screens. |
| **Default AP RTM** | Override check print format (RTM template file) for AP checks from this account. Blank means use the system-default AP format. |
| **Include AR (Y/N)** | `Y` — account is available for selection in Accounts Receivable screens. |
| **Include PR (Y/N)** | `Y` — account is available for selection in Payroll screens. |
| **Default PR RTM** | Override check print format for Payroll checks from this account. Blank means use the system-default Payroll format. |
| **Business Status Cash Balance (Y/N)** | `Y` — this account's balance is included in the Business Status cash balance display. |
| **Active (Y/N)** | `N` — account is inactive: hidden from all selection screens but retained for historical reference. Closed accounts should be set inactive rather than deleted. |
| **Currency** | If Multi-Currency is enabled, specify the currency denomination for this account. |

---

### Field Descriptions — Defaults

| Field | Description |
|---|---|
| **Default Bank Account Numbers (1-99)** | Designates the default account number (the internal 1-99 counter, not the User Defined Sort number) for each module: AP, AR, and Payroll. |
| **Default Print Format (AP & PR)** | Sets the default check-printing RTM template for AP and Payroll. A bank-account-specific format entered on the Set Up Banks screen overrides this selection. |

---

## AD-C — Accounts Payable Defaults

*Source: [ad-c_accounts_payable_defaults.htm](../../../samples/chm/extracted/ad-c_accounts_payable_defaults.htm)*

**Purpose.** Controls operational behavior of the Accounts Payable module — check printing options, voucher entry behavior, vendor list display, aging period definitions, and AP-H ACH integration.

| Field | Description |
|---|---|
| **Attach Notes from PAPA** | `Y` or blank — customer notes entered in AP-A Enter Vendors are pulled into sales orders via the Purchase Order feature. `N` — feature disabled. |
| **Include Beg/End Balance in AP-G** | `Y` (default) — AP-G Print Pro Forma Check Register includes the checking account beginning and ending balances. `N` — register lists only the checks to be paid. |
| **Remove Frgt & Tax from Discount (Y/N)** | `Y` — the calculated early-payment terms discount in AP-E Print Vouchers/Invoices Due by Date and AP-H Print Checks excludes freight and tax amounts from invoices entered in AP-C Enter Purchase Order Invoices. `N` — discount calculated on the full invoice amount including freight and tax. |
| **Default Search Key in AP-A Opening List** | Controls the sort/index order of vendors on the AP-A opening list. Use the Lookup button to choose the desired index. |
| **Print report for more than 13 invoices per check?** | `Y` — when a vendor has more than 13 invoices being paid on one check, AP-H prints a separate report listing the invoices at the end of the check run instead of voiding intermediate checks to list them. `N` — standard void-and-reprint behavior. |
| **Use Inv Date as Post Date in AP-B** | `Y` — AP-B Enter Vouchers defaults the GL Post Date field to the Invoice Date. `N` or blank — today's date is suggested as the GL Post Date. |
| **Print Check in English/Spanish (E/S)** | `E` or blank — check amount written in English text. `S` — check amount written in Spanish text. |
| **Use Job or Customer Code in AP-B (J/C)** | `J` — AP-B Enter Vouchers allows associating a voucher with a Job Number (as defined in SM-P-F Enter Jobs). `C` — vouchers can be associated with a Customer code. |
| **Use Open Period Start Date in AP-B** | `Y` — AP-B uses the Accounting Open Period Start Date (set in AD-A) rather than the overall Open Period Start Date. Mirrors the same flag in AD-A; shown here for AP-specific context. |
| **Prevent Creating new Vendors in AP-B** | `Y` — AP-B Enter Vouchers cannot create vendors on the fly; a vendor must already exist in AP-A. `N` or blank — on-the-fly vendor creation is permitted. |
| **AP-H Export Program Name** | Name of a custom TAS Pro program for generating an ACH payment file. When populated, AP-H Print Checks calls this program after check printing to produce the ACH file for bank submission. |
| **Aging Periods (Periods 1-5)** | Up to five aging bucket definitions (in days) used by AP-I Print Aging. Period 1 should always be `0` days to capture all invoices. Example: `0 / 30 / 60 / 90 / 120`. These defaults can be changed on-the-fly within AP-I. |

---

## Cross-references

- **AD-A** sets the foundational GL account codes consumed by every posting module. Changes here affect AR, AP, SO, PO, IN, WO, GL, AM, CS, and PR simultaneously.
- **SM-C Enter Item Classes** can override the system-default Inventory, COGS, Sales, WIP, Absorbed Labor, and Overhead accounts on a per-Item-Class-and-Location basis when **Permit use of Item Class GLs** is `Y` in AD-A.
- **SM-E Enter Tax Codes** can override the **SO Sales Tax Withheld** account on a per-tax-code basis.
- **AM-B Fiscal Year End Routine** automatically updates the **Fiscal Year Date** in AD-A and posts closing entries to **GL Retained Earnings**.
- **AD-B** checking account definitions are referenced by AP-H Print Checks, AP-E Print Vouchers/Invoices Due by Date, AR-C Record Payments, AR-N Enter/Print Sales Order Deposits, and GL-J Reconcile Check Register.
- **AD-C** AP defaults are consumed by AP-B Enter Vouchers, AP-C Enter PO Invoices, AP-E, AP-G Print Pro Forma Check Register, AP-H Print Checks, and AP-I Print Aging.
- Related module documentation: [GL](../../gl-general-ledger/), [AP](../../ap-accounts-payable/), [AR](../../ar-accounts-receivable/), [AM](../../am-accounting-management/).
