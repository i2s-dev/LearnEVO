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

### FCR field map — confirmed from multi-file analysis (Pass 412, 2026-06-30)

Cross-validated across 17 EvoERP `.B` files with known DDF metadata. Fields confirmed as
**C** (constant across all files), **V** (varies), or **K** (known function).

```
Offset  Size  Status  Meaning
------  ----  ------  -------------------------------------------------------
0x00    2     K       "FC" magic (0x46 0x43) — Btrieve file signature
0x02    2     C=0     Flags or format subversion (always 0 in EvoERP)
0x04    2     V       Varies (1, 67, 123) — possibly key format flags
0x06    2     C=0     Reserved / unused
0x08    4     V       Varies — NOT a reliable record count; appears to be
                      a checkpoint counter or B-tree page counter
0x0C    4     V       0 or 16384 — possibly free page chain head pointer
0x10    4     C=0     Constant 0 — reserved
0x14    2     V       Varies — possibly key specification length/count
0x16    2     K       LOGICAL RECORD LENGTH (= DDF record_end; 100% confirmed
                      cross-validated against 12 DDF tables)
0x18    2     V       Varies — unknown (may be key definition data)
0x1A    2     C=0     Constant 0 — reserved
0x1C    2     V       Varies (0..675) — NOT page size (values don't match
                      standard Btrieve page sizes 512/1024/2048/4096)
0x1E    2     C=0     Constant 0 — NOT index count despite prior hypothesis
0x20    4     C=0     Constant 0 — NOT record count in this Pervasive version
0x24    2     C=1     Constant 1 — file format marker
0x26    2     C=0     Constant 0
0x28    4     V       Varies — unknown (index/page related)
0x2C    4     C=0     Constant 0 (unused pages count or free-page tail)
0x30    2     C=0     Constant 0
0x32-   ~     C=0     Bytes 0x32-0x43 all constant 0 in EvoERP files
0x44    2     V       Varies (0, 1, 2)
0x48    4     V       Two values: 0x07000000 or 0x09510000
                      (Pervasive-internal version or capability flags)
0x4C    4     C=1     Constant 1 — format marker
0x50    4     V       Varies — unknown
0x54    4     C=0     Constant 0
0x58    4     C=0xFFFF0000  Bitmask sentinel (high 16 bits set)
0x5C    4     C=0xFFFFFFFF  All-1s sentinel — free page list end marker
0x60    4     V       0xFF0000FF or 0xFFFFFFFF — another sentinel mask
0x64    2     C=0xFFFF     All-1s sentinel
0x66-   ~     C=0     Bytes 0x66-0x71 all constant 0 in EvoERP files
0x70    2     C=0     Constant 0
0x72    2     K       PHYSICAL RECORD LENGTH = logical + overhead (confirmed)
                      Standard overhead = 10 bytes (Btrieve record header)
                      Anomalous overhead = 2 bytes (BKARCUST, ISJAVA — reason unknown)
0x74    2     V       Varies — key-definition data
0x76    2     V       Varies — key-definition data
0x78    4     V       Varies — unknown
0x7C    4     C=0     Constant 0
```

#### Record header overhead (confirmed Pass 412)

The 10-byte Btrieve record header appended to each physical record contains:
- B-tree management pointers and delete/modification flags
- Confirmed: physical = logical + 10 for 15/17 analyzed files
- Two anomalous files (BKARCUST, ISJAVA) have physical = logical + 2 — cause unknown;
  may relate to large-record compression, different file version, or Default vs. active company

#### Cross-validation table (logical record vs. DDF)

| Table | DDF end | FCR 0x16 | FCR 0x72 | overhead |
|-------|--------:|--------:|--------:|--------:|
| BKICMSTR | 617 | 617 | 627 | 10 |
| BKARCUST | 2498 | 2498 | 2500 | **2** |
| BKARINV | 1551 | 1551 | 1561 | 10 |
| WORKORD | 1173 | 1173 | 1183 | 10 |
| BKGLCOA | 556 | 556 | 566 | 10 |
| BKGLTRAN | 137 | 137 | 147 | 10 |
| AHSYLOG | 27 | 27 | 37 | 10 |
| BKPSUSER | 71 | 71 | 81 | 10 |
| ISEXUSER | 83 | 83 | 93 | 10 |
| ISACCESS | 275 | 275 | 285 | 10 |
| ISJAVA | 2044 | 2044 | 2046 | **2** |
| BKLOGON | 46 | 46 | 56 | 10 |

Note: The full FCR layout is not publicly documented by Pervasive. FCR+0x16 (logical record
size) and FCR+0x72 (physical record size) are confirmed by cross-validation across 12 DDF
tables. All other field assignments are inferred from pattern analysis.

### Header byte decode (BKICMSTR.B FCR sample)

```
Offset  Hex value   Interpretation
------  ---------   -----------------------------------------------------------
00-01:  46 43       "FC" — Btrieve file magic
02-03:  00 00       Constant 0 (flags/version)
04-05:  43 00       LE16 = 67 — varies; possibly key format flags
08-09:  05 00       LE16 = 5 — checkpoint/generation counter
16-17:  69 02       LE16 = 617 — LOGICAL RECORD SIZE (DDF confirmed) ✓
24-25:  01 00       Constant 1 — format marker
58-5B:  00 00 FF FF LE32 = 0xFFFF0000 — sentinel mask
5C-5F:  FF FF FF FF LE32 = 0xFFFFFFFF — free page list end sentinel
72-73:  73 02       LE16 = 627 — PHYSICAL RECORD SIZE (617+10) ✓
```

### Companion files

| Extension | Purpose |
|-----------|---------|
| `.B` | Main Btrieve data file (records + B-tree indexes embedded) |
| `.mdx` | Multi-Index Xtra — dBASE IV compound index format; used ONLY for the 10 DBF-format FILEDICT/FILELOC/BKLUGRID/BKMENUSU/errmsg tables — NOT present on Btrieve `.B` files |
| `.XLB` | Btrieve overflow/blob companion — magic `46 43 00 00` (= "FC\0\0", same as `.B`); present ONLY on tables that have variable-length memo/blob fields; 7 tables in EvoERP (all AP-related except BKISTAX) |
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

## `.XLB` companion files — complete catalog (Pass 361 2026-06-26)

`.XLB` files are Btrieve overflow companions for tables that store variable-length
memo/blob fields. Magic bytes `46 43 00 00` (= "FC\0\0") confirm they are Btrieve
format. NOT a "lock byte" file — that was a prior misidentification (corrected Pass 292).

**Only 7 tables in EvoERP have XLB files:**

| Table | Corresponding module | Max size (AB company) | Contents |
|-------|---------------------|-----------------------|----------|
| `BKAPAPOL.XLB` | AP — AP Policy | 112 KB | AP policy terms/conditions text |
| `BKAPCHKF.XLB` | AP — Check Form | 84 KB | Check form template blob |
| `BKAPCHKH.XLB` | AP — Check Header | 11.5 MB | Check memo text (one per check) |
| `BKAPHPOL.XLB` | AP — Historical Policy | **115 MB** | Archive of historical AP policy text |
| `BKAPINVL.XLB` | AP — Invoice Line | 9.7 MB | Invoice line extended descriptions |
| `BKAPINVT.XLB` | AP — Invoice Header | 21.8 MB | Invoice header memo text |
| `BKISTAX.XLB` | IS — Tax | 56 KB | Tax configuration blob |

**Pattern:** Files exist per-company subfolder (AB, Default, I2, Testdata, UU = 5 companies).
`BKAPHPOL.XLB` = 115 MB in AB = largest single data file; stores full-text AP policy history.

**Implication:** Of the 659 tables, only 7 (1%) have variable-length memo fields.
All AP-module tables (except the non-AP `BKISTAX`). All other EvoERP fields are
fixed-length — consistent with the Btrieve fixed-record-size model.

---

## Btrieve status codes and TAS Pro I/O error handling (Pass 408, 2026-06-30)

Source: `samples/errmsg_clean.txt` (extracted from `samples/errmsg.dbf`, TAS Pro 5.0 runtime
error message table — same messages used by TAS Pro 7 runtime).

### TAS Pro error codes → Btrieve status code mapping

TAS Pro error codes 200–225 are the localized messages for Btrieve engine status codes.
The `@` in the message is a runtime substitution for the file name.

| TAS err | Btrieve status | Message summary |
|---------|---------------|-----------------|
| 200 | 1 | Physical I/O error during disk read/write |
| 201 | 4 | File not open — must call `open` first |
| 202 | 5 | Duplicate key — key value already exists, duplicates not allowed |
| 203 | 6 | Key changed during traversal — tried `next`/`prev` after modifying the key field |
| 204 | 10 | Attempt to modify a non-modifiable key segment |
| 205 | 11 | Pre-image file error — cannot access/create/open the transaction log |
| 206 | 12 | Pre-image disk full |
| 207 | 13 | Unrecoverable error — restore from backup |
| 208 | 14 | Invalid file format — not a Btrieve file; check `type` in `open` |
| 209 | 15 | Pre-image not enabled — `/T` transaction trailer required |
| 210 | 16 | Nested transaction — a prior `BEGIN_TRANS` must be `COMMIT`-ed first |
| 211 | 17 | Transaction process error — disk probably full; restore from backup |
| 212 | 18 | No active transaction — `ROLLBACK_TRANS` requires prior `BEGIN_TRANS` |
| 213 | 19 | Transaction file limit exceeded — max 12 files per transaction |
| 214 | 20 | File is read-only — no write or delete permitted |
| 215 | 21 | Buffer overflow — too many open files; adjust `/M` memory option |
| 216 | 22 | Owner already set for this file |
| 217 | 23 | Wrong owner name — file cannot be opened |
| 218 | 24 | Expanded memory manager error |
| 219 | 81 | Write-write conflict — record changed by another user since last read |
| 220 | 83 | Lock table full — adjust `/L` in Btrieve loader |
| 221 | 84 | Record was deleted by another user — use locking to prevent |
| 222 | 85 | Transaction data mismatch — record must be read within its own transaction |
| 223 | 86 | Too many open files (DOS `FILES=` limit) |
| 225 | 90 | DOS access restriction on file/record |

**Notes:**
- Status codes 25–80 are Btrieve internal states not surfaced to the TAS application layer.
- Status codes 82 and 88–89 are not mapped (gaps in the 220–225 range).
- These correspond to TAS Pro 5.0 / Btrieve 5.x. Btrieve 6.x+ (used in EvoERP) added status codes 90+ for Pervasive network and security errors; the TAS 7 runtime added handling for these beyond the errmsg.dbf table.

### TAS Pro runtime I/O status codes (not Btrieve engine codes)

TAS Pro adds its own layer of runtime status messages for file operation outcomes that Btrieve signals but TAS interprets:

| TAS err | Trigger | Message |
|---------|---------|---------|
| 265 | `find` / `save` lock wait | "The record in file: @ is locked by another user." (silent — no retry prompt) |
| 266 | `find` / `save` lock wait | "The record in file: @ is locked by another user. Do you wish to try again? (Y/N)" |
| 268 | `scan` / `find N` | "The search reached the end of the file." |
| 269 | `find P` beyond first | "The search reached the beginning of the file." |
| 270 | `find M/E/K` no match | "The record was not found." |
| 271 | `find` on empty file | "There are no records in the file." |
| 272 | `delete` with no active record | "There is no active record in the file so you cannot delete it." |

Error 265 is a "soft lock" (wait silently), 266 is interactive (asks user to retry). The
program controls which variant appears via TAS Pro's file open lock mode parameter.

### `flerr()` — programmatic error checking

TAS Pro's `flerr(fnum('TABLENAME'))` function returns the last Btrieve status code for a
given file handle. Used in two patterns:

**Explicit check after find/save:**
```
find M srch BKICMSTR = MTMRP.PARTNO
if flerr(fnum('BKICMSTR')) <> 0
    ; handle not-found or I/O error
endif
```

**`ifna` — implicit not-found handling:**
TAS Pro's `ifna LABEL` clause on a find statement jumps to LABEL when the result is
"record not found" (Btrieve status 9 = end of file, or status 4 equivalent).
`ifna` is syntactic sugar for `if flerr() = not-found-status then goto LABEL`.
No explicit `flerr()` call needed.

**`err LABEL`** — jumps to LABEL on ANY I/O error (status <> 0), including locking errors.
Combined with `ifna` for full coverage:
```
find M srch BKBMMSTR = INVNUM ifna NoRecord err IOError
```

### Btrieve operation codes (standard reference)

The `flerr()` status reflects the result of the most recent Btrieve operation. Standard
Btrieve operation codes that TAS Pro invokes internally:

| Op code | Btrieve operation | TAS Pro keyword |
|---------|------------------|-----------------|
| 0 | Open | `open TABLENAME ...` |
| 1 | Close | `close TABLENAME` |
| 2 | Insert | `save TABLENAME` (new record) |
| 3 | Update | `save TABLENAME` (existing record) |
| 4 | Delete | `delete TABLENAME` |
| 5 | Get Equal | `find E` |
| 6 | Get Next | `find N` or `scan` loop iteration |
| 7 | Get Previous | `find P` |
| 8 | Get Greater or Equal | `find M` (by match) |
| 9 | Get Greater Than | (TAS `find A` — absolute position) |
| 10 | Get Less or Equal | (reverse-direction find) |
| 11 | Get Less Than | (reverse-direction find) |
| 12 | Get First | `find F` |
| 13 | Get Last | `find L` |
| 22 | Get by percentage | (not used by TAS Pro) |
| 28 | Get Direct | (TAS `find A` — direct page access) |
| 33 | Begin transaction | `BEGIN_TRANS` |
| 34 | End transaction (commit) | `COMMIT_TRANS` |
| 35 | Abort transaction (rollback) | `ROLLBACK_TRANS` |
| 30 | Set owner | (file security — not used in EvoERP) |
| 31 | Clear owner | (file security) |

**Lock modes (TAS `open` statement flag):**
TAS Pro opens files with a lock flag that determines how concurrent access is handled:

| Open flag | Btrieve equivalent | Behavior |
|-----------|--------------------|---------|
| (default) | No lock | Read/write with retry on lock conflict |
| `type R` | Read-only | No writes allowed; no lock conflicts |
| (auto-lock) | Record lock on read | Prevents write-write conflict (status 81) |
| `scope R` in scan | Bounded key range | Limits scan to within a key range |

When a lock conflict occurs (status 81 or 83), TAS Pro either:
1. Displays error 265 (silent — program handles retry in code), or
2. Displays error 266 with Y/N prompt (user decides whether to retry)

The choice is controlled by the calling program's error-handling setup before the `find`.

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
- Full internal layout of `.XLB` blob files (magic confirmed as FC\0\0; internal record format not decoded).

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
