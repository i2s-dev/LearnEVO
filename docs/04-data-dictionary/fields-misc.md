# Unassigned / Misc Tables: Field Reference

Status: verified-schema

Tables present in `Evo-DBA_File_Fields 052421.xlsx` with no module assignment.
Many are marked "NOT USED" in the source — may be legacy, temp, or inactive tables.

---

## AHSYLOG
**NOT USED**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | AHSY_USER_ACCES_1 | STRING | 1 | — | — |
| 2 | AHSY_USER_ACCES_10 | STRING | 1 | — | — |
| 3 | AHSY_USER_ACCES_11 | STRING | 1 | — | — |
| 4 | AHSY_USER_ACCES_12 | STRING | 1 | — | — |
| 5 | AHSY_USER_ACCES_13 | STRING | 1 | — | — |
| 6 | AHSY_USER_ACCES_14 | STRING | 1 | — | — |
| 7 | AHSY_USER_ACCES_15 | STRING | 1 | — | — |
| 8 | AHSY_USER_ACCES_16 | STRING | 1 | — | — |
| 9 | AHSY_USER_ACCES_17 | STRING | 1 | — | — |
| 10 | AHSY_USER_ACCES_18 | STRING | 1 | — | — |
| 11 | AHSY_USER_ACCES_19 | STRING | 1 | — | — |
| 12 | AHSY_USER_ACCES_2 | STRING | 1 | — | — |
| 13 | AHSY_USER_ACCES_20 | STRING | 1 | — | — |
| 14 | AHSY_USER_ACCES_3 | STRING | 1 | — | — |
| 15 | AHSY_USER_ACCES_4 | STRING | 1 | — | — |
| 16 | AHSY_USER_ACCES_5 | STRING | 1 | — | — |
| 17 | AHSY_USER_ACCES_6 | STRING | 1 | — | — |
| 18 | AHSY_USER_ACCES_7 | STRING | 1 | — | — |
| 19 | AHSY_USER_ACCES_8 | STRING | 1 | — | — |
| 20 | AHSY_USER_ACCES_9 | STRING | 1 | — | — |
| 21 | AHSY_USER_CTRL | STRING | 1 | — | — |
| 22 | AHSY_USER_LEVL | STRING | 2 | — | — |
| 23 | AHSY_USER_MENU | STRING | 4 | — | — |

## ARTTEMP
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKART_AMOUNT | NUMERIC | 8 | 2 | Amount |
| 2 | BKART_CHECK | NUMERIC | 8 | — | Check Number |
| 3 | BKART_CNTR | INTEGER | 2 | — | Transaction Counter - tied to Trans. Num. |
| 4 | BKART_CUST | STRING | 10 | — | Customer Code |
| 5 | BKART_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKART_ENTDATE | DATE | 4 | — | Date Entered |
| 7 | BKART_INVC | NUMERIC | 8 | — | Not used |
| 8 | BKART_NOTE | STRING | 1 | — | Note Y or Blank |
| 9 | BKART_POSTDATE | DATE | 4 | — | Post Date |
| 10 | BKART_TRXN | NUMERIC | 8 | — | Transaction Number |
| 11 | BKART_TRXNLINK | NUMERIC | 8 | — | Transaction Num - Link to BKARINVT |
| 12 | BKART_TYPE | STRING | 1 | — | Transaction Type O/P/A |

## BKABCUST
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAB_EXP | DATE | 4 | — | — |
| 2 | BKAB_PERIOD | INTEGER | 2 | — | — |
| 3 | BKAB_STAND_ALNE | STRING | 1 | — | — |
| 4 | BKAB_START | DATE | 4 | — | — |
| 5 | BKAB_WARNING | INTEGER | 2 | — | — |

## BKABVEND
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAB_REG_NAME | STRING | 25 | — | — |
| 2 | BKAB_SERIAL | NUMERIC | 8 | — | — |

## BKAPNOTE
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_NOTE_DATE | DATE | 4 | — | Date |
| 2 | BKAP_NOTE_ENTBY | STRING | 10 | — | Enter By |
| 3 | BKAP_NOTE_NOTES_1 | STRING | 76 | — | — |
| 4 | BKAP_NOTE_NOTES_2 | STRING | 76 | — | — |
| 5 | BKAP_NOTE_NOTES_3 | STRING | 76 | — | — |
| 6 | BKAP_NOTE_NOTES_4 | STRING | 76 | — | — |
| 7 | BKAP_NOTE_NOTES_5 | STRING | 76 | — | — |
| 8 | BKAP_NOTE_NOTES_6 | STRING | 76 | — | — |
| 9 | BKAP_NOTE_NOTES_7 | STRING | 76 | — | — |
| 10 | BKAP_NOTE_NOTES_8 | STRING | 76 | — | — |
| 11 | BKAP_NOTE_SRCH1 | STRING | 10 | — | Search 1 |
| 12 | BKAP_NOTE_SRCH2 | STRING | 10 | — | Search 2 |

## BKARCHKH
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_CHK_AMTPD | NUMERIC | 8 | 2 | Amount Payed |
| 2 | BKAP_CHK_CHKACT | INTEGER | 2 | — | Bank Account |
| 3 | BKAP_CHK_CHKDTE | DATE | 4 | — | Check Date |
| 4 | BKAP_CHK_DESC | STRING | 25 | — | Description |
| 5 | BKAP_CHK_DISC | NUMERIC | 8 | 2 | Discount |
| 6 | BKAP_CHK_INVAMT | NUMERIC | 8 | 2 | Invoice Amount |
| 7 | BKAP_CHK_INVDTE | DATE | 4 | — | Invoice Date |
| 8 | BKAP_CHK_INVNUM | STRING | 10 | — | Invoice/Voucer Number |
| 9 | BKAP_CHK_ISCUR | STRING | 3 | — | Currency |
| 10 | BKAP_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 11 | BKAP_CHK_TYPE | STRING | 1 | — | Type |
| 12 | BKAP_CHK_VNDCOD | STRING | 10 | — | Vendor Code |

## BKARDPST
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKARTXNB
**NOT USED**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## BKBMCNFG
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_CNFG_AUTO | STRING | 1 | — | — |
| 2 | BKBM_CNFG_GLACT | STRING | 10 | — | — |
| 3 | BKBM_CNFG_GLDPT | STRING | 4 | — | — |
| 4 | BKBM_CNFG_LABOR | STRING | 1 | — | — |
| 5 | BKBM_CNFG_NUM | NUMERIC | 8 | — | — |
| 6 | BKBM_CNFG_POST | STRING | 1 | — | — |
| 7 | BKBM_CNFG_ROLL | STRING | 1 | — | — |

## BKBMDIM
**BOM dimensions** — used by T7BMA/T7CCCITM/J7CCITEMSYNC. Stores length/width/height/weight dimensions per BOM item code.

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_DIM_COMP | STRING | 15 | — | Component Part Code |
| 2 | BKBM_DIM_EXTRA | STRING | 50 | — | Extra |
| 3 | BKBM_DIM_LINE | INTEGER | 2 | — | Line Number |
| 4 | BKBM_DIM_MACH | STRING | 4 | — | Machine |
| 5 | BKBM_DIM_PARENT | STRING | 15 | — | Parent Part Code |
| 6 | BKBM_DIM_PART_X | NUMERIC | 8 | 4 | Diminsion X |
| 7 | BKBM_DIM_PART_Y | NUMERIC | 8 | 4 | Diminsion Y |
| 8 | BKBM_DIM_REMN_X | NUMERIC | 8 | 4 | Remnant X |
| 9 | BKBM_DIM_REMN_Y | NUMERIC | 8 | 4 | Remnant Y |
| 10 | BKBM_DIM_TRIM_X | NUMERIC | 8 | 2 | Trim Dim X |
| 11 | BKBM_DIM_TRIM_Y | NUMERIC | 8 | 2 | Trim Dim Y |

## BKCMCTL1
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | — |

## BKCMCTL2
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | — |

## BKCMCTL3
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | — |

## BKCMCTL4
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | — |

## BKCMCTRL
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | — |

## BKCMDE
**NOT USED**

Fields: 41

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCT_ADD1 | STRING | 30 | — | Address Line 1 |
| 2 | BKCM_ACCT_ADD2 | STRING | 30 | — | Address Line 2 |
| 3 | BKCM_ACCT_ADD3 | STRING | 30 | — | Address Line 3 |
| 4 | BKCM_ACCT_ALPHA | STRING | 6 | — | Alpha Search |
| 5 | BKCM_ACCT_CCARD | STRING | 25 | — | Credit Card Company |
| 6 | BKCM_ACCT_CEXP | DATE | 4 | — | CC Exp. Date |
| 7 | BKCM_ACCT_CITY | STRING | 26 | — | City |
| 8 | BKCM_ACCT_CMPNM | STRING | 25 | — | Company Name |
| 9 | BKCM_ACCT_CNTRY | STRING | 30 | — | Country |
| 10 | BKCM_ACCT_CNUM | STRING | 25 | — | Credit Card Number |
| 11 | BKCM_ACCT_CODE | STRING | 10 | — | Account Code |
| 12 | BKCM_ACCT_CONT1 | STRING | 30 | — | Contact 1 |
| 13 | BKCM_ACCT_CUST | STRING | 1 | — | Y/N |
| 14 | BKCM_ACCT_DLOAD | STRING | 1 | — | Y/N |
| 15 | BKCM_ACCT_EMAIL | STRING | 128 | — | Email Address |
| 16 | BKCM_ACCT_EMPS | NUMERIC | 8 | — | Number  Employees |
| 17 | BKCM_ACCT_EXTRA | STRING | 200 | — | Extra |
| 18 | BKCM_ACCT_FAX | STRING | 25 | — | Fax Number |
| 19 | BKCM_ACCT_FONE_1 | STRING | 15 | — | — |
| 20 | BKCM_ACCT_FONE_2 | STRING | 15 | — | — |
| 21 | BKCM_ACCT_FONE_3 | STRING | 15 | — | — |
| 22 | BKCM_ACCT_FTHRE_1 | STRING | 25 | — | — |
| 23 | BKCM_ACCT_FTHRE_2 | STRING | 25 | — | — |
| 24 | BKCM_ACCT_FTIME | INTEGER | 2 | — | not used |
| 25 | BKCM_ACCT_FTWO_1 | STRING | 2 | — | — |
| 26 | BKCM_ACCT_FTWO_2 | STRING | 2 | — | — |
| 27 | BKCM_ACCT_FTWO_3 | STRING | 2 | — | — |
| 28 | BKCM_ACCT_LEAD | STRING | 5 | — | Lead Source |
| 29 | BKCM_ACCT_NAME | STRING | 30 | — | Name |
| 30 | BKCM_ACCT_OLDCD | STRING | 10 | — | Old Account Code |
| 31 | BKCM_ACCT_PHONE | STRING | 25 | — | Phone Number |
| 32 | BKCM_ACCT_PNAME | STRING | 25 | — | Prospect Name |
| 33 | BKCM_ACCT_REM_1 | STRING | 60 | — | — |
| 34 | BKCM_ACCT_REM_2 | STRING | 60 | — | — |
| 35 | BKCM_ACCT_REP | STRING | 5 | — | Rep Num. |
| 36 | BKCM_ACCT_SICCD | STRING | 7 | — | SIC Code |
| 37 | BKCM_ACCT_START | DATE | 4 | — | Start Date |
| 38 | BKCM_ACCT_STATE | STRING | 2 | — | State |
| 39 | BKCM_ACCT_TERR | STRING | 4 | — | Territory |
| 40 | BKCM_ACCT_TITLE | STRING | 30 | — | Title |
| 41 | BKCM_ACCT_ZIP | STRING | 10 | — | Zip Code |

## BKCMEFTM
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_FTME_ATIME | INTEGER | 2 | — | — |
| 2 | BKCM_FTME_BALNC | NUMERIC | 8 | 2 | — |
| 3 | BKCM_FTME_CODE | STRING | 10 | — | Contact Code |
| 4 | BKCM_FTME_DESC | STRING | 25 | — | Description |
| 5 | BKCM_FTME_FTIME | INTEGER | 2 | — | — |
| 6 | BKCM_FTME_LASTP | DATE | 4 | — | Last Payment |
| 7 | BKCM_FTME_NTIME | INTEGER | 2 | — | — |

## BKCMPCFC
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_PCFC_DESC | STRING | 25 | — | — |
| 2 | BKCM_PCFC_FCODE | STRING | 3 | — | — |
| 3 | BKCM_PCFC_REP | STRING | 5 | — | — |

## BKCMSBDF
**CM subdirectory/folder defaults** — used by T7MDEFNDC (menu defaults for DC terminals). Configures folder paths for DC programs.

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_SBDF_BINC | NUMERIC | 8 | 2 | — |
| 2 | BKCM_SBDF_DHOLD | STRING | 1 | — | — |
| 3 | BKCM_SBDF_ICONV | NUMERIC | 8 | 6 | — |
| 4 | BKCM_SBDF_MINC | INTEGER | 2 | — | — |
| 5 | BKCM_SBDF_NCHG | INTEGER | 2 | — | — |

## BKCMTEMP
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | — |
| 2 | BKCMT_CODE | STRING | 10 | — | — |
| 3 | BKCMT_COMP | STRING | 2 | — | — |
| 4 | BKCMT_GROUP | STRING | 8 | — | — |
| 5 | BKCMT_KEYF | STRING | 20 | — | — |
| 6 | BKCMT_TAG | STRING | 1 | — | — |

## BKCMTMP1
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | — |
| 2 | BKCMT_CODE | STRING | 10 | — | — |
| 3 | BKCMT_COMP | STRING | 2 | — | — |
| 4 | BKCMT_GROUP | STRING | 8 | — | — |
| 5 | BKCMT_KEYF | STRING | 20 | — | — |
| 6 | BKCMT_TAG | STRING | 1 | — | — |

## BKCMTMP2
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | — |
| 2 | BKCMT_CODE | STRING | 10 | — | — |
| 3 | BKCMT_COMP | STRING | 2 | — | — |
| 4 | BKCMT_GROUP | STRING | 8 | — | — |
| 5 | BKCMT_KEYF | STRING | 20 | — | — |
| 6 | BKCMT_TAG | STRING | 1 | — | — |

## BKCMTMP3
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | — |
| 2 | BKCMT_CODE | STRING | 10 | — | — |
| 3 | BKCMT_COMP | STRING | 2 | — | — |
| 4 | BKCMT_GROUP | STRING | 8 | — | — |
| 5 | BKCMT_KEYF | STRING | 20 | — | — |
| 6 | BKCMT_TAG | STRING | 1 | — | — |

## BKCMTMP4
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | — |
| 2 | BKCMT_CODE | STRING | 10 | — | — |
| 3 | BKCMT_COMP | STRING | 2 | — | — |
| 4 | BKCMT_GROUP | STRING | 8 | — | — |
| 5 | BKCMT_KEYF | STRING | 20 | — | — |
| 6 | BKCMT_TAG | STRING | 1 | — | — |

## BKDCCFG
**DC terminal/scanner configuration** — used by T7ADCA/T7AUTODCH/J7EIMDCRev. Stores per-terminal DC scanner settings.

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKDC_CFG_BANKP | NUMERIC | 8 | — | — |
| 2 | BKDC_CFG_BANKS | INTEGER | 2 | — | — |
| 3 | BKDC_CFG_EXPPTH | STRING | 60 | — | — |
| 4 | BKDC_CFG_IDLEP | NUMERIC | 8 | — | — |
| 5 | BKDC_CFG_IDLES | INTEGER | 2 | — | — |
| 6 | BKDC_CFG_IMPPTH | STRING | 60 | — | — |
| 7 | BKDC_CFG_JOBTME | STRING | 60 | — | — |

## BKGLHIST
**NOT USED**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_TRN_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_TRN_BATCH | NUMERIC | 8 | — | Batch Number |
| 3 | BKGL_TRN_CODE | STRING | 10 | — | Trans Code |
| 4 | BKGL_TRN_DATE | DATE | 4 | — | Date |
| 5 | BKGL_TRN_DC | STRING | 1 | — | Debit/Credit |
| 6 | BKGL_TRN_DESC | STRING | 25 | — | Description |
| 7 | BKGL_TRN_ENTDTE | DATE | 4 | — | Enter Date |
| 8 | BKGL_TRN_EXTRA | STRING | 25 | — | Extra |
| 9 | BKGL_TRN_GLACCT | STRING | 10 | — | GL Account Code |
| 10 | BKGL_TRN_GLDPT | STRING | 4 | — | GL Department |
| 11 | BKGL_TRN_INVC | STRING | 10 | — | Invoice |
| 12 | BKGL_TRN_PART | STRING | 15 | — | — |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POST | STRING | 1 | — | Posted flag |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Trans Number |
| 16 | BKGL_TRN_TYPE | STRING | 2 | — | Type |

## BKGLICC
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_CHK_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_CHK_CHKACT | INTEGER | 2 | — | Checking Accoun Num |
| 3 | BKGL_CHK_CUST | STRING | 10 | — | — |
| 4 | BKGL_CHK_DATE | DATE | 4 | — | Date |
| 5 | BKGL_CHK_DATER | DATE | 4 | — | — |
| 6 | BKGL_CHK_EXTRA | STRING | 100 | — | — |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — | Reconciled Y/N |
| 8 | BKGL_CHK_NAME | STRING | 25 | — | Pay to Name |
| 9 | BKGL_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 10 | BKGL_CHK_TYPE | STRING | 1 | — | Type |
| 11 | BKGL_CHK_VEND | STRING | 10 | — | — |

## BKGLTMP
**NOT USED**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_TRN_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_TRN_BATCH | NUMERIC | 8 | — | Batch Number |
| 3 | BKGL_TRN_CODE | STRING | 10 | — | Trans Code |
| 4 | BKGL_TRN_DATE | DATE | 4 | — | Date |
| 5 | BKGL_TRN_DC | STRING | 1 | — | Debit/Credit |
| 6 | BKGL_TRN_DESC | STRING | 25 | — | Description |
| 7 | BKGL_TRN_ENTDTE | DATE | 4 | — | Enter Date |
| 8 | BKGL_TRN_EXTRA | STRING | 25 | — | Extra |
| 9 | BKGL_TRN_GLACCT | STRING | 10 | — | GL Account Code |
| 10 | BKGL_TRN_GLDPT | STRING | 4 | — | GL Department |
| 11 | BKGL_TRN_INVC | STRING | 10 | — | Invoice |
| 12 | BKGL_TRN_PART | STRING | 15 | — | — |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POST | STRING | 1 | — | Posted flag |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Trans Number |
| 16 | BKGL_TRN_TYPE | STRING | 2 | — | Type |

## BKGLTMP2
**NOT USED**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKGL_TRN_AMT | NUMERIC | 8 | 2 | Amount |
| 2 | BKGL_TRN_BATCH | NUMERIC | 8 | — | Batch Number |
| 3 | BKGL_TRN_CODE | STRING | 10 | — | Trans Code |
| 4 | BKGL_TRN_DATE | DATE | 4 | — | Date |
| 5 | BKGL_TRN_DC | STRING | 1 | — | Debit/Credit |
| 6 | BKGL_TRN_DESC | STRING | 25 | — | Description |
| 7 | BKGL_TRN_ENTDTE | DATE | 4 | — | Enter Date |
| 8 | BKGL_TRN_EXTRA | STRING | 25 | — | Extra |
| 9 | BKGL_TRN_GLACCT | STRING | 10 | — | GL Account Code |
| 10 | BKGL_TRN_GLDPT | STRING | 4 | — | GL Department |
| 11 | BKGL_TRN_INVC | STRING | 10 | — | Invoice |
| 12 | BKGL_TRN_PART | STRING | 15 | — | — |
| 13 | BKGL_TRN_PERIOD | INTEGER | 2 | — | Period |
| 14 | BKGL_TRN_POST | STRING | 1 | — | Posted flag |
| 15 | BKGL_TRN_TRXN | NUMERIC | 8 | — | Trans Number |
| 16 | BKGL_TRN_TYPE | STRING | 2 | — | Type |

## BKICALTD
**NOT USED**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_ALTD_DESC | STRING | 30 | — | Description |
| 2 | BKIC_ALTD_NOTE | STRING | 30 | — | Note |
| 3 | BKIC_ALTD_PCODE | STRING | 15 | — | Item Number |
| 4 | BKIC_ALTD_SPECS_1 | STRING | 30 | — | — |
| 5 | BKIC_ALTD_SPECS_10 | STRING | 30 | — | — |
| 6 | BKIC_ALTD_SPECS_11 | STRING | 30 | — | — |
| 7 | BKIC_ALTD_SPECS_12 | STRING | 30 | — | — |
| 8 | BKIC_ALTD_SPECS_2 | STRING | 30 | — | — |
| 9 | BKIC_ALTD_SPECS_3 | STRING | 30 | — | — |
| 10 | BKIC_ALTD_SPECS_4 | STRING | 30 | — | — |
| 11 | BKIC_ALTD_SPECS_5 | STRING | 30 | — | — |
| 12 | BKIC_ALTD_SPECS_6 | STRING | 30 | — | — |
| 13 | BKIC_ALTD_SPECS_7 | STRING | 30 | — | — |
| 14 | BKIC_ALTD_SPECS_8 | STRING | 30 | — | — |
| 15 | BKIC_ALTD_SPECS_9 | STRING | 30 | — | — |
| 16 | BKIC_ALTD_TYPE | STRING | 1 | — | Type |

## BKICALTP
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_ALTP_ACODE | STRING | 25 | — | — |
| 2 | BKIC_ALTP_NOTES_1 | STRING | 30 | — | — |
| 3 | BKIC_ALTP_NOTES_2 | STRING | 30 | — | — |
| 4 | BKIC_ALTP_NOTES_3 | STRING | 30 | — | — |
| 5 | BKIC_ALTP_PCODE | STRING | 15 | — | — |
| 6 | BKIC_ALTP_TYPE | STRING | 1 | — | — |

## BKICDIM
**Item dimensions** — used by T7BMA/T7INLF/T7INLG (BOM and IN programs). Stores per-item dimensional data (size/weight specs).

Fields: 47

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKICDIM_ALLOY | STRING | 20 | — | Alloy |
| 2 | BKICDIM_ALTDESC | STRING | 30 | — | Alternate Description |
| 3 | BKICDIM_APPR_BY | STRING | 20 | — | Approved By |
| 4 | BKICDIM_APPR_DT | DATE | 4 | — | Approval Date |
| 5 | BKICDIM_CAMBER | STRING | 15 | — | Camber |
| 6 | BKICDIM_COATING_1 | STRING | 20 | — | — |
| 7 | BKICDIM_COATING_2 | STRING | 20 | — | — |
| 8 | BKICDIM_COIL_1 | STRING | 10 | — | — |
| 9 | BKICDIM_COIL_2 | STRING | 10 | — | — |
| 10 | BKICDIM_COIL_3 | STRING | 10 | — | — |
| 11 | BKICDIM_DENSITY | NUMERIC | 8 | 4 | Density |
| 12 | BKICDIM_EDGE_1 | STRING | 20 | — | — |
| 13 | BKICDIM_EDGE_2 | STRING | 20 | — | — |
| 14 | BKICDIM_ELONGAT | STRING | 15 | — | Elongation |
| 15 | BKICDIM_F_TOL_1 | NUMERIC | 8 | 4 | — |
| 16 | BKICDIM_F_TOL_2 | NUMERIC | 8 | 4 | — |
| 17 | BKICDIM_FINISH_1 | STRING | 20 | — | — |
| 18 | BKICDIM_FINISH_2 | STRING | 20 | — | — |
| 19 | BKICDIM_FIRST | NUMERIC | 8 | 4 | Length |
| 20 | BKICDIM_GENERIC | STRING | 15 | — | Generic Phantom Part |
| 21 | BKICDIM_HARDNES | STRING | 20 | — | Hardness |
| 22 | BKICDIM_NOTES_1 | STRING | 30 | — | — |
| 23 | BKICDIM_NOTES_10 | STRING | 30 | — | — |
| 24 | BKICDIM_NOTES_11 | STRING | 30 | — | — |
| 25 | BKICDIM_NOTES_12 | STRING | 30 | — | — |
| 26 | BKICDIM_NOTES_2 | STRING | 30 | — | — |
| 27 | BKICDIM_NOTES_3 | STRING | 30 | — | — |
| 28 | BKICDIM_NOTES_4 | STRING | 30 | — | — |
| 29 | BKICDIM_NOTES_5 | STRING | 30 | — | — |
| 30 | BKICDIM_NOTES_6 | STRING | 30 | — | — |
| 31 | BKICDIM_NOTES_7 | STRING | 30 | — | — |
| 32 | BKICDIM_NOTES_8 | STRING | 30 | — | — |
| 33 | BKICDIM_NOTES_9 | STRING | 30 | — | — |
| 34 | BKICDIM_PARENT | STRING | 15 | — | Parent Item |
| 35 | BKICDIM_PARTNO | STRING | 15 | — | Item Number |
| 36 | BKICDIM_S_TOL_1 | NUMERIC | 8 | 4 | — |
| 37 | BKICDIM_S_TOL_2 | NUMERIC | 8 | 4 | — |
| 38 | BKICDIM_SECOND | NUMERIC | 8 | 4 | Width |
| 39 | BKICDIM_SETUP | NUMERIC | 8 | 8 | Setup |
| 40 | BKICDIM_SHPCOND_1 | STRING | 20 | — | — |
| 41 | BKICDIM_SHPCOND_2 | STRING | 20 | — | — |
| 42 | BKICDIM_T_TOL_1 | NUMERIC | 8 | 4 | — |
| 43 | BKICDIM_T_TOL_2 | NUMERIC | 8 | 4 | — |
| 44 | BKICDIM_TEMPER | STRING | 20 | — | Tempor |
| 45 | BKICDIM_TENSIL | STRING | 20 | — | Tensile |
| 46 | BKICDIM_THICK | NUMERIC | 8 | 4 | Thickness |
| 47 | BKICDIM_YIELD | STRING | 20 | — | Yield |

## BKICMFG
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_MFG_MANUF | STRING | 25 | — | Not Used |
| 2 | BKIC_MFG_MCODE | STRING | 25 | — | Not Used |
| 3 | BKIC_MFG_PCODE | STRING | 15 | — | Part Number |
| 4 | BKIC_MFG_REMARK_1 | STRING | 30 | — | — |
| 5 | BKIC_MFG_REMARK_2 | STRING | 30 | — | — |
| 6 | BKIC_MFG_REMARK_3 | STRING | 30 | — | — |

## BKICREQ
**NOT USED**

Fields: 46

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_REQ_AGENT | STRING | 25 | — | — |
| 2 | BKIC_REQ_BATCH^ | NUMERIC | 8 | — | — |
| 3 | BKIC_REQ_BY | INTEGER | 2 | — | — |
| 4 | BKIC_REQ_DDATE | DATE | 4 | — | — |
| 5 | BKIC_REQ_DESC | STRING | 30 | — | — |
| 6 | BKIC_REQ_ERDATE | DATE | 4 | — | — |
| 7 | BKIC_REQ_FROM | STRING | 10 | — | — |
| 8 | BKIC_REQ_IDATE | DATE | 4 | — | — |
| 9 | BKIC_REQ_ITM_NO | STRING | 9 | — | — |
| 10 | BKIC_REQ_MATDIM | STRING | 1 | — | — |
| 11 | BKIC_REQ_MFG | STRING | 25 | — | — |
| 12 | BKIC_REQ_MPART^ | STRING | 25 | — | — |
| 13 | BKIC_REQ_NOTES_1 | STRING | 30 | — | — |
| 14 | BKIC_REQ_NOTES_10 | STRING | 30 | — | — |
| 15 | BKIC_REQ_NOTES_2 | STRING | 30 | — | — |
| 16 | BKIC_REQ_NOTES_3 | STRING | 30 | — | — |
| 17 | BKIC_REQ_NOTES_4 | STRING | 30 | — | — |
| 18 | BKIC_REQ_NOTES_5 | STRING | 30 | — | — |
| 19 | BKIC_REQ_NOTES_6 | STRING | 30 | — | — |
| 20 | BKIC_REQ_NOTES_7 | STRING | 30 | — | — |
| 21 | BKIC_REQ_NOTES_8 | STRING | 30 | — | — |
| 22 | BKIC_REQ_NOTES_9 | STRING | 30 | — | — |
| 23 | BKIC_REQ_NUM | NUMERIC | 8 | — | — |
| 24 | BKIC_REQ_OPER | INTEGER | 2 | — | — |
| 25 | BKIC_REQ_ORDNUM | NUMERIC | 8 | — | — |
| 26 | BKIC_REQ_ORDQTY | NUMERIC | 8 | 2 | — |
| 27 | BKIC_REQ_PARENT | STRING | 15 | — | — |
| 28 | BKIC_REQ_PART^ | STRING | 15 | — | — |
| 29 | BKIC_REQ_PART^2 | STRING | 15 | — | — |
| 30 | BKIC_REQ_PROJ | STRING | 15 | — | — |
| 31 | BKIC_REQ_RQTY | NUMERIC | 8 | 2 | — |
| 32 | BKIC_REQ_STATUS | STRING | 1 | — | — |
| 33 | BKIC_REQ_TOADDR_1 | STRING | 30 | — | — |
| 34 | BKIC_REQ_TOADDR_2 | STRING | 30 | — | — |
| 35 | BKIC_REQ_TOADDR_3 | STRING | 30 | — | — |
| 36 | BKIC_REQ_TOCITY | STRING | 20 | — | — |
| 37 | BKIC_REQ_TOCONT | STRING | 25 | — | — |
| 38 | BKIC_REQ_TOFAX | STRING | 25 | — | — |
| 39 | BKIC_REQ_TOLOCN | STRING | 10 | — | — |
| 40 | BKIC_REQ_TONAME | STRING | 30 | — | — |
| 41 | BKIC_REQ_TOPH^ | STRING | 25 | — | — |
| 42 | BKIC_REQ_TOST | STRING | 2 | — | — |
| 43 | BKIC_REQ_TOZIP | STRING | 10 | — | — |
| 44 | BKIC_REQ_TYPE | STRING | 1 | — | — |
| 45 | BKIC_REQ_WOPRE | NUMERIC | 8 | — | — |
| 46 | BKIC_REQ_WOSUF | INTEGER | 2 | — | — |

## BKICTAX
**Item tax codes** — used by T7ESE/J7DCSSOE/J7HHRTSSOE. Per-item sales tax classification codes.

Fields: 46

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_TAX_COLECT_1 | NUMERIC | 8 | 2 | — |
| 2 | BKIC_TAX_COLECT_10 | NUMERIC | 8 | 2 | — |
| 3 | BKIC_TAX_COLECT_11 | NUMERIC | 8 | 2 | — |
| 4 | BKIC_TAX_COLECT_12 | NUMERIC | 8 | 2 | — |
| 5 | BKIC_TAX_COLECT_2 | NUMERIC | 8 | 2 | — |
| 6 | BKIC_TAX_COLECT_3 | NUMERIC | 8 | 2 | — |
| 7 | BKIC_TAX_COLECT_4 | NUMERIC | 8 | 2 | — |
| 8 | BKIC_TAX_COLECT_5 | NUMERIC | 8 | 2 | — |
| 9 | BKIC_TAX_COLECT_6 | NUMERIC | 8 | 2 | — |
| 10 | BKIC_TAX_COLECT_7 | NUMERIC | 8 | 2 | — |
| 11 | BKIC_TAX_COLECT_8 | NUMERIC | 8 | 2 | — |
| 12 | BKIC_TAX_COLECT_9 | NUMERIC | 8 | 2 | — |
| 13 | BKIC_TAX_FRGHT | STRING | 1 | — | Freight |
| 14 | BKIC_TAX_GLACT | STRING | 10 | — | GL Account |
| 15 | BKIC_TAX_GLDPT | STRING | 4 | — | GL Department |
| 16 | BKIC_TAX_LOCAL | STRING | 2 | — | Local (County/City) |
| 17 | BKIC_TAX_NAME | STRING | 25 | — | Local Name |
| 18 | BKIC_TAX_NONTAX_1 | NUMERIC | 8 | 2 | — |
| 19 | BKIC_TAX_NONTAX_10 | NUMERIC | 8 | 2 | — |
| 20 | BKIC_TAX_NONTAX_11 | NUMERIC | 8 | 2 | — |
| 21 | BKIC_TAX_NONTAX_12 | NUMERIC | 8 | 2 | — |
| 22 | BKIC_TAX_NONTAX_2 | NUMERIC | 8 | 2 | — |
| 23 | BKIC_TAX_NONTAX_3 | NUMERIC | 8 | 2 | — |
| 24 | BKIC_TAX_NONTAX_4 | NUMERIC | 8 | 2 | — |
| 25 | BKIC_TAX_NONTAX_5 | NUMERIC | 8 | 2 | — |
| 26 | BKIC_TAX_NONTAX_6 | NUMERIC | 8 | 2 | — |
| 27 | BKIC_TAX_NONTAX_7 | NUMERIC | 8 | 2 | — |
| 28 | BKIC_TAX_NONTAX_8 | NUMERIC | 8 | 2 | — |
| 29 | BKIC_TAX_NONTAX_9 | NUMERIC | 8 | 2 | — |
| 30 | BKIC_TAX_NUMBER | STRING | 15 | — | — |
| 31 | BKIC_TAX_OUTSTD | NUMERIC | 8 | 2 | Outstanding |
| 32 | BKIC_TAX_RATE | NUMERIC | 8 | 4 | Tax Rate |
| 33 | BKIC_TAX_STATE | STRING | 2 | — | State |
| 34 | BKIC_TAX_TAXBLE_1 | NUMERIC | 8 | 2 | — |
| 35 | BKIC_TAX_TAXBLE_10 | NUMERIC | 8 | 2 | — |
| 36 | BKIC_TAX_TAXBLE_11 | NUMERIC | 8 | 2 | — |
| 37 | BKIC_TAX_TAXBLE_12 | NUMERIC | 8 | 2 | — |
| 38 | BKIC_TAX_TAXBLE_2 | NUMERIC | 8 | 2 | — |
| 39 | BKIC_TAX_TAXBLE_3 | NUMERIC | 8 | 2 | — |
| 40 | BKIC_TAX_TAXBLE_4 | NUMERIC | 8 | 2 | — |
| 41 | BKIC_TAX_TAXBLE_5 | NUMERIC | 8 | 2 | — |
| 42 | BKIC_TAX_TAXBLE_6 | NUMERIC | 8 | 2 | — |
| 43 | BKIC_TAX_TAXBLE_7 | NUMERIC | 8 | 2 | — |
| 44 | BKIC_TAX_TAXBLE_8 | NUMERIC | 8 | 2 | — |
| 45 | BKIC_TAX_TAXBLE_9 | NUMERIC | 8 | 2 | — |
| 46 | BKIC_TAX_VENDOR | STRING | 10 | — | Vendor Code for Tax Authority |

## BKICVAL
**Item valuation overrides** — used by T7SMJL (job cost). Stores valuation adjustment records per item.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_VAL_CODE | STRING | 15 | — | — |
| 2 | BKIC_VAL_DATE | DATE | 4 | — | — |
| 3 | BKIC_VAL_TOTVL | NUMERIC | 8 | 2 | — |
| 4 | BKIC_VAL_UOH | NUMERIC | 8 | 2 | — |

## BKLOGON
**NOT USED**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKLOGON_CMPY | STRING | 2 | — | — |
| 2 | BKLOGON_CODE | STRING | 15 | — | — |
| 3 | BKLOGON_CURPRT | INTEGER | 2 | — | — |
| 4 | BKLOGON_INUSE | STRING | 1 | — | — |
| 5 | BKLOGON_MENU | INTEGER | 2 | — | — |
| 6 | BKLOGON_PRINTER | INTEGER | 2 | — | — |
| 7 | BKLOGON_PROG | STRING | 8 | — | — |
| 8 | BKLOGON_PSWD | STRING | 10 | — | — |
| 9 | BKLOGON_SCRTY | STRING | 2 | — | — |
| 10 | BKLOGON_SUBMENU | INTEGER | 2 | — | — |

## BKMATRIM
**Material trim specifications** — used by T7ROD (RO-D routing). Stores outside-process material trim dimensions per routing.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMA_TRIM_FIRST | NUMERIC | 8 | 2 | — |
| 2 | BKMA_TRIM_MACH | STRING | 4 | — | — |
| 3 | BKMA_TRIM_SECND | NUMERIC | 8 | 2 | — |

## BKPCKIT
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPC_KIT_COMP | STRING | 15 | — | — |
| 2 | BKPC_KIT_DATELM | DATE | 4 | — | — |
| 3 | BKPC_KIT_LOC | STRING | 10 | — | — |
| 4 | BKPC_KIT_LOT_^ | STRING | 15 | — | — |
| 5 | BKPC_KIT_QTY_A | NUMERIC | 8 | 2 | — |
| 6 | BKPC_KIT_QTY_R | NUMERIC | 8 | 2 | — |
| 7 | BKPC_KIT_QTY_S | NUMERIC | 8 | 2 | — |

## BKPCPLOT
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPC_PLOT_COMPD | DATE | 4 | — | — |
| 2 | BKPC_PLOT_CUST | STRING | 10 | — | — |
| 3 | BKPC_PLOT_INKO | NUMERIC | 8 | 2 | — |
| 4 | BKPC_PLOT_ISDTE | DATE | 4 | — | — |
| 5 | BKPC_PLOT_LOC | STRING | 10 | — | — |
| 6 | BKPC_PLOT_LOT_^ | STRING | 15 | — | — |
| 7 | BKPC_PLOT_PLOT^ | STRING | 15 | — | — |
| 8 | BKPC_PLOT_PROD | STRING | 15 | — | — |
| 9 | BKPC_PLOT_QTY | NUMERIC | 8 | 2 | — |
| 10 | BKPC_PLOT_SPDTE | DATE | 4 | — | — |
| 11 | BKPC_PLOT_STAT | STRING | 1 | — | — |
| 12 | BKPC_PLOT_STRTD | DATE | 4 | — | — |

## BKPRBOOK
**NOT USED**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_SLS_CLASS_1 | STRING | 2 | — | — |
| 2 | BKPR_SLS_CLASS_2 | STRING | 2 | — | — |
| 3 | BKPR_SLS_COGS_1 | NUMERIC | 8 | 2 | — |
| 4 | BKPR_SLS_COGS_10 | NUMERIC | 8 | 2 | — |
| 5 | BKPR_SLS_COGS_11 | NUMERIC | 8 | 2 | — |
| 6 | BKPR_SLS_COGS_12 | NUMERIC | 8 | 2 | — |
| 7 | BKPR_SLS_COGS_2 | NUMERIC | 8 | 2 | — |
| 8 | BKPR_SLS_COGS_3 | NUMERIC | 8 | 2 | — |
| 9 | BKPR_SLS_COGS_4 | NUMERIC | 8 | 2 | — |
| 10 | BKPR_SLS_COGS_5 | NUMERIC | 8 | 2 | — |
| 11 | BKPR_SLS_COGS_6 | NUMERIC | 8 | 2 | — |
| 12 | BKPR_SLS_COGS_7 | NUMERIC | 8 | 2 | — |
| 13 | BKPR_SLS_COGS_8 | NUMERIC | 8 | 2 | — |
| 14 | BKPR_SLS_COGS_9 | NUMERIC | 8 | 2 | — |
| 15 | BKPR_SLS_COMM_1 | NUMERIC | 8 | 2 | — |
| 16 | BKPR_SLS_COMM_10 | NUMERIC | 8 | 2 | — |
| 17 | BKPR_SLS_COMM_11 | NUMERIC | 8 | 2 | — |
| 18 | BKPR_SLS_COMM_12 | NUMERIC | 8 | 2 | — |
| 19 | BKPR_SLS_COMM_2 | NUMERIC | 8 | 2 | — |
| 20 | BKPR_SLS_COMM_3 | NUMERIC | 8 | 2 | — |
| 21 | BKPR_SLS_COMM_4 | NUMERIC | 8 | 2 | — |
| 22 | BKPR_SLS_COMM_5 | NUMERIC | 8 | 2 | — |
| 23 | BKPR_SLS_COMM_6 | NUMERIC | 8 | 2 | — |
| 24 | BKPR_SLS_COMM_7 | NUMERIC | 8 | 2 | — |
| 25 | BKPR_SLS_COMM_8 | NUMERIC | 8 | 2 | — |
| 26 | BKPR_SLS_COMM_9 | NUMERIC | 8 | 2 | — |
| 27 | BKPR_SLS_EMPNUM | INTEGER | 2 | — | — |
| 28 | BKPR_SLS_EXPACT | STRING | 10 | — | — |
| 29 | BKPR_SLS_EXPDPT | STRING | 4 | — | — |
| 30 | BKPR_SLS_EXTRA | STRING | 100 | — | — |
| 31 | BKPR_SLS_FNMI | STRING | 25 | — | — |
| 32 | BKPR_SLS_GROSS_1 | NUMERIC | 8 | 2 | — |
| 33 | BKPR_SLS_GROSS_10 | NUMERIC | 8 | 2 | — |
| 34 | BKPR_SLS_GROSS_11 | NUMERIC | 8 | 2 | — |
| 35 | BKPR_SLS_GROSS_12 | NUMERIC | 8 | 2 | — |
| 36 | BKPR_SLS_GROSS_2 | NUMERIC | 8 | 2 | — |
| 37 | BKPR_SLS_GROSS_3 | NUMERIC | 8 | 2 | — |
| 38 | BKPR_SLS_GROSS_4 | NUMERIC | 8 | 2 | — |
| 39 | BKPR_SLS_GROSS_5 | NUMERIC | 8 | 2 | — |
| 40 | BKPR_SLS_GROSS_6 | NUMERIC | 8 | 2 | — |
| 41 | BKPR_SLS_GROSS_7 | NUMERIC | 8 | 2 | — |
| 42 | BKPR_SLS_GROSS_8 | NUMERIC | 8 | 2 | — |
| 43 | BKPR_SLS_GROSS_9 | NUMERIC | 8 | 2 | — |
| 44 | BKPR_SLS_HOW_1 | STRING | 1 | — | — |
| 45 | BKPR_SLS_HOW_2 | STRING | 1 | — | — |
| 46 | BKPR_SLS_LNME | STRING | 25 | — | — |
| 47 | BKPR_SLS_PAID_1 | NUMERIC | 8 | 2 | — |
| 48 | BKPR_SLS_PAID_10 | NUMERIC | 8 | 2 | — |
| 49 | BKPR_SLS_PAID_11 | NUMERIC | 8 | 2 | — |
| 50 | BKPR_SLS_PAID_12 | NUMERIC | 8 | 2 | — |
| 51 | BKPR_SLS_PAID_2 | NUMERIC | 8 | 2 | — |
| 52 | BKPR_SLS_PAID_3 | NUMERIC | 8 | 2 | — |
| 53 | BKPR_SLS_PAID_4 | NUMERIC | 8 | 2 | — |
| 54 | BKPR_SLS_PAID_5 | NUMERIC | 8 | 2 | — |
| 55 | BKPR_SLS_PAID_6 | NUMERIC | 8 | 2 | — |
| 56 | BKPR_SLS_PAID_7 | NUMERIC | 8 | 2 | — |
| 57 | BKPR_SLS_PAID_8 | NUMERIC | 8 | 2 | — |
| 58 | BKPR_SLS_PAID_9 | NUMERIC | 8 | 2 | — |
| 59 | BKPR_SLS_QUOTA_1 | NUMERIC | 8 | 2 | — |
| 60 | BKPR_SLS_QUOTA_10 | NUMERIC | 8 | 2 | — |
| 61 | BKPR_SLS_QUOTA_11 | NUMERIC | 8 | 2 | — |
| 62 | BKPR_SLS_QUOTA_12 | NUMERIC | 8 | 2 | — |
| 63 | BKPR_SLS_QUOTA_2 | NUMERIC | 8 | 2 | — |
| 64 | BKPR_SLS_QUOTA_3 | NUMERIC | 8 | 2 | — |
| 65 | BKPR_SLS_QUOTA_4 | NUMERIC | 8 | 2 | — |
| 66 | BKPR_SLS_QUOTA_5 | NUMERIC | 8 | 2 | — |
| 67 | BKPR_SLS_QUOTA_6 | NUMERIC | 8 | 2 | — |
| 68 | BKPR_SLS_QUOTA_7 | NUMERIC | 8 | 2 | — |
| 69 | BKPR_SLS_QUOTA_8 | NUMERIC | 8 | 2 | — |
| 70 | BKPR_SLS_QUOTA_9 | NUMERIC | 8 | 2 | — |
| 71 | BKPR_SLS_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKPR_SLS_RATE_2 | NUMERIC | 8 | 4 | — |
| 73 | BKPR_SLS_RCPTS_1 | NUMERIC | 8 | 2 | — |
| 74 | BKPR_SLS_RCPTS_10 | NUMERIC | 8 | 2 | — |
| 75 | BKPR_SLS_RCPTS_11 | NUMERIC | 8 | 2 | — |
| 76 | BKPR_SLS_RCPTS_12 | NUMERIC | 8 | 2 | — |
| 77 | BKPR_SLS_RCPTS_2 | NUMERIC | 8 | 2 | — |
| 78 | BKPR_SLS_RCPTS_3 | NUMERIC | 8 | 2 | — |
| 79 | BKPR_SLS_RCPTS_4 | NUMERIC | 8 | 2 | — |
| 80 | BKPR_SLS_RCPTS_5 | NUMERIC | 8 | 2 | — |
| 81 | BKPR_SLS_RCPTS_6 | NUMERIC | 8 | 2 | — |
| 82 | BKPR_SLS_RCPTS_7 | NUMERIC | 8 | 2 | — |
| 83 | BKPR_SLS_RCPTS_8 | NUMERIC | 8 | 2 | — |
| 84 | BKPR_SLS_RCPTS_9 | NUMERIC | 8 | 2 | — |
| 85 | BKPR_SLS_WHEN_1 | STRING | 1 | — | — |
| 86 | BKPR_SLS_WHEN_2 | STRING | 1 | — | — |

## BKPRSTFL
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_ST_STCODE | STRING | 2 | — | — |
| 2 | BKPR_ST_TAXNUM | STRING | 10 | — | — |

## BKPRTCFG
**NOT USED**

Fields: 205

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPRT_CFG_CMD_1 | STRING | 70 | — | — |
| 2 | BKPRT_CFG_CMD_10 | STRING | 70 | — | — |
| 3 | BKPRT_CFG_CMD_11 | STRING | 70 | — | — |
| 4 | BKPRT_CFG_CMD_12 | STRING | 70 | — | — |
| 5 | BKPRT_CFG_CMD_13 | STRING | 70 | — | — |
| 6 | BKPRT_CFG_CMD_14 | STRING | 70 | — | — |
| 7 | BKPRT_CFG_CMD_15 | STRING | 70 | — | — |
| 8 | BKPRT_CFG_CMD_16 | STRING | 70 | — | — |
| 9 | BKPRT_CFG_CMD_17 | STRING | 70 | — | — |
| 10 | BKPRT_CFG_CMD_18 | STRING | 70 | — | — |
| 11 | BKPRT_CFG_CMD_19 | STRING | 70 | — | — |
| 12 | BKPRT_CFG_CMD_2 | STRING | 70 | — | — |
| 13 | BKPRT_CFG_CMD_20 | STRING | 70 | — | — |
| 14 | BKPRT_CFG_CMD_3 | STRING | 70 | — | — |
| 15 | BKPRT_CFG_CMD_4 | STRING | 70 | — | — |
| 16 | BKPRT_CFG_CMD_5 | STRING | 70 | — | — |
| 17 | BKPRT_CFG_CMD_6 | STRING | 70 | — | — |
| 18 | BKPRT_CFG_CMD_7 | STRING | 70 | — | — |
| 19 | BKPRT_CFG_CMD_8 | STRING | 70 | — | — |
| 20 | BKPRT_CFG_CMD_9 | STRING | 70 | — | — |
| 21 | BKPRT_CFG_COND_1 | STRING | 1 | — | — |
| 22 | BKPRT_CFG_COND_10 | STRING | 1 | — | — |
| 23 | BKPRT_CFG_COND_2 | STRING | 1 | — | — |
| 24 | BKPRT_CFG_COND_3 | STRING | 1 | — | — |
| 25 | BKPRT_CFG_COND_4 | STRING | 1 | — | — |
| 26 | BKPRT_CFG_COND_5 | STRING | 1 | — | — |
| 27 | BKPRT_CFG_COND_6 | STRING | 1 | — | — |
| 28 | BKPRT_CFG_COND_7 | STRING | 1 | — | — |
| 29 | BKPRT_CFG_COND_8 | STRING | 1 | — | — |
| 30 | BKPRT_CFG_COND_9 | STRING | 1 | — | — |
| 31 | BKPRT_CFG_COPY_1 | INTEGER | 2 | — | — |
| 32 | BKPRT_CFG_COPY_10 | INTEGER | 2 | — | — |
| 33 | BKPRT_CFG_COPY_11 | INTEGER | 2 | — | — |
| 34 | BKPRT_CFG_COPY_12 | INTEGER | 2 | — | — |
| 35 | BKPRT_CFG_COPY_13 | INTEGER | 2 | — | — |
| 36 | BKPRT_CFG_COPY_14 | INTEGER | 2 | — | — |
| 37 | BKPRT_CFG_COPY_15 | INTEGER | 2 | — | — |
| 38 | BKPRT_CFG_COPY_16 | INTEGER | 2 | — | — |
| 39 | BKPRT_CFG_COPY_17 | INTEGER | 2 | — | — |
| 40 | BKPRT_CFG_COPY_18 | INTEGER | 2 | — | — |
| 41 | BKPRT_CFG_COPY_19 | INTEGER | 2 | — | — |
| 42 | BKPRT_CFG_COPY_2 | INTEGER | 2 | — | — |
| 43 | BKPRT_CFG_COPY_20 | INTEGER | 2 | — | — |
| 44 | BKPRT_CFG_COPY_21 | INTEGER | 2 | — | — |
| 45 | BKPRT_CFG_COPY_22 | INTEGER | 2 | — | — |
| 46 | BKPRT_CFG_COPY_23 | INTEGER | 2 | — | — |
| 47 | BKPRT_CFG_COPY_24 | INTEGER | 2 | — | — |
| 48 | BKPRT_CFG_COPY_25 | INTEGER | 2 | — | — |
| 49 | BKPRT_CFG_COPY_26 | INTEGER | 2 | — | — |
| 50 | BKPRT_CFG_COPY_27 | INTEGER | 2 | — | — |
| 51 | BKPRT_CFG_COPY_28 | INTEGER | 2 | — | — |
| 52 | BKPRT_CFG_COPY_29 | INTEGER | 2 | — | — |
| 53 | BKPRT_CFG_COPY_3 | INTEGER | 2 | — | — |
| 54 | BKPRT_CFG_COPY_30 | INTEGER | 2 | — | — |
| 55 | BKPRT_CFG_COPY_31 | INTEGER | 2 | — | — |
| 56 | BKPRT_CFG_COPY_32 | INTEGER | 2 | — | — |
| 57 | BKPRT_CFG_COPY_33 | INTEGER | 2 | — | — |
| 58 | BKPRT_CFG_COPY_34 | INTEGER | 2 | — | — |
| 59 | BKPRT_CFG_COPY_35 | INTEGER | 2 | — | — |
| 60 | BKPRT_CFG_COPY_36 | INTEGER | 2 | — | — |
| 61 | BKPRT_CFG_COPY_37 | INTEGER | 2 | — | — |
| 62 | BKPRT_CFG_COPY_38 | INTEGER | 2 | — | — |
| 63 | BKPRT_CFG_COPY_39 | INTEGER | 2 | — | — |
| 64 | BKPRT_CFG_COPY_4 | INTEGER | 2 | — | — |
| 65 | BKPRT_CFG_COPY_40 | INTEGER | 2 | — | — |
| 66 | BKPRT_CFG_COPY_41 | INTEGER | 2 | — | — |
| 67 | BKPRT_CFG_COPY_42 | INTEGER | 2 | — | — |
| 68 | BKPRT_CFG_COPY_43 | INTEGER | 2 | — | — |
| 69 | BKPRT_CFG_COPY_44 | INTEGER | 2 | — | — |
| 70 | BKPRT_CFG_COPY_45 | INTEGER | 2 | — | — |
| 71 | BKPRT_CFG_COPY_46 | INTEGER | 2 | — | — |
| 72 | BKPRT_CFG_COPY_47 | INTEGER | 2 | — | — |
| 73 | BKPRT_CFG_COPY_48 | INTEGER | 2 | — | — |
| 74 | BKPRT_CFG_COPY_49 | INTEGER | 2 | — | — |
| 75 | BKPRT_CFG_COPY_5 | INTEGER | 2 | — | — |
| 76 | BKPRT_CFG_COPY_50 | INTEGER | 2 | — | — |
| 77 | BKPRT_CFG_COPY_6 | INTEGER | 2 | — | — |
| 78 | BKPRT_CFG_COPY_7 | INTEGER | 2 | — | — |
| 79 | BKPRT_CFG_COPY_8 | INTEGER | 2 | — | — |
| 80 | BKPRT_CFG_COPY_9 | INTEGER | 2 | — | — |
| 81 | BKPRT_CFG_DCMPY | STRING | 2 | — | — |
| 82 | BKPRT_CFG_DMENU | INTEGER | 2 | — | — |
| 83 | BKPRT_CFG_DPRTR | INTEGER | 2 | — | — |
| 84 | BKPRT_CFG_DSPMN | STRING | 1 | — | — |
| 85 | BKPRT_CFG_KEY | STRING | 2 | — | — |
| 86 | BKPRT_CFG_LPTNO_1 | INTEGER | 1 | — | — |
| 87 | BKPRT_CFG_LPTNO_10 | INTEGER | 1 | — | — |
| 88 | BKPRT_CFG_LPTNO_2 | INTEGER | 1 | — | — |
| 89 | BKPRT_CFG_LPTNO_3 | INTEGER | 1 | — | — |
| 90 | BKPRT_CFG_LPTNO_4 | INTEGER | 1 | — | — |
| 91 | BKPRT_CFG_LPTNO_5 | INTEGER | 1 | — | — |
| 92 | BKPRT_CFG_LPTNO_6 | INTEGER | 1 | — | — |
| 93 | BKPRT_CFG_LPTNO_7 | INTEGER | 1 | — | — |
| 94 | BKPRT_CFG_LPTNO_8 | INTEGER | 1 | — | — |
| 95 | BKPRT_CFG_LPTNO_9 | INTEGER | 1 | — | — |
| 96 | BKPRT_CFG_NAME_1 | STRING | 25 | — | — |
| 97 | BKPRT_CFG_NAME_10 | STRING | 25 | — | — |
| 98 | BKPRT_CFG_NAME_2 | STRING | 25 | — | — |
| 99 | BKPRT_CFG_NAME_3 | STRING | 25 | — | — |
| 100 | BKPRT_CFG_NAME_4 | STRING | 25 | — | — |
| 101 | BKPRT_CFG_NAME_5 | STRING | 25 | — | — |
| 102 | BKPRT_CFG_NAME_6 | STRING | 25 | — | — |
| 103 | BKPRT_CFG_NAME_7 | STRING | 25 | — | — |
| 104 | BKPRT_CFG_NAME_8 | STRING | 25 | — | — |
| 105 | BKPRT_CFG_NAME_9 | STRING | 25 | — | — |
| 106 | BKPRT_CFG_PMAX_1 | INTEGER | 2 | — | — |
| 107 | BKPRT_CFG_PMAX_10 | INTEGER | 2 | — | — |
| 108 | BKPRT_CFG_PMAX_2 | INTEGER | 2 | — | — |
| 109 | BKPRT_CFG_PMAX_3 | INTEGER | 2 | — | — |
| 110 | BKPRT_CFG_PMAX_4 | INTEGER | 2 | — | — |
| 111 | BKPRT_CFG_PMAX_5 | INTEGER | 2 | — | — |
| 112 | BKPRT_CFG_PMAX_6 | INTEGER | 2 | — | — |
| 113 | BKPRT_CFG_PMAX_7 | INTEGER | 2 | — | — |
| 114 | BKPRT_CFG_PMAX_8 | INTEGER | 2 | — | — |
| 115 | BKPRT_CFG_PMAX_9 | INTEGER | 2 | — | — |
| 116 | BKPRT_CFG_PORT_1 | INTEGER | 2 | — | — |
| 117 | BKPRT_CFG_PORT_10 | INTEGER | 2 | — | — |
| 118 | BKPRT_CFG_PORT_2 | INTEGER | 2 | — | — |
| 119 | BKPRT_CFG_PORT_3 | INTEGER | 2 | — | — |
| 120 | BKPRT_CFG_PORT_4 | INTEGER | 2 | — | — |
| 121 | BKPRT_CFG_PORT_5 | INTEGER | 2 | — | — |
| 122 | BKPRT_CFG_PORT_6 | INTEGER | 2 | — | — |
| 123 | BKPRT_CFG_PORT_7 | INTEGER | 2 | — | — |
| 124 | BKPRT_CFG_PORT_8 | INTEGER | 2 | — | — |
| 125 | BKPRT_CFG_PORT_9 | INTEGER | 2 | — | — |
| 126 | BKPRT_CFG_PPLNE_1 | INTEGER | 2 | — | — |
| 127 | BKPRT_CFG_PPLNE_10 | INTEGER | 2 | — | — |
| 128 | BKPRT_CFG_PPLNE_2 | INTEGER | 2 | — | — |
| 129 | BKPRT_CFG_PPLNE_3 | INTEGER | 2 | — | — |
| 130 | BKPRT_CFG_PPLNE_4 | INTEGER | 2 | — | — |
| 131 | BKPRT_CFG_PPLNE_5 | INTEGER | 2 | — | — |
| 132 | BKPRT_CFG_PPLNE_6 | INTEGER | 2 | — | — |
| 133 | BKPRT_CFG_PPLNE_7 | INTEGER | 2 | — | — |
| 134 | BKPRT_CFG_PPLNE_8 | INTEGER | 2 | — | — |
| 135 | BKPRT_CFG_PPLNE_9 | INTEGER | 2 | — | — |
| 136 | BKPRT_CFG_PRTR_1 | STRING | 8 | — | — |
| 137 | BKPRT_CFG_PRTR_10 | STRING | 8 | — | — |
| 138 | BKPRT_CFG_PRTR_2 | STRING | 8 | — | — |
| 139 | BKPRT_CFG_PRTR_3 | STRING | 8 | — | — |
| 140 | BKPRT_CFG_PRTR_4 | STRING | 8 | — | — |
| 141 | BKPRT_CFG_PRTR_5 | STRING | 8 | — | — |
| 142 | BKPRT_CFG_PRTR_6 | STRING | 8 | — | — |
| 143 | BKPRT_CFG_PRTR_7 | STRING | 8 | — | — |
| 144 | BKPRT_CFG_PRTR_8 | STRING | 8 | — | — |
| 145 | BKPRT_CFG_PRTR_9 | STRING | 8 | — | — |
| 146 | BKPRT_CFG_PWDT_1 | INTEGER | 2 | — | — |
| 147 | BKPRT_CFG_PWDT_10 | INTEGER | 2 | — | — |
| 148 | BKPRT_CFG_PWDT_2 | INTEGER | 2 | — | — |
| 149 | BKPRT_CFG_PWDT_3 | INTEGER | 2 | — | — |
| 150 | BKPRT_CFG_PWDT_4 | INTEGER | 2 | — | — |
| 151 | BKPRT_CFG_PWDT_5 | INTEGER | 2 | — | — |
| 152 | BKPRT_CFG_PWDT_6 | INTEGER | 2 | — | — |
| 153 | BKPRT_CFG_PWDT_7 | INTEGER | 2 | — | — |
| 154 | BKPRT_CFG_PWDT_8 | INTEGER | 2 | — | — |
| 155 | BKPRT_CFG_PWDT_9 | INTEGER | 2 | — | — |
| 156 | BKPRT_CFG_USEPR_1 | INTEGER | 2 | — | — |
| 157 | BKPRT_CFG_USEPR_10 | INTEGER | 2 | — | — |
| 158 | BKPRT_CFG_USEPR_11 | INTEGER | 2 | — | — |
| 159 | BKPRT_CFG_USEPR_12 | INTEGER | 2 | — | — |
| 160 | BKPRT_CFG_USEPR_13 | INTEGER | 2 | — | — |
| 161 | BKPRT_CFG_USEPR_14 | INTEGER | 2 | — | — |
| 162 | BKPRT_CFG_USEPR_15 | INTEGER | 2 | — | — |
| 163 | BKPRT_CFG_USEPR_16 | INTEGER | 2 | — | — |
| 164 | BKPRT_CFG_USEPR_17 | INTEGER | 2 | — | — |
| 165 | BKPRT_CFG_USEPR_18 | INTEGER | 2 | — | — |
| 166 | BKPRT_CFG_USEPR_19 | INTEGER | 2 | — | — |
| 167 | BKPRT_CFG_USEPR_2 | INTEGER | 2 | — | — |
| 168 | BKPRT_CFG_USEPR_20 | INTEGER | 2 | — | — |
| 169 | BKPRT_CFG_USEPR_21 | INTEGER | 2 | — | — |
| 170 | BKPRT_CFG_USEPR_22 | INTEGER | 2 | — | — |
| 171 | BKPRT_CFG_USEPR_23 | INTEGER | 2 | — | — |
| 172 | BKPRT_CFG_USEPR_24 | INTEGER | 2 | — | — |
| 173 | BKPRT_CFG_USEPR_25 | INTEGER | 2 | — | — |
| 174 | BKPRT_CFG_USEPR_26 | INTEGER | 2 | — | — |
| 175 | BKPRT_CFG_USEPR_27 | INTEGER | 2 | — | — |
| 176 | BKPRT_CFG_USEPR_28 | INTEGER | 2 | — | — |
| 177 | BKPRT_CFG_USEPR_29 | INTEGER | 2 | — | — |
| 178 | BKPRT_CFG_USEPR_3 | INTEGER | 2 | — | — |
| 179 | BKPRT_CFG_USEPR_30 | INTEGER | 2 | — | — |
| 180 | BKPRT_CFG_USEPR_31 | INTEGER | 2 | — | — |
| 181 | BKPRT_CFG_USEPR_32 | INTEGER | 2 | — | — |
| 182 | BKPRT_CFG_USEPR_33 | INTEGER | 2 | — | — |
| 183 | BKPRT_CFG_USEPR_34 | INTEGER | 2 | — | — |
| 184 | BKPRT_CFG_USEPR_35 | INTEGER | 2 | — | — |
| 185 | BKPRT_CFG_USEPR_36 | INTEGER | 2 | — | — |
| 186 | BKPRT_CFG_USEPR_37 | INTEGER | 2 | — | — |
| 187 | BKPRT_CFG_USEPR_38 | INTEGER | 2 | — | — |
| 188 | BKPRT_CFG_USEPR_39 | INTEGER | 2 | — | — |
| 189 | BKPRT_CFG_USEPR_4 | INTEGER | 2 | — | — |
| 190 | BKPRT_CFG_USEPR_40 | INTEGER | 2 | — | — |
| 191 | BKPRT_CFG_USEPR_41 | INTEGER | 2 | — | — |
| 192 | BKPRT_CFG_USEPR_42 | INTEGER | 2 | — | — |
| 193 | BKPRT_CFG_USEPR_43 | INTEGER | 2 | — | — |
| 194 | BKPRT_CFG_USEPR_44 | INTEGER | 2 | — | — |
| 195 | BKPRT_CFG_USEPR_45 | INTEGER | 2 | — | — |
| 196 | BKPRT_CFG_USEPR_46 | INTEGER | 2 | — | — |
| 197 | BKPRT_CFG_USEPR_47 | INTEGER | 2 | — | — |
| 198 | BKPRT_CFG_USEPR_48 | INTEGER | 2 | — | — |
| 199 | BKPRT_CFG_USEPR_49 | INTEGER | 2 | — | — |
| 200 | BKPRT_CFG_USEPR_5 | INTEGER | 2 | — | — |
| 201 | BKPRT_CFG_USEPR_50 | INTEGER | 2 | — | — |
| 202 | BKPRT_CFG_USEPR_6 | INTEGER | 2 | — | — |
| 203 | BKPRT_CFG_USEPR_7 | INTEGER | 2 | — | — |
| 204 | BKPRT_CFG_USEPR_8 | INTEGER | 2 | — | — |
| 205 | BKPRT_CFG_USEPR_9 | INTEGER | 2 | — | — |

## BKSYCFG
**NOT USED**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_CFG_ACCTG | STRING | 1 | — | — |
| 2 | BKSY_CFG_ADVWO | STRING | 1 | — | — |
| 3 | BKSY_CFG_LITEWO | STRING | 1 | — | — |
| 4 | BKSY_CFG_SALES | STRING | 1 | — | — |

## BKSYHELP
**System help lookup** — opened by 1,040+ programs as a standard session table for F1 context-sensitive help text.

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_HELP_PATH | STRING | 70 | — | — |

## BKSYLOG
**NOT USED**

Fields: 215

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_LOGON_APYN | STRING | 1 | — | — |
| 2 | BKSY_LOGON_ARYN | STRING | 1 | — | — |
| 3 | BKSY_LOGON_CHR | STRING | 1 | — | — |
| 4 | BKSY_LOGON_CODE | STRING | 15 | — | — |
| 5 | BKSY_LOGON_GLYN | STRING | 1 | — | — |
| 6 | BKSY_LOGON_ICYN | STRING | 1 | — | — |
| 7 | BKSY_LOGON_O1YN | STRING | 1 | — | — |
| 8 | BKSY_LOGON_O2YN | STRING | 1 | — | — |
| 9 | BKSY_LOGON_OKAP_1 | STRING | 1 | — | — |
| 10 | BKSY_LOGON_OKAP_10 | STRING | 1 | — | — |
| 11 | BKSY_LOGON_OKAP_11 | STRING | 1 | — | — |
| 12 | BKSY_LOGON_OKAP_12 | STRING | 1 | — | — |
| 13 | BKSY_LOGON_OKAP_13 | STRING | 1 | — | — |
| 14 | BKSY_LOGON_OKAP_14 | STRING | 1 | — | — |
| 15 | BKSY_LOGON_OKAP_15 | STRING | 1 | — | — |
| 16 | BKSY_LOGON_OKAP_16 | STRING | 1 | — | — |
| 17 | BKSY_LOGON_OKAP_17 | STRING | 1 | — | — |
| 18 | BKSY_LOGON_OKAP_18 | STRING | 1 | — | — |
| 19 | BKSY_LOGON_OKAP_19 | STRING | 1 | — | — |
| 20 | BKSY_LOGON_OKAP_2 | STRING | 1 | — | — |
| 21 | BKSY_LOGON_OKAP_20 | STRING | 1 | — | — |
| 22 | BKSY_LOGON_OKAP_3 | STRING | 1 | — | — |
| 23 | BKSY_LOGON_OKAP_4 | STRING | 1 | — | — |
| 24 | BKSY_LOGON_OKAP_5 | STRING | 1 | — | — |
| 25 | BKSY_LOGON_OKAP_6 | STRING | 1 | — | — |
| 26 | BKSY_LOGON_OKAP_7 | STRING | 1 | — | — |
| 27 | BKSY_LOGON_OKAP_8 | STRING | 1 | — | — |
| 28 | BKSY_LOGON_OKAP_9 | STRING | 1 | — | — |
| 29 | BKSY_LOGON_OKAR_1 | STRING | 1 | — | — |
| 30 | BKSY_LOGON_OKAR_10 | STRING | 1 | — | — |
| 31 | BKSY_LOGON_OKAR_11 | STRING | 1 | — | — |
| 32 | BKSY_LOGON_OKAR_12 | STRING | 1 | — | — |
| 33 | BKSY_LOGON_OKAR_13 | STRING | 1 | — | — |
| 34 | BKSY_LOGON_OKAR_14 | STRING | 1 | — | — |
| 35 | BKSY_LOGON_OKAR_15 | STRING | 1 | — | — |
| 36 | BKSY_LOGON_OKAR_16 | STRING | 1 | — | — |
| 37 | BKSY_LOGON_OKAR_17 | STRING | 1 | — | — |
| 38 | BKSY_LOGON_OKAR_18 | STRING | 1 | — | — |
| 39 | BKSY_LOGON_OKAR_19 | STRING | 1 | — | — |
| 40 | BKSY_LOGON_OKAR_2 | STRING | 1 | — | — |
| 41 | BKSY_LOGON_OKAR_20 | STRING | 1 | — | — |
| 42 | BKSY_LOGON_OKAR_3 | STRING | 1 | — | — |
| 43 | BKSY_LOGON_OKAR_4 | STRING | 1 | — | — |
| 44 | BKSY_LOGON_OKAR_5 | STRING | 1 | — | — |
| 45 | BKSY_LOGON_OKAR_6 | STRING | 1 | — | — |
| 46 | BKSY_LOGON_OKAR_7 | STRING | 1 | — | — |
| 47 | BKSY_LOGON_OKAR_8 | STRING | 1 | — | — |
| 48 | BKSY_LOGON_OKAR_9 | STRING | 1 | — | — |
| 49 | BKSY_LOGON_OKGL_1 | STRING | 1 | — | — |
| 50 | BKSY_LOGON_OKGL_10 | STRING | 1 | — | — |
| 51 | BKSY_LOGON_OKGL_11 | STRING | 1 | — | — |
| 52 | BKSY_LOGON_OKGL_12 | STRING | 1 | — | — |
| 53 | BKSY_LOGON_OKGL_13 | STRING | 1 | — | — |
| 54 | BKSY_LOGON_OKGL_14 | STRING | 1 | — | — |
| 55 | BKSY_LOGON_OKGL_15 | STRING | 1 | — | — |
| 56 | BKSY_LOGON_OKGL_16 | STRING | 1 | — | — |
| 57 | BKSY_LOGON_OKGL_17 | STRING | 1 | — | — |
| 58 | BKSY_LOGON_OKGL_18 | STRING | 1 | — | — |
| 59 | BKSY_LOGON_OKGL_19 | STRING | 1 | — | — |
| 60 | BKSY_LOGON_OKGL_2 | STRING | 1 | — | — |
| 61 | BKSY_LOGON_OKGL_20 | STRING | 1 | — | — |
| 62 | BKSY_LOGON_OKGL_3 | STRING | 1 | — | — |
| 63 | BKSY_LOGON_OKGL_4 | STRING | 1 | — | — |
| 64 | BKSY_LOGON_OKGL_5 | STRING | 1 | — | — |
| 65 | BKSY_LOGON_OKGL_6 | STRING | 1 | — | — |
| 66 | BKSY_LOGON_OKGL_7 | STRING | 1 | — | — |
| 67 | BKSY_LOGON_OKGL_8 | STRING | 1 | — | — |
| 68 | BKSY_LOGON_OKGL_9 | STRING | 1 | — | — |
| 69 | BKSY_LOGON_OKIC_1 | STRING | 1 | — | — |
| 70 | BKSY_LOGON_OKIC_10 | STRING | 1 | — | — |
| 71 | BKSY_LOGON_OKIC_11 | STRING | 1 | — | — |
| 72 | BKSY_LOGON_OKIC_12 | STRING | 1 | — | — |
| 73 | BKSY_LOGON_OKIC_13 | STRING | 1 | — | — |
| 74 | BKSY_LOGON_OKIC_14 | STRING | 1 | — | — |
| 75 | BKSY_LOGON_OKIC_15 | STRING | 1 | — | — |
| 76 | BKSY_LOGON_OKIC_16 | STRING | 1 | — | — |
| 77 | BKSY_LOGON_OKIC_17 | STRING | 1 | — | — |
| 78 | BKSY_LOGON_OKIC_18 | STRING | 1 | — | — |
| 79 | BKSY_LOGON_OKIC_19 | STRING | 1 | — | — |
| 80 | BKSY_LOGON_OKIC_2 | STRING | 1 | — | — |
| 81 | BKSY_LOGON_OKIC_20 | STRING | 1 | — | — |
| 82 | BKSY_LOGON_OKIC_3 | STRING | 1 | — | — |
| 83 | BKSY_LOGON_OKIC_4 | STRING | 1 | — | — |
| 84 | BKSY_LOGON_OKIC_5 | STRING | 1 | — | — |
| 85 | BKSY_LOGON_OKIC_6 | STRING | 1 | — | — |
| 86 | BKSY_LOGON_OKIC_7 | STRING | 1 | — | — |
| 87 | BKSY_LOGON_OKIC_8 | STRING | 1 | — | — |
| 88 | BKSY_LOGON_OKIC_9 | STRING | 1 | — | — |
| 89 | BKSY_LOGON_OKLM | STRING | 1 | — | — |
| 90 | BKSY_LOGON_OKPO_1 | STRING | 1 | — | — |
| 91 | BKSY_LOGON_OKPO_10 | STRING | 1 | — | — |
| 92 | BKSY_LOGON_OKPO_11 | STRING | 1 | — | — |
| 93 | BKSY_LOGON_OKPO_12 | STRING | 1 | — | — |
| 94 | BKSY_LOGON_OKPO_13 | STRING | 1 | — | — |
| 95 | BKSY_LOGON_OKPO_14 | STRING | 1 | — | — |
| 96 | BKSY_LOGON_OKPO_15 | STRING | 1 | — | — |
| 97 | BKSY_LOGON_OKPO_16 | STRING | 1 | — | — |
| 98 | BKSY_LOGON_OKPO_17 | STRING | 1 | — | — |
| 99 | BKSY_LOGON_OKPO_18 | STRING | 1 | — | — |
| 100 | BKSY_LOGON_OKPO_19 | STRING | 1 | — | — |
| 101 | BKSY_LOGON_OKPO_2 | STRING | 1 | — | — |
| 102 | BKSY_LOGON_OKPO_20 | STRING | 1 | — | — |
| 103 | BKSY_LOGON_OKPO_3 | STRING | 1 | — | — |
| 104 | BKSY_LOGON_OKPO_4 | STRING | 1 | — | — |
| 105 | BKSY_LOGON_OKPO_5 | STRING | 1 | — | — |
| 106 | BKSY_LOGON_OKPO_6 | STRING | 1 | — | — |
| 107 | BKSY_LOGON_OKPO_7 | STRING | 1 | — | — |
| 108 | BKSY_LOGON_OKPO_8 | STRING | 1 | — | — |
| 109 | BKSY_LOGON_OKPO_9 | STRING | 1 | — | — |
| 110 | BKSY_LOGON_OKPR_1 | STRING | 1 | — | — |
| 111 | BKSY_LOGON_OKPR_10 | STRING | 1 | — | — |
| 112 | BKSY_LOGON_OKPR_11 | STRING | 1 | — | — |
| 113 | BKSY_LOGON_OKPR_12 | STRING | 1 | — | — |
| 114 | BKSY_LOGON_OKPR_13 | STRING | 1 | — | — |
| 115 | BKSY_LOGON_OKPR_14 | STRING | 1 | — | — |
| 116 | BKSY_LOGON_OKPR_15 | STRING | 1 | — | — |
| 117 | BKSY_LOGON_OKPR_16 | STRING | 1 | — | — |
| 118 | BKSY_LOGON_OKPR_17 | STRING | 1 | — | — |
| 119 | BKSY_LOGON_OKPR_18 | STRING | 1 | — | — |
| 120 | BKSY_LOGON_OKPR_19 | STRING | 1 | — | — |
| 121 | BKSY_LOGON_OKPR_2 | STRING | 1 | — | — |
| 122 | BKSY_LOGON_OKPR_20 | STRING | 1 | — | — |
| 123 | BKSY_LOGON_OKPR_3 | STRING | 1 | — | — |
| 124 | BKSY_LOGON_OKPR_4 | STRING | 1 | — | — |
| 125 | BKSY_LOGON_OKPR_5 | STRING | 1 | — | — |
| 126 | BKSY_LOGON_OKPR_6 | STRING | 1 | — | — |
| 127 | BKSY_LOGON_OKPR_7 | STRING | 1 | — | — |
| 128 | BKSY_LOGON_OKPR_8 | STRING | 1 | — | — |
| 129 | BKSY_LOGON_OKPR_9 | STRING | 1 | — | — |
| 130 | BKSY_LOGON_OKSO_1 | STRING | 1 | — | — |
| 131 | BKSY_LOGON_OKSO_10 | STRING | 1 | — | — |
| 132 | BKSY_LOGON_OKSO_11 | STRING | 1 | — | — |
| 133 | BKSY_LOGON_OKSO_12 | STRING | 1 | — | — |
| 134 | BKSY_LOGON_OKSO_13 | STRING | 1 | — | — |
| 135 | BKSY_LOGON_OKSO_14 | STRING | 1 | — | — |
| 136 | BKSY_LOGON_OKSO_15 | STRING | 1 | — | — |
| 137 | BKSY_LOGON_OKSO_16 | STRING | 1 | — | — |
| 138 | BKSY_LOGON_OKSO_17 | STRING | 1 | — | — |
| 139 | BKSY_LOGON_OKSO_18 | STRING | 1 | — | — |
| 140 | BKSY_LOGON_OKSO_19 | STRING | 1 | — | — |
| 141 | BKSY_LOGON_OKSO_2 | STRING | 1 | — | — |
| 142 | BKSY_LOGON_OKSO_20 | STRING | 1 | — | — |
| 143 | BKSY_LOGON_OKSO_3 | STRING | 1 | — | — |
| 144 | BKSY_LOGON_OKSO_4 | STRING | 1 | — | — |
| 145 | BKSY_LOGON_OKSO_5 | STRING | 1 | — | — |
| 146 | BKSY_LOGON_OKSO_6 | STRING | 1 | — | — |
| 147 | BKSY_LOGON_OKSO_7 | STRING | 1 | — | — |
| 148 | BKSY_LOGON_OKSO_8 | STRING | 1 | — | — |
| 149 | BKSY_LOGON_OKSO_9 | STRING | 1 | — | — |
| 150 | BKSY_LOGON_OKSY_1 | STRING | 1 | — | — |
| 151 | BKSY_LOGON_OKSY_10 | STRING | 1 | — | — |
| 152 | BKSY_LOGON_OKSY_11 | STRING | 1 | — | — |
| 153 | BKSY_LOGON_OKSY_12 | STRING | 1 | — | — |
| 154 | BKSY_LOGON_OKSY_13 | STRING | 1 | — | — |
| 155 | BKSY_LOGON_OKSY_14 | STRING | 1 | — | — |
| 156 | BKSY_LOGON_OKSY_15 | STRING | 1 | — | — |
| 157 | BKSY_LOGON_OKSY_16 | STRING | 1 | — | — |
| 158 | BKSY_LOGON_OKSY_17 | STRING | 1 | — | — |
| 159 | BKSY_LOGON_OKSY_18 | STRING | 1 | — | — |
| 160 | BKSY_LOGON_OKSY_19 | STRING | 1 | — | — |
| 161 | BKSY_LOGON_OKSY_2 | STRING | 1 | — | — |
| 162 | BKSY_LOGON_OKSY_20 | STRING | 1 | — | — |
| 163 | BKSY_LOGON_OKSY_3 | STRING | 1 | — | — |
| 164 | BKSY_LOGON_OKSY_4 | STRING | 1 | — | — |
| 165 | BKSY_LOGON_OKSY_5 | STRING | 1 | — | — |
| 166 | BKSY_LOGON_OKSY_6 | STRING | 1 | — | — |
| 167 | BKSY_LOGON_OKSY_7 | STRING | 1 | — | — |
| 168 | BKSY_LOGON_OKSY_8 | STRING | 1 | — | — |
| 169 | BKSY_LOGON_OKSY_9 | STRING | 1 | — | — |
| 170 | BKSY_LOGON_OTH1_1 | STRING | 1 | — | — |
| 171 | BKSY_LOGON_OTH1_10 | STRING | 1 | — | — |
| 172 | BKSY_LOGON_OTH1_11 | STRING | 1 | — | — |
| 173 | BKSY_LOGON_OTH1_12 | STRING | 1 | — | — |
| 174 | BKSY_LOGON_OTH1_13 | STRING | 1 | — | — |
| 175 | BKSY_LOGON_OTH1_14 | STRING | 1 | — | — |
| 176 | BKSY_LOGON_OTH1_15 | STRING | 1 | — | — |
| 177 | BKSY_LOGON_OTH1_16 | STRING | 1 | — | — |
| 178 | BKSY_LOGON_OTH1_17 | STRING | 1 | — | — |
| 179 | BKSY_LOGON_OTH1_18 | STRING | 1 | — | — |
| 180 | BKSY_LOGON_OTH1_19 | STRING | 1 | — | — |
| 181 | BKSY_LOGON_OTH1_2 | STRING | 1 | — | — |
| 182 | BKSY_LOGON_OTH1_20 | STRING | 1 | — | — |
| 183 | BKSY_LOGON_OTH1_3 | STRING | 1 | — | — |
| 184 | BKSY_LOGON_OTH1_4 | STRING | 1 | — | — |
| 185 | BKSY_LOGON_OTH1_5 | STRING | 1 | — | — |
| 186 | BKSY_LOGON_OTH1_6 | STRING | 1 | — | — |
| 187 | BKSY_LOGON_OTH1_7 | STRING | 1 | — | — |
| 188 | BKSY_LOGON_OTH1_8 | STRING | 1 | — | — |
| 189 | BKSY_LOGON_OTH1_9 | STRING | 1 | — | — |
| 190 | BKSY_LOGON_OTH2_1 | STRING | 2 | — | — |
| 191 | BKSY_LOGON_OTH2_10 | STRING | 2 | — | — |
| 192 | BKSY_LOGON_OTH2_11 | STRING | 2 | — | — |
| 193 | BKSY_LOGON_OTH2_12 | STRING | 2 | — | — |
| 194 | BKSY_LOGON_OTH2_13 | STRING | 2 | — | — |
| 195 | BKSY_LOGON_OTH2_14 | STRING | 2 | — | — |
| 196 | BKSY_LOGON_OTH2_15 | STRING | 2 | — | — |
| 197 | BKSY_LOGON_OTH2_16 | STRING | 2 | — | — |
| 198 | BKSY_LOGON_OTH2_17 | STRING | 2 | — | — |
| 199 | BKSY_LOGON_OTH2_18 | STRING | 2 | — | — |
| 200 | BKSY_LOGON_OTH2_19 | STRING | 2 | — | — |
| 201 | BKSY_LOGON_OTH2_2 | STRING | 2 | — | — |
| 202 | BKSY_LOGON_OTH2_20 | STRING | 2 | — | — |
| 203 | BKSY_LOGON_OTH2_3 | STRING | 2 | — | — |
| 204 | BKSY_LOGON_OTH2_4 | STRING | 2 | — | — |
| 205 | BKSY_LOGON_OTH2_5 | STRING | 2 | — | — |
| 206 | BKSY_LOGON_OTH2_6 | STRING | 2 | — | — |
| 207 | BKSY_LOGON_OTH2_7 | STRING | 2 | — | — |
| 208 | BKSY_LOGON_OTH2_8 | STRING | 2 | — | — |
| 209 | BKSY_LOGON_OTH2_9 | STRING | 2 | — | — |
| 210 | BKSY_LOGON_POYN | STRING | 1 | — | — |
| 211 | BKSY_LOGON_PRYN | STRING | 1 | — | — |
| 212 | BKSY_LOGON_PSWD | STRING | 10 | — | — |
| 213 | BKSY_LOGON_SCTY | STRING | 2 | — | — |
| 214 | BKSY_LOGON_SOYN | STRING | 1 | — | — |
| 215 | BKSY_LOGON_SYYN | STRING | 1 | — | — |

## BKSYPRTR
**System printer assignments** — used by 33+ programs including EVODCSETUP/EVODEFPRINT. Stores default and per-station printer settings.

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_PRTR_EXEC | STRING | 8 | — | — |
| 2 | BKSY_PRTR_LASER | STRING | 1 | — | — |
| 3 | BKSY_PRTR_LPTNM | INTEGER | 1 | — | — |
| 4 | BKSY_PRTR_NAME | STRING | 30 | — | — |
| 5 | BKSY_PRTR_PMAX | INTEGER | 2 | — | — |
| 6 | BKSY_PRTR_POST | STRING | 8 | — | — |
| 7 | BKSY_PRTR_PPLNE | INTEGER | 2 | — | — |
| 8 | BKSY_PRTR_PRUN | STRING | 1 | — | — |
| 9 | BKSY_PRTR_PWDT | INTEGER | 2 | — | — |
| 10 | BKSY_PRTR_TAS | STRING | 1 | — | — |
| 11 | BKSY_PRTR_TYPE | STRING | 8 | — | — |

## BKUMSRTY
**NOT USED**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SCRTY_GROUP | STRING | 1 | — | — |
| 2 | SCRTY_ITEM_1 | STRING | 1 | — | — |
| 3 | SCRTY_ITEM_10 | STRING | 1 | — | — |
| 4 | SCRTY_ITEM_11 | STRING | 1 | — | — |
| 5 | SCRTY_ITEM_12 | STRING | 1 | — | — |
| 6 | SCRTY_ITEM_13 | STRING | 1 | — | — |
| 7 | SCRTY_ITEM_14 | STRING | 1 | — | — |
| 8 | SCRTY_ITEM_15 | STRING | 1 | — | — |
| 9 | SCRTY_ITEM_16 | STRING | 1 | — | — |
| 10 | SCRTY_ITEM_17 | STRING | 1 | — | — |
| 11 | SCRTY_ITEM_18 | STRING | 1 | — | — |
| 12 | SCRTY_ITEM_19 | STRING | 1 | — | — |
| 13 | SCRTY_ITEM_2 | STRING | 1 | — | — |
| 14 | SCRTY_ITEM_20 | STRING | 1 | — | — |
| 15 | SCRTY_ITEM_3 | STRING | 1 | — | — |
| 16 | SCRTY_ITEM_4 | STRING | 1 | — | — |
| 17 | SCRTY_ITEM_5 | STRING | 1 | — | — |
| 18 | SCRTY_ITEM_6 | STRING | 1 | — | — |
| 19 | SCRTY_ITEM_7 | STRING | 1 | — | — |
| 20 | SCRTY_ITEM_8 | STRING | 1 | — | — |
| 21 | SCRTY_ITEM_9 | STRING | 1 | — | — |
| 22 | SCRTY_LEVEL | STRING | 2 | — | — |
| 23 | SCRTY_MENU | INTEGER | 2 | — | — |

## BKUPDATE
**NOT USED**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKUP_COMPANY | STRING | 2 | — | — |
| 2 | BKUP_DATE | DATE | 4 | — | — |
| 3 | BKUP_UPDATE | STRING | 1 | — | — |
| 4 | BKUPDATE_VER | STRING | 15 | — | — |

## BOMCHG
**NOT USED**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BOM_CHG_ACOMP | STRING | 1 | — | — |
| 2 | BOM_CHG_AEXTRA | STRING | 100 | — | — |
| 3 | BOM_CHG_AQTY | NUMERIC | 8 | 8 | — |
| 4 | BOM_CHG_AREF | STRING | 20 | — | — |
| 5 | BOM_CHG_ASCRAP | NUMERIC | 8 | 2 | — |
| 6 | BOM_CHG_BEXTRA | STRING | 100 | — | — |
| 7 | BOM_CHG_BQTY | NUMERIC | 8 | 8 | — |
| 8 | BOM_CHG_BREF | STRING | 20 | — | — |
| 9 | BOM_CHG_BSCRAP | NUMERIC | 8 | 2 | — |
| 10 | BOM_CHG_CDATE | DATE | 4 | — | — |
| 11 | BOM_CHG_COMP | STRING | 15 | — | — |
| 12 | BOM_CHG_DCOMP | STRING | 1 | — | — |
| 13 | BOM_CHG_PARENT | STRING | 15 | — | — |
| 14 | BOM_CHG_UID | STRING | 20 | — | — |
| 15 | BOM_CHG_USER | STRING | 15 | — | — |

## CCEDIXRF
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CC_EDI_CUSTCODE | STRING | 10 | — | — |
| 2 | CC_EDI_NEXT | NUMERIC | 8 | — | — |
| 3 | CC_EDI_SENDERID | STRING | 15 | — | — |
| 4 | CC_EDI_SHIPTO | STRING | 10 | — | — |
| 5 | CC_EDI_SHPTCODE | STRING | 17 | — | — |
| 6 | CC_EDI_SHPTZIP | STRING | 10 | — | — |

## DBACNAME
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CNAME_CODE | STRING | 2 | — | — |
| 2 | CNAME_FILLER | STRING | 40 | — | — |
| 3 | CNAME_NAME | STRING | 25 | — | — |

## ESTCHGS
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESCH_AMT | NUMERIC | 8 | 2 | — |
| 2 | MTESCH_DESC | STRING | 30 | — | — |
| 3 | MTESCH_QUOTE | NUMERIC | 8 | — | — |

## ESTMAT
**NOT USED**

Fields: 18

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESMAT_CODE | STRING | 15 | — | — |
| 2 | MTESMAT_COST1 | NUMERIC | 8 | 6 | — |
| 3 | MTESMAT_COST2 | NUMERIC | 8 | 6 | — |
| 4 | MTESMAT_COST3 | NUMERIC | 8 | 6 | — |
| 5 | MTESMAT_COST4 | NUMERIC | 8 | 6 | — |
| 6 | MTESMAT_COST5 | NUMERIC | 8 | 6 | — |
| 7 | MTESMAT_COSTCD | STRING | 1 | — | — |
| 8 | MTESMAT_DESC | STRING | 30 | — | — |
| 9 | MTESMAT_QTYPER | NUMERIC | 8 | 8 | — |
| 10 | MTESMAT_QUOTE | NUMERIC | 8 | — | — |
| 11 | MTESMAT_QUREF | NUMERIC | 8 | — | — |
| 12 | MTESMAT_REMARKS_1 | STRING | 30 | — | — |
| 13 | MTESMAT_REMARKS_2 | STRING | 30 | — | — |
| 14 | MTESMAT_REMARKS_3 | STRING | 30 | — | — |
| 15 | MTESMAT_REMARKS_4 | STRING | 30 | — | — |
| 16 | MTESMAT_REMARKS_5 | STRING | 30 | — | — |
| 17 | MTESMAT_SCRAP | NUMERIC | 8 | 2 | — |
| 18 | MTESMAT_UM | STRING | 3 | — | — |

## ESTROUT
**NOT USED**

Fields: 48

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESRO_DESC | STRING | 30 | — | — |
| 2 | MTESRO_INSTR_1 | STRING | 60 | — | — |
| 3 | MTESRO_INSTR_10 | STRING | 60 | — | — |
| 4 | MTESRO_INSTR_11 | STRING | 60 | — | — |
| 5 | MTESRO_INSTR_12 | STRING | 60 | — | — |
| 6 | MTESRO_INSTR_13 | STRING | 60 | — | — |
| 7 | MTESRO_INSTR_14 | STRING | 60 | — | — |
| 8 | MTESRO_INSTR_15 | STRING | 60 | — | — |
| 9 | MTESRO_INSTR_2 | STRING | 60 | — | — |
| 10 | MTESRO_INSTR_3 | STRING | 60 | — | — |
| 11 | MTESRO_INSTR_4 | STRING | 60 | — | — |
| 12 | MTESRO_INSTR_5 | STRING | 60 | — | — |
| 13 | MTESRO_INSTR_6 | STRING | 60 | — | — |
| 14 | MTESRO_INSTR_7 | STRING | 60 | — | — |
| 15 | MTESRO_INSTR_8 | STRING | 60 | — | — |
| 16 | MTESRO_INSTR_9 | STRING | 60 | — | — |
| 17 | MTESRO_LAB1 | NUMERIC | 8 | 4 | — |
| 18 | MTESRO_LAB2 | NUMERIC | 8 | 4 | — |
| 19 | MTESRO_LAB3 | NUMERIC | 8 | 4 | — |
| 20 | MTESRO_LAB4 | NUMERIC | 8 | 4 | — |
| 21 | MTESRO_LAB5 | NUMERIC | 8 | 4 | — |
| 22 | MTESRO_MACH1 | NUMERIC | 8 | 4 | — |
| 23 | MTESRO_MACH2 | NUMERIC | 8 | 4 | — |
| 24 | MTESRO_MACH3 | NUMERIC | 8 | 4 | — |
| 25 | MTESRO_MACH4 | NUMERIC | 8 | 4 | — |
| 26 | MTESRO_MACH5 | NUMERIC | 8 | 4 | — |
| 27 | MTESRO_MISCCOST | NUMERIC | 8 | 6 | — |
| 28 | MTESRO_MISCDESC | STRING | 30 | — | — |
| 29 | MTESRO_OPCOST | NUMERIC | 8 | 6 | — |
| 30 | MTESRO_OPER | STRING | 3 | — | — |
| 31 | MTESRO_OVER1 | NUMERIC | 8 | 4 | — |
| 32 | MTESRO_OVER2 | NUMERIC | 8 | 4 | — |
| 33 | MTESRO_OVER3 | NUMERIC | 8 | 4 | — |
| 34 | MTESRO_OVER4 | NUMERIC | 8 | 4 | — |
| 35 | MTESRO_OVER5 | NUMERIC | 8 | 4 | — |
| 36 | MTESRO_PARTSHR | NUMERIC | 8 | 2 | — |
| 37 | MTESRO_QUOTE | NUMERIC | 8 | — | — |
| 38 | MTESRO_SETUP1 | NUMERIC | 8 | 4 | — |
| 39 | MTESRO_SETUP2 | NUMERIC | 8 | 4 | — |
| 40 | MTESRO_SETUP3 | NUMERIC | 8 | 4 | — |
| 41 | MTESRO_SETUP4 | NUMERIC | 8 | 4 | — |
| 42 | MTESRO_SETUP5 | NUMERIC | 8 | 4 | — |
| 43 | MTESRO_SETUPHRS | NUMERIC | 8 | 2 | — |
| 44 | MTESRO_TIMEPART | NUMERIC | 8 | 6 | — |
| 45 | MTESRO_TYPE | STRING | 1 | — | — |
| 46 | MTESRO_VENDNAME | STRING | 25 | — | — |
| 47 | MTESRO_VENDOR | STRING | 10 | — | — |
| 48 | MTESRO_WC | STRING | 12 | — | — |

## ISAMRPF
**NOT USED**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_FC_CQTY | NUMERIC | 8 | 2 | — |
| 2 | BKMRP_FC_DATE | DATE | 4 | — | — |
| 3 | BKMRP_FC_DATE1 | DATE | 4 | — | — |
| 4 | BKMRP_FC_EXTRA | STRING | 25 | — | — |
| 5 | BKMRP_FC_FLAG | STRING | 1 | — | — |
| 6 | BKMRP_FC_NUM | NUMERIC | 8 | — | — |
| 7 | BKMRP_FC_OQTY | NUMERIC | 8 | 2 | — |
| 8 | BKMRP_FC_PART | STRING | 15 | — | — |
| 9 | BKMRP_FC_QTY | NUMERIC | 8 | 2 | — |

## ISAPHCHG
**NOT USED**

Fields: 32

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAP_CHG_AARD | DATE | 4 | — | — |
| 2 | ISAP_CHG_ACONV | NUMERIC | 8 | 5 | — |
| 3 | ISAP_CHG_ADISC | NUMERIC | 8 | 2 | — |
| 4 | ISAP_CHG_AERD | DATE | 4 | — | — |
| 5 | ISAP_CHG_AEXTRA | STRING | 150 | — | — |
| 6 | ISAP_CHG_AGLA | STRING | 10 | — | — |
| 7 | ISAP_CHG_AGLD | STRING | 4 | — | — |
| 8 | ISAP_CHG_ALOC | STRING | 10 | — | — |
| 9 | ISAP_CHG_AOOQTY | NUMERIC | 8 | 2 | — |
| 10 | ISAP_CHG_AOPER | INTEGER | 2 | — | — |
| 11 | ISAP_CHG_APRICE | NUMERIC | 8 | 4 | — |
| 12 | ISAP_CHG_AWOP | NUMERIC | 8 | — | — |
| 13 | ISAP_CHG_AWOS | INTEGER | 2 | — | — |
| 14 | ISAP_CHG_BARD | DATE | 4 | — | — |
| 15 | ISAP_CHG_BCONV | NUMERIC | 8 | 5 | — |
| 16 | ISAP_CHG_BDISC | NUMERIC | 8 | 2 | — |
| 17 | ISAP_CHG_BERD | DATE | 4 | — | — |
| 18 | ISAP_CHG_BEXTRA | STRING | 150 | — | — |
| 19 | ISAP_CHG_BGLA | STRING | 10 | — | — |
| 20 | ISAP_CHG_BGLD | STRING | 4 | — | — |
| 21 | ISAP_CHG_BLOC | STRING | 10 | — | — |
| 22 | ISAP_CHG_BOOQTY | NUMERIC | 8 | 2 | — |
| 23 | ISAP_CHG_BOPER | INTEGER | 2 | — | — |
| 24 | ISAP_CHG_BPRICE | NUMERIC | 8 | 4 | — |
| 25 | ISAP_CHG_BWOP | NUMERIC | 8 | — | — |
| 26 | ISAP_CHG_BWOS | INTEGER | 2 | — | — |
| 27 | ISAP_CHG_CDATE | DATE | 4 | — | — |
| 28 | ISAP_CHG_LINEID | INTEGER | 2 | — | — |
| 29 | ISAP_CHG_PCODE | STRING | 15 | — | — |
| 30 | ISAP_CHG_PONUM | NUMERIC | 8 | — | — |
| 31 | ISAP_CHG_REVLVL | STRING | 10 | — | — |
| 32 | ISAP_CHG_USER | STRING | 15 | — | — |

## ISARICHG
**NOT USED**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | — |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | — |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | — |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | — |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | — |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | — |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | — |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | — |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | — |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | — |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | — |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | — |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | — |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | — |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | — |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | — |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | — |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | — |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | — |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | — |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | — |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | — |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | — |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | — |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | — |
| 26 | ISAR_CHG_USER | STRING | 15 | — | — |

## ISARINVX
**AR invoice cross-reference extension** — used by T7ESB/T7SOA/T7SOB (SO and estimate programs). Links invoices to extended reference data.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_INV_EXRTA2 | STRING | 100 | — | — |
| 2 | ISAR_INV_EXTRA1 | STRING | 100 | — | — |
| 3 | ISAR_INV_NUM | NUMERIC | 8 | — | — |
| 4 | ISAR_INV_SONUM | NUMERIC | 8 | — | — |

## ISAUTODC
**Auto data collection config** — used by T7AUTODCH/T7AUTODEJH (scheduled automatic DC batch posting programs).

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_AUTO_DATE | DATE | 4 | — | — |
| 2 | IS_AUTO_EMP | INTEGER | 2 | — | — |
| 3 | IS_AUTO_EXTRA | STRING | 100 | — | — |
| 4 | IS_AUTO_FILE | STRING | 8 | — | — |
| 5 | IS_AUTO_FLAG | STRING | 1 | — | — |
| 6 | IS_AUTO_IP | STRING | 64 | — | — |
| 7 | IS_AUTO_OPER | INTEGER | 2 | — | — |
| 8 | IS_AUTO_PARTS | NUMERIC | 8 | 2 | — |
| 9 | IS_AUTO_SHIFT | INTEGER | 2 | — | — |
| 10 | IS_AUTO_TIME | TIME | 4 | — | — |
| 11 | IS_AUTO_WOPRE | NUMERIC | 8 | — | — |
| 12 | IS_AUTO_WOSUF | INTEGER | 2 | — | — |

## ISBILLSH
**NOT USED**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BILLSH_BILL | STRING | 10 | — | — |
| 2 | IS_BILLSH_EXTRA | STRING | 100 | — | — |
| 3 | IS_BILLSH_FLAG | STRING | 1 | — | — |
| 4 | IS_BILLSH_SHIP | STRING | 10 | — | — |

## ISBMTMP

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 10 | — | — |
| 2 | BKBM_COMPONENT | STRING | 15 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | — |
| 4 | BKBM_DATE2 | DATE | 4 | — | — |
| 5 | BKBM_EST_LINE | NUMERIC | 8 | — | — |
| 6 | BKBM_EXTRA | STRING | 50 | — | Extra |
| 7 | BKBM_P_TYPE | STRING | 10 | — | — |
| 8 | BKBM_PARENT | STRING | 15 | — | Parent Part Code |
| 9 | BKBM_PROD_DUPOP | STRING | 1 | — | Duplicate Option blank / 1 / 2 |
| 10 | BKBM_PROD_LINE^ | INTEGER | 2 | — | — |
| 11 | BKBM_PROD_OP | STRING | 3 | — | Option ( If  in second position) |
| 12 | BKBM_PROD_OPDSC | STRING | 5 | — | — |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | — |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | — |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | — |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | — |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | — |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | — |
| 19 | BKBM_PROD_PRICE | NUMERIC | 8 | 4 | Option Pricing |
| 20 | BKBM_PROD_RTNUM | INTEGER | 2 | — | Routing  Sequence Number |
| 21 | BKBM_PROD_SCRAP | NUMERIC | 8 | 2 | Scrap Allowance Percent |
| 22 | BKBM_PROD_TYPE | STRING | 1 | — | Part Type |
| 23 | BKBM_PROD_VEND | STRING | 10 | — | Vendor Code |
| 24 | BKBM_QTY_REQD | NUMERIC | 8 | 8 | Quantity Required |
| 25 | BKBM_REFERENCE | STRING | 20 | — | Reference |
| 26 | BKBM_REV | STRING | 5 | — | Revision (not used) |
| 27 | BKBM_UID | STRING | 20 | — | — |

## ISBTCSB

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_INFO_AL1 | STRING | 25 | — | — |
| 2 | ISSR_INFO_AL10 | STRING | 25 | — | — |
| 3 | ISSR_INFO_AL11 | STRING | 25 | — | — |
| 4 | ISSR_INFO_AL12 | STRING | 25 | — | — |
| 5 | ISSR_INFO_AL13 | STRING | 25 | — | — |
| 6 | ISSR_INFO_AL14 | STRING | 25 | — | — |
| 7 | ISSR_INFO_AL15 | STRING | 25 | — | — |
| 8 | ISSR_INFO_AL16 | STRING | 25 | — | — |
| 9 | ISSR_INFO_AL17 | STRING | 25 | — | — |
| 10 | ISSR_INFO_AL18 | STRING | 25 | — | — |
| 11 | ISSR_INFO_AL19 | STRING | 25 | — | — |
| 12 | ISSR_INFO_AL2 | STRING | 25 | — | — |
| 13 | ISSR_INFO_AL20 | STRING | 25 | — | — |
| 14 | ISSR_INFO_AL3 | STRING | 25 | — | — |
| 15 | ISSR_INFO_AL4 | STRING | 25 | — | — |
| 16 | ISSR_INFO_AL5 | STRING | 25 | — | — |
| 17 | ISSR_INFO_AL6 | STRING | 25 | — | — |
| 18 | ISSR_INFO_AL7 | STRING | 25 | — | — |
| 19 | ISSR_INFO_AL8 | STRING | 25 | — | — |
| 20 | ISSR_INFO_AL9 | STRING | 25 | — | — |
| 21 | ISSR_INFO_ALPHA_1 | STRING | 25 | — | — |
| 22 | ISSR_INFO_ALPHA_10 | STRING | 25 | — | — |
| 23 | ISSR_INFO_ALPHA_11 | STRING | 25 | — | — |
| 24 | ISSR_INFO_ALPHA_12 | STRING | 25 | — | — |
| 25 | ISSR_INFO_ALPHA_13 | STRING | 25 | — | — |
| 26 | ISSR_INFO_ALPHA_14 | STRING | 25 | — | — |
| 27 | ISSR_INFO_ALPHA_15 | STRING | 25 | — | — |
| 28 | ISSR_INFO_ALPHA_16 | STRING | 25 | — | — |
| 29 | ISSR_INFO_ALPHA_17 | STRING | 25 | — | — |
| 30 | ISSR_INFO_ALPHA_18 | STRING | 25 | — | — |
| 31 | ISSR_INFO_ALPHA_19 | STRING | 25 | — | — |
| 32 | ISSR_INFO_ALPHA_2 | STRING | 25 | — | — |
| 33 | ISSR_INFO_ALPHA_20 | STRING | 25 | — | — |
| 34 | ISSR_INFO_ALPHA_3 | STRING | 25 | — | — |
| 35 | ISSR_INFO_ALPHA_4 | STRING | 25 | — | — |
| 36 | ISSR_INFO_ALPHA_5 | STRING | 25 | — | — |
| 37 | ISSR_INFO_ALPHA_6 | STRING | 25 | — | — |
| 38 | ISSR_INFO_ALPHA_7 | STRING | 25 | — | — |
| 39 | ISSR_INFO_ALPHA_8 | STRING | 25 | — | — |
| 40 | ISSR_INFO_ALPHA_9 | STRING | 25 | — | — |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | — |
| 42 | ISSR_INFO_DATE1 | DATE | 4 | — | — |
| 43 | ISSR_INFO_DATE2 | DATE | 4 | — | — |
| 44 | ISSR_INFO_DATE3 | DATE | 4 | — | — |
| 45 | ISSR_INFO_DATE4 | DATE | 4 | — | — |
| 46 | ISSR_INFO_DATE5 | DATE | 4 | — | — |
| 47 | ISSR_INFO_DATE_1 | DATE | 4 | — | — |
| 48 | ISSR_INFO_DATE_2 | DATE | 4 | — | — |
| 49 | ISSR_INFO_DATE_3 | DATE | 4 | — | — |
| 50 | ISSR_INFO_DATE_4 | DATE | 4 | — | — |
| 51 | ISSR_INFO_DATE_5 | DATE | 4 | — | — |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | — |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | — |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | — |

## ISCCBTXN
**Corrugated/Cut box transactions** — used by J7CCFABXFER (CC Fabrication Transfer). Tracks fabric/corrugated transfer records by LOT/BIN/LOC.

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_TXN_ALPHA | STRING | 15 | — | — |
| 2 | ISCC_TXN_BIN | STRING | 15 | — | — |
| 3 | ISCC_TXN_EXTRA | STRING | 50 | — | — |
| 4 | ISCC_TXN_FABRIC | STRING | 15 | — | — |
| 5 | ISCC_TXN_GDATE | DATE | 4 | — | — |
| 6 | ISCC_TXN_JOB | STRING | 15 | — | — |
| 7 | ISCC_TXN_LOC | STRING | 10 | — | — |
| 8 | ISCC_TXN_LOT | STRING | 15 | — | — |
| 9 | ISCC_TXN_LOTQTY | NUMERIC | 8 | 2 | — |
| 10 | ISCC_TXN_NEDQTY | NUMERIC | 8 | 2 | — |
| 11 | ISCC_TXN_PULQTY | NUMERIC | 8 | 2 | — |
| 12 | ISCC_TXN_SDATE | DATE | 4 | — | — |
| 13 | ISCC_TXN_SER | STRING | 25 | — | — |
| 14 | ISCC_TXN_STATUS | STRING | 1 | — | — |
| 15 | ISCC_TXN_TDATE | DATE | 4 | — | — |
| 16 | ISCC_TXN_TRANS | NUMERIC | 8 | — | — |

## ISCCICM
**Mattress cover/fabric product specification** — used by T7CCCITM (CC-C item maintenance) and J7CCITEMSYNC. Stores cover design data: fabric/ticking, fill layers (FILIT_1..4/FILQTY_1..4), cushion type, color, stripe, law label, sewing notations, SolidWorks CAD reference.

Fields: 59

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_ICM_AMTPP | STRING | 25 | — | — |
| 2 | ISCC_ICM_BOXNO | STRING | 30 | — | — |
| 3 | ISCC_ICM_BOXQTY | STRING | 30 | — | — |
| 4 | ISCC_ICM_BTNCOD | STRING | 25 | — | — |
| 5 | ISCC_ICM_BTNQTY | NUMERIC | 8 | — | — |
| 6 | ISCC_ICM_CODE | STRING | 15 | — | — |
| 7 | ISCC_ICM_COLLEC | STRING | 120 | — | — |
| 8 | ISCC_ICM_CONST | STRING | 60 | — | — |
| 9 | ISCC_ICM_CUBE | STRING | 30 | — | — |
| 10 | ISCC_ICM_CUSFD | STRING | 60 | — | — |
| 11 | ISCC_ICM_CUSHTY | STRING | 60 | — | — |
| 12 | ISCC_ICM_CUSITM | STRING | 60 | — | — |
| 13 | ISCC_ICM_CUSLAB | STRING | 60 | — | — |
| 14 | ISCC_ICM_CUST | STRING | 60 | — | — |
| 15 | ISCC_ICM_CVL | STRING | 25 | — | — |
| 16 | ISCC_ICM_CWEIGH | NUMERIC | 8 | 6 | — |
| 17 | ISCC_ICM_DACLB | STRING | 60 | — | — |
| 18 | ISCC_ICM_DACLS | STRING | 60 | — | — |
| 19 | ISCC_ICM_DESC | STRING | 30 | — | — |
| 20 | ISCC_ICM_DESC2 | STRING | 30 | — | — |
| 21 | ISCC_ICM_EUROT | STRING | 60 | — | — |
| 22 | ISCC_ICM_FABLAB | STRING | 60 | — | — |
| 23 | ISCC_ICM_FABRIC | STRING | 60 | — | — |
| 24 | ISCC_ICM_FILIT_1 | STRING | 15 | — | — |
| 25 | ISCC_ICM_FILIT_2 | STRING | 15 | — | — |
| 26 | ISCC_ICM_FILIT_3 | STRING | 15 | — | — |
| 27 | ISCC_ICM_FILIT_4 | STRING | 15 | — | — |
| 28 | ISCC_ICM_FILQTY_1 | STRING | 20 | — | — |
| 29 | ISCC_ICM_FILQTY_2 | STRING | 20 | — | — |
| 30 | ISCC_ICM_FILQTY_3 | STRING | 20 | — | — |
| 31 | ISCC_ICM_FILQTY_4 | STRING | 20 | — | — |
| 32 | ISCC_ICM_FSIZE | STRING | 30 | — | — |
| 33 | ISCC_ICM_HAVPIC | STRING | 60 | — | — |
| 34 | ISCC_ICM_HINGE | STRING | 25 | — | — |
| 35 | ISCC_ICM_LABLOC | STRING | 60 | — | — |
| 36 | ISCC_ICM_LAWLAB | STRING | 60 | — | — |
| 37 | ISCC_ICM_MILFD | STRING | 60 | — | — |
| 38 | ISCC_ICM_PDF | STRING | 60 | — | — |
| 39 | ISCC_ICM_PERCOM | STRING | 25 | — | — |
| 40 | ISCC_ICM_PNAME | STRING | 60 | — | — |
| 41 | ISCC_ICM_POLY | STRING | 20 | — | — |
| 42 | ISCC_ICM_PRICE | STRING | 60 | — | — |
| 43 | ISCC_ICM_SEWNOT | STRING | 60 | — | — |
| 44 | ISCC_ICM_SOLIDF | STRING | 25 | — | — |
| 45 | ISCC_ICM_SPY | STRING | 25 | — | — |
| 46 | ISCC_ICM_SSL | STRING | 60 | — | — |
| 47 | ISCC_ICM_STRIPE | STRING | 25 | — | — |
| 48 | ISCC_ICM_TCOLOR | STRING | 60 | — | — |
| 49 | ISCC_ICM_TIECOD | STRING | 25 | — | — |
| 50 | ISCC_ICM_TIELEN | STRING | 25 | — | — |
| 51 | ISCC_ICM_TIELOC | STRING | 60 | — | — |
| 52 | ISCC_ICM_TIEMAT | STRING | 30 | — | — |
| 53 | ISCC_ICM_TIEQTY | STRING | 20 | — | — |
| 54 | ISCC_ICM_TIES | STRING | 10 | — | — |
| 55 | ISCC_ICM_UVL | STRING | 25 | — | — |
| 56 | ISCC_ICM_WELT | STRING | 60 | — | — |
| 57 | ISCC_ICM_WLENG | STRING | 30 | — | — |
| 58 | ISCC_ICM_ZIPPER | STRING | 25 | — | — |
| 59 | ISICC_ICM_ | STRING | 25 | — | — |

## ISCCMTF
**Corrugated/Cut material transfer staging** — used by J7CCITEMSYNC. 2-field staging table for CC item sync operations.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_MTF_ITEM | STRING | 15 | — | — |
| 2 | ISCC_MTF_MTF | STRING | 60 | — | — |

## ISCMGRP
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_MTF_ITEM | STRING | 15 | — | — |
| 2 | ISCC_MTF_MTF | STRING | 60 | — | — |

## ISCONVRT
**Unit conversion table** — used by J7RCCONVTABLE and J7RCPITEX (RC customer system). Stores per-item PUM/SUM and weight conversion factor for items needing non-standard UOM conversion.

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CONV_DATE | DATE | 4 | — | — |
| 2 | IS_CONV_DESC | STRING | 90 | — | — |
| 3 | IS_CONV_EXTRA | STRING | 100 | — | — |
| 4 | IS_CONV_ITEM | STRING | 15 | — | — |
| 5 | IS_CONV_PCONV | NUMERIC | 8 | 6 | — |
| 6 | IS_CONV_PUM | STRING | 10 | — | — |
| 7 | IS_CONV_SCONV | NUMERIC | 8 | 6 | — |
| 8 | IS_CONV_SUM | STRING | 10 | — | — |
| 9 | IS_CONV_WTCONV | NUMERIC | 8 | 6 | — |

## ISDCSER

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISDC_SER_ALPHA | STRING | 30 | — | — |
| 2 | ISDC_SER_BIN | STRING | 15 | — | — |
| 3 | ISDC_SER_DATE | DATE | 4 | — | — |
| 4 | ISDC_SER_EMP | INTEGER | 2 | — | — |
| 5 | ISDC_SER_EXTRA | STRING | 100 | — | — |
| 6 | ISDC_SER_FLAG | STRING | 1 | — | — |
| 7 | ISDC_SER_GDATE | DATE | 4 | — | — |
| 8 | ISDC_SER_ITEM | STRING | 15 | — | — |
| 9 | ISDC_SER_LOC | STRING | 10 | — | — |
| 10 | ISDC_SER_LOT | STRING | 15 | — | — |
| 11 | ISDC_SER_OPER | INTEGER | 2 | — | — |
| 12 | ISDC_SER_PARTS | NUMERIC | 8 | 2 | — |
| 13 | ISDC_SER_QTY | NUMERIC | 8 | 2 | — |
| 14 | ISDC_SER_SERIAL | STRING | 25 | — | — |
| 15 | ISDC_SER_TIME | TIME | 4 | — | — |
| 16 | ISDC_SER_WOPRE | NUMERIC | 8 | — | — |
| 17 | ISDC_SER_WOSUF | INTEGER | 2 | — | — |

## ISDEPT
**Department code table** — used by T7APB/T7ARB/T7GLB/T7GLJ (AP/AR/GL programs). Department reference lookup.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_GF_DEPT | STRING | 10 | — | — |
| 2 | IS_GF_DEPT_DESC | STRING | 40 | — | — |
| 3 | IS_GF_DEPT_MISC | STRING | 100 | — | — |

## ISDIV
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_GF_DIV | STRING | 10 | — | — |
| 2 | IS_GF_DIV_DESC | STRING | 40 | — | — |
| 3 | IS_GF_DIV_MISC | STRING | 100 | — | — |

## ISDROP
**System dropdown values** — used by T7DROPDOWN and 25 other programs. Stores system-wide dropdown list options by code/type.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_DROP_CODE | STRING | 10 | — | — |
| 2 | IS_DROP_DESC | STRING | 30 | — | — |
| 3 | IS_DROP_EXTRA | STRING | 50 | — | — |
| 4 | IS_DROP_TEXT | STRING | 30 | — | — |

## ISEAB
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_EAB_CONTACT | STRING | 20 | — | — |
| 2 | IS_EAB_EMAIL | STRING | 30 | — | — |
| 3 | IS_EAB_EXTRA | STRING | 100 | — | — |
| 4 | IS_EAB_FNAME | STRING | 15 | — | — |
| 5 | IS_EAB_LNAME | STRING | 15 | — | — |
| 6 | IS_EAB_USER | STRING | 15 | — | — |

## ISGLFCOA
**NOT USED**

Fields: 67

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_3YPAST_1 | NUMERIC | 8 | 2 | — |
| 2 | ISGL_3YPAST_10 | NUMERIC | 8 | 2 | — |
| 3 | ISGL_3YPAST_11 | NUMERIC | 8 | 2 | — |
| 4 | ISGL_3YPAST_12 | NUMERIC | 8 | 2 | — |
| 5 | ISGL_3YPAST_13 | NUMERIC | 8 | 2 | — |
| 6 | ISGL_3YPAST_14 | NUMERIC | 8 | 2 | — |
| 7 | ISGL_3YPAST_2 | NUMERIC | 8 | 2 | — |
| 8 | ISGL_3YPAST_3 | NUMERIC | 8 | 2 | — |
| 9 | ISGL_3YPAST_4 | NUMERIC | 8 | 2 | — |
| 10 | ISGL_3YPAST_5 | NUMERIC | 8 | 2 | — |
| 11 | ISGL_3YPAST_6 | NUMERIC | 8 | 2 | — |
| 12 | ISGL_3YPAST_7 | NUMERIC | 8 | 2 | — |
| 13 | ISGL_3YPAST_8 | NUMERIC | 8 | 2 | — |
| 14 | ISGL_3YPAST_9 | NUMERIC | 8 | 2 | — |
| 15 | ISGL_3YPAST_YE | NUMERIC | 8 | 2 | — |
| 16 | ISGL_4YPAST_1 | NUMERIC | 8 | 2 | — |
| 17 | ISGL_4YPAST_10 | NUMERIC | 8 | 2 | — |
| 18 | ISGL_4YPAST_11 | NUMERIC | 8 | 2 | — |
| 19 | ISGL_4YPAST_12 | NUMERIC | 8 | 2 | — |
| 20 | ISGL_4YPAST_13 | NUMERIC | 8 | 2 | — |
| 21 | ISGL_4YPAST_14 | NUMERIC | 8 | 2 | — |
| 22 | ISGL_4YPAST_2 | NUMERIC | 8 | 2 | — |
| 23 | ISGL_4YPAST_3 | NUMERIC | 8 | 2 | — |
| 24 | ISGL_4YPAST_4 | NUMERIC | 8 | 2 | — |
| 25 | ISGL_4YPAST_5 | NUMERIC | 8 | 2 | — |
| 26 | ISGL_4YPAST_6 | NUMERIC | 8 | 2 | — |
| 27 | ISGL_4YPAST_7 | NUMERIC | 8 | 2 | — |
| 28 | ISGL_4YPAST_8 | NUMERIC | 8 | 2 | — |
| 29 | ISGL_4YPAST_9 | NUMERIC | 8 | 2 | — |
| 30 | ISGL_4YPAST_YE | NUMERIC | 8 | 2 | — |
| 31 | ISGL_5YPAST_1 | NUMERIC | 8 | 2 | — |
| 32 | ISGL_5YPAST_10 | NUMERIC | 8 | 2 | — |
| 33 | ISGL_5YPAST_11 | NUMERIC | 8 | 2 | — |
| 34 | ISGL_5YPAST_12 | NUMERIC | 8 | 2 | — |
| 35 | ISGL_5YPAST_13 | NUMERIC | 8 | 2 | — |
| 36 | ISGL_5YPAST_14 | NUMERIC | 8 | 2 | — |
| 37 | ISGL_5YPAST_2 | NUMERIC | 8 | 2 | — |
| 38 | ISGL_5YPAST_3 | NUMERIC | 8 | 2 | — |
| 39 | ISGL_5YPAST_4 | NUMERIC | 8 | 2 | — |
| 40 | ISGL_5YPAST_5 | NUMERIC | 8 | 2 | — |
| 41 | ISGL_5YPAST_6 | NUMERIC | 8 | 2 | — |
| 42 | ISGL_5YPAST_7 | NUMERIC | 8 | 2 | — |
| 43 | ISGL_5YPAST_8 | NUMERIC | 8 | 2 | — |
| 44 | ISGL_5YPAST_9 | NUMERIC | 8 | 2 | — |
| 45 | ISGL_5YPAST_YE | NUMERIC | 8 | 2 | — |
| 46 | ISGL_6YPAST_1 | NUMERIC | 8 | 2 | — |
| 47 | ISGL_6YPAST_10 | NUMERIC | 8 | 2 | — |
| 48 | ISGL_6YPAST_11 | NUMERIC | 8 | 2 | — |
| 49 | ISGL_6YPAST_12 | NUMERIC | 8 | 2 | — |
| 50 | ISGL_6YPAST_13 | NUMERIC | 8 | 2 | — |
| 51 | ISGL_6YPAST_14 | NUMERIC | 8 | 2 | — |
| 52 | ISGL_6YPAST_2 | NUMERIC | 8 | 2 | — |
| 53 | ISGL_6YPAST_3 | NUMERIC | 8 | 2 | — |
| 54 | ISGL_6YPAST_4 | NUMERIC | 8 | 2 | — |
| 55 | ISGL_6YPAST_5 | NUMERIC | 8 | 2 | — |
| 56 | ISGL_6YPAST_6 | NUMERIC | 8 | 2 | — |
| 57 | ISGL_6YPAST_7 | NUMERIC | 8 | 2 | — |
| 58 | ISGL_6YPAST_8 | NUMERIC | 8 | 2 | — |
| 59 | ISGL_6YPAST_9 | NUMERIC | 8 | 2 | — |
| 60 | ISGL_6YPAST_YE | NUMERIC | 8 | 2 | — |
| 61 | ISGL_ACCT | STRING | 10 | — | — |
| 62 | ISGL_ACCTD | STRING | 25 | — | — |
| 63 | ISGL_CEXTRA | STRING | 100 | — | — |
| 64 | ISGL_CR_DR | STRING | 1 | — | — |
| 65 | ISGL_GLDPT | STRING | 4 | — | — |
| 66 | ISGL_NON_CASH | STRING | 1 | — | — |
| 67 | ISGL_TYPE | STRING | 1 | — | — |

## ISGLNBGT
**GL next-period budget/balance** — used by T7AMB/T7AMH/T7AMQ/T7GLA (asset management and GL). Stores budget and next-period GL balances.

Fields: 35

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_BGT_ACCT | STRING | 10 | — | — |
| 2 | ISGL_BGT_BUD2_1 | NUMERIC | 8 | 2 | — |
| 3 | ISGL_BGT_BUD2_10 | NUMERIC | 8 | 2 | — |
| 4 | ISGL_BGT_BUD2_11 | NUMERIC | 8 | 2 | — |
| 5 | ISGL_BGT_BUD2_12 | NUMERIC | 8 | 2 | — |
| 6 | ISGL_BGT_BUD2_13 | NUMERIC | 8 | 2 | — |
| 7 | ISGL_BGT_BUD2_14 | NUMERIC | 8 | 2 | — |
| 8 | ISGL_BGT_BUD2_2 | NUMERIC | 8 | 2 | — |
| 9 | ISGL_BGT_BUD2_3 | NUMERIC | 8 | 2 | — |
| 10 | ISGL_BGT_BUD2_4 | NUMERIC | 8 | 2 | — |
| 11 | ISGL_BGT_BUD2_5 | NUMERIC | 8 | 2 | — |
| 12 | ISGL_BGT_BUD2_6 | NUMERIC | 8 | 2 | — |
| 13 | ISGL_BGT_BUD2_7 | NUMERIC | 8 | 2 | — |
| 14 | ISGL_BGT_BUD2_8 | NUMERIC | 8 | 2 | — |
| 15 | ISGL_BGT_BUD2_9 | NUMERIC | 8 | 2 | — |
| 16 | ISGL_BGT_BUDGET_1 | NUMERIC | 8 | 2 | — |
| 17 | ISGL_BGT_BUDGET_10 | NUMERIC | 8 | 2 | — |
| 18 | ISGL_BGT_BUDGET_11 | NUMERIC | 8 | 2 | — |
| 19 | ISGL_BGT_BUDGET_12 | NUMERIC | 8 | 2 | — |
| 20 | ISGL_BGT_BUDGET_13 | NUMERIC | 8 | 2 | — |
| 21 | ISGL_BGT_BUDGET_14 | NUMERIC | 8 | 2 | — |
| 22 | ISGL_BGT_BUDGET_2 | NUMERIC | 8 | 2 | — |
| 23 | ISGL_BGT_BUDGET_3 | NUMERIC | 8 | 2 | — |
| 24 | ISGL_BGT_BUDGET_4 | NUMERIC | 8 | 2 | — |
| 25 | ISGL_BGT_BUDGET_5 | NUMERIC | 8 | 2 | — |
| 26 | ISGL_BGT_BUDGET_6 | NUMERIC | 8 | 2 | — |
| 27 | ISGL_BGT_BUDGET_7 | NUMERIC | 8 | 2 | — |
| 28 | ISGL_BGT_BUDGET_8 | NUMERIC | 8 | 2 | — |
| 29 | ISGL_BGT_BUDGET_9 | NUMERIC | 8 | 2 | — |
| 30 | ISGL_BGT_DATE | DATE | 4 | — | — |
| 31 | ISGL_BGT_EDATE | DATE | 4 | — | — |
| 32 | ISGL_BGT_EXTRA | STRING | 50 | — | — |
| 33 | ISGL_BGT_FLAG | STRING | 1 | — | — |
| 34 | ISGL_BGT_GLDPT | STRING | 4 | — | — |
| 35 | ISGL_BGT_WHO | STRING | 30 | — | — |

## ISICESA
**NOT USED**

Fields: 64

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## ISLBLMAP
**Inventory label field mapping** — used by T7ING (IN-G inventory labels). Maps label template fields to item master column names.

Fields: 102

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LABEL_BCOLOR_1 | STRING | 10 | — | — |
| 2 | IS_LABEL_BCOLOR_10 | STRING | 10 | — | — |
| 3 | IS_LABEL_BCOLOR_11 | STRING | 10 | — | — |
| 4 | IS_LABEL_BCOLOR_12 | STRING | 10 | — | — |
| 5 | IS_LABEL_BCOLOR_13 | STRING | 10 | — | — |
| 6 | IS_LABEL_BCOLOR_14 | STRING | 10 | — | — |
| 7 | IS_LABEL_BCOLOR_15 | STRING | 10 | — | — |
| 8 | IS_LABEL_BCOLOR_16 | STRING | 10 | — | — |
| 9 | IS_LABEL_BCOLOR_17 | STRING | 10 | — | — |
| 10 | IS_LABEL_BCOLOR_18 | STRING | 10 | — | — |
| 11 | IS_LABEL_BCOLOR_19 | STRING | 10 | — | — |
| 12 | IS_LABEL_BCOLOR_2 | STRING | 10 | — | — |
| 13 | IS_LABEL_BCOLOR_20 | STRING | 10 | — | — |
| 14 | IS_LABEL_BCOLOR_21 | STRING | 10 | — | — |
| 15 | IS_LABEL_BCOLOR_22 | STRING | 10 | — | — |
| 16 | IS_LABEL_BCOLOR_23 | STRING | 10 | — | — |
| 17 | IS_LABEL_BCOLOR_24 | STRING | 10 | — | — |
| 18 | IS_LABEL_BCOLOR_25 | STRING | 10 | — | — |
| 19 | IS_LABEL_BCOLOR_26 | STRING | 10 | — | — |
| 20 | IS_LABEL_BCOLOR_27 | STRING | 10 | — | — |
| 21 | IS_LABEL_BCOLOR_28 | STRING | 10 | — | — |
| 22 | IS_LABEL_BCOLOR_29 | STRING | 10 | — | — |
| 23 | IS_LABEL_BCOLOR_3 | STRING | 10 | — | — |
| 24 | IS_LABEL_BCOLOR_30 | STRING | 10 | — | — |
| 25 | IS_LABEL_BCOLOR_4 | STRING | 10 | — | — |
| 26 | IS_LABEL_BCOLOR_5 | STRING | 10 | — | — |
| 27 | IS_LABEL_BCOLOR_6 | STRING | 10 | — | — |
| 28 | IS_LABEL_BCOLOR_7 | STRING | 10 | — | — |
| 29 | IS_LABEL_BCOLOR_8 | STRING | 10 | — | — |
| 30 | IS_LABEL_BCOLOR_9 | STRING | 10 | — | — |
| 31 | IS_LABEL_CDATE | DATE | 4 | — | — |
| 32 | IS_LABEL_CUST | STRING | 10 | — | — |
| 33 | IS_LABEL_DESC | STRING | 30 | — | — |
| 34 | IS_LABEL_DFLT | STRING | 1 | — | — |
| 35 | IS_LABEL_EDATE | DATE | 4 | — | — |
| 36 | IS_LABEL_EXTRA | STRING | 100 | — | — |
| 37 | IS_LABEL_FCOLOR_1 | STRING | 10 | — | — |
| 38 | IS_LABEL_FCOLOR_10 | STRING | 10 | — | — |
| 39 | IS_LABEL_FCOLOR_11 | STRING | 10 | — | — |
| 40 | IS_LABEL_FCOLOR_12 | STRING | 10 | — | — |
| 41 | IS_LABEL_FCOLOR_13 | STRING | 10 | — | — |
| 42 | IS_LABEL_FCOLOR_14 | STRING | 10 | — | — |
| 43 | IS_LABEL_FCOLOR_15 | STRING | 10 | — | — |
| 44 | IS_LABEL_FCOLOR_16 | STRING | 10 | — | — |
| 45 | IS_LABEL_FCOLOR_17 | STRING | 10 | — | — |
| 46 | IS_LABEL_FCOLOR_18 | STRING | 10 | — | — |
| 47 | IS_LABEL_FCOLOR_19 | STRING | 10 | — | — |
| 48 | IS_LABEL_FCOLOR_2 | STRING | 10 | — | — |
| 49 | IS_LABEL_FCOLOR_20 | STRING | 10 | — | — |
| 50 | IS_LABEL_FCOLOR_21 | STRING | 10 | — | — |
| 51 | IS_LABEL_FCOLOR_22 | STRING | 10 | — | — |
| 52 | IS_LABEL_FCOLOR_23 | STRING | 10 | — | — |
| 53 | IS_LABEL_FCOLOR_24 | STRING | 10 | — | — |
| 54 | IS_LABEL_FCOLOR_25 | STRING | 10 | — | — |
| 55 | IS_LABEL_FCOLOR_26 | STRING | 10 | — | — |
| 56 | IS_LABEL_FCOLOR_27 | STRING | 10 | — | — |
| 57 | IS_LABEL_FCOLOR_28 | STRING | 10 | — | — |
| 58 | IS_LABEL_FCOLOR_29 | STRING | 10 | — | — |
| 59 | IS_LABEL_FCOLOR_3 | STRING | 10 | — | — |
| 60 | IS_LABEL_FCOLOR_30 | STRING | 10 | — | — |
| 61 | IS_LABEL_FCOLOR_4 | STRING | 10 | — | — |
| 62 | IS_LABEL_FCOLOR_5 | STRING | 10 | — | — |
| 63 | IS_LABEL_FCOLOR_6 | STRING | 10 | — | — |
| 64 | IS_LABEL_FCOLOR_7 | STRING | 10 | — | — |
| 65 | IS_LABEL_FCOLOR_8 | STRING | 10 | — | — |
| 66 | IS_LABEL_FCOLOR_9 | STRING | 10 | — | — |
| 67 | IS_LABEL_FLAG | STRING | 1 | — | — |
| 68 | IS_LABEL_ITEM | STRING | 15 | — | — |
| 69 | IS_LABEL_NTYPE_1 | STRING | 3 | — | — |
| 70 | IS_LABEL_NTYPE_10 | STRING | 3 | — | — |
| 71 | IS_LABEL_NTYPE_11 | STRING | 3 | — | — |
| 72 | IS_LABEL_NTYPE_12 | STRING | 3 | — | — |
| 73 | IS_LABEL_NTYPE_13 | STRING | 3 | — | — |
| 74 | IS_LABEL_NTYPE_14 | STRING | 3 | — | — |
| 75 | IS_LABEL_NTYPE_15 | STRING | 3 | — | — |
| 76 | IS_LABEL_NTYPE_16 | STRING | 3 | — | — |
| 77 | IS_LABEL_NTYPE_17 | STRING | 3 | — | — |
| 78 | IS_LABEL_NTYPE_18 | STRING | 3 | — | — |
| 79 | IS_LABEL_NTYPE_19 | STRING | 3 | — | — |
| 80 | IS_LABEL_NTYPE_2 | STRING | 3 | — | — |
| 81 | IS_LABEL_NTYPE_20 | STRING | 3 | — | — |
| 82 | IS_LABEL_NTYPE_21 | STRING | 3 | — | — |
| 83 | IS_LABEL_NTYPE_22 | STRING | 3 | — | — |
| 84 | IS_LABEL_NTYPE_23 | STRING | 3 | — | — |
| 85 | IS_LABEL_NTYPE_24 | STRING | 3 | — | — |
| 86 | IS_LABEL_NTYPE_25 | STRING | 3 | — | — |
| 87 | IS_LABEL_NTYPE_26 | STRING | 3 | — | — |
| 88 | IS_LABEL_NTYPE_27 | STRING | 3 | — | — |
| 89 | IS_LABEL_NTYPE_28 | STRING | 3 | — | — |
| 90 | IS_LABEL_NTYPE_29 | STRING | 3 | — | — |
| 91 | IS_LABEL_NTYPE_3 | STRING | 3 | — | — |
| 92 | IS_LABEL_NTYPE_30 | STRING | 3 | — | — |
| 93 | IS_LABEL_NTYPE_4 | STRING | 3 | — | — |
| 94 | IS_LABEL_NTYPE_5 | STRING | 3 | — | — |
| 95 | IS_LABEL_NTYPE_6 | STRING | 3 | — | — |
| 96 | IS_LABEL_NTYPE_7 | STRING | 3 | — | — |
| 97 | IS_LABEL_NTYPE_8 | STRING | 3 | — | — |
| 98 | IS_LABEL_NTYPE_9 | STRING | 3 | — | — |
| 99 | IS_LABEL_NUM | STRING | 15 | — | — |
| 100 | IS_LABEL_OBS | STRING | 1 | — | — |
| 101 | IS_LABEL_RTM | STRING | 12 | — | — |
| 102 | IS_LABEL_VEND | STRING | 10 | — | — |

## ISLOTS
**PARENT COMPONENT LOT TO SERIAL MAP**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | — |
| 2 | IS_SER_CDESC | STRING | 30 | — | — |
| 3 | IS_SER_COMP | STRING | 15 | — | — |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | — |
| 5 | IS_SER_EXRA | STRING | 100 | — | — |
| 6 | IS_SER_FDATE | DATE | 4 | — | — |
| 7 | IS_SER_PARENT | STRING | 15 | — | — |
| 8 | IS_SER_PDESC | STRING | 30 | — | — |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | — |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | — |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | — |

## ISLTYPE
**LINK TYPE (NOT USED)**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LT_DESC | STRING | 30 | — | — |
| 2 | IS_LT_EXTRA | STRING | 100 | — | — |
| 3 | IS_LT_SEC | INTEGER | 2 | — | — |
| 4 | IS_LT_TYPE | STRING | 3 | — | — |

## ISPOBOX
**NOT USED**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISPOHTRK

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TRK_CDATE | DATE | 4 | — | — |
| 2 | IS_TRK_EXTRA | STRING | 100 | — | — |
| 3 | IS_TRK_NUM | STRING | 25 | — | — |
| 4 | IS_TRK_ORD | NUMERIC | 8 | — | — |
| 5 | IS_TRK_RDATE | DATE | 4 | — | — |
| 6 | IS_TRK_SHPVIA | STRING | 10 | — | — |
| 7 | IS_TRK_STATUS | STRING | 50 | — | — |

## ISPOLOG

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISPO_LOG_DATE | DATE | 4 | — | — |
| 2 | ISPO_LOG_EMP | INTEGER | 2 | — | — |
| 3 | ISPO_LOG_EXTRA | STRING | 100 | — | — |
| 4 | ISPO_LOG_NAME | STRING | 50 | — | — |
| 5 | ISPO_LOG_PONUM | NUMERIC | 8 | — | — |
| 6 | ISPO_LOG_PRGM | STRING | 8 | — | — |
| 7 | ISPO_LOG_REASON | STRING | 50 | — | — |
| 8 | ISPO_LOG_TIME | TIME | 4 | — | — |
| 9 | ISPO_LOG_WHO | STRING | 15 | — | — |

## ISPOS

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCL_CLASS | STRING | 5 | — | Class |
| 2 | BKCM_ACCL_CODE | STRING | 10 | — | Account Code |

## ISPOSC

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACCC_CCODE | STRING | 5 | — | Code for Type of Entry |
| 2 | BKCM_ACCC_DESC | STRING | 25 | — | Description of Code |

## ISPOTRK

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TRK_CDATE | DATE | 4 | — | — |
| 2 | IS_TRK_EXTRA | STRING | 100 | — | — |
| 3 | IS_TRK_NUM | STRING | 25 | — | — |
| 4 | IS_TRK_ORD | NUMERIC | 8 | — | — |
| 5 | IS_TRK_RDATE | DATE | 4 | — | — |
| 6 | IS_TRK_SHPVIA | STRING | 10 | — | — |
| 7 | IS_TRK_STATUS | STRING | 50 | — | — |

## ISPRESN

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PRESN_REASON | STRING | 30 | — | — |

## ISREPDEF
**Report definitions** — used by T7REPDEF/EXCOM/T7SOAXCOM. Stores saved report filter configurations by program and user.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_DEF_EXTRA | STRING | 50 | — | — |
| 2 | ISREP_DEF_LABEL | STRING | 5 | — | — |
| 3 | ISREP_DEF_TITLE | STRING | 30 | — | — |

## ISRTLOAD
**Routing load runtime table** — used by T7SOA/T7SOB/T7SOB75 (SO entry programs). Loads routing cost data for outside-process operations during SO entry.

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LOAD_ALOAD | STRING | 15 | — | — |
| 2 | IS_LOAD_BALQTY | NUMERIC | 8 | 2 | — |
| 3 | IS_LOAD_BIN | STRING | 15 | — | — |
| 4 | IS_LOAD_CNTR | INTEGER | 2 | — | — |
| 5 | IS_LOAD_DATE1 | DATE | 4 | — | — |
| 6 | IS_LOAD_DATE2 | DATE | 4 | — | — |
| 7 | IS_LOAD_DESC | STRING | 30 | — | — |
| 8 | IS_LOAD_EXTRA | STRING | 100 | — | — |
| 9 | IS_LOAD_ITEM | STRING | 15 | — | — |
| 10 | IS_LOAD_LOADNUM | NUMERIC | 8 | — | — |
| 11 | IS_LOAD_LOADQTY | NUMERIC | 8 | 2 | — |
| 12 | IS_LOAD_LOC | STRING | 10 | — | — |
| 13 | IS_LOAD_LOT | STRING | 15 | — | — |
| 14 | IS_LOAD_NUM2 | NUMERIC | 8 | — | — |
| 15 | IS_LOAD_ORDQTY | NUMERIC | 8 | 2 | — |
| 16 | IS_LOAD_SCANQTY | NUMERIC | 8 | 2 | — |
| 17 | IS_LOAD_SCCOGS | NUMERIC | 8 | 4 | — |
| 18 | IS_LOAD_SER | STRING | 25 | — | — |
| 19 | IS_LOAD_SOLINE | STRING | 3 | — | — |
| 20 | IS_LOAD_SONUM | NUMERIC | 8 | — | — |
| 21 | IS_LOAD_TRUCK | STRING | 15 | — | — |

## ISRTMS
**RTM printer assignments** — used by J7CCSOLABELS/J7NMITEMRTM/J7NMRTMPRINTER. Maps items to specific RTM report templates and printers.

Fields: 29

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RTM_CONTLBL | STRING | 12 | — | — |
| 2 | IS_RTM_CUST | STRING | 10 | — | — |
| 3 | IS_RTM_DATE | DATE | 4 | — | — |
| 4 | IS_RTM_DESC | STRING | 30 | — | — |
| 5 | IS_RTM_DFLT | STRING | 1 | — | — |
| 6 | IS_RTM_EXTRA | STRING | 100 | — | — |
| 7 | IS_RTM_FLAG | STRING | 1 | — | — |
| 8 | IS_RTM_ITEM | STRING | 15 | — | — |
| 9 | IS_RTM_MISCLBL1 | STRING | 12 | — | — |
| 10 | IS_RTM_MISCLBL2 | STRING | 12 | — | — |
| 11 | IS_RTM_MISCLBL3 | STRING | 12 | — | — |
| 12 | IS_RTM_MIXEDLBL | STRING | 12 | — | — |
| 13 | IS_RTM_PARTLBL | STRING | 12 | — | — |
| 14 | IS_RTM_PRINTER_1 | STRING | 90 | — | — |
| 15 | IS_RTM_PRINTER_10 | STRING | 90 | — | — |
| 16 | IS_RTM_PRINTER_2 | STRING | 90 | — | — |
| 17 | IS_RTM_PRINTER_3 | STRING | 90 | — | — |
| 18 | IS_RTM_PRINTER_4 | STRING | 90 | — | — |
| 19 | IS_RTM_PRINTER_5 | STRING | 90 | — | — |
| 20 | IS_RTM_PRINTER_6 | STRING | 90 | — | — |
| 21 | IS_RTM_PRINTER_7 | STRING | 90 | — | — |
| 22 | IS_RTM_PRINTER_8 | STRING | 90 | — | — |
| 23 | IS_RTM_PRINTER_9 | STRING | 90 | — | — |
| 24 | IS_RTM_PROGRAM | STRING | 15 | — | — |
| 25 | IS_RTM_QTY | INTEGER | 2 | — | — |
| 26 | IS_RTM_QUICKLBL | STRING | 12 | — | — |
| 27 | IS_RTM_RTM | STRING | 12 | — | — |
| 28 | IS_RTM_SHIPLBL | STRING | 12 | — | — |
| 29 | IS_RTM_VEND | STRING | 10 | — | — |

## ISSCOMP
**SPC component specifications** — used by T7SCOMP/T7SPC. Statistical Process Control; defines which components/features are inspected per process.

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SCOMP | STRING | 50 | — | — |
| 2 | IS_SCOMP_COMPND | STRING | 30 | — | — |
| 3 | IS_SCOMP_DETAIL | STRING | 20 | — | — |
| 4 | IS_SCOMP_VIS | STRING | 1 | — | — |
| 5 | IS_SCOMP_WHO | STRING | 40 | — | — |

## ISSDET
**SPC detail measurements** — used by T7SDET/T7SPC/T7SPCLIVEGRID. Stores individual measurement readings per SPC inspection sample.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SDET_DETAIL | STRING | 20 | — | — |
| 2 | IS_SDET_SUB | STRING | 1 | — | — |
| 3 | IS_SDET_TYPE | STRING | 20 | — | — |
| 4 | IS_SDET_WHO | STRING | 40 | — | — |

## ISSEPROC
**SPC process definitions** — used by T7SEPROC/T7SPC. Defines SPC measurement processes with control limits and specifications.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SEPROC_PROC | STRING | 25 | — | — |
| 2 | IS_SEPROC_WHO | STRING | 40 | — | — |

## ISSEQUIP
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SEQUIP_DESC | STRING | 40 | — | — |
| 2 | IS_SEQUIP_NAME | STRING | 20 | — | — |

## ISSERR
**SPC error/defect records** — used by T7SPC/T7SPCLIVEGRID/T7SPCREP. Records defect events with error code, process, quantity, and WO reference.

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SERR_ADIAG | STRING | 1000 | — | — |
| 2 | IS_SERR_ADOF | STRING | 1000 | — | — |
| 3 | IS_SERR_AREWORK | STRING | 1000 | — | — |
| 4 | IS_SERR_COUNT | INTEGER | 2 | — | — |
| 5 | IS_SERR_DATE | DATE | 4 | — | — |
| 6 | IS_SERR_DIAG | STRING | 0 | — | — |
| 7 | IS_SERR_DOF | STRING | 0 | — | — |
| 8 | IS_SERR_ERROR | STRING | 25 | — | — |
| 9 | IS_SERR_EXTRA | STRING | 50 | — | — |
| 10 | IS_SERR_OPER | INTEGER | 2 | — | — |
| 11 | IS_SERR_PROCESS | STRING | 25 | — | — |
| 12 | IS_SERR_REF | STRING | 50 | — | — |
| 13 | IS_SERR_REWORK | STRING | 0 | — | — |
| 14 | IS_SERR_SERIAL | STRING | 20 | — | — |
| 15 | IS_SERR_TIME | TIME | 4 | — | — |
| 16 | IS_SERR_WOPRE | NUMERIC | 8 | — | — |
| 17 | IS_SERR_WOSUF | INTEGER | 2 | — | — |

## ISSETYPE
**SPC error/event type codes** — used by T7SETYPE/T7SPC/T7SPCREP. Defines categories of defects (error types) for SPC classification.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SETYPE_ERR | STRING | 25 | — | — |
| 2 | IS_SETYPE_WHO | STRING | 40 | — | — |

## ISSHIPA
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SHPA_CODE | STRING | 10 | — | — |
| 2 | IS_SHPA_EXTRA | STRING | 50 | — | — |
| 3 | IS_SHPA_PASS | STRING | 30 | — | — |
| 4 | IS_SHPA_TOKEN | STRING | 30 | — | — |
| 5 | IS_SHPA_USER | STRING | 30 | — | — |

## ISSMTCFG
**SM time configuration** — used by T7SMTEND/T7SMTSET. Stores scheduling time-slot configuration for the SM scheduling module.

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SMT_CAP | INTEGER | 2 | — | — |
| 2 | IS_SMT_CNTR | INTEGER | 2 | — | — |
| 3 | IS_SMT_COMP | STRING | 15 | — | — |
| 4 | IS_SMT_CURRENT | STRING | 1 | — | — |
| 5 | IS_SMT_DATE | DATE | 4 | — | — |
| 6 | IS_SMT_EMP | STRING | 4 | — | — |
| 7 | IS_SMT_EXTRA | STRING | 50 | — | — |
| 8 | IS_SMT_LOT | STRING | 15 | — | — |
| 9 | IS_SMT_MACHINE | STRING | 4 | — | — |
| 10 | IS_SMT_OPER | STRING | 3 | — | — |
| 11 | IS_SMT_REEL | INTEGER | 2 | — | — |
| 12 | IS_SMT_RQTY | NUMERIC | 8 | 4 | — |
| 13 | IS_SMT_TIME | TIME | 4 | — | — |
| 14 | IS_SMT_WOPRE | NUMERIC | 8 | — | — |
| 15 | IS_SMT_WOSUF | INTEGER | 2 | — | — |

## ISSNOTES
**NOT USED**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NOTE_ALPHA | STRING | 6000 | — | — |
| 2 | IS_NOTE_CDATE | DATE | 4 | — | — |
| 3 | IS_NOTE_CONTACT | STRING | 30 | — | — |
| 4 | IS_NOTE_CTIME | STRING | 10 | — | — |
| 5 | IS_NOTE_CWHO | STRING | 15 | — | — |
| 6 | IS_NOTE_EDATE | DATE | 4 | — | — |
| 7 | IS_NOTE_ETIME | STRING | 10 | — | — |
| 8 | IS_NOTE_EWHO | STRING | 15 | — | — |
| 9 | IS_NOTE_EXTRA | STRING | 100 | — | — |
| 10 | IS_NOTE_GROUP | STRING | 4 | — | — |
| 11 | IS_NOTE_ID | STRING | 48 | — | — |
| 12 | IS_NOTE_NOTE | STRING | 0 | — | — |
| 13 | IS_NOTE_PRIVATE | STRING | 1 | — | — |
| 14 | IS_NOTE_TYPE | STRING | 3 | — | — |

## ISSPC
**SPC master records** — used by T7SPC/T7SPCLIVEGRID/T7ROJA. Master SPC measurement log: WO/Sequence/Inspector/Employee/Accepted/Rework/Scrap qtys.

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SPC_ANOTES | STRING | 1000 | — | — |
| 2 | IS_SPC_CUST | STRING | 10 | — | — |
| 3 | IS_SPC_DATE | DATE | 4 | — | — |
| 4 | IS_SPC_DETAIL | STRING | 20 | — | — |
| 5 | IS_SPC_EMPNUM | INTEGER | 2 | — | — |
| 6 | IS_SPC_EXTRA | STRING | 100 | — | — |
| 7 | IS_SPC_GOOD | INTEGER | 2 | — | — |
| 8 | IS_SPC_NOTES | STRING | 0 | — | — |
| 9 | IS_SPC_OPER | INTEGER | 2 | — | — |
| 10 | IS_SPC_PART | STRING | 15 | — | — |
| 11 | IS_SPC_REWORK | INTEGER | 2 | — | — |
| 12 | IS_SPC_SIDE | STRING | 1 | — | — |
| 13 | IS_SPC_TESTE_1 | STRING | 60 | — | — |
| 14 | IS_SPC_TESTE_2 | STRING | 60 | — | — |
| 15 | IS_SPC_TESTE_3 | STRING | 60 | — | — |
| 16 | IS_SPC_TESTR | STRING | 1 | — | — |
| 17 | IS_SPC_TESTT | STRING | 30 | — | — |
| 18 | IS_SPC_TIME | TIME | 4 | — | — |
| 19 | IS_SPC_TYPE | STRING | 20 | — | — |
| 20 | IS_SPC_WOPRE | NUMERIC | 8 | — | — |
| 21 | IS_SPC_WOSUF | INTEGER | 2 | — | — |

## ISSTEQUI
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | — |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | — |
| 3 | IS_STYPE_WHO | STRING | 40 | — | — |

## ISSTRACK
**SPC session tracking** — used by T7SPC. Audit trail for SPC data entry sessions.

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STRACK_AR | STRING | 1 | — | — |
| 2 | IS_STRACK_CLOT | STRING | 15 | — | — |
| 3 | IS_STRACK_COMP | STRING | 15 | — | — |
| 4 | IS_STRACK_CSER | STRING | 20 | — | — |
| 5 | IS_STRACK_DATE | DATE | 4 | — | — |
| 6 | IS_STRACK_EXTRA | STRING | 50 | — | — |
| 7 | IS_STRACK_NOTE | STRING | 1000 | — | — |
| 8 | IS_STRACK_OPER | INTEGER | 2 | — | — |
| 9 | IS_STRACK_PROC | STRING | 25 | — | — |
| 10 | IS_STRACK_PSER | STRING | 20 | — | — |
| 11 | IS_STRACK_TIME | TIME | 4 | — | — |
| 12 | IS_STRACK_WOPRE | NUMERIC | 8 | — | — |
| 13 | IS_STRACK_WOSUF | INTEGER | 2 | — | — |

## ISSTTYPE
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | — |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | — |
| 3 | IS_STYPE_WHO | STRING | 40 | — | — |

## ISSTYPE
**SPC/general type codes** — used by T7GENAED/T7GENGET/T7SDET/T7SERR. General event type codes shared between SPC and QC modules.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | — |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | — |
| 3 | IS_STYPE_WHO | STRING | 40 | — | — |

## ISTOOLOG
**NOT USED**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISTOOL_ACTHRS | NUMERIC | 8 | 1 | — |
| 2 | ISTOOL_ALPHA_1 | STRING | 30 | — | — |
| 3 | ISTOOL_ALPHA_2 | STRING | 30 | — | — |
| 4 | ISTOOL_ALPHA_3 | STRING | 30 | — | — |
| 5 | ISTOOL_ALPHA_4 | STRING | 30 | — | — |
| 6 | ISTOOL_ALPHA_5 | STRING | 30 | — | — |
| 7 | ISTOOL_COST | NUMERIC | 8 | 2 | — |
| 8 | ISTOOL_DATE | DATE | 4 | — | — |
| 9 | ISTOOL_DATES_1 | DATE | 4 | — | — |
| 10 | ISTOOL_DATES_2 | DATE | 4 | — | — |
| 11 | ISTOOL_DATES_3 | DATE | 4 | — | — |
| 12 | ISTOOL_EMP | INTEGER | 2 | — | — |
| 13 | ISTOOL_ESTHRS | NUMERIC | 8 | 1 | — |
| 14 | ISTOOL_EXTRA | STRING | 100 | — | — |
| 15 | ISTOOL_FLAG_1 | STRING | 1 | — | — |
| 16 | ISTOOL_FLAG_2 | STRING | 1 | — | — |
| 17 | ISTOOL_FLAG_3 | STRING | 1 | — | — |
| 18 | ISTOOL_ITEM | STRING | 15 | — | — |
| 19 | ISTOOL_LOGNUM | NUMERIC | 8 | — | — |
| 20 | ISTOOL_NOTES_1 | STRING | 60 | — | — |
| 21 | ISTOOL_NOTES_10 | STRING | 60 | — | — |
| 22 | ISTOOL_NOTES_2 | STRING | 60 | — | — |
| 23 | ISTOOL_NOTES_3 | STRING | 60 | — | — |
| 24 | ISTOOL_NOTES_4 | STRING | 60 | — | — |
| 25 | ISTOOL_NOTES_5 | STRING | 60 | — | — |
| 26 | ISTOOL_NOTES_6 | STRING | 60 | — | — |
| 27 | ISTOOL_NOTES_7 | STRING | 60 | — | — |
| 28 | ISTOOL_NOTES_8 | STRING | 60 | — | — |
| 29 | ISTOOL_NOTES_9 | STRING | 60 | — | — |
| 30 | ISTOOL_OPER | INTEGER | 2 | — | — |
| 31 | ISTOOL_TOOL | STRING | 15 | — | — |
| 32 | ISTOOL_WOPRE | NUMERIC | 8 | — | — |
| 33 | ISTOOL_WORKDESC | STRING | 60 | — | — |
| 34 | ISTOOL_WOSUF | INTEGER | 2 | — | — |

## ISUSAGE
**Item usage history** — used by T7INA/T7INAS/T7INF/T7INP (IN programs). Tracks per-item usage metrics and consumption history.

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISTS_USE_AMT_1 | NUMERIC | 8 | 2 | — |
| 2 | ISTS_USE_AMT_10 | NUMERIC | 8 | 2 | — |
| 3 | ISTS_USE_AMT_11 | NUMERIC | 8 | 2 | — |
| 4 | ISTS_USE_AMT_12 | NUMERIC | 8 | 2 | — |
| 5 | ISTS_USE_AMT_13 | NUMERIC | 8 | 2 | — |
| 6 | ISTS_USE_AMT_14 | NUMERIC | 8 | 2 | — |
| 7 | ISTS_USE_AMT_15 | NUMERIC | 8 | 2 | — |
| 8 | ISTS_USE_AMT_16 | NUMERIC | 8 | 2 | — |
| 9 | ISTS_USE_AMT_17 | NUMERIC | 8 | 2 | — |
| 10 | ISTS_USE_AMT_18 | NUMERIC | 8 | 2 | — |
| 11 | ISTS_USE_AMT_19 | NUMERIC | 8 | 2 | — |
| 12 | ISTS_USE_AMT_2 | NUMERIC | 8 | 2 | — |
| 13 | ISTS_USE_AMT_20 | NUMERIC | 8 | 2 | — |
| 14 | ISTS_USE_AMT_21 | NUMERIC | 8 | 2 | — |
| 15 | ISTS_USE_AMT_22 | NUMERIC | 8 | 2 | — |
| 16 | ISTS_USE_AMT_23 | NUMERIC | 8 | 2 | — |
| 17 | ISTS_USE_AMT_24 | NUMERIC | 8 | 2 | — |
| 18 | ISTS_USE_AMT_25 | NUMERIC | 8 | 2 | — |
| 19 | ISTS_USE_AMT_26 | NUMERIC | 8 | 2 | — |
| 20 | ISTS_USE_AMT_3 | NUMERIC | 8 | 2 | — |
| 21 | ISTS_USE_AMT_4 | NUMERIC | 8 | 2 | — |
| 22 | ISTS_USE_AMT_5 | NUMERIC | 8 | 2 | — |
| 23 | ISTS_USE_AMT_6 | NUMERIC | 8 | 2 | — |
| 24 | ISTS_USE_AMT_7 | NUMERIC | 8 | 2 | — |
| 25 | ISTS_USE_AMT_8 | NUMERIC | 8 | 2 | — |
| 26 | ISTS_USE_AMT_9 | NUMERIC | 8 | 2 | — |
| 27 | ISTS_USE_CODE | STRING | 15 | — | — |
| 28 | ISTS_USE_QTY_1 | NUMERIC | 8 | 2 | — |
| 29 | ISTS_USE_QTY_10 | NUMERIC | 8 | 2 | — |
| 30 | ISTS_USE_QTY_11 | NUMERIC | 8 | 2 | — |
| 31 | ISTS_USE_QTY_12 | NUMERIC | 8 | 2 | — |
| 32 | ISTS_USE_QTY_13 | NUMERIC | 8 | 2 | — |
| 33 | ISTS_USE_QTY_14 | NUMERIC | 8 | 2 | — |
| 34 | ISTS_USE_QTY_15 | NUMERIC | 8 | 2 | — |
| 35 | ISTS_USE_QTY_16 | NUMERIC | 8 | 2 | — |
| 36 | ISTS_USE_QTY_17 | NUMERIC | 8 | 2 | — |
| 37 | ISTS_USE_QTY_18 | NUMERIC | 8 | 2 | — |
| 38 | ISTS_USE_QTY_19 | NUMERIC | 8 | 2 | — |
| 39 | ISTS_USE_QTY_2 | NUMERIC | 8 | 2 | — |
| 40 | ISTS_USE_QTY_20 | NUMERIC | 8 | 2 | — |
| 41 | ISTS_USE_QTY_21 | NUMERIC | 8 | 2 | — |
| 42 | ISTS_USE_QTY_22 | NUMERIC | 8 | 2 | — |
| 43 | ISTS_USE_QTY_23 | NUMERIC | 8 | 2 | — |
| 44 | ISTS_USE_QTY_24 | NUMERIC | 8 | 2 | — |
| 45 | ISTS_USE_QTY_25 | NUMERIC | 8 | 2 | — |
| 46 | ISTS_USE_QTY_26 | NUMERIC | 8 | 2 | — |
| 47 | ISTS_USE_QTY_3 | NUMERIC | 8 | 2 | — |
| 48 | ISTS_USE_QTY_4 | NUMERIC | 8 | 2 | — |
| 49 | ISTS_USE_QTY_5 | NUMERIC | 8 | 2 | — |
| 50 | ISTS_USE_QTY_6 | NUMERIC | 8 | 2 | — |
| 51 | ISTS_USE_QTY_7 | NUMERIC | 8 | 2 | — |
| 52 | ISTS_USE_QTY_8 | NUMERIC | 8 | 2 | — |
| 53 | ISTS_USE_QTY_9 | NUMERIC | 8 | 2 | — |
| 54 | ISTS_USE_TYPE | STRING | 1 | — | — |

## ISVAR
**NOT USED**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_VAR_ADD1 | STRING | 30 | — | — |
| 2 | IS_VAR_ADD2 | STRING | 30 | — | — |
| 3 | IS_VAR_CITY | STRING | 20 | — | — |
| 4 | IS_VAR_COMPANY | STRING | 30 | — | — |
| 5 | IS_VAR_CONTACT | STRING | 30 | — | — |
| 6 | IS_VAR_EMAIL1_1 | STRING | 50 | — | — |
| 7 | IS_VAR_EMAIL1_2 | STRING | 50 | — | — |
| 8 | IS_VAR_EMAIL1_3 | STRING | 50 | — | — |
| 9 | IS_VAR_EMAIL1_4 | STRING | 50 | — | — |
| 10 | IS_VAR_EMAIL1_5 | STRING | 50 | — | — |
| 11 | IS_VAR_EXTRA | STRING | 150 | — | — |
| 12 | IS_VAR_LOGO | STRING | 256 | — | — |
| 13 | IS_VAR_STATE | STRING | 2 | — | — |
| 14 | IS_VAR_WEB | STRING | 100 | — | — |
| 15 | IS_VAR_WEBSUP | STRING | 100 | — | — |
| 16 | IS_VAR_WEBUPD | STRING | 100 | — | — |
| 17 | IS_VAR_ZIP | STRING | 8 | — | — |

## JGPITEMS
**Physical inventory items (legacy)** — used by T7ING/T7INH/T7INI/T7INJ. JG-era physical inventory item records (86 fields). PI count storage.

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JGP_ALLERGEN_1 | STRING | 100 | — | — |
| 2 | JGP_ALLERGEN_2 | STRING | 100 | — | — |
| 3 | JGP_ALLERGEN_3 | STRING | 100 | — | — |
| 4 | JGP_ALLERGEN_4 | STRING | 100 | — | — |
| 5 | JGP_ALLERGEN_5 | STRING | 100 | — | — |
| 6 | JGP_ALLERGEN_6 | STRING | 100 | — | — |
| 7 | JGP_ALLERGEN_7 | STRING | 100 | — | — |
| 8 | JGP_ALLERGEN_8 | STRING | 100 | — | — |
| 9 | JGP_ALLERGEN_9 | STRING | 100 | — | — |
| 10 | JGP_ASTM | STRING | 1 | — | — |
| 11 | JGP_C_OF_ORIGIN | STRING | 30 | — | — |
| 12 | JGP_CATALOG | STRING | 750 | — | — |
| 13 | JGP_CERT_1 | STRING | 100 | — | — |
| 14 | JGP_CERT_2 | STRING | 100 | — | — |
| 15 | JGP_CERT_3 | STRING | 100 | — | — |
| 16 | JGP_CERT_4 | STRING | 100 | — | — |
| 17 | JGP_CERT_5 | STRING | 100 | — | — |
| 18 | JGP_CERT_6 | STRING | 100 | — | — |
| 19 | JGP_CERT_7 | STRING | 100 | — | — |
| 20 | JGP_CERT_8 | STRING | 100 | — | — |
| 21 | JGP_CERT_9 | STRING | 100 | — | — |
| 22 | JGP_EXTRA | STRING | 100 | — | — |
| 23 | JGP_GEN_ALPHA_1 | STRING | 15 | — | — |
| 24 | JGP_GEN_ALPHA_2 | STRING | 15 | — | — |
| 25 | JGP_GEN_ALPHA_3 | STRING | 15 | — | — |
| 26 | JGP_GEN_ALPHA_4 | STRING | 15 | — | — |
| 27 | JGP_GEN_ALPHA_5 | STRING | 15 | — | — |
| 28 | JGP_GEN_DATE_1 | DATE | 4 | — | — |
| 29 | JGP_GEN_DATE_2 | DATE | 4 | — | — |
| 30 | JGP_GEN_DATE_3 | DATE | 4 | — | — |
| 31 | JGP_GEN_DATE_4 | DATE | 4 | — | — |
| 32 | JGP_GEN_DATE_5 | DATE | 4 | — | — |
| 33 | JGP_GEN_FLAG_1 | STRING | 1 | — | — |
| 34 | JGP_GEN_FLAG_2 | STRING | 1 | — | — |
| 35 | JGP_GEN_FLAG_3 | STRING | 1 | — | — |
| 36 | JGP_GEN_FLAG_4 | STRING | 1 | — | — |
| 37 | JGP_GEN_FLAG_5 | STRING | 1 | — | — |
| 38 | JGP_GEN_NUM | NUMERIC | 8 | — | — |
| 39 | JGP_IND_CUBE | NUMERIC | 8 | 4 | — |
| 40 | JGP_IND_D | NUMERIC | 8 | 4 | — |
| 41 | JGP_IND_H | NUMERIC | 8 | 4 | — |
| 42 | JGP_IND_UPC | STRING | 13 | — | — |
| 43 | JGP_IND_W | NUMERIC | 8 | 4 | — |
| 44 | JGP_IND_WT | NUMERIC | 8 | 4 | — |
| 45 | JGP_ISBN | STRING | 17 | — | — |
| 46 | JGP_ITEM | STRING | 15 | — | — |
| 47 | JGP_LITEM | STRING | 30 | — | — |
| 48 | JGP_LOCATION1 | STRING | 10 | — | — |
| 49 | JGP_LOCATION2 | STRING | 10 | — | — |
| 50 | JGP_LOCATION3 | STRING | 10 | — | — |
| 51 | JGP_LONG_DESC | STRING | 750 | — | — |
| 52 | JGP_MC_BARCODE | STRING | 14 | — | — |
| 53 | JGP_MC_QTY | NUMERIC | 8 | 2 | — |
| 54 | JGP_MCART_CUBE | NUMERIC | 8 | 4 | — |
| 55 | JGP_MCART_D | NUMERIC | 8 | 4 | — |
| 56 | JGP_MCART_H | NUMERIC | 8 | 4 | — |
| 57 | JGP_MCART_W | NUMERIC | 8 | 4 | — |
| 58 | JGP_MCART_WT | NUMERIC | 8 | 4 | — |
| 59 | JGP_MIN_AGE | INTEGER | 2 | — | — |
| 60 | JGP_NET_ACOST | NUMERIC | 8 | 2 | — |
| 61 | JGP_NET_COST | STRING | 1 | — | — |
| 62 | JGP_PAL_BARCODE | STRING | 14 | — | — |
| 63 | JGP_PAL_QTY | NUMERIC | 8 | 2 | — |
| 64 | JGP_PALLET_CUBE | NUMERIC | 8 | 4 | — |
| 65 | JGP_PALLET_D | NUMERIC | 8 | 4 | — |
| 66 | JGP_PALLET_H | NUMERIC | 8 | 4 | — |
| 67 | JGP_PALLET_W | NUMERIC | 8 | 4 | — |
| 68 | JGP_PALLET_WT | NUMERIC | 8 | 4 | — |
| 69 | JGP_PREF_CRIT | STRING | 1 | — | — |
| 70 | JGP_PRODUCER | STRING | 1 | — | — |
| 71 | JGP_REVDT_BACK | STRING | 4 | — | — |
| 72 | JGP_REVDT_FRONT | STRING | 4 | — | — |
| 73 | JGP_SP_BARCODE | STRING | 14 | — | — |
| 74 | JGP_SP_QTY | NUMERIC | 8 | 2 | — |
| 75 | JGP_SPACK_CUBE | NUMERIC | 8 | 4 | — |
| 76 | JGP_SPACK_D | NUMERIC | 8 | 4 | — |
| 77 | JGP_SPACK_H | NUMERIC | 8 | 4 | — |
| 78 | JGP_SPACK_W | NUMERIC | 8 | 4 | — |
| 79 | JGP_SPACK_WT | NUMERIC | 8 | 4 | — |
| 80 | JGP_TARRIF_CODE | STRING | 15 | — | — |
| 81 | JGP_UOM_CUBE | NUMERIC | 8 | 4 | — |
| 82 | JGP_UOM_D | NUMERIC | 8 | 4 | — |
| 83 | JGP_UOM_H | NUMERIC | 8 | 4 | — |
| 84 | JGP_UOM_UPC | STRING | 13 | — | — |
| 85 | JGP_UOM_W | NUMERIC | 8 | 4 | — |
| 86 | JGP_UOM_WT | NUMERIC | 8 | 4 | — |

## JSPCNLCD
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JSP_CNLCD_CDATE | DATE | 4 | — | — |
| 2 | JSP_CNLCD_CODE | STRING | 1 | — | — |
| 3 | JSP_CNLCD_DESC | STRING | 30 | — | — |
| 4 | JSP_CNLCD_EXTRA | STRING | 100 | — | — |
| 5 | JSP_CNLCD_LCODE | STRING | 10 | — | — |
| 6 | JSP_CNLCD_WHO | STRING | 20 | — | — |

## JSPCNLSO
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JSP_CNLSO_CDATE | DATE | 4 | — | — |
| 2 | JSP_CNLSO_CQTY | NUMERIC | 8 | 2 | — |
| 3 | JSP_CNLSO_CTIME | TIME | 4 | — | — |
| 4 | JSP_CNLSO_CUST | STRING | 10 | — | — |
| 5 | JSP_CNLSO_EXTRA | STRING | 100 | — | — |
| 6 | JSP_CNLSO_FLAG | STRING | 1 | — | — |
| 7 | JSP_CNLSO_GDATE | DATE | 4 | — | — |
| 8 | JSP_CNLSO_ITEM | STRING | 15 | — | — |
| 9 | JSP_CNLSO_SONUM | NUMERIC | 8 | — | — |
| 10 | JSP_CNLSO_STAT | STRING | 1 | — | — |
| 11 | JSP_CNLSO_UNUM | NUMERIC | 8 | 4 | — |
| 12 | JSP_CNLSO_WHO | STRING | 20 | — | — |

## MENUFILE
**NOT USED**

Fields: 108

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MENU_CODE | STRING | 4 | — | — |
| 2 | MENU_ESCAPE | STRING | 4 | — | — |
| 3 | MENU_LEFT | STRING | 4 | — | — |
| 4 | MENU_LINES_1 | STRING | 30 | — | — |
| 5 | MENU_LINES_10 | STRING | 30 | — | — |
| 6 | MENU_LINES_11 | STRING | 30 | — | — |
| 7 | MENU_LINES_12 | STRING | 30 | — | — |
| 8 | MENU_LINES_13 | STRING | 30 | — | — |
| 9 | MENU_LINES_14 | STRING | 30 | — | — |
| 10 | MENU_LINES_15 | STRING | 30 | — | — |
| 11 | MENU_LINES_16 | STRING | 30 | — | — |
| 12 | MENU_LINES_17 | STRING | 30 | — | — |
| 13 | MENU_LINES_18 | STRING | 30 | — | — |
| 14 | MENU_LINES_19 | STRING | 30 | — | — |
| 15 | MENU_LINES_2 | STRING | 30 | — | — |
| 16 | MENU_LINES_20 | STRING | 30 | — | — |
| 17 | MENU_LINES_3 | STRING | 30 | — | — |
| 18 | MENU_LINES_4 | STRING | 30 | — | — |
| 19 | MENU_LINES_5 | STRING | 30 | — | — |
| 20 | MENU_LINES_6 | STRING | 30 | — | — |
| 21 | MENU_LINES_7 | STRING | 30 | — | — |
| 22 | MENU_LINES_8 | STRING | 30 | — | — |
| 23 | MENU_LINES_9 | STRING | 30 | — | — |
| 24 | MENU_LL_COL | INTEGER | 2 | — | — |
| 25 | MENU_LL_ROW | INTEGER | 2 | — | — |
| 26 | MENU_NAMES_1 | STRING | 4 | — | — |
| 27 | MENU_NAMES_10 | STRING | 4 | — | — |
| 28 | MENU_NAMES_11 | STRING | 4 | — | — |
| 29 | MENU_NAMES_12 | STRING | 4 | — | — |
| 30 | MENU_NAMES_13 | STRING | 4 | — | — |
| 31 | MENU_NAMES_14 | STRING | 4 | — | — |
| 32 | MENU_NAMES_15 | STRING | 4 | — | — |
| 33 | MENU_NAMES_16 | STRING | 4 | — | — |
| 34 | MENU_NAMES_17 | STRING | 4 | — | — |
| 35 | MENU_NAMES_18 | STRING | 4 | — | — |
| 36 | MENU_NAMES_19 | STRING | 4 | — | — |
| 37 | MENU_NAMES_2 | STRING | 4 | — | — |
| 38 | MENU_NAMES_20 | STRING | 4 | — | — |
| 39 | MENU_NAMES_3 | STRING | 4 | — | — |
| 40 | MENU_NAMES_4 | STRING | 4 | — | — |
| 41 | MENU_NAMES_5 | STRING | 4 | — | — |
| 42 | MENU_NAMES_6 | STRING | 4 | — | — |
| 43 | MENU_NAMES_7 | STRING | 4 | — | — |
| 44 | MENU_NAMES_8 | STRING | 4 | — | — |
| 45 | MENU_NAMES_9 | STRING | 4 | — | — |
| 46 | MENU_OPTIONS_1 | STRING | 1 | — | — |
| 47 | MENU_OPTIONS_10 | STRING | 1 | — | — |
| 48 | MENU_OPTIONS_11 | STRING | 1 | — | — |
| 49 | MENU_OPTIONS_12 | STRING | 1 | — | — |
| 50 | MENU_OPTIONS_13 | STRING | 1 | — | — |
| 51 | MENU_OPTIONS_14 | STRING | 1 | — | — |
| 52 | MENU_OPTIONS_15 | STRING | 1 | — | — |
| 53 | MENU_OPTIONS_16 | STRING | 1 | — | — |
| 54 | MENU_OPTIONS_17 | STRING | 1 | — | — |
| 55 | MENU_OPTIONS_18 | STRING | 1 | — | — |
| 56 | MENU_OPTIONS_19 | STRING | 1 | — | — |
| 57 | MENU_OPTIONS_2 | STRING | 1 | — | — |
| 58 | MENU_OPTIONS_20 | STRING | 1 | — | — |
| 59 | MENU_OPTIONS_3 | STRING | 1 | — | — |
| 60 | MENU_OPTIONS_4 | STRING | 1 | — | — |
| 61 | MENU_OPTIONS_5 | STRING | 1 | — | — |
| 62 | MENU_OPTIONS_6 | STRING | 1 | — | — |
| 63 | MENU_OPTIONS_7 | STRING | 1 | — | — |
| 64 | MENU_OPTIONS_8 | STRING | 1 | — | — |
| 65 | MENU_OPTIONS_9 | STRING | 1 | — | — |
| 66 | MENU_PROG_1 | STRING | 8 | — | — |
| 67 | MENU_PROG_10 | STRING | 8 | — | — |
| 68 | MENU_PROG_11 | STRING | 8 | — | — |
| 69 | MENU_PROG_12 | STRING | 8 | — | — |
| 70 | MENU_PROG_13 | STRING | 8 | — | — |
| 71 | MENU_PROG_14 | STRING | 8 | — | — |
| 72 | MENU_PROG_15 | STRING | 8 | — | — |
| 73 | MENU_PROG_16 | STRING | 8 | — | — |
| 74 | MENU_PROG_17 | STRING | 8 | — | — |
| 75 | MENU_PROG_18 | STRING | 8 | — | — |
| 76 | MENU_PROG_19 | STRING | 8 | — | — |
| 77 | MENU_PROG_2 | STRING | 8 | — | — |
| 78 | MENU_PROG_20 | STRING | 8 | — | — |
| 79 | MENU_PROG_3 | STRING | 8 | — | — |
| 80 | MENU_PROG_4 | STRING | 8 | — | — |
| 81 | MENU_PROG_5 | STRING | 8 | — | — |
| 82 | MENU_PROG_6 | STRING | 8 | — | — |
| 83 | MENU_PROG_7 | STRING | 8 | — | — |
| 84 | MENU_PROG_8 | STRING | 8 | — | — |
| 85 | MENU_PROG_9 | STRING | 8 | — | — |
| 86 | MENU_RIGHT | STRING | 4 | — | — |
| 87 | MENU_TITLE | STRING | 30 | — | — |
| 88 | MENU_TYPES_1 | STRING | 1 | — | — |
| 89 | MENU_TYPES_10 | STRING | 1 | — | — |
| 90 | MENU_TYPES_11 | STRING | 1 | — | — |
| 91 | MENU_TYPES_12 | STRING | 1 | — | — |
| 92 | MENU_TYPES_13 | STRING | 1 | — | — |
| 93 | MENU_TYPES_14 | STRING | 1 | — | — |
| 94 | MENU_TYPES_15 | STRING | 1 | — | — |
| 95 | MENU_TYPES_16 | STRING | 1 | — | — |
| 96 | MENU_TYPES_17 | STRING | 1 | — | — |
| 97 | MENU_TYPES_18 | STRING | 1 | — | — |
| 98 | MENU_TYPES_19 | STRING | 1 | — | — |
| 99 | MENU_TYPES_2 | STRING | 1 | — | — |
| 100 | MENU_TYPES_20 | STRING | 1 | — | — |
| 101 | MENU_TYPES_3 | STRING | 1 | — | — |
| 102 | MENU_TYPES_4 | STRING | 1 | — | — |
| 103 | MENU_TYPES_5 | STRING | 1 | — | — |
| 104 | MENU_TYPES_6 | STRING | 1 | — | — |
| 105 | MENU_TYPES_7 | STRING | 1 | — | — |
| 106 | MENU_TYPES_8 | STRING | 1 | — | — |
| 107 | MENU_TYPES_9 | STRING | 1 | — | — |
| 108 | MENU_WIDTH | INTEGER | 2 | — | — |

## MKASSIGN
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKASSIGN_ACCT | STRING | 10 | — | — |
| 2 | MKASSIGN_NXTDAT | DATE | 4 | — | — |
| 3 | MKASSIGN_NXTSEQ | INTEGER | 2 | — | — |
| 4 | MKASSIGN_PRCODE | NUMERIC | 8 | — | — |
| 5 | MKASSIGN_SALEND | DATE | 4 | — | — |
| 6 | MKASSIGN_TRACK | NUMERIC | 8 | — | — |

## MKDEF
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKDEF_CALENDAR | STRING | 1 | — | — |
| 2 | MKDEF_ECNEXTID | NUMERIC | 8 | — | — |
| 3 | MKDEF_ENEXTID | NUMERIC | 8 | — | — |
| 4 | MKDEF_FNEXTID | NUMERIC | 8 | — | — |
| 5 | MKDEF_FUCODE | STRING | 3 | — | — |
| 6 | MKDEF_HISTORYCD | STRING | 2 | — | — |
| 7 | MKDEF_PRICECD | NUMERIC | 8 | — | — |
| 8 | MKDEF_REQUIRE | STRING | 1 | — | — |
| 9 | MKDEF_TCNEXTID | NUMERIC | 8 | — | — |
| 10 | MKDEF_TNEXTID | NUMERIC | 8 | — | — |
| 11 | MKDEF_TRACK | NUMERIC | 8 | — | — |

## MKEVENT
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKEVENT_ACTIVE | STRING | 1 | — | — |
| 2 | MKEVENT_CLASS | NUMERIC | 8 | — | — |
| 3 | MKEVENT_DESC | STRING | 45 | — | — |
| 4 | MKEVENT_FORM | NUMERIC | 8 | — | — |
| 5 | MKEVENT_FUCODE | STRING | 3 | — | — |
| 6 | MKEVENT_GENNAME | STRING | 45 | — | — |
| 7 | MKEVENT_HISTCD | STRING | 2 | — | — |
| 8 | MKEVENT_MEDIA | STRING | 1 | — | — |
| 9 | MKEVENT_NUM | NUMERIC | 8 | — | — |
| 10 | MKEVENT_REM1 | STRING | 60 | — | — |
| 11 | MKEVENT_REM2 | STRING | 60 | — | — |
| 12 | MKEVENT_SENDTO | INTEGER | 2 | — | — |

## MKFORM
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKFORM_ACTIVE | STRING | 1 | — | — |
| 2 | MKFORM_ATT | STRING | 25 | — | — |
| 3 | MKFORM_DESC | STRING | 45 | — | — |
| 4 | MKFORM_FILE | STRING | 25 | — | — |
| 5 | MKFORM_MEDIA | STRING | 1 | — | — |
| 6 | MKFORM_NUM | NUMERIC | 8 | — | — |

## MKTCLASS
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTCLASS_ACTIVE | STRING | 1 | — | — |
| 2 | MKTCLASS_CLASS | STRING | 45 | — | — |
| 3 | MKTCLASS_NUM | NUMERIC | 8 | — | — |

## MKTNOTE
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKNOTE_TEXT | STRING | 70 | — | — |
| 2 | MKTNOTE_LINE | INTEGER | 2 | — | — |
| 3 | MKTNOTE_TRACK | NUMERIC | 8 | — | — |

## MKTRACK
**MK tracking** — used by T7GLJ (GL journal). Tracks GL journal entries for MK module transactions.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTRACK_ACTIVE | STRING | 1 | — | — |
| 2 | MKTRACK_CLASS | NUMERIC | 8 | — | — |
| 3 | MKTRACK_DESC | STRING | 45 | — | — |
| 4 | MKTRACK_NUM | NUMERIC | 8 | — | — |

## MKTROUT
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTROUT_DAYSNXT | INTEGER | 2 | — | — |
| 2 | MKTROUT_EVENT | NUMERIC | 8 | — | — |
| 3 | MKTROUT_FIXED | STRING | 1 | — | — |
| 4 | MKTROUT_JUMP | STRING | 1 | — | — |
| 5 | MKTROUT_NEXTSEQ | INTEGER | 2 | — | — |
| 6 | MKTROUT_PRICECD | NUMERIC | 8 | — | — |
| 7 | MKTROUT_SALEBEG | STRING | 1 | — | — |
| 8 | MKTROUT_SALECLO | STRING | 1 | — | — |
| 9 | MKTROUT_SALELEN | INTEGER | 2 | — | — |
| 10 | MKTROUT_SEQ | INTEGER | 2 | — | — |
| 11 | MKTROUT_TRACK | NUMERIC | 8 | — | — |

## MTINVDEF
**NOT USED**

Fields: 109

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIC_PROD_ABC | STRING | 1 | — | Vendor Approval ,1,2 |
| 2 | MTIC_PROD_ACTIV | STRING | 1 | — | Active Inventory Y/N |
| 3 | MTIC_PROD_AVAIL | NUMERIC | 8 | 2 | Available |
| 4 | MTIC_PROD_CLASS | STRING | 4 | — | Product Class |
| 5 | MTIC_PROD_CLDES | STRING | 30 | — | Product Class Description |
| 6 | MTIC_PROD_CODE | STRING | 15 | — | Produce Code (Part Number) |
| 7 | MTIC_PROD_COMM | NUMERIC | 8 | 4 | Commission |
| 8 | MTIC_PROD_COST | STRING | 1 | — | Not Used |
| 9 | MTIC_PROD_CUBFT | NUMERIC | 8 | 4 | Cubic Feet |
| 10 | MTIC_PROD_CUM | STRING | 3 | — | Not Used |
| 11 | MTIC_PROD_CUSNM | STRING | 30 | — | Customer Name (not used) |
| 12 | MTIC_PROD_CUST | STRING | 10 | — | Customer Code |
| 13 | MTIC_PROD_CYCLE | STRING | 1 | — | Cycle Count Code |
| 14 | MTIC_PROD_DELBF | INTEGER | 2 | — | MRP Delay Buffer |
| 15 | MTIC_PROD_DESC | STRING | 30 | — | Description - Line 1 |
| 16 | MTIC_PROD_DRAW | STRING | 15 | — | Drawing Number |
| 17 | MTIC_PROD_ESTCD | STRING | 1 | — | Not Used |
| 18 | MTIC_PROD_EXPBF | INTEGER | 2 | — | MRP Expedite Buffer |
| 19 | MTIC_PROD_FRT | NUMERIC | 8 | 6 | Freight Percent |
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | — |
| 21 | MTIC_PROD_GLINV | STRING | 10 | — | Not Used |
| 22 | MTIC_PROD_GLWIP | STRING | 10 | — | GL WIP Account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | — | Not Used |
| 24 | MTIC_PROD_LEAD | INTEGER | 2 | — | Lead Time - Days |
| 25 | MTIC_PROD_LOC | STRING | 10 | — | Inventory Bin Location |
| 26 | MTIC_PROD_LONGP | STRING | 25 | — | Not Used |
| 27 | MTIC_PROD_LOT | STRING | 1 | — | Lot Control Y/N |
| 28 | MTIC_PROD_LOTSZ | NUMERIC | 8 | — | Lot Size |
| 29 | MTIC_PROD_MRP | STRING | 1 | — | MRP Item Y/N |
| 30 | MTIC_PROD_MRPSW | STRING | 1 | — | MRP Round to Whole Number Y/N |
| 31 | MTIC_PROD_OPT | STRING | 1 | — | Has Options Y/N |
| 32 | MTIC_PROD_OPTCD | STRING | 5 | — | Not Used |
| 33 | MTIC_PROD_OPTCS | STRING | 1 | — | Not Used |
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | — |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | — |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | — |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | — |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | — |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | — |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | — |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | — |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | — |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | — |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | — |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | — |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | — |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | — |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | — |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | — |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | — |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | — |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | — |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | — |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | — |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | — |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | — |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | — |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | — |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | — |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | — |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | — |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | — |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | — |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | — |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | — |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | — |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | — |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | — |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | — |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | — |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | — |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | — |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | — |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | — |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | — |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | — |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | — |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | — |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | — |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | — |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | — |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | — |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | — |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | — |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | — |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | — |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | — |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | — |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | — |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | — |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | — |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | — |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | — |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | — |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | — |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## MWOPTEMP
**NOT USED**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MWOP_CNTR | NUMERIC | 8 | — | — |
| 2 | MWOP_EXTRA | STRING | 100 | — | — |
| 3 | MWOP_QTYCOM | NUMERIC | 8 | 2 | — |
| 4 | MWOP_SERIAL | STRING | 25 | — | — |
| 5 | MWOP_SRC | INTEGER | 2 | — | — |
| 6 | MWOP_STATUS | STRING | 10 | — | — |
| 7 | MWOP_WOPRE | NUMERIC | 8 | — | — |
| 8 | MWOP_WOSUF | INTEGER | 2 | — | — |

## NZITPRE
**NOT USED**

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | NZ_IPRE_DESC_1 | STRING | 30 | — | — |
| 2 | NZ_IPRE_DESC_10 | STRING | 30 | — | — |
| 3 | NZ_IPRE_DESC_11 | STRING | 30 | — | — |
| 4 | NZ_IPRE_DESC_12 | STRING | 30 | — | — |
| 5 | NZ_IPRE_DESC_13 | STRING | 30 | — | — |
| 6 | NZ_IPRE_DESC_14 | STRING | 30 | — | — |
| 7 | NZ_IPRE_DESC_15 | STRING | 30 | — | — |
| 8 | NZ_IPRE_DESC_16 | STRING | 30 | — | — |
| 9 | NZ_IPRE_DESC_17 | STRING | 30 | — | — |
| 10 | NZ_IPRE_DESC_18 | STRING | 30 | — | — |
| 11 | NZ_IPRE_DESC_2 | STRING | 30 | — | — |
| 12 | NZ_IPRE_DESC_3 | STRING | 30 | — | — |
| 13 | NZ_IPRE_DESC_4 | STRING | 30 | — | — |
| 14 | NZ_IPRE_DESC_5 | STRING | 30 | — | — |
| 15 | NZ_IPRE_DESC_6 | STRING | 30 | — | — |
| 16 | NZ_IPRE_DESC_7 | STRING | 30 | — | — |
| 17 | NZ_IPRE_DESC_8 | STRING | 30 | — | — |
| 18 | NZ_IPRE_DESC_9 | STRING | 30 | — | — |
| 19 | NZ_IPRE_NXTNUM_1 | NUMERIC | 8 | — | — |
| 20 | NZ_IPRE_NXTNUM_10 | NUMERIC | 8 | — | — |
| 21 | NZ_IPRE_NXTNUM_11 | NUMERIC | 8 | — | — |
| 22 | NZ_IPRE_NXTNUM_12 | NUMERIC | 8 | — | — |
| 23 | NZ_IPRE_NXTNUM_13 | NUMERIC | 8 | — | — |
| 24 | NZ_IPRE_NXTNUM_14 | NUMERIC | 8 | — | — |
| 25 | NZ_IPRE_NXTNUM_15 | NUMERIC | 8 | — | — |
| 26 | NZ_IPRE_NXTNUM_16 | NUMERIC | 8 | — | — |
| 27 | NZ_IPRE_NXTNUM_17 | NUMERIC | 8 | — | — |
| 28 | NZ_IPRE_NXTNUM_18 | NUMERIC | 8 | — | — |
| 29 | NZ_IPRE_NXTNUM_2 | NUMERIC | 8 | — | — |
| 30 | NZ_IPRE_NXTNUM_3 | NUMERIC | 8 | — | — |
| 31 | NZ_IPRE_NXTNUM_4 | NUMERIC | 8 | — | — |
| 32 | NZ_IPRE_NXTNUM_5 | NUMERIC | 8 | — | — |
| 33 | NZ_IPRE_NXTNUM_6 | NUMERIC | 8 | — | — |
| 34 | NZ_IPRE_NXTNUM_7 | NUMERIC | 8 | — | — |
| 35 | NZ_IPRE_NXTNUM_8 | NUMERIC | 8 | — | — |
| 36 | NZ_IPRE_NXTNUM_9 | NUMERIC | 8 | — | — |
| 37 | NZ_IPRE_PREFIX_1 | NUMERIC | 8 | — | — |
| 38 | NZ_IPRE_PREFIX_10 | NUMERIC | 8 | — | — |
| 39 | NZ_IPRE_PREFIX_11 | NUMERIC | 8 | — | — |
| 40 | NZ_IPRE_PREFIX_12 | NUMERIC | 8 | — | — |
| 41 | NZ_IPRE_PREFIX_13 | NUMERIC | 8 | — | — |
| 42 | NZ_IPRE_PREFIX_14 | NUMERIC | 8 | — | — |
| 43 | NZ_IPRE_PREFIX_15 | NUMERIC | 8 | — | — |
| 44 | NZ_IPRE_PREFIX_16 | NUMERIC | 8 | — | — |
| 45 | NZ_IPRE_PREFIX_17 | NUMERIC | 8 | — | — |
| 46 | NZ_IPRE_PREFIX_18 | NUMERIC | 8 | — | — |
| 47 | NZ_IPRE_PREFIX_2 | NUMERIC | 8 | — | — |
| 48 | NZ_IPRE_PREFIX_3 | NUMERIC | 8 | — | — |
| 49 | NZ_IPRE_PREFIX_4 | NUMERIC | 8 | — | — |
| 50 | NZ_IPRE_PREFIX_5 | NUMERIC | 8 | — | — |
| 51 | NZ_IPRE_PREFIX_6 | NUMERIC | 8 | — | — |
| 52 | NZ_IPRE_PREFIX_7 | NUMERIC | 8 | — | — |
| 53 | NZ_IPRE_PREFIX_8 | NUMERIC | 8 | — | — |
| 54 | NZ_IPRE_PREFIX_9 | NUMERIC | 8 | — | — |

## OPQCDESC
**Operation QC descriptions** — used by T7DCA/T7DCALABEL/T7ADCA (DC programs). QC description text per routing operation for the DC workstation display.

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | OPQC_DATE | DATE | 4 | — | — |
| 2 | OPQC_DESC | STRING | 30 | — | — |
| 3 | OPQC_EXTRA | STRING | 50 | — | — |
| 4 | OPQC_OPER | INTEGER | 2 | — | — |
| 5 | OPQC_QCCODE | STRING | 2 | — | — |
| 6 | OPQC_QTY | NUMERIC | 8 | 2 | — |
| 7 | OPQC_SERIAL | STRING | 25 | — | — |
| 8 | OPQC_UID | STRING | 30 | — | — |
| 9 | OPQC_WOPRE | NUMERIC | 8 | — | — |
| 10 | OPQC_WOSUF | INTEGER | 2 | — | — |

## SUMCUST
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMCUST_COGS | NUMERIC | 8 | 4 | — |
| 2 | SUMCUST_CUST | STRING | 10 | — | — |
| 3 | SUMCUST_MONTH | INTEGER | 2 | — | — |
| 4 | SUMCUST_SALES | NUMERIC | 8 | 4 | — |
| 5 | SUMCUST_YEAR | INTEGER | 2 | — | — |

## SUMINV
**NOT USED**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMINV_DOL_ADJ | NUMERIC | 8 | 4 | — |
| 2 | SUMINV_DOL_FILL | NUMERIC | 8 | 4 | — |
| 3 | SUMINV_DOL_ISS | NUMERIC | 8 | 4 | — |
| 4 | SUMINV_DOL_RSTK | NUMERIC | 8 | 4 | — |
| 5 | SUMINV_DOL_RWIP | NUMERIC | 8 | 4 | — |
| 6 | SUMINV_DOL_SHPC | NUMERIC | 8 | 4 | — |
| 7 | SUMINV_DOL_SHPS | NUMERIC | 8 | 4 | — |
| 8 | SUMINV_DOL_WORC | NUMERIC | 8 | 4 | — |
| 9 | SUMINV_LOCATION | STRING | 10 | — | — |
| 10 | SUMINV_MONTH | INTEGER | 2 | — | — |
| 11 | SUMINV_PARTNO | STRING | 15 | — | — |
| 12 | SUMINV_UN_ADJ | NUMERIC | 8 | 2 | — |
| 13 | SUMINV_UN_FILL | NUMERIC | 8 | 2 | — |
| 14 | SUMINV_UN_ISS | NUMERIC | 8 | 2 | — |
| 15 | SUMINV_UN_RSTK | NUMERIC | 8 | 2 | — |
| 16 | SUMINV_UN_RWIP | NUMERIC | 8 | 2 | — |
| 17 | SUMINV_UN_SHPS | NUMERIC | 8 | 2 | — |
| 18 | SUMINV_UN_WORC | NUMERIC | 8 | 2 | — |
| 19 | SUMINV_YEAR | INTEGER | 2 | — | — |

## SUMWC
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMWC_LABOR | NUMERIC | 8 | 2 | — |
| 2 | SUMWC_MONTH | INTEGER | 2 | — | — |
| 3 | SUMWC_SCRAP | NUMERIC | 8 | 2 | — |
| 4 | SUMWC_SETUP | NUMERIC | 8 | 2 | — |
| 5 | SUMWC_UNITS | NUMERIC | 8 | 2 | — |
| 6 | SUMWC_WORKCTR | STRING | 12 | — | — |
| 7 | SUMWC_YEAR | INTEGER | 2 | — | — |

## TEMPOLD
**Used for**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTD_CODE | STRING | 10 | — | Contact Code |
| 2 | BKCM_ACTD_DATE | DATE | 4 | — | Date |
| 3 | BKCM_ACTD_DCODE | STRING | 2 | — | Date Code |
| 4 | BKCM_ACTD_EXTRA | STRING | 100 | — | — |

## TESTARRA
**NOT USED**

Fields: 101

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TARRAY_1 | STRING | 1 | — | — |
| 2 | TARRAY_10 | STRING | 1 | — | — |
| 3 | TARRAY_100 | STRING | 1 | — | — |
| 4 | TARRAY_11 | STRING | 1 | — | — |
| 5 | TARRAY_12 | STRING | 1 | — | — |
| 6 | TARRAY_13 | STRING | 1 | — | — |
| 7 | TARRAY_14 | STRING | 1 | — | — |
| 8 | TARRAY_15 | STRING | 1 | — | — |
| 9 | TARRAY_16 | STRING | 1 | — | — |
| 10 | TARRAY_17 | STRING | 1 | — | — |
| 11 | TARRAY_18 | STRING | 1 | — | — |
| 12 | TARRAY_19 | STRING | 1 | — | — |
| 13 | TARRAY_2 | STRING | 1 | — | — |
| 14 | TARRAY_20 | STRING | 1 | — | — |
| 15 | TARRAY_21 | STRING | 1 | — | — |
| 16 | TARRAY_22 | STRING | 1 | — | — |
| 17 | TARRAY_23 | STRING | 1 | — | — |
| 18 | TARRAY_24 | STRING | 1 | — | — |
| 19 | TARRAY_25 | STRING | 1 | — | — |
| 20 | TARRAY_26 | STRING | 1 | — | — |
| 21 | TARRAY_27 | STRING | 1 | — | — |
| 22 | TARRAY_28 | STRING | 1 | — | — |
| 23 | TARRAY_29 | STRING | 1 | — | — |
| 24 | TARRAY_3 | STRING | 1 | — | — |
| 25 | TARRAY_30 | STRING | 1 | — | — |
| 26 | TARRAY_31 | STRING | 1 | — | — |
| 27 | TARRAY_32 | STRING | 1 | — | — |
| 28 | TARRAY_33 | STRING | 1 | — | — |
| 29 | TARRAY_34 | STRING | 1 | — | — |
| 30 | TARRAY_35 | STRING | 1 | — | — |
| 31 | TARRAY_36 | STRING | 1 | — | — |
| 32 | TARRAY_37 | STRING | 1 | — | — |
| 33 | TARRAY_38 | STRING | 1 | — | — |
| 34 | TARRAY_39 | STRING | 1 | — | — |
| 35 | TARRAY_4 | STRING | 1 | — | — |
| 36 | TARRAY_40 | STRING | 1 | — | — |
| 37 | TARRAY_41 | STRING | 1 | — | — |
| 38 | TARRAY_42 | STRING | 1 | — | — |
| 39 | TARRAY_43 | STRING | 1 | — | — |
| 40 | TARRAY_44 | STRING | 1 | — | — |
| 41 | TARRAY_45 | STRING | 1 | — | — |
| 42 | TARRAY_46 | STRING | 1 | — | — |
| 43 | TARRAY_47 | STRING | 1 | — | — |
| 44 | TARRAY_48 | STRING | 1 | — | — |
| 45 | TARRAY_49 | STRING | 1 | — | — |
| 46 | TARRAY_5 | STRING | 1 | — | — |
| 47 | TARRAY_50 | STRING | 1 | — | — |
| 48 | TARRAY_51 | STRING | 1 | — | — |
| 49 | TARRAY_52 | STRING | 1 | — | — |
| 50 | TARRAY_53 | STRING | 1 | — | — |
| 51 | TARRAY_54 | STRING | 1 | — | — |
| 52 | TARRAY_55 | STRING | 1 | — | — |
| 53 | TARRAY_56 | STRING | 1 | — | — |
| 54 | TARRAY_57 | STRING | 1 | — | — |
| 55 | TARRAY_58 | STRING | 1 | — | — |
| 56 | TARRAY_59 | STRING | 1 | — | — |
| 57 | TARRAY_6 | STRING | 1 | — | — |
| 58 | TARRAY_60 | STRING | 1 | — | — |
| 59 | TARRAY_61 | STRING | 1 | — | — |
| 60 | TARRAY_62 | STRING | 1 | — | — |
| 61 | TARRAY_63 | STRING | 1 | — | — |
| 62 | TARRAY_64 | STRING | 1 | — | — |
| 63 | TARRAY_65 | STRING | 1 | — | — |
| 64 | TARRAY_66 | STRING | 1 | — | — |
| 65 | TARRAY_67 | STRING | 1 | — | — |
| 66 | TARRAY_68 | STRING | 1 | — | — |
| 67 | TARRAY_69 | STRING | 1 | — | — |
| 68 | TARRAY_7 | STRING | 1 | — | — |
| 69 | TARRAY_70 | STRING | 1 | — | — |
| 70 | TARRAY_71 | STRING | 1 | — | — |
| 71 | TARRAY_72 | STRING | 1 | — | — |
| 72 | TARRAY_73 | STRING | 1 | — | — |
| 73 | TARRAY_74 | STRING | 1 | — | — |
| 74 | TARRAY_75 | STRING | 1 | — | — |
| 75 | TARRAY_76 | STRING | 1 | — | — |
| 76 | TARRAY_77 | STRING | 1 | — | — |
| 77 | TARRAY_78 | STRING | 1 | — | — |
| 78 | TARRAY_79 | STRING | 1 | — | — |
| 79 | TARRAY_8 | STRING | 1 | — | — |
| 80 | TARRAY_80 | STRING | 1 | — | — |
| 81 | TARRAY_81 | STRING | 1 | — | — |
| 82 | TARRAY_82 | STRING | 1 | — | — |
| 83 | TARRAY_83 | STRING | 1 | — | — |
| 84 | TARRAY_84 | STRING | 1 | — | — |
| 85 | TARRAY_85 | STRING | 1 | — | — |
| 86 | TARRAY_86 | STRING | 1 | — | — |
| 87 | TARRAY_87 | STRING | 1 | — | — |
| 88 | TARRAY_88 | STRING | 1 | — | — |
| 89 | TARRAY_89 | STRING | 1 | — | — |
| 90 | TARRAY_9 | STRING | 1 | — | — |
| 91 | TARRAY_90 | STRING | 1 | — | — |
| 92 | TARRAY_91 | STRING | 1 | — | — |
| 93 | TARRAY_92 | STRING | 1 | — | — |
| 94 | TARRAY_93 | STRING | 1 | — | — |
| 95 | TARRAY_94 | STRING | 1 | — | — |
| 96 | TARRAY_95 | STRING | 1 | — | — |
| 97 | TARRAY_96 | STRING | 1 | — | — |
| 98 | TARRAY_97 | STRING | 1 | — | — |
| 99 | TARRAY_98 | STRING | 1 | — | — |
| 100 | TARRAY_99 | STRING | 1 | — | — |
| 101 | TEST | STRING | 10 | — | — |

## TESTFILE
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TESTFILE_1 | STRING | 10 | — | — |
| 2 | TESTFILE_10 | NUMERIC | 8 | 2 | — |
| 3 | TESTFILE_11 | STRING | 50 | — | — |
| 4 | TESTFILE_2 | STRING | 20 | — | — |
| 5 | TESTFILE_3 | NUMERIC | 8 | 2 | — |
| 6 | TESTFILE_4 | NUMERIC | 8 | 2 | — |
| 7 | TESTFILE_5 | STRING | 40 | — | — |
| 8 | TESTFILE_6 | NUMERIC | 8 | 4 | — |
| 9 | TESTFILE_7 | STRING | 40 | — | — |
| 10 | TESTFILE_8 | STRING | 30 | — | — |
| 11 | TESTFILE_9 | STRING | 25 | — | — |

## WBTRVMEMO
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BTRV_MEM_BUFF | STRING | 512 | — | — |
| 2 | BTRV_MEM_CNTR | INTEGER | 4 | — | — |
| 3 | BTRV_MEM_LINK | INTEGER | 4 | — | — |
| 4 | BTRV_MEM_SIZE | INTEGER | 4 | — | — |
| 5 | BTRV_MEM_SUBC | INTEGER | 4 | — | — |

## WOBOMCHG
**WOBOM CHANGES (NOT USED)**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WBOM_CHG_ACOMP | STRING | 1 | — | — |
| 2 | WBOM_CHG_AEXTRA | STRING | 100 | — | — |
| 3 | WBOM_CHG_AQTY | NUMERIC | 8 | 8 | — |
| 4 | WBOM_CHG_AREF | STRING | 20 | — | — |
| 5 | WBOM_CHG_ASCRAP | NUMERIC | 8 | 2 | — |
| 6 | WBOM_CHG_BEXTRA | STRING | 100 | — | — |
| 7 | WBOM_CHG_BQTY | NUMERIC | 8 | 8 | — |
| 8 | WBOM_CHG_BREF | STRING | 20 | — | — |
| 9 | WBOM_CHG_BSCRAP | NUMERIC | 8 | 2 | — |
| 10 | WBOM_CHG_CDATE | DATE | 4 | — | — |
| 11 | WBOM_CHG_COMP | STRING | 15 | — | — |
| 12 | WBOM_CHG_DCOMP | STRING | 1 | — | — |
| 13 | WBOM_CHG_PARENT | STRING | 15 | — | — |
| 14 | WBOM_CHG_UID | STRING | 20 | — | — |
| 15 | WBOM_CHG_USER | STRING | 15 | — | — |
| 16 | WBOM_CHG_WOPRE | NUMERIC | 8 | — | — |
| 17 | WBOM_CHG_WOSUF | INTEGER | 2 | — | — |

## XXICMSTR
**NOT USED**

Fields: 64

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |
