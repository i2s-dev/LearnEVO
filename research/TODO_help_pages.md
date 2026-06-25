# TODO — Help System Content Gaps

Status: in-progress
Generated: 2026-04-21. Last recount: 2026-04-21 after completing sections A, D, F.

**Totals:** ~2,720 pages in the help system; **88 are stubs** (was 104 — 16 resolved).

**Completed this pass:** Section A (11 broken-link duplicates fixed via a build-side canonicalizer), Section D (4 format pages written), Section F (1 architecture page written). See [learnevo-help/content/topics.py](../learnevo-help/content/topics.py) and [learnevo-help/content/glossary.py](../learnevo-help/content/glossary.py).

Stubs come from [learnevo-help/build.py:372-422](../learnevo-help/build.py#L372-L422): the build script scans every page for `(#foo)` links and synthesizes a placeholder for any target ID that doesn't have a real page. So "stub" = "something linked to this, but nobody wrote the content yet."

---

## A. Broken links — DONE ✓

Resolved by two changes in [learnevo-help/build.py](../learnevo-help/build.py):

1. Added `_canonicalize(pid)` helper — if a wiki-link or see-also ref matches a glossary term case-insensitively, rewrite to `glossary-<slug>`.
2. Threaded that through `convert_wiki_links` and `_resolve_ref` so both code paths canonicalize.

Also added two new glossary entries to cover binary filenames that had no home: `EvoHELP.CHM` and `tp7runtime.exe`. See [learnevo-help/content/glossary.py](../learnevo-help/content/glossary.py).

All 11 stubs eliminated: `Btrieve`, `CFB`, `DCY`, `DDF`, `DFM`, `FIFO`, `Pervasive`, `RTM`, `Twofish`, `EvoHELP.CHM`, `tp7runtime.exe`.

---

## B. Recipe stubs — need real content (35)

Every Recipe page is a stub. Recipe IDs are baked into the search synonyms at [build.py:533-581](../learnevo-help/build.py#L533-L581) but no recipe content has been written.

Ordered roughly by likely priority (daily-use workflows first):

### B.1 Daily-use workflows
- [ ] `recipe-login` — how to start EVO and sign in
- [x] `recipe-enter-customer` ✓ (written in recipes.py)
- [x] `recipe-enter-vendor` ✓ (written 2026-06-25)
- [x] `recipe-enter-item` ✓ (written 2026-06-25)
- [x] `recipe-enter-po` ✓ (written 2026-06-25)
- [x] `recipe-receive-po` ✓ (written 2026-06-25)
- [ ] `recipe-receive-stock` — direct receipt without PO
- [x] `recipe-enter-voucher` ✓ (written in recipes.py)
- [x] `recipe-print-checks` ✓ (written in recipes.py)
- [ ] `recipe-pick-invoices`
- [ ] `recipe-print-invoice`
- [x] `recipe-record-payment` ✓ (written in recipes.py)
- [ ] `recipe-print-statements`

### B.2 Sales / shipping
- [x] `recipe-enter-so` ✓ (written in recipes.py)
- [x] `recipe-so-pick-ship` ✓ (written 2026-06-25)
- [ ] `recipe-so-to-cash`
- [ ] `recipe-estimate`
- [ ] `recipe-rfq`
- [ ] `recipe-rma`
- [ ] `recipe-credit-memo`

### B.3 Manufacturing
- [x] `recipe-work-order` ✓ (written in recipes.py)
- [x] `recipe-enter-bom` ✓ (written 2026-06-25)
- [x] `recipe-enter-routing` ✓ (written 2026-06-25)
- [x] `recipe-run-mrp` ✓ (written in recipes.py)
- [x] `recipe-dc-labor` ✓ (written 2026-06-25)

### B.4 Inventory
- [x] `recipe-adjust-inventory` ✓ (written 2026-06-25)
- [ ] `recipe-transfer-stock`
- [x] `recipe-physical-inventory` ✓ (written in recipes.py)
- [ ] `recipe-close-po`

### B.5 Period / compliance
- [x] `recipe-ar-aging` ✓ (written 2026-06-25)
- [x] `recipe-month-end-close` ✓ (written in recipes.py)
- [ ] `recipe-year-end-close`
- [x] `recipe-financial-statements` ✓ (written 2026-06-25)
- [ ] `recipe-1099`
- [ ] `recipe-void-check`
- [ ] `recipe-purge-history`
- [ ] `recipe-po-to-payment`

### B.6 Admin / utilities
- [ ] `recipe-add-user`
- [ ] `recipe-add-company`
- [ ] `recipe-switch-company`
- [ ] `recipe-backup`
- [ ] `recipe-update-evo`
- [ ] `recipe-custom-report`
- [ ] `recipe-export-csv`

---

## C. Module stubs — need real content (45)

Modules referenced from somewhere in the corpus but not yet documented. Many of these two-letter codes are guesses from linkers — some may turn out to be aliases, dead codes, or wrong references.

Verify each against actual EVO menu structure before writing.

```
module-AB   module-AC   module-CM   module-CP   module-CR
module-DE   module-DI   module-EX   module-FA   module-FL
module-FO   module-FP   module-HH   module-IC   module-IM
module-IS   module-LC   module-LM   module-LO   module-LW
module-MA   module-MM   module-PC   module-PL   module-PS
module-QT   module-QU   module-RF   module-RM   module-RO
module-RT   module-SA   module-SB   module-SC   module-SD
module-SL   module-SU   module-SY   module-TA   module-UM
module-UP   module-US   module-UT   module-WC   module-YS
```

**Next step before writing:** dump EVO's module list (from menu tables or filename `T7xx*` / `T6xx*` patterns) and reconcile against this list. Any entry above that isn't a real module → the link that created it should be fixed. Any real module missing from above → write a proper page for it.

---

## D. File-format stubs — DONE ✓

All four written in [learnevo-help/content/topics.py](../learnevo-help/content/topics.py). Content drawn from the deep-dive docs in [docs/02-file-formats/](../docs/02-file-formats/) plus fresh sample inspection.

- [x] `format-src` — TAS Pro 7 source code (text)
- [x] `format-rwn` — compiled TAS Pro 7 program (covers the encrypted DCY/SCY/LCY family)
- [x] `format-dfm` — Delphi-style form layout
- [x] `format-rtm` — ReportBuilder report template

---

## E. Cross-cutting topic stubs — need real content (8)

High-value deep dives; several of these are foundational to the mission.

- [ ] `encryption` — overview of EVO's crypto use
- [ ] `dcy-rwn-decryption` — concrete algorithm for decrypting `.DCY` / `.RWN` files
- [ ] `src-deep-dive` — TAS Pro 7 SRC language walk-through
- [ ] `taspro7-ini-reference` — TP7Runtime configuration file
- [ ] `help-system` — how EVO's own help system works (`EvoHELP.CHM`)
- [ ] `reporting-pipeline` — end-to-end: data → RTM → ReportBuilder → output
- [ ] `menu-codes-reference` — canonical list of `XX-Y` / `XX-Y-Z` menu codes
- [ ] `field-search` — what this means in the EVO UI (F-key? form feature?)

---

## F. Architecture stubs — DONE ✓

- [x] `subsystem-evoupdate` — the `.UPD` update/patch mechanism. Includes evidence that `.UPD` files are Btrieve-format (FC magic), the full EvoUpdate program family, and the four restructure phases per FD.

---

## G. Pages that don't exist *at all* and aren't even stubs

The auto-stub system guarantees a placeholder exists for **every page that is linked to**. So "not linked anywhere yet" is the only way a page can be totally absent. Candidates I suspect are missing outright (need verification):

- [ ] **Per-table schema pages** for every `BK*` table that doesn't yet have one. Expected IDs: `table-BK<xx><name>`. Compare actual table IDs in `pages.json` against a definitive list pulled from the `.DCY` files in `\\i2s109-solidcrm\DBAMFG$\`.
- [ ] **Per-form UI pages** for every `.DFM` file not yet linked. Expected IDs: `form-<name>`. Enumerate DFMs on the share and diff against existing `form-*` pages.
- [ ] **Per-report pages** for every `.RTM` file. Expected IDs: `report-<name>`. Enumerate RTMs and diff.
- [ ] **Launcher / entry-point pages**: `StartEvo.exe`, `RUN.bat`, individual EVO utilities in `C:\ISTS\`.
- [ ] **Network topology / install layout** — how the local client and share interact during a session.
- [ ] **Btrieve / Pervasive low-level I/O page** — the glossary entries exist but no deep-dive on how TAS Pro issues Btrieve ops.

These need a dedicated enumeration pass before they can be itemized the way the stub list above is.

---

## How to use this file

1. Work items in sections **B–F** are the concrete backlog — pick one, write the real content into [learnevo-help/build.py](../learnevo-help/build.py) (or a new content-source file the build script reads), rebuild, verify no stub.
2. Section **A** is a link-repair pass, not a writing pass — cheaper to knock out first to reduce stub count.
3. Section **G** requires a discovery pass before it becomes actionable; treat it as an open research thread.
4. When a stub is eliminated, **remove its line from this file** and re-run the stub count at the top.
5. Rebuild after changes: `python learnevo-help/build.py`, then confirm stub count fell by the expected amount.
