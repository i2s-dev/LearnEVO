# Quality Control (QC)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `QC`
- **Tables**: 2 (prefixes `BKQC`)
- **UI forms**: 15 (prefixes `T7QC`, `T6QC`)
- **Menu operations**: 0

## UI forms (15)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7QCA.DFM` | New Screen | 13 | 41 | 0 |
| `T7QCB.DFM` | New Screen | 16 | 46 | 0 |
| `T7QCC.DFM` | New Screen | 12 | 38 | 0 |
| `T7QCD.DFM` | New Screen | 18 | 51 | 0 |
| `T7QCFA.DFM` | New Screen | 39 | 100 | 0 |
| `T7QCFD.DFM` | New Screen | 6 | 25 | 0 |
| `T7QCFF.DFM` | New Screen | 12 | 38 | 0 |
| `T7QCGA.DFM` |  | 0 | 1 | 0 |
| `T7QCGD.DFM` | New Screen | 14 | 43 | 0 |
| `T7QCMTHD.DFM` |  | 0 | 1 | 0 |
| `T7QCRESULTS.DFM` | QC Testing Results | 7 | 28 | 0 |
| `T7QCRSLT.DFM` |  | 0 | 1 | 0 |
| `T7QCSPEC.DFM` |  | 0 | 1 | 0 |
| `t7qcfb.DFM` | New Screen | 7 | 27 | 0 |
| `t7qcgb.DFM` | New Screen | 6 | 25 | 0 |

## Database tables (2)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKQCMSTR** | `BKQCMSTR.B` | 14 | `BKQC_VEND_CODE`, `BKQC_RECV_DATE`, `BKQC_PO_NUM` |
| **BKQCTRAN** | `BKQCTRAN.B` | 21 | `BKQC_TRN_PO`, `BKQC_TRN_VEND`, `BKQC_TRN_CODE` |

## Live Data Analysis (Pass 420, 2026-06-30)

Queried via DSN=DBA ODBC against the live i2 Systems database.

### BKQCMSTR — QC receive events

| Metric | Value |
|--------|------:|
| Total receive events | 53,300 |
| Total quantity received | 90,391,770 |
| Total quantity bought off (passed) | 88,814,517 |
| Total quantity rejected | 1,564,898 |
| **Overall rejection rate** | **~1.73%** |

- Latest receive date: 2026-06-30 (module is actively used)
- One record per PO receive event; primary key = BKQC_VEND_CODE + BKQC_RECV_DATE + BKQC_PO_NUM

### BKQCTRAN — QC transaction detail

| Metric | Value |
|--------|------:|
| Total transaction records | 54,216 |
| Avg items per receive event | ~1.02 |

- One record per part number within a receive event
- BKQC_TRN_CODE = item part number being inspected
- Most frequently inspected items: TOOLING (881×), PROTO (398×), OUT2 (366×), 3120155 (283×), 700-01607-4 (219×)
- Note: TOOLING and PROTO entries confirm QC module used for both production parts and project-specific material tracking

**Interpretation:** QC module is heavily used — 53,300 receive events over company history with 1.73% rejection rate. Almost all receives pass inspection (98.3%). The small number of items per receive (1.02 average) means most POs receive one line at a time through QC inspection.

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
