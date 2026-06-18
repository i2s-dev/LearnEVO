# EvoERP Boot Sequence

Status: partial — StartEvo.exe fully confirmed (Pass 105); runtime config verified; some
post-login steps still inferred from file names.

## The chain, in order

1. **Shortcut**: `C:\ISTS\EvoERP.lnk` (size 1,470 B). Invokes
   `C:\ISTS\StartEvo.exe` with the working directory set to `C:\ISTS`.

2. **Launcher**: `C:\ISTS\StartEvo.exe` (37,216 B, Oct 2024). **Confirmed** (Pass 105):
   a .NET assembly with three confirmed steps:
   - **DomainAuthenticate** — validates the Windows domain user before proceeding.
   - **KillEvoProcesses** — terminates any stale EvoERP processes from previous sessions
     (prevents zombie `evoerp.exe` instances from locking Btrieve files).
   - **LaunchEvoWithUser** — launches `evoerp.exe` under the authenticated user context.
   Also confirmed: registers the `evo://` URI scheme for deep-link launching;
   connects to Pervasive PSQL via DSN `EVOADMIN`; runs
   `SELECT count(*) FROM tas_menus` as the **license gate** before launching
   (if 0 rows → abort, EvoERP not licensed for this database).

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
| `CHMHELP.EVO`            | **Sentinel flag file** — 35-byte text file containing "EvoHELP now set for this computer\r\n". Written when EvoHELP CHM help is first configured on a workstation; presence signals setup is complete. |
| `RBuilder.ini`           | ReportBuilder designer preferences. |
| `DFM\`                   | Local cache of large T7 DFMs for fast load. |
| `PDFS\`                  | Local output directory for generated PDFs. |

## Open questions (Pass 106l)

- **Exact command line to `evoerp.exe`** — StartEvo.exe's `LaunchEvoWithUser` step
  passes some argv to `evoerp.exe`. Likely includes the target `.rwn` path and possibly
  user credentials. Not yet confirmed from dynamic trace.
- **suwin6.dcy pre-load** — does the runtime load `suwin6.dcy` before any network I/O?
  That file ships locally in `C:\ISTS` and may be a baseline data-dictionary cache.
- **Login → Btrieve mapping** — how company selection sets the per-company Btrieve
  file suffix (`.BI2`, `.BAT`, etc.). Likely via `EVOMENU_SELCOMP.DCY` setting a
  global company code variable that FILELOC picks up.

**Resolved (Pass 105 + 106l):**
- StartEvo.exe role: DomainAuthenticate → KillEvoProcesses → LaunchEvoWithUser ✅
- License gate: `SELECT count(*) FROM tas_menus` via DSN EVOADMIN ✅
- `evo://` URI scheme registration ✅
- `CHMHELP.EVO` = CHM setup sentinel flag ✅
