# TAS Pro 6 `.RUN` File Format — Bytecode Analysis

Status: **partial** — file structure confirmed; opcode table in progress

Last updated: 2026-06-15

---

## Overview

`.RUN` files are compiled TAS Professional 6 programs. They are unencrypted.
Analysed via Rosetta Stone: 7 `.SRC` source + `.RUN` binary pairs in
`samples/rosetta/`. Primary sample: `BKAWLB.RUN` (139,533 bytes) paired with
`BKAWLB.src` (24,953 bytes).

---

## File Layout (confirmed from BKAWLB.RUN)

```
Offset  Size   Description
------  ----   -----------
0x00    0x34   File header (13 × 4-byte LE fields; see table below)
0x34    0x01   Padding (0x00)
0x35    0x05   Magic: "TAS32"
0x3A    0x01   Compiler version byte (BKAWLB=0x71, BKMRF.org2=0x58, BKMRF.TEST=0x51)
0x3B    0x45   Compiler metadata (zero-padded)
0x80    N×16   Table name slots: each slot is 8-char ASCII name, 8 null bytes
               (N determined by header; up to 30 slots observed)
0x80+N×16 M   Variable storage — pre-zeroed at load time (size = header[0x18])
...           Code + string pool — immediately follows variable storage
```

The code/data section begins at `0x80 + (number_of_table_slots × 16) + header[0x18]`.
For BKAWLB.RUN: `0x80 + (30 × 16) + 0x5A0 = 0x80 + 0x1E0 + 0x5A0 = 0x6C0`.

---

## Header Fields (offsets 0x00-0x33, all LE 32-bit)

| Offset | Value (BKAWLB) | Hypothesis |
|--------|---------------|-----------|
| 0x00   | 0x38D9 = 14553 | Unknown — may be entry point offset or code size |
| 0x04   | 0x105A2 = 66978 | Unknown section offset |
| 0x08   | 0x923E = 37438 | Unknown |
| 0x0C   | 0x1C4 = 452 | var_table_size (inferred) |
| 0x10   | 0xA = 10 | Unknown count |
| 0x14   | 0x17F = 383 | Unknown |
| 0x18   | 0x5A0 = 1440 | Variable storage size in bytes |
| 0x1C   | 0x1E = 30 | Table slot count (max slots allocated) |
| 0x20   | 0x47D0 = 18384 | Unknown offset |
| 0x24   | 0xFFFF = 65535 | Sentinel / max value |
| 0x28   | 0x5316 = 21270 | Unknown |
| 0x2C   | 0x0 = 0 | Zero |
| 0x30   | 0x1A4 = 420 | Unknown |

---

## Table Name Slots (0x80+)

Up to 30 slots; each slot is 16 bytes: 8-byte ASCII table name + 8 null bytes.
Empty slots are all-zero. Order matches the #LIB includes and `open` statements,
with library tables appearing after user tables.

BKAWLB.RUN table slots (in slot order):
```
slot[ 0] 0x0080: BKSYMSTR
slot[ 1] 0x0090: WORKORD
slot[ 2] 0x00A0: BKICMSTR
slot[ 3] 0x00B0: BKARCUST
slot[ 4] 0x00C0: BKSYHELP   (from #LIB)
slot[ 5] 0x00D0: DBAHLPID   (from #LIB)
slot[ 6] 0x00E0: TASCOLOR   (from #LIB LOOKUPS)
slot[ 7] 0x00F0: MTICMSTR
slot[ 8] 0x0100: CLASMSTR
slot[ 9] 0x0110: BKSBVEND
slot[10] 0x0120: BKSBMFG
slot[11] 0x0130: BKICREF
slot[12] 0x0140: BKICLOC
slot[13] 0x0150: BKSYPRTR
```

**Key finding:** Table names appear AGAIN in the code section as inline strings.
The runtime resolves table names at runtime via string lookup, not by table slot index.

---

## Variable Storage Region

All zero in the file. Runtime pre-initializes variables here.
Size = header[0x18] (1440 bytes in BKAWLB). Immediately follows the table slot area.

---

## Code + String Pool

Starts at offset 0x6C0 in BKAWLB. Dense binary instruction stream. No section boundary
between code and string data — strings are embedded inline as PUSH_VALUE instructions.

### Byte Distribution (BKAWLB.RUN, full file)

| Byte | Count | %    | Note |
|------|-------|------|------|
| 0x00 | 67098 | 48.1% | Zero padding (addresses, variable storage) |
| 0x20 | 7751  | 5.6%  | Space char (frequent in string data) |
| 0x41 | 3353  | 2.4%  | PUSH_VALUE opcode |
| 0x46 | 3140  | 2.3%  | LOAD_VAR opcode |
| 0x4E | 2301  | 1.6%  | ARRAY_IDX opcode |

---

## Known Opcodes (confirmed from BKAWLB.SRC vs BKAWLB.RUN correlation)

All arguments are little-endian.

| Opcode | Name | Arg bytes | Evidence |
|--------|------|-----------|---------|
| `0x41` | PUSH_VALUE | `0x00 LL LL data[LL]` | String literals match source; table names passed as strings; 'X', 'Y', 'C' etc. match assignments |
| `0x46` | LOAD_VAR | `ADDR4` | Precedes array element assignments with repeating address patterns |
| `0x4E` | ARRAY_IDX | `IDX4` | Follows LOAD_VAR for array assignments; IDX increments per element |
| `0x0A` | PUSH_ADDR | `ADDR4` | Seen before `0x0F 0x00` pairs in MENU_HLDR area |
| `0x0F` | OP_0F | `0x00` | Appears after PUSH_ADDR; purpose unknown |
| `0x4B` | CALL? | `0x00 ADDR4` | Appears for function-call-like constructs |
| `0x49` | PUSH_VAR? | `0x00 0x00 ADDR4` | Appears before string concat (e.g., prg.name + string) |
| `0x35` | FIELD_REF? | `ADDR4` | Appears in string pool area |

### PUSH_VALUE detail (`0x41`)

```
41 00 LL_lo LL_hi [LL bytes of data]
```

Used for BOTH plain string literals AND compiled expression blobs. The data can be:
- Printable ASCII: a literal string from source (e.g., `'AW-L-B'`, `'Sort by'`)
- Binary: a compiled sub-expression (e.g., form layout spec, mask definition)
  Binary blobs often start with `fd` and end with `ff`.

String sequence in BKAWLB matches source code in order:
```
Source: prg.name = "AW-L-B"
Binary: 41 00 06 00  41 57 2d 4c 2d 42               ("AW-L-B", 6 bytes)

Source: open BKARCUST lock N  (table name passed as string)
Binary: 41 00 08 00  42 4b 41 52 43 55 53 54          ("BKARCUST", 8 bytes)

Source: sort_by_text = 'Start Date '
Binary: 41 00 0b 00  53 74 61 72 74 20 44 61 74 65 20  ("Start Date ", 11 bytes)

Source: e.status[1] = 'X'
Binary: 41 00 01 00  58                               ("X", 1 byte)

Source: inc.all.class = 'Y'
Binary: 41 00 01 00  59                               ("Y", 1 byte)

Source: prg_hdr prg.name+'  Print Work Order Schedule'
Binary: 41 00 1b 00  2020...                          ("  Print Work Order Schedule", 27 bytes)
```

---

## TAS Pro 7 vs TAS Pro 6 — Key Differences

| Feature | TAS Pro 6 `.RUN` | TAS Pro 7 `.RWN` (decrypted) |
|---------|-----------------|------------------------------|
| Magic bytes | "TAS32" at offset 0x35 | None — no plaintext header |
| Encryption | None | Twofish-192-CFB (IV from heap) |
| String pool | Inline (`41 00 LL LL data`) | Absent — externalized to `.DCY` |
| Table names | In header table + inline strings | Externalized (assumed `.DCY`) |
| Variable storage | Zero block in file | Absent from file |
| Byte distribution | 48% zeros, biased | Uniform ~0.5% per byte |
| `0x41` opcode | Frequent (PUSH_VALUE) | Not seen in suwin7.rwn |

The **uniformly distributed byte distribution** of TAS Pro 7 decrypted bytecode is
confirmed correct — it results from having no zero padding (variable storage externalized)
and no ASCII strings (externalized to .DCY). The decryption is verified correct.

---

## Batch Decrypt Results (2026-06-15)

- Files scanned: 1,145 `.RWN` files from `\\i2s109-solidcrm\DBAMFG$\` (all subdirs)
- OK: 1,144 (99.9%)
- FAIL: 1 — `t6ine1.RWN` starts with `TPF0` (binary Delphi form, misnamed .RWN)
- Output: `samples/rwn_decrypted/` (1,122 unique files, ~283 MB, gitignored)
- Summary CSV: `samples/rwn_decrypted/decrypt_summary.csv`

---

## BKMRF Variants (same source, different compile)

`samples/rosetta/` contains three binaries from the same source:
- `BKMRF.RUN` — 159,375 bytes, version byte 0x?? (full linked)
- `BKMRF.org2` — 89,175 bytes, version 0x58 (earlier/partial)
- `BKMRF.TEST` — 85,898 bytes, version 0x51 (test compile)

These can be byte-diffed to identify which bytes are stable (opcode values) vs.
variable (addresses that change between compiles). Planned for next analysis pass.

---

## References

- Source: `samples/rosetta/BKAWLB.src`
- Binary: `samples/rosetta/BKAWLB.RUN`
- Analysis script: `scripts/tas6_analyze.py`
