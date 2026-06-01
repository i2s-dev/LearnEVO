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

- [x] **Manufacturing** ✅ — 8 of 8 subtopics.
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

- [ ] **Sales** ⬜ — 8 subtopics.
  - [ ] Sales Orders (SO-*)
  - [ ] Service and Repair (SR-*)
  - [ ] RMA
  - [ ] Sales Analysis (SA-*)
  - [ ] Sales Commissions (CS-*)
  - [ ] Contact Manager (CM-*)
  - [ ] Accounts Receivable (AR-*)
  - [ ] Contract Review

- [ ] **Queries & Reports** ⬜ — 2 subtopics.
  - [ ] Queries
  - [ ] Setup Queries & Reports

- [ ] **Hand Held Data Collection** ⬜ — 14 subtopics (HH-A … HH-M + Paperless Shop Floor overview).
  - [ ] How to Use Paperless Shop Floor Tracking
  - [ ] HH-A Scan & Ship
  - [ ] HH-B Print Bar Code Labels
  - [ ] HH-C Issue Materials
  - [ ] HH-D Enter Finished Production
  - [ ] HH-E Enter PI Tag Counts
  - [ ] HH-F Enter Labor
  - [ ] HH-G Receive Purchase Order
  - [ ] HH-H Enter Shipping Information
  - [ ] HH-I Paperless Shop Floor Tracking
  - [ ] HH-J Print Work Order Label
  - [ ] HH-K Transfer Inventory
  - [ ] HH-L Multi-user Paperless Shop Floor
  - [ ] HH-M Issue Scrap Component

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
