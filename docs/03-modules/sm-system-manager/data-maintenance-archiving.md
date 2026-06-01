# EVO Data Maintenance — Archive & Purge Reference

Status: verified (source: ISTech Support PDF "Data_Maintenance.pdf", 2026-06-01)

---

## Purpose

Archiving moves closed/old records out of the active files into a separate archive set,
which speeds up reports, Stock Status rebuilds, IN-A lookups, and MRP generation.
Archived records are **not deleted** — they remain accessible via dedicated menu paths
or a toggle on EVO-ERP lookup/drill-down grids.

Purging **permanently deletes** records. Never purge without a verified backup.

---

## Recommended Schedule (per PDF)

| Data Type | EVO Menu | Archive After | Purge After | Notes |
|---|---|---|---|---|
| **Sales Orders** (closed) | **SM-J-J** | **6 months** | 3 years | Access archived via **SO-T** |
| **Work Orders** (closed) | SM-J-J *(WO variant)* | **6 months** | 10 years | Speeds up Stock Status, IN-A, MRP |
| **Invoices** | **SM-J-K** | 7 years | Optional | SA-M / SA-N can use Active or Archived |
| **Purchase Orders** (closed) | **SM-J-R** | 3 years | 10 years | Can archive/purge by vendor |
| **Inventory** (obsolete items) | **IN-L-O** | 5 years | 10 years | Must mark items Obsolete first |
| **Inventory Transactions** | SM-J-D (consolidate) / **SM-J-V** (archive) | 5 years | 10 years | Archive by fiscal year-end; no Restore option; view via IN-E or IN-O |
| **GL Transactions** | AM-I (consolidate) / **AM-T** (archive, EVO only) | 7 years | Optional | No Restore option; view via GL-C, GL-D |
| **AP — by Date** | **AM-J** | 2 years | 10 years | Fully-paid invoices only |
| **AP — by Vendor** | **AM-O** | 5 years | 15 years | Archives entire vendor master + all records |
| **AR — by Date** | **AM-K** | 2 years | 10 years | Fully-paid invoices only |
| **AR — by Customer** | **AM-P** | 5 years | 15 years | Archives entire customer master + all records |
| **Service/Repair & RMA** | **SM-J-P** | 5 years | 15 years | Access archived via SO-O-J / SO-O-K |
| **Sales Quotes** (closed) | **SM-J-T** | 5 years | 15 years | Archived data can be restored |
| **Inventory Audit Info** | **SM-J-S** | — | 10 years | Clear only; no archive |

---

## Archiving Closed Sales Orders — Step-by-Step (SM-J-J)

Navigate to **SM → J → J** in EVO. The screen is titled
"SM-J-J Archive/Restore Sales Orders".

| Field | Value to Enter |
|---|---|
| Archive / Restore / Purge | `A` |
| SO Number From | *(leave blank — all SOs)* |
| SO Number Thru | *(leave blank — all SOs)* |
| Date From | `00/00/00` *(no lower bound)* |
| Date Thru | Date 6 months ago, e.g. `12/01/25` |
| Customer From | *(leave blank — all customers)* |
| Customer Thru | *(leave blank — all customers)* |

Click **Process**.

The "Date" field is the SO close/ship date. Setting Thru = 6 months ago
archives every closed SO that shipped on or before that date, regardless
of customer or SO number.

### Setting Date From to 00/00/00 will NOT re-archive already-archived orders

SM-J-J only reads from the active `BKARINV` file. When an order is archived,
its record is removed from `BKARINV` entirely — there is nothing left to
re-process. `00/00/00` simply means "no lower bound on what remains in the
active file."

Confirmed via live ODBC query (2026-06-01):
- `ISARAINV` (archive) contains SOs back to **2004** — prior archiving has occurred.
- `BKARINV` (active) only goes back to **2016** — older records are already gone.

**What this does NOT affect:** Receivables, shipment history, SO-O-H report.

**What it speeds up:** All SO-O reports (except SO-O-H), Stock Status rebuild, IN-A, MRP generation.

### Known INVCD status codes (from live DB query, 2026-06-01)

| Code | Meaning |
|---|---|
| `Y` | Fully invoiced and closed — primary archive target |
| `N` | Closed without invoice (cancelled / no-charge) |
| `X` | Cancelled |
| *(blank)* | Open order |

### Test candidate — SO 70677

Confirmed via live ODBC query against `BKARINV` on 2026-06-01:

| Field | Value |
|---|---|
| SO Number | **70677** |
| Invoice Number | 88320 |
| Customer | SPECIFICATION LIGHTING SALES (5A03) |
| Ship / Invoice Date | 2025-08-11 (~10 months old) |
| Status | `Y` |

After running SM-J-J, verify the archive worked:
1. Go to **SO-T** and search for SO 70677 — it should appear.
2. Confirm it is **gone** from the normal SO-O active lookup.

---

## Work Orders — also 6 months

Closed Work Orders should be archived on the same schedule:

- Menu: SM-J-J (Work Order variant) or the WO archive path.
- Archive after **6 months**.
- Speeds up: Stock Status rebuild, IN-A, MRP.
- Job Cost reports can already report on Active or Archived files — no loss of reporting.

---

## Important Warnings

- **Purge = permanent.** No recovery without a backup. Always archive first; only purge
  when the age threshold well exceeds the archive threshold.
- **Inventory Transactions (SM-J-V) and GL Transactions (AM-T)** do **not** have a
  Restore option. Make a verified backup before running either.
- **Inventory Transaction consolidation (SM-J-D)** is also irreversible. Lot/Serial
  transactions are excluded from consolidation.
- **AP/AR by Vendor/Customer (AM-O / AM-P)** archives the entire master record — all
  invoices, payments, and POs/SOs for that entity. Confirm no active relationship exists
  before running.

---

## Physical Archive File Locations (Sales Orders)

All files live in `\\i2s109-solidcrm\DBAMFG$\` alongside the active files —
there is no separate archive subfolder.

| File | Contents |
|---|---|
| `ISARAINV.B` | Archived closed SO headers |
| `ISARAIVL.B` | Archived closed SO lines |
| `ISARADSC.B` | Archived closed SO notes |
| `ISARAHIN.B` | Archived invoice headers |
| `ISARAHIL.B` | Archived invoice lines |
| `ISARAHDS.B` | Archived invoice notes |
| `ISSOABOX.B` | Archived shipping detail |
| `ISSOAHBX.B` | Archived invoice box allocation |
| `ISSOALOT.B` | Archived invoice lot control |
| `ISSOASER.B` | Archived invoice serial control |

Naming pattern: active table `BKARINV` → archive equivalent `ISARAINV`
(prefix shifts from `BK` to `IS`, `A` inserted to denote archive).

---

## Accessing Archived Data (EVO-ERP)

| Data Type | How to View Archived Records |
|---|---|
| Sales Orders | SO-T |
| Service/Repair & RMA | SO-O-J and SO-O-K (toggle Active/Archived at prompt) |
| Invoices (SA reports) | SA-M, SA-N — select "Archived" option |
| Purchase Orders | EVO-ERP lookup/drill-down grids have an Active/Archived toggle |
| AR reports | AR-R — Active or Archived option |
| AP reports | AP-R — Active or Archived option |
| Inventory Transactions | IN-E or IN-O |
| GL Transactions | GL-C or GL-D |
