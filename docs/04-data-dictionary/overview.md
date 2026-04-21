# EvoERP Data Dictionary — Overview

Status: draft. Counts are authoritative (from the deployed DDF files
as of 2026-04-17). Per-table field lists are still pending.

## The big picture

EvoERP's data layer is **Pervasive PSQL (Btrieve)**, using the standard
Pervasive data-dictionary file set. Each "company" in EVO is a separate
directory under `\\I2S109-SOLIDCRM\DBAMFG$\` whose file extension
encodes the company code — for example, company `22`:

- `\\I2S109-SOLIDCRM\DBAMFG$\22\BKARCUST.B22` — AR customer master.
- `\\I2S109-SOLIDCRM\DBAMFG$\Default\BKARCUST.B`  — same table,
  `Default` company.

Observed company folders:
`22`, `AB`, `AT`, `CA`, `Goldstar`, `I2`, `IT`, `UU`, `Default`,
plus `DefaultSQL`, `Testdata`, `DEV`, `Recovered`, `Bak Up`, `Menu Backup`.

## Data dictionary files (Pervasive standard)

Located in every company directory. The `Default` set is the
authoritative schema template. Copies in `../../samples/ddf/`:

| File          | Role |
| ------------- | ---- |
| `FILE.DDF`    | **Catalog** — one row per data table. Columns: table name, filename. |
| `FIELD.DDF`   | **Schema** — one row per field of every table. Columns include field name, position, type, length, dec, flags. |
| `INDEX.DDF`   | Index definitions per table. |
| `ATTRIB.DDF`  | Field attributes (picture format, allowed chars, etc.). |
| `OCCURS.DDF`  | Array-field occurrence counts (TAS `array N`). |
| `RELATE.DDF`  | Declared inter-table relationships (referential integrity). |
| `TRIGGER.DDF` | Trigger definitions. |
| `VIEW.DDF`    | Defined SQL views. |
| `PROC.DDF`    | Stored procedures. |
| `VARIANT.DDF` | (Pervasive internal — variant types.) |

All are in Btrieve format. They are **readable via Pervasive ODBC**
(Pervasive/Actian is already installed on this workstation — it's in
the system PATH). That opens a read-only SQL path into the entire EVO
data model — excellent for documentation, but note the strict rule in
[CLAUDE.md](../../CLAUDE.md): no writes of any kind against
`\\i2s109-solidcrm`. ODBC `SELECT` only.

## Table inventory — 649 tables grouped by prefix

Full raw list: `../../samples/ddf/tables.txt`
Grouped: `../../samples/ddf/tables_by_prefix.txt`

Key families (from the `BK*` generation — legacy backbone):

| Prefix | Count | Meaning (hypothesis) |
| ------ | ----- | -------------------- |
| `BKAB` | 2     | Address Book (customer + vendor light records) |
| `BKAC` | 1     | Accounting misc (report) |
| `BKAP` | 24    | **Accounts Payable** — APO orders, CHKF/CHKH checks, INVT invoices, VEND vendors, QUOT/RFQ quotes, EIVT/EVND EDI/eInvoice, NOTE |
| `BKAR` | 27    | **Accounts Receivable** — CUST customers, INVI/INVL/INVT/INVV invoices + lines + taxes, CHKF/CHKH checks, DPST deposits, RDSC/HDSC descriptions, DEP dept, HINV history |
| `BKBM` | 10    | **Bill of Materials** — AMTR/AVAL/EMTR/DIM/CNFG |
| `BKCM` | 46    | **Company Master / multi-company setup** (largest family) — accounts, currencies, config |
| `BKCP` | 2     | Company Preferences / EC |
| `BKDC` | 7     | **Data Collection** (shop-floor barcode) — LAB labels |
| `BKED` | 6     | **EDI** — headers, lines, vendor maps, notes |
| `BKES` | 3     | **Estimating / Quoting** |
| `BKFL` | 1     | Field Help (UI) |
| `BKFO` | 1     | Form Config |
| `BKGL` | 28    | **General Ledger** — ACHK/AGJL/AGJR accounts-and-journals, CCOA chart-of-accounts, ATRN transactions |
| `BKIC` | 16    | **Inventory Core** — AMTR/EMTR masters, APMA alt-parts, DIM dimensions, ALTD/ALTP alternate parts |
| `BKIS` | 2     | Tax (HTAX/TAX) |
| `BKLO` | 1     | Logon |
| `BKMA` | 2     | Materials (cost / trim) |
| `BKMR` | 3     | **MRP** — Forecast, PO-suggestions, workflow |
| `BKPC` | 2     | Piece-count / Kits |
| `BKPI` | 7     | **Physical Inventory** — FROZ/LCNT/LOT/MSTR/PHYS |
| `BKPO` | 2     | Purchase Order X/XH |
| `BKPR` | 16    | **Payroll / Commissions** — ACOM, AGNT, BOOK, COMM, CURP |
| `BKPS` | 1     | User Security (USER) |
| `BKQC` | 2     | Quality Control — MSTR/TRAN |
| `BKQT` | 2     | Quote temp |
| `BKRF` | 2     | **RFQ** — Request-for-Quote |
| `BKRT` | 4     | Routing (CST/EMTR/SPEC/TEMP) |
| `BKSA` | 1     | Sales Report |
| `BKSB` | 3     | **Subcontract** — MFG/PART/VEND |
| `BKSH` | 1     | Shortages |
| `BKSL` | 2     | Sales levels |
| `BKSO` | 7     | **Sales Order** — HLOT/HSER history lots/serials, LOCK, NOTE, PO |
| `BKSY` | 8     | **System** — AP/AR configs, CFG, HELP, LOG, MSTR (the one we saw opened in SRC) |
| `BKUM` | 1     | Unit of measure |
| `BKUP` | 1     | Updates |
| `BKWO` | 1     | Work Order PO |
| `BKYS` | 1     | **System #2** — the second system master opened in `Bkaph.src`:51 |

And the `MT*` "master" second generation:

| Prefix | Count | Meaning |
| ------ | ----- | ------- |
| `MTEX` | 1  | Exchange rate history |
| `MTIC` | 3  | Inventory — AMTR/EMTR/MSTR |
| `MTIN` | 1  | Inventory default |
| `MTMR` | 1  | MRP master |

And the `WO*` work-order cluster (30 tables):
`WOBOM`/`WOBOMCHG`/`WOBOMHRM`/`WOBOMREM`, `WOHLABOR`/`WOHMAT`/
`WOHRECV`/`WOHROUT`, `WOLABOR`/`WOLABRPT`/`WOMAT`, `WORECV`,
`WORKACHG`/`WORKCHG`/`WORKCTR`/`WORKHORD`/`WORKORD`/`WORKSORD`,
`WOROCHG`/`WOROUT`/`WOROUTMP`, `WOSROUT`, `WODATE`, plus more
— full list in `tables_by_prefix.txt`.

The 365 "other" tables are a mix of customer-specific, customizations,
and non-prefixed utility tables (e.g. `CALENDAR`, `CALTEMP`,
`CCEDIXRF`). Each will get its own classification as we read modules.

## How to query the schema (read-only recipe)

Because Pervasive ODBC is installed locally (PATH shows
`C:\Program Files\Actian\PSQL\bin`), the most efficient way to build
per-table field listings is:

```sql
-- from a read-only ODBC / PCC session against the Default database
SELECT Xf$Name AS TableName, Xe$File AS FileName, Xe$Size AS RecLen
FROM   X$File;

SELECT  f.Xf$Name, fld.Xe$Name, fld.Xe$DataType,
        fld.Xe$Offset, fld.Xe$Size, fld.Xe$Dec
FROM    X$File f
JOIN    X$Field fld ON fld.Xe$File = f.Xf$Id
ORDER   BY f.Xf$Name, fld.Xe$Offset;
```

This is a **read-only SELECT** — permitted by the scope rules. But I
should **ask the user before running it** anyway, because attaching to
the production database is a stateful action.

## Full schema extracted

The complete per-field schema for all 659 tables is now in
`../../samples/ddf/schema.md` (Markdown, ~27k lines) and
`../../samples/ddf/schema.json` (machine-readable).

Extraction pipeline: `scripts/parse_ddf.py` reads the standard Pervasive
FILE.DDF and FIELD.DDF record layouts directly — FILE.DDF record is
98 bytes (Xf$Id, Xf$Name[20], Xf$Loc[64], Xf$Flags, reserved);
FIELD.DDF record is 32 bytes (Xe$Id, Xe$File, Xe$Name[20],
Xe$DataType, Xe$Offset, Xe$Size, Xe$Dec, Xe$Flags).
`scripts/build_schema.py` joins them.

Total: **659 tables**, **24,113 fields**. Mean 36.6 fields/table.
Largest: `BKPRGLFL` (Payroll GL Field Layout) at 664 fields,
`BKSLEVEL` (422), `BKAPINVL`/`BKAPRIVL` (AP invoice lines, 390 each),
`BKPRMSTR`/`BKPRW2` (payroll master + W2 output, 384 each).

### Field naming convention (confirmed by extraction)

Fields are prefixed with a 4-letter table abbreviation + underscore:

| Table prefix → field prefix | Example |
| --------------------------- | ------- |
| `BKAR*`  → `BKAR_*`         | `BKAR_CUSTCODE`, `BKAR_CUSTNAME` in `BKARCUST` |
| `BKAP*`  → `BKAP_*`         | `BKAP_VENDCODE`, `BKAP_VENDNAME` in `BKAPVEND` |
| `BKIC*`  → `BKIC_PROD_*`    | `BKIC_PROD_CODE` in `BKICMSTR` |
| `BKSY*`  → `BKSY_*`         | `BKSY_COMP_NAME` in `BKSYMSTR` |
| `AHSYLOG` → `AHSY_USER_*`   | `AHSY_USER_LEVL`, `AHSY_USER_ACCES_N` |
| `ARTTEMP`→ `BKART_*`        | AR transactions |

Fields in TAS-Pro source code are referenced with **dots** instead of
underscores (e.g. `BKAP.VENDCODE` in `.SRC`) — the compiler converts
both spellings.

### Type codes observed

Actual type distribution across 24k fields:

| Code | Meaning | Size in record |
| ---- | ------- | -------------- |
| `STRING` (0)   | Fixed-length alpha, trailing-space padded |
| `INTEGER` (1)  | 2 or 4-byte signed integer |
| `FLOAT` (2)    | 8-byte IEEE double (common for money+quantities) |
| `DATE` (3)     | 4-byte Pervasive date |
| `TIME` (4)     | 4-byte time |
| `DECIMAL` (5), `MONEY` (6) | BCD decimal |
| `LOGICAL` (7)  | 1-byte yes/no |
| `NUMERIC` (8)  | ASCII numeric (often used for ID fields) |
| `UBINARY` (14) | Unsigned binary (e.g. for counters) |

## Security table — `AHSYLOG`

One of the most important tables: stores per-user access rights.
Fields: `AHSY_USER_LEVL` (2 bytes, user level code), `AHSY_USER_MENU`
(4 bytes, starting menu for this user), `AHSY_USER_CTRL` (1 byte),
`AHSY_USER_ACCES_1` through `AHSY_USER_ACCES_20` (1 byte each = 20
module access flags).

This implies the security model is a **20-cell permission grid** per
user — probably one flag per module area (AR, AP, IN, SO, PO, WO, GL,
MRP, …). Field AHSY_USER_MENU picks the starting menu tree, so
user-specific menus are driven by DB content.

## ISJAVA table (integration point)

Strings extracted from `EvoPVT.jar` show the Java helper writes into a
table called `ISJAVA` with columns `IS_JAVA_UID`, `IS_JAVA_DATE`,
`IS_JAVA_PARAM_*`. This is an **in-process job queue** — the Java
utility drops parameters in the DB and EVO TAS programs pick them up.

## Things still to verify

- Exact meaning of every `BK<prefix>` and `WO<suffix>` — now possible
  by reading fields in `schema.md`.
- Whether the `MT*` "master" tables are read by every company or are
  also per-company-suffixed.
- Whether the "Default" folder is the per-seed schema template or an
  active company.
- Where the `BKARHINV` subfolder fits (it holds a single `BKARHINV.BI2`
  — probably an overflow/history partition for company I2).
- Parse `INDEX.DDF` for primary-key / secondary-index information.
- Parse `RELATE.DDF` for foreign-key relationships.
