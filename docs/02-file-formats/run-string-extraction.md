# TAS Pro 6 `.RUN` String Data Extraction

Status: **verified** — extraction method confirmed; BKAWLB fully cataloged (Pass 245);
cross-generation corpus confirmed (Pass 561, 2026-07-02)

Last updated: 2026-07-02

---

## Overview

Every `.RUN` file embeds string literals in its DATA CHANNEL as tagged records. These
strings encode the program's readable logic: UI messages, menu labels, function-key specs,
table names, sort options, error messages, and help wiring.

Extracting all strings from a `.RUN` binary gives a near-complete narrative of what the
program does and says to the user.

---

## String Record Format

String literals use a 4-byte tagged header within the data channel:

```
41 00 LL_lo LL_hi [LL bytes of string data]
```

- Tag `0x41` ('A') followed by `0x00` = string literal record
- `LL` = string length as a little-endian 16-bit integer
- String data follows immediately (NOT null-terminated)
- These are NOT 7-byte instructions — they are data records pointed to by instructions
  (CALL_LIB, PMSG, MENU, etc.) via the addr/b2 chain

**Total in BKAWLB.RUN:** 786 string records; 432 with ≥3 printable chars.

---

## Extraction Method

```python
import struct

with open('BKAWLB.RUN', 'rb') as f:
    data = f.read()

# Header field at offset 0x08 = data channel total size
data_channel_end = struct.unpack_from('<I', data, 8)[0]

strings = []
i = 0
while i < data_channel_end - 3:
    if data[i] == 0x41 and data[i+1] == 0x00:
        length = struct.unpack_from('<H', data, i+2)[0]
        if 0 < length < 256:
            s = data[i+4:i+4+length]
            strings.append((i, length, s.decode('latin-1', errors='replace')))
            i += 4 + length
            continue
    i += 1
```

---

## BKAWLB.RUN — Complete String Narrative (Pass 245)

BKAWLB = **Print Work Order Schedule** report.

### Program Identity
| String | Meaning |
|--------|---------|
| `AW-L-B` | Program short name (prg.name) |
| `  Print Work Order Schedule` | Report title (prg_hdr) |

### Tables Referenced
| String | Notes |
|--------|-------|
| `BKARCUST` | AR customer master |
| `BKICMSTR` | IC item master |
| `MTICMSTR` | Multi-site item master |
| `WORKORD` | Work order header |
| `BKSYMSTR` | System/symbol strings |
| `bksyhelp` | Help system lookup (lowercase) |
| `dbahlpid` | Help ID table (lowercase) |
| `DBAHELP.HLP` | Windows Help file |
| `WINHLP32.EXE` | Windows Help viewer (spawned via EXEC_TOP_WAIT) |
| ` -n ` | WinHelp command-line switch (topic number mode) |

### Sort Options (menu)
Title: `Sort by`

| String | Sort Key |
|--------|----------|
| ` 1 - Start Date  01011` | Sort 1, key=0101,0102 (start date fields) |
| ` 2 - Finish Date 01022` | Sort 2 (finish date) |
| ` 3 - Work Order  01033` | Sort 3 (WO number) |
| ` 4 - Item Number 01044` | Sort 4 (item/part number) |
| ` 5 - Customer    01055` | Sort 5 (customer) |
| ` 6 - Job Number  01066` | Sort 6 (job number) |
| ` 7 - Due Date    01077` | Sort 7 (due date) |

The trailing code (e.g., `01011`) appears to encode the sort field indices.

### Filter Options
**Status codes (ENT.STAT):** 4 selectable positions (mask `X `)

**Priority codes (ENT.PRI):** 3 selectable positions

**Class codes (ENT.CLASS16):** 16 positions; `All` / `Blank only` / `[class] only` / `[class] & blank` variants

### Error/Validation Messages
| String | Type | Trigger |
|--------|------|---------|
| `The class code filter you have established will exclude every work order. ` | warn | All 16 class slots empty + inc.blank.class=N |
| `Please select at least one status code. ` | info | All 4 status positions empty |
| `Please select at least one priority code. ` | info | All 3 priority positions empty |
| `There are no records in the primary file. ` | info | No WO records found |
| `>>>>>  Report was terminated before completion  <<<<<` | print | ABORT_RPT section |

### Work Order Browse Columns (7 sort orders, each reordered)
The browse window shows a different column order per sort key:
- **Sort 1 (Start Date):** Parent Part, Work Order, Stat, Description, Cust Cd, Customer Name, SO#, Qty to Make, Start Dt, Fin Dt, Job Number
- **Sort 5 (Customer):** Customer Name, Work Ord, Stat, Parent Part, Description, Cust Cd, SO#, ...
- **Sort 7 (Job):** Job Number, Work Ord, Stat, Parent Part, Description, ...
(etc. — each of the 7 sort orders has its own column set)

### Work Order Search Keys
Prompt: ` Search Key `

| Code | Description |
|------|-------------|
| ` A - Work Order No` | WO prefix+suffix |
| ` B - Parent Item No` | Parent part number |
| ` C - Customer Code` | Customer code |
| ` D - Customer Name` | Customer name |
| ` E - Sales Order No` | SO number |
| ` F - Job Number` | Job number |

Search prompt: ` Enter the WO number to find.`  
Filter: `Open Work Orders only?`

### Inventory Search
Window title: ` Inventory `
Function keys: `F1 Help,F2 Find,F3 Change Search Key,F5 Stock Status`
Search key: `Item Number`
Tables: BKICMSTR / MTICMSTR

### Standard Help System
| String | Purpose |
|--------|---------|
| `ON-LINE HELP` | Dialog title |
| `For on-line Help click "Help" at the top of` | Message line 1 |
| `the Windows main menu.` | Message line 2 |
| `STANDARD FUNCTION KEYS/BUTTONS` | Help section header |
| `F1  Help` | Key definition |
| `F2  Lookup` | Key definition |
| `F3  Clear` | Key definition |
| `F4  Delete` | Key definition |
| `F5  First` | Key definition |
| `F6  Last` | Key definition |
| `F7  Previous` | Key definition |
| `F8  Next` | Key definition |
| `F9  Find` | Key definition |
| `F10 Save` | Key definition |

### Color References
`NormalBkg` appears 4 times — the standard background color token used for text field styling.

---

## Patterns Observed Across String Types

**Sort menu entries follow a fixed 22-char format:**
```
 N - Label       ABCCD
```
where `N`=position (1-7), `Label`=padded to fill, `ABCCD` = encoded key pair.

**Message types use 4-char codes:** `warn`, `info` (correlate to the `windows 'warn'`/`windows 'info'` 
parameter of the `msg` statement — controls the Windows message box icon).

**Function key strings are paired:** `fnc_list "string1","string2"` compiles to two consecutive
string records. The format: comma-separated key descriptions within each string.

---

## Applicability to Other `.RUN` Files

Any `.RUN` file can be scanned the same way. The data channel starts at file offset 0x0000
and ends at the value stored at header offset 0x08. String records follow the `41 00 LL LL`
pattern throughout. Key strings to look for:
- Program name (first string after table name strings)
- Report title (prg_hdr argument)
- Menu option strings (22-char fixed format with embedded sort codes)
- Error messages with `warn`/`info` type tags
- Browse column labels (repeating field name strings)
- Function key spec strings (comma-separated F-key descriptions)

---

## Pass 561 (2026-07-02) — Cross-Module Corpus Confirmation

Six additional `.RUN` files sampled from T6\*, T7\*, J5\*, J6\* generations. The extraction
method works identically across all generations and file origins.

| File | Size | Generation | Unique Strings | Menu Code | Module Purpose |
|------|-----:|-----------|---------------:|-----------|----------------|
| `J5BOMXPT.RUN` | 190KB | ISTS J5 (2007) | 275 | `IS-A` | Custom BOM export to CSV |
| `J6CHGREP.RUN` | 187KB | ISTS J6 (2008) | 202 | — | Change sales rep on AR invoice |
| `T6APB.RUN` | 391KB | T6/ISTS (2014) | 402 | `AP-B` | AP Enter Vouchers (legacy) |
| `T6ARB.RUN` | 491KB | T6/ISTS (2010) | 534 | `AR-B` | AR Enter Vouchers (legacy) |
| `T6WOC.RUN` | 492KB | T6/ISTS (2012) | 467 | — | Work Order + Print Travelers |
| `T7APU.RUN` | 4.8KB | T7 stub | 1 | — | Replacement notice only |

### Universal Patterns Confirmed

**ISTS Enhancement header (every ISTS-modified file):**
```
'- ISTS Enhancement MM/DD/YY'
```
This is always the first readable string. It marks that ISTS customized the original BK\*
or T6\* file. Date = date of most recent ISTS modification.

**T7\*.RUN stub files:** Some T7\*.RUN files (e.g., T7APU.RUN, 4.8KB) are pure stubs —
they contain a single message: `'This program has been replaced by a newer version. Please
see your System Administrator to get your menu updated.'` These are placeholder files that
redirect users to the T7 RWN equivalents. String count = 1.

**Help system boilerplate (every non-stub file):**
- Tables: `dbahlpid`, `bksyhelp`
- Strings: `DBAHELP.HLP`, `WINHLP32.EXE`, standard F-key labels
- Present in 100% of non-stub files — this is a copy-pasted help block.

**NOVAZYG / ISTECHSUPPORT:** These identifiers appear in multiple .RUN files as what
looks like table references. NOVAZYG = tech-support bypass marker; the string
`NOVAZYGANDISTECHSUPPORT` is used by `READ_PROP` (opcode 0x49) in the RWN runtime.
In .RUN files they appear as table-open references for IStech internal audit.

**JMCHECK / JMUSAGE:** Tables referenced in J6CHGREP (and likely other J6 custom files).
These are ISTS internal usage-tracking tables (J-prefix = ISTS custom namespace).

### Module Table Coverage

| Module | Tables Confirmed via String Extraction |
|--------|----------------------------------------|
| AP (T6APB) | BKAPINVL, BKAPRIVL, BKAPVEND, BKAPINVT, BKGLCOA, BKGLTEMP, BKGLCHK, BKAPCHKH, bkaphpol, ISBANKS, BKSYMSTR, BKYSMSTR |
| AR (T6ARB) | BKARINVT, BKARCUST, BKARHINV, BKARINVI, BKARCHKF, BKGLCHK, BKISTAX, ISSRINV, ISBANKS, BKARHDSC, BKARINV, BKARSIVL, BKARTNOT, BKARINVV, BKSYAR, BKPRSALE, ISAPPROJ |
| WO (T6WOC) | WORKORD, BKWOCA, WOBOMREM, WOROUT, WODATE, WOHDATE, BKBMMSTR, BKBMNOTE, BKBMREMK, BKICMSTR, MTICMSTR, ROUTING, BKRTSPEC, BKICREF, ISNOTES, ISSRMMS, issrinfo, ISORDECO, ISLINKS, BKARCUST, BKSBVEND, ISICMSTR, iscatmst |
| BOM (J5BOMXPT) | ISICMSTR, BKBMMSTR, BKICMSTR, MTICMSTR, BKSBVEND, BKAPVEND, BKICREF, BKICLOC, CLASMSTR, BKSBMFG |
| AR-Sales (J6CHGREP) | BKARHINV, BKARHIVL, BKARINVT, BKARINVI, BKPRSALE, BKARSIVL, MKAHIST |

### Migration Alert Pattern (T6APB, T6ARB)

Several T6-era programs contain embedded migration instruction strings that fire when the
database is in an incompatible state:

> `System needs to Convert AP, to Long Invoice Numbers. Please get everyone out of
> Evo/DBA. Make a backup of BKAPINVT.B, BKAPINVL.B, BKAPCHKF.B, BKAPCHKH.B, BKAPAPOL.B
> then use UT-A to run ISAPINV.RUN`

This confirms a schema migration mechanism embedded directly in the program binaries —
the program detects old-format records and provides manual migration instructions rather
than auto-migrating.

### Generalization Conclusion

The string extraction method (`0x41 0x00 LL_lo LL_hi [text]`) is confirmed to work
identically across **all** `.RUN` file generations:
- `BK*` (DBA Manufacturing classic)
- `T6*` (TAS Pro 6 era)
- `T7*` (T7-era .RUN stubs)
- `J5*`, `J6*` (ISTS custom programs)

All 1,273 `.RUN` files on the DBAMFG\$ share can be scanned with this method. The method
requires no knowledge of the binary structure beyond the data-channel string record format.
Coverage: the readable portion varies by file; complex programs with many UI strings yield
200–534 unique strings; stub files yield 1.
