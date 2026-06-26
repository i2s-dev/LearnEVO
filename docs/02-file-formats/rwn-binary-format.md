# `.RWN` Binary Format (TAS Pro 7 Compiled Program)

Status: partial — header confirmed, symbol tables confirmed, pool decoded, 60+ opcodes observed, sub-code families mapped, pool confirmed at 2875-instr + 2669-instr scale; OP_1A/OP_31 behavioral patterns documented; branch target encoding still requires tp7runtime.exe, C:78/100
Last updated: 2026-06-26

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
0x6C0*      hdr[0x00] bytes         Dispatch / instruction table (8-byte entries)
var         var                     Pool / data section (typed values + compound blobs)
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
| 0x18   | 0x0000_120C = 4,620 | 0x0000_120C = 4,620   | Byte offset of first non-TEMP variable (= 60 × 77 — TAS Pro 7 always allocates 60 TEMP vars?) |
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

## Dispatch / Instruction Table (offset 0x6C0)

Each entry is **8 bytes**: `[op:1][b1:1][b2:1][sub:1][pool_offset_LE32:4]`.

**Instruction word encoding:**
- Byte 0: **opcode** — the operation
- Byte 1: **b1** — appears to always be 0x00 (not yet characterized)
- Byte 2: **b2** — **universally 0x00** across 3,204,306 instructions in 1,119 programs (one exception: 0x57 EXECUTE_FORM has b2=0xFE when launching the main/top-level form, b2=0x00 for sub-form launches)
- Byte 3: **sub-code** — groups related opcodes into families (see Sub-Code Families below)
- Bytes 4–7: **pool_offset** (LE32) — byte offset into the pool section (for data ops), or a branch target value (for control-flow ops — see branch encoding note)

**Dispatch table starts at program offset 0x6C0 (confirmed universal across all 1,119 programs examined).**

In `.dec` files (output of `scripts/rwn_decrypt.py`), the file has an 8-byte validation prefix prepended,
so: file_offset(dispatch) = 8 + 0x6C0 = 0x6C8.

Null terminator: `00 00 00 00  00 00 00 00`

---

### Sub-Code Families (confirmed at 3.2M instruction scale, Pass 229)

The sub-code byte groups opcodes into functional families. Every opcode within a family shares the same sub-code:

| Sub  | Count    | Family description | Key opcodes |
|------|----------|--------------------|-------------|
| 0x0A | 1,462K   | **ASSIGN** — variable and property assignment | 0x0F(1.4M), 0x8A(18K), 0x37(11K), 0x56(6.6K) |
| 0x04 | 592K     | **CALL** — procedure calls and library calls | 0x42(549K), 0x45(21K), 0x16(18K), 0x15(17K), 0xC0(4K) |
| 0x14 | 544K     | **BRANCH** — all control flow | 0x3B(462K), 0x6A(41K), 0xD2(23K), 0x19(13K), 0x93(4.6K) |
| 0x05 | 163K     | **FORM** — UI form lifecycle | 0x20(143K), 0x57(11K), 0xD1(4.9K), 0x29(4K) |
| 0x21 | 46K      | **EVAL** — expression evaluation | 0x1A(46K) |
| 0x36 | 35K      | **EXIT** — program/proc exit | 0x40(35K) |
| 0x0F | 37K      | **READ** — property/field reads | 0x49(30K), 0x0C(5.4K), 0xCC(1.3K) |
| 0x06 | 49K      | **FIELD I/O** — DB field access | 0x06(28K), 0x08(19K), 0xB7(820), 0xBD(791) |
| 0x10 | 43K      | **STATUS** — status/flag operations | 0x31(23K), 0xD3(10K), 0x11(8K), 0xCD(1.7K) |
| 0x19 | 39K      | **VAR MGMT** — push/pop and var ops | 0x48(16K), 0xDC(16K), 0xC7(7.4K) |
| 0x09 | 49K      | **HANDLE** — resource handle ops | 0x4B(25K), 0x4A(12K), 0x43(5K), 0x47(4.9K), 0x46(2.5K) |
| 0x2B | 23K      | **FIELD ACCESS (sub-group)** | 0x89(23K) |
| 0x00 | 12K      | **SET** — unconditional set ops | 0xB9(11K) |
| 0x0B | 7K       | **UNKNOWN** | 0x38(7K) |
| 0x15 | 3K       | **RETURN** | 0x30(3K) |
| 0x0C | ~1K      | **DB NAVIGATE** | 0x9A(db ops) |

**KEY DISCOVERY — 0x48 and 0xDC are perfectly paired operations:**
- 0x48 appears exactly 16,125 times in exactly 948 files
- 0xDC appears exactly 16,121 times in exactly 948 files (4-count rounding difference)
- Both have sub=0x19 (VAR MGMT family)
- This strongly implies 0x48=PUSH and 0xDC=POP (or START_BLOCK/END_BLOCK equivalent)

---

### Opcode Table (Pass 229 — 1,119-program frequency analysis + disassembly)

Top opcodes by frequency across 3,204,306 instructions in 1,119 .dec files:

| Opcode | sub  | Freq     | Coverage | Meaning | Confidence |
|--------|------|----------|----------|---------|------------|
| 0x0F   | 0x0A | 1,437K (44.85%) | 1119/1119 | **ASSIGN** — assign value/property | 95% |
| 0x42   | 0x04 | 549K (17.16%) | 1119/1119 | **GOSUB / CALL PROC** — call procedure | 90% |
| 0x3B   | 0x14 | 462K (14.43%) | 1119/1119 | **COND_BRANCH** — conditional jump | 95% |
| 0x20   | 0x05 | 143K (4.46%)  | 1118/1119 | **CREATE/BIND** — load DFM / bind event handler | 95% |
| 0x1A   | 0x21 | 46K (1.46%)   | varies    | **EVAL** — expression evaluation (intermediate) | 70% |
| 0x6A   | 0x14 | 41K (1.29%)   | varies    | **GOTO_LABEL** — jump to named label (pool string) | 85% |
| 0x40   | 0x36 | 35K (1.10%)   | varies    | **EXIT** — end program / return code | 90% |
| 0x49   | 0x0F | 30K (0.96%)   | varies    | **READ_PROP** — read named property (pool string → value) | 80% |
| 0x06   | 0x06 | 28K (0.88%)   | varies    | **FIELD_READ** — read DB field value | 65% |
| 0x4B   | 0x09 | 25K (0.81%)   | varies    | **OPEN_FORM** — open/load DFM form (cf. 0x20 CREATE) | 70% |
| 0xD2   | 0x14 | 23K (0.74%)   | varies    | **GOTO** — unconditional jump | 85% |
| 0x31   | 0x10 | 23K (0.73%)   | varies    | **GET_STATUS** — read status flag | 60% |
| 0x45   | 0x04 | 21K (0.67%)   | varies    | **CALL_LIB2** — library call variant | 55% |
| 0x08   | 0x06 | 19K (0.62%)   | varies    | **FIELD_WRITE** — write DB field value | 65% |
| 0x16   | 0x04 | 18K (0.58%)   | varies    | **CALL_LIB** — external library/system call | 55% |
| 0x8A   | 0x0A | 18K (0.56%)   | varies    | **ASSIGN2** — assign variant (conditional?) | 65% |
| 0x48   | 0x19 | 16K (0.50%)   | 948/1119  | **PUSH** — push value onto stack | 70% |
| 0xDC   | 0x19 | 16K (0.50%)   | 948/1119  | **POP** — pop value from stack | 70% |
| 0x57   | 0x05 | 11K (0.35%)   | 1119/1119 | **EXECUTE_FORM** — run form event loop (ShowModal) | 99% |
| 0x37   | 0x0A | 11K (0.34%)   | varies    | **ASSIGN_EXPR** — assign expression result | 60% |
| 0x19   | 0x14 | 13K (0.40%)   | varies    | **LOOP** — loop-back jump | 65% |
| 0x89   | 0x2B | 23K          | varies    | **GET_FIELD** — get specific field (context TBD) | 60% |
| 0xB9   | 0x00 | 11K          | varies    | **SET_FIELD** — set specific field (pairs with GET_FIELD) | 60% |
| 0x11   | 0x10 | 8K           | varies    | **STATUS_CHECK** — status check variant | 55% |
| 0x30   | 0x15 | 3K           | varies    | **RETURN** — return from procedure | 85% |
| 0x15   | 0x04 | 17K          | varies    | **TERMINATE** — terminate (variant of CALL family) | 60% |
| 0x29   | 0x05 | 4K           | varies    | **FORM_OP** — form operation (FORM family) | 55% |
| 0x71   | 0x05 | varies       | varies    | **EXIT2** — exit variant | 80% |
| 0x9A   | 0x0C | varies       | varies    | **DB_READ** — read from database file | 75% |

### Additional Opcodes from T7FOD (Pass 312 — 2875-instruction corpus, semantics TBD)

T7FOD.RWN.dec (276,693 bytes, 2875 instructions, 1479 vars, 103 procs) adds 31 new opcodes to the
observed set. Instruction stream: 0x6C8 – 0x609F (8-byte format, all b1=0x00). Pool at 0x60A0.

| Opcode | sub | Count | Notes |
|--------|-----|-------|-------|
| 0x2A   | 0x1A | 31 | High frequency — likely CALC or comparison operator |
| 0xC7   | 0x19 | 21 | Possibly PUSH variant (sub=0x19 same as PUSH/POP family) |
| 0x4A   | 0x09 | 15 | READ family (sub=0x09 same as READ_PROP 0x49) — READ variant |
| 0xD3   | 0x10 | 12 | STATUS family (sub=0x10 same as GET_STATUS 0x31) — variant |
| 0xA1   | 0x00 | 11 | Unusual sub=0x00 — special operation (EXIT/TERM candidate) |
| 0x5C   | 0x0C | 8  | DB family (sub=0x0C same as DB_READ 0x9A) — DB variant |
| 0x56   | 0x0A | 8  | ASSIGN family (sub=0x0A) — ASSIGN variant |
| 0x93   | 0x14 | 5  | BRANCH family (sub=0x14); also in .RUN as FIELD_ENTER_BODY |
| 0xC0   | 0x04 | 5  | CALL family (sub=0x04) — CALL variant |
| 0x0C   | 0x0F | 5  | READ sub-family? |
| 0x5A   | 0x25 | 5  | Unknown sub=0x25 |
| 0x5B   | 0x1E | 4  | Unknown sub=0x1E |
| 0x47   | 0x09 | 2  | READ family (sub=0x09) |
| 0x43   | 0x09 | 2  | READ family (sub=0x09) |
| 0xDA   | 0x0A | 2  | ASSIGN family |
| 0x1D   | 0x1A | 2  | Same sub as 0x2A; possibly paired |
| 0x2B   | 0x06 | 3  | FIELD family (sub=0x06) |
| 0x44   | 0x05 | 1  | FORM family (sub=0x05) |
| 0x46   | 0x09 | 1  | READ family |
| 0x4A   | 0x09 | — | (see above) |
| 0x6D   | 0x23 | 1  | Unknown |
| 0xB7   | 0x06 | 1  | FIELD family |
| 0xBD   | 0x06 | 1  | FIELD family |
| 0xC6   | 0x0F | 1  | READ sub-family? |
| 0xCC   | 0x0F | 1  | READ sub-family? |
| 0xCD   | 0x10 | 1  | STATUS family |
| 0xD1   | 0x05 | 1  | FORM family |
| 0xD9   | 0x07 | 1  | Unknown |
| 0x0B   | 0x0A | 1  | ASSIGN family |
| 0x12   | 0x0A | 1  | ASSIGN family |
| 0x2C   | 0x32 | 1  | Unknown |
| 0x34   | 0x15 | 1  | RETURN family (sub=0x15 same as RETURN 0x30) |

**Pool confirmation from T7FOD (Pass 312):** The flat-byte-stream pool structure
(type tags 0x41/0x43/0x46/0x4E/0xFF/0xFD) confirmed at 2875-instruction scale.
Pool starts at 0x60A0; first entry = STRING "T7FOD.DFM" (0x09 bytes at pool+4).
ISTS customization marker at pool+0x4A: " - ISTS Enhancement 06/02/16".

---

### Additional Observations from T7FOE (Pass 354 — 2669-instruction corpus)

T7FOE.RWN.dec (265,362 bytes, 2669 instructions) — "FO-E Print Option Where Used" report program.
Instruction stream: 0x6C8 – 0x5A2F (8-byte format). Pool at 0x5A30.
Pool[0] = STRING "T7FOE.DFM" (9 bytes). Pool[0x31] = " - ISTS Enhancement 06/03/16".

**Frequency distribution in T7FOE (top opcodes):**

| Opcode | sub  | Count | Meaning (vs. 3.2M analysis) |
|--------|------|-------|-----------------------------|
| 0x0F   | 0x0A | 1282  | ASSIGN — dominant opcode, 48% of all instructions (consistent with 44.85% at scale) |
| 0x42   | 0x04 | 445   | GOSUB/CALL PROC — 1 in 6 instructions is a procedure call |
| 0x3B   | 0x14 | 362   | COND_BRANCH — 2nd most common after ASSIGN |
| 0x20   | 0x05 | 114   | CREATE/BIND — many event handler bindings |
| 0x1A   | 0x21 | 33    | EVAL — see below |
| 0x6A   | 0x14 | 28    | GOTO_LABEL |
| 0xD2   | 0x14 | 27    | GOTO |
| 0x49   | 0x0F | 27    | READ_PROP |
| 0x40   | 0x36 | 26    | EXIT |
| 0x31   | 0x10 | 13    | GET_STATUS — see below |

**OP_1A (EVAL, sub=0x21) new behavioral observations:**
- 33× in T7FOE; pool poff sometimes points to STRING entries containing property names
  - I#1198: EVAL → pool STRING "Signature10"
  - I#1798: EVAL → pool STRING "Notes SHIP VIA"  
  - I#927:  EVAL → pool STRING "Signature8" (nearby context)
  - I#1305: EVAL near OP_42 → STRING "INB" (subprogram ref)
- Pool STRING data for EVAL is a **named accessor**: property name, column name, or procedure name
- Often appears immediately after OP_3B (conditional branch lands on EVAL)
- Sometimes appears in consecutive pairs (I#97+98, I#167+168, I#1798+1803)
- Pool poff=null (0x00) type = pointer falls inside another pool entry's data (inline argument)
- Confirms "intermediate expression evaluation" role — evaluates a named property or expression

**OP_31 (GET_STATUS, sub=0x10) new behavioral observation:**
- 13× in T7FOE — CONSISTENT STRUCTURAL PATTERN observed for all 13 occurrences:
  ```
  [OP_42 = CALL PROC]
  [OP_31 = GET_STATUS]     ← always sandwiched between two GOSUB/CALL operations
  [OP_42 = CALL PROC]
  ```
- This confirms GET_STATUS = check result/status of the preceding operation; result feeds next call
- poff may be NULL (result goes to implicit stack) or a BLOB (argument block for the status check)
- Shares sub=0x10 with OP_D3 (STATUS variant, 12× in T7FOD) and OP_11 (STATUS_CHECK, 8K at scale)

**Notable program-wide semantic observations (Pass 229 disassembly):**

- **0x57 with b2=0xFE** = top-level form execution (main window); b2=0x00 = sub-form or dialog
- **0x49 READ_PROP** reads pool string as property name → checks system property by name
  - Example: EVOMENU_SELCOMP [0]: `READ_PROP("NOVAZYGANDISTECHSUPPORT")` — checks tech-support mode flag
  - Followed by COND_BRANCH to skip multi-company selection when in tech-support mode
- **0x6A GOTO_LABEL** with pool string = jump to named label (e.g., STR("Items"))
- **0x4B OPEN_FORM** appears in place of 0x20 CREATE/BIND in some programs — distinction TBD (open existing vs create new instance?)
- **ISTS customization marker**: programs modified by i2 Systems start with `ASSIGN " - ISTS Enhancement MM/DD/YY"` as instruction [0] (confirmed in EVODEFPRINT.RWN)
- **Source file types**: .SRC-compiled programs have full proc names; EVO.LIB-compiled programs have garbled/blank proc names (1865-instr EvoChangePass uses EVO.LIB); NZLICE.LIB is Novazygandis license library

---

### Branch Target Encoding (OPEN QUESTION)

For branch-family opcodes (sub=0x14: 0x3B COND_BRANCH, 0x6A GOTO_LABEL, 0xD2 GOTO, etc.),
the poff field encoding varies by opcode.

**What is known (Pass 241, 2026-06-24):**
- 0x6A GOTO_LABEL: poff IS a pool byte offset → points to a STRING pool entry (label name). Runtime resolves label name → instruction address.
- 0x49 READ_PROP: poff IS a pool byte offset → points to a STRING pool entry (property name). Confirmed: EVOMENU_SELCOMP [0] poff=0 → STRING "NOVAZYGANDISTECHSUPPORT". ✓
- 0x20 CREATE/BIND (form creation, poff=0): poff IS a pool byte offset → points to a STRING pool entry (DFM filename). Confirmed: T7COLORS [0] poff=0 → STRING "T7COLORS.DFM". ✓
- 0x3B COND_BRANCH: poff is NOT a pool byte offset in the same sense. Confirmed: for EVOMENU_SELCOMP [1] poff=19, pool[19]='H' (byte 15 of "NOVAZYGANDISTECHSUPPORT"), NOT at an entry boundary. For 8 similar DC programs (T7DEBE etc.) with 15 instructions and COND_BRANCH at instruction [14], poffs are 206, 503, 537, 719 — completely different values for programs with the same instruction count.
- 0x20 CREATE/BIND (event handler bindings, poff > 0): poffs 9, 18, 27, 36... in T7COLORS and EvoDCmenu don't land at pool entry boundaries either. These may use poff as an event handler ID or method index, NOT as a pool byte offset.

**Ruled out:**
- poff as instruction index (0x3B poff=291 for EVOMENU_SELCOMP instruction [13] → #291, out of range for 44 instructions)
- poff as byte offset from dispatch start (non-8-aligned)
- poff as instruction index packed in low byte (poff=388, low byte=0x84=132, invalid)

**Refined hypothesis (Pass 242, 2026-06-24 — suwin6t.rwn deep analysis)**:

Each opcode type uses poff to point to a SPECIFIC BYTE WITHIN a pool entry, not uniformly to the entry start:
- 0x49 READ_PROP: poff → type byte (0x41) = entry start (header+0)
- 0x20 CREATE/BIND form creation: poff → type byte (0x41) = entry start (header+0)  
- 0x20 CREATE/BIND event bindings: poff → content start = header+4 (e.g., suwin6t [68] poff=1074 → pool[1074]='F')
- 0x6A GOTO_LABEL: poff → reserved byte (header+1) for "F" entry; poff → content start (header+4) for "*.*" entry — inconsistent, may indicate poff semantics differ even within GOTO_LABEL by sub-variant
- 0x0F ASSIGN, 0x42 GOSUB, 0x3B COND_BRANCH: poff → into compound blob body (not a STRING entry boundary)

**Evidence from suwin6t.rwn (95,262 bytes, 729 instructions)**:
- GOTO_LABEL [57] poff=901: STRING "F" header at pool[900], poff=901 = header+1
- GOTO_LABEL [66] poff=1041: STRING "*.*" header at pool[1037], poff=1041 = header+4 (content start)
- CREATE/BIND [68] poff=1074: STRING "F" header at pool[1070], poff=1074 = header+4 (content start)
- ASSIGN [0] poff=0: STRING "NZISSHOULDLOCKTHESCREENCOMPLETELY" header at pool[0], but poff=0 = header+0

**Pool readable strings in suwin6t** (screen-lock / session auth purpose confirmed):
- pool[0]: "NZISSHOULDLOCKTHESCREENCOMPLETELY" — lock flag variable
- pool[61]: "SUWIN6" — program name
- pool[865]: "WHOAMI.*" — reads all WHOAMI table fields
- pool[957]: "WHOAMI.DBA" — specific WHOAMI field
- pool[972]: "EVOSERVICE" (space-padded to 35 chars) — service name comparison
- pool[1041]: "*.*" — wildcard pattern
- pool[904]: "F" — boolean false constant (1-byte string)

**Instruction counting caveat**: Pool entries can start with `41 00` (STRING type + reserved byte = 0x00), which satisfies the naive b1=0x00 instruction check. Real instruction count = naive count minus any trailing 0x41/0x46/0x43/0x4E/0x52 "instructions". Confirmed across EVOMENU_SELCOMP, T7PASS, T7COLORS, EvoDCmenu, and suwin6t.

**Open**: Exact per-opcode poff delta (header+0 vs header+1 vs header+4) needs tp7runtime.exe disassembly to resolve definitively. See `research/OPEN_QUESTIONS.md`.

---

**CONFIRMED — 0x20 vs 0x57 semantic distinction (Pass 110c/110d, 2026-06-19):**
- 0x20 = CREATE/BIND: first occurrence loads DFM (TForm.Create); subsequent occurrences bind event handlers
- 0x57 = EXECUTE: enters the form's event loop (TForm.ShowModal); LAST substantive operation in most programs
- T7MSG exception: uses 0x57 alone because it has no event handlers to bind — MOUNT+EXECUTE collapsed into one step
- Sequence in a typical TAS Pro 7 program:
  ```
  [0]  0x20 poff=pool→"DFM_NAME"   # Create form from DFM file
  [1+] 0x20 poff=...               # Bind event handlers
  [n]  0x57 b2=FE poff=0           # Execute main form (ShowModal); b2=FE = main form
  [n+1] 0x40 poff=exit_code        # Program exit
  ```
- **poff interpretation by opcode family (updated Pass 242):**
  - Read opcodes (0x49 READ_PROP): poff → pool entry start (header+0, type byte = 0x41) ✓ confirmed
  - Form creation (0x20 CREATE/BIND [0]): poff → pool entry start (header+0) ✓ confirmed
  - Label opcodes (0x6A GOTO_LABEL): poff → somewhere within STRING entry (header+1 to header+4); opcode-specific delta TBD
  - Event bind (0x20 CREATE/BIND bindings): poff → content start (header+4) of STRING entry
  - Branch opcodes (0x3B COND_BRANCH, 0xD2 GOTO): poff points into compound blob body; NOT at STRING entry boundary
  - Assign/call opcodes (0x0F ASSIGN, 0x42 GOSUB): poff points into compound blob body
  - Exit opcodes (0x40, 0x71): poff may be a direct value (exit code)

---

## Pool / Data Section

Immediately follows the dispatch table (at `0x6C0 + hdr[0x00]`).

### Typed pool values

The pool is a flat byte array of **typed values**. Each value begins with a 1-byte type code:

| Type byte | ASCII | Size | Encoding | Meaning |
|-----------|-------|------|----------|---------|
| 0x41      | A     | variable | `[41][00][len16_LE][data]` | String or binary blob |
| 0x52      | R     | 5 bytes  | `[52][value32_LE]`  | Real/numeric constant |
| 0x53      | S     | 5 bytes  | `[53][value32_LE]`  | (string ref?) |
| 0x46      | F     | 5 bytes  | `[46][var_table_offset32_LE]` | Variable reference (= var_index × 77) |
| 0x43      | C     | 5 bytes  | `[43][pool_offset32_LE]`     | Pool pointer (byte offset into pool section) |
| 0x4E      | N     | 5 bytes  | `[4E][value32_LE]`  | Numeric constant |
| 0x4D      | M     | 5 bytes  | `[4D][value32_LE]`  | (type M?) |
| 0x4C      | L     | 5 bytes  | `[4C][value32_LE]`  | Logical value |
| 0x44      | D     | 5 bytes  | `[44][value32_LE]`  | Date? |
| 0x49      | I     | 5 bytes  | `[49][value32_LE]`  | Integer |
| 0xFF      | —     | 1 byte   | sentinel only       | End-of-blob sentinel |
| 0xFD      | —     | 1 byte   | marker only         | Begin-of-blob marker |

### Critical: type 0x46 (F) = variable reference

`F_value / 77 = variable_index`. The 0x46 type byte followed by `(var_index * 77)` as a LE32
references the variable at that index in the variable symbol table.

**Confirmed from suwin7.rwn:**
- `46 A6 12 00 00` = 0x12A6 = 4774 = 62 × 77 → var[62] = SERIALNUMBER
- `46 F3 12 00 00` = 0x12F3 = 4851 = 63 × 77 → var[63] = SNVALUE
- `46 59 12 00 00` = 0x1259 = 4697 = 61 × 77 → var[61] = WAIT_SECS
- `46 0C 12 00 00` = 0x120C = 4620 = 60 × 77 → var[60] = CURR_TIME
- `46 4D 00 00 00` = 0x004D = 77  =  1 × 77 → var[1]  = TEMP1
- `46 00 00 00 00` = 0x0000 = 0   =  0 × 77 → var[0]  = TEMP0

### Critical: type 0x43 (C) = pool pointer

The LE32 value is a **byte offset into the pool section** referencing another pool entry.

**Confirmed from suwin7.rwn:**
- `43 33 00 00 00` = pool[0x0033] → STR "DEMO"
- `43 5B 00 00 00` = pool[0x005B] → VALR(0)
- `43 80 00 00 00` = pool[0x0080] → VALR(800,000)
- `43 85 00 00 00` = pool[0x0085] → VALR(900,000)
- `43 73 01 00 00` = pool[0x0173] → STR "lblUserSerialNum"
- `43 87 01 00 00` = pool[0x0187] → STR "Caption"
- `43 AE 01 00 00` = pool[0x01AE] → STR "DEMO" (second 'DEMO' pool entry)

### Compound blob structure

Most pool 0x41-type entries that contain binary (non-printable) data are **compound argument blobs**.
These blobs encode the arguments for one or more dispatch table instructions.

Blob layout (data bytes, after the `41 00 len16` header):
```
FD          begin-of-blob marker
[1+ metadata bytes]   flags, arg-count, or unknown
[0x46 F entries]      variable references (= var_index × 77)
[0x43 C entries]      pool pointers (arguments by reference)
[0x4E/0x52/etc.]      inline numeric constants
FF          end-of-blob sentinel
```

Multiple dispatch entries point to different byte offsets WITHIN the same blob,
each reading the specific sub-field relevant to its operation.

**Blob example — e[3] from suwin7.rwn:**
```
FD 00 00 00 00 00 07 46 A6 12 00 00 43 33 00 00 00 00 00 00 00 00 00 FF 00
                  ^        SERIALNUMBER        ^   pool→'DEMO'          ^sentinel
                  |
                  d[5](op0x42,sub4) and d[6](op0x3B,sub0x14) point into here
```
Semantic: evaluates `SERIALNUMBER` against the string "DEMO" — likely `IF SERIALNUMBER = 'DEMO' THEN ...`

**Known semantics from suwin7.rwn blob analysis:**
- Blob with F=SERIALNUMBER + C→'DEMO': validates serial number is "DEMO"
- Blob with F=SNVALUE × 2 + C→VALR(800000) + C→VALR(900000): countdown timer comparison
- Blob with C→'lblUserSerialNum' + C→'Caption': sets `lblUserSerialNum.Caption` UI property
- Blob with C→'lblUserLicType' + C→'Caption': sets `lblUserLicType.Caption` UI property

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
| File table at offset 0x80, 16-byte entries | 100/100 | Confirmed by matching .SRC open statements |
| Header[0x14] = variable count | 100/100 | suwin7: 68 variables, header[0x14]=68 |
| Header[0x20] = variable table byte size | 100/100 | suwin7: 68×77=5236=header[0x20] |
| Header[0x0C] = procedure table byte size | 95/100 | suwin7: 3 procs × 53 bytes = 159 = header[0x0C] |
| Variable entry size = 77 bytes | 100/100 | Spacing between TEMP0/TEMP1 names confirmed = 77 |
| Variable name: non-printable byte 0 = type code | 100/100 | All TEMP* vars have byte 0 = 0x05; name verified |
| Variable name: printable byte 0 = first char of name | 100/100 | CURR_TIME, WAIT_SECS, I, LICTYPE all verified |
| Procedure entry size = 53 bytes | 95/100 | Spacing between proc names = 53 |
| Source filename = 60 bytes before var table | 100/100 | "suwin7.src" found at expected offset |
| Procedure and variable names are plaintext | 100/100 | Direct observation across 1,119 programs |
| Dispatch table starts at 0x6C0 (program-relative) | 95/100 | Confirmed in 1,119 programs; header[0x00]=dispatch size; universal |
| Instruction size = 8 bytes (uniform) | 99/100 | 3,204,306 instructions parsed at uniform 8-byte stride; disp_size always divisible by 8 |
| b2 byte (instruction byte 2) = 0x00 universally | 99/100 | 3,204,306 instructions analyzed; ONE exception: 0x57 EXECUTE_FORM has b2=0xFE for main-form launch |
| Sub-code byte groups opcodes into functional families | 95/100 | 15+ sub-code values each map consistently to a group of related opcodes across 1,119 programs |
| 0x48 (PUSH) and 0xDC (POP) are perfectly paired operations | 90/100 | Appear 16,121/16,125 times in exactly the same 948/1119 files; same sub=0x19 |
| 0x20 = CREATE/BIND, loads DFM from pool string | 95/100 | T7PASS [0]: `CREATE/BIND("T7PASS.DFM")` — direct disassembly |
| 0x57 = EXECUTE_FORM (runs form event loop) | 99/100 | Universal in 1,119/1,119 programs; T7PASS [4]: EXECUTE_FORM b2=FE |
| 0x49 = READ_PROP — reads named system property | 80/100 | EVOMENU_SELCOMP [0]: READ_PROP("NOVAZYGANDISTECHSUPPORT") followed by COND_BRANCH |
| 0x6A = GOTO_LABEL — jumps to named label (pool string) | 80/100 | EVOMENU_SELCOMP: GOTO_LABEL("Items") — label name resolved from pool string |
| Pool type 0x46 (F) = variable reference, value = var_index × 77 | 95/100 | suwin7: 6 F-values all exact multiples of 77; named vars confirmed |
| Pool type 0x43 (C) = pool pointer (byte offset into pool) | 90/100 | suwin7: 7 C-values confirmed to point to pool entry starts |
| Pool type 0x41 (A) = string, format [41][00][len16][data] | 95/100 | All strings confirmed; pool[0] for T7PASS = "T7PASS.DFM" ✓ |
| Pool fixed-width types (R=0x52,N=0x4E,S=0x53,C=0x43,F=0x46) = 5 bytes | 80/100 | Confirmed layout from symbol extraction |
| Compound blobs use FD=begin-marker, FF=end-sentinel | 85/100 | All binary BLOBs in suwin7 follow this pattern |
| .dec files have 8-byte validation prefix before program | 100/100 | rwn_decrypt.py prepends pt[0:4]=pt[4:8] validation block; all header reads need +8 offset |
| ISTS enhancement marker = `ASSIGN(" - ISTS Enhancement MM/DD/YY")` at [0] | 90/100 | EVODEFPRINT.RWN [0]: `ASSIGN " - ISTS Enhancement 06/15/17"` |
| TAS32 (old hypothesis) present in decrypted RWN | WRONG | Old analysis used sha1("mabufoju") key; TAS32 not present with correct key K_B |

---

## Extractor Script

See `scripts/rwn_extract_symbols.py` for a script that extracts procedure names,
variable names, and the source filename from any decrypted RWN file.
