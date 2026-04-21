# EvoERP Documentation Plaza — Index

## 🚀 Launch the interactive help browser

**→ Open [`../learnevo-help/launch.bat`](../learnevo-help/launch.bat)** ←

Runs a local HTTP server and opens a full browser-based help system with:
- **2,718 cross-linked pages** (17 topics, 45 recipes, 22 modules, 36 glossary entries, 759 menu codes, 659 database tables, 1,109 UI forms, 71 other)
- **18,799-token full-text search** with keyword synonyms (`customer` → all AR-related pages; `AP-H` → jumps straight to Print Checks)
- Keyboard shortcuts (`Ctrl+K` search, `g h` home, arrow-keys to navigate results)
- Sidebar navigation grouped by section
- Inbound/outbound link graph on every page

See [learnevo-help/README.md](../learnevo-help/README.md) for details and how to extend.

---

Status: growing. Every session adds more detail. If a topic isn't listed
here, it hasn't been investigated yet — see `../research/OPEN_QUESTIONS.md`.

## Read-first rules
- See [../CLAUDE.md](../CLAUDE.md). Scope: no writes to `C:\ISTS` or
  `\\i2s109-solidcrm`. Ever.

## Table of contents

### 00 — Overview
- [What EvoERP is, at a glance](00-overview/what-is-evoerp.md)
- [EvoHELP.CHM — authoritative topic index](00-overview/help-system.md) — *verified, 779 topics*
- [Master index — every operation, one table (menu + help + forms)](00-overview/master-index.md) — *verified, 759 ops*

### 01 — Architecture
- [High-level architecture (runtime, data, UI layers)](01-architecture/overview.md) — *draft*
- [Security, login, and company selection](01-architecture/security-and-login.md) — *draft*
- [Java integration via `EvoPVT.jar` + `ISJAVA` task queue](01-architecture/java-integration.md) — *verified*
- [Supporting subsystems (Notes, Scheduler, Service, DC, Links, FNO, Update, …)](01-architecture/subsystems.md) — *draft*

### 02 — File formats
- [File format catalog (all extensions seen in EVO)](02-file-formats/catalog.md)
- [.SRC — TAS Pro 4GL source language](02-file-formats/src-tas-pro-language.md) — *draft*
- [.DFM — Delphi form format (plaintext)](02-file-formats/dfm-delphi-forms.md) — *draft*
- [.DCY / .RWN — compiled proprietary binaries](02-file-formats/dcy-rwn-binaries.md) — *partially decrypted*
- [.DCY / .RWN — decryption findings (Twofish-CFB, block-0 cracked)](02-file-formats/decryption-findings.md) — *partial, key not recovered*
- [.RTM / .btm — Nevrona ReportBuilder templates](02-file-formats/rtm-reportbuilder.md) — *verified*
- [.IMP / .UPD / .XPT / others](02-file-formats/other-formats.md) — *verified*

### 03 — Modules
- [Module naming (T6/T7 prefixes, AR/AP/IN/SO/PO/WO/GL)](03-modules/naming-and-inventory.md) — *draft*
- [DFM form inventory — every UI form, grouped by module](03-modules/dfm-form-inventory.md) — *verified, 1109 forms parsed*
- [Plaintext SRC deep-dive — reading the 7 legacy sources](03-modules/src-deep-dive.md) — *verified*

**Per-module deep-dive pages** (each joins menu codes + schema + UI forms):
- [AR — Accounts Receivable](03-modules/ar-accounts-receivable/README.md) (17 menu / 24 forms / 29 tables)
- [AP — Accounts Payable](03-modules/ap-accounts-payable/README.md) (19 / 33 / 26)
- [IN — Inventory](03-modules/in-inventory/README.md) (40 / 67 / 19)
- [SO — Sales Orders](03-modules/so-sales-orders/README.md) (48 / 69 / 7)
- [PO — Purchase Orders](03-modules/po-purchase-orders/README.md) (29 / 41 / 8)
- [WO — Work Orders](03-modules/wo-work-orders/README.md) (31 / 68 / 30)
- [GL — General Ledger](03-modules/gl-general-ledger/README.md) (16 / 24 / 28)
- [BM — Bill of Materials](03-modules/bm-bill-of-materials/README.md) (10 / 16 / 10)
- [MR — MRP](03-modules/mr-mrp/README.md) (12 / 18 / 4)
- [PR — Payroll](03-modules/pr-payroll/README.md) (29 / 40 / 16)
- [DC — Data Collection](03-modules/dc-data-collection/README.md) (7 / 26 / 7)
- [QC — Quality Control](03-modules/qc-quality-control/README.md) (0 / 15 / 2)
- [JC — Job Costing](03-modules/jc-job-costing/README.md) (18 / 14 / 2)
- [CS — Commission System](03-modules/cs-commission-system/README.md) (16 / 12 / 16)
- [ES — Estimating](03-modules/es-estimating/README.md) (8 / 7 / 4)
- [SR — Service / Repair](03-modules/sr-service-repair/README.md) (9 / 12 / 0)
- [PI — Physical Inventory](03-modules/pi-physical-inventory/README.md) (9 / 10 / 7)
- [SH — Shipping](03-modules/sh-shipping/README.md) (16 / 15 / 1)
- [ED — EDI](03-modules/ed-edi/README.md) (6 / 3 / 6)
- [SM — System Manager / Setup](03-modules/sm-system-manager/README.md) (34 / 109 / 10)

### 04 — Data dictionary
- [Data dictionary overview — 649 tables, Pervasive DDF set](04-data-dictionary/overview.md) — *draft*

### 05 — Reports (ReportBuilder .RTM)
- [Reporting pipeline overview + RTM cross-reference](05-reports/overview.md) — *verified*

### 06 — Menu system
- [Menu system overview — 554 codes across 38 modules](06-menu-system/overview.md) — *verified*

### 07 — Runtime & boot sequence
- [How EVO starts up (StartEvo.exe → tp7runtime.exe → EvoERPmenu.rwn)](07-runtime-boot/boot-sequence.md) — *draft*

---

## Legend
- *draft* — first pass, some claims not yet verified.
- *verified* — every claim has a cited source in the EVO files.
- *open-questions* — important gaps documented in `research/OPEN_QUESTIONS.md`.
- *partial* — covers some aspects but known to be incomplete.
