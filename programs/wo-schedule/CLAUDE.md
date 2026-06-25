# WO Schedule — Program Notes

Standalone replacement for EVO WO-L-B (Print Work Order Schedule).
Mirrors T7WOLB.DFM (filter form) and T6WOLB2.RTM (ISTS Enhanced report).

---

## Intentional differences from EVO's output

The following are deliberate formatting improvements over the original EVO report.
Do **not** change these to match EVO without explicit instruction.

| Area | EVO format | Our format | Reason |
|------|-----------|-----------|--------|
| Print date | `6/25/2026` (no leading zero) | `06/25/2026` (leading zero) | More readable and consistent with MM/DD/YYYY convention used elsewhere in the report |
| Class codes in criteria | `WB only` (codes concatenated) | `W B only` (space-separated) | Easier to read when multiple codes are listed; unambiguous when codes are more than one character |

---

## Source files studied

- `samples/T7WOLB.DFM` — filter form definition (all field names, captions, hints)
- `samples/T6WOLB2.RTM` — ISTS-enhanced report template (column layout, ISTS additions)
- `samples/T6WOLB1.RTM` — base report template (for reference/comparison)

## Database access

- DSN: `DBA` (Pervasive SQL ODBC)
- Primary tables: `WORKORD`, `BKICMSTR`, `WOROUT`, `WOLABOR`, `BKSYMSTR`
- Class code field: `BKICMSTR.BKIC_PROD_CLASS` (not in WORKORD)
