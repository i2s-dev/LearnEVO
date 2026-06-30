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
- [System Overview — vendor's 11-part tour (install, companies, cadence, archiving)](00-overview/system-overview.md) — *verified, from EvoHELP.CHM*
- [Evo-ERP Tools — Tools menu utilities (Users, Size, Google Calendar, Notes Search)](00-overview/evo-erp-tools.md) — *verified, from EvoHELP.CHM*
- [EvoHELP.CHM — authoritative topic index](00-overview/help-system.md) — *verified, 779 topics*
- [Master index — every operation, one table (menu + help + forms)](00-overview/master-index.md) — *verified, 759 ops*

### 01 — Architecture
- [High-level architecture (runtime, data, UI layers)](01-architecture/overview.md) — *draft*
- [Security, login, and company selection](01-architecture/security-and-login.md) — *draft*
- [Java integration via `EvoPVT.jar` + `ISJAVA` task queue](01-architecture/java-integration.md) — *verified*
- [Supporting subsystems (Notes, Scheduler, Service, DC, Links, FNO, Update, …)](01-architecture/subsystems.md) — *draft*
- [Connecting external software to the EVO database (ODBC, DSN, bitness)](01-architecture/external-odbc-connections.md) — *verified*
- [Network topology, Pervasive SQL server mode, per-company databases](01-architecture/network-topology.md) — *verified*

### 02 — File formats
- [File format catalog (all extensions seen in EVO)](02-file-formats/catalog.md)
- [.SRC — TAS Pro 4GL source language](02-file-formats/src-tas-pro-language.md) — *draft*
- [.DFM — Delphi form format (plaintext)](02-file-formats/dfm-delphi-forms.md) — *draft*
- [.DCY / .RWN — compiled proprietary binaries](02-file-formats/dcy-rwn-binaries.md) — *partially decrypted*
- [.RWN binary format — internal structure (header, proc/var tables, string pool, dispatch table)](02-file-formats/rwn-binary-format.md) — *verified, 2026-06-16*
- [RWN/RUN string dumps — analysis technique + ISTS.CFG extraction (2,575 files)](02-file-formats/rwn-strings-analysis.md) — *verified*
- [.DCY / .RWN — decryption findings (Twofish-CFB, IV confirmed 2026-06-15)](02-file-formats/decryption-findings.md) — *FULLY SOLVED — 1144/1145 files decrypt*
- [DCY forms catalog — all 41 decrypted DCY files: form types, UI structure, purpose](02-file-formats/dcy-forms-catalog.md) — *verified, 2026-06-17*
- [TAS Pro 7 UI controls catalog — all 51 control types, frequencies, purpose (from 1,136 DFMs)](02-file-formats/tas-pro-7-controls.md) — *verified, 2026-06-17*
- [.RUN — TAS Pro 6 bytecode format (Rosetta Stone analysis)](02-file-formats/run-tas6-bytecode.md) — *partial — dual-channel architecture confirmed, b2=data_size proven, C:78*
- [.RUN string extraction — method + BKAWLB full string catalog](02-file-formats/run-string-extraction.md) — *verified, 2026-06-24*
- [TAS Professional error code table — all 392 codes from ERRMSG.DBF](02-file-formats/tas-pro-error-codes.md) — *verified, Pass 247 2026-06-24*
- [.B / .mdx — Btrieve/Pervasive PSQL data file format (DDF system, page structure, type codes, company routing)](02-file-formats/btrieve-b-format.md) — *partial, 2026-06-18*
- [TAS Pro 7 data infrastructure modules (wtasdmgr, wtasdatam, wtasinit — FILEDICT system)](02-file-formats/tas-data-infrastructure.md) — *verified, 2026-06-16*
- [.RTM / .btm — Nevrona ReportBuilder templates](02-file-formats/rtm-reportbuilder.md) — *verified*
- [.IMP / .UPD / .XPT / others](02-file-formats/other-formats.md) — *verified*
- [.IMP / .XPT — Import/Export definition files (442-byte and 32000-byte binary templates)](02-file-formats/imp-xpt-import-export.md) — *verified, Pass 325 2026-06-26*

### 03 — Modules
- [Module naming (T6/T7 prefixes, AR/AP/IN/SO/PO/WO/GL)](03-modules/naming-and-inventory.md) — *draft*
- [DFM form inventory — every UI form, grouped by module](03-modules/dfm-form-inventory.md) — *verified, 1109 forms parsed*
- [Plaintext SRC deep-dive — reading the 7 legacy sources](03-modules/src-deep-dive.md) — *verified*
- [AR + SO form analysis — complete workflow forms for AR (T7ARA-I) and SO (T7SOA-G)](03-modules/ar-so-form-analysis.md) — *partial*
- [GL + WO form analysis — 24 GL forms, WO lifecycle (68 forms), journal types, WO status codes](03-modules/gl-wo-form-analysis.md) — *partial*
- [BM + IN form analysis — BOM status/type codes, 16 BM forms, 67+ IN forms confirmed](03-modules/bm-in-form-analysis.md) — *partial*
- [AP check printing workflow — complete step-by-step from Bkaph.SRC + Bkapha.SRC](03-modules/ap-check-workflow.md) — *verified*
- [Module ↔ Database cross-reference — which RWN opens which tables, ownership matrix](03-modules/module-db-cross-reference.md) — *verified, 2026-06-16*
- [Undocumented modules — 20+ modules with DFM-confirmed forms (AM, FA, JC, SA, SH, SM, PR, PO, etc.)](03-modules/undocumented-modules.md) — *partial*
- [Module Code Reference — all 42 modules, full names, groups, item counts](03-modules/module-codes.md) — *verified 2026-06-30*

**Per-module deep-dive pages** (each joins menu codes + schema + UI forms):
- [AR — Accounts Receivable](03-modules/ar-accounts-receivable/README.md) (17 menu / 24 forms / 29 tables) — + [help-content.md](03-modules/ar-accounts-receivable/help-content.md)
- [AP — Accounts Payable](03-modules/ap-accounts-payable/README.md) (19 / 33 / 26) — + [help-content.md](03-modules/ap-accounts-payable/help-content.md) *(21 CHM topics)*
- [IN — Inventory](03-modules/in-inventory/README.md) (40 / 67 / 19) — + [help-content.md](03-modules/in-inventory/help-content.md) *(38 CHM topics)*
- [SO — Sales Orders](03-modules/so-sales-orders/README.md) (48 / 69 / 7) — + [help-content.md](03-modules/so-sales-orders/help-content.md)
- [SA — Sales Analysis](03-modules/sa-sales-analysis/README.md) — + [help-content.md](03-modules/sa-sales-analysis/help-content.md)
- [PO — Purchase Orders](03-modules/po-purchase-orders/README.md) (29 / 41 / 8) — + [help-content.md](03-modules/po-purchase-orders/help-content.md) *(27 CHM topics)*
- [WO — Work Orders](03-modules/wo-work-orders/README.md) (31 / 68 / 30) — + [help-content.md](03-modules/wo-work-orders/help-content.md) *(52 CHM topics)*
- [GL — General Ledger](03-modules/gl-general-ledger/README.md) (16 / 24 / 28) — + [help-content.md](03-modules/gl-general-ledger/help-content.md) *(18 CHM topics)* — Pass321 2026-06-26: all 9 BKGLTRAN.TYPE codes confirmed from BKGLO.RUN binary; 20 BKGL*.RUN programs inventoried; C:83→97
- [BM — Bill of Materials](03-modules/bm-bill-of-materials/README.md) (10 / 16 / 10) — + [help-content.md](03-modules/bm-bill-of-materials/help-content.md) *(16 CHM topics)*
- [RO — Routings](03-modules/ro-routings/README.md) — + [help-content.md](03-modules/ro-routings/help-content.md) *(22 CHM topics)*
- [LC — Lot Control](03-modules/lc-lot-control/README.md) — + [help-content.md](03-modules/lc-lot-control/help-content.md) *(6 CHM topics)*
- [SC — Serial Control](03-modules/sc-serial-control/README.md) — + [help-content.md](03-modules/sc-serial-control/help-content.md) *(8 CHM topics)*
- [FO — Features & Options](03-modules/fo-features-options/README.md) — + [help-content.md](03-modules/fo-features-options/help-content.md) *(5 CHM topics)*
- [MR — MRP](03-modules/mr-mrp/README.md) (12 / 18 / 4) — + [help-content.md](03-modules/mr-mrp/help-content.md) *(14 CHM topics)*
- [PR — Payroll](03-modules/pr-payroll/README.md) (29 / 40 / 16) — + [help-content.md](03-modules/pr-payroll/help-content.md) *(35 CHM topics)*
- [DC — Data Collection](03-modules/dc-data-collection/README.md) (7 / 26 / 7) — + [help-content.md](03-modules/dc-data-collection/help-content.md) *(14 CHM topics)*
- [QC — Quality Control](03-modules/qc-quality-control/README.md) (0 / 15 / 2)
- [JC — Job Costing](03-modules/jc-job-costing/README.md) (20 ops / 14 DFMs / 0 own tables) — + [help-content.md](03-modules/jc-job-costing/help-content.md) *(20 CHM topics)* · *Pass318-319 2026-06-26: all 19 BKJC*.RUN binary-analyzed; BKJCENG shared engine; 6 dual-menu programs; 11 archive tables — C:92*
- [LW — Labor/WIP/Job Cost](03-modules/lw-labor-wip/README.md) (19 menu ops / shared WO tables) — *verified, 2026-06-19 · WO+JC menu alias; 3-path time entry chain documented*
- [CS — Commission System](03-modules/cs-commission-system/README.md) (16 / 12 / 16) — + [help-content.md](03-modules/cs-commission-system/help-content.md)
- [CM — Contact Manager](03-modules/cm-contact-manager/README.md) — + [help-content.md](03-modules/cm-contact-manager/help-content.md)
- [ES — Estimating](03-modules/es-estimating/README.md) (8 / 7 / 4) — + [help-content.md](03-modules/es-estimating/help-content.md) *(10 CHM topics)*
- [SR — Service / Repair](03-modules/sr-service-repair/README.md) (9 / 12 / 0) — + [help-content.md](03-modules/sr-service-repair/help-content.md)
- [PI — Physical Inventory](03-modules/pi-physical-inventory/README.md) (9 / 10 / 7) — + [help-content.md](03-modules/pi-physical-inventory/help-content.md) *(8 CHM topics)*
- [WC — Warehouse Control](03-modules/wc-warehouse-control/README.md) — + [help-content.md](03-modules/wc-warehouse-control/help-content.md) *(5 CHM topics)*
- [SH — Scheduling](03-modules/sh-shipping/README.md) (16 / 15 / 1) — + [help-content.md](03-modules/sh-shipping/help-content.md) *(22 CHM topics)* · *folder name `sh-shipping/` is a legacy mislabel; module is Scheduling*
- [ED — EDI](03-modules/ed-edi/README.md) (6 / 3 / 6) — *Pass320 2026-06-26: CandoEDI middleware architecture confirmed; X12 sets 850/860/810/855/856; BKEDI.DUN.*/MST.* namespaces — C:90*
- [CR — Contract Review](03-modules/cr-contract-review/README.md) — + [help-content.md](03-modules/cr-contract-review/help-content.md)
- [QU — Queries & Reports](03-modules/qu-queries/help-content.md) *(7 CHM topics: overview + QU-A through QU-F)*
- [HH — Hand Held Data Collection](03-modules/hh-handheld/README.md) (32 programs, 6 functional groups) — + [help-content.md](03-modules/hh-handheld/help-content.md) *(15 CHM topics: Paperless Shop Floor + HH-A through HH-M)*
- [SM — System Manager / Setup](03-modules/sm-system-manager/README.md) (34 / 109 / 10) — + [help-content.md](03-modules/sm-system-manager/help-content.md) *(56 CHM topics)*
- [SM — Data Maintenance: Archive & Purge schedule (all modules)](03-modules/sm-system-manager/data-maintenance-archiving.md) — *verified, from ISTech PDF*
- [UT — Utilities](03-modules/ut-utilities/help-content.md) *(12 CHM topics)*
- [SD — System Defaults](03-modules/sd-system-defaults/help-content.md) *(22 CHM topics)*
- [PS — Password Security](03-modules/ps-password-security/help-content.md) *(7 CHM topics)*
- [DE — Data Exchange](03-modules/de-data-exchange/help-content.md) *(15 CHM topics)*
- [IM — International Module](03-modules/im-international/help-content.md) *(3 CHM topics)*
- [FA — Fixed Assets](03-modules/fa-fixed-assets/README.md) (2 tables / 3 programs) — + [help-content.md](03-modules/fa-fixed-assets/help-content.md) *(6 CHM topics)* · *Pass377 2026-06-29: all 3 RWN decrypted; ISFXASST(23f)+ISFXATRN(12f) DDF-confirmed; GL posting workflow confirmed (T7FAB→BKGLTRAN); C:92*
- [AM — Accounting Maintenance](03-modules/am-accounting-maintenance/help-content.md) *(18 CHM topics)*
- [AD — Accounting Defaults](03-modules/ad-accounting-defaults/help-content.md) *(3 CHM topics)*
- [US — Settings](03-modules/us-settings/help-content.md) *(8 CHM topics: US-A through US-H)*
- [MM-Support — Main Menu (Support) Programs](03-modules/mm-support/help-content.md) *(3 CHM topics: Check for Updates, Send Files, Send Screen Print)*
- [MM-File — Main Menu (File) Programs](03-modules/mm-file/help-content.md) *(2 CHM topics: Maintain Database, Report Editor)*
- [YS — Yes/No System Parameters (T7YSYN.RWN)](03-modules/ys-system-params.md) — *Pass230: 495 ISTS.CFG.* params + BKYS.* field layout; BKYSMSTR*
- [MA — Map Deposits (T7MAPDEPO.RWN)](03-modules/ma-map-deposits.md) — *Pass230: AR deposit-to-invoice mapping; BKAR.DEP+ISAR.DEPL tables*
- [SM — Workstation Config (t7slsfc.RWN)](03-modules/sm-system-manager/workstation-config.md) — *Pass230: email/SMTP (49 vars), per-module screen selectors, UI flags, Java paths*
- [SM — Security & Access Control](03-modules/sm-system-manager/security-access-control.md) — *Pass249: three-tier model (BKPSUSER→BKSLEVEL→ISACCESS); BKSLEVEL 20-menu correction; BKSL.*/IS.ACC.* namespaces*
- [Shared Dialogs — T7RTMVALID.RWN (RTM format picker)](03-modules/shared-dialogs.md) — *Pass230: cross-module shared utility for ReportBuilder template selection*
- [FL — File Location Manager (WTASFLOC.RWN)](03-modules/fl-file-location.md) — *Pass231: CF_*/LOC_*/DICT_* namespaces confirmed; 8 TAS internal tables (FILELOC/FILEDICT/FILEKEY/FILEKNUM/FILEDES/FILEDFLD/ERRMSG/FILEDBF)*
- [SP — Statistical Process Control (T7SPC + 8 programs, 7 tables)](03-modules/sp-spc/README.md) — *Pass251: dual-track AOI+operator+traceability architecture; ISSPC/ISSERR/ISSTRACK/ISSTYPE/ISSDET/ISSETYPE/ISSEPROC full schemas*
- [SD — Standard Detail Codes (T7SDET, ISSDET/ISSTYPE)](03-modules/sd-detail-codes/README.md) — *Pass251: cross-module quality classification; ISSDET compound PK (TYPE+DETAIL); used by SPC/SR/NCR*
- [BR — Brand / CRM Classification & System Configuration (T7BRANDS + T7BROWSER)](03-modules/br-brands/README.md) — *Pass256: T7BRANDS = master EvoERP config editor (400+ ISTS.CFG.* flags, EMAIL.CFG.* SMTP, IS.* feature flags, ISCC 13f CC token table); T7BROWSER = 360° cross-module entity viewer*
- [EX — SQL Export (SQLEXPORT.RWN)](03-modules/ex-sql-export.md) — *Pass231: Java bridge vars[60-71] confirmed; EVOBI2 BI database; EVO.CFG.* + per-module screen selectors; same bridge pattern as 8 other Java programs*
- [SU — Setup / UI Configuration (WBKLUGRID/EvoERPDrillM/T7gdm)](03-modules/su-setup.md) — *Pass232: LUGRID_* 13-var + DRILLM.* 9-var namespaces confirmed; T7gdm = Grid copy utility (SKIP/REPLACE/OVERWRITE modes)*
- [RT — Runtime License Validator / Session Initializer (T7RTMVALID)](03-modules/rt-runtime-license.md) — *Pass233: 160 vars confirmed; 10 ISIS sub-table handles; tax/currency/localization globals; IS.* flag set; NZLICE.LIB session-init library*
- [CU — WO Material Cut Sheet (T7CUTSHEET2/T7CUTSHEET2b)](03-modules/cu-wo-cut-sheet.md) — *Pass233: WOMAT.* 17-var + MTLOT.* 22-var + MTWO.WIP.* 20-var confirmed; authentication gate; lot vs no-lot variants*
- [PA — Paperless DC / Shop Floor Control (T7Paperless/T7PACKMENU/T7PASS)](03-modules/pa-paperless-dc.md) — *Pass233: 13 namespaces confirmed; MTWO.WIP.* 76-var; MTWORO.* 44-var routing ops; MTRO.* 47-var routing master; IS.TRAY.* 21-var; LAB.* + T.* DC labor buffers; A*/H* dual/history handles*

### 05 — Glossary
- [Glossary — EvoERP terminology reference](05-glossary/glossary.md) — *verified, from EvoHELP.CHM*

### 05b — Customizations
- [J7* customization modules — i2 Systems / customer-specific EvoERP extensions (37 modules, 109 files)](customizations/j7-customizations.md) — *partial (DFM analysis; RWN logic encrypted)*

### 05c — Module Map
- [EvoERP module interdependency map — 40 modules, tier classification, Mermaid dependency graph, key data flows](06-module-map/module-map.md) — *derived from CHM cross-references*

### 05d — Configuration Keys
- [ISTS.CFG.* key directory — 535 unique configuration parameter keys from rwn_strings](05-configuration/ists-cfg-keys.md) — *partial, 535 keys cataloged*

### 06 — Data dictionary
- [Data dictionary overview — 649 tables, Pervasive DDF set](04-data-dictionary/overview.md) — *draft*
- [File names — complete table index (vendor help, by module)](04-data-dictionary/file-names-index.md) — *verified, ~320 tables*
- [Tier 1 tables — 12 core tables fully documented (AHSYLOG, BKARCUST, BKARINV, BKAPVEND, BKGLCOA, WORKORD, BKSYMSTR, etc.)](04-data-dictionary/tier1-tables.md) — *partial*
- [Tier 2 tables — BKSLEVEL (SOLVED), BKPRGLFL (SOLVED), BKAPPO, BKAPPOL, WO detail tables, payroll, BKYSMSTR YN flags](04-data-dictionary/tier2-tables.md) — *partial*
- [Tier 3 tables — MTICMSTR (MT inventory master), BKBMMSTR (BOM), BKRTEMTR (MT routing), WORKCTR, ISNOTES, ISSCHED (scheduler), BKRTCST, BKRTSPEC](04-data-dictionary/tier3-tables.md) — *partial, 2026-06-17*
- [Tier 4 tables — BKCM* Contact Manager family (46 tables), ISLBLMAP (label→RTM mapping, 102 fields), IS2DBAR (2D barcode config, 109 fields), BKSOLOCK, BKSOHLOT/BKSOHSER](04-data-dictionary/tier4-tables.md) — *partial, 2026-06-17*
- [Tier 5 tables — ISUSAGE (246f, 7yr usage history), ISAPAINL (390f, AP 75-GL-line archive), ISALINKS/ISLINKS (311f, document attachments), ISESTASM (213f, MT estimate master), ISESADTL (203f), ISMICADT/ESA/EST (108f each, costing snapshots), ISTAXGRP (105f, tax groups), ISPRMSTR (384f, extended payroll master)](04-data-dictionary/tier5-tables.md) — *partial, 2026-06-17*
- [Tier 6 tables — Inventory support: BKICLOC (32f, per-location qtys), BKICLOCM (12f, location master), BKICPMAT (85f, customer price matrix), BKICDIM (47f, item dimensions/specs), BKICTAX (46f, state tax by item), BKICREQ (41f, requisitions); MT cost snapshots: MTICAMTR/MTICEMTR (108f each); SO architecture finding: SO = BKARINV](04-data-dictionary/tier6-tables.md) — *partial, 2026-06-17*
- [Tier 7 tables — Pass 91–95 new findings: MTWC (work center), MTWORO (routing ops), IS.TRIG (triggers, 23f), BKRFQ (RFQ breaks), BKICPMAT (pricing matrix), BKAP.REM/TMC (remittance+bank ACH), MTWO.WIP (WO costs 14f), IS.SPC/SERR/STRACK, DRILLM, IS.FIB, CFFLOC registry, IS.CATM, BKCM code tables, ISSR.INFO, IS.REM](04-data-dictionary/tier7-tables.md) — *partial, 2026-06-18*
- [Tier 8 tables — DDF-exact schemas: BKAPPO (57f PO header), BKAPPOL (38f PO lines), BKGLTRAN, BKGLCOA (65f COA), BKDCSHFT/TLAB/PLAB, BKARCUST (106f), BKARINV, BKARINVL, BKAPVEND, BKAPINVL, WORKORD (74f), BKICMSTR (64f), BKGLPER, BKBMMSTR, BKARTNOT, ARTTEMP, BKACTRPT (29f), 18 tables total 1240 fields](04-data-dictionary/tier8-tables.md) — *partial, 2026-06-18*
- [Tier 9 tables — Java-confirmed schemas (EvoPVT.jar): BKLOGON, BKSYUSER, BKSLEVEL (422f), BKSYCFG, BKUPDATE, BKSYMSTR (286f), AHSYLOG, CALENDAR, ISSHIPCO, ISREMIND, ISBSF (143f), MACHINE, WORKCTR (24f), ROUTING (62f), BKBMMSTR (26f), ISFOHEAD, ISFOLINE (78f), BKICLOC (32f), BKQCMSTR — 19 tables](04-data-dictionary/tier9-tables.md) — *partial, 2026-06-18*
- [Tier 10 tables — Previously undocumented families (Pass 108): MK* marketing automation (11 tables: MKTRACK/TROUT/EVENT/FORM/ASSIGN/AHIST/DEF+3 code tables), SUM* SA summaries (4 tables), ISAR* AR archive (30 tables — BKARINV/BKARCUST clones), BKAB* license (2 tables), ISAC* corrective action CAR/NCR (3 tables), ISGL* extended GL (6 tables), WO history (11 tables: WOHBOM/DATE/EXCH/LABOR/MAT/RECV/ROUT+WOROUT/WOROUTMP/WOROCHG), ISSE* service equipment (10 tables)](04-data-dictionary/tier10-tables.md) — *partial, 2026-06-18*
- [Tier 11 tables — Module archive and extended tables (Pass 108): EvoERP archive pattern documented; ISSO* SO IS tables (10t: ISSOBOX packing/ISSOINFO/ISSOREVU approval); ISSR* SR archive (21t — BKARINV clones + ISSR_INFO 54f pattern); ISRM* RMA archive (14t); ISSS* staging (4t); ISST* scan tracking (4t); ISPO* PO tracking (7t: ISPOTRK carrier tracking); ISAP* AP extended (15t: ISAPAINL 390f AP archive invoice); ISPR* extended payroll (7t: ISPRMSTR 384f, ISPREQ WO labor auth)](04-data-dictionary/tier11-tables.md) — *partial, 2026-06-18*
- [Variable-to-field name map — TAS program variable names (BKIC.PROD.*, BKAR.*, BKAP.*) mapped to DB fields](04-data-dictionary/variable-field-map.md) — *verified, 2026-06-16*
- [Primary keys — 200+ tables with primary key fields from INDEX.DDF](04-data-dictionary/primary-keys.md) — *partial*
- [FILELOC routing table — 401 logical buffer names → 863 physical filenames, 6 companies; schema, alias groups, company codes, CodeBase entries (Pass 388, 2026-06-29)](04-data-dictionary/fileloc-routing.md) — *verified*
- [Cross-module foreign key relationships — 270 inferred FKs, 68 parent tables; global invoice/PO/txn number architecture; NOTETEMP/ROUTTEMP/XXICMSTR super-tables](04-data-dictionary/fk-cross-module.md) — *inferred, Pass 411 2026-06-30*

### 07 — Reports (ReportBuilder .RTM)
- [Reporting pipeline overview + RTM cross-reference](05-reports/overview.md) — *verified*
- [RTM Report Template Inventory by Module — 1,734 RTMs, generation breakdown, custom EN* prefixes](02-file-formats/rtm-module-inventory.md) — *verified, Pass 411 2026-06-30*

### 08 — Menu system
- [Menu system overview — 554 codes across 38 modules](06-menu-system/overview.md) — *verified*
- [Code → Program → DB Table mapping (870 entries)](06-menu-system/code-program-mapping.md) — *verified*

### 09 — Runtime & boot sequence
- [How EVO starts up (StartEvo.exe → tp7runtime.exe → EvoERPmenu.rwn)](07-runtime-boot/boot-sequence.md) — *draft*

### 10 — IT Procedures & Case Studies
- [Packaging items stuck on open order report — SD-M "Create 0 Qty SO Lines" fix](procedures/packaging-items-stuck-on-open-order-report.md) — *verified, 2026-06-18*

---

## Legend
- *draft* — first pass, some claims not yet verified.
- *verified* — every claim has a cited source in the EVO files.
- *open-questions* — important gaps documented in `research/OPEN_QUESTIONS.md`.
- *partial* — covers some aspects but known to be incomplete.
