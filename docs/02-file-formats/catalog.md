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
| `.B`   | 19    | Btrieve data file (record store)  | No (binary index+data) | *todo* |
| `.UPD` | 9     | Update/patch manifest             | ?         | *open-question* |
| `.HTM` | 9     | Static HTML (help / generated)    | Yes       | n/a |
| `.dll` | 9     | Windows DLLs (`c4dll`, `qtintf70`, etc.) | n/a | *todo* |
| `.SRC` | 7     | **TAS Pro 4GL source** (partial — most sources are off-server) | **Yes (plaintext)** | [src-tas-pro-language.md](src-tas-pro-language.md) |
| `.IMP` | 11    | Import definition                 | ?         | *open-question* |
| `.mdx` | 10    | Btrieve multi-index companion     | No (binary) | *todo* |
| `.lnk` | 10    | Windows shortcuts                 | n/a       | n/a |
| `.ico` | 10    | Icons                             | n/a       | n/a |
| `.csv` | 11    | CSV exports/imports               | Yes       | n/a |

### Local-only files (`C:\ISTS\`)

| File               | Role |
| ------------------ | ---- |
| `StartEvo.exe`     | Launcher — spawns TP7 runtime against network menu. |
| `evoerp.exe` / `tp7runtime.exe` | TAS Pro 7 runtime engine (identical size; `evoerp.exe` is a renamed copy). |
| `RBDsgnr.exe`      | Nevrona ReportBuilder designer (edits `.RTM` files). |
| `EvoPVT.jar`       | Java helper — purpose not yet investigated (*open-question*). |
| `PV.EXE`           | 2005 TAS PostView / print viewer (*todo*). |
| `c4dll.dll`        | **CodeBase 4** DBF engine DLL (xBase/dBase compat layer). |
| `qtintf70.dll`     | Qt 3 interface DLL — supports legacy UI widgets. |
| `quricol32.dll`    | QR code rendering (for barcode/QR-enabled forms). |
| `zipdll.dll` / `unzdll.dll` | ZIP compression — used by backup/update flows. |
| `taspro7.ini`      | TAS Pro 7 configuration (paths, colors, fonts). |
| `EvoSettings.INI`  | Per-machine app settings (AR/AP access flags). |
| `WHOAMI.DBA`       | Per-machine identity (35 bytes — user/terminal tag). *open-question* |
| `CHMHELP.EVO`      | 35-byte marker — purpose unknown. *open-question* |
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
