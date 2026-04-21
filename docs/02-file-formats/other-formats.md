# Other EvoERP File Formats

Status: verified by direct inspection of sample files.

## `.IMP` — Import definition (plaintext)

Source: `../../samples/imp/BKDEB.IMP`. Fixed-width plaintext, one
import definition per line. Sample first line of `BKDEB.IMP`:

```
U:\PROFPN.CSV                           SC
```

Column 1 = source filename (fixed-width field). Column 2 = mode
(`SC` = Source Copy / Standard Conversion? *to confirm*).

The `BKDE` family of IMP files (BKDEB..BKDEH, BKDES) are pre-canned
"Dealer / Data Entry" import templates. `BKPIPHYS.IMP` imports physical
inventory counts. `ISWCD.IMP` imports work-center definitions.

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

## `.XPT` — Export layout (plaintext, fixed-width)

Source: `../../samples/xpt/BKAPEVND.XPT`. Format:

```
<output.TXT>  <flag>   <FIELD1>   <FIELD2>   ...   <FIELDN>
```

Sample first line of `BKAPEVND.XPT`:

```
BKAPEVND.TXT  T  BKAP.CLASS   BKAP.VENDCODE   BKAP.VENDNAME   ...
```

The first token is the destination file (a `.TXT` under the same
directory). The second token appears to be a type/mode flag (`T` =
Tabular?). The rest is a space-padded list of TAS-style field names
(dotted notation) to emit as columns.

The `.XPT` family (20 files) covers most of the BKAP/BKAR/BKSO tables
— these are **canned CSV-style exports** that the user can invoke from
the menu.

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
