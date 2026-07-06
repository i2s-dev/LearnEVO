# CR — Contract Review: Field Reference

Status: verified-schema + inferred meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The CR module implements an **ISO 9001-style contract review workflow** for Sales Orders.
Before an SO can be confirmed as binding, designated department approvers must review and
sign off. The MOTPAS ("motor password") field is each approver's PIN code that serves as
an electronic signature.

Two tables: ISCTREVU (approver configuration) and ISSOREVU (per-SO approval status).
T7SON accesses ISSOREVU via the `IS.SOVU.*` (12-var) named-variable namespace.

---

## ISCTREVU
**CONTRACT REVIEW APPROVER LIST** — defines who must review/approve SOs

Fields: 17 | Key: IS_CREVU_EMP

Each row is one approver. The system checks ISCTREVU to determine who must sign off
before allowing an SO to proceed.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CREVU_ACTIVE | STRING | 1 | — | Active flag: `Y` = this approver is currently active in the workflow |
| 2 | IS_CREVU_ADATE | DATE | 4 | — | Last approval date (when this approver most recently signed off) |
| 3 | IS_CREVU_ADMIN | STRING | 1 | — | Admin flag: `Y` = this approver has admin override capability |
| 4 | IS_CREVU_ATIME | TIME | 4 | — | Time of last approval |
| 5 | IS_CREVU_CDATE | DATE | 4 | — | Record creation date |
| 6 | IS_CREVU_DEPT | STRING | 25 | — | Approver's department name |
| 7 | IS_CREVU_EDATE | DATE | 4 | — | Effective date / employee start date |
| 8 | IS_CREVU_EMP | INTEGER | 2 | — | Employee number (PK, FK → payroll employee master) |
| 9 | IS_CREVU_EMPNME | STRING | 25 | — | Employee name (denormalized for display) |
| 10 | IS_CREVU_EXTRA | STRING | 100 | — | User-defined extra data |
| 11 | IS_CREVU_FLAG_1 | STRING | 1 | — | Document-type approval flag 1 (which SO types require this approver) |
| 12 | IS_CREVU_FLAG_2 | STRING | 1 | — | Document-type approval flag 2 |
| 13 | IS_CREVU_FLAG_3 | STRING | 1 | — | Document-type approval flag 3 |
| 14 | IS_CREVU_FLAG_4 | STRING | 1 | — | Document-type approval flag 4 |
| 15 | IS_CREVU_FLAG_5 | STRING | 1 | — | Document-type approval flag 5 |
| 16 | IS_CREVU_LEVEL | STRING | 2 | — | Approval level code (e.g., which workflow stage this approver covers) |
| 17 | IS_CREVU_MOTPAS | STRING | 10 | — | Approver PIN/password — entered at approval time as electronic signature |

**Notes:**
- FLAG_1..5: exact meaning requires RWN decryption; likely correspond to SO order types
  (standard/RMA/service/blanket/etc.) that this approver is responsible for.
- IS_CREVU_MOTPAS must match the PIN the approver types when signing the review.
- IS_CREVU_ADMIN approvers can override the workflow without all other signatures.

## ISSOREVU
**CONTRACT REVIEW STATUS** — per-SO contract review tracking

Fields: 12 | Key: IS_SOVU_SONUM + IS_SOVU_EMPNUM

One row per SO × approver combination. When all required approvers have approved
(IS_SOVU_APPROVE='Y'), the SO contract review is complete.

TAS access namespace: `IS.SOVU.*` (12 vars, accessed by T7SON — 361 procs).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SOVU_ADATE | DATE | 4 | — | Approval date (when this approver signed off) |
| 2 | IS_SOVU_APPROVE | STRING | 1 | — | Approval status: `Y`=approved, `N`=rejected, `W`=waiting/pending |
| 3 | IS_SOVU_DEPT | STRING | 25 | — | Approver's department (denormalized from ISCTREVU) |
| 4 | IS_SOVU_EDATE | DATE | 4 | — | Expected/required-by date for this approval |
| 5 | IS_SOVU_EMPNME | STRING | 25 | — | Approver's name (denormalized) |
| 6 | IS_SOVU_EMPNUM | INTEGER | 2 | — | Employee number of approver |
| 7 | IS_SOVU_ENTBY | STRING | 25 | — | User who created/requested this review record |
| 8 | IS_SOVU_ENTMOT | STRING | 10 | — | Entry motor code — PIN entered by the person who submitted the SO for review |
| 9 | IS_SOVU_EXTRA | STRING | 100 | — | User-defined extra data |
| 10 | IS_SOVU_MOTPAS | STRING | 10 | — | Approver's sign-off PIN (entered at approval time, matched against ISCTREVU.IS_CREVU_MOTPAS) |
| 11 | IS_SOVU_REQUIRE | STRING | 1 | — | Required flag: `Y`=this approval is mandatory before SO can proceed |
| 12 | IS_SOVU_SONUM | NUMERIC | 8 | — | SO number being reviewed (FK → BKARINV.BKAR_INV_SONUM) |

**Workflow:** When an SO is entered, T7SON creates one ISSOREVU row per active ISCTREVU
approver. Each approver logs into SO review, enters their MOTPAS PIN, and the system sets
IS_SOVU_APPROVE='Y'. The SO cannot be confirmed until all REQUIRE='Y' rows are approved.

**Confidence: 80/100** — table descriptions and IS.SOVU.* variable namespace confirmed
from T7SON analysis (Pass 173); field semantics inferred from naming + MOTPAS/ENTMOT
pattern seen in other review tables; exact FLAG_1..5 semantics and APPROVE value set
require RWN decryption.
