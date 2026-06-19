# Sales Analysis (SA)

Status: verified (auto-generated from extracted schema + CHM help content).

- **Module code**: `SA`
- **Tables**: 1 (prefix `BKSA`)
- **UI forms**: 18+ (prefixes `T7SA`, `T6SA`)
- **Menu operations**: 17 (SA-A through SA-P, plus sub-programs SA-F-A through SA-F-D)

SA is a **reporting-only module** — it contains no data-entry programs. All reports read from posted invoice history (BKARHINV / BKARHIVL) and, for bookings, from the open sales order file (BKSOX). The module's one database table (BKSAREPT) stores saved report filter configurations.

→ See **[help-content.md](help-content.md)** for a full narrative description of all 17 programs.

## Menu operations

| Code | Operation |
| ---- | --------- |
| `SA-A` | Print Daily Sales/Bookings |
| `SA-B` | Print Profit by Invoice |
| `SA-C` | Print Customer Detail |
| `SA-D` | Print Customer Summary |
| `SA-E` | Print Customer Class Detail |
| `SA-F-A` | Chart/Export Profit by Invoice |
| `SA-F-B` | Chart/Export Customer Detail/Summary |
| `SA-F-C` | Chart/Export Salesperson Summary |
| `SA-F-D` | Chart/Export Item Sales Analysis |
| `SA-G` | Print Customer Class Summary |
| `SA-H` | Print Salesperson Detail |
| `SA-I` | Print Salesperson Summary |
| `SA-J` | Print Inventory Detail |
| `SA-L` | Print Product Class (Item Class) |
| `SA-M` | Print User-Defined Detail |
| `SA-N` | Print User-Defined Summary |
| `SA-O` | Top Customer Report |
| `SA-P` | Print Sales Report |

## Database tables (1)

| Table | File on disk | Fields | Purpose |
| ----- | ------------ | -----: | ------- |
| **BKSAREPT** | `BKSAREPT.B` | 57 | Saved report filter configurations |

## BKSAREPT — Sales Analysis Saved Report Filters (57 fields)

Primary key: `BKSA_TYPE` (STRING 8) + `BKSA_NAME` (STRING 15)

This table stores named, user-saved filter settings for SA reports. When a user saves a report definition in SA-M or SA-N (User-Defined reports), one row is inserted here. Each row captures the report template and up to 26 filter ranges across all possible filter dimensions.

### Header fields

| Field | Type | Meaning |
|-------|------|---------|
| `BKSA_TYPE` | STRING 8 | Report type category (PK 1) — identifies which SA program |
| `BKSA_NAME` | STRING 15 | Saved configuration name (PK 2) |
| `BKSA_RTM` | STRING 15 | ReportBuilder template filename (.RTM) to use |
| `BKSA_BASE` | STRING 1 | Base calculation type (e.g. A=annual, S=summary) |
| `BKSA_TITLE` | STRING 40 | Custom report title override |

### Filter range pairs (FROM/THRU — 26 pairs)

Each pair defines an inclusive range for one filter dimension. The exact meaning of each pair number depends on the BKSA_TYPE value (which SA program). The type map is not fully known without live data or RWN source, but the field sizes suggest the following dimensions:

| Pair | Type | Likely dimension |
|------|------|-----------------|
| 1 | FLOAT | Numeric range 1 (e.g. invoice number range) |
| 2 | DATE | Date range 1 (primary date filter) |
| 3 | DATE | Date range 2 (secondary date) |
| 4 | FLOAT | Numeric range 2 |
| 5 | STRING 10 | Customer code range |
| 6 | STRING 10 | Part/item code range |
| 7 | STRING 2 | State code range |
| 8 | STRING 2 | Department/class 2-char range |
| 9 | STRING 10 | Customer class range |
| 10 | STRING 10 | Item class range |
| 11 | STRING 30 | Description/name range 1 |
| 12 | STRING 30 | Description/name range 2 |
| 13 | STRING 4 | GL department range |
| 14 | STRING 4 | Code range (4-char) |
| 15 | UBINARY | Numeric index range 1 |
| 16 | UBINARY | Numeric index range 2 |
| 17 | STRING 10 | Code range (10-char) |
| 18 | STRING 15 | Salesperson code range |
| 19 | STRING 25 | Name range |
| 20 | FLOAT | Amount range |
| 21 | STRING 15 | Code range (15-char) |
| 22 | STRING 4 | Code range (4-char) |
| 23 | DATE | Date range 3 |
| 24 | FLOAT | Amount range 2 |
| 25 | FLOAT | Amount range 3 |
| 26 | STRING 3 | Currency code range (multi-currency) |

## Data sources read by SA reports

SA does not have its own data tables — all reports read from other modules:

| Source table | Used for |
|---|---|
| `BKARHINV` (84f) | Posted invoice headers — invoice date, customer, totals, salesperson |
| `BKARHIVL` (28f) | Posted invoice lines — item code, qty, price, COGS per line |
| `BKARCUST` (106f) | Customer master — name, class, territory, salesperson, sort |
| `BKICMSTR` (64f) | Item master — item description, class |
| `BKSOX` (84f) | Open sales orders — for SA-A Bookings report |
| `BKPRSALE` (87f) | Salesperson master — commission configuration |

## Notes

- SA-F-A through SA-F-D produce charts or CSV exports instead of printed reports. They share the same data source as their print counterparts.
- BKSAREPT supports only SA-M and SA-N (user-defined configurations). The other SA programs have their filter settings entered at run time and not saved.
- Multi-currency processing is supported throughout SA where the currency module (IM) is enabled.
