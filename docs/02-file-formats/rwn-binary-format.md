# `.RWN` Binary Format (TAS Pro 7 Compiled Program)

Status: partial — header confirmed, symbol tables confirmed, bytecode opcodes C:15/100
Last updated: 2026-06-16

---

## Overview

`.RWN` files are TAS Pro 7 compiled programs, encrypted with Twofish-192-CFB-128 (key K_B).
After decryption (see `decryption-findings.md`), the plaintext is a structured binary with:

- A 128-byte header
- A file reference table
- Zero-padding
- A dispatch / jump table (8-byte entries)
- A string constant pool
- Bytecode
- A procedure symbol table
- A source filename record
- A variable symbol table

**Critical finding (2026-06-16)**: procedure names, variable names, and the source filename are all
stored as plaintext in every RWN file. They can be extracted without bytecode disassembly.

---

## Format Marker

At decrypted offset **0x35**: the 5-byte ASCII string **`TWINB`** (TAS Windows B).
This is the TAS Pro 7 equivalent of `TAS32` at offset 0x35 in `.RUN` (TAS Pro 6) files.

```
Offset  Content
0x34    0x01 (prefix / version byte)
0x35    "TWINB" (5 bytes)
0x3A    varies
```

---

## File Layout (decrypted)

```
Offset      Size                    Content
──────────  ──────────────────────  ───────────────────────────────────────────────────
0x000       128 bytes               Header (32 DWORDs — see below)
0x080       var×16 bytes            File reference table (16-byte null-padded entries)
var         1×16 bytes              Table terminator (all-zero entry)
var         padding to align        Zero padding
0x6C0*      hdr[0x00] bytes         Dispatch / jump table (8-byte entries)
var         var                     String constant pool
var         var                     Bytecode instructions
end-proc    hdr[0x0C] bytes         Procedure symbol table (53-byte records)
end-proc    60 bytes                Source filename (space-padded to 60 bytes)
end-src     hdr[0x20] bytes         Variable symbol table (77-byte records)
```

*Dispatch table starts at 0x6C0 in every file examined (likely fixed offset).

---

## Header (bytes 0x00–0x7F)

| Offset | Value (suwin7) | Value (T7INA) | Meaning (confirmed) |
|--------|----------------|---------------|---------------------|
| 0x00   | 0x0000_0118 = 280   | 0x0001_2358 = 74,584 | Dispatch table size (bytes) |
| 0x04   | 0x0000_02AC = 684   | 0x0003_B825 = 243,749 | Unknown |
| 0x08   | 0x0000_01C7 = 455   | 0x0002_47D4 = 149,460 | Unknown |
| 0x0C   | 0x0000_009F = 159   | 0x0000_48E0 = 18,656 | Procedure table size (bytes); = proc_count × 53 |
| 0x10   | 0x0000_0000 = 0     | 0x0000_0000 = 0       | Unknown (always 0?) |
| 0x14   | 0x0000_0044 = 68    | 0x0000_0F4D = 3,917   | **Variable count** |
| 0x18   | 0x0000_120C = 4,620 | 0x0000_120C = 4,620   | Unknown (same in both — likely a compiler version constant) |
| 0x1C   | 0x0000_003C = 60    | 0x0000_003C = 60      | Source filename block size = 60 (always) |
| 0x20   | 0x0000_1474 = 5,236 | 0x0004_9A29 = 301,609 | **Variable table size** (= var_count × 77) |
| 0x24   | 0x0000_FFFF         | 0x0007_D000           | Unknown |
| 0x30   | 0x0000_003C = 60    | 0x0000_0168 = 360     | Unknown |
| 0x34   | 0x01 "TWINB"        | 0x01 "TWINB"          | Format marker (always) |

**Derived values:**
- `proc_count = hdr[0x0C] / 53`
- `var_count = hdr[0x14]`
- `var_table_size = hdr[0x20]` (should equal `var_count × 77`)
- Variable table offset from file end: `len(data) - hdr[0x20]`
- Source filename offset: `len(data) - hdr[0x20] - 60`
- Procedure table offset: `len(data) - hdr[0x20] - 60 - hdr[0x0C]`

---

## File Reference Table (offset 0x80)

Same structure as `.RUN` files:

```
Offset 0x80: first entry (16-byte ASCII null-padded name)
Offset 0x90: second entry
...
Offset N:    all-zero 16-byte entry (terminator)
```

Each name corresponds to a `open <NAME> lock N` statement in TAS Pro 7 source.
Names are uppercase and padded with spaces and nulls to exactly 16 bytes.

**Example from T7INA.RWN (53 database files):**
BKICMSTR, CLASMSTR, MTICMSTR, ISICMSTR, ISITP, BKARCUST, BKAPVEND, BKAPDESC,
BKPSUSER, BKYSMSTR, ISUDFINV, ISREPLNK, BKICLOC, BKICLOCM, ISNOTES, ISLINKS,
ISECO, BKAPPOL, BKAPPO, WOBOM, WORKORD, BKMRPFC, BKBMMSTR, MTMRP, ISGLDATE,
INVTXN, ISUSAGE, BKSBMFG, BKSBVEND, ISBINLOC, ROUTING, BKARINV, BKSBPART,
BKICPMAT, BKSYHELP, DBAHLPID, ISIS, ISLOG, ISDRILL, ISACCESS, LANGDICT,
BKCMACCN, ISNTYPE, BKARINVL, MKAHIST, BKSYMSTR, BKGLTRAN, DBAFIFO, ISTRIGRS,
ISREMIND, LOT, SERIAL, ISNCR.

---

## Dispatch Table (offset 0x6C0)

Structure: 8-byte entries, `[4-byte DWORD A] [4-byte DWORD B]`.
DWORD B increases monotonically — likely byte offsets into the bytecode/data section.
DWORD A encodes an opcode byte (in byte 0) + type/flag bytes.

**Observed first-DWORD values in suwin7.rwn:**

| DWORD A (little-endian) | Opcode byte (byte 0) | Count | Meaning (unconfirmed) |
|-------------------------|---------------------|-------|----------------------|
| 0x0A00_000F             | 0x0F                | 13    | Unknown opcode 0x0F  |
| 0x1400_003B             | 0x3B                | 6     | Unknown opcode 0x3B  |
| 0x0400_0042             | 0x42                | 9     | Unknown opcode 0x42  |
| 0x0500_0020             | 0x20                | 3     | Unknown opcode 0x20  |
| 0x0900_0043             | 0x43                | 1     | Unknown opcode 0x43  |
| 0x0400_0045             | 0x45                | 1     | Unknown opcode 0x45  |
| 0x05FE_0057             | 0x57                | 1     | Unknown opcode 0x57  |

---

## String Constant Pool

Follows immediately after the dispatch table. Format:

```
[type_byte=0x41] [0x00] [uint16 LE length] [ASCII chars]
```

Each entry is variable-length. `0x41` = the type marker for string constants.

**Example from suwin7.rwn:**
- `41 00 0A 00 "SUWIN7.DFM"` → 10-char string
- `41 00 21 00 "THISSHOULDREALLYFUCKRICKATKISONUPA"` → 33-char string (developer comment)
- `41 00 04 00 "DEMO"` → 4-char string

---

## Procedure Symbol Table

Located at `len(data) - hdr[0x20] - 60 - hdr[0x0C]`.
Entry size: **53 bytes**.
Entry count: `hdr[0x0C] / 53`.

**Entry structure:**
```
Byte 0:      name length (Pascal short string length byte)
Bytes 1–15:  procedure name, null-padded to 15 bytes (max 15-char name)
Bytes 16–52: metadata (37 bytes — offsets, flags, counts; not fully decoded)
```

**Name availability varies by compilation source:**

| Source type | Procedure names available? | Example modules |
|-------------|---------------------------|-----------------|
| Compiled from `.SRC` | ✅ Yes | suwin7.rwn, EvoDCmenu.RWN, evoDCs.RWN |
| Compiled from `LISTG60.LIB` | ❌ No (byte 0 = 0x00) | T7INA.RWN (352 procs), T7APM.RWN (105 procs) |
| Compiled from `NZLICE.LIB` | ⚠️ Partial / garbled | T7WOM.RWN |

When procedure names ARE present (SRC-compiled), each entry uses a Pascal short string at byte 0:

**Example from suwin7.rwn (SRC-compiled):**
| # | Name         | Length | Note |
|---|--------------|--------|------|
| 0 | START        | 5      | byte[0]=0x05 = length |
| 1 | DOCOUNTDOWN  | 11     | byte[0]=0x0B = length |
| 2 | GETSERIALNUM | 12     | byte[0]=0x0C = length |

---

## Source Filename Record

60-byte space-padded ASCII string immediately before the variable table.
Contains the original TAS Pro 7 `.SRC` filename used to compile the program.

**Examples:**
- suwin7.rwn → `"suwin7.src"` (padded to 60 bytes with spaces)
- T7INA.RWN → expected `"T7INA.SRC"` (not yet verified)

---

## Variable Symbol Table

Located at `len(data) - hdr[0x20]`.
Entry size: **77 bytes**.
Entry count: `hdr[0x14]`.

**Entry structure:**
```
Bytes 0–14:  15-byte name field (space-padded).
             Byte 0 is EITHER:
               - Non-printable (< 0x20): a compiler type-category code; name starts at byte 1.
                 0x05 = compiler-generated temp variable (TEMP0–TEMPn).
               - Printable ASCII: the first character of the variable name; name spans bytes 0–14.
             All user-declared named variables have printable byte 0 (= first letter of name).
Byte 15:     null terminator (0x00)
Bytes 16–76: metadata (61 bytes — type code, size, array info, etc.; not fully decoded)
```

**Example from suwin7.rwn (68 variables):**

| Type | Name(s) | Note |
|------|---------|------|
| 0x05 | TEMP0–TEMP59 | Compiler-generated temporaries; 60 vars |
| C    | CURR_TIME    | User-declared; 'C' is first char AND at byte 0 |
| W    | WAIT_SECS    | |
| S    | SERIALNUMBER, SNVALUE | |
| D    | DUMMY_L      | |
| I    | I            | Single-char variable |
| M    | MUCHAR       | |
| L    | LICTYPE      | |

Variable count for T7INA.RWN: **3,917 variables** (DWORD[0x14] = 0x0F4D).

---

## Confirmed Facts

| Claim | Confidence | Evidence |
|-------|-----------|---------|
| Format marker "TWINB" at offset 0x35 | 100/100 | Both suwin7.rwn and T7INA.RWN |
| File table at offset 0x80, 16-byte entries | 100/100 | Confirmed by matching .SRC open statements (BKAWLB.SRC ↔ .RUN format) |
| Header[0x14] = variable count | 100/100 | suwin7: 68 variables, header[0x14]=68 |
| Header[0x20] = variable table byte size | 100/100 | suwin7: 68×77=5236=0x1474=header[0x20] |
| Header[0x0C] = procedure table byte size | 95/100 | suwin7: 3 procs × 53 bytes = 159 = header[0x0C] |
| Variable entry size = 77 bytes | 100/100 | Spacing between TEMP0/TEMP1 names confirmed = 77 |
| Variable name: non-printable byte 0 = type code, name at bytes 1–14 | 100/100 | All TEMP* vars have byte 0 = 0x05; name verified |
| Variable name: printable byte 0 = first char of name, name spans bytes 0–14 | 100/100 | CURR_TIME, WAIT_SECS, I, LICTYPE all verified |
| Procedure entry size = 53 bytes | 95/100 | Spacing between START/DOCOUNTDOWN/GETSERIALNUM = 53 |
| Source filename = 60 bytes before var table | 100/100 | "suwin7.src" found at expected offset |
| Procedure names are plaintext in binary | 100/100 | Direct observation |
| Variable names are plaintext in binary | 100/100 | Direct observation |
| Dispatch table starts at 0x6C0 | 80/100 | Both examined files; may be derived from file table size |
| Header[0x00] = dispatch table size | 80/100 | suwin7: header[0x00]=280, 0x6C0+280=0x7D8=string pool start |
| TAS32 (old hypothesis) present in decrypted RWN | WRONG | Old analysis used sha1("mabufoju") key; TAS32 not present with correct key K_B |

---

## Extractor Script

See `scripts/rwn_extract_symbols.py` for a script that extracts procedure names,
variable names, and the source filename from any decrypted RWN file.
