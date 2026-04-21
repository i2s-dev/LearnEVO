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

```
enter e.status[1] mask 'X ' up acr pre pre.stat() upar START
enter INC.ALL.CLASS mask 'YN' up post post.incall() acr
    {
      func post.incall
        if inc.all.class = 'Y'
           for(mcntr;1;6;1)
             inc.class[mcntr] = ' '
           next
           inc.blank.class = 'Y'
        endif
        ret .t.
    }
```

`enter` defines an input field bound to a variable. Modifiers:
- `mask '...'` — accepted characters.
- `up` — uppercase input.
- `acr` — accept on carriage return.
- `pre <expr>` / `post <expr>` — pre/post hook (inline expression or
  a function call).
- `upar <label>` — up-arrow jumps to label `<label>`.

Inline function definitions live in **`{ ... }` blocks** immediately
after the statement that references them. Syntax:
```
{
  func <name>
    <body...>
    ret <value>
}
```
`ret .t.` returns the literal true (boolean). `.f.` is false — xBase-style
literals.

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
program has a Windows form) · `#WINREPORT` · `#FORMSENCRYPTED` (form
file is encrypted) · `#FORCERWN` (must run as RWN, not RUN) ·
`#MAINMENU` · `#ALL_LOC` · `#DONTCOMPILE` · `#UDX`, `#LIB`, `#INC`,
`#PRO3`, `#TDATA`.

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
| `B` | Byte (single byte; to verify) |
| `R` | Record position / pointer into a file |
| `P` | Pointer (to verify — may be memory pointer) |
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

`USECODEBASE` (switch to the CodeBase DBF engine instead of Btrieve),
`BTRIEVE_VERSION`, `PERVASIVE_SERVER`, `LOCK_OWNER`, `CREATE_DBF`,
`CONVERT_TO_DBF`, `RESTRUCTURE_DBF`, `PACK_DBF`, `REINDEX_DBF`,
`REC_LOCK`, `UNLOCK`, `DUPCHECK`, `IFDUPCB`, `DELETED`, `CBDELETED`.

### Integration / system keywords

`OLECALL` (COM/OLE), `SQLCALL`, `MYSQL_QUERY`, `GET_WEBSOURCE` (HTTP
fetch), `LOAD_DLL` / `REMOVE_DLL`, `GET_IP`, `GET_UNC_PATH`,
`GET_SERVER_DATETIME`, `SENDKEYS`, `APPACTIVATE`, `REGEDIT`,
`ISREMOTESESSION`, `QRCODE`, `EXPORTGRID`, `COPYTOCLIPBOARD`,
`ENCRYPTSTR` / `DECRYPTSTR`, `COMPILE_EXPR`, `COMPILE_SRC` (run-time
eval/compile), `EXEC_TOP_WAIT` (shell-exec and wait), `PLAYWAV`.

This is a very well-rounded 4GL — it has Windows API, COM, HTTP,
SQL, and on-the-fly code compilation.

## Things still to verify

- Full grammar (a formal list of every statement) — accreting.
- Expression operators observed: `.a.` = AND, `.o.` = OR (inferred),
  `.n.` = NOT (inferred), `$` = in-set/contains, `=` `<>` relational.
  Need to confirm from an arithmetic expression.
- How includes (`#INC HELPSCRN`) are resolved — need the `HELPSCRN.INC`
  or equivalent file.
- What `SETUP_COLOR` expands to (`TASCOLOR.OVL` not found on share).
- Scope rules for variables defined inside `{ }` function blocks.
