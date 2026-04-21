# What EvoERP Is, at a Glance

Status: draft.

## One-paragraph summary

**EvoERP** is a manufacturing ERP for small/mid shops. It is the
current incarnation of **DBA Manufacturing** (originally early-90s DOS,
then Windows in the 2000s) produced by a company that — for users of
this software — is now maintained via Computer Keyes / IDE2
("I-System Tech"). The application runs on the **TAS Professional 7**
runtime (`tp7runtime.exe`), an xBase-family 4GL with a Delphi/VCL
Windows UI layer. Reports are rendered by **Nevrona ReportBuilder**.
Data lives in server-side **Btrieve** / **CodeBase DBF** files on
`\\i2s109-solidcrm\DBAMFG$\`.

## Version

`C:\ISTS\DFM\EVO.VER`: `1\t2024.1` — the installed release is **2024.1**.

## Stack layers

```
┌─────────────────────────────────────────────────────────┐
│  User-facing menu + forms                               │
│  EvoERPmenu.rwn, T7*.DFM, T7*.RWN                        │
├─────────────────────────────────────────────────────────┤
│  Business logic (TAS Pro 4GL)                           │
│  BK*.SRC → *.RUN (Pro 6)                                 │
│  T7*.SRC → *.RWN (Pro 7)                                 │
├─────────────────────────────────────────────────────────┤
│  Runtime — TAS Professional 7                           │
│  tp7runtime.exe  (EXE is 33.3 MB)                       │
│  + qtintf70.dll (Qt/CLX), c4dll.dll (CodeBase DBF)      │
├─────────────────────────────────────────────────────────┤
│  Reports — Nevrona ReportBuilder                         │
│  RBDsgnr.exe, *.RTM templates, PDFS\*.pdf output         │
├─────────────────────────────────────────────────────────┤
│  Data                                                   │
│  Btrieve (*.B + *.mdx), CodeBase (*.DBF), and bulk      │
│  .TXT reports / exports, all on the network share       │
└─────────────────────────────────────────────────────────┘
```

## Major modules (by file prefix)

Three-generation mix:
- **BK\*** — Bookkeeping/backbone, legacy since the TAS-Pro 3→5 port.
- **T6\*** — TAS Pro 6 generation (pre-Windows-native UI).
- **T7\*** — TAS Pro 7 generation (current Delphi-UI era).

Functional area codes, 1–2 letters, after the generation prefix:
- `AR` — Accounts Receivable
- `AP` — Accounts Payable
- `IN` — Inventory
- `SO` — Sales Order
- `PO` — Purchase Order
- `WO` — Work Order / job / labor routing
- `GL` — General Ledger
- `MR` — MRP
- `CC` — Cycle Count / Count (needs verification)
- `SH` — Shipping
- `CR` — CRM-related

## How a user starts it

1. Double-clicks `C:\ISTS\EvoERP.lnk` → runs `C:\ISTS\StartEvo.exe`.
2. `StartEvo.exe` reads `taspro7.ini` (`DfltRunPrg = \\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn`).
3. Spawns `tp7runtime.exe` (aka `evoerp.exe`) with that RWN as the
   initial program.
4. The runtime loads **EvoERPmenu.rwn** from the share, which renders
   the login, company selection, and main menu.
5. Menu picks launch other `.rwn` / `.run` modules in the same share.

See `docs/07-runtime-boot/boot-sequence.md` for the detailed trace.
