# PS — Password Security

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → System Manager → Password Security (7 topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

The Password Security module controls who can log in to Evo-ERP, what menus they can access, which programs auto-chain to other programs, and who is authorized to digitally sign Purchase Orders or approve Contract Review records. It is the central access-control layer for the entire system: user accounts, security levels, per-user menu customization, and approval workflows all originate here.

---

## Contents

- [PS-A — System Users/Passwords](#ps-a--system-userspasswords)
- [PS-E — Evo Menu Access by User Report](#ps-e--evo-menu-access-by-user-report)
- [PS-F — Evo Menu Access by Program](#ps-f--evo-menu-access-by-program)
- [PS-G — Maintain Menu Access](#ps-g--maintain-menu-access)
- [PS-H — Configure Auto-Chain Programs](#ps-h--configure-auto-chain-programs)
- [PS-I — Enter Digital Signers for PO](#ps-i--enter-digital-signers-for-po)
- [PS-J — Enter Contract Review Signers](#ps-j--enter-contract-review-signers)
- [Cross-references](#cross-references)

---

## PS-A — System Users/Passwords

*Source: [ps-a_system_users_passwords.htm](../../../samples/chm/extracted/ps-a_system_users_passwords.htm)*

**Purpose.** Use this program to create *Logon IDs* and *Passwords* for all Evo-ERP users. The credentials entered here are what users supply at the Evo login screen. Each Logon ID is linked to a startup company preference and a default security level. The user menus that restrict which programs each user can run are defined in PS-G and keyed on the same Logon ID.

### Default users on a new installation

A new system ships with two pre-defined users: `ADMIN` and `STARTUP`.

### Creating a new user

1. Open PS-A. The *System Users* lookup window lists all existing Logon ID records.
2. Click **Add** (or press Alt-A). A second screen opens.
3. Enter the **Logon ID** — the identifier the user will type at the login prompt.
4. Enter the **Startup Company** code — the company the user is placed in automatically on login.
5. Enter the **Security Level** (1–999):
   - `1` is the administrator level: can see and edit all data in lookup drill-down grids.
   - `999` (or blank) is the least-privileged level: most limited access.
   - Levels `1`–`5` allow editing of data directly inside lookup grids; assign these only to administrators.
   - Each lookup grid can be assigned its own required security level in SU-A Maintain Grid Lookups (default is `999`). Only users whose Security Level number is less than or equal to the grid's required level can view that grid.
6. Enter the **Security Code** — controls which default menu template is applied when no user-specific menu exists in PS-G:

   | Code | Role |
   |------|------|
   | `A`  | Admin |
   | `P`  | Power User |
   | `1`  | Sales Rep 1 |
   | `2`  | Sales Rep 2 |
   | `C`  | Customer |
   | `V`  | Vendor |
   | `U`  | User (default if nothing is defined) |
   | `E`  | Engineer |

   - **Customer** (`C`) and **Vendor** (`V`): the login name must match their Customer or Vendor Code respectively.
   - **Sales Rep 1/2** (`1`/`2`): the login name must match the sales rep's number. This enables SA-M and SA-N reports to auto-filter from/through that sales rep so they can only see their own data. Customer and Vendor filtering is planned but not yet implemented.
   - **Engineer** (`E`): limits access in IN-B Enter Inventory and BM-A Enter Bills of Material — the user can only create or edit items whose Active Status is `E`, and bills of material whose parent item has Active Status `E`.

7. On save, you are prompted to enter the user's **initial password**. The user will be forced to change it at first login.

### After setup

- Users can change their own password from within Evo: **File → Change Password**.
- To delete a Logon ID, highlight it in the lookup window and click **Delete** (or press the Delete key).

### Password Reset

An administrator cannot see a user's existing password but can click **Reset Password** and assign a new temporary one. On the user's next login, they are notified that the password was reset by ADMIN and are required to choose a new password immediately.

---

## PS-E — Evo Menu Access by User Report

*Source: [ps-e_evo_menu_access_by_user_r.htm](../../../samples/chm/extracted/ps-e_evo_menu_access_by_user_r.htm)*

**Purpose.** Generates a printed report of the menu options assigned to a range of users. Useful for auditing which programs each user can access.

### Operation

Enter the **From** and **Through** user range, then click **Print**. The report lists all menu items assigned to each user's menu within that range.

---

## PS-F — Evo Menu Access by Program

*Source: [ps-f_evo_menu_access_by_progra.htm](../../../samples/chm/extracted/ps-f_evo_menu_access_by_progra.htm)*

**Purpose.** Generates a printed report listing every user who has a specified program on their menu. The inverse of PS-E — useful for auditing who can run a particular program.

### Operation

Enter the **program name** directly or select it from the dropdown list, then click **Print**. The report shows all users whose menus include that program.

---

## PS-G — Maintain Menu Access

*Source: [ps-g_maintain_menu_access.htm](../../../samples/chm/extracted/ps-g_maintain_menu_access.htm)*

**Purpose.** Create and edit per-user menus that control which programs each user can access. This is the primary tool for tailoring the Evo interface to each person's role.

### Built-in template menus

The system ships with the following template menus:

| Template | Edit allowed | Delete allowed |
|----------|-------------|----------------|
| Admin | No | No |
| PowerUser | Yes | No |
| User | Yes | No |
| SalesRep | Yes | No |
| Customer | Yes | No |
| Vendor | Yes | No |

The **Admin** menu always grants access to all programs and cannot be modified. When new programs are added during a software update, they appear automatically on the Admin menu once the `ADMIN` user logs in after the update.

### Relationship to PS-A Security Code

If a user in PS-A has Security Code `A` (Admin) but no user-specific menu has been created in PS-G, that user always gets the full Admin menu, including any programs added by future updates.

### Creating a new user menu

1. Click **Add User**. Enter the **Access Code** — this must match the user's Login Name as defined in PS-A.
2. Optionally select an existing menu to **copy from** by typing a name or selecting from the dropdown. Starting from a template (e.g., PowerUser) and removing items is easier than building from scratch.

### Adding a group back to one or all users

If a module group (e.g., Mfg, Sales) was previously removed from a user's menu and needs to be restored:

1. Click **Add Group**.
2. Select the user to copy the group *from* (typically `ADMIN` or another fully-configured user).
3. Specify whether to add the group to a **single user** or **all users**.
4. Choose the group to add. If the user already has that group it will not be duplicated.

### Keeping menus current after software updates

- **Update to Latest Prg** button: updates program filenames for all programs users currently have access to (e.g., replaces the older `BKARA.RUN` Classic-style screen with the GUI `T7ARA.RWN` equivalent). It does not add new programs to any menu.
- **Change Prg Name** button: changes a single program's filename across all user menus at once.
- After any update, log in once as `ADMIN` to trigger the menu refresh.

### Editing a menu

- Select a menu and click **Edit**.
- Drag the **gray boxes** on the left to reorder menu groups (controls which group — Mfg, Sales, etc. — appears first when the user logs in).
- Right-click a group or button to **Delete** it or **move it to another group**. For example, Inventory and Purchasing can be merged onto a single screen.
- To remove a single program line or rearrange items, select the **Menu Lines** tab on the left. The left list shows what the user has access to; the right list shows what has been removed. New programs added during an update appear on the right side, available to be inserted into menus.

### Restoring a removed button

1. Go to the bottom of the button list and press the down-arrow key once to create a blank line.
2. Type the button code or use the dropdown to select the button and its image.
3. After re-establishing the button, add the menu-line program detail back to it.

Tip: if many items need to be restored, it is faster to delete the user and recreate them starting as a copy of another user, then selectively remove programs.

---

## PS-H — Configure Auto-Chain Programs

*Source: [ps-h-configure_auto_chain_programs.htm](../../../samples/chm/extracted/ps-h-configure_auto_chain_programs.htm)*

**Purpose.** Configure automatic program-to-program chaining — for example, having the Print Invoice program automatically invoke the Post Invoice program when printing is complete.

### Operation

1. Click **Add**.
2. Choose a **User Name** from the list. Leave blank to apply the chain to all users.
3. Select the desired **chain combination** from the dropdown list of available pairings.
4. Set the chain behavior:
   - `A` — **Ask**: the system prompts the user before launching the chained program.
   - `Y` — **Yes/Auto**: the chained program launches automatically without prompting.

> **Note:** If no users and passwords are configured in the system, the setting can only be `A` (Ask). The `Y` option becomes available only when password security is active.

> **Important:** Auto-chaining bypasses normal menu-access checks. The chained program will run even if the user's menu would not normally permit access to it. Assign `Y` chains with care.

---

## PS-I — Enter Digital Signers for PO

*Source: [ps-i_enter_digital_signers_for_po.htm](../../../samples/chm/extracted/ps-i_enter_digital_signers_for_po.htm)*

**Purpose.** Assign passwords and digital signature image files to employees who are authorized to approve and sign Purchase Orders.

### Prerequisites

Each authorized signer must first be created as an employee record in SM-G Enter Employees before they can be designated as a PO signer here.

### Fields

| Field | Description |
|-------|-------------|
| **Employee Number** | The employee number of the authorized signer (must exist in SM-G). |
| **Password** | The signer's approval password, used when digitally signing a PO. |
| **Signature Image Path** | Full path and filename of the image file that will print as the signer's handwritten signature on the PO document. |
| **Initials** | The signer's initials, printed in the PO "Entered By" field. |
| **Threshold** | Maximum dollar value of Purchase Orders this signer can approve. Enter `0` for unlimited authority. |

---

## PS-J — Enter Contract Review Signers

*Source: [ps-j_enter_contract_review_signers.htm](../../../samples/chm/extracted/ps-j_enter_contract_review_signers.htm)*

**Purpose.** Enter and assign passwords and department assignments to employees authorized to approve Contract Review records (linked to Sales Orders).

### Operation

For each approver, enter:

| Field | Description |
|-------|-------------|
| **Name** | The approver's name. |
| **Department** | The department the approver represents in the contract review process. |
| **Password** | The approver's contract review password. |
| **Administrative level** | Designate at least one approver as Administrative. An Administrative approver can create and manage other approvers. |

### Activation and security

Once any approvers are established, the Contract Review procedure is **enabled system-wide**. After that point, only a Contract Review Administrative-level approver can load the PS-J program itself.

### Bulk approval of existing orders

Click the **App SOs** button at the bottom of the screen to globally approve a range of Sales Orders. This allows orders that were already in process before Contract Review was enabled to bypass the approval workflow so they can ship without going through individual review.

---

## Cross-references

| This program | Connects to |
|--------------|-------------|
| PS-A | PS-G (menus keyed on Logon ID); SU-A (grid security levels); SA-M, SA-N (sales rep/customer report filters) |
| PS-G | PS-A (Access Code = Login Name); PS-E, PS-F (reporting on menu assignments) |
| PS-H | Any program pair listed in the chain dropdown (e.g., PO print → PO post) |
| PS-I | SM-G Enter Employees (employee must exist first); PO module (signature prints on Purchase Orders) |
| PS-J | SO module / Contract Review workflow (approvals gate shipment of Sales Orders) |

- **PO module** — PS-I digital signers govern who can approve and sign purchase orders; see the PO section of this documentation.
- **Contract Review / SO module** — PS-J signers gate the Contract Review approval step on Sales Orders; see the SO/CR section of this documentation.
- **SU-A Maintain Grid Lookups** — grid-level security levels interact with the user Security Level set in PS-A.
- **SM-G Enter Employees** — prerequisite for PS-I; PO signers must be employees.
- **IN-B Enter Inventory / BM-A Enter Bills of Material** — Engineer security code (`E`) in PS-A restricts which items the user can create or edit in these programs.
