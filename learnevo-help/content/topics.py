"""
Hand-authored conceptual pages for the LearnEVO help program.
Each TOPIC is a tuple (id, title, section, body_markdown, keywords).

Body uses a light Markdown subset — rendered client-side by marked-lite.
Wiki-style links with [[page-id]] or [[page-id|label]] render as in-app links.
"""

TOPICS = [

# =====================================================================
# 00 — Getting Started / Orientation
# =====================================================================

("welcome", "Welcome to the EVO Help System", "Getting Started",
"""
This help browser covers **every aspect of EvoERP** — menu operations,
modules, forms, database tables, file formats, architecture, and
step-by-step task walkthroughs.

## What is EVO?

EvoERP is a **manufacturing ERP** for small/mid shops — the current
incarnation of DBA Manufacturing. It runs on the **TAS Professional 7**
runtime, stores data in **Pervasive SQL (Btrieve)**, and uses
**Nevrona ReportBuilder** for output. See [[what-is-evoerp]] for details.

## How to find things

- **Search** — press `Ctrl+K` anywhere, or click the search box. Type
  anything: a menu code (`AP-H`), a table name (`BKARCUST`), a concept
  ("multi-company"), or just plain English ("how do I print checks").
- **Left sidebar** — grouped catalog of every topic, module, menu code,
  table, and form.
- **Cross-references** — every page links to related pages. Click any
  blue term to jump there.

## Start here if you're…

- **New to EVO** → [[quick-tour]]
- **A user learning a module** → [[module-map]]
- **Trying to do a specific task** → [[recipes-index]]
- **A developer / integrator** → [[architecture-overview]]
- **Looking up database fields** → [[tables-index]]

## Top-level guides

- [[quick-tour]] — a 10-minute introduction to the EVO UI
- [[core-workflows]] — the five business processes EVO supports
- [[menu-navigation]] — how to get anywhere with keyboard shortcuts
- [[architecture-overview]] — technical stack in one page
- [[data-dictionary-overview]] — the 659 tables and 24,113 fields
- [[file-formats]] — DFM, DCY, RWN, RTM, and the rest
""",
["welcome", "help", "overview", "start", "evo", "introduction"]),

("quick-tour", "Quick Tour — Your First 10 Minutes in EVO", "Getting Started",
"""
A fast walkthrough of the EVO interface.

## 1. Launching EVO

On any workstation where EVO is installed:

```
Double-click C:\\ISTS\\EvoERP.lnk (or the "Evo ~ ERP" desktop shortcut)
```

The launcher (`StartEvo.exe`) reads `C:\\ISTS\\taspro7.ini`, spawns
`tp7runtime.exe`, and points it at the main menu RWN on the network:

```
\\\\I2S109-SOLIDCRM\\DBAMFG$\\EvoERPmenu.rwn
```

See [[boot-sequence]] for the deep trace.

## 2. Login

The login screen is driven by `EVOMENU_LOGIN.DCY`. Type your user code
and password. The runtime reads your record from the [[table-AHSYLOG|AHSYLOG]]
table, which holds 20 per-module permission flags and your starting
menu code.

## 3. Company selection

After login you'll see a company list (from `EVOMENU_SELCOMP.DCY`).
Each company is a separate **per-code data folder** on the share — e.g.
`\\\\i2s109-solidcrm\\DBAMFG$\\22\\*.B22` for company "22". Data
tables are completely isolated between companies; the COA, inventory,
and ledger are all per-company. See [[multi-company]].

## 4. Main menu

The EvoERP main menu is a hierarchical tree. Top level is organized by
module letter:

- **AD** — Admin defaults
- **AM** — Archive / Maintenance
- **AP** — Accounts Payable
- **AR** — Accounts Receivable
- **BM** — Bill of Materials
- **ES** — Estimating
- **GL** — General Ledger
- **IN** — Inventory
- **PO** — Purchase Orders
- **SO** — Sales Orders
- **WO** — Work Orders
- **PR** — Payroll
- **MR** — MRP
- …and more ([[module-map]])

Picking a menu item runs a `.RWN` program loaded from the share.

## 5. Screen layout in a typical form

EVO screens are rendered by the TAS runtime from plaintext DFM files
(`T7XXY.DFM`). A typical entry screen has:

- **Title bar** — shows the menu code and operation name (e.g. "AR-A Enter Customers")
- **Menu bar / toolbar** — standard navigation, F-keys
- **Fields** — TAS-specific `TTASENTER`/`TTASNumEnter`/`TTASDateEdit` controls
- **Grid** — `TTASDataGrid` for line-item entry (orders, invoices)
- **Status bar** — hint text for the current field (updated by `HelpStatusBar`)

Common keyboard shortcuts:

| Key | Action |
| --- | ------ |
| `F1` | Context help (opens topic in EvoHELP.CHM) |
| `F2` | Lookup / browse (the ubiquitous "search for a record") |
| `F3` | Change search key / secondary lookup |
| `F5` | Copy record as new |
| `F10` | Print / commit / save |
| `ESC` | Back up one level |
| `INS` | Insert a new record |
| `DEL` | Delete / reverse the current record |
| `PgDn` | Next page / next section of a multi-page form |
| `PgUp` | Previous page |
| `Ctrl+Q` | Quick-exit the current screen |

Every screen shows the active F-keys at the bottom via `fnc_list`
in the source.

## 6. Your first task

Try **AR-A (Enter Customers)** to browse. Route:

```
Main Menu → AR Accounts Receivable → AR-A Enter Customers
```

You can browse existing customers with F2 Lookup, view details, and
(if your permission flag allows) edit. See
[[recipe-enter-customer]] for a guided walk-through.

## What's next

- [[core-workflows]] — how real work flows through EVO
- [[module-map]] — what every module does
- [[menu-navigation]] — keyboard-driven navigation
- [[recipes-index]] — concrete tasks
""",
["tour", "quick start", "first time", "login", "company", "main menu", "f2", "lookup",
 "keyboard", "shortcuts", "keys", "navigation", "user interface", "ui"]),

("menu-navigation", "Menu Navigation and Keyboard Shortcuts", "Getting Started",
"""
The EVO UI is built for **fast keyboard operation**. Most experienced
users never touch the mouse.

## Menu-code format

All operations are named `XX-Y[-Z]`:

- `XX` — 2-letter module code (AR, AP, IN, SO, etc.)
- `Y` — single letter sub-operation within the module
- `Z` — optional second-letter drill (e.g. `BM-J-C` = BOM → Approved
  Manufacturers)

The convention is:
- First letter `A` is usually "Enter master data" (e.g. `AR-A` = Enter
  Customers, `AP-A` = Enter Vendors, `IN-A` = Enter Items).
- Subsequent letters (B, C, …) walk the business process — entry,
  approval, printing, reporting — roughly alphabetically.

See [[menu-codes-reference]] for every code and what it does.

## Global keys

| Key | Action | When |
| --- | ------ | ---- |
| `F1` | **Context help** — opens the corresponding CHM help topic | Any screen |
| `F2` | **Lookup** — browse/search records for this field | Any field bound to a key |
| `F3` | **Alternate lookup** — switch to secondary search key | On a lookup field |
| `F4` | **Change info** (on some screens) | Varies |
| `F5` | **Copy record as new** | On a browse screen |
| `F10` | **Print / commit** | Typically on the final entry page |
| `ESC` | **Back up** — cancels the current dialog, returns to parent | Any screen |
| `INS` | **Insert new** | Browse screens |
| `DEL` | **Delete / reverse** | Browse screens |
| `PgUp` / `PgDn` | Multi-page form navigation | Forms with tabs |
| `Ctrl+Q` | Quick-exit | Most screens |
| `HOME` | First record | Browse screens |
| `END` | Last record | Browse screens |

## Typing a menu code directly

On the main menu, you can type the menu code (e.g. `AR-C`) and hit Enter
to jump straight there. Shorter than navigating the tree.

## Search-by-first-letter

In any menu tree, typing a letter jumps to the first entry starting with
that letter.

## Status bar

Watch the status bar at the bottom — every field shows one-line help
from the DFM's `HelpStatusBarMsg` property. If you're unsure what a field
wants, that's your first stop.

## Custom F-key mapping

An admin can remap F-keys using `DFMALTS` (DFM-specific alt-key binder).
See the "Set ALT Keys for DFMs" screen under [[module-SM|System Manager]].

## Related

- [[quick-tour]]
- [[module-map]]
- [[menu-codes-reference]]
""",
["keyboard", "shortcuts", "f1", "f2", "f5", "f10", "esc", "menu", "navigation"]),

# =====================================================================
# 01 — Core Workflows
# =====================================================================

("core-workflows", "The Five Core Workflows", "Concepts",
"""
EvoERP supports five end-to-end business processes. Every menu operation
fits into one of them. Learning the workflows is more useful than
memorizing menu codes.

## 1. Buy → Receive → Pay  (Purchasing)

```
PO-A Enter PO  →  PO-C Receive  →  AP-B Enter Voucher  →  AP-F Pick  →
AP-H Print Checks  →  AP-B Post
```

Tables touched: `BKAPVEND`, `BKAPPO`, `BKAPPOL`, `BKAPINVT`, `BKAPCHKF`,
`BKAPCHKH`, `BKICMSTR` (on-order qty).

Detailed recipe: [[recipe-po-to-payment]].

## 2. Sell → Pick → Ship → Invoice → Collect  (Sales)

```
SO-A Enter SO  →  SO-C Print Pick Ticket  →  SO-C Print Packing Slip  →
SO-F Print Invoice  →  AR-B Post Invoice  →  AR-C Record Payment
```

Tables touched: `BKARCUST`, `BKICMSTR`, `BKSONOTE`, `BKARINV`, `BKARINVL`,
`BKARINVI`, `BKARTXN`, `BKARCHKF`.

Detailed recipe: [[recipe-so-to-cash]].

## 3. Make  (Manufacturing)

```
ES-A Estimate  →  BM-A Enter BOM  →  RO-A Enter Routing  →
WO-A Enter Work Order  →  DC-A Data Collection (labor + material)  →
WO-C Receive Finished  →  AM-C Consolidate GL
```

Tables touched: `BKESTQT`, `BKBMMSTR`, `BKBMAMTR`, `BKRTEMTR`, `ROUTING`,
`WORKORD`, `WOBOM`, `WOROUT`, `WOLABOR`, `WORECV`, `MACHINE`, `TOOL`.

Detailed recipe: [[recipe-work-order]].

## 4. Inventory Lifecycle

```
PO-C Receive  →  IN-E Transfer (bin-to-bin)  →  IN-F/PI-A Count  →
IN-G Adjust  →  IN-I Valuation Report
```

Tables touched: `BKICMSTR`, `BKICLOC`, `BKICDIM`, `INVTXN`, `BKPIMSTR`,
`BKPIPHYS`.

Detailed recipe: [[recipe-physical-inventory]].

## 5. Financial Close

```
AM-A Reset Close Date  →  AM-B Fiscal Year-End  →  AM-I Consolidate GL  →
AM-R Out-of-Balance Report  →  GL-X Financial Statements  →
AM-J Purge Old
```

Tables touched: `BKGLACHK`, `BKGLAGJL`, `BKGLCCOA`, `BKGLATRN`, `BKSYMSTR`
(period/fiscal settings).

Detailed recipe: [[recipe-month-end-close]].

## How the workflows connect

- POs close when all lines are received AND invoiced.
- SOs close when all lines are shipped AND paid (via AR-C).
- WOs close when finished-good quantity matches planned AND all
  components are issued AND labor is posted.
- Every posting writes to [[module-GL|GL]] via temporary tables
  (`BKGLTEMP`, `BKGLCHK`) and then commits.
- Month-end rolls the [[table-BKSYMSTR|BKSYMSTR]] period pointer,
  making prior periods read-only.

## Related

- [[module-map]] — module-to-workflow mapping
- [[recipes-index]] — all step-by-step tasks
""",
["workflow", "process", "procurement", "sales", "manufacturing", "inventory", "close",
 "purchase to pay", "order to cash", "make", "p2p", "o2c"]),

# =====================================================================
# 02 — Architecture
# =====================================================================

("architecture-overview", "EVO Architecture in One Page", "Architecture",
"""
The EvoERP stack, top to bottom.

## Layer diagram

```
┌─────────────────────────────────────────────────────────┐
│  User-facing UI                                         │
│  T7*.DFM (plaintext Delphi forms, 1,109 total)          │
│  Rendered by the TAS Pro 7 runtime                      │
├─────────────────────────────────────────────────────────┤
│  Business logic — TAS Pro 4GL                           │
│  BK*.SRC → *.RUN  (TAS Pro 5/6 legacy, plaintext)       │
│  T7*.SRC → *.RWN  (TAS Pro 7, encrypted — Twofish CFB)  │
├─────────────────────────────────────────────────────────┤
│  Runtime                                                │
│  C:\\ISTS\\tp7runtime.exe  (Delphi 7, 33 MB)             │
│  + qtintf70.dll (Qt CLX), c4dll.dll (CodeBase DBF)      │
│  + DCPcrypt (Twofish, SHA1)                             │
├─────────────────────────────────────────────────────────┤
│  Reports                                                │
│  RBDsgnr.exe → *.RTM templates                          │
│  Rendered via Nevrona ReportBuilder, EXEC_RB keyword    │
├─────────────────────────────────────────────────────────┤
│  Data                                                   │
│  Pervasive PSQL (Btrieve) — 659 tables, 24,113 fields   │
│  Per-company files: *.B / *.B22 / *.BI2 / …             │
│  Catalog in FILE.DDF / FIELD.DDF / INDEX.DDF            │
└─────────────────────────────────────────────────────────┘
```

## Where each piece lives

- **Client install** (`C:\\ISTS\\`): `StartEvo.exe`, `tp7runtime.exe`,
  DLLs, local caches (`DFM\\`, `PDFS\\`), `WHOAMI.DBA` seat identity.
- **Shared share** (`\\\\i2s109-solidcrm\\DBAMFG$\\`): every `.RWN`,
  `.DCY`, `.DFM`, `.RTM`, plus per-company data folders (`Default`,
  `22`, `AB`, `I2`, `Goldstar`, etc.).

## How a click becomes a database write

1. User selects a menu item → runtime loads `T7XXY.RWN` from the share.
2. RWN's compiled TAS-Pro code runs: `open BKARCUST lock W`, `enter`
   statements build a record, `ins` writes it.
3. Pervasive handles the write to the per-company `.B` file.
4. Any GL posting goes through `BKGLTEMP` → `BKGLCHK` → `BKGLACHK`.
5. Reports call `EXEC_RB` with an `.RTM` template that renders to screen,
   printer, or PDF (via the `TASFile` data pipeline).

## Concurrency and locking

EVO uses **cooperative record locking**. A program opens a table with
`lock W` (write) and the Pervasive engine tracks who holds the lock
via [[table-BKSYMSTR|BKSYMSTR]] `WHOAMI` / `LOCK_OWNER`. Other users
see the message "Record is in use by XXX".

## Integration surfaces

- **ODBC** — Pervasive exposes every table via SQL. Documented in the
  help topic `odbc_data_connection`.
- **Java** — `EvoPVT.jar` is a JavaFX helper that writes tasks into an
  `ISJAVA` table that TAS programs poll. See [[java-integration]].
- **OLE / COM** — TAS's `OLECALL` keyword invokes COM objects.
- **HTTP** — `GET_WEBSOURCE` runtime keyword fetches URLs.
- **Email** — built-in SMTP (`EvoEMTrns.RWN`).

## Related

- [[boot-sequence]] — what happens at launch
- [[security-model]] — users, companies, permissions
- [[file-formats]] — the eight file types you'll encounter
- [[reporting-pipeline]] — how reports flow
""",
["architecture", "stack", "layers", "tas pro", "runtime", "pervasive", "delphi",
 "client server", "concurrency", "locking"]),

("boot-sequence", "Boot Sequence — Launch to Main Menu", "Architecture",
"""
Step-by-step of what happens when a user launches EVO.

## 1. Shortcut click

`C:\\ISTS\\EvoERP.lnk` points to `C:\\ISTS\\StartEvo.exe` with working
directory `C:\\ISTS\\`.

## 2. StartEvo.exe

The launcher (37 KB):

1. Checks that `tp7runtime.exe` exists.
2. Reads `C:\\ISTS\\taspro7.ini` for the default run-program path.
3. Spawns `tp7runtime.exe` with the menu RWN as the initial program.

## 3. taspro7.ini — the machine config

```
[Setup]
DataDictPath=\\\\I2S109-SOLIDCRM\\DBAMFG$\\
DfltRunPrg=\\\\I2S109-SOLIDCRM\\DBAMFG$\\EvoERPmenu.rwn
MultiUser=1
HelpFileName=\\\\I2S109-SOLIDCRM\\DBAMFG$\\EvoHELP.CHM

[FileManager]
UseCodeBase=0
UseBtrvMemos=1

[Misc]
Serial=<license>
Date=<date>
```

See [[taspro7-ini-reference]] for every section.

## 4. tp7runtime.exe — the runtime engine

A 33 MB Delphi 7 executable that:

1. Reads `taspro7.ini` and the registry key
   `HKCU\\Software\\Addsum\\TAS Pro 7\\`.
2. Performs license check (R4 check against `Serial=`).
3. Loads DLLs: `qtintf70.dll` (Qt CLX), `c4dll.dll` (CodeBase),
   `zipdll.dll`/`unzdll.dll` (zip).
4. Reads local bootstrap files: `suwin6.dcy`, `suwin7.dcy`,
   `suwin6t.rwn`, `suwin7.rwn` from `C:\\ISTS\\`.
5. Loads the main RWN: `\\\\I2S109-SOLIDCRM\\DBAMFG$\\EvoERPmenu.rwn`.
6. Decrypts the RWN (Twofish CFB, key in runtime — see [[dcy-rwn-decryption]]).
7. Executes the compiled TAS 4GL program.

## 5. EvoERPmenu.RWN — the main menu program

The main-menu RWN:

1. Loads `EVOLOGO.DCY` (splash screen).
2. Prompts login via `EVOMENU_LOGIN.DCY`:
   - User enters code and password.
   - TAS program reads `AHSYLOG` for the user record.
   - Validates password (stored encrypted via TAS `ENCRYPTSTR`).
   - Sets session state from `AHSY_USER_ACCES_*` permission flags.
3. Prompts company selection via `EVOMENU_SELCOMP.DCY`:
   - User picks one of the active companies.
   - Runtime sets the `DfltCompanyCode` and adjusts file-open paths
     (e.g. `BKARCUST.B22` for company "22").
4. Displays the hierarchical menu tree from `EVOERPMENU.DCY`.

## 6. Per-user / per-workstation state

- `C:\\ISTS\\WHOAMI.DBA` (35 bytes) — this workstation's identity.
  Written by `EVOSERVICESETUP` and used for lock ownership.
- `C:\\ISTS\\CHMHELP.EVO` (35 bytes) — "EvoHELP now set for this
  computer" marker — confirms the CHM help file has been configured.
- `C:\\ISTS\\EvoSettings.INI` — per-machine module access toggles.

## 7. Menu-item selection

Picking a menu entry (e.g. "Enter Customers" under AR):

1. Runtime reads the menu-node record from `EVOERPMENU.DCY`.
2. Menu node stores the RWN filename to run (`T7ARA.RWN`).
3. Runtime loads and decrypts `T7ARA.RWN`.
4. Also loads `T7ARA.DFM` (plaintext form layout) and renders the window.
5. TAS program starts executing; the user is now "in AR-A".

## Idle timeout

The runtime has an idle timer (`tmrExitLicense`) that can force
logout after inactivity — see the [[table-BKSYMSTR|BKSYMSTR]] timeout
settings.

## Related

- [[security-model]]
- [[multi-company]]
- [[taspro7-ini-reference]]
""",
["boot", "startup", "launch", "startevo", "tp7runtime", "login", "company", "menu"]),

("security-model", "Security, Users, and Permissions", "Architecture",
"""
How EVO decides who sees what.

## The user master — AHSYLOG table

Every user is a row in [[table-AHSYLOG|AHSYLOG]], which has 23 fields:

| Field | Size | Meaning |
| ----- | ---- | ------- |
| `AHSY_USER_LEVL` | 2 | Role/level code (`AD`=admin, `SU`=super, `MG`=manager, `US`=user) |
| `AHSY_USER_MENU` | 4 | Starting menu code for this user |
| `AHSY_USER_CTRL` | 1 | Active flag |
| `AHSY_USER_ACCES_1..20` | 1 each | Per-module permission flags |

## The 20 permission slots

Each `AHSY_USER_ACCES_N` holds a single character: `Y` = full,
`R` = read-only, `N` = no access. The mapping from slot number to
module is maintained by the admin via `SM-H (Enter Users)`. Typical
layout observed in similar DBA Manufacturing installs:

| Slot | Module |
| ---- | ------ |
| 1 | AR |
| 2 | AP |
| 3 | IN |
| 4 | SO |
| 5 | PO |
| 6 | WO |
| 7 | GL |
| 8 | BM |
| 9 | MR |
| 10 | PR |
| 11 | DC |
| 12 | QC |
| 13 | JC |
| 14 | CS |
| 15 | ES |
| 16 | SR |
| 17 | PI |
| 18 | SH |
| 19 | ED |
| 20 | SM |

*(Note: the exact mapping on this install needs to be confirmed — the
table has 20 slots and ~20 modules; the pairing is admin-configurable.)*

## The user's starting menu

`AHSY_USER_MENU` (4 chars) points to a menu tree root stored in
`EVOERPMENU.DCY`. Different users can see entirely different menus —
e.g. a shop-floor user might start at a custom "DC only" menu with no
AP/GL visibility at all.

## Login flow

1. Login screen reads user input.
2. Program looks up `AHSYLOG` by user code.
3. Password is stored encrypted via the TAS runtime's `ENCRYPTSTR`
   (same symmetric scheme as the form encryption). Password field was
   not observed in the `AHSYLOG` schema extract — likely in a parallel
   table such as `BKPSUSER`.
4. If valid, the program sets session variables from `AHSY_USER_*` and
   loads the user's menu tree.

## Per-machine identity

[`WHOAMI.DBA`](ref:whoami-dba) on every workstation stores a 35-byte
"who is this seat" record. Decoded: `ADMIN[padded]HH:MM:SS PYYYYMMDD\\r\\n`.
Used for:
- Multi-user record-lock ownership display ("in use by ADMIN")
- Printer/form override lookups per seat
- License seat counting

## Password policy

Configurable under `SM` — typical options include:
- Minimum length (default 4)
- Forced change every N days
- Lockout after N failures

Screens: `EVOCHANGEPASS.DCY` (user-initiated change),
`EVORESETPASS.DCY` (admin-initiated).

## Auditing

Every transaction carries the current user's `WHOAMI` code in a
"last modified by" field, so you can trace who did what. Table-
specific audit trails exist in `BKSYLOG` (system log).

## Related

- [[table-AHSYLOG]]
- [[multi-company]] — companies are orthogonal to users
- [[recipe-add-user]] — hands-on
""",
["security", "user", "permissions", "access", "password", "login", "role", "auth",
 "ahsylog", "whoami"]),

("multi-company", "Multi-Company Setup", "Architecture",
"""
EVO supports running any number of independent "companies" against a
single installation. Each company has its own data but shares the
program code.

## How it works

Every data table exists once per company, identified by a file-
extension suffix. Example:

| File | Company |
| ---- | ------- |
| `BKARCUST.B` | `Default` |
| `BKARCUST.B22` | Company `22` |
| `BKARCUST.BI2` | Company `I2` |
| `BKARCUST.BAB` | Company `AB` |

All companies share:

- The same table schema (Pervasive DDF in each company folder)
- The same compiled programs (RWN files)
- The same forms (DFMs)
- The same help file

## Company folders seen on this install

- `\\\\i2s109-solidcrm\\DBAMFG$\\Default\\` — primary/seed company
- `22`, `AB`, `AT`, `CA`, `Goldstar`, `I2`, `IT`, `UU` — active user-
  facing companies
- `DefaultSQL` — SQL-centric variant (for the EvoPVT.jar helper)
- `Testdata`, `DEV` — non-production
- `Bak Up`, `Menu Backup`, `Recovered` — backups

## Switching companies

At login, the user picks from the active-company list
(`EVOMENU_SELCOMP.DCY`). The runtime then sets its default data path
to the chosen company folder, and all subsequent `open <table>` calls
read from that folder's files.

Switching companies mid-session requires logging out and back in.

## What's per-company vs shared

**Per-company** (unique per folder):
- Customer master (`BKARCUST`)
- Vendor master (`BKAPVEND`)
- Inventory (`BKICMSTR`)
- All transactional data (orders, invoices, GL)
- Company settings (`BKSYMSTR`)
- Users? — `AHSYLOG` is typically per-company, so each company has
  its own user list

**Shared across companies**:
- Programs (`.RWN`, `.RUN`, `.DFM`)
- Reports (`.RTM`)
- Help file (`EvoHELP.CHM`)
- Menu tree (`EVOERPMENU.DCY`) — but individual users can have
  different menus via `AHSY_USER_MENU`

## Consolidation

Two use cases for multi-company:

1. **Legal separation** — each LLC/entity has its own company.
   Financials, AP/AR, taxes all segregated.
2. **Divisional** — one legal entity, multiple divisions reporting
   independently. Use `AM-G (Consolidate Financials)` to roll up.

## Data volumes

Some tables can be LARGE. Typical sizes seen (per company):
- Invoice-line tables: tens of millions of rows after years of use
- GL transaction tables: hundreds of thousands per year
- Inventory transaction log: depends on data-collection intensity

## Related

- [[table-BKSYMSTR]] — company settings live here
- [[recipe-add-company]]
- [[module-AM|AM - Archive/Maintenance]] for periodic cleanup
""",
["company", "multi-company", "companies", "data folder", "separation", "division",
 "consolidation", "b22", "default"]),

# =====================================================================
# 03 — Modules overview
# =====================================================================

("module-map", "Module Map — All 20+ Functional Areas", "Modules",
"""
EVO is organized into functional modules identified by 2-letter codes.
Each gets a dedicated page with menu codes, tables, forms, and
workflows.

| Code | Module | Menu ops | Tables | Forms |
| ---- | ------ | -------: | -----: | ----: |
| [[module-AR|AR]] | Accounts Receivable | 17 | 29 | 24 |
| [[module-AP|AP]] | Accounts Payable | 19 | 26 | 33 |
| [[module-IN|IN]] | Inventory | 40 | 19 | 67 |
| [[module-SO|SO]] | Sales Orders | 48 | 7 | 69 |
| [[module-PO|PO]] | Purchase Orders | 29 | 8 | 41 |
| [[module-WO|WO]] | Work Orders | 31 | 30 | 68 |
| [[module-GL|GL]] | General Ledger | 16 | 28 | 24 |
| [[module-BM|BM]] | Bill of Materials | 10 | 10 | 16 |
| [[module-MR|MR]] | MRP | 12 | 4 | 18 |
| [[module-PR|PR]] | Payroll | 29 | 16 | 40 |
| [[module-DC|DC]] | Data Collection | 7 | 7 | 26 |
| [[module-QC|QC]] | Quality Control | 0 | 2 | 15 |
| [[module-JC|JC]] | Job Costing | 18 | 2 | 14 |
| [[module-CS|CS]] | Commission System | 16 | 16 | 12 |
| [[module-ES|ES]] | Estimating | 8 | 4 | 7 |
| [[module-SR|SR]] | Service / Repair | 9 | 0 | 12 |
| [[module-PI|PI]] | Physical Inventory | 9 | 7 | 10 |
| [[module-SH|SH]] | Shipping | 16 | 1 | 15 |
| [[module-ED|ED]] | EDI | 6 | 6 | 3 |
| [[module-SM|SM]] | System Manager | 34 | 10 | 109 |
| [[module-AM|AM]] | Archive / Maintenance | 17 | — | — |
| [[module-AD|AD]] | Admin Defaults | 3 | — | — |

## Supporting subsystems

- [[subsystem-evonotes|Evo Notes]] — per-record notes/CRM
- [[subsystem-evoscheduler|Evo Scheduler]] — cron-like job runner
- [[subsystem-evolinks|Evo Links]] — document attachments
- [[subsystem-evofno|Evo FNO]] — Features and Options configurator
- [[subsystem-evoupdate|Evo Update]] — in-app software updates

## Module-to-workflow mapping

| Workflow | Primary modules | Supporting |
| -------- | --------------- | ---------- |
| Procurement | PO, AP | IN, GL |
| Sales | SO, AR, SH | IN, CS |
| Manufacturing | WO, BM, RO, DC | IN, JC, QC |
| Inventory | IN, PI | LC, SC |
| Close | AM, GL | SM |
| Payroll | PR | GL, CS |

## Related

- [[core-workflows]]
- [[menu-codes-reference]]
""",
["modules", "map", "modules list", "areas", "functions"]),

# =====================================================================
# 04 — Data / reference
# =====================================================================

("tables-index", "Database Tables — Full Reference", "Data",
"""
EVO has **659 tables**, **24,113 fields** total. The full schema was
extracted from the Pervasive DDF set.

## By module-prefix

Tables group by 4-letter prefix (first 2 letters = module, next 2
= sub-area):

| Prefix | # Tables | Meaning |
| ------ | -------: | ------- |
| BKAP | 24 | Accounts Payable |
| BKAR | 27 | Accounts Receivable |
| BKBM | 10 | Bill of Materials |
| BKCM | 46 | Company Master / currency |
| BKGL | 28 | General Ledger |
| BKIC | 16 | Inventory Core |
| BKPR | 16 | Payroll |
| BKSY | 8 | System config |
| BKPO | 2 | Purchase Orders (w/ more under BKAP) |
| BKSO | 7 | Sales Orders |
| BKCS | 16 | Commission System |
| BKQC | 2 | Quality Control |
| WO*  | 30 | Work Orders / routing / labor |
| MT*  | 6 | Master second-generation |
| Other | ~365 | Customization, utility, non-prefixed |

## Top 20 tables by field count

| Table | Fields | Role |
| ----- | -----: | ---- |
| `BKPRGLFL` | 664 | Payroll GL Field Layout |
| `BKSLEVEL` | 422 | Sales Levels config |
| `BKAPINVL` | 390 | AP Invoice Lines |
| `BKAPRIVL` | 390 | AP Retention Invoice Lines |
| `BKPRMSTR` | 384 | Payroll master |
| `BKPRW2` | 384 | Payroll W-2 output |
| `BKYSMSTR` | 355 | Secondary system master |
| `BKSYMSTR` | 286 | Primary system master |
| `BKSYLOG` | 215 | System log |
| `BKPRTCFG` | 205 | Payroll tax config |

## Key tables by purpose

| Purpose | Primary table |
| ------- | ------------- |
| [[table-BKARCUST|Customer master]] | `BKARCUST` |
| [[table-BKAPVEND|Vendor master]] | `BKAPVEND` |
| [[table-BKICMSTR|Item master]] | `BKICMSTR` |
| Sales order header | `BKARINV` |
| Sales order lines | `BKARINVL` |
| Purchase order header | `BKAPPO` |
| Purchase order lines | `BKAPPOL` |
| Work order header | `WORKORD` |
| Work order BOM | `WOBOM` |
| Work order routing | `WOROUT` |
| Labor transactions | `WOLABOR` |
| GL Chart of Accounts | `BKGLCCOA` |
| GL Accounts (balances) | `BKGLACHK` |
| GL Journal entries | `BKGLAGJL` |
| User master | `AHSYLOG` |
| System settings | `BKSYMSTR` |

## Searching for a field

- Press `Ctrl+K` and search field names directly (e.g. "invoice
  number" finds `BKAR_INV_NUM`, `BKAP_INV_NUM`).
- Use the [[field-search]] tool to search by type/size/prefix.
- Or jump to a specific table via its page.

## Naming conventions

- Field names use `<prefix>_<area>_<name>` format, e.g. `BKAR_CUSTCODE`.
- In TAS source, the same field is written with dots: `BKAR.CUSTCODE`.
- The compiler normalizes both spellings.

## Type codes

| Code | Meaning | Binary size |
| ---- | ------- | ----------- |
| STRING | fixed-length alpha | `size` bytes |
| INTEGER | signed 2 or 4 byte int | 2 or 4 |
| FLOAT | IEEE 754 double | 8 |
| DATE | Pervasive date | 4 |
| TIME | Pervasive time | 4 |
| DECIMAL / MONEY | BCD decimal | varies |
| LOGICAL | boolean | 1 |
| NUMERIC | ASCII numeric | varies |
| UBINARY | unsigned binary | 1, 2, or 4 |

## Accessing via SQL

Every table is available over **Pervasive ODBC**. The field names at the
SQL level match the DDF names. For help setting up ODBC, see
[[odbc-access]].

## Related

- [[data-dictionary-overview]]
- [[field-search]]
""",
["tables", "database", "schema", "fields", "reference"]),

("odbc-access", "Accessing EVO Data via SQL (Pervasive ODBC)", "Integration",
"""
Because EVO uses Pervasive PSQL under the hood, every table is
available via **ODBC** as a SQL-queryable data source — **read-only
from a BI tool's perspective, writable if you configure the DSN that
way**.

## Setup

On this workstation, Pervasive ODBC is already installed:

```
C:\\Program Files\\Actian\\PSQL\\bin
```

To configure an ODBC DSN:

1. Control Panel → Administrative Tools → ODBC Data Sources (32-bit).
2. Add System DSN → Pervasive ODBC Client Interface.
3. Point it at the company's database (e.g. `DBAMFG`).
4. Test connection.

## Useful queries

### List every customer
```sql
SELECT BKAR_CUSTCODE, BKAR_CUSTNAME, BKAR_OUTINV
FROM BKARCUST
WHERE BKAR_OUTINV > 0
ORDER BY BKAR_CUSTNAME;
```

### Open POs with vendor
```sql
SELECT PO.BKAP_APO_NUM, V.BKAP_VENDNAME, PO.BKAP_APO_DATE,
       PO.BKAP_APO_TOTAMT
FROM BKAPAPO PO
JOIN BKAPVEND V ON V.BKAP_VENDCODE = PO.BKAP_APO_VEND
WHERE PO.BKAP_APO_STATUS = 'O';
```

### Inventory valuation
```sql
SELECT BKIC_PROD_CODE, BKIC_PROD_DESC,
       BKIC_PROD_UOH,
       BKIC_PROD_AVGC,
       BKIC_PROD_UOH * BKIC_PROD_AVGC AS valuation
FROM BKICMSTR
WHERE BKIC_PROD_UOH > 0
ORDER BY valuation DESC;
```

### Schema exploration (via system catalog)
```sql
SELECT Xf$Name AS TableName, Xf$Loc AS FileName
FROM X$File
ORDER BY Xf$Name;

SELECT f.Xf$Name AS TableName, fld.Xe$Name AS FieldName,
       fld.Xe$DataType, fld.Xe$Offset, fld.Xe$Size
FROM X$File f
JOIN X$Field fld ON fld.Xe$File = f.Xf$Id
WHERE f.Xf$Name = 'BKARCUST';
```

## Writing back via SQL

You can INSERT/UPDATE from SQL, but **don't** — EVO enforces business
rules (GL posting, lock protocols, audit trail) inside the TAS programs
that SQL bypasses. Direct SQL writes can orphan records.

For automated writes, use the [[java-integration|ISJAVA queue]] —
the Java tool writes parameters into a table that TAS programs poll
and process, preserving all business rules.

## Related

- [[tables-index]] — every table available
- [[java-integration]]
""",
["odbc", "sql", "pervasive", "actian", "integration", "query"]),

# =====================================================================
# 05 — File formats
# =====================================================================

("file-formats", "File Formats Guide", "Reference",
"""
EVO uses roughly a dozen file types. Some are standard, some custom.

## Program files

| Ext | Type | Readable? | Detail |
| --- | ---- | --------- | ------ |
| `.SRC` | TAS 4GL source | **Plaintext** | [[format-src|SRC language guide]] |
| `.RUN` | TAS Pro 5/6 compiled program | Binary, readable strings | Legacy generation |
| `.RWN` | TAS Pro 7 compiled program | **Encrypted** (Twofish CFB) | [[format-rwn]] / [[dcy-rwn-decryption]] |
| `.LIB` | TAS library source | Plaintext | Rarely seen |
| `.LCY` | TAS library encrypted | Encrypted | Same as RWN scheme |

## UI / forms

| Ext | Type | Readable? | Detail |
| --- | ---- | --------- | ------ |
| `.DFM` | Delphi form layout | **Plaintext** | [[format-dfm]] |
| `.DCY` | Encrypted DFM | Encrypted | Same encryption as RWN |
| `.SCR` | Legacy screen def | Binary | Pre-Delphi era |

## Data

| Ext | Type | Readable? | Detail |
| --- | ---- | --------- | ------ |
| `.B` | Btrieve data file | Binary | Per-company |
| `.B22`, `.BI2`, etc. | Btrieve, per-company | Binary | Suffix = company code |
| `.mdx` | Btrieve index | Binary | Paired with `.B` |
| `.XLB` | Btrieve lock file | Binary | Runtime-created |
| `.DDF` | Pervasive data dict | Binary | FILE / FIELD / INDEX / etc. |
| `.UPD` | DDF update snapshot | Binary (Btrieve) | Shipped with updates |

## Reporting

| Ext | Type | Readable? | Detail |
| --- | ---- | --------- | ------ |
| `.RTM` | ReportBuilder template | Binary (Delphi TPF0) | [[format-rtm]] |
| `.btm` | Backup RTM | Binary | Same format |
| `.PDF` | Output | — | Reports rendered to PDF |
| `.TXT` | Output / export | Plaintext | Report spools, XPT exports |
| `.XPT` | Export layout def | Plaintext | Fixed-width config |
| `.IMP` | Import layout def | Plaintext | Simple CSV-like |

## Other

| Ext | Type | Detail |
| --- | ---- | ------ |
| `.CHM` | Windows HTML Help | `EvoHELP.CHM` |
| `.jar` | Java archive | `EvoPVT.jar` |
| `.DBA` | Identity token | `WHOAMI.DBA` |
| `.EVO` | Marker file | `CHMHELP.EVO` |
| `.INI` | Config | `taspro7.ini`, `EvoSettings.INI` |
| `.dll` | Windows DLL | `c4dll.dll`, `qtintf70.dll` |

## Related

- [[format-src]], [[format-dfm]], [[format-rwn]], [[format-rtm]]
- [[dcy-rwn-decryption]]
""",
["file", "format", "extension", "src", "dfm", "dcy", "rwn", "rtm", "b", "btrieve"]),

("subsystem-evonotes", "Evo Notes — Per-Record Attached Notes", "Architecture",
"""
Evo Notes is a **per-record note-log system** that attaches free-form
notes to any master record — customer, vendor, item, work order,
invoice, whatever. Universal. Used as a lightweight CRM and audit trail.

## How it works

- Every master record has an "Evo Notes" button on its form.
- Clicking it opens `EvoNotes.RWN` with the current record's key.
- Each note has: author (WHOAMI), timestamp, subject, body.
- Notes are append-only from the user's view (admins can delete).
- Notes are searchable globally via `EvoNoteSearch.RWN`.

## Relevant programs

- `EvoNotes.RWN` — main entry/display
- `EvoNotesARCH.RWN` — archive
- `EvoNoteSearch.RWN` — cross-record search
- `EvoNotesPrt.RWN` — print
- `EvoNotesRpt.RWN` — report
- `classic2evonts.DFM` — migrate from classic DBA notes

## Related

- [[architecture-overview]]
- [[subsystem-evolinks]]
""",
["notes", "evo notes", "notes system", "crm", "record notes"]),

("subsystem-evoscheduler", "Evo Scheduler — Cron-Like Job Runner", "Architecture",
"""
`EvoScheduler.RWN` runs EVO jobs on a schedule — like cron for the ERP.
Paired with `EvoService.RWN` for unattended execution as a Windows
service.

## Typical jobs

- Nightly MRP (`AUTOT7MRF.RWN`)
- Morning aging reports
- EDI file pickups
- Backup runs

## Configuration

- `EvoSchedSetup.RWN` — edit schedule entries (name, cron-like
  expression, program to run, arguments).
- Stored in a scheduler table (naming TBD; likely `BKSCHED*` but not
  found in the 659-table inventory — may be created dynamically).

## Related

- [[architecture-overview]]
- [[recipe-run-mrp]]
""",
["scheduler", "cron", "schedule", "auto", "unattended", "batch", "evo scheduler"]),

("subsystem-evolinks", "Evo Links — Document Attachments", "Architecture",
"""
Evo Links attaches arbitrary documents (PDFs, photos, emails, scanned
forms, etc.) to master records.

## How it works

- Files stored in `\\\\i2s109-solidcrm\\DBAMFG$\\LinkDoc\\`.
- Database table maps `<record-key, filename>`.
- Display-in-context from any master form via "Evo Links" button.

## Programs

- `EvoLinks.RWN` — main
- `EvoLinkCVT.RWN` — converter / migration

## Related

- [[subsystem-evonotes]]
- [[architecture-overview]]
""",
["links", "attachments", "documents", "files", "evo links"]),

("subsystem-evofno", "Evo Features & Options — Product Configurator", "Architecture",
"""
Features & Options (FNO) is EVO's **product configurator** — the
"Dell-laptop style" choose-your-CPU/RAM/screen dialog. Launched from
sales-order line entry for configurable items.

## How it works

1. An item has `BKIC_PROD_FNO_FLAG = Y` in its master record.
2. When entering that item on an SO, EVO launches `EvoFNOSO.RWN`.
3. User walks through feature categories (e.g. "Color") and picks
   options (e.g. "Red").
4. The configured line's price is the sum of feature-option prices.
5. Optional: generate a unique SKU / item code for this configuration.

## Related modules

- `EvoFNO.RWN` — master config
- `EvoFNOPO.RWN` — on PO entry (buy configured items)
- `EvoFNOSO.RWN` — on SO entry (sell configured items)
- `EvoFNOWO.RWN` — on WO entry (make configured items)

## Help topic

CHM topic: `using_features_and_options_in_sales_orders` and
`setting_up_features_and_options`.

## Related

- [[module-SO]]
- [[architecture-overview]]
""",
["fno", "features", "options", "configurator", "configurable", "evo fno"]),

("java-integration", "Java Integration — EvoPVT.jar + ISJAVA Queue", "Integration",
"""
`C:\\ISTS\\EvoPVT.jar` is a JavaFX helper that extends EVO with
capabilities TAS can't easily do (modern SQL, HTTPS, OAuth,
advanced CSV).

## Usage pattern — ISJAVA queue

The integration is **queue-based**:

1. Java tool writes a parameterized row into the `ISJAVA` table:
```sql
INSERT INTO ISJAVA (IS_JAVA_UID, IS_JAVA_DATE, IS_JAVA_PARAM_1, ...)
VALUES (?, ?, ?, ...);
```
2. A TAS program polls `ISJAVA` by UID.
3. TAS processes the row and writes results back (either to ISJAVA
   itself or to a domain table).

This keeps business logic in TAS while using Java for transport and
third-party integrations.

## Structure of EvoPVT.jar

Inside the JAR (unzip-able):

- `com.evoerp.Evo` — JavaFX main application
- `com.evoerp.TASKS.sql.PervasiveDatabase` — JDBC wrapper
- `com.evoerp.TASKS.sql.Main$WindowsUtils` — CLI entry
- `com.evoerp.javafx.*` — UI widgets (SplashScreen, TabularView,
  CalendarView, LookupPane, …)
- `com.evoerp.sql.*` — lightweight SQL builder (AliasTable, Clause,
  AndClause, BinaryClause, …)
- `com.evoerp.util.*` — CSV, file, Windows registry helpers
- `com.pervasive.jdbc` — Pervasive JDBC driver
- `org.apache.commons.{codec,logging}` — shipped dependencies

## Invoking

- Standalone: `java -jar EvoPVT.jar` — opens the JavaFX UI.
- From TAS: `EXEC_TOP_WAIT "java -jar ... args"` — spawn with args.

## Related

- [[odbc-access]]
- [[architecture-overview]]
""",
["java", "jar", "evopvt", "isjava", "integration", "jdbc", "javafx"]),

("what-is-evoerp", "What is EvoERP? — At a Glance", "Getting Started",
"""
## One-paragraph summary

EvoERP is a **manufacturing ERP** for small and mid-size shops — the
current incarnation of **DBA Manufacturing**. It's sold by Addsum
Business Software and runs on the **TAS Professional 7** runtime.
Data lives in **Pervasive PSQL (Btrieve)**, the UI is **Delphi-based
VCL forms**, and reports render via **Nevrona ReportBuilder**.

## Installed version on this site

`C:\\ISTS\\DFM\\EVO.VER` reads `2024.1` — this is the installed release.

## Who built it

- **Addsum Business Software, Inc.** (current vendor / publisher,
  2004 → present).
- Earlier: **MGM Holdings, Inc.** (1984 – 2003).
- Core 4GL from **Business Tools, Inc.** (1985 – 1995).

## What's in this installation

- Client: `C:\\ISTS\\` (runtime, DLLs, local caches)
- Shared code + data: `\\\\i2s109-solidcrm\\DBAMFG$\\`
- Companies in use: `Default`, `22`, `AB`, `AT`, `CA`, `Goldstar`,
  `I2`, `IT`, `UU` (plus `DefaultSQL`, `Testdata`, `DEV`)
- Total database tables: **659**, with **24,113 fields**
- Compiled program modules: **2,439** (RWN/RUN/DCY)
- UI forms: **1,109** plaintext DFMs
- Report templates: **959** RTM + btm
- Help topics in the CHM: **779**
- User-facing operations: **759** unique menu codes

## What makes EVO different from general ERPs

- **Per-company file separation** — companies are entire directory
  clones. Cleaner than logical "company codes" in a shared DB.
- **TAS Pro 4GL** — not SQL-first. Business logic is code, not
  stored procedures.
- **Every record has notes** — [[subsystem-evonotes|Evo Notes]]
  attaches to any master record.
- **Heavy manufacturing DNA** — Work Orders, Routings, Data
  Collection, and MRP are first-class.
- **Simple integration surface** — ODBC for reads, [[java-integration|ISJAVA queue]]
  for writes.

## Related

- [[architecture-overview]]
- [[module-map]]
- [[core-workflows]]
- [[boot-sequence]]
""",
["evoerp", "what is", "overview", "addsum", "dba", "tas pro", "manufacturing", "erp"]),

("data-dictionary-overview", "Data Dictionary Overview", "Data",
"""
EVO's data layer is **Pervasive PSQL (Btrieve)**, exposed via the
standard Pervasive data-dictionary file set.

## The DDF files

Every company folder has:

- `FILE.DDF` — table catalog (which tables exist, what filename each has)
- `FIELD.DDF` — schema (every field of every table: name, type, offset, size)
- `INDEX.DDF` — index definitions
- `ATTRIB.DDF` — field attributes (picture, allowed chars)
- `OCCURS.DDF` — array-field repeat counts
- `RELATE.DDF` — declared inter-table relationships
- `TRIGGER.DDF` — triggers
- `VIEW.DDF` — SQL views
- `PROC.DDF` — stored procedures

## Scale

- **659 tables** total
- **24,113 fields**
- **Mean 37 fields per table**
- Largest: `BKPRGLFL` (payroll GL field layout) with 664 fields

## Per-company file extensions

Table files are named `<TABLE>.B<company-code>`:

| File | Company |
| ---- | ------- |
| `BKARCUST.B` | `Default` |
| `BKARCUST.B22` | Company `22` |
| `BKARCUST.BI2` | Company `I2` |

## Naming conventions

Field names follow `<tab-abbr>_<area>_<name>`:

- `BKAR_CUSTCODE` — BKARCUST's CUSTCODE field
- `BKAP_VENDNAME` — BKAPVEND's VENDNAME field
- `AHSY_USER_LEVL` — AHSYLOG's user level

In TAS source code, dots replace underscores (the compiler normalizes):

- `BKAR.CUSTCODE` in source = `BKAR_CUSTCODE` in DDF

## Access via SQL

Every table is available via Pervasive ODBC. See [[odbc-access]] for
DSN setup and example queries.

## Related

- [[tables-index]] — full table list
- [[odbc-access]] — SQL access
- [[architecture-overview]] — where the data layer fits
""",
["data dictionary", "schema", "ddf", "pervasive", "btrieve", "field", "table"]),

# =====================================================================
# File-format deep-dive pages
# =====================================================================

("format-src", "SRC — TAS Professional 4GL Source", "Reference",
"""
`.SRC` files are the **plaintext source code** for TAS Professional
programs — the language EVO is written in. ASCII, CR+LF line endings,
no BOM. Keywords are case-insensitive; `;` starts a line comment.

Only a handful survive on the share (`BKAWLB.SRC`, `BKDCA.SRC`,
`BKLME.SRC`, `BKMRF.SRC`, `BKROA.SRC`, `Bkaph.SRC`, `Bkapha.SRC`) —
copies in `samples/src/`. Most TAS source has been stripped before
distribution; only compiled `.RWN` / `.RUN` ships.

## Top-of-file directives

```src
;BKAWLB.src
;Cvtd from TAS-Pro 3.0 edt to 5.0 src on 01/18/96
;
#UDX           ;allow both UDFs and UDCs
#LIB LOOKUPS   ;link the DBA Routines library
#LIB windows
#INC HELPSCRN  ;source-level include
SETUP_COLOR    ;macro from TASCOLOR.OVL
```

| Directive | Meaning |
| --- | --- |
| `#PRO3` | Target the Pro-3 compiler dialect (rare, often commented out). |
| `#UDX` | Allow **U**ser-**D**efined **F**unctions and **C**ommands. |
| `#LIB <name>` | Link against a named library (`LOOKUPS`, `windows`, `DBA`). |
| `#INC <name>` | Source-level include. |
| `#TDATA <n>` | Set total data segment size. |
| `#WINFORM` | This program has a Windows form (loads paired `.DFM`). |
| `#WINREPORT` | This program drives a ReportBuilder template. |
| `#FORMSENCRYPTED` | Companion form is `.DCY` (encrypted), not `.DFM`. |
| `#FORCERWN` | Must run as RWN, not legacy RUN. |
| `#MAINMENU` | Program is a menu entry. |
| `#DONTCOMPILE` | Skip this file during batch compile. |

## Variables — `define`

```src
define PRT_WHR     type A size 1
define PAGE        type I size 5
define SELECT_FROM1 type D size 8
define MENU_HLDR   type A size 22 array 7
define inc.all.class, inc.blank.class type A size 1
```

Field types, from the compiler's own error 7621 — `"Field type must be
one of: I, B, R, P, T, D, N, L, A, F"`:

| Code | Type |
| --- | --- |
| `A` | Alpha (fixed-length string) |
| `N` | Numeric (decimal; `dec <n>` sets fraction digits) |
| `I` | Integer (up to 10 digits) |
| `B` | Byte |
| `R` | Record position / file pointer |
| `P` | Memory pointer |
| `T` | Time |
| `D` | Date |
| `L` | Logical (boolean; `.t.` / `.f.` literals) |
| `F` | File handle / float |

Arrays: `array <N>` — 1-based, fixed size. Identifiers can contain `.`
(`inc.all.class`) — a holdover from dBase/Clipper tradition; the
compiler rewrites `.` to `_` when persisting to the DDF, so source
`BKAR.CUSTCODE` = DDF `BKAR_CUSTCODE`.

## Database I/O

```src
open BKARCUST lock N
find F srch BKSY.ARINV.NUM nlock
clr BKSYMSTR rec
```

- `open <table> lock N` — open a Btrieve data file, `N` = shared read.
- `find F srch <key>` — find first record matching key.
- `clr <table> rec` — clear the record buffer.
- Field access: `bksy.comp.name` — prefix is a 4-letter table
  abbreviation (`BKSY` = `BKSYMSTR`).

## Control flow

`if cond ... [else_if ...] [else ...] endif`
`for(v; start; end; step) ... next`
`while ... loop_if ... exit_if`
`select ... otherwise ... endselect`
`goto <label>`, `gosub <label>` / `return`, `chain`, `chainr`, `quit`.

Keyboard traps: `trap <key> goto <label>` / `trap <key> gosub <label>`
/ `trap <key> dflt` (revert to default behaviour).

## UI — screens and input

```src
mount SELECT2 type S
prg_hdr "LW-J-B  Print Work Order Schedule"

START:
  xtrap chg ignr
  fnc_list '','Esc Exit'
  enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
  menu at 5,5 len 9 wdt 19 fld MENU_HLDR cntr SORT_BY nch 7 ttl "Sort by"
```

Input-statement grammar, **verbatim from the runtime string table**:

```
ENTER  |(*field_name*) (*MASK f/c/e*) (*HELP lbl/@udf*) (*UPAR lbl*)
       (*UP*) (*ACR*) (*PSWD*) (*AT col;row*) (*NOREV*) (*COLOR f/c/e*)
       (*PRE udf*) (*POST udf*) (*DFLT f/c/e*) (*VLD udf*) (*VLDM f/c/e*)
       (*DO udf*) (*ARRAY*) (*CNTR fn/v*)
       (*ENUM f/c/e1,...*) (*AUTO_SRCH*) (*GROUP f/c/e*)
       (*NOCLICKOFF*) (*NOCLICKON*)
```

Inline user-defined functions live in `{ … }` blocks attached to the
statement that references them:

```src
enter INC.ALL.CLASS mask 'YN' up post post.incall() acr
  {
    func post.incall
      if inc.all.class = 'Y'
         for(mcntr;1;6;1)
           inc.class[mcntr] = ' '
         next
         inc.blank.class = 'Y'
      endif
      ret .t.
  }
```

## What the language can reach

From the runtime's keyword list — not a toy 4GL:

- **Windows:** `OLECALL` (COM/OLE), `LOAD_DLL`, `REGEDIT`, `SENDKEYS`,
  `APPACTIVATE`, `ISREMOTESESSION`, `GET_UNC_PATH`, `PLAYWAV`.
- **Network / HTTP:** `GET_WEBSOURCE`, `GET_IP`,
  `GET_SERVER_DATETIME`.
- **SQL:** `SQLCALL`, `MYSQL_QUERY`.
- **Runtime eval:** `COMPILE_EXPR`, `COMPILE_SRC`, `EXEC_TOP_WAIT`.
- **Crypto:** `ENCRYPTSTR`, `DECRYPTSTR`.
- **Data engine:** `USECODEBASE` (switch to CodeBase DBF),
  `BTRIEVE_VERSION`, `PERVASIVE_SERVER`, `CREATE_DBF`,
  `REC_LOCK`, `UNLOCK`, `DUPCHECK`.
- **Reporting:** region-based (`INIT_REGION`, `MARK_REGION`,
  `PRINT_REPORT`) and ReportBuilder (`EXEC_RB`, `RTM_FN`,
  `REPORTNAME`, `PRINT_ARCHIVE`). See [[format-rtm]].
- **Forms:** `WMOUNT`, `LOAD_FORM`, `LOAD_MODAL_FORM`, `DATA_GRID`
  (bind a `TASDataGrid`), `NAVIGATOR`, `SET_OBJ_PROP`.

## Naming convention for SRC files

- `BK*` — Book-keeping / backbone modules from the TAS-Pro 3→5 era.
- `T6*` — TAS Pro 6 generation (mostly compiled `.RUN`, not shipped as `.SRC`).
- `T7*` — TAS Pro 7 generation (mostly compiled `.RWN` + `.DFM`).

Module letter code in positions 3–4: `AR` / `AP` / `IN` / `SO` / `PO`
/ `WO` / `GL` / `LW` / `LA` / `AW`.

## Related

- [[format-rwn]] — the compiled binary this source produces
- [[format-dfm]] — the paired UI form
- [[format-rtm]] — the report templates SRC programs drive
- [[src-deep-dive]] — longer walk-through of a single program
- [[file-formats]]
""",
["src", "source", "tas", "4gl", "language", "compiler", "syntax"]),


("format-rwn", "RWN / DCY — Compiled TAS Pro 7 Binaries (Encrypted)", "Reference",
"""
`.RWN` is the **compiled TAS Pro 7 program** — the binary that
`tp7runtime.exe` loads and runs. `.DCY` is the **encrypted form file**
paired with it (the plaintext form is a `.DFM`). `.SCY` and `.LCY` are
the same scheme applied to `.SRC` and `.LIB`.

All four formats share one encryption pipeline. That pipeline is
**confirmed by static analysis**, though the key itself has not been
recovered from the runtime.

## The encryption scheme

- **Cipher:** Twofish (16-byte block) via the DCPcrypt Delphi library
  (`TDCP_twofish`). No other 16-byte-block cipher is present in the
  runtime.
- **Mode:** CFB (ciphertext feedback). Proven by a divergence pattern
  across file pairs: where two plaintexts match, their ciphertexts
  XOR to the same value; where they diverge, the divergence begins
  on a 16-byte boundary.
- **IV:** the zero block. The first-block keystream is identical for
  every encrypted file on the install — verified across 37 RWN and
  14 DCY samples.
- **Key:** a 16/24/32-byte Twofish key derived at runtime from a
  passphrase baked into `tp7runtime.exe`. **Not recovered.**
- **File layout:**
  ```
  [8-byte per-file salt] [CFB-encrypted body of same length as plaintext]
  ```
  The salt varies per file but does **not** influence the keystream —
  different-salt/same-plaintext files produce identical ciphertext
  after the salt. Role appears to be integrity-check or timestamp.

The recovered first-block keystream is:

```
Stream[0] = 0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54
```

XOR this against bytes `8..23` of any encrypted file on the install
and you get the plaintext's first 16 bytes.

## How the encryption was identified

Strings inside `tp7runtime.exe`:

- At file offset `0x6232e4`:
  `"You may only encrypt .DFM, .SRC & .LIB files."` → `DFM→DCY`,
  `SRC→SCY`, `LIB→LCY`. The older `.RUN` format was never encrypted.
- At `0x34e735`: `TDCP_twofish`, `Twofish.pas`, `DCPcrypt`,
  `TDCP_sha1` — the full DCPcrypt library is statically linked.
- At nearby offsets:
  `"@TAS 7i Run Programs (RWN)|*.RWN|TAS 5.1 Run Programs (RUN)|*.RUN"`
  — the file-dialog filter, which dates the split between RUN (TAS 5/6)
  and RWN (TAS 7).

## Why the key is hard to get statically

The passphrase is never stored as a bare string. It is constructed at
run time from DCPcrypt's key-setup routine (`TDCP_cipher.InitStr`)
which applies SHA-1 expansion to whatever phrase is supplied. Tried
and failed:

1. Every printable string ≥ 3 chars in `tp7runtime.exe` (474,537 of
   them) as a direct Twofish key with zero / space / repeat padding.
2. MD5 / SHA-1 / SHA-256 of each of those strings.
3. ~60 hand-crafted EVO/TAS-related phrases with upper / lower /
   reverse / padded variants.
4. High-entropy scan of the 20 KB of `.text` around the `.DCY`
   references and the Twofish-class VMT.

None matched. What would work: live-debugger breakpoint on
`TDCP_twofish.Init`, read the key buffer. That requires a running
process, which is out of scope for static read-only analysis.

## What can be read today

- **First 16 bytes of every encrypted file** — via `Stream[0]` XOR.
  - Every `.DCY` decrypts to `object EditForm<N>:` (standard Delphi
    form text header) → confirms same plaintext domain as `.DFM`.
  - Every `.RWN` decrypts to a fixed 16-byte header whose bytes at
    positions 3/7/11/14/15 are invariant `f3 79 b2 31 ec` across 23
    samples → that's the TAS-Pro-7 compiled-program magic.
- **Full plaintext for 13 DCY files** that have a matching plaintext
  DFM still on the share. XORing plaintext with ciphertext yields the
  per-file keystream; the keystream validates that the DFM is the
  genuine source of the DCY.

Pairs in `samples/crypto/pairs/`:
`DBAMENU_LOGIN`, `DBAMENU_SELCOMP`, `EVOEMSG`, `EVOERROR`,
`EVOGETDATE`, `EVOMESSAGE`, `EVORESETPASS`, `GETALPHAGEN`,
`IMAGEPRINT`, `MDUMMY`, `NZEDEFS`, `PRINTTLL`, `T7CLOADING`.

## Naming conventions

- `T7<xx><y>.RWN` — TAS Pro 7 compiled program. `<xx>` = module code
  (AR / AP / IN / SO / PO / WO / GL …), `<y>` = variant letter.
- `T6<xx><y>.RUN` — older unencrypted TAS Pro 5/6 generation.
- `BK*.RWN` / `BK*.RUN` — backbone legacy modules.
- `EvoERPmenu.RWN` + `EVOERPMENU.DCY` — the main-menu program + form.
- Generic Evo* programs (`EvoNotes.RWN`, `EvoLinks.RWN`,
  `EvoScheduler.RWN`, `EvoUPDATE.RWN`, …) — later Addsum additions.

## Related

- [[dcy-rwn-decryption]] — full evidence trail + scripts
- [[format-dfm]] — the plaintext form paired with `.DCY`
- [[format-src]] — source language; `.SCY` is its encrypted form
- [[glossary-twofish]], [[glossary-dcpcrypt]], [[glossary-cfb]]
- [[file-formats]]
""",
["rwn", "dcy", "scy", "lcy", "encryption", "twofish", "dcpcrypt", "compiled", "tas"]),


("format-dfm", "DFM / DCY — Delphi Form Layout", "Reference",
"""
`.DFM` files are **standard Borland Delphi form-resource files** in
their textual representation — the output of the Delphi IDE's
"Save As → Text DFM" option. Plaintext, ASCII. `.DCY` is the same
content encrypted with the same Twofish-CFB scheme as `.RWN`
(see [[format-rwn]]).

The runtime picks which to load based on a source-level directive:
`#FORMSENCRYPTED` → load `.DCY`; otherwise → `.DFM`.

## Structure

```dfm
object EditForm1: TEditForm1
  Left = 460
  Top = 224
  Hint = 'C:\\TASPRO7\\DBA7\\T7ARAE.DFM'
  BorderStyle = bsSingle
  Caption = 'New Screen'
  ClientHeight = 471
  ClientWidth = 666
  Color = clBtnFace
  Font.Name = 'Arial'
  FormStyle = fsStayOnTop
  Icon.Data = {
    0000010001002020000001000800A80800001600000028000000200000004000
    ...
  }
  object Panel1: TPanel
    ...
  end
end
```

- Top-level: `object <Instance>: <Class>` … `end`.
- Properties are `Name = Value` pairs.
- Nested `object … end` blocks are child controls.
- Strings: single-quoted (`'Arial'`).
- Sets: `[bold, italic]`.
- Enumerations: bare identifiers (`clBtnFace`, `DEFAULT_CHARSET`).
- Binary blobs (icons, bitmaps) hex-encoded in `{ … }` braces,
  wrapped across lines.

The `Hint =` property often retains the **original developer path**
(e.g. `C:\\TASPRO7\\DBA7\\T7ARAE.DFM` in `T7ARA.DFM:4`) — a useful
breadcrumb for matching a deployed form back to its source layout.

## Component library

From the runtime's string table and observed samples:

- **Standard VCL:** `TForm`, `TLabel`, `TEdit`, `TButton`, `TPanel`,
  `TGroupBox`, `TDBGrid`, `TComboBox`, `TCheckBox`, `TMemo`.
- **TAS-specific:** `TEditForm1` (base form), `TTASEdit`,
  `TASDataGrid`, `TASNavigator`. Bound from SRC via `DATA_GRID …`,
  `NAVIGATOR …`, `SET_OBJ_PROP …`.
- **Third-party:** Nevrona ReportBuilder designer components appear
  inside `.RTM` not `.DFM`.

The presence of `qtintf70.dll` (Qt 3 / Borland CLX) on the install
dates the form library to the **Delphi 6–7** era (2001-2002).

## Pairing rules

| Program file | Form file |
| --- | --- |
| `FOO.SRC` + no `#FORMSENCRYPTED` | `FOO.DFM` (plaintext) |
| `FOO.SRC` + `#FORMSENCRYPTED` | `FOO.DCY` (encrypted) |
| `FOO.RWN` (compiled from above) | same `.DFM` or `.DCY` |

Name match is **case-insensitive and extension-driven**. Example:
`T7ARA.RWN` loads `T7ARA.DFM` (or `T7ARA.DCY` if encrypted).

## What you can learn from a plaintext DFM

Without executing anything, a DFM gives you:

- Every input field's name, position, size, validation mask.
- Every button's caption + OnClick handler name (which is a SRC
  function entry-point).
- Every data-grid's column layout and bound pipeline.
- The form's tab order (`TabOrder` property).
- Embedded icons / glyphs — decodable as Windows `.ico` / `.bmp`
  payloads from the `{ … }` hex blobs.

## Why it matters

- **All UI is readable** without reverse-engineering the binary.
- A Python parser walking `object … end` emits a full field
  inventory — `samples/dfm_parsed/dfm_summary.csv` already has 1,109
  forms parsed.
- Breakage during an update is detectable: compare old vs new DFM
  with a tree-diff on the object graph.

## Spec reference

Embarcadero's "About the Form File Format" documents the text-DFM
serialization. It is the Pascal `TComponent.WriteComponent` output
and is stable across Delphi 2 – XE. No EVO-specific extensions
observed — the file parses in any Delphi IDE.

## Related

- [[format-rwn]] — encryption applied when DFM becomes DCY
- [[format-src]] — the SRC code that binds and drives the form
- [[format-rtm]] — ReportBuilder templates use a binary Delphi
  stream (`TPF0`) that is the same underlying mechanism
- [[dcy-rwn-decryption]]
- [[file-formats]]
""",
["dfm", "dcy", "form", "delphi", "ui", "layout", "vcl"]),


("format-rtm", "RTM / btm — Nevrona ReportBuilder Template", "Reference",
"""
`.RTM` files are **Nevrona ReportBuilder** report templates. Every
printed or exported report in EVO renders from one. `.btm` is a
backup/snapshot at the same format. Authored in
`C:\\ISTS\\RBDsgnr.exe` (the stand-alone ReportBuilder designer).

## Binary structure

RTMs are **Delphi binary-form streams** — the `TStream.WriteComponent`
output that Delphi uses internally for compiled `.dfm` resources.

First 4 bytes — the magic:
```
54 50 46 30    "TPF0"
```

After the magic, the body is a Delphi binary component tree with the
standard encoding:

- Length-prefixed ASCII class names and property names.
- Typed property values (`vaString`, `vaInt32`, `vaSet`, `vaCollection`, …).
- Nested components for child controls.

A naïve hex dump shows those class/property name strings as readable
text, which is why raw RTM dumps look "text-y" in places.

## Component tree

Top-level is `TppReport`. Observed component classes in
`samples/btm/I2SCHK1.btm` (an A/P check layout):

```
TppReport, TppDataPipeline, TppDetailBand, TppSubReport,
TppChildReport, TppShape, TppLabel, TppDBText, TppDBMemo
```

Observed properties:

| Property | Meaning |
| --- | --- |
| `Template.FileName` | Sibling RTM referenced (e.g. `C:\\SOURCE\\apr99\\Bkapha1.rtm`) |
| `DataPipelineName` | A `TASFile` pipeline bound at runtime |
| `PrinterSetup.*` | Paper size, margins, printer name |
| `DeviceType` | `Screen` / `Printer` / `TextFile` |
| `OutlineSettings.*` | PDF outlines / bookmarks |
| `TextSearchSettings.*` | Preview search |

## How TAS programs invoke it

From the `tp7runtime.exe` keyword table:

- `RTM_FN <filename>` — specify the RTM to use.
- `REPORTNAME <string>` — display name in preview window.
- `USE_PRINTER <name>` — override the target printer.
- `PRINT_TO_FILE <path>` — spool to file instead of a printer.
- `NOPRINTWHRDIALOG` — skip the "Where do you want to print?" prompt.
- `PRINT_CANCEL` — abort current print.
- `PRINT_ARCHIVE` — archive a preview-copy.
- `EXEC_RB` — "execute ReportBuilder" — hand control to RB.

Buffer setup happens via `OUTPUT_REPORT_DATA`, `UPDATE_REPORT_DATA`,
`SETUP_REPORT_BUFF`. The source program fills a record buffer, the
pipeline pushes it into the RTM's `TppDBText` / `TppDBMemo` fields,
and RB iterates until the buffer is empty.

## The `TASFile` pipeline

When an RTM says `DataPipelineName = TASFile`, it refers to a
TAS-specific pipeline built into `tp7runtime.exe`. Field names in the
template use TAS DDF names — example from `I2SCHK1.btm`:
`BKAP_CHK_INVNUM`, `BKAP.CHK.AMTPD`, `BKAP_CHK_INVDTE`. (Dots and
underscores are interchangeable — the runtime normalizes.)

At run time, TAS fills that pipeline with one record per row; RB
renders each record through the component tree.

## Designer

- `C:\\ISTS\\RBDsgnr.exe` (~6.2 MB) — Nevrona ReportBuilder's
  stand-alone designer. Opens, edits, and saves `.RTM` files.
- Settings persist in `C:\\ISTS\\RBuilder.ini`.
- Opening a sample RTM is a safe read — it does not touch the
  network share unless you Save.

## Caller → template map

`samples/rtm_callers.csv` holds the RTM→caller cross-reference built
by grepping every `.RUN` / `.RWN` string dump for `.rtm` filenames.
Use it to answer "which program prints template X?" or "which
template does program Y use?". The data also powers the "Called by"
block on each per-RTM help page.

## Related

- [[format-src]] — SRC keywords that drive reporting
- [[format-dfm]] — shares the Delphi stream mechanism
- [[reporting-pipeline]] — end-to-end from data to PDF
- [[Nevrona ReportBuilder|ReportBuilder]]
- [[file-formats]]
""",
["rtm", "btm", "reportbuilder", "report", "nevrona", "tpf0", "template", "print"]),


# =====================================================================
# Subsystem pages
# =====================================================================

("subsystem-evoupdate", "Evo Update — Data Dictionary Patch Mechanism", "Architecture",
"""
**Evo Update** is the subsystem that patches the production Pervasive
**data dictionary** — the set of DDF files (`FILEDICT.B`, `FILEKEY.B`,
`FILELOC.B`, `FILEKNUM.B`, `FILEDES.B`, `FILEDEF.B`, `FIELDDEF.B`,
`INDEXDEF.B`) that define every EVO table and field.

Shipped updates arrive as `.UPD` files in the same format as the
production DDFs. The update program reads the `.UPD` files, compares
them to the live dictionary, and restructures any table whose schema
changed.

## The `.UPD` file format

`.UPD` files are **Btrieve data files** — identical structure to the
live DDFs they patch. First 4 bytes of every sampled `.UPD` file
(`FILEDEF.UPD`, `FILEDICT.UPD`, `FILES.UPD`):

```
46 43 00 00    "FC\\0\\0"
```

That is the Pervasive/Btrieve 6.x+ File Control Record signature.
In other words: an `.UPD` is just a Btrieve table, opened by the
update program and iterated record-by-record.

Distributed `.UPD` companions:

| File | Role |
| --- | --- |
| `FILELOC.UPD` | File-location records (where each data file lives per company) |
| `FILEDICT.UPD` | Main dictionary — one row per table |
| `FILEKEY.UPD` | Key definitions |
| `FILEKNUM.UPD` | Key-number assignments |
| `FILEDES.UPD` | File descriptions |
| `FILEDEF.UPD` | File-definition records |
| `FIELDDEF.UPD` | Field definitions |
| `INDEXDEF.UPD` | Index definitions |
| `FILES.UPD` | Master list of files touched by the update |

Error messages in the update program reference these by name
verbatim; e.g. `EvoUPDTE.RUN`:
`"Error: Cannot locate the FILELOC.UPD file. UPDATE cannot run
without this file."`

## The program family

Historically layered — each generation kept the prior's name and
added a new one:

| Program | Era / role |
| --- | --- |
| `DBAUPDTE.RUN` | DOS-era DBA update (still present; emits a "this version is Windows-only" warning) |
| `DBAUPDT1.RUN`, `DBAUPDT2.RUN` | Two-phase companions of DBAUPDTE |
| `UPDFILE.RUN` | Core file-update helper (touches BKSYMSTR, enforces main-company restriction) |
| `ISUPDATE.RUN` | ISTech 2005 enhancement — "IS-UPDATE Update Data Dictionaries" |
| `EvoUPDTE.RUN` | Modern Evo-branded variant |
| `EvoUPDSetup.RWN` | Setup phase |
| `EVOUPDATE.RWN` | Main TP7 update program |
| `EvoERPupd.RWN` | ERP-wide orchestration |
| `EvoPRupd.RWN` | Payroll-module update |
| `evoForceUpd.RWN` | Force-update variant (bypasses some checks) |
| `t7jUPD.RWN` | Journal-update (T7 era) |
| `SCHUPD.RUN` | Scheduled update |

## What an update actually does

From `EvoUPDTE.RUN` plaintext strings:

1. **Prerequisites.** "Please make sure that no other users are
   currently logged into DBA." Update locks out everybody. Runs only
   from the main (default) company; `UPDFILE.RUN`:
   `"This can only be run from the main (default) company."`
2. **Backup demand.** `"This routine if not completely successful can
   delete the data file being restructured. It could also leave some
   files complete and others not. To protect against this YOU MUST
   MAKE A COMPLETE SYSTEM BACKUP BEFORE CONTINUING."`
3. **Scan.** Reads every `.UPD` file; builds a work list of File
   Descriptors (FDs) to process.
4. **For each FD, four phases:**
   - `Update Offsets`
   - `Delete Old FD`
   - `Save New FD`
   - `Restructure` — rewrite the Btrieve `.B` file under the new
     schema.
5. **Log.** Progress lines like `"Working on FD: <name>"` and any
   errors go to the screen; completion updates the `BKUPDATE` table.

## Related tables

- `BKUPDATE` — update history / tracking
- `BKSYMSTR` — system master (checks for other logged-in users)
- All DDF tables above (as both source and target)

## Safety properties

- Write-side scope: only the live DDF tables and the data files
  being restructured. No code files (`.RWN`/`.DCY`) touched — that's
  a separate distribution step (file-copy, not this subsystem).
- Not idempotent: a half-completed run can leave the dictionary
  inconsistent. Error messages explicitly warn the operator that a
  restored backup may be the only recovery path.
- Single-user: enforces no-other-logins and main-company-only at
  start.

## Related

- [[architecture-overview]]
- [[data-dictionary-overview]]
- [[recipe-update-evo]]
- [[recipe-backup]]
""",
["update", "upd", "ddf", "data dictionary", "patch", "evoupdate", "restructure", "filedict", "filedef"]),


# =====================================================================
# Placeholder stubs for many more pages — auto-generated module pages,
# recipes, tables, etc. come from the build script.
# =====================================================================
]
