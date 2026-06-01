# CR — Contract Review

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Sales → Contract Review (2 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Contract Review (CR) module provides a structured, department-by-department approval workflow for Sales Orders before they are released to manufacturing or shipping. An administrator assigns which departments must sign off on a given order; each authorized departmental approver then records their approval individually. Supporting documents (customer POs, drawings, inspection sheets, etc.) and free-text notes can be attached at either the order level or the department level throughout the review lifecycle.

---

## Contents

- [CR-A — Assign Departments to Sales Order](#cr-a--assign-departments-to-sales-order)
- [CR-B — View/Enter SO Approvals](#cr-b--viewenter-so-approvals)
- [Cross-references](#cross-references)

---

## CR-A — Assign Departments to Sales Order

*Source: [cr-a_assign_departments_to_sales_orders.htm](../../../samples/chm/extracted/cr-a_assign_departments_to_sales_orders.htm)*

**Purpose.** Use this program to assign the departments required for contract approval before the order can be manufactured or shipped.

### General Program Operation

1. Enter your **Contract Review ID** and **password**. Access is restricted to users who have been designated an Administrator for Contract Review.
2. Enter a **Sales Order Number**.
   - If no approvals have yet been established for that order, the program will prompt you to add them.
   - If departments had already been assigned, the existing assignments are displayed.
3. Select which departments are **required** for this order and which are **not required**. Only departments marked as required will appear in CR-B as pending approvals.

### Key Concepts

| Concept | Detail |
|---|---|
| **Contract Review ID / Password** | Separate credential set used exclusively within the CR module; distinct from the user's standard EvoERP login. |
| **Administrator role** | Only users with the Administrator designation in CR can access CR-A to add or modify department assignments. |
| **Department assignment** | Per-order configuration — the same order can require a different set of departments depending on its characteristics. |
| **Add prompt** | When an SO is entered for the first time in CR-A, the system automatically prompts to add the initial department list. |

### Linked Documents and Notes

Documents such as a PDF of the customer Purchase Order, engineering drawings, and quantity requirements — and as the contract progresses, inspection sheets, packing slips, invoices, and other files — can be linked to the contract using the **Evo Links** button. Free-text notes can be entered using the **Evo Notes** button.

Links and Notes can be scoped in two ways:

- **Contract-level** — associated with the Sales Order as a whole.
- **Department-level** — associated with a specific approving department.

---

## CR-B — View/Enter SO Approvals

*Source: [cr-b_view_enter_so_approvals.htm](../../../samples/chm/extracted/cr-b_view_enter_so_approvals.htm)*

**Purpose.** Use this program to enter contract approvals, view approval status, or view linked documents associated with a contract.

### General Program Operation

1. Enter the **Sales Order Number**.
2. The program displays the list of required approvals for that order, showing:
   - Each department assigned as required in CR-A.
   - The current **approval status** for each department.
   - The **date approved** for any department that has already been approved.
3. To record an approval:
   - Click on the **Approved** field for the relevant department.
   - Enter `Y`.
   - The system will prompt for your **Contract Approval ID** and **password**.
   - If you are an authorized approver for the selected department, the approval status is saved.

### Key Concepts

| Concept | Detail |
|---|---|
| **Sales Order Number** | Primary lookup key; drives which department list and approval statuses are displayed. |
| **Approved field** | Toggle field; enter `Y` to trigger the approval credential prompt. |
| **Contract Approval ID / Password** | Per-user credential that confirms the approver's identity and department authorization at the time of approval. |
| **Authorized approver** | A user must be pre-configured as an authorized approver for a specific department; entering credentials for a department the user is not authorized for will not save the approval. |
| **Date approved** | Recorded automatically when the approval is accepted; displayed in the approval list for audit purposes. |
| **Read-only view** | Users who are not authorized approvers can still open CR-B to view approval status and linked documents without being able to record an approval. |

### Linked Documents and Notes

Identical capability to CR-A: documents and notes can be linked or entered via the **Evo Links** and **Evo Notes** buttons, scoped either to the contract as a whole or to a specific approving department. This allows reviewers at any stage to attach inspection sheets, packing slips, invoices, or other artifacts directly within the approval workflow.

---

## Cross-references

| Module | Relationship |
|---|---|
| **SO — Sales Orders** | CR operates entirely on SO records. A Sales Order must exist before it can be assigned departments in CR-A or have approvals entered in CR-B. The approval status visible in CR-B governs whether the order is cleared for manufacturing or shipment. |
| **AR — Accounts Receivable** | Customer identity on the SO flows through to the contract; invoices generated after shipment are an AR function. CR-B supports attaching invoice documents as linked files once the contract progresses to that stage. |
| **Evo Links** | Cross-module document attachment mechanism used in both CR-A and CR-B to associate external files (PDFs, drawings, etc.) with a contract or department. |
| **Evo Notes** | Cross-module free-text note facility used in both CR-A and CR-B. |
