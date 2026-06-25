# BR — Brand / CRM Classification & System Configuration

Status: verified | Pass 256 (2026-06-25)

---

## Overview

The BR subsystem covers two related programs under the EvoERP CRM / Brand menu:

- **T7BRANDS** — Master EvoERP system configuration editor. Despite the name, this is the central control panel for all system-wide feature flags, email/UI settings, brand category codes, and CC/tax/Java integration paths. It is **not** just a brand code editor.
- **T7BROWSER** — Cross-module 360° entity viewer (CRM contact browser). Displays AR invoices, AP POs, Work Orders, Inventory transactions, GL transactions, and Marketing activity for a selected customer/vendor contact.

---

## Programs (2)

| Program | Procs | Source | DB Files |
|---------|-------|--------|----------|
| T7BRANDS.RWN | 53 | EVO.LIB | 40 (incl. ISIS, BKCMACCC, BKCMACCN, BKCMACCN, ISCC, BKAPVEND, BKARCUST, BKICMSTR, BKGLTRAN, BKAPPOL/BKAPPO, LOT, SERIAL, ISTRIGRS, ISREMIND, ISNCR, BKMRPFC, DBAFIFO, LANGDICT, FILELOC, ISICMSTR, ISLINKS, ...) |
| T7BROWSER.RWN | 4 | t7browser.SRC | 55 (session init overhead + BKCMACCN, BKARCUST, BKAPVEND, BKICMSTR, BKARINVL, BKAPPOL, BKAPPO, WORKORD, WOBOM, INVTXN, BKGLTRAN, BKGLX, MKAHIST, ...) |

T7BROWSER has a readable `.SRC` source file (one of only 7 in the EvoERP system) — TAS Pro 6 era source.

---

## T7BRANDS — What It Actually Does

T7BRANDS is EvoERP's **master configuration editor**. It manages at least five distinct configuration domains, all stored in the ISIS key-value table:

### 1. Brand / Account Category Codes (BKCMACCC)

The only pure CRUD data domain. Two fields:

| Field | Type | Notes |
|-------|------|-------|
| BKCM_ACCC_CCODE | STRING/5 | PK — category code |
| BKCM_ACCC_DESC | STRING/25 | Description |

### 2. System Feature Flags (ISIS table — IS.* namespace)

400+ ISTS.CFG.* variables loaded from ISIS by key name. Partial confirmed list:

| Var | Meaning |
|-----|---------|
| ISTS.CFG.PASSWD | System master password |
| ISTS.CFG.ACCESS | Access control mode |
| ISTS.CFG.CC | Credit card processing enabled |
| ISTS.CFG.CCUID / ISTS.CFG.CCPSW | CC processor credentials |
| ISTS.CFG.ATOS | Auto-transfer to SO |
| ISTS.CFG.WODSO | WO → SO auto link |
| ISTS.CFG.SOLOT / ISTS.CFG.SOSER | SO lot/serial tracking |
| ISTS.CFG.WOCALC | WO cost calculation mode |
| ISTS.CFG.AVATAX / ISTS.CFG.AVAACT | AvaTax integration enabled/active |
| ISTS.CFG.AVAKEY / ISTS.CFG.AVACOD / ISTS.CFG.AVACO | AvaTax API key, code, company |
| ISTS.CFG.DCSEQ | Data collection sequence mode |
| ISTS.CFG.DCSYNC | Data collection sync mode |
| ISTS.CFG.ECO | Engineering Change Order enabled |
| ISTS.CFG.JOB | Job costing enabled |
| ISTS.CFG.MANINV | Manual inventory mode |
| ISTS.CFG.MRPDAY / ISTS.CFG.MRPDOL | MRP day/dollar thresholds |
| ISTS.CFG.VOIC / ISTS.CFG.VOWO / ISTS.CFG.VOPO | Void controls (IC/WO/PO) |
| ISTS.CFG.VOSO / ISTS.CFG.VOAR / ISTS.CFG.VOAP | Void controls (SO/AR/AP) |
| ISTS.CFG.SHIFT2 / ISTS.CFG.SHIFT3 | Shift 2/3 time boundaries |
| ISTS.CFG.XDBA | External DBA mode |
| ISTS.CFG.RCYCL / ISTS.CFG.URNT | Recycle/return controls |
| ISTS.CFG.GLDATE / ISTS.CFG.GLCTRL | GL date/control settings |
| ISTS.CFG.WCBF | Work center burden factor |
| ISTS.CFG.PIPTL / ISTS.CFG.PRTL | PI/PR title labels |
| ISTS.CFG.BBCOLO | Background color |
| ... (400+ total) | See `samples/rwn_symbols.json` T7BRANDS entry |

### 3. Feature Flag Booleans (ISIS — IS.* short namespace)

Read at session start into runtime boolean vars:

| Var | Meaning |
|-----|---------|
| IS.MULTI.CURR | Multi-currency enabled |
| IS.LANDED.COST | Landed cost enabled |
| IS.UPC / IS.UPC.1 / IS.UPC.2 | UPC barcode modes |
| IS.RETAIL.PRICE | Retail pricing enabled |
| IS.COMM.PRICE | Commission pricing enabled |
| IS.IMAGING | Document imaging enabled |
| IS.AUTO.TAX.CAL | Automatic tax calculation |
| IS.EZPAY | EZPay CC integration |
| IS.RMA | Return Merchandise Authorization enabled |
| IS.DEMO | Demo mode |
| IS.MULTI.CPAY | Multiple CC payment enabled |
| IS.PO.TAX | PO tax enabled |
| IS.SPEC.SUP / IS.SPEC.SUPF / IS.SPEC.SUPT | Special supplier flags |

### 4. Email / SMTP Configuration (ISIS — EMAIL.CFG.* namespace)

| Var | Meaning |
|-----|---------|
| EMAIL.CFG.SMTP / EMAIL.CFG.PORT | SMTP server + port |
| EMAIL.CFG.SEC | Security mode (TLS/SSL) |
| EMAIL.CFG.EMAIL / EMAIL.CFG.NAME | From address/name |
| EMAIL.CFG.USER / EMAIL.CFG.PASS / EMAIL.CFG.EPASS | SMTP credentials (EPASS=encrypted) |
| EMAIL.CFG.SUBJ / EMAIL.CFG.BOD1-9 | Default email subject/body templates |
| EMAIL.CFG.SIG1-9 | Email signature lines |
| EMAIL.CFG.BCC / EMAIL.CFG.ECB / EMAIL.CFG.EVB | BCC and event callbacks |
| EMAIL.CFG.APTH | Attachment path |
| EMAIL.CFG.EFAIL | Failure handling mode |

### 5. EvoERP UI Configuration (ISIS — EVO.CFG.* namespace)

| Var | Meaning |
|-----|---------|
| EVO.CFG.TOOLBAR | Toolbar display mode |
| EVO.CFG.OLWOA / EVO.CFG.OLPOA / etc. | Overlay modes per module |
| EVO.CFG.SOUNDS | Sound effects enabled |
| EVO.CFG.REMIND / EVO.CFG.EREMIND / EVO.CFG.REMSEC | Reminder system settings |
| EVO.CFG.QPRINT | Quick print mode |
| EVO.CFG.CFU | Config update mode |
| EVO.CFG.TOPMOST | Always-on-top window mode |
| EVO.CFG.AREN | AR entry notifications |
| HOTBUTTON1-6P / HOTBUTTON1-6I / HOTBUTTON1-6H | Toolbar hotbutton program/icon/hint |
| JAVA.PATH / JAVA.PATH2 | Java executable paths (for EvoPVT.jar) |
| XCPATH | XCommerce integration path |

---

## T7BROWSER — Cross-Module 360° Entity Viewer

T7BROWSER displays a unified view of all EvoERP activity for a selected contact (customer, vendor, or inventory item). Despite the 55-table DB list, most are standard session-init overhead. The business tables it accesses:

| Table | Data Shown |
|-------|-----------|
| BKCMACCN | CRM contact master (the entity being browsed) |
| BKCMACCC | Brand category lookup |
| BKARCUST | AR customer details |
| BKAPVEND | AP vendor details |
| BKICMSTR / ISICMSTR | Inventory item details |
| BKARINVL | AR invoice lines (sales history) |
| BKAPPOL / BKAPPO | AP PO lines (purchase history) |
| WORKORD / WOBOM | Work orders and BOM (production history) |
| INVTXN | Inventory transactions |
| BKGLTRAN / BKGLX | GL transactions and cross-references |
| MKAHIST | Marketing activity history |
| BKSYAR | AR system settings |
| MKECLASS / CLASS | Marketing/classification codes |
| ISGLDATE | GL date table |
| ISNUMBER | Auto-numbering |

T7BROWSER has **0 named vars** in rwn_symbols.json — it is entirely form-driven, relying on DFM layout and TAS Pro runtime for display. No standalone business logic variables.

The presence of ISBROKER + ISDUTY in the DB list is standard EvoERP session init (landed-cost infrastructure), not browser-specific logic.

---

## Credit Card Token Table (ISCC)

Managed by T7BRANDS via ISTS.CFG.CC flag + TOLKEN var. Full schema confirmed from DDF:

| Field | Type | Size | Notes |
|-------|------|------|-------|
| IS_CC_CODE | STRING | 10 | PK — CC token code |
| IS_CC_SORT | FLOAT | 8 | Sort order |
| IS_CC_TOLKEN | STRING | 20 | Payment gateway token |
| IS_CC_MASKED | STRING | 24 | Masked card number (display) |
| IS_CC_EXP | STRING | 4 | Expiration date MMYY |
| IS_CC_ADDRESS | STRING | 40 | Billing address |
| IS_CC_ZIP | STRING | 10 | Billing ZIP |
| IS_CC_CARDTYPE | STRING | 15 | Card type (VISA/MC/AMEX/etc.) |
| IS_CC_CARDNAME | STRING | 25 | Cardholder name |
| IS_CC_STATUS | STRING | 25 | Token status |
| IS_CC_STDATE | DATE | 4 | Status date |
| IS_CC_XCTRAN | STRING | 10 | Transaction cross-reference |
| IS_CC_EXTRA | STRING | (truncated in DDF) | Extra/overflow field |

IS_CC_TOLKEN contains the gateway-issued token (not the raw card number) — standard PCI-compliant tokenization pattern.

---

## POS Integration

T7BRANDS holds `ISPOSI.H` (POS integration handle). The ISPOSI table is **not in the DDF** (not a standard Btrieve/Pervasive file registered at install time) — it is likely registered dynamically via FILELOC or opened as a runtime-only table. Its schema is unknown. The presence of ISPOSI.H confirms that the POS module is optionally integrated via T7BRANDS configuration.

---

## Key Relationships

- T7BRANDS reads/writes ISIS (key-value config store) for all ISTS.CFG.* / IS.* / EMAIL.CFG.* / EVO.CFG.* settings
- T7BRANDS is the only program that should write ISIS — all other programs read IS.* flags read-only at session start
- T7BROWSER reads but does not write any of the above tables — it is a pure display/browse program
- BKCMACCN (154f CRM contact master) is browsed by T7BROWSER but maintained by the CM (CRM) module programs
- ISCC (CC tokens) are bound to customer accounts — CC processing uses ISTS.CFG.CC + ISTS.CFG.CCUID/CCPSW

---

**Confidence: 90/100** — BKCMACCC schema confirmed from DDF; T7BRANDS var list confirmed from rwn_symbols.json (1233 vars); ISTS.CFG.* flags enumerated from named vars; ISCC 13-field schema confirmed from DDF; T7BROWSER 360° scope confirmed from DB file list. Gap: ISPOSI table schema unknown (not in DDF); ISIS key-value field layout (how ISTS.CFG.* is stored) inferred from key-name pattern, not confirmed from ISIS DDF entry.
