# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-06-12

---

## 1. Project in one paragraph

We are reverse-engineering **EvoERP**, a manufacturing ERP built on TAS Professional 7
(`tp7runtime.exe`). The vendor has granted explicit permission to decompile. EvoERP has
two compiled-program formats: `.RUN` (TAS Pro 6, unencrypted) and `.RWN` (TAS Pro 7,
encrypted). The `.RWN` cipher is **Twofish-CFB** (DCPcrypt `TDCP_twofish`), the passphrase
is confirmed as **`mabufoju`**, the 192-bit key derivation is confirmed (SHA1 digest + 4
zero bytes), and a working pure-Python Twofish implementation passes NIST test vectors.
The one remaining blocker is the **initial IV** (the `block_buf` value at cipher+0x3C when
`tp7runtime.exe` first calls `EncryptBlock`) — it is uninitialized heap memory and cannot
be determined without a debugger session. **There are only 7 `.SRC` files on the network
share** (all TAS Pro 6 era, all already analyzed). The entire TAS Pro 7 logic (1,124 `.RWN`
files) is binary-only.

---

## 2. What we CAN do right now (fully unblocked)

| Task | Where to start |
|------|---------------|
| Analyze `.RUN` files (TAS Pro 6 compiled — unencrypted) | `samples/rosetta/*.RUN` |
| **Rosetta Stone opcode mapping** — correlate `.SRC` constructs with `.RUN` binary patterns | `samples/rosetta/` — 7 complete SRC+RUN pairs |
| Read and document `.DFM` form files (UI layout) | `\\i2s109-solidcrm\DBAMFG$\DFM\` (read-only) |
| Read and document `.RTM` ReportBuilder report templates | Network share, read-only |
| Study `.B` Btrieve data files via `.DDF` schema files | Network share, read-only |
| Study `tp7runtime.exe` in read-only mode (string search, Capstone disassembly) | `C:\ISTS\tp7runtime.exe` (read-only) |
| Update `docs/`, `PROJECT-STRUCTURE.md`, `HELP-RESOURCES.md`, `EVO-DECOMPILE-TODO.md` | This workspace (read-write) |
| Module documentation from `.DFM` forms, `.RTM` reports, and database schema | Docs in `docs/03-modules/` |
| Per-table field meaning documentation (659 tables) | `docs/04-data-dictionary/` |

---

## 3. What we CANNOT do yet (blocked)

| Blocked task | Blocker |
|-------------|---------|
| Decrypt any `.RWN` or `.DCY` file | Initial IV (block_buf) unknown — requires debugger |
| Disassemble `.RWN` bytecode | Blocked on decryption |
| Write `rwn_decrypt.py` or batch decryptor | Blocked on IV |
| Read module logic for any of the 1,124 `.RWN` programs | Blocked on decryption |
| Write stub or placeholder code for the `.RWN` path | Forbidden — creates false progress |

---

## 4. The current blocker — and how to resolve it

**Blocker:** The initial value of `block_buf` (cipher+0x3C, 16 bytes) is unknown.
`tp7runtime.exe`'s TDCP_blockcipher constructor allocates this buffer via `GetMem` but
never zeroes it. The `Init` call chain (TDCP_cipher.Init → Twofish.Init) also never
touches it. The value when `EncryptBlock` is first called depends on prior heap state
and can only be observed at runtime.

**What we know (all confirmed by disassembly):**
- Cipher: Twofish (TDCP_twofish from DCPcrypt) — VMT confirmed, q-box tables verified ✓
- Passphrase: **`mabufoju`** — hardcoded at tp7runtime.exe file offset `0x75D154` ✓
- Key: SHA1('mabufoju')[0:20] + `\x00\x00\x00\x00` = 24-byte (192-bit) key ✓
- Mode: CFB (mode=2 written to cipher+0x34 in validate_func) ✓
- Validation: first 8 bytes of every `.RWN`; pass when decrypted pt[0:4] == pt[4:8] ✓
- All 20+ scanned `.RWN` files have constant ct[0:4]^ct[4:8] = 0x3E0A37C5 ✓
- Python twofish_pure.py passes NIST 192-bit test vector ✓
- IV=zeros tested → keystream XOR = 0xCE14BE8C ≠ 0x3E0A37C5 → **IV is not zeros**

**How to resolve — one debugger session:**
1. Install x64dbg (free): https://x64dbg.com/
2. Launch `tp7runtime.exe` with a small `.RWN` (e.g. `suwin7.rwn`, 8.6 KB from `C:\ISTS\`)
3. Set breakpoint at **file offset `0x34DF50`** (= VA `0x74EB50`): this is `mode2_handler`,
   called when the cipher first processes data in CFB mode
4. When breakpoint hits, EAX = cipher object pointer
5. Read 16 bytes at `[EAX + 0x3C]` — that is `block_buf`, the actual IV
6. Share those 16 bytes; `rwn_decrypt.py` can be written and tested immediately

See `BROKEN.md` entry B-004 for full context and prior attempts.

---

## 5. Research state snapshot

| Area | Status | Confidence | Notes |
|------|--------|-----------|-------|
| `.RWN` cipher identified | ✅ Done | 95/100 | Twofish-CFB, VMT + q-boxes confirmed |
| Passphrase | ✅ Confirmed | 90/100 | 'mabufoju' at file offset 0x75D154 |
| Key derivation | ✅ Confirmed | 90/100 | SHA1 + 4 zeros = 192-bit |
| Validation structure | ✅ Confirmed | 88/100 | pt[0:4]==pt[4:8], XOR constant 0x3E0A37C5 |
| twofish_pure.py implementation | ✅ Done | 95/100 | Passes NIST 192-bit test vector |
| Initial IV (block_buf) | ❌ Blocked | 0/100 | Uninitialized heap; requires debugger |
| `.RWN` decryptor script | ❌ Blocked | — | Blocked on IV |
| `.SRC` source files | ✅ Done | 90/100 | Only 7 files exist; all analyzed |
| `.RUN` header structure | 🔄 Partial | 85/100 | Magic + string sections confirmed |
| `.RUN` opcode table | ❌ Not started | 0/100 | 7 Rosetta Stone pairs ready |
| `.DCY` data dictionary | ❌ Blocked | 60/100 | Same encryption as .RWN; blocked on IV |
| `.DFM` forms | 🔄 Partial | 87/100 | 1,109 parsed; content coverage ongoing |
| `.RTM` report templates | 🔄 Partial | 78/100 | 899+ inventoried; content coverage ongoing |
| Database schema | ✅ Done | 92/100 | 659 tables, 24,113 fields extracted |
| Module documentation | 🔄 Partial | 65/100 | Core modules documented; 35+ shallow |
| `PROJECT-STRUCTURE.md` | 🔄 In progress | 72/100 | Updated each session |
| `HELP-RESOURCES.md` | 🔄 In progress | 65/100 | Updated each session |
| `EVO-DECOMPILE-TODO.md` | ✅ Current | — | Master checklist, updated 2026-06-12 |

---

## 6. Key documents — read these before working

| Document | Purpose |
|----------|---------|
| `BROKEN.md` | **Read first every session.** All bugs found, all fixes tried, all blockers. |
| `EVO-DECOMPILE-TODO.md` | Master checklist with confidence ratings for every analysis area |
| `docs/README.md` | Index of all documentation completed so far |
| `PROJECT-STRUCTURE.md` | Catalog of every EvoERP file and its purpose |
| `HELP-RESOURCES.md` | User-facing knowledge base: tables, fields, how-to recipes |
| `research/OPEN_QUESTIONS.md` | Unresolved questions — pick from here for next work |
| `CLAUDE.md` | Scope rules, autonomy protocol, confidence ratings, all standing instructions |
| `docs/02-file-formats/decryption-findings.md` | Full `.RWN` cipher reverse-engineering findings |

---

## 7. Highest-value next tasks (in priority order)

1. **Debugger session for IV** — user runs x64dbg, reads [EAX+0x3C] at mode2_handler
   entry (file 0x34DF50). This is the single action that unblocks the most.
   *(Claude cannot do this — requires user interaction with a running process.)*

2. **`.RUN` opcode mapping** — 7 Rosetta Stone pairs in `samples/rosetta/`; start with
   `BKAWLB.SRC` + `BKAWLB.RUN` (smallest pair); map `proc`/`return` first, then
   `open`/`close`, then `if`/`endif`. Unblocked; high value even before RWN decryption.

3. **Per-table field meaning documentation** — 659 tables, most without narrative docs.
   Start with Tier 1 tables in `EVO-DECOMPILE-TODO.md §16`. Fully unblocked.

4. **Module documentation** — Read `.DFM` forms and `.RTM` reports for undocumented
   modules (DE, FA, JC, SC, SH, LC, SR, QC, etc.). Fully unblocked.

5. **Business workflow recipes** — Document end-to-end processes (SO→ship→invoice,
   WO lifecycle, AP check run, etc.) in `docs/` and `HELP-RESOURCES.md`. Unblocked.
