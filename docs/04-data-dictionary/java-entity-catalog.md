# EvoPVT.jar SQL Entity Catalog

**Status: verified** | Pass 423 (2026-06-30)

---

## Overview

EvoPVT.jar (the EvoERP Java bridge library) contains a complete set of SQL table entity classes
in the package `com.evoerp.sql.tables`. These classes represent every table accessible from the
Java layer via Pervasive JDBC (port 1583).

| Metric | Value |
|--------|-------|
| Total entity classes | 533 |
| Total fields cataloged | 18,858 |
| Source | `samples/jar/extracted/com/evoerp/sql/tables/*.class` |
| Extraction method | `javap -p` bytecode decompilation |
| Full catalog | `samples/jar/java_table_schemas.json` |

Field types in Java layer:

| Type | Count | Notes |
|------|-------|-------|
| STRING | 10,254 | Maps to Pervasive CHAR/VARCHAR |
| DECIMAL | 6,407 | Maps to Pervasive DECIMAL/NUMERIC |
| DATE | 1,084 | Maps to Pervasive DATE |
| INTEGER | 989 | Maps to Pervasive INTEGER |
| TIME | 124 | Maps to Pervasive TIME (LocalTimeField) |

---

## Table Family Groups

### BK\* — Core Production Tables (single-company)

| Family | Tables | Key Tables |
|--------|--------|------------|
| BKAP | 23 | BKAPVEND (72f), BKAPO (66f), BKAPINVL (390f) |
| BKAR | 27 | BKARCUST (106f), BKARINV (81f), BKARINVL (390f ≡ BKAPINVL alias) |
| BKBM | 10 | BKBMMSTR (26f), BKBMCOMP, BKBMPREV |
| BKCM | 46 | See Contact Manager section below |
| BKDC | 7 | BKDCSHFT, BKDCCFG, BKDCLAB1-5 (Btrieve-only) |
| BKED | 6 | BKEDIH (81f), BKEDIL, BKEDIDN (idle at i2) |
| BKES | 3 | BKESTQT (81f, 6894 rows), BKESTQTL (462,727 rows), BKESTCFG |
| BKGL | 24 | BKGLCOA (65f), BKGLTRAN, BKGLSTMT (104f) |
| BKIC | 16 | BKICMSTR (64f), BKICLOC (32f), BKICPMAT (85f) |
| BKPI | 7 | BKPIMSTR, PIBINLOC (14f, 22279 rows), PIBINLOT (14f, 40 rows) |
| BKPO | 2 | BKPOX (purchase order) |
| BKPR | 16 | Payroll tables |
| BKQC | 2 | BKQCMSTR (53,300 rows) |
| BKSO | 7 | Sales order tables |
| BKSY | 8 | BKSYMSTR (286f), BKSYCFG (4f), BKSLEVEL (422f) |
| BKWO | 1 | BKWOMSTR |

### IS\* — ISTS Enhancement Layer

| Family | Tables | Notes |
|--------|--------|-------|
| ISAP | 11 | AP enhancement tables |
| ISAR | 22 | AR enhancement tables |
| ISES | 7 | Estimating (ISESTAQT=5,816, ISESTAQL=130,792 archived IS-era quotes) |
| ISSO | 9 | SO enhancement |
| ISSR | 10 | SR (Service/RMA) tables |
| ISWO | 6 | WO enhancement |
| ISGL | 6 | GL enhancement |
| ISPR | 5 | PR enhancement |
| ISPO | 5 | PO enhancement |
| ISFO | 5 | FO (features/options) enhancement |
| ISQC | 3 | QC enhancement |
| ISIC | 4 | IC (inventory cycle) enhancement |

### MT\* — Multi-Company Catalog Tables

| Table | Fields | Notes |
|-------|--------|-------|
| MTICMSTR | varies | Multi-company item master (50,990 rows) |
| MTMRP | 13 | MRP work table (37,137 rows) |
| MTEXCHG | 7 | Multi-currency exchange rates |

### WO\* and WORK\* — Work Order Sub-Tables

The WO family has three variants: active (WO*), historical (WOH*), and estimated (WOE*):

| Base Name | Active | Historical | Estimated | Fields |
|-----------|--------|------------|-----------|--------|
| Labor | WOLABOR | WOHLABOR | WOELABOR | 45 |
| Material | WOMAT | WOHMAT | WOEMAT | 17 |
| Routing | WOROUT | WOHROUT | WOERECV | 81 |
| BOM | WOBOM | WOHBOM | — | 24 |
| Date | WODATE | WOHDATE | — | 5 |
| Exchange | WOEXCHG | WOHEXCHG | WOEXCHG | 10 |

Singleton tables:
- `WORKORD` (73f) — active work orders
- `WORKHORD` (73f) — historical work orders archive
- `WORKSORD` (73f) — scheduled work orders
- `WORKCHG` (25f) — work order changes/revisions
- `WORKCTR` (24f) — work center master (MTWC.* namespace)

### MK\* — Marketing / Activity Tracking Module

Newly documented from Java entity catalog. 11 tables:

| Table | Fields | Purpose |
|-------|--------|---------|
| MKDEF | 11 | Module config: ECNEXTID/ENEXTID/FNEXTID/TNEXTID/TRACK/CALENDAR |
| MKEVENT | 12 | Event/activity type: class, description, form template, media, reminders |
| MKECLASS | 3 | Event classification codes |
| MKICLASS | 3 | Inbound activity classes |
| MKTRACK | 4 | Campaign/track definitions: NUM/CLASS/DESC/ACTIVE |
| MKTCLASS | 3 | Track classification codes |
| MKTROUT | 11 | Track routing: SEQ/EVENT/DAYSNXT/NEXTSEQ/JUMP/FIXED/PRICECD/SALEBEG/SALECLO/SALELEN |
| MKFORM | 6 | Form templates: NUM/DESC/FILE/ATT/ACTIVE |
| MKASSIGN | 6 | Activity assignments: ACCT/NXTDAT/NXTSEQ/PRCODE + others |
| MKTNOTE | 3 | Track notes: TRACK/LINE/TEXT |
| MKAHIST | 9 | Activity history: ACCT/DATE/EVENT/FORM + others |

MK module is used by the GL bank reconciliation (T7GLJ opens MKTRACK) and as an audit log
(MKAHIST is opened by virtually every module as an activity/audit trail — 158 total programs).
The core MK marketing workflow is likely licensed and used through T7CMx or T7MKx programs
not yet enumerated (network share access blocked).

---

## Contact Manager (BKCM\*) — 46 Tables

Confirmed three-entity architecture (Pass 53/347):

| Entity | Table | Fields | Notes |
|--------|-------|--------|-------|
| Customer account | BKCMCUST | 106 | Links to BKARCUST |
| Prospect account | BKCMACCT | 41 | CODE+NAME+ADDR+REP+SICCD+CUST+LEAD+TERR+CCARD+EMAIL+EMPS |
| Account notes | BKCMACCN | 154 | 10× CONT/TITLE/PHONE/DEAR/EMAIL + UDF dates/alpha |
| Activity history | BKCMACTH | 21 | Start/stop/MIN/BMIN/RATE/AMT/BALNC billing |
| Follow-up | BKCMACTF | 11 | Follow-up + SO link |
| Event codes | BKCMHCOD | 9 | Event codes + rate + BPART billing parts |
| Sales rep access | BKCMREP | 14 | VIEW/CHANGE/GWARN/AADD flags |
| Territory | BKCMTERR | 2 | Territory code + description |
| Campaign/mailing | BKCMMHST | 72 | 20-class include + 20-class exclude + 9 range filters |
| Dunning | BKCMDUN | 36 | 10-level dunning ladder |
| Dunning history | BKCMDUNH | 6 | — |
| Account EFT | BKCMEFTM | 7 | Electronic funds transfer setup |
| EFT history | BKCMFTME | 7 | — |
| Form templates | BKCMFORM | 8 | Document form templates |
| Temp tables | BKCMTMP1-4 | 6 each | Calculation temporaries |

Most BKCM* tables are NOT registered in the Pervasive PSQL DDF (Btrieve-only access).
This is why `SELECT * FROM BKCMCUST` fails in ODBC — these tables bypass the relational layer.

---

## Estimating Summary Table (ESTSUM)

`ESTSUM.class` (213 fields, MTESUM_ prefix) — the multi-company estimating quote summary table:

Key field groups:
- Header: `MTESUM_QUOTE`, `MTESUM_CLASS`, `MTESUM_CODE`, `MTESUM_DESC`, `MTESUM_UM`, `MTESUM_REV`
- Dates: `MTESUM_DATE`, `MTESUM_CDATE`, `MTESUM_EXPDATE`, `MTESUM_FIN_DATE`
- Status: `MTESUM_STATUS` (A=Active, C=Converted, I=Inactive, X=Cancelled, D=Archived)
- Sales: `MTESUM_CUSTCODE`, `MTESUM_NAME`, `MTESUM_ATTN`, `MTESUM_SLSP_NUM_1/2`
- Cost arrays (10 qty-breaks × 10 cost types): MAT, MATMU, SETUP, LAB, LABMU, OP, OPMU, OH, OHMU, OVALL, MISC, TOTAL, PRICE, VOVHD — 10 fields each = 140 cost fields
- Notes: `MTESUM_NOTES_1..10`
- Extra: `MTESUM_EXTRA_1..10`

The MTESUM_ prefix confirms this is a multi-class (MT*) estimating table analogous to MTICMSTR for inventory. Relation to `BKESTQT` (the single-company active quote table, 6,894 rows) needs confirmation.

---

## Standalone Tables of Note

| Table | Fields | Purpose |
|-------|--------|---------|
| ROUTING / ROUTAING / ROUTTEMP | 62 | Work center routing definitions |
| MACHINE | 16 | Machine master |
| TOOL | 14 | Tool master |
| DISCOUNT | 85 | Pricing matrix (BKIC_PMAT_ fields — alias of BKICPMAT) |
| SERIAL / SERIALH | 30 | Serial number tracking / history |
| LOT | 22 | Lot tracking master |
| MENUFILE | 108 | TAS Pro menu definitions (MENU_CODE + 20× MENU_LINES + other nav fields) |
| NZITPRE | 54 | NZ item number prefix table (16 descriptions + 10 next-number counters) |
| BUCKETS | 14 | AR aging buckets |
| ARTTEMP | 12 | AR transaction temporary |
| CALENDAR / CALTEMP | 5/2 | Business calendar |
| CCEDIXRF | 6 | CandoEDI cross-reference |
| SCHEDCAL / SCHWO | 6/10 | Scheduling calendar / scheduled work order list |
| LANGDICT | 5 | Language/localization dictionary |
| TESTFILE | 11 | Test file (development artifact) |

---

## Pervasive System Catalog Tables (X$)

EvoPVT.jar includes entity classes for Pervasive's internal DDF catalog tables,
enabling the Java layer to query the schema directly via JDBC:

| Table | Purpose |
|-------|---------|
| X$ATTRIB | Table attributes |
| X$FIELD | Field definitions |
| X$FILE | Table/file definitions |
| X$INDEX | Index definitions |
| X$OCCURS | Repeating group definitions |
| X$PROC | Stored procedures |
| X$RELATE | Relationships/foreign keys |
| X$TRIGGER | Trigger definitions |
| X$VARIANT | Variant field definitions |
| X$VIEW | View definitions |

These are the same tables exposed by Pervasive's `SELECT * FROM X$FILE` catalog queries,
confirming that EvoPVT.jar can introspect the database schema at runtime.

---

## Usage Notes

- Full JSON catalog: `samples/jar/java_table_schemas.json` — 533 entries, field names + types
- Java field types (STRING/DECIMAL/DATE/INTEGER/TIME) are the Java layer's view; Pervasive stores
  all fields as `CHAR` segments internally; Java types reflect the application-layer interpretation
- Tables NOT in Pervasive DDF (Btrieve-only) still have entity classes here (e.g. most BKCM* tables)
  — the Java layer accesses them via Btrieve API directly through jBtrieve, not through the DDF

**Confidence: 92/100** — Field names and types confirmed from javap bytecode decompilation of all
533 `.class` files in EvoPVT.jar; semantic interpretation of some table purposes inferred from
field name patterns and cross-reference with existing module documentation.
