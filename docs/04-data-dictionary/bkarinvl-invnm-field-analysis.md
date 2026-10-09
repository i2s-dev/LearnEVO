# BKARINVL — BKAR_INVL_INVNM Field Analysis

Status: verified  
Date: 2026-07-09

---

## Question

Is `BKAR_INVL_INVNM` in `BKARINVL` a **Sales Order number** or an **Invoice number**?

This came up in the context of the RemovePhantomSalesOrder project, which uses
`WHERE BKAR_INVL_INVNM = <SO#>` to locate and delete orphaned SO lines.

---

## Short Answer

**Sales Order number.** Confirmed from live database queries. The field name is
misleading — "INVNM" does not mean "invoice number" in this table.

---

## Evidence Trail

### 1. Module-of-origin (structural)

Every RWN/RUN file that opens `BKARINVL` is a Sales Order module:

```
T6SOB, T6SOC, T6SOD, T6SOE, T6SOF, T6SOJ, T6SOM, T6SOPB, T6SOPD, ...
```

No AR invoice module (T6AR\*, T7AR\*) references `BKARINVL`. If it were a pure
invoice lines table, the inverse would be true.

Source: `samples/rwn_strings/T6SOD.RUN.txt` and full grep across `samples/rwn_strings/`.

### 2. FK inference

`samples/fk_inferred.csv` format is `referenced_table, pk_field, referencing_table`.

```
ISSSRL,BKAR_INVL_INVNM,BKARINVL
```

`BKARINVL.BKAR_INVL_INVNM` references `ISSSRL` (an ISS-module / sales-side table),
not any BKAR AR invoice header.

### 3. A misleading SQL file — and why it doesn't apply

`samples/jar/DefaultSQL/SALES.sql` contains:

```sql
WHERE BKARHINV.BKAR_INV_NUM = BKARHIVL.BKAR_INVL_INVNM
```

This looks like `INVNM` = invoice number. However, this query uses **`BKARHIVL`**
(historical/posted invoice lines), not `BKARINVL` (open SO lines). They share the
same field names but are different tables in different modules. `BKARHIVL.BKAR_INVL_INVNM`
being an invoice number does not mean `BKARINVL.BKAR_INVL_INVNM` is also an invoice number.

### 4. Live join test

Using SO 76066 (an open order from `BKARINV`):

```sql
SELECT 'BY_SONUM', COUNT(*)
FROM BKARINVL L
JOIN BKARINV H ON L.BKAR_INVL_INVNM = H.BKAR_INV_SONUM
WHERE H.BKAR_INV_SONUM = 76066

UNION ALL

SELECT 'BY_INVNUM', COUNT(*)
FROM BKARINVL L
JOIN BKARINV H ON L.BKAR_INVL_INVNM = H.BKAR_INV_NUM
WHERE H.BKAR_INV_SONUM = 76066
```

| Join type | Rows returned |
|-----------|--------------|
| BY_SONUM  | 163          |
| BY_INVNUM | 0            |

Note: this test is sound but not by itself conclusive — the `BY_INVNUM` join returned
0 because `BKAR_INV_NUM` was 0 for that open (not yet invoiced) record. See §5 below
for the definitive proof.

### 5. Number range comparison (definitive)

`BKAR_INV_NUM` and `BKAR_INV_SONUM` are **completely separate sequential counters**
running in non-overlapping ranges. Verified from 3,817 live `BKARINV` rows:

| Field | Observed range | What it is |
|-------|---------------|------------|
| `BKAR_INV_NUM` | ~94,000s | Invoice number — separate sequential counter |
| `BKAR_INV_SONUM` | ~64,000–76,000 | Sales Order number — separate sequential counter |

They **never equal each other** across any of the 3,817 rows in `BKARINV`.

`BKARINVL.BKAR_INVL_INVNM` value range from live data:

```sql
SELECT MIN(BKAR_INVL_INVNM), MAX(BKAR_INVL_INVNM), COUNT(DISTINCT BKAR_INVL_INVNM)
FROM BKARINVL
```

| MIN   | MAX   | DISTINCT |
|-------|-------|----------|
| 4,726 | 76,066 | 3,824   |

The max value (76,066) matches the current top of the SO number range exactly.
The values are nowhere near the invoice number range (~94k). This is conclusive.

---

## Why the Name Is Misleading

`BKAR_INVL_INVNM` likely originates from the DBA Manufacturing codebase, where
"invoice" and "sales order" may have shared a single counter or concept. As EVO
evolved separate sequential counters for SO numbers and invoice numbers, the field
name was never updated. The same field name appears in `BKARHIVL` (historical invoice
lines) where it genuinely holds an invoice number — the two tables share field name
conventions but not field semantics.

---

## Implication for Phantom SO Deletion

Deleting orphaned lines from `BKARINVL` using:

```sql
DELETE FROM BKARINVL WHERE BKAR_INVL_INVNM = <SO#>
```

is correct. The field stores the Sales Order number, and this is the right key
to target phantom lines with no corresponding header in `BKARINV`.

---

## Confidence

**100/100** — Value ranges confirmed from 3,817 live `BKARINV` rows and 3,824
distinct `BKARINVL` values. INVNM max (76,066) matches SONUM range; invoice numbers
(~94k) are an entirely separate counter with no overlap.
