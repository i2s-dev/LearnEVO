# CLAUDE.md — LearnEVO Playground

Rules and durable context for every future session in this workspace.
If anything here is ambiguous, stop and ask. Do not guess.

---

## 0. BROKEN.md — mandatory first read every session

**ALWAYS read `BROKEN.md` at the repo root before doing anything in this workspace.**
This document logs every bug found and every fix attempted (successful or not).

Rules:
- Every bug or mistake encountered **must** be logged in `BROKEN.md`. No exceptions.
- Log: symptom, root cause, every attempt (whether it worked or not), date, and a lesson.
- Newest entries go on top. When fixed, mark status ✅ FIXED.
- **Never retry a fix already listed as "didn't work"** without explicit reasoning for why a
  different outcome is expected now.
- Before attempting any fix, re-read the relevant `BROKEN.md` entry. If you are about to
  retry something already listed as failed, stop and pick a different approach — or ask.

---

## 1. Scope — where I may and may NOT act

**READ-ONLY (never write, edit, delete, rename, move, create, or overwrite):**

- `C:\ISTS\` — the local EvoERP client install (and all subfolders).
- `\\i2s109-solidcrm\` — the network share (and every subfolder, including
  `\\i2s109-solidcrm\DBAMFG$\`, `\\i2s109-solidcrm\evo-ERP\`,
  `\\i2s109-solidcrm\ISTS\`, `\\i2s109-solidcrm\EVOReports\`,
  `\\i2s109-solidcrm\2004.1\`).

Reading, opening, hex-dumping, grepping, copying-out-to-this-folder: all fine.
Any write-side operation on those paths: forbidden, full stop. If a tool call
would touch them, don't run it — even if it looks harmless (e.g. "just
creating a backup", "just touching a timestamp").

**READ-WRITE (free to do anything):**

- `C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\`
  — this folder and everything under it. This is the playground, notes,
  extracted samples, and documentation plaza.

If I need to study a file from a forbidden path, I **copy** it into this
folder (preserving the original) and work on the copy.

---

## 2. Mission

The user wants to learn, in full and from the ground up, how the EvoERP
software works — every module, every file, every data flow. My job:

1. **Study the actual program files** as the primary source of truth.
2. **Document** findings here, organized by topic, in a way that builds up
   a complete picture over many sessions.
3. **Stay autonomous** — after finishing a documentation pass, immediately
   pick the next unknown and dig into it. No waiting for prompts.
4. **Use online research** only to get footholds (e.g. what is TAS
   Professional 7, what is a .DFM file format) or when stuck. Most work
   happens inside the EVO files themselves.

Keep the docs **meticulous**: cite file paths and offsets, include short
code excerpts, note what is confirmed vs. inferred vs. guessed.

---

## 3. What EVO is (working model — update as I learn more)

- **EvoERP** is a manufacturing ERP, evolved from DBA Manufacturing.
- Built on **TAS Professional 7** (`tp7runtime.exe`) — an xBase-family 4GL
  runtime from Computer Keyes / Business Tools.
- Main launcher: `C:\ISTS\StartEvo.exe` → runs `tp7runtime.exe` against
  `\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn`.
- Reporting engine: **Nevrona ReportBuilder** (`RBDsgnr.exe`, `.RTM` files).
- Data dictionary / forms / compiled code all live on the network share.
- File type quick-reference (confirmed by inspection):
  - `.SRC` — TAS Pro 7 source code (text)
  - `.RWN` — compiled TAS Pro 7 program (runtime-loadable)
  - `.RUN` — older TAS Pro 6 compiled program
  - `.DFM` — Delphi-style form (UI layout)
  - `.DCY` — data dictionary (schema definitions)
  - `.RTM` — ReportBuilder report template
  - `.B`   — Btrieve / B-tree data file
  - `.TXT` — exported report / data dump
  - `.DBA` — configuration / identity file (e.g. WHOAMI.DBA)
  - `.UPD` — update/patch definition
  - `.IMP` — import definition

All of this is **starter knowledge** — the documentation in `docs/`
supersedes it once filled in.

---

## 4. Working conventions

- **File naming in the ERP:** `T7xxy.*` = TAS Pro 7 era, module `xx`
  (AR=A/R, AP=A/P, IN=Inventory, SO=Sales Orders, PO=Purchase Orders,
  WO=Work Orders, GL=General Ledger), variant `y`. `T6xxy.*` = older
  TAS Pro 6 generation, often still in use.
- **Folder layout in this workspace:**
  - `docs/` — the documentation plaza, organized by topic.
  - `research/` — scratch notes, open questions, dead ends.
  - `samples/` — copies of small EVO files pulled over for inspection.
    Each sample's source path is recorded in a sibling `.source.txt`.
  - `scripts/` — any tooling I write to parse/analyze EVO files.
- **Docs style:** Markdown, short sentences, cite with
  `path\to\file.ext:offset` or line numbers. Mark status tags at the top
  of each doc: `Status: draft | verified | partial | open-questions`.
- **Never** claim something is "verified" unless I can point at the bytes
  or code lines that prove it.

---

## 5. Autonomy protocol

When a task completes:
1. Write/update the doc for what I just learned.
2. Update the index (`docs/README.md`) so the new doc is discoverable.
3. Open `research/OPEN_QUESTIONS.md`, pick the highest-value unknown, and
   start on it. Don't stop to ask unless I hit the scope boundary in §1
   or genuinely need a decision from the user.

End-of-turn summary: one or two sentences — what I documented, what I'm
digging into next.

---

## 6. Bug-fix tracking (mandatory)

Every bug I attempt to fix in this workspace **must** be logged in
`BUGS.md` at the repo root. This is non-negotiable.

For each bug:
- Record the symptom, the final root cause, and **every single thing I
  tried** — whether it worked, whether it didn't, and why.
- Date each attempt. Newest bug entries go on top.
- Never repeat a fix that is already listed as "didn't work" for the same
  bug without explicit reasoning for why I expect a different outcome now.
- When a bug is fixed, mark status and capture a one-line lesson so I
  don't waste the user's time rediscovering it next month.

Before attempting any fix, re-read the relevant `BUGS.md` section. If I
catch myself about to retry something already listed as failed, stop and
pick a different approach — or ask.

---

## 7. ANALYZE command

When the user types **ANALYZE** into the chat, execute the following loop immediately and autonomously — no further prompting needed:

1. **Read `EVO-DECOMPILE-TODO.md`** in full. Identify every item that is either:
   - Not yet started (⬜), or
   - Started but below C: 90/100

2. **Prioritize work in this order:**
   a. Untouched areas (⬜, no work done at all) — broadest coverage gain first
   b. Lowest-confidence started items (🔄 or ✅ with C: < 50) — biggest relative gains
   c. Items in the 50–74 range — push toward 75+
   d. Items in the 75–89 range — push toward 90+

3. **For each item worked:**
   - Study the relevant EVO files (copy to `samples/` first if from a read-only path)
   - Document findings in the appropriate `docs/` file
   - Update confidence rating and checkbox in `EVO-DECOMPILE-TODO.md`
   - Update `docs/README.md` index if a new doc is created
   - Update `research/OPEN_QUESTIONS.md` if a question is answered or a new one surfaces

4. **Keep going** until blocked by encryption (§14 items requiring RWN decryption) or a
   genuine decision point. Do not stop between topics to ask.

5. **Session-end:** update `EVO-DECOMPILE-TODO.md` with all new confidence ratings and
   checked boxes, then give a one-paragraph summary of what changed.

---

## 8. Confidence ratings — mandatory on every EVO answer

**Every single response about EvoERP or this project must end with a confidence rating.**
No exceptions. This applies to:
- Any question about how EVO works
- Any explanation of a module, table, field, or workflow
- Any claim about a file format, data flow, or behavior
- Any "how do I" answer
- Any guess or inference about the system
- Even short factual answers (e.g., "The AP vendor table is BKAPVEND")

**Format:** Append to the end of every answer:

> **Confidence: XX/100** — one sentence explaining what is verified vs. inferred vs. unknown.

Use the same 0–100 scale as `EVO-DECOMPILE-TODO.md`:
- 90–100: Fully verified from file bytes / source code / confirmed schema
- 70–89: Mostly verified; minor gaps or unconfirmed edge cases
- 50–69: Solid foundation with confirmed facts; significant unknowns remain
- 30–49: Key facts confirmed; core logic or schema incomplete
- 10–29: Surface-level only — structure identified, content opaque
- 0–9: Essentially unknown

If a response covers multiple topics with different confidence levels, give the **lowest** rating that applies and call out which part is the weakest.

---

## 9. Final deliverable documents

Two master documents must be built up over time and kept current as research progresses.
These are the end-state products that define "done."

### 8.1 PROJECT-STRUCTURE.md

A single file at the workspace root that catalogs **every path and file within the EvoERP
install and network share** and explains:
- What each file is (type, format, purpose)
- Which module or subsystem owns it
- How it relates to other files (e.g., T7INA.RWN ↔ T7INA.DFM, RTM ↔ SRC caller, .B ↔ DDF)
- Which database tables it reads or writes (where known)
- Generation (BK\*, T6\*, T7\*, EVO\*, J7\*, etc.)

Organized hierarchically: top-level directories → subdirectories → individual files.
Cross-references use relative paths. Status column: `confirmed | inferred | unknown`.

Update this document every session as new files are discovered or relationships confirmed.

### 8.2 HELP-RESOURCES.md

A comprehensive, searchable knowledge base — the EvoHELP.CHM on steroids. Its purpose:
**allow a user (or a user + Claude) to answer abstract "how do I…" questions about EVO**
without needing to know exact menu codes or table names in advance.

Structure:
- **Keyword index** — every significant term in EVO (table names, field names, menu codes,
  module names, business concepts) with a one-line definition and pointer to deeper docs
- **How-to recipes** — step-by-step answers to common tasks (e.g., "How do I add a new
  column to a report and print it?", "How do I create a new vendor?", "How do I close the
  month?")
- **Concept explanations** — what is a Work Order, what is a Routing, what is MRP, etc.
- **Table quick-reference** — one-liner per table: what it stores, primary key, which module
- **Field lookup** — given a field name (e.g., BKAP_CHK_INVNUM), explain what it means and
  where it appears in the UI
- **Error / symptom index** — if something goes wrong or looks wrong, what to check

Write in plain English. Abstract questions are the target audience: a user who knows what
they want to accomplish but does not know which menu, table, or file is involved.

Keep this document updated as each module and workflow is documented. It is the
user-facing summary of everything in `docs/`.

---

## 10. Decompilation work — what is and is NOT currently unblocked

**At the start of every session, read `START-HERE-DOCUMENTATION-PROGRESS.md`.**
That document is the authoritative record of what is unblocked, what is blocked, the
current blocker, how to resolve it, and the highest-value next tasks. It supersedes any
older summary you may have in context.

Short version (as of 2026-06-12):
- **Unblocked:** `.RUN`, `.DFM`, `.RTM`, `.B` analysis; Rosetta Stone opcode mapping;
  all documentation updates; per-table field docs; module logic from forms+reports
- **Blocked:** any `.RWN` / `.DCY` decryption — cipher is Twofish-CFB, passphrase is
  `mabufoju`, key derivation is SHA1+4zeros (192-bit) — but the initial IV (`block_buf`)
  is uninitialized heap and requires one debugger session to recover
- **Note:** Only 7 `.SRC` files exist on the network share; all TAS Pro 7 logic is
  binary-only in `.RWN` files
- Do NOT write stub or placeholder code for blocked tasks — it creates false progress

---

## 11. Living documents — keep these current every session

The following documents must be updated whenever relevant findings are made. They are
not one-time artifacts; they are the running record of the project. Update them in the
same session as the work that generates the findings — do not defer.

| Document | What it tracks | Update trigger |
|----------|---------------|----------------|
| `BROKEN.md` | Every bug, mistake, and failed fix — **mandatory read at session start** | Any bug encountered or fix attempted |
| `BUGS.md` | learnevo-help browser bugs and launcher fixes | Any UI/server bug or launcher change |
| `START-HERE-DOCUMENTATION-PROGRESS.md` | Current blocker, what is/isn't unblocked, research snapshot | Any change to what is blocked or unblocked |
| `EVO-DECOMPILE-TODO.md` | Confidence ratings and checklist for every analysis area | Any finding that changes a confidence rating |
| `research/OPEN_QUESTIONS.md` | Unresolved questions; answers when resolved | Any question answered or newly discovered |
| `PROJECT-STRUCTURE.md` | Catalog of every EvoERP file and its purpose | Any new file discovered or relationship confirmed |
| `HELP-RESOURCES.md` | User-facing knowledge base: tables, fields, recipes | Any module, table, or workflow documented |
| `docs/02-file-formats/decryption-findings.md` | RWN/DCY cipher reverse-engineering — all confirmed facts and failed attempts | Any cipher/key/IV finding |
| `docs/README.md` | Index of all docs in `docs/` | Any new doc created |

Rules:
- Update confidence ratings in `EVO-DECOMPILE-TODO.md` when findings change them.
- Mark questions resolved in `OPEN_QUESTIONS.md` inline with the answer and date.
- Update `START-HERE-DOCUMENTATION-PROGRESS.md` whenever the blocker changes.
- Update `decryption-findings.md` immediately after any cipher/key/IV finding, successful or not.
- Never let `BROKEN.md` get behind — log every attempt before it is forgotten.

---

## 12. Launcher scripts (.bat / .ps1) — keep them current

The user launches tools in this workspace via `.bat` files (e.g.
`RUN.bat`, `learnevo-help\launch.bat`). Whenever I change how a tool
starts up, fix a startup-related bug, or learn a new invariant about a
process (zombie cleanup, headers, port handling, environment), I **must**
update the relevant launcher scripts in the same change so the user's
one-click experience stays correct.

Concrete rules:
- If a fix only works "after restarting X", the launcher must make that
  restart automatic, not rely on the user remembering.
- If stale processes from prior sessions can cause bugs, add a cleanup
  step at the top of the launcher. Prefer calling a small `.ps1` helper
  over inlining complex PowerShell in a `.bat` (batch quoting is fragile).
- Keep the two launchers (`RUN.bat` at repo root, `learnevo-help\launch.bat`)
  behaviorally identical. They should both run `server.py`, not
  `python -m http.server`, so the `Cache-Control: no-store` header is
  always present.
- Log every launcher change in `BUGS.md` under the bug that motivated it.
