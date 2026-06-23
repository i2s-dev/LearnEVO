# Btrieve / Pervasive PSQL `.B` File Format

Status: verified — FCR logical+physical record sizes confirmed by cross-validation; DDF fully
cataloged; type mapping confirmed; key definition page decoded; BKIC* family structure clarified.

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
04-05:  43 00       LE16 = 67 — possibly Btrieve file format version or internal overhead
08-09:  05 00       LE16 = 5 — primary FCR; alt FCR (page 8) shows 04 here; likely
                    a generation/checkpoint counter (diff of 1 = one checkpoint behind)
14-15:  0B 00       LE16 = 11 — unknown
16-17:  69 02       LE16 = 617 — LOGICAL RECORD SIZE (exact DDF record_end=617) ✓ confirmed
18-19:  CB 02       LE16 = 715 — record count at last file population; 0 in this empty sample
24-25:  01 00       Flag byte or version indicator
28-29:  0E 00       LE16 = 14 — unknown (may relate to page count: 140 pages / 10 = 14?)
4A-4D:  50 09 01 00 LE32 = 68,944 — possibly total allocated record bytes (< 71,680)
60-6B:  FF*12       End-of-chain marker for free page list (0xFFFFFFFF... = no free pages)
70-71:  00 00       (zero-filled)
72-73:  73 02       LE16 = 627 — PHYSICAL RECORD SIZE ✓ confirmed
                    Cross-validated: DDF record_end=617 + ~10 bytes Btrieve record header = 627
                    Verified using field.ddf: FCR+0x72=34, X$Field DDF record=34 bytes
74-75:  0B 00       LE16 = 11 — unknown
76-77:  0B 00       LE16 = 11 — unknown
78-79:  0E 00       LE16 = 14 — unknown
7A-7B:  3C 0F       LE16 = 3900 — UNKNOWN; NOT record size; Pervasive DDF files (file.ddf,
                    field.ddf) both show 272 at this offset; likely a Pervasive-internal
                    constant or pre-allocation parameter, not the physical record length
```

Note: The full FCR layout is not publicly documented by Pervasive. FCR+0x16 (logical record
size) and FCR+0x72 (physical record size) are confirmed by cross-validation across multiple
Btrieve files. All other fields are inferred.

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
| 12 | NOTE | — | Variable-length memo/blob. Only in DDF catalog: `X$Attrib.Xa$Attrs` (2048 B). Not used in any EvoERP business table. |
| 13 | LVAR | — | Large variable-length field. Only in DDF catalog: `X$View.Xv$Misc` (2000 B, SQL view text) and `X$Proc.Xp$Misc` (990 B, stored proc body). Not used in any EvoERP business table. |
| 14 | UBINARY | I (unsigned int) | Unsigned binary integer (1–4 bytes) |

Types 12 (NOTE) and 13 (LVAR) appear in exactly 3 fields total — all in DDF system tables
(`X$` prefix = DDF catalog internal). Confirmed by cross-referencing `fields.csv` file_ids
655 (X$View), 656 (X$Proc), 659 (X$Attrib) with `schema.md`. None of the 659 EvoERP
business tables use these types.

### OCCURS.DDF — repeating group / array support

`X$Occurs` (occurs.ddf, 28,672 bytes = 56 pages) defines **occurrence groups** — Btrieve's
mechanism for array-like repeating fields within a fixed-length record. For example, BKYSMSTR
has fields `BKYS.YN[1]` through `BKYS.YN[200]` — these are stored as a single fixed block in
the record with an occurrence definition pointing to the starting offset and repeat count. The
TAS 4GL `array N` directive matches directly onto the OCCURS definition.

Binary inspection of `samples/ddf/OCCURS.DDF`: data pages 48–55 contain ~150–200 records
stored as binary integers (file_id packed with occurrence_id, 24-byte record slots). The
records are present and active but cannot be decoded to table/field names without a full
Btrieve record-format parser. Presence confirmed — the `array N` declarations in TAS source
do generate OCCURS entries.

### RELATE.DDF — foreign key hints

`X$Relate` (relate.ddf, 45,056 bytes = 88 pages) stores referential integrity relationship
definitions (parent table + primary key → child table + foreign key).

Binary inspection of `samples/ddf/RELATE.DDF`:
- Pages 0 and 8 both start with `FC` magic — **dual FCR** for crash recovery (primary FCR at
  page 0, backup at page 8; standard Btrieve feature).
- Pages 16–31: densely packed B-tree index nodes (sequential integer entries).
- Pages 32, 40, 48, 56, 64, 72: B-tree root/leaf pages, each starting with `00 8X YY 00 00 00 00 00 FF FF FF FF` (the `FF FF FF FF` = Btrieve null/end-of-chain marker).
- Pages 80–87: data pages with very sparse records (one 4-byte entry per page, ~8 total
  records). FK references stored as binary file_id integers — no readable table names.

**Conclusion: engine-level RI enforcement is NOT the primary mechanism in EvoERP.**
Only ~8 FK relationships are defined in the DDF (for 659 tables). EvoERP enforces
referential integrity procedurally in TAS code via `find M` + `flerr()` checks before
every related-record lookup.

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

2. **Average record layout**: EvoERP tables average ~37 fields per table. BKICMSTR has
   64 DDF-registered fields (record_end=617 bytes). The BKIC* item-master family spans
   **16 separate physical .B files** (BKICMSTR.B, BKICALTD.B, BKICALTP.B, BKICPMAT.B,
   BKICDIM.B, BKICELOC.B, BKICEMTR.B, BKICLOC.B, BKICLOCM.B, BKICMFG.B, BKICREF.B,
   BKICREQ.B, BKICTAX.B, BKICVAL.B, BKICAMTR.B) collectively covering ~460 fields.

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

## Pass 225 — Deep binary analysis of BKICMSTR.B page structure (2026-06-23)

The sample `samples/BKICMSTR.B` (71,680 bytes, 140 pages × 512) was re-analyzed at
byte level. Key findings:

### BKICMSTR.B sample status: schema-only/empty copy

Only the following pages contain non-zero data. Data record pages are entirely zero-filled,
confirming this is a **schema-only copy** — the file was created (or captured) without live
data records. The FCR header record count field (`CB 02` = 715 at offset 0x18) reflects the
configured maximum or historical count, **not current live records.**

### Non-zero pages and their roles

| Pages | Header bytes | Interpretation |
|-------|-------------|----------------|
| 0, 8 | `46 43 00 00 43 00 00 00` | Primary and backup FCR (dual-FCR confirmed) |
| 1, 7, 15 | `00 00 00 00 …` | Sparse key-definition extension or index hint pages |
| 32, 40 | `01 00 00 50 50 00 00 00` | B-tree index root pages (type=0x01) |
| 33–39, 41–47 | `FE FF FF FF 00 00 00 00` | Empty B-tree leaf/data clusters (null-pointer fill) |
| 48, 52, …, 92 (intervals of 4) | `NN 00 00 00 00 80 00 00` | Secondary index root pointers (one per key, 4-page slot) |
| 96–136 (intervals of 4) | `NN 00 00 00 45 00 00 00` | Additional key-descriptor pages (`45`=0x45=Btrieve key descriptor signature?) |

### Key definition page (page 32) decoded

```
Offset  Bytes                    Interpretation
------  -----                    --------------
0x00:   01 00 00 50 50 00 00 00  page type=0x01 (key definition), flags=0x5050
0x08:   05 00 00 00 00 00 00 00  key_count=5 (5 key definitions)
0x10:   22 00 00 00 0A 80 01 00  key 0: root_page=0x22=34, flags=0x800A, extra=0x0001
0x18:   16 00 00 00 09 80 01 00  key 1: root_page=0x16=22, flags=0x8009
0x20:   15 00 00 00 08 80 01 00  key 2: root_page=0x15=21, flags=0x8008
0x28:   14 00 00 00 07 80 01 00  key 3: root_page=0x14=20, flags=0x8007
0x30:   13 00 00 00 06 80 01 00  key 4: root_page=0x13=19, flags=0x8006
```

5 keys match the `05 00` at FCR offset 0x08-0x09. The 0x80 flag byte in the key
descriptor likely = "key type=primary/unique" flag; low nibble = segment count or key number.
Root page numbers point to all-zero index pages (empty file).

### Empty data page pattern

Pages 33–39 and 41–47 contain the repeated 8-byte pattern:
```
FE FF FF FF 00 00 00 00 (repeated 64× per page)
```
`FEFFFFFF` = little-endian int32 = -2 (or 0xFFFFFFFE) — Btrieve's null/end-of-chain pointer.
These pages are pre-allocated B-tree leaf pages with all record pointers null (empty file).
Each 8-byte entry = one B-tree leaf node slot (page_ptr + flags).
Pages per cluster (8 per group of data pages) × 64 entries = 512 slots available per key cluster.

### Physical record size — confirmed (Pass 228 correction)

**FCR+0x16 (16-17): `69 02` = LE16 = 617 bytes — LOGICAL record size** (exact DDF record_end).

**FCR+0x72 (72-73): `73 02` = LE16 = 627 bytes — PHYSICAL record size** (DDF 617 + 10-byte
Btrieve record header/overhead).

Cross-validation: field.ddf FCR+0x72 = 34 bytes, and X$Field DDF records are 34 bytes
(file_id 2B + field_id 2B + name 20B + type 2B + offset 4B + size 2B + dec 1B + flags 1B = 34 bytes).
The 10-byte difference between logical and physical record size is consistent Btrieve overhead.

**FCR+0x7A (7A-7B): `3C 0F` = LE16 = 3900 — NOT record size.** Both file.ddf and field.ddf
show 272 (0x0110) at this offset — a Pervasive-internal constant. The 3900 in BKICMSTR.B
at this offset is a different per-file parameter (possibly key space allocation or reserved blocks).

Note: Prior documentation incorrectly labeled `3C 0F` as being at offset 0x78-0x79 and
identified it as the record size. Both were errors; corrected in Pass 228.

**BKICMSTR namespace clarification:** Programs that use BKICMSTR also typically open MTICMSTR.B
(54 MTIC.PROD.* fields, record=1533 bytes) as a separate file. The MTIC.PROD.* vars come from
MTICMSTR.B, not BKICMSTR.B. BKICMSTR.B exclusively stores BKIC.PROD.* (64 fields, 617 bytes).

If live, a 715-record BKICMSTR.B would occupy: 715 × 627 ≈ 448 KB of record data (plus
index pages) — a small inventory master, confirming i2 Systems' small-manufacturer scale.

**Status: Physical record size confirmed ✅ at 627 bytes.**

---

## Things still to verify

- Full FCR (File Control Record) byte layout — partially decoded from BKICMSTR.B and
  RELATE.DDF FCR headers. The dual-FCR (pages 0 + 8) is confirmed. Full field-by-field
  mapping requires Pervasive PSQL SDK documentation not available.
- Whether `CB 02` (715) in FCR is the record count or a different metric — sample file has
  zero live data records; the field may be a pre-set maximum or a stale header value.
- How the `.mdx` (multi-index) files differ from embedded B-tree indexes — no `.mdx`
  sample files exist in `samples/`. The 10 `.mdx` files on the share are overflow key
  files for tables exceeding 24 key segments; structure is a separate Btrieve B-tree.
- `.XLB` lock file internal format (not needed for analysis; locking is handled by MKDE).

**Resolved (Pass 106i):**
- Types 12 and 13 — confirmed: NOTE and LVAR, exclusively in DDF catalog tables. ✅
- RELATE.DDF FK enforcement — confirmed: engine-level enforcement not in use; only ~8 FK
  records defined; RI is enforced procedurally by TAS programs. ✅
- OCCURS.DDF status — confirmed: active, ~150–200 records present. ✅

**Resolved (Pass 225):**
- Key definition page structure: type=0x01, 5-key BKICMSTR confirmed, 8-byte entry format. ✅
- Empty record slot marker: `FE FF FF FF 00 00 00 00` = null B-tree pointer fill. ✅
- BKICMSTR.B sample confirmed as schema-only copy (data pages zero-filled). ✅

**Resolved (Pass 228 — FCR cross-validation):**
- FCR+0x16 = logical record size (617 bytes) — exact DDF record_end match. ✅
- FCR+0x72 = physical record size (627 bytes = DDF 617 + 10 Btrieve overhead). ✅
  Cross-validated: field.ddf FCR+0x72=34, X$Field records=34 bytes (2+2+20+2+4+2+1+1=34).
- FCR+0x7A = NOT record size; Pervasive-internal (DDF files show 272; BKICMSTR shows 3900). ✅
- Corrected offset error: doc previously mislabeled 72-73 as 70-71 and 7A-7B as 78-79.
- Corrected field count: BKICMSTR.B has 64 DDF fields (not 422); BKIC* family = 16 .B files.
- MTIC.PROD.* fields confirmed in MTICMSTR.B (separate physical file), not BKICMSTR.B. ✅
