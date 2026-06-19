# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-06-19 (Pass 110 — RWN bytecode pool type system decoded from suwin7.rwn; F-type=var_ref (val/77=var_index) and C-type=pool_ptr confirmed; compound blob structure mapped; Header[0x18]=60×77=first non-TEMP var offset; RWN bytecode confidence C:15→35/100)

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
| `.RWN` / `.DCY` cipher | ✅ SOLVED | 100/100 | Twofish-192-CFB; assembly-proven 2026-06-16 |
| RWN key K_B | ✅ Confirmed | 100/100 | `a898d21e2fd6ca294026e5d633d9047f91f7ed35` (live Frida) |
| DCY key K_D | ✅ Confirmed | 100/100 | `691e8041ab265b4e6ee052ccc946dba4caac60da` (live Frida) |
| Passphrase "mabufoju" | ❌ WRONG | — | Never the runtime passphrase; actual passphrase unknown but keys are captured |
| Key derivation | ✅ Confirmed | 100/100 | SHA1(passphrase)[0:20] + 4 zeros = 192-bit; IV param always 0 |
| Body P_start = K0 | ✅ Confirmed | 100/100 | Assembly-proven: DCPcrypt partial-block = no feedback update → block_buf stays K0 |
| Validation structure | ✅ Confirmed | 100/100 | pt[0:4]==pt[4:8]; K0 XOR filter: RWN=0x3E0A37C5, DCY=0x0955DC84 |
| `twofish_pure.py` | ✅ Done | 95/100 | Passes NIST 192-bit test vector |
| `.RWN` decryptor | ✅ Done | 99/100 | `scripts/rwn_decrypt.py` — K_B key, no IV file; 5/5 samples verified |
| `.DCY` decryptor | ✅ Done | 99/100 | `scripts/dcy_decrypt.py` — K_D key, no IV file; 41/48 OK (7 suwin* different format) |
| `.SRC` source files | ✅ Done | 90/100 | Only 7 files exist; all analyzed |
| `.RUN` file structure | ✅ Confirmed | 72/100 | Header / table slots / var storage / code+pool |
| `.RUN` opcode table | 🔄 Started | 22/100 | 0x41 PUSH_VALUE, 0x46 LOAD_VAR, 0x4E ARRAY_IDX identified |
| TAS Pro 7 `.RWN` bytecode | 🔄 Started | 35/100 | Pool type system decoded (F=var_ref, C=pool_ptr, compound blobs); 6 opcode roles inferred; opcode semantics need multi-program comparison |
| `.DCY` binary format | ✅ DONE | 95/100 | **Pass 109**: 8-byte ID header + DFM content (text "object..." 37/41; binary ff0a00+classname+TPF0 4/41); all 41 forms = Delphi TEditForm definitions for launcher/utility programs; EVOUSERS/WBKLUGRID documented |
| `suwin*.DCY` format | ⬜ Unknown | 0/100 | 7 files; K_D fails; possibly use K_A or K_C |
| K_A / K_C key purposes | ⬜ Unknown | 0/100 | Captured live; which file types they encrypt is unknown |
| `.DFM` forms | 🔄 Partial | 87/100 | 1,109 parsed; content coverage ongoing |
| `.RTM` report templates | 🔄 Partial | 78/100 | 899+ inventoried; content coverage ongoing |
| Database schema | ✅ Done | 92/100 | 659 tables, 24,113 fields extracted |
| Module documentation | 🔄 Partial | 72/100 | 50+ modules documented from DFM+CHM; 16 still opaque |
| `PROJECT-STRUCTURE.md` | 🔄 In progress | 72/100 | Updated each session |
| `HELP-RESOURCES.md` | 🔄 In progress | 75/100 | Updated 2026-06-15 — 25+ module sections |
| `EVO-DECOMPILE-TODO.md` | ✅ Current | — | Master checklist, updated 2026-06-16 |

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

1. **✅ DONE (Pass 109) Parse DCY binary format** — all 41 DCY files decoded: 8-byte ID header + DFM content.
   37/41 text DFM ("object EditForm..."), 4/41 binary DFM (ff0a00+classname+TPF0). All are Delphi
   UI form definitions for launcher/utility programs. See `docs/02-file-formats/decryption-findings.md`.

2. **Identify K_A / K_C purposes** — try K_A and K_C against `suwin*.DCY` (7 files).
   Also watch what files EVO opens at startup (Frida file-open hook) — K_A fired at boot.

3. **`.RWN` bytecode disassembly** (C:35/100, Pass 110) — pool type system decoded; compound blob
   structure confirmed; F-type=var_ref, C-type=pool_ptr proven from suwin7.rwn.
   **Next:** run `rwn_dispatch_compare.py` across ≥5 programs to find common opcodes (control-flow
   invariants). Cross-reference BKMRF 3-way compile diff (BKMRF.org2 vs BKMRF.TEST vs BKMRF.RUN)
   to isolate stable opcode bytes from variable address bytes. Target: C:50/100.

4. **`.RUN` opcode mapping (continued)** — continue from BKAWLB analysis; map
   `if`/`goto`/`proc`/`return` constructs. Use `scripts/tas6_analyze.py`.

5. **Per-table field meaning documentation** — 659 tables, most without narrative docs.
   Start with Tier 1 tables in `EVO-DECOMPILE-TODO.md §16`. Fully unblocked.

6. **Module documentation** — Read `.DFM` forms and `.RTM` reports for undocumented
   modules (DE, FA, JC, SC, SH, LC, SR, QC, etc.). Fully unblocked.

7. **Business workflow recipes** — Document end-to-end processes (SO→ship→invoice,
   WO lifecycle, AP check run, etc.) in `docs/` and `HELP-RESOURCES.md`. Unblocked.
