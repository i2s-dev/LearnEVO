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

2. **Exact ACCES_1..20 → module mapping** in the security model.
   Easiest path: watch a running `Enter Users` (`SM-?`) screen save a
   user and read the bytes written to `AHSYLOG`.

3. **Password hashing algorithm.**
   Almost certainly a call to the runtime's `ENCRYPTSTR` with a
   built-in key. Not decoded.

4. ~~**Menu tree storage format.**~~ **RESOLVED 2026-06-17.**
   `EVOERPMENU.DCY` decrypted with K_D → Delphi VCL TEditForm1 DFM, 20,868 lines.
   **Finding:** The DCY file is the main ERP window shell only — it contains:
   - TMainMenu with ~35 TMenuItems (top-level bar: File, Module, Tools, Size, Support, Help)
   - TToolBar with 33 TToolButtons (the icon toolbar)
   - 8 × TTASStrList (empty at parse time — populated at runtime)
   - TImage, TPanel, TStatusBar, TStatusBar, TShellExe, etc.
   **The 554+ module-level menu codes (AR-1, IN-2, etc.) are NOT stored here.**
   They are built at runtime by EvoERPmenu.RWN dynamically. The DCY is just the window frame.

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
    - LM = Lot Management (LM-B Item Generator Templates; LM-H Purge QC Receipts — confirmed 2 menu entries)

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
