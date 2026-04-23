# Evo-ERP Tools (Tools menu)

Status: verified (text is a near-verbatim rendering of the vendor's
help file, extracted via [scripts/chm_to_md.py](../../scripts/chm_to_md.py)).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../samples/chm/extracted/).

The **Tools** dropdown on the Evo-ERP main menu surfaces four utility
programs. This doc consolidates the CHM's four topic pages under the
"Evo-ERP Tools" category. Only one of these — **Evo Notes Search** —
has a dedicated DFM form ([EvoNoteSearch.DFM](../../samples/dfm_parsed/dfm_summary.csv) row 75);
the others are inline menu handlers inside the main menu runtime.

---

## 1. Users Tool

*Source: [users_tool.htm](../../samples/chm/extracted/users_tool.htm) ·
Invocation: **Tools → Users***

**Purpose.** View who is currently logged in and what program each
user is in. Only the `ADMIN` user can Enable / Disable / force-logout
other users.

**Operation.** Opens a list of users with:
- Company they are logged into.
- Program they are currently in.

> **Caveat from the vendor:** "Not all programs yet have the feature
> enabled" — so some Evo users may show as on the menu when actually
> inside a program, and Classic (TAS Pro 6) users may not appear at
> all.

**Buttons:**

| Button | Effect |
|---|---|
| **Enable Logins** | Re-enables login for DBA Classic and Evo-ERP after a prior Disable. |
| **Disable Logins** | Blocks DBA Classic logins entirely; blocks all Evo-ERP logins *except* `ADMIN`. Stays disabled until `ADMIN` re-enables. |
| **Logout Users** | Checks for DBA Classic users (warns if present) and closes the Evo-ERP main menu for all users — each user is kicked out when their current program exits. Also disables logins as a side effect. |
| **Clear User** | Removes a user from the Login Display file only. Does **not** actually log the user out. If the user is still live, the entry reappears within ~10 seconds after reopening the Users screen. Use for clearing hung records. |

> **Login Display file** = `ISLOG` ("Active user list") per
> [file-names-index.md · System Manager](../04-data-dictionary/file-names-index.md#system-manager).
> "Clear User" deletes a row from `ISLOG` but doesn't kill the
> underlying session.

---

## 2. Size Tool

*Source: [size_tool.htm](../../samples/chm/extracted/size_tool.htm) ·
Invocation: **Tools → (size choice)***

**Purpose.** Control the Evo-ERP main-menu window size — from
**Toolbar-only** up through **Maximized**.

**Operation.** Pick the desired size from the Tools menu. The choice
is remembered per user for the next login.

> One of the rare Evo-ERP settings that is stored per user, not per
> company — likely written into the per-workstation `.INI` under
> `C:\ISTS\` (the per-user runtime dir per [CLAUDE.md §1](../../CLAUDE.md)).

---

## 3. Google Calendar

*Source: [google_calendar.htm](../../samples/chm/extracted/google_calendar.htm) ·
Invocation: **Tools → Google Calendar***

**Purpose.** Open the Google Internet Calendar from inside Evo-ERP.

**Operation.** If the user has no Google Calendar account, there's a
registration option. Once registered, the user can share calendars
and appointments with others — including the **IS Tech Support
Calendar**, which the vendor uses to publish scheduled updates,
training classes, and other events.

> This is effectively a browser-launch shortcut to
> `calendar.google.com`. No local state; nothing to back up or
> migrate. The value-add is the shared **IS Tech Support Calendar**
> feed.

---

## 4. Evo Notes Search

*Source: [evo_notes_search.htm](../../samples/chm/extracted/evo_notes_search.htm) ·
Form: [EvoNoteSearch.DFM](../../samples/dfm_parsed/dfm_summary.csv) ·
Invocation: **Tools → Note Search***

**Purpose.** Search the **entire Evo Notes database** for any
substring of text inside a note.

**Operation.** Enter the substring, choose:
- **Case-sensitive?** yes/no.
- **Scope** — Active, Archived, or Both.

> **Performance warning from the vendor:** "Since this is not an
> indexed search, depending on the size of your Notes database, it
> may be slow."

**Backing store.** Notes live in the `ISNOTES` table (with `ISNTYPE`
for note-type codes) per [file-names-index.md · System Manager](../04-data-dictionary/file-names-index.md#system-manager).
Archive counterpart isn't in the canonical file-names list — the
Active/Archived toggle presumably scans both without a separate
archive table, or a downstream archive file was added post-2024.1.
**Open question** — worth checking `EvoNoteSearch.DFM` for the actual
table references. Recorded in
[research/OPEN_QUESTIONS.md](../../research/OPEN_QUESTIONS.md) if a
slot exists.

---

## Cross-references

- Login / active-user plumbing — Users Tool reads/writes `ISLOG`. For
  the rest of the System Manager schema see
  [file-names-index.md · System Manager](../04-data-dictionary/file-names-index.md#system-manager).
- Main menu startup (which hosts the Tools dropdown) —
  [07-runtime-boot/boot-sequence.md](../07-runtime-boot/boot-sequence.md).
- Notes system (read by Evo Notes Search) — no dedicated doc yet;
  candidate for the next pass.

## Quirks worth noting

- **Two of the four topics have verbatim typos** in the CHM source:
  - *Evo Notes Search*: "search **teh** entire Evo Notes database".
  - *Users Tool*: "clears a user from the Login Display file (as in
    the case of a hung entry." — unmatched opening parenthesis.
- **Google Calendar topic shows character-encoding damage** in the
  source: `Tools ?Google Calendar` where the `?` was originally a
  dash/arrow. The CHM uses ISO-8859-1 but some upstream paste
  dropped the character.
- These are vendor-side issues preserved for fidelity; not something
  we need to fix in the help, just to be aware of when searching.
