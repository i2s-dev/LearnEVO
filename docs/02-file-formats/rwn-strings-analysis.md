# RWN String Dumps — Analysis Technique
Status: confirmed | verified

## What These Are

`samples/rwn_strings/` contains **2,575 `.txt` files** — one per `.RUN` or `.RWN` program file.
Each file contains all printable ASCII strings extracted from the binary program, one per line.

Example:
```
samples/rwn_strings/BKAPA.RUN.txt      (~1,958 lines)
samples/rwn_strings/BKARA.RUN.txt      (~3,501 lines)
samples/rwn_strings/BKWOA.RUN.txt      (~3,284 lines)
samples/rwn_strings/BKGLA.RUN.txt      (~1,331 lines)
```

**Format:** Plain ASCII, one string per line, LF line endings.

This is the primary way to understand program behavior **without decrypting the `.RWN`/`.RUN`
binaries**. It gives us table names, field labels, error messages, and configuration keys for
every program in the system.

---

## What You Can Extract

### 1. Table Names (Database I/O)

Programs reference the tables they open directly by name. From `BKAPA.RUN.txt`:
```
BKYSMSTR
BKSYMSTR
BKAPVEND
BKAPVND2
BKAPDESC
BKARCUST
BKCMVNDH
BKCMVNFC
BKCMVNDF
BKICMSTR
BKGLCOA
ISSHIPCO
ISTERMS
ISTAXGRP
```

This tells us exactly which tables AP-A (vendor entry) reads and writes — without source code.

### 2. UI Labels and Field Names

Form labels appear as strings:
```
Enter Vendors
Vendor Code
Alpha Sort
Company Name
Address
City, State, Zip
Contact
Phone
Fax
Email
Terms
GL Account
```

### 3. Error Messages (Validation Logic)

Error messages reveal input validation rules:
```
Vendor Code can not be blank.
This vendor already exists.
This is not a valid Currency account.
This is not a valid GL account.
Customer codes cannot contain single or double quote marks, nor commas.
Cannot change Status since Actual Costs have been incurred for this Work Order.
```

### 4. ISTS.CFG.* Configuration Keys

Over **900 configuration parameters** follow the `ISTS.CFG.*` naming pattern. These are
feature flags and settings stored in the system configuration (BKSYMSTR / BKYSMSTR):

```
ISTS.CFG.APSORT       — AP sort order setting
ISTS.CFG.ARSORT       — AR sort order setting
ISTS.CFG.EVONTS       — EvoNotes feature toggle
ISTS.CFG.VIAMST       — Ship-via master toggle
ISTS.CFG.WOCALC       — Work order calculation method
ISTS.CFG.WOOPEN       — Work order open setting
ISTS.CFG.WOONLY       — WO-only mode
ISTS.CFG.WOOVER       — WO override flag
```

These are the key names for the YN[N] boolean array in BKYSMSTR. By extracting all
`ISTS.CFG.*` strings from the rwn_strings files, we can map the full configuration directory.

### 5. Menu Code References

Menu codes appear as strings in most program files:
```
AP-A
AP-B
MM-L
CM-E
CS-B
DE-J-E
```

### 6. Function Key Mappings

Consistent across all programs:
```
F1 Help
F2 Lookup
F3 Clear
F5 First
F6 Last
F7 Previous
F8 Next
F9 Find
F10 Save
```

### 7. System / License Info

```
You are missing the License file. Please contact lynn@istechsupport.com.
Evo - ERP License
ISTECH Support License
ISTS DEMO
```

Support contact: `lynn@istechsupport.com` (ISTECH support)

---

## How to Use This for Research

**To understand what a program does:**
1. Find its string file in `samples/rwn_strings/`
2. Look for table names (uppercase, pattern BK\*, WO\*, MT\*, IS\*)
3. Look for UI label strings (mixed case, sentence-like)
4. Look for error messages (validation rules)
5. Look for `ISTS.CFG.*` keys (feature flags this program reads)

**To map all ISTS.CFG.* keys:**
Run: `grep -h "ISTS\.CFG\." samples\rwn_strings\*.txt | sort -u`
This will produce the complete configuration key directory from all 2,575 programs.

**To find which programs use a specific table:**
Run: `grep -l "BKARCUST" samples\rwn_strings\*.txt`
This returns every program that references the AR customer table.

---

## Coverage

| File pattern | Count | Notes |
|-------------|-------|-------|
| `*.RUN.txt` | Most of 2,575 | TAS Pro 6 legacy programs |
| `*.RWN.txt` | Subset | TAS Pro 7 programs (strings still extractable even from encrypted RWN) |
| `*.dcy.txt` | A few | Bootstrap DCY string dumps |

The bootstrap files (`suwin6.dcy.txt`, `suwin6t.rwn.txt`, `suwin7.dcy.txt`, `suwin7.rwn.txt`)
contain strings from the runtime initialization files.

---

## Limitations

- Strings only — no bytecode, no control flow, no loop/branch structure
- String order in file is arbitrary (not sorted by program flow)
- Some strings may be false positives (data constants vs. code references)
- `.RWN` files are encrypted; string extraction for `.RWN` files may be less complete than `.RUN`

---

*Last updated: 2026-06-11*
*Confidence: 82/100 — File format confirmed by direct sampling; content types confirmed; extraction technique confirmed. Full ISTS.CFG.* directory not yet extracted.*
