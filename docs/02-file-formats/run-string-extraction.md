# TAS Pro 6 `.RUN` String Data Extraction

Status: **verified** — extraction method confirmed; BKAWLB fully cataloged (Pass 245)

Last updated: 2026-06-24

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
