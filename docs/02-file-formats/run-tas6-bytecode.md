# TAS Pro 6 `.RUN` File Format — Bytecode Analysis

Status: **partial** — instruction format confirmed C:35/100; opcodes in progress

Last updated: 2026-06-19

---

## Overview

`.RUN` files are compiled TAS Professional 6 programs. They are unencrypted.
Analysed via Rosetta Stone: 7 `.SRC` source + `.RUN` binary pairs in
`samples/rosetta/`. Primary sample: `BKAWLB.RUN` (139,533 bytes) paired with
`BKAWLB.src` (24,953 bytes).

---

## File Layout (confirmed from BKAWLB.RUN)

```
Offset              Size   Description
------              ----   -----------
0x00                0x34   File header (13 × 4-byte LE fields; see table below)
0x34                0x01   Padding (0x00)
0x35                0x05   Magic: "TAS32"
0x3A                0x01   Compiler version byte (BKAWLB=0x71, BKMRF.org2=0x58)
0x3B                0x45   Compiler metadata (zero-padded)
0x80                N×16   Table name slots: 8-char ASCII name + 8 null bytes (N = h[7])
0x80 + N×16         M      Var section (size = h[6]):
                             [0 .. runtime_base-1]: zero-initialized runtime var storage
                             [runtime_base .. M-1]: var descriptor table (see below)
0x80 + N×16 + M     2      Code section preamble (2 bytes; value = 0 for BKAWLB)
0x80 + N×16 + M + 2 ...    Instruction stream (7-byte fixed-length instructions)
   ...later in code section: inline string pool (41-tagged entries)
```

**code_start formula (confirmed):**
```
code_start = 0x80 + (h[7] × 16) + h[6]
```
For BKAWLB.RUN: `0x80 + (30 × 16) + 0x5A0 = 0x80 + 0x1E0 + 0x5A0 = 0x800`.

> **NOTE — previous doc error:** an earlier version of this document stated code_start=0x6C0
> for BKAWLB, which was incorrect. The correct value is 0x800. The 0x6C0 value corresponds
> to where the var descriptor table begins (0x0260 + 0x0460 = 0x06C0), not code_start.

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

## Var Section Layout (confirmed from BKAWLB.RUN)

The var section (h[6]=1440 bytes) has two sub-regions:

```
var_section offset  Contents
------------------  --------
0x0000 – 0x045F     Runtime variable storage (1120 bytes, all zeros in file)
                    At load time, these bytes hold actual variable values.
                    The runtime_base threshold 0x0460 appears fixed across programs.
0x0460 – end        Var descriptor table (320 bytes in BKAWLB)
                    Variable-size entries, one per user variable.
                    At LOAD TIME this is read by the runtime to set up var types/sizes.
                    At RUNTIME these bytes may be overwritten by variable data for
                    vars with runtime_offset >= 0x0460.
```

### Var Descriptor Entries (confirmed from BKAWLB — 45 entries, 7 bytes each)

Entries are EXACTLY 7 bytes each (verified: all 45 cumulative offsets hold). Format:

```
Byte  Field           Notes
[0]   type_tag        Variable type code (e.g. 0x4B=alpha, 0x71=?, 0x3B=?, 0x0F=?, 0x1F=?)
[1]   0x00            Always zero (padding)
[2]   b2              Runtime storage size in bytes for this variable
[3-6] runtime_offset  LE4 = sum of all previous b2 values = byte offset in runtime var pool
```

Confirmed entry sequence for BKAWLB (45 entries starting at var_section[0x0460], abs file 0x06C0):

| Entry# | Desc pos | Hex | type | b2 | off | Cumulative |
|--------|----------|-----|------|----|-----|------------|
| 0 | desc+0x0000 | `4B 00 09 00 00 00 00` | 0x4B | 9 | 0 | param cfrom (a size 8) |
| 1 | desc+0x0007 | `71 00 05 09 00 00 00` | 0x71 | 5 | 9 | param prg.name (a size ?) |
| 2 | desc+0x000E | `3B 00 14 0E 00 00 00` | 0x3B | 20 | 14 | var 3 (size 20) |
| 3 | desc+0x0015 | `0F 00 0A 22 00 00 00` | 0x0F | 10 | 34 | var 4 (size 10) |
| 4 | desc+0x001C | `1F 00 35 2C 00 00 00` | 0x1F | 53 | 44 | var 5 (size 53) |
| 5..8 | desc+0x0023.. | type=0x1F b2=53 | 0x1F | 53 | 97,150,203,256 | vars 6..9 |
| 38 | desc+0x0103 | `0E 00 61 B1 02 00 00` | 0x0E | 97 | 689 | array element (b2=97) |
| 38..41 | desc+0x0103.. | type=0x0E b2=97 | 0x0E | 97 | 786,883,980 | array elements |
| 44 | desc+0x0134 | `37 00 0A 4C 04 00 00` | 0x37 | 10 | 1100 | last var |

Total runtime storage = 1110 bytes; 45 × 7 = 315 bytes for descriptor table.

**runtime_base varies** (NOT always 0x0460):
- Programs with var_size=1440, table_count=30: runtime_base=0x0460=1120 (BKAWLB, BKLME)
- Programs with var_size=2640, table_count=55: runtime_base=0x02D0=720 (BKMRF, BKDCA, BKAPH, BKAPHA, BKROA)
- Formula: `runtime_base = var_size - (num_user_vars × 7)` where the zero-init area holds SYSTEM/LIBRARY variables not listed in the descriptor table. The descriptor table covers ONLY user-declared variables.
- runtime_base is NOT directly stored in a header field (no header field matches across all 6 programs tested).

### Instruction Address Semantics for Var References

For var-section instructions, `addr` = the variable's **runtime address** = runtime_base + its runtime_offset:

```
addr = runtime_base + cumulative sum of all preceding variables' b2 values
```

Example (BKAWLB):
```
var[0] (cfrom, off=0):    addr = 0x0460 + 0   = 0x0460  → instruction [i0]
var[1] (prg.name, off=9): addr = 0x0460 + 9   = 0x0469  → instruction [i1]
var[2] (off=14):          addr = 0x0460 + 14  = 0x046E  → instruction [i2, i3]
```

For **array elements**, the addr is computed directly by the compiler as:
```
addr = addr_of_first_element + n × element_size
```
Instructions [i4..i7] reference addrs 0x04CF, 0x0530, 0x0591, 0x05F2 = 0x046E + 97, 194, 291, 388 (stride 97 = b2 of the instruction, matching element size). These hit positions within the runtime pool that are NOT at descriptor entry boundaries — the runtime computes element locations via stride, not by separate descriptor entries per element.

---

## Code Section

### Preamble

Two bytes at code_start. Value varies per program:
- BKAWLB.RUN: `00 00`
- BKMRF.RUN: `04 2E` (= 0x2E04 LE = 11780)
- BKDCA.RUN: `1D E9` (= 0xE91D LE = 59677)

The non-zero values for BKMRF/BKDCA may indicate an **inline data section** of that many
bytes before the instruction stream. BKMRF instructions have been confirmed at
abs=0x3C4A (offset +11786 from code_start), consistent with preamble=11780.

### Instruction Format (CONFIRMED, 7 bytes, BKAWLB)

```
Byte  Field      Notes
----  -----      -----
[0]   opcode     Operation code
[1]   0x00       Always zero (padding or reserved)
[2]   b2         Sub-opcode / type qualifier / operand size hint
[3-6] addr LE4   4-byte LE address field
```

All instructions are **exactly 7 bytes**. Confirmed for BKAWLB; same format implied for
BKMRF/BKDCA (brute-force scan found 100% b1=0x00 alignment at +2 from code_start for all).

Instructions start at **code_start + 2** for BKAWLB (after the 2-byte preamble).
For BKMRF/BKDCA, the instruction stream likely starts at a higher offset (after an inline
data section).

### Confirmed instruction sequence from BKAWLB (first 30 instructions)

```
[i 0] 0x4B b2=0x09  addr=0x0460  (var[0]: cfrom α8, type_tag=0x4B)
[i 1] 0x20 b2=0x05  addr=0x0469  (var[1]: prg.name α6?, type_tag=0x05)
[i 2] 0xC1 b2=0x00  addr=0x046E  (var[2], same as i3)
[i 3] 0x0E b2=0x61  addr=0x046E  (var[2], 97-byte entry)
[i 4] 0x0E b2=0x61  addr=0x04CF  (var[3] = var[2]+97)
[i 5] 0x0E b2=0x61  addr=0x0530  (var[4] = var[3]+97)
[i 6] 0x0E b2=0x61  addr=0x0591  (var[5] = var[4]+97)
[i 7] 0xC0 b2=0x04  addr=0x05F2  (var[6] = var[5]+97)
[i 8] 0x49 b2=0x09  addr=0x05F6  (var[7], 4 bytes after var[6])
[i 9] 0x3B b2=0x14  addr=0x05FF  BRANCH family (same as RWN opcode 0x3B)
[i10] 0x0F b2=0x0A  addr=0x0613  ASSIGN (same as RWN opcode 0x0F)
[i11] 0x45 b2=0x05  addr=0x061D
[i12] 0x48 b2=0x19  addr=0x0622
```

### Branch / code-reference instructions

When `addr >= code_start`, the addr is a **code branch target** (absolute file offset).
Seen for: 0x3B (branch), 0x0E (with higher addrs), and others.

Example: `0x0E b2=0x61 addr=0x0083E` where 0x083E > code_start=0x0800.

---

## Inline String Pool (in code section)

String literals are embedded in the code section using a tagged format:

```
41 00 LL_lo LL_hi [LL bytes of string data]
```

These are NOT 7-byte instructions — they are **data records** that appear within the
code section at addresses referenced by instructions. For BKAWLB, the first string
`'AW-L-B'` appears at abs=0x03FCB (rel_code=0x37CB), after thousands of instructions.

### First instruction — fixed runtime init

The first instruction of every observed `.RUN` file is opcode 0x4B:

- BKMRF.RUN / .org2 / .TEST: `4B 00 09 00 00 00 00` (addr=0 = system runtime base)
- BKAWLB.RUN: `4B 00 09 60 04 00 00` (addr=0x0460 = user var section base)

`b2=0x09` is consistent across all files. This instruction likely **initializes the variable
storage area** — 0x4B is the type_tag for the first user variable (cfrom alpha-8), and
addr points to the start of the user var descriptor table.

Header field h[4]=10 in every tested file; b2=9 = h[4]-1. Possibly encodes TAS Pro API version.

### Byte Distribution (BKAWLB.RUN, full file)

| Byte | Count | %    | Note |
|------|-------|------|------|
| 0x00 | 67098 | 48.1% | Zero padding (addresses, variable storage) |
| 0x20 | 7751  | 5.6%  | Space char (frequent in string data) |
| 0x41 | 3353  | 2.4%  | PUSH_VALUE opcode |
| 0x46 | 3140  | 2.3%  | LOAD_VAR opcode |
| 0x4E | 2301  | 1.6%  | ARRAY_IDX opcode |

---

## Known Opcodes

> **Code section layout note:** The code section is NOT a pure instruction stream.
> It contains 7-byte INSTRUCTIONS interleaved with variable-length DATA RECORDS.
> Instructions reference data records via addr field pointing into the code section.
> Data records have a type tag (e.g., 0x41 = string type), a 2-byte LE length, then content.
> The 0x41 that appears frequently is the STRING TYPE TAG in data records, not a 7-byte opcode.

### Confirmed 7-byte instructions (from BKAWLB instruction stream)

All 7-byte instructions: `[op:1][0x00:1][b2:1][addr_LE4:4]`

| Opcode | Seen b2 | Observed addr range | Inferred role |
|--------|---------|---------------------|---------------|
| `0x4B` | 0x09 | var_section (0x0460+) | VAR_INIT — initialize user var section; first instr every file |
| `0x20` | 0x05 | var_section | VAR_DECLARE? (var[1] ref, param prg.name) |
| `0xC1` | 0x00 | var_section | Unknown (appears just before 0x0E series) |
| `0x0E` | 0x61 | var_section AND code | ARRAY_INIT? repeated for consecutive array elements (stride 97) |
| `0xC0` | 0x04 | var_section | Unknown |
| `0x49` | 0x09 | var_section | PUSH_VAR? (references 4-byte var after 97-byte block) |
| `0x3B` | 0x14 | var_section | BRANCH family (same opcode as in .RWN; likely GOSUB/GOTO) |
| `0x0F` | 0x0A | var_section | ASSIGN (same opcode as in .RWN) |
| `0x45` | 0x05 | var_section | Unknown |
| `0x48` | 0x19 | var_section | Unknown |
| `0x1F` | 0x?? | var_section | Unknown |
| `0x13` | 0x?? | var_section | Unknown |
| `0x06` | 0x?? | var_section | Unknown |

### Older byte-frequency based observations (pre-7-byte-format confirmation)

These were identified from byte frequency and pattern analysis before the 7-byte format
was confirmed. Some may be data-record type tags rather than instruction opcodes.

| Byte | Name | Evidence | Status |
|------|------|-----------|--------|
| `0x41` | STRING_TYPE_TAG | `41 00 LL LL data` — string data records in code section | CONFIRMED (data record, NOT instr) |
| `0x46` | LOAD_VAR | Precedes array element assignments with repeating address patterns | Probable instr |
| `0x4E` | ARRAY_IDX | Follows LOAD_VAR for array assignments; IDX increments per element | Probable instr |
| `0x0A` | PUSH_ADDR | Seen before `0x0F 0x00` pairs in MENU_HLDR area | Probable instr |
| `0x35` | FIELD_REF? | Repeating with stride 53 at BKMRF code start | Possible instr |
| `0x43` | OP_43? | Second most frequent non-zero byte (~2%) | Unknown |
| `0xFF` | END_EXPR? | End of binary expression blobs | Data marker |
| `0xFD` | EXPR_HDR? | Start of binary expression blobs | Data marker |

**Byte frequency summary (stable opcodes from 3-way compile diff, BKMRF variants):**

| Byte | Role | Approx % in code section |
|------|------|--------------------------|
| `0x00` | address padding / arg bytes | 51% |
| `0x20` | possibly SPACE literal or common opcode | 3.5% |
| `0x46` | LOAD_VAR | 2.7% |
| `0x41` | PUSH_VALUE | 2.2% |
| `0x43` | unknown (OP_43?) | 2.0% |
| `0xFF` | end-of-expr marker? | 1.6% |
| `0x4E` | ARRAY_IDX | 1.5% |
| `0x30` | probably numeric literal `0` | 1.2% |
| `0x01` | probably numeric literal `1` | 1.2% |
| `0x0A` | PUSH_ADDR | 1.0% |
| `0x0F` | OP_0F | 0.85% |
| `0x49` | PUSH_VAR? | 0.82% |
| `0xFD` | expr-header? | 0.82% |

### PUSH_VALUE detail (`0x41`)

```
41 00 LL_lo LL_hi [LL bytes of data]
```

Used for BOTH plain string literals AND compiled expression blobs. The data can be:
- Printable ASCII: a literal string from source (e.g., `'AW-L-B'`, `'Sort by'`)
- Binary: a compiled sub-expression (e.g., form layout spec, mask definition)
  Binary blobs often start with `fd` and end with `ff`.

**Important:** Some `41 00 LL LL` matches are FALSE POSITIVES — the `41 00` bytes at that
offset are NOT a PUSH_VALUE instruction; they coincidentally form that pattern within other
instruction data. The 256-byte "string" at BKMRF.org2 0x24C3 is an example: it is part of
larger instruction stream, not a string push.

**Strings appear in EXECUTION ORDER** — confirmed from BKMRF.org2: first string `'NLT'` at
offset 0x35CD matches source line 98 (`opt.types = 'NLT'`); immediately followed by 9 table
names matching the `open` statements in lines 131-139.

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
