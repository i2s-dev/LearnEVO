"""
Glossary — EVO / TAS / accounting / manufacturing terms.
Each entry: (term, short_def, body_md, see_also).
"""

GLOSSARY = [

("ACH", "Automated Clearing House — electronic bank transfer",
"The electronic funds transfer system used in the US for direct deposit and direct debit. EVO generates ACH files for payroll direct deposit (`PR-E`) and vendor e-payments (`J7ADTNACHA.RWN`).",
["AP-H", "PR-E", "recipe-print-checks"]),

("Aging", "Categorizing open receivables/payables by days overdue",
"EVO aging reports bucket invoices into current/30/60/90/over-90 days. Run via `AR-F` (AR side) and `AP-I` (AP side).",
["AR-F", "AP-I"]),

("BOM", "Bill of Materials — components of an assembly",
"A parent-child list of what goes into making an item. In EVO, BOMs live in `BKBMMSTR`. Can be single-level (direct children only) or multi-level (recursively exploded). See [[module-BM]].",
["module-BM", "BKBMMSTR"]),

("Btrieve", "The original name for Pervasive's database engine",
"Btrieve is the Btree+ISAM engine that's evolved into **Pervasive PSQL** (now **Actian Zen**). EVO uses it for all data storage. Every table is a `.B` or `.B<company-code>` file. See [[architecture-overview]].",
["Pervasive", "DDF", "table-BKARCUST"]),

("CFB", "Cipher Feedback — a block-cipher operating mode",
"A mode that turns a block cipher into a stream cipher by feeding ciphertext back through the encryption. EVO's `.DCY`/`.RWN` encryption is Twofish in CFB mode. See [[dcy-rwn-decryption]].",
["Twofish", "dcy-rwn-decryption"]),

("CHM", "Compiled HTML Help — Microsoft's help-file format",
"`EvoHELP.CHM` is the user-facing help file, opened with F1 from inside EVO. Contains 779 topics — one per menu operation plus 90 conceptual chapters.",
["EvoHELP.CHM", "help-system"]),

("DCPcrypt", "The Delphi cryptography library used by TAS Pro 7",
"Open-source Delphi crypto: provides Twofish, SHA1, DES, 3DES, and base cipher/hash classes. Embedded in `tp7runtime.exe`. See [[dcy-rwn-decryption]].",
["Twofish", "tp7runtime.exe"]),

("DDF", "Data Definition File — Pervasive's schema catalog",
"Btrieve stores schema in a set of DDF files: `FILE.DDF` (tables), `FIELD.DDF` (columns), `INDEX.DDF`, `ATTRIB.DDF`, etc. EVO has 659 tables catalogued this way. See [[tables-index]].",
["Btrieve", "tables-index"]),

("DFM", "Delphi Form (UI layout)",
"Delphi's form-resource format — plaintext, human-readable. EVO UI screens are `.DFM` files like `T7ARA.DFM`. See [[format-dfm]].",
["format-dfm", "DCY"]),

("DCY", "Encrypted DFM",
"The encrypted form of a `.DFM`. Produced by the TAS Pro 7 compiler with `#FORMSENCRYPTED <phrase>`. See [[dcy-rwn-decryption]].",
["DFM", "encryption"]),

("EDI", "Electronic Data Interchange",
"Trading-partner standard for exchanging POs, invoices, ASNs, etc. In EVO, the [[module-ED|ED module]] processes inbound and generates outbound.",
["module-ED"]),

("ERP", "Enterprise Resource Planning",
"Integrated software for running a business end-to-end. EVO is an ERP for small/mid manufacturers.",
["core-workflows"]),

("F2 Lookup", "The ubiquitous 'find a record' key in EVO",
"Pressing F2 on any field bound to a key brings up a browse/search window for that entity. Works on customer codes, vendor codes, item codes, GL accounts, and most other lookup-driven fields.",
["menu-navigation"]),

("FIFO", "First In, First Out — inventory costing method",
"Oldest receipts are sold first. EVO supports FIFO via lot-layer tracking in `BKICLOT`.",
["Costing methods", "module-IN"]),

("FNO", "Features and Options — configurable-product module",
"Lets you sell an item with user-selected variants (size, color, options). Configurator UI launches from SO lines. See [[subsystem-evofno]].",
["subsystem-evofno"]),

("GL", "General Ledger — the accounting book of record",
"Where every posting ends up. See [[module-GL]].",
["module-GL"]),

("JC", "Job Costing",
"Actual-cost-vs-planned reporting for work orders. See [[module-JC]].",
["module-JC"]),

("LIFO", "Last In, First Out — inventory costing method",
"Newest receipts are sold first. Supported in EVO via lot layers.",
["FIFO", "module-IN"]),

("MRP", "Material Requirements Planning",
"The scheduling algorithm that balances supply and demand to suggest what to buy and make. See [[module-MR]] and [[recipe-run-mrp]].",
["module-MR", "recipe-run-mrp"]),

("Nevrona ReportBuilder", "The report-rendering engine used by EVO",
"Third-party Delphi component for report layout. Each report is an `.RTM` template; `RBDsgnr.exe` is the designer. See [[format-rtm]].",
["RTM", "format-rtm"]),

("ODBC", "Open Database Connectivity",
"Standard SQL interface. Pervasive PSQL's ODBC driver lets you query EVO data from Excel, Power BI, Crystal Reports, etc. See [[odbc-access]].",
["odbc-access", "Pervasive"]),

("PO", "Purchase Order",
"Document ordering goods/services from a vendor. See [[module-PO]].",
["module-PO"]),

("Pervasive", "The database engine (now Actian)",
"Pervasive Software → now Actian — the vendor of PSQL (Btrieve). EVO installations need the PSQL client or workgroup engine.",
["Btrieve", "odbc-access"]),

("RFQ", "Request for Quote",
"Pre-purchase inquiry asking vendors to price goods. `RF-A Enter RFQ` in EVO.",
["recipe-rfq", "PO-E"]),

("RMA", "Return Merchandise Authorization",
"Customer return document. Entered as `SO-P-F`.",
["recipe-rma"]),

("Routing", "The sequence of operations to produce an item",
"Defines which work centers touch the product, in what order, for how long. Stored in `ROUTING` and `BKRTEMTR`. See [[module-RO]].",
["module-RO", "work centers"]),

("RTM", "ReportBuilder Template",
"Binary Delphi stream (`TPF0` magic) holding a Nevrona ReportBuilder report layout. See [[format-rtm]].",
["format-rtm", "Nevrona ReportBuilder"]),

("RWN", "TAS Pro 7 compiled program (encrypted)",
"The current-generation compiled TAS program. Encrypted. Each menu operation's logic lives in a `.RWN`. See [[format-rwn]].",
["format-rwn", "DCY"]),

("SO", "Sales Order",
"Customer order document. See [[module-SO]].",
["module-SO"]),

("SRC", "TAS Pro 4GL source code (plaintext)",
"Human-readable TAS-Pro source. Usually `.SRC`, compiled to `.RWN`. See [[format-src]] and [[src-deep-dive]].",
["format-src", "src-deep-dive"]),

("TAS Professional (TAS Pro 7)", "The 4GL language and runtime EVO is built on",
"A dialect of xBase family, developed by Business Tools / MGM / Addsum. The runtime is `tp7runtime.exe`. See [[architecture-overview]].",
["architecture-overview"]),

("Twofish", "The block cipher used to encrypt EVO RWN/DCY files",
"128-bit block, 128/192/256-bit key, ex-AES finalist. In EVO, used in CFB mode with a fixed runtime key. See [[dcy-rwn-decryption]].",
["CFB", "encryption"]),

("VCL", "Visual Component Library — Delphi's UI framework",
"Standard Delphi UI widgets. EVO extends them with `TTAS*` subclasses (e.g. `TTASEnter`, `TTASDataGrid`).",
["format-dfm"]),

("Voucher", "An AP invoice in EVO terminology",
"Synonymous with 'AP bill'. Entered via `AP-B`. See [[recipe-enter-voucher]].",
["recipe-enter-voucher", "module-AP"]),

("WIP", "Work In Process — in-production inventory value",
"The dollar value of components that have been issued to work orders but not yet received as finished goods. Reported by `WO-L-B`.",
["module-WO", "module-IN"]),

("WO", "Work Order — manufacturing order",
"The document that tells the shop floor what to make. See [[module-WO]] and [[recipe-work-order]].",
["module-WO", "recipe-work-order"]),

]
