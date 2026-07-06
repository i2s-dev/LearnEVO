# QU — Queries and Drill-Down: Field Reference

Status: verified-schema + inferred meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The QU module supports ad-hoc SQL queries (T7JSQL.RWN = SQL Editor, menu code TA-R)
and the drill-down lookup infrastructure (ISDRILL — runtime session state). Three tables:

- **ISDRILL** — active drill-down session state (per-session, written by every TAS lookup)
- **ISQRYSQL** — saved named SQL query definitions
- **ISVARSQL** — named query variable definitions (bind parameters for ISQRYSQL queries)

ISDRILL is confirmed accessed by 999+ programs (second only to universal infrastructure
tables). It is the universal TAS Pro 7 lookup mechanism.

---

## ISDRILL
**ACTIVE DRILL DOWN FILE** — runtime session state for lookups and drill-down navigation

Fields: 46 | Key: runtime singleton per session

One record per active lookup session. TAS Pro writes filter conditions to ISDRILL when
the user invokes a field lookup (e.g., pressing F2 for a customer lookup), then reads
the result. ISDRILLM (the master config) defines what columns and keys to display;
ISDRILL holds the live session parameters.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LOOKUP_COMM | STRING | 150 | — | Command buffer — TAS command string passed to the lookup dialog |
| 2 | LOOKUP_FILE | STRING | 15 | — | Target file/table name to search (e.g., "BKARCUST") |
| 3 | LOOKUP_FILTERS_1..20 | STRING | 80 | — | 20 filter condition slots (WHERE clause fragments passed to lookup engine) |
| 24 | LOOKUP_FROM | STRING | 30 | — | Starting key value for range lookup |
| 25 | LOOKUP_GRID | STRING | 15 | — | Grid layout template name (FK → ISDRILLM via BKLUGRID) |
| 26 | LOOKUP_KEY | INTEGER | 2 | — | Key index number to use for navigation |
| 27 | LOOKUP_REC | INTEGER | 4 | — | Current record pointer (position within result set) |
| 28..46 | LOOKUP_WHILE_1..20 | STRING | 80 | — | 20 while/sort condition slots (active-record scope limiters) |

**Notes:**
- LOOKUP_FILTERS_1..20 (20 slots × 80 chars) and LOOKUP_WHILE_1..20 (20 slots × 80 chars)
  carry query conditions as TAS expression strings.
- The full field list in sorted order: LOOKUP_COMM (1), LOOKUP_FILE (2), LOOKUP_FILTERS_1–20
  (fields 3–22), LOOKUP_FROM (23), LOOKUP_GRID (24), LOOKUP_KEY (25), LOOKUP_REC (26),
  LOOKUP_WHILE_1–20 (fields 27–46) = 46 total.
- This is a session-scoped temp table — records are not persistent across logins.

## ISQRYSQL
**VARIABLE QUERY** — saved SQL query store

Fields: 2 | Key: IS_QRY_NAME

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_QRY_NAME | STRING | 30 | — | Query name (PK — user-assigned unique identifier) |
| 2 | IS_QRY_QUERY | STRING | 1000 | — | SQL query text (up to 1,000 characters) |

**Notes:**
- Used by T7JSQL.RWN (SQL Editor, menu code TA-R) to store and retrieve named queries.
- 1,000-char query limit means complex multi-join queries may be truncated.
- ISVARSQL (below) stores bind variable definitions for parameterized queries.

## ISVARSQL
**VARIABLE QUERY** — SQL query bind variable definitions

Fields: 4 | Key: IS_VAR_QNAME + IS_VAR_ORDER

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_VAR_ORDER | INTEGER | 2 | — | Variable order/sequence within the query |
| 2 | IS_VAR_QNAME | STRING | 30 | — | Query name this variable belongs to (FK → ISQRYSQL.IS_QRY_NAME) |
| 3 | IS_VAR_TYPE | STRING | 1 | — | Variable data type: `S`=String, `N`=Numeric, `D`=Date (inferred) |
| 4 | IS_VAR_VNAME | STRING | 30 | — | Variable name (as it appears in the SQL query as a placeholder) |

**Notes:**
- ISVARSQL supports parameterized queries: the user provides values for each variable
  before running the query, replacing placeholders in IS_QRY_QUERY.
- PK is QNAME + ORDER — multiple variables per query are ordered by IS_VAR_ORDER.

**Confidence: 82/100** — ISDRILL architecture confirmed from EvoERPDrillM.RWN analysis
(Pass 115); ISQRYSQL/ISVARSQL meanings clear from naming; IS_VAR_TYPE exact codes
(S/N/D) inferred, not verified from TAS source.
