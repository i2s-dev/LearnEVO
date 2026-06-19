# EvoERP File Format Catalog

Status: draft (expanding). Counts are from the `\\I2S109-SOLIDCRM\DBAMFG$\`
network share as of 2026-04-17.

This is the master index of every file extension observed in the EvoERP
installation. For any extension, see its own `.md` if one exists;
otherwise the row here is the current best summary.

| Ext   | Count  | Type                              | Readable? | Doc |
| ----- | ------ | --------------------------------- | --------- | --- |
| `.TXT` | 4088  | Exported reports / data dumps     | Yes (ASCII) | *todo* |
| `.RUN` | 1265  | TAS Pro **6** compiled program    | No (binary) | *todo* |
| `.DFM` | 1120+ | **Delphi form** (UI layout)       | **Yes (plaintext)** | [dfm-delphi-forms.md](dfm-delphi-forms.md) |
| `.RWN` | 1115+ | TAS Pro **7** compiled program    | No (encrypted/compressed) | [dcy-rwn-binaries.md](dcy-rwn-binaries.md) |
| `.RTM` | 899+  | Nevrona **ReportBuilder** template| No (binary) | *todo* |
| `.pdf` | ~700  | Generated reports / documents     | Yes (PDF) | n/a |
| `.tmp` | 270   | Temporary files                   | n/a       | n/a |
| `.XLS` | 195   | Excel exports                     | Yes       | n/a |
| `.log` | 74    | Runtime / update logs             | Yes       | *todo* |
| `.btm` | 60    | Unknown — candidate: batch/temp   | ?         | *open-question* |
| `.DCY` | 41    | **Data dictionary** definition    | No (encrypted) | [dcy-rwn-binaries.md](dcy-rwn-binaries.md) |
| `.jar` | 37    | Java archive (e.g. `EvoPVT.jar`)  | n/a       | *todo* |
| `.exe` | 50    | Windows executables               | n/a       | *todo* |
| `.XPT` | 20    | Unknown — candidate: SAS export?  | ?         | *open-question* |
| `.B`   | 659   | Btrieve PSQL data file (record store) | No (binary B-tree) | [btrieve-b-format.md](btrieve-b-format.md) |
| `.UPD` | 9     | Update/patch manifest             | ?         | *open-question* |
| `.HTM` | 9     | Static HTML (help / generated)    | Yes       | n/a |
| `.dll` | 9     | Windows DLLs (`c4dll`, `qtintf70`, etc.) | n/a | *todo* |
| `.SRC` | 7     | **TAS Pro 4GL source** (partial — most sources are off-server) | **Yes (plaintext)** | [src-tas-pro-language.md](src-tas-pro-language.md) |
| `.IMP` | 11    | Import definition                 | ?         | *open-question* |
| `.mdx` | 10    | Btrieve multi-index companion     | No (binary) | [btrieve-b-format.md](btrieve-b-format.md) |
| `.lnk` | 10    | Windows shortcuts                 | n/a       | n/a |
| `.ico` | 10    | Icons                             | n/a       | n/a |
| `.csv` | 11    | CSV exports/imports               | Yes       | n/a |

### Menu system files (xBase / CodeBase format)

| File | Format | Purpose |
|------|--------|---------|
| `BKMENUSU.DBF` | xBase/dBASE DBF | **Menu tree master** — GROUPS/BUTTONS/items; read by `c4dll.dll` |
| `BKMENUSU.CLX` | Clipper index | Index file for BKMENUSU.DBF |
| `BKMENUSU.DBT` | Memo file | Memo fields for BKMENUSU.DBF |
| `BKMENUSU.MDX` | Multi-index | Additional index for BKMENUSU.DBF |
| `BKMENUSU.TXT` | CSV text export | Human-readable dump of full menu tree (870 lines) |
| `BKMENUST.TXT` | CSV text export | Setup Wizard menu only (109 lines) |
| `BKMENUSTC.TXT` | CSV text export | Setup Wizard (company copy) |
| `BKMENUSTR.TXT` | CSV text export | Setup Wizard (reset copy) |

These are accessed by the CodeBase 4 engine (`c4dll.dll` in `C:\ISTS\`), not by
Pervasive/Btrieve. `StartEvo.exe` accesses them via DSN `EVOADMIN` as `tas_menus`.

### Local-only files (`C:\ISTS\`)

| File               | Role |
| ------------------ | ---- |
| `StartEvo.exe`     | Launcher — spawns TP7 runtime against network menu. |
| `evoerp.exe` / `tp7runtime.exe` | **Tas Premier 7i runtime v7.1.9.1** by Addsum Business Software (2004-2014). 31.8 MB x86 PE32. `evoerp.exe` is a renamed copy. |
| `RBDsgnr.exe`      | Nevrona ReportBuilder designer (edits `.RTM` files). |
| `EvoPVT.jar`       | Java helper — purpose not yet investigated (*open-question*). |
| `PV.EXE`           | 2005 TAS PostView / print viewer (*todo*). |
| `c4dll.dll`        | **CodeBase v1.0.0.1** by Sequiter Software Inc. — reads BKMENUSU.DBF + CDX indexes (dBASE/FoxPro engine). |
| `qtintf70.dll`     | **Borland Delphi-Qt2.x Interface Library v7.0.4.258** — CLX/Qt UI bridge enabling Delphi VCL on Qt 2.x. |
| `quricol32.dll`    | **Quricol QR Barcode Library** by Serhiy Perevoznyk — QR barcode generation for shipping labels and forms. |
| `zipdll.dll` / `unzdll.dll` | ZIP compression — used by backup/update flows. |
| `taspro7.ini`      | TAS Pro 7 configuration (paths, colors, fonts). |
| `EvoSettings.INI`  | Per-machine app settings (AR/AP access flags). |
| `WHOAMI.DBA`       | Per-machine identity file — stub (2 bytes CRLF) on this workstation; byte layout unknown. *open-question* |
| `CHMHELP.EVO`      | **Decoded (2026-06-19):** plaintext "EvoHELP now set for this computer.\r\n" (35 bytes). Presence marker written when EvoHELP.CHM is installed; tp7runtime.exe checks this before enabling F1 help. |
| `DFM\`             | Local cache of the large T7 form files (`T7ARA`, `T7INA`, etc.) so they load fast. |
| `PDFS\`            | Local PDF staging directory. |

## Parallel generations

EvoERP contains **three code generations** intermixed:
1. **TAS Pro 3 → 5 era** — `BK*.SRC` (old source, see `BKAWLB.SRC`:2 comment
   "Cvtd from TAS-Pro 3.0 edt to 5.0 src on 01/18/96"). Still compiled and used.
2. **TAS Pro 6 era** — `.RUN` modules, pre-Windows-native UI.
3. **TAS Pro 7 era (current)** — `.RWN` modules with `.DFM` forms. Prefix `T7*`.

Many `T6*.RUN` files and `T7*.RWN` files exist **side by side**, sometimes for
the same functional area (e.g. `T6SOB4.RTM` vs. `T7SOA.DFM`). Treat these as
legacy-vs-current when documenting modules.

## Source paths from `taspro7.ini` (history)

The TAS Pro IDE on a developer machine once referenced:
- `F:\Projects\TAS\istech\` — the primary source tree (not present locally).
- `F:\Projects\TAS\MyProgram\` — scratch project.
- `C:\TASPRO7\DBA7\` — legacy install path.
- `C:\ISTECH` — referenced as library (`Lib Directory=C:\ISTECH`).

These paths confirm that **`\\i2s109-solidcrm\DBAMFG$\` is a deployment
directory**, not a source directory. The plaintext `.SRC` files living there
(BKAWLB, BKDCA, BKLME, BKMRF, BKROA, Bkaph, Bkapha) are either intentionally
deployed or leftovers — **open question** why only these seven.
