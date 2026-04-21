# EvoERP Boot Sequence

Status: draft — traces based on `taspro7.ini`, `EvoSettings.INI`, and
filenames; has not yet been confirmed by dynamic tracing.

## The chain, in order

1. **Shortcut**: `C:\ISTS\EvoERP.lnk` (size 1,470 B). Invokes
   `C:\ISTS\StartEvo.exe` with the working directory set to `C:\ISTS`.

2. **Launcher**: `C:\ISTS\StartEvo.exe` (37,216 B, Oct 2024). Its role
   — based on the surrounding file set — is likely:
   - Check that `tp7runtime.exe` exists and is not already running for
     this user (the `EvoSched.RWN` and `EvoService*.RWN` present on
     the share suggest there's a service-tier mode too).
   - Read `C:\ISTS\taspro7.ini` for the default run-program path.
   - Launch `tp7runtime.exe` (or the identical-size `evoerp.exe`)
     passing the target `.rwn`.
   - Confirming the exact argv form is a **todo** — open question.

3. **Runtime**: `C:\ISTS\tp7runtime.exe` (33.3 MB, Jul 2023). This is
   the TAS Professional 7 runtime engine. Reads its config from
   `C:\ISTS\taspro7.ini`:
   ```
   [Setup]
   DataDictPath=\\I2S109-SOLIDCRM\DBAMFG$\
   DfltRunPrg=\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn
   MultiUser=1
   DefaultPath=\\I2S109-SOLIDCRM\DBAMFG$\
   Titlebar=Evo ~ ERP
   HelpFileName=\\I2S109-SOLIDCRM\DBAMFG$\EvoHELP.CHM
   ```
   Loads:
   - `qtintf70.dll` — Qt 3 / Borland CLX UI support (shipped in `C:\ISTS`).
   - `c4dll.dll` — CodeBase 4 (xBase/DBF) engine for ancillary files.
   - `suwin6.dcy` / `suwin7.dcy` — local dictionary caches used before
     the network is reachable (both shipped in `C:\ISTS`).
   - `suwin6t.rwn` / `suwin7.rwn` — tiny bootstrap RWNs.

4. **Main menu program**: `\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn`
   (497,383 B). Renders:
   - The logo/splash (`EVOLOGO.DCY` → `ISSPLASH.DCY`?).
   - Login screen (`EVOMENU_LOGIN.DCY`, `EvoDC_LOGIN.DCY`,
     `DBAMENU_LOGIN.DCY`).
   - Company selection (`EVOMENU_SELCOMP.DCY`).
   - The hierarchical main menu (`EVOERPMENU.DCY` pairs with it).

5. **Per-module dispatch**: Menu choices run further `.RWN` files —
   e.g. picking "Inventory → Item Master" likely runs
   `T7INA.RWN` with `C:\ISTS\DFM\T7INA.DFM` as its form layout.

## Per-machine state files

| File in `C:\ISTS\`       | Role (inferred) |
| ------------------------ | --------------- |
| `taspro7.ini`            | Runtime config — paths, fonts, colors, license serial (`[Misc] Serial=670538`). |
| `EvoSettings.INI`        | Per-machine module access toggles (e.g. `[ARA] SAVE ACCESS=1`). |
| `WHOAMI.DBA`             | 35-byte user/terminal identity. Likely used for multi-user lock keys. |
| `CHMHELP.EVO`            | 35-byte marker — purpose unknown. |
| `RBuilder.ini`           | ReportBuilder designer preferences. |
| `DFM\`                   | Local cache of large T7 DFMs for fast load. |
| `PDFS\`                  | Local output directory for generated PDFs. |

## Questions I need to answer next

1. Does `StartEvo.exe` do anything besides spawn `tp7runtime.exe`?
   (Strings analysis of the exe would tell me.)
2. What is the exact command line passed to `tp7runtime.exe`?
3. Does the runtime pre-load `suwin6.dcy` before any network I/O? If so,
   it might contain a baseline data-dictionary map we can parse.
4. How does login + company selection map to the Btrieve/DBF files on
   the share? (Need to find `EVOUSERS` records.)
