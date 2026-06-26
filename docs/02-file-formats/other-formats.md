# Other EvoERP File Formats

Status: verified by direct inspection of sample files.

## `.IMP` — Import definition (**binary, 442 bytes**)

**CORRECTION (Pass 325 2026-06-26):** Not plaintext — fixed-size binary.

Full format: 40-byte source filename (space-padded) + 2-byte mode code (`SC`/`DC`/`RC`/`RIC`)
+ 100 × uint16 LE import column map + 100 × uint16 LE export column map (entry 100 = 0x0A0D
CRLF sentinel). Empty files (0 bytes) = no import configured.

Mode codes: `SC`=Standard CSV, `DC`=Delimited CSV, `RC`=Btrieve raw copy.

The `BKDE` family (BKDEB..BKDEH, BKDES) are pre-canned "Dealer / Data Entry" import templates.
`BKPIPHYS.IMP` imports physical inventory counts. `ISWCD.IMP` imports work-center definitions.

→ Full format documentation: [imp-xpt-import-export.md](imp-xpt-import-export.md)

## `.UPD` — Pervasive DDF update manifest (binary Btrieve)

Source: `../../samples/upd/FILEDEF.UPD`. Starts with `FC` magic (same
as the DDFs) — it's a Btrieve file.

There are exactly nine of these on the share, all named `FILE*.UPD`:
`FILEDEF`, `FILEDES`, `FILEDFLD`, `FILEDICT`, `FILEKEY`, `FILEKNUM`,
`FILELOC`, `FILEREL`, `FILES`. These mirror the nine Pervasive system
catalog tables (`FILE.DDF`, `FIELD.DDF`, `INDEX.DDF`, `ATTRIB.DDF`,
`OCCURS.DDF`, `RELATE.DDF`, `VIEW.DDF`, `TRIGGER.DDF`, `PROC.DDF`).

Working hypothesis: when an EVO update arrives, it ships a set of
`FILE*.UPD` snapshots of the *new* DDF state. The runtime reads these
and applies a schema migration against the live DDFs. (Hence the TAS
runtime keywords `RESTRUCTURE_DBF`, `PACK_DBF`, `REINDEX_DBF`.)

## `.XPT` — Export layout (**binary, 32000 bytes fixed**)

**CORRECTION (Pass 325 2026-06-26):** Not plaintext — fixed-size binary block.

Full format: 12-byte target filename (space-padded) + 1-byte type flag (`S`=Standard,
`T`=Tabular, `F`=Full/Formatted, `D`=Detail, ` `=Default) + N × 15-byte column accessor
names (space-padded ASCII) terminated by a 15-zero slot + spaces to fill 32000 bytes.

The `.XPT` family covers BKAP/BKAR/BKIC/BKSO/INVTXN/WORKORD/BKBMMSTR tables —
canned CSV-style exports invokable from the DE menu. INVTXN.XPT confirms 25 `MTIT.*`
INVTXN field accessors. BKAPPOL.XPT lists 39 `BKAP.POL.*` fields.

→ Full format documentation: [imp-xpt-import-export.md](imp-xpt-import-export.md)

## `.btm` — Backup RTM (same as RTM)

Source: `../../samples/btm/I2SCHK1.btm`. Identical TPF0 binary format
to `.RTM`. The `.btm` extension is a convention for "backup"/prior
revision; 60 of these on the share. See
[rtm-reportbuilder.md](rtm-reportbuilder.md) for the format.

## `.B<code>` — Btrieve data file per company

Example: `\\I2S109-SOLIDCRM\DBAMFG$\22\BKARCUST.B22`.
Standard Pervasive MKDE file — FC magic, paged, B-tree indexed.
The suffix (`.B` for Default, `.B22`, `.BAB`, `.BI2`, etc.) carries the
company code. See the [data-dictionary overview](../04-data-dictionary/overview.md).

Companion files:
- `.mdx`  — multi-index helper (10 files on the share)
- `.XLB`  — extended lock / owner file (paired with many `.B`)
- `.BI2`  — appears to be an overflow / split file for company `I2`

## `.TXT` — exported report / data (ASCII)

4,088 on the share. These are the output of the XPT exports and the
legacy report spools. Each is a flat fixed-width or CSV dump — the
companion `.XPT` describes the layout.

## `.log` — runtime / update log

74 of them. Plain text. Runtime-append logs from update / conversion
events.

## `.CHM` — Windows HTML Help (EvoHELP.CHM)

`\\I2S109-SOLIDCRM\DBAMFG$\EvoHELP.CHM` — standard Microsoft
compiled-HTML help file. Opens with `hh.exe` on any Windows machine.
Mentioned in `taspro7.ini` under `HelpFileName=`.

## `.dfm` (binary variant)

A small number of DFMs on the share are actual **binary** Delphi form
streams (same TPF0 magic as RTMs). Our text parser silently fails on
those (25 cases, listed in `../../samples/dfm_parsed/errors.txt`).
All 25 happen to be **zero-byte placeholders** on this installation,
so they contain no layout data regardless of format — see
[docs/03-modules/dfm-form-inventory.md](../03-modules/dfm-form-inventory.md)
for the catalog.

## `.DBA` — identity token

`C:\ISTS\WHOAMI.DBA` — 35 bytes. Binary blob used by the runtime as a
per-workstation identity (read by the TAS `WHOAMI` function). Format
not yet decoded; likely a license-bound seat token.

## `.EVO`

`C:\ISTS\CHMHELP.EVO` — 35 bytes. Purpose unknown; size matches
`WHOAMI.DBA`, so possibly a similar marker. Looks like a counterpart
to the `.CHM` help file (maybe a "CHM help present"/"help cached" tag).
*Still an open question.*
