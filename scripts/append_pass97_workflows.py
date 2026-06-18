import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 97 — Business Workflow Recipes (2026-06-18)

---

### Recipe 10: GL Journal Entry (Manual)

**When to use:** Recording adjusting entries, accruals, reclassifications, or any
transaction that must go directly to the General Ledger without an AR/AP/PR sub-ledger.

**Module path:** GL → GL-A (Journal Entry) or GL-B (Recurring Journal Entry)

**Steps:**

```
1. GL-A (Journal Entry)
   - Enter: Journal date (BKGLTRAN.JRNLDATE)
   - Enter: Journal description (BKGLTRAN.DESC)
   - For each line:
     a. GL account number → BKGLCOA.GLACCT (must exist in chart of accounts)
     b. Debit or credit amount
     c. Reference / memo for this line
   - Total debits must equal total credits (entry is balanced)
   - Post → creates BKGLTRAN rows, updates BKGLCOA period balances

2. If entry is recurring (e.g., monthly accrual):
   - Use GL-B (Recurring Journal Entry) instead
   - Set: frequency, start/end date, template
   - Run GL-B monthly to generate the actual transaction

3. Verify posting:
   - GL-O-A (GL Trial Balance) — confirm accounts changed as expected
   - GL-O-B (GL Detail Listing) — shows individual BKGLTRAN rows
```

**Key tables:**
- BKGLTRAN — journal transaction rows (one per debit/credit line)
- BKGLCOA — chart of accounts (GL account master + period balances)
- BKGLPER — period status (open/closed per fiscal period)

**Pre-requisite:** The fiscal period must be open in BKGLPER. If the period is closed,
use GL-G (Reopen Period) before entry. Re-close after posting.

**Common errors:**
- "Account not found" — account code not in BKGLCOA; add via GL-C (COA maintenance)
- "Period closed" — open the period via GL-G first
- Entry not balanced — system will not allow posting; check debit/credit totals

**Confidence: 76/100** — Module path confirmed from menu codes; table structure verified;
exact field-by-field behavior of GL-A form inferred from DFM (T7GLA*) — RWN logic blocked.

---

### Recipe 11: Period-End Archiving and Purging

**When to use:** At month-end or year-end to archive completed transactions and purge
old data, keeping the live database fast. Run in the order shown — archive before purge.

**Module path:** SM → SM-J series (T7SMJA through T7SMJH)

**Typical sequence (monthly):**

```
1. SM-JA — Inventory Reconciliation (report only)
   - Purpose: verify inventory balance matches transaction history BEFORE archiving
   - Set: RPT.ONLY = Y (no changes, just report)
   - Review: any discrepancies must be resolved before archiving

2. SM-JC — Inventory Transaction Archive
   - After confirming SM-JA is clean, archive old inventory transactions
   - Set: date range (archive transactions before cut-off date)
   - Transaction types: select which of [ASPJWIQOCMTRG] to include
     A=AR, S=SO, P=PO, J=JC, W=WO, I=Inventory, Q=QC, O=overhead,
     C=cost adj, M=MRP, T=transfer, R=return, G=GL
   - Consolidation: optionally consolidate to summary records
   - Result: old BKISTXN rows moved to archive file

3. SM-JB — Work Order Archive (if month-end WO closure done)
   - Archive finished/cancelled WOs older than cut-off date
   - Options: ARCH.CLOSE (archive closed WOs), ARCH.CANCEL (archive cancelled WOs)
   - Orphan WO cleanup: orphan.woex = archive orphaned WO extensions
   - Archived WOs can be restored via SM-JB → Restore option

4. SM-JF — PO Archive
   - Archive received/closed POs older than cut-off
   - Range: PO number range + vendor range + date range

5. SM-JG — QC Receiver Archive
   - arch.or.purge = A (archive) or P (purge, deletes permanently)
   - Date range + QC receiver# range + vendor range
   - Use A (archive) unless disk space is critical

6. SM-JH — DC Data Collection Purge
   - CUT.DATE: purges all data collection records before this date
   - WARNING: this is a permanent delete; DC records cannot be restored
   - Only purge after confirming all DC transactions are posted to WO/JC

7. SM-JE — WO Purge (year-end / old closed WOs)
   - PURGE.CLOSE / PURGE.CANCEL: selects which WO statuses to purge
   - WO range + act.fin.date range
   - WARNING: purge is permanent; run SM-JB archive FIRST

8. SM-JD — Inventory Transaction Purge (if separate from archive)
   - Purges previously archived INV transaction records from archive file
   - Use after verifying the archive was successful
```

**Key tables affected:**
- BKISTXN / archive equivalent — inventory transactions
- WORKORD / WORKCHG — WO header and detail (archived to separate files)
- BKAPPO / BKAPPOL — PO header/detail (archived)
- BKQCRECV — QC receiver (archived or purged)
- DC data collection tables (purged)

**Safety rules:**
- Always run SM-JA (reconciliation) before SM-JC (archive)
- Archive before purge — SM-JB before SM-JE, SM-JG before purge mode
- Keep archive files for at least one fiscal year before deleting
- Coordinate with GL month-end close — post all sub-ledgers first

**Confidence: 72/100** — SM-J forms fully confirmed from DFMs; step order is best-practice
inference; exact table names for archive files not confirmed.

---

### Recipe 12: EvoERP Backup and Restore

**When to use:** Before major changes (software updates, configuration changes, year-end),
and as part of scheduled maintenance. Three backup scopes available.

**Module path:** SM → SM-O or directly via EvoERPbackup launcher

**Backup scopes:**

| Scope | Contents | When to use |
|-------|----------|-------------|
| Full System | All EvoERP program files + company data | Before software updates |
| Company Data | All .B (Btrieve) data files for selected company | Before configuration changes |
| Custom | User-selected file list (CSTFILELIST) | Targeted backup of specific tables |

**Steps:**

```
1. Open EvoERPbackup
   - Select scope: fullsystem / compdata / custom
   - If custom: edit CSTFILELIST to select specific files

2. Specify archive:
   - zipName: output archive file name
   - zipfiles: file list to include (auto-populated for Full/Company scopes)

3. COMP.TAG / EXT / NAME: component list
   - EVO automatically populates this from the component registry
   - Verify the component count before proceeding

4. Run backup
   - Creates a ZIP archive at the specified path
   - Monitor for errors (locked files, path not found)

5. Verify:
   - Check ZIP file size is plausible
   - Optionally test-restore to a temp location
```

**Restore procedure:**
- No automated restore tool in EvoERP — use Windows file extraction
- For data restore: stop EvoERP services first, extract .B files,
  restart Pervasive SQL service, then restart EvoERP
- For full system restore: extract to a staging folder, validate,
  then copy over production path

**Confidence: 68/100** — EvoERPbackup form confirmed from DFM; exact menu path to launch
it (SM-O or direct) inferred; restore steps are general Btrieve/Pervasive procedure.

---

### Recipe 13: New User Setup

**When to use:** Adding a new EvoERP user, assigning security level, and configuring
starting menu and preferences.

**Module path:** SM → SM-A (User Maintenance) + SM-B (Security Levels)

**Steps:**

```
1. SM-A (User Maintenance) — create the user record
   - Enter: AHSYLOG.AHSY_USER_ID (user name / login)
   - Enter: AHSYLOG.AHSY_PASSWORD (initial password — user should change)
   - Assign: AHSYLOG.AHSY_USER_LEVL (security level — 2-char code)
     Security level controls what menus the user can see and which
     operations they can perform (via BKSLEVEL matrix)
   - Set: AHSYLOG.AHSY_USER_TYPE (user type: A=Admin, U=User, etc.)
   - Set access flags: AHSYLOG.AHSY_USER_ACCES_1..20 (optional overrides)
   - Set: starting menu / company

2. SM-B (Security Level Maintenance) — verify or create the security level
   - If using existing level: verify BKSLEVEL matrix has correct permissions
   - If new level needed: create BKSLEVEL row for the new level code
   - For each of 20 menu sections: set YN master toggle + individual op flags
   - 20 operations per section = what the user can do within that menu

3. WBK (Workbench / Menu Customizer) — optional menu customization
   - If this user needs a custom menu (vs. the global EvoERP menu):
     Use WBK to create a custom menu layout
   - Assign: GROUP/BUTTON/CAPTION/IMAGE for each menu item
   - Set: FASTSELECT (keyboard shortcut) for frequently used options
   - Assign: ACCESS_CODE (security check per button)

4. Test the login:
   - Log in as the new user
   - Verify menu shows expected modules
   - Attempt an operation in a restricted area — confirm access denied
   - Verify starting company is correct

5. EvoSettings.INI (per-user preferences):
   - Stored in [User:NAME] section of EvoSettings.INI on the workstation
   - Set on first login: screen layout, column widths, grid preferences
   - Email configuration (if user sends from EvoERP): [EMAIL CO# X User:Y] section
     requires SMTP host, port, credentials
```

**Key tables:**
- AHSYLOG — user master (PK: AHSY_USER_ID)
- BKSLEVEL — security permission matrix (PK: BKSL_MENU + BKSL_LEVEL)
- BKLOGON — active sessions (updated on each login)

**Common errors:**
- User can see all menus even with restricted level — check BKSLEVEL YN flag for
  each menu section; YN=Y grants access regardless of individual op flags
- User cannot log in — password case-sensitivity; check AHSY_PASSWORD format
- "Access denied" on everything — AHSY_USER_LEVL not matching a BKSLEVEL row

**Confidence: 74/100** — AHSYLOG + BKSLEVEL confirmed from DDF and DFMs; WBK steps
confirmed from WBK DFM analysis; BKLOGON behavior inferred.

---

### Recipe 14: Inventory Manual Adjustment

**When to use:** Correcting a quantity or cost discrepancy found outside of a formal
physical count (Recipe 8). Also used for writing off obsolete stock, adjusting for
damaged goods, or correcting a posting error.

**Module path:** IN → IN-G (Inventory Adjustment — Quantity) or IN-H (Cost Adjustment)

**Quantity adjustment (IN-G):**

```
1. IN-G (Inventory Adjustment)
   - Enter: item code (BKICMSTR / MTICMSTR)
   - Enter: adjustment quantity (positive = add, negative = remove)
   - Enter: GL account for the offset entry (inventory adjustment account)
   - Enter: reason code or note
   - Enter: lot / serial number if item is lot/serial tracked
   - Enter: bin location if location tracking is active
   - Post: creates BKISTXN row (type I = Inventory adjustment),
           updates BKICLOC (per-location quantity),
           posts offset to GL via BKGLTRAN

2. Verify:
   - IN-O-A (Item Inquiry) — confirm new on-hand qty
   - GL-O-B (GL Detail) — confirm GL offset was posted to correct account
```

**Cost adjustment (IN-H):**

```
1. IN-H (Cost Adjustment)
   - Enter: item code
   - Enter: cost adjustment amount (per unit or total)
   - System recalculates weighted average cost (if AVCO costing)
   - Or sets new standard cost (if STND costing — requires separate cost roll)
   - Posts BKISTXN row (type C = cost adjustment)
```

**Key tables:**
- BKICMSTR / MTICMSTR — item master (on-hand qty, average cost)
- BKICLOC — per-location quantity (updated if location tracking active)
- BKISTXN — inventory transaction history (I or C type row added)
- BKGLTRAN — GL offset entry

**Notes:**
- Adjustments bypass the formal Physical Inventory (PI module) — use PI for
  periodic full counts, IN-G only for spot corrections
- Large adjustments should be approved; EvoERP does not require approval for
  IN-G by default (no approval routing like WOAC/SOAC)
- Lot/serial tracked items: must specify lot/serial on adjustment

**Confidence: 70/100** — Module path confirmed from menu codes; table flow is standard
inventory adjustment logic for Btrieve-based systems; DFM for T7ING not specifically
analyzed (no T7ING.DFM found in samples — behavior inferred from module pattern).

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
