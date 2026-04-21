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

1. **Decrypt `.RWN` / `.DCY`.** Would need either:
   - A key extracted from `tp7runtime.exe` (requires careful reverse
     engineering), or
   - A running trace that captures the decryption call.

   Impact if resolved: we could read every compiled program's logic
   without running it, close most "how does XX-Y actually work" gaps.

2. **Exact ACCES_1..20 → module mapping** in the security model.
   Easiest path: watch a running `Enter Users` (`SM-?`) screen save a
   user and read the bytes written to `AHSYLOG`.

3. **Password hashing algorithm.**
   Almost certainly a call to the runtime's `ENCRYPTSTR` with a
   built-in key. Not decoded.

4. **Menu tree storage format.** Is the EVO menu tree a DB table, or
   inside `EVOERPMENU.DCY`? If DB: can be dumped. If DCY: gated on #1.

5. **`WHOAMI.DBA` format** (35 bytes). Per-workstation identity token.
   Purpose is clear (identifies the seat for locking + license), but
   the 35-byte layout is not reverse-engineered.

6. **`CHMHELP.EVO`** (35 bytes). Same size as `WHOAMI.DBA` — likely a
   similar identity-style marker. Purpose unknown.

7. **`.btm` vs. `.RTM` — is `.btm` automatic backup?** Filenames align
   with RTMs suggesting yes, but the snapshot-on-save mechanism hasn't
   been observed in action.

8. **Scheduler job table.** Presumably a `BKSCHED*` or similar, but
   we didn't find one in the 649-table inventory. Possibly named
   differently or only populated at run time in memory.

9. **EvoLinks attachment storage.** Hypothesis: `LinkDoc\` folder for
   the files, a database table for the `<record-key, filename>`
   mapping. Not confirmed by table-name inspection.

10. **`BKARHINV/BKARHINV.BI2`** — appears to be a company `I2`
    overflow / split file. But the parent `BKARHINV.B22`/`.B` etc.
    exist in normal positions, so this `BKARHINV/` subdir is unusual.
    Exact purpose TBD.

11. **The 205 help-only menu codes.** Operations documented in the
    CHM but with no matching readable `.RUN`/`.RWN` string. List in
    `samples/master_index.csv`.

12. **Customization forms (`J7*`).** 20+ customer-specific
    customization modules (`J7AIJCG`, `J7BEFWebInv`, `J7CCCutSheet`,
    `J7CRSOW`, `J7DCMatLabels`, etc.). We inventoried them but didn't
    dig into any single one. They're third-party and vary by customer.

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

- **Build an "EVO everything" SVG diagram** of module ↔ table ↔ form
  dependencies, sourced from the CSVs we now have. A visualization
  pass, not a research pass.

---

The autonomous pass achieved effectively complete external understanding
of EvoERP. Further depth requires a running instance, database ODBC
attach, or RWN decryption — all of which are out of scope for the
read-only study.
