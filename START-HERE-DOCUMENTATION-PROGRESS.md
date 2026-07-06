# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-07-06 (Rule overhaul — new operating rules added to CLAUDE.md §13: Issues/ folder splits BROKEN.md; section indexes on TODO docs; Explore agents for large docs; BUGS.md merged into KNOWN-ISSUES.md; FULL TASK COMPLETE signal; never read PROJECT-STRUCTURE/HELP-RESOURCES directly. Pass 570 — PO-A bullet-point field descriptions converted to structured field table in po-purchase-orders/help-content.md (21-field header table + 19-field line-item table + totals + program operations); per-form narrative C:89→C:90. Pass 569 — CHM field-level semantics mined for IN/SO/WO forms: IN item type table corrected 6→10 codes (N/R/M/F/A/B/L/T/K/O) + 8 Active Status codes (Y/N/O/D/E/P/S/Q) added; SO-A 28-field header screen table added; WO-A status codes corrected to actual MTWO_WIP_STATUS values S/F/R/C/X/I with transition rules; L1152 per-form narrative C:86→C:89. Pass 568: all 5 C:\ISTS\ DLLs identified (c4dll.dll=CodeBase v6.5, quricol32.dll=Quricol QR Barcode); PV.EXE corrected to Process Viewer; System Architecture C:93→94. Pass 567: UPDTP7.EXE dual-mechanism (batch-script generator vs Robocopy — two separate update paths). Pass 566: Terminal Server/Citrix deployment documented (C:42); Pervasive License Admin documented (C:62). Pass 565: workstation setup procedure created; form-to-table mapping (C:65, 726/870 forms mapped). Pass 564: form-to-menu-code mapping C:87→C:90; DE module CSV pipeline documented. Pass 563: TPF0 binary property table documented. Pass 562-559: RTM sub-report cross-ref complete (2,578 cross-refs); BKISWCE1 #1 caller (244); all RTM sub-items C:90+. Pass 551: DDF-confirmed ISEXUSER/ISACCESS/BKLOGON; 7-layer auth model. Pass 431: Excel DDB import: 579 tables / 21,299 fields.)

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
| Identify K_A key purpose | K_C confirmed = suwin6.dcy (ISTech License dialog); K_A still unknown — captured live but which file type uses it is not yet known |

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
| `.RUN` opcode table | 🔄 Started | 87/100 | string records `41 00 LL_lo LL_hi` confirmed; BKAWLB fully cataloged (786 records/432 readable); OP_5D=inv_menu descriptor confirmed Pass 565b; method in run-string-extraction.md |
| TAS Pro 7 `.RWN` bytecode | 🔄 Started | 82/100 | 60+ opcodes; 15 sub-code families; branch target = computed/runtime pool; static CFG architecturally impossible; T7YSYN: 1243 vars, 15-byte name field, 52 procs |
| `.DCY` binary format | ✅ DONE | 95/100 | 8-byte ID header + DFM content; all 41 forms = Delphi TEditForm; EVOUSERS/WBKLUGRID documented |
| `suwin*.DCY` format | 🔄 Partial | 50/100 | suwin6.dcy ✅ SOLVED (Pass 387): K_C=ISTech License dialog; suwin7.dcy fails all 5 keys |
| K_A / K_C key purposes | 🔄 Partial | 65/100 | K_C = suwin6.dcy (ISTech License); K_A still unknown |
| `.DFM` forms | 🔄 Partial | 90/100 | 1,109 parsed; form-to-menu-code 90/100 (Pass 563); form-to-table 65/100 (Pass 564, 726/870 mapped); per-form narrative 90/100 (Pass 570, PO-A full field table; Pass 569, CHM semantics for IN/SO/WO) |
| `.RTM` report templates | ✅ Good | 92/100 | 1,305 inventoried; sub-report cross-ref complete (2,578 links in rtm_crossrefs.csv); BKISWCE1 #1 caller (244); ISRTMS 29-field schema confirmed (Pass 559-560) |
| Database schema | ✅ Done | 95/100 | 659 tables (DDF); 579 tables / 21,299 fields from Excel export (Pass 431); 33 per-module field files in docs/04-data-dictionary/ |
| YN slot mapping (BKYSMSTR) | 🔄 Partial | 82/100 | 250-slot live snapshot complete; 88 DFM+SRC confirmed; YN[102-143]=42 module-enable slots (BKMENUSU GROUPS order); YN[150-198]=all empty; 162 slots still unknown |
| ISTS.CFG key directory | ✅ Done | 88/100 | 495 confirmed keys from T7YSYN; full docs/05-configuration/ists-cfg-keys.md |
| Module documentation | ✅ All 90+ | 92/100 | All scorecard modules at C:90+; 50+ modules documented in modules.py narratives; full DFM, RTM, RWN symbol coverage |
| `PROJECT-STRUCTURE.md` | ✅ Current | 92/100 | Updated Pass 544/551; 659 tables cataloged from DDF; all major RWN programs mapped |
| `HELP-RESOURCES.md` | ✅ Current | 92/100 | Updated Pass 431+ — all 579 DBA tables + 21,299 fields; 44 recipe pages; full keyword index |
| `EVO-DECOMPILE-TODO.md` | ✅ Current | — | Master checklist, updated Pass 551 (2026-07-02) |

---

## 6. Key documents — read these before working

| Document | Purpose |
|----------|---------|
| `BROKEN.md` | **Read first every session.** Short index only — summaries + links to `Issues/` detail files. Full content is in `Issues/<id>-<slug>.md`. |
| `EVO-DECOMPILE-TODO.md` | Master checklist — **read the SECTION INDEX at the top only** (first ~35 lines); Grep for a section anchor to jump to it. |
| `docs/README.md` | Index of all documentation completed so far |
| `PROJECT-STRUCTURE.md` | **Never read directly.** Use an Explore agent with a specific question. |
| `HELP-RESOURCES.md` | **Never read directly.** Use an Explore agent with a specific question. |
| `research/OPEN_QUESTIONS.md` | Unresolved questions — pick from here for next work |
| `CLAUDE.md` | Scope rules, autonomy protocol, confidence ratings, all standing instructions (system-injected — already active) |
| `docs/02-file-formats/decryption-findings.md` | Full `.RWN` cipher reverse-engineering findings |

---

## 7. Highest-value next tasks (in priority order)

1. **YN[N] ↔ ISTS.CFG.* mapping — push from C:82 toward C:90** — 162 of 250 slots unknown.
   Options: (a) T7YSYN pool expression tree parser (complex, multi-token compound format);
   (b) additional DFM control binding analysis; (c) live query more companies' BKYSMSTR.
   Blocked slots YN[102-143]: module-enable order confirmed (BKMENUSU GROUPS order), but
   value semantics (Y/Z/A/Q/1/space flags) blocked by RWN encryption.
   `docs/05-configuration/ists-cfg-keys.md` is the working document.

2. **Identify K_A purpose** — K_C confirmed (Pass 387) = suwin6.dcy ISTech License dialog.
   K_A still unknown — fired at boot; Frida file-open hook needed to identify which file uses K_A.

3. **`.RWN` bytecode deeper analysis** (C:82 natural ceiling) — 60+ opcodes confirmed;
   static CFG impossible (branch targets = computed runtime pool). Only angle that could move
   this is T7YSYN pool tree parser to map YN slot indices, or a live debugger session.

4. **✅ Per-form narrative: C:90 reached (Pass 570)** — PO-A full field table added; AR-A/AP-A
   already had tables; SO-A/WO-A have comprehensive paragraph coverage. Remaining 1,106 non-CHM
   forms require RWN decryption for table bindings — natural ceiling without decryption.

5. **✅ DONE (Pass 550+) Module documentation** — All scorecard modules at C:90+;
   50+ modules documented in `learnevo-help/content/modules.py` narratives. DFM, RTM, RWN
   symbol coverage complete for all accessible programs.

6. **✅ DONE (Pass 307-497) Business workflow recipes** — 44 recipe pages in learnevo-help;
   full SO/WO/AP/GL/period-end/year-end workflows documented; Acctug.pdf (Pass 497) confirms.

7. **✅ DONE (Pass 431) Per-table field meaning documentation** — 579 tables / 21,299 fields
   from `Evo-DBA_File_Fields 052421.xlsx`; 33 per-module field files in `docs/04-data-dictionary/`;
   master table index in `docs/04-data-dictionary/table-index.md`. ~65% field descriptions present.

8. **suwin7.dcy decryption** — fails all 5 known keys (K_A/K_B/K_C/K_D/K_E). May use
   a 6th key from a different ISTech subsystem. Requires Frida session to capture.

9. **learnevo-help content completeness** — A few sub-90 module stubs may remain; run the
   help server and check for any missing narratives via the browser UI.
