# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-06-15

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

| Blocked task | Status |
|-------------|---------|
| Decrypt any `.RWN` or `.DCY` file | **DONE** — 1,144/1,145 files OK; CSV summary in `samples/rwn_decrypted/` |
| Disassemble `.RWN` bytecode | Unblocked but no clear structure yet — TAS Pro 7 bytecode is uniform (expected) |
| Write `rwn_decrypt.py` or batch decryptor | **DONE** — `scripts/rwn_decrypt.py` |
| Read module logic for any of the 1,124 `.RWN` programs | Unblocked — requires DCY IV for field names; bytecode dense |
| `.DCY` data dictionary decryption | Still blocked — IV_dcy not yet captured (same Frida method, different XOR filter) |

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

**How to resolve — Frida (preferred, no install needed):**

`scripts/get_iv_frida.py` (v5) implements a self-filtering approach:
1. Run EVO (main menu visible)
2. Run: `python scripts/get_iv_frida.py` — wait for ARMED banner
3. Open any MODULE from the EVO main menu (Work Orders, Inventory, etc.)
   — NOT a sub-menu within an already-open module (those load .DCY, not .RWN)
4. IV is extracted and saved to `scripts/iv_bytes.bin` automatically
5. Run: `python scripts/verify_iv.py`

**Key detail:** v5 hooks `EncryptBlock` (RVA 0x350248), not `mode2_handler`. After
EncryptBlock executes in-place on block_buf, K = Encrypt(block_buf) is in memory.
Only .RWN validation decrypts produce K[0:4]^K[4:8] = 0x3E0A37C5. .DCY loads (wrong
XOR) are automatically ignored. IV = Decrypt(K) computed in Python. Self-verifying.

**Fallback — x64dbg:**
1. Install x64dbg (free): https://x64dbg.com/
2. Attach to running evoerp.exe
3. Set breakpoint at VA `0xFAEB50` (mode2_handler, loaded evoerp.exe base 0xC60000)
   — or compute: module_base + 0x34EB50
4. Open a module window from EVO main menu
5. When breakpoint hits: EBX = cipher obj; read [EBX+0x3C] (4 bytes) = heap ptr P;
   read *P for 16 bytes = actual block_buf IV
6. Share those 16 bytes hex; `scripts/verify_iv.py --hex "xx xx..."` checks them

See BROKEN.md B-004, B-005, B-006 for all prior attempts and dead ends.

---

## 5. Research state snapshot

| Area | Status | Confidence | Notes |
|------|--------|-----------|-------|
| `.RWN` cipher identified | ✅ Done | 95/100 | Twofish-CFB, VMT + q-boxes confirmed |
| Passphrase | ✅ Confirmed | 90/100 | 'mabufoju' at file offset 0x75D154 |
| Key derivation | ✅ Confirmed | 90/100 | SHA1 + 4 zeros = 192-bit |
| Validation structure | ✅ Confirmed | 88/100 | pt[0:4]==pt[4:8], XOR constant 0x3E0A37C5 |
| twofish_pure.py implementation | ✅ Done | 95/100 | Passes NIST 192-bit test vector |
| Initial IV (block_buf) | ✅ Confirmed | 100/100 | IV = `9c da c3 45 a5 f0 1c 2c 96 57 92 d9 0b 1a bc 1e` |
| `.RWN` decryptor script | ✅ Done | — | 1,144/1,145 OK; `samples/rwn_decrypted/decrypt_summary.csv` |
| `.SRC` source files | ✅ Done | 90/100 | Only 7 files exist; all analyzed |
| `.RUN` file structure | ✅ Confirmed | 72/100 | Header / table slots / var storage / code+pool; see run-tas6-bytecode.md |
| `.RUN` opcode table | 🔄 Started | 22/100 | 0x41 PUSH_VALUE, 0x46 LOAD_VAR, 0x4E ARRAY_IDX identified |
| TAS Pro 7 `.RWN` bytecode | 🔄 Started | 8/100 | Confirmed correct decryption; uniform bytes = externalized strings; opcodes unknown |
| `.DCY` data dictionary | 🔄 Partial | 65/100 | RWN IV confirmed; DCY uses different IV (not yet captured) |
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

1. **Capture DCY IV** — run `scripts/get_iv_frida.py` while opening a DCY-loading event
   in EVO (e.g., navigate within a module). Use `--xor 0x09553584` filter for DCY.
   Unlocks: `.DCY` data dictionary → field names → meaningful RWN analysis.

2. **BKMRF 3-way compile diff** — diff `BKMRF.org2` vs `BKMRF.TEST` vs `BKMRF.RUN` to
   isolate stable bytes (opcodes) from variable bytes (addresses). High confidence gain.

3. **`.RUN` opcode mapping (continued)** — continue from BKAWLB analysis; map
   `if`/`goto`/`proc`/`return` constructs. Use `scripts/tas6_analyze.py`.

4. **Per-table field meaning documentation** — 659 tables, most without narrative docs.
   Start with Tier 1 tables in `EVO-DECOMPILE-TODO.md §16`. Fully unblocked.

5. **Module documentation** — Read `.DFM` forms and `.RTM` reports for undocumented
   modules (DE, FA, JC, SC, SH, LC, SR, QC, etc.). Fully unblocked.

6. **Business workflow recipes** — Document end-to-end processes (SO→ship→invoice,
   WO lifecycle, AP check run, etc.) in `docs/` and `HELP-RESOURCES.md`. Unblocked.
