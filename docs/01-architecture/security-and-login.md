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

### Password storage

Not yet observed in any plaintext. Candidate columns on `AHSYLOG` or
a parallel `BKPSUSER` table (present in the table inventory,
1 field discovered — record likely has an encrypted-password column we
haven't decoded yet). The runtime has `ENCRYPTSTR` / `DECRYPTSTR`
keywords, suggesting the password is stored encrypted with a
runtime-private key.

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

## Admin setup

The `SM-*` menu operations (34 entries — see
[06-menu-system/overview.md](../06-menu-system/overview.md)) are
where user+company administration lives. Key operations to map to
the AHSYLOG ACCES_1..20 columns:

- `SM-???` Enter Users → `EVOUSERS.DCY` + `AHSYLOG` rows.
- `SM-???` Change Password → `EVOCHANGEPASS.DCY`.
- `SM-???` Reset Password → `EVORESETPASS.DCY`.
- `SM-???` Company Setup → writes `DfltCompanyCode`-ish metadata.

Specific SM-x codes are listed in the menu overview; mapping each to
its DCY form is a follow-up.

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
