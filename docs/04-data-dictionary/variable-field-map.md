# Variable-to-Field Name Map
Status: verified | C:92/100 — derived from rwn_extract_symbols.py against 1,122 decrypted RWN files (2026-06-16)

TAS Pro 7 programs access database records through buffer variables named `TABLE.FIELD`
(dot-separated, stored in the procedure's variable table). This document maps those
programmatic names to the physical Btrieve field names in the DDF schema.

**Convention:** `BKXX.FIELDNAME` in code = `BKXX_FIELDNAME` (or close variant) in the DDF.
The table prefix is always the same; the field suffix may have underscores added/dropped.

---

## BKICMSTR — Inventory Item Master

Source: T7INA.RWN (BKIC.PROD.* variables, 63 unique)

| Variable name | Meaning |
|--------------|---------|
| BKIC.PROD.CODE | Item/part number (primary key) |
| BKIC.PROD.DESC | Item description |
| BKIC.PROD.TYPE | Item type code (M=manufactured, P=purchased, R=raw material, S=subcontract) |
| BKIC.PROD.UM | Unit of measure |
| BKIC.PROD.CAT | Item category |
| BKIC.PROD.TXBLE | Taxable flag |
| BKIC.PROD.CLASS | Item class code |
| BKIC.PROD.RLVL | Reorder level (quantity threshold to trigger replenishment) |
| BKIC.PROD.RAMT | Reorder amount (quantity to order) |
| BKIC.PROD.LSALE | Last sale date |
| BKIC.PROD.LORD | Last order/purchase date |
| BKIC.PROD.LRCPT | Last receipt date |
| BKIC.PROD.ADTR | Allow direct receipts flag |
| BKIC.PROD.TO | Transfer out flag or account |
| BKIC.PROD.LSTC | Last cost |
| BKIC.PROD.AVGC | Average cost |
| BKIC.PROD.UOH | Units on hand |
| BKIC.PROD.UOSO | Units on sales order |
| BKIC.PROD.TOTVL | Total value (UOH × avg cost) |
| BKIC.PROD.UOO | Units on purchase order (on order) |
| BKIC.PROD.UBO | Units on back order |
| BKIC.PROD.USMTD | Unit sales month-to-date |
| BKIC.PROD.GSMTD | Gross sales month-to-date |
| BKIC.PROD.CMTD | Cost month-to-date |
| BKIC.PROD.NSMTD | Net sales month-to-date |
| BKIC.PROD.NGMTD | Net gross (margin) month-to-date |
| BKIC.PROD.USYTD | Unit sales year-to-date |
| BKIC.PROD.GSYTD | Gross sales year-to-date |
| BKIC.PROD.CYTD | Cost year-to-date |
| BKIC.PROD.NSYTD | Net sales year-to-date |
| BKIC.PROD.NGYTD | Net margin year-to-date |
| BKIC.PROD.USLYR | Unit sales last year |
| BKIC.PROD.GSLYR | Gross sales last year |
| BKIC.PROD.CLYR | Cost last year |
| BKIC.PROD.NSLYR | Net sales last year |
| BKIC.PROD.NGLYR | Net margin last year |
| BKIC.PROD.USVAR | Unit sales variance (YTD vs LYR) |
| BKIC.PROD.GSVAR | Gross sales variance |
| BKIC.PROD.CVAR | Cost variance |
| BKIC.PROD.NSVAR | Net sales variance |
| BKIC.PROD.NGVAR | Net margin variance |
| BKIC.PROD.GLA | GL asset account (inventory account) |
| BKIC.PROD.DPTA | GL department — asset |
| BKIC.PROD.GLC | GL COGS account |
| BKIC.PROD.DPTC | GL department — COGS |
| BKIC.PROD.GLS | GL sales account |
| BKIC.PROD.DPTS | GL department — sales |
| BKIC.PROD.GLSNT | GL sales/net account |
| BKIC.PROD.DPTNT | GL department — sales/net |
| BKIC.PROD.PRICE | Standard sell price |
| BKIC.PROD.PMAT | Purchase/material cost method |
| BKIC.PROD.MANUF | Manufacturer code |
| BKIC.PROD.NOTE | Notes flag or notes text |
| BKIC.PROD.AVLAB | Average labor cost |
| BKIC.PROD.AVSET | Average setup cost |
| BKIC.PROD.AVOP | Average outside processing cost |
| BKIC.PROD.AVMAT | Average material cost |
| BKIC.PROD.AVFO | **MRP expedite threshold (days)** — if supply-late-by > AVFO → ACTION="EXPEDITE", else → "EXPSENS" (SRC-confirmed BKMRF.SRC L1386; previously mislabelled "avg fixed overhead") |
| BKIC.PROD.AVVO | **MRP delay sensitivity (days)** — if supply-early-by > AVVO → ACTION="DELAY", else → "DELSENS" (SRC-confirmed BKMRF.SRC L1554; previously mislabelled "avg variable overhead") |
| BKIC.PROD.EXTRA | Extra/user-defined field |
| BKIC.PROD.TAXIN | Tax-inclusive price flag |
| BKIC.PROD.ISUPC | UPC barcode |
| BKIC.PROD.LONGP | Long part number / alternate part |
| BKIC.IS.DCODE | Discount code (ISICMSTR table reference) |

---

## BKARCUST — AR Customer Master

Source: T7ARA.RWN (BKAR.* variables, 81 unique)

| Variable name | Meaning |
|--------------|---------|
| BKAR.CUSTCODE | Customer code (primary key) |
| BKAR.CUSTNAME | Customer/company name |
| BKAR.ADD1 | Address line 1 |
| BKAR.ADD2 | Address line 2 |
| BKAR.CITY | City |
| BKAR.STATE | State |
| BKAR.ZIP | ZIP / postal code |
| BKAR.CONTACT | Primary contact name |
| BKAR.TELEPHONE | Main phone |
| BKAR.FAX.PHONE | Fax number |
| BKAR.EMAIL | Email address |
| BKAR.COUNTRY | Country |
| BKAR.CREDITLMT | Credit limit |
| BKAR.CREDIT.HLD | Credit hold flag |
| BKAR.REMAINCRD | Remaining credit (limit minus outstanding) |
| BKAR.OUTINV | Outstanding invoice total |
| BKAR.LASTSALE | Last sale date |
| BKAR.LASTPMT | Last payment date |
| BKAR.CHG.INTRST | Charge interest flag (Y/N) |
| BKAR.DAYS.TOPAY | Average days to pay |
| BKAR.DISC.CODE | Discount code |
| BKAR.FOB | FOB point |
| BKAR.FORECAST | Sales forecast amount |
| BKAR.GLACCT | Default GL account |
| BKAR.GLDPT | Default GL department |
| BKAR.GROSS.MTD | Gross sales month-to-date |
| BKAR.GROSS.YTD | Gross sales year-to-date |
| BKAR.GROSS.LYR | Gross sales last year |
| BKAR.GROSS.PVAR | Gross sales variance (prior period) |
| BKAR.COGS.MTD | Cost of goods sold MTD |
| BKAR.COGS.YTD | Cost of goods sold YTD |
| BKAR.COGS.LYR | Cost of goods sold last year |
| BKAR.COGS.PVAR | COGS variance |
| BKAR.NET.MTD | Net sales month-to-date |
| BKAR.NET.YTD | Net sales year-to-date |
| BKAR.NET.LYR | Net sales last year |
| BKAR.NET.PVAR | Net sales variance |
| BKAR.PNET.MTD | Prior net MTD |
| BKAR.PNET.YTD | Prior net YTD |
| BKAR.HIST.YN | Keep history flag |
| BKAR.IS.MCCODE | Chain/multi-company code (ISCHAINM) |
| BKAR.IS.REP | Sales rep code |
| BKAR.IS.TAXGRP | Tax group |
| BKAR.IS.TAXIN | Tax-inclusive flag |
| BKAR.CUST.YEAR | Customer since year |
| BKAR.CARRIER | Default carrier |
| BKAR.CLASS | Customer class |
| BKAR.COMM | Commission rate |
| BKAR.COOP.AMT | Co-op advertising amount |
| BKAR.COOP.RATE | Co-op advertising rate |
| BKAR.EXTRA | Extra/user-defined field |
| BKAR.FOLUPDTE | Follow-up date |
| BKAR.LEAD.SRC | Lead source code |
| BKAR.LEAD.SRC2 | Lead source code 2 |
| BKAR.MAIL.LIST | Mailing list flag |
| BKAR.NEW.CUST | New customer flag |
| BKAR.NOTES | Notes flag |

---

## BKAPVEND — AP Vendor Master

Source: T7APA.RWN (BKAP.* variables; vendor-master portion)

| Variable name | Meaning |
|--------------|---------|
| BKAP.VENDCODE | Vendor code (primary key) |
| BKAP.VENDNAME | Vendor name |
| BKAP.ADD1 | Address line 1 |
| BKAP.ADD2 | Address line 2 |
| BKAP.ADD3 | Address line 3 |
| BKAP.CITY | City |
| BKAP.STATE | State |
| BKAP.ZIP | ZIP |
| BKAP.COUNTRY | Country |
| BKAP.CONTACT | Contact name |
| BKAP.TELEPHONE | Phone |
| BKAP.EMAIL | Email |
| BKAP.ALPHA1 | Alpha sort key 1 |
| BKAP.ALPHA2 | Alpha sort key 2 |
| BKAP.CLASS | Vendor class |
| BKAP.CREDLIM | Credit limit |
| BKAP.CUST.CODE | Customer code (if vendor is also a customer) |
| BKAP.DATE1 | User date 1 |
| BKAP.DATE2 | User date 2 |
| BKAP.DESC | Description/notes |
| BKAP.EXTRA | Extra/user-defined field |
| BKAP.FOB.POINT | FOB point |
| BKAP.FTERMS.NUM | Freight terms number |
| BKAP.GL.ACCT | Default GL account |
| BKAP.GL.DPT | Default GL department |
| BKAP.HIST.YN | Keep history flag |
| BKAP.IS.DCODE | Discount code |
| BKAP.IS.MCCODE | Chain/multi-company code |
| BKAP.IS.TAXGRP | Tax group |
| BKAP.IS.TAXIN | Tax-inclusive flag |
| BKAP.LASTPMT | Last payment date |
| BKAP.LASTPURCH | Last purchase date |
| BKAP.NEW.VEND | New vendor flag |
| BKAP.NOTES | Notes flag |
| BKAP.OUT.CREDIT | Outstanding credit |
| BKAP.OUTINV | Outstanding invoice total |
| BKAP.PURCH.MTD | Purchases month-to-date |
| BKAP.PURCH.YTD | Purchases year-to-date |
| BKAP.PURCH.LYR | Purchases last year |
| BKAP.PURCH.VAR | Purchases variance |
| BKAP.TERMS.NUM | Terms number |

---

## BKAPPO — AP Purchase Order Header

Source: T7POA.RWN (BKAP.PO.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKAP.PO.NUM | PO number (primary key) |
| BKAP.PO.PRTD | Printed flag |
| BKAP.PO.VNDCOD | Vendor code |
| BKAP.PO.VNDNME | Vendor name (denormalized) |
| BKAP.PO.VNDA1/A2 | Vendor address lines |
| BKAP.PO.VNDCTY/ST/ZIP | Vendor city/state/zip |
| BKAP.PO.SHPCOD | Ship-to code |
| BKAP.PO.SHPNME | Ship-to name |
| BKAP.PO.SHPA1/A2 | Ship-to address |
| BKAP.PO.SHPCTY/ST/ZIP | Ship-to city/state/zip |
| BKAP.PO.SHPVIA | Ship via |
| BKAP.PO.TERMD | Terms discount percentage |
| BKAP.PO.TERMNM | Terms name |
| BKAP.PO.ENTBY | Entered by (user code) |
| BKAP.PO.OBYCUS | Ordered by customer |
| BKAP.PO.TAXABLE | Taxable flag |
| BKAP.PO.CONFIRM | Confirmation number |
| BKAP.PO.DESC | PO description |
| BKAP.PO.EMPNUM | Employee number |
| BKAP.PO.ENDLNE | End line number |
| BKAP.PO.EXTRA | Extra/user-defined field |
| BKAP.PO.FOB | FOB point |
| BKAP.PO.GLDPT | GL department |
| BKAP.PO.INVNUM | Invoice number (when received) |
| BKAP.PO.ISBROKE | Is brokered flag |
| BKAP.PO.ISCUR | Is foreign currency flag |
| BKAP.PO.ISMCDT | Multi-company date |
| BKAP.PO.ISREV | Is revised flag |
| BKAP.PO.ISRVDT | Revision date |
| BKAP.PO.ISTXGR | Tax group |
| BKAP.PO.ITOTAL | Invoice total |
| BKAP.PO.LOC | Location code |

---

## WORKORD — Work Order Header

Source: T7WOA.RWN (MTWO.WIP.* variables)

| Variable name | Meaning |
|--------------|---------|
| MTWO.WIP.WOPRE | WO number prefix |
| MTWO.WIP.WOSUF | WO number suffix |
| MTWO.WIP.BLANK | Blank/spacer |
| MTWO.WIP.MULT | Multiplier/quantity factor |
| MTWO.WIP.SQTY | Scheduled quantity |
| MTWO.WIP.PRTY | Priority |
| MTWO.WIP.SSTART | Scheduled start date |
| MTWO.WIP.SFIN | Scheduled finish date |
| MTWO.WIP.ASTART | Actual start date |
| MTWO.WIP.AFIN | Actual finish date |
| MTWO.WIP.COMQTY | Completed quantity |
| MTWO.WIP.STATUS | Work order status |
| MTWO.WIP.LOCK | Lock flag |
| MTWO.WIP.ESETUP | Estimated setup cost |
| MTWO.WIP.EMAT | Estimated material cost |
| MTWO.WIP.EOUTPR | Estimated outside processing cost |
| MTWO.WIP.ELABOR | Estimated labor cost |
| MTWO.WIP.ASETUP | Actual setup cost |
| MTWO.WIP.AMAT | Actual material cost |
| MTWO.WIP.AOUTPR | Actual outside processing cost |
| MTWO.WIP.ALABOR | Actual labor cost |
| MTWO.WIP.ETOT | Estimated total cost |
| MTWO.WIP.ATOTAL | Actual total cost |
| MTWO.WIP.EST | Estimate flag |
| MTWO.WIP.CODE | WO type/code |

---

## BKARINV — AR Invoice Header

Source: T7SOA.RWN (BKAR.INV.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKAR.INV.NUM | Invoice number (primary key) |
| BKAR.INV.SONUM | Sales order number |
| BKAR.INV.INVCD | Invoice code/type |
| BKAR.INV.INVDTE | Invoice date |
| BKAR.INV.CUSCOD | Customer code |
| BKAR.INV.CUSNME | Customer name (denormalized) |
| BKAR.INV.CUSA1/A2 | Customer address |
| BKAR.INV.CUSCTY/CUSST/CUSZIP | Customer city/state/zip |
| BKAR.INV.CUSCNT | Customer country |
| BKAR.INV.CUSATT | Customer attention (contact) |
| BKAR.INV.SHPCTY/SHPST/SHPZIP | Ship-to city/state/zip |
| BKAR.INV.SHPCOD | Ship-to code |
| BKAR.INV.SHPNME | Ship-to name |
| BKAR.INV.SHPA1/A2 | Ship-to address |
| BKAR.INV.SHPATN | Ship-to attention |
| BKAR.INV.SHPVIA | Ship via |
| BKAR.INV.SHPCNT | Ship-to country |

---

## BKBMMSTR — Bill of Materials

Source: T7FOC.RWN (BKBM.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKBM.KEY | BOM record key (parent code + line number) |
| BKBM.PARENT | Parent item/part number |
| BKBM.PROD.LINE# | BOM line sequence number |
| BKBM.COMPONENT | Component item code |
| BKBM.QTY.REQD | Quantity required per parent |
| BKBM.REFERENCE | Reference designator (PCB silkscreen etc.) |
| BKBM.PROD.TYPE | Component type (M=manufactured, P=purchased, R=raw, S=subcontract) |
| BKBM.PROD.SCRAP | Scrap/yield factor |
| BKBM.PROD.OP | Operation step (routing step this component is issued at) |
| BKBM.PROD.OPYN | Include in operation Y/N flag |
| BKBM.PROD.PRICE | Standard component price |
| BKBM.PROD.RTNUM | Routing number reference |

---

## BKPRAGNT / BKPRMSTR — Commission Agent / Sales Rep

Source: T7CSA.RWN (BKPR.AGNT.* and BKPR.SLS.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKPR.AGNT.NUM | Agent/rep number (primary key) |
| BKPR.AGNT.CODE | Agent code |
| BKPR.AGNT.GLACT | GL account for commission payable |
| BKPR.AGNT.GLDPT | GL department |
| BKPR.SLS.EMPNUM | Salesperson employee number |
| BKPR.SLS.CLASS | Salesperson class/tier |
| BKPR.SLS.RATE | Commission rate (%) |
| BKPR.SLS.HOW | Calculation method (G=gross, N=net, C=COGS) |
| BKPR.SLS.WHEN | Payment timing (I=on invoice, P=on payment) |
| BKPR.SLS.QUOTA | Sales quota amount |
| BKPR.SLS.GROSS | Gross sales this period |
| BKPR.SLS.COGS | Cost of goods this period |
| BKPR.SLS.RCPTS | Cash receipts this period |
| BKPR.SLS.COMM | Commission earned this period |
| BKPR.SLS.PAID | Commission paid this period |
| BKPR.SLS.FNMI | First name + middle initial |
| BKPR.SLS.LNME | Last name |
| BKPR.SLS.EXPACT | Expense account |

---

## BKDCLAB — DC Labor Transactions

Source: T7ADCA.RWN (LAB.* variables)

| Variable name | Meaning |
|--------------|---------|
| LAB.DATE | Labor transaction date |
| LAB.EMP | Employee number |
| LAB.WOPRE / LAB.WOSUF | Work order prefix / suffix |
| LAB.WOKEY | Full work order key |
| LAB.OPER | Operation number |
| LAB.POSTED | Posted-to-WO flag |
| LAB.SHIFT | Shift code |
| LAB.START / LAB.FINISH | Clock-in / clock-out times |
| LAB.PARTS | Parts completed count |
| LAB.SCRAPPED | Scrapped quantity |
| LAB.NOJOBS | Number of jobs on this entry |
| LAB.RUNHRS / LAB.SETUPHRS | Run hours / setup hours |
| LAB.REGOVER | Regular (R) or overtime (O) flag |
| LAB.APPROVAL | Approval status |
| LAB.ADT.SUPER | Audit supervisor code |
| LAB.ADT.IN / LAB.ADT.OUT | Audit in/out timestamps |
| LAB.ESSDATE | Employee self-service entry date |
| LAB.SCRAPCD | Scrap reason code |

---

## LOT — Lot Control Master

Source: T7LCA.RWN (MTLOT.* variables)

| Variable name | Meaning |
|--------------|---------|
| MTLOT.CODE | Item code (part number this lot belongs to) |
| MTLOT.KEY | Lot record key |
| MTLOT.LOT | Lot number |
| MTLOT.EXPDATE | Expiration date |
| MTLOT.ONHAND | Quantity on hand in this lot |
| MTLOT.PO | Purchase order number that received this lot |
| MTLOT.RECDOC | Receiving document number |
| MTLOT.VENDOR | Vendor code |
| MTLOT.RECDATE | Receipt date |
| MTLOT.RECQTY | Received quantity |
| MTLOT.POCOST | PO cost (unit cost at receipt) |

---

## SERIAL — Serial Number Master

Source: T7SCA.RWN (MTSER.* variables)

| Variable name | Meaning |
|--------------|---------|
| MTSER.CODE | Item code (part number this serial belongs to) |
| MTSER.KEY | Serial record key |
| MTSER.SERIAL | Serial number |
| MTSER.LOT | Lot number (if also lot-controlled) |
| MTSER.PO | Purchase order number |
| MTSER.RECDOC | Receiving document number |
| MTSER.VENDOR | Vendor code |
| MTSER.RECDATE | Receipt date |
| MTSER.POCOST | PO cost at receipt |
| MTSER.SO | Sales order number (when shipped) |
| MTSER.CUSTCODE | Customer code (when shipped) |

---

## BKMRPFC — MRP Forecast

Source: T7MRA.RWN (BKMRP.FC.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKMRP.FC.KEY | Forecast record key |
| BKMRP.FC.PART | Item/part number |
| BKMRP.FC.DATE | Forecast date |
| BKMRP.FC.QTY | Forecast quantity |
| BKMRP.FC.OQTY | Original forecast quantity |
| BKMRP.FC.CQTY | Consumed quantity (demand already satisfied) |
| BKMRP.FC.FLAG | Processing flag |
| BKMRP.FC.DATE1 | Secondary date (e.g., expiry or due date) |
| BKMRP.FC.NUM | Reference number |
| BKMRP.FC.EXTRA | Extra/user-defined field |

---

## BKPIPHYS — Physical Inventory Physical Count

Source: T7PIC.RWN (BKPH.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKPH.TAGNUM | Physical count tag number |
| BKPH.ACTQTY | Actual counted quantity |
| BKPH.EMPNUM | Employee number (counter) |
| BKPH.EMPNAME | Employee name |
| BKPH.COMMENT | Count comment |
| BKPH.COUNTDATE | Count date |
| BKPH.YEAR | PI year |
| BKPH.QTR | PI quarter |
| BKPH.LOC | Location code |
| BKPH.CODE | Item code |
| BKPH.FDATE | Freeze date |
| BKPH.LOT | Lot number |

---

## BKGLCOA — GL Chart of Accounts

Source: T7GLA.RWN (BKGL.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKGL.ACCT | GL account number (primary key part 1) |
| BKGL.GLDPT | GL department code (primary key part 2) |
| BKGL.KEY | Combined GL key |
| BKGL.ACCTD | Account description |
| BKGL.TYPE | Account type (A=asset, L=liability, E=equity, I=income, X=expense) |

---

## BKGLGJRN — GL General Journal Header

Source: T7GLB.RWN (BKGL.GJ.* variables)

| Variable name | Meaning |
|--------------|---------|
| BKGL.GJ.TRANSDT | Transaction date |
| BKGL.GJ.TRANSNM | Transaction name / description |
| BKGL.GJ.TYPE | Journal type |
| BKGL.GJ.TYPEN | Journal type name (human-readable) |
| BKGL.GJ.POSTED | Posted flag |
| BKGL.GJ.CVCODE | Currency/conversion code |
| BKGL.GJ.INVCHKN | Invoice/check number |
| BKGL.GJ.NUMLNES | Number of journal lines |
| BKGL.GJ.CHKACT | Check account |
| BKGL.GJ.JOB | Job cost reference |
| BKGL.GJ.EXTRA | Extra/user-defined field |

**Related tables:** BKGLGJLN (journal lines), BKGLCHK (check register)

---

## ROUTING — Work Order Routing

Source: T7ROA.RWN (MTRO.* and LIST.CYC.* variables)

| Variable name | Meaning |
|--------------|---------|
| MTRO.CODE | Routing/operation code |
| MTRO.TYPE.STR | Routing type string |
| LIST.CYC.DATE | Cycle time capture date |
| LIST.CYCWONUM | Work order number for cycle data |
| LIST.CYCMACH | Machine/work center for cycle |
| LIST.CYCHR / .CYCMIN / .CYCSEC | Cycle time in hours/minutes/seconds |
| LIST.CYCPARTS | Parts produced in cycle |
| LIST.CYCEMP | Employee on this cycle |

**Related tables:** BKRTCST (routing costs), BKRTSPEC (routing specs), BKRTTEMP (routing templates)

---

## MTMRP — Multi-Company MRP Working Table

Source: T7AUTOMRF.RWN (MTMRP.* variables)

| Variable name | Meaning |
|--------------|---------|
| MTMRP.PARTNO | Part number |
| MTMRP.KEY | MRP record key |
| MTMRP.DATE | Planned order date |
| MTMRP.QTY | Planned order quantity |
| MTMRP.ONHAND | On-hand quantity at planning time |
| MTMRP.PEGTO | Pegged-to demand order (traceability) |
| MTMRP.ORDER | Firmed/released order reference |
| MTMRP.STARTDT | Planned start date |

**Summary:** MTMRP is the multi-company MRP scratch table — populated during an MRP run with planned orders, on-hand snapshots, and pegging links before orders are firmed or released. The `MT` prefix indicates this is a cross-company shared table (same schema used across all company codes).

---

## BKBOLHDR — Bill of Lading Header

Source: T7BOL.RWN (LOAD.*, SEAL.*, TRAILER.*, DRIVER.* variables)

| Variable name | Meaning |
|--------------|---------|
| LOAD.NUMBER | Load/BOL number |
| SEAL.NUMBER | Trailer seal number |
| TRAILER.NUMBER | Trailer identifier |
| AUTHOR.NUMBER | Authorization number |
| CONTROL.NUMBER | BOL control number |
| PICKUP.TIME | Scheduled pickup time |
| DRIVER.ARRIVED | Driver arrival timestamp |
| LOADING.START | Loading start timestamp |
| LOADING.END | Loading completion timestamp |
| DRIVER.DEPARTED | Driver departure timestamp |

**Summary:** BOL header tracks all carrier/logistics data for an outbound shipment — trailer, seal, authorization, and the complete driver timing sequence.

---

## ISACTION — Action Items

Source: T7ACTION.RWN (IS.ACTION.* variables)

| Variable name | Meaning |
|--------------|---------|
| IS.ACTION.TYPE | Action type code |
| IS.ACTION.DESC | Action description |
| IS.ACTION.MISC | Miscellaneous field |

---

## ACRDTYPE — Activity Control Record Types

Source: T7ACRDTYPE.RWN (AC.RD.* variables)

| Variable name | Meaning |
|--------------|---------|
| AC.RD.TYPE | Record type code |
| AC.RD.REASON | Reason code |
| AC.RD.DISPO | Disposition code (rework / scrap / use-as-is) |
| AC.RD.EXTRA1 | Extra field 1 |
| AC.RD.EXTRA2 | Extra field 2 |

---

## BKSBPART — Alternate / Substitute Parts

Source: T7ALTPART.RWN (BKSBPART DB file)

**Summary:** Links a primary item code to acceptable substitute items. Used in SO and WO when a primary item is out of stock. Primary key is likely BKSBPART.CODE (primary item) + BKSBPART.SUB (substitute item). Full field list blocked (RWN LIB-compiled).

---

## ISCHAINM — Multi-Company Chain Master

Source: T7CHAIN.RWN + T7CHAINM.RWN (ISCHAINM DB file)

**Summary:** Defines multi-company "chains" — groups of EVO company databases linked for intercompany transactions. One home company + linked subsidiaries/affiliates. Field names blocked (EVO.LIB).

---

## WCTRLOAD — Work Center Capacity Load

Source: T7VSCHED.RWN (WCTRLOAD DB file)

**Summary:** Work center capacity load table — aggregates WO operations scheduled to each work center by date bucket. Used by the Visual Scheduler (T7VSCHED) to display loading vs. capacity. Related to WORKCTR (work center master).

---

## ISQSOA — Quick Sales Order Staging

Source: T7QSOA.RWN (ISQSOA DB file)

**Summary:** Staging table for the Quick SO entry workflow. Holds in-progress quick orders before they are committed to BKARINV/BKARINVL.

---

## ISUDFINV — User-Defined Invoice Fields

Source: T7UDFINV.RWN (ISUDFINV DB file)

**Summary:** Stores custom field definitions added to AR invoices. Per-site extension mechanism without modifying core BKARINV schema.

---

## ISWOEX — Work Order Extensions

Source: T7PAPERLESS.RWN (ISWOEX DB file)

**Summary:** IS WO Extensions — per-operation dispatch status, operator notes, and scan data for the Paperless Shop Floor system. Extends WORKORD/WOROUT without modifying core WO tables.

---

## ISFUTYPE — Follow-Up Type Codes

Source: T7CARFUP.RWN (ISFUTYPE DB file)

**Summary:** Follow-up type code master for Corrective Action Requests (CARs). Defines categories of follow-up actions (e.g., verification visit, re-inspection, closure). Links to AC module ACRDTYPE.

---

## Notes on naming convention

TAS Pro 7 maps database records to named buffer variables. The pattern is:
- `BK` prefix = core EvoERP business tables (inherited from DBAmanufacturing)
- `IS` prefix = i2Systems / EvoERP extension tables
- `MT` prefix = multi-company or mirror tables
- Variable `BKIC.PROD.CODE` → DDF field `BKIC_PROD_CODE` (underscores replace dots)
- Some tables use a two-part prefix (`BKIC.PROD.*`) where `PROD` names the record buffer

These variable names appear in all decrypted RWN files and are the key to understanding
what data each module manipulates.
