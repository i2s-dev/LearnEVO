# EvoERP Module Naming & Inventory

Status: draft. Fills in as I read modules.

## Naming decoder

Every compiled module name parses as:

```
<gen> <area> <variant> [suffix]
```

- **`<gen>`** — generation prefix:
  - `BK` — legacy xBase-era backbone (TAS 3/5).
  - `MT` — "master" second generation (co-exists with BK).
  - `T6` — TAS Pro 6 generation.
  - `T7` — TAS Pro 7 generation (current).
  - `ACT7`, `AUTOT7`, `J7`, `HT6` — specialized variants.
  - `EVO`, `Evo` — infrastructure / platform.
  - `IS`, `BK` in front of `T7` — shop-specific customizations.

- **`<area>`** — functional module (usually 2 letters):
  - `AR` — Accounts Receivable
  - `AP` — Accounts Payable
  - `IN` — Inventory
  - `SO` — Sales Orders
  - `PO` — Purchase Orders
  - `WO` — Work Orders
  - `GL` — General Ledger
  - `MR` — MRP
  - `DC` — Data Collection (shop-floor barcode)
  - `SH` — Shipping
  - `CR` — CRM
  - `HH` — Handheld (*needs verification*)
  - `CC` — Cycle Count or "Custom Code" (*needs verification*)
  - `EI` — EDI / import (*needs verification*)
  - `CI` — Customer Invoice (*needs verification*)

- **`<variant>`** — A/B/C... letter selecting within the area:
  - Often `A` = master maintenance, `B` = entry/processing,
    `C` = inquiry, `D` = report/batch — but this is a habit, not a
    guaranteed convention. Confirm per-module.

- **`<suffix>`** — optional mode letter (e.g. `T7ARA` base, `T7ARA2`
  variation, `T7ARAE` the "edit" form referenced in
  `samples/dfm/T7ARA.DFM`:4).

## Matrix (what's in the wild, first pass)

From `//I2S109-SOLIDCRM/DBAMFG$/*.RWN` (sampled):

| Prefix family | Example files (not exhaustive)                        | Area              |
| ------------- | ----------------------------------------------------- | ----------------- |
| EvoERP\*      | `EvoERPmenu`, `EvoERPbackup`, `EvoERPupd`, `EvoERPDrillM` | Platform |
| EvoDC\*       | `EvoDC`, `EvoDCmenu`, `EvoDCmenu2`, `EvoDCsetup`      | Data collection |
| EvoNote\*     | `EvoNotes`, `EvoNotesRpt`, `EvoNoteSearch`, `EvoNotesARCH` | Notes/CRM |
| EvoSched\*    | `EvoSched`, `EvoScheduler`, `EvoSchedSetup`           | Scheduler |
| EvoService\*  | `EvoService`, `EvoServiceSetup`, `EvoServiceRemove`   | Windows service |
| EvoFNO\*      | `EvoFNO`, `EvoFNOPO`, `EvoFNOSO`, `EvoFNOWO`          | "FNO" — TBD |
| EvoLink\*     | `EvoLinks`, `EvoLinkCVT`                              | Integration links |
| J7\*          | `J7APCHECK`, `J7CCCutSheet`, `J7CCFABXFER`, `J7CJBUsage`, `J7BEFWebInv`, `J7CRSOW`, `J7DCMatLabels`, `J7EIMDCRev`, `J7HH…` | Customer-specific customs |
| ACT7\*        | `ACT7SHKNOTE`                                         | Custom (shakedown note?) |
| AUTOT7\*      | `AUTOT7MRF`                                           | Auto-run MRP forecast? |
| BOM/EDIT…     | `BOMTREE`, `EDITBOMTREE`                              | Bill-of-materials tools |
| CASH/COMM…    | `CASHFLOW`, `COMMISSIONRPT`, `CALREM`                 | Finance reports |
| CRM           | `CRMDASHBOARD`                                        | CRM dashboard |

## Per-module docs

Each of these will get its own page under
`docs/03-modules/<code>/README.md` once I study the source/DFM for the
area. Priority order (highest business-impact first, broad to narrow):

1. **Boot / menu** (`EvoERPmenu`, `EVOMENU_LOGIN`, `EVOUSERS`)
2. **Inventory** (`T7IN*`, `BKIN*`)
3. **Sales Order** (`T7SO*`, `BKSO*`)
4. **Purchase Order** (`T7PO*`, `BKPO*`)
5. **Work Order / Manufacturing** (`T7WO*`, `BKWO*`, `BKMRF`, `J7CC*`)
6. **A/R** (`T7AR*`, `BKAR*`)
7. **A/P** (`T7AP*`, `BKAP*`, `Bkaph`, `Bkapha`)
8. **GL**
9. **Platform** (scheduler, service, backup, updates)
10. **Customizations** (`J7*`)

## Open questions

- Exact meaning of the `J7` prefix (our leading hypothesis: "Job 7" or a
  customer initial like "J"=specific client custom). The fact that
  there are many of them suggests one large custom-code client.
- What does `FNO` stand for in `EvoFNO*`? (Fast-NOn-posted? First-NOtice?)
- `HH` in `J7HH*` = handheld? Or customer initials?
- `T6` vs `T7` — are any `T6*` modules still actively used, or are they
  all dead code kept for legacy data?
