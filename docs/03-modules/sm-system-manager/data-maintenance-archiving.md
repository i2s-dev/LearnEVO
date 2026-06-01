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

## Immediate Action: Archive Closed Sales Orders ≥ 6 Months Old

Per the PDF recommendation and the team request, the priority task is:

1. In EVO, navigate to **SM-J-J** (System Manager → J → J).
2. Choose **Archive** (not Purge).
3. Set the cutoff date to **6 months ago** (i.e., on or before 2025-12-01 as of today 2026-06-01).
4. Run the archive.
5. Verify: archived orders are accessible via **SO-T**.

**What this does NOT affect:** Receivables, shipment history, SO-O-H report.

**What it speeds up:** All SO-O reports (except SO-O-H), Stock Status rebuild, IN-A, MRP generation.

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
