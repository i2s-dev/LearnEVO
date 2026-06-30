# DC — Document Control: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKDCCLAB
**DC POST LOCK FILE**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | — |
| 2 | LAB_ADT_OUT | STRING | 100 | — | — |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | — |
| 4 | LAB_APPROVAL | STRING | 1 | — | — |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | — |
| 7 | LAB_DATE2 | DATE | 4 | — | — |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | — |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | — |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | — |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | — |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | — |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | — |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | — |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | — |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | — |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | — |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | — |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | — |
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
| 1 | LAB_ADT_IN | STRING | 100 | — | — |
| 2 | LAB_ADT_OUT | STRING | 100 | — | — |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | — |
| 4 | LAB_APPROVAL | STRING | 1 | — | — |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | — |
| 7 | LAB_DATE2 | DATE | 4 | — | — |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | — |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | — |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | — |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | — |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | — |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | — |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | — |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | — |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | — |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | — |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | — |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | — |
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
| 1 | LAB_ADT_IN | STRING | 100 | — | — |
| 2 | LAB_ADT_OUT | STRING | 100 | — | — |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | — |
| 4 | LAB_APPROVAL | STRING | 1 | — | — |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | — |
| 7 | LAB_DATE2 | DATE | 4 | — | — |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | — |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | — |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | — |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | — |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | — |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | — |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | — |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | — |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | — |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | — |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | — |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | — |
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
| 1 | LAB_ADT_IN | STRING | 100 | — | — |
| 2 | LAB_ADT_OUT | STRING | 100 | — | — |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | — |
| 4 | LAB_APPROVAL | STRING | 1 | — | — |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | — |
| 7 | LAB_DATE2 | DATE | 4 | — | — |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | — |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | — |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | — |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | — |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | — |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | — |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | — |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | — |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | — |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | — |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | — |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | — |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## BKDCSHFT
**DC SHIFTS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKDC_SH_BRK1IN_1 | TIME | 4 | — | — |
| 2 | BKDC_SH_BRK1IN_2 | TIME | 4 | — | — |
| 3 | BKDC_SH_BRK1IN_3 | TIME | 4 | — | — |
| 4 | BKDC_SH_BRK1OUT_1 | TIME | 4 | — | — |
| 5 | BKDC_SH_BRK1OUT_2 | TIME | 4 | — | — |
| 6 | BKDC_SH_BRK1OUT_3 | TIME | 4 | — | — |
| 7 | BKDC_SH_BRK2IN_1 | TIME | 4 | — | — |
| 8 | BKDC_SH_BRK2IN_2 | TIME | 4 | — | — |
| 9 | BKDC_SH_BRK2IN_3 | TIME | 4 | — | — |
| 10 | BKDC_SH_BRK2OUT_1 | TIME | 4 | — | — |
| 11 | BKDC_SH_BRK2OUT_2 | TIME | 4 | — | — |
| 12 | BKDC_SH_BRK2OUT_3 | TIME | 4 | — | — |
| 13 | BKDC_SH_BUFFER_1 | TIME | 4 | — | — |
| 14 | BKDC_SH_BUFFER_2 | TIME | 4 | — | — |
| 15 | BKDC_SH_BUFFER_3 | TIME | 4 | — | — |
| 16 | BKDC_SH_EXTRA | STRING | 50 | — | Extra |
| 17 | BKDC_SH_FIN_1 | TIME | 4 | — | — |
| 18 | BKDC_SH_FIN_2 | TIME | 4 | — | — |
| 19 | BKDC_SH_FIN_3 | TIME | 4 | — | — |
| 20 | BKDC_SH_FINBUF_1 | TIME | 4 | — | — |
| 21 | BKDC_SH_FINBUF_2 | TIME | 4 | — | — |
| 22 | BKDC_SH_FINBUF_3 | TIME | 4 | — | — |
| 23 | BKDC_SH_LUNCHIN_1 | TIME | 4 | — | — |
| 24 | BKDC_SH_LUNCHIN_2 | TIME | 4 | — | — |
| 25 | BKDC_SH_LUNCHIN_3 | TIME | 4 | — | — |
| 26 | BKDC_SH_LUNCHOT_1 | TIME | 4 | — | — |
| 27 | BKDC_SH_LUNCHOT_2 | TIME | 4 | — | — |
| 28 | BKDC_SH_LUNCHOT_3 | TIME | 4 | — | — |
| 29 | BKDC_SH_NAME1 | STRING | 25 | — | Shift Name 1 |
| 30 | BKDC_SH_NAME2 | STRING | 25 | — | Shift Name 2 |
| 31 | BKDC_SH_NAME3 | STRING | 25 | — | Shift Name 3 |
| 32 | BKDC_SH_START_1 | TIME | 4 | — | — |
| 33 | BKDC_SH_START_2 | TIME | 4 | — | — |
| 34 | BKDC_SH_START_3 | TIME | 4 | — | — |

## BKDCTLAB
**TEMPORARY DC LABOR TRANSACTIONS**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | LAB_ADT_IN | STRING | 100 | — | — |
| 2 | LAB_ADT_OUT | STRING | 100 | — | — |
| 3 | LAB_ADT_SUPER | STRING | 100 | — | — |
| 4 | LAB_APPROVAL | STRING | 1 | — | — |
| 5 | LAB_DATE | DATE | 4 | — | Date |
| 6 | LAB_DATE1 | DATE | 4 | — | — |
| 7 | LAB_DATE2 | DATE | 4 | — | — |
| 8 | LAB_EMP | INTEGER | 2 | — | Employee Number |
| 9 | LAB_ESSDATE | DATE | 4 | — | — |
| 10 | LAB_EXTRA | STRING | 50 | — | Extra |
| 11 | LAB_FINISH | TIME | 4 | — | Finish Time |
| 12 | LAB_JCNUM | STRING | 12 | — | — |
| 13 | LAB_NOJOBS | INTEGER | 2 | — | No of Jobs |
| 14 | LAB_OPER | INTEGER | 2 | — | Operation Sequence |
| 15 | LAB_PARTS | NUMERIC | 8 | 2 | Parts Produced |
| 16 | LAB_POSTED | STRING | 1 | — | Posted Y/N |
| 17 | LAB_REGOVER | STRING | 1 | — | Regular or Overtime |
| 18 | LAB_RUNHRS | NUMERIC | 8 | 2 | Run Hours |
| 19 | LAB_SCRAPCD_1 | STRING | 2 | — | — |
| 20 | LAB_SCRAPCD_2 | STRING | 2 | — | — |
| 21 | LAB_SCRAPCD_3 | STRING | 2 | — | — |
| 22 | LAB_SCRAPCD_4 | STRING | 2 | — | — |
| 23 | LAB_SCRAPCD_5 | STRING | 2 | — | — |
| 24 | LAB_SCRAPPED | NUMERIC | 8 | 2 | Parts Scrapped |
| 25 | LAB_SCRAPQTY_1 | NUMERIC | 8 | 2 | — |
| 26 | LAB_SCRAPQTY_2 | NUMERIC | 8 | 2 | — |
| 27 | LAB_SCRAPQTY_3 | NUMERIC | 8 | 2 | — |
| 28 | LAB_SCRAPQTY_4 | NUMERIC | 8 | 2 | — |
| 29 | LAB_SCRAPQTY_5 | NUMERIC | 8 | 2 | — |
| 30 | LAB_SETUPHRS | NUMERIC | 8 | 2 | Setup Hours |
| 31 | LAB_SHIFT | INTEGER | 2 | — | Shift |
| 32 | LAB_START | TIME | 4 | — | Start Time |
| 33 | LAB_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 34 | LAB_WOSUF | INTEGER | 2 | — | Work Order Suffix |
