# EvoHELP.CHM — The Authoritative Topic Index

Status: verified — extracted from
`\\I2S109-SOLIDCRM\DBAMFG$\EvoHELP.CHM` (1.7 MB, Microsoft HTML Help
ITSF format).

## What the CHM contains

A compressed archive of **779 `.htm` topics** (individual help pages)
plus a hierarchical table of contents. Two kinds of pages live inside:

- **Per-menu-code pages** — 636 of them. Filename format
  `<code>_<slug>.htm`. Example: `ap-h_print_checks.htm`.
- **Conceptual / "chapter" pages** — 90 of them. Filename format
  `<topic>.htm`. Example: `sales_orders.htm`,
  `multi_currency_processing_chart.htm`.

Copy of the help file: `../../samples/chm/EvoHELP.CHM`. Raw strings
dump: `../../samples/chm/chm_strings.txt`. Menu→help-page CSV:
`../../samples/chm/menu_help.csv`.

## Why this matters for the documentation

The CHM is the **official** list of EVO functionality. Every menu code
we found in the RUN-file strings has a help page — but the CHM has
**82 extra menu codes** that are not in our `.RUN` dump (636 vs 554).
Those likely fall into three buckets:

1. **Recent additions** that only exist as encrypted `.RWN` and
   not in any `.RUN`.
2. **Customer-specific / optional features** the installed copy
   doesn't use.
3. **Older features** removed from the code base but kept in the help
   for legacy users.

## The 90 conceptual chapters

Full list (all `.htm` filenames under the CHM root without a menu-code
prefix):

### Accounting

- `accounting_defaults` — the three `AD-A/B/C` default-setting pages
- `accounting_maintenance` — `AM-*` archive / fiscal-year operations
- `accounts_payable`
- `accounts_receivable`
- `archiving_or_purging_old_data`
- `general_ledger`
- `month_end_accounting`
- `sales_commissions` / `extended_commissions`
- `sales_analysis`

### Inventory & manufacturing

- `inventory` / `configuring_items`
- `bills_of_material` / `edit_bom_tree_view`
- `routings` / `size_tool`
- `material_requirements`
- `work_orders`
- `job_costing`
- `physical_inventory`
- `lot_control` / `serial_control`
- `quality`
- `data_collection` / `hand_held_data_collection` /
  `how_to_use_paperless_shop_floor_tracking`
- `scheduling` / `how_finite_scheduling_works` /
  `how_infinite_scheduling_works` / `how_lead_time_scheduling_works` /
  `how_manual_scheduling_works`
- `warehouse_control`
- `estimating` / `estimaing` (sic — both spellings) / `estimating_files`
- `fixed_assets` — *a module we hadn't catalogued yet*
- `multiple_currency_startup` / `multi_currency_processing_chart` /
  `international_module`
- `bkact_inactive_inventory_program`
- `bkrebwo_rebuild_work_order_costs`

### Sales / CRM

- `sales_orders` / `using_a_sales_order_system` /
  `using_features_and_options_in_sales_orders`
- `contact_manager` / `contact_manager_setup`
- `contract_review`
- `how_to_use_rma`
- `how_to_use_service_and_repair` / `service_and_repair`

### Purchase / supplier

- `purchase_orders`
- `how_to_use_approved_vendors_and_manufacturers`

### Infrastructure

- `password_security` — confirms the security model
- `settings` / `setting_up_features_and_options` / `setting_up_printing`
- `users_tool`
- `system_defaults` / `system_maintenance`
- `installation` / `maintain_database`
- `using_multiple_companies` / `how_to_use_multiple_locations`
- `using_terminal_server_and_citrix`
- `odbc_data_connection` — confirms ODBC SQL is a documented feature
- `send_files` / `send_screen_print`
- `check_for_updates`
- `utilities`
- `data_exchange` / `importing_manufacturing_data` /
  `importing_master_files`
- `in_l_p_image_link_utility`
- `google_calendar` — Google Calendar sync feature
- `using_evo_links`
- `using_evo_notes` / `evo_notes_search`
- `ta_c_set_configuration` — `TA-C` is the configuration entry point
- `sequence_of_events`
- `important_times`
- `features_and_options`
- `main_menu_file_programs`
- `file_names`
- `payroll` / `payroll_tax_calculation_by_state`
- `report_editor`
- `queries_and_reports`

### Meta

- `evoerp_help_file` — the "about the help file" page
- `glossary`
- `cshelp` — context-sensitive help

## Things discovered that weren't in our module map

- **Fixed Assets** module (`fixed_assets.htm`) — not one of the top
  20 modules we catalogued. Likely tied to `BKFA*` tables (if they
  exist).
- **Contact Manager** — separate CRM-adjacent subsystem.
- **Google Calendar sync** — integration feature.
- **Terminal Server / Citrix** support — documented.
- **ODBC data connection** — end-user ODBC guide.

## How to read the CHM directly

`C:\Windows\hh.exe <path-to-chm>` opens it in the standard Windows
HTML Help viewer. Example:
`hh.exe "\\I2S109-SOLIDCRM\DBAMFG$\EvoHELP.CHM"`.

The runtime can also open it contextually; the `cshelp.htm` entry is
probably driven by pressing F1 on any EVO screen — the runtime passes
the current `prg_hdr` code (e.g. `AR-C`) through to the help system,
which opens `ar-c_record_payments.htm`.

## Things still to do

- Extract the full HTML content from the CHM (needs an unCHM tool:
  `chmlib`, `7z`, or Windows' `hh -decompile`). That would give us
  the **authoritative English description** of every EVO operation.
- Cross-reference each menu code in `../../samples/menu_codes.csv`
  with its help topic slug to ensure consistency.
- Build a single "EVO everything" master index joining:
  menu code ↔ RWN/RUN ↔ DFM form ↔ help topic ↔ tables touched.
