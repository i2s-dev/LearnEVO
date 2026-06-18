# RWN / RUN Program Analysis Techniques
Status: confirmed | verified | Pass 106 updated 2026-06-18

Two complementary techniques are used to analyze EvoERP program binaries without source code.
They evolved as decryption became available: Technique 1 works on all files; Technique 2
requires the decryption key (now confirmed — see `docs/02-file-formats/decryption-findings.md`).

---

## Technique 1 — String Extraction (pre-decryption, all 2,575 files)

`samples/rwn_strings/` contains **2,575 `.txt` files** — one per `.RUN`, `.RWN`, or `.DCY`
program file. Each file contains all printable ASCII strings (≥4 chars) extracted from the
raw binary.

### What you can extract

| Category | How to recognize | Example |
|---|---|---|
| Table names | ALL_CAPS, pattern BK\*/WO\*/MT\*/IS\*/MT\* | `BKARCUST`, `WORKORD` |
| UI labels | Mixed case, sentence-like | `Enter Vendors`, `Vendor Code` |
| Error messages | Sentence with punctuation | `Vendor Code can not be blank.` |
| ISTS.CFG.* keys | Starts with `ISTS.CFG.` | `ISTS.CFG.APSORT` |
| Menu code refs | Pattern XX-Y[-Z] | `AP-A`, `DE-J-E` |
| Function key labels | F1–F10 labels | `F2 Lookup` |
| Support/license strings | Email/company | `lynn@istechsupport.com` |

### Common grep recipes

```powershell
# All ISTS.CFG.* keys across all 2,575 programs:
grep -h "ISTS\.CFG\." samples\rwn_strings\*.txt | sort -u

# Find which programs reference a table:
grep -l "BKARCUST" samples\rwn_strings\*.txt

# Extract all error messages from a module:
grep "\." samples\rwn_strings\BKAPA.RUN.txt | grep -v "ISTS\."
```

**535 unique ISTS.CFG.* keys** have been extracted and cataloged in
`docs/05-configuration/ists-cfg-keys.md`.

### Limitations (Technique 1)

- Strings only — no control flow, no loop/branch structure
- String order is arbitrary (not sorted by program flow)
- `.RWN` files are encrypted; strings inside encrypted regions are not visible — only
  unencrypted header/footer strings are captured
- Potential false positives (data constants vs. code strings)

---

## Technique 2 — Symbol Extraction (post-decryption, 1,122 RWN files)

**`samples/rwn_symbols.json`** — the master index of all 1,122 decrypted RWN programs.
Built by `scripts/rwn_extract_symbols.py` against the decrypted binary format.

Unlike string extraction, symbol extraction reads the **binary's own metadata tables** —
the file reference table, variable symbol table, and procedure symbol table — so results
are exact and structurally meaningful.

### JSON record format

Each entry in `rwn_symbols.json` is a JSON object:

```json
{
  "path": "\\\\i2s109-solidcrm\\DBAMFG$\\T7ARA.RWN",
  "size": 123456,
  "marker": "TWINB",
  "source_file": "T7ARA.SRC",
  "db_files": ["BKARCUST", "BKARINV", "BKGLTRAN", ...],
  "proc_count": 47,
  "procedures": ["calc_tax", "post_ar", "get_customer", ...],
  "var_count": 3917,
  "named_vars": ["BKIC.PROD.CODE", "BKAR.INV.NUM", "TEMP.AMT", ...]
}
```

| Field | Meaning |
|---|---|
| `path` | Original network share path |
| `size` | Decrypted binary size in bytes |
| `marker` | Always `TWINB` (TAS Pro 7 marker at offset 0x35 of decrypted body) |
| `source_file` | Source filename embedded in binary (60-byte space-padded field, e.g. `T7ARA.SRC` or `LISTG60.LIB`) |
| `db_files` | **Exact** list of database table names from the binary's file reference table (starts at 0x80, 16-byte null-padded entries) |
| `proc_count` | Number of procedure entries in the symbol table |
| `procedures` | List of procedure names (empty strings for LIB-compiled modules where byte 0 = 0x00) |
| `var_count` | Number of variable entries in the symbol table |
| `named_vars` | List of variable names (dot-notation buffer access, e.g. `BKIC.PROD.CODE`, `SCAN.WO`, `ISTS.EDATE`) |

### Source file field — what it tells you

The `source_file` field (60-byte space-padded ASCII string before the variable table) identifies
what was compiled to produce this RWN:

| `source_file` value | Meaning |
|---|---|
| `T7ARA.SRC` | Compiled from T7ARA.SRC (TAS Pro 7 source) |
| `LISTG60.LIB` | Linked-in from the standard library; procedures have no names |
| `suwin7.src` | Boot/license module |
| Blank | Unknown / stripped |

Only 7 `.SRC` files exist on this install (all in `\\i2s109-solidcrm\DBAMFG$\`):
`BKLME.SRC`, `EVOSCHED.SRC`, `EVOSERVICE.SRC`, `BKPLE.SRC`, `ISREPLNK.SRC`, `ISUSERON.SRC`,
`suwin7.src`. Most T7\*.RWN modules show their original T7\*.SRC filename even without source.

### Variable naming convention (named_vars)

Variable names follow TAS Pro 7 dot-notation for buffer access:

| Pattern | Meaning |
|---|---|
| `BKIC.PROD.CODE` | BKICMSTR table, field PROD_CODE |
| `BKAR.INV.NUM` | BKARINV table, field INV_NUM |
| `SCAN.WO` | Local buffer field named SCAN, subfield WO |
| `ISTS.EDATE` | System date buffer field |
| `TEMP.AMT`, `TEMP0`..`TEMP59` | Temporary variables |
| `IS.LOG.*` | ISLOG table fields |
| `LPASSWORD` | Login password variable |
| `COMPANY_NAME` | Current company name |

Buffer variables with the table's registered prefix (BKIC, BKAR, etc.) confirm which fields
a program actually reads or writes — beyond what `db_files` alone shows.

### How to query rwn_symbols.json

```python
import json

with open('samples/rwn_symbols.json') as f:
    programs = json.load(f)

# Find all programs that open BKARCUST:
ar_cust_users = [p for p in programs if 'BKARCUST' in p['db_files']]

# DB fingerprint: tables opened by T7ARA.RWN:
t7ara = next(p for p in programs if 'T7ARA.RWN' in p['path'])
print(t7ara['db_files'])

# Find programs with BKAR.INV.* buffer access:
ar_inv_writers = [p for p in programs
                  if any('BKAR.INV' in v for v in p.get('named_vars', []))]

# Count programs per source file:
from collections import Counter
Counter(p['source_file'] for p in programs).most_common(10)
```

### `rwn_symbols_summary.csv` — pre-computed summary

`samples/rwn_symbols_summary.csv` is a flat CSV version of `rwn_symbols.json`:
one row per program, columns: `path, size, source_file, db_files (pipe-separated),
proc_count, var_count`. Useful for Excel/LibreOffice analysis.

---

## Upgrade path: Technique 1 → Technique 2

| Dimension | Technique 1 (string extract) | Technique 2 (symbol extract) |
|---|---|---|
| Coverage | 2,575 files (all RUN+RWN+DCY) | 1,122 decrypted RWN files |
| Table names | Heuristic (uppercase strings) | Exact (file reference table) |
| Field/var names | None | Full variable symbol table |
| Procedure names | None | Procedure symbol table (SRC modules) |
| Reliability | 80–90% (false positives possible) | 99%+ (binary metadata) |
| Requires decryption | No | Yes (K_B confirmed — see decryption-findings.md) |

For any analysis task, prefer Technique 2 when the file is a `.RWN` (confirmed decryptable).
Fall back to Technique 1 for `.RUN` legacy programs (no decryption needed or available).

---

## Standard analysis workflow

1. **Identify the program file** (from BKMENUSU.TXT menu code → program name mapping)
2. **Query rwn_symbols.json** for DB fingerprint, proc count, and variable names
3. **Read `rwn_strings/` text file** for UI labels, error messages, ISTS.CFG.* keys
4. **Cross-reference db_files** against the DDF schema (`samples/ddf/schema.md`) for field
   meanings
5. **Cross-reference named_vars** against BKARINV/BKARCUST etc. for specific field access
6. **Document findings** in the module's section of `docs/03-modules/` or `HELP-RESOURCES.md`

---

## Coverage statistics (confirmed 2026-06-18)

| Artifact | Count | Notes |
|---|---|---|
| `rwn_strings/` text files | 2,575 | One per program file (RUN+RWN+DCY) |
| `rwn_symbols.json` entries | 1,122 | Decrypted RWN files only |
| ISTS.CFG.* keys extracted | 535 | From Technique 1 across all 2,575 programs |
| Unique table names cataloged | 659 | From Pervasive DDF (X$File + X$Field) |
| Programs with named procedures | ~850 | SRC-compiled modules (byte 0 ≥ 0x20 in sym table) |
| Programs with LISTG60.LIB | ~270 | Library-linked; procedures unnamed |

---

*Last updated: 2026-06-18 (Pass 106)*
*Confidence: 90/100 — Both techniques fully documented with verified field formats; rwn_symbols.json
structure confirmed by direct Python inspection; extraction scripts tested on live data. Remaining
gap: procedure symbol table parsing for SRC modules not yet fully validated against a known SRC
file (only 7 SRC files available on this install).*
