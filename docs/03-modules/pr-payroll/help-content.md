# PR — Payroll

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Payroll (35 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Payroll module is designed to speed up and simplify payroll tasks and to make sure that payroll information is properly posted to the appropriate journals. You can enter new employee records, change existing records, enter standard deductions or user-defined deductions, print payroll checks, void payroll checks, and pay withholding liability through Accounts Payable. You can maintain separate payroll divisions with different payroll defaults. A history of previous payrolls is maintained. If you are using the Work Orders or Data Collection module, you can collect direct labor hours through WO-F Enter Labor, Data Collection, or WO-M Batch Labor Entry and post those hours into Payroll (through WO-L-E Print/Post Labor to Payroll) to avoid double entry.

---

## Contents

### Core Programs

- [PR-A — Enter Employees](#pr-a--enter-employees)
- [PR-B — Enter Pay Info](#pr-b--enter-pay-info)
- [PR-C — Print Payroll Register](#pr-c--print-payroll-register)
- [PR-D — Print Payroll Checks](#pr-d--print-payroll-checks)
- [PR-E — Print Employee Info](#pr-e--print-employee-info)
- [PR-F — Maintain Tax Tables](#pr-f--maintain-tax-tables)
- [PR-G — Void Payroll Checks](#pr-g--void-payroll-checks)
- [PR-H — Transfer Liabilities to AP](#pr-h--transfer-liabilities-to-ap)
- [PR-I — Print Pay History](#pr-i--print-pay-history)
- [PR-J — Enter Time Cards](#pr-j--enter-time-cards)
- [PR-K — Print/Post Time Cards](#pr-k--printpost-time-cards)
- [PR-M — Payroll Division Defaults](#pr-m--payroll-division-defaults)
- [PR-N — Purge Payroll History](#pr-n--purge-payroll-history)
- [PR-O — Year End Routine](#pr-o--year-end-routine)
- [PR-P — Enter Raise Dates](#pr-p--enter-raise-dates)
- [PR-Q — Enter Review Dates](#pr-q--enter-review-dates)
- [PR-R — Payroll Defaults](#pr-r--payroll-defaults)
- [PR-S — Assign Password to Employee](#pr-s--assign-password-to-employee)

### Quarterly and Annual Reports

- [PR-L-A — Print Quarterly Info](#pr-l-a--print-quarterly-info)
- [PR-L-B — Print QTD Earnings Register](#pr-l-b--print-qtd-earnings-register)
- [PR-L-C — Print QTD Taxable Earnings](#pr-l-c--print-qtd-taxable-earnings)
- [PR-L-D — Print Detail Earnings Ledger](#pr-l-d--print-detail-earnings-ledger)
- [PR-L-E — Print Detail Deductions Ledger](#pr-l-e--print-detail-deductions-ledger)
- [PR-L-F — Print Subject to Report](#pr-l-f--print-subject-to-report)
- [PR-L-G — Print 941 and Schedule B Reports](#pr-l-g--print-941-and-schedule-b-reports)
- [PR-L-H — Print 940 Forms](#pr-l-h--print-940-forms)
- [PR-L-I — Print W-2 Forms](#pr-l-i--print-w-2-forms)
- [PR-L-K — Print Payroll Hours](#pr-l-k--print-payroll-hours)
- [PR-L-L — Print 941B Forms](#pr-l-l--print-941b-forms)
- [PR-L-M — Print Employer Contributions](#pr-l-m--print-employer-contributions)
- [PR-L-N — Print Payroll Wages Detail](#pr-l-n--print-payroll-wages-detail)
- [PR-L-P — Print Employee Raises](#pr-l-p--print-employee-raises)
- [PR-L-Q — Print Employee Reviews](#pr-l-q--print-employee-reviews)

### Reference

- [Payroll Tax Calculation by State](#payroll-tax-calculation-by-state)

---

## Core Programs

---

## PR-A — Enter Employees

*Source: [pr-a_enter_employees.htm](../../../samples/chm/extracted/pr-a_enter_employees.htm)*

**Purpose.** Use this program to add new employee records or change current ones. You can also indicate which employees have been terminated so they are excluded from PR-B Enter Pay Info and various reports. Note: the Employee file for Payroll and the Employee file for Labor Reporting in Work Orders are not the same file. If a new employee has been added in SM-G Enter Employees but not entered into the payroll file, the program will advise you when starting so you can enter the employee into payroll and maintain integrity of employee numbers between the two files.

### Main Screen Fields

**Employee No** — The employee number. You must assign this number; it is not assigned automatically. 4-digit numeric field. If implementing commissions for salespeople, this number is also used as the salesperson number.

**Division** — The employee payroll division (4-character alphanumeric). If you have groups of employees requiring different default information, you can set up multiple divisions. Examples: employees in different states with different deduction requirements; employees in GL departments used as profit/cost centers; different pay periods (biweekly vs. weekly). Payroll divisions are processed one-by-one in PR-B. Before using PR-A you must set up at least one division using PR-M Payroll Defaults — every employee must be assigned to a payroll division.

**Shift** — The shift number this employee is assigned to. Used by the Data Collection module to determine which breaks and buffers apply.

**Terminated?** — Enter `Y` if this employee has been terminated. Excludes the employee from PR-B Enter Pay Info.

**Termination Date** — The date a terminated employee was terminated.

**Allow Clock Multi-Jobs** — For employees posting Work Order labor using Data Collection: indicates whether simultaneous clocking into more than one Work Order is allowed.

**Name: First / MI** — Employee's first name and middle initial. 25-character alphanumeric.

**Name: Last** — Employee's last name. 25-character alphanumeric.

**Address: Street** — Employee's street address. 30-character alphanumeric.

**Address: City/St/Zip** — Employee's city, state, and zip code. 25-character alphanumeric.

**Telephone - Home** — Employee's telephone number. 15-character alphanumeric.

**Telephone - Mobile** — Employee's cell phone number. 15-character alphanumeric.

**Telephone - SOS** — Employee's emergency contact number. 15-character alphanumeric.

**Contact** — Name of the employee's emergency contact person.

**Social Security No** — Employee's social security number. 11-character alphanumeric.

**Birth Date** — Employee's birth date.

**Start Date** — Date the employee started work.

**Benefits Date** — Date the employee becomes eligible to receive benefits such as vacation and sick pay.

**Pay Type [H/S/C]** — `H` = Hourly, `S` = Salaried, `C` = Commissioned.

**Regular Payrate** — Regular pay amount per hour (if hourly) or per pay period (if salaried).

**Overtime Payrate** — Overtime payrate; same criterion as regular payrate (hourly or by pay period).

**Holiday Payrate** — Payrate for holiday pay: hourly amount if hourly employee, or per-period amount if salaried.

**Last Paid** — Date of the last payroll check for this employee.

**Direct Deposit** — Enter `Y` if the employee is Direct Deposit and should receive a printed stub instead of an actual check.

**Marital Status [S/M/H]** — `M` = Married, `S` = Single, `H` = Single Head of Household.

**Federal Exemptions** — Number of federal income tax exemptions claimed on the employee's W-4. Enter `99` if exempt from federal income tax.

**Additional Federal WH** — Additional amount (positive number) to be withheld from the employee for federal taxes (from W-4).

**State Exemptions** — Number of state income tax exemptions. Enter `99` if exempt from state income tax or if there is no state income tax.

**Additional State WH** — Additional amount (positive number) withheld from the employee's pay for state taxes. Default is `0.00`.

**Special State Amount #1** — Number of special state tax exemptions the employee is entitled to, if your state has them.

**Special State Amount #2** — Special state amounts required by certain states for the state tax calculation routine.

**WC Rate (Employee)** — Workman's Compensation cost per hour (in Oregon, per day) deducted from the employee's pay. Does not apply to California.

**WC Rate (Employer)** — Workman's Compensation cost per hour (in Oregon, per day) charged to the employer. Does not apply to California.

**Exempt from SDI?** — `Y` if the employee is exempt from state disability deductions; `N` if not. Enter `Y` if SDI is not used in your state.

**Employee Job Position** — The position in the company held by this employee.

**Sync PR Master with JC Master?** — For employees who will also be used to report labor to Work Orders. Enter `Y` to synchronize non-pay rate information with the Work Order/Job Cost employee file. Enter `$` to also maintain synchronization of pay rates.

### Std and Misc Deductions Screen

**Federal Income Tax** — Amount of federal income tax withheld quarter-to-date and year-to-date.

**FICA (SS)** — Social security portion of FICA withheld QTD and YTD.

**FICA (Med)** — Medicare portion of FICA withheld QTD and YTD.

**State Income Tax** — Amount of state income tax withheld QTD and YTD.

**SDI** — Amount of state disability insurance premiums withheld QTD and YTD.

**Workers Comp** — Amount of workman's compensation insurance cost withheld from the employee QTD and YTD. Does not apply to California.

**Misc** — A taxable amount that can be deducted from the employee's paycheck each pay period. On-the-fly deduction for special situations. Can be used in addition to or instead of standard deductions created in PR-M.

**Spcl** — A second on-the-fly taxable deduction identical in function to Misc. Can be used in addition to or instead of standard deductions from PR-M.

**Last Descrip** — The last description used when the Misc and Special deductions were entered during PR-B. Display only.

**Last Amt** — The last amount when either of these on-the-fly deductions were entered for this employee.

**Last GL Account** — The last GL account used when these deductions were entered through PR-B.

**QTD Total** — Total amount of the deduction quarter-to-date.

**YTD Total** — Total amount of the deduction year-to-date.

### User-Defined Deduction Screen

Payroll allows up to 15 user-defined deductions per payroll division through PR-M Payroll Defaults. Fields:

**Deduction No** — Number of the user-defined deduction (1–15). Reference only.

**Description** — Name of the user-defined deduction as established in PR-M. Reference only.

**Pre-Tax?** — `Y` if the deduction is set up as pre-tax in PR-M. If `Y`, the *Exempt from* section will show Y/N values for each standard deduction. If `N`, the *Exempt from* section is blank. Reference only.

**"Exempt from" Section** — When Pre-Tax? is `Y`, indicates whether this deduction is exempt from each of: Fed Inc Tax, FICA (SS), FICA (Med), FUTA, State Inc Tax, SUTA, SDI, Workers Comp. Reference only.

**"Employee Portion" Section** — Shows the type of deduction for the employee portion as set up in PR-M: Flat $ Amount, $ Amt X Total Hours, or % of Gross Pay. Reference only.

**Deduction Amount** — Amount or percentage to be deducted each payroll.

**Pay Period $ Limit** — Maximum dollar amount that can be deducted per pay period.

**Annual $ Limit** — Maximum dollar amount that can be deducted per year.

**Deducted QTD** — Amount deducted from the employee quarter-to-date.

**Deducted YTD** — Amount deducted from the employee year-to-date.

**"Employer Portion" Section** — Shows the type of employer contribution: Flat $ Amount, $ Amt X Total Hours, % of Gross Pay, or Matching Percentage. Reference only.

**Deduction Amount (Employer)** — Amount or percentage to be contributed by the employer each payroll.

**Pay Period $ Limit (Employer)** — Maximum dollar amount that can be contributed per pay period.

**Annual $ Limit (Employer)** — Maximum dollar amount that can be contributed per year.

**Contribution QTD** — Amount contributed by the employer quarter-to-date.

**Contribution YTD** — Amount contributed by the employer year-to-date.

### Vacation/Sick Pay Screen

**VACATION ACCRUAL**

**Accrual Method** — `P` = accrued as a percentage of hours worked; `H` = fixed number of hours.

**Accrual Rate (If Percentage)** — Multiplied by hours worked to determine vacation hours accumulated during the pay period. Formula: `(No. days/year vacation x work hrs/day) / 2080`. Example for two weeks: `(10 x 8) / 2080 = .03846154` vacation hours per hour worked.

**Accrual Hours (If fixed number of hours)** — Number of vacation hours to be accrued per pay period, month, or year.

**Accrue by [P/M/Y]** — Whether vacation accrual occurs each pay Period, Monthly, or once per Year.

**Limit** — Maximum number of vacation hours allowed for this employee per year.

**Hours Due** — Number of unpaid vacation hours accumulated to date.

**Next Accrual Date** — Maximum date that vacation should next be accrued. Automatically advances by pay period, month, or year depending on accrual frequency.

**SICK PAY ACCRUAL** — Logic is identical to that of vacation pay.

### Pay Categories Screen

Assign General Ledger accounts for seven standard income categories (regular, overtime, doubletime, holiday, commission, vacation, sick pay) plus up to three user-defined income categories for this employee's payroll division. Defaults can be set in PR-M for each division.

Each income category requires a GL expense or liability account. For non-direct labor employees this is an expense account. If debiting direct labor to work-in-process and crediting an Accrued Payroll account in Work Orders, this account should be the Accrued Payroll expense account.

**Regular** — GL account charged for regular (non-overtime) pay. QTD and YTD hours and dollars displayed.

**Overtime** — GL account for overtime pay. QTD and YTD hours and dollars displayed.

**Doubletime** — GL account for doubletime pay. QTD and YTD hours and dollars displayed.

**Holiday** — GL account for holiday pay. QTD and YTD hours and dollars displayed.

**Commission** — GL account for commission income. QTD and YTD hours and dollars displayed.

**Vacation** — GL account for vacation pay. QTD and YTD hours and dollars displayed.

**Sick** — GL account for sick pay. QTD and YTD hours and dollars displayed.

**User-Defined Categories** — Up to three user-defined income categories can be set up through PR-M for the division. Their titles appear in the far left column; enter their respective GL accounts to the right.

**User-Defined Category Pay Rates** — If using user-defined income categories, enter the respective pay rates in Category 1, Category 2, or Category 3 fields.

### Bank Info Screen

Enter employee account and routing information for NACHA file for direct deposit submittal.

### 2020 W-4 Screen

Enter the additional information from the new W-4 form beginning in 2020. If using the 2020 or later W-4, do not enter Federal Exemptions or Additional Federal Withholding on the main screen.

### General Program Operation

**Adding a New Employee Record** — Before using this program, set up defaults for payroll divisions in PR-M. If cutting over from another payroll system at mid-year, read *Changing Payroll in Mid-Year* below. From the opening screen, click *Add* (or press Insert) to go to the main screen. Enter the employee number, then assign a division code using F2 or the lookup button. Complete remaining fields. Click additional buttons (*Std/Misc Deds*, *User-Defined Deds*, *Vac/Sick*, *Pay Categories*) to complete all screens. Save with F10 or the *Save* button.

**Entering Standard and Misc/Special Deductions** — From the main screen, click *Std/Misc Deds* to access standard federal and state deductions (with QTD and YTD amounts) and to set up Misc and/or Special deductions.

**Entering User-Defined Deductions** — From the main screen, click *User-Defined Deds* to see the list of deductions. Highlight a deduction and press Enter. Enter employee and employer (if applicable) portions. Click *Back to list* to return to the list.

**Entering Vacation and Sick Pay** — From the main screen, click *Vac/Sick*. Enter accruals and limits.

**Entering Pay Categories** — From the main screen, click *Pay Categories*. Set up standard and user-defined payrates and GL codes.

**Changing an Existing Employee Record** — From the opening screen, highlight an employee (sorted by employee number by default; click *Chg Search Key* to sort by name). Click *Edit* or press Enter. Save changes with F10. To find directly by number, click *Find*.

**Deleting an Existing Employee Record** — You may not delete an employee record. Set *Terminated?* to `Y` to exclude the employee from payroll processing. Records are maintained on file as historical records.

**Pay History Inquiry** — From the main screen, click *Pay History* to see a scrolling window of payroll dates, check numbers, hours, gross pay, and net pay. For more detail, use PR-I Print Pay History.

**Changing Payroll in Mid-Year** — If cutting over from another payroll system during the year, QTD and YTD balances must be entered. The preferred method is to run one dummy payroll for each completed quarter (using the last payroll date of that quarter) plus one for the current quarter's QTD information. When processing these dummy payrolls in PR-B, manually force the deductions to agree with records from the previous system. This creates one history record per quarter per employee and updates all QTD and YTD figures.

---

## PR-B — Enter Pay Info

*Source: [pr-b_enter_pay_info.htm](../../../samples/chm/extracted/pr-b_enter_pay_info.htm)*

**Purpose.** Use this program to enter payroll information prior to printing payroll checks. This is step one in the normal payroll procedure. Step two is PR-C Print Payroll Register; step three is PR-D Print Payroll Checks.

### Main Screen Fields

**(Employee Number and Name)** — Employee number and full name from the employee file. Fields are not labeled.

**Div** — The employee's division as set up in PR-A.

**PAY TYPES**

**Regular** — Regular pay hours, rate, and gross pay amount (rate × hours).

**Overtime** — Overtime pay hours, rate, and gross pay amount (rate × hours).

**Double** — Doubletime pay hours, rate (regular rate × 2), and gross pay amount.

**Holiday** — Holiday pay hours, rate (defaults to regular rate), and gross pay amount.

**Commission** — Any commission pay amount. Also reflects commissions transferred through CS-D Transfer Sales Commissions.

**Vacation** — Vacation pay hours, rate, and gross pay amount.

**Sick** — Sick pay hours, rate, and gross pay amount.

**User Defined Pay Types (3)** — Up to three user-defined income categories as defined in PR-M for the division. Titles are displayed; enter hours and pay rates and the program calculates the pay amount.

**Total Hrs** — Total hours of all income categories combined for this payroll.

**Gross Pay** — Total payroll amount before any deductions.

**Net Pay** — Calculated net pay reflecting gross pay less all deductions.

**Days in Period** — Number of days worked during the payroll period. Defaults to the days associated with the Pay Period selected for this division in PR-M. Changing this value affects tax deduction calculations. If the pay amount covers more days than the normal pay period, update this field to reflect the correct number of days or incorrect tax amounts will be withheld.

**PAYCHECK SUMMARY** — Organized in two columns: the right column shows Gross Pay at the top and Net Pay at the bottom; the left column lists each standard deduction and a summary of user-defined deductions.

### User-Defined Deductions Screen

**Deduction No** — Number of the user-defined deduction (1–15). Reference only.

**Description** — Name of the deduction as established in PR-M. Reference only.

**Pre-Tax?** — `Y` if pre-tax deduction. Reference only.

**"Exempt from" Section** — Y/N values for each standard deduction. Reference only.

**"Employee Portion" Section** — Type of deduction (Flat $ Amount, $ Amt X Total Hours, % of Gross Pay). Reference only.

**Deduction Amount** — Amount or percentage to be deducted. Reference only.

**Pay Period $ Limit** — Maximum amount per pay period. Reference only.

**Annual $ Limit** — Maximum amount per year. Reference only.

**Deducted QTD** — Amount deducted QTD. Reference only.

**Deducted YTD** — Amount deducted YTD. Reference only.

**Deduction this paycheck** — The amount to be deducted on this paycheck. Editable.

**"Employer Portion" Section** — Type of contribution (Flat $ Amount, $ Amt X Total Hours, % of Gross Pay, Matching Percentage). Reference only.

**Contrib. this paycheck** — The amount to be contributed by the employer for this paycheck. Editable.

### Standard and Misc Deductions Screen

**STANDARD DEDUCTIONS**

**Fed Inc Tax** — Federal income tax withheld on this paycheck.

**FUTA** — Employer-only deduction; no entry in WH Amount column but employer expense appears in EC Amount column.

**FICA (SS)** — Social security FICA withheld. Employer's portion shown in EC Amount column.

**FICA (Med)** — Medicare FICA withheld. Employer's portion shown in EC Amount column.

**St Inc Tax** — State income tax withheld.

**SUTA** — Employer-only; no entry in WH Amount column but employer expense shown in EC Amount column.

**SDI** — Amount withheld for state disability insurance.

**Workers Comp** — Amount withheld for workman's compensation (rate × hours or days, where applicable by state). Employer's portion shown in EC Amount column.

**OTHER DEDUCTIONS**

**(Miscellaneous Deduction)** — Optional on-the-fly deduction for special situations such as reimbursing an employee. Description is entered each time.

**WH Amount** — Amount of the Miscellaneous deduction to be withheld this paycheck.

**GL Account** — GL account to which the Miscellaneous deduction is charged.

**(Special Deduction)** — Second optional on-the-fly deduction for special situations.

**WH Amount** — Amount of the Special deduction to be withheld this paycheck.

**GL Account** — GL account to which the Special deduction is charged.

### General Program Operation

**Adding New Payroll Records** — The opening screen shows existing payroll records and active employee names without payroll records. Payroll records are created when labor posts to payroll via WO-L-E or PR-K, or from this program. The P column shows `C` for records not yet processed for payment, `P` for records processed for payment. The right column shows `D` for Direct Deposit or `M` for a printed check (based on PR-A setting; changeable for this payroll only by clicking the D/M button).

Tag employees for processing: click *Tag All* to tag all active employees; *Tag Division* to tag employees in a specific division; *Tag/Untag One* or click an employee to tag one.

Once employees are tagged: click *Pay All (review each)* to process all while reviewing each; *Pay All (no review)* to process all without review; *Pay One* to process one at a time.

**Entering Pay Amounts** — Click *Pay Amounts*. Enter hours and/or pay rates. Click *Pay Amounts Done* or press Enter to finish. While entering, the *Days in period* field defaults to the Pay Period days for this division; change if the pay period is longer than normal (e.g., includes vacation pay days), otherwise incorrect tax amounts will be withheld.

**Entering User-Defined Deductions** — Click *User-Defined Deds*. Highlight and select a deduction. Enter or change employee deduction and employer contribution. Click *Back to list* to select another or *Main Screen* to return.

**Entering Standard and Miscellaneous Deductions** — Click *Std/Misc Deds*. Edit any standard federal and state deductions. Enter on-the-fly Misc or Special deductions with description, amount, and GL account. To reimburse an employee, enter the amount as a negative number (e.g., `-100.00`); this way the employee gets the amount without it being added to gross pay or included in tax calculations.

**Saving** — Once entries are complete and *OK to save?* is `Y`, click *Save* (or F10). If multiple employees were tagged, the next employee is displayed in succession. To skip an employee, set *OK to save?* to `N` before saving; changes are preserved but the record is not marked for payment.

**Changing an Existing Payroll Record** — Highlight the employee on the opening screen, click *Tag/Untag One*, then *Pay One*. Make changes and save. Records can be changed until PR-D Print Payroll Checks is run, after which all payroll processing records are cleared.

**Removing a Payroll Record** — Tag the employee, click *Pay One*, click *Pay Amounts*, set all Hours values to `0`, save. Net Pay will be zero; no paycheck will be printed.

---

## PR-C — Print Payroll Register

*Source: [pr-c_print_payroll_register.htm](../../../samples/chm/extracted/pr-c_print_payroll_register.htm)*

**Purpose.** Print the payroll register after entering payroll information in PR-B and before running PR-D Print Payroll Checks. This allows you to review all payroll information and make any corrections before checks are printed. The report includes all payroll information for each employee for the current pay period, plus totals for all employees. There is also an option to reprint a prior payroll register.

**General Program Operation.** Choose whether to print the current or a prior payroll register. If you choose *prior*, you are prompted for a date range, employee number range, whether to include terminated employees, and whether to print subtotals only. After printing, the program returns to the Payroll menu.

---

## PR-D — Print Payroll Checks

*Source: [pr-d_print_payroll_checks.htm](../../../samples/chm/extracted/pr-d_print_payroll_checks.htm)*

**Purpose.** Print the payroll information entered in PR-B on either pin-feed checks or laser checks. The default check type is set through AD-B Checking Accounts Defaults. Always run PR-C Print Payroll Register before running this program to verify all entries are correct.

**General Program Operation.** After selecting the program, your bank accounts are presented in a pop-up window. The highlighted account is your default payroll checking account (as specified in AD-B). Press Enter or click to choose the default, or select another account. The cursor moves to the *Beginning Chk Number* field showing the next available check number (originally entered in AD-B). The check date (posting date) and period ending date may be changed but default to the current date.

Employees designated as Direct Deposit are processed first, printing their pay information to plain paper as stubs. The program asks if the stubs printed correctly and posts them if the response is `Y`. After stubs are posted, you are prompted for a printer (in case checks are loaded in a different tray) for printing the actual checks.

After all checks have printed, the program asks if they printed correctly. When you answer `Y`:
- The current payroll file is cleared.
- Checks are added to the GL check register.
- Employee pay history is updated.
- Current taxes withheld are added to outstanding tax amounts.
- The *Next Check #* is incremented in AD-B.
- A copy of each check is saved to the payroll history file.
- For Direct Deposit: the Next Direct Deposit reference is updated in SD-R Assign Next Numbers and a copy of the pay detail is saved to the pay history file.

---

## PR-E — Print Employee Info

*Source: [pr-e_print_employe_information.htm](../../../samples/chm/extracted/pr-e_print_employe_information.htm)*

**Purpose.** Get a report of all employee information.

**General Program Operation.** Enter a range of employee codes to limit the report. If no limits are entered, the program prints information for all employees.

---

## PR-F — Maintain Tax Tables

*Source: [pr-f_maintain_tax_tables.htm](../../../samples/chm/extracted/pr-f_maintain_tax_tables.htm)*

**Purpose.** Enter or maintain tax tables for states that have income tax and for federal taxes. An updated set of state tax tables is provided each December for the following year and updated as needed during the year as states or the federal government release changes to withholding amounts. Some states have payroll withholding calculations not well suited to a table; the logic is embedded within PR-B or is a combination of tables and program. See the Payroll Tax Calculation by State section for a list of states and how their calculations are handled. Regardless of how updates to tax rates are obtained, FICA and Medicare rates and limits are stored in the Payroll Division file and must be updated by the user in PR-M Payroll Defaults.

### Field Explanations

**Tax code** — 3-character alphanumeric identifying the state and marital status. Examples: `WVS` = West Virginia Single. Federal tables stored under `USO` (other/single head of household?), `USM` (married), and `USS` (single).

**Description** — Tax description of the contents of the tax table.

**PAY AMOUNT FIELDS**

**From** — Lower limit of a tax bracket.

**To** — Upper limit of a tax bracket.

**TAX WITHHOLDING FIELDS**

**Tax Amount** — Minimum tax for a tax bracket.

**Plus Column** — Extra percentage of income added to the minimum tax to increase the tax evenly within a bracket.

**Excess over column** — Lower limit for calculation of the percentage tax. Same as the From field.

**General Program Operation.** Before using these tables, verify that the ones you need reflect the current tax structure. Much of the actual tax calculation occurs within PR-B; if there are inaccuracies, a software update may be needed (contact IS Tech Support at 866-516-3282). This program only needs to be used when tax changes occur that affect amounts only (not internal calculations). Check screen display against your most recent state tax tables.

---

## PR-G — Void Payroll Checks

*Source: [pr-g_void_payroll_check.htm](../../../samples/chm/extracted/pr-g_void_payroll_check.htm)*

**Purpose.** Void a payroll check after it has already been printed and posted. If you wish to cancel a check not yet printed, use PR-B and reset all Hours fields to zero. Note: you cannot void a payroll check if you have purged the payroll history information for that check (using PR-N Purge Payroll History).

**General Program Operation.** Enter the *Employee #* (use F2 or the Lookup button to select from a pop-up window). The employee name, division, and a pop-up listing of all payroll checks for that person are displayed. Select the check to void and press Enter. If you have more than one bank account, a pop-up shows your accounts; select the correct one.

The *Trans Date* defaults to today's date (changeable). You are asked if you want to reduce the current quarter-to-date earnings. If you answer `Y`, a warning appears: if taxes for this check have already been transferred via PR-H Transfer Liabilities to AP, you must use PR-H to back out previously transferred tax accounts. Using the printout from this program for the voided check, enter negative amounts to create reversing entries to the Accounts Payable payment file and to the General Ledger.

The program asks where to send the Payroll Void Register report (screen, printer, disk). This report is in the same format as the regular payroll register from PR-C; printing it to the printer is recommended for a hard copy record.

After the report has printed, you are asked if you want to void the check. If you answer `Y`, the program reverses every operation that PR-D Print Payroll Checks performed:
- Clears the check record from the payroll file.
- Adds an offsetting deposit to the check register.
- Subtracts the pay amount from the employee pay history.
- Marks the check as voided in the payroll check history.
- Posts offsetting entries to the General Ledger and Payroll Journal.

---

## PR-H — Transfer Liabilities to AP

*Source: [pr-h_transfer_liabilities_to_ap.htm](../../../samples/chm/extracted/pr-h_transfer_liabilities_to_ap.htm)*

**Purpose.** Transfer payroll taxes held in the payroll liability accounts to Accounts Payable. The transferred amounts are then available to be selected for payment by AP check. Liability accounts covered include:

- Federal Income Tax
- FICA withholding (Social Security)
- FICA withholding (Medicare)
- Federal Unemployment Tax (FUTA)
- State Income Tax
- State Unemployment Tax (SUTA)
- SDI
- Workman's Compensation
- Miscellaneous Deduction
- Special Deduction
- User-Defined Deductions (1–15)

Outstanding withholding amounts are updated every time paychecks are printed and with every transfer. You may choose which amounts and what portion of each to transfer.

**Prerequisites.** Before running:
- Specify the AP account in AD-A General Ledger Defaults.
- Specify payroll liability accounts in PR-M Payroll Defaults.
- Enter appropriate vendors for payroll withholding in AP-A Enter Vendors.

### Field Descriptions

**PR Division** — If using multiple payroll divisions, run this program separately for each division.

**State Code** — The state code associated with the selected division. Display only.

**Trans Date** — Transaction date of the transfer. This is the GL posting date used when payroll liability accounts are debited and the AP account is credited.

**General Program Operation.** Identify the payroll division (type it, use F2 lookup, or use standard record search keys). Accept or change the transaction date. The cursor moves to the *Amt to Pay* column opposite the first Outstanding amount; the entire outstanding amount is offered as a default. Press Enter to accept the default, or type a different amount. Repeat for each amount to transfer. Press F10 (or click *Save*) when finished.

When you transfer payroll taxes:
- The next AP invoice number is updated.
- Appropriate invoice line items are added to the AP transaction file.
- Outstanding amounts in the vendor record are updated.
- The transaction is posted to the General Ledger and Purchases journal.
- Outstanding taxes in PR-M are updated.

You do not need to transfer all amounts; press F10 at any time to save and transfer only the amounts you want. If there are no outstanding amounts, a message is displayed and the cursor returns to the PR Division field. Run this program separately for each payroll division.

---

## PR-I — Print Pay History

*Source: [pr-i_print_pay_history.htm](../../../samples/chm/extracted/pr-i_print_pay_history.htm)*

**Purpose.** Print a detailed listing of payroll transactions from the payroll history file. The report can be limited by a range of employee codes and by payroll dates. The history file grows with each pay period; it can be purged whenever you wish (see PR-N Purge Payroll History).

---

## PR-J — Enter Time Cards

*Source: [pr-j_enter_time_cards.htm](../../../samples/chm/extracted/pr-j_enter_time_cards.htm)*

**Purpose.** If you calculate payroll hours from time cards, use this program to calculate hours as you enter start and stop times and deduct times for breaks. After entry, time cards are printed, reviewed, then posted to the current payroll file via PR-K Print/Post Time Cards.

**General Program Operation.** Before using, set the desired time format in PR-M Payroll Defaults for each affected division. Three choices:

- **AM/PM TIME**: Time entered in hours, minutes, seconds with AM/PM designation. Example: 3:30 PM entered as `3:30:00 PM`.
- **24 HOUR TIME**: Time entered in 24-hour format. Example: 3:30 PM entered as `15:30:00`.
- **DECIMAL TIME**: 24-hour format with decimalized hours. Example: 3:30 PM entered as `15.50`.

**Time Card Entry.** Enter the employee number (or use F2 to select from a pop-up). The employee's name is displayed automatically. The date defaults to the current date and may be overridden. Enter Start time, Stop time, then Type: `R` for regular, `O` for overtime, `D` for double time. Enter time to deduct for lunch or breaks in the *Deduct* field. The *Total* field shows the result. After the Deduct field is entered, the entry area clears for another entry.

**Editing Previously Entered Lines.** Press F2 (or click *Display Lines*) to see a listing. Highlight and press Enter to select a line. Navigation keys: F5/*First*, F6/*Last*, F7/*Previous*, F8/*Next*. Save the batch with F10 (or click *Save*) after all entries are completed; exiting without saving loses entries.

A batch can be changed by entering the employee number again to display current entries. Use arrow keys to roll lines into the entry area. Delete a line with F4 (or click *Delete*) while it is in the entry area. Changes can be made until time card entries are posted to the current payroll file through PR-K; even after posting, hours can still be changed through PR-B.

---

## PR-K — Print/Post Time Cards

*Source: [pr-k_print_post_time_cards.htm](../../../samples/chm/extracted/pr-k_print_post_time_cards.htm)*

**Purpose.** Print the entries made in PR-J Enter Time Cards or transferred from Data Collection and, after reviewing them, post the hours to the current payroll file for processing through PR-B.

The report lists: employee, date, start time, stop time, type, deduct, and total hours, sorted by employee and by date within employee. Grand totals for regular time, overtime, and double time are provided per employee.

**General Program Operation.** Enter from/thru ranges of employee number, transaction dates, and types (`R`=regular, `O`=overtime, `D`=double time; pressing Enter on the Type field selects all three types).

You are asked *post when printing?* Recommended workflow: first run the report without posting to review entries for mistakes or omissions. Return to PR-J to edit or add entries if needed. Then run the report again specifying post while printing. Compare employee totals on the report to the totals in PR-B Enter Pay Info — the report totals for regular, overtime, and double time will now be inserted in the corresponding fields in PR-B.

**Transfer from Data Collection.** If the *Enable Shift Start/Stop* default is set to `Y` in SD-F Data Collection Defaults, you are prompted to transfer shift information from Data Collection. Enter from/thru ranges of employee number, date, and payroll division. Once data has transferred, print and post to payroll as described above.

---

## PR-M — Payroll Division Defaults

*Source: [pr-m_payroll_division_defaults.htm](../../../samples/chm/extracted/pr-m_payroll_division_defaults.htm)*

**Purpose.** Enter defaults for each of your Payroll divisions. This is the foundational setup required before any employees can be entered (at least one division must be created before PR-A can be used).

### Main Screen Fields

**Division** — The division code identifying the accounts and deduction information for the payroll division. At least one division must be created; every employee must be assigned to one. Divisions can handle different groups of employees with different deductions and GL accounts, or benefits for employees in different states. Individual employees can be assigned GL accounts different from the division defaults, so multiple divisions are not required solely for GL posting purposes.

**Name** — Name for the division (e.g., "California", "Direct Labor", "Supervisory Labor"). 20-character alphanumeric. Reference only.

**State** — Two-letter state designator for this division. Required.

**Pay Period [DWBSM]** — Normal pay period for this division's payroll:

| Code | Description | Days | Hours |
|------|-------------|------|-------|
| D | Daily | 1 | 8 |
| W | Weekly | 5 | 40 |
| B | Bi-weekly | 10 | 80 |
| S | Semi-monthly | 11 | 88 |
| M | Monthly | 22 | 176 |

**Time Card Format [ABC]** — Three formats available: AM/PM time, 24-hour time, and decimal time. Used by PR-J Enter Time Cards.

**WC Calculation [GHD]** — How workman's compensation is calculated: `H` = rate × hours worked; `D` = rate × days worked; `G` = rate × gross pay. In some states WC is a payroll deduction; in states like California it is paid separately as an insurance premium. PR-L-K Print Payroll Hours lists all hours and wages and is helpful in preparing WC forms.

**Pay Categories - PR Expense Accts** — GL expense accounts for each pay category. Can be overridden at the employee level in PR-A:

- Regular
- Overtime
- Doubletime
- Holiday
- Commission
- Vacation
- Sick Pay
- User-Defined (3)

**Accrual Rate - Vacation** — Enter a rate here only if all employees in the division receive an identical number of vacation hours, or to set a division default. Formula: `(No. days/year vacation × work hrs/day) / 2080`. Example for two weeks: `(10 × 8) / 2080 = .03846154`. Individual employees can have their own rate and annual cap in PR-A.

**Accrual Rate - Sick Pay** — Same as vacation rate logic. Enter only if all employees receive the same number of sick days, or to set a division default.

### User-Defined Deduction Screen

The system supports up to 15 user-defined deductions per division based on three calculation methods: percentage of gross pay, fixed flat amounts, or rate times total hours. Supports pre-tax deductions (e.g., 401K, Section 125 plan). Names assigned to these deductions appear on all screens and reports. Percentages and amounts are division-wide defaults but can be overridden at the employee level in PR-A. The 15 deductions are defined separately for each division.

**Deduction No** — Number 1–15 for this deduction.

**Description** — Name of the user-defined deduction.

**Pre-Tax?** — `Y` if the deduction is pre-tax. The *Exempt from* section will require Y/N values for each standard deduction. If `N`, the Exempt from section is blank.

**"Exempt from" Section** — When Pre-Tax? is `Y`, specify Y or N for: Fed Inc Tax, FICA (SS), FICA (Med), FUTA, State Inc Tax, SUTA, SDI, Workers Comp.

**EMPLOYEE PORTION**

**Calc Method** — Calculation method for the employee's portion. Enter `0` for no employee deduction amount; press F1 to see applicable codes. Three basic methods: Flat $ Amount, $ Amt X Total Hours, % of Gross Pay.

**Deduction Amount** — Amount or percentage to be deducted each payroll. Default value; can be overridden in PR-A.

**Pay Period $ Limit** — Maximum dollar amount per pay period. Default; can be overridden in PR-A.

**Annual $ Limit** — Maximum dollar amount per year. Default; can be overridden in PR-A.

**Liability GL Acct** — GL liability account where withheld amounts accumulate.

**Vendor** — Institution to receive the funds. Enables transfer through PR-H Transfer Liabilities to AP. Select from vendors set up in AP-A Enter Vendors (F2 or lookup button).

**Amount Outstanding** — Total amount not yet transferred through PR-H.

**EMPLOYER PORTION**

**Calc Meth** — Calculation method for the employer's portion. Enter `0` for no employer contribution; press F1 for codes. Four methods: Flat $ Amount, $ Amt X Total Hours, % of Gross Pay, Matching Percentage.

**Deduction Amount** — Amount or percentage to be contributed by employer each payroll. Default; can be overridden in PR-A.

**Pay Period $ Limit** — Maximum per pay period. Default; can be overridden in PR-A.

**Annual $ Limit** — Maximum per year. Default; can be overridden in PR-A.

**Expense GL Acct** — GL expense account for the employer expense.

**Advance EIC / Negative Deduction** — To set up Advance EIC as a user-defined deduction, create it as a fixed amount, NOT pre-tax. The logic in PR-B treats any negative deduction as pre-tax. Set up the applicable Advance EIC amount for the employee in PR-A as a negative amount. Override the amount as necessary in PR-B based on the Advance EIC table in Circular E for the current pay period gross wages.

### Standard Deductions — Rates Screen

**FICA [SS] Employee%, Employer%, $Limit** — Employee rate, employer rate, and limit in terms of maximum gross pay amount (not the FICA SS deducted amount).

**FICA (Md) Employee%, Employer%, $Limit** — Employee rate, employer rate, and limit in terms of maximum gross pay amount (not the FICA Medicare deducted amount).

**FUTA Employer%, $Limit, Credit%** — Employer rate, limit, and maximum credit allowed by federal statute. Limit is in terms of maximum gross pay amount, not total FUTA expense.

**SUTA Employer%, $Limit** — Employer rate and limit. Limit is in terms of maximum gross pay amount, not total SUTA expense.

**SDI Employer%, $Limit** — Employer rate and limit for state disability insurance. Limit is in terms of maximum gross pay amount, not total SDI expense.

### Standard Deductions — GL Accounts and Vendors Screen

**Liability Accts** — GL liability accounts for each standard deduction to accumulate withheld amounts until paid. Can be overridden at the employee level in PR-A:

- FIT — Federal Income Tax
- FICA [SS] — Social Security
- FICA [Md] — Medicare
- FUTA — Federal Unemployment
- SIT — State Income Tax
- SUTA — State Unemployment
- SDI — State Disability Insurance
- Work Comp — Workman's Compensation
- Spcl Ded — Special Deduction
- Misc Ded — Miscellaneous Deduction

**EC Expense Accts** — For categories where the employer pays a portion: FICA, FUTA, SUTA, SDI, and Workman's Comp all require expense account assignments.

**Vendors** — Institution to receive funds for each category. Examples: a bank as depository for federal income tax funds (FICA), a specific state agency for unemployment tax (SUTA). Enables transfer through PR-H. Select from vendors set up in AP-A Enter Vendors (F2 or lookup button).

**$Outstanding** — Total amount not yet transferred through PR-H. Calculated against liability accounts only.

### General Program Operation

**Adding a Division.** From the opening screen, click *Add*. Complete the main screen plus three additional screens: User-Defined Deductions, Standard Deductions — Rates, and Standard Deductions — GL Accounts and Vendors. Save with F10.

**Entering User-Defined Deductions.** Click *User Deds*. The list of existing deductions is displayed (numbered 1–15). To add or edit, highlight a line and click or press Enter. Complete all fields. Click *Back to List* when finished.

**Entering Standard Deduction Rates.** Click *Std Deds [Rates]*. Enter various rates. Click *Main Screen* when finished.

**Entering Standard Deduction GL Accounts and Vendors.** Click *Std Deds [GL/Vndr]*. Enter GL accounts and vendor designations. Click *Main Screen* when finished.

**Editing an Existing Division.** From the opening screen, highlight the division, click or press Enter (or click *Edit*). Edit any fields. Save with F10.

**Duplicating a Division.** Highlight the division to copy; click *Duplicate a Divisions*. Enter the new division code. The new division is added to the list. Edit the new division for any needed changes.

**Deleting a Division.** Only possible if no employees are assigned to it. Highlight the division; click *Delete*. Confirm with *Yes*.

---

## PR-N — Purge Payroll History

*Source: [pr-n_purge_payroll_history.htm](../../../samples/chm/extracted/pr-n_purge_payroll_history.htm)*

**Purpose.** Clear the payroll history file.

**General Program Operation.** Before purging, consider backing up the file to archive media or printing the payroll history using PR-I Print Pay History. You have the opportunity to print the information as part of the purge process. You can purge payroll check history based on payroll date, a range of employee numbers, and/or a payroll division.

---

## PR-O — Year End Routine

*Source: [pr-o_year_end_routine.htm](../../../samples/chm/extracted/pr-o_year_end_routine.htm)*

**Purpose.** Create a W-2 data file and reset each employee's quarter-to-date and year-to-date pay amounts to zero to prepare for the new calendar year.

**General Program Operation.** You must run this program prior to the first payroll of the new calendar year. Enter `Y` in the *Proceed with Payroll year end routine?* field and processing begins. The W-2 file created (BKPRW2.B*) is a replica of each employee's master payroll record and is the source for PR-L-I Print W-2 Forms.

---

## PR-P — Enter Raise Dates

*Source: [pr-p_enter_raise_dates.htm](../../../samples/chm/extracted/pr-p_enter_raise_dates.htm)*

**Purpose.** Enter dates and notes associated with employee raises.

**General Program Operation.** For each raise date, enter the date, amount, two lines of summary notes, and (by clicking the Notes button) up to 24 additional lines of notes associated with the raise date. Raises entered with a future date are noted as Future Raises. Raise history can be viewed from PR-A Enter Employees if enabled in PR-R Payroll Defaults.

---

## PR-Q — Enter Review Dates

*Source: [pr-q_enter_review_dates.htm](../../../samples/chm/extracted/pr-q_enter_review_dates.htm)*

**Purpose.** Enter dates and notes associated with employee reviews.

**General Program Operation.** For each review date, enter the date and two lines of summary notes, and (by clicking the Notes button) up to 24 additional lines of notes. Reviews entered with a future date are noted as Future Reviews. Review history can be viewed from PR-A Enter Employees if enabled in PR-R Payroll Defaults.

---

## PR-R — Payroll Defaults

*Source: [pr-r_payroll_defaults.htm](../../../samples/chm/extracted/pr-r_payroll_defaults.htm)*

**Purpose.** Enter default settings for payroll.

### Fields

**Raise Info Access from PR-A** — If set to `Y`, a button to view raise history is available in PR-A Enter Employees.

**Review Info Access from PR-A** — If set to `Y`, a button to view review history is available in PR-A Enter Employees.

**Using Payroll** — Indicate `Y` or `N` whether the Payroll module is being used.

**Consolidate GL Postings in PR-D** — If set to `Y`, PR-D Print Payroll Checks will consolidate the GL Transaction postings, eliminating personal pay information from the GL Detail.

**PR-B Pull in Misc Income User Defined Category 1** — If set to `Y`, PR-B Enter Pay Info will pull Misc Income Category 1 (as defined in PR-A Enter Employees) into the check calculation.

**PR-B Pull in Misc Income User Defined Category 2** — If set to `Y`, PR-B Enter Pay Info will pull Misc Income Category 2 into the check calculation.

**PR-B Pull in Misc Income User Defined Category 3** — If set to `Y`, PR-B Enter Pay Info will pull Misc Income Category 3 into the check calculation.

---

## PR-S — Assign Password to Employee

*Source: [pr-s_assign_password_to_employ.htm](../../../samples/chm/extracted/pr-s_assign_password_to_employ.htm)*

**Purpose.** Assign employee passwords to be used when clocking in and out of shift at DC-L Shift Clock In/Out.

**General Program Operation.** Enter the Employee number and password, then confirm the password.

---

## Quarterly and Annual Reports

---

## PR-L-A — Print Quarterly Info

*Source: [pr-l-a_print_quarterly_info.htm](../../../samples/chm/extracted/pr-l-a_print_quarterly_info.htm)*

**Purpose.** Get a report of employee gross payroll and tax information for the current quarter. Use as a reference for quarterly tax reports.

**General Program Operation.** Enter a range of employee numbers and/or divisions; leave blank to include all employees. **Important:** this is the only report that uses the QTD subtotals and therefore must be run prior to the first payroll of a new quarter. All other forms and reports (e.g., PR-L-B, PR-L-G) use the detail payroll transaction file for a date range and do not need to be run before the next quarter's first payroll.

---

## PR-L-B — Print QTD Earnings Register

*Source: [pr-l-b_print_qtd_earnings_register.htm](../../../samples/chm/extracted/pr-l-b_print_qtd_earnings_register.htm)*

**Purpose.** Summary listing of earnings by employee by quarter.

**General Program Operation.** Select a from/thru range of employees and dates.

---

## PR-L-C — Print QTD Taxable Earnings

*Source: [pr-l-c_print_qtd_taxable_earnings.htm](../../../samples/chm/extracted/pr-l-c_print_qtd_taxable_earnings.htm)*

**Purpose.** Summary listing of taxable and total wages by employee by quarter.

**General Program Operation.** Select a range of employees, a quarter, and a taxable limit.

---

## PR-L-D — Print Detail Earnings Ledger

*Source: [pr-l-d_print_detail_earnings_ledger.htm](../../../samples/chm/extracted/pr-l-d_print_detail_earnings_ledger.htm)*

**Purpose.** Summary listing of total wages and standard type deductions by employee for any date range.

**General Program Operation.** Select a from/thru range of employees and dates.

---

## PR-L-E — Print Detail Deductions Ledger

*Source: [pr-l-e_print_detail_deductions_ledger.htm](../../../samples/chm/extracted/pr-l-e_print_detail_deductions_ledger.htm)*

**Purpose.** Summary listing of total wages and user-defined deductions (as specified in PR-M Payroll Defaults) by employee for any date range.

**General Program Operation.** Select a from/thru range of employees, dates, and payroll divisions.

---

## PR-L-F — Print Subject to Report

*Source: [pr-l-f_print_subject_to_report.htm](../../../samples/chm/extracted/pr-l-f_print_subject_to_report.htm)*

**Purpose.** Listing of wages subject to FUTA and SUTA taxes by employee by quarter.

**General Program Operation.** Select a from/thru range of employees and divisions; select the year and quarter. A window displays the actual date ranges that will be used. Option to suppress zero year-to-date quantities to shorten the report.

**Note:** If you begin using Payroll at any point after the calendar year has already started, this report will not be accurate for the first partial year. Once you are past the first partial year, the report will be fully accurate.

---

## PR-L-G — Print 941 and Schedule B Reports

*Source: [pr-l-g_print_941_and_schedule_b_reports.htm](../../../samples/chm/extracted/pr-l-g_print_941_and_schedule_b_reports.htm)*

**Purpose.** Print the federal Form 941 — the payroll form submitted to the federal government quarterly. The form includes payroll amounts, taxes withheld, adjustments, and tax liability. The fields on screen correspond directly with the 941 form. If you have not been running payroll for an entire quarter, you will need to supplement the payroll data on screen.

**General Program Operation.** Enter the year and choose a quarter from the menu, then verify the beginning date. The program calculates the quarter's payroll information from your system data. You have the opportunity to change any amounts and supply additional information not stored in the system. When all fields are complete, the form prints (screen, printer, or disk file). After the form is printed, you have the option to print the Schedule B report that accompanies the 941.

---

## PR-L-H — Print 940 Forms

*Source: [pr-l-h_print_940_form.htm](../../../samples/chm/extracted/pr-l-h_print_940_form.htm)*

**Purpose.** Print the federal Form 940 — the payroll form submitted annually. Includes information about FUTA (federal unemployment taxes) and SUTA (state unemployment taxes). If you have not been running payroll for the entire year, supplement the payroll data on screen with your totals prior to starting Payroll.

The fields on screen correspond directly with the 940 form. Use the PART title (e.g., Part I, Part II) and the letter or number in front of each line to find the related line on the actual form.

**General Program Operation.** When you run the program, you are first asked to verify the rates. If correct, press Enter; otherwise enter new percentages. To permanently change rates for payroll, use PR-M Payroll Defaults.

Once rates are verified, the main screen displays. The program calculates appropriate amounts from your system data. You can change these amounts and supply additional information. Note that Part V (Computation of Tentative Credit) only applies if you enter `N` to questions A or B, or enter `Y` to question C.

When completed, you are asked if your entries are correct. If yes, proceed to print (screen preview, printer, or disk file).

---

## PR-L-I — Print W-2 Forms

*Source: [pr-l-i_print_w-2_forms.htm](../../../samples/chm/extracted/pr-l-i_print_w-2_forms.htm)*

**Purpose.** Print the employee's year-to-date payroll information on pre-printed W-2 forms or to a file for electronic submittal.

When you run PR-O Year End Routine at calendar year end, the program creates a W-2 file (`BKPRW2.B*`) that is a replica of each employee's master payroll record. W-2 data is extracted from this file. You can run W-2s whenever convenient once PR-O has been run.

**General Program Operation.** Choose to print based on Division or Dept, from/thru Employee #, or from/thru Employee Last Name. If no limits are specified, all employees currently in the system are printed.

Enter: Federal and State ID Codes, Local Income Tax Deduction Number (1–15), Locality, Second Locality Tax Deduction Number (1–15), Second Locality Name, Pension Plan Tax Deduction Number (1–15), 401K or Deferral Deduction Number (1–15), Cafeteria Plan Deduction Number (1–15), and Advanced EIC Deduction Number (1–15). These deduction numbers correspond to the 15 user-defined deductions set up in PR-M for each payroll division.

As many as five user-defined deductions can be entered against the 401K or Deferral category; as many as six against the Cafeteria Plan category. Do not enter the same deduction number more than once on a line — doing so will multiply the amount on the W-2s.

**Local Tax Liability:** A Local exempt from field was added to user-defined deductions effective 12/28/98. Go to PR-M and redefine any user-defined deductions that apply to local tax — in the *Exempt from* section there is a *Local* field. A second locality has been added to the PR-L-I entry screen for employees who moved during the year or if you have more than one locality to report.

You are asked whether to print in alpha order (default `Y`) and whether to print W-2s with no earnings (default `N`).

**Editing W-2 Data.** To change data that will print on the W-2, click *Edit W-2 Data* (or press Home key). The screen looks identical to PR-A Enter Employees but presents the frozen W-2 file, not the active employee file. Edit any YTD or other fields and save, then print W-2s.

**Printing test page.** The program does not prompt for a test page. Test with a range of two employees to verify alignment before running all W-2s. Adjustments can be made using *Modify Forms* in the File menu.

**W-3 preparation.** The last W-2 printed is a summary W-2 that prints at the top of a new page and is marked VOID. Do not submit to the Social Security Administration; it is intended to help prepare the W-3 Transmittal form. The total number of W-2s printed is in the Control Number box. If you have multiple divisions with different user-defined deductions for different categories, print each division's W-2 forms separately and manually calculate totals for the W-3.

---

## PR-L-K — Print Payroll Hours

*Source: [pr-l-k_print_payroll_hours.htm](../../../samples/chm/extracted/pr-l-k_print_payroll_hours.htm)*

**Purpose.** Listing of all payroll hours and pay amounts for regular time, overtime, double time, holidays, vacation time, and sick time. Often used to prepare workman's compensation reports.

**General Program Operation.** Select from/thru ranges of employee numbers, payroll divisions, and dates.

---

## PR-L-L — Print 941B Forms

*Source: [pr-l-l_print_941b_forms.htm](../../../samples/chm/extracted/pr-l-l_print_941b_forms.htm)*

**Purpose.** Print federal 941B forms. Can print a plain-paper proforma report or directly on pre-printed 941B forms.

**General Program Operation.** Enter your Employee Tax ID Code. Indicate the quarter (1–4), the year, the quarter beginning date, and quarter ending date. If you indicate `Y` to print a plain paper proforma report, you get a detailed listing of daily tax liability for each day of each month within the quarter plus monthly and quarterly totals. If you indicate `N`, the program prints directly to the 941B format.

---

## PR-L-M — Print Employer Contributions

*Source: [pr-l-m_print_employer_contributions.htm](../../../samples/chm/extracted/pr-l-m_print_employer_contributions.htm)*

**Purpose.** Listing of employer matching contributions to any of the 15 user-defined deductions set up through PR-M Payroll Defaults.

**General Program Operation.** Enter from/thru ranges of employee codes, payroll dates, and divisions. After printing, the program returns to the Payroll reports submenu.

---

## PR-L-N — Print Payroll Wages Detail

*Source: [pr-l-n_print_payroll_wages_detail.htm](../../../samples/chm/extracted/pr-l-n_print_payroll_wages_detail.htm)*

**Purpose.** Listing of wages paid broken down into income categories tracked by Payroll: regular, overtime, doubletime, holiday, commission, vacation, sick, and three user-defined categories.

**General Program Operation.** Enter from/thru ranges of pay dates, divisions, and employee numbers.

---

## PR-L-P — Print Employee Raises

*Source: [pr-l-p_print_employee_raises.htm](../../../samples/chm/extracted/pr-l-p_print_employee_raises.htm)*

**Purpose.** Listing of raises and dates and any notes associated with those raises.

**General Program Operation.** Enter from/thru ranges of employee numbers, dates, and whether to include summary lines and notes.

---

## PR-L-Q — Print Employee Reviews

*Source: [pr-l-q_print_employee_reviews.htm](../../../samples/chm/extracted/pr-l-q_print_employee_reviews.htm)*

**Purpose.** Listing of reviews and dates and any notes associated with those reviews.

**General Program Operation.** Enter from/thru ranges of employee numbers, dates, and whether to include summary lines and notes.

---

## Payroll Tax Calculation by State

*Source: [payroll_tax_calculation_by_state.htm](../../../samples/chm/extracted/payroll_tax_calculation_by_state.htm)*

Some states have some or all of their tax calculation written into the PR-B program because the calculation is not well suited to the tax table. Regardless of how updates to tax rates are obtained, FICA and Medicare rates and limits are stored in the Payroll Division file and must be updated by the user in PR-M Payroll Defaults for each division.

The table below indicates by state whether the tax calculation is entirely in the tax table, or if there are also programmed entries in the PR-B program to be considered.

| State | No Tax | Tax Table | PR-B Program |
|-------|--------|-----------|--------------|
| AK | X | | |
| AL | | X | X |
| AR | | X | X |
| AZ | | | X |
| CA | | X | X |
| CO | | X | |
| CT | | X | X |
| DC | | X | |
| DE | | X | X |
| FL | X | | |
| GA | | X | X |
| HI | | X | |
| IA | | X | X |
| ID | | X | |
| IL | | X | |
| IN | | | X |
| KS | | X | |
| KY | | X | X |
| LA | | | X |
| MA | | | X |
| MD | | X | X |
| ME | | X | X |
| MI | | X | X |
| MN | | X | |
| MO | | X | X |
| MS | | X | X |
| MT | | X | |
| NC | | X | X |
| ND | | X | |
| NE | | X | |
| NH | X | | |
| NJ | | X | |
| NM | | X | |
| NV | X | | |
| NY | | X | X |
| OH | | X | |
| OK | | X | X |
| OR | | X | X |
| PA | | X | |
| PR | | X | X |
| RI | | X | |
| SC | | X | X |
| SD | X | | |
| TN | X | | |
| TX | X | | |
| UT | | X | |
| VA | | X | |
| VT | | X | |
| WA | X | | |
| WI | | X | X |
| WV | | X | |
| WY | X | | |

**No Tax** — No state income tax; no state tax calculation is performed.
**Tax Table** — Tax calculation uses the tax table maintained in PR-F Maintain Tax Tables.
**PR-B Program** — Tax calculation has programmed logic embedded in PR-B Enter Pay Info (either alone or in combination with the tax table). For states with PR-B Program logic, ensure you are running the most current version of the payroll programs as well as the tax tables each year. Contact IS Tech Support at 866-516-3282 if inaccuracies are found.

---

## Cross-references

- **GL (General Ledger)** — Payroll posts to the GL for all income categories (regular, overtime, doubletime, holiday, commission, vacation, sick, user-defined) and all tax liabilities. PR-D Print Payroll Checks adds checks to the GL check register. PR-G Void Payroll Checks posts offsetting entries to the GL and Payroll Journal. PR-H Transfer Liabilities to AP posts to the GL and Purchases journal.
- **AP (Accounts Payable)** — PR-H Transfer Liabilities to AP transfers outstanding payroll tax liabilities (FIT, FICA, FUTA, SIT, SUTA, SDI, WC, and user-defined deductions) to AP for payment. Requires AP-A Enter Vendors to have vendor records set up for each payroll liability payee.
- **SM-G Enter Employees** — The Work Orders/Labor Reporting employee file. When a new employee is added to SM-G but not yet to the payroll file, PR-A advises the user. The *Sync PR Master with JC Master?* field in PR-A keeps the two files synchronized.
- **PR-R Payroll Defaults** — Module-level flags: whether Payroll is in use, whether to consolidate GL postings in PR-D, whether user-defined income categories pull automatically into PR-B, and whether raise/review history is accessible from PR-A.
- **PR-M Payroll Division Defaults** — Division-level configuration for all payroll processing: state, pay period, GL accounts, tax rates, FICA/FUTA/SUTA/SDI rates, up to 15 user-defined deductions, and vendor assignments for PR-H transfers.
- **AD-B Checking Accounts Defaults** — Default payroll checking account and next check number used by PR-D Print Payroll Checks.
- **AD-A General Ledger Defaults** — AP account required by PR-H Transfer Liabilities to AP.
- **WO-L-E Print/Post Labor to Payroll** — Posts direct labor hours from Work Orders into the Payroll current payroll file, feeding PR-B Enter Pay Info.
- **Data Collection / DC-L Shift Clock In/Out** — Time collected via Data Collection can be transferred into PR-K Print/Post Time Cards. PR-S Assign Password to Employee sets up the shift clock-in password.
- **CS-D Transfer Sales Commissions** — Commission amounts transferred to payroll appear in the Commission field of PR-B Enter Pay Info.
