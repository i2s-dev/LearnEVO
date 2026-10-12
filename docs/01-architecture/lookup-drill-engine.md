# Lookup / Drill Engine (WBKLOOKUP, ISDRILL, ISDRILLM, BKLUGRID)

Status: partial — mechanism verified from data/config files 2026-10-12; internal program logic not decompiled.

How EVO shows a lookup grid (magnifier buttons, "drill" buttons like WO-A → Material Issues).
Learned while diagnosing [KI-003](../../Issues/KI-003-wo-a-material-issues-empty-file.md).

## Provenance tags

Each fact is tagged with where it came from, because some sources can't be cited to the vendor:

| Tag | Source | Citable to ISTS? |
|-----|--------|------------------|
| **[OBS]** | Seen in the running EVO UI | Yes |
| **[DATA]** | Customer data files / file metadata, read with standard tools (Zen ODBC, `ls`) | Yes |
| **[CFG]** | Unencrypted vendor config/scratch files (dBase .DBF/.DBT, plain Btrieve data) | Grey — reveals internals |
| **[DEC]** | Decrypted .RWN program code (this project's research only) | **No** |

## Components

| Piece | Location (i2s-evo) | Format | Role |
|-------|--------------------|--------|------|
| `WBKLOOKUP.RWN` | `\\i2s-evo\EVOERP\` | encrypted TAS program | The generic lookup/grid program [DEC] |
| `drill\BKLUGRID.DBF/.dbt/.mdx` | `\\i2s-evo\EVOERP\Drill\` | dBase IV + memo | Grid definitions: one record per grid name [CFG] |
| `drill\ISDRILLM.B` | `\\i2s-evo\EVOERP\Drill\` | Btrieve, reclen 400 | Drill-link master: parent grid → child grid, with link fields [CFG] |
| `<company>\ISDRILL.B<co>` | e.g. `\\i2s-evo\EVOERP\I2\ISDRILL.BI2` | Btrieve, reclen 3456 | Per-company **scratch records**: the calling program writes the lookup request here [CFG] |

WBKLOOKUP opens `drill\ISDRILLM.B` and `drill\BKLUGRID.DBF` by literal path [DEC]. The per-company
`I2\ISDRILLM.BI2` (2024-09-29) appears to be unused by the current code [DEC — inferred].

## BKLUGRID.DBF — grid definitions [CFG]

dBase file, 278 records (2026-10-11 version). Fields:
`LUGRID_NAM, LUGRID_DAT (memo), LUGRID_FDN (file), LUGRID_KDA (memo), LUGRID_END, LUGRID_FOR (program),
LUGRID_PRO, LUGRID_DEL, LUGRID_TEX, LUGRID_KEY, LUGRID_EXB (date), LUGRID_EXA, LUGRID_EXT`.

- `LUGRID_DAT` memo = column list, one CSV line per column: `"expr","Header",...`
- `LUGRID_KDA` memo = selectable keys: `"TAS key name","Label","start field"`
- Memo block pointers are 10-digit block numbers into `.dbt` (block size from .dbt header offset 20).

Example — **WOBOMMI** ("Work Order Materials", file WOBOM, program WBKLOOKUP, dated 04/13/18):

```
DAT:  "WOBOM.COMPCODE","Component" / "ISFUNC.TYPE(WOBOM.COMPCODE)","Type" / "WOBOM.COMPDESC","Description"
      "WOBOM.TOTQTY","Qty Required" / "WOBOM.UM","UM" / "WOBOM.QTYISSUED","Qty Issued" / "WOBOM.%ISSUED","% Issued"
      "ISFUNC.ACBN()","BOM Note" / "ISFUNC.WBMSCRAP()","Qty Scrapped"
KDA:  "WOBOM.KEY","Materials","WOBOM.WOPRE"
      "WOBOM.KEY5","Components","WOBOM.COMPCODE"
KEY:  WOBOM.WOPRE, WOBOM.WOSUF, WOBOM.UID
```

The 2026-10-11 version is **byte-identical** to the backup `Drill\BKLUGRID.xBF/.xbt` (2025-05-31) for this
grid, apart from memo block numbers (523/524 vs 525/526).

## ISDRILLM.B — drill links [CFG]

Text-searchable records of the form `PARENTGRID  CHILDGRID  Label  ChildFile  ParentLinkFields  ChildLinkFields  keyno  ...`.
Relevant WO links:

| Parent | Child | Label | Child file | Link |
|--------|-------|-------|-----------|------|
| WORKORDERS | WOMATL | Materials | WOMAT | MTWO.WIP.WOPRE/WOSUF → WOMAT.WOPRE/WOSUF |
| WOBOMMI | WOMATL | Materials Issued | WOMAT | WOBOM.WOPRE/WOSUF → WOMAT.WOPRE/WOSUF (key 3, dated 09/17/18) |
| A_WORKORDERS | A_WOMATL | Archived Matreials *(sic)* | WOHMAT | archive equivalents |

## ISDRILL scratch record — the lookup request [CFG]

When a program opens a lookup, it writes one record into the company's ISDRILL file. Field layout
(from the RWN field tables [DEC]; record boundaries confirmed against live data [CFG]):

| Field | Offset | Size | Example (WO-A Material Issues, 2026-10-12) |
|-------|--------|------|---------------------------------------------|
| ID | 0 | 30 | `T7WOA073325A20261012` = program + HHMMSS + flag + YYYYMMDD |
| LOOKUP.GRID | 30 | 15 | `WOBOMMI` |
| LOOKUP.REC | 45 | 4 | 0 |
| LOOKUP.KEY | 49 | 2 | 0 |
| LOOKUP.FILE | 51 | 15 | `WOBOM` |
| LOOKUP.FILTERS | 66 | 1600 | blank |
| LOOKUP.COMM | 1666 | 150 | `WOBOMMI Work Order Materials 2` |
| LOOKUP.WHILE | 1816 | 1600 | `WOBOM.WOPRE = VAL( 55977 ) .A. WOBOM.WOSUF = INT(VAL( 1 ))` |
| LOOKUP.PFILTER | 3416 | 20 | blank — **new in 2026 builds** [DEC] |
| LOOKUP.PWHILE | 3436 | 20 | blank — **new in 2026 builds** [DEC] |

Observed patterns in I2's file (2026-10-12) [CFG]:
- **Drill-style calls** (WOBOMMI from T7WOA, BINS from T7INA/T7INLJ) store `KEY=0` and put
  `GRID Label keyno` in COMM, with a WHILE expression restricting to the parent record.
- **Plain lookups** (INVENTORY from T7INA, COA from T7GLE) set `KEY` (1, 2), leave COMM blank and use
  `"All" = "All"` as FILTER/WHILE.
- The file holds roughly one record per program session, so it shows the *last* lookup each session opened.
  This makes it a useful **diagnostic**: copy `I2\ISDRILL.BI2` right after a failing click and decode it.

Record lengths by company (header offset 0x16) [DATA]: I2/AB/AT/CA/Default/Testdata = **3456**;
`22\`, root `ISDRILL.B` and `Drill\ISDRILL.B` = 3416 (pre-PFILTER layout).

## Messages [DEC]

- `"Empty File"` — appears only in WBKLOOKUP.RWN (3 lookup routines), right after the record fetch. Means
  the lookup returned no records.
- `"You do not have security rights to view this lookup."` — immediately follows it in the same routines.
- `"Grid X was not found in the Grids file. Please contact your ISTech Support person."` — missing BKLUGRID record.
- 2026 build additions: `"Filter failed to find a match. Key"`, `"This is a Program Filter and cannot be removed."`,
  debug lines `Grid.Filters: lu_for_expr = …` / `lu_while_expr = …` (written when `LOOKUP.DBG` is on),
  `wbklookup_Drill_noadd lf= ln= lc= cp= lk= lr= sv=` (written by T7WOA to `drill.dbg`).

## Version history seen

| File | Before | After (2026-10-11 10:23) |
|------|--------|--------------------------|
| WBKLOOKUP.RWN | "ISTS Enhancement 05/30/24", 679,177 B (June 2026 sample) | "ISTS Enhancement 05/05/26", 718,359 B |
| T7WOA.RWN | 967,566 B (2025-03-28 build) | "ISTS Enhancement 09/16/26", 1,031,261 B [OBS title bar] |

## Related

- [WO-A Material Issues button](../03-modules/wo-work-orders/wo-a-material-issues.md)
- [2026-10-11 ISTS update — changed files](2026-10-11-ists-update.md)
- [ODBC DDF null-indicator misalignment](../04-data-dictionary/odbc-ddf-null-indicator-offsets.md)
