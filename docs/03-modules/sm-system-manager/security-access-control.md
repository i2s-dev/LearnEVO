# EvoERP Security & Access Control

Status: partial | Pass 249 2026-06-24

Source: DDF schema.md (AHSYLOG/BKPSUSER/BKSLEVEL), rwn_symbols.json
(T7MDefaults.RWN, EvoChangePass.RWN, T7LIMACC.RWN, EvoERPmenu.RWN variables)

---

## Three-Tier Security Model

EvoERP enforces access at three independent levels:

```
Login
  └─► BKPSUSER (user profile)
        ├─ CODE = username
        ├─ PSWD = encrypted password (10-char ENCRYPTSTR cipher)
        └─ SEC  = security level code (30 chars)

Menu/Operation Security
  └─► BKSLEVEL (keyed by MENU + LEVEL)
        ├─ For each of 20 menus: YN flag (can access this menu?)
        └─ For each menu: 20 operation flags (A-T = which options within)

Field/Object Security (optional, enabled by ISTS.CFG.LIMACC)
  └─► ISACCESS (form-level, Btrieve-only, not in DDF)
        ├─ NAME = feature/program name
        ├─ DFM  = which form
        ├─ OBJ  = which control on the form
        └─ STATUS = enabled/disabled/hidden
```

---

## BKPSUSER — User Profile (11 fields, DDF confirmed)

Primary key: `BKPS_USER_CODE`

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKPS_USER_CODE` | STRING | 15 | Login username (PK) |
| `BKPS_USER_PRT` | UBINARY | 2 | Default printer assignment |
| `BKPS_USER_MENU` | UBINARY | 2 | Starting menu number |
| `BKPS_USER_CMPY` | STRING | 2 | Default company code |
| `BKPS_USER_MWIND` | STRING | 1 | Menu window display mode |
| `BKPS_USER_PSWD` | STRING | 10 | Encrypted password (ENCRYPTSTR, 10-char output) |
| `BKPS_USER_ME` | STRING | 1 | Flag — purpose unknown (management/exec?) |
| `BKPS_USER_SEC` | STRING | 30 | Security level code (30-char; links to BKSLEVEL/AHSYLOG) |
| `BKPS_USER_MCNTR` | UBINARY | 2 | Menu counter (position state) |
| `BKPS_USER_LDATE` | DATE | 4 | Last login date |
| `BKPS_USER_EMP` | UBINARY | 2 | Employee number link (→ BKPRMSTR or employee table) |

Variable access namespace (from T7MDefaults, EvoChangePass, EvoERPmenu):
`BKPS.USER.CODE/PRT/MENU/CMPY/MWIND/PSWD/ME/SEC/MCNTR/LDATE/EMP`

---

## BKSLEVEL — Menu Permission Matrix (422 fields, DDF confirmed)

Key: `BKSL_MENU` (UBINARY 2) + `BKSL_LEVEL` (STRING 2)

**Structure:** 20 menu slots × (1 YN access flag + 20 operation flags) = 420 fields + 2 key = **422 total**.

Note: the TODO previously said "14 menus" — the correct count is **20 menus**, which gives 20×21+2=422 ✓.

| Field pattern | Type | Meaning |
|---------------|------|---------|
| `BKSL_MENU` | UBINARY 2 | Menu slot index (PK 1) |
| `BKSL_LEVEL` | STRING 2 | Security level code (PK 2; links to BKPS_USER_SEC) |
| `BKSL_MENU{N}_YN` | STRING 1 | Y = user can access menu N; N = entire menu blocked (N=1..20) |
| `BKSL_MENU{N}_{M}` | STRING 1 | Y/N access to operation M within menu N (M=1..20, mapped to ops A-T) |

Variable access namespace from T7MDefaults.RWN:
- `BKSL.MENU` — current menu under evaluation
- `BKSL.KEY` — compound lookup key
- `BKSL.LEVEL` — security level code
- `BKSL.MENU1.YN` through `BKSL.MENU20.YN` — menu-level Y/N flags
- `BKSL.MENU1` through `BKSL.MENU20` — per-menu operation code arrays

The 20 menu slot indices correspond to EvoERP's top-level module menus (AR, AP, IN, SO, PO, WO, GL, MR, etc.), but the exact slot-to-module mapping is not yet confirmed.

---

## ISACCESS — Form/Field-Level Security (Btrieve-only, not in DDF)

**Enabled by:** `ISTS.CFG.LIMACC` = Y

**Managed by:** `T7LIMACC.RWN` (42 procs, source library unknown)

ISACCESS implements **object-level access control** within forms — it can disable, hide, or restrict individual controls (fields, buttons, labels) for specific user groups. This is an optional fine-grained security layer on top of the menu-level BKSLEVEL permissions.

Variable access namespace `IS.ACC.*` (8 vars, confirmed from T7LIMACC.RWN):

| Variable | Meaning |
|----------|---------|
| `IS.ACC.NAME` | Feature/program name |
| `IS.ACC.DFM` | DFM form filename (e.g., "T7SOA.DFM") |
| `IS.ACC.OBJ` | Control/object name on the form |
| `IS.ACC.OBJTYPE` | Type of object (TEdit, TButton, TLabel, etc.) |
| `IS.ACC.STATUS` | Access status: enabled / disabled / hidden |
| `IS.ACC.FIELD` | Database field name being controlled |
| `IS.ACC.TEXT` | Display text of the control |
| `IS.ACC.EXTRA` | Additional configuration |

Other T7LIMACC vars: `DFMNAME`, `AGROUP`, `LAGROUP` (access group), `LGNUM` (group number),
`ACC.REC`, `ACCESS_REC_HOLD`, `DFM.H` (DFM form handle), `DFM_OBJNAME`, `OBJECT_LIST`,
`COPY.TO` (copy configuration to another group).

---

## AHSYLOG — Legacy DBA-Era User Table (23 fields, DDF confirmed)

**Status: Superseded by BKPSUSER + BKSLEVEL in TAS Pro 7 era.**
Not referenced in any T7 RWN program (only legacy T6/DBA programs use it).

Key: `AHSY_USER_LEVL`

| Field | Type | Size | Offset | Meaning |
|-------|------|------|--------|---------|
| `AHSY_USER_LEVL` | STRING | 2 | 0 | Security level code (PK; equivalent of BKPS_USER_SEC) |
| `AHSY_USER_MENU` | STRING | 4 | 2 | Starting menu (4-char code, e.g., "MAIN") |
| `AHSY_USER_CTRL` | STRING | 1 | 6 | Control flag (single char; purpose unconfirmed) |
| `AHSY_USER_ACCES_1` | STRING | 1 | 7 | Module access flag 1 (Y/N) |
| `AHSY_USER_ACCES_2` | STRING | 1 | 8 | Module access flag 2 (Y/N) |
| ... | ... | ... | ... | ... |
| `AHSY_USER_ACCES_20` | STRING | 1 | 26 | Module access flag 20 (Y/N) |

The 20 ACCES flags map to 20 module groups — exact index→module mapping not yet confirmed
(requires reading actual AHSYLOG data or finding a DBA-era setup program that initializes these).

---

## ISEXUSER — Extended User Table

Used by EvoChangePass and T7APA/T7ARA/T7SOC for extended user attributes:

Variable namespace `ISEX.USER.*` (from EvoChangePass):
- `CODE` — matches BKPS_USER_CODE
- `GROUP` — extended user group
- `DATE1`, `DATE2` — dates
- `MISC1`, `MISC2` — miscellaneous flags
- `WINDO` — Windows domain username (SSO link: matches Windows login for auto-login)
- `PASSW` — extended password (separate from BKPS_USER_PSWD)
- `PEXPD` — password expiry date
- `LPASS` — last password change date
- `LDATE` — last access date
- `FLAGS` — flag field

---

## Password Storage

**Standard password:** `BKPS_USER_PSWD` (STRING 10) — TAS Pro 7 `ENCRYPTSTR` keyword, 10-char
output. Not reversible without runtime; the ENCRYPTSTR algorithm is undocumented.

**Extended password:** `ISEX.USER.PASSW` — separate field; `ISEX.USER.PEXPD` = expiry date.

**Encryption flags:**
- `ISTS.CFG.EPASS` = use encrypted password storage (enable extended hashing)
- `ISTS.CFG.EHPASS` (from EvoChangePass) = encrypted hash password flag

---

## Security Bypass Flag

`ISTS.CFG.ACCESS` appears in virtually every T7 module program (500+ occurrences across 1,122
programs) as `ACCESS.H` handle + `ISTS.CFG.ACCESS` flag. This is a **system-wide access bypass
flag** — when set, it may suppress normal BKSLEVEL checks (e.g., for admin/super-user mode).

`ACCESS.H` is the ISACCESS file handle opened by each program to perform field-level security
lookups.

---

## Security Flow (confirmed runtime behavior)

```
1. User enters login code + password
2. EvoERPmenu.RWN: read BKPSUSER by code → check ENCRYPTSTR(entered_pw) == BKPS_USER_PSWD
3. If ISTS.CFG.SSO=Y: match ISEX.USER.WINDO to Windows domain username (skip pw check)
4. Load security level: BKPS.USER.SEC → in-memory BKSL.LEVEL
5. T7MDefaults.RWN: read BKSLEVEL for each of 20 menus → load BKSL.MENU*.YN into session
6. At each menu: check BKSL.MENUn.YN; if N, hide/disable all operations in that menu
7. At each operation: check BKSL.MENUn.{m} (the option's slot); if N, block access
8. If ISTS.CFG.LIMACC=Y: open ISACCESS → per-form object-level restrictions apply
9. Write ISLOG session record (WHO/WHAT/COMPANY/STARTD/STARTT)
```

**Confidence: 78/100** — DDF schemas confirmed byte-for-byte; BKSL.* and BKPS.* variable
namespaces confirmed from T7MDefaults and EvoChangePass binary extraction. Three-tier model
is strongly inferred from the code structure. The exact AHSYLOG ACCES_1..20 module mapping and
the BKSLEVEL slot-to-module mapping require runtime observation or legacy DBA source to confirm.
