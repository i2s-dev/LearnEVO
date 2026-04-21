# CLAUDE.md — LearnEVO Playground

Rules and durable context for every future session in this workspace.
If anything here is ambiguous, stop and ask. Do not guess.

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

## 7. Launcher scripts (.bat / .ps1) — keep them current

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
