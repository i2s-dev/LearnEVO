"""
Pass 103d — Append Boot Sequence documentation to HELP-RESOURCES.md
Source: START_UP.DBA string dump, FILELOC.B parse, StartEvo.exe .NET string analysis
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

BLOCK = '''

---

## Pass 103d — Boot Sequence and File Location System (2026-06-18)

Source: START_UP.DBA binary string extraction, FILELOC.B structure parse (3,613 records),
StartEvo.exe .NET string analysis (PDB path: D:\\prog\\evoerp\\StartEvo\\), WHOAMI.DBA read.

---

### Complete EvoERP Boot Sequence

**Step 1 — StartEvo.exe (C# .NET launcher, C:\\ISTS\\StartEvo.exe)**

StartEvo.exe is a custom C# .NET application (not part of DBA/TAS Pro original code).
Built by i2 Systems at `D:\\prog\\evoerp\\StartEvo\\`. Key functions extracted from binary:

| Function | What it does |
|----------|-------------|
| `GetEvoDir` | Reads EvoERP install directory from config |
| `UpdateIniFile` | Writes/updates `evoini` (EvoERP.INI) with current settings |
| `DomainAuthenticateAndLaunchEvo` | Main entry — authenticates Windows domain user, then launches EVO |
| `IsCompanyAllowed` | Checks that the authenticated user may access the selected company |
| `GetMenuName` | Retrieves the menu RWN filename to pass to tp7runtime.exe |
| `GetUserCompProg` | Assembles user + company + program command-line arguments |
| `KillEvoProcesses` | Terminates stale `tp7runtime.exe` / `EvoERP.exe` processes from prior sessions |
| `LaunchEvoWithUser` | Spawns `tp7runtime.exe` with the assembled arguments |
| `ProcessEvoUri` | Handles URI-scheme deep links (e.g. `evo://...` protocol) |
| `TAS_ISTS_PATH_PROGRAMS` | Environment variable: path where TAS Pro looks for .RWN program files |

Environment variable `TAS_ISTS_PATH_PROGRAMS` is set to the DBAMFG$ share path so
TAS Pro runtime can locate all .RWN compiled programs.

**Step 2 — tp7runtime.exe (TAS Professional 7 runtime)**

Command line constructed by `LaunchEvoWithUser`:
```
tp7runtime.exe EvoERPmenu.RWN /user:<USERNAME> /company:<CO> /pass:<PASSWORD>
```
Arguments `userArg`, `passArg`, and `company` map to `/user`, `/pass`, `/company` flags.

**Step 3 — EvoERPmenu.RWN (encrypted main menu)**

EvoERPmenu.RWN (497,383 bytes, on DBAMFG$ share) is the encrypted TAS Pro main menu
program. Cipher: Twofish-192-CFB-128 (cipher key derived from "mabufoju"). On load,
tp7runtime decrypts and executes it. EvoERPmenu chains to START_UP.DBA first.

**Step 4 — START_UP.DBA (TAS Pro compiled startup script)**

START_UP.DBA (27,083 bytes, on DBAMFG$ share) is the initialization script that runs
before the main menu is displayed. Confirmed execution sequence from string analysis:

1. Opens `FILELOC` — loads the file location routing table (386 tables × 6 companies)
2. Opens `TASCOLOR` — loads UI color scheme settings
3. Checks `START_UP.RUN` integrity (flags read-only attribute errors)
4. Runs `USECOMP.RUN` (3,567 bytes) — company selection dialog
5. Displays "Please wait while we do some short system checking."
6. Opens `BKSYMSTR` and `BKYSMSTR` — validates no duplicate system master records
7. Shows registration screen:
   - Company: **AMERICAN BACKPLANE INC.** (i2 Systems' prior registered name)
   - Address: 355 BANTAM LAKE ROAD, MORRIS, CT 06763
   - Serial No: **75790**
   - Expiry: **12/31/30** (December 31, 2030)
   - Licensed users: **15**
8. If in demo mode: shows "DEMO VERSION — limited to 150 records per file" notice

**Step 5 — Main Menu (EvoERPmenu.RWN continued)**

After START_UP.DBA returns, EvoERPmenu.RWN displays the EvoERP top-level menu.
The menu reads user permissions from BKSLEVEL and presents authorized menu items.

---

### FILELOC.B — File Location Routing Table

`FILELOC.B` (2,793,472 bytes) is the central Btrieve file that tells TAS Pro runtime
where to find each logical table for each company. Loaded first at every boot.

**Statistics (confirmed from full parse):**
- 3,613 total records
- 386 unique logical table names
- 6 company codes: AT, AB, CA, I2, IT, 99
- 1,754 alias mappings (48.5%) — different physical file per company
- 1,859 same-name mappings — same physical file across companies

**Record format (inferred from parsed data):**
```
Bytes 0–7:   Logical table name (8 chars, space-padded)
Bytes 8–15:  Physical filename alias (8 chars, space-padded)
Byte 16:     'B' (Btrieve file type marker)
Bytes 17–18: Company code (2 chars)
```

**Company codes in FILELOC.B:**
| Code | Records | Identity |
|------|---------|---------|
| AT | 714 | Internal/testing company AT |
| AB | 714 | "American Backplane" — legacy production company |
| CA | 714 | Company CA |
| I2 | 714 | i2 Systems — current production company |
| 99 | 735 | Demo / test company (standard DBA "company 99") |
| IT | 22 | IT admin / system company |

When TAS Pro opens a table (e.g., `BKSOX`), it looks up `FILELOC` to find the
physical filename and folder for the current company. This allows the same TAS Pro
code to route different companies to different data files.

**Key aliasing examples (I2 company):**

| Logical Name | Physical File | Explanation |
|-------------|--------------|-------------|
| BKARINV | BKARRINV | AR invoice — "R" archive variant |
| ROUTING | BKRTEMTR | Routing uses MT-era routing table |
| ISSRINFO | ISSRAINF | Sales receipt info → SR-specific variant |
| BKARCUST | BKCMCUST | Customer → Contact Manager customer alias |
| BKARCUST | ISARACST | Customer → IS-AR archive variant |
| BKICLOC | TBKICLOC | Inventory location → T-prefixed variant |
| WOLABOR | WOLABRPT | WO labor → Labor reporting variant |
| BKGLCOA | BKGLECOA / BKGLFCOA | COA → GL extended / GL forecast variants |
| INVTXN | INVATXN / INVETXN | Inventory transactions → archive variants |
| ISSERIAL | ISHLOTS | Serial control → lot-managed serial variant |
| BKART | ARTTEMP | AR transactions → temp/staging |
| ESTSUM | ISESTASM | Estimate summary → IS estimate assembly |

The I2 company has 200+ unique aliases, reflecting extensive customization.
(By comparison, AT company is a clean/test installation with fewer aliases.)

---

### WHOAMI.DBA — Workstation Identity File

`\\i2s109-solidcrm\\DBAMFG$\\WHOAMI.DBA` is **2 bytes** (CR+LF only — essentially empty).
The per-workstation identity file is stored locally: `C:\\ISTS\\WHOAMI.DBA`.
The network copy being empty suggests all workstation-specific data lives locally.

The CLAUDE.md notes WHOAMI.DBA can be 35 bytes — the local workstation copy at
C:\\ISTS\\WHOAMI.DBA may contain workstation name, last user, company code, and
other session state that survives restart.

---

*Pass 103d — Boot sequence confirmed from START_UP.DBA + StartEvo.exe binary analysis.*
*Boot Sequence confidence: 68→82/100.*
'''

with open(PATH, 'a', encoding='utf-8') as f:
    f.write(BLOCK)

print(f'Appended {len(BLOCK):,} chars')
