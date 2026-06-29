# TAS Pro 6 `.RUN` File Format — Bytecode Analysis

Status: **partial** — dual-channel architecture confirmed C:88/100; 3 new header fields confirmed Pass 341; cross-file corpus 374/397 files Pass 356; Pass 366: OP_8D structural pattern confirmed as DISPATCH_CONT; Pass 367: OP_25=PFMT, OP_22=PBLNK, OP_0C=DEL_REC confirmed; OP_43/OP_47=array-field-subscript pair, OP_29=array-iter-init structural; pfmt/pblnk CORRECTION applied — they DO compile to instructions; 5 unknowns remain

Last updated: 2026-06-29

---

## Overview

`.RUN` files are compiled TAS Professional 6 programs. They are unencrypted.
Analysed via Rosetta Stone: 7 `.SRC` source + `.RUN` binary pairs in
`samples/rosetta/`. Primary sample: `BKAWLB.RUN` (139,533 bytes) paired with
`BKAWLB.SRC` (691-line source).

---

## Dual-Channel Architecture (confirmed from BKAWLB — Pass 244)

**MAJOR DISCOVERY (Pass 244):** A `.RUN` file has two PARALLEL channels sharing the same
file bytes:

```
INSTRUCTION CHANNEL — starts at code_off (0x06C0 for BKAWLB)
  - Sequential 7-byte instruction records: [opcode][0x00][b2][addr_LE4]
  - One continuous stream of 2078 instructions total
  - Sub-sections: preamble (I#0–45, file 0x06C0–0x0801) and interactive (I#46–2077, file 0x0802–0x3F8B)

DATA CHANNEL — starts at file offset 0x0000
  - Packed variable-length records; NO gaps between records
  - Each record is referenced by exactly one instruction via [addr, b2]
  - Records are sequential: addr[I+1] = addr[I] + b2[I]  (CONFIRMED 100% by addr chain)
  - Total size stored in header at offset 0x08 (= 0x923E for BKAWLB)
```

**Key invariants:**
- `b2` = number of bytes consumed in the data channel for this instruction (CONFIRMED)
- `addr` = **absolute file offset** of this instruction's data record (CONFIRMED)
- `addr + b2` = addr of next instruction's data record (no gaps, no overlaps)
- `b2 = 0` (e.g., ENT_BLOCK): instruction has no data record; addr points to where next record starts

**The data channel overlaps the instruction channel region (0x06C0–0x3F92).** Some instructions'
data records span file offsets within the instruction range. This is intentional: ENTER field
descriptors for ENT sections (I#64+) share bytes with the instruction stream. The runtime reads
specific offsets within each descriptor type — it does not scan byte-by-byte.

---

## File Layout (confirmed from BKAWLB.RUN — Pass 244)

```
Offset              Size   Description
------              ----   -----------
DATA CHANNEL:
0x00000             var    DATA CHANNEL starts here: packed variable-length records, instruction-referenced
   (data records for I#0–45 preamble: 0x0000–0x0456 = 1110 bytes)
   (data records for I#46–2077 interactive: 0x0460–0x923D = 36414 bytes; overlap with code zone)
   Total data channel = h[0x08] bytes (0x923E for BKAWLB)

FILE HEADER (within data channel):
0x00                0x34   File header (13 × 4-byte LE fields; see table below)
0x34                0x01   Padding (0x00)
0x35                0x05   Magic: "TAS32"
0x3A                0x01   Compiler version byte (BKAWLB=0x71, BKMRF.org2=0x58)
0x3B                0x45   Compiler metadata (zero-padded)
0x80                N×16   Table name slots: 8-char ASCII name + 8 null bytes (N = h[7])
0x80 + N×16         h[6]   Var section:
                             [0x0000 .. runtime_base-1]: zero-initialized runtime var storage (BKAWLB: 1120 bytes)
                             [runtime_base .. h[6]-1]:  DATA RECORDS for preamble instructions (BKAWLB: 0x0460–0x05FB)

INSTRUCTION CHANNEL (overlapping the data channel):
code_off=0x06C0     46×7   PREAMBLE: instructions I#0–45 (init code: open tables, finds, menu)
0x0802              2032×7 INTERACTIVE: instructions I#46–2077 (ENT sections, VIEW, PRT_DETAIL, etc.)
   (code_start formula: 0x80 + h[7]×16 + h[6] = 0x0800; instruction stream starts 2 bytes later at 0x0802)
   (preamble ends at 0x0801 = last byte of I#45; code_start 0x0800 falls within I#45's addr field bytes)
```

**Key formula:**
```
code_off = 0x80 + (h[7] × 16) + runtime_base       (= 0x06C0 for BKAWLB)
code_start = 0x80 + (h[7] × 16) + h[6]             (= 0x0800 for BKAWLB; I#46 starts at 0x0802)
runtime_base = h[6] - (preamble_count × 7)          (= 0x0460 for BKAWLB: 1440 - 46*7 = 1118? CHECK)
```

**Overlap:** Data records for interactive instructions (I#64+) fall within the instruction channel range
(0x06C0–0x3F92). The same file bytes serve dual roles simultaneously.

---

## Header Fields (offsets 0x00-0x33, all LE 32-bit)

| Offset | Value (BKAWLB) | Status | Notes |
|--------|---------------|--------|-------|
| 0x00   | 0x38D9 = 14553 | **CONFIRMED Pass341** | **INSTRUCTION STREAM BYTE COUNT** = instruction_count × 7; confirmed exact integer division across 5 files (BKAWLB=2079, BKMRF=2639, BKDCA=3471, BKLME=2137, BKROA=4577 instructions) |
| 0x04   | 0x105A2 = 66978 | unknown | Offset within post-data-channel section; not a clean section marker |
| 0x08   | 0x923E = 37438 | **CONFIRMED Pass244** | **DATA CHANNEL TOTAL SIZE** = sum of all b2 values; last addr + last b2 = this value |
| 0x0C   | 0x1C4 = 452 | inferred | Possibly var table descriptor size (not confirmed) |
| 0x10   | 0xA = 10 | **CONFIRMED Pass341** | **FORMAT CONSTANT = 10** always; same across all 5 files; likely format version or magic value |
| 0x14   | 0x17F = 383 | unknown | Not define-statement count (SRC has 45 defines, this=383); possibly string/symbol pool count |
| 0x18   | 0x5A0 = 1440 | **CONFIRMED Pass244** | **VARIABLE STORAGE SIZE** in bytes (= h[6]); 1440 for 30-slot programs, 2640 for 55-slot programs |
| 0x1C   | 0x1E = 30 | **CONFIRMED Pass244** | **TABLE SLOT COUNT** (max slots allocated) (= h[7]); 30 for small programs, 55 for large |
| 0x20   | 0x47D0 = 18384 | unknown | Possibly an offset into the post-data-channel section or a section size |
| 0x24   | 0xFFFF = 65535 | unknown | 0xFFFF in BKAWLB/BKDCA/BKLME; 256000 in BKMRF/BKROA; possibly a limit counter |
| 0x28   | 0x5316 = 21270 | unknown | Varies widely; no clear formula found |
| 0x2C   | 0x0 = 0 | **CONFIRMED Pass341** | **ALWAYS ZERO** across all 5 files; reserved/unused |
| 0x30   | 0x1A4 = 420 | unknown | 420 for 30-slot programs; varies for 55-slot (600/780/660) |

### Cross-file header comparison (Pass 341 — 5 sample files)

| File | Size | h00 (instr×7) | instrs | h08 (data) | h18 (vars) | h1C (slots) | h10 (const) |
|------|------|---------------|--------|------------|------------|-------------|-------------|
| BKAWLB.RUN | 139533 | 14553 | 2079 | 37438 | 1440 | 30 | 10 |
| BKMRF.RUN | 159375 | 18473 | 2639 | 37021 | 2640 | 55 | 10 |
| BKDCA.RUN | 230690 | 24297 | 3471 | 49603 | 2640 | 55 | 10 |
| BKLME.RUN | 127835 | 14959 | 2137 | 33547 | 1440 | 30 | 10 |
| BKROA.RUN | 281173 | 32039 | 4577 | 70023 | 2640 | 55 | 10 |

**Key takeaway:** All programs share two var/table-slot configurations: 1440-var/30-slot (smaller) and 2640-var/55-slot (larger). h[0x10]=10 is invariant. h[0x00]/7 gives exact instruction count.

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

## Code Section Header (code_start) — CORRECTED Pass 312

The header at `code_start` has **variable size** — instructions start IMMEDIATELY after the
header bytes. There is no "inline data block" before instructions.

| Program | cs | Header bytes | hdr_size | Stream starts |
|---------|-----|-------------|---------|---------------|
| BKAWLB.RUN | 0x0800 | `00 00` | 2 bytes | cs+2 = 0x0802 |
| BKMRF.org2 | 0x0940 | `57 09 00 00` | 4 bytes | cs+4 = 0x0944 |
| BKMRF.TEST | 0x0940 | `57 09 00 00` | 4 bytes | cs+4 = 0x0944 |
| BKMRF.RUN  | 0x0E40 | `04 2E 15 00 00` | 5 bytes | cs+5 = 0x0E45 |

**Rule:** LE16 at cs[0] = 0 → 2-byte header; non-zero → longer header (4 or 5 bytes confirmed).
Exact semantics of non-zero fields TBD (entry-point offset or section count — not "inline size").

**CORRECTION (Pass 312):** Prior documentation claimed "non-zero LE16 = inline data block size
before instructions." This was wrong. Previous claim "BKMRF.RUN instructions at abs=0x3C4A" was
also wrong — confirmed start is **0x0E45** (397 aligned 0x3B b1-zero occurrences from that offset).

---

## Code Instruction Stream (Region 2) — BKAWLB

Starts at abs file 0x0802 (code_start + 2 for BKAWLB).
Corresponds to source lines 116+ (labeled sections).

Same 7-byte format: `[opcode:1][0x00:1][b2:1][addr_LE4:4]`
For code: `addr` = absolute runtime address (≥ runtime_base = 0x0460), OR code branch offset.

Total instructions decoded from 0x06C0 (both regions): 2078.

### Sample: ENT.STAT section (source lines 115–127) — confirmed Pass 243

Source:
```
ENT.STAT:
  enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
  enter e.status[2] mask 'X ' up acr
  enter e.status[3] mask 'X ' up acr
  enter e.status[4] mask 'X ' up acr
  { func pre.stat
      trap F1 GOSUB SHOWHELP
      trap ESC goto EXIT2
      trap f10 goto start_prt
      fnc_list 'F1 Help','F10 Print,Esc Exit'
      ret .t.
  }
```

Corresponding instructions (I#46+, file 0x0802+):
```
I#46   CALL_LIB    (library/section init call)
I#47   RET_FUNC    (section header return)
I#48   ENT_BLOCK   (block header for 4 enter statements)
I#49   ENTER b2=0x61  (enter e.status[1])
I#50   ENTER b2=0x61  (enter e.status[2])
I#51   ENTER b2=0x61  (enter e.status[3])
I#52   ENTER b2=0x61  (enter e.status[4])
I#53   SET_PROP_CTX   (post func body begin)
...    ...            (func pre.stat body — see separate body below)
```

Positional confirmation: 4 consecutive OP_0E at I#49–52 = the 4 `enter e.status[N]` (Pass 243).
The inline `{ func pre.stat }` body is compiled separately after the ENTER block.

**All ENT section enters (I#46–213) use OP_0E (0x0E) — NOT OP_93.**
The 0x93/0x65/0x53 cluster appears later in the binary (I#425+) and does not correspond to
the ENT section's ENTER statements.

---

## Instruction Format (confirmed, 7 bytes — Pass 244)

```
Byte  Field      Notes
----  -----      -----
[0]   opcode     Operation code
[1]   0x00       Always zero (padding or reserved)
[2]   b2         SIZE of this instruction's inline data record in the data channel
[3-6] addr LE4   ABSOLUTE FILE OFFSET of this instruction's inline data record
```

**b2 = data record size — CONFIRMED 100% by addr chain verification (Pass 244):**
- Every instruction consumes exactly `b2` bytes from the data channel starting at `addr`
- `addr[I+1] = addr[I] + b2[I]` — verified across all 2078 instructions, zero exceptions
- `b2 = 0`: instruction has no data (e.g., ENT_BLOCK); addr just points to where next record starts
- b2 is a FIXED constant per opcode (every ENTER has b2=97, every TRAP has b2=10, etc.)

**addr = absolute file offset — CONFIRMED:**
- `addr` is NOT relative to code_off and NOT a runtime variable address
- `addr` = the byte position in the file where this instruction's data record starts
- First instruction (CALL_LIB at I#0) has addr=0x0000 — data starts at file byte 0

**Data records can contain embedded instruction records:**
- Some opcodes (OP_93, OP_65, OP_53) have data records that themselves contain 7-byte instruction-format records
- These nested records reference deeper data via their own addr/b2 fields
- This creates a hierarchical descriptor structure for complex constructs like enter fields

---

## Known Opcodes (Pass 240 + Pass 362 — combined Rosetta Stone findings)

### Confirmed by positional alignment or binary pattern

| Opcode | Name | b2 | Evidence / source context |
|--------|------|----|---------------------------|
| `0x0F` | ASSIGN | 0x0A | Baseline; var assignments throughout |
| `0x3B` | COND_BRANCH | 0x14 | Baseline; conditional goto |
| `0x42` | GOSUB | 0x04 | Baseline; also used as FIELD_TERM in ENTER cluster context |
| `0x48` | PUSH | 0x19 | Baseline |
| `0x49` | READ_PROP | 0x09 | Baseline |
| `0x57` | EXEC_FORM | 0x05 | Baseline |
| `0x6A` | GOTO_LABEL | — | Baseline |
| `0x71` | CHK_PARAM | 0x05 | Baseline; appears at I#1 (BKAWLB/BKROA/BKDCA) = parameter-check at program entry |
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
| `0x4A` | QUIT | 0x09 | Positional: BKAWLB I#1787 = `quit` at source L426 (EXIT2 label); b2=9 matches CALL_LIB (Pass 362) |

### Confirmed in preamble (init) region — opcode = source statement type

| Opcode | Name | b2 | Source statement |
|--------|------|----|-----------------|
| `0x1F` | OPEN_LOCK_N | 0x35=53 | `open TABLE lock N` — 5× in BKAWLB preamble (Pass 240) |
| `0x40` | OPEN_LOCK_R | 0x35=53 | `open TABLE lock R` — same b2=53 as OP_1F; appears where read-only/openv opens expected (BKDCA uses exclusively, BKROA uses for lock R; Pass 362) |
| `0x13` | FIND_QUALIFIED | 0x21=33 | `find F srch FIELD err LABEL` or `find F srch FIELD nlock` — with qualifier (Pass 240/362) |
| `0x1A` | FIND_BASIC | 0x21=33 | `find F srch FIELD` — no err label, no nlock; BKDCA I#19 = `find F srch BKYS.WONUM` (L118, no err); b2=33 same as OP_13 (Pass 362) |
| `0x06` | CLR | — | `clr BKSYMSTR rec` (Pass 240) |
| `0x1C` | MOUNT | — | `mount SELECT2 type S` (Pass 240) |
| `0x21` | MENU | — | `menu at 5,5 ...` (Pass 240) |
| `0x73` | PRG_HDR | — | `prg_hdr prg.name+'...'` — rare (3 total) (Pass 240) |
| `0x25` | PFMT | 0x0A | `pfmt N` — set print format line ref; 8 in BKLME = 8 `pfmt` in source (exact match — Pass 367) |
| `0x22` | PBLNK | 0x0A | `pblnk N` — print N blank lines; 7 in BKLME = 7 `pblnk` in source (exact match — Pass 367) |
| `0x0C` | DEL_REC | — | `del TABLE nocnf` — delete current record; 1 in BKLME = 1 `del INVTXN nocnf` (exact match — Pass 367) |
| `0x43` | ARRAY_FLD_BEGIN | 0x09 | Database field array subscript open: always [OP_43][ASSIGN][OP_47]; local-var arrays use plain ASSIGN instead (Pass 367) |
| `0x47` | ARRAY_FLD_END | 0x09 | Database field array subscript close: always [OP_43][ASSIGN][OP_47] (Pass 367) |
| `0x29` | ARRAY_ITER_INIT | 0x05 | Array iteration init: appears immediately before FOR_LOOP at `next` or before OP_43; linked-list array seek (Pass 367) |

### Probable (pattern-based, not yet positionally proved)

| Opcode | Name | b2 | Evidence |
|--------|------|----|----------|
| `0xBE` | PMSG | 0x28=40 | Print message; addrs spaced by 40 in sequence (Pass 240) |
| `0x46` | LOAD_VAR | — | Precedes array element assignments with repeating address patterns |
| `0x4E` | ARRAY_IDX | — | Follows LOAD_VAR for array assignments; IDX increments per element |
| `0x0A` | PUSH_ADDR | — | Seen before `0x0F 0x00` pairs in MENU_HLDR area |

### Enter-Field Execution Family — OP_93/OP_65/OP_53 (Pass 243+244+353)

These three opcodes form the "FIELD_ENTER" group used for interactive enter fields in the main
program flow (NOT the preamble ENT.xx declarations). Together they define and execute one enter field.

| Opcode | b2 | Count | Data record content |
|--------|----|-------|---------------------|
| `0x93` | 0x14=20 | 29 | 20-byte blob containing **data channel references** — field setup/validation callback context |
| `0x65` | 0x0A=10 | 62 | 10-byte blob; appears 1–N times after OP_93; continuation of field descriptor |
| `0x53` | 0x7D=125 | 34 | 125-byte blob containing **data channel references** — full field execution block |
| `0x42` | 0x04=4   |    | Field terminator — closes the OP_53 block for one enter field |

**Cluster pattern per enter field** (Pass 353 confirmed from BKAWLB.RUN I#425–I#435):

```
[OP_93 b2=20]          ← field setup blob (references data channel UI string records)
[OP_65 b2=10] × N      ← callback attribute descriptors (N ≥ 1; often 2)
[OP_3B b2=20]?         ← conditional branch (for `upar` or `acr` target, optional)
[OP_53 b2=125]         ← full field execution blob
[OP_42 b2=4]           ← field terminator
```

One cluster = one TAS Pro 6 `enter` field statement. Example mapping from BKAWLB.SRC/RUN:

```
Source:  enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
Binary:  I#425: OP_93  b2=20 addr=0x20d6   ← blob refs data channel 0x4af8="Esc Exit"
         I#426: OP_65  b2=10               ← callback attr 1
         I#427: OP_65  b2=10               ← callback attr 2
         I#428: OP_3B  b2=20               ← COND_BRANCH for `upar START`
         I#429: OP_53  b2=125 addr=0x2112  ← full execution blob
         I#430: OP_42  b2=4   addr=0x218f  ← field terminator
```

**CRITICAL CORRECTION (Pass 353):** The blobs are **NOT** nested instruction streams. Prior
documentation (Pass 244) that described "embedded instruction records (COND_JMP + PMSG + partial
RET_FUNC)" was an incorrect interpretation — those bytes do not parse cleanly as 7-byte instructions
(20-byte blob ≠ 2×7+clean; 125-byte blob similarly). The blobs contain **absolute data channel
offsets** pointing to UI string records (prompt text, help text, function key labels). Confirmed:
OP_93 blob at 0x20d6 references data channel offset 0x4af8 = "Esc Exit" (from `fnc_list` in source).

**Internal byte layout still unknown:** The exact sub-field structure within the 20-byte, 10-byte, and
125-byte blobs requires tp7runtime.exe disassembly to decode fully.

**Field inheritance:** Some consecutive `enter` fields omit OP_93 — I#435 (field 2 in a group) has
OP_53 with no preceding OP_93, inheriting the prior field's setup context.

**Why different from ENTER (0x0E)?** ENTER (0x0E) is used in preamble ENT sections to DEFINE/REGISTER
enter fields. OP_93/65/53 are used in interactive code to EXECUTE an enter interaction with full
pre/post callback and lookup logic. The blobs reference data channel records that provide runtime
context (UI strings, prompt text, callbacks).

**CORRECTION (Pass 367 — supersedes Pass 243):** `pfmt` and `pblnk` DO compile to bytecode
instructions: **OP_25 = PFMT** (b2=10) and **OP_22 = PBLNK** (b2=10). Count matches in BKLME:
8 OP_25 = 8 `pfmt` in source (exact); 7 OP_22 = 7 `pblnk` in source (exact). Pass 243 correctly
ruled out OP_53=pfmt and OP_65=pblnk, but incorrectly concluded pfmt/pblnk compile to zero. The
"PRT_TOF = 2 instructions" claim missed the leading pfmt/pblnk instructions. BKAWLB PRT_TOF
(8 pfmt + 2 pblnk + page=page+1 + ret) compiles to **12 instructions**, not 2.

`pfmt N` = set the current print format line reference at runtime (OP_25, b2=10).
`pblnk N` = print N blank lines at this point in the report (OP_22, b2=10).

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

## Rosetta Stone Results — BKAWLB binary section map (Pass 243)

### Confirmed binary-to-source alignments

| Binary range | Source label | Source lines | Notes |
|--------------|-------------|--------------|-------|
| I#0–44 | Preamble (init) | ~1–113 | OPEN_TBL×5, init, menu |
| I#45 | Gap/dummy | — | 7-byte padding between preamble/interactive |
| I#46–213 | Interactive stream | 115–338 | All ENT sections + sort-by blocks |
| I#48–52 | ENT.STAT (4 enters) | 116–119 | 4 consecutive ENTER (0x0E) |
| I#63–69 | ENT.CLASS16 (6 enters) | 148–153 | 6 consecutive ENTER (0x0E) |
| I#82–89 | ENT.CLASSB+START (7 enters) | 168–211 | 7 consecutive ENTER (0x0E) |
| I#99–101 | START date range (2 enters) | ~171–177 | 2 consecutive ENTER (0x0E) |
| I#111–119 | START WO/INV/CUST (8 enters) | ~179–223 | 8 consecutive ENTER (0x0E) |
| I#214 | VIEW section | 338–339 | MOUNT instruction confirmed |
| I#217–218 | VIEW traps | 341–342 | trap F1+F2 pair |
| I#223–240 | PRT_DETAIL filter start | 350–361 | 18 consecutive COND_JMP |
| I#241–268 | PRT_DETAIL body | 363–398 | for-loops + class check; FOR_OP at I#243 |
| I#269–290 | PRT_DETAIL last filters | 398–407 | 17 COND_JMPs (CLASS_OK + 8 compound) |
| I#291–312 | FIND_NEXT + end | 410–412 | FIND_KEY at I#292; RET_FUNC I#312 |
| I#313–372 | Named subroutines | 446–514 | DSP_WORD1/2, SETUP_INV/CUST, etc. |
| I#425–470 | 0x93/0x65/0x53 cluster 1 | ~115–145 (func bodies) | 8 blocks = ENT.STAT/PRI/CLASS func bodies |
| I#521–531 | FUNC_PREPOST×2 + 7 ARG_DESC + ENTER×2 | ~179–207 | START2/3 with pre.wo1/post.wo1 |
| I#581–703 | 0x93/0x65/0x53 cluster 2 | TBD | 10 blocks |
| I#1021–1077 | 0x93/0x65/0x53 cluster 3 | TBD | in subroutine section |
| I#1773–1784 | ABORT_RPT | 413–419 | 12 instructions for 5 pmsg statements |
| I#1785–1786 | FINISH/EXIT | 421–424 | CALL_LIB (PRTR_SETUP 'F') + RET_FUNC |
| I#1787 | EXIT2: quit | 426 | OP_4A instruction |
| I#1789 | PRT_TOF: page=page+1 | 429 | ASSIGN instruction |
| I#1790 | PRT_TOF: ret | 440 | RET_FUNC instruction |

### pfmt/pblnk declarative finding (confirmed Pass 243)

`pfmt N` and `pblnk N` in TAS Pro 6 compile to **zero bytecode instructions**. They are
format directives that reference numbered format lines defined in the `\R5...` report block
at the bottom of the source file. The report runtime uses these numbers when printing — no
instruction is needed at execution time.

**PRT_TOF** in BKAWLB has: 8 × `pfmt` + 2 × `pblnk` + `page=page+1` + `ret`
Compiles to: 2 instructions — ASSIGN (page=page+1) at I#1789, RET_FUNC (ret) at I#1790.

---

## BKMRF Variants — 3-Way Byte-Diff Results (Pass 312)

`samples/rosetta/` contains three binaries from the same source:
- `BKMRF.RUN` — 159,375 bytes, version 0x60, cs=0x0E40, stream at 0x0E45, ~2734 instructions
- `BKMRF.org2` — 89,175 bytes, version 0x58, cs=0x0940, stream at 0x0944, ~1917 instructions
- `BKMRF.TEST` — 85,898 bytes, version 0x51, cs=0x0940, stream at 0x0944, ~1851 instructions

**3-way byte stability analysis (first 332 common instructions, org2 vs TEST):**

| Byte pos | Field | org2 vs TEST | org2 vs RUN | Interpretation |
|----------|-------|-------------|-------------|----------------|
| 0 | opcode | **100% stable** | 22% | Opcodes confirmed; RUN starts different sequence |
| 1 | b1 | **100% stable** | **100%** | Always 0x00 — confirmed across ALL variants |
| 2 | b2 | **100% stable** | 23% | b2 is opcode-fixed constant |
| 3 | addr byte0 (LSB) | 100% (same cs) | 0% | Compile-dependent offsets |
| 4 | addr byte1 | 100% (same cs) | 0% | Compile-dependent offsets |
| 5 | addr byte2 | **100% stable** | **100%** | Always 0x00 across ALL variants |
| 6 | addr byte3 (MSB) | **100% stable** | **100%** | Always 0x00 across ALL variants |

**Key findings:**
- **b1 (byte 1) = ALWAYS 0x00** — confirmed universally across all three variants.
- **Addr bytes 5–6 = ALWAYS 0x00** — effective address space is **16-bit** (max addr 0xFFFF).
  The addr field stores a 2-byte LE16 value in bytes 3–4 with zero padding in bytes 5–6.
- **Opcode (byte 0) and b2 (byte 2) are stable** between org2 and TEST (100%). The low match
  vs RUN (22%) reflects different entry points / instruction sequences, NOT opcode instability.
- org2 and TEST share a **332-instruction common prefix** (first 332 instructions identical byte-for-byte).

**Corrected instruction format:**

```
[op:1][0x00:1][b2:1][addr_LE16:2][0x00:2]   (7 bytes total)
        ^^^^                       ^^^^^^
    always zero               always zero
```

Effective address space is 16-bit (bytes 3–4). The 4-byte addr field's upper half is always 0.

---

## Named Variable Export Table (Pass 351 — 2026-06-26)

Programs that expose shared variables to other programs contain a **Named Variable Export Table**
in a section beyond the data channel. Each entry is **48 bytes**:

```
[NAME:16 bytes] [DESCRIPTOR:32 bytes]
  Name = up to 15 ASCII chars, right-padded with spaces, null-terminated.
  Descriptor layout:
    [0..2]  : 3 zero bytes
    [3]     : type letter ('A'=alpha, 'I'=integer/index, 'R'=real, 'L'=long,
                            'D'=date, 'N'=numeric, 'V'=variable-length)
    [4]     : 0x00
    [5]     : element_size in bytes
    [6..15] : 10 zero bytes
    [16..19]: 0xFF 0xFF 0xFF 0xFF (sentinel)
    [20..23]: element_size again (LE32)
    [24..31]: 8 zero bytes
```

**Example — BKINC.RUN IC Library buffer cluster** (confirmed Pass 351):
| Name | Type | Size | Purpose |
|------|------|------|---------|
| `BKICLOC.H` | I | 5 | IC Location handle array |
| `BKICL_JITPRG` | A | 10 | JIT Program code for current IC Location item |
| `BKICL_BUFF` | A | 255 | IC Location read buffer |
| `BKICL_REC` | R | 10 | IC Location record pointer |
| `BKIC.LOC.KEY` | V | 25 | IC Location composite key |
| `BKICMSTR.H` | I | 5 | IC Master handle array |
| `BKIC_JITPRG` | A | 10 | JIT Program code for current IC Master item |
| `BKIC_BUFF` | A | 255 | IC Master read buffer |
| `BKIC_REC` | R | 10 | IC Master record pointer |

The `BKICL_` prefix = BK IC L-ibrary shared buffer. This namespace appears in 200+ programs
(all modules that process IC items: AP, WO, SO, PO, BM, IN, SC, DC, HH, …).

**`BKICL_JITPRG` is NOT a database table** — it is this in-program variable (10-char alpha)
holding the JIT scheduling program code for the current IC item. Not present in the 659-table
DDF because it mirrors a field embedded in `BKIC_PROD_EXTRA` (100-byte extension area) rather
than being registered as a named DDF column.

---

## Three-Zone Data Channel Architecture (Pass 363 — 2026-06-29)

The **data channel** spans from `0x0200` to `h[0x08]-1`. It is divided into three physically
contiguous zones with distinct roles:

### Zone 1 — Static Header + Table Name Registry (`0x0000`–`0x01FF`)

Bytes `0x00`–`0x7F`: file header (see §Header). Bytes `0x80`–`0x1FF`: table name registry —
`h[0x0C]` bytes total, each slot 16 bytes wide (up to 15 ASCII chars right-padded with `0x00`).
All `open TABLE lock N` source statements compile into slots here — NOT into runtime instructions.

### Zone 2 — Zero-Filled Runtime Buffers (`0x0200`–`CODE_START + instruction_stream_bytes - 1`)

The instruction stream starts at `CODE_START = 0x6C0`. Each instruction has `addr` pointing to
its data record somewhere in the data channel. For **main-program instructions** (I#0 through the
subroutine transition), addr points into the preamble + zero-fill region. These data records are
**ZERO at compile time** — they are runtime-allocated variable storage. Reading them from the file
yields all zeros (not meaningful static content).

A **5-byte gap** separates the instruction stream end from the post-instruction data:
`00 FE 00 00 00` at `instruction_stream_end` to `instruction_stream_end + 4`.

### Zone 3 — Post-Instruction Static String Data (`instruction_stream_end + 5` to `h[0x08] - 1`)

For **subroutine-body instructions** (I#transition through I#N-1), addr points into this zone.
These records contain real static data: string literals, subroutine descriptor bytes, etc.
The data channel end marker `h[0x08]` is exactly `last_data_record_start + last_b2`.

**h[0x08] confirmed for two files:**
| File | h[0x08] | instruction_stream_end | zone3_start |
|------|---------|----------------------|-------------|
| BKMRF.RUN | 0x909D | 0x4EE2 | 0x4EE7 |
| BKLME.RUN | 0x830B | 0x4128 | 0x412D |

### Zone 4 — Post-Data-Channel Field Definitions (`h[0x08]` to end of file)

Beyond the data channel, a separate zone holds compiled ENTER field definitions and screen layouts.
Format: TAS string records `41 00 NN_lo NN_hi [NN bytes of string data]`. These encode field prompts,
help strings, validation messages — the compile-time form layout separate from the runtime instruction
stream. Not addressed by any instruction's `addr` field (they are accessed by a different mechanism).

**BKMRF post-data-channel example** (starting at `0x909D`):
```
41 00 01 00 5A         → 1-char string: "Z"
41 00 07 00 ...        → 7-char string: "BKMRPSW"
41 00 04 00 ...        → 4-char string: "DONE"
```

### Subroutine Structure

Subroutines sit in the upper portion of the instruction stream (I#transition to I#N-1). Each
subroutine begins with **OP_49=FUNC_ENTRY(b2=9)** and ends with **OP_20=RET_FUNC(b2=5)**.

```
[OP_20 b2=5]          ← end of prior subroutine (or end of main program)
[OP_49 b2=9]          ← subroutine entry: 9-byte descriptor in zone3
  [body instructions] ← instructions with addr pointing into zone3 static data
[OP_20 b2=5]          ← end of this subroutine
[OP_49 b2=9]          ← next subroutine entry
  ...
```

**BKMRF transition at I#1327** (first instruction with zone3 data); **BKLME transition at I#1169**.

**Library subroutines:** `#LIB includes` compile their library function bodies into this same
subroutine area — NOT as inline main-program instructions. The 20 preamble instructions (I#0–I#19)
are runtime-generated startup sequences (header scan + table registry scan), not library code.

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

## Cross-File Corpus Analysis (Pass 356 — 2026-06-26)

Analyzed 5 Rosetta Stone pairs (BKAWLB, BKLME, BKMRF, BKROA, BKDCA2~1) + 397 `.RUN` files from `samples/`.

### Universal instruction start at 0x06C0

**Confirmed across 374/397 files (94.2%):** the non-null instruction stream always begins at absolute
file offset `0x06C0 = 1728 bytes`.

Outliers (23 files):
- **19 small files** (3,322–5,054 bytes) — stub programs whose early null-fill runs into the first 20
  test windows, but their opcodes still originate at 0x6C0.
- **3 × T6EDI*.RUN** (215K–262K bytes: `T6EDIE.RUN`, `t6edib.RUN`, `t6ediex.RUN`) — EDI-related programs
  with a different/longer header. These three are the only confirmed exceptions.

**Corollary:** For any standard `.RUN` file, you can safely start parsing instructions at `0x6C0`
without needing to compute the `0x80 + h[7]×16 + h[6]` formula.

### Cross-file opcode frequency (13,489 instructions, 5 files)

95 unique opcodes observed. Top 25 by frequency:

| Opcode | Count | Pct | Name (if known) |
|--------|-------|-----|-----------------|
| `0x0F` | 5058 | 37.5% | ASSIGN |
| `0x3B` | 1966 | 14.6% | COND_BRANCH |
| `0x20` | 651 | 4.8% | RET_FUNC |
| `0x42` | 632 | 4.7% | JMP — unconditional jump (for `else` clause and `fexit`; BKDCA I#62=L197 `else`) |
| `0x01` | 564 | 4.2% | ARG_DESC |
| `0x4B` | 419 | 3.1% | CALL_LIB |
| `0x06` | 267 | 2.0% | CLR |
| `0x45` | 256 | 1.9% | FOR_LOOP (b2=5; used at both `for(...)` setup and `next` increment) |
| `0x37` | 206 | 1.5% | TRAP |
| `0x16` | 182 | 1.3% | GOTO — explicit `goto LABEL`; BKDCA I#42=L169 `goto NO.EN.SHFT` |
| `0x65` | 170 | 1.3% | FIELD_CALLBACK |
| `0x49` | 160 | 1.2% | FUNC_ENTRY (subroutine entry marker — see §Three-Zone Architecture) |
| `0xBE` | 142 | 1.1% | PMSG |
| `0x0E` | 134 | 1.0% | ENTER |
| `0x6A` | 131 | 1.0% | GOTO_LABEL |
| `0x15` | 119 | 0.9% | GOSUB — subroutine call; BKLME I#83=L222 `gosub PRT_TOF` |
| `0x4A` | 98 | 0.7% | QUIT (b2=9; confirmed I#1787 BKAWLB=L426 `quit`; high count from library includes — Pass 362) |
| `0x8A` | 98 | 0.7% | ? (b2=9, invariant) |
| `0x1A` | 97 | 0.7% | FIND_BASIC (b2=**33** ← freq-table b2 was wrong; `find F srch FIELD` no-qualifier; BKDCA I#19=L118 — Pass 362) |
| `0x43` | 90 | 0.7% | ARRAY_FLD_BEGIN (b2=9; always [OP_43][ASSIGN][OP_47]; database field array subscript — before ASSIGN of MTIC.PROD.RCOST[N] etc.; local-var arrays use plain ASSIGN instead — Pass 367) |
| `0x31` | 88 | 0.7% | ? (b2=16, invariant) |
| `0x53` | 84 | 0.6% | ENTER_FIELD_FULL |
| `0x48` | 83 | 0.6% | LOOP_BODY_ENTRY (b2=25; appears ONLY at `for(...)` declaration, never at `next`; marks loop-body start — Pass 364/367) |
| `0x2D` | 83 | 0.6% | CALLBACK_RET — stores callback return value; appears as [OP_2D][RET_FUNC] (terminal) or [OP_2D][GOTO exit] (non-terminal); b2=6 |
| `0x47` | 83 | 0.6% | ARRAY_FLD_END (b2=9; paired with OP_43: [OP_43][ASSIGN][OP_47]; database field array subscript close — Pass 367) |

Remaining 70 opcodes appear at <0.6% each; total unique = 95.

**Pass 362 updates:** OP_4A=QUIT confirmed; OP_1A=FIND_BASIC confirmed (b2=33, freq-table had wrong b2); OP_40=OPEN_R confirmed (same b2=53 as OP_1F); OP_71 renamed CHK_PARAM (appears at I#1 in all programs = entry param check); OP_48=PUSH and OP_57=EXEC_FORM removed from unknowns list (already confirmed).

**Pass 363 updates:** OP_02=CLRSCR(b2=0) confirmed — source L161 `clrscr` → BKMRF I#26 OP_02. OP_49 renamed from READ_PROP to FUNC_ENTRY(b2=9) — appears at every subroutine boundary immediately after OP_20=RET_FUNC; contains 9-byte subroutine descriptor. Three-zone data channel architecture confirmed (see §Three-Zone Data Channel Architecture below).

**Pass 364 updates (2026-06-29):** OP_15=GOSUB confirmed — BKLME I#83=L222 `gosub PRT_TOF`; b2=4 invariant. OP_42=JMP confirmed (was "GOSUB/FIELD_TERM" in frequency table) — BKDCA I#62=L197 `else`; compiler-inserted unconditional jump for `else` and `fexit`; b2=4. OP_16=GOTO confirmed (strong inference) — BKDCA I#42=L169 `goto NO.EN.SHFT`; explicit programmer `goto LABEL`; b2=4. OP_45=FOR_LOOP inferred — BKDCA for-loop structure at I#35 (`for(i;1;3;1)`) and I#40 (`next`); b2=5. Key distinction: OP_42(JMP) is compiler-generated structured flow; OP_16(GOTO) is explicit unstructured programmer goto.

**Pass 365 updates (2026-06-29):** OP_A1(b2=0)=LABEL_MARKER inferred — zero-width data record, always appears immediately before RET_FUNC sharing the same data channel addr; marks goto-target labels (exit points) inside callback functions. OP_2D(b2=6)=CALLBACK_RET inferred — stores callback function return value (.T./.F. equivalent); observed as [OP_2D][RET_FUNC] (terminal exit) and [OP_2D][GOTO] (non-terminal branch to shared exit label). OP_32(b2=6)=CALLBACK_SEP inferred — appears immediately after RET_FUNC before next FUNC_PRE or ARG_DESC+ENTER; separates successive callback function blocks in enter-field sequences. OP_43(b2=9)/OP_47(b2=9) always appear as pair [OP_43][ASSIGN][OP_47] in data-processing loops (zone3 and main body); identical data records across files = shared library operation; semantics still unknown. OP_29(b2=5) always precedes FOR_LOOP; count=13 identical across all 5 sample files = shared library subroutine; semantics unknown.

**Remaining unknowns (Pass 365):** OP_25, OP_22, OP_43, OP_5D, OP_56, OP_1B, OP_44, OP_47, OP_19, OP_29, OP_8D — ~11 unknowns remain (OP_32+OP_2D inferred, OP_A1 newly identified; down from 13 in Pass 364). OP_93/65/53 blob internal layout unknown; T6EDI* header format different from standard.

**Pass 366 updates (2026-06-29):** OP_8D(b2=20) structural pattern confirmed via BKDCA full-instruction-range analysis. OP_8D always appears as part of a **[CALL_LIB][OP_8D]** pair immediately before RET_FUNC in enter-field callback sequences. Together the pair pre-registers a 4-instruction CONTINUATION BLOCK: CALL_LIB (data=`00 00` prefix + embedded-ASSIGN ref) registers block[0]; OP_8D (data=20-byte block of 3×7-byte embedded instruction refs) registers block[1..3]. The 4 embedded addresses point to **DISTANT non-adjacent instructions** (e.g., I#393→points to I#604-607 which are 211 instructions away; I#495→points to I#826-829 which are 332 instructions away). All address chains are sequentially verified (addr[k+1] = addr[k] + b2[k]). Interpretation: **DISPATCH_CONT** — dispatch continuation registration; the TAS runtime dispatches to the pre-registered block when the current callback exits via RET_FUNC. I#1721 (after OP_53 in ENTER cluster) is a distinct context and may represent a variant use of OP_8D. I#236's data does not parse cleanly and may be a library-call variant. Confidence: 65/100 — 3 clean instances confirmed; 2 anomalous instances unexplained.

**Pass 367 updates (2026-06-29):** 6 new opcode mappings confirmed; pfmt/pblnk corrected.
- **OP_25(b2=10) = PFMT** — `pfmt N` (set print format line): 8 in BKLME = 8 `pfmt` in source (exact count match). CORRECTS Pass 243 which incorrectly stated pfmt→zero instructions.
- **OP_22(b2=10) = PBLNK** — `pblnk N` (print blank lines): 7 in BKLME = 7 `pblnk` in source (exact count match). CORRECTS Pass 243 which incorrectly stated pblnk→zero instructions.
- **OP_0C(b2≈6) = DEL_REC** — `del TABLE nocnf`: 1 in BKLME = 1 `del INVTXN nocnf` in source (exact count match).
- **OP_43(b2=9) = ARRAY_FLD_BEGIN** — always appears as [OP_43][ASSIGN][OP_47] triple; marks start of a database-table field array subscript access (e.g., `MTIT.STDCST=MTIC.PROD.RCOST[13]`, `BKYS.GLNUM[5]`). Local-variable arrays (e.g., `QTY.A[isct]=0`, `MEMORY1[1]="ADJUSTMT"`) compile to plain ASSIGN with no bracketing opcodes.
- **OP_47(b2=9) = ARRAY_FLD_END** — closing partner of OP_43; always [OP_43][ASSIGN][OP_47].
- **OP_29(b2=5) = ARRAY_ITER_INIT** — appears immediately before FOR_LOOP (at `next` statements) and immediately before OP_43 (for direct array element access); count=13 in both BKDCA and BKLME matching each instance of OP_43 or array-for-loop; related to TAS Pro's linked-list array model requiring iteration to reach element N.
- **FOR_LOOP dual-use confirmed**: OP_45(b2=5) used at BOTH `for(var;start;end;step)` declaration AND at `next` (increment + loop-back). OP_48 appears ONLY at the `for()` declaration (= LOOP_BODY_ENTRY marker); never at `next`.
- **pfmt/pblnk CORRECTION**: Both do compile to instructions (OP_25, OP_22). BKAWLB PRT_TOF (8 pfmt + 2 pblnk + 1 assign + 1 ret) compiles to 12 instructions, not 2 as claimed in Pass 243.

**Remaining unknowns (Pass 367):** OP_5D, OP_56, OP_1B, OP_44, OP_19 — **5 unknowns remain** (down from 10 in Pass 366). Note: OP_22 count in BKLME=7 exactly matches `pblnk` count but ≈ `rcn` count (8 lines, some with double `rcn` token); pblnk interpretation preferred for exact match. OP_07(b2=22) — 22-byte records, NOT in unknowns; pattern 22=3×7+1 suggests embedded instruction triple + 1 extra byte.

---

## References

- Source: `samples/rosetta/BKAWLB.SRC`
- Binary: `samples/rosetta/BKAWLB.RUN`
- Analysis script: `scripts/analyze_run.py`
