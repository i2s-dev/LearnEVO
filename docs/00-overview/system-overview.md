# System Overview (from EvoHELP.CHM)

Status: verified (text is a near-verbatim rendering of the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../samples/chm/extracted/).
Extracted with `hh.exe -decompile` and rendered via
[scripts/chm_to_md.py](../../scripts/chm_to_md.py).

This doc consolidates the 11 topics the help file groups under
"System Overview" — the vendor's own tour of how EvoERP is installed,
how companies work, when to run what, and where the data lives. Each
subsection cites the originating `.htm` so the raw source is one click
away. The full database-table list is split out into a sibling doc:
[File Names (complete table index)](../04-data-dictionary/file-names-index.md).

---

## 1. Welcome / Help File

*Source: [evoerp_help_file.htm](../../samples/chm/extracted/evoerp_help_file.htm)*

Evo~ERP is described by its vendor as "an operational software package
for manufacturers, distributors and job shops" — a toolset for cost
control, inventory management, and on-time delivery. The bundled help
documents every system program and is reachable via F1 inside any
screen.

**Technical support tiers** (verbatim):
- Free: [IS Tech Support forum](http://www.istechforum.com/).
- Silver: forum + unlimited email to an assigned support rep.
- Gold: all of the above + unlimited phone support.
- Per-call phone support also available.

---

## 2. Installation

*Source: [installation.htm](../../samples/chm/extracted/installation.htm)*

**Three-step install:** EvoERP software → Pervasive SQL → workstation
setup.

**License files** (delivered by email after purchase):
`BKARSIVL.B`, `START_UP.RUN`, `SUWIN6.DCY`. Without these, running a
demo only gets you 30 days. Contact `sales@evoerp.com` if missing.

**Pervasive SQL:**
- **Workgroup** edition — max 5 users.
- **Client/Server** edition — required for 6+ users.
- 30-day trial ships with Server edition. Typical install, accept
  defaults. No ODBC driver setup needed at install time — see
  §6 below.
- The license is a text string entered via the **Pervasive License
  Administrator Utility** on the server. Error **161** at load =
  license not loaded or 30-day trial expired.

**EvoERP:**
- Download demo ZIP from `evoerp.com`, unzip, run `EvoERPInstall.EXE`.
- Default location `C:\EVOERP` (overridable).
- After extraction, drop `BKARSIVL.B` into the `DEFAULT` subfolder and
  the other license files alongside the app folder.
- Share the app folder and all subfolders with **full control** for
  every user.

**Workstation setup** (each client PC):
- Install the Pervasive client (typical, no DB/ODBC config).
- Browse to the server's app folder, double-click `EVOERP.EXE`.
- Workstation Setup copies files locally, writes registry entries,
  creates a desktop icon.
- On Vista / Win7 / Win8: right-click → **Run as Administrator** for
  the setup run *and* the first run of the icon. After that it runs
  normally.
- If Admin does the setup but the end-user profile is different,
  grant the end-user profile full rights to `C:\ISTS\`.

**First login:** username `ADMIN`, password `ADMIN` → full menu.
Create real users via
[PS-A System Users/Passwords](../../samples/chm/extracted/ps-a_system_users_passwords.htm)
and wire up access via
[PS-G Maintain Menu Access](../../samples/chm/extracted/ps-g_maintain_menu_access.htm).

> **LearnEVO note** — matches our observation that `C:\ISTS\` is the
> per-workstation runtime dir (§1 of [CLAUDE.md](../../CLAUDE.md)).
> All the app code lives on the share; `C:\ISTS\` is only a local
> launcher + cache of user-specific files.

---

## 3. Using Terminal Server and Citrix

*Source: [using_terminal_server_and_citrix.htm](../../samples/chm/extracted/using_terminal_server_and_citrix.htm)*

TS/Citrix needs a **per-user ISTS folder** because the default
`C:\ISTS` is shared across sessions. Procedure:

1. Pick an unused drive letter. Enter it at
   [SD-A Company Defaults](../../samples/chm/extracted/sd-a_company_defaults.htm)
   as the **Alternate Drive for ISTS**.
2. In each user profile, map that letter to a per-user folder with an
   `ISTS` subfolder — e.g. if letter is `M:`, each user sees their own
   `M:\ISTS`.
3. The icon points at `M:\ISTS\STARTEVO.EXE`. The per-user `.INI`,
   `.EXE`, and other user-specific files live under there.
4. On the TS host itself, **delete** everything in `C:\ISTS` and strip
   permissions so no one can recreate anything in it.
5. For each user: log in, browse to the share, right-click
   `EVOERP.EXE` → **Run as Administrator**. First icon run also needs
   Run as Admin, after which it's normal.
6. Each user profile needs full rights to its own ISTS folder.

---

## 4. Setting up Printing

*Source: [setting_up_printing.htm](../../samples/chm/extracted/setting_up_printing.htm)*

Print format selection is **per document type, per defaults screen** —
not one central setting. Where to configure each:

| Document | Configured at |
|---|---|
| AP & Payroll checks | [AD-B Checking Account Defaults](../../samples/chm/extracted/ad-b_checking_account_defaults.htm) |
| Statements | [AR-S / SD-P Customer AR Defaults](../../samples/chm/extracted/sd-p_customer_ar_defaults.htm) |
| Acknowledgments, packing slips, invoices, sales quotations | [SD-M Sales Orders Defaults](../../samples/chm/extracted/sd-m_sales_order_defaults.htm) |
| PO and RFQ formats | [SD-C Purchase Orders Defaults](../../samples/chm/extracted/sd-c_purchase_order_defaults.htm) |
| Customer quotes (estimates) | [SD-G Estimating Defaults](../../samples/chm/extracted/sd-g_estimating_defaults.htm) |

**Emailing** — every graphical (RTM) form or report can be emailed
directly from the printer-selection dialog. Customer/vendor email
address is pulled from the master record. SMTP server and signature
boilerplate live at
[US-A Customize Settings](../../samples/chm/extracted/us-a_customize_settings.htm).

---

## 5. Using Multiple Companies

*Source: [using_multiple_companies.htm](../../samples/chm/extracted/using_multiple_companies.htm)*

**~1,200 possible companies.** Each is a **2-char alphanumeric code**.
All companies share one set of program files, but each has its own
data files; a user is in exactly one company at a time.

**The default ("blank") company:**
- Lives in the `DEFAULT` subfolder.
- Has no company code.
- Is what you see on first login.
- Its data files use extension `*.B`.

**Additional companies:**
- Each lives in its own subfolder (e.g. `TESTDATA` for sample
  company 99, "Evolution Enterprises").
- Their data files use `*.Bxx` where `xx` is the 2-char code —
  e.g. `.B99`.

**Single-company shops should use the blank company.** You do not need
to create a second company to get clean files — just clear the few
demo GL accounts via
[UT-K-A Clear Data](../../samples/chm/extracted/ut-k-a_clear_data.htm)
or
[AM-C Enter General Ledger Accounts](../../samples/chm/extracted/am-c_enter_general_ledger_accounts.htm).

**UT-I Create/Delete Company** creates/removes companies. It can
copy data from an existing company or initialize empty files. Common
uses: temporary training company (create, experiment, delete);
second real company seeded from the first.

**UT-K-A Clear Data** lets you selectively clear six file groupings:
GL Chart of Accounts, AR Customers, AP Vendors, Inventory Items,
Payroll Employees, Manufacturing Systems. For each, enter **C** (keep
masters, clear transactions), **D** (clear everything), or **N**
(leave alone). Can be slow on large files.

**Changing company:** File menu → Change Company. The active company
name is shown in the bottom banner at all times.

**Per-user defaults** for startup company and startup menu are set at
[PS-A System Users/Passwords](../../samples/chm/extracted/password_security.htm)
and
[PS-G Maintain Menu Access](../../samples/chm/extracted/ps-g_maintain_menu_access.htm).

---

## 6. ODBC Data Connection

*Source: [odbc_data_connection.htm](../../samples/chm/extracted/odbc_data_connection.htm)*

Pervasive SQL ships with two engines: **Transactional** (what EvoERP
uses natively) and **Relational** (the ODBC/JDBC face). You need the
Relational side only if you're going to:
- Run Crystal Reports, MS Access, or other external report writer
  against EvoERP data.
- Connect UPS, FedEx, or other shipping software.
- Run EvoERP's Java apps: BM-N (BOM Availability), SH-R (Scheduling),
  SA-F-A/B/C/D (Sales Analysis), DE-A (Data Export), GL-R (Business
  Status).

**Setup sequence:**

1. **Build DDF files.** Per-company. Run via **UT-A**, program
   `ODBCDDF`. The standard post-update utility run refreshes DDFs so
   new tables/fields show up — no separate step most of the time.
2. **Define the database on the server.** Server console: open
   **Pervasive Control Center** (Start → Programs → Pervasive →
   Control Center & Documentation). Select **New Database**, confirm
   the server, name the database, point at the **company folder**.
   Accept all other defaults.
3. **For the Java apps**: configure via
   [SM-T Enter Java Settings](../../samples/chm/extracted/sm-t_enter_java_settings.htm).

> **LearnEVO note** — our deeper writeup lives at
> [01-architecture/external-odbc-connections.md](../01-architecture/external-odbc-connections.md).

---

## 7. Sequence of Events

*Source: [sequence_of_events.htm](../../samples/chm/extracted/sequence_of_events.htm)*

Manufacturing breaks into **five spheres** of activity. The help file
lists the steps inside each (and the key reports for each). For
accounting cadence see §8 (Important Times).

### 7a. Manufacturing Planning

Inventory planning, scheduling, capacity planning — all interact.
Steps (not strictly sequential):

**Planning Work Orders and Purchase Orders**
- Convert sales orders ([SO-N](../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm))
  and estimates ([ES-E](../../samples/chm/extracted/es-e_convert_estimates.htm)) to work orders.
- Enter forecasts ([MR-A Enter Forecast](../../samples/chm/extracted/mr-a_enter_forecast.htm)).
- Print Reorder Report ([IN-D](../../samples/chm/extracted/in-k_adjust_physical_levels.htm)).
- Generate material requirements ([MR-F](../../samples/chm/extracted/mr-f_generate_mrp_requirements.htm)).
- Generate WOs via MRP ([MR-I](../../samples/chm/extracted/mr-i_generate_work_orders.htm)) or manually ([WO-A](../../samples/chm/extracted/wo-a_enter_work_orders.htm)).
- Generate POs via MRP ([MR-J](../../samples/chm/extracted/mr-j_generate_purchase_orders.htm)) or manually ([PO-A](../../samples/chm/extracted/po-a_enter_purchase_orders.htm)).
- Generate RFQs ([MR-K](../../samples/chm/extracted/mr-k_generare_rfqs.htm) or [PO-E](../../samples/chm/extracted/po-e_enter_print_rfqs.htm)).

**Scheduling Existing Orders**
- Reorder Report to align PO receiving + WO finish dates ([IN-D](../../samples/chm/extracted/in-k_adjust_physical_levels.htm)).
- Sales Order / Work Order Schedule ([SO-O-G](../../samples/chm/extracted/so-o-g_print_sales_order_work_order_schedule.htm)).
- Scheduling programs: finite ([SH-E](../../samples/chm/extracted/sh-e_finite_scheduling.htm)), infinite ([SH-F](../../samples/chm/extracted/sh-f_infinte_scheduling.htm)), lead-time ([SH-P](../../samples/chm/extracted/sh-p_lead_time_scheduling.htm)).
- Work-center load viewing/printing ([SH-K](../../samples/chm/extracted/sh-k_view_work_center_load.htm), [SH-R](../../samples/chm/extracted/sh-r_work_center_scheduler.htm)).
- Adjust capacity at [RO-C](../../samples/chm/extracted/ro-c_enter_work_centers.htm); reschedule WO dates at [SH-A](../../samples/chm/extracted/sh-a_edit_wo_start_finish_dates.htm).
- Respond to **EXPEDITE** / **DELAY** messages from the Order Action
  Report ([MR-H](../../samples/chm/extracted/mr-h_print_order_action_report.htm)).
- Assign sequences to machines at [SH-D](../../samples/chm/extracted/sh-d_manually_schedule_machines.htm).

**Key planning reports:** Reorder Report (IN-D), Forecast (MR-B), WO
Schedule (SH-G), Machine Schedule (SH-J), Work Center Load (SH-I),
Order Action Report (MR-H).

### 7b. Manufacturing Database Maintenance

**Inventory management:**
- Set reorder levels / amounts / lead times ([IN-B](../../samples/chm/extracted/in-b_enter_inventory.htm) or [MR-D](../../samples/chm/extracted/mr-d_enter_mrp_parameters.htm)).
- Lead-time generator ([SH-N](../../samples/chm/extracted/sh-n_generate_lead_times.htm)).
- Cycle / selective counts or full physical ([IN-J](../../samples/chm/extracted/in-j_print_physical_check.htm), [IN-C](../../samples/chm/extracted/in-l-j_transfer_inventory.htm), [PHYSICAL INVENTORY](../../samples/chm/extracted/physical_inventory.htm)).

**Product specifications:**
- Standard costs ([IN-L-A](../../samples/chm/extracted/in-l-a_enter_standard_costs.htm), [IN-L-E](../../samples/chm/extracted/in-l-e_update_materoal_standard_costs.htm)).
- Bills of material ([BM-A](../../samples/chm/extracted/bm-a_ener_bills_of_material.htm)).
- Routing time standards ([RO-A](../../samples/chm/extracted/ro-a_enter_routings.htm)).
- Cost rollups ([BM-G](../../samples/chm/extracted/bm-g_print_rollup_standard_costs.htm)).
- Estimating material costs ([ES-H](../../samples/chm/extracted/es-h_enter_material_costs.htm)).
- Work-center capacity/rates ([RO-C](../../samples/chm/extracted/ro-n_enter_test_requirements.htm)).

**Key reports:** MRP Parameters (MR-E), Physical Check (IN-J),
Inventory Value (IN-F), BOM (BM-B), Routings (RO-J-A), Costed BOM
(BM-G), Material Costs (ES-I), Work Centers (RO-J-B).

### 7c. Work Orders

Life cycle:
1. Create manually ([WO-A](../../samples/chm/extracted/wo-a_enter_work_orders.htm)), from SO ([SO-N](../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm)),
   from estimate ([ES-E](../../samples/chm/extracted/es-e_convert_estimates.htm)), or via MRP ([MR-I](../../samples/chm/extracted/mr-i_generate_work_orders.htm)).
2. Modify routing ([WO-K-A](../../samples/chm/extracted/wo-k-a_enter_work_order_routings.htm)) or BOM ([WO-K-B](../../samples/chm/extracted/wo-k-b_enter_work_order_bills_of_material.htm)) if needed.
3. Generate multi-date ([WO-K-C](../../samples/chm/extracted/wo-k-c_create_multi-date_work_orders.htm))
   or multi-assembly ([WO-K-D](../../samples/chm/extracted/wo-k-d_create_multi-assy_work_orders.htm)) WOs.
4. Release to shop floor ([WO-B](../../samples/chm/extracted/wo-b_release_work_orders.htm)).
5. Shop paper: travelers ([WO-C](../../samples/chm/extracted/wo-c_print_travelers.htm)), pick lists ([WO-D](../../samples/chm/extracted/wo-d_print_pick_lists.htm)),
   labor cards/labels ([WO-E](../../samples/chm/extracted/wo-e_print_labor_cards_labels.htm)).
6. PO materials to specific WOs ([PO-A](../../samples/chm/extracted/po-a_enter_purchase_orders.htm)).
7. Issue material from inventory ([WO-G](../../samples/chm/extracted/wo-g_issue_materials.htm)).
8. Enter labor: manually ([WO-M](../../samples/chm/extracted/wo-m_batch_labor_entry.htm), [WO-F](../../samples/chm/extracted/wo-f_enter_labor.htm)) or via Data
   Collection ([DC-A](../../samples/chm/extracted/dc-a_enter_labor_production.htm), [DC-C](../../samples/chm/extracted/dc-c_enter_labor_only.htm)). Batch-post labor if
   auto-post is off ([WO-N](../../samples/chm/extracted/wo-n_post_labor_batches.htm), [DC-H](../../samples/chm/extracted/dc-h_post_labor_transactions.htm)).
9. Misc / extra costs ([WO-H](../../samples/chm/extracted/wo-h_entermisc_extra_costs.htm)).
10. Report finished production; optionally backflush; optionally
    close WO ([WO-I](../../samples/chm/extracted/wo-i_enter_finished_production.htm)).
11. Close WO ([WO-J](../../samples/chm/extracted/wo-j_close_cancel_orders.htm)).

**Key reports:** WO Schedule (WO-L-B), Work Center Backlog (WO-L-C),
Work Center Schedule (SH-I), WO Status (WO-L-A), WO Shortages (WO-L-F).

### 7d. Purchase Orders

1. Enter manually ([PO-A](../../samples/chm/extracted/po-a_enter_purchase_orders.htm)), convert from RFQ ([PO-G](../../samples/chm/extracted/po-g_convert_rfqs.htm)),
   or generate via MRP ([MR-J](../../samples/chm/extracted/mr-j_generate_purchase_orders.htm)).
2. Print ([PO-B](../../samples/chm/extracted/po-b_print_purchase_orders.htm)).
3. Receive ([PO-C](../../samples/chm/extracted/po-c_receive_purchase_orders.htm)).
4. Close (if not using AP) ([PO-K](../../samples/chm/extracted/po-k_close_purchase_orders.htm)).
5. Or enter vendor invoices in AP ([AP-C](../../samples/chm/extracted/ap-c_enter_purchase_order_invoices.htm)) — this auto-closes the
   PO when fully received **and** invoiced.
6. Move QC → inventory if applicable ([PO-J-C](../../samples/chm/extracted/po-j-c_enter_inspection_buyoffs.htm)).

**Key reports:** Open PO Listing (PO-I-A), Received POs (PO-I-E).

### 7e. Sales Orders

1. Enter manually ([SO-A](../../samples/chm/extracted/so-a_enter_sales_orders.htm)), from invoice history ([SO-H](../../samples/chm/extracted/so-h_display_invoice_history.htm)),
   from sales quotations ([SO-P-C](../../samples/chm/extracted/so-p-c_convert_sales_quotations.htm)), or from estimate ([ES-E](../../samples/chm/extracted/es-e_convert_estimates.htm)).
2. Convert SO → WO ([SO-N](../../samples/chm/extracted/so-n_convers_sales_orders_to_work_orders.htm)) as needed.
3. Acknowledgments ([SO-B](../../samples/chm/extracted/so-b_print_acknowledgments.htm)).
4. Packing slips ([SO-C](../../samples/chm/extracted/so-c_print_packing_slips.htm)) and shipping labels ([SO-D](../../samples/chm/extracted/so-d_print_shipping_labels.htm)).
5. Release for invoicing ([SO-E](../../samples/chm/extracted/so-e_release_sales_orders.htm)).
6. Print invoices ([SO-F](../../samples/chm/extracted/so-f_print_invoices.htm)).
7. Post invoices ([SO-G](../../samples/chm/extracted/so-g_post_invoices.htm)).

**Key reports:** Open SO Listing (SO-O-A), Backorder Listing (SO-O-B),
Shipping Schedule (SO-O-E), Available to Ship (SO-O-F).

---

## 8. Important Times — Daily / Monthly / Yearly

*Source: [important_times.htm](../../samples/chm/extracted/important_times.htm)*

> "The importance of backing up your data files cannot be overstated."
> — the vendor, bluntly.

### Daily

- **Back up data files** (`*.B*`). Include every active company folder
  under `DBAMFG`, not just the default.
- Process SO / WO / PO, receivables, payables, PO Invoice recon.
- Planning: scheduling, material requirements, forecasting.
- Update inventory management, product specs.
- **Run
  [GL-O Print/Post General Ledger Batches](../../samples/chm/extracted/gl-o_print_post_general_ledger_baches.htm)
  every day.** Easier to review/correct than letting a week pile up.
  No need to "close" a prior month before posting new-month entries —
  GL posts to the period matching each transaction's posting date.

### Monthly

For full detail see §9 (Month End Accounting) below. Summary:

- Full backup of programs + data; archive offsite.
- **AR Aging** ([AR-F](../../samples/chm/extracted/ar-f_print_aging.htm)) answering N to deposits → matches AR GL account.
- **AP Aging** ([AP-I](../../samples/chm/extracted/ap-i_print_aging.htm)) answering N to deposits → matches AP GL account.
- **Inventory value** ([IN-F](../../samples/chm/extracted/in-l-j_transfer_inventory.htm)) as of month end → matches inventory GL; adjust via [GL-B](../../samples/chm/extracted/gl-b_enter_post_general_journal_trxns.htm) if needed.
- **PO Received not Invoiced** ([PO-I-F](../../samples/chm/extracted/po-i-f_print_received_not_invoiced.htm)) → matches that GL account.
- **WIP Summary** ([JC-M](../../samples/chm/extracted/jc-m_print_wip_summary.htm)) → matches WIP GL.
- Charge interest on past-due ([AR-D](../../samples/chm/extracted/ar-d_charge_interest_on_invoices.htm)). Print/mail statements ([AR-E](../../samples/chm/extracted/ar-e_print_statements.htm)).
- Generate recurring/reversing JEs ([GL-B](../../samples/chm/extracted/gl-b_enter_post_general_journal_trxns.htm)), recurring sales
  orders ([SO-K](../../samples/chm/extracted/so-k_generate_recurring_sales_order.htm)), recurring AP vouchers ([AP-P](../../samples/chm/extracted/ap-p_generate_recurring_vouchers.htm)).
- Transfer sales taxes to AP ([AR-L](../../samples/chm/extracted/ar-l_transfer_sales_taxes.htm)); sales commissions to payroll + AP ([CS-D](../../samples/chm/extracted/cs-d_transfer_sales_commissions.htm)).
- Reconcile on-hand ([SM-J-C](../../samples/chm/extracted/sm-j-c_reconcile_inventory_on_hand.htm)).
- Month-end adjustments (depreciation etc.) via [GL-B](../../samples/chm/extracted/gl-b_enter_post_general_journal_trxns.htm).
- Optionally archive AP / AR / closed SO / closed WO / closed PO (see §9 + §10).
- Reset GL close date ([AM-A](../../samples/chm/extracted/am-a_reset_general_ledger_close_date.htm)).
- Reconcile check register ([GL-J](../../samples/chm/extracted/gl-j_reconcile_check_register.htm)); print ([GL-I](../../samples/chm/extracted/gl-i_print_check_register.htm)) → match each
  checking account's GL balance.
- Review Detailed Trial Balance ([GL-E](../../samples/chm/extracted/gl-h_print_chart_of_accounts.htm)) and Journals ([GL-D](../../samples/chm/extracted/gl-d_print_journals.htm)).
- Print financials ([GL-F](../../samples/chm/extracted/gl-o_print_post_general_ledger_baches.htm), [GL-N](../../samples/chm/extracted/gl-n_print_custom_financial_statements.htm)).

### Calendar Year End

- Full backup, archive offsite.
- Print **1099s** in early January for qualifying vendors.
- Clear monthly sales-commission totals, roll unpaid to new January
  ([CS-Q](../../samples/chm/extracted/cs-q_commission_year_end_routine.htm)).
- Optionally archive: AP vouchers ([AM-J](../../samples/chm/extracted/am-j_archive_purge_ap_history.htm)), customer payments ([AM-K](../../samples/chm/extracted/am-k_archive_purge_ar_history.htm)),
  closed SOs ([SM-J-J](../../samples/chm/extracted/sm-j-j_purge_closed_sales_orders.htm)), closed WOs ([SM-J-B](../../samples/chm/extracted/sm-j-b_archive_work_orders.htm)),
  closed POs ([SM-J-R](../../samples/chm/extracted/sm-j-r-archive_purchase_orders.htm)), inactive vendors ([AM-O](../../samples/chm/extracted/am-o_archive_purge_vendor_data.htm)),
  inactive customers ([AM-P](../../samples/chm/extracted/am-p_archive_purge_customer_data.htm)).

### Calendar Year End — Payroll

- **Run [PR-O Year End Routine](../../samples/chm/extracted/pr-o_year_end_routine.htm) before the first payroll of the
  new calendar year.**
- Print **W-2s** in early January ([PR-L-I](../../samples/chm/extracted/pr-l-i_print_w-2_forms.htm)).
- Update tax tables ([PR-F](../../samples/chm/extracted/pr-f_maintain_tax_tables.htm)) and verify **FICA / SDI** at
  [PR-M Payroll Defaults](../../samples/chm/extracted/pr-m_payroll_division_defaults.htm) — **only after W-2s are run.**

### Fiscal Year End

- Full backup of programs + files, archive offsite.
- Run [AM-B Fiscal Year End Routine](../../samples/chm/extracted/am-b_fiscal_year_end_routine.htm) on **day one** of the new
  fiscal year.
- Enter new-year budget via [AM-Q Enter Budget Information](../../samples/chm/extracted/am-q_enter_budget_information.htm).

---

## 9. Month End Accounting — Detail

*Source: [month_end_accounting.htm](../../samples/chm/extracted/month_end_accounting.htm)*

**There is no hard monthly close.** You can post freely to any period
in the current year or up to **six years** past. Instead, a **GL Open
Period Start Date** gates what non-privileged users can post to. Set
via [AM-A Reset General Ledger Close Date](../../samples/chm/extracted/am-a_reset_general_ledger_close_date.htm); can be temporarily
moved to make a late adjustment and then restored.

**The Open Period Start Date is the closest thing to a "close"** — but
it's an access gate, not a transformation of data. Accounting can be
left open for GL / AP voucher entry / optionally AR payments while
the rest of the org sees the period as closed.

### Recommended month-end sequence (verbatim order from the help)

1. **Full backup** (programs + data), archive offsite.
2. **Print control reports** — each runs as-of the month end date, so
   they can be printed after you've started transacting in the new
   month.

| Control report | Ties out against |
|---|---|
| [IN-F Inventory Value](../../samples/chm/extracted/in-l-j_transfer_inventory.htm) + [PO-J-B Inventory in QC](../../samples/chm/extracted/po-j-b_printinventory_in_qc.htm) | Inventory GL account(s). If off, run [UT-K-G Recalc Inventory Book Value](../../samples/chm/extracted/ut-k-g_recalc_inventory_book_value.htm) and JE the delta. |
| [PO-I-F Received not Invoiced](../../samples/chm/extracted/po-i-f_print_received_not_invoiced.htm) + [PO-J-B](../../samples/chm/extracted/po-j-b_printinventory_in_qc.htm) | POs Received not Invoiced GL. |
| [AR-F Print Aging](../../samples/chm/extracted/ar-f_print_aging.htm) N to deposits | AR GL. |
| [AR-F](../../samples/chm/extracted/ar-f_print_aging.htm) **O**nly deposits | Customer Deposits GL. |
| [JC-M WIP Summary](../../samples/chm/extracted/jc-m_print_wip_summary.htm) (as-of populates the date fields — **do not change them**) | WIP GL. |
| [AP-I Print Aging](../../samples/chm/extracted/ap-i_print_aging.htm) N to deposits | AP GL. |
| [AP-I](../../samples/chm/extracted/ap-i_print_aging.htm) **O**nly deposits | PO Deposits GL. |
| [GL-I Check Register](../../samples/chm/extracted/gl-i_print_check_register.htm) — Uncleared Only through month end (after bank recon) | Each checking-account GL. |

3. **Typical month-end activities** (charge interest, statements,
   recurring JEs, recurring SOs, recurring AP vouchers, transfer
   sales taxes / commissions, reconcile on-hand, recalc inventory
   book value, month-end adjustments, optional archive/purge,
   reconcile check register). These are the same items as the
   "Monthly" list in §8, but now with the control-report cross-tie
   done first.

4. **Manufacturing adjustments — three variances.** All posted via
   [GL-B](../../samples/chm/extracted/gl-b_enter_post_general_journal_trxns.htm) and [GL-O](../../samples/chm/extracted/gl-o_print_post_general_ledger_baches.htm).

| Variance | Compared against | Adjusts |
|---|---|---|
| **Labor Variance** | Actual direct labor vs Absorbed Labor | WIP Variance + Labor Variance (both expense, adjacent to COGS) |
| **Fixed Overhead Variance** | Actual fixed OH vs Absorbed Fixed OH | WIP Variance + Fixed Overhead Variance (expense, following Labor Variance in COGS section) |
| **Variable Overhead Variance** | Actual variable OH vs Absorbed Variable OH | WIP Variance + Variable Overhead Variance (expense, following Fixed OH Variance in COGS section) |

5. **Reset GL Open Period Start & End Date** via [AM-A](../../samples/chm/extracted/am-a_reset_general_ledger_close_date.htm) if desired.
6. **Print financials** ([GL-F](../../samples/chm/extracted/gl-o_print_post_general_ledger_baches.htm) or [GL-N](../../samples/chm/extracted/gl-n_print_custom_financial_statements.htm)).

---

## 10. Archiving or Purging Old Data

*Source: [archiving_or_purging_old_data.htm](../../samples/chm/extracted/archiving_or_purging_old_data.htm)*

**Always take a full program+data backup** before any purge or
consolidation, on permanent media (DVD) stored offsite. Purge and
consolidate are **one-way**; archive just moves data to a separate
file (Archive programs have a restore option).

**After any purge / archive / consolidate**, reindex the affected
files using **UT-C** or the **Pervasive Rebuild Utility** to reclaim
disk space.

**The 2 GB file limit.** If any single data file reaches 2 GB, EvoERP
programs that touch it **stop working**. Check periodically via
Explorer (sort by size). To lift the limit: **Pervasive Control Center
→ Configure Local Engine → Performance Tuning → uncheck
"Limit Segment size to 2 GB"**. Stop and restart the Pervasive service
(all users out) for the change to take effect.

### What each archive/purge program does

| Program | Operates on | Files to reindex after |
|---|---|---|
| [SM-J-J Sales Orders](../../samples/chm/extracted/sm-j-j_purge_closed_sales_orders.htm) | Closed SO skeletons (receivables + shipment history untouched). Speeds up SO-O reports (except SO-O-H), Stock Status rebuild, IN-A, MRP. Archived orders viewable via SO-O-J / SO-O-K. | BKARINV, BKARINVL, BKARDESC |
| [SM-J-K Invoices](../../samples/chm/extracted/sm-j-j_purge_or_archive_invoice_history.htm) | Old invoices. Speeds up SA reports. Active Shipment file stays in IN-A/AR-A; archived data has its own button. SA-M/SA-N have an Active/Archived toggle. | BKARHINV, BKARHIVL, BKARHDSC, BKSOHSER, BKSOHLOT |
| [SM-J-B Work Orders](../../samples/chm/extracted/sm-j-b_archive_work_orders.htm) | Closed WOs. Recommended **monthly/quarterly**. JC reports can target Active or Archived. Speeds up Stock Status rebuild, IN-A, MRP. | Active: WORKORD, WOBOM, WOROUT, WOMAT, WOLABOR, WORECV, OUTPROC, WOEXCHG, WODATE. After purging Archived: WORKHORD, WOHBOM, WOHROUT, WOHMAT, WOHLABOR, WOHRECV, OUTHPROC, WOHEXCHG, WOHDATE |
| [SM-J-R Purchase Orders](../../samples/chm/extracted/sm-j-r-archive_purchase_orders.htm) | Closed POs. Speeds up PO-I-F. | BKAPHPO, BKAPHPOL |
| [SM-J-D Inventory Transactions](../../samples/chm/extracted/sm-j-d_consolicate_invventory_transactions.htm) | Consolidates detail to one net transaction per month × part × txn type. **Irreversible.** Lot/Serial txns are **not** consolidated. | INVTXN |
| [AM-I GL Transactions](../../samples/chm/extracted/am-i_consolidate_gl_detail.htm) | Consolidates to net debit + net credit per month × account × journal type, for date/account/journal ranges. **Irreversible.** | BKGLTRAN |
| [AM-J Accounts Payable (date)](../../samples/chm/extracted/am-j_archive_purge_ap_history.htm) | Voucher / invoice / payment detail for invoices fully paid as of specified date. AP-R has Active/Archived toggle. | BKAPINVT, BKAPINVL, BKAPCHKH |
| [AM-O Accounts Payable (vendor)](../../samples/chm/extracted/am-o_archive_purge_vendor_data.htm) | All AP + PO detail for vendors inactive since a date. Supports range by Vendor Code / Class. | BKAPINVT, BKAPINVL, BKAPCHKH, BKAPHPO, BKAPHPOL, BKAPVEND |
| [AM-K Accounts Receivable (date)](../../samples/chm/extracted/am-k_archive_purge_ar_history.htm) | Voucher / invoice / payment detail for invoices fully paid as of date. AR-R has Active/Archived toggle. | BKARINVT, BKARINVV, BKARCHKF |
| [AM-P Accounts Receivable (customer)](../../samples/chm/extracted/am-p_archive_purge_customer_data.htm) | All AR + sales/shipment for inactive customers. Range by Customer Code / Class. | BKARINVT, BKARINVV, BKARCHKF, BKARINV, BKARINVL, BKARHINV, BKARHIVL |
| [SM-J-P Service/Repair & RMA](../../samples/chm/extracted/sm-j-p_purge_archive_service_rma_orders.htm) | Closed S/R & RMA skeletons (receivables + shipment history untouched). Speeds up SO-O (except SO-O-H), Stock Status rebuild, IN-A. Archived viewable at SO-O-J / SO-O-K. | ISSRINV, ISSRINVL, ISSRINFO, ISSRMMS, ISRMAI, ISSRDESC |
| SM-J-T Sales Quotes | Closed sales quotes. Purge = gone. Archive is restorable. | BKESTQT, BKESTQTL |
| SM-J-S Inventory Audit Info | Part-number change history in ISICADT + ISMICADT. Grows fast with Std Cost rollups. Filter by date / item range / source. | ISICADT, ISMICADT |

---

## 11. File Names

*Source: [file_names.htm](../../samples/chm/extracted/file_names.htm)*

The help file lists the physical filename of every data table, grouped
by module. Data files use `*.B` (default company) or `*.Bxx` (other
companies). **To get current per-field layout of any of these files,
run [UT-H Print File Layouts](../../samples/chm/extracted/ut-h_print_file_layouts.htm)** — it lists all field names and
properties.

The full list (~320+ tables) lives in its own doc so it can be
indexed / searched / cross-linked independently:

**→ [File Names — complete table index](../04-data-dictionary/file-names-index.md)**

---

## Cross-links in this workspace

- [What EvoERP is, at a glance](what-is-evoerp.md) — LearnEVO's own
  stack summary (complements §1 here).
- [Help system topology](help-system.md) — how the CHM itself is
  structured / indexed.
- [External ODBC connections](../01-architecture/external-odbc-connections.md)
  — deep dive on §6 above.
- [Menu system overview](../06-menu-system/overview.md) — every
  `XX-Y-Z` code referenced here is documented there.
- [Per-module pages](../README.md#per-module-deep-dive-pages-each-joins-menu-codes--schema--ui-forms)
  — AR / AP / IN / SO / PO / WO / GL / PR / etc.
