# Plaintext SRC Deep-Dive

Status: verified. Complete analysis of the 7 plaintext `.SRC` files
available on the deployment share. These are the only readable
EvoERP program listings we have without decrypting `.RWN`.

Source files (copies in `../../samples/src/`):

| File | Size | Menu | Purpose |
| ---- | ---: | ---- | ------- |
| `Bkaph.src`   | 41 KB | **AP-H**   | Print A/P Checks (dot-matrix / legacy) |
| `Bkapha.src`  | 46 KB | **AP-H-A** | Print A/P Checks (laser format) |
| `BKAWLB.SRC`  | 24 KB | **LW-J-B** (aliased `AW-L-B` after 2000 merge) | Print Work Order Schedule |
| `BKDCA.SRC`   | 29 KB | **DC-A**   | Data Collection Entry (shop floor) |
| `BKLME.SRC`   | 29 KB | **LM-E**   | Label Management (lot/serial history) |
| `BKMRF.SRC`   | 55 KB | **MR-F**   | MRP — dependent demand generation |
| `BKROA.SRC`   | 73 KB | **RO-A**   | Routing Master — Enter Routings |

The 7 are a representative cross-section: AP, inventory/labels, data
collection, MRP, routing, and a work-order listing. The absence of the
`BKSO*`/`BKAR*` core-business sources suggests the share holds only
historical leftover sources; the bulk of the dev tree isn't here.

## What each program opens — the table-dependency map

Tables opened with `open <TABLE> lock <N|W|R>` directly from each SRC:

| Program | Menu | Tables opened (core) |
| ------- | ---- | -------------------- |
| **Bkaph** | AP-H | BKAPCHKF, BKAPCHKH, BKAPINVT, BKAPVEND, BKGLCHK, BKGLCOA, BKGLTEMP, BKPRTCFG, BKSYMSTR, BKYSMSTR |
| **Bkapha** | AP-H-A | same as Bkaph + extra laser-format tables |
| **BKAWLB** | LW-J-B | BKARCUST, BKICMSTR, MTICMSTR, BKSYMSTR, WORKORD |
| **BKDCA** | DC-A | BKDCSHFT, BKGLCOA, BKGLTEMP, BKPRMSTR, BKSYMSTR, BKYSMSTR, MACHINE, MTICMSTR, TOOL, WOLABOR |
| **BKLME** | LM-E | BKAPVEND, BKICMSTR, MTICMSTR, BKSYMSTR, BKYSMSTR, INVTXN |
| **BKMRF** | MR-F | BKAPPO, BKAPPOL, BKARINV, BKARINVL, BKBMMSTR, BKICLOC, BKICMSTR, BKMRPFC, BKMRPSW, CALENDAR, MTICMSTR, WORKORD, … |
| **BKROA** | RO-A | BKAPVEND, BKICMSTR, BKRTEMTR, BKRTSPEC, BKRTTEMP, BKYSMSTR, MACHINE, MTICMSTR, ROUTING, ROUTTEMP |

### Observations

- **`BKSYMSTR` + `BKYSMSTR` are pervasive dependencies** — almost every
  business program opens one or both. These two are the "system
  settings" tables that hold company-level defaults (account codes,
  fiscal rules, printer/form overrides). Any program that prints or
  posts needs them.

- **`BKGLCOA` (Chart of Accounts) + `BKGLTEMP`** appear whenever a
  program posts to GL (AP checks, DC labor entry, etc.). The normal
  pattern is: hit the real ledger via `BKGLTEMP` first, then
  `BKGLCHK` validates, then commit.

- **`BKICMSTR` + `MTICMSTR` always appear together** — this confirms
  the hypothesis that `MT*` is a second-generation inventory master
  overlay on `BK*`. Programs need both to find a part.

- **`BKDCA` (DC-A)** opens `MACHINE`, `TOOL`, `WOLABOR` — the shop-floor
  labor and equipment tables. Combined with `BKPRMSTR` (payroll
  master), this is where labor actuals roll through to both Job
  Costing (`WOLABOR`) and eventual payroll (`BKPRMSTR`).

- **`BKMRF` (MRP)** touches the widest set: POs, invoices, BOMs, on-
  hand locations (`BKICLOC`), forecasts (`BKMRPFC`), and the work
  order header (`WORKORD`). Classic MRP — supply + demand nets out.

- **`BKROA` (Routing)** is the biggest source (2433 lines) — routing
  editing is inherently the most complex UI in the system because
  routings have: header, operations, specs, temporary/staging copies,
  machine+tool+vendor lookups, and nested labor/cost overrides.

## Common idioms observed

### The "TAS 3→5 conversion" banner

All `BK*.SRC` files carry:
```
;Cvtd from TAS-Pro 3.0 edt to 5.0 src on <date>
```
— these were hand-converted from the DOS-era "EDT" (editor/data entry)
format to TAS Pro 5 source. Some were converted in 1995-1996 and
modified into the 2000s. The history comments at the top of each file
are a 10-year patch log.

### File layout inside an SRC

```
;HEADER COMMENTS
;Copyright DBA Software, Inc. 1992-1999 …
;Portions Copyright 1985-1995 Business Tools, Inc. …
;
;History / Modification summary
;
#UDX
#LIB ...
#INC ...
#TDATA 256000
SETUP_COLOR
;
DEFINE <vars>
PARAM <parameters>
OPEN <table> lock X
FIND F srch <key>  err EXIT NLOCK
... (init business state)

MOUNT <screen> type S
prg_hdr "XX-Y  Operation Title"

START:
    ...  ENTER / MENU / TRAP / etc.

PRINT_SECTION:
    ...

EXIT:
    close <tables>
    quit
```

### `chain` — jumping between modules

Bkaph.src:62 pattern:
```
else_if bkys.yn[48] $ '145'
   MESSAGE[1]=BKSY.PRGS.WHR * "BKAPHA"
   chain MESSAGE[1]
   quit
```

`chain <path>` **replaces the current program with another RWN/RUN** —
process control transfers completely. This is how EVO transitions
from `AP-H` to `AP-H-A` when the user has selected laser checks:
AP-H notices the `bkys.yn[48]` config flag is in `'1'`, `'4'`, or `'5'`
(three laser formats) and hands off to `BKAPHA`. The `BKSY.PRGS.WHR`
field stores the full UNC path to the programs directory.

### `else_if`, `.a.`, `.o.`, `.n.`, `$` operators

All 7 sources use the xBase-style operators:
- `.a.` — AND
- `.o.` — OR
- `.n.` — NOT
- `$` — "is a member of" (left operand is contained in right string)
- `.t.` / `.f.` — true / false

Numeric comparisons use `=`, `<>`, `<`, `<=`, `>`, `>=`.

### Inline function bodies after an `ENTER`

The TAS Pro pattern is to follow an `enter … pre pre.x() post post.x()`
statement with the body of `pre.x` / `post.x` in a `{ ... }` block
immediately below. These blocks define **local UDFs** scoped to the
program. Example from BKAWLB.SRC:117-127:

```
ENT.STAT:
    enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
    ...
    {
      func pre.stat
        trap F1 GOSUB SHOWHELP
        trap ESC goto EXIT2
        trap f10 goto start_prt
        fnc_list 'F1 Help','F10 Print,Esc Exit'
        ret .t.
    }
```

The inline block is **physical** syntax — the compiler treats the
`{ … }` as a local scope attached to the containing `enter` statement.

### `mount <screen> type S`

The legacy non-Windows way to paint input forms. Mounts a
compiled-screen resource defined elsewhere (either embedded or in a
companion `.SCR` file). In the T7 era this is replaced by
`LOAD_FORM` which loads a `.DFM`.

### The `prg_hdr` convention

`prg_hdr "XX-Y  Operation Title"` sets the title bar. The text always
follows the `XX-Y  Description` pattern — same as the menu. This is
how we extracted 554 menu codes from the RUN-file string tables: every
compiled program echoes its own menu code via `prg_hdr`.

## Where the rest of the source lives

`taspro7.ini` history entries pointed at `F:\Projects\TAS\istech\` and
`C:\TASPRO7\DBA7\` on a developer machine — those trees likely contain
the full source. We don't have access to them; the 7 files here are
leftover artifacts on the deployment share.

## Relationship to the RWN binaries

Every `.SRC` in the share has a matching `.RWN` sibling. The
`.SRC` is never loaded at run time — it's only there as a reference
copy. The runtime always executes the compiled `.RWN` (encrypted).

## `func` / `{}` — full semantics (Pass 107)

Two forms of function declaration, both confirmed from all 7 SRC files:

### Form 1: Inline `{}` block (local to an `enter` group)

```tas
enter <field> pre pre.funcname() post post.funcname() ...
{
  func pre.funcname
    ; body
    ret .t.

  func post.funcname
    ; body
    ret .t.
}
```

- The `{ }` block appears **immediately after** the `enter` statement(s) that reference `funcname()`.
- Multiple `func` definitions may share a single `{ }` block (see BKAWLB.SRC:183-207).
- These are **local to the program unit** — they cannot be called from outside the SRC file.
- `ret .t.` = return true (allow the operation to proceed); `ret .f.` = return false (abort/reject the field entry).

### Form 2: Top-level `func` (program-scope subroutine)

```tas
    define param_var type A size 1 LOCAL
func FUNC_NAME param_var
    ; body
    ret .t.
```

- Appears at the top level (no wrapping `{}`).
- Can optionally take **one parameter** declared with `define ... LOCAL` immediately above the `func` header.
- Visible from anywhere else in the same SRC file (including from `enter pre/post` hooks or `gosub` calls).
- `ret` alone (no value) = return from subroutine; `ret .t.` / `ret .f.` = return boolean.

### Confirmed in BKAWLB.SRC:
```tas
    define inv_from type A size 1 LOCAL
func SETUP_INV inv_from
    fnc_list "F1 Help,F2 Lookup","F10 Print,Esc Exit"
    if up(inv_from) = 'F' DO
        trap F2 GOSUB DSP_INV_1
    ...
    ret .t.
func POST_INV
    fnc_list "F1 Help","F10 Print,Esc Exit"
    trap F2 DFLT
    ret .t.
```

## `#INC` and `#LIB` — include/library resolution (Pass 107)

All 7 SRC files use both directives in their preamble:

```
#UDX          ; allow User-Defined Extensions (UDFs + UDCs)
#LIB DBA      ; link DBA.LIB compiled library
#LIB lookups  ; link LOOKUPS.LIB compiled library
#LIB WINDOWS  ; link WINDOWS.LIB compiled library
#inc isdef    ; include ISDEF.SRC source file (some programs only)
#INC HELPSCRN ; include HELPSCRN.SRC (present in all 7 files)
```

**Resolution rules:**
- Both `#INC` and `#inc` are valid (case-insensitive).
- `#INC <name>` resolves `<name>.SRC` in the compiler search path.
- `#LIB <name>` links `<name>.LIB` (pre-compiled) from the search path.
- Search path = `DataDictPath` from `taspro7.ini` (i.e., `\\I2S109-SOLIDCRM\DBAMFG$\`).
- `HELPSCRN.SRC` is the universal F1 help screen template; `ISDEF.SRC` is an IS-module definition include.
- `#PRO3` (commented out in BKAWLB.SRC as `;#PRO3`) = backward-compat flag for TAS Pro 3.0 programs.

## `SETUP_COLOR` and `Color Array` (Pass 107)

```tas
SETUP_COLOR      ;use the color values in TASCOLOR.OVL
Color Array Norm
```

- `SETUP_COLOR` is a **TAS built-in keyword** (not a `#` directive) that opens the `TASCOLOR` Btrieve table and reads the system color palette into internal color variables. The comment "TASCOLOR.OVL" is the developer's shorthand; the actual data source is the `TASCOLOR` table (confirmed present as a DB file in RWN fingerprints).
- `Color Array Norm` selects the **Normal** color scheme for subsequent UI elements. Other variants: `Color Array Inverse` (highlighted/selected) and `Color Array High` (error/warning). These switch which row of the TASCOLOR array the runtime uses for the next painted region.
- SETUP_COLOR appears in 5 of the 7 SRC files; the two that omit it (BKROA.SRC doesn't have it either) use legacy monochrome forms.

## Things still to document from the SRCs

- The exact **GL posting sequence** from Bkaph — a complete reference implementation of how a typical post works.
- **Screen drawing** logic — how the pre-Windows `mount`+`enter` model paints and refreshes.
- **Expression precedence** — the relative priority of `+/-/*//`, comparison operators, and `.a./.o./.n.` when no parentheses are used. Not directly observable from the 7 SRC files (they use explicit parens or single-operator expressions).
