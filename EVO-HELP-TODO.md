# EVO-HELP-TODO

Tracks documentation progress against the **EvoHELP.CHM** table of
contents (`\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM`, decompiled to
[samples/chm/extracted/](samples/chm/extracted/)).

The CHM has **14 top-level categories**. For each one, we're
consolidating the vendor's help text into our own LearnEVO docs,
cross-linking to menu codes, forms, and schema as we go.

Status key: ✅ done · 🟡 in progress · ⬜ not started.

---

## Top-level categories

- [x] **System Overview** ✅ — 11 subtopics consolidated into
      [docs/00-overview/system-overview.md](docs/00-overview/system-overview.md).
      File-names list split out to
      [docs/04-data-dictionary/file-names-index.md](docs/04-data-dictionary/file-names-index.md).
  - [x] Evo-ERP and DBA Help File (welcome)
  - [x] Installation
  - [x] Using Terminal Server and Citrix
  - [x] Setting up Printing
  - [x] Using Multiple Companies
  - [x] ODBC Data Connection
  - [x] Sequence of Events
  - [x] Important Times
  - [x] Archiving or Purging Old Data
  - [x] Month End Accounting
  - [x] File Names

- [x] **Manufacturing** ✅ — 8 subtopics consolidated.
  - [x] Work Orders (WO-*) ✅ — [docs/03-modules/wo-work-orders/help-content.md](docs/03-modules/wo-work-orders/help-content.md) *(52 CHM topics consolidated)*
  - [x] Job Costing (JC-*) ✅ — [docs/03-modules/jc-job-costing/help-content.md](docs/03-modules/jc-job-costing/help-content.md) *(20 CHM topics consolidated)*
  - [x] Purchase Orders (PO-*) ✅ — [docs/03-modules/po-purchase-orders/help-content.md](docs/03-modules/po-purchase-orders/help-content.md) *(27 CHM topics consolidated)*
  - [x] Material Requirements (MR-*, MRP) ✅ — [docs/03-modules/mr-mrp/help-content.md](docs/03-modules/mr-mrp/help-content.md) *(14 CHM topics consolidated)*
  - [x] Scheduling (SH-*) ✅ — [docs/03-modules/sh-shipping/help-content.md](docs/03-modules/sh-shipping/help-content.md) *(22 CHM topics consolidated)* · *folder name is a legacy mislabel; module is Scheduling*
  - [x] Data Collection (DC-*) ✅ — [docs/03-modules/dc-data-collection/help-content.md](docs/03-modules/dc-data-collection/help-content.md) *(14 CHM topics consolidated)*
  - [x] Estimating (ES-*) ✅ — [docs/03-modules/es-estimating/help-content.md](docs/03-modules/es-estimating/help-content.md) *(10 CHM topics consolidated)*
  - [x] Quality (QC) ✅ — [docs/03-modules/qc-quality-control/help-content.md](docs/03-modules/qc-quality-control/help-content.md)

- [x] **Items** ✅ — 8 subtopics consolidated.
  - [x] Inventory (IN-*) ✅ — docs/03-modules/in-inventory/help-content.md (38 CHM topics)
  - [x] Routings (RO-*) ✅ — docs/03-modules/ro-routings/help-content.md (22 CHM topics)
  - [x] Bills of Material (BM-*) ✅ — docs/03-modules/bm-bill-of-materials/help-content.md (16 CHM topics)
  - [x] Lot Control (LC-*) ✅ — docs/03-modules/lc-lot-control/help-content.md (6 CHM topics)
  - [x] Serial Control (SC-*) ✅ — docs/03-modules/sc-serial-control/help-content.md (8 CHM topics)
  - [x] Features & Options (FO-*) ✅ — docs/03-modules/fo-features-options/help-content.md (5 CHM topics)
  - [x] Physical Inventory (PI-*) ✅ — docs/03-modules/pi-physical-inventory/help-content.md (8 CHM topics)
  - [x] Warehouse Control (WC-*) ✅ — docs/03-modules/wc-warehouse-control/help-content.md (5 CHM topics)

- [x] **Sales** ✅ — 7 subtopics consolidated (no RMA CHM content found).
  - [x] Sales Orders (SO-*) ✅ — [docs/03-modules/so-sales-orders/help-content.md](docs/03-modules/so-sales-orders/help-content.md) *(51 CHM topics consolidated)*
  - [x] Service and Repair (SR-*) ✅ — [docs/03-modules/sr-service-repair/help-content.md](docs/03-modules/sr-service-repair/help-content.md) *(8 CHM topics consolidated)*
  - [ ] RMA ⬜ — no CHM source content found in extracted files
  - [x] Sales Analysis (SA-*) ✅ — [docs/03-modules/sa-sales-analysis/help-content.md](docs/03-modules/sa-sales-analysis/help-content.md) *(18 CHM topics consolidated)*
  - [x] Sales Commissions (CS-*) ✅ — [docs/03-modules/cs-commission-system/help-content.md](docs/03-modules/cs-commission-system/help-content.md) *(15 CHM topics consolidated)*
  - [x] Contact Manager (CM-*) ✅ — [docs/03-modules/cm-contact-manager/help-content.md](docs/03-modules/cm-contact-manager/help-content.md) *(8 CHM topics consolidated)*
  - [x] Accounts Receivable (AR-*) ✅ — [docs/03-modules/ar-accounts-receivable/help-content.md](docs/03-modules/ar-accounts-receivable/help-content.md) *(16 CHM topics consolidated)*
  - [x] Contract Review (CR-*) ✅ — [docs/03-modules/cr-contract-review/help-content.md](docs/03-modules/cr-contract-review/help-content.md) *(2 CHM topics consolidated)*

- [x] **Queries & Reports** ✅ — 2 subtopics consolidated.
  - [x] Queries (QU-*) ✅ — [docs/03-modules/qu-queries/help-content.md](docs/03-modules/qu-queries/help-content.md) *(7 CHM topics: overview + QU-A through QU-F)*
  - [x] Setup Queries & Reports ✅ — covered in QU-F (Query Executor) above

- [x] **Hand Held Data Collection** ✅ — 15 CHM topics consolidated.
  - [x] How to Use Paperless Shop Floor Tracking ✅
  - [x] HH-A Scan & Ship ✅
  - [x] HH-B Print Bar Code Labels ✅
  - [x] HH-C Issue Materials ✅
  - [x] HH-D Enter Finished Production ✅
  - [x] HH-E Enter PI Tag Counts ✅
  - [x] HH-F Enter Labor ✅
  - [x] HH-G Receive Purchase Order ✅
  - [x] HH-H Enter Shipping Information ✅
  - [x] HH-I Paperless Shop Floor Tracking ✅
  - [x] HH-J Print Work Order Label ✅
  - [x] HH-K Transfer Inventory ✅
  - [x] HH-L Multi-user Paperless Shop Floor ✅
  - [x] HH-M Issue Scrap Component ✅
  All consolidated into [docs/03-modules/hh-handheld/help-content.md](docs/03-modules/hh-handheld/help-content.md)

- [ ] **System Manager** ⬜ — 7 subtopics.
  - [ ] Utilities (UT-*)
  - [ ] System Maintenance (SM-*)
  - [ ] System Defaults (SD-*)
  - [ ] International Module
  - [ ] Password Security (PS-*)
  - [ ] Data Exchange (DE-*)
  - [ ] TAS Utility Programs

- [ ] **Accounting** ⬜ — 5 subtopics.
  - [ ] General Ledger (GL-*)
  - [ ] Accounts Payable (AP-*)
  - [ ] Fixed Assets
  - [ ] Accounting Maintenance (AM-*)
  - [ ] Accounting Defaults (AD-*)

- [ ] **Payroll** ⬜ — ~34 subtopics (PR-A through PR-S + quarterly/year-end routines + state-specific tax calc).
  - [ ] PR-A through PR-S (core programs)
  - [ ] PR-L-A through PR-L-Q (quarterly / annual reports)
  - [ ] Payroll Tax Calculation by State
  - [ ] PR-O Year End Routine
  - [ ] PR-M/PR-R Defaults

- [ ] **Settings** ⬜ — 8 subtopics (US-A … US-H).
  - [ ] US-A Customize Settings
  - [ ] US-B Customize Menu
  - [ ] US-C Reset Screen Size/Location
  - [ ] US-D Reset Password
  - [ ] US-E Update PO Electronic Signature Info
  - [ ] US-F Enter Reminders
  - [ ] US-G Enter Triggers
  - [ ] US-H Update Contract Review Password

- [ ] **Main Menu (Support) Programs** ⬜ — 3 subtopics.
  - [ ] Check for Updates
  - [ ] Send Files
  - [ ] Send Screen Print

- [ ] **Main Menu (File) Programs** ⬜ — 2 subtopics.
  - [ ] Maintain Database
  - [ ] Report Editor

- [x] **Evo-ERP Tools** ✅ — 4 subtopics consolidated into
      [docs/00-overview/evo-erp-tools.md](docs/00-overview/evo-erp-tools.md).
  - [x] Users Tool
  - [x] Size Tool
  - [x] Google Calendar
  - [x] Evo Notes Search

- [ ] **Glossary** ⬜ — single terminology reference page.

---

## How to work the list

1. Pick the next ⬜ category (prefer the one that unblocks the most
   per-module pages in [docs/03-modules/](docs/03-modules/)).
2. Run the extractor: `python scripts/chm_to_md.py <topic>.htm …`.
3. Consolidate into the appropriate `docs/…` folder (not
   necessarily `docs/00-overview/` — a per-module writeup may
   belong under `docs/03-modules/<xx>/` instead).
4. Update [docs/README.md](docs/README.md) index.
5. Update status here (⬜ → 🟡 → ✅) and tick the child boxes.
6. Commit.

## Notes

- **779 topic pages** total in the CHM. Top-level category count
  is 14; System Overview accounts for 11 of them. The remaining 13
  categories together cover the other 768 pages.
- CHM TOC raw source: [samples/chm/extracted/EVOHELP.hhc](samples/chm/extracted/EVOHELP.hhc).
- Keyword index: [samples/chm/extracted/EVOHELP.hhk](samples/chm/extracted/EVOHELP.hhk).
- Some categories overlap with existing per-module pages (e.g.
  Accounts Receivable already has
  [docs/03-modules/ar-accounts-receivable/](docs/03-modules/ar-accounts-receivable/)) —
  merge rather than duplicate.
- **Completed as of 2026-06-01:** System Overview, Manufacturing (all 8 subtopics),
  Items (all 8 subtopics), Sales (7 of 8 subtopics — RMA has no CHM source content),
  Queries & Reports, Hand Held Data Collection (15 CHM topics), Evo-ERP Tools.
  Remaining: System Manager, Accounting, Payroll, Settings, Main Menu (Support) Programs,
  Main Menu (File) Programs, Glossary.
