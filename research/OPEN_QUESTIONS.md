# Open Questions — Final Sweep

**Resolved** questions have their answer inline. **Still open** items
are the few remaining gaps after the bulk autonomous pass.

## RESOLVED during the autonomous pass

### Runtime, language, and tooling

- **What is `.DCY` / `.RWN` — encrypted or compressed?**
  Encrypted. The runtime's own string table says
  "You may only encrypt .DFM, .SRC & .LIB files." So the T7
  compiler *produces* encrypted forms. See
  [docs/02-file-formats/dcy-rwn-binaries.md](../docs/02-file-formats/dcy-rwn-binaries.md).

- **What TAS Pro 7 language looks like.**
  Fully documented from the runtime's embedded compiler. See
  [docs/02-file-formats/src-tas-pro-language.md](../docs/02-file-formats/src-tas-pro-language.md).

- **Are the `.RUN` (Pro 6) files also encrypted?**
  **No** — plaintext strings are readable. This was the key that
  unlocked the 554-code menu extraction.

- **Where is the source tree?**
  Not on this install. `taspro7.ini` history references
  `F:\Projects\TAS\istech\` on a developer machine. Only 7 leftover
  `.SRC` files are on the deployment share.

- **What's in `EvoPVT.jar`?**
  JavaFX SQL helper that writes to an `ISJAVA` task-queue table
  via the Pervasive JDBC driver. Full analysis at
  [docs/01-architecture/java-integration.md](../docs/01-architecture/java-integration.md).

### Data

- **How many tables / fields?**
  659 tables, 24,113 fields. Complete schema at
  `samples/ddf/schema.md`. Derived from standard Pervasive DDF set.

- **Multi-company layout?**
  Per-company directories on the share, each with its own copy of
  every `.B*` file. The file-extension code picks the company:
  `BKARCUST.B22` = AR customers for company `22`.

- **Where is the security model?**
  `AHSYLOG` table with 20 per-user access flags
  (`AHSY_USER_ACCES_1..20`), plus starting-menu code `AHSY_USER_MENU`
  (4 bytes) and role `AHSY_USER_LEVL` (2 bytes). See
  [docs/01-architecture/security-and-login.md](../docs/01-architecture/security-and-login.md).

### UI / forms

- **What's inside the DFMs?**
  Plaintext Delphi VCL forms using custom `TTAS*` components.
  1,109 successfully parsed; 25 failures are all zero-byte
  placeholders.

- **Menu system shape?**
  `XX-Y[-Z]` codes, 554 distinct in `.RUN` strings + 636 in CHM
  help (759 unique across both). See
  [docs/06-menu-system/overview.md](../docs/06-menu-system/overview.md).

### Reports & exports

- **What's in a `.RTM`?**
  Nevrona ReportBuilder `TppReport` tree serialized as Delphi
  `TPF0` binary. See
  [docs/02-file-formats/rtm-reportbuilder.md](../docs/02-file-formats/rtm-reportbuilder.md).

- **What about `.IMP` / `.UPD` / `.XPT`?**
  IMP = plaintext import config. UPD = Btrieve schema-update snapshot.
  XPT = plaintext export layout. See
  [docs/02-file-formats/other-formats.md](../docs/02-file-formats/other-formats.md).

## STILL OPEN (post-autonomous)

These items **require a running system or access to encrypted files**
to resolve fully:

~~1. **Decrypt `.RWN` / `.DCY` — last blocker is the IV.**~~ **FULLY RESOLVED 2026-06-16.**

   Cipher: Twofish-192-CFB-128. No external IV file needed — P_initial = Encrypt_K(zeros)
   is computed deterministically from the key. Keys captured live via Frida (2026-06-16):
   - RWN: K_B = `a898d21e2fd6ca294026e5d633d9047f91f7ed35` + 4 zeros
   - DCY: K_D = `691e8041ab265b4e6ee052ccc946dba4caac60da` + 4 zeros
   Body P_start = K0 = Encrypt_K(P_initial) — assembly-proven via DCPcrypt partial-block behavior.
   Decryptors: `scripts/rwn_decrypt.py` (5/5 samples OK) and `scripts/dcy_decrypt.py` (41/48 OK).
   Note: "mabufoju" passphrase was WRONG; old IV `9cda...` was an artifact of the wrong key.
   See `docs/02-file-formats/decryption-findings.md` and BROKEN.md B-007 for full detail.

   **New open sub-question:** 7 `suwin*.DCY` files fail K_D decryption → see item #13 below.

2. ~~**Exact ACCES_1..20 → module mapping**~~ **PARTIALLY RESOLVED 2026-06-25 (Pass286).**
   T7-era security does NOT use `AHSYLOG` — zero T7 programs access it (confirmed Pass270).
   T7 security: `BKPSUSER.BKPS_USER_SEC` = security level code → `BKSLEVEL` (422-field
   permission matrix, 20 sections × 21 flags each). `BKPSUSER` managed by T7PSA.RWN.
   `ISEXUSER` stores extended flags: ISEX.USER.GROUP/DATE1/DATE2/PASSW/PEXPD/LPASS/FLAGS.
   `ISACCESS` = additional access control table (T7PSA also opens this, role TBD).
   **Remaining open:** exact BKSLEVEL index→module mapping (which BKSL_MENU code controls
   which EvoERP module) and exact ISACCESS role still requires decrypted T7PSA bytecode.

3. **Password hashing algorithm.**
   Almost certainly a call to the runtime's `ENCRYPTSTR` with a
   built-in key. Not decoded.

4. ~~**Menu tree storage format.**~~ **FULLY RESOLVED 2026-06-18 (Pass 105).**
   `EVOERPMENU.DCY` is the visual window shell (TEditForm1 with 8 empty TTASStrLists).
   **The actual menu items live in `BKMENUSU.DBF`** — an xBase/dBASE format file on the share,
   read by `c4dll.dll` (CodeBase 4 engine). `StartEvo.exe` accesses it via PSQL DSN=EVOADMIN
   as `tas_menus`. `BKMENUSU.TXT` is the plain-text CSV export: 870 lines with every menu
   code, its label, and its program file. Format: `"CODE","Label","program.rwn"`.
   **Full mapping in `samples/BKMENUSU.TXT`.**

5. ~~**`WHOAMI.DBA` format**~~ **PARTIALLY RESOLVED 2026-06-17.**
   On this system, `C:\ISTS\WHOAMI.DBA` and `\\i2s109-solidcrm\DBAMFG$\WHOAMI.DBA`
   are both 2 bytes (CR+LF only — never initialized on this workstation).
   The "35-byte" format in earlier notes refers to a workstation where EVO has been
   configured. **`START_UP.DBA`** (27,083 bytes in `\\i2s109-solidcrm\DBAMFG$\`) is
   the DBA Manufacturing era startup program (TAS Pro 6 compiled binary — analogous
   to a .RUN file). Contains embedded registration: Ser No 75790, Exp 12/31/30,
   15 users, "American Backplane Inc." (legacy customer, now i2 Systems).
   Cannot decode WHOAMI.DBA format without a populated file from a configured workstation.

6. ~~**`CHMHELP.EVO`**~~ **RESOLVED 2026-06-17.**
   35 bytes = plain ASCII text: `"EvoHELP now set for this computer\r\n"`.
   Not a binary format — a simple marker file written when the CHM help system is
   configured for this workstation. Written once; presence/content tells the runtime
   that EvoHELP.CHM has been registered for this machine.

7. **`.btm` vs. `.RTM` — is `.btm` automatic backup?** Filenames align
   with RTMs suggesting yes, but the snapshot-on-save mechanism hasn't
   been observed in action.

8. ~~**Scheduler job table.**~~ **RESOLVED 2026-06-17.**
   Scheduler table = **ISSCHED**. Confirmed by DB fingerprint analysis:
   `EvoRemind.RWN`, `EvoSched.RWN`, `EvoScheduler.RWN`, `EVOSERVICE.RWN` all open ISSCHED.
   Also: `SCHEDCAL` table used by T7SHE (SH-E shop scheduling due dates) and T7SMH.

9. ~~**EvoLinks attachment storage.**~~ **RESOLVED 2026-06-17.**
   Table = **ISLINKS**. `EvoLinks.RWN` (156 procs) opens ISLINKS as its PRIMARY table.
   ISLINKS = the document attachment cross-reference (record key → linked document path/filename).
   Secondary users: T7SMSB, T7SMSC, T7SMTEND (SM sub-modules for document linking setup).

10. ~~**`BKARHINV/BKARHINV.BI2`**~~ **RESOLVED (2026-06-01).**
    The `BKARHINV/` subdirectory is a stale 2020 maintenance artifact.
    Full multi-company layout confirmed:
    - Each company's live Btrieve data lives in its own subdirectory:
      `DBAMFG$\I2\` (748 `.BI2` files, active), `DBAMFG$\22\` (frozen
      since 2/2020), `DBAMFG$\AB\`, `DBAMFG$\AT\`, `DBAMFG$\CA\`, etc.
    - The live AR Invoice History for company I2 is
      `DBAMFG$\I2\BKARHINV.BI2` (256 MB, updated 5/29/2026).
    - In March 2020 a rebuild operation left behind:
      `DBAMFG$\I2\BKARHINV.BI2.old` (154 MB, 3/18/2020) and a copy in
      `DBAMFG$\BKARHINV\BKARHINV.BI2` (154 MB, 3/25/2020). Both are
      orphaned backups — never cleaned up.
    - Company 22 (`BKARHINV.B22`, 74 MB, last written 2/8/2020) is
      an inactive/archived company.

11. ~~**The 205 help-only menu codes.**~~ **RESOLVED (2026-06-01).**
    All 205 codes are in encrypted `.RWN` programs — their logic is
    inaccessible without RWN decryption, but their *documentation* is
    now complete: every one is covered by the CHM consolidation pass
    (all 14 categories, ~700+ topics). Breakdown by module: SM 26,
    WO 21, HH 12, QC 11, SD 11, SO 10, BM 8, CM 8, TA 8, US 8,
    and 28 other modules with 1–6 codes each. These programs work
    correctly at runtime — they are simply opaque to static analysis.

13. **`suwin*.DCY` format — PARTIALLY RESOLVED 2026-06-17.**
    - **suwin6.dcy** → validated by **K_C** (`fdc2883f6d6537dd667270406d0a4c85969295ac`). Decrypted content is binary (not Delphi VCL text). K_C = bootstrap DCY key.
    - **suwin7.dcy** → still fails K_A, K_B, K_C, K_D. 3,527 bytes, entropy 7.945. A 5th key exists or it uses a completely different format.
    - **suwin6t.rwn / suwin7.rwn** → both validate with K_B (standard RWN key — expected).
    - **K_A** (`d97f05679438037073c30628734764020859f77e`) purpose remains unknown.
    - Remaining: identify what K_A encrypts; find key for suwin7.dcy.

~~12. **Customization forms (`J7*`).**~~ **RESOLVED 2026-06-17.**
    All 50 J7 RWN modules cataloged; 16 DFMs read for form titles and field labels.
    Key findings:
    - i2 Systems manufactures **corrugated packaging and mattress components** (BOX,CDBD,INSERT; mattress serial labels; TRAY,PALLET)
    - Confirmed customers: Lapco (outdoor workwear), Albertsons (grocery chain)
    - J7CC* = Corrugated/Cut operations: CCCutSheet, CCFabXfer, CCItemSync, CCPIC (PI count), CCSOLabels, CCSHI
    - J7HH* = Handheld: scan-to-ship mattresses, inventory adjust/transfer (EB=Edwards Brands?)
    - J7DC* = Data collection: Print Mattress Labels (J7DCMatLabels), Shipping scan (J7DCSSOE)
    - J7*SO* = Customer-specific SO variants: LapcoSO, i2SystemSOOE, RCSOImport, SOAImpLines
    - J7RC* = RC customer system integration (ConvTable, Pitex, SOImport)
    - J7NM* = NM division: Bins, Import, RTM reports
    - J7PT* = PT system integration: RecPOLine, PTWOKI
    - J7TMCKanban = TMC Kanban scheduling (599KB = complex)
    - J7SyncWOtoSO = Syncs WO data back to SO (422KB)
    - Full catalog in docs/03-modules/module-db-cross-reference.md Pass 18.

14. ~~**Module codes DE, IS, MM, PL, DI, RM, LM — unconfirmed names.**~~ **RESOLVED 2026-06-18.**
    - DE = Data Exchange (33 ops: import inventory/BOM/routings/customers/vendors/COA/labor; export to QuickBooks)
    - IS = i2 Systems Custom Reports (J5/J6/JM-prefix programs: Item Recap, Production Report, Top-N Shipped, New Customer)
    - MM = Manufacturing Management Reporting hub (4 menu ops reusing AP-J/AR-G/AP-A programs as reporting shortcuts)
    - PL = Payroll Link (confirmed from BKPLE.SRC: "Payroll Software Link Setup")
    - DI = Data Import Labor (DI-G = BKDIG, single-entry sub-module)
    - RM = Return Material Authorization — current module code (legacy code was AB in DBA era; RM is active in EVO menu)
    - LM = Lot/List Management (LM-B Item Generator Templates; LM-H Purge QC Receipts; **LM-E = Consolidate Inventory Transactions confirmed from BKLME.SRC**)

15. ~~**Full identity of the 16 "opaque" module codes (AB/CP/EX/FL/LM/MA/MM/PC/PL/RT/SB/SL/SY/UM/UP/YS).**~~ **RESOLVED Pass 106m 2026-06-18.**
    All 16 confirmed from DDF schema grep + share scan + BKLME.SRC read + BKMENUSU.TXT:
    - AB = Authorization/Licensing (BKABCUST/BKABVEND: license start/exp/period; serial+registered name; T6AB*.RTM = alt billing templates)
    - CP = Computer/Checkmark Payroll (legacy) — BKCPMSTR path config + BKCPEC AP check export records; superseded by PL
    - EX = Execute launcher wrapper — t7exec.RUN (one file, not a business module)
    - FL = Field Help — BKFLDHLP (HLP_CODE/INDEX/LINE — F1 context help text, not user-navigable)
    - LM = Lot/List Management — BKLMA-BKLMI.RUN; LM-E = Consolidate Inv Txns (SRC confirmed)
    - MA = Map Deposits + Material — T7MAPDEPO.DFM (BKAR.DEP.* apply deposits to SO); BKMATCST (10-tier qty/cost), BKMATRIM (machine trim)
    - MM = Mfg Maintenance (TAS6 legacy) — BKMMA-BKMMN.RUN (14 ops); predecessor to DM→LM
    - PC = Production Control (legacy) — BKPCKIT (kit components), BKPCPLOT (lot tracking with status/dates)
    - PL = Pay Link (active in menu) — "Pay Link" group; T6PLA.RUN (Checkmark), BKPLB/C/D.RUN
    - RT = Routing Templates (for Estimating) — BKRTCST/BKRTEMTR/BKRTSPEC/BKRTTEMP; T7RTMVALID = shared format-picker dialog
    - SB = Spec Book / Approved Source List — BKSBMFG (mfr+mfr-part), BKSBPART (substitutes), BKSBVEND (vendor+vendor-part); keyed by parent+product+customer
    - SL = Security Levels — BKSLEVEL (menu+level+13 flags), BKSLMSTR (level master); t7slsfc.RWN on share
    - SY = System tables (internal prefix) — BKSYMSTR/BKYSMSTR/BKSY* managed by SM/AD; not a menu group
    - UM = User Menu Security — BKUMSRTY (SCRTY_LEVEL/MENU/GROUP/ITEM_1..13)
    - UP = Update Management — BKUPDATE (company/update-flag/date/version)
    - YS = Yes/No System Parameters — T7YSYN.RWN edits BKYSMSTR (195+ YN flags)

16. **RWN bytecode pool type system + opcode table — PARTIALLY RESOLVED Pass 110/110b 2026-06-19.**
    Pool type system decoded from `suwin7.rwn` (34-instruction license-check program):
    - `0x41` = variable-length entry: `[41][00][len16][data]`. If data starts with `0xFD` it is a
      **compound blob** (argument block for one or more instructions). Printable-ASCII data = string constant.
    - `0x46` (F) = **variable reference**: `[46][val32_LE]` where `val32 = var_index × 77`.
      Confirmed: 4774/77=62 → SERIALNUMBER, 4851/77=63 → SNVALUE, 4697/77=61 → WAIT_SECS, 4620/77=60 → CURR_TIME.
    - `0x43` (C) = **pool pointer**: `[43][val32_LE]` where `val32` = byte offset from pool section start.
      Confirmed: C=0x33 → STR "DEMO", C=0x173 → STR "lblUserSerialNum", C=0x187 → STR "Caption".
    - `0x52` (R), `0x4E` (N), `0x4D` (M), `0x4C` (L), `0x49` (I), `0x44` (D), `0x53` (S) = fixed 5-byte numeric.
    - `0xFD` = compound blob begin marker (1 byte). `0xFF` = end-of-blob sentinel (1 byte).
    - Header[0x18] = 4620 = 60 × 77 = byte offset of first user-declared (non-TEMP) variable; TAS Pro 7
      always allocates exactly 60 TEMP variables (TEMP0–TEMP59) before user-declared variables.
    - Multiple dispatch entries point to different byte offsets within the same blob (each reads its own sub-field).

    **Pass 110b additions (25-program survey, 2026-06-19):**
    - DISP_START = 0x6C0 confirmed universal constant across ALL 25 programs (from 2-instruction T7MSG to 663-variable t7slsfc).
    - **0x57 (sub=0x05)**: Universal — in all 25 programs. T7MSG (the simplest TAS Pro 7 program, a message dialog with 2 instructions) uses 0x57 as its FIRST (and only functional) instruction, pointing to "T7MSG.DFM". Primary form-execution opcode: MOUNT/RUN form.
    - **0x20 (sub=0x05)**: Near-universal — 24/25 programs; only T7MSG lacks it. Also references DFM filenames. T7MSG proves 0x57 alone is sufficient to mount+run a form — 0x20 may be a secondary form-link or property-set operation.
    - **Branch family (sub=0x14)**: Opcodes 0x3B, 0xD2, 0x6A all share sub=0x14. Three jump/branch variants (exact conditional vs. unconditional distinction TBD).
    - **Proc names**: Length-prefixed Pascal short strings — byte[0]=name_length, bytes[1:1+length]=name. Confirmed from T7askbut: `\x14T7ASKBUT.ONOPENFILES`, `\x10T7ASKBUT.ONSTART`, `\x10T7ASKBUT.ONCLOSE`; domtest: `\x05START`.
    - **0x9A (sub=0x06)**: 1/25 programs — T7S1.RWN uses it to read "T7S1.TXT"; file-read opcode.
    - Full 17-opcode table in `docs/02-file-formats/rwn-binary-format.md`.

    **Still open sub-questions:**
    - What do the bytes immediately after the `0xFD` marker encode? (Values 0x00, 0x9A, 0x4D observed; 0x9A in
      blobs involving SNVALUE comparisons — may be a sub-opcode or argument-count byte.)
    - **0x57 vs 0x20 exact distinction**: Both sub=0x05, both reference DFMs. Hypothesis: 0x57=primary MOUNT (creates main window), 0x20=secondary MOUNT or SETPROP (registers event handlers). Needs more minimal-program data.
    - **0x40 role**: T7MSG uses it as FINAL instruction [1] (after 0x57 mounts the form), T7pass also uses it as a final instruction. Likely EXECUTE/WAIT (run the event loop until form closes) or EXIT.
    - **0x30 (sub=0x15)**: 10/25 programs, once per program. RETURN? END-OF-PROC?
    - Does `0x43` (C) type always encode a pool-section byte offset, or can it be a direct integer in some
      contexts? (All C values in suwin7.rwn are valid pool offsets, but sample size = 1 program.)
    - Does T7INA.RWN also have exactly 60 TEMP variables? Header[0x18]=4620 in both suwin7 and T7INA —
      is 60 TEMP vars a TAS Pro 7 compiler invariant? (t7slsfc also confirmed via 663-var header — 60 TEMP + 603 user)
    **Pass 110c additions (10-program form lifecycle analysis, 2026-06-19):**
    - **0x20 vs 0x57 RESOLVED**: 0x20 = CREATE FORM (first use → DFM string = TForm.Create) / BIND HANDLER (subsequent uses). 0x57 = EXECUTE FORM (ShowModal — enter event loop). Standard sequence: `[0x20→DFM][0x20→handler...][0x57→DFM][0x40/0x71→EXIT]`. T7MSG exception: uses 0x57 alone (0 procs, so Create+ShowModal collapsed).
    - **0x40/0x71 = EXIT PROGRAM**: Both are terminal opcodes. 0x40 sub=0x36 appears in T7MSG and t7pass. 0x71 sub=0x05 appears in T7askbut. Semantics identical; variant may encode a return code.
    - **evoDCs first instruction**: 0x20 → A[6]:460c12000000 (binary blob, not DFM string). This may be a dynamic form or a NULL form creation — needs further investigation.

    **Pass 229 additions (2026-06-23 — 3.2M instruction scale analysis + disassembly):**
    - **b2 byte = 0x00 universally CONFIRMED** across 3,204,306 instructions in 1,119 programs. Single exception: 0x57 EXECUTE_FORM has b2=0xFE for main-form launch.
    - **Sub-code families CONFIRMED at scale**: 15 sub-code values each map to a consistent family of related opcodes across ALL 1,119 programs.
    - **0x48/0xDC perfectly paired**: 0x48 appears 16,125×, 0xDC appears 16,121× in exactly the same 948 files (sub=0x19). Almost certainly PUSH/POP.
    - **0x49 = READ_PROP CONFIRMED**: EVOMENU_SELCOMP [0] reads `READ_PROP("NOVAZYGANDISTECHSUPPORT")` — tech-support mode bypass built into company selector dialog.
    - **0x6A = GOTO_LABEL**: uses pool STRING as label name (runtime label resolution). EVOMENU_SELCOMP: GOTO_LABEL("Items").
    - **0x4B = OPEN_FORM** (distinct from 0x20 CREATE/BIND) — EvoERPbackup uses 0x4B with DFM filename. Difference (open-existing vs create-new?) TBD.
    - **ISTS enhancement marker**: i2 Systems custom programs start with `ASSIGN(" - ISTS Enhancement MM/DD/YY")` at instruction [0] (EVODEFPRINT confirmed 06/15/17).
    - **Branch target encoding STILL UNKNOWN**: for 0x3B COND_BRANCH and 0xD2 GOTO, poff points into compound blob body (not at a STRING entry boundary). Pass 241 ruled out: instruction index, dispatch byte offset, packed low byte. Pass 242 confirmed: for GOTO_LABEL and CREATE/BIND, poff is an opcode-specific offset INTO a pool STRING entry (header+0, header+1, or header+4 depending on opcode). COND_BRANCH/GOTO poff points to compound blob body — needs tp7runtime.exe disassembly.
    - **Per-opcode poff delta (Pass 242 new finding)**: READ_PROP poff → header+0; CREATE/BIND form poff → header+0; GOTO_LABEL poff → header+1 OR header+4 (inconsistent across samples); CREATE/BIND bindings poff → header+4; ASSIGN/GOSUB/COND_BRANCH poff → compound blob body. Resolving the inconsistency requires tp7runtime.exe disassembly.
    - **New opcodes from suwin6t.rwn (Pass 242)**: OP_1A (sub=0x21, 11×), OP_31 (sub=0x10, 11×), OP_D9 (sub=0x07, 1×), OP_B9 (1×), OP_89 (1×), OP_8A (1×), OP_0C (1×), OP_45 (1×). OP_1A and OP_31 are significant (11× each in a 729-instruction program).
    - **Pool type 0x53 identified**: appears to be a second string type (same format as 0x41 but different type byte). Need more samples.
    - Current status: **C: 73/100**. Remaining unknowns: branch target encoding (requires tp7runtime disassembly); per-opcode poff delta; pool types 0x53/0x48/0x0C/etc.; semantics of OP_1A/OP_31; CALL family sub-semantics.

17. **TAS Pro 6 `.RUN` bytecode — 7-byte instruction format CONFIRMED, semantics mostly open (2026-06-19).**
    - Instruction format `[op:1][0x00:1][b2:1][addr_LE4:4]` confirmed for BKAWLB. Code section has
      instructions interleaved with inline data records (0x41-tagged strings/blobs).
    - **Resolved sub-questions (2026-06-19):**
      - **Var descriptor entry format CONFIRMED**: exactly 7 bytes per entry. `[type_tag:1][0x00:1][storage_size:1][runtime_offset_LE4:4]`. 45 entries for BKAWLB, cumulative offsets hold across all 45 entries.
      - **runtime_base NOT universal**: 0x0460 for var_size=1440/table_count=30 programs; 0x02D0 for var_size=2640/table_count=55. Header field that encodes it: not yet identified.
      - **Instruction addr semantics**: addr = runtime_base + cumulative_runtime_offset. Array elements: addr = first_element_addr + n×element_size (no per-element descriptor entries).
    - **Resolved (Pass 243, 2026-06-24):**
      - **pfmt/pblnk = DECLARATIVE** — they compile to ZERO bytecode in TAS Pro 6. They are report
        format directives processed at print time by the .RTM file, not executed as instructions.
        Proof: BKAWLB has 9 pfmt + 2 pblnk statements but 34×OP_53 + 62×OP_65 — impossible ratio.
      - **OP_53 ≠ PFMT, OP_65 ≠ PBLNK** — previous identification was wrong.
      - **PRT_TOF** (8 pfmt + 2 pblnk + page=page+1 + ret) = 2 bytecode instructions only:
        ASSIGN(page=page+1) at I#1789 + RET_FUNC(ret) at I#1790.
      - **All ENT section ENTERs use OP_0E (0x0E)** — confirmed in I#46–213 (preamble interactive stream).
      - **Binary section map for BKAWLB**: I#214=VIEW(MOUNT); I#223–240=PRT_DETAIL 18 COND_JMPs;
        I#1773–1790 = ABORT_RPT through PRT_TOF; I#313–372 = subroutine area (DSP_WORD1–DSP_CUST_2).
    - **Resolved (Pass 244):**
      - **Dual-channel architecture confirmed**: b2 = data record size; addr = absolute file offset.
        Data channel starts at file offset 0, records pack sequentially (addr_next = addr_prev + b2_prev).
        100% verified across all 2078 instructions. Data channel total = h[0x08] bytes (0x923E for BKAWLB).
      - **OP_93/OP_65/OP_53 = FIELD_ENTER execution family**: data records contain embedded 7-byte instruction
        records for field validation/callback logic. OP_93(20 bytes)=field setup; OP_65(10 bytes)=callback attr;
        OP_53(125 bytes)=full field exec (~17 embedded instructions).
      - **BKMRF pre-instruction value**: = total data channel bytes for preamble instructions (same h[0x08] concept).
    - **Still open:**
      - **Exact semantic meaning** of each embedded instruction within OP_93/OP_65/OP_53/OP_8D data blobs.
      - **OP_8D(b2=20)**: follows OP_53 in field-enter clusters; data contains embedded instructions; role unknown.
      - **Remaining unknown opcodes**: OP_25, OP_22, OP_15, OP_16, OP_32, OP_2D, OP_43, OP_4A,
        OP_5D, OP_56, OP_1B, OP_1A, OP_44, OP_47, OP_48, OP_57
      - **runtime_base formula**: which header field encodes the runtime_base threshold?

## Newly Confirmed Tables (Pass 239) — DDF Schemas Not Yet Validated

| Table | First Seen | Confirmed From | Schema Status |
|---|---|---|---|
| BKSYPRTR | ISSHPCAL2+T7ISASER (Pass 239) | DB file table entry | DDF not found; system printer configuration |

## Newly Confirmed Tables (Pass 236–237) — DDF Schemas Not Yet Validated

These tables were first documented from var extraction but have not been cross-checked against
the 659-table DDF schema catalog (tier2-tables.md). May not be present in the Pervasive DDFs.

| Table | First Seen | Confirmed From | Schema Status |
|---|---|---|---|
| BKSYAR | T7SORevu (Pass 238) | DB file table entry | DDF not found; AR system params (parallel to BKSYAP) |
| ISARCHG | T7SORevu (Pass 238) | DB file table entry | DDF not found; IS-era AR change audit (parallel to ISAPCHG) |
| BKICREF | T7POS (Pass 236) | DB file table entry | DDF not found; structure unknown |
| ISORDECO | T7POSI (Pass 236) | DB file table entry | DDF not found; structure unknown |
| BKSYAP | T7POA (Pass 237) | BKSY.AP.* 24-var namespace | DDF not found; new AP system params table |
| ISAPEX | T7POA (Pass 237) | ISAPEX.* 22-var namespace | DDF not found; ACH/bank approval record |
| ISECO | T7POA (Pass 237) | IS.ECO.* 12-var namespace | DDF not found; ECO record |
| ISJOB | T7POA (Pass 237) | IS.JOB.* 9-var namespace | DDF not found; job-cost job master |

**Next step:** Search for these table names in the 659-table DDF listing. If absent, they may be
Btrieve tables defined in `.DDF` files outside the main DBAMFG$ share, or they may be newer
additions not in the DDF extract.

---

## Nice-to-have follow-ups (not blocking)

- **Extract CHM contents fully.** Ran `hh -decompile` but it quietly
  produced nothing. A `chmlib`/`7z` port would extract the actual
  HTML topic bodies. The help topics would triple the qualitative
  understanding of "what does this operation do" beyond what we have.

- **Scripted diff of DFMs across releases.** Given that we parse DFMs
  reliably, and the CHM hints at additions over time, a diff-tool
  would show exactly what changed between two EVO releases.

- **Cross-reference RTM data-field names to their TAS buffer source.**
  When a TppDBText is bound to `BKAP.CHK.AMTPD`, we know that string
  is the TAS program's buffer-column name — but the *source field* it
  reads from lives in the TAS program. Only partial without decrypted
  RWNs.

- ~~**Build an "EVO everything" SVG diagram**~~ **DONE (2026-06-01).**
  Module interdependency map with Mermaid directed graph, 40-module
  tier table, and key data flow narratives at
  [docs/06-module-map/module-map.md](../docs/06-module-map/module-map.md).

---

The autonomous pass achieved effectively complete external understanding
of EvoERP. Further depth requires a running instance, database ODBC
attach, or RWN decryption — all of which are out of scope for the
read-only study.
