# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-06-16 (session 5)

---

## 1. Project in one paragraph

We are reverse-engineering **EvoERP**, a manufacturing ERP built on TAS Professional 7
(`tp7runtime.exe`). The vendor has granted explicit permission to decompile. EvoERP has
two compiled-program formats: `.RUN` (TAS Pro 6, unencrypted) and `.RWN` (TAS Pro 7,
encrypted). The `.RWN` and `.DCY` cipher is **Twofish-CFB-128**.

**ALL CIPHER PARAMETERS CONFIRMED 2026-06-16 (live Frida capture + Python verification):**
- Algorithm: Twofish-192, CFB-128 mode
- Key size: SHA1(passphrase)[0:20] + 4 zero bytes = 24-byte (192-bit) key
- IV param: always 0 → P_initial = Encrypt_K(all-zeros block)
- Body P_start: K0 = Encrypt_K(P_initial) — NOT P_initial itself
- DCY key (K_D): `691e8041ab265b4e6ee052ccc946dba4caac60da` + `00000000`
- RWN key (K_B): `a898d21e2fd6ca294026e5d633d9047f91f7ed35` + `00000000`
- The passphrase "mabufoju" was WRONG — actual passphrase unknown but not needed
- Decryption verified: MDUMMY.DCY → `object EditForm1: TEditForm1\r\n...` ✓

**There are only 7 `.SRC` files on the network share** (all TAS Pro 6 era, all already
analyzed). The entire TAS Pro 7 logic (1,124 `.RWN` files) is binary-only and now
fully decryptable. Next priority: build batch decryptors using the correct keys and
begin disassembling `.RWN` bytecode.

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
| Decrypt any `.RWN` or `.DCY` file | **DONE** — cipher fully solved 2026-06-16; `rwn_decrypt.py` + `dcy_decrypt.py` use correct K_B/K_D keys |
| Disassemble `.RWN` bytecode | Unblocked — TAS Pro 7 bytecode structure not yet mapped; uniform opaque bytes expected |
| Read module logic for any of the 1,124 `.RWN` programs | Unblocked — bytecode disassembly + DCY format parsing needed first |
| `.DCY` data dictionary binary structure | **Partially done** — decryption works; binary field layout not yet reverse-engineered |
| Identify K_A / K_C key purposes | Unknown — captured live but which file types use them is not yet known |

---

## 4. Current state — NO HARD BLOCKER

**As of 2026-06-16, all cipher work is complete.** No active decryption blocker exists.

What was the blocker (historical, for reference):
- Needed: `block_buf` heap value (IV) to decrypt .RWN and .DCY files
- Solution: live Frida capture via `scripts/frida_capture_key_and_iv.py`
- Discovery: IV param is always 0; keys are SHA1(runtime_passphrase) not "mabufoju";
  body P_start = K0 = Encrypt_K(P_initial), not P_initial itself
- See BROKEN.md B-007 for full history

Current decryption scripts:
- `scripts/rwn_decrypt.py` — uses K_B (`a898d21e...`), P_start=K0, no IV file needed
- `scripts/dcy_decrypt.py` — uses K_D (`691e8041...`), P_start=K0, no IV file needed
- Both verified 2026-06-16: `python scripts/dcy_decrypt.py --validate-only` → 41/48 OK ✓

**Highest-value next work: parse DCY binary format** (see §7 below).

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
| `.DCY` data dictionary | 🔄 Partial | 82/100 | IV confirmed; 41/48 files decrypt; binary format not yet parsed |
| `.DFM` forms | 🔄 Partial | 87/100 | 1,109 parsed; content coverage ongoing |
| `.RTM` report templates | 🔄 Partial | 78/100 | 899+ inventoried; content coverage ongoing |
| Database schema | ✅ Done | 92/100 | 659 tables, 24,113 fields extracted |
| Module documentation | 🔄 Partial | 72/100 | 50+ modules now documented from DFM+CHM; 16 still opaque (no DFMs, no CHM) |
| `PROJECT-STRUCTURE.md` | 🔄 In progress | 72/100 | Updated each session |
| `HELP-RESOURCES.md` | 🔄 In progress | 75/100 | Updated 2026-06-15 — 25+ module sections added |
| `EVO-DECOMPILE-TODO.md` | ✅ Current | — | Master checklist, updated 2026-06-15 |

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

1. **Parse DCY binary format** — decrypted DCY files are in `samples/dcy_decrypted/`.
   Reverse-engineer the binary structure to extract table names, field names, field types.
   Start with `DBAMENU_LOGIN.DCY.dec` (2,234 bytes, smallest) then `DUMMY.DCY.dec`.
   Unlocks: field name resolution for all 659 tables → meaningful RWN bytecode analysis.

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
