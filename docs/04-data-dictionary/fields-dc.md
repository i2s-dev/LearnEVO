# DC — Document Control: Field Reference

Status: verified-schema + completed field meanings (Pass 574d, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKDCCLAB
**DC POST LOCK FILE**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | Audit trail — login record (who scanned in, timestamp) |
| 2 | LAB_ADT_OUT | STRING | 100 | — | Audit trail — logout record (who scanned out, timestamp) |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | Supervisor audit record (supervisor override or approval log) |
| 4 | LAB_APPROVAL | STRING | 1 | — | Supervisor approval flag: `Y`=approved, `N`=pending |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | Secondary date (e.g., shift date if different from scan date) |
| 7 | LAB_DATE2 | DATE | 4 | — | Tertiary date (e.g., pay period or posting period date) |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | Employee Self-Service (ESS) date — date entered via ESS terminal |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | Job/cost center number (alternate job reference for labor cost tracking) |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | Scrap reason code slot 1 (FK → SCRAP table) |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | Scrap reason code slot 2 |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | Scrap reason code slot 3 |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | Scrap reason code slot 4 |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | Scrap reason code slot 5 |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 1 |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 2 |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 3 |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 4 |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 5 |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## BKDCHLAB
**ARCHIVED DC LABOR TRANSACTIONS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | Audit trail — login record (who scanned in, timestamp) |
| 2 | LAB_ADT_OUT | STRING | 100 | — | Audit trail — logout record (who scanned out, timestamp) |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | Supervisor audit record (supervisor override or approval log) |
| 4 | LAB_APPROVAL | STRING | 1 | — | Supervisor approval flag: `Y`=approved, `N`=pending |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | Secondary date (e.g., shift date if different from scan date) |
| 7 | LAB_DATE2 | DATE | 4 | — | Tertiary date (e.g., pay period or posting period date) |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | Employee Self-Service (ESS) date — date entered via ESS terminal |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | Job/cost center number (alternate job reference for labor cost tracking) |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | Scrap reason code slot 1 (FK → SCRAP table) |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | Scrap reason code slot 2 |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | Scrap reason code slot 3 |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | Scrap reason code slot 4 |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | Scrap reason code slot 5 |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 1 |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 2 |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 3 |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 4 |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 5 |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## BKDCLAB
**POSTED DC LABOR TRANSACTIONS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | Audit trail — login record (who scanned in, timestamp) |
| 2 | LAB_ADT_OUT | STRING | 100 | — | Audit trail — logout record (who scanned out, timestamp) |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | Supervisor audit record (supervisor override or approval log) |
| 4 | LAB_APPROVAL | STRING | 1 | — | Supervisor approval flag: `Y`=approved, `N`=pending |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | Secondary date (e.g., shift date if different from scan date) |
| 7 | LAB_DATE2 | DATE | 4 | — | Tertiary date (e.g., pay period or posting period date) |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | Employee Self-Service (ESS) date — date entered via ESS terminal |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | Job/cost center number (alternate job reference for labor cost tracking) |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | Scrap reason code slot 1 (FK → SCRAP table) |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | Scrap reason code slot 2 |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | Scrap reason code slot 3 |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | Scrap reason code slot 4 |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | Scrap reason code slot 5 |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 1 |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 2 |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 3 |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 4 |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 5 |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## BKDCPLAB
**UNPOSTED DC LABOR TRANSACTIONS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | Audit trail — login record (who scanned in, timestamp) |
| 2 | LAB_ADT_OUT | STRING | 100 | — | Audit trail — logout record (who scanned out, timestamp) |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | Supervisor audit record (supervisor override or approval log) |
| 4 | LAB_APPROVAL | STRING | 1 | — | Supervisor approval flag: `Y`=approved, `N`=pending |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | Secondary date (e.g., shift date if different from scan date) |
| 7 | LAB_DATE2 | DATE | 4 | — | Tertiary date (e.g., pay period or posting period date) |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | Employee Self-Service (ESS) date — date entered via ESS terminal |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | Job/cost center number (alternate job reference for labor cost tracking) |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | Scrap reason code slot 1 (FK → SCRAP table) |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | Scrap reason code slot 2 |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | Scrap reason code slot 3 |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | Scrap reason code slot 4 |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | Scrap reason code slot 5 |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 1 |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 2 |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 3 |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 4 |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 5 |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## BKDCSHFT
**DC SHIFTS** — shift schedule configuration (3 shifts × timing)

Fields: 34 | Key: singleton (one record)

Defines start/end times, break periods, and lunch periods for up to 3 shifts.
Suffix _1/_2/_3 = Shift 1/Shift 2/Shift 3. At i2 Systems, BKDCSHFT=1.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKDC_SH_BRK1IN_1 | TIME | 4 | — | Break 1 start time — Shift 1 |
| 2 | BKDC_SH_BRK1IN_2 | TIME | 4 | — | Break 1 start time — Shift 2 |
| 3 | BKDC_SH_BRK1IN_3 | TIME | 4 | — | Break 1 start time — Shift 3 |
| 4 | BKDC_SH_BRK1OUT_1 | TIME | 4 | — | Break 1 end time — Shift 1 |
| 5 | BKDC_SH_BRK1OUT_2 | TIME | 4 | — | Break 1 end time — Shift 2 |
| 6 | BKDC_SH_BRK1OUT_3 | TIME | 4 | — | Break 1 end time — Shift 3 |
| 7 | BKDC_SH_BRK2IN_1 | TIME | 4 | — | Break 2 start time — Shift 1 |
| 8 | BKDC_SH_BRK2IN_2 | TIME | 4 | — | Break 2 start time — Shift 2 |
| 9 | BKDC_SH_BRK2IN_3 | TIME | 4 | — | Break 2 start time — Shift 3 |
| 10 | BKDC_SH_BRK2OUT_1 | TIME | 4 | — | Break 2 end time — Shift 1 |
| 11 | BKDC_SH_BRK2OUT_2 | TIME | 4 | — | Break 2 end time — Shift 2 |
| 12 | BKDC_SH_BRK2OUT_3 | TIME | 4 | — | Break 2 end time — Shift 3 |
| 13 | BKDC_SH_BUFFER_1 | TIME | 4 | — | Ramp-up buffer time at start of Shift 1 (grace period before overtime kicks in) |
| 14 | BKDC_SH_BUFFER_2 | TIME | 4 | — | Ramp-up buffer time at start of Shift 2 |
| 15 | BKDC_SH_BUFFER_3 | TIME | 4 | — | Ramp-up buffer time at start of Shift 3 |
| 16 | BKDC_SH_EXTRA | STRING | 50 | — | Extra |
| 17 | BKDC_SH_FIN_1 | TIME | 4 | — | Shift 1 finish/end time |
| 18 | BKDC_SH_FIN_2 | TIME | 4 | — | Shift 2 finish/end time |
| 19 | BKDC_SH_FIN_3 | TIME | 4 | — | Shift 3 finish/end time |
| 20 | BKDC_SH_FINBUF_1 | TIME | 4 | — | Wind-down buffer at end of Shift 1 |
| 21 | BKDC_SH_FINBUF_2 | TIME | 4 | — | Wind-down buffer at end of Shift 2 |
| 22 | BKDC_SH_FINBUF_3 | TIME | 4 | — | Wind-down buffer at end of Shift 3 |
| 23 | BKDC_SH_LUNCHIN_1 | TIME | 4 | — | Lunch start time — Shift 1 |
| 24 | BKDC_SH_LUNCHIN_2 | TIME | 4 | — | Lunch start time — Shift 2 |
| 25 | BKDC_SH_LUNCHIN_3 | TIME | 4 | — | Lunch start time — Shift 3 |
| 26 | BKDC_SH_LUNCHOT_1 | TIME | 4 | — | Lunch end/out time — Shift 1 |
| 27 | BKDC_SH_LUNCHOT_2 | TIME | 4 | — | Lunch end/out time — Shift 2 |
| 28 | BKDC_SH_LUNCHOT_3 | TIME | 4 | — | Lunch end/out time — Shift 3 |
| 29 | BKDC_SH_NAME1 | STRING | 25 | — | Shift Name 1 |
| 30 | BKDC_SH_NAME2 | STRING | 25 | — | Shift Name 2 |
| 31 | BKDC_SH_NAME3 | STRING | 25 | — | Shift Name 3 |
| 32 | BKDC_SH_START_1 | TIME | 4 | — | Shift 1 start time |
| 33 | BKDC_SH_START_2 | TIME | 4 | — | Shift 2 start time |
| 34 | BKDC_SH_START_3 | TIME | 4 | — | Shift 3 start time |

**Confidence: 82/100** — LAB_* pipeline table architecture (5 identical tables: unposted/lock/posted/history/temp)
confirmed from Pass 130; LAB_ADT_*/ESSDATE/JCNUM meanings inferred from DC module context; BKDCSHFT
3-shift timing structure clear from field naming; exact LAB_REGOVER values (R/O vs Y/N) and LAB_APPROVAL
workflow require RWN decryption; DC module confirmed idle at i2 Systems (BKDCCFG=0).

## BKDCTLAB
**TEMPORARY DC LABOR TRANSACTIONS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | Audit trail — login record (who scanned in, timestamp) |
| 2 | LAB_ADT_OUT | STRING | 100 | — | Audit trail — logout record (who scanned out, timestamp) |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | Supervisor audit record (supervisor override or approval log) |
| 4 | LAB_APPROVAL | STRING | 1 | — | Supervisor approval flag: `Y`=approved, `N`=pending |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | Secondary date (e.g., shift date if different from scan date) |
| 7 | LAB_DATE2 | DATE | 4 | — | Tertiary date (e.g., pay period or posting period date) |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | Employee Self-Service (ESS) date — date entered via ESS terminal |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | Job/cost center number (alternate job reference for labor cost tracking) |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | Scrap reason code slot 1 (FK → SCRAP table) |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | Scrap reason code slot 2 |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | Scrap reason code slot 3 |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | Scrap reason code slot 4 |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | Scrap reason code slot 5 |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 1 |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 2 |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 3 |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 4 |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | Quantity scrapped under reason code 5 |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |
