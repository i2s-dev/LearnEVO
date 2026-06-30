# Security, Login, and Company Selection

Status: draft — assembled from the `AHSYLOG` / `EVOUSERS.DCY` /
`EVOLOGO` / `EvoMenu_LOGIN.DCY` evidence. Not yet confirmed by a
running trace.

## User authentication

### Table — `AHSYLOG`

Authoritative per-user access record. Schema (from extracted DDF):

| # | Field | Type | Size |
|---|-------|------|-----:|
| 1 | `AHSY_USER_LEVL` | STRING | 2 |
| 2 | `AHSY_USER_MENU` | STRING | 4 |
| 3 | `AHSY_USER_CTRL` | STRING | 1 |
| 4-23 | `AHSY_USER_ACCES_1` … `AHSY_USER_ACCES_20` | STRING | 1 each |

Meaning (inferred):
- `AHSY_USER_LEVL` — 2-char role/level code (e.g. `AD`, `SU`, `MG`).
- `AHSY_USER_MENU` — 4-char starting-menu code for this user (e.g.
  `MAIN` / `SMDF`).
- `AHSY_USER_CTRL` — 1-char control flag (active/disabled / admin?).
- `AHSY_USER_ACCES_1..20` — **20 per-module permission flags.** Each
  is one byte — probably `'Y'` / `'N'` / possibly `'R'` (read-only).
  Likely index corresponds to module order (AR=1, AP=2, IN=3, SO=4, …
  — to confirm).

### Login form (`EVOMENU_LOGIN.DCY` + ...)

The login UI is driven by the encrypted data dictionary
`EVOMENU_LOGIN.DCY` loaded by `EvoERPmenu.RWN`. Related files that
appear to participate:

- `EVOMENU_LOGIN.DCY` — login screen layout (encrypted).
- `EvoDC_LOGIN.DCY` / `DBAMENU_LOGIN.DCY` / `WBKMENU_LOGIN.DCY` —
  alternate login flavors (DBA classic, data-collection mode).
- `EVORESETPASS.DCY` / `EVOCHANGEPASS.DCY` — password reset / change.
- `EVOUSERS.DCY` — user admin screen (Enter Users — SM-??).

### Password storage — `BKSYUSER` (confirmed Pass 410, 2026-06-30)

Physical file: `\\i2s109-solidcrm\DBAMFG$\Default\BKSYUSER.B` (31,744 bytes, Btrieve FC magic).
This table is Btrieve-only (not in PSQL DDF).

Fields from FILEDICT:
- `BKSY.USER.CODE` — user login code (key field)
- `BKSY.USER.PSWD` — password hash/stored value
- `BKSY.USER.LEVL` — security level assignment
- `BKSY.USER.CTRL` — control flags
- `BKSY.USER.NAME` — user display name

Binary analysis: records contain `'N'`-padded fields — no plaintext passwords visible.
The runtime uses `ENCRYPTSTR`/`DECRYPTSTR` keywords, suggesting passwords are stored
with TAS Pro's built-in symmetric encryption.

`BKSYUSER` is distinct from `AHSYLOG`:
- `BKSYUSER` = authentication (who you are, password, level)
- `AHSYLOG` = authorization (what you can access per module)

## Per-workstation identity — `WHOAMI.DBA`

`C:\ISTS\WHOAMI.DBA` — 35-byte file on every workstation. Read by the
TAS `WHOAMI` function (runtime keyword at offset 7965 in
`tp7runtime.keywords.txt`). Used:
1. As input to the **multi-user lock manager** (`LOCK_OWNER` keyword).
2. As a **seat identity** paired with the license check.
3. Possibly as a per-workstation default (printer, form overrides).

## Company selection

Following login, `EVOMENU_SELCOMP.DCY` drives company selection.
Companies map to data folders as described in
[docs/04-data-dictionary/overview.md](../04-data-dictionary/overview.md):
`\\I2S109-SOLIDCRM\DBAMFG$\<COMPANY>\*.B<CODE>`.

Known company codes on this installation (folder suffixes):

- `Default` / `.B` — the seed / primary company
- `22`, `AB`, `AT`, `CA`, `Goldstar`, `I2`, `IT`, `UU` — user-visible
  companies
- `DefaultSQL` — SQL-oriented variant (probably for the
  Pervasive-SQL Java helper in `EvoPVT.jar`)
- `Testdata`, `DEV` — non-production
- `Bak Up`, `Menu Backup`, `Recovered` — backups

The login program sets `DfltCompanyCode` in `taspro7.ini` after the
user's selection.

## Multi-layer security model (confirmed Pass 105, 2026-06-18)

EvoERP has **four distinct access control layers**, applied sequentially:

| Layer | Mechanism | Table / File | Scope |
|-------|-----------|--------------|-------|
| 1. License gate | `StartEvo.exe` queries `tas_menus` via PSQL DSN=EVOADMIN | `BKMENUSU.DBF` | Whether a program is licensed at all |
| 2. User/module | `AHSYLOG.AHSY_USER_ACCES_1..20` flags | `AHSYLOG` | Which of 20 module groups a user can access |
| 3. Menu access | `WBKMENUSETUP.RWN` / `BKPSUSER.SEC` | `BKPSUSER` | Which individual program codes the user's security level permits |
| 4. Field-level | `T7LIMACC.RWN` (PS-L "Enter Field Specific Access") | unknown table | Which individual fields a user can view or edit |

### Layer 2 — `AHSYLOG` module-level flags

`AHSY_USER_ACCES_1..20` — 20 one-byte flags per user. Each is `'Y'`/`'N'`/`'R'` (read-only inferred). The module-to-index mapping is not yet confirmed; the 20 slots likely correspond to the ~20 nav tab module groups.

`AHSY_USER_LEVL` (2 chars) links to `BKSLEVEL` — the security level permission matrix. See §BKSLEVEL below for confirmed structure.

### `BKSLEVEL` — Security Level Access Masks (confirmed Pass 410, 2026-06-30)

Physical file: `\\i2s109-solidcrm\DBAMFG$\Default\BKSLEVEL.B` (50,176 bytes, Btrieve FC magic).

**Record structure** (424 bytes per record; confirmed from FCR[0x16]=424):

| Offset | Size | Field | Notes |
|--------|------|-------|-------|
| 0 | 4 | Btrieve record header | Delete flag + internal |
| 4 | 1 | `BKSL.LEVEL` | Security level code: ASCII digit `'1'`–`'9'` |
| 5 | 1 | Separator | Space `0x20` |
| 6 | 418 | Access mask | 19 groups × 22 bytes = 418 bytes |
| — | **424** | Total | |

The 418-byte access mask is 19 entries of:
- `BKSL.MENUn` (21 bytes): per-operation Y/N flags for that menu group (each byte = `'Y'` or `'N'`)
- `BKSL.MENUn.YN` (1 byte): master enable/disable flag for the entire group

**This installation has all levels set to all-`'N'`** — every byte in every access mask is `0x4E` ('N'). This means level-based access control is **disabled** in this installation; access is enforced entirely through `AHSYLOG.AHSY_USER_ACCES_1..20` per-user flags.

**Levels present** (5 records in BKSLEVEL.B):
Levels '1', '2', '3', '4', '5' — all with all-N (deny) masks.

### `BKSLMSTR` — Security Level Names (confirmed Pass 410, 2026-06-30)

Physical file: `\\i2s109-solidcrm\DBAMFG$\Default\BKSLMSTR.B` (29,696 bytes).
Contains descriptive names for each security level:

| Level | Name |
|-------|------|
| 1 | All |
| 2 | All except PR |
| 3 | ALL EXCEPT SYSMGR,GL,AM,AD,PR |
| 4 | MFG,ITEM ONLY |

These names describe the **intended** access template for each level, but since all masks are all-N in this installation, the templates are not currently enforced by BKSLEVEL. The level assignment in AHSYLOG is present but the level-gate is effectively bypassed.

### Layer 3 — `BKPSUSER` program-level access

`BKPSUSER` (11 fields, confirmed Pass 46):

| Field | Size | Meaning |
|-------|------|---------|
| `CODE` | 15 | User code (PK, links to AHSYLOG) |
| `PSWD` | 10 | Per-program password (for sensitive programs) |
| `PRT` | 1 | Print permission flag |
| `MENU` | 4 | Starting menu (4-char code) |
| `CMPY` | — | Default company |
| `MWIND` | — | Max windows open |
| `ME` | — | Memo flag |
| `SEC` | 30 | Security code string (which programs allowed) |
| `MCNTR` | — | Menu counter |
| `LDATE` | — | Last login date |
| `EMP` | — | Links to BKPRMSTR (employee record) |

### Security administration programs (from BKMENUSU.TXT, Pass 105)

| Menu code | Label | Program |
|-----------|-------|---------|
| PS-A / ST-H-A | System Users/Passwords | `t7psa.rwn` |
| PS-B | DBA System Security Levels | `bkpsb.run` (legacy) |
| PS-C | DBA Company Logon Access | `bkpsc.run` (legacy) |
| PS-E | Evo Menu Access by User Report | `t7pse.rwn` |
| PS-F | Evo Menu Access by Program | `t7psf.rwn` |
| PS-G / ST-H-B / TA-G | Maintain Menu Access Records | `WBKMENUSETUP.RWN` |
| PS-H | Configure Auto-Chain Programs | `T7CHAIN.RWN` |
| PS-I | Enter Approved Signers for POs | `T7DIGSIGADMIN.RWN` |
| PS-J | Enter Contract Review Signers | `T7CTREVUADMIN.RWN` |
| PS-K | Enter Vendor Approval | `J7appvend.rwn` (J7 custom) |
| PS-L | Enter Field Specific Access | `T7LIMACC.rwn` |

## Admin setup

The security administration path is:
- **PS-A** (`t7psa.rwn`) — Enter users, set roles, set passwords
- **PS-G** (`WBKMENUSETUP.RWN`) — Configure which menu items each user/level can see
- **PS-B/C** (`bkpsb.run`, `bkpsc.run`) — Legacy DBA-era level/company access (still present)
- **PS-L** (`T7LIMACC.rwn`) — Field-specific access (granular field-level read/write control)

## Session / locking

Runtime keywords `LOCK_OWNER`, `REC_LOCK`, `UNLOCK`,
`DUPCHECK`, `IFDUPCB` indicate the TAS program explicitly reserves
records it intends to modify. When a user picks an action like
"Enter Vouchers" (`AP-B`), the program opens `BKAPINVT` with
`open BKAPINVT lock W` (write-lock) and other users see
`LOCK_OWNER = <WHOAMI>`.

`EVOUSERS.DCY` plus `BKLOGON` (1 table on the inventory) probably also
track who is currently logged in to prevent double-login of the same
seat and to drive the "who's in the system" status bar.

## Help System Scope — `DBAHLPID.B` (Pass 410, 2026-06-30)

Physical file: `\\i2s109-solidcrm\DBAMFG$\Default\DBAHLPID.B` (178,176 bytes).
Btrieve-only table. Maps menu/help topic codes to help page IDs.

**Record format**: `8XX-Y    ` (9-char fixed-width key) + 1-byte sequential page ID.
- `8` = section prefix (all EvoERP help = section 8)
- `XX` = 2-char module code
- `-Y` = operation letter (A, B, C, ...)
- Trailing spaces = fixed-width padding

Contains **647 unique operations across 43 modules**. Modules with no help topics defined
(e.g. QC) are absent even if they exist in the menu. One module (`AI`) has 4 operations
in DBAHLPID but no BKMENUSU.TXT GROUPS/BUTTONS entry — likely a hidden internal module.

This is the most complete functional scope catalog for EvoERP: every accessible menu operation
that has context-sensitive help is enumerated in DBAHLPID. See
[module-codes.md](../03-modules/module-codes.md) for the full 42-module reference.

`DBAHELP.B` (94,208 bytes): the companion file containing actual help text. Contains no
printable strings ≥15 chars — help text is stored in an encoded/binary format.

## Things still to verify

- [ ] Confirm ACCES_1..20 index → module mapping. Easiest: open
  `EVOUSERS.DCY` in the running app while watching the AHSY record
  being written.
- [ ] Password hashing algorithm. Is it just `ENCRYPTSTR` (symmetric
  TAS obfuscation)?
- [ ] How `AHSY_USER_MENU` maps to an actual menu tree entry. We know
  menu codes look like `SO-A`, but `AHSY_USER_MENU` is 4 chars —
  perhaps it points to a custom **main-menu** subtree (e.g. `MMAR` =
  "Main Menu → AR").
