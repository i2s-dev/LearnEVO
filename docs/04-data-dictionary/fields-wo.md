# WO — Work Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

Pass 574k-9: all blanks filled. Identical-schema tables collapsed to cross-references.

---

## BKSHORT
**TEMP FILE FOR SHORTAGE REPORT**

Fields: 9 | Prefix: BK_SHORT_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_SHORT_DATE | DATE | 4 | — | Shortage report date |
| 2 | BK_SHORT_DESC | STRING | 25 | — | Component part description |
| 3 | BK_SHORT_PCODE | STRING | 15 | — | Component part code |
| 4 | BK_SHORT_PPCODE | STRING | 15 | — | Parent/assembly part code |
| 5 | BK_SHORT_PPDESC | STRING | 25 | — | Parent/assembly description |
| 6 | BK_SHORT_QTYREQ | NUMERIC | 8 | 2 | Quantity required |
| 7 | BK_SHORT_SHORT | NUMERIC | 8 | 2 | Shortage quantity |
| 8 | BK_SHORT_WO_SUF | INTEGER | 2 | — | WO suffix |
| 9 | BK_SHORT_WONUM | NUMERIC | 8 | — | WO prefix/number |

## ISLSMAP
**PAPERLESS SHOP FLOOR BATCH TRACKER**

Fields: 31 | Prefix: IS_MAP_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–5 | IS_MAP_ALPHA_1..5 | STRING | 25 | — | Alpha user-defined fields 1–5 |
| 6 | IS_MAP_BATCH | STRING | 25 | — | Batch ID/number |
| 7 | IS_MAP_CCODE | STRING | 15 | — | Component item code |
| 8 | IS_MAP_CLOT | NUMERIC | 8 | — | Component lot number |
| 9 | IS_MAP_CQTY | NUMERIC | 8 | 2 | Component quantity consumed |
| 10 | IS_MAP_CQTYPER | NUMERIC | 8 | 8 | Component quantity per assembly |
| 11 | IS_MAP_CSERIAL | STRING | 25 | — | Component serial number |
| 12–16 | IS_MAP_DATE_1..5 | DATE | 4 | — | Date user-defined fields 1–5 |
| 17 | IS_MAP_EXTRA | STRING | 100 | — | Extra/custom data |
| 18–22 | IS_MAP_FLAG_1..5 | STRING | 1 | — | Boolean flags 1–5 |
| 23 | IS_MAP_OPER | INTEGER | 2 | — | Operation number |
| 24 | IS_MAP_PCODE | STRING | 15 | — | Parent/assembly part code |
| 25 | IS_MAP_PLOT | STRING | 15 | — | Parent lot number |
| 26 | IS_MAP_POSITION | STRING | 10 | — | Position on tray |
| 27 | IS_MAP_PQTY | NUMERIC | 8 | 2 | Parent/assembly quantity |
| 28 | IS_MAP_PSERIAL | STRING | 25 | — | Parent serial number |
| 29 | IS_MAP_TRAYNUM | STRING | 25 | — | Tray number |
| 30 | IS_MAP_WOPRE | NUMERIC | 8 | — | WO prefix |
| 31 | IS_MAP_WOSUF | INTEGER | 2 | — | WO suffix |

## ISMACS
**MACHINE SCHEDULE**

Fields: 11 | Prefix: IS_MACS_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_MACS_EXTRA | STRING | 100 | — | Extra/custom data |
| 2 | IS_MACS_FDATE | DATE | 4 | — | Scheduled finish date |
| 3 | IS_MACS_FTIME | TIME | 4 | — | Scheduled finish time |
| 4 | IS_MACS_MACNUM | STRING | 4 | — | Machine number |
| 5 | IS_MACS_OPER | INTEGER | 2 | — | Operation number |
| 6 | IS_MACS_SDATE | DATE | 4 | — | Scheduled start date |
| 7 | IS_MACS_STIME | TIME | 4 | — | Scheduled start time |
| 8 | IS_MACS_TREM | NUMERIC | 8 | 2 | Time remaining (hours) |
| 9 | IS_MACS_WC | STRING | 12 | — | Work center code |
| 10 | IS_MACS_WOPRE | NUMERIC | 8 | — | WO prefix |
| 11 | IS_MACS_WOSUF | INTEGER | 2 | — | WO suffix |

## ISPREQ
**PARTS REQUEST**

Fields: 23 | Prefix: IS_PREQ_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PREQ_CDATE | DATE | 4 | — | Creation/request date |
| 2 | IS_PREQ_CLOSED | STRING | 1 | — | Closed flag (Y/N) |
| 3 | IS_PREQ_EMP | INTEGER | 2 | — | Requesting employee number |
| 4 | IS_PREQ_EXTRA | STRING | 100 | — | Extra/custom data |
| 5 | IS_PREQ_INOTE | STRING | 200 | — | Internal note |
| 6 | IS_PREQ_IQTY | NUMERIC | 8 | 4 | Issued quantity |
| 7 | IS_PREQ_LCOST | NUMERIC | 8 | 2 | Last/average cost |
| 8 | IS_PREQ_LOC | STRING | 15 | — | Warehouse location |
| 9 | IS_PREQ_LOT | STRING | 15 | — | Lot ID |
| 10 | IS_PREQ_NOB | STRING | 1 | — | Not-on-BOM flag (Y/N; component not on BOM) |
| 11 | IS_PREQ_NOTE | STRING | 200 | — | Note / reason for request |
| 12 | IS_PREQ_NOTE2 | STRING | 200 | — | Note, line 2 |
| 13 | IS_PREQ_OPER | INTEGER | 2 | — | Operation number |
| 14 | IS_PREQ_PART | STRING | 15 | — | Part code |
| 15 | IS_PREQ_PRINTED | STRING | 1 | — | Printed flag (Y/N) |
| 16 | IS_PREQ_QTY | NUMERIC | 8 | 4 | Quantity requested |
| 17 | IS_PREQ_RDATE | DATE | 4 | — | Required date |
| 18 | IS_PREQ_REASON | STRING | 30 | — | Reason code |
| 19 | IS_PREQ_SCRAP | STRING | 2 | — | Scrap code |
| 20 | IS_PREQ_SERIAL | STRING | 25 | — | Serial number |
| 21 | IS_PREQ_WC | STRING | 12 | — | Work center |
| 22 | IS_PREQ_WOPRE | NUMERIC | 8 | — | WO prefix |
| 23 | IS_PREQ_WOSUF | INTEGER | 2 | — | WO suffix |

## ISQCMTHD
**PAPERLESS SHOP FLOOR TEST METHODS**

Fields: 44 | Prefix: ISQC_MTD_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISQC_MTD_DESC | STRING | 60 | — | Test description, line 1 |
| 2 | ISQC_MTD_DESC2 | STRING | 60 | — | Test description, line 2 |
| 3 | ISQC_MTD_ENTBY | INTEGER | 2 | — | Entered by (employee number) |
| 4 | ISQC_MTD_ENTDT | DATE | 4 | — | Entry date |
| 5 | ISQC_MTD_EXTRA | STRING | 100 | — | Extra/custom data |
| 6–30 | ISQC_MTD_METHOD_1..25 | STRING | 100 | — | Test method instruction lines 1–25 |
| 31–40 | ISQC_MTD_NOTES_1..10 | STRING | 60 | — | Additional notes lines 1–10 |
| 41 | ISQC_MTD_REV | STRING | 5 | — | Revision number |
| 42 | ISQC_MTD_REVBY | INTEGER | 2 | — | Revised by (employee number) |
| 43 | ISQC_MTD_REVDT | DATE | 4 | — | Revision date |
| 44 | ISQC_MTD_TSTCOD | STRING | 30 | — | Test code |

## ISQCRSLT
**PAPERLESS SHOP FLOOR TEST RESULTS**

Fields: 57 | Prefix: ISQC_SPC_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISQC_SPC_ACCEPT | STRING | 1 | — | Acceptance flag (Y/N) |
| 2 | ISQC_SPC_ADATE | DATE | 4 | — | Approval date |
| 3–7 | ISQC_SPC_ALPHA_1..5 | STRING | 25 | — | Alpha user-defined fields 1–5 |
| 8–12 | ISQC_SPC_ANOTES_1..5 | STRING | 60 | — | Approval notes lines 1–5 |
| 13 | ISQC_SPC_APPBY | INTEGER | 2 | — | Approved by (employee number) |
| 14 | ISQC_SPC_BATCH | STRING | 25 | — | Batch ID |
| 15 | ISQC_SPC_CNTR | INTEGER | 2 | — | Counter / sequence number |
| 16 | ISQC_SPC_CODE | STRING | 15 | — | Item code |
| 17–21 | ISQC_SPC_DATE_1..5 | DATE | 4 | — | Date user-defined fields 1–5 |
| 22 | ISQC_SPC_EXPMAX | STRING | 2 | — | Expected maximum limit |
| 23 | ISQC_SPC_EXPMIN | STRING | 2 | — | Expected minimum limit |
| 24 | ISQC_SPC_EXTRA | STRING | 100 | — | Extra/custom data |
| 25 | ISQC_SPC_INVNUM | NUMERIC | 8 | — | Invoice / SO number |
| 26 | ISQC_SPC_ITMNO | STRING | 9 | — | Item number (test sequence) |
| 27 | ISQC_SPC_LOT | STRING | 15 | — | Lot ID |
| 28 | ISQC_SPC_LOTQTY | NUMERIC | 8 | 2 | Lot quantity |
| 29 | ISQC_SPC_LRNUM | NUMERIC | 8 | — | Lot record number |
| 30 | ISQC_SPC_MAX | STRING | 15 | — | Maximum limit / spec |
| 31 | ISQC_SPC_MIN | STRING | 15 | — | Minimum limit / spec |
| 32 | ISQC_SPC_NUMERC | STRING | 1 | — | Numeric result flag (Y/N) |
| 33 | ISQC_SPC_OPER | INTEGER | 2 | — | Operation number |
| 34 | ISQC_SPC_PASS | STRING | 1 | — | Pass/fail flag (P/F) |
| 35 | ISQC_SPC_PONUM | NUMERIC | 8 | — | PO number |
| 36 | ISQC_SPC_PSFAIL | STRING | 4 | — | Pass/fail result code |
| 37 | ISQC_SPC_RCVNUM | NUMERIC | 8 | — | Receive number |
| 38 | ISQC_SPC_RESULT | STRING | 15 | — | Test result value |
| 39 | ISQC_SPC_SAMPLE | STRING | 25 | — | Sample ID |
| 40 | ISQC_SPC_SAMQTY | NUMERIC | 8 | 2 | Sample quantity |
| 41 | ISQC_SPC_SERIAL | STRING | 25 | — | Serial number |
| 42 | ISQC_SPC_SOLINE | NUMERIC | 8 | — | SO line number |
| 43 | ISQC_SPC_SONUM | NUMERIC | 8 | — | SO number |
| 44 | ISQC_SPC_TCNTR | INTEGER | 2 | — | Test counter |
| 45 | ISQC_SPC_TDATE | DATE | 4 | — | Test date |
| 46 | ISQC_SPC_TESTBY | INTEGER | 2 | — | Tested by (employee number) |
| 47–51 | ISQC_SPC_TNOTES_1..5 | STRING | 60 | — | Test notes lines 1–5 |
| 52 | ISQC_SPC_TSTCOD | STRING | 30 | — | Test code |
| 53 | ISQC_SPC_TSTLOT | STRING | 1 | — | Test lot flag (Y/N) |
| 54 | ISQC_SPC_TSTQTY | NUMERIC | 8 | 2 | Test quantity |
| 55 | ISQC_SPC_UNITS | STRING | 15 | — | Units of measure |
| 56 | ISQC_SPC_WOPRE | NUMERIC | 8 | — | WO prefix |
| 57 | ISQC_SPC_WOSUF | INTEGER | 2 | — | WO suffix |

## ISQCSPEC
**PAPERLESS SHOP FLOOR TEST REQUIREMENTS**

Identical schema to [ISQCRSLT](#isqcrslt) (ISQC_SPC_ prefix). Planned/required test specifications vs. actual results in ISQCRSLT.

## ISSERIAL
**PARENT TO COMPONENT SERIAL MAP**

Fields: 11 | Prefix: IS_SER_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | Assembly date |
| 2 | IS_SER_CDESC | STRING | 30 | — | Component description |
| 3 | IS_SER_COMP | STRING | 15 | — | Component part code |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | Component serial number |
| 5 | IS_SER_EXRA | STRING | 100 | — | Extra/custom data (source field name: EXRA) |
| 6 | IS_SER_FDATE | DATE | 4 | — | Assembly finish date |
| 7 | IS_SER_PARENT | STRING | 15 | — | Parent/assembly part code |
| 8 | IS_SER_PDESC | STRING | 30 | — | Parent description |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | Parent serial number |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | WO prefix |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | WO suffix |

## ISWODESC
**DBA WORK ORDER NOTES**

Fields: 5 | Prefix: BK_DESC_ — all described; see BKARRDSC in fields-so.md for schema.

| # | Field | Description |
|---|-------|-------------|
| 1 | BK_DESC_CODE | not used |
| 2 | BK_DESC_DESC | not used |
| 3 | BK_DESC_LINE | Notes line number |
| 4 | BK_DESC_NOTES | Notes - text |
| 5 | BK_DESC_NUM | WO Number |

## ISWOEX
**WORK ORDER HEADER 2**

Fields: 39 | Prefix: IS_WOEX_

Extended user-defined fields attached to WO header.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WOEX_ALPHA1 | STRING | 30 | — | Alpha UDF 1 (30-char) |
| 2 | IS_WOEX_ALPHA2 | STRING | 30 | — | Alpha UDF 2 (30-char) |
| 3 | IS_WOEX_ALPHA3 | STRING | 1 | — | Alpha flag 1 (1-char) |
| 4 | IS_WOEX_ALPHA4 | STRING | 1 | — | Alpha flag 2 (1-char) |
| 5 | IS_WOEX_ALPHA5 | STRING | 1 | — | Alpha flag 3 (1-char) |
| 6 | IS_WOEX_CAUSE | STRING | 30 | — | Cause code or description |
| 7 | IS_WOEX_CDATE | DATE | 4 | — | Close/complete date |
| 8–12 | IS_WOEX_DATE1..5 | DATE | 4 | — | Date UDFs 1–5 |
| 13–17 | IS_WOEX_DESC1..5 | STRING | 30 | — | Description UDFs 1–5 |
| 18 | IS_WOEX_EXTRA | STRING | 100 | — | Extra/custom data |
| 19 | IS_WOEX_GDATE | DATE | 4 | — | Guarantee/warranty expiry date |
| 20–24 | IS_WOEX_INT1..5 | INTEGER | 2 | — | Integer UDFs 1–5 |
| 25 | IS_WOEX_ITP | STRING | 20 | — | Inspection/test plan name |
| 26 | IS_WOEX_ITPP | STRING | 1 | — | ITP passed flag (Y/N) |
| 27 | IS_WOEX_MCLASS | STRING | 6 | — | Material class |
| 28 | IS_WOEX_MNUM | NUMERIC | 8 | — | Material/BOM alternate number |
| 29–33 | IS_WOEX_NOTE_1..5 | STRING | 100 | — | Note lines 1–5 |
| 34 | IS_WOEX_NUM1 | NUMERIC | 8 | 3 | Numeric UDF 1 |
| 35 | IS_WOEX_NUM2 | NUMERIC | 8 | 4 | Numeric UDF 2 |
| 36 | IS_WOEX_RF | STRING | 1 | — | Rework flag (Y/N) |
| 37 | IS_WOEX_WC | STRING | 12 | — | Work center |
| 38 | IS_WOEX_WOPRE | NUMERIC | 8 | — | WO prefix |
| 39 | IS_WOEX_WOSUF | INTEGER | 2 | — | WO suffix |

## ISWOHDSC
**ARCHIVED DBA WORK ORDER NOTES**

Identical schema to [ISWODESC](#iswodesc) (BK_DESC_ prefix). Archived WO note lines.

## ISWOPRIO
**WORK ORDER PRIORITY MASTER**

Fields: 4 | Prefix: IS_WOPRIO_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WOPRIO_COLOR | NUMERIC | 8 | — | Display color (Windows COLORREF value) |
| 2 | IS_WOPRIO_DESC | STRING | 30 | — | Priority description |
| 3 | IS_WOPRIO_EXTRA | STRING | 100 | — | Extra/custom data |
| 4 | IS_WOPRIO_PRIO | STRING | 1 | — | Priority code (single character) |

## ISWOROEX
**WORK ORDER ROUTING ADJUNCT FILE**

Fields: 51 | Prefix: IS_WROEX_

Extended user-defined fields attached to WO routing operations.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WROEX_ALPHA1 | STRING | 1 | — | Alpha flag 1 |
| 2 | IS_WROEX_ALPHA2 | STRING | 2 | — | Alpha UDF 2 (2-char) |
| 3–12 | IS_WROEX_ALPHA3_1..10 | STRING | 15 | — | Alpha UDFs 1–10 (15-char) |
| 13 | IS_WROEX_DATE1 | DATE | 4 | — | Date UDF 1 |
| 14–23 | IS_WROEX_DATE2_1..10 | DATE | 4 | — | Date UDFs 1–10 |
| 24 | IS_WROEX_DESC1 | STRING | 30 | — | Description UDF |
| 25 | IS_WROEX_EXTRA | STRING | 100 | — | Extra/custom data |
| 26 | IS_WROEX_FDAY | INTEGER | 2 | — | Finish day offset |
| 27–31 | IS_WROEX_FLAG_1..5 | STRING | 1 | — | Boolean flags 1–5 |
| 32 | IS_WROEX_FOI | STRING | 1 | — | First-off inspection flag (Y/N) |
| 33–37 | IS_WROEX_INT_1..5 | INTEGER | 2 | — | Integer UDFs 1–5 |
| 38 | IS_WROEX_ITP | STRING | 20 | — | Inspection/test plan name |
| 39 | IS_WROEX_ITPP | STRING | 1 | — | ITP passed flag (Y/N) |
| 40 | IS_WROEX_LQTY | NUMERIC | 8 | 2 | Lot quantity |
| 41 | IS_WROEX_NUM1 | NUMERIC | 8 | — | Numeric UDF 1 |
| 42–46 | IS_WROEX_NUM2_1..5 | NUMERIC | 8 | — | Numeric UDFs 1–5 |
| 47 | IS_WROEX_OPER | INTEGER | 2 | — | Operation number |
| 48 | IS_WROEX_PRMACH | STRING | 4 | — | Primary machine number |
| 49 | IS_WROEX_SDAY | INTEGER | 2 | — | Start day offset |
| 50 | IS_WROEX_WOPRE | NUMERIC | 8 | — | WO prefix |
| 51 | IS_WROEX_WOSUF | INTEGER | 2 | — | WO suffix |

## ISWOTRAY
**PAPERLESS BATCH TRACKING**

Fields: 52 | Prefix: IS_TRAY_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–20 | IS_TRAY_ALPHA_1..20 | STRING | 25 | — | Alpha UDFs 1–20 |
| 21–25 | IS_TRAY_BIN_1..5 | STRING | 15 | — | Bin locations 1–5 |
| 26–30 | IS_TRAY_BINQTY_1..5 | NUMERIC | 8 | 2 | Bin quantities 1–5 |
| 31 | IS_TRAY_CODE | STRING | 15 | — | Item code |
| 32 | IS_TRAY_COMQTY | NUMERIC | 8 | 2 | Completed quantity |
| 33–37 | IS_TRAY_DATE_1..5 | DATE | 4 | — | Date UDFs 1–5 |
| 38 | IS_TRAY_EXTRA | STRING | 100 | — | Extra/custom data |
| 39–43 | IS_TRAY_LOC_1..5 | STRING | 10 | — | Warehouse locations 1–5 |
| 44 | IS_TRAY_NUM | STRING | 25 | — | Tray number |
| 45 | IS_TRAY_OPDESC | STRING | 30 | — | Operation description |
| 46 | IS_TRAY_OPER | INTEGER | 2 | — | Operation number |
| 47 | IS_TRAY_QCQTY | NUMERIC | 8 | 2 | QC quantity |
| 48 | IS_TRAY_QCREQD | STRING | 1 | — | QC required flag (Y/N) |
| 49 | IS_TRAY_SCRPQTY | NUMERIC | 8 | 2 | Scrap quantity |
| 50 | IS_TRAY_SQTY | NUMERIC | 8 | 2 | Start quantity |
| 51 | IS_TRAY_WOPRE | NUMERIC | 8 | — | WO prefix |
| 52 | IS_TRAY_WOSUF | INTEGER | 2 | — | WO suffix |

## MTEXCHG
**EXTRA CHARGES**

Fields: 7 | Prefix: EXCHG_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | EXCHG_AMT | NUMERIC | 8 | 6 | Charge amount |
| 2 | EXCHG_CODE | STRING | 15 | — | Item/part code for charge |
| 3 | EXCHG_COST | NUMERIC | 8 | 6 | Cost amount |
| 4 | EXCHG_DESC | STRING | 30 | — | Charge description |
| 5 | EXCHG_EXTRA | STRING | 50 | — | Extra/custom data |
| 6 | EXCHG_LINE | NUMERIC | 8 | — | Line number |
| 7 | EXCHG_QUOTE | NUMERIC | 8 | — | Quote number |

## OUTHPROC
**OUTSIDE PROCESSING TRANSACTIONS - ARCHIVE**

Identical schema to [OUTPROC](#outproc) (MTPO_ prefix). Archived outside-processing transactions.

## OUTPROC
**OUTSIDE PROCESSING TRANSACTIONS**

Fields: 15 | Prefix: MTPO_ — all described in source.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTPO_ASSY | STRING | 15 | — | Assembly Used |
| 2 | MTPO_ASSYDESC | STRING | 30 | — | Assembly Description |
| 3 | MTPO_COST | NUMERIC | 8 | 4 | Cost |
| 4 | MTPO_DATE | DATE | 4 | — | Date |
| 5 | MTPO_DESC | STRING | 25 | — | Description |
| 6 | MTPO_EXTPR | NUMERIC | 8 | 2 | Extra Process |
| 7 | MTPO_EXTRA | STRING | 50 | — | Extra |
| 8 | MTPO_OPER | INTEGER | 2 | — | WO Operation |
| 9 | MTPO_PO | NUMERIC | 8 | — | PO Inspect/Receive PO Number |
| 10 | MTPO_PROD | STRING | 15 | — | Part Code |
| 11 | MTPO_QTY | NUMERIC | 8 | 2 | Quantity |
| 12 | MTPO_VENDNAME | STRING | 20 | — | PO Inspect/Receive Vendor Name |
| 13 | MTPO_VENDOR | STRING | 10 | — | PO Inspect/Receive Vendor |
| 14 | MTPO_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 15 | MTPO_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## QCCODES
**QC CODES**

Fields: 2 — all described in source.

| # | Field | Description |
|---|-------|-------------|
| 1 | MTQC_CODE | QC Code |
| 2 | MTQC_DESC | QC Code Description |

## SCRAP
**SCRAP CODES**

Fields: 21 | Prefix: MTSCRAP_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1–5 | MTSCRAP_ALPHA_1..5 | STRING | 30 | — | Alpha UDFs 1–5 |
| 6 | MTSCRAP_CODE | STRING | 2 | — | Scrap code |
| 7–11 | MTSCRAP_DATE_1..5 | DATE | 4 | — | Date UDFs 1–5 |
| 12 | MTSCRAP_DESC | STRING | 30 | — | Scrap description |
| 13 | MTSCRAP_EXTRA | STRING | 50 | — | Extra/custom data |
| 14–18 | MTSCRAP_FLAG_1..5 | STRING | 1 | — | Boolean flags 1–5 |
| 19 | MTSCRAP_GLACCT | STRING | 10 | — | GL account for scrap posting |
| 20 | MTSCRAP_GLDPT | STRING | 4 | — | GL department for scrap posting |
| 21 | MTSCRAP_TYPE | STRING | 1 | — | Scrap type code |

## WCTRLOAD
**WORK CENTER LOAD %**

Fields: 8 | Prefix: WC_LOAD_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WC_LOAD_CAP | NUMERIC | 8 | 2 | Capacity (hours available in period) |
| 2 | WC_LOAD_DATE | DATE | 4 | — | Period date |
| 3 | WC_LOAD_EXTRA | STRING | 100 | — | Extra/custom data |
| 4 | WC_LOAD_LOAD | NUMERIC | 8 | 2 | Current load (hours scheduled) |
| 5 | WC_LOAD_TOTHRS | NUMERIC | 8 | 2 | Total hours scheduled |
| 6 | WC_LOAD_UDATE | DATE | 4 | — | Last update date |
| 7 | WC_LOAD_UTIL | NUMERIC | 8 | 2 | Utilization percent |
| 8 | WC_LOAD_WC | STRING | 12 | — | Work center code |

## WOBOM
**WORK ORDER BILL OF MATERIAL**

Fields: 26 | Prefix: WOBOM_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_^ISSUED | NUMERIC | 8 | 2 | Issued flag (computed; ^ prefix) |
| 2 | WOBOM_AMATCST | NUMERIC | 8 | 2 | Actual material cost |
| 3 | WOBOM_ASSY | STRING | 15 | — | Assembly part code |
| 4 | WOBOM_ASSYDESC | STRING | 30 | — | Assembly description |
| 5 | WOBOM_ASSYQTY | NUMERIC | 8 | 2 | Assembly build quantity |
| 6 | WOBOM_BINLOC | STRING | 10 | — | Bin location |
| 7 | WOBOM_COMPCODE | STRING | 15 | — | Component part code |
| 8 | WOBOM_COMPDESC | STRING | 30 | — | Component description |
| 9 | WOBOM_EMATCST | NUMERIC | 8 | 2 | Estimated material cost |
| 10 | WOBOM_EXTRA | STRING | 50 | — | Extra/custom data |
| 11 | WOBOM_LINE^ | INTEGER | 2 | — | Line number (computed) |
| 12 | WOBOM_OPER | INTEGER | 2 | — | Operation number where component is used |
| 13 | WOBOM_OPTION | STRING | 1 | — | Option/feature flag |
| 14 | WOBOM_QTYISSUED | NUMERIC | 8 | 4 | Quantity issued |
| 15 | WOBOM_QTYPER | NUMERIC | 8 | 8 | Quantity per assembly |
| 16 | WOBOM_REFERENCE | STRING | 20 | — | Design/BOM reference designator |
| 17 | WOBOM_REV | STRING | 5 | — | BOM revision |
| 18 | WOBOM_SCRAPQTY | NUMERIC | 8 | 8 | Scrap quantity allowance |
| 19 | WOBOM_SEQ | INTEGER | 2 | — | Sequence number |
| 20 | WOBOM_START | DATE | 4 | — | Start date |
| 21 | WOBOM_TOTQTY | NUMERIC | 8 | 4 | Total quantity required |
| 22 | WOBOM_UID | STRING | 30 | — | Unique identifier |
| 23 | WOBOM_UM | STRING | 3 | — | Unit of measure |
| 24 | WOBOM_VEND | STRING | 10 | — | Preferred vendor for component |
| 25 | WOBOM_WOPRE | NUMERIC | 8 | — | WO prefix |
| 26 | WOBOM_WOSUF | INTEGER | 2 | — | WO suffix |

## WOBOMHRM
**WO BILL OF MATERIAL REMARKS - ARCHIVE**

Identical schema to [WOBOMREM](#wobomrem) (WOBOM_RM_ prefix). Archived BOM remarks.

## WOBOMREM
**WO BILL OF MATERIAL REMARKS**

Fields: 7 | Prefix: WOBOM_RM_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_RM_COMP | STRING | 15 | — | Component part code |
| 2 | WOBOM_RM_LINE | INTEGER | 2 | — | Remark line number |
| 3 | WOBOM_RM_LINENM | INTEGER | 2 | — | BOM line number |
| 4 | WOBOM_RM_PARENT | STRING | 15 | — | Parent/assembly part code |
| 5 | WOBOM_RM_REMARK | STRING | 30 | — | Remark text |
| 6 | WOBOM_RM_WOPRE | NUMERIC | 8 | — | WO prefix |
| 7 | WOBOM_RM_WOSUF | INTEGER | 2 | — | WO suffix |

## WODATE
**WORK ORDER DATES**

Fields: 12 | Prefix: WODATE_

Scheduling date records linking sub-WOs to parent and top-level WOs.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WODATE_DELPRE | NUMERIC | 8 | — | Delivery WO prefix (FK to delivery WO) |
| 2 | WODATE_DELSUF | INTEGER | 2 | — | Delivery WO suffix |
| 3 | WODATE_EXTRA | STRING | 100 | — | Extra/custom data |
| 4 | WODATE_FINISH | DATE | 4 | — | Scheduled finish date |
| 5 | WODATE_PARPRE | NUMERIC | 8 | — | Parent WO prefix |
| 6 | WODATE_PARSUF | INTEGER | 2 | — | Parent WO suffix |
| 7 | WODATE_QTY | NUMERIC | 8 | 2 | Quantity for this date entry |
| 8 | WODATE_START | DATE | 4 | — | Scheduled start date |
| 9 | WODATE_TOPPRE | NUMERIC | 8 | — | Top-level WO prefix |
| 10 | WODATE_TOPSUF | INTEGER | 2 | — | Top-level WO suffix |
| 11 | WODATE_WOPRE | NUMERIC | 8 | — | This WO prefix |
| 12 | WODATE_WOSUF | INTEGER | 2 | — | This WO suffix |

## WOEXCHG
**WORK ORDER EXTRA CHARGES**

Fields: 10 | Prefix: MTWO_EX_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_EX_CHG | NUMERIC | 8 | 6 | Charge amount |
| 2 | MTWO_EX_CHGDESC | STRING | 30 | — | Charge description |
| 3 | MTWO_EX_DATE | DATE | 4 | — | Charge date |
| 4 | MTWO_EX_DESC | STRING | 30 | — | General description |
| 5 | MTWO_EX_GLACCT | STRING | 10 | — | GL account for charge |
| 6 | MTWO_EX_GLDPT | STRING | 4 | — | GL department for charge |
| 7 | MTWO_EX_OP | INTEGER | 2 | — | Operation number |
| 8 | MTWO_EX_PROD | STRING | 15 | — | Product/assembly code |
| 9 | MTWO_EX_WOPRE | NUMERIC | 8 | — | WO prefix |
| 10 | MTWO_EX_WOSUF | INTEGER | 2 | — | WO suffix |

## WOHBOM
**WORK ORDER BILL OF MATERIAL - ARCHIVE**

Identical schema to [WOBOM](#wobom) (WOBOM_ prefix). Archived WO BOM.

## WOHDATE
**WORK ORDER DATES - ARCHIVE**

Identical schema to [WODATE](#wodate) (WODATE_ prefix). Archived WO date records.

## WOHEXCHG
**WORK ORDER EXTRA CHARGES - ARCHIVE**

Identical schema to [WOEXCHG](#woexchg) (MTWO_EX_ prefix). Archived WO extra charges.

## WOHLABOR
**LABOR TRANSACTIONS - ARCHIVE**

Identical schema to [WOLABOR](#wolabor) (MTWOLA_ prefix). Archived labor transactions.

## WOHMAT
**MATERIAL TRANSACTIONS - ARCHIVE**

Identical schema to [WOMAT](#womat) (WOMAT_ + MTWO_PRODCODE prefix). Archived material transactions.

## WOHRECV
**WORK ORDER RECEIPTS - ARCHIVE**

Identical schema to [WORECV](#worecv) (MTWOR_ prefix). Archived WO receipts.

## WOHROUT
**WORK ORDER ROUTING - ARCHIVE**

Identical schema to [WOROUT](#worout) (MTWORO_ prefix). Archived WO routing.

## WOLABOR
**LABOR TRANSACTIONS**

Fields: 45 | Prefix: MTWOLA_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | Assembly part code |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | Assembly description |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | Audit trail string |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | Operation completed flag (Y/N) |
| 5 | MTWOLA_DATE | DATE | 4 | — | Transaction date |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | Secondary/end date |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | Break/deduct time |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | Primary employee number |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | Secondary employee number |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | Extra/custom data |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | Fixed overhead cost |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | Labor cost |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | Labor rate ($/hr) |
| 14 | MTWOLA_MACH | STRING | 4 | — | Machine number |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | Machine cost |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | Machine date |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | Miscellaneous cost |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | Misc charge description |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | Number of jobs/assemblies in crew |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | Operation number |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | Overtime team count |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | Parts completed count |
| 23 | MTWOLA_POSTED | STRING | 1 | — | Posted to GL flag (Y/N) |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | QC code |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | QC code description |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | Regular/overtime flag (R/O) |
| 27 | MTWOLA_REWORK | STRING | 1 | — | Rework flag (Y/N) |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | Run hours |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | Scrap code description |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | Scrap code |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | Scrapped quantity |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | Setup cost |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | Setup hours |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | Shift number |
| 35 | MTWOLA_START | TIME | 4 | — | Start time |
| 36 | MTWOLA_STOP | TIME | 4 | — | Stop time |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | Team size (persons on job) |
| 38 | MTWOLA_TOOL | STRING | 15 | — | Tool number/code |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | Tool date |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | Transaction number |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | Variable overhead cost |
| 42 | MTWOLA_WC | STRING | 12 | — | Work center code |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | Work center date |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | WO prefix |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | WO suffix |

## WOMAT
**MATERIAL TRANSACTIONS**

Fields: 17 | Mixed prefix: MTWO_PRODCODE + WOMAT_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_PRODCODE | STRING | 15 | — | Parent/product code (assembly being built) |
| 2 | WOMAT_COST | NUMERIC | 8 | 2 | Material cost |
| 3 | WOMAT_DATE | DATE | 4 | — | Issue date |
| 4 | WOMAT_EXTRA | STRING | 50 | — | Extra/custom data |
| 5 | WOMAT_KIT | STRING | 1 | — | Kit issue flag (Y/N) |
| 6 | WOMAT_LOT | STRING | 15 | — | Lot ID issued |
| 7 | WOMAT_PCODE | STRING | 15 | — | Component part code issued |
| 8 | WOMAT_PDESC | STRING | 30 | — | Component description |
| 9 | WOMAT_PRODDESC | STRING | 30 | — | Product/assembly description |
| 10 | WOMAT_QTYISSUED | NUMERIC | 8 | 4 | Quantity issued |
| 11 | WOMAT_QTYSCRAP | NUMERIC | 8 | 2 | Scrap quantity |
| 12 | WOMAT_REF | STRING | 15 | — | Reference |
| 13 | WOMAT_SCDESC | STRING | 30 | — | Scrap code description |
| 14 | WOMAT_SCRAPCD | STRING | 2 | — | Scrap code |
| 15 | WOMAT_SERIAL | STRING | 25 | — | Serial number issued |
| 16 | WOMAT_WOPRE | NUMERIC | 8 | — | WO prefix |
| 17 | WOMAT_WOSUF | INTEGER | 2 | — | WO suffix |

## WORECV
**WORK ORDER RECEIPTS**

Fields: 11 | Prefix: MTWOR_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOR_ASSY | STRING | 15 | — | Assembly part code |
| 2 | MTWOR_AVGC | NUMERIC | 8 | 4 | Average cost at receipt |
| 3 | MTWOR_DATE | DATE | 4 | — | Receipt date |
| 4 | MTWOR_DESC | STRING | 30 | — | Assembly description |
| 5 | MTWOR_LOT | STRING | 15 | — | Lot ID assigned |
| 6 | MTWOR_QTY | NUMERIC | 8 | 2 | Quantity received/completed |
| 7 | MTWOR_REF | STRING | 15 | — | Reference |
| 8 | MTWOR_SERIAL | STRING | 25 | — | Serial number assigned |
| 9 | MTWOR_USESTD | STRING | 1 | — | Use standard cost flag (Y/N) |
| 10 | MTWOR_WOPRE | NUMERIC | 8 | — | WO prefix |
| 11 | MTWOR_WOSUF | INTEGER | 2 | — | WO suffix |

## WORKACHG
**ARCHIVED WO CHANGES**

Identical schema to [WORKCHG](#workchg) (WO_CHG_ prefix). Archived WO change audit log.

## WORKCHG
**WO CHANGES**

Fields: 25 | Prefix: WO_CHG_

Change audit log: A_ = after-value, B_ = before-value fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WO_CHG_AASD | DATE | 4 | — | After: actual ship/complete date |
| 2 | WO_CHG_ACLASS | STRING | 1 | — | After: class code |
| 3 | WO_CHG_ADDATE | DATE | 4 | — | After: due date |
| 4 | WO_CHG_ADESC | STRING | 30 | — | After: description |
| 5 | WO_CHG_AEXTRA | STRING | 150 | — | After: extra data |
| 6 | WO_CHG_AFDATE | DATE | 4 | — | After: finish date |
| 7 | WO_CHG_APRIO | STRING | 1 | — | After: priority |
| 8 | WO_CHG_AQTY | NUMERIC | 8 | 2 | After: quantity |
| 9 | WO_CHG_ASDATE | DATE | 4 | — | After: start date |
| 10 | WO_CHG_ASTATUS | STRING | 1 | — | After: status |
| 11 | WO_CHG_BASD | DATE | 4 | — | Before: actual ship/complete date |
| 12 | WO_CHG_BCLASS | STRING | 1 | — | Before: class code |
| 13 | WO_CHG_BDDATE | DATE | 4 | — | Before: due date |
| 14 | WO_CHG_BDESC | STRING | 30 | — | Before: description |
| 15 | WO_CHG_BEXTRA | STRING | 150 | — | Before: extra data |
| 16 | WO_CHG_BFDATE | DATE | 4 | — | Before: finish date |
| 17 | WO_CHG_BPRIO | STRING | 1 | — | Before: priority |
| 18 | WO_CHG_BQTY | NUMERIC | 8 | 2 | Before: quantity |
| 19 | WO_CHG_BSDATE | DATE | 4 | — | Before: start date |
| 20 | WO_CHG_BSTATUS | STRING | 1 | — | Before: status |
| 21 | WO_CHG_CDATE | DATE | 4 | — | Change date |
| 22 | WO_CHG_CODE | STRING | 15 | — | WO item/assembly code |
| 23 | WO_CHG_USER | STRING | 15 | — | User who made the change |
| 24 | WO_CHG_WOPRE | NUMERIC | 8 | — | WO prefix |
| 25 | WO_CHG_WOSUF | INTEGER | 2 | — | WO suffix |

## WORKCTR
**WORK CENTERS**

Fields: 25 | Prefix: MTWC_

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWC_^UTIL | NUMERIC | 8 | 2 | Utilization rate (computed) |
| 2 | MTWC_AVGQTIME | INTEGER | 2 | — | Average queue time (days) |
| 3 | MTWC_COST_LB | NUMERIC | 8 | 6 | Labor burden cost rate |
| 4 | MTWC_DEPT | STRING | 4 | — | Department code |
| 5 | MTWC_DEPTDESC | STRING | 30 | — | Department description |
| 6 | MTWC_EST_VOVHD | NUMERIC | 8 | 4 | Estimated variable overhead rate |
| 7 | MTWC_EXTRA | STRING | 100 | — | Extra/custom data |
| 8 | MTWC_FOVHD | NUMERIC | 8 | 4 | Fixed overhead rate ($/hr) |
| 9 | MTWC_HRS_SHIFT | INTEGER | 2 | — | Hours per shift |
| 10 | MTWC_HRSWEEK | INTEGER | 2 | — | Hours per week |
| 11 | MTWC_LABOR | NUMERIC | 8 | 4 | Labor rate ($/hr) |
| 12 | MTWC_LEAD | INTEGER | 2 | — | Lead time (days) |
| 13 | MTWC_LEVEL_YN | STRING | 1 | — | Level-loaded scheduling flag (Y/N) |
| 14 | MTWC_MACHINE | NUMERIC | 8 | 4 | Machine rate ($/hr) |
| 15 | MTWC_MIN_CHG | NUMERIC | 8 | 2 | Minimum charge |
| 16 | MTWC_OUTPROC | STRING | 1 | — | Outside processing work center flag (Y/N) |
| 17 | MTWC_PARENT_WC | STRING | 12 | — | Parent work center code |
| 18 | MTWC_PARENT_YN | STRING | 1 | — | Has parent work center flag (Y/N) |
| 19 | MTWC_QPR1 | INTEGER | 2 | — | Queue priority code 1 |
| 20 | MTWC_QPR2 | INTEGER | 2 | — | Queue priority code 2 |
| 21 | MTWC_QPR3 | INTEGER | 2 | — | Queue priority code 3 |
| 22 | MTWC_SETUP | NUMERIC | 8 | 4 | Setup rate ($/hr) |
| 23 | MTWC_VOVHD | NUMERIC | 8 | 4 | Variable overhead rate ($/hr) |
| 24 | MTWC_WC | STRING | 12 | — | Work center code |
| 25 | MTWC_WCDESC | STRING | 30 | — | Work center description |

## WORKHORD
**WORK ORDER HEADER - ARCHIVE**

Identical schema to [WORKORD](#workord) (MTWO_WIP_ + MTWO_CUST* prefix). Archived WO headers.

## WORKORD
**WORK ORDER HEADER**

Fields: 82 | Prefix: MTWO_WIP_ (plus MTWO_CUSTCODE, MTWO_CUSTNAME)

Variance fields: `^` suffix = budgeted amount; `V` suffix = variance (actual minus budget).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_CUSTCODE | STRING | 10 | — | Customer Code |
| 2 | MTWO_CUSTNAME | STRING | 25 | — | Customer Name |
| 3 | MTWO_WIP_AEXTRA | NUMERIC | 8 | 2 | Actual extra/misc cost |
| 4 | MTWO_WIP_AFIN | DATE | 4 | — | Actual Finish Date |
| 5 | MTWO_WIP_AFOVHD | NUMERIC | 8 | 2 | Actual fixed overhead cost |
| 6 | MTWO_WIP_ALABOR | NUMERIC | 8 | 2 | Actual Labor Cost |
| 7 | MTWO_WIP_AMAT | NUMERIC | 8 | 2 | Actual Material Cost |
| 8 | MTWO_WIP_AMISC | NUMERIC | 8 | 2 | Actual misc cost |
| 9 | MTWO_WIP_AOTH | NUMERIC | 8 | 2 | Actual other/subcontract cost |
| 10 | MTWO_WIP_AOUTPR | NUMERIC | 8 | 2 | Actual Outside Process Cost |
| 11 | MTWO_WIP_ASETUP | NUMERIC | 8 | 2 | Actual Setup Cost |
| 12 | MTWO_WIP_ASTART | DATE | 4 | — | Actual Start Date |
| 13 | MTWO_WIP_ATOTAL | NUMERIC | 8 | 2 | Actual Total Cost |
| 14 | MTWO_WIP_AVOVHD | NUMERIC | 8 | 2 | Actual variable overhead cost |
| 15 | MTWO_WIP_BLANK | STRING | 1 | — | Blank/reserved field |
| 16 | MTWO_WIP_CHGORD | INTEGER | 2 | — | Change order number |
| 17 | MTWO_WIP_CODE | STRING | 15 | — | Item/assembly code |
| 18 | MTWO_WIP_COMQTY | NUMERIC | 8 | 2 | Completed quantity |
| 19 | MTWO_WIP_CONTAT | STRING | 25 | — | Contact / attention name |
| 20 | MTWO_WIP_CUSORD | STRING | 25 | — | Customer order number |
| 21 | MTWO_WIP_DDATE | DATE | 4 | — | Due date |
| 22 | MTWO_WIP_DESC | STRING | 30 | — | Assembly description |
| 23 | MTWO_WIP_EEXTRA | NUMERIC | 8 | 2 | Estimated extra/misc cost |
| 24 | MTWO_WIP_EFOVHD | NUMERIC | 8 | 2 | Estimated fixed overhead cost |
| 25 | MTWO_WIP_ELABOR | NUMERIC | 8 | 2 | Est. Labor Cost |
| 26 | MTWO_WIP_EMAT | NUMERIC | 8 | 2 | Est. Material Cost |
| 27 | MTWO_WIP_EMISC | NUMERIC | 8 | 2 | Estimated misc cost |
| 28 | MTWO_WIP_EOTH | NUMERIC | 8 | 2 | Estimated other/subcontract cost |
| 29 | MTWO_WIP_EOUTPR | NUMERIC | 8 | 2 | Est. Outside Process Cost |
| 30 | MTWO_WIP_ESETUP | NUMERIC | 8 | 2 | Est. Setup Cost |
| 31 | MTWO_WIP_EST | NUMERIC | 8 | — | Estimated cost flag/total |
| 32 | MTWO_WIP_ETOT | NUMERIC | 8 | 2 | Est. Total Cost |
| 33 | MTWO_WIP_EXTRA^ | NUMERIC | 8 | 2 | Extra cost (budgeted) |
| 34 | MTWO_WIP_EXTRAV | NUMERIC | 8 | 2 | Extra cost variance |
| 35 | MTWO_WIP_FOVHD^ | NUMERIC | 8 | 2 | Fixed overhead cost (budgeted) |
| 36 | MTWO_WIP_FOVHDV | NUMERIC | 8 | 2 | Fixed overhead variance |
| 37–46 | MTWO_WIP_INSTR_1..10 | STRING | 60 | — | Work order instruction lines 1–10 |
| 47 | MTWO_WIP_LABOR^ | NUMERIC | 8 | 2 | Labor cost (budgeted) |
| 48 | MTWO_WIP_LABORV | NUMERIC | 8 | 2 | Labor cost variance |
| 49 | MTWO_WIP_LOC | STRING | 10 | — | Warehouse location |
| 50 | MTWO_WIP_LOCK | STRING | 1 | — | Lock flag (Y/N) |
| 51 | MTWO_WIP_MAT^ | NUMERIC | 8 | 2 | Material cost (budgeted) |
| 52 | MTWO_WIP_MATV | NUMERIC | 8 | 2 | Material cost variance |
| 53 | MTWO_WIP_MISC^ | NUMERIC | 8 | 2 | Misc cost (budgeted) |
| 54 | MTWO_WIP_MISCV | NUMERIC | 8 | 2 | Misc cost variance |
| 55 | MTWO_WIP_MULT | STRING | 1 | — | Multiplier/factor flag |
| 56 | MTWO_WIP_OTHPER | NUMERIC | 8 | 2 | Other/subcontract percent |
| 57 | MTWO_WIP_OTHV | NUMERIC | 8 | 2 | Other cost variance |
| 58 | MTWO_WIP_OUTPR^ | NUMERIC | 8 | 2 | Outside processing cost (budgeted) |
| 59 | MTWO_WIP_OUTPRV | NUMERIC | 8 | 2 | Outside processing cost variance |
| 60 | MTWO_WIP_PPRCE | NUMERIC | 8 | 4 | Part price (SO-linked sell price) |
| 61 | MTWO_WIP_PROJ | STRING | 15 | — | Project code |
| 62 | MTWO_WIP_PRTY | STRING | 1 | — | Priority |
| 63 | MTWO_WIP_QCONV | STRING | 1 | — | Quantity conversion flag |
| 64 | MTWO_WIP_SCHED_1 | STRING | 1 | — | Schedule flag 1 |
| 65 | MTWO_WIP_SCHED_2 | STRING | 1 | — | Schedule flag 2 |
| 66 | MTWO_WIP_SCONV | STRING | 1 | — | Size conversion flag |
| 67 | MTWO_WIP_SETUP^ | NUMERIC | 8 | 2 | Setup cost (budgeted) |
| 68 | MTWO_WIP_SETUPV | NUMERIC | 8 | 2 | Setup cost variance |
| 69 | MTWO_WIP_SFIN | DATE | 4 | — | Scheduled Finish Date |
| 70 | MTWO_WIP_SOLINE | NUMERIC | 8 | — | SO line number |
| 71 | MTWO_WIP_SONUM | NUMERIC | 8 | — | SO Number |
| 72 | MTWO_WIP_SQTY | NUMERIC | 8 | 2 | Start Quantity |
| 73 | MTWO_WIP_SSTART | DATE | 4 | — | Scheduled Start Date |
| 74 | MTWO_WIP_STATUS | STRING | 1 | — | Status |
| 75 | MTWO_WIP_TOT^ | NUMERIC | 8 | 2 | Total cost (budgeted) |
| 76 | MTWO_WIP_TOTV | NUMERIC | 8 | 2 | Total cost variance |
| 77 | MTWO_WIP_USERCD | STRING | 1 | — | User-defined class code |
| 78 | MTWO_WIP_VOVHD | NUMERIC | 8 | 2 | Variable overhead cost (actual) |
| 79 | MTWO_WIP_VOVHD^ | NUMERIC | 8 | 2 | Variable overhead cost (budgeted) |
| 80 | MTWO_WIP_VOVHDV | NUMERIC | 8 | 2 | Variable overhead cost variance |
| 81 | MTWO_WIP_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 82 | MTWO_WIP_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOROCHG
**WO ROUTING CHANGES**

Fields: 24 | Prefix: WORO_CHG_

Change audit log for routing operations: A_ = after-value, B_ = before-value fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WORO_CHG_AEXTRA | STRING | 100 | — | After: extra data |
| 2 | WORO_CHG_ALONG | NUMERIC | 8 | 7 | After: long-time/queue hours |
| 3 | WORO_CHG_AMACH | STRING | 4 | — | After: machine number |
| 4 | WORO_CHG_ANUMP | NUMERIC | 8 | 2 | After: number of persons |
| 5 | WORO_CHG_AOPER | STRING | 1 | — | After: operation type flag |
| 6 | WORO_CHG_ASETUP | TIME | 4 | — | After: setup time |
| 7 | WORO_CHG_ASTDT | STRING | 1 | — | After: standard time flag |
| 8 | WORO_CHG_ATOOL | STRING | 15 | — | After: tool code |
| 9 | WORO_CHG_AWC | STRING | 12 | — | After: work center |
| 10 | WORO_CHG_BEXTRA | STRING | 100 | — | Before: extra data |
| 11 | WORO_CHG_BLONG | NUMERIC | 8 | 7 | Before: long-time/queue hours |
| 12 | WORO_CHG_BMATCH | STRING | 4 | — | Before: machine number (source field: BMATCH) |
| 13 | WORO_CHG_BNUMP | NUMERIC | 8 | 2 | Before: number of persons |
| 14 | WORO_CHG_BSETUP | TIME | 4 | — | Before: setup time |
| 15 | WORO_CHG_BSTDT | STRING | 1 | — | Before: standard time flag |
| 16 | WORO_CHG_BTOOL | STRING | 15 | — | Before: tool code |
| 17 | WORO_CHG_BWC | STRING | 12 | — | Before: work center |
| 18 | WORO_CHG_CDATE | DATE | 4 | — | Change date |
| 19 | WORO_CHG_DOPER | STRING | 1 | — | Deleted operation flag |
| 20 | WORO_CHG_OPER | INTEGER | 2 | — | Operation number |
| 21 | WORO_CHG_PART | STRING | 15 | — | Part/assembly code |
| 22 | WORO_CHG_USER | STRING | 15 | — | User who made the change |
| 23 | WORO_CHG_WOPRE | NUMERIC | 8 | — | WO prefix |
| 24 | WORO_CHG_WOSUF | INTEGER | 2 | — | WO suffix |

## WOROUT
**WORK ORDER ROUTING**

Fields: 83 | Prefix: MTWORO_

Per-operation routing step. Cost fields: A_ = actual, E_ = estimated.
INSTR_1..15 = operation instructions.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | Completed flag (computed) |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | Actual run hours |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | Actual fixed overhead cost |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | Actual labor cost |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | Actual machine cost |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | Actual outside process cost |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | Actual setup cost |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | Actual setup hours |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | Actual variable overhead cost |
| 10 | MTWORO_CODE | STRING | 15 | — | Item/assembly code |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | Contention count (scheduling conflicts) |
| 12 | MTWORO_DEPT | STRING | 3 | — | Department code |
| 13 | MTWORO_DESC | STRING | 30 | — | Operation description |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | Estimated fixed overhead cost |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | Estimated labor cost |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | Estimated machine cost |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | Estimated outside process cost |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | Estimated setup cost |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | Estimated setup hours |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | Estimated setup time (TIME type) |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | Estimated run hours |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | Estimated variable overhead cost |
| 23 | MTWORO_EXTRA | STRING | 150 | — | Extra/custom data |
| 24 | MTWORO_FINISH | DATE | 4 | — | Scheduled finish date |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | Alternate/revised finish date |
| 26 | MTWORO_FINISHED | DATE | 4 | — | Actual finished date |
| 27–41 | MTWORO_INSTR_1..15 | STRING | 60 | — | Operation instruction lines 1–15 |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | Lead time (days) |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | Long/queue time (hours, high precision) |
| 44 | MTWORO_MACHNO | STRING | 4 | — | Machine number |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | Mode: per-part or per-hour flag |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | Minimum charge |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | Actual misc cost |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | Estimated misc cost |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | Misc charge description |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | Negative overlap (hours; operation starts before prior finishes) |
| 51 | MTWORO_NUM | INTEGER | 2 | — | Routing step number |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | Number of persons (crew size) |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | Number of processes (machines in parallel) |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | Operation template pointer (computed) |
| 55 | MTWORO_OPER | INTEGER | 2 | — | Operation number |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | Secondary operation number |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | Operation description (alt field) |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | Positive overlap time (hours) |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | Parts per hour (production rate) |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | Piece rate ($/piece) |
| 61 | MTWORO_PO | NUMERIC | 8 | — | PO number (outside processing) |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | Production rate (parts/hour) |
| 63 | MTWORO_PRINT | STRING | 1 | — | Printed flag (Y/N) |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | Routing priority code |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | Project number (outside processing) |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | Quantity completed at this operation |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | Scheduled work center |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | Scrapped quantity |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | Start quantity at operation |
| 70 | MTWORO_START | DATE | 4 | — | Scheduled start date |
| 71 | MTWORO_STARTED | DATE | 4 | — | Actual started date |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | Standard time basis flag (hrs vs pieces) |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | Started quantity |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | Time per piece (TIME type) |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | Time per part, alternate (TIME type) |
| 76 | MTWORO_TOOL | STRING | 15 | — | Tool number/code |
| 77 | MTWORO_TYPE | STRING | 1 | — | Routing type (L=labor, M=machine, O=outside) |
| 78 | MTWORO_VEND | STRING | 10 | — | Vendor code (outside processing) |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | Vendor name (outside processing) |
| 80 | MTWORO_WC | STRING | 12 | — | Work center code |
| 81 | MTWORO_WCDESC | STRING | 30 | — | Work center description |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOROUTMP
**AGGREGATE WO ROUTINGS (Temporary)**

Identical schema to [WOROUT](#worout) (MTWORO_ prefix). Temporary aggregate routing view for scheduling.
