# Local EVO Instance Feasibility Research

Status: active research  
Date: 2026-06-24  
Goal: Determine whether all EVO files can be copied locally and EVO run against the local copy instead of the network share, for safe offline testing.

---

## Summary Verdict

**Feasible.** All four original blockers are either resolved or downgraded. A local snapshot instance of EVO is achievable with the Workgroup Pervasive engine already installed on this machine and three line-changes to `taspro7.ini`.

---

## The Three Config Lines That Control Everything

File: `C:\ISTS\taspro7.ini` — `[Setup]` section

```ini
DataDictPath=\\I2S109-SOLIDCRM\DBAMFG$\    ← Pervasive DDF location + data root
DfltRunPrg=\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn  ← main menu program
DefaultPath=\\I2S109-SOLIDCRM\DBAMFG$\     ← base for all program chaining
```

Changing all three to a local folder (e.g. `C:\EVOLocal\`) redirects the entire TAS Pro session to local files.

---

## Blocker Analysis

### Blocker 1 — Startup path (RESOLVED: Confidence 92/100)

`taspro7.ini` is a plain-text INI file we can edit freely. Three values cover the full redirect:
- `DataDictPath` — where TAS Pro looks for Btrieve DDF schema files
- `DfltRunPrg` — the .RWN to run at launch
- `DefaultPath` — the base path for all bare-name program references

**Evidence:** All three are present, readable, and point to the network share. No other config files in `C:\ISTS\` control data paths.

---

### Blocker 2 — Hardcoded paths in .RWN programs (LARGELY RESOLVED: Confidence 72/100)

Two mechanisms control how TAS Pro programs reference files:

**Data files** — SRC source files show bare logical names:
```
open BKSYMSTR lock R
open WORKORD lock N
open BKICMSTR lock N
```
These are resolved by TAS Pro against `DataDictPath`. No absolute paths in any of the 6 SRC files examined.

**Other programs (chaining)** — SRC files use the pattern:
```
chain bksy.prgs.whr * "BKAPG"
```
`BKSY_PRGS_WHR` in BKSYMSTR is **blank** (confirmed via live query). So this resolves to `"" * "BKAPG"` = `"BKAPG"` — a bare name that TAS Pro resolves against `DefaultPath`. All program chaining goes through `DefaultPath`.

**Remaining risk (the 28%):** The compiled .RWN bytecode is encrypted (Twofish-CFB). A minority of programs may contain hardcoded absolute UNC paths for edge cases (e.g. calling external tools, referencing specific RTM/DFM files by absolute path). We cannot verify without decryption. The most visible cases — RTM Template.FileName values — are binary-patchable (see Blocker 6).

---

### Blocker 3 — Dead snapshot is acceptable (NON-ISSUE)

User confirmed: a frozen copy of the data is the goal. No sync requirement.

---

### Blocker 4 — Local Pervasive engine (RESOLVED: Confidence 85/100)

**No server service is running locally** — confirmed, no Pervasive services found.

**BUT `w3dbsmgr.exe` is installed in two locations:**
- `C:\Program Files (x86)\Actian\PSQL\bin\w3dbsmgr.exe`
- `C:\Program Files (x86)\Pervasive Software\PSQL\bin\w3dbsmgr.exe`

`w3dbsmgr.exe` is the **Pervasive Workgroup Engine** (also called the MicroKernel Database Engine in workstation mode). It can open .B files directly on the local disk without a network Pervasive server. This is exactly what's needed for a local snapshot.

**Remaining risk (the 15%):** The Workgroup Engine license may restrict the number of sessions or may require activation against the local machine. Untested. Also: the 32-bit Pervasive v11 install vs the 64-bit Actian v12 client — the TAS Pro 7 runtime is likely 32-bit, so the v11 32-bit engine is the right one.

Also installed: `butil.exe`, `builder.exe`, `pvddl.exe` — useful tools for verifying the local DDF/data setup.

---

### Blocker 5 — DDF paths after copy (CONFIDENCE 85/100)

Pervasive DDF files (`FILE.DDF`, `FIELD.DDF`, `INDEX.DDF`) define the logical table schema. Standard Pervasive practice is to store file paths **relative to the DDF location**. If that's the case here, copying the DDF files and .B files together into one local folder gives a self-contained database — no path edits needed.

The `DataDictPath` in `taspro7.ini` tells TAS Pro (and the Pervasive requestor) where to find the DDF files. Pointing it at the local copy folder is the only change needed.

**Remaining risk:** If any DDF entries use absolute UNC paths, they'll need updating. This can be done with `pvddl.exe` or direct Btrieve editing. Not yet verified.

---

### Blocker 6 — Binary patching RTM files (CONFIDENCE 88/100)

RTM files (Delphi TPF0 binary DFM format) store `Template.FileName` and child report paths as length-prefixed strings. Both T6WOLB1.RTM and T6WOLA1.RTM have dead paths from old server installs. These are directly patchable — find the byte sequence, update the length byte, replace the string, shift remaining bytes.

Known broken paths:

| File | Bad path | Correct path |
|------|----------|--------------|
| T6WOLB1.RTM | `\\I2s44-hapi\dbamfg$\T6WOLB1.RTM` | `\\i2s109-solidcrm\DBAMFG$\T6WOLB1.RTM` |
| T6WOLB1.RTM | `C:\DBAMFG\BKISWCE1.RTM` | `\\i2s109-solidcrm\DBAMFG$\BKISWCE1.RTM` |
| T6WOLA1.RTM | `C:\TASPRO7\dba7\t6wola1.RTM` | `\\i2s109-solidcrm\DBAMFG$\t6wola1.RTM` |
| T6WOLA1.RTM | `C:\DBAMFG\bksam1.rtm` | `\\i2s109-solidcrm\DBAMFG$\BKSAM1.RTM` |

For a local instance these would be patched to the local folder path instead.

**Remaining risk:** Binary format parsing is exact — a mis-aligned length byte corrupts the file. Original stays on the share as backup.

---

### Blocker 7 — Full local EVO running end-to-end (CONFIDENCE 68/100)

With blockers 1, 3, 4 resolved and 2, 5, 6 mostly resolved:

**Steps required:**
1. Copy `\\i2s109-solidcrm\DBAMFG$\` → local folder (e.g. `C:\EVOLocal\`)
2. Start Workgroup Engine (`w3dbsmgr.exe`) pointing at `C:\EVOLocal\`
3. Edit `C:\ISTS\taspro7.ini` — update 3 lines to `C:\EVOLocal\`
4. Binary-patch RTM files with corrected local paths
5. Launch EVO via `StartEvo.exe` / `tp7runtime.exe`

**What's likely to work:** Login, navigation, data browsing, most reports  
**What may fail:** Any .RWN with hardcoded absolute UNC paths in encrypted bytecode; any feature calling external tools by absolute path; multi-user locking (Workgroup Engine handles this differently)

---

## Revised Confidence Ratings

| Task | Original | Revised | Key finding |
|------|----------|---------|-------------|
| 1. Change startup path | 70/100 | 92/100 | `taspro7.ini` has exactly the right 3 settings |
| 2. .RWN paths relative | 35/100 | 72/100 | `BKSY_PRGS_WHR` is blank; `open` uses logical names |
| 3. Copy files | 95/100 | 95/100 | Unchanged |
| 4. Local Pervasive engine | 45/100 | 85/100 | `w3dbsmgr.exe` (Workgroup Engine) already installed |
| 5. DDF paths | 78/100 | 85/100 | Standard relative-path DDF convention likely applies |
| 6. Patch RTM files | 88/100 | 88/100 | Unchanged; already analyzed |
| 7. Full EVO running | 30/100 | 68/100 | All major blockers resolved; encrypted .RWN edge cases remain |

---

## Files Referenced

| File | Purpose |
|------|---------|
| `C:\ISTS\taspro7.ini` | TAS Pro 7 runtime config — the master control |
| `C:\ISTS\StartEvo.exe` | EVO launcher |
| `C:\ISTS\RBuilder.ini` | ReportBuilder Designer layout prefs (no path config) |
| `C:\ISTS\EvoSettings.INI` | Per-user EVO settings (printer, UI prefs — no paths) |
| `C:\Program Files (x86)\Actian\PSQL\bin\w3dbsmgr.exe` | Workgroup Engine (v12, 32-bit) |
| `C:\Program Files (x86)\Pervasive Software\PSQL\bin\w3dbsmgr.exe` | Workgroup Engine (v11, 32-bit) |
| `\\i2s109-solidcrm\DBAMFG$\` | Production EVO data and programs |

---

## Next Steps (not yet done)

- [ ] Check the size of `\\i2s109-solidcrm\DBAMFG$\` to estimate copy time/space
- [ ] Test starting `w3dbsmgr.exe` against a small set of local .B files to confirm it works
- [ ] Check DDF files to confirm relative vs. absolute paths
- [ ] Write binary patcher for RTM files
- [ ] Test full copy + launch
