# DECOMPILE-INSTRUCTIONS.md

Status: active-research | Last updated: 2026-06-12

> **DOCUMENT CONFIDENCE: 78/100**
>
> **⚠️ MAJOR CORRECTION (2026-06-12): Cipher is TDCP_twofish, NOT TDCP_3des.**
> All prior testing assumed 3DES for the .RWN decrypt path. That was wrong. Sections below
> updated accordingly. TDCP_3des is present in tp7runtime.exe but used in OTHER code paths,
> not the RWN header validation or main decrypt loop.
>
> What is verified (high confidence):
> - .RUN file format header structure (magic bytes, "TAS32q" marker, file table at 0x80) — confirmed by direct hex inspection
> - .RUN entropy (4.35 bits/byte) — confirmed; unencrypted bytecode
> - .RWN entropy (~8.0 bits/byte) — confirmed; encrypted
> - .RWN header constants: byte[11]=0x89, byte[15]=0x01 across 8 separate files — confirmed
> - Standard decompression (zlib, gzip, deflate) does not apply to .RWN — confirmed by test
> - **XOR encryption is NOT used** — tested simple XOR and repeating-key XOR (key=bytes 0–7,
>   key=bytes 8–15, key=reversed bytes 0–7); none produce TAS32 at decrypted offset 0xC5 — ruled out
> - **AES is NOT used** — AES S-box (`63 7C 77 7B...`) is absent from tp7runtime.exe — confirmed
> - **Encryption library is DCPcrypt** (David Barton's Delphi Crypto Library) — confirmed via TDS
>   debug symbols in tp7runtime.exe `.debug` section (22 MB Borland TDS format)
> - **Cipher for .RWN decryption is TDCP_twofish (Twofish)** — confirmed from VMT class name:
>   global [0x74f25c] = VA 0x74F2A8 (raw 0x34E6A8); VMT[-0x2C] → VA 0x74F308 → PShortString
>   with len=12, text='TDCP_twofish'. Instance size 0x10E8. Constructor at VMT slot 11 = VA 0x750818.
> - **TDCP_3des is present but used elsewhere** — TDS symbols confirm it; VMT at raw 0x00723694;
>   called by functions at 0x124B70 and 0x31DAC0, NOT by the RWN decrypt path
> - **SHA1 used for key derivation** — `@Tp7runtime@TDCP_sha1` confirmed; DCPcrypt's `InitStr`
>   hashes the passphrase with SHA1 to produce cipher key bytes
> - **TAS32 magic is at offset 0xC5 in the decrypted buffer** — confirmed from code analysis
>   of the validation routine (VA 0xB5C8B9): `ADD EAX, 0xC5` + `MOV ECX, 5` + `CALL 0x45a4c4`
>   (5-byte compare), three independent instances — see known plaintext anchor below
> - **Candidate passphrase confirmed from global chain** — double-dereference:
>   [0xB8B0CC] (DATA raw 0x78A2CC) = 0x00B6F454 → [0x00B6F454] (DATA raw 0x76E654) = 0x00563D84 →
>   Delphi AnsiString at 0x00563D84 = **"An error has occurred during conversion of this field
>   from alpha to the appropriate binary form."**
>   Function 0x742654 calls `LStrAsg` to overwrite its passphrase var with this string immediately
>   before calling `InitStr(twofish_cipher, passphrase)`. This is the most credible passphrase
>   candidate found so far — but NOT yet validated against T7INA.RWN (testing is next).
> - **InitStr key derivation confirmed by code inspection** (from TDCP_3des.Init at raw 0x724504):
>   - `FillChar(buf, 24, 0)` — 24-byte buffer zeroed first
>   - `Move(SHA1_output[0:20], buf, 20)` — copy 20 SHA1 bytes
>   - Result: key = SHA1(passphrase)[0:20] + `\x00\x00\x00\x00` (4 zero bytes)
>   - **Not cycling** — prior doc was wrong; padding is zeros, not SHA1[0:4]
>   - For Twofish (max 256 bits): keybits = min(160, 256) = 160; buffer likely 32 bytes;
>     SHA1[0:20] padded with 12 zero bytes
> - **Decrypt function at raw 0x742654** (VA 0x742654 relative to start of CODE at 0x400C00):
>   - Reads 8 bytes from TMemoryStream → local buffer [EBP-0x11]
>   - Creates TDCP_twofish from global [0x74f25c]; calls InitStr with passphrase string
>   - Sets cipher mode byte [EBX+0x34] = 2
>   - Calls `cipher.VMT[+0x50](buffer, buffer, 8)` → mode=2 → function at 0x74eb50
>   - Compares DWORD[EBP-0x11] with DWORD[EBP-0xd] (header validation check)
>   - If equal: enters main decrypt loop (function 0x74e374) with 0x2000-byte chunks
> - **Main decrypt loop at 0x74e374**: reads 0x2000 bytes at a time from source stream
>   (via stream VMT[+0xC]); calls `cipher.VMT[+0x50]` (mode=2) on each chunk; writes to output
>   stream via VMT[+0x10]; loops while bytesRead == 0x2000
> - **Mode=2 dispatch**: `VMT[+0x50]` checks [EAX+0x34] and dispatches:
>   - mode=0 → 0x74e7fc; mode=1 → 0x74e9ac (CFB-8 byte-by-byte); **mode=2 → 0x74eb50** (used for RWN)
>   - mode=3 → 0x74ed44
> - **File loader function** at raw 0x7424D0 (VA 0x7424D0):
>   - Creates TMemoryStream from global VMT at [0x46FCC4]
>   - Calls 0x477568 to fill stream from source file data
>   - Calls 0x742654 (decrypt/validate) with the stream
>
> What is inferred but not yet proven (medium confidence):
> - Bytes 0–7 of the .RWN header are the per-file IV (one Twofish block = 16 bytes, but
>   the code reads exactly 8 bytes before calling the cipher — may be half-block nonce)
> - Encrypted content starts at byte 16 or byte 8 (exactly where the stream pointer is after
>   the 8-byte header read; exact split needs code tracing)
> - The passphrase string at 0x00563D84 may be runtime-modified before use — [0xB8B0CC] is
>   a pointer and could be updated before function 0x742654 is called
> - Mode=2 at 0x74eb50 is CBC block mode (most common; CFB-8 is mode=1, confirmed)
> - Decrypted content structure resembles .RUN format with TAS Pro 7 extensions
>
> What is unknown (blocks reaching 100%):
> - **Whether "An error has..." passphrase produces TAS32 at decrypted offset 0xC5** —
>   cannot test until Twofish library is available in Python (pycryptodome lacks Twofish)
> - Exact cipher mode for mode=2 (function 0x74eb50 — not yet fully disassembled)
> - Whether key uses 128 or 160 effective bits (Twofish supports 128/192/256 only;
>   DCPcrypt may silently truncate 160-bit key to 128)
> - Exact .RUN bytecode section offset and opcode table — not yet mapped
>
> **Known plaintext test:** T7INA.RWN, file offset 0xD5–0xD9 (`81 BC 08 E9 3F`) must
> decrypt to ASCII "TAS32" (`54 41 53 33 32`). Decrypted offset in context buffer: 0xC5.
> The IV is bytes[0:8] = `F8 13 B6 7B 3D 24 BC 45`.
>
> **To reach 100%: test "An error has..." passphrase with TDCP_twofish + mode=2, validate
> TAS32 appears at decrypted offset 0xC5 of T7INA.RWN, then ship the decryptor.**

Authorization: Vendor has granted explicit permission to decompile. The EvoERP version
installed at \\i2s109-solidcrm\ is an older abandoned version no longer supported by the vendor.

---

## Overview

EvoERP uses two distinct compiled-program formats:

| Format | Extension | Generation | Encrypted | Count | Rosetta Stone |
|--------|-----------|------------|-----------|-------|---------------|
| TAS Pro 6 compiled | `.RUN` | BKAWLB era | No | ~7 | Yes — 7 SRC+RUN pairs |
| TAS Pro 7 compiled | `.RWN` | T7*, J7* era | **Yes** | ~1,149 | No source available |

The `.RUN` files are unencrypted bytecode and can be disassembled using the Rosetta Stone
approach. The `.RWN` files are encrypted (entropy ~8.0 bits/byte) and require decryption
before disassembly. These are separate problems with different solutions.

---

## Part 1: Disassembling `.RUN` Files (TAS Pro 6)

### What we know about the .RUN format

Confirmed by hex inspection of `BKAWLB.RUN` (139,533 bytes, entropy 4.35 bits/byte):

**Header (offset 0x00–0x7F):**
```
Offset  Size  Content
------  ----  -------
0x00    4     Magic: D9 38 00 00  (little-endian 0x000038D9)
0x04    4     Unknown DWORD (varies per file)
0x08    4     Unknown DWORD — possible bytecode section offset
0x0C    4     Unknown DWORD — possible symbol table size or count
0x10    4     Unknown DWORD
0x14    4     Unknown DWORD
0x18    4     Unknown DWORD
0x1C    4     Unknown DWORD
0x20    4     Unknown DWORD
0x24    4     0xFFFF0000 — possible sentinel / end-of-header marker
0x28    4     Unknown DWORD
0x2C    4     00 00 00 00
0x30    4     Unknown DWORD
0x34    7     ASCII string "TAS32q\0" — format/version identifier
0x3B    ...   Padding / unknown fields up to 0x7F
```

**File reference table (offset 0x80):**
Each database file the program opens is listed as a 16-byte null-padded ASCII entry.
These match the `open <FILENAME> lock N` statements in the corresponding `.SRC` exactly.

Example from `BKAWLB.RUN`:
```
0x0080: BKSYMSTR (padded to 16 bytes)
0x0090: WORKORD
0x00A0: BKICMSTR
0x00B0: BKARCUST
0x00C0: BKSYHELP
0x00D0: DBAHLPID
0x00E0: TASCOLOR
0x00F0: MTICMSTR
... (continues until a null entry terminates the table)
```

**Bytecode section:**
Begins after the file reference table (exact start offset still being mapped). The
bytecode is TAS Pro 6 p-code (pseudo-code bytecode), related to xBase/Clipper family.

---

### Step-by-step: Rosetta Stone mapping

We have 7 complete source + compiled pairs:

| Source file | Compiled file | Size (compiled) |
|-------------|---------------|-----------------|
| BKAPH.SRC   | BKAPH.RUN     | 266,998 bytes   |
| BKAPHA.SRC  | BKAPHA.RUN    | 270,995 bytes   |
| BKAWLB.SRC  | BKAWLB.RUN    | 139,533 bytes   |
| BKDCA.SRC   | BKDCA.RUN     | 230,690 bytes   |
| BKLME.SRC   | BKLME.RUN     | 127,835 bytes   |
| BKMRF.SRC   | BKMRF.RUN     | 159,375 bytes   |
| BKROA.SRC   | BKROA.RUN     | 281,173 bytes   |

Copies are in `samples/rosetta/`.

**Process:**

1. **Map the file table.** For each pair, compare the `open` statements in the `.SRC`
   against the 16-byte entries at 0x80 in the `.RUN`. Confirm that every opened file
   appears exactly once in the table, and verify the table terminator (all-zero entry).

2. **Find where bytecode starts.** After the file table (last non-zero entry + 16 bytes),
   look for the start of executable opcodes. In xBase-family bytecodes, procedures
   typically start with a `PROC` or `FUNCTION` marker opcode followed by a name string.
   Cross-reference with the procedure names in the `.SRC`.

3. **Map opcodes from known source constructs.** TAS Pro 6 source uses:
   - `define <name> type <t> size <n>` — variable declaration
   - `open <file> lock N` — open database
   - `find F srch <field> nlock` — keyed record lookup
   - `if / endif` — conditional
   - `do / enddo` / `for / next` — loops
   - `proc <name> / return` — subroutines
   - `display "text" at row col` — screen output
   - `ask <var>` — keyboard input
   - `print <field>` — report output

   For each construct in the source, find the corresponding byte pattern in the binary.
   Start with `proc` + `return` (most distinctive) and work inward.

4. **Build a lookup table.** Format: `opcode_byte → TAS Pro 6 mnemonic`. Keep a
   running `docs/rwn-opcode-table.md` as opcodes are confirmed.

5. **Write a Python disassembler.** Once ~20 opcodes are mapped, write
   `scripts/run_disasm.py` to decode `.RUN` files and emit pseudo-source.

---

### TAS Pro 6 source language quick reference

(Confirmed from inspection of the 7 `.SRC` files)

```
; comment
#UDX              — allow user-defined functions/commands
#LIB <name>       — link to a library module
#INC <name>       — include a header

define <name> type <t> size <n>       — declare variable (t: A=alpha, n=numeric, i=integer, d=date, t=time)
define <name> type <t> size <n> array <count>  — array
param <var1>, <var2>                  — declare parameters

open <file> lock N                    — open Btrieve file (N=no lock)
find F srch <field> nlock             — find by key, no lock
find N nlock                          — find next record
close <file>                          — close file

if <condition>                        — conditional start
  elseif / else / endif
for <var> = <start> to <end>          — counted loop
  next <var>
do while <condition>                  — while loop
  enddo

proc <name>                           — procedure definition
  return [<value>]
call <proc>(<args>)                   — call procedure

display "text" at <row> <col>         — write to screen
ask <var> at <row> <col>              — keyboard input
print <expr>                          — print to report
```

---

## Part 2: Decrypting `.RWN` Files (TAS Pro 7)

This is the hard problem. Every `.RWN` file is encrypted. Standard compression
(zlib, gzip, deflate) does not apply — all standard decompression attempts fail.

### What we know about the .RWN header

Confirmed by comparing 8 RWN files (T7INA, T7SOA, T7POA, T7WOA, T7APA, T7ARA,
suwin6t, suwin7):

```
Offset  Size  Content
------  ----  -------
0x00    8     Per-file value — varies entirely between files.
              Likely: encryption IV/nonce, or CRC32 + salt, or file-derived seed.
0x08    4     Unknown DWORD — varies, but high byte (byte[11]) is ALWAYS 0x89.
              Little-endian value is always in range 0x89??????.
0x0C    4     Unknown DWORD — varies, but high byte (byte[15]) is ALWAYS 0x01.
              Little-endian value is always in range 0x01??????.
0x10    ...   Encrypted content — entropy ≈ 8.0 bits/byte.
```

**Key observations:**
- Byte[11] = 0x89 across ALL known .RWN files (constant). Format marker or version byte.
- Byte[15] = 0x01 across ALL known .RWN files (constant). Likely format version = 1.
- Bytes 0–7 vary completely between files — candidate for per-file nonce/IV.
- The encryption is **NOT** a simple XOR with a fixed key — tested: key=bytes[0:8], key=bytes[8:16],
  key=reversed bytes[0:8]; none yield TAS32 at offset 0xC5. Ruled out.
- The encryption is NOT standard zlib, gzip, or deflate.
- The encryption is NOT AES (AES S-box absent from tp7runtime.exe — confirmed).
- **⚠️ CORRECTION (2026-06-12): The cipher is Twofish (TDCP_twofish), NOT 3DES.**
  TDS debug symbols confirm both TDCP_3des and TDCP_twofish are compiled into tp7runtime.exe.
  The RWN decrypt path (function 0x742654 and main loop 0x74e374) uses the class stored at
  global [0x74f25c] = VMT 0x74F2A8 = **TDCP_twofish** (class name confirmed from VMT[-0x2C]).
  TDCP_3des (VMT at raw 0x00723694) is present but used in different code paths (0x124B70, 0x31DAC0).

**Encryption model (revised, high confidence):**
```
File layout:
  [0x00–0x07]  8-byte header value (per-file; purpose: IV candidate or validation checksum)
  [0x08–0x0F]  Unencrypted header metadata (byte[11]=0x89, byte[15]=0x01)
  [0x10–EOF]   Twofish-encrypted content (mode=2 via cipher.VMT[+0x50])

Key derivation (DCPcrypt InitStr pattern, confirmed from code):
  SHA1(passphrase) → 20 bytes; FillChar(key_buf, 0) then Move(sha1, buf, 20)
  Key = SHA1(passphrase)[0:20] + zero padding (NOT cycling)
  Twofish keybits = 160 (may internally use 128 or 192 — needs testing)
  Passphrase candidate: "An error has occurred during conversion of this field
    from alpha to the appropriate binary form."  (from global chain [0xB8B0CC])
```

**Known plaintext anchor (use this to validate any candidate key):**
- File T7INA.RWN, bytes at file offset 0xD5–0xD9: `81 BC 08 E9 3F`
- These must decrypt to `54 41 53 33 32` ("TAS32")
- In the decrypted content buffer: TAS32 is at offset 0xC5 (confirmed from code at raw 0x75BCBA)

---

### Method A: Ghidra analysis of tp7runtime.exe — confirm passphrase and mode

The encryption algorithm is **Twofish (DCPcrypt TDCP_twofish)**. The leading candidate
passphrase is **"An error has occurred during conversion of this field from alpha to the
appropriate binary form."** extracted from the global pointer chain [0xB8B0CC]→[0xB6F454]→
0x00563D84. Ghidra can confirm this is the value actually passed to InitStr at runtime.

**Setup:**
1. Download Ghidra from https://ghidra-sre.org/ (NSA open-source reverse engineering tool).
   Requires Java 11+. (Note: Java 1.8 installed locally is too old — install Java 17 JDK.)
2. Create a new project. Import `C:\ISTS\tp7runtime.exe` (33,347,600 bytes, 32-bit PE).
3. Auto-analyze: accept defaults. This will take several minutes on a 33 MB binary.

**All key addresses are confirmed:**
*(raw = VA − 0x400C00 for CODE section; VA − 0x400E00 for DATA section)*
| Address (VA) | Address (raw) | What it is |
|---|---|---|
| 0x00742654 | 0x00341A54 | RWN header decrypt + validation function |
| 0x0074E374 | 0x0034D774 | Main decrypt loop (0x2000-byte chunks) |
| 0x0074E1F8 | 0x0034D5F8 | InitStr (SHA1 → cipher.Init) |
| 0x0074EB50 | 0x0034DF50 | mode=2 cipher operation (Twofish block decrypt) |
| 0x0074F2A8 | 0x0034E6A8 | TDCP_twofish VMT (class confirmed) |
| 0x00750818 | 0x0034FC18 | TDCP_twofish constructor (VMT slot 11) |
| 0x00B5C8BA | 0x0075BCBA | TAS32 validation (ADD EAX,0xC5; MOV ECX,5; CALL compare) |
| 0x00B5DE90 | 0x0075D290 | "TAS32" string (5 raw bytes) |
| 0x00563D84 | 0x00163184 | Delphi AnsiString: "An error has occurred..." (CODE section) |
| 0x00B8B0CC | 0x0078A2CC | Global pointer → [0xB6F454] → 0x00563D84 (DATA section) |

**In Ghidra:** go to `0x742654`. Decompiler pane will show the InitStr call and the
passphrase argument. Verify it resolves to the "An error has..." string. Also check whether
[0xB8B0CC] is ever written before this function is called (if yes, the pointer may be updated
to a different passphrase at runtime).

**What to confirm:**
- The passphrase string (is "An error has..." what is actually passed, or does code modify it?)
- The mode=2 function at 0x74eb50 — is it CBC, OFB, or CFB-block?
- The block offset where encrypted data begins (byte 8 or byte 16?)

**Python implementation (ready to test — needs Twofish library):**
```python
# scripts/rwn_decrypt.py
# pip install pycryptodome  (no Twofish; try: pip install pyaes or compile twofish)
# Currently testing with the twofish pure-python package or ctypes call to twofish.dll
import sys, hashlib

PASSPHRASE = b"An error has occurred during conversion of this field from alpha to the appropriate binary form."
sha1 = hashlib.sha1(PASSPHRASE).digest()   # 20 bytes
# DCPcrypt: FillChar(buf, 0) then Move(sha1, buf, 20) → 20 bytes + zero pad
# Twofish keybits = 160; actual effective bits TBD (128 or 160 depending on DCPcrypt impl)
key20 = sha1                                # 20 bytes as-is
key16 = sha1[:16]                           # truncate to 128 bits
key24 = sha1 + b'\x00' * 4                 # 192-bit: 20 bytes + 4 zeros
key32 = sha1 + b'\x00' * 12                # 256-bit: 20 bytes + 12 zeros

def try_twofish_decrypt(key, iv, ciphertext):
    """Test Twofish decryption once a library is available."""
    # TODO: replace with actual Twofish call
    # from twofish import Twofish
    # t = Twofish(key)
    # ... CBC mode decrypt using iv ...
    pass

with open("samples/rosetta/T7INA.RWN", "rb") as f:
    rwn = f.read()
iv8 = rwn[0:8]                    # first 8 bytes (IV candidate)
ct = rwn[0x10:0x10 + 0x100]      # ciphertext from byte 16, enough to cover offset 0xC5
```

**Validation:** after decryption, bytes at context offset 0xC5–0xC9 must equal `TAS32`.

---

### Method B: Runtime memory dump

If Ghidra analysis is too time-consuming, you can dump the decrypted content from memory
while `tp7runtime.exe` is running. This requires a debugger (x64dbg, WinDbg, or OllyDbg).

**Process:**
1. Launch `tp7runtime.exe` with a small test `.RWN` (e.g., `suwin7.rwn`, only 8,610 bytes).
2. Attach x64dbg before the program fully starts.
3. Set a breakpoint on `ReadFile` or `fread`.
4. When the breakpoint hits for the `.RWN` file, note the destination buffer address.
5. After the decryption loop completes (step through the code), dump the buffer to a file.
6. The dumped content is the decrypted bytecode — compare it against a `.RUN` file to
   understand the format differences between TAS Pro 6 and TAS Pro 7.

**Tool:** x64dbg (free, open source) — https://x64dbg.com/

---

### Method C: Brute-force key search — STATUS: EXHAUSTED FOR PRINTABLE STRINGS

This approach has been fully executed. Summary of what was searched and found nothing:

| Search space | Count tested | Key derivations tried | Result |
|---|---|---|---|
| Printable ASCII strings 1–80 chars, CODE section | 52,217 | SHA1+cycle, SHA1+zeropad, MD5×2, raw | No match |
| Printable ASCII strings 1–80 chars, DATA section | 453 | All of above | No match |
| Aligned 24-byte raw windows, loader function area | 1,104 | Direct as 3DES key, CBC+ECB+CFB | No match |
| Non-ASCII 24-byte windows, DATA section (raw 0x768200–0x78B000) | 31,493 | Direct as 3DES key | No match |
| Simple XOR (key=bytes0-7, key=bytes8-15, key=reversed) | 3 | — | No match |

**Conclusion:** The key is NOT an ASCII string anywhere in tp7runtime.exe. It is either:
- A binary (non-printable) blob somewhere in the binary (CODE or DATA)
- The key pointer at context+0x488 is populated at runtime from a source not in the binary
  (e.g., read from a registry entry, a file, or computed from machine/install data)
- The "passphrase" is not passed to InitStr at all, and Init is called directly with raw bytes
  from a region not yet searched (e.g., a global constant array, a resource section)

**⚠️ Remaining avenues — STATUS REVISED (2026-06-12):**
Avenues 1 and 2 below are now superseded by the Twofish discovery. The cipher is Twofish,
not 3DES, so 3DES-targeted brute-force is irrelevant. Avenues 3 and 4 remain valid:

1. ~~Raw 16-byte windows as 3DES key~~ — **OBSOLETE** (cipher is Twofish, not 3DES)
2. ~~CODE section raw bytes as 24-byte 3DES keys~~ — **OBSOLETE** (same reason)
3. **Ghidra decompiler** — confirm passphrase argument to InitStr; disassemble 0x74eb50 (mode=2)
4. **Runtime memory dump via x64dbg** — break inside 0x742654 after InitStr returns; read key
   bytes from TDCP_twofish cipher object at [EBX + key_offset]; 16–32 bytes → test immediately

**DCPcrypt key derivation detail (confirmed from TDCP_3des.Init disassembly at raw 0x724504):**
DCPcrypt's `InitStr(keystr)` calls SHA1(keystr) → 20 bytes, then calls `cipher.Init(key, keybits, NULL)`.
Key setup inside `Init`:
  1. `FillChar(key_buf, key_buf_size, 0)` — zero-fill the full key buffer first
  2. `Move(sha1_output, key_buf, keybytes)` — copy SHA1 result (keybytes = 20)
  3. Result: SHA1[0:20] + zero bytes for the remainder
**Padding is ZEROS, not cycling** — prior doc was wrong. SHA1[0:4] is NOT repeated.
For Twofish (max 256 bits / 32 bytes): keybits = min(160, 256) = 160 → sha1 20 bytes + 12 zero bytes.
For TDCP_3des (max 192 bits / 24 bytes): keybits = min(160, 192) = 160 → sha1 20 bytes + 4 zero bytes.
Then 3DES splits the 24-byte buffer: k1=buf[0:8], k2=buf[8:16], k3=buf[16:24].
Since keybits(160) > 0x80(128): k3 is distinct (buf[16:24] = SHA1[16:20] + 0x00000000).

**Python validation function (ready for Twofish — pycryptodome lacks Twofish; workaround below):**
```python
# scripts/rwn_validate.py  — paste a candidate passphrase and test it
# NOTE: As of 2026-06-12, pycryptodome does NOT include Twofish.
# Workaround options:
#   A) pip install twofish     (pure Python; may need MSVC build tools)
#   B) pip install pyaes       (AES only; no help)
#   C) ctypes call into a Twofish DLL (e.g., libtomcrypt.dll or custom build)
#   D) Use x64dbg memory dump (Method B) to get decrypted bytes directly
import hashlib

PASSPHRASE = b"An error has occurred during conversion of this field from alpha to the appropriate binary form."

with open("samples/rosetta/T7INA.RWN", "rb") as f:
    rwn = f.read()

IV8  = rwn[0:8]                    # F8 13 B6 7B 3D 24 BC 45 (8-byte header)
CT   = rwn[0x10:0x10 + 0x100]     # ciphertext from byte 16; covers target at 0xC5

sha1 = hashlib.sha1(PASSPHRASE).digest()   # 20 bytes
# DCPcrypt key buffer variants (all zero-padded, not cycling):
key16 = sha1[:16]                  # 128-bit Twofish
key20 = sha1                       # 160-bit (non-standard; DCPcrypt may use as-is)
key24 = sha1 + b'\x00' * 4        # 192-bit Twofish
key32 = sha1 + b'\x00' * 12       # 256-bit Twofish (max)

def try_twofish(key, iv, ct):
    """Placeholder — replace with actual Twofish call once library available."""
    try:
        from twofish import Twofish         # pip install twofish
        bs = 16                             # Twofish block size = 16 bytes
        T = Twofish(key)
        # CBC mode: XOR each block with previous ciphertext block (IV for first)
        pt = bytearray()
        prev = iv[:bs] if len(iv) >= bs else (iv + b'\x00' * bs)[:bs]
        for i in range(0, len(ct) - len(ct) % bs, bs):
            block = ct[i:i+bs]
            dec = T.decrypt(bytes(block))
            pt += bytes(x ^ p for x, p in zip(dec, prev))
            prev = block
        return bytes(pt[0xC5:0xCA]) == b'TAS32'
    except ImportError:
        print("Twofish not installed; cannot test")
        return None

# Test all key variants
for label, k in [("128-bit", key16), ("160-bit", key20), ("192-bit", key24), ("256-bit", key32)]:
    result = try_twofish(k, IV8, CT)
    print(f"Twofish {label}: TAS32={result}")
```

---

## Part 3: After decryption — disassembling `.RWN` bytecode

Once decrypted, a `.RWN` file likely has a similar structure to `.RUN` but with TAS Pro 7
extensions. The disassembly process:

1. **Verify the decrypted header** matches a known format (magic bytes, "TAS32" or similar).
2. **Locate the file reference table** (should still start near offset 0x80 or at a documented
   offset in the header).
3. **Locate the bytecode section** using the header offsets.
4. **Extend the opcode table** from Part 1 to cover TAS Pro 7 additions (new keywords,
   new screen/print/database operations added in the T7 generation).
5. **Run the disassembler** and compare output against known `.SRC` files to validate.

---

## Part 4: Bulk decompilation pipeline

Once the decryptor and disassembler both work:

```
scripts/
  rwn_decrypt.py      — decrypt a .RWN → .RUN-like binary
  run_disasm.py       — disassemble a .RUN/.decrypted file → .SRC-like text
  batch_decompile.ps1 — run both over all 1,149 files, write to decompiled/
```

Target output directory: `decompiled/` (in this workspace).
Each file gets a `.tas` extension (to distinguish from original `.SRC` files).
Preserve the original directory structure under `decompiled/DBAMFG$/`.

---

## Current research status

| Task | Status | Notes |
|------|--------|-------|
| .RUN header mapped | Partial | Magic, file table confirmed. Bytecode start not yet pinpointed. |
| .RUN opcode table | Not started | Needs Rosetta Stone analysis against 7 pairs |
| .RWN header mapped | Partial | First 16 bytes understood; encrypted content starts byte 16 |
| .RWN encryption algorithm | **CONFIRMED (CORRECTED)** | **Twofish (TDCP_twofish) — NOT 3DES** |
| TDCP_twofish VMT + class name | **CONFIRMED** | VA 0x74F2A8, raw 0x34E6A8; class name verified from VMT[-0x2C] |
| TDCP_3des present but not used for RWN | **CONFIRMED** | VMT raw 0x00723694; used at 0x124B70 and 0x31DAC0 only |
| AES ruled out | **CONFIRMED** | AES S-box absent from tp7runtime.exe |
| XOR ruled out | **CONFIRMED** | Tested 3 XOR key schemes; none match TAS32 at offset 0xC5 |
| TAS32 at decrypted offset 0xC5 | **CONFIRMED** | VA 0xB5C8B9: ADD EAX,0xC5; MOV ECX,5; CALL 0x45a4c4 (3 instances) |
| Decrypt function (header validate) | **CONFIRMED** | raw 0x742654 — creates Twofish, calls InitStr, does header check |
| Main decrypt loop | **CONFIRMED** | Function 0x74e374 — 0x2000-byte chunks via mode=2 Twofish |
| Mode dispatch | **CONFIRMED** | VMT[+0x50] mode=2 → 0x74eb50; mode=1 → 0x74e9ac (CFB-8) |
| Function 0x74eb50 (mode=2) | Not disassembled | Likely CBC block mode; needs Ghidra or disasm |
| Candidate passphrase identified | **CONFIRMED** | "An error has occurred..." from global chain [0xB8B0CC] |
| InitStr key derivation | **CONFIRMED** | SHA1(pass)[0:20] + zero pad; NOT cycling — confirmed from code |
| Passphrase tested with Twofish | **NOT YET DONE** | pycryptodome lacks Twofish; need library or x64dbg |
| Printable-string 3DES search (obsolete) | Superseded | All those tests used 3DES — irrelevant now that cipher is Twofish |
| Ghidra static analysis | **Next priority** | Confirm passphrase + disassemble 0x74eb50 (mode=2) |
| x64dbg runtime dump | Fallback | Break in 0x742654 after InitStr call; read key bytes from cipher object |
| .RWN master key / passphrase | **Candidate found** | "An error has..." — untested; validation blocked on Twofish library |
| Decryptor script | Not written | Template written; blocked on Twofish Python library |
| Disassembler script | Not written | Blocked on opcode table |

---

## Files in samples/rosetta/

```
Rosetta Stone pairs (TAS Pro 6):
  BKAPH.SRC / BKAPH.RUN       — A/P batch (266 KB compiled)
  BKAPHA.SRC / BKAPHA.RUN     — A/P batch variant (270 KB compiled)
  BKAWLB.SRC / BKAWLB.RUN    — A/R labor backlog (139 KB compiled)
  BKDCA.SRC / BKDCA.RUN      — D/C analysis (230 KB compiled)
  BKLME.SRC / BKLME.RUN      — Labor/manufacturing (127 KB compiled)
  BKMRF.SRC / BKMRF.RUN      — MRF module (159 KB compiled)
  BKMRF.org2 / BKMRF.TEST    — Intermediate/test variants of BKMRF
  BKROA.SRC / BKROA.RUN      — R/O analysis (281 KB compiled)

Encrypted TAS Pro 7 samples:
  T7INA.RWN      — Inventory module A (790 KB)
  suwin6t.rwn    — TAS Pro 6 runtime shell (95 KB) — encrypted despite .rwn extension
  suwin7.rwn     — TAS Pro 7 runtime shell (8.6 KB) — encrypted
```

---

## tp7runtime.exe PE section table (confirmed)

`tp7runtime.exe` is a 32-bit PE, ImageBase=0x400000, 33,347,600 bytes.
Use these formulas to convert between file offsets (raw) and virtual addresses (VA):

| Section | RVA | VSize | Raw Start | Raw Size | VA→Raw formula |
|---------|-----|-------|-----------|----------|----------------|
| CODE | 0x1000 | 0x767C40 | 0x400 | 0x767E00 | raw = VA − 0x400C00 |
| DATA | 0x769000 | 0x22CD0 | 0x768200 | 0x22E00 | raw = VA − 0x400E00 |
| BSS | 0x78C000 | 0xBE3D | 0x78B000 | 0 (no file data) | — |
| .idata | 0x78D000 | — | — | — | — |
| .edata | — | — | — | — | — |
| .tls | — | — | — | — | — |
| .rdata | — | — | — | — | — |
| .reloc | — | — | — | — | — |
| .rsrc | — | — | — | — | — |
| .debug | — | ~22 MB | — | — | Borland TDS format (debug symbols) |

**Important:** DATA section starts at raw 0x768200. The BSS section has no file data
(raw size = 0) — globals in BSS range (VA 0x78C000+) have no file representation and
hold runtime values only.

Key globals confirmed in DATA section:
| VA | Raw | Content |
|----|-----|---------|
| 0x74F25C | 0x34E65C | TDCP_twofish VMT pointer (= 0x74F2A8) |
| 0x74C698 | 0x34BA98 | SHA1 hasher class pointer |
| 0x46FCC4 | 0x06F0C4 | TMemoryStream VMT pointer |
| 0xB8B0CC | 0x78A2CC | Passphrase global (pointer chain start) |
| 0xB6F454 | 0x76E654 | Passphrase pointer level 2 |
| 0x563D84 | 0x163184 (CODE) | Delphi AnsiString: "An error has occurred..." |

---

## Confidence ratings

- .RUN file table structure: **92/100** — directly verified from hex + source comparison
- .RUN magic "TAS32q" location: **100/100** — confirmed at offset 0x39
- .RUN bytecode section location: **30/100** — known to follow file table; exact offset unmapped
- .RWN bytes 0–7 = per-file nonce/IV: **65/100** — varies per file (good); but Twofish block = 16 bytes so 8-byte IV is half-block; purpose TBD
- .RWN byte[11]=0x89, byte[15]=0x01 as format marker: **95/100** — confirmed across 8 files
- .RWN encryption algorithm = Twofish (DCPcrypt): **92/100** — VMT class name confirmed; minor uncertainty on mode=2 behavior
- .RWN cipher is NOT 3DES for RWN path: **95/100** — TDCP_3des VMT distinct from TDCP_twofish VMT; code path unambiguous
- AES ruled out: **100/100** — S-box absent from entire binary
- XOR ruled out: **100/100** — three XOR schemes tested, none produce TAS32 at offset 0xC5
- TAS32 at decrypted offset 0xC5: **96/100** — confirmed (ADD EAX, 0xC5 + MOV ECX, 5 + CALL compare), three instances; VA 0xB5C8B9
- Decrypt function at VA 0x742654: **90/100** — Twofish creation, InitStr call, and header validate all observed
- Main decrypt loop at 0x74e374: **90/100** — 0x2000-byte chunked VMT[+0x50] mode=2 calls confirmed
- Mode=2 → 0x74eb50 (cipher block mode): **88/100** — dispatch chain confirmed; internal behavior of 0x74eb50 not yet disassembled
- Candidate passphrase "An error has...": **55/100** — confirmed as the static value at global chain destination; uncertain whether it is runtime-modified before use
- InitStr key derivation = SHA1 + zero pad (not cycling): **88/100** — confirmed from TDCP_3des.Init disassembly; Twofish Init likely identical pattern
- Passphrase produces TAS32 at 0xC5: **0/100** — not yet tested (blocked on Twofish Python library)
- DCPcrypt SHA1 key derivation applies to Twofish too: **80/100** — InitStr is shared infrastructure; both TDCP_3des and TDCP_twofish call the same InitStr at 0x74e1f8
