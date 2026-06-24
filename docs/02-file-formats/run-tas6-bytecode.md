# TAS Pro 6 `.RUN` File Format — Bytecode Analysis

Status: **partial** — instruction format confirmed C:65/100; opcodes in progress (Pass 240)

Last updated: 2026-06-24

---

## Overview

`.RUN` files are compiled TAS Professional 6 programs. They are unencrypted.
Analysed via Rosetta Stone: 7 `.SRC` source + `.RUN` binary pairs in
`samples/rosetta/`. Primary sample: `BKAWLB.RUN` (139,533 bytes) paired with
`BKAWLB.SRC` (691-line source).

---

## Two-Region Architecture (confirmed from BKAWLB — Pass 240)

Every `.RUN` file contains **two instruction streams**, both using the identical 7-byte
instruction format:

```
Region 1 — PREAMBLE (init) stream, at file 0x06C0 for BKAWLB
  - Executes immediately at program load time
  - Opens tables, runs finds, sets defaults, mounts forms, shows menu
  - Corresponds to source lines 42–113 (setup code before first label)
  - Instruction addrs reference the var pool as RAW OFFSETS (< runtime_base = 0x0460)

Region 2 — CODE (interactive) stream, at file 0x0802 for BKAWLB
  - Entry point is given by the 2-byte preamble header at code_start (0x0800)
  - Executes the interactive logic: ENTERs, TRAPs, loops, print routines
  - Corresponds to source lines 116+ (labeled sections: ENT.STAT, ASSIGN, VIEW, etc.)
  - Instruction addrs reference vars as ABSOLUTE RUNTIME ADDRESSES (>= runtime_base)
```

**Address semantics distinction (critical):**
- Preamble instructions: `addr` = raw var pool offset (< 0x0460 = runtime_base)
- Code instructions: `addr` = absolute runtime address (= runtime_base + var_pool_offset)

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
                             [0x0000 .. runtime_base-1]: zero-initialized runtime var storage
                             [runtime_base .. M-1]: PREAMBLE INSTRUCTION STREAM (region 1)
0x80 + N×16 + M     2      Code section header (2 bytes; value = entry offset LE2)
0x80 + N×16 + M + 2 ...    CODE INSTRUCTION STREAM (region 2)
   ...later in code section: inline string pool (41-tagged entries)
```

**code_start formula (confirmed):**
```
code_start = 0x80 + (h[7] × 16) + h[6]
```
For BKAWLB.RUN: `0x80 + (30 × 16) + 0x5A0 = 0x80 + 0x1E0 + 0x5A0 = 0x800`.

**Both 0x06C0 and 0x0802 are instruction stream starts in BKAWLB (not a contradiction):**
- 0x06C0 = start of preamble instruction stream (within the var section, at runtime_base offset)
- 0x0800 = code_start by formula (contains the 2-byte entry-point header)
- 0x0802 = start of interactive code instruction stream

An earlier doc version stated "code_start=0x6C0 was wrong; correct value is 0x800." That correction was incomplete: 0x06C0 IS a valid instruction stream (the preamble), and 0x0802 is where the interactive code begins. Both are real instruction streams.

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
| 0x18   | 0x5A0 = 1440 | Variable storage size in bytes (= h[6]) |
| 0x1C   | 0x1E = 30 | Table slot count (max slots allocated) (= h[7]) |
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
                    runtime_base = 0x0460 for BKAWLB (var_size=1440, table_count=30)
0x0460 – end        PREAMBLE INSTRUCTION STREAM (region 1)
                    45 instructions × 7 bytes = 315 bytes, starting at abs file 0x06C0
                    These are real 7-byte instructions executing init code (opens, finds, etc.)
```

**runtime_base varies by program:**
- Programs with var_size=1440, table_count=30: runtime_base=0x0460=1120 (BKAWLB, BKLME)
- Programs with var_size=2640, table_count=55: runtime_base=0x02D0=720 (BKMRF, BKDCA, BKAPH, BKAPHA, BKROA)
- runtime_base is NOT directly stored in a header field.

---

## Preamble Instruction Stream (Region 1) — BKAWLB

Preamble starts at abs file 0x06C0 (= 0x0260 [var section start] + 0x0460 [runtime_base]).
Contains **45 instructions × 7 bytes** encoding source lines 42–113.

Each instruction: `[opcode:1][0x00:1][b2:1][addr_LE4:4]`
For preamble: `addr` = raw var pool offset (< 0x0460).

| I# | File off | Bytes | Opcode | b2 | addr | Source line / role |
|----|----------|-------|--------|----|----|---------------------|
| 0  | 0x06C0   | `4B 00 09 00 00 00 00` | CALL_LIB  | 9  | 0x0000 | library init (SETUP_COLOR) |
| 1  | 0x06C7   | `71 00 05 09 00 00 00` | EXIT2?    | 5  | 0x0009 | param prg.name (off=9) |
| 2  | 0x06CE   | `3B 00 14 0E 00 00 00` | COND_BRANCH? | 20 | 0x000E | var (off=14) |
| 3  | 0x06D5   | `0F 00 0A 22 00 00 00` | ASSIGN    | 10 | 0x0022 | var (off=34) |
| 4  | 0x06DC   | `1F 00 35 2C 00 00 00` | TABLE_HANDLE | 53 | 0x002C | open table 1 (BKSYMSTR) |
| 5..8 | ...   | `1F 00 35 61/96/CB/00 00 00 00` | TABLE_HANDLE | 53 | 97,150,203,256 | open tables 2..5 |
| ...| ...     | ...   | ...    | ...| ...  | find, clr, assigns... |
| ~38..41 | ... | `0E 00 61 ...` | ENTER?    | 97 | var offsets | e.status[1..4] |
| ~42 | ...   | `13 00 21 ...` | FIND_KEY  | 33 | var off    | find F srch BKSY... |
| ~43 | ...   | `06 00 ...`    | CLR       | -  | var off    | clr BKSYMSTR rec |
| ~44 | ...   | `1C 00 ...`    | MOUNT     | -  | var off    | mount SELECT2 type S |
| ~45 | ...   | `21 00 ...`    | MENU      | -  | var off    | menu at 5,5... |

Source lines covered by preamble: 42–113 (SETUP_COLOR through MENU).

---

## Code Section Header (0x0800)

Two bytes at code_start:
- BKAWLB.RUN: `00 00` → entry at instruction 0 (code stream starts immediately at 0x0802)
- BKMRF.RUN: `04 2E` (= 0x2E04 LE = 11780) → inline data block precedes instructions
- BKDCA.RUN: `1D E9` (= 0xE91D LE = 59677) → large inline data block

Non-zero values indicate an **inline data section** of that many bytes before the instruction
stream. BKMRF instructions confirmed at abs=0x3C4A (offset +11786 from code_start), consistent
with preamble=11780.

---

## Code Instruction Stream (Region 2) — BKAWLB

Starts at abs file 0x0802 (code_start + 2 for BKAWLB).
Corresponds to source lines 116+ (labeled sections).

Same 7-byte format: `[opcode:1][0x00:1][b2:1][addr_LE4:4]`
For code: `addr` = absolute runtime address (≥ runtime_base = 0x0460), OR code branch offset.

Total instructions decoded from 0x06C0 (both regions): 2078.

### Sample: ENT.STAT section (source lines 116–127)

Source:
```
ENT.STAT:
  xtrap chg ignr
  enter e.status[1] ; enter e.status[2] ; enter e.status[3] ; enter e.status[4]
  func pre.stat
    trap F1 do PRE_STAT1
    trap ESC do PRE_STAT2
    trap F10 do PRE_STAT3
  ret .t.
```

Corresponding instructions (I#46+, file 0x0802+):
```
OP_4B  CALL_LIB   (xtrap chg ignr — library call)
OP_C1  ENT_BLOCK  (block header for 4 enter statements)
OP_0E  ENTER b2=0x61 (enter e.status[1])
OP_0E  ENTER b2=0x61 (enter e.status[2])
OP_0E  ENTER b2=0x61 (enter e.status[3])
OP_0E  ENTER b2=0x61 (enter e.status[4])
  ... function pre.stat body ...
OP_37  TRAP (trap F1 do PRE_STAT1)
OP_37  TRAP (trap F2 do PRE_STAT2)
OP_37  TRAP (trap F10 do PRE_STAT3)
OP_20  RET_FUNC   (ret .t.)
```

Positional confirmation method: 4 consecutive OP_0E = the 4 `enter e.status[N]`; 3 consecutive
OP_37 = the 3 traps. No other sequence in the source produces 4 consecutive enters or 3 traps.

---

## Instruction Format (confirmed, 7 bytes)

```
Byte  Field      Notes
----  -----      -----
[0]   opcode     Operation code
[1]   0x00       Always zero (padding or reserved)
[2]   b2         Fixed per opcode — encodes operand descriptor size, sub-opcode, or type info
[3-6] addr LE4   4-byte LE address field (semantics depend on region and opcode)
```

**b2 field:** b2 is a FIXED constant for a given opcode — it does NOT switch per instruction.
Example: every OP_0E (ENTER) has b2=0x61=97; every OP_37 (TRAP) has b2 TBD.

---

## Known Opcodes (Pass 240 — combined Rosetta Stone findings)

### Confirmed by positional alignment or binary pattern

| Opcode | Name | b2 | Evidence / source context |
|--------|------|----|---------------------------|
| `0x0F` | ASSIGN | 0x0A | Baseline; var assignments throughout |
| `0x3B` | COND_BRANCH | 0x14 | Baseline; conditional goto |
| `0x40` | EXIT | — | Baseline |
| `0x42` | GOSUB | — | Baseline |
| `0x48` | PUSH | 0x19 | Baseline |
| `0x49` | READ_PROP | 0x09 | Baseline |
| `0x57` | EXEC_FORM | — | Baseline |
| `0x6A` | GOTO_LABEL | — | Baseline |
| `0x71` | EXIT2 | — | Baseline |
| `0xDC` | POP | — | Baseline |
| `0x0E` | ENTER | 0x61 | Positional: 4 in a row = `enter e.status[1..4]` (Pass 240) |
| `0x37` | TRAP | — | Positional: 3 in a row = 3 traps in `func pre.stat` (Pass 240) |
| `0x20` | RET_FUNC | 0x05 | End of every function body (`ret .t.`/`ret .f.`) (Pass 240) |
| `0x08` | TRAP_DFLT | — | Where `trap KEY dflt` expected (Pass 240) |
| `0xC0` | SET_PROP_CTX | 0x04 | Always precedes READ_PROP group (Pass 240) |
| `0xC1` | ENT_BLOCK | 0x00 | Always precedes ENTER groups — block setup (Pass 240) |
| `0x4B` | CALL_LIB | 0x09 | First instruction of every file; `fnc_list`, `xtrap`, `prtr_setup` (Pass 240) |
| `0x39` | FUNC_PREPOST | 0x51 | Before complex ENTER; pre/post function descriptor (Pass 240) |
| `0x01` | ARG_DESC | 0x1D | Between OP_39 and ENTER; argument descriptor (Pass 240) |

### Confirmed in preamble (init) region — opcode = source statement type

| Opcode | Name | b2 | Source statement |
|--------|------|----|-----------------|
| `0x1F` | TABLE_HANDLE | 0x35=53 | `open TABLE lock N` — 5× in preamble, stride 53 (Pass 240) |
| `0x13` | FIND_KEY | 0x21=33 | `find F srch BKSY.ARINV.NUM nlock` (Pass 240) |
| `0x06` | CLR | — | `clr BKSYMSTR rec` (Pass 240) |
| `0x1C` | MOUNT | — | `mount SELECT2 type S` (Pass 240) |
| `0x21` | MENU | — | `menu at 5,5 ...` (Pass 240) |
| `0x73` | PRG_HDR | — | `prg_hdr prg.name+'...'` — rare (3 total) (Pass 240) |

### Probable (pattern-based, not yet positionally proved)

| Opcode | Name | b2 | Evidence |
|--------|------|----|----------|
| `0x53` | PFMT | 0x7D=125 | Repeating in print section loop; b2=125 consistent (Pass 240) |
| `0x93` | FOR_LOOP | — | Loop header preceding paired OP_65 in `for(mcntr;1;3;1)` area (Pass 240) |
| `0x65` | PBLNK/WRITE | — | 2 per loop iteration in print section (Pass 240) |
| `0xBE` | PMSG | 0x28=40 | Print message; addrs spaced by 40 in sequence (Pass 240) |
| `0x46` | LOAD_VAR | — | Precedes array element assignments with repeating address patterns |
| `0x4E` | ARRAY_IDX | — | Follows LOAD_VAR for array assignments; IDX increments per element |
| `0x0A` | PUSH_ADDR | — | Seen before `0x0F 0x00` pairs in MENU_HLDR area |

### Data records (NOT 7-byte instructions)

| Tag | Name | Format | Notes |
|-----|------|--------|-------|
| `0x41` | STRING_LITERAL | `41 00 LL_lo LL_hi [LL bytes]` | Inline strings in code section; NOT an opcode |

---

## Inline String Pool (in code section)

String literals are embedded in the code section using a tagged format:

```
41 00 LL_lo LL_hi [LL bytes of string data]
```

These are NOT 7-byte instructions — they are **data records** referenced by instructions.

String sequence in BKAWLB matches source code execution order:
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

## BKMRF Variants (same source, different compile)

`samples/rosetta/` contains three binaries from the same source:
- `BKMRF.RUN` — 159,375 bytes, version byte 0x?? (full linked)
- `BKMRF.org2` — 89,175 bytes, version 0x58 (earlier/partial)
- `BKMRF.TEST` — 85,898 bytes, version 0x51 (test compile)

These can be byte-diffed to identify which bytes are stable (opcode values) vs.
variable (addresses that change between compiles). Planned for next analysis pass.

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
| `0x41` opcode | Frequent (STRING_LITERAL data) | Not seen |

---

## Batch Decrypt Results (2026-06-15)

- Files scanned: 1,145 `.RWN` files from `\\i2s109-solidcrm\DBAMFG$\` (all subdirs)
- OK: 1,144 (99.9%)
- FAIL: 1 — `t6ine1.RWN` starts with `TPF0` (binary Delphi form, misnamed .RWN)
- Output: `samples/rwn_decrypted/` (1,122 unique files, ~283 MB, gitignored)
- Summary CSV: `samples/rwn_decrypted/decrypt_summary.csv`

---

## References

- Source: `samples/rosetta/BKAWLB.SRC`
- Binary: `samples/rosetta/BKAWLB.RUN`
- Analysis script: `scripts/analyze_run.py`
