<!-- SECTION INDEX — Read this first. Grep for an anchor to jump to a section. -->
<!--  All rules are preserved in full below — only read sections relevant to your task. -->

| # | Anchor | Section | When relevant |
|---|--------|---------|---------------|
| 0a | `SECTION:0a-programs` | programs/ — custom standalone software | Building or modifying a program in programs/ |
| 0 | `SECTION:0-broken-md` | BROKEN.md — mandatory first read | Every session start; before any fix attempt |
| 1 | `SECTION:1-scope` | Scope — read-only vs read-write paths | Any file operation; any write action |
| 2 | `SECTION:2-mission` | Mission | Orientation; first session |
| 3 | `SECTION:3-what-evo-is` | What EVO is (working model) | First session; unfamiliar file types |
| 4 | `SECTION:4-conventions` | Working conventions | Naming files, creating docs, citing sources |
| 5 | `SECTION:5-autonomy` | Autonomy protocol | End of any task; deciding whether to continue or stop |
| 6 | `SECTION:6-issue-tracking` | Bug-fix and issue tracking | Any bug encountered or fix attempted |
| 7 | `SECTION:7-analyze` | ANALYZE command | When user types ANALYZE |
| 8 | `SECTION:8-confidence` | Confidence ratings | Every EVO answer |
| 9 | `SECTION:9-deliverables` | Final deliverable documents | Updating PROJECT-STRUCTURE or HELP-RESOURCES |
| 10 | `SECTION:10-decompilation` | Decompilation work — current status | Any decompilation or decryption task |
| 11 | `SECTION:11-living-docs` | Living documents — keep current | After any documentation pass |
| 12 | `SECTION:12-launchers` | Launcher scripts | Any change to RUN.bat or launch.bat |
| 13 | `SECTION:13-new-rules` | New operating rules (2026-07-06) | Agent workflow, issue routing, document navigation |

---

# CLAUDE.md — LearnEVO Playground

Rules and durable context for every future session in this workspace.
If anything here is ambiguous, stop and ask. Do not guess.

---

<!-- SECTION:0a-programs -->
## 0a. programs/ — custom standalone software

The `programs/` folder at the repo root is where all custom standalone programs
are built and stored. These are tools that interface with or replace EvoERP
functionality, built using data learned from the LearnEVO research.

- Each program lives in its own subfolder: `programs/<program-name>/`
- Programs use **DSN=DBA** (Pervasive SQL ODBC) for database access
- Python + tkinter + reportlab is the default stack unless another is chosen
- `requirements.txt` must be kept current in each program folder
- Programs must **never write to** `C:\ISTS\` or `\\i2s109-solidcrm\` (read-only rule from §1 applies)
- Current programs:
  - `wo-schedule/` — Print Work Order Schedule (mirrors EVO WO-L-B / T7WOLB.DFM + T6WOLB2.RTM)

---

<!-- SECTION:0-broken-md -->
## 0. BROKEN.md — mandatory first read every session

**ALWAYS read `BROKEN.md` at the repo root before doing anything in this workspace.**

**New structure (2026-07-06):**
- `BROKEN.md` contains only short summaries, keywords, status, and a link for each issue.
- Full issue details live in individual files under `Issues/` (e.g., `Issues/B-007-dcy-body-decryption.md`).
- **Do NOT pre-read Issues/ files before work.** Only open an Issues/ file when a new task
  or action touches a similar problem — look up the relevant issue then.

Rules:
- Every bug or mistake encountered **must** be logged: create a new `Issues/` file immediately
  and add a one-line summary + link to `BROKEN.md`.
- Log in the Issues/ file: symptom, root cause, every attempt (worked or not), date, lesson.
- Newest entries go on top of BROKEN.md. When fixed, mark status ✅ FIXED in both places.
- **Never retry a fix already listed as "didn't work"** without explicit reasoning for why a
  different outcome is expected now.
- Before attempting any fix, check the relevant `BROKEN.md` entry. If a related Issues/ file
  exists, open it. If you are about to retry something already listed as failed, stop and
  pick a different approach — or ask.

---

<!-- SECTION:1-scope -->
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

<!-- SECTION:2-mission -->
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

<!-- SECTION:3-what-evo-is -->
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

<!-- SECTION:4-conventions -->
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
  - `Issues/` — individual issue detail files, one per BROKEN.md entry.
- **Docs style:** Markdown, short sentences, cite with
  `path\to\file.ext:offset` or line numbers. Mark status tags at the top
  of each doc: `Status: draft | verified | partial | open-questions`.
- **Never** claim something is "verified" unless I can point at the bytes
  or code lines that prove it.

---

<!-- SECTION:5-autonomy -->
## 5. Autonomy protocol

When a task completes:
1. Write/update the doc for what I just learned.
2. Update the index (`docs/README.md`) so the new doc is discoverable.
3. Open `research/OPEN_QUESTIONS.md`, pick the highest-value unknown, and
   start on it. **Stop and notify the user** if you hit: the scope boundary in §1,
   a genuine blocker (missing file, ambiguous requirement, unexpected system state),
   or any decision that requires user input. Do not push through blockers by guessing.
4. **Signal completion:** end the turn with **"FULL TASK COMPLETE"** followed by
   a one-paragraph summary of what changed and what is next.

---

<!-- SECTION:6-issue-tracking -->
## 6. Bug-fix and issue tracking (mandatory)

All bugs — both EvoERP production issues and learnevo-help tool bugs — are tracked
in **`KNOWN-ISSUES.md`** at the repo root. `BUGS.md` is deprecated and merged into
`KNOWN-ISSUES.md` (2026-07-06). Do not write to `BUGS.md`.

Create an Issues/ file for any bug that: (a) required more than one attempt to resolve,
(b) could plausibly recur in a future session, or (c) produced a non-obvious lesson.
Do not create Issues/ files for trivial single-attempt fixes caught immediately — log
those inline in the relevant doc with a one-sentence note at most.

For each qualifying issue:
- Create a new file under `Issues/` (e.g., `Issues/KI-006-ap-check-lock.md`).
- Add a one-line entry to `KNOWN-ISSUES.md` with ID, description, status, and link.
- In the Issues/ file: record symptom, root cause, every single attempt (worked or not),
  date, and a lesson.
- When fixed: mark ✅ FIXED in `KNOWN-ISSUES.md` and the Issues/ file; remove from
  BROKEN.md if duplicated there.
- Never repeat a fix that is already listed as "didn't work" for the same bug without
  explicit reasoning for why a different outcome is expected.

Before attempting any fix, read the relevant KNOWN-ISSUES.md entry and its Issues/ file.

---

<!-- SECTION:7-analyze -->
## 7. ANALYZE command

When the user types **ANALYZE** into the chat, execute the following loop immediately and autonomously — no further prompting needed:

1. **Read only the SECTION INDEX at the top of `EVO-DECOMPILE-TODO.md`** (first ~50 lines).
   Do NOT read the entire document. The index lists every section with line numbers,
   confidence ratings, and status. Identify items below C:90 or not yet started.

2. **Prioritize work in this order:**
   a. Untouched areas (⬜, no work done at all) — broadest coverage gain first
   b. Lowest-confidence started items (🔄 or ✅ with C: < 50) — biggest relative gains
   c. Items in the 50–74 range — push toward 75+
   d. Items in the 75–89 range — push toward 90+

3. **For each item worked:**
   - Grep for the section's anchor string (e.g., `SECTION:7-modules`) in
     `EVO-DECOMPILE-TODO.md`, Read around that location, and update only that section.
     Do NOT use line numbers — use anchors only.
   - Study the relevant EVO files (copy to `samples/` first if from a read-only path)
   - Document findings in the appropriate `docs/` file
   - Jump to the section in `EVO-DECOMPILE-TODO.md` and update only that section's
     confidence rating and checkbox; then update the line numbers in the top SECTION INDEX.
   - Update `docs/README.md` index if a new doc is created
   - Update `research/OPEN_QUESTIONS.md` if a question is answered or a new one surfaces

4. **Keep going** until blocked by encryption (§14 items requiring RWN decryption) or a
   genuine decision point. Do not stop between topics to ask.

5. **Session-end:** update the SECTION INDEX at the top of `EVO-DECOMPILE-TODO.md` with
   all updated confidence ratings and statuses, then end with **"FULL TASK COMPLETE"** and
   a one-paragraph summary of what changed.

---

<!-- SECTION:8-confidence -->
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

<!-- SECTION:9-deliverables -->
## 9. Final deliverable documents

Two master documents are maintained by the project. **Never read these directly** —
always spawn an Explore agent to get the information you need from them.

### 9.1 PROJECT-STRUCTURE.md

A single file at the workspace root that catalogs every path and file within the EvoERP
install and network share. To use it: spawn an Explore agent with a specific question
(e.g., "What tables does T7INA.RWN read?") and use the returned answer.

### 9.2 HELP-RESOURCES.md

A comprehensive, searchable knowledge base. To use it: spawn an Explore agent with a
specific lookup (e.g., "What is BKAP_CHK_INVNUM?") and use the returned answer.

Both documents must be kept updated after each documentation session. Do not let findings
sit un-recorded; update them per the tier rules in §13.7.

---

<!-- SECTION:10-decompilation -->
## 10. Decompilation work — current status

**At the start of every session, read `START-HERE-DOCUMENTATION-PROGRESS.md`.**
That document is the authoritative record of what is unblocked, what is blocked, the
current blocker, how to resolve it, and the highest-value next tasks.

Current state (as of 2026-07-06):
- **Cipher fully solved (2026-06-16):** Twofish-192-CFB; K_B=RWN, K_D=DCY; no IV file needed.
- **Unblocked:** `.RUN`, `.DFM`, `.RTM`, `.B` analysis; all documentation updates;
  module logic from forms+reports; per-table field docs.
- **Highest-value next work:** YN[N]↔ISTS.CFG mapping, K_A key purpose, RWN bytecode.
- Do NOT write stub or placeholder code for blocked tasks — it creates false progress.

---

<!-- SECTION:11-living-docs -->
## 11. Living documents — keep these current every session

The following documents must be updated whenever relevant findings are made. Use separate
agents to update these documents in parallel so the main context window stays clean.

| Document | What it tracks | Update trigger |
|----------|---------------|----------------|
| `KNOWN-ISSUES.md` | All EvoERP and learnevo-help bugs (merged from BUGS.md) | Any bug confirmed, workaround discovered, or issue fixed |
| `Issues/` folder | Individual issue detail files linked from KNOWN-ISSUES.md | New issue created or existing one updated |
| `BROKEN.md` | Index of all bugs/mistakes — short summaries + links to Issues/ | Any bug encountered or fix attempted |
| `START-HERE-DOCUMENTATION-PROGRESS.md` | Current blocker, what is/isn't unblocked, research snapshot | Any change to what is blocked or unblocked |
| `EVO-DECOMPILE-TODO.md` | Confidence ratings and checklist (update section index + target section only) | Any finding that changes a confidence rating |
| `EVO-HELP-TODO.md` | Help content progress (update section index + target section only) | Any help page added or completed |
| `research/OPEN_QUESTIONS.md` | Unresolved questions; answers when resolved | Any question answered or newly discovered |
| `PROJECT-STRUCTURE.md` | Catalog of every EvoERP file (update via agent) | Any new file discovered or relationship confirmed |
| `HELP-RESOURCES.md` | User-facing knowledge base (update via agent) | Any module, table, or workflow documented |
| `docs/02-file-formats/decryption-findings.md` | RWN/DCY cipher findings | Any cipher/key/IV finding |
| `docs/README.md` | Index of all docs in `docs/` | Any new doc created |

Rules:
- Update `EVO-DECOMPILE-TODO.md` and `EVO-HELP-TODO.md` by section only — jump to the
  relevant line range, update that section, then update the SECTION INDEX at the top.
  Never read or rewrite the entire document.
- Update PROJECT-STRUCTURE.md and HELP-RESOURCES.md per the tier rules in §13.7.
- Never let `BROKEN.md` fall behind — create the Issues/ file and add the index entry
  before moving on.

---

<!-- SECTION:12-launchers -->
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
- Log every launcher change in `KNOWN-ISSUES.md` under the bug that motivated it.

---

<!-- SECTION:13-new-rules -->
## 13. New operating rules (2026-07-06)

These rules supersede any conflicting older instructions above.

### 13.1 Issues/ folder — individual issue files

- `Issues/` lives at the repo root. One `.md` file per issue (bugs, mistakes, known issues).
- Naming convention: `Issues/<ID>-<short-slug>.md` (e.g., `Issues/B-007-dcy-decryption.md`).
- `BROKEN.md` and `KNOWN-ISSUES.md` are indexes — they contain only the one-line summary,
  keywords, status, and a markdown link to the Issues/ file.
- Issues/ files are **NOT** to be read before starting work. Only open one when a task
  touches a similar problem.

**BROKEN.md vs KNOWN-ISSUES.md — what goes where:**

- **BROKEN.md** is for post-mortems. Something broke, was diagnosed, and was resolved (or
  its cause fully understood). The lesson is recorded to prevent recurrence. Past-tense.
  *Analogy: we clogged the drain and turned on the faucet — the pipe burst. We repaired
  it and documented: never turn the faucet on when the drain is clogged.*
- **KNOWN-ISSUES.md** is for active unresolved issues. Something is wrong, it's been
  noticed, there may be a workaround, but it has not been fixed. Present-tense.
  *Analogy: the faucet leaks. It's annoying, we work around it, but it hasn't been fixed.*
- **Rule:** active/unresolved → KNOWN-ISSUES. Resolved with a lesson → BROKEN.
- An issue may start in KNOWN-ISSUES and move to BROKEN once resolved.

### 13.2 Section indexes for EVO-DECOMPILE-TODO.md and EVO-HELP-TODO.md

- Both TODO documents have a **SECTION INDEX** at the very top.
- The index lists: section number, grep anchor, heading, description, status/confidence.
- **Only read the SECTION INDEX** to decide what to work on — never read the whole document.
- Each section in the document body has a unique HTML anchor comment immediately before its
  heading, e.g. `<!-- SECTION:7-modules -->`. These never shift regardless of edits above.
- To navigate to a section: `Grep` for its anchor string (e.g., `SECTION:7-modules`), then
  `Read` around that line. Do NOT use line numbers — they drift as content is added.
- To update a section: Grep for its anchor, read/edit only that section, then update its
  status/confidence in the SECTION INDEX at the top. Never update line numbers.
- Mark a section ✅ COMPLETE in the SECTION INDEX once it reaches C:90+.
- When adding a new section to either TODO document, add an anchor comment in the format
  `<!-- SECTION:<N>-<short-slug> -->` immediately before the heading, and add a row to
  the SECTION INDEX.

### 13.3 Right tool for document lookups

Use the decision tree below — do not default to Explore agents for every large file.

| Situation | Tool |
|-----------|------|
| Know the exact symbol, field name, or string | `Grep` directly |
| Know the approximate section (anchor known) | `Grep` for anchor, then `Read` around it |
| Know approximate line range | `Read` with `offset`/`limit` |
| Open-ended question, location unknown, file >500 lines | Explore agent |
| Structural/summary question ("what's undocumented?") | Explore agent |
| PROJECT-STRUCTURE.md or HELP-RESOURCES.md (always large) | Explore agent — see §13.6 |

Explore agents are the right tool when **location is unknown and the question is open-ended**.
They are overkill when you know what you're looking for — use Grep or targeted Read instead.

### 13.4 Speed, accuracy, and token efficiency

- Prioritize speed and accuracy. Minimize context usage.
- If a problem is encountered that blocks progress, **stop immediately**, notify the user
  with a clear description of the issue, and wait for instructions. Do not try to work
  around blockers without direction.
- Do not read large files speculatively. Only read what is needed for the current task.

### 13.5 Task completion signal

- When a full task is completed, end the response with **"FULL TASK COMPLETE"** followed
  by a 1–2 sentence summary of what changed and what is next.
- After a very long ANALYZE loop, perform a `/compact` or pause and summarize before
  continuing.

### 13.6 Never read PROJECT-STRUCTURE.md or HELP-RESOURCES.md directly

- Always spawn an Explore agent with a specific question.
- Return the agent's answer to the user or use it in your work.
- Do not open these files yourself under any circumstances.

### 13.7 Live document update — tiered by change size

Choose the method based on the size of the change, not the size of the document:

| Change size | Method |
|-------------|--------|
| One row, one confidence rating, one status flag | `Edit` directly — no full read needed |
| One section updated or reorganized | `Read` the section (offset/limit or Grep anchor), then `Edit` |
| Large structural change (merge, reorganize, 10+ entries) | Agent |
| Any change to PROJECT-STRUCTURE.md or HELP-RESOURCES.md | Always agent (§13.6) |

The `Edit` tool is surgical — it replaces a specific string without reading the whole file.
Use it for small targeted changes. Reserve agents for changes that require understanding the
document's current state before writing.

Keep KNOWN-ISSUES.md clean: when an issue is fully resolved and has no further diagnostic
value, move its Issues/ file to `Issues/archive/` and remove it from the active list.
