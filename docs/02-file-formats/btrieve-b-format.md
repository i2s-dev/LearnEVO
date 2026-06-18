# Btrieve / Pervasive PSQL `.B` File Format

Status: partial — binary page structure identified from sample; DDF fully cataloged;
type mapping confirmed from fields.csv.

---

## What Btrieve is

Pervasive PSQL (formerly Btrieve / Micro Kernel Database Engine, MKDE) is the embedded
database engine that stores all EvoERP operational data. EvoERP uses Pervasive SQL 2000i
(v8.x era). All business tables are stored as `.B` files (plus optional `.mdx` companion).
The schema is defined in four `.DDF` catalog files (`file.ddf`, `field.ddf`, `index.ddf`
plus five auxiliary: `attrib.ddf`, `occurs.ddf`, `relate.ddf`, `view.ddf`, `trigger.ddf`).

**Total confirmed:** 659 tables, 24,113 fields, 15,998 index segments (from DDF analysis).

---

## `.B` file physical format

### Magic and page structure

Every `.B` file (and every `.DDF` file) starts with the two ASCII bytes `FC` (0x46, 0x43).
This is the Btrieve File Control Record (FCR) signature, present across all Btrieve 5.x–7.x
versions.

```
Offset 0-1:  "FC" (0x46 0x43) — Btrieve magic / version marker
```

Files are divided into fixed-size **pages**. The standard page size used throughout EvoERP
is **512 bytes**.

Confirmed from `samples/BKICMSTR.B`:
- File size: 71,680 bytes
- Page count: 71,680 / 512 = **140 pages**
- This is an inventory item master table with ~715 items at the time the sample was copied.

### Page types (standard Btrieve)

| Page type | Description |
|-----------|-------------|
| Page 0 | **File Control Record (FCR)** — file header: page size, record size, key count, owner name, file version, free page chain |
| Index pages | B-tree key index nodes — contain key values and pointers to data/child pages |
| Data pages | Fixed-length record storage — packed records, each with a usage byte prefix |
| Free pages | Recycled deleted records — chained by the FCR's free page list |

### Header byte decode (BKICMSTR.B FCR sample)

```
Offset  Hex value   Interpretation (partial — full FCR spec is proprietary)
------  ---------   -----------------------------------------------------------
00-01:  46 43       "FC" — Btrieve file magic
02-03:  00 00       File format subversion
04-05:  43 00       LE16 = 67 — possibly internal record overhead or alignment
08-09:  05 00       LE16 = 5 — likely number of key definitions
14-15:  0B 00       LE16 = 11 — possibly log position or version byte
16-17:  69 02       LE16 = 617
18-19:  CB 02       LE16 = 715 — record count (matches ~715 inventory items expected)
36-37:  01 00       Flag byte
3A-3D:  0E 00 00 08 Probably root page pointer or high-water page
4A-4D:  50 09 01 00 LE32 = 68,944 — possibly total allocated bytes (< 71,680 = consistent)
60-6B:  FF*12       End-of-chain marker for free page list (0xFFFFFFFF... = no free pages)
70-71:  73 02       LE16 = 627
72-73:  0B 00       LE16 = 11
74-75:  0B 00       LE16 = 11
76-77:  0E 00       LE16 = 14
78-79:  3C 0F       LE16 = 3900 — possibly record length (BKICMSTR has many fields)
```

Note: The full FCR layout is not publicly documented by Pervasive. The above is inferred
from known Btrieve v6 file format patterns and is partly confirmed, partly guessed.

### Companion files

| Extension | Purpose |
|-----------|---------|
| `.B` | Main Btrieve data file (records + B-tree indexes embedded) |
| `.mdx` | Multi-Index Xtra — overflow key file when >24 key segments per table. 10 files on the share. |
| `.XLB` | Extended Lock Byte file — Pervasive's concurrency manager. Paired with each `.B`. |
| `.B22`, `.BAB`, `.BI2`, etc. | Per-company variant — same schema, different physical file. Suffix = company code. |

---

## DDF system (X$ catalog tables)

The schema is stored in a set of special Btrieve files called the **Data Dictionary Files
(DDF)**. All seven DDF files are themselves Btrieve format (start with `FC` magic).

### DDF file registry

| DDF file | Logical name | Purpose |
|----------|-------------|---------|
| `file.ddf` | `X$File` | Table registry: file_id → logical name + physical `.B` filename |
| `field.ddf` | `X$Field` | Field definitions: file_id + field_id → name, type, offset, size, decimals, flags |
| `index.ddf` | `X$Index` | Index segment map: file_id + index_num + part_num → field_id |
| `attrib.ddf` | `X$Attrib` | User-defined column attributes (constraint metadata) |
| `occurs.ddf` | `X$Occurs` | Occurrence / repeating-group definitions (array fields) |
| `relate.ddf` | `X$Relate` | Foreign key / referential integrity relationships |
| `view.ddf` | `X$View` | Named SQL views over Btrieve tables |

The DDF files in `samples/ddf/`:
| File | Size | Records (approx.) |
|------|------|-------------------|
| `file.ddf` | 123,904 B | 659 tables |
| `field.ddf` | 4,914,176 B | 24,113 fields |
| `index.ddf` | 485,888 B | 15,998 index segments |
| `attrib.ddf` | 28,672 B | small (column attributes) |
| `occurs.ddf` | 28,672 B | small (array field definitions) |
| `relate.ddf` | 45,056 B | small (FK relationships) |
| `view.ddf` | 32,768 B | small (SQL views) |

### X$File → X$Field → X$Index relationship

```
X$File (file.ddf)
  ├── file_id (integer PK)  ← links to →  X$Field.file_id
  ├── logical_name           (e.g., BKICMSTR)
  └── physical_file          (e.g., BKICMSTR.B)

X$Field (field.ddf)
  ├── file_id + field_id (composite PK)
  ├── name               (e.g., BKIC.PROD.CODE)
  ├── type_code          (see type table below)
  ├── type_name          (e.g., STRING)
  ├── offset             (byte offset of field in record)
  ├── size               (field byte width)
  └── dec                (decimal precision)

X$Index (index.ddf)
  ├── file_id + index_num + part_num (composite key)
  ├── field_id           (which field this key segment is on)
  └── (key flags: ascending/descending, unique/duplicate, ignore-nulls)
```

### Btrieve DDF data types (observed in EvoERP)

Extracted from `samples/ddf/fields.csv`:

| Code | Type name | TAS 4GL analogue | Notes |
|------|-----------|-----------------|-------|
| 0 | STRING | A (alpha) | Fixed-length, space-padded |
| 1 | INTEGER | I (integer) | Signed 2-byte or 4-byte integer |
| 2 | FLOAT | N (numeric, large) | IEEE double-precision float |
| 3 | DATE | D (date) | Btrieve 4-byte date (YYYYMMDD packed) |
| 4 | TIME | T (time) | Btrieve 4-byte time (HHMMSSHH) |
| 7 | LOGICAL | L (logical) | 1-byte boolean (0/1) |
| 12 | ? | — | Possibly DECIMAL (packed BCD) or NOTE |
| 13 | ? | — | Possibly LVAR (large variable-length) |
| 14 | UBINARY | I (unsigned int) | Unsigned binary integer (1–4 bytes) |

Types 12 and 13 appear in a small number of fields — likely specialized types for memo
or packed-decimal data. Not yet confirmed from source code.

### OCCURS.DDF — repeating group / array support

`X$Occurs` (occurs.ddf) defines **occurrence groups** — Btrieve's mechanism for
array-like repeating fields within a fixed-length record. For example, BKYSMSTR has
fields `BKYS.YN[1]` through `BKYS.YN[200]` — these are stored as a single fixed block
in the record with an occurrence definition pointing to the starting offset and repeat
count. The TAS 4GL `array N` directive matches directly onto the OCCURS definition.

### RELATE.DDF — foreign key hints

`X$Relate` (relate.ddf, 45,056 bytes = 88 pages) stores referential integrity
relationship definitions (parent table + primary key → child table + foreign key).
EvoERP's TAS programs enforce referential integrity procedurally (via `find M` + `flerr()`
checks), but the DDF relationship table allows the Pervasive SQL engine to also enforce
them at the record-engine level. Whether enforcement is active in production is unknown.

---

## Company file routing

EvoERP runs 6 companies (AT, AB, CA, I2, IT, 99). Each company has its own physical
copy of every `.B` file, identified by the company code in the file extension:

| Extension | Company |
|-----------|---------|
| `.B` (plain) | Default / I2 (fallback) |
| `.BAT` | AT company |
| `.BAB` | AB company |
| `.BCA` | CA company |
| `.BI2` | I2 company (current production) |
| `.B99` | Company 99 (demo/test) |
| `.BIT` | IT company (sysadmin) |
| `.B22` | Company "22" (legacy/frozen) |

The routing is managed by `FILELOC.B` (3,613 records × 6 companies — see
[tas-data-infrastructure.md](tas-data-infrastructure.md)). TAS Pro runtime looks up
the logical table name in FILELOC to find the correct physical file for the current
company before any `open` statement executes.

---

## Multi-company DDF and schema

The DDF files (`file.ddf`, `field.ddf`, `index.ddf`) are **shared across all companies**
and define the schema once. The per-company routing is handled entirely at the FILELOC
level — the DDF always refers to the "base" `.B` filename, and the runtime substitutes
the company-specific extension at open time.

---

## Key observations for EvoERP analysis

1. **All 659 tables, 24,113 fields, and 15,998 index segments** are confirmed from the
   DDF files in `samples/ddf/`. The full schema is in `samples/ddf/schema.md`.

2. **Average record layout**: EvoERP tables average ~37 fields per table; BKICMSTR (item
   master) has one of the largest layouts at 422 fields.

3. **Btrieve integer keys** are stored in binary, not ASCII. TAS Pro converts them for
   display. String keys (e.g., PROD.CODE) are stored raw in the B-tree.

4. **No NULL semantics**: Btrieve uses fixed-length records. Empty strings are space-padded
   to field width. Zero is used for uninitialized numeric fields. No NULL concept exists —
   EvoERP programs use "" and 0 as sentinel values.

5. **Key segment composition**: Most TAS tables have 2–4 key definitions (indexes).
   FILELOC's 386 table entries each have a single primary key. BKICMSTR likely has keys
   on PROD.CODE (primary), product class, unit-of-measure, etc. — confirmed via TAS source
   patterns in BKROA.SRC and BKMRF.SRC where `find M srch MTIC.PROD.CODE` is the standard
   primary key lookup.

---

## Things still to verify

- Full FCR (File Control Record) byte layout — need Pervasive SDK documentation.
  Only partially decoded from sample header.
- Types 12 and 13 in the DDF — exact Btrieve data type meaning.
- Whether RELATE.DDF FKs are enforced at the engine level or only procedurally.
- How the `.mdx` (multi-index) files differ from embedded B-tree indexes.
- `.XLB` lock file internal format (not needed for analysis; locking is handled by MKDE).
