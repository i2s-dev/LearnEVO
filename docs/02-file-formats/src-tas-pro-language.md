# `.SRC` — TAS Professional 4GL Source

Status: draft. Based on the seven `.SRC` files present on the deployment
share (`BKAWLB`, `BKDCA`, `BKLME`, `BKMRF`, `BKROA`, `Bkaph`, `Bkapha`) —
copies in `../../samples/src/`.

## What the format is

Plaintext ASCII. Lines terminated CR+LF. No BOM. Indented with spaces.
Case-insensitive for keywords; identifiers appear mixed-case but are
traditionally lowercase/uppercase in ways that don't matter to the compiler.

Comments: `;` to end of line. Block comments are not used; multiple `;`
lines are the convention.

## Top-of-file directives (compiler pragmas)

Observed in `samples/src/BKAWLB.SRC`:1–10:

```
;BKAWLB.src
;Cvtd from TAS-Pro 3.0 edt to 5.0 src on 01/18/96 at 12:27 p
;
;#PRO3 ;this tells the compiler this is a Pro 3.0 program
#UDX  ;allow both UDFs and UDCs in this program
#LIB LOOKUPS   ;access the DBA Routines library
#LIB windows
#LIB DBA   ;access the dba Routines library
#INC HELPSCRN
SETUP_COLOR   ;use the color values in TASCOLOR.OVL
```

| Directive       | Meaning |
| --------------- | ------- |
| `#PRO3`         | Target the Pro-3 compiler dialect (rare — commented out here). |
| `#UDX`          | Allow both **U**ser-**D**efined **F**unctions and **C**ommands. |
| `#LIB <name>`   | Link against a named library (e.g. `LOOKUPS`, `windows`, `DBA`). |
| `#INC <name>`   | Source-level include (e.g. `HELPSCRN`). |
| `SETUP_COLOR`   | Macro/command from `TASCOLOR.OVL` — loads color constants. |

## Language constructs observed

### Variable declaration — `define`

```
define PRT_WHR     type A  size 1
define PAGE        type i  size 5
define SELECT_FROM1 type d size 8
define SORT_BY_TEXT type A size 11
define MENU_HLDR   type A  size 22 array 7
define inc.all.class, inc.blank.class type a size 1
define inc.class   type a size 1 array 6
```

**Types** (case-insensitive):
- `A` — alphanumeric (fixed-length string).
- `i` — integer (size = number of digits).
- `n` — numeric (decimal; see `size 6` + implicit decimals).
- `d` — date.
- `t` — time.

Identifiers commonly use `.` as a word separator (`inc.all.class`) — dots
are legal in names, a holdover from dBase/Clipper tradition.

Arrays: `array N` — 1-based, fixed size.

### Parameters — `param`

```
param cfrom, prg.name
```
List of variables (already `define`d above) that receive the calling
program's arguments.

### Database I/O

From `BKAWLB.SRC`:75–82:
```
open BKARCUST lock N
open BKICMSTR lock N
open MTICMSTR lock N
open WORKORD lock N
open BKSYMSTR lock N
find F srch BKSY.ARINV.NUM nlock
clr BKSYMSTR rec
```
- `open <table> lock N` — open a data table with `N` = no-lock (shared read).
- `find F srch <key>` — find first record matching key `<key>`. `nlock` = no lock.
- `clr <table> rec` — clear the record buffer for the table.
- Table-qualified field access: `bksy.comp.name` — fields are prefixed by
  a 4-letter table abbreviation (`BKSY` = BKSYMSTR).

### UI — screen mount and `enter`

```
mount SELECT2 type S
prg_hdr "LW-J-B  Print Work Order Schedule"

START:
    xtrap chg ignr
    fnc_list '','Esc Exit'
    MENU_HLDR[1]=" 1 - Start Date  01011"
    MENU_HLDR[2]=" 2 - Finish Date 01022"
    ...
    menu at 5,5 len 9 wdt 19 fld MENU_HLDR cntr SORT_BY nch 7 mcw 17 esc EXIT2 ttl "Sort by"
```

- `mount <screen> type S` — mount a screen layout (`.SCR`/`.DFM`-like).
- `prg_hdr` — set the program header (title bar line).
- Labels like `START:` are goto targets.
- `xtrap` / `fnc_list` set keyboard traps and the bottom-of-screen hint.
- `menu at R,C len L wdt W fld <arr> cntr <var> nch N ttl "title"` —
  pop-up selection menu bound to an array.

### `enter` fields and pre/post hooks

`enter` binds a screen field to a variable. Full syntax:

```
enter <variable> [option ...]
```

**Complete option set** (confirmed from all 7 SRC files, Pass 108):

| Option | Syntax example | Meaning |
|--------|---------------|---------|
| `mask <pattern>` | `mask 'YN'`, `mask "ASPJWIQOC"` | Input mask: only characters present in the pattern string are accepted. A space `' '` in the mask means "any character allowed in that position." |
| `up` | `up` | Auto-uppercase: convert all input to uppercase. |
| `acr` | `acr` | Auto-carriage-return: advance to next field automatically when the field is full. |
| `pre <expr>` | `pre pre.stat()`, `pre bkys.yn[59]='Y'` | Pre-entry hook. Accepts either a function call or a bare boolean expression. If the result is `.f.`, the field is **skipped** (cursor moves past it). |
| `post <func()>` | `post post.incall()` | Post-entry hook: function called after the user confirms their input. Returning `.f.` rejects the entry and keeps the cursor on the field. |
| `vld <expr>` | `vld select_thru1>=select_from1`, `vld chk.part()` | Validation: the expression (or function return) must be `.t.` for the input to commit. |
| `vldm <message>` | `vldm 'Thru cannot be < From'` | Error message displayed when `vld` fails. If omitted, no message is shown (cursor just bounces back). |
| `dflt <value>` | `dflt 1`, `dflt select_from1` | Default value: pre-fills the field when it is empty. Can be a literal or another variable's current value. |
| `upar <label>` | `upar START` | Up-arrow destination: pressing the up-arrow key jumps to this program label. |
| `at <row>,<col>` | `at 18,1` | Screen position: overrides the screen-layout coordinates for this field. |
| `help <label>` | `help HELP.TYPE` | Context-sensitive help: pressing F1 transfers control to this gosub label instead of the default help handler. |
| `noclickoff` | `noclickoff` | Prevents mouse clicks from moving the cursor away from this field. Standard in T7-era EVO programs. |

**Notes:**
- `pre` and `vld` both accept either a function call or an inline expression — there is no separate syntax for each form.
- `vldm` is only meaningful when a `vld` option is present on the same `enter` statement.
- `mask`, `up`, `acr`, `dflt`, `upar`, `at`, `help`, `noclickoff` are all independent; any subset may be combined in any order.
- `noclickoff` appears on almost every field in T7 programs — it is the EVO standard to prevent accidental mouse-click navigation in character-based screens.

**Inline function blocks** follow the `enter` statement(s) that reference them:

```tas
enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
{
  func pre.stat
    trap F1 GOSUB SHOWHELP
    trap ESC goto EXIT2
    fnc_list 'F1 Help','Esc Exit'
    ret .t.
}
```

`ret .t.` — allow entry. `ret .f.` — abort / skip. `ret` alone — return from subroutine.

### Control flow

- `if cond ... [else ...] endif`
- `for(var;start;end;step) ... next`
- `goto <label>` / `gosub <label>` / `return` (from gosub).
- `trap <key> goto <label>` — keyboard trap.
- `trap <key> gosub <label>` — keyboard trap with subroutine call.
- `trap <key> dflt` — revert key to default behavior.

## Naming convention for `.SRC` files

- **`BK*`** — older Book-keeping / backbone modules from the TAS-Pro 3→5
  conversion era. Example: `BKARCUST` table is the AR customer master.
- **`T6*`** — TAS Pro 6 generation (mostly `.RUN`, not `.SRC`).
- **`T7*`** — TAS Pro 7 generation (mostly `.RWN` + `.DFM`).

Module letter codes in the middle of the name:
- `AR` — Accounts Receivable
- `AP` — Accounts Payable
- `IN` — Inventory
- `SO` — Sales Order
- `PO` — Purchase Order
- `WO` — Work Order (labor/job)
- `GL` — General Ledger
- `LW` / `LA` — Labor (legacy prefixes; LW merged into AW in 2000 per
  comment in `BKAWLB.SRC`:14–16)

## Authoritative keyword list (from the runtime itself)

`tp7runtime.exe` embeds the full compiler/IDE, so its string table
**is** the language reference. Extract is in
`../../samples/rwn/tp7runtime.keywords.txt`. Headline items:

### Compiler pragmas observed in the runtime
`#TDATA` (set total data segment size) · `#ADD_FLDS` · `#WINFORM` (this
program has a Windows form — compile-time pragma; maps to `@Specline@mount_winform`
internally; **not found in any of the 2,575 EVO program string dumps**: all T7
programs in this installation are natively Windows-form already, so `#WINFORM` is
only needed when upgrading a T5/T6 text-mode program to T7 Windows mode) ·
`#WINREPORT` · `#FORMSENCRYPTED` (form file is encrypted) · `#FORCERWN` (must
run as RWN, not RUN) · `#MAINMENU` · `#ALL_LOC` · `#DONTCOMPILE` ·
`#UDX`, `#LIB`, `#INC`, `#PRO3`, `#TDATA`.

### Control flow keywords
`if` / `else` / `else_if` / `endif`
`for (v; start; end; step) ... next` · `while ... loop_if ... exit_if`
`select ... otherwise ... endselect`
`floop_if` / `fexit_if` / `sloop_if` / `sexit_if` (loop/exit within
`for` and `select`).
`ret`, `return`, `goto`, `gosub`, `gosubl`, `chain`, `chainr`, `quit`.

### Field (variable) types
From the compiler's own error message (`7621`): "Field type must be
one of: **I, B, R, P, T, D, N, L, A, F**".

| Code | Type |
| ---- | ---- |
| `A` | Alpha (fixed-length string) |
| `N` | Numeric (decimal; `dec` sets fraction digits) |
| `I` | Integer (max 10 digits) |
| `B` | Byte (1–3 chars; errmsg.dbf error 614 confirmed) |
| `R` | Record position / pointer into a file (errmsg.dbf confirmed) |
| `P` | Pointer — memory/file pointer (errmsg.dbf error 614 confirmed) |
| `T` | Time |
| `D` | Date |
| `L` | Logical (boolean) |
| `F` | File handle / float (to verify) |

Arrays: `array <N>`, 1-based. Decimal precision: `dec <n>` after `size`.

### Input-statement grammar — verbatim from the runtime

```
CLRLNE |(*AT col,row*) (*NCHR f/c/e*) (*NOCOLOR*) (*COLOR f/c/e*) (*ABS*)

DEL    |(*file_name/@filenum*) (*NOCNF*) (*GOTO lbl*) (*ERR lbl/NO_ERR*)

DALL   |(*filename/@filenum*) (*KEY keyname/@keynum*) (*START f/c/e*)
       (*SCOPE arfn f/c/e*) (*FOR f/c/e*) (*WHILE f/c/e*)
       (*CNTR fn/v*) (*DISP*)
       # Confirmed TAS Pro 7 keyword (tp7runtime.keywords.txt). Conditional batch-delete:
       # KEY=filter by key range, SCOPE=scope array function, FOR/WHILE=predicates,
       # CNTR=progress counter variable, DISP=display progress. More powerful than DEL.

ENTER  |(*field_name*) (*MASK f/c/e*) (*HELP lbl/@udf*) (*UPAR lbl*)
       (*UP*) (*ACR*) (*PSWD*) (*AT col;row*) (*NOREV*) (*COLOR f/c/e*)
       (*PRE udf*) (*POST udf*) (*DFLT f/c/e*) (*VLD udf*) (*VLDM f/c/e*)
       (*DO udf*) (*ARRAY*) (*CNTR fn/v*)
       (*ENUM f/c/e1,f/c/e2,...,f/c/ex*) (*AUTO_SRCH*)
       (*GROUP f/c/e*) (*NOCLICKOFF*) (*NOCLICKON*)
```

Notation: `f/c/e` = field-or-constant-or-expression. `|` marks the
position where the required argument list begins. `(*...*)` = optional.

### Reporting keywords

The runtime has first-class support for a report pipeline:
- Region-based (legacy): `INIT_REGION`, `MARK_REGION`, `REGIONSOFF`,
  `NO_PRINT_FLD`, `SETUP_REPORT_BUFF`, `OUTPUT_REPORT_DATA`,
  `UPDATE_REPORT_DATA`, `PRINT_REPORT`.
- ReportBuilder-based: `EXEC_RB`, `RTM_FN`, `REPORTNAME`, `USE_PRINTER`,
  `PRINT_TO_FILE`, `NOPRINTWHRDIALOG`, `PRINT_CANCEL`, `PRINT_ARCHIVE`.

### Windowing / form keywords

`WMOUNT`, `LOAD_FORM`, `LOAD_MODAL_FORM`, `RELEASE_FORM`,
`ACTIVATE_FORM`, `REFRESHFORM`, `SET_FOCUS`, `SET_OBJECT`,
`SET_OBJ_PROP`, `GET_OBJ_PROP`, `ENABLE_ALL`, `DISABLE_ALL`,
`DATA_GRID` (bind a `TASDataGrid`), `NAVIGATOR` (bind a
`TASNavigator`), `COMBO_ITEM`.

### Data-engine keywords

`USECODEBASE` (opcode 7975 — switch the active data engine from Btrieve to CodeBase
DBF; **not used in any of the 2,575 EVO programs in this installation** — EVO is
Btrieve-only; CodeBase support is a latent TAS Pro capability unused here),
`BTRIEVE_VERSION`, `PERVASIVE_SERVER`, `LOCK_OWNER` (opcode 8032 — returns username of current record owner),
`CREATE_DBF`, `CONVERT_TO_DBF`, `RESTRUCTURE_DBF`, `PACK_DBF`,
`REINDEX_DBF` (opcode 7986 — rebuild CodeBase DBF index; function syntax:
`REINDEX_DBF()`; runtime error if called on a non-CodeBase (Btrieve) file: "You
cannot use the REINDEX_DBF() function for non-CodeBase files."; **not the same
as UT-C which rebuilds Btrieve B-tree indices via T7REINDEX.RWN**),
`REC_LOCK` (opcode 7992 — acquire exclusive record lock), `UNLOCK` (opcode 7813),
`DUPCHECK`, `IFDUPCB`, `DELETED`, `CBDELETED`.

**UT-C Re-Index** (T7REINDEX.RWN — Btrieve B-tree rebuild utility): invoked from
the System Manager menu when Btrieve Status 2 errors or corrupted key structures
occur. T7REINDEX.DFM type=TShellExe (wraps an external shell executable for the
Btrieve API rebuild). **WARNING (from EvoHELP):** do not reindex while other users
are on the system; back up the file first. This is completely separate from
`REINDEX_DBF()` which is CodeBase-only.

#### Transaction model — no BEGIN/COMMIT/ROLLBACK

TAS Pro 7 has **no explicit transaction keywords**. `BEGIN_TRAN`, `COMMIT`, and
`ROLLBACK` do not exist in the runtime. The entire keyword list (187 entries in
`tp7runtime.keywords.txt`) contains only three data-consistency keywords:
`REC_LOCK`, `UNLOCK`, `LOCK_OWNER`. Data integrity is handled by:

1. **Btrieve record-level locking** — `open TABLE lock R` (exclusive open) or
   `find G nlock` (shared read); Btrieve's native optimistic/pessimistic concurrency.
2. **Application-level sequencing** — programs save/write records one at a time in
   dependency order; no atomic multi-table writes.
3. **No rollback** — if a multi-step write fails midway, the program must explicitly
   reverse any prior writes. EVO programs handle this with conditional `del` + `save`
   sequences, not a transaction log.

This is the inherited Btrieve model: each Btrieve record operation (save/delete) is
its own atomic unit. Multi-record operations are not atomic at the database layer.

#### WHOAMI — workstation identity (opcode 7965)

`WHOAMI` is a **built-in TAS Pro 7 keyword** (not a Btrieve table). It reads/writes
the workstation identity file `C:\ISTS\WHOAMI.DBA`. Zero programs in the 1,122-RWN
corpus open a Btrieve table named `WHOAMI` — all workstation-identity access goes
through the keyword.

Key behaviors confirmed:
- `WHOAMI` variable holds the current workstation/user identity string.
- `WHOAMIFULL` — extended identity (full name or domain\user form).
- `WHOAMI.EXTRA` — additional workstation metadata field (used in J7* custom programs).
- `REWHOAMI` / `REWHOAMIFULL` — re-read the identity (refresh from WHOAMI.DBA).
- 161 programs reference `WHOAMI` as a named variable; EVOERPMENU + suwin6t are
  the primary identity-consumers (session init + screen-lock guard).
- `WHOAMI.DBA` at `C:\ISTS\` is 2 bytes (0x0D 0x0A = empty/reset) when no session
  is active. The runtime writes the active identity on login and clears it on logout.

### Integration / system keywords

`OLECALL` (COM/OLE), `SQLCALL`, `MYSQL_QUERY`, `GET_WEBSOURCE` (HTTP
fetch), `LOAD_DLL` / `REMOVE_DLL`, `GET_IP`, `GET_UNC_PATH`,
`GET_SERVER_DATETIME`, `SENDKEYS`, `APPACTIVATE`, `REGEDIT`,
`ISREMOTESESSION`, `QRCODE`, `EXPORTGRID`, `COPYTOCLIPBOARD`,
`ENCRYPTSTR` / `DECRYPTSTR`, `COMPILE_EXPR`, `COMPILE_SRC` (run-time
eval/compile), `EXEC_TOP_WAIT` (shell-exec and wait), `PLAYWAV`.

This is a very well-rounded 4GL — it has Windows API, COM, HTTP,
SQL, and on-the-fly code compilation.

#### OLECALL — COM/OLE automation (opcode 8013)

Invokes a COM/OLE object method or property. Used by EvoERP for **Excel data export**:
4 programs confirmed as callers via `EXCELCONN`/`EXCELCON` variable (connection handle):

| Program | Module | Purpose |
|---------|--------|---------|
| `T7JCE.RWN` | JC — Job Cost Efficiency | Export WO cost data to Excel |
| `T7SON.RWN` | SO-N — RMA / special orders | Export SO/RMA data to Excel |
| `T7WOLA.RWN` | WO-LA — WO Schedule list | Export WO schedule to Excel |
| `T7WOLD.RWN` | WO-LD — WO Detail list | Export WO detail to Excel |

`SENDKEYS` (opcode 8019) + `APPACTIVATE` (opcode 8020) are companion keywords used to
activate the Excel window and send keystrokes to it. Exact parameter form (object
dispatch syntax) cannot be confirmed without decrypted bytecode.

Note: `COM.LINE`, `COM.SLSP` etc. in other programs mean *commission*, not COM objects.

#### SQLCALL / MYSQL_QUERY — SQL execution (opcodes 8018 / 8023)

`SQLCALL` (generic SQL) and `MYSQL_QUERY` (MySQL-specific variant) execute external
SQL queries. Primary caller: `T7jsql.RWN` (52 procs, 216 KB, EVO.LIB) — the Java SQL
bridge. Key variables:

- `HOST` / `PORT` / `NAME` — Java server connection target
- `JAVA.PATH` / `JAVA.NAME` — path to EvoPVT JAR
- `TREEDEST` — query result destination
- `DICT_HNDL` / `KEY_HNDL` / `LOC_HNDL` — DDF file handles (for schema generation pass)

`QUERYEXECUTE.RWN` (26 procs, ISTECH.LIB) uses the same HOST/PORT/NAME/JAVA.PATH pattern
= second Java-bridge SQL executor (the interactive query launcher from the QU module).

#### GET_WEBSOURCE — HTTP fetch (confirmed caller: T7GETWEB.RWN)

`T7GETWEB.RWN` (7.5 KB, 6 procs, source `t7getweb.SRC`) is the primary GET_WEBSOURCE
caller. Opens `BKARDEP` (AR deposits) + `BKARINVT` (AR transactions) + item/customer
tables. Two web-fetch actions (`BTNGETWEB.CLICK` + `BTNGETWEB2.CLICK`). The URL
parameters are string literals embedded in the bytecode (not named variables). Purpose:
**web payment gateway sync** — polls payment processor for AR deposit confirmations.

#### EXEC_TOP_WAIT — shell execute with wait (opcode 8051)

Launches an external executable and blocks TAS Pro until it exits. Used by the EvoUpdate
pipeline (`EvoERPupd.RWN` → `EVOUPDATE.RWN`) to run `UPDTP7.EXE` (schema patch runner)
as part of the version-upgrade flow. Also used for `LAUNCH.ESA` in `T7SOA.RWN` (launches
`T7PSEA.RWN`, the tech-support FTP upload utility).

#### PLAYWAV — audio playback (opcode 7755)

Plays a PCM WAV file. `EVO.CFG.SOUNDS` (checked in 926 programs) is the global
enable/disable flag — most programs check it before any sound playback. Key indicators:

- `DINGED.ONCE` in `autoT7POJC.RWN` = anti-replay flag (sound plays once per event on
  PO quality-control receiving threshold notification)
- `MSGSOUND` (opcode 7879) = simpler system-beep variant (no WAV file needed)
- `KDWaveEditor` VCL component registered in `tp7runtime.exe` = runtime audio recording/editing
  capability (for customizing alert sounds)

The WAV file paths are string literals in the bytecode, not named variables — specific
filenames cannot be confirmed without bytecode disassembly.

## Additional language constructs — from BKROA, BKMRF, BKDCA analysis

### Comment styles

Two comment forms are accepted:
- `;` — semicolon to end-of-line (most common)
- `&&` — double-ampersand to end-of-line (seen in BKMRF.SRC; also used for commented-out section labels `&& OPEN_FILES:`)

### Arithmetic and relational operators

All confirmed from BKMRF.SRC and BKROA.SRC:

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Add / string concat | `MRP.QTY = BKAR.INVL.PQTY + BKAR.INVL.UBO` |
| `-` | Subtract / negate | `MRP.QTY = MTWO.WIP.SQTY - MTWO.WIP.COMQTY` |
| `*` | Multiply / string concat | `MTMRP.QTY = MTMRP.QTY * -1.00` / `str(a)*"-"*str(b)` |
| `/` | Divide | `MTRO.PROC.PERHR = 3600.00 / temp.secs` |
| `=` | Equal | `if mtic.prod.code <> bkap.pol.pcode` |
| `<>` | Not equal | `vld inc.forecast<>""` |
| `>` | Greater than | `if MRP.QTY>0` |
| `<` | Less than | `if MRP.QTY<0` |
| `>=` | Greater or equal | (inferred; `<=` confirmed) |
| `<=` | Less or equal | `if MRP.QTY<=0` |
| `.a.` | Logical AND | `if bkap.pol.pqty = 0 .a. bkap.pol.qc.qty = 0` |
| `.o.` | Logical OR | `if MTIC.PROD.MRP="Y" .o. mtic.prod.code=''` |
| `.n.` | Logical NOT | `if .n. windows()` |
| `$` | In-set / contains | `if MTWO.WIP.STATUS $ "CXI"` — true if char is in string |

String concatenation uses both `*` and `+` — both work, `*` is the traditional form.

Empty string literal: `""` (double-quote pair). The result of a `just()` / `str()` call can be assigned back and compared to `""`.

### Full variable types

From compiler error 7621 (`Field type must be one of: I, B, R, P, T, D, N, L, A, F`) plus observed types in source:

| Code | Type | Notes |
|------|------|-------|
| `A` | Alpha (string) | Fixed length. `size N` sets length. |
| `N` | Numeric | Decimal. `dec N` sets fraction digits. |
| `I` | Integer | Up to 10 digits. |
| `B` | Byte | Single-byte value; rarely used. |
| `R` | Record position | Stores a record's key / position in a Btrieve file. Size 8 or 10. |
| `P` | Pointer | Memory pointer; use unclear from source. |
| `T` | Time | 8-char `HH:MM:SS` time value. |
| `D` | Date | 8-char `YYYYMMDD` date value. |
| `L` | Logical (boolean) | `.t.` / `.f.` literals; no size needed. |
| `F` | Float / file | Unconfirmed from source. |
| `V` | Variant | Observed in BKDCA.SRC: `define t.wokey type V size 10` — may hold mixed types or a composite key. |
| `O` | Object/flag | Observed in BKDCA.SRC: `define POST.FAIL type o size 1` — purpose unclear; possibly an internal object handle. |

### Additional database I/O patterns

**Find modes** (confirmed by multiple SRC files):

| Mode | Meaning |
|------|---------|
| `find F` | First record (by current index) |
| `find N` | Next record |
| `find G` | Greater-or-equal — first record with key >= specified key |
| `find M` | Match — exact key match (returns first matching record) |
| `find L` | Last record |
| `find P` | Previous record |

Modifiers appended to `find`:
- `err <label>` — jump to label if no record found
- `nlock` — do not acquire a lock on the found record
- `noclr` — do not clear the record buffer before filling it

**`open` lock modes:**
- `lock N` — no lock (shared read, multiple readers)
- `lock R` — read lock (exclusive read; prevents others from writing)

**`openv` — open by variable:**
```
openv "BKDCPLAB" fnum dcplab lock R
```
Opens a file by string name. `fnum var` assigns the file handle number to variable `var`.
Then later use `@var` to reference the file by handle: `save @dcplab nocnf`.

**`setact TABLE file ALIAS`** — redirect a logical table to a physical file:
```
setact ROUTING file BKRTEMTR   ;use BKRTEMTR as the physical file for ROUTING
setact routing file routing    ;restore ROUTING to its normal physical file
```

**`casinit`** — initialize / (re-)create a data file:
```
casinit file, .t., 'B'*co()
```
Creates/clears the file named in `file`. Second arg `.t.` = confirm. Third arg is the filename prefix. `co()` returns the 2-char company code.

**`rcn TABLE rcn var get/set`** — save and restore a record position (record cursor):
```
rcn ROUTING rcn TEMP.REC get   ;save current record position of ROUTING into TEMP.REC
rcn ROUTING rcn TEMP.REC set   ;restore ROUTING cursor to position saved in TEMP.REC
```
`TEMP.REC` must be of type `R` (record position).

**`clr TABLE buff`** vs **`clr TABLE rec`** vs **`clr TABLE`**:
- `clr TABLE buff` — clear the full record buffer (all fields to empty/0)
- `clr TABLE rec` — clear current record only
- `clr TABLE` (no modifier) — same as `buff` in practice

**`updta array clr`** — clear all elements of an array to zero:
```
updta LINE.OPER clr
updta HOLD.SEQ, HOLD.OP, HOLD.DESC clr   ;clear multiple arrays
```

**`ifna TABLE ... [endif]`** — if-not-available block: executes if the last `find` for TABLE found no record:
```
ifna BKICMSTR
   ret              ;bail out if lookup failed
endif
```
The `endif` is optional for a single-statement body — `ifna X ret` works inline.

**`scan @handle key <field> ... ends`** — scan loop (seen commented out in BKDCA.SRC):
```
scan @dcPlab key lab.emp
  ;process each record
ends
```
Iterates all records in a file ordered by a key.

### `while / endw` loop

```
while <condition>
   ;body
   exit          ;break out of while loop
endw
```
Also `while .t.` for infinite loops (use `exit` to break). `exit` exits the innermost `while` loop.

### Additional control-flow keywords

- `else_if <condition>` — chained if (confirmed in BKROA.SRC `else_if MTWC.OUTPROC="W"`)
- `fexit_if <condition>` — exit the current `for()` loop if condition is true
- `fexit` — exit the current `for()` loop unconditionally (BKDCA.SRC)
- `exit` — exit from a `while` loop (confirmed in multiple places)
- `trap <key1>,<key2> goto/gosub <label>` — trap multiple keys in one statement
- `trap <key> dflt` — restore key to default behavior (cancel trap)
- `trap <key> ignr` — ignore key (no action)
- `trap <key> goto <label>` and `trap <key> gosub <label>` (confirmed)

### Built-in functions

Confirmed from source analysis across all 7 SRC files:

| Function | Returns | Example |
|----------|---------|---------|
| `windows()` | L | True if running under Windows (not DOS) |
| `clicked_on()` | L | True if this field was activated by mouse click |
| `zask(msg, default)` | L | Modal yes/no dialog; returns `.t.`/`.f.` |
| `iif(cond, a, b)` | any | Inline conditional: if cond then a else b |
| `loc(str, sub)` | I | Position of `sub` in `str`; 0 if not found |
| `just(str, dir)` | A | Justify string; dir `'L'`=left-trim, `'R'`=right-trim |
| `str(val)` | A | Convert numeric/date to string |
| `str(val, width, dec)` | A | Convert with explicit width and decimals |
| `trim(str, side)` | A | Trim spaces; `'L'`=left, `'R'`=right |
| `mid(str, start, len)` | A | Substring: `mid(mtro.operdesc,1,20)` |
| `chr(n)` | A | Character with ASCII code n: `chr(33)` = `!` |
| `round(val, dec)` | N | Round to `dec` decimal places |
| `ttof(time)` | N | Time-to-float: convert time to fractional seconds |
| `ftot(n)` | T | Float-to-time: convert fractional seconds to time |
| `flerr(handle)` | I | File error code for file handle; 0 = success, non-0 = error |
| `fnum(name)` | I | File handle number for a table name: `fnum('bkarinvl')` |
| `co()` | A | Returns current 2-char company code |
| `max_cols()` | I | Returns max screen columns |
| `etyp()` | A | Entry type: `'C'` = change, other values for add/delete |
| `dpath()` | A | Returns default data path |

### Screen and UI commands

**`pmsg`** — print message to screen (no wait):
```
pmsg 'Text ' at col,row nocr         ;print at row/col, no carriage return
pmsg value at col,row nocr           ;print a variable value
pmsg 'A',ccr(),'B',ccf() at 1,1 nocr ;ccr() = color-reverse start, ccf() = color-forward (end)
pmsg value at col,row ptw S          ;print into window S
```

**`msg`** — display a message (pauses for keypress or `nowait`):
```
msg 'Text' nowait                    ;display without waiting
msg 'Text' windows 'w'              ;Windows message box, warning style
msg 'Text' windows 'info'           ;Windows info box
```

**`window`** — create a pop-up window:
```
window at row,col len height wdt width box 's'
window at row,col len h wdt w box 's' shd 'r' scolor N bcolor N wcolor N ttl 'title' ttlw 'l'
```
`shd 'r'` = shadow right; `scolor`/`bcolor`/`wcolor` = shadow/border/window color index; `ttlw 'l'` = title align left.

**`pbox`** — draw a box:
```
pbox s at row,col len height wdt width
```

**`bell`** — sound a bell (beep).

**`clrscr`** — clear the entire screen.

**`redsp`** — redisplay (refresh) current screen.

**`rscr`** — restore screen to previous saved state.

**`saves`** — save current screen state (push onto screen stack).

**`picture remove`** — remove all graphical pictures/icons from screen.

**`setline var with 'part1','part2',...`** — concatenate string literals into a variable:
```
setline op_title1 with 'Order',' ',' Op',' ','Description'
```

**`listf`** — browse/list data from a Btrieve file:
```
listf field1,field2,...
      start key1,key2!
      while condition
      key KEYNAME
      file TABLENAME
      noadd noshift
      fline title1,title2
      cbf ' '
```
`start` = starting key values; `!` terminates multi-part key. `noadd` = no inserting new records. `noshift` = no column shifting. `fline` = header line(s). `cbf` = column blank fill char.

**`listm`** — browse/list in-memory arrays:
```
listm field1,' ',field2,... actv N maxa M cntr var ccolor CC NOSHIFT noadd ENTER func() use_traps fline t1,t2 blnes N
```
`actv N` = N active (used) rows. `maxa M` = M maximum rows. `cntr var` = cursor position variable. `ENTER func()` = callback when Enter pressed. `blnes N` = blank lines after header.

**`sorta`** — sort parallel arrays:
```
sorta hold.seq[seq.cntr] move hold.seq[seq.cntr],hold.op[seq.cntr],hold.desc[seq.cntr] num op.max cntr seq.cntr
```
Sort array by `hold.seq`, moving `hold.op` and `hold.desc` in parallel. `num` = total elements. `cntr` = result count variable.

**`RDLIST`** — redisplay the current `listm`/`listf` widget.

**`equ_mid`** — extract a substring from an array element:
```
equ_mid OK fld MESSAGE[MCNTR4] start 2 nchr 1
```
Sets `OK` = 1 character from `MESSAGE[MCNTR4]` starting at position 2.

**`scrn L`** / **`scrn r`** — save (`L`) / restore (`r`) screen (alternative to `saves`/`rscr`; `L` may mean "lock", `r` = restore).

**`scrn r` at line context:** also used after `mount` to re-display fields.

**`prg_hdr "title"`** — set the program title bar text (also `PRG_HDR`; case-insensitive).

### Keyboard trap special keys

Beyond letter keys and function keys, traps confirmed for:
- `ESC` — Escape
- `HOME`, `END` — Home, End
- `F1`..`F10` — Function keys
- `PG_DN`, `PG_UP` — Page Down/Up
- `INT` — Interrupt signal
- `L_EXIT` — a custom-defined exit event (seen in BKDCA.SRC)
- `CHG` — change event (field value changed): `xtrap chg ignr` = ignore change events

**`xtrap_si_udc` / `xtrap_rstr_udc`** — save and restore all UDC (User Defined Command) trap state. Call before overriding traps in a modal sub-screen; restore on return.

**`xtrap chg ignr`** — suppress the "change" event.

### T7 key trapping via DFM properties

In TAS Pro 7 `.RWN` programs, key trapping is **not** done through a standalone `trap`
keyword. Instead, it is configured through DFM form properties:

| Property | Opcode | Purpose |
|----------|--------|---------|
| `KeyTraps` | 8091 | List of key-trap definitions for the form |
| `KeyTrapHint` | 8092 | Status-bar hint text to display for each trap |

This is confirmed from `tp7runtime.keywords.txt` — `KeyTraps` and `KeyTrapHint` are
registered as DFM section property names (under `# Entry / object properties (DFM)`).
The TAS6 `trap <key> gosub/goto` runtime keyword exists in `.RUN` (TAS6) programs;
in T7 the equivalent binding is declared in the `.DFM` at design time. The `KeyTraps`
property controls which keys activate programmatic callbacks from within a T7 form.

### MAGLIB — graphical button library

The `#lib maglib` include provides push-button icons for Windows:
```
mag_start                           ;initialize maglib
zret = magbutton(col, row, id, state)  ;draw/update button id at col,row; state 0=up, 1=pressed
picture remove                      ;remove all buttons/images
```
Called in `pre` hooks with `state=1` and in `post` hooks with `state=0` to simulate button press visual feedback.

### Extended types V and O (Pass 106i)

Two types not listed in compiler error 7621 appear in `BKDCA.SRC`:

| Code | Observed name | Usage | Interpretation |
|------|--------------|-------|----------------|
| `V` | `t.wokey` | Holds `lab.wokey` temporarily; also assigned `= 0` (numeric clear) | **Variant** — general-purpose holder that accepts any type. Acts as a typed buffer for composite or mixed-type keys. |
| `O` | `POST.FAIL`, `POST.OTHER`, `MONTH` | Defined but never used in BKDCA.SRC | **Overpunch / legacy numeric** — possibly a packed sign-byte numeric type from older TAS versions. Dead code in this file; may be used in older BK-era programs. |

Type `V` confirmed active (assigned and read at lines 627/645/770 of BKDCA.SRC).
Type `O` confirmed declared but unused in the one SRC file where it appears.

### `find R` — confirmed absent

No `find R` statement was found in any of the 7 SRC files. `lock R` (read-lock on open)
is confirmed. The `find` modes in use are: F, N, G, M, L, P only.
Type `R` variable usage is exclusively with the `rcn` (record cursor) statement, not `find`.

### Print / reporting commands (Pass 393 — from BKAPH.SRC)

Confirmed from `BKAPH.SRC` and `BKAPHA.SRC` (AP check printing — TAS Pro 5/6 era):

- **`format VALUE recv ALPHAVAR NOCMA NOFD`** — convert a number to formatted alpha text.
  `NOCMA` = suppress thousands commas; `NOFD` = suppress fractional digits. Used to render
  check amounts as words (e.g., `format TOT.RAMT recv DOLLAR.ALPHA NOCMA NOFD` → "00123 45").
- **`pfmt N`** — select print format slot N (sets column layout / line spacing for the printer).
- **`pvert N`** — advance N lines on the printer.
- **`ptof`** — advance to top-of-form (form feed to next physical check/page).
- **`pchr 'CMD'`** — emit a printer control sequence by name (`'pcmp'`=form advance, `'preg'`=regular-print resume).
- **`pset wdt N`** — set print width to N characters.
- **`pset wdt N tlnes T plnes P`** — full page setup: width N, total lines T per page, print lines P (body lines per page).
- **`pon S`** — redirect print output to screen (`S` = screen).
- **`RTM_VALID`** — validate the current RTM filename before printing (checks file exists and is readable). Must be called after setting `rtm_name` and before `setup_print_buff`/`exec_rb`.
- **`setup_print_buff pb_num N fldlst 'field1','field2',... [link_to M]`** — define print buffer N with named field list. `link_to M` attaches this buffer as a child/detail of buffer M (sub-report nesting). Field names use underscore separators matching DDF names (e.g., `'bkap_chk_invnum'`). This is the TAS Pro 5/6 name for what later became `SETUP_REPORT_BUFF`.
- **`output_print_data pb_num N fldlst var1,var2,...`** — emit a row of data to print buffer N. Values are program variables (no quotes), matched positionally to the `setup_print_buff` field list. TAS Pro 5/6 name for `OUTPUT_REPORT_DATA`.
- **`print_cancel()`** — built-in function that returns `.t.` if the user cancelled the print dialog. Call after RTM setup and before the main print loop.

### File open modes — `lock f` (Pass 393)

TAS Pro supports a **full file lock** mode in addition to record-level locking:
```
open BKAPCHKF lock f err LABEL
```
`lock f` = exclusive file-level lock. Prevents any other process from opening the file at
all while the lock is held. Used in AP check printing to prevent concurrent AP-E/F/G/H
sessions from corrupting the BKAPCHKF staging file. Must be opened with `err LABEL` to
handle the case where another session holds the lock.

### Multi-currency built-in functions (Pass 393 — from BKAPH.SRC)

Confirmed from BKAPH.SRC multi-currency sections:
- **`isis_get`** — load ISIS multi-currency config into the `isis.*` variable namespace.
  Must be called before any multi-currency operations; populates `isis.multi.curr`,
  `isis.mcf.*`, `isis.mcr.*` etc.
- **`isis_mcrate(DATE, CURCODE)`** — returns the exchange rate for `CURCODE` on `DATE`.
  Used to compute amount conversions for FX gain/loss postings.
- **`is_mc_cvt(FROMCUR, TOCUR, DATE, AMT)`** — converts `AMT` from currency `FROMCUR`
  to `TOCUR` using the rate on `DATE`.
- **`is_curr_ctrl("MODULE", CURCODE)`** — applies multi-currency GL account overrides for
  the named module (e.g., `"AP"`), setting `BKGL.ACCT`/`BKGL.GLDPT` to the multi-currency
  AP GL accounts from ISMCF.
- **`findv M fnum HANDLE key KEY val VALUE`** — seek a record by value in a file opened
  by handle. `findv` variant of `find` for variable-handle files.

### Multi-statement syntax on one line (Pass 393 — from BKAPHA.SRC)

TAS Pro allows multiple assignments on a single line separated by `|`:
```
lnes=0 | tot.amt=0 | tot.damt=0 | tot.ramt=0
```
This is equivalent to four separate assignment statements. Confirmed from BKAPHA.SRC L829.
The `|` separator is distinct from `&&` (comment to end-of-line) and `;` (comment).

### RTM file mapping for AP laser checks (Pass 393 — from BKAPHA.SRC L796-798)

`BKYS.YN[48]` controls which RTM template is used:
| YN[48] | RTM file | Format |
|--------|----------|--------|
| `'1'` | `bkapha1.rtm` | Standard laser check |
| `'4'` | `bkapha2.rtm` | Laser check variant 2 |
| `'5'` | `bkapha3.rtm` | Laser check variant 3 |

## Things still to verify

- How `#INC HELPSCRN` is resolved — `HELPSCRN.INC` or equivalent not found on share.
  Likely an include file in the standard DBA library path.
- What `SETUP_COLOR` expands to — it's a UDC (User Defined Command) from `TASCOLOR.OVL`
  which is not on the share. Sets color constants used by subsequent screen commands.
- Scope rules for variables defined inside `{ }` function blocks — from observation,
  they appear to share the outer scope (e.g., `which` parameter in `func pre.scrn which`
  receives the value from the outer `enter` call, not a local copy).
- Type `O` semantics — only seen as dead-code defines; behavior not observable from these files.
