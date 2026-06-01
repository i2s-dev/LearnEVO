# QC — Quality Control

Status: verified (summarized from the vendor's help file).

Source CHM: `\\i2s109-solidcrm\DBAMFG$\EVOHELP.CHM` →
[samples/chm/EvoHELP.CHM](../../../samples/chm/EvoHELP.CHM) →
decompiled to [samples/chm/extracted/](../../../samples/chm/extracted/).
Extracted via [scripts/chm_to_md.py](../../../scripts/chm_to_md.py).

This doc consolidates the **11 help topics** under the CHM's
*Manufacturing → Quality* category. Programs cover four reporting
functions (QC-A through QC-E), the full Non-Conformance Report (NCR)
lifecycle (QC-F-A through QC-F-E), and Corrective Action Report (CAR)
entry (QC-G-A). Each program gets its purpose, key behaviors, and
cross-links. Full verbatim source is one click away via each `Source:`
link.

For the companion schema + menu view of this module, see
[README.md](README.md) in this folder.

---

## Contents

**Quality reports**
- [QC-A Quality Control Receiving Report](#qc-a-quality-control-receiving-report)
- [QC-B Quality Control Materials Report](#qc-b-quality-control-materials-report)
- [QC-C Production Scrap Report](#qc-c-production-scrap-report)
- [QC-D Quality Control Labor Report](#qc-d-quality-control-labor-report)
- [QC-E Vendor Quality Performance](#qc-e-vendor-quality-performance)

**Non-Conformance Reports (NCR) — QC-F**
- [QC-F-A Enter NCR](#qc-f-a-enter-ncr)
- [QC-F-B Print NCR](#qc-f-b-print-ncr)
- [QC-F-C Disposition NCR](#qc-f-c-disposition-ncr)
- [QC-F-D Close NCR](#qc-f-d-close-ncr)
- [QC-F-E View NCR](#qc-f-e-view-ncr)

**Corrective Action Reports (CAR) — QC-G**
- [QC-G-A Enter CAR](#qc-g-a-enter-car)

**Cross-references**
- [Cross-references](#cross-references)

---

## QC-A Quality Control Receiving Report

*Source: [qc-a_quality_control_receiving.htm](../../../samples/chm/extracted/qc-a_quality_control_receiving.htm)*

**Purpose:** Generates a report of Scrap or QC Code rejections reported
against suppliers in PO-J-C Enter Inspection Buyoffs.

**General operation:** Enter the date range and specify whether to report
on Scrap codes or QC codes. Then provide the ranges to filter on:

- Scrap/QC code range
- Item number range
- Item Class range
- Vendor range

The report draws its data exclusively from inspection buyoff records
entered in [PO-J-C Enter Inspection Buyoffs](../po-purchase-orders/help-content.md).
It answers the question: of all items received from suppliers and
inspected, which were rejected, for what reason, and in what quantity?

---

## QC-B Quality Control Materials Report

*Source: [qc-b_quality_control_materials.htm](../../../samples/chm/extracted/qc-b_quality_control_materials.htm)*

**Purpose:** Generates a report of Scrap Code rejections reported on
components during WO material issuance.

**Data source:** Rejections entered in any of the following Work Order
programs:

- WO-G Issue Materials
- WO-K-M Parts Requester
- WO-K-R Issue Scrap Component

**General operation:** Enter the date range and the filter ranges:

- Scrap code range
- Parent Item range
- Parent Item Class range
- Component Item range
- Component Item Class range
- Work Order number range

This report focuses on **component-level** scrap — material that was
issued or scrapped during production rather than at receiving. It is
distinct from QC-A (receiving-side) and QC-C (finished-part-side).

---

## QC-C Production Scrap Report

*Source: [qc-c_production_scrap_report.htm](../../../samples/chm/extracted/qc-c_production_scrap_report.htm)*

**Purpose:** Generates a report of Scrap Codes reported on finished or
in-process parts in WO-I Enter Finished Production.

**Data source:** Scrap codes entered in WO-I Enter Finished Production.

**General operation:** Enter the date range and the filter ranges:

- Scrap code range
- Parent Item range
- Parent Item Class range
- Work Order number range

This report captures scrap recorded at the **finished production** step —
i.e., parts that failed acceptance at the point of completion rather than
during component issuance (QC-B) or at receiving (QC-A).

---

## QC-D Quality Control Labor Report

*Source: [qc-d_quality_control_labor_rep.htm](../../../samples/chm/extracted/qc-d_quality_control_labor_rep.htm)*

**Purpose:** Generates a report of Scrap Code or Rework rejections
reported on parts in process during labor entry.

**Data source:** Rejections entered via any of the following programs:

- DC-A Enter Labor/Production
- DC-B Enter Production Only
- WO-F Enter Labor
- WO-M Batch Labor Entry

**General operation:** Enter the date range and the filter ranges:

- Scrap/Rework code range
- Parent Item range
- Parent Item Class range
- Work Order number range

This report captures quality problems recorded at the **labor/operation
level** — during the data collection or labor entry step, before the
work order reaches final production reporting. It complements QC-B
(material issuance scrap) and QC-C (finished production scrap).

---

## QC-E Vendor Quality Performance

*Source: [qc-e_vendor_quality_perfirmanc.htm](../../../samples/chm/extracted/qc-e_vendor_quality_perfirmanc.htm)*

**Purpose:** Generates a performance report comparing good receipts
versus Scrap or QC Code rejections reported against suppliers.

**Data source:** Inspection buyoff records in PO-J-C Enter Inspection
Buyoffs (same source as QC-A, but presented as a performance summary
rather than a rejection detail list).

**General operation:** Enter the date range and specify:

- Vendor range
- Vendor Class range
- Whether to include item detail in the output
- Whether to base percentages on total value or item quantities

This is the primary **vendor scorecard** report for quality. It expresses
each vendor's rejection rate as a percentage, giving management a
consolidated view of supplier quality performance over a period.

---

## QC-F-A Enter NCR

*Source: [qc-f-a_enter_ncr.htm](../../../samples/chm/extracted/qc-f-a_enter_ncr.htm)*

**Purpose:** Allows entry of a Non-Conformance Report (NCR) originating
from one of three sources:

| Origin code | Meaning |
|---|---|
| I | In-House — production rejection detected internally |
| V | Vendor — supplier rejection detected at receiving |
| R | RMA — item rejected by the customer after shipment |

**General operation:**

1. Enter an NCR number, or leave it blank and the system will assign the
   next available number when the NCR is saved.
2. Enter the **item number** rejected and, if known, the **component**
   causing the rejection.
3. Drawing number and Revision are optional fields.
4. Enter the **Quantity** and **Defect type**.
5. Indicate whether **inventory needs to be checked** and enter the
   **Warehouse Location**.
6. Select the **origin** (I, V, or R) and enter a **brief description**.
7. Optionally add **notes** and **linked images**.
8. Complete the appropriate origin-specific section on the lower part of
   the screen. This lower section is optional — information may not
   always be known at the time of entry.

The NCR is the starting point of the nonconformance lifecycle. After
entry, the NCR moves through Print (QC-F-B), Disposition (QC-F-C),
and Close (QC-F-D). A Corrective Action Report (QC-G-A) may be
spawned if corrective action is required during disposition.

---

## QC-F-B Print NCR

*Source: [qc-f-b_print_ncr.htm](../../../samples/chm/extracted/qc-f-b_print_ncr.htm)*

**Purpose:** Prints one or more NCRs — typically to attach a paper copy
to the discrepant material while it awaits disposition.

**General operation:**

- Specify an NCR number or a range of NCR numbers to print.
- Choose whether to include **Notes** and **Linked Documents** in the
  printout.

This is an informational print step. It does not change the status of
the NCR. Its primary use is physical identification — a printed NCR
tag travels with the nonconforming material through the disposition
process.

---

## QC-F-C Disposition NCR

*Source: [qc-f-c_disposition_ncr.htm](../../../samples/chm/extracted/qc-f-c_disposition_ncr.htm)*

**Purpose:** Records the disposition decision for an open NCR and
indicates whether Corrective Action is required.

**General operation:**

1. Select the NCR to disposition.
2. Choose a **disposition** from the available options:
   - Repair
   - Return
   - Rework
   - Scrap
   - Use as Is
3. The **disposition date** defaults to today but can be changed.
4. The **dispositioner** is populated automatically from the EVO user
   login — it cannot be overridden.
5. Optionally designate a **Scrap code** or **QC code** as applicable.
6. Indicate whether **Corrective Action is Required**.
7. If corrective action is required, **assign a CAR number**. This CAR
   number links the NCR to a record in QC-G-A Enter CAR.

Disposition is the decision point in the NCR lifecycle. Once
dispositioned, the NCR awaits physical completion of the action (e.g.,
rework performed, material returned) before it is formally closed via
QC-F-D.

---

## QC-F-D Close NCR

*Source: [qc-f-d_close_ncr.htm](../../../samples/chm/extracted/qc-f-d_close_ncr.htm)*

**Purpose:** Closes an NCR once the action required by the disposition
has been completed.

**General operation:**

- Select an NCR number or range and/or a date range.
- All NCRs matching the selection are closed.

Closure is the final step in the NCR lifecycle. An NCR should only be
closed after the disposition action (repair, rework, return, scrap, or
use-as-is) is physically complete. The program applies a bulk closure
mechanism — any NCR in the selected range that has been dispositioned
will be marked closed.

---

## QC-F-E View NCR

*Source: [qc-f-e_view_ncr.htm](../../../samples/chm/extracted/qc-f-e_view_ncr.htm)*

**Purpose:** View an existing NCR in read-only mode, without allowing
editing.

**General operation:**

- Enter the NCR number to view.
- The same screen as QC-F-A Enter NCR is presented, but all fields are
  locked (View Only mode).

This program is appropriate for users who need to look up NCR details
but should not have edit access. It provides visibility into the full
NCR record — header fields, origin section, notes, and linked images —
without any risk of inadvertent changes.

---

## QC-G-A Enter CAR

*Source: [qc-g-a_enter_car.htm](../../../samples/chm/extracted/qc-g-a_enter_car.htm)*

**Purpose:** Allows entry of a Corrective Action Report (CAR). A CAR
documents the investigation and corrective actions taken in response to
a nonconformance. It can originate independently or be linked to an
NCR that was dispositioned with "Corrective Action Required."

**Origins:** Same three origin types as NCR:

| Origin | Meaning |
|---|---|
| In-House | Production rejection detected internally |
| Receiving (Vendor) | Supplier rejection detected at receiving |
| RMA | Item rejected by the customer after shipment |

**General operation — header:**

1. Enter a CAR number, or leave blank for the system to assign the next
   number on save.
2. Enter the **item number** rejected and, if known, the **component**
   causing the rejection.
3. Drawing number and Revision are optional.
4. Enter the **Quantity** and **Defect type**.
5. Indicate whether **inventory** needs checking.

**General operation — action and follow-up (lower half of screen):**

The CAR owner workflow follows these stages, documented in sequence on
the lower half of the form:

| Stage | Who / When |
|---|---|
| Initiation | Initiator assigns the CAR to an owner |
| Action assignment | Owner logs in, creates an action, assigns a team |
| Immediate Containment Action | Team documents containment steps taken |
| Root Cause | Team documents the identified root cause |
| Planned Corrective Action | Team documents the planned fix |
| Implemented Corrective Action | Team confirms the fix was implemented |
| Actions to Prevent Reoccurrence | Team documents systemic prevention measures |
| Sign-off and close | Final approval closes the CAR |

A CAR linked from an NCR (via the CAR number assigned in QC-F-C
Disposition NCR) inherits the nonconformance details. A standalone CAR
can also be entered directly without a preceding NCR.

---

## Cross-references

The QC module draws data from and links to several other EvoERP modules:

**Purchase Orders (PO)**
- PO-J-C Enter Inspection Buyoffs — source data for QC-A (Receiving
  Report) and QC-E (Vendor Quality Performance). Inspection buyoffs
  are the receiving-side quality checkpoint.

**Work Orders (WO)**
- WO-F Enter Labor — source of labor-step scrap/rework data for QC-D.
- WO-G Issue Materials — source of component scrap data for QC-B.
- WO-I Enter Finished Production — source of finished-part scrap data
  for QC-C.
- WO-K-M Parts Requester — additional source for QC-B.
- WO-K-R Issue Scrap Component — additional source for QC-B.
- WO-M Batch Labor Entry — additional source for QC-D.

**Data Collection (DC)**
- DC-A Enter Labor/Production — source of labor-step scrap/rework data
  for QC-D.
- DC-B Enter Production Only — additional source for QC-D.

**Inventory (IN)**
- Warehouse location field on the NCR (QC-F-A) links to the inventory
  location of the discrepant material.

**NCR → CAR linkage (within QC)**
- QC-F-C Disposition NCR assigns a CAR number when corrective action is
  required; that CAR number is then worked in QC-G-A Enter CAR.
