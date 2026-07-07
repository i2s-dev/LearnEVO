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
| 1 | AHSY_USER_ACCES_1 | STRING | 1 | — | User access flag for menu slot 1 (Y/N) |
| 2 | AHSY_USER_ACCES_10 | STRING | 1 | — | User access flag for menu slot 10 (Y/N) |
| 3 | AHSY_USER_ACCES_11 | STRING | 1 | — | User access flag for menu slot 11 (Y/N) |
| 4 | AHSY_USER_ACCES_12 | STRING | 1 | — | User access flag for menu slot 12 (Y/N) |
| 5 | AHSY_USER_ACCES_13 | STRING | 1 | — | User access flag for menu slot 13 (Y/N) |
| 6 | AHSY_USER_ACCES_14 | STRING | 1 | — | User access flag for menu slot 14 (Y/N) |
| 7 | AHSY_USER_ACCES_15 | STRING | 1 | — | User access flag for menu slot 15 (Y/N) |
| 8 | AHSY_USER_ACCES_16 | STRING | 1 | — | User access flag for menu slot 16 (Y/N) |
| 9 | AHSY_USER_ACCES_17 | STRING | 1 | — | User access flag for menu slot 17 (Y/N) |
| 10 | AHSY_USER_ACCES_18 | STRING | 1 | — | User access flag for menu slot 18 (Y/N) |
| 11 | AHSY_USER_ACCES_19 | STRING | 1 | — | User access flag for menu slot 19 (Y/N) |
| 12 | AHSY_USER_ACCES_2 | STRING | 1 | — | User access flag for menu slot 2 (Y/N) |
| 13 | AHSY_USER_ACCES_20 | STRING | 1 | — | User access flag for menu slot 20 (Y/N) |
| 14 | AHSY_USER_ACCES_3 | STRING | 1 | — | User access flag for menu slot 3 (Y/N) |
| 15 | AHSY_USER_ACCES_4 | STRING | 1 | — | User access flag for menu slot 4 (Y/N) |
| 16 | AHSY_USER_ACCES_5 | STRING | 1 | — | User access flag for menu slot 5 (Y/N) |
| 17 | AHSY_USER_ACCES_6 | STRING | 1 | — | User access flag for menu slot 6 (Y/N) |
| 18 | AHSY_USER_ACCES_7 | STRING | 1 | — | User access flag for menu slot 7 (Y/N) |
| 19 | AHSY_USER_ACCES_8 | STRING | 1 | — | User access flag for menu slot 8 (Y/N) |
| 20 | AHSY_USER_ACCES_9 | STRING | 1 | — | User access flag for menu slot 9 (Y/N) |
| 21 | AHSY_USER_CTRL | STRING | 1 | — | User control flag |
| 22 | AHSY_USER_LEVL | STRING | 2 | — | User security level code |
| 23 | AHSY_USER_MENU | STRING | 4 | — | User default menu code |

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
| 1 | BKAB_EXP | DATE | 4 | — | License/account expiration date |
| 2 | BKAB_PERIOD | INTEGER | 2 | — | Accounting period |
| 3 | BKAB_STAND_ALNE | STRING | 1 | — | Standalone flag (Y/N) |
| 4 | BKAB_START | DATE | 4 | — | Account start date |
| 5 | BKAB_WARNING | INTEGER | 2 | — | Warning days before expiration |

## BKABVEND
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAB_REG_NAME | STRING | 25 | — | Registered company name |
| 2 | BKAB_SERIAL | NUMERIC | 8 | — | Software serial number |

## BKAPNOTE
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_NOTE_DATE | DATE | 4 | — | Date |
| 2 | BKAP_NOTE_ENTBY | STRING | 10 | — | Enter By |
| 3 | BKAP_NOTE_NOTES_1 | STRING | 76 | — | AP vendor note line 1 |
| 4 | BKAP_NOTE_NOTES_2 | STRING | 76 | — | AP vendor note line 2 |
| 5 | BKAP_NOTE_NOTES_3 | STRING | 76 | — | AP vendor note line 3 |
| 6 | BKAP_NOTE_NOTES_4 | STRING | 76 | — | AP vendor note line 4 |
| 7 | BKAP_NOTE_NOTES_5 | STRING | 76 | — | AP vendor note line 5 |
| 8 | BKAP_NOTE_NOTES_6 | STRING | 76 | — | AP vendor note line 6 |
| 9 | BKAP_NOTE_NOTES_7 | STRING | 76 | — | AP vendor note line 7 |
| 10 | BKAP_NOTE_NOTES_8 | STRING | 76 | — | AP vendor note line 8 |
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
| 1 | BKAR_TXN_BIN | STRING | 15 | — | Bin location |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | Reserved extra field |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | Warehouse location |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | Ship receipt number |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | Stock item code |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | Temporary SO reference |

## BKBMCNFG
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_CNFG_AUTO | STRING | 1 | — | Auto-post flag (Y/N) |
| 2 | BKBM_CNFG_GLACT | STRING | 10 | — | Default GL account |
| 3 | BKBM_CNFG_GLDPT | STRING | 4 | — | Default GL department |
| 4 | BKBM_CNFG_LABOR | STRING | 1 | — | Include labor flag (Y/N) |
| 5 | BKBM_CNFG_NUM | NUMERIC | 8 | — | Configuration record number |
| 6 | BKBM_CNFG_POST | STRING | 1 | — | Post to GL flag (Y/N) |
| 7 | BKBM_CNFG_ROLL | STRING | 1 | — | Roll-up costs flag (Y/N) |

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
| 1 | BKCM_CTRL_USER | STRING | 10 | — | Controlling user code |

## BKCMCTL2
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | Controlling user code |

## BKCMCTL3
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | Controlling user code |

## BKCMCTL4
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | Controlling user code |

## BKCMCTRL
**NOT USED**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_CTRL_USER | STRING | 10 | — | Controlling user code |

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
| 19 | BKCM_ACCT_FONE_1 | STRING | 15 | — | Account phone 1 |
| 20 | BKCM_ACCT_FONE_2 | STRING | 15 | — | Account phone 2 |
| 21 | BKCM_ACCT_FONE_3 | STRING | 15 | — | Account phone 3 |
| 22 | BKCM_ACCT_FTHRE_1 | STRING | 25 | — | Account field three 1 |
| 23 | BKCM_ACCT_FTHRE_2 | STRING | 25 | — | Account field three 2 |
| 24 | BKCM_ACCT_FTIME | INTEGER | 2 | — | not used |
| 25 | BKCM_ACCT_FTWO_1 | STRING | 2 | — | Account field two 1 |
| 26 | BKCM_ACCT_FTWO_2 | STRING | 2 | — | Account field two 2 |
| 27 | BKCM_ACCT_FTWO_3 | STRING | 2 | — | Account field two 3 |
| 28 | BKCM_ACCT_LEAD | STRING | 5 | — | Lead Source |
| 29 | BKCM_ACCT_NAME | STRING | 30 | — | Name |
| 30 | BKCM_ACCT_OLDCD | STRING | 10 | — | Old Account Code |
| 31 | BKCM_ACCT_PHONE | STRING | 25 | — | Phone Number |
| 32 | BKCM_ACCT_PNAME | STRING | 25 | — | Prospect Name |
| 33 | BKCM_ACCT_REM_1 | STRING | 60 | — | Account remark line 1 |
| 34 | BKCM_ACCT_REM_2 | STRING | 60 | — | Account remark line 2 |
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
| 1 | BKCM_FTME_ATIME | INTEGER | 2 | — | Actual time (minutes) |
| 2 | BKCM_FTME_BALNC | NUMERIC | 8 | 2 | Balance amount |
| 3 | BKCM_FTME_CODE | STRING | 10 | — | Contact Code |
| 4 | BKCM_FTME_DESC | STRING | 25 | — | Description |
| 5 | BKCM_FTME_FTIME | INTEGER | 2 | — | Forecast time (minutes) |
| 6 | BKCM_FTME_LASTP | DATE | 4 | — | Last Payment |
| 7 | BKCM_FTME_NTIME | INTEGER | 2 | — | Next scheduled time (minutes) |

## BKCMPCFC
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_PCFC_DESC | STRING | 25 | — | Price/freight code description |
| 2 | BKCM_PCFC_FCODE | STRING | 3 | — | Freight code |
| 3 | BKCM_PCFC_REP | STRING | 5 | — | Rep/salesperson code |

## BKCMSBDF
**CM subdirectory/folder defaults** — used by T7MDEFNDC (menu defaults for DC terminals). Configures folder paths for DC programs.

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_SBDF_BINC | NUMERIC | 8 | 2 | Billing increment amount |
| 2 | BKCM_SBDF_DHOLD | STRING | 1 | — | Debit hold flag (Y/N) |
| 3 | BKCM_SBDF_ICONV | NUMERIC | 8 | 6 | Invoice conversion factor |
| 4 | BKCM_SBDF_MINC | INTEGER | 2 | — | Minimum billing increment |
| 5 | BKCM_SBDF_NCHG | INTEGER | 2 | — | Number of charge cycles |

## BKCMTEMP
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | CRM activity code |
| 2 | BKCMT_CODE | STRING | 10 | — | CRM template code |
| 3 | BKCMT_COMP | STRING | 2 | — | Company code |
| 4 | BKCMT_GROUP | STRING | 8 | — | Group code |
| 5 | BKCMT_KEYF | STRING | 20 | — | Key field value |
| 6 | BKCMT_TAG | STRING | 1 | — | Tag/flag (Y/N) |

## BKCMTMP1
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | CRM activity code |
| 2 | BKCMT_CODE | STRING | 10 | — | CRM template code |
| 3 | BKCMT_COMP | STRING | 2 | — | Company code |
| 4 | BKCMT_GROUP | STRING | 8 | — | Group code |
| 5 | BKCMT_KEYF | STRING | 20 | — | Key field value |
| 6 | BKCMT_TAG | STRING | 1 | — | Tag/flag (Y/N) |

## BKCMTMP2
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | CRM activity code |
| 2 | BKCMT_CODE | STRING | 10 | — | CRM template code |
| 3 | BKCMT_COMP | STRING | 2 | — | Company code |
| 4 | BKCMT_GROUP | STRING | 8 | — | Group code |
| 5 | BKCMT_KEYF | STRING | 20 | — | Key field value |
| 6 | BKCMT_TAG | STRING | 1 | — | Tag/flag (Y/N) |

## BKCMTMP3
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | CRM activity code |
| 2 | BKCMT_CODE | STRING | 10 | — | CRM template code |
| 3 | BKCMT_COMP | STRING | 2 | — | Company code |
| 4 | BKCMT_GROUP | STRING | 8 | — | Group code |
| 5 | BKCMT_KEYF | STRING | 20 | — | Key field value |
| 6 | BKCMT_TAG | STRING | 1 | — | Tag/flag (Y/N) |

## BKCMTMP4
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTIVITY | STRING | 5 | — | CRM activity code |
| 2 | BKCMT_CODE | STRING | 10 | — | CRM template code |
| 3 | BKCMT_COMP | STRING | 2 | — | Company code |
| 4 | BKCMT_GROUP | STRING | 8 | — | Group code |
| 5 | BKCMT_KEYF | STRING | 20 | — | Key field value |
| 6 | BKCMT_TAG | STRING | 1 | — | Tag/flag (Y/N) |

## BKDCCFG
**DC terminal/scanner configuration** — used by T7ADCA/T7AUTODCH/J7EIMDCRev. Stores per-terminal DC scanner settings.

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKDC_CFG_BANKP | NUMERIC | 8 | — | Bank primary account number |
| 2 | BKDC_CFG_BANKS | INTEGER | 2 | — | Bank secondary code |
| 3 | BKDC_CFG_EXPPTH | STRING | 60 | — | Export path for DC files |
| 4 | BKDC_CFG_IDLEP | NUMERIC | 8 | — | Idle polling period |
| 5 | BKDC_CFG_IDLES | INTEGER | 2 | — | Idle sleep seconds |
| 6 | BKDC_CFG_IMPPTH | STRING | 60 | — | Import path for DC files |
| 7 | BKDC_CFG_JOBTME | STRING | 60 | — | Job time configuration string |

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
| 12 | BKGL_TRN_PART | STRING | 15 | — | Item part number associated with entry |
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
| 3 | BKGL_CHK_CUST | STRING | 10 | — | Customer code |
| 4 | BKGL_CHK_DATE | DATE | 4 | — | Date |
| 5 | BKGL_CHK_DATER | DATE | 4 | — | Date record was reconciled |
| 6 | BKGL_CHK_EXTRA | STRING | 100 | — | Reserved extra field |
| 7 | BKGL_CHK_FLAG | STRING | 1 | — | Reconciled Y/N |
| 8 | BKGL_CHK_NAME | STRING | 25 | — | Pay to Name |
| 9 | BKGL_CHK_NUM | NUMERIC | 8 | — | Check Number |
| 10 | BKGL_CHK_TYPE | STRING | 1 | — | Type |
| 11 | BKGL_CHK_VEND | STRING | 10 | — | Vendor code |

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
| 12 | BKGL_TRN_PART | STRING | 15 | — | Item part number associated with entry |
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
| 12 | BKGL_TRN_PART | STRING | 15 | — | Item part number associated with entry |
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
| 4 | BKIC_ALTD_SPECS_1 | STRING | 30 | — | Alternate item specification line 1 |
| 5 | BKIC_ALTD_SPECS_10 | STRING | 30 | — | Alternate item specification line 10 |
| 6 | BKIC_ALTD_SPECS_11 | STRING | 30 | — | Alternate item specification line 11 |
| 7 | BKIC_ALTD_SPECS_12 | STRING | 30 | — | Alternate item specification line 12 |
| 8 | BKIC_ALTD_SPECS_2 | STRING | 30 | — | Alternate item specification line 2 |
| 9 | BKIC_ALTD_SPECS_3 | STRING | 30 | — | Alternate item specification line 3 |
| 10 | BKIC_ALTD_SPECS_4 | STRING | 30 | — | Alternate item specification line 4 |
| 11 | BKIC_ALTD_SPECS_5 | STRING | 30 | — | Alternate item specification line 5 |
| 12 | BKIC_ALTD_SPECS_6 | STRING | 30 | — | Alternate item specification line 6 |
| 13 | BKIC_ALTD_SPECS_7 | STRING | 30 | — | Alternate item specification line 7 |
| 14 | BKIC_ALTD_SPECS_8 | STRING | 30 | — | Alternate item specification line 8 |
| 15 | BKIC_ALTD_SPECS_9 | STRING | 30 | — | Alternate item specification line 9 |
| 16 | BKIC_ALTD_TYPE | STRING | 1 | — | Type |

## BKICALTP
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_ALTP_ACODE | STRING | 25 | — | Alternate product code |
| 2 | BKIC_ALTP_NOTES_1 | STRING | 30 | — | Alternate product note line 1 |
| 3 | BKIC_ALTP_NOTES_2 | STRING | 30 | — | Alternate product note line 2 |
| 4 | BKIC_ALTP_NOTES_3 | STRING | 30 | — | Alternate product note line 3 |
| 5 | BKIC_ALTP_PCODE | STRING | 15 | — | Primary product code |
| 6 | BKIC_ALTP_TYPE | STRING | 1 | — | Alternate type code |

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
| 6 | BKICDIM_COATING_1 | STRING | 20 | — | Coating specification 1 |
| 7 | BKICDIM_COATING_2 | STRING | 20 | — | Coating specification 2 |
| 8 | BKICDIM_COIL_1 | STRING | 10 | — | Coil specification 1 |
| 9 | BKICDIM_COIL_2 | STRING | 10 | — | Coil specification 2 |
| 10 | BKICDIM_COIL_3 | STRING | 10 | — | Coil specification 3 |
| 11 | BKICDIM_DENSITY | NUMERIC | 8 | 4 | Density |
| 12 | BKICDIM_EDGE_1 | STRING | 20 | — | Edge specification 1 |
| 13 | BKICDIM_EDGE_2 | STRING | 20 | — | Edge specification 2 |
| 14 | BKICDIM_ELONGAT | STRING | 15 | — | Elongation |
| 15 | BKICDIM_F_TOL_1 | NUMERIC | 8 | 4 | Flatness tolerance 1 |
| 16 | BKICDIM_F_TOL_2 | NUMERIC | 8 | 4 | Flatness tolerance 2 |
| 17 | BKICDIM_FINISH_1 | STRING | 20 | — | Surface finish 1 |
| 18 | BKICDIM_FINISH_2 | STRING | 20 | — | Surface finish 2 |
| 19 | BKICDIM_FIRST | NUMERIC | 8 | 4 | Length |
| 20 | BKICDIM_GENERIC | STRING | 15 | — | Generic Phantom Part |
| 21 | BKICDIM_HARDNES | STRING | 20 | — | Hardness |
| 22 | BKICDIM_NOTES_1 | STRING | 30 | — | Dimension note line 1 |
| 23 | BKICDIM_NOTES_10 | STRING | 30 | — | Dimension note line 10 |
| 24 | BKICDIM_NOTES_11 | STRING | 30 | — | Dimension note line 11 |
| 25 | BKICDIM_NOTES_12 | STRING | 30 | — | Dimension note line 12 |
| 26 | BKICDIM_NOTES_2 | STRING | 30 | — | Dimension note line 2 |
| 27 | BKICDIM_NOTES_3 | STRING | 30 | — | Dimension note line 3 |
| 28 | BKICDIM_NOTES_4 | STRING | 30 | — | Dimension note line 4 |
| 29 | BKICDIM_NOTES_5 | STRING | 30 | — | Dimension note line 5 |
| 30 | BKICDIM_NOTES_6 | STRING | 30 | — | Dimension note line 6 |
| 31 | BKICDIM_NOTES_7 | STRING | 30 | — | Dimension note line 7 |
| 32 | BKICDIM_NOTES_8 | STRING | 30 | — | Dimension note line 8 |
| 33 | BKICDIM_NOTES_9 | STRING | 30 | — | Dimension note line 9 |
| 34 | BKICDIM_PARENT | STRING | 15 | — | Parent Item |
| 35 | BKICDIM_PARTNO | STRING | 15 | — | Item Number |
| 36 | BKICDIM_S_TOL_1 | NUMERIC | 8 | 4 | Squareness tolerance 1 |
| 37 | BKICDIM_S_TOL_2 | NUMERIC | 8 | 4 | Squareness tolerance 2 |
| 38 | BKICDIM_SECOND | NUMERIC | 8 | 4 | Width |
| 39 | BKICDIM_SETUP | NUMERIC | 8 | 8 | Setup |
| 40 | BKICDIM_SHPCOND_1 | STRING | 20 | — | Shipping condition 1 |
| 41 | BKICDIM_SHPCOND_2 | STRING | 20 | — | Shipping condition 2 |
| 42 | BKICDIM_T_TOL_1 | NUMERIC | 8 | 4 | Thickness tolerance 1 |
| 43 | BKICDIM_T_TOL_2 | NUMERIC | 8 | 4 | Thickness tolerance 2 |
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
| 4 | BKIC_MFG_REMARK_1 | STRING | 30 | — | Manufacturing remark line 1 |
| 5 | BKIC_MFG_REMARK_2 | STRING | 30 | — | Manufacturing remark line 2 |
| 6 | BKIC_MFG_REMARK_3 | STRING | 30 | — | Manufacturing remark line 3 |

## BKICREQ
**NOT USED**

Fields: 46

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_REQ_AGENT | STRING | 25 | — | Requesting agent |
| 2 | BKIC_REQ_BATCH^ | NUMERIC | 8 | — | Batch number |
| 3 | BKIC_REQ_BY | INTEGER | 2 | — | Requested by employee number |
| 4 | BKIC_REQ_DDATE | DATE | 4 | — | Date due/needed |
| 5 | BKIC_REQ_DESC | STRING | 30 | — | Requisition description |
| 6 | BKIC_REQ_ERDATE | DATE | 4 | — | Expected receipt date |
| 7 | BKIC_REQ_FROM | STRING | 10 | — | From location/department |
| 8 | BKIC_REQ_IDATE | DATE | 4 | — | Issue date |
| 9 | BKIC_REQ_ITM_NO | STRING | 9 | — | Item number |
| 10 | BKIC_REQ_MATDIM | STRING | 1 | — | Material dimension flag |
| 11 | BKIC_REQ_MFG | STRING | 25 | — | Manufacturer name |
| 12 | BKIC_REQ_MPART^ | STRING | 25 | — | Manufacturer part number |
| 13 | BKIC_REQ_NOTES_1 | STRING | 30 | — | Requisition note line 1 |
| 14 | BKIC_REQ_NOTES_10 | STRING | 30 | — | Requisition note line 10 |
| 15 | BKIC_REQ_NOTES_2 | STRING | 30 | — | Requisition note line 2 |
| 16 | BKIC_REQ_NOTES_3 | STRING | 30 | — | Requisition note line 3 |
| 17 | BKIC_REQ_NOTES_4 | STRING | 30 | — | Requisition note line 4 |
| 18 | BKIC_REQ_NOTES_5 | STRING | 30 | — | Requisition note line 5 |
| 19 | BKIC_REQ_NOTES_6 | STRING | 30 | — | Requisition note line 6 |
| 20 | BKIC_REQ_NOTES_7 | STRING | 30 | — | Requisition note line 7 |
| 21 | BKIC_REQ_NOTES_8 | STRING | 30 | — | Requisition note line 8 |
| 22 | BKIC_REQ_NOTES_9 | STRING | 30 | — | Requisition note line 9 |
| 23 | BKIC_REQ_NUM | NUMERIC | 8 | — | Requisition number |
| 24 | BKIC_REQ_OPER | INTEGER | 2 | — | Routing operation |
| 25 | BKIC_REQ_ORDNUM | NUMERIC | 8 | — | Work/purchase order number |
| 26 | BKIC_REQ_ORDQTY | NUMERIC | 8 | 2 | Ordered quantity |
| 27 | BKIC_REQ_PARENT | STRING | 15 | — | Parent item code |
| 28 | BKIC_REQ_PART^ | STRING | 15 | — | Part/item code |
| 29 | BKIC_REQ_PART^2 | STRING | 15 | — | Part code (alternate key) |
| 30 | BKIC_REQ_PROJ | STRING | 15 | — | Project code |
| 31 | BKIC_REQ_RQTY | NUMERIC | 8 | 2 | Requested quantity |
| 32 | BKIC_REQ_STATUS | STRING | 1 | — | Requisition status code |
| 33 | BKIC_REQ_TOADDR_1 | STRING | 30 | — | Ship-to address line 1 |
| 34 | BKIC_REQ_TOADDR_2 | STRING | 30 | — | Ship-to address line 2 |
| 35 | BKIC_REQ_TOADDR_3 | STRING | 30 | — | Ship-to address line 3 |
| 36 | BKIC_REQ_TOCITY | STRING | 20 | — | Ship-to city |
| 37 | BKIC_REQ_TOCONT | STRING | 25 | — | Ship-to contact |
| 38 | BKIC_REQ_TOFAX | STRING | 25 | — | Ship-to fax |
| 39 | BKIC_REQ_TOLOCN | STRING | 10 | — | Ship-to location code |
| 40 | BKIC_REQ_TONAME | STRING | 30 | — | Ship-to name |
| 41 | BKIC_REQ_TOPH^ | STRING | 25 | — | Ship-to phone |
| 42 | BKIC_REQ_TOST | STRING | 2 | — | Ship-to state |
| 43 | BKIC_REQ_TOZIP | STRING | 10 | — | Ship-to ZIP code |
| 44 | BKIC_REQ_TYPE | STRING | 1 | — | Requisition type code |
| 45 | BKIC_REQ_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 46 | BKIC_REQ_WOSUF | INTEGER | 2 | — | Work order suffix |

## BKICTAX
**Item tax codes** — used by T7ESE/J7DCSSOE/J7HHRTSSOE. Per-item sales tax classification codes.

Fields: 46

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_TAX_COLECT_1 | NUMERIC | 8 | 2 | Tax collected for period 1 |
| 2 | BKIC_TAX_COLECT_10 | NUMERIC | 8 | 2 | Tax collected for period 10 |
| 3 | BKIC_TAX_COLECT_11 | NUMERIC | 8 | 2 | Tax collected for period 11 |
| 4 | BKIC_TAX_COLECT_12 | NUMERIC | 8 | 2 | Tax collected for period 12 |
| 5 | BKIC_TAX_COLECT_2 | NUMERIC | 8 | 2 | Tax collected for period 2 |
| 6 | BKIC_TAX_COLECT_3 | NUMERIC | 8 | 2 | Tax collected for period 3 |
| 7 | BKIC_TAX_COLECT_4 | NUMERIC | 8 | 2 | Tax collected for period 4 |
| 8 | BKIC_TAX_COLECT_5 | NUMERIC | 8 | 2 | Tax collected for period 5 |
| 9 | BKIC_TAX_COLECT_6 | NUMERIC | 8 | 2 | Tax collected for period 6 |
| 10 | BKIC_TAX_COLECT_7 | NUMERIC | 8 | 2 | Tax collected for period 7 |
| 11 | BKIC_TAX_COLECT_8 | NUMERIC | 8 | 2 | Tax collected for period 8 |
| 12 | BKIC_TAX_COLECT_9 | NUMERIC | 8 | 2 | Tax collected for period 9 |
| 13 | BKIC_TAX_FRGHT | STRING | 1 | — | Freight |
| 14 | BKIC_TAX_GLACT | STRING | 10 | — | GL Account |
| 15 | BKIC_TAX_GLDPT | STRING | 4 | — | GL Department |
| 16 | BKIC_TAX_LOCAL | STRING | 2 | — | Local (County/City) |
| 17 | BKIC_TAX_NAME | STRING | 25 | — | Local Name |
| 18 | BKIC_TAX_NONTAX_1 | NUMERIC | 8 | 2 | Non-taxable sales for period 1 |
| 19 | BKIC_TAX_NONTAX_10 | NUMERIC | 8 | 2 | Non-taxable sales for period 10 |
| 20 | BKIC_TAX_NONTAX_11 | NUMERIC | 8 | 2 | Non-taxable sales for period 11 |
| 21 | BKIC_TAX_NONTAX_12 | NUMERIC | 8 | 2 | Non-taxable sales for period 12 |
| 22 | BKIC_TAX_NONTAX_2 | NUMERIC | 8 | 2 | Non-taxable sales for period 2 |
| 23 | BKIC_TAX_NONTAX_3 | NUMERIC | 8 | 2 | Non-taxable sales for period 3 |
| 24 | BKIC_TAX_NONTAX_4 | NUMERIC | 8 | 2 | Non-taxable sales for period 4 |
| 25 | BKIC_TAX_NONTAX_5 | NUMERIC | 8 | 2 | Non-taxable sales for period 5 |
| 26 | BKIC_TAX_NONTAX_6 | NUMERIC | 8 | 2 | Non-taxable sales for period 6 |
| 27 | BKIC_TAX_NONTAX_7 | NUMERIC | 8 | 2 | Non-taxable sales for period 7 |
| 28 | BKIC_TAX_NONTAX_8 | NUMERIC | 8 | 2 | Non-taxable sales for period 8 |
| 29 | BKIC_TAX_NONTAX_9 | NUMERIC | 8 | 2 | Non-taxable sales for period 9 |
| 30 | BKIC_TAX_NUMBER | STRING | 15 | — | Tax authority code/number |
| 31 | BKIC_TAX_OUTSTD | NUMERIC | 8 | 2 | Outstanding |
| 32 | BKIC_TAX_RATE | NUMERIC | 8 | 4 | Tax Rate |
| 33 | BKIC_TAX_STATE | STRING | 2 | — | State |
| 34 | BKIC_TAX_TAXBLE_1 | NUMERIC | 8 | 2 | Taxable sales for period 1 |
| 35 | BKIC_TAX_TAXBLE_10 | NUMERIC | 8 | 2 | Taxable sales for period 10 |
| 36 | BKIC_TAX_TAXBLE_11 | NUMERIC | 8 | 2 | Taxable sales for period 11 |
| 37 | BKIC_TAX_TAXBLE_12 | NUMERIC | 8 | 2 | Taxable sales for period 12 |
| 38 | BKIC_TAX_TAXBLE_2 | NUMERIC | 8 | 2 | Taxable sales for period 2 |
| 39 | BKIC_TAX_TAXBLE_3 | NUMERIC | 8 | 2 | Taxable sales for period 3 |
| 40 | BKIC_TAX_TAXBLE_4 | NUMERIC | 8 | 2 | Taxable sales for period 4 |
| 41 | BKIC_TAX_TAXBLE_5 | NUMERIC | 8 | 2 | Taxable sales for period 5 |
| 42 | BKIC_TAX_TAXBLE_6 | NUMERIC | 8 | 2 | Taxable sales for period 6 |
| 43 | BKIC_TAX_TAXBLE_7 | NUMERIC | 8 | 2 | Taxable sales for period 7 |
| 44 | BKIC_TAX_TAXBLE_8 | NUMERIC | 8 | 2 | Taxable sales for period 8 |
| 45 | BKIC_TAX_TAXBLE_9 | NUMERIC | 8 | 2 | Taxable sales for period 9 |
| 46 | BKIC_TAX_VENDOR | STRING | 10 | — | Vendor Code for Tax Authority |

## BKICVAL
**Item valuation overrides** — used by T7SMJL (job cost). Stores valuation adjustment records per item.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_VAL_CODE | STRING | 15 | — | Item code |
| 2 | BKIC_VAL_DATE | DATE | 4 | — | Valuation date |
| 3 | BKIC_VAL_TOTVL | NUMERIC | 8 | 2 | Total valuation amount |
| 4 | BKIC_VAL_UOH | NUMERIC | 8 | 2 | Units on hand at valuation |

## BKLOGON
**NOT USED**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKLOGON_CMPY | STRING | 2 | — | Company code |
| 2 | BKLOGON_CODE | STRING | 15 | — | User login code |
| 3 | BKLOGON_CURPRT | INTEGER | 2 | — | Current printer selection |
| 4 | BKLOGON_INUSE | STRING | 1 | — | Currently logged in flag (Y/N) |
| 5 | BKLOGON_MENU | INTEGER | 2 | — | Current menu position |
| 6 | BKLOGON_PRINTER | INTEGER | 2 | — | Default printer number |
| 7 | BKLOGON_PROG | STRING | 8 | — | Currently running program |
| 8 | BKLOGON_PSWD | STRING | 10 | — | Login password |
| 9 | BKLOGON_SCRTY | STRING | 2 | — | Security level code |
| 10 | BKLOGON_SUBMENU | INTEGER | 2 | — | Current sub-menu position |

## BKMATRIM
**Material trim specifications** — used by T7ROD (RO-D routing). Stores outside-process material trim dimensions per routing.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMA_TRIM_FIRST | NUMERIC | 8 | 2 | First trim amount |
| 2 | BKMA_TRIM_MACH | STRING | 4 | — | Machine code |
| 3 | BKMA_TRIM_SECND | NUMERIC | 8 | 2 | Second trim amount |

## BKPCKIT
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPC_KIT_COMP | STRING | 15 | — | Kit component item code |
| 2 | BKPC_KIT_DATELM | DATE | 4 | — | Eliminate/expire date |
| 3 | BKPC_KIT_LOC | STRING | 10 | — | Warehouse location |
| 4 | BKPC_KIT_LOT_^ | STRING | 15 | — | Lot number |
| 5 | BKPC_KIT_QTY_A | NUMERIC | 8 | 2 | Available quantity |
| 6 | BKPC_KIT_QTY_R | NUMERIC | 8 | 2 | Required quantity |
| 7 | BKPC_KIT_QTY_S | NUMERIC | 8 | 2 | Shipped quantity |

## BKPCPLOT
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPC_PLOT_COMPD | DATE | 4 | — | Completed date |
| 2 | BKPC_PLOT_CUST | STRING | 10 | — | Customer code |
| 3 | BKPC_PLOT_INKO | NUMERIC | 8 | 2 | Ink/overlay quantity |
| 4 | BKPC_PLOT_ISDTE | DATE | 4 | — | Issue date |
| 5 | BKPC_PLOT_LOC | STRING | 10 | — | Warehouse location |
| 6 | BKPC_PLOT_LOT_^ | STRING | 15 | — | Lot number |
| 7 | BKPC_PLOT_PLOT^ | STRING | 15 | — | Plot item code |
| 8 | BKPC_PLOT_PROD | STRING | 15 | — | Product item code |
| 9 | BKPC_PLOT_QTY | NUMERIC | 8 | 2 | Quantity required |
| 10 | BKPC_PLOT_SPDTE | DATE | 4 | — | Ship-promised date |
| 11 | BKPC_PLOT_STAT | STRING | 1 | — | Status flag |
| 12 | BKPC_PLOT_STRTD | DATE | 4 | — | Start date |

## BKPRBOOK
**NOT USED**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_SLS_CLASS_1 | STRING | 2 | — | Salesperson commission class 1 |
| 2 | BKPR_SLS_CLASS_2 | STRING | 2 | — | Salesperson commission class 2 |
| 3 | BKPR_SLS_COGS_1 | NUMERIC | 8 | 2 | COGS for period 1 |
| 4 | BKPR_SLS_COGS_10 | NUMERIC | 8 | 2 | COGS for period 10 |
| 5 | BKPR_SLS_COGS_11 | NUMERIC | 8 | 2 | COGS for period 11 |
| 6 | BKPR_SLS_COGS_12 | NUMERIC | 8 | 2 | COGS for period 12 |
| 7 | BKPR_SLS_COGS_2 | NUMERIC | 8 | 2 | COGS for period 2 |
| 8 | BKPR_SLS_COGS_3 | NUMERIC | 8 | 2 | COGS for period 3 |
| 9 | BKPR_SLS_COGS_4 | NUMERIC | 8 | 2 | COGS for period 4 |
| 10 | BKPR_SLS_COGS_5 | NUMERIC | 8 | 2 | COGS for period 5 |
| 11 | BKPR_SLS_COGS_6 | NUMERIC | 8 | 2 | COGS for period 6 |
| 12 | BKPR_SLS_COGS_7 | NUMERIC | 8 | 2 | COGS for period 7 |
| 13 | BKPR_SLS_COGS_8 | NUMERIC | 8 | 2 | COGS for period 8 |
| 14 | BKPR_SLS_COGS_9 | NUMERIC | 8 | 2 | COGS for period 9 |
| 15 | BKPR_SLS_COMM_1 | NUMERIC | 8 | 2 | Commission earned in period 1 |
| 16 | BKPR_SLS_COMM_10 | NUMERIC | 8 | 2 | Commission earned in period 10 |
| 17 | BKPR_SLS_COMM_11 | NUMERIC | 8 | 2 | Commission earned in period 11 |
| 18 | BKPR_SLS_COMM_12 | NUMERIC | 8 | 2 | Commission earned in period 12 |
| 19 | BKPR_SLS_COMM_2 | NUMERIC | 8 | 2 | Commission earned in period 2 |
| 20 | BKPR_SLS_COMM_3 | NUMERIC | 8 | 2 | Commission earned in period 3 |
| 21 | BKPR_SLS_COMM_4 | NUMERIC | 8 | 2 | Commission earned in period 4 |
| 22 | BKPR_SLS_COMM_5 | NUMERIC | 8 | 2 | Commission earned in period 5 |
| 23 | BKPR_SLS_COMM_6 | NUMERIC | 8 | 2 | Commission earned in period 6 |
| 24 | BKPR_SLS_COMM_7 | NUMERIC | 8 | 2 | Commission earned in period 7 |
| 25 | BKPR_SLS_COMM_8 | NUMERIC | 8 | 2 | Commission earned in period 8 |
| 26 | BKPR_SLS_COMM_9 | NUMERIC | 8 | 2 | Commission earned in period 9 |
| 27 | BKPR_SLS_EMPNUM | INTEGER | 2 | — | Salesperson employee number |
| 28 | BKPR_SLS_EXPACT | STRING | 10 | — | Commission expense GL account |
| 29 | BKPR_SLS_EXPDPT | STRING | 4 | — | Commission expense GL department |
| 30 | BKPR_SLS_EXTRA | STRING | 100 | — | Reserved extra field |
| 31 | BKPR_SLS_FNMI | STRING | 25 | — | First name / middle initial |
| 32 | BKPR_SLS_GROSS_1 | NUMERIC | 8 | 2 | Gross sales for period 1 |
| 33 | BKPR_SLS_GROSS_10 | NUMERIC | 8 | 2 | Gross sales for period 10 |
| 34 | BKPR_SLS_GROSS_11 | NUMERIC | 8 | 2 | Gross sales for period 11 |
| 35 | BKPR_SLS_GROSS_12 | NUMERIC | 8 | 2 | Gross sales for period 12 |
| 36 | BKPR_SLS_GROSS_2 | NUMERIC | 8 | 2 | Gross sales for period 2 |
| 37 | BKPR_SLS_GROSS_3 | NUMERIC | 8 | 2 | Gross sales for period 3 |
| 38 | BKPR_SLS_GROSS_4 | NUMERIC | 8 | 2 | Gross sales for period 4 |
| 39 | BKPR_SLS_GROSS_5 | NUMERIC | 8 | 2 | Gross sales for period 5 |
| 40 | BKPR_SLS_GROSS_6 | NUMERIC | 8 | 2 | Gross sales for period 6 |
| 41 | BKPR_SLS_GROSS_7 | NUMERIC | 8 | 2 | Gross sales for period 7 |
| 42 | BKPR_SLS_GROSS_8 | NUMERIC | 8 | 2 | Gross sales for period 8 |
| 43 | BKPR_SLS_GROSS_9 | NUMERIC | 8 | 2 | Gross sales for period 9 |
| 44 | BKPR_SLS_HOW_1 | STRING | 1 | — | Commission calculation method flag 1 |
| 45 | BKPR_SLS_HOW_2 | STRING | 1 | — | Commission calculation method flag 2 |
| 46 | BKPR_SLS_LNME | STRING | 25 | — | Last name |
| 47 | BKPR_SLS_PAID_1 | NUMERIC | 8 | 2 | Commission paid in period 1 |
| 48 | BKPR_SLS_PAID_10 | NUMERIC | 8 | 2 | Commission paid in period 10 |
| 49 | BKPR_SLS_PAID_11 | NUMERIC | 8 | 2 | Commission paid in period 11 |
| 50 | BKPR_SLS_PAID_12 | NUMERIC | 8 | 2 | Commission paid in period 12 |
| 51 | BKPR_SLS_PAID_2 | NUMERIC | 8 | 2 | Commission paid in period 2 |
| 52 | BKPR_SLS_PAID_3 | NUMERIC | 8 | 2 | Commission paid in period 3 |
| 53 | BKPR_SLS_PAID_4 | NUMERIC | 8 | 2 | Commission paid in period 4 |
| 54 | BKPR_SLS_PAID_5 | NUMERIC | 8 | 2 | Commission paid in period 5 |
| 55 | BKPR_SLS_PAID_6 | NUMERIC | 8 | 2 | Commission paid in period 6 |
| 56 | BKPR_SLS_PAID_7 | NUMERIC | 8 | 2 | Commission paid in period 7 |
| 57 | BKPR_SLS_PAID_8 | NUMERIC | 8 | 2 | Commission paid in period 8 |
| 58 | BKPR_SLS_PAID_9 | NUMERIC | 8 | 2 | Commission paid in period 9 |
| 59 | BKPR_SLS_QUOTA_1 | NUMERIC | 8 | 2 | Sales quota for period 1 |
| 60 | BKPR_SLS_QUOTA_10 | NUMERIC | 8 | 2 | Sales quota for period 10 |
| 61 | BKPR_SLS_QUOTA_11 | NUMERIC | 8 | 2 | Sales quota for period 11 |
| 62 | BKPR_SLS_QUOTA_12 | NUMERIC | 8 | 2 | Sales quota for period 12 |
| 63 | BKPR_SLS_QUOTA_2 | NUMERIC | 8 | 2 | Sales quota for period 2 |
| 64 | BKPR_SLS_QUOTA_3 | NUMERIC | 8 | 2 | Sales quota for period 3 |
| 65 | BKPR_SLS_QUOTA_4 | NUMERIC | 8 | 2 | Sales quota for period 4 |
| 66 | BKPR_SLS_QUOTA_5 | NUMERIC | 8 | 2 | Sales quota for period 5 |
| 67 | BKPR_SLS_QUOTA_6 | NUMERIC | 8 | 2 | Sales quota for period 6 |
| 68 | BKPR_SLS_QUOTA_7 | NUMERIC | 8 | 2 | Sales quota for period 7 |
| 69 | BKPR_SLS_QUOTA_8 | NUMERIC | 8 | 2 | Sales quota for period 8 |
| 70 | BKPR_SLS_QUOTA_9 | NUMERIC | 8 | 2 | Sales quota for period 9 |
| 71 | BKPR_SLS_RATE_1 | NUMERIC | 8 | 4 | Commission rate 1 |
| 72 | BKPR_SLS_RATE_2 | NUMERIC | 8 | 4 | Commission rate 2 |
| 73 | BKPR_SLS_RCPTS_1 | NUMERIC | 8 | 2 | Cash receipts for period 1 |
| 74 | BKPR_SLS_RCPTS_10 | NUMERIC | 8 | 2 | Cash receipts for period 10 |
| 75 | BKPR_SLS_RCPTS_11 | NUMERIC | 8 | 2 | Cash receipts for period 11 |
| 76 | BKPR_SLS_RCPTS_12 | NUMERIC | 8 | 2 | Cash receipts for period 12 |
| 77 | BKPR_SLS_RCPTS_2 | NUMERIC | 8 | 2 | Cash receipts for period 2 |
| 78 | BKPR_SLS_RCPTS_3 | NUMERIC | 8 | 2 | Cash receipts for period 3 |
| 79 | BKPR_SLS_RCPTS_4 | NUMERIC | 8 | 2 | Cash receipts for period 4 |
| 80 | BKPR_SLS_RCPTS_5 | NUMERIC | 8 | 2 | Cash receipts for period 5 |
| 81 | BKPR_SLS_RCPTS_6 | NUMERIC | 8 | 2 | Cash receipts for period 6 |
| 82 | BKPR_SLS_RCPTS_7 | NUMERIC | 8 | 2 | Cash receipts for period 7 |
| 83 | BKPR_SLS_RCPTS_8 | NUMERIC | 8 | 2 | Cash receipts for period 8 |
| 84 | BKPR_SLS_RCPTS_9 | NUMERIC | 8 | 2 | Cash receipts for period 9 |
| 85 | BKPR_SLS_WHEN_1 | STRING | 1 | — | When commission is paid flag 1 |
| 86 | BKPR_SLS_WHEN_2 | STRING | 1 | — | When commission is paid flag 2 |

## BKPRSTFL
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_ST_STCODE | STRING | 2 | — | State code |
| 2 | BKPR_ST_TAXNUM | STRING | 10 | — | State tax ID number |

## BKPRTCFG
**NOT USED**

Fields: 205

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPRT_CFG_CMD_1 | STRING | 70 | — | Printer init/reset command string for printer 1 |
| 2 | BKPRT_CFG_CMD_10 | STRING | 70 | — | Printer init/reset command string for printer 10 |
| 3 | BKPRT_CFG_CMD_11 | STRING | 70 | — | Printer init/reset command string for printer 11 |
| 4 | BKPRT_CFG_CMD_12 | STRING | 70 | — | Printer init/reset command string for printer 12 |
| 5 | BKPRT_CFG_CMD_13 | STRING | 70 | — | Printer init/reset command string for printer 13 |
| 6 | BKPRT_CFG_CMD_14 | STRING | 70 | — | Printer init/reset command string for printer 14 |
| 7 | BKPRT_CFG_CMD_15 | STRING | 70 | — | Printer init/reset command string for printer 15 |
| 8 | BKPRT_CFG_CMD_16 | STRING | 70 | — | Printer init/reset command string for printer 16 |
| 9 | BKPRT_CFG_CMD_17 | STRING | 70 | — | Printer init/reset command string for printer 17 |
| 10 | BKPRT_CFG_CMD_18 | STRING | 70 | — | Printer init/reset command string for printer 18 |
| 11 | BKPRT_CFG_CMD_19 | STRING | 70 | — | Printer init/reset command string for printer 19 |
| 12 | BKPRT_CFG_CMD_2 | STRING | 70 | — | Printer init/reset command string for printer 2 |
| 13 | BKPRT_CFG_CMD_20 | STRING | 70 | — | Printer init/reset command string for printer 20 |
| 14 | BKPRT_CFG_CMD_3 | STRING | 70 | — | Printer init/reset command string for printer 3 |
| 15 | BKPRT_CFG_CMD_4 | STRING | 70 | — | Printer init/reset command string for printer 4 |
| 16 | BKPRT_CFG_CMD_5 | STRING | 70 | — | Printer init/reset command string for printer 5 |
| 17 | BKPRT_CFG_CMD_6 | STRING | 70 | — | Printer init/reset command string for printer 6 |
| 18 | BKPRT_CFG_CMD_7 | STRING | 70 | — | Printer init/reset command string for printer 7 |
| 19 | BKPRT_CFG_CMD_8 | STRING | 70 | — | Printer init/reset command string for printer 8 |
| 20 | BKPRT_CFG_CMD_9 | STRING | 70 | — | Printer init/reset command string for printer 9 |
| 21 | BKPRT_CFG_COND_1 | STRING | 1 | — | Conditional flag for printer 1 |
| 22 | BKPRT_CFG_COND_10 | STRING | 1 | — | Conditional flag for printer 10 |
| 23 | BKPRT_CFG_COND_2 | STRING | 1 | — | Conditional flag for printer 2 |
| 24 | BKPRT_CFG_COND_3 | STRING | 1 | — | Conditional flag for printer 3 |
| 25 | BKPRT_CFG_COND_4 | STRING | 1 | — | Conditional flag for printer 4 |
| 26 | BKPRT_CFG_COND_5 | STRING | 1 | — | Conditional flag for printer 5 |
| 27 | BKPRT_CFG_COND_6 | STRING | 1 | — | Conditional flag for printer 6 |
| 28 | BKPRT_CFG_COND_7 | STRING | 1 | — | Conditional flag for printer 7 |
| 29 | BKPRT_CFG_COND_8 | STRING | 1 | — | Conditional flag for printer 8 |
| 30 | BKPRT_CFG_COND_9 | STRING | 1 | — | Conditional flag for printer 9 |
| 31 | BKPRT_CFG_COPY_1 | INTEGER | 2 | — | Default copy count for print job 1 |
| 32 | BKPRT_CFG_COPY_10 | INTEGER | 2 | — | Default copy count for print job 10 |
| 33 | BKPRT_CFG_COPY_11 | INTEGER | 2 | — | Default copy count for print job 11 |
| 34 | BKPRT_CFG_COPY_12 | INTEGER | 2 | — | Default copy count for print job 12 |
| 35 | BKPRT_CFG_COPY_13 | INTEGER | 2 | — | Default copy count for print job 13 |
| 36 | BKPRT_CFG_COPY_14 | INTEGER | 2 | — | Default copy count for print job 14 |
| 37 | BKPRT_CFG_COPY_15 | INTEGER | 2 | — | Default copy count for print job 15 |
| 38 | BKPRT_CFG_COPY_16 | INTEGER | 2 | — | Default copy count for print job 16 |
| 39 | BKPRT_CFG_COPY_17 | INTEGER | 2 | — | Default copy count for print job 17 |
| 40 | BKPRT_CFG_COPY_18 | INTEGER | 2 | — | Default copy count for print job 18 |
| 41 | BKPRT_CFG_COPY_19 | INTEGER | 2 | — | Default copy count for print job 19 |
| 42 | BKPRT_CFG_COPY_2 | INTEGER | 2 | — | Default copy count for print job 2 |
| 43 | BKPRT_CFG_COPY_20 | INTEGER | 2 | — | Default copy count for print job 20 |
| 44 | BKPRT_CFG_COPY_21 | INTEGER | 2 | — | Default copy count for print job 21 |
| 45 | BKPRT_CFG_COPY_22 | INTEGER | 2 | — | Default copy count for print job 22 |
| 46 | BKPRT_CFG_COPY_23 | INTEGER | 2 | — | Default copy count for print job 23 |
| 47 | BKPRT_CFG_COPY_24 | INTEGER | 2 | — | Default copy count for print job 24 |
| 48 | BKPRT_CFG_COPY_25 | INTEGER | 2 | — | Default copy count for print job 25 |
| 49 | BKPRT_CFG_COPY_26 | INTEGER | 2 | — | Default copy count for print job 26 |
| 50 | BKPRT_CFG_COPY_27 | INTEGER | 2 | — | Default copy count for print job 27 |
| 51 | BKPRT_CFG_COPY_28 | INTEGER | 2 | — | Default copy count for print job 28 |
| 52 | BKPRT_CFG_COPY_29 | INTEGER | 2 | — | Default copy count for print job 29 |
| 53 | BKPRT_CFG_COPY_3 | INTEGER | 2 | — | Default copy count for print job 3 |
| 54 | BKPRT_CFG_COPY_30 | INTEGER | 2 | — | Default copy count for print job 30 |
| 55 | BKPRT_CFG_COPY_31 | INTEGER | 2 | — | Default copy count for print job 31 |
| 56 | BKPRT_CFG_COPY_32 | INTEGER | 2 | — | Default copy count for print job 32 |
| 57 | BKPRT_CFG_COPY_33 | INTEGER | 2 | — | Default copy count for print job 33 |
| 58 | BKPRT_CFG_COPY_34 | INTEGER | 2 | — | Default copy count for print job 34 |
| 59 | BKPRT_CFG_COPY_35 | INTEGER | 2 | — | Default copy count for print job 35 |
| 60 | BKPRT_CFG_COPY_36 | INTEGER | 2 | — | Default copy count for print job 36 |
| 61 | BKPRT_CFG_COPY_37 | INTEGER | 2 | — | Default copy count for print job 37 |
| 62 | BKPRT_CFG_COPY_38 | INTEGER | 2 | — | Default copy count for print job 38 |
| 63 | BKPRT_CFG_COPY_39 | INTEGER | 2 | — | Default copy count for print job 39 |
| 64 | BKPRT_CFG_COPY_4 | INTEGER | 2 | — | Default copy count for print job 4 |
| 65 | BKPRT_CFG_COPY_40 | INTEGER | 2 | — | Default copy count for print job 40 |
| 66 | BKPRT_CFG_COPY_41 | INTEGER | 2 | — | Default copy count for print job 41 |
| 67 | BKPRT_CFG_COPY_42 | INTEGER | 2 | — | Default copy count for print job 42 |
| 68 | BKPRT_CFG_COPY_43 | INTEGER | 2 | — | Default copy count for print job 43 |
| 69 | BKPRT_CFG_COPY_44 | INTEGER | 2 | — | Default copy count for print job 44 |
| 70 | BKPRT_CFG_COPY_45 | INTEGER | 2 | — | Default copy count for print job 45 |
| 71 | BKPRT_CFG_COPY_46 | INTEGER | 2 | — | Default copy count for print job 46 |
| 72 | BKPRT_CFG_COPY_47 | INTEGER | 2 | — | Default copy count for print job 47 |
| 73 | BKPRT_CFG_COPY_48 | INTEGER | 2 | — | Default copy count for print job 48 |
| 74 | BKPRT_CFG_COPY_49 | INTEGER | 2 | — | Default copy count for print job 49 |
| 75 | BKPRT_CFG_COPY_5 | INTEGER | 2 | — | Default copy count for print job 5 |
| 76 | BKPRT_CFG_COPY_50 | INTEGER | 2 | — | Default copy count for print job 50 |
| 77 | BKPRT_CFG_COPY_6 | INTEGER | 2 | — | Default copy count for print job 6 |
| 78 | BKPRT_CFG_COPY_7 | INTEGER | 2 | — | Default copy count for print job 7 |
| 79 | BKPRT_CFG_COPY_8 | INTEGER | 2 | — | Default copy count for print job 8 |
| 80 | BKPRT_CFG_COPY_9 | INTEGER | 2 | — | Default copy count for print job 9 |
| 81 | BKPRT_CFG_DCMPY | STRING | 2 | — | Default company code |
| 82 | BKPRT_CFG_DMENU | INTEGER | 2 | — | Default menu number |
| 83 | BKPRT_CFG_DPRTR | INTEGER | 2 | — | Default printer number |
| 84 | BKPRT_CFG_DSPMN | STRING | 1 | — | Display menu flag (Y/N) |
| 85 | BKPRT_CFG_KEY | STRING | 2 | — | Printer config record key |
| 86 | BKPRT_CFG_LPTNO_1 | INTEGER | 1 | — | LPT port number for printer 1 |
| 87 | BKPRT_CFG_LPTNO_10 | INTEGER | 1 | — | LPT port number for printer 10 |
| 88 | BKPRT_CFG_LPTNO_2 | INTEGER | 1 | — | LPT port number for printer 2 |
| 89 | BKPRT_CFG_LPTNO_3 | INTEGER | 1 | — | LPT port number for printer 3 |
| 90 | BKPRT_CFG_LPTNO_4 | INTEGER | 1 | — | LPT port number for printer 4 |
| 91 | BKPRT_CFG_LPTNO_5 | INTEGER | 1 | — | LPT port number for printer 5 |
| 92 | BKPRT_CFG_LPTNO_6 | INTEGER | 1 | — | LPT port number for printer 6 |
| 93 | BKPRT_CFG_LPTNO_7 | INTEGER | 1 | — | LPT port number for printer 7 |
| 94 | BKPRT_CFG_LPTNO_8 | INTEGER | 1 | — | LPT port number for printer 8 |
| 95 | BKPRT_CFG_LPTNO_9 | INTEGER | 1 | — | LPT port number for printer 9 |
| 96 | BKPRT_CFG_NAME_1 | STRING | 25 | — | Display name for printer 1 |
| 97 | BKPRT_CFG_NAME_10 | STRING | 25 | — | Display name for printer 10 |
| 98 | BKPRT_CFG_NAME_2 | STRING | 25 | — | Display name for printer 2 |
| 99 | BKPRT_CFG_NAME_3 | STRING | 25 | — | Display name for printer 3 |
| 100 | BKPRT_CFG_NAME_4 | STRING | 25 | — | Display name for printer 4 |
| 101 | BKPRT_CFG_NAME_5 | STRING | 25 | — | Display name for printer 5 |
| 102 | BKPRT_CFG_NAME_6 | STRING | 25 | — | Display name for printer 6 |
| 103 | BKPRT_CFG_NAME_7 | STRING | 25 | — | Display name for printer 7 |
| 104 | BKPRT_CFG_NAME_8 | STRING | 25 | — | Display name for printer 8 |
| 105 | BKPRT_CFG_NAME_9 | STRING | 25 | — | Display name for printer 9 |
| 106 | BKPRT_CFG_PMAX_1 | INTEGER | 2 | — | Maximum page width (chars) for printer 1 |
| 107 | BKPRT_CFG_PMAX_10 | INTEGER | 2 | — | Maximum page width (chars) for printer 10 |
| 108 | BKPRT_CFG_PMAX_2 | INTEGER | 2 | — | Maximum page width (chars) for printer 2 |
| 109 | BKPRT_CFG_PMAX_3 | INTEGER | 2 | — | Maximum page width (chars) for printer 3 |
| 110 | BKPRT_CFG_PMAX_4 | INTEGER | 2 | — | Maximum page width (chars) for printer 4 |
| 111 | BKPRT_CFG_PMAX_5 | INTEGER | 2 | — | Maximum page width (chars) for printer 5 |
| 112 | BKPRT_CFG_PMAX_6 | INTEGER | 2 | — | Maximum page width (chars) for printer 6 |
| 113 | BKPRT_CFG_PMAX_7 | INTEGER | 2 | — | Maximum page width (chars) for printer 7 |
| 114 | BKPRT_CFG_PMAX_8 | INTEGER | 2 | — | Maximum page width (chars) for printer 8 |
| 115 | BKPRT_CFG_PMAX_9 | INTEGER | 2 | — | Maximum page width (chars) for printer 9 |
| 116 | BKPRT_CFG_PORT_1 | INTEGER | 2 | — | Port number for printer 1 |
| 117 | BKPRT_CFG_PORT_10 | INTEGER | 2 | — | Port number for printer 10 |
| 118 | BKPRT_CFG_PORT_2 | INTEGER | 2 | — | Port number for printer 2 |
| 119 | BKPRT_CFG_PORT_3 | INTEGER | 2 | — | Port number for printer 3 |
| 120 | BKPRT_CFG_PORT_4 | INTEGER | 2 | — | Port number for printer 4 |
| 121 | BKPRT_CFG_PORT_5 | INTEGER | 2 | — | Port number for printer 5 |
| 122 | BKPRT_CFG_PORT_6 | INTEGER | 2 | — | Port number for printer 6 |
| 123 | BKPRT_CFG_PORT_7 | INTEGER | 2 | — | Port number for printer 7 |
| 124 | BKPRT_CFG_PORT_8 | INTEGER | 2 | — | Port number for printer 8 |
| 125 | BKPRT_CFG_PORT_9 | INTEGER | 2 | — | Port number for printer 9 |
| 126 | BKPRT_CFG_PPLNE_1 | INTEGER | 2 | — | Lines per page for printer 1 |
| 127 | BKPRT_CFG_PPLNE_10 | INTEGER | 2 | — | Lines per page for printer 10 |
| 128 | BKPRT_CFG_PPLNE_2 | INTEGER | 2 | — | Lines per page for printer 2 |
| 129 | BKPRT_CFG_PPLNE_3 | INTEGER | 2 | — | Lines per page for printer 3 |
| 130 | BKPRT_CFG_PPLNE_4 | INTEGER | 2 | — | Lines per page for printer 4 |
| 131 | BKPRT_CFG_PPLNE_5 | INTEGER | 2 | — | Lines per page for printer 5 |
| 132 | BKPRT_CFG_PPLNE_6 | INTEGER | 2 | — | Lines per page for printer 6 |
| 133 | BKPRT_CFG_PPLNE_7 | INTEGER | 2 | — | Lines per page for printer 7 |
| 134 | BKPRT_CFG_PPLNE_8 | INTEGER | 2 | — | Lines per page for printer 8 |
| 135 | BKPRT_CFG_PPLNE_9 | INTEGER | 2 | — | Lines per page for printer 9 |
| 136 | BKPRT_CFG_PRTR_1 | STRING | 8 | — | Printer device code for slot 1 |
| 137 | BKPRT_CFG_PRTR_10 | STRING | 8 | — | Printer device code for slot 10 |
| 138 | BKPRT_CFG_PRTR_2 | STRING | 8 | — | Printer device code for slot 2 |
| 139 | BKPRT_CFG_PRTR_3 | STRING | 8 | — | Printer device code for slot 3 |
| 140 | BKPRT_CFG_PRTR_4 | STRING | 8 | — | Printer device code for slot 4 |
| 141 | BKPRT_CFG_PRTR_5 | STRING | 8 | — | Printer device code for slot 5 |
| 142 | BKPRT_CFG_PRTR_6 | STRING | 8 | — | Printer device code for slot 6 |
| 143 | BKPRT_CFG_PRTR_7 | STRING | 8 | — | Printer device code for slot 7 |
| 144 | BKPRT_CFG_PRTR_8 | STRING | 8 | — | Printer device code for slot 8 |
| 145 | BKPRT_CFG_PRTR_9 | STRING | 8 | — | Printer device code for slot 9 |
| 146 | BKPRT_CFG_PWDT_1 | INTEGER | 2 | — | Print width (chars) for printer 1 |
| 147 | BKPRT_CFG_PWDT_10 | INTEGER | 2 | — | Print width (chars) for printer 10 |
| 148 | BKPRT_CFG_PWDT_2 | INTEGER | 2 | — | Print width (chars) for printer 2 |
| 149 | BKPRT_CFG_PWDT_3 | INTEGER | 2 | — | Print width (chars) for printer 3 |
| 150 | BKPRT_CFG_PWDT_4 | INTEGER | 2 | — | Print width (chars) for printer 4 |
| 151 | BKPRT_CFG_PWDT_5 | INTEGER | 2 | — | Print width (chars) for printer 5 |
| 152 | BKPRT_CFG_PWDT_6 | INTEGER | 2 | — | Print width (chars) for printer 6 |
| 153 | BKPRT_CFG_PWDT_7 | INTEGER | 2 | — | Print width (chars) for printer 7 |
| 154 | BKPRT_CFG_PWDT_8 | INTEGER | 2 | — | Print width (chars) for printer 8 |
| 155 | BKPRT_CFG_PWDT_9 | INTEGER | 2 | — | Print width (chars) for printer 9 |
| 156 | BKPRT_CFG_USEPR_1 | INTEGER | 2 | — | User printer assignment for user slot 1 |
| 157 | BKPRT_CFG_USEPR_10 | INTEGER | 2 | — | User printer assignment for user slot 10 |
| 158 | BKPRT_CFG_USEPR_11 | INTEGER | 2 | — | User printer assignment for user slot 11 |
| 159 | BKPRT_CFG_USEPR_12 | INTEGER | 2 | — | User printer assignment for user slot 12 |
| 160 | BKPRT_CFG_USEPR_13 | INTEGER | 2 | — | User printer assignment for user slot 13 |
| 161 | BKPRT_CFG_USEPR_14 | INTEGER | 2 | — | User printer assignment for user slot 14 |
| 162 | BKPRT_CFG_USEPR_15 | INTEGER | 2 | — | User printer assignment for user slot 15 |
| 163 | BKPRT_CFG_USEPR_16 | INTEGER | 2 | — | User printer assignment for user slot 16 |
| 164 | BKPRT_CFG_USEPR_17 | INTEGER | 2 | — | User printer assignment for user slot 17 |
| 165 | BKPRT_CFG_USEPR_18 | INTEGER | 2 | — | User printer assignment for user slot 18 |
| 166 | BKPRT_CFG_USEPR_19 | INTEGER | 2 | — | User printer assignment for user slot 19 |
| 167 | BKPRT_CFG_USEPR_2 | INTEGER | 2 | — | User printer assignment for user slot 2 |
| 168 | BKPRT_CFG_USEPR_20 | INTEGER | 2 | — | User printer assignment for user slot 20 |
| 169 | BKPRT_CFG_USEPR_21 | INTEGER | 2 | — | User printer assignment for user slot 21 |
| 170 | BKPRT_CFG_USEPR_22 | INTEGER | 2 | — | User printer assignment for user slot 22 |
| 171 | BKPRT_CFG_USEPR_23 | INTEGER | 2 | — | User printer assignment for user slot 23 |
| 172 | BKPRT_CFG_USEPR_24 | INTEGER | 2 | — | User printer assignment for user slot 24 |
| 173 | BKPRT_CFG_USEPR_25 | INTEGER | 2 | — | User printer assignment for user slot 25 |
| 174 | BKPRT_CFG_USEPR_26 | INTEGER | 2 | — | User printer assignment for user slot 26 |
| 175 | BKPRT_CFG_USEPR_27 | INTEGER | 2 | — | User printer assignment for user slot 27 |
| 176 | BKPRT_CFG_USEPR_28 | INTEGER | 2 | — | User printer assignment for user slot 28 |
| 177 | BKPRT_CFG_USEPR_29 | INTEGER | 2 | — | User printer assignment for user slot 29 |
| 178 | BKPRT_CFG_USEPR_3 | INTEGER | 2 | — | User printer assignment for user slot 3 |
| 179 | BKPRT_CFG_USEPR_30 | INTEGER | 2 | — | User printer assignment for user slot 30 |
| 180 | BKPRT_CFG_USEPR_31 | INTEGER | 2 | — | User printer assignment for user slot 31 |
| 181 | BKPRT_CFG_USEPR_32 | INTEGER | 2 | — | User printer assignment for user slot 32 |
| 182 | BKPRT_CFG_USEPR_33 | INTEGER | 2 | — | User printer assignment for user slot 33 |
| 183 | BKPRT_CFG_USEPR_34 | INTEGER | 2 | — | User printer assignment for user slot 34 |
| 184 | BKPRT_CFG_USEPR_35 | INTEGER | 2 | — | User printer assignment for user slot 35 |
| 185 | BKPRT_CFG_USEPR_36 | INTEGER | 2 | — | User printer assignment for user slot 36 |
| 186 | BKPRT_CFG_USEPR_37 | INTEGER | 2 | — | User printer assignment for user slot 37 |
| 187 | BKPRT_CFG_USEPR_38 | INTEGER | 2 | — | User printer assignment for user slot 38 |
| 188 | BKPRT_CFG_USEPR_39 | INTEGER | 2 | — | User printer assignment for user slot 39 |
| 189 | BKPRT_CFG_USEPR_4 | INTEGER | 2 | — | User printer assignment for user slot 4 |
| 190 | BKPRT_CFG_USEPR_40 | INTEGER | 2 | — | User printer assignment for user slot 40 |
| 191 | BKPRT_CFG_USEPR_41 | INTEGER | 2 | — | User printer assignment for user slot 41 |
| 192 | BKPRT_CFG_USEPR_42 | INTEGER | 2 | — | User printer assignment for user slot 42 |
| 193 | BKPRT_CFG_USEPR_43 | INTEGER | 2 | — | User printer assignment for user slot 43 |
| 194 | BKPRT_CFG_USEPR_44 | INTEGER | 2 | — | User printer assignment for user slot 44 |
| 195 | BKPRT_CFG_USEPR_45 | INTEGER | 2 | — | User printer assignment for user slot 45 |
| 196 | BKPRT_CFG_USEPR_46 | INTEGER | 2 | — | User printer assignment for user slot 46 |
| 197 | BKPRT_CFG_USEPR_47 | INTEGER | 2 | — | User printer assignment for user slot 47 |
| 198 | BKPRT_CFG_USEPR_48 | INTEGER | 2 | — | User printer assignment for user slot 48 |
| 199 | BKPRT_CFG_USEPR_49 | INTEGER | 2 | — | User printer assignment for user slot 49 |
| 200 | BKPRT_CFG_USEPR_5 | INTEGER | 2 | — | User printer assignment for user slot 5 |
| 201 | BKPRT_CFG_USEPR_50 | INTEGER | 2 | — | User printer assignment for user slot 50 |
| 202 | BKPRT_CFG_USEPR_6 | INTEGER | 2 | — | User printer assignment for user slot 6 |
| 203 | BKPRT_CFG_USEPR_7 | INTEGER | 2 | — | User printer assignment for user slot 7 |
| 204 | BKPRT_CFG_USEPR_8 | INTEGER | 2 | — | User printer assignment for user slot 8 |
| 205 | BKPRT_CFG_USEPR_9 | INTEGER | 2 | — | User printer assignment for user slot 9 |

## BKSYCFG
**System configuration flags** — feature toggle table read by EvoERPmenu.RWN at session start. Controls which major subsystems are enabled.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_CFG_ACCTG | STRING | 1 | — | Accounting module enabled flag (Y/N) |
| 2 | BKSY_CFG_ADVWO | STRING | 1 | — | Advanced Work Order mode enabled (Y/N) |
| 3 | BKSY_CFG_LITEWO | STRING | 1 | — | Lite (simplified) Work Order mode enabled (Y/N) |
| 4 | BKSY_CFG_SALES | STRING | 1 | — | Sales module enabled flag (Y/N) |

## BKSYHELP
**System help lookup** — opened by 1,040+ programs as a standard session table for F1 context-sensitive help text.

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_HELP_PATH | STRING | 70 | — | Path to help files directory |

## BKSYLOG
**Session authorization matrix** — the runtime per-user access control table. Populated at login by EvoERPmenu.RWN / dbamenu_flex.RWN (via the `LOGON`/`LLOGON` handle). Not opened directly by module programs — the menu reads it and propagates access flags to ISTS.CFG keys (GLCTRL, POSEC, SOSEC, WHCTRL) which all programs then read.

Structure: 20 single-char Y/N "OK" flags per module (OKAP, OKAR, OKGL, OKIC, OKPO, OKPR, OKSO, OKSY, OTH1, OTH2) mapping to the 20 menu slots in each module letter (A–T), plus top-level Y/N enable flags (APYN, ARYN, GLYN, ICYN, POYN, PRYN, SOYN, SYYN, OKLM), and session identity fields (CODE/PSWD/SCTY/CHR). This is the access-control mechanism: BKSY_LOGON_OKGL_3='Y' means the user has access to GL menu item G (3rd slot). Index mapping to menu codes not yet confirmed.

Fields: 215

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_LOGON_APYN | STRING | 1 | — | AP module enabled for this user (Y/N) |
| 2 | BKSY_LOGON_ARYN | STRING | 1 | — | AR module enabled for this user (Y/N) |
| 3 | BKSY_LOGON_CHR | STRING | 1 | — | User type/character code |
| 4 | BKSY_LOGON_CODE | STRING | 15 | — | User code (login ID) |
| 5 | BKSY_LOGON_GLYN | STRING | 1 | — | GL module enabled for this user (Y/N) |
| 6 | BKSY_LOGON_ICYN | STRING | 1 | — | IC (Inventory Control) module enabled for this user (Y/N) |
| 7 | BKSY_LOGON_O1YN | STRING | 1 | — | Other module 1 enabled for this user (Y/N) |
| 8 | BKSY_LOGON_O2YN | STRING | 1 | — | Other module 2 enabled for this user (Y/N) |
| 9 | BKSY_LOGON_OKAP_1 | STRING | 1 | — | AP module access flag for menu slot 1 (Y/N) |
| 10 | BKSY_LOGON_OKAP_10 | STRING | 1 | — | AP module access flag for menu slot 10 (Y/N) |
| 11 | BKSY_LOGON_OKAP_11 | STRING | 1 | — | AP module access flag for menu slot 11 (Y/N) |
| 12 | BKSY_LOGON_OKAP_12 | STRING | 1 | — | AP module access flag for menu slot 12 (Y/N) |
| 13 | BKSY_LOGON_OKAP_13 | STRING | 1 | — | AP module access flag for menu slot 13 (Y/N) |
| 14 | BKSY_LOGON_OKAP_14 | STRING | 1 | — | AP module access flag for menu slot 14 (Y/N) |
| 15 | BKSY_LOGON_OKAP_15 | STRING | 1 | — | AP module access flag for menu slot 15 (Y/N) |
| 16 | BKSY_LOGON_OKAP_16 | STRING | 1 | — | AP module access flag for menu slot 16 (Y/N) |
| 17 | BKSY_LOGON_OKAP_17 | STRING | 1 | — | AP module access flag for menu slot 17 (Y/N) |
| 18 | BKSY_LOGON_OKAP_18 | STRING | 1 | — | AP module access flag for menu slot 18 (Y/N) |
| 19 | BKSY_LOGON_OKAP_19 | STRING | 1 | — | AP module access flag for menu slot 19 (Y/N) |
| 20 | BKSY_LOGON_OKAP_2 | STRING | 1 | — | AP module access flag for menu slot 2 (Y/N) |
| 21 | BKSY_LOGON_OKAP_20 | STRING | 1 | — | AP module access flag for menu slot 20 (Y/N) |
| 22 | BKSY_LOGON_OKAP_3 | STRING | 1 | — | AP module access flag for menu slot 3 (Y/N) |
| 23 | BKSY_LOGON_OKAP_4 | STRING | 1 | — | AP module access flag for menu slot 4 (Y/N) |
| 24 | BKSY_LOGON_OKAP_5 | STRING | 1 | — | AP module access flag for menu slot 5 (Y/N) |
| 25 | BKSY_LOGON_OKAP_6 | STRING | 1 | — | AP module access flag for menu slot 6 (Y/N) |
| 26 | BKSY_LOGON_OKAP_7 | STRING | 1 | — | AP module access flag for menu slot 7 (Y/N) |
| 27 | BKSY_LOGON_OKAP_8 | STRING | 1 | — | AP module access flag for menu slot 8 (Y/N) |
| 28 | BKSY_LOGON_OKAP_9 | STRING | 1 | — | AP module access flag for menu slot 9 (Y/N) |
| 29 | BKSY_LOGON_OKAR_1 | STRING | 1 | — | AR module access flag for menu slot 1 (Y/N) |
| 30 | BKSY_LOGON_OKAR_10 | STRING | 1 | — | AR module access flag for menu slot 10 (Y/N) |
| 31 | BKSY_LOGON_OKAR_11 | STRING | 1 | — | AR module access flag for menu slot 11 (Y/N) |
| 32 | BKSY_LOGON_OKAR_12 | STRING | 1 | — | AR module access flag for menu slot 12 (Y/N) |
| 33 | BKSY_LOGON_OKAR_13 | STRING | 1 | — | AR module access flag for menu slot 13 (Y/N) |
| 34 | BKSY_LOGON_OKAR_14 | STRING | 1 | — | AR module access flag for menu slot 14 (Y/N) |
| 35 | BKSY_LOGON_OKAR_15 | STRING | 1 | — | AR module access flag for menu slot 15 (Y/N) |
| 36 | BKSY_LOGON_OKAR_16 | STRING | 1 | — | AR module access flag for menu slot 16 (Y/N) |
| 37 | BKSY_LOGON_OKAR_17 | STRING | 1 | — | AR module access flag for menu slot 17 (Y/N) |
| 38 | BKSY_LOGON_OKAR_18 | STRING | 1 | — | AR module access flag for menu slot 18 (Y/N) |
| 39 | BKSY_LOGON_OKAR_19 | STRING | 1 | — | AR module access flag for menu slot 19 (Y/N) |
| 40 | BKSY_LOGON_OKAR_2 | STRING | 1 | — | AR module access flag for menu slot 2 (Y/N) |
| 41 | BKSY_LOGON_OKAR_20 | STRING | 1 | — | AR module access flag for menu slot 20 (Y/N) |
| 42 | BKSY_LOGON_OKAR_3 | STRING | 1 | — | AR module access flag for menu slot 3 (Y/N) |
| 43 | BKSY_LOGON_OKAR_4 | STRING | 1 | — | AR module access flag for menu slot 4 (Y/N) |
| 44 | BKSY_LOGON_OKAR_5 | STRING | 1 | — | AR module access flag for menu slot 5 (Y/N) |
| 45 | BKSY_LOGON_OKAR_6 | STRING | 1 | — | AR module access flag for menu slot 6 (Y/N) |
| 46 | BKSY_LOGON_OKAR_7 | STRING | 1 | — | AR module access flag for menu slot 7 (Y/N) |
| 47 | BKSY_LOGON_OKAR_8 | STRING | 1 | — | AR module access flag for menu slot 8 (Y/N) |
| 48 | BKSY_LOGON_OKAR_9 | STRING | 1 | — | AR module access flag for menu slot 9 (Y/N) |
| 49 | BKSY_LOGON_OKGL_1 | STRING | 1 | — | GL module access flag for menu slot 1 (Y/N) |
| 50 | BKSY_LOGON_OKGL_10 | STRING | 1 | — | GL module access flag for menu slot 10 (Y/N) |
| 51 | BKSY_LOGON_OKGL_11 | STRING | 1 | — | GL module access flag for menu slot 11 (Y/N) |
| 52 | BKSY_LOGON_OKGL_12 | STRING | 1 | — | GL module access flag for menu slot 12 (Y/N) |
| 53 | BKSY_LOGON_OKGL_13 | STRING | 1 | — | GL module access flag for menu slot 13 (Y/N) |
| 54 | BKSY_LOGON_OKGL_14 | STRING | 1 | — | GL module access flag for menu slot 14 (Y/N) |
| 55 | BKSY_LOGON_OKGL_15 | STRING | 1 | — | GL module access flag for menu slot 15 (Y/N) |
| 56 | BKSY_LOGON_OKGL_16 | STRING | 1 | — | GL module access flag for menu slot 16 (Y/N) |
| 57 | BKSY_LOGON_OKGL_17 | STRING | 1 | — | GL module access flag for menu slot 17 (Y/N) |
| 58 | BKSY_LOGON_OKGL_18 | STRING | 1 | — | GL module access flag for menu slot 18 (Y/N) |
| 59 | BKSY_LOGON_OKGL_19 | STRING | 1 | — | GL module access flag for menu slot 19 (Y/N) |
| 60 | BKSY_LOGON_OKGL_2 | STRING | 1 | — | GL module access flag for menu slot 2 (Y/N) |
| 61 | BKSY_LOGON_OKGL_20 | STRING | 1 | — | GL module access flag for menu slot 20 (Y/N) |
| 62 | BKSY_LOGON_OKGL_3 | STRING | 1 | — | GL module access flag for menu slot 3 (Y/N) |
| 63 | BKSY_LOGON_OKGL_4 | STRING | 1 | — | GL module access flag for menu slot 4 (Y/N) |
| 64 | BKSY_LOGON_OKGL_5 | STRING | 1 | — | GL module access flag for menu slot 5 (Y/N) |
| 65 | BKSY_LOGON_OKGL_6 | STRING | 1 | — | GL module access flag for menu slot 6 (Y/N) |
| 66 | BKSY_LOGON_OKGL_7 | STRING | 1 | — | GL module access flag for menu slot 7 (Y/N) |
| 67 | BKSY_LOGON_OKGL_8 | STRING | 1 | — | GL module access flag for menu slot 8 (Y/N) |
| 68 | BKSY_LOGON_OKGL_9 | STRING | 1 | — | GL module access flag for menu slot 9 (Y/N) |
| 69 | BKSY_LOGON_OKIC_1 | STRING | 1 | — | IC module access flag for menu slot 1 (Y/N) |
| 70 | BKSY_LOGON_OKIC_10 | STRING | 1 | — | IC module access flag for menu slot 10 (Y/N) |
| 71 | BKSY_LOGON_OKIC_11 | STRING | 1 | — | IC module access flag for menu slot 11 (Y/N) |
| 72 | BKSY_LOGON_OKIC_12 | STRING | 1 | — | IC module access flag for menu slot 12 (Y/N) |
| 73 | BKSY_LOGON_OKIC_13 | STRING | 1 | — | IC module access flag for menu slot 13 (Y/N) |
| 74 | BKSY_LOGON_OKIC_14 | STRING | 1 | — | IC module access flag for menu slot 14 (Y/N) |
| 75 | BKSY_LOGON_OKIC_15 | STRING | 1 | — | IC module access flag for menu slot 15 (Y/N) |
| 76 | BKSY_LOGON_OKIC_16 | STRING | 1 | — | IC module access flag for menu slot 16 (Y/N) |
| 77 | BKSY_LOGON_OKIC_17 | STRING | 1 | — | IC module access flag for menu slot 17 (Y/N) |
| 78 | BKSY_LOGON_OKIC_18 | STRING | 1 | — | IC module access flag for menu slot 18 (Y/N) |
| 79 | BKSY_LOGON_OKIC_19 | STRING | 1 | — | IC module access flag for menu slot 19 (Y/N) |
| 80 | BKSY_LOGON_OKIC_2 | STRING | 1 | — | IC module access flag for menu slot 2 (Y/N) |
| 81 | BKSY_LOGON_OKIC_20 | STRING | 1 | — | IC module access flag for menu slot 20 (Y/N) |
| 82 | BKSY_LOGON_OKIC_3 | STRING | 1 | — | IC module access flag for menu slot 3 (Y/N) |
| 83 | BKSY_LOGON_OKIC_4 | STRING | 1 | — | IC module access flag for menu slot 4 (Y/N) |
| 84 | BKSY_LOGON_OKIC_5 | STRING | 1 | — | IC module access flag for menu slot 5 (Y/N) |
| 85 | BKSY_LOGON_OKIC_6 | STRING | 1 | — | IC module access flag for menu slot 6 (Y/N) |
| 86 | BKSY_LOGON_OKIC_7 | STRING | 1 | — | IC module access flag for menu slot 7 (Y/N) |
| 87 | BKSY_LOGON_OKIC_8 | STRING | 1 | — | IC module access flag for menu slot 8 (Y/N) |
| 88 | BKSY_LOGON_OKIC_9 | STRING | 1 | — | IC module access flag for menu slot 9 (Y/N) |
| 89 | BKSY_LOGON_OKLM | STRING | 1 | — | LM (Labor Module?) enabled for this user (Y/N) |
| 90 | BKSY_LOGON_OKPO_1 | STRING | 1 | — | PO module access flag for menu slot 1 (Y/N) |
| 91 | BKSY_LOGON_OKPO_10 | STRING | 1 | — | PO module access flag for menu slot 10 (Y/N) |
| 92 | BKSY_LOGON_OKPO_11 | STRING | 1 | — | PO module access flag for menu slot 11 (Y/N) |
| 93 | BKSY_LOGON_OKPO_12 | STRING | 1 | — | PO module access flag for menu slot 12 (Y/N) |
| 94 | BKSY_LOGON_OKPO_13 | STRING | 1 | — | PO module access flag for menu slot 13 (Y/N) |
| 95 | BKSY_LOGON_OKPO_14 | STRING | 1 | — | PO module access flag for menu slot 14 (Y/N) |
| 96 | BKSY_LOGON_OKPO_15 | STRING | 1 | — | PO module access flag for menu slot 15 (Y/N) |
| 97 | BKSY_LOGON_OKPO_16 | STRING | 1 | — | PO module access flag for menu slot 16 (Y/N) |
| 98 | BKSY_LOGON_OKPO_17 | STRING | 1 | — | PO module access flag for menu slot 17 (Y/N) |
| 99 | BKSY_LOGON_OKPO_18 | STRING | 1 | — | PO module access flag for menu slot 18 (Y/N) |
| 100 | BKSY_LOGON_OKPO_19 | STRING | 1 | — | PO module access flag for menu slot 19 (Y/N) |
| 101 | BKSY_LOGON_OKPO_2 | STRING | 1 | — | PO module access flag for menu slot 2 (Y/N) |
| 102 | BKSY_LOGON_OKPO_20 | STRING | 1 | — | PO module access flag for menu slot 20 (Y/N) |
| 103 | BKSY_LOGON_OKPO_3 | STRING | 1 | — | PO module access flag for menu slot 3 (Y/N) |
| 104 | BKSY_LOGON_OKPO_4 | STRING | 1 | — | PO module access flag for menu slot 4 (Y/N) |
| 105 | BKSY_LOGON_OKPO_5 | STRING | 1 | — | PO module access flag for menu slot 5 (Y/N) |
| 106 | BKSY_LOGON_OKPO_6 | STRING | 1 | — | PO module access flag for menu slot 6 (Y/N) |
| 107 | BKSY_LOGON_OKPO_7 | STRING | 1 | — | PO module access flag for menu slot 7 (Y/N) |
| 108 | BKSY_LOGON_OKPO_8 | STRING | 1 | — | PO module access flag for menu slot 8 (Y/N) |
| 109 | BKSY_LOGON_OKPO_9 | STRING | 1 | — | PO module access flag for menu slot 9 (Y/N) |
| 110 | BKSY_LOGON_OKPR_1 | STRING | 1 | — | PR module access flag for menu slot 1 (Y/N) |
| 111 | BKSY_LOGON_OKPR_10 | STRING | 1 | — | PR module access flag for menu slot 10 (Y/N) |
| 112 | BKSY_LOGON_OKPR_11 | STRING | 1 | — | PR module access flag for menu slot 11 (Y/N) |
| 113 | BKSY_LOGON_OKPR_12 | STRING | 1 | — | PR module access flag for menu slot 12 (Y/N) |
| 114 | BKSY_LOGON_OKPR_13 | STRING | 1 | — | PR module access flag for menu slot 13 (Y/N) |
| 115 | BKSY_LOGON_OKPR_14 | STRING | 1 | — | PR module access flag for menu slot 14 (Y/N) |
| 116 | BKSY_LOGON_OKPR_15 | STRING | 1 | — | PR module access flag for menu slot 15 (Y/N) |
| 117 | BKSY_LOGON_OKPR_16 | STRING | 1 | — | PR module access flag for menu slot 16 (Y/N) |
| 118 | BKSY_LOGON_OKPR_17 | STRING | 1 | — | PR module access flag for menu slot 17 (Y/N) |
| 119 | BKSY_LOGON_OKPR_18 | STRING | 1 | — | PR module access flag for menu slot 18 (Y/N) |
| 120 | BKSY_LOGON_OKPR_19 | STRING | 1 | — | PR module access flag for menu slot 19 (Y/N) |
| 121 | BKSY_LOGON_OKPR_2 | STRING | 1 | — | PR module access flag for menu slot 2 (Y/N) |
| 122 | BKSY_LOGON_OKPR_20 | STRING | 1 | — | PR module access flag for menu slot 20 (Y/N) |
| 123 | BKSY_LOGON_OKPR_3 | STRING | 1 | — | PR module access flag for menu slot 3 (Y/N) |
| 124 | BKSY_LOGON_OKPR_4 | STRING | 1 | — | PR module access flag for menu slot 4 (Y/N) |
| 125 | BKSY_LOGON_OKPR_5 | STRING | 1 | — | PR module access flag for menu slot 5 (Y/N) |
| 126 | BKSY_LOGON_OKPR_6 | STRING | 1 | — | PR module access flag for menu slot 6 (Y/N) |
| 127 | BKSY_LOGON_OKPR_7 | STRING | 1 | — | PR module access flag for menu slot 7 (Y/N) |
| 128 | BKSY_LOGON_OKPR_8 | STRING | 1 | — | PR module access flag for menu slot 8 (Y/N) |
| 129 | BKSY_LOGON_OKPR_9 | STRING | 1 | — | PR module access flag for menu slot 9 (Y/N) |
| 130 | BKSY_LOGON_OKSO_1 | STRING | 1 | — | SO module access flag for menu slot 1 (Y/N) |
| 131 | BKSY_LOGON_OKSO_10 | STRING | 1 | — | SO module access flag for menu slot 10 (Y/N) |
| 132 | BKSY_LOGON_OKSO_11 | STRING | 1 | — | SO module access flag for menu slot 11 (Y/N) |
| 133 | BKSY_LOGON_OKSO_12 | STRING | 1 | — | SO module access flag for menu slot 12 (Y/N) |
| 134 | BKSY_LOGON_OKSO_13 | STRING | 1 | — | SO module access flag for menu slot 13 (Y/N) |
| 135 | BKSY_LOGON_OKSO_14 | STRING | 1 | — | SO module access flag for menu slot 14 (Y/N) |
| 136 | BKSY_LOGON_OKSO_15 | STRING | 1 | — | SO module access flag for menu slot 15 (Y/N) |
| 137 | BKSY_LOGON_OKSO_16 | STRING | 1 | — | SO module access flag for menu slot 16 (Y/N) |
| 138 | BKSY_LOGON_OKSO_17 | STRING | 1 | — | SO module access flag for menu slot 17 (Y/N) |
| 139 | BKSY_LOGON_OKSO_18 | STRING | 1 | — | SO module access flag for menu slot 18 (Y/N) |
| 140 | BKSY_LOGON_OKSO_19 | STRING | 1 | — | SO module access flag for menu slot 19 (Y/N) |
| 141 | BKSY_LOGON_OKSO_2 | STRING | 1 | — | SO module access flag for menu slot 2 (Y/N) |
| 142 | BKSY_LOGON_OKSO_20 | STRING | 1 | — | SO module access flag for menu slot 20 (Y/N) |
| 143 | BKSY_LOGON_OKSO_3 | STRING | 1 | — | SO module access flag for menu slot 3 (Y/N) |
| 144 | BKSY_LOGON_OKSO_4 | STRING | 1 | — | SO module access flag for menu slot 4 (Y/N) |
| 145 | BKSY_LOGON_OKSO_5 | STRING | 1 | — | SO module access flag for menu slot 5 (Y/N) |
| 146 | BKSY_LOGON_OKSO_6 | STRING | 1 | — | SO module access flag for menu slot 6 (Y/N) |
| 147 | BKSY_LOGON_OKSO_7 | STRING | 1 | — | SO module access flag for menu slot 7 (Y/N) |
| 148 | BKSY_LOGON_OKSO_8 | STRING | 1 | — | SO module access flag for menu slot 8 (Y/N) |
| 149 | BKSY_LOGON_OKSO_9 | STRING | 1 | — | SO module access flag for menu slot 9 (Y/N) |
| 150 | BKSY_LOGON_OKSY_1 | STRING | 1 | — | SY module access flag for menu slot 1 (Y/N) |
| 151 | BKSY_LOGON_OKSY_10 | STRING | 1 | — | SY module access flag for menu slot 10 (Y/N) |
| 152 | BKSY_LOGON_OKSY_11 | STRING | 1 | — | SY module access flag for menu slot 11 (Y/N) |
| 153 | BKSY_LOGON_OKSY_12 | STRING | 1 | — | SY module access flag for menu slot 12 (Y/N) |
| 154 | BKSY_LOGON_OKSY_13 | STRING | 1 | — | SY module access flag for menu slot 13 (Y/N) |
| 155 | BKSY_LOGON_OKSY_14 | STRING | 1 | — | SY module access flag for menu slot 14 (Y/N) |
| 156 | BKSY_LOGON_OKSY_15 | STRING | 1 | — | SY module access flag for menu slot 15 (Y/N) |
| 157 | BKSY_LOGON_OKSY_16 | STRING | 1 | — | SY module access flag for menu slot 16 (Y/N) |
| 158 | BKSY_LOGON_OKSY_17 | STRING | 1 | — | SY module access flag for menu slot 17 (Y/N) |
| 159 | BKSY_LOGON_OKSY_18 | STRING | 1 | — | SY module access flag for menu slot 18 (Y/N) |
| 160 | BKSY_LOGON_OKSY_19 | STRING | 1 | — | SY module access flag for menu slot 19 (Y/N) |
| 161 | BKSY_LOGON_OKSY_2 | STRING | 1 | — | SY module access flag for menu slot 2 (Y/N) |
| 162 | BKSY_LOGON_OKSY_20 | STRING | 1 | — | SY module access flag for menu slot 20 (Y/N) |
| 163 | BKSY_LOGON_OKSY_3 | STRING | 1 | — | SY module access flag for menu slot 3 (Y/N) |
| 164 | BKSY_LOGON_OKSY_4 | STRING | 1 | — | SY module access flag for menu slot 4 (Y/N) |
| 165 | BKSY_LOGON_OKSY_5 | STRING | 1 | — | SY module access flag for menu slot 5 (Y/N) |
| 166 | BKSY_LOGON_OKSY_6 | STRING | 1 | — | SY module access flag for menu slot 6 (Y/N) |
| 167 | BKSY_LOGON_OKSY_7 | STRING | 1 | — | SY module access flag for menu slot 7 (Y/N) |
| 168 | BKSY_LOGON_OKSY_8 | STRING | 1 | — | SY module access flag for menu slot 8 (Y/N) |
| 169 | BKSY_LOGON_OKSY_9 | STRING | 1 | — | SY module access flag for menu slot 9 (Y/N) |
| 170 | BKSY_LOGON_OTH1_1 | STRING | 1 | — | Other module 1 access flag for menu slot 1 (Y/N) |
| 171 | BKSY_LOGON_OTH1_10 | STRING | 1 | — | Other module 1 access flag for menu slot 10 (Y/N) |
| 172 | BKSY_LOGON_OTH1_11 | STRING | 1 | — | Other module 1 access flag for menu slot 11 (Y/N) |
| 173 | BKSY_LOGON_OTH1_12 | STRING | 1 | — | Other module 1 access flag for menu slot 12 (Y/N) |
| 174 | BKSY_LOGON_OTH1_13 | STRING | 1 | — | Other module 1 access flag for menu slot 13 (Y/N) |
| 175 | BKSY_LOGON_OTH1_14 | STRING | 1 | — | Other module 1 access flag for menu slot 14 (Y/N) |
| 176 | BKSY_LOGON_OTH1_15 | STRING | 1 | — | Other module 1 access flag for menu slot 15 (Y/N) |
| 177 | BKSY_LOGON_OTH1_16 | STRING | 1 | — | Other module 1 access flag for menu slot 16 (Y/N) |
| 178 | BKSY_LOGON_OTH1_17 | STRING | 1 | — | Other module 1 access flag for menu slot 17 (Y/N) |
| 179 | BKSY_LOGON_OTH1_18 | STRING | 1 | — | Other module 1 access flag for menu slot 18 (Y/N) |
| 180 | BKSY_LOGON_OTH1_19 | STRING | 1 | — | Other module 1 access flag for menu slot 19 (Y/N) |
| 181 | BKSY_LOGON_OTH1_2 | STRING | 1 | — | Other module 1 access flag for menu slot 2 (Y/N) |
| 182 | BKSY_LOGON_OTH1_20 | STRING | 1 | — | Other module 1 access flag for menu slot 20 (Y/N) |
| 183 | BKSY_LOGON_OTH1_3 | STRING | 1 | — | Other module 1 access flag for menu slot 3 (Y/N) |
| 184 | BKSY_LOGON_OTH1_4 | STRING | 1 | — | Other module 1 access flag for menu slot 4 (Y/N) |
| 185 | BKSY_LOGON_OTH1_5 | STRING | 1 | — | Other module 1 access flag for menu slot 5 (Y/N) |
| 186 | BKSY_LOGON_OTH1_6 | STRING | 1 | — | Other module 1 access flag for menu slot 6 (Y/N) |
| 187 | BKSY_LOGON_OTH1_7 | STRING | 1 | — | Other module 1 access flag for menu slot 7 (Y/N) |
| 188 | BKSY_LOGON_OTH1_8 | STRING | 1 | — | Other module 1 access flag for menu slot 8 (Y/N) |
| 189 | BKSY_LOGON_OTH1_9 | STRING | 1 | — | Other module 1 access flag for menu slot 9 (Y/N) |
| 190 | BKSY_LOGON_OTH2_1 | STRING | 2 | — | Other module 2 extended flag for slot 1 |
| 191 | BKSY_LOGON_OTH2_10 | STRING | 2 | — | Other module 2 extended flag for slot 10 |
| 192 | BKSY_LOGON_OTH2_11 | STRING | 2 | — | Other module 2 extended flag for slot 11 |
| 193 | BKSY_LOGON_OTH2_12 | STRING | 2 | — | Other module 2 extended flag for slot 12 |
| 194 | BKSY_LOGON_OTH2_13 | STRING | 2 | — | Other module 2 extended flag for slot 13 |
| 195 | BKSY_LOGON_OTH2_14 | STRING | 2 | — | Other module 2 extended flag for slot 14 |
| 196 | BKSY_LOGON_OTH2_15 | STRING | 2 | — | Other module 2 extended flag for slot 15 |
| 197 | BKSY_LOGON_OTH2_16 | STRING | 2 | — | Other module 2 extended flag for slot 16 |
| 198 | BKSY_LOGON_OTH2_17 | STRING | 2 | — | Other module 2 extended flag for slot 17 |
| 199 | BKSY_LOGON_OTH2_18 | STRING | 2 | — | Other module 2 extended flag for slot 18 |
| 200 | BKSY_LOGON_OTH2_19 | STRING | 2 | — | Other module 2 extended flag for slot 19 |
| 201 | BKSY_LOGON_OTH2_2 | STRING | 2 | — | Other module 2 extended flag for slot 2 |
| 202 | BKSY_LOGON_OTH2_20 | STRING | 2 | — | Other module 2 extended flag for slot 20 |
| 203 | BKSY_LOGON_OTH2_3 | STRING | 2 | — | Other module 2 extended flag for slot 3 |
| 204 | BKSY_LOGON_OTH2_4 | STRING | 2 | — | Other module 2 extended flag for slot 4 |
| 205 | BKSY_LOGON_OTH2_5 | STRING | 2 | — | Other module 2 extended flag for slot 5 |
| 206 | BKSY_LOGON_OTH2_6 | STRING | 2 | — | Other module 2 extended flag for slot 6 |
| 207 | BKSY_LOGON_OTH2_7 | STRING | 2 | — | Other module 2 extended flag for slot 7 |
| 208 | BKSY_LOGON_OTH2_8 | STRING | 2 | — | Other module 2 extended flag for slot 8 |
| 209 | BKSY_LOGON_OTH2_9 | STRING | 2 | — | Other module 2 extended flag for slot 9 |
| 210 | BKSY_LOGON_POYN | STRING | 1 | — | PO module enabled for this user (Y/N) |
| 211 | BKSY_LOGON_PRYN | STRING | 1 | — | PR (Payroll/Production?) module enabled for this user (Y/N) |
| 212 | BKSY_LOGON_PSWD | STRING | 10 | — | User password (stored encrypted via ENCRYPTSTR) |
| 213 | BKSY_LOGON_SCTY | STRING | 2 | — | Security level code |
| 214 | BKSY_LOGON_SOYN | STRING | 1 | — | SO module enabled for this user (Y/N) |
| 215 | BKSY_LOGON_SYYN | STRING | 1 | — | SY (System admin) module enabled for this user (Y/N) |

## BKSYPRTR
**System printer assignments** — used by 33+ programs including EVODCSETUP/EVODEFPRINT. Stores default and per-station printer settings.

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSY_PRTR_EXEC | STRING | 8 | — | Printer executable/driver name |
| 2 | BKSY_PRTR_LASER | STRING | 1 | — | Laser printer flag (Y/N) |
| 3 | BKSY_PRTR_LPTNM | INTEGER | 1 | — | LPT port number |
| 4 | BKSY_PRTR_NAME | STRING | 30 | — | Printer name |
| 5 | BKSY_PRTR_PMAX | INTEGER | 2 | — | Maximum pages per job |
| 6 | BKSY_PRTR_POST | STRING | 8 | — | Post-print command |
| 7 | BKSY_PRTR_PPLNE | INTEGER | 2 | — | Lines per page |
| 8 | BKSY_PRTR_PRUN | STRING | 1 | — | Print-run mode flag |
| 9 | BKSY_PRTR_PWDT | INTEGER | 2 | — | Page width in characters |
| 10 | BKSY_PRTR_TAS | STRING | 1 | — | TAS native print flag (Y/N) |
| 11 | BKSY_PRTR_TYPE | STRING | 8 | — | Printer type code |

## BKUMSRTY
**NOT USED**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SCRTY_GROUP | STRING | 1 | — | Security group code |
| 2 | SCRTY_ITEM_1 | STRING | 1 | — | Security item access flag for slot 1 (Y/N) |
| 3 | SCRTY_ITEM_10 | STRING | 1 | — | Security item access flag for slot 10 (Y/N) |
| 4 | SCRTY_ITEM_11 | STRING | 1 | — | Security item access flag for slot 11 (Y/N) |
| 5 | SCRTY_ITEM_12 | STRING | 1 | — | Security item access flag for slot 12 (Y/N) |
| 6 | SCRTY_ITEM_13 | STRING | 1 | — | Security item access flag for slot 13 (Y/N) |
| 7 | SCRTY_ITEM_14 | STRING | 1 | — | Security item access flag for slot 14 (Y/N) |
| 8 | SCRTY_ITEM_15 | STRING | 1 | — | Security item access flag for slot 15 (Y/N) |
| 9 | SCRTY_ITEM_16 | STRING | 1 | — | Security item access flag for slot 16 (Y/N) |
| 10 | SCRTY_ITEM_17 | STRING | 1 | — | Security item access flag for slot 17 (Y/N) |
| 11 | SCRTY_ITEM_18 | STRING | 1 | — | Security item access flag for slot 18 (Y/N) |
| 12 | SCRTY_ITEM_19 | STRING | 1 | — | Security item access flag for slot 19 (Y/N) |
| 13 | SCRTY_ITEM_2 | STRING | 1 | — | Security item access flag for slot 2 (Y/N) |
| 14 | SCRTY_ITEM_20 | STRING | 1 | — | Security item access flag for slot 20 (Y/N) |
| 15 | SCRTY_ITEM_3 | STRING | 1 | — | Security item access flag for slot 3 (Y/N) |
| 16 | SCRTY_ITEM_4 | STRING | 1 | — | Security item access flag for slot 4 (Y/N) |
| 17 | SCRTY_ITEM_5 | STRING | 1 | — | Security item access flag for slot 5 (Y/N) |
| 18 | SCRTY_ITEM_6 | STRING | 1 | — | Security item access flag for slot 6 (Y/N) |
| 19 | SCRTY_ITEM_7 | STRING | 1 | — | Security item access flag for slot 7 (Y/N) |
| 20 | SCRTY_ITEM_8 | STRING | 1 | — | Security item access flag for slot 8 (Y/N) |
| 21 | SCRTY_ITEM_9 | STRING | 1 | — | Security item access flag for slot 9 (Y/N) |
| 22 | SCRTY_LEVEL | STRING | 2 | — | Security level code |
| 23 | SCRTY_MENU | INTEGER | 2 | — | Menu number for this security record |

## BKUPDATE
**NOT USED**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKUP_COMPANY | STRING | 2 | — | Company code updated |
| 2 | BKUP_DATE | DATE | 4 | — | Date of last update |
| 3 | BKUP_UPDATE | STRING | 1 | — | Update applied flag (Y/N) |
| 4 | BKUPDATE_VER | STRING | 15 | — | Version/update number |

## BOMCHG
**NOT USED**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BOM_CHG_ACOMP | STRING | 1 | — | After: component required flag (Y/N) |
| 2 | BOM_CHG_AEXTRA | STRING | 100 | — | After: extra field |
| 3 | BOM_CHG_AQTY | NUMERIC | 8 | 8 | After: quantity per assembly |
| 4 | BOM_CHG_AREF | STRING | 20 | — | After: reference designator |
| 5 | BOM_CHG_ASCRAP | NUMERIC | 8 | 2 | After: scrap factor |
| 6 | BOM_CHG_BEXTRA | STRING | 100 | — | Before: extra field |
| 7 | BOM_CHG_BQTY | NUMERIC | 8 | 8 | Before: quantity per assembly |
| 8 | BOM_CHG_BREF | STRING | 20 | — | Before: reference designator |
| 9 | BOM_CHG_BSCRAP | NUMERIC | 8 | 2 | Before: scrap factor |
| 10 | BOM_CHG_CDATE | DATE | 4 | — | Change date |
| 11 | BOM_CHG_COMP | STRING | 15 | — | Component item code |
| 12 | BOM_CHG_DCOMP | STRING | 1 | — | Delete component flag (Y/N) |
| 13 | BOM_CHG_PARENT | STRING | 15 | — | Parent assembly item code |
| 14 | BOM_CHG_UID | STRING | 20 | — | Unique change ID |
| 15 | BOM_CHG_USER | STRING | 15 | — | User who made the change |

## CCEDIXRF
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CC_EDI_CUSTCODE | STRING | 10 | — | Customer code |
| 2 | CC_EDI_NEXT | NUMERIC | 8 | — | Next EDI transaction number |
| 3 | CC_EDI_SENDERID | STRING | 15 | — | EDI sender ID |
| 4 | CC_EDI_SHIPTO | STRING | 10 | — | Ship-to code |
| 5 | CC_EDI_SHPTCODE | STRING | 17 | — | Ship-to location code |
| 6 | CC_EDI_SHPTZIP | STRING | 10 | — | Ship-to zip code |

## DBACNAME
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CNAME_CODE | STRING | 2 | — | Company code |
| 2 | CNAME_FILLER | STRING | 40 | — | Reserved filler field |
| 3 | CNAME_NAME | STRING | 25 | — | Company name |

## ESTCHGS
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESCH_AMT | NUMERIC | 8 | 2 | Estimated charge amount |
| 2 | MTESCH_DESC | STRING | 30 | — | Charge description |
| 3 | MTESCH_QUOTE | NUMERIC | 8 | — | Quote number |

## ESTMAT
**NOT USED**

Fields: 18

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESMAT_CODE | STRING | 15 | — | Material item code |
| 2 | MTESMAT_COST1 | NUMERIC | 8 | 6 | Cost tier 1 |
| 3 | MTESMAT_COST2 | NUMERIC | 8 | 6 | Cost tier 2 |
| 4 | MTESMAT_COST3 | NUMERIC | 8 | 6 | Cost tier 3 |
| 5 | MTESMAT_COST4 | NUMERIC | 8 | 6 | Cost tier 4 |
| 6 | MTESMAT_COST5 | NUMERIC | 8 | 6 | Cost tier 5 |
| 7 | MTESMAT_COSTCD | STRING | 1 | — | Cost code (tier selector) |
| 8 | MTESMAT_DESC | STRING | 30 | — | Material description |
| 9 | MTESMAT_QTYPER | NUMERIC | 8 | 8 | Quantity per assembly |
| 10 | MTESMAT_QUOTE | NUMERIC | 8 | — | Quote number |
| 11 | MTESMAT_QUREF | NUMERIC | 8 | — | Quote reference line number |
| 12 | MTESMAT_REMARKS_1 | STRING | 30 | — | Remark line 1 |
| 13 | MTESMAT_REMARKS_2 | STRING | 30 | — | Remark line 2 |
| 14 | MTESMAT_REMARKS_3 | STRING | 30 | — | Remark line 3 |
| 15 | MTESMAT_REMARKS_4 | STRING | 30 | — | Remark line 4 |
| 16 | MTESMAT_REMARKS_5 | STRING | 30 | — | Remark line 5 |
| 17 | MTESMAT_SCRAP | NUMERIC | 8 | 2 | Scrap factor |
| 18 | MTESMAT_UM | STRING | 3 | — | Unit of measure |

## ESTROUT
**NOT USED**

Fields: 48

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESRO_DESC | STRING | 30 | — | Routing operation description |
| 2 | MTESRO_INSTR_1 | STRING | 60 | — | Routing instruction line 1 |
| 3 | MTESRO_INSTR_10 | STRING | 60 | — | Routing instruction line 10 |
| 4 | MTESRO_INSTR_11 | STRING | 60 | — | Routing instruction line 11 |
| 5 | MTESRO_INSTR_12 | STRING | 60 | — | Routing instruction line 12 |
| 6 | MTESRO_INSTR_13 | STRING | 60 | — | Routing instruction line 13 |
| 7 | MTESRO_INSTR_14 | STRING | 60 | — | Routing instruction line 14 |
| 8 | MTESRO_INSTR_15 | STRING | 60 | — | Routing instruction line 15 |
| 9 | MTESRO_INSTR_2 | STRING | 60 | — | Routing instruction line 2 |
| 10 | MTESRO_INSTR_3 | STRING | 60 | — | Routing instruction line 3 |
| 11 | MTESRO_INSTR_4 | STRING | 60 | — | Routing instruction line 4 |
| 12 | MTESRO_INSTR_5 | STRING | 60 | — | Routing instruction line 5 |
| 13 | MTESRO_INSTR_6 | STRING | 60 | — | Routing instruction line 6 |
| 14 | MTESRO_INSTR_7 | STRING | 60 | — | Routing instruction line 7 |
| 15 | MTESRO_INSTR_8 | STRING | 60 | — | Routing instruction line 8 |
| 16 | MTESRO_INSTR_9 | STRING | 60 | — | Routing instruction line 9 |
| 17 | MTESRO_LAB1 | NUMERIC | 8 | 4 | Estimate labor cost rate 1 |
| 18 | MTESRO_LAB2 | NUMERIC | 8 | 4 | Estimate labor cost rate 2 |
| 19 | MTESRO_LAB3 | NUMERIC | 8 | 4 | Estimate labor cost rate 3 |
| 20 | MTESRO_LAB4 | NUMERIC | 8 | 4 | Estimate labor cost rate 4 |
| 21 | MTESRO_LAB5 | NUMERIC | 8 | 4 | Estimate labor cost rate 5 |
| 22 | MTESRO_MACH1 | NUMERIC | 8 | 4 | Estimate machine cost rate 1 |
| 23 | MTESRO_MACH2 | NUMERIC | 8 | 4 | Estimate machine cost rate 2 |
| 24 | MTESRO_MACH3 | NUMERIC | 8 | 4 | Estimate machine cost rate 3 |
| 25 | MTESRO_MACH4 | NUMERIC | 8 | 4 | Estimate machine cost rate 4 |
| 26 | MTESRO_MACH5 | NUMERIC | 8 | 4 | Estimate machine cost rate 5 |
| 27 | MTESRO_MISCCOST | NUMERIC | 8 | 6 | Miscellaneous cost |
| 28 | MTESRO_MISCDESC | STRING | 30 | — | Miscellaneous cost description |
| 29 | MTESRO_OPCOST | NUMERIC | 8 | 6 | Total operation cost |
| 30 | MTESRO_OPER | STRING | 3 | — | Routing operation code |
| 31 | MTESRO_OVER1 | NUMERIC | 8 | 4 | Estimate overhead rate 1 |
| 32 | MTESRO_OVER2 | NUMERIC | 8 | 4 | Estimate overhead rate 2 |
| 33 | MTESRO_OVER3 | NUMERIC | 8 | 4 | Estimate overhead rate 3 |
| 34 | MTESRO_OVER4 | NUMERIC | 8 | 4 | Estimate overhead rate 4 |
| 35 | MTESRO_OVER5 | NUMERIC | 8 | 4 | Estimate overhead rate 5 |
| 36 | MTESRO_PARTSHR | NUMERIC | 8 | 2 | Parts shared quantity |
| 37 | MTESRO_QUOTE | NUMERIC | 8 | — | Quote/estimate number |
| 38 | MTESRO_SETUP1 | NUMERIC | 8 | 4 | Estimate setup cost 1 |
| 39 | MTESRO_SETUP2 | NUMERIC | 8 | 4 | Estimate setup cost 2 |
| 40 | MTESRO_SETUP3 | NUMERIC | 8 | 4 | Estimate setup cost 3 |
| 41 | MTESRO_SETUP4 | NUMERIC | 8 | 4 | Estimate setup cost 4 |
| 42 | MTESRO_SETUP5 | NUMERIC | 8 | 4 | Estimate setup cost 5 |
| 43 | MTESRO_SETUPHRS | NUMERIC | 8 | 2 | Estimated setup hours |
| 44 | MTESRO_TIMEPART | NUMERIC | 8 | 6 | Time per part (hours) |
| 45 | MTESRO_TYPE | STRING | 1 | — | Routing type code (I=internal/O=outside) |
| 46 | MTESRO_VENDNAME | STRING | 25 | — | Outside vendor name |
| 47 | MTESRO_VENDOR | STRING | 10 | — | Outside vendor code |
| 48 | MTESRO_WC | STRING | 12 | — | Work center code |

## ISAMRPF
**NOT USED**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_FC_CQTY | NUMERIC | 8 | 2 | Committed quantity |
| 2 | BKMRP_FC_DATE | DATE | 4 | — | Forecast date |
| 3 | BKMRP_FC_DATE1 | DATE | 4 | — | Alternate forecast date |
| 4 | BKMRP_FC_EXTRA | STRING | 25 | — | Reserved extra field |
| 5 | BKMRP_FC_FLAG | STRING | 1 | — | Forecast status flag |
| 6 | BKMRP_FC_NUM | NUMERIC | 8 | — | Forecast record number |
| 7 | BKMRP_FC_OQTY | NUMERIC | 8 | 2 | Open/unfulfilled quantity |
| 8 | BKMRP_FC_PART | STRING | 15 | — | Part/item code |
| 9 | BKMRP_FC_QTY | NUMERIC | 8 | 2 | Forecasted quantity |

## ISAPHCHG
**NOT USED**

Fields: 32

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAP_CHG_AARD | DATE | 4 | — | Before: actual receipt date |
| 2 | ISAP_CHG_ACONV | NUMERIC | 8 | 5 | Before: unit conversion factor |
| 3 | ISAP_CHG_ADISC | NUMERIC | 8 | 2 | Before: discount percent |
| 4 | ISAP_CHG_AERD | DATE | 4 | — | Before: expected receipt date |
| 5 | ISAP_CHG_AEXTRA | STRING | 150 | — | Before: extra field |
| 6 | ISAP_CHG_AGLA | STRING | 10 | — | Before: GL account |
| 7 | ISAP_CHG_AGLD | STRING | 4 | — | Before: GL department |
| 8 | ISAP_CHG_ALOC | STRING | 10 | — | Before: bin location |
| 9 | ISAP_CHG_AOOQTY | NUMERIC | 8 | 2 | Before: original order quantity |
| 10 | ISAP_CHG_AOPER | INTEGER | 2 | — | Before: routing operation |
| 11 | ISAP_CHG_APRICE | NUMERIC | 8 | 4 | Before: unit price |
| 12 | ISAP_CHG_AWOP | NUMERIC | 8 | — | Before: WO prefix |
| 13 | ISAP_CHG_AWOS | INTEGER | 2 | — | Before: WO suffix |
| 14 | ISAP_CHG_BARD | DATE | 4 | — | After: actual receipt date |
| 15 | ISAP_CHG_BCONV | NUMERIC | 8 | 5 | After: unit conversion factor |
| 16 | ISAP_CHG_BDISC | NUMERIC | 8 | 2 | After: discount percent |
| 17 | ISAP_CHG_BERD | DATE | 4 | — | After: expected receipt date |
| 18 | ISAP_CHG_BEXTRA | STRING | 150 | — | After: extra field |
| 19 | ISAP_CHG_BGLA | STRING | 10 | — | After: GL account |
| 20 | ISAP_CHG_BGLD | STRING | 4 | — | After: GL department |
| 21 | ISAP_CHG_BLOC | STRING | 10 | — | After: bin location |
| 22 | ISAP_CHG_BOOQTY | NUMERIC | 8 | 2 | After: original order quantity |
| 23 | ISAP_CHG_BOPER | INTEGER | 2 | — | After: routing operation |
| 24 | ISAP_CHG_BPRICE | NUMERIC | 8 | 4 | After: unit price |
| 25 | ISAP_CHG_BWOP | NUMERIC | 8 | — | After: WO prefix |
| 26 | ISAP_CHG_BWOS | INTEGER | 2 | — | After: WO suffix |
| 27 | ISAP_CHG_CDATE | DATE | 4 | — | Change date |
| 28 | ISAP_CHG_LINEID | INTEGER | 2 | — | PO line ID |
| 29 | ISAP_CHG_PCODE | STRING | 15 | — | Part/item code |
| 30 | ISAP_CHG_PONUM | NUMERIC | 8 | — | PO number |
| 31 | ISAP_CHG_REVLVL | STRING | 10 | — | Revision level |
| 32 | ISAP_CHG_USER | STRING | 15 | — | User who made the change |

## ISARICHG
**NOT USED**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | Before: actual ship date |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | Before: commission rate 1 |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | Before: commission rate 2 |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | Before: discount percent |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | Before: estimated ship date |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | Before: extra field |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | Before: bin location |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | Before: original order quantity |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | Before: unit price |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | After: actual ship date |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | After: commission rate 1 |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | After: commission rate 2 |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | After: discount percent |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | After: estimated ship date |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | After: extra field |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | After: bin location |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | After: original order quantity |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | After: unit price |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | Change date |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | Invoice number |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | SO line ID |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | Part/item code |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | Revision level |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | Sales order number |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | Unique sequence number |
| 26 | ISAR_CHG_USER | STRING | 15 | — | User who made the change |

## ISARINVX
**AR invoice cross-reference extension** — used by T7ESB/T7SOA/T7SOB (SO and estimate programs). Links invoices to extended reference data.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_INV_EXRTA2 | STRING | 100 | — | Extra field 2 |
| 2 | ISAR_INV_EXTRA1 | STRING | 100 | — | Extra field 1 |
| 3 | ISAR_INV_NUM | NUMERIC | 8 | — | Invoice number |
| 4 | ISAR_INV_SONUM | NUMERIC | 8 | — | Sales order number |

## ISAUTODC
**Auto data collection config** — used by T7AUTODCH/T7AUTODEJH (scheduled automatic DC batch posting programs).

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_AUTO_DATE | DATE | 4 | — | Auto-DC transaction date |
| 2 | IS_AUTO_EMP | INTEGER | 2 | — | Employee number |
| 3 | IS_AUTO_EXTRA | STRING | 100 | — | Reserved extra field |
| 4 | IS_AUTO_FILE | STRING | 8 | — | Source file code |
| 5 | IS_AUTO_FLAG | STRING | 1 | — | Status flag |
| 6 | IS_AUTO_IP | STRING | 64 | — | Client IP address |
| 7 | IS_AUTO_OPER | INTEGER | 2 | — | Routing operation number |
| 8 | IS_AUTO_PARTS | NUMERIC | 8 | 2 | Parts count/quantity |
| 9 | IS_AUTO_SHIFT | INTEGER | 2 | — | Shift number |
| 10 | IS_AUTO_TIME | TIME | 4 | — | Transaction time |
| 11 | IS_AUTO_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 12 | IS_AUTO_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISBILLSH
**NOT USED**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BILLSH_BILL | STRING | 10 | — | Bill-to customer code |
| 2 | IS_BILLSH_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_BILLSH_FLAG | STRING | 1 | — | Active flag (Y/N) |
| 4 | IS_BILLSH_SHIP | STRING | 10 | — | Ship-to customer code |

## ISBMTMP

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 10 | — | Child item type code |
| 2 | BKBM_COMPONENT | STRING | 15 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | Start effective date |
| 4 | BKBM_DATE2 | DATE | 4 | — | End effective date |
| 5 | BKBM_EST_LINE | NUMERIC | 8 | — | Estimate line number |
| 6 | BKBM_EXTRA | STRING | 50 | — | Extra |
| 7 | BKBM_P_TYPE | STRING | 10 | — | Parent item type code |
| 8 | BKBM_PARENT | STRING | 15 | — | Parent Part Code |
| 9 | BKBM_PROD_DUPOP | STRING | 1 | — | Duplicate Option blank / 1 / 2 |
| 10 | BKBM_PROD_LINE^ | INTEGER | 2 | — | Production line number |
| 11 | BKBM_PROD_OP | STRING | 3 | — | Option ( If  in second position) |
| 12 | BKBM_PROD_OPDSC | STRING | 5 | — | Operation description code |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | Operation approval flag 1 (Y/N) |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | Operation approval flag 2 (Y/N) |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | Operation approval flag 3 (Y/N) |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | Operation approval flag 4 (Y/N) |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | Operation approval flag 5 (Y/N) |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | Operation approval flag 6 (Y/N) |
| 19 | BKBM_PROD_PRICE | NUMERIC | 8 | 4 | Option Pricing |
| 20 | BKBM_PROD_RTNUM | INTEGER | 2 | — | Routing  Sequence Number |
| 21 | BKBM_PROD_SCRAP | NUMERIC | 8 | 2 | Scrap Allowance Percent |
| 22 | BKBM_PROD_TYPE | STRING | 1 | — | Part Type |
| 23 | BKBM_PROD_VEND | STRING | 10 | — | Vendor Code |
| 24 | BKBM_QTY_REQD | NUMERIC | 8 | 8 | Quantity Required |
| 25 | BKBM_REFERENCE | STRING | 20 | — | Reference |
| 26 | BKBM_REV | STRING | 5 | — | Revision (not used) |
| 27 | BKBM_UID | STRING | 20 | — | Unique identifier |

## ISBTCSB

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_INFO_AL1 | STRING | 25 | — | Serial record alpha lookup 1 |
| 2 | ISSR_INFO_AL10 | STRING | 25 | — | Serial record alpha lookup 10 |
| 3 | ISSR_INFO_AL11 | STRING | 25 | — | Serial record alpha lookup 11 |
| 4 | ISSR_INFO_AL12 | STRING | 25 | — | Serial record alpha lookup 12 |
| 5 | ISSR_INFO_AL13 | STRING | 25 | — | Serial record alpha lookup 13 |
| 6 | ISSR_INFO_AL14 | STRING | 25 | — | Serial record alpha lookup 14 |
| 7 | ISSR_INFO_AL15 | STRING | 25 | — | Serial record alpha lookup 15 |
| 8 | ISSR_INFO_AL16 | STRING | 25 | — | Serial record alpha lookup 16 |
| 9 | ISSR_INFO_AL17 | STRING | 25 | — | Serial record alpha lookup 17 |
| 10 | ISSR_INFO_AL18 | STRING | 25 | — | Serial record alpha lookup 18 |
| 11 | ISSR_INFO_AL19 | STRING | 25 | — | Serial record alpha lookup 19 |
| 12 | ISSR_INFO_AL2 | STRING | 25 | — | Serial record alpha lookup 2 |
| 13 | ISSR_INFO_AL20 | STRING | 25 | — | Serial record alpha lookup 20 |
| 14 | ISSR_INFO_AL3 | STRING | 25 | — | Serial record alpha lookup 3 |
| 15 | ISSR_INFO_AL4 | STRING | 25 | — | Serial record alpha lookup 4 |
| 16 | ISSR_INFO_AL5 | STRING | 25 | — | Serial record alpha lookup 5 |
| 17 | ISSR_INFO_AL6 | STRING | 25 | — | Serial record alpha lookup 6 |
| 18 | ISSR_INFO_AL7 | STRING | 25 | — | Serial record alpha lookup 7 |
| 19 | ISSR_INFO_AL8 | STRING | 25 | — | Serial record alpha lookup 8 |
| 20 | ISSR_INFO_AL9 | STRING | 25 | — | Serial record alpha lookup 9 |
| 21 | ISSR_INFO_ALPHA_1 | STRING | 25 | — | Serial record alpha field 1 |
| 22 | ISSR_INFO_ALPHA_10 | STRING | 25 | — | Serial record alpha field 10 |
| 23 | ISSR_INFO_ALPHA_11 | STRING | 25 | — | Serial record alpha field 11 |
| 24 | ISSR_INFO_ALPHA_12 | STRING | 25 | — | Serial record alpha field 12 |
| 25 | ISSR_INFO_ALPHA_13 | STRING | 25 | — | Serial record alpha field 13 |
| 26 | ISSR_INFO_ALPHA_14 | STRING | 25 | — | Serial record alpha field 14 |
| 27 | ISSR_INFO_ALPHA_15 | STRING | 25 | — | Serial record alpha field 15 |
| 28 | ISSR_INFO_ALPHA_16 | STRING | 25 | — | Serial record alpha field 16 |
| 29 | ISSR_INFO_ALPHA_17 | STRING | 25 | — | Serial record alpha field 17 |
| 30 | ISSR_INFO_ALPHA_18 | STRING | 25 | — | Serial record alpha field 18 |
| 31 | ISSR_INFO_ALPHA_19 | STRING | 25 | — | Serial record alpha field 19 |
| 32 | ISSR_INFO_ALPHA_2 | STRING | 25 | — | Serial record alpha field 2 |
| 33 | ISSR_INFO_ALPHA_20 | STRING | 25 | — | Serial record alpha field 20 |
| 34 | ISSR_INFO_ALPHA_3 | STRING | 25 | — | Serial record alpha field 3 |
| 35 | ISSR_INFO_ALPHA_4 | STRING | 25 | — | Serial record alpha field 4 |
| 36 | ISSR_INFO_ALPHA_5 | STRING | 25 | — | Serial record alpha field 5 |
| 37 | ISSR_INFO_ALPHA_6 | STRING | 25 | — | Serial record alpha field 6 |
| 38 | ISSR_INFO_ALPHA_7 | STRING | 25 | — | Serial record alpha field 7 |
| 39 | ISSR_INFO_ALPHA_8 | STRING | 25 | — | Serial record alpha field 8 |
| 40 | ISSR_INFO_ALPHA_9 | STRING | 25 | — | Serial record alpha field 9 |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | Item/serial code |
| 42 | ISSR_INFO_DATE1 | DATE | 4 | — | Serial record date 1 |
| 43 | ISSR_INFO_DATE2 | DATE | 4 | — | Serial record date 2 |
| 44 | ISSR_INFO_DATE3 | DATE | 4 | — | Serial record date 3 |
| 45 | ISSR_INFO_DATE4 | DATE | 4 | — | Serial record date 4 |
| 46 | ISSR_INFO_DATE5 | DATE | 4 | — | Serial record date 5 |
| 47 | ISSR_INFO_DATE_1 | DATE | 4 | — | Serial record date field 1 |
| 48 | ISSR_INFO_DATE_2 | DATE | 4 | — | Serial record date field 2 |
| 49 | ISSR_INFO_DATE_3 | DATE | 4 | — | Serial record date field 3 |
| 50 | ISSR_INFO_DATE_4 | DATE | 4 | — | Serial record date field 4 |
| 51 | ISSR_INFO_DATE_5 | DATE | 4 | — | Serial record date field 5 |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | Reserved extra field |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | Serial record number |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | Unique record ID |

## ISCCBTXN
**Corrugated/Cut box transactions** — used by J7CCFABXFER (CC Fabrication Transfer). Tracks fabric/corrugated transfer records by LOT/BIN/LOC.

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_TXN_ALPHA | STRING | 15 | — | Alpha lookup code |
| 2 | ISCC_TXN_BIN | STRING | 15 | — | Bin location |
| 3 | ISCC_TXN_EXTRA | STRING | 50 | — | Reserved extra field |
| 4 | ISCC_TXN_FABRIC | STRING | 15 | — | Fabric/cover specification code |
| 5 | ISCC_TXN_GDATE | DATE | 4 | — | Guarantee/warranty date |
| 6 | ISCC_TXN_JOB | STRING | 15 | — | Job/work order code |
| 7 | ISCC_TXN_LOC | STRING | 10 | — | Warehouse location |
| 8 | ISCC_TXN_LOT | STRING | 15 | — | Lot number |
| 9 | ISCC_TXN_LOTQTY | NUMERIC | 8 | 2 | Lot quantity |
| 10 | ISCC_TXN_NEDQTY | NUMERIC | 8 | 2 | Needed quantity |
| 11 | ISCC_TXN_PULQTY | NUMERIC | 8 | 2 | Pulled quantity |
| 12 | ISCC_TXN_SDATE | DATE | 4 | — | Ship date |
| 13 | ISCC_TXN_SER | STRING | 25 | — | Serial number |
| 14 | ISCC_TXN_STATUS | STRING | 1 | — | Transaction status flag |
| 15 | ISCC_TXN_TDATE | DATE | 4 | — | Transaction date |
| 16 | ISCC_TXN_TRANS | NUMERIC | 8 | — | Transaction number |

## ISCCICM
**Mattress cover/fabric product specification** — used by T7CCCITM (CC-C item maintenance) and J7CCITEMSYNC. Stores cover design data: fabric/ticking, fill layers (FILIT_1..4/FILQTY_1..4), cushion type, color, stripe, law label, sewing notations, SolidWorks CAD reference.

Fields: 59

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_ICM_AMTPP | STRING | 25 | — | Amount per piece |
| 2 | ISCC_ICM_BOXNO | STRING | 30 | — | Box number/identifier |
| 3 | ISCC_ICM_BOXQTY | STRING | 30 | — | Box quantity |
| 4 | ISCC_ICM_BTNCOD | STRING | 25 | — | Button code |
| 5 | ISCC_ICM_BTNQTY | NUMERIC | 8 | — | Button quantity |
| 6 | ISCC_ICM_CODE | STRING | 15 | — | Item/cover code |
| 7 | ISCC_ICM_COLLEC | STRING | 120 | — | Collection name/description |
| 8 | ISCC_ICM_CONST | STRING | 60 | — | Construction description |
| 9 | ISCC_ICM_CUBE | STRING | 30 | — | Cubic dimensions |
| 10 | ISCC_ICM_CUSFD | STRING | 60 | — | Customer fd field |
| 11 | ISCC_ICM_CUSHTY | STRING | 60 | — | Cushion type |
| 12 | ISCC_ICM_CUSITM | STRING | 60 | — | Customer item code |
| 13 | ISCC_ICM_CUSLAB | STRING | 60 | — | Customer label text |
| 14 | ISCC_ICM_CUST | STRING | 60 | — | Customer designation |
| 15 | ISCC_ICM_CVL | STRING | 25 | — | Cover version/level |
| 16 | ISCC_ICM_CWEIGH | NUMERIC | 8 | 6 | Cover weight |
| 17 | ISCC_ICM_DACLB | STRING | 60 | — | Day Act law label text |
| 18 | ISCC_ICM_DACLS | STRING | 60 | — | Day Act class spec |
| 19 | ISCC_ICM_DESC | STRING | 30 | — | Cover description line 1 |
| 20 | ISCC_ICM_DESC2 | STRING | 30 | — | Cover description line 2 |
| 21 | ISCC_ICM_EUROT | STRING | 60 | — | Euro top construction spec |
| 22 | ISCC_ICM_FABLAB | STRING | 60 | — | Fabric label specification |
| 23 | ISCC_ICM_FABRIC | STRING | 60 | — | Fabric/ticking specification |
| 24 | ISCC_ICM_FILIT_1 | STRING | 15 | — | Fill/comfort layer item code 1 |
| 25 | ISCC_ICM_FILIT_2 | STRING | 15 | — | Fill/comfort layer item code 2 |
| 26 | ISCC_ICM_FILIT_3 | STRING | 15 | — | Fill/comfort layer item code 3 |
| 27 | ISCC_ICM_FILIT_4 | STRING | 15 | — | Fill/comfort layer item code 4 |
| 28 | ISCC_ICM_FILQTY_1 | STRING | 20 | — | Fill/comfort layer quantity 1 |
| 29 | ISCC_ICM_FILQTY_2 | STRING | 20 | — | Fill/comfort layer quantity 2 |
| 30 | ISCC_ICM_FILQTY_3 | STRING | 20 | — | Fill/comfort layer quantity 3 |
| 31 | ISCC_ICM_FILQTY_4 | STRING | 20 | — | Fill/comfort layer quantity 4 |
| 32 | ISCC_ICM_FSIZE | STRING | 30 | — | Foundation size code |
| 33 | ISCC_ICM_HAVPIC | STRING | 60 | — | Has picture flag/path |
| 34 | ISCC_ICM_HINGE | STRING | 25 | — | Hinge type/code |
| 35 | ISCC_ICM_LABLOC | STRING | 60 | — | Label location spec |
| 36 | ISCC_ICM_LAWLAB | STRING | 60 | — | Law label specification |
| 37 | ISCC_ICM_MILFD | STRING | 60 | — | Military standard fd field |
| 38 | ISCC_ICM_PDF | STRING | 60 | — | PDF document path |
| 39 | ISCC_ICM_PERCOM | STRING | 25 | — | Perimeter construction |
| 40 | ISCC_ICM_PNAME | STRING | 60 | — | Product name |
| 41 | ISCC_ICM_POLY | STRING | 20 | — | Polyester content spec |
| 42 | ISCC_ICM_PRICE | STRING | 60 | — | Price information |
| 43 | ISCC_ICM_SEWNOT | STRING | 60 | — | Sewing notations |
| 44 | ISCC_ICM_SOLIDF | STRING | 25 | — | SolidWorks file reference |
| 45 | ISCC_ICM_SPY | STRING | 25 | — | Spring/platform spec |
| 46 | ISCC_ICM_SSL | STRING | 60 | — | Steel/spring law label |
| 47 | ISCC_ICM_STRIPE | STRING | 25 | — | Stripe pattern code |
| 48 | ISCC_ICM_TCOLOR | STRING | 60 | — | Ticking color description |
| 49 | ISCC_ICM_TIECOD | STRING | 25 | — | Tie code |
| 50 | ISCC_ICM_TIELEN | STRING | 25 | — | Tie length |
| 51 | ISCC_ICM_TIELOC | STRING | 60 | — | Tie location spec |
| 52 | ISCC_ICM_TIEMAT | STRING | 30 | — | Tie material |
| 53 | ISCC_ICM_TIEQTY | STRING | 20 | — | Tie quantity |
| 54 | ISCC_ICM_TIES | STRING | 10 | — | Ties configuration |
| 55 | ISCC_ICM_UVL | STRING | 25 | — | Upper version/level |
| 56 | ISCC_ICM_WELT | STRING | 60 | — | Welt/edge spec |
| 57 | ISCC_ICM_WLENG | STRING | 30 | — | Width/length spec |
| 58 | ISCC_ICM_ZIPPER | STRING | 25 | — | Zipper type/code |
| 59 | ISICC_ICM_ | STRING | 25 | — | Reserved/unnamed field |

## ISCCMTF
**Corrugated/Cut material transfer staging** — used by J7CCITEMSYNC. 2-field staging table for CC item sync operations.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_MTF_ITEM | STRING | 15 | — | Item code |
| 2 | ISCC_MTF_MTF | STRING | 60 | — | Manufacturer/fabric description |

## ISCMGRP
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISCC_MTF_ITEM | STRING | 15 | — | Item code |
| 2 | ISCC_MTF_MTF | STRING | 60 | — | Manufacturer/fabric description |

## ISCONVRT
**Unit conversion table** — used by J7RCCONVTABLE and J7RCPITEX (RC customer system). Stores per-item PUM/SUM and weight conversion factor for items needing non-standard UOM conversion.

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CONV_DATE | DATE | 4 | — | Conversion record date |
| 2 | IS_CONV_DESC | STRING | 90 | — | Conversion description |
| 3 | IS_CONV_EXTRA | STRING | 100 | — | Reserved extra field |
| 4 | IS_CONV_ITEM | STRING | 15 | — | Item code |
| 5 | IS_CONV_PCONV | NUMERIC | 8 | 6 | Primary unit conversion factor |
| 6 | IS_CONV_PUM | STRING | 10 | — | Primary unit of measure |
| 7 | IS_CONV_SCONV | NUMERIC | 8 | 6 | Secondary unit conversion factor |
| 8 | IS_CONV_SUM | STRING | 10 | — | Secondary unit of measure |
| 9 | IS_CONV_WTCONV | NUMERIC | 8 | 6 | Weight conversion factor |

## ISDCSER

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISDC_SER_ALPHA | STRING | 30 | — | Alpha lookup code |
| 2 | ISDC_SER_BIN | STRING | 15 | — | Bin location |
| 3 | ISDC_SER_DATE | DATE | 4 | — | Transaction date |
| 4 | ISDC_SER_EMP | INTEGER | 2 | — | Employee number |
| 5 | ISDC_SER_EXTRA | STRING | 100 | — | Reserved extra field |
| 6 | ISDC_SER_FLAG | STRING | 1 | — | Status flag |
| 7 | ISDC_SER_GDATE | DATE | 4 | — | Guarantee/warranty date |
| 8 | ISDC_SER_ITEM | STRING | 15 | — | Item code |
| 9 | ISDC_SER_LOC | STRING | 10 | — | Warehouse location |
| 10 | ISDC_SER_LOT | STRING | 15 | — | Lot number |
| 11 | ISDC_SER_OPER | INTEGER | 2 | — | Routing operation number |
| 12 | ISDC_SER_PARTS | NUMERIC | 8 | 2 | Parts quantity |
| 13 | ISDC_SER_QTY | NUMERIC | 8 | 2 | Quantity |
| 14 | ISDC_SER_SERIAL | STRING | 25 | — | Serial number |
| 15 | ISDC_SER_TIME | TIME | 4 | — | Transaction time |
| 16 | ISDC_SER_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 17 | ISDC_SER_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISDEPT
**Department code table** — used by T7APB/T7ARB/T7GLB/T7GLJ (AP/AR/GL programs). Department reference lookup.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_GF_DEPT | STRING | 10 | — | Department code |
| 2 | IS_GF_DEPT_DESC | STRING | 40 | — | Department description |
| 3 | IS_GF_DEPT_MISC | STRING | 100 | — | Miscellaneous/extra field |

## ISDIV
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_GF_DIV | STRING | 10 | — | Division code |
| 2 | IS_GF_DIV_DESC | STRING | 40 | — | Division description |
| 3 | IS_GF_DIV_MISC | STRING | 100 | — | Miscellaneous/extra field |

## ISDROP
**System dropdown values** — used by T7DROPDOWN and 25 other programs. Stores system-wide dropdown list options by code/type.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_DROP_CODE | STRING | 10 | — | Drop-ship code |
| 2 | IS_DROP_DESC | STRING | 30 | — | Description |
| 3 | IS_DROP_EXTRA | STRING | 50 | — | Reserved extra field |
| 4 | IS_DROP_TEXT | STRING | 30 | — | Display text |

## ISEAB
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_EAB_CONTACT | STRING | 20 | — | Contact name |
| 2 | IS_EAB_EMAIL | STRING | 30 | — | Email address |
| 3 | IS_EAB_EXTRA | STRING | 100 | — | Reserved extra field |
| 4 | IS_EAB_FNAME | STRING | 15 | — | First name |
| 5 | IS_EAB_LNAME | STRING | 15 | — | Last name |
| 6 | IS_EAB_USER | STRING | 15 | — | User code |

## ISGLFCOA
**NOT USED**

Fields: 67

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_3YPAST_1 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 1 |
| 2 | ISGL_3YPAST_10 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 10 |
| 3 | ISGL_3YPAST_11 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 11 |
| 4 | ISGL_3YPAST_12 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 12 |
| 5 | ISGL_3YPAST_13 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 13 |
| 6 | ISGL_3YPAST_14 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 14 |
| 7 | ISGL_3YPAST_2 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 2 |
| 8 | ISGL_3YPAST_3 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 3 |
| 9 | ISGL_3YPAST_4 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 4 |
| 10 | ISGL_3YPAST_5 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 5 |
| 11 | ISGL_3YPAST_6 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 6 |
| 12 | ISGL_3YPAST_7 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 7 |
| 13 | ISGL_3YPAST_8 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 8 |
| 14 | ISGL_3YPAST_9 | NUMERIC | 8 | 2 | GL account balance 3 years ago period 9 |
| 15 | ISGL_3YPAST_YE | NUMERIC | 8 | 2 | GL account year-end balance 3 years ago |
| 16 | ISGL_4YPAST_1 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 1 |
| 17 | ISGL_4YPAST_10 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 10 |
| 18 | ISGL_4YPAST_11 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 11 |
| 19 | ISGL_4YPAST_12 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 12 |
| 20 | ISGL_4YPAST_13 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 13 |
| 21 | ISGL_4YPAST_14 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 14 |
| 22 | ISGL_4YPAST_2 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 2 |
| 23 | ISGL_4YPAST_3 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 3 |
| 24 | ISGL_4YPAST_4 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 4 |
| 25 | ISGL_4YPAST_5 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 5 |
| 26 | ISGL_4YPAST_6 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 6 |
| 27 | ISGL_4YPAST_7 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 7 |
| 28 | ISGL_4YPAST_8 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 8 |
| 29 | ISGL_4YPAST_9 | NUMERIC | 8 | 2 | GL account balance 4 years ago period 9 |
| 30 | ISGL_4YPAST_YE | NUMERIC | 8 | 2 | GL account year-end balance 4 years ago |
| 31 | ISGL_5YPAST_1 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 1 |
| 32 | ISGL_5YPAST_10 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 10 |
| 33 | ISGL_5YPAST_11 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 11 |
| 34 | ISGL_5YPAST_12 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 12 |
| 35 | ISGL_5YPAST_13 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 13 |
| 36 | ISGL_5YPAST_14 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 14 |
| 37 | ISGL_5YPAST_2 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 2 |
| 38 | ISGL_5YPAST_3 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 3 |
| 39 | ISGL_5YPAST_4 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 4 |
| 40 | ISGL_5YPAST_5 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 5 |
| 41 | ISGL_5YPAST_6 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 6 |
| 42 | ISGL_5YPAST_7 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 7 |
| 43 | ISGL_5YPAST_8 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 8 |
| 44 | ISGL_5YPAST_9 | NUMERIC | 8 | 2 | GL account balance 5 years ago period 9 |
| 45 | ISGL_5YPAST_YE | NUMERIC | 8 | 2 | GL account year-end balance 5 years ago |
| 46 | ISGL_6YPAST_1 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 1 |
| 47 | ISGL_6YPAST_10 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 10 |
| 48 | ISGL_6YPAST_11 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 11 |
| 49 | ISGL_6YPAST_12 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 12 |
| 50 | ISGL_6YPAST_13 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 13 |
| 51 | ISGL_6YPAST_14 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 14 |
| 52 | ISGL_6YPAST_2 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 2 |
| 53 | ISGL_6YPAST_3 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 3 |
| 54 | ISGL_6YPAST_4 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 4 |
| 55 | ISGL_6YPAST_5 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 5 |
| 56 | ISGL_6YPAST_6 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 6 |
| 57 | ISGL_6YPAST_7 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 7 |
| 58 | ISGL_6YPAST_8 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 8 |
| 59 | ISGL_6YPAST_9 | NUMERIC | 8 | 2 | GL account balance 6 years ago period 9 |
| 60 | ISGL_6YPAST_YE | NUMERIC | 8 | 2 | GL account year-end balance 6 years ago |
| 61 | ISGL_ACCT | STRING | 10 | — | GL account code |
| 62 | ISGL_ACCTD | STRING | 25 | — | GL account description |
| 63 | ISGL_CEXTRA | STRING | 100 | — | Reserved extra field |
| 64 | ISGL_CR_DR | STRING | 1 | — | Normal balance: Credit or Debit (C/D) |
| 65 | ISGL_GLDPT | STRING | 4 | — | GL department code |
| 66 | ISGL_NON_CASH | STRING | 1 | — | Non-cash item flag (Y/N) |
| 67 | ISGL_TYPE | STRING | 1 | — | Account type code |

## ISGLNBGT
**GL next-period budget/balance** — used by T7AMB/T7AMH/T7AMQ/T7GLA (asset management and GL). Stores budget and next-period GL balances.

Fields: 35

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISGL_BGT_ACCT | STRING | 10 | — | GL account code |
| 2 | ISGL_BGT_BUD2_1 | NUMERIC | 8 | 2 | Secondary budget amount for period 1 |
| 3 | ISGL_BGT_BUD2_10 | NUMERIC | 8 | 2 | Secondary budget amount for period 10 |
| 4 | ISGL_BGT_BUD2_11 | NUMERIC | 8 | 2 | Secondary budget amount for period 11 |
| 5 | ISGL_BGT_BUD2_12 | NUMERIC | 8 | 2 | Secondary budget amount for period 12 |
| 6 | ISGL_BGT_BUD2_13 | NUMERIC | 8 | 2 | Secondary budget amount for period 13 |
| 7 | ISGL_BGT_BUD2_14 | NUMERIC | 8 | 2 | Secondary budget amount for period 14 |
| 8 | ISGL_BGT_BUD2_2 | NUMERIC | 8 | 2 | Secondary budget amount for period 2 |
| 9 | ISGL_BGT_BUD2_3 | NUMERIC | 8 | 2 | Secondary budget amount for period 3 |
| 10 | ISGL_BGT_BUD2_4 | NUMERIC | 8 | 2 | Secondary budget amount for period 4 |
| 11 | ISGL_BGT_BUD2_5 | NUMERIC | 8 | 2 | Secondary budget amount for period 5 |
| 12 | ISGL_BGT_BUD2_6 | NUMERIC | 8 | 2 | Secondary budget amount for period 6 |
| 13 | ISGL_BGT_BUD2_7 | NUMERIC | 8 | 2 | Secondary budget amount for period 7 |
| 14 | ISGL_BGT_BUD2_8 | NUMERIC | 8 | 2 | Secondary budget amount for period 8 |
| 15 | ISGL_BGT_BUD2_9 | NUMERIC | 8 | 2 | Secondary budget amount for period 9 |
| 16 | ISGL_BGT_BUDGET_1 | NUMERIC | 8 | 2 | Budget amount for period 1 |
| 17 | ISGL_BGT_BUDGET_10 | NUMERIC | 8 | 2 | Budget amount for period 10 |
| 18 | ISGL_BGT_BUDGET_11 | NUMERIC | 8 | 2 | Budget amount for period 11 |
| 19 | ISGL_BGT_BUDGET_12 | NUMERIC | 8 | 2 | Budget amount for period 12 |
| 20 | ISGL_BGT_BUDGET_13 | NUMERIC | 8 | 2 | Budget amount for period 13 |
| 21 | ISGL_BGT_BUDGET_14 | NUMERIC | 8 | 2 | Budget amount for period 14 |
| 22 | ISGL_BGT_BUDGET_2 | NUMERIC | 8 | 2 | Budget amount for period 2 |
| 23 | ISGL_BGT_BUDGET_3 | NUMERIC | 8 | 2 | Budget amount for period 3 |
| 24 | ISGL_BGT_BUDGET_4 | NUMERIC | 8 | 2 | Budget amount for period 4 |
| 25 | ISGL_BGT_BUDGET_5 | NUMERIC | 8 | 2 | Budget amount for period 5 |
| 26 | ISGL_BGT_BUDGET_6 | NUMERIC | 8 | 2 | Budget amount for period 6 |
| 27 | ISGL_BGT_BUDGET_7 | NUMERIC | 8 | 2 | Budget amount for period 7 |
| 28 | ISGL_BGT_BUDGET_8 | NUMERIC | 8 | 2 | Budget amount for period 8 |
| 29 | ISGL_BGT_BUDGET_9 | NUMERIC | 8 | 2 | Budget amount for period 9 |
| 30 | ISGL_BGT_DATE | DATE | 4 | — | Budget period start date |
| 31 | ISGL_BGT_EDATE | DATE | 4 | — | Budget period end date |
| 32 | ISGL_BGT_EXTRA | STRING | 50 | — | Reserved extra field |
| 33 | ISGL_BGT_FLAG | STRING | 1 | — | Budget record status flag |
| 34 | ISGL_BGT_GLDPT | STRING | 4 | — | GL department code |
| 35 | ISGL_BGT_WHO | STRING | 30 | — | Last modified by (user name) |

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
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | Long product code/description |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | Manufacturer code |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | Net GL last year |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | Net GL month-to-date |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | Net GL variance |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | Net GL year-to-date |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | Primary material type code |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | Turnover rate |
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
| 1 | IS_LABEL_BCOLOR_1 | STRING | 10 | — | Background color for label field 1 |
| 2 | IS_LABEL_BCOLOR_10 | STRING | 10 | — | Background color for label field 10 |
| 3 | IS_LABEL_BCOLOR_11 | STRING | 10 | — | Background color for label field 11 |
| 4 | IS_LABEL_BCOLOR_12 | STRING | 10 | — | Background color for label field 12 |
| 5 | IS_LABEL_BCOLOR_13 | STRING | 10 | — | Background color for label field 13 |
| 6 | IS_LABEL_BCOLOR_14 | STRING | 10 | — | Background color for label field 14 |
| 7 | IS_LABEL_BCOLOR_15 | STRING | 10 | — | Background color for label field 15 |
| 8 | IS_LABEL_BCOLOR_16 | STRING | 10 | — | Background color for label field 16 |
| 9 | IS_LABEL_BCOLOR_17 | STRING | 10 | — | Background color for label field 17 |
| 10 | IS_LABEL_BCOLOR_18 | STRING | 10 | — | Background color for label field 18 |
| 11 | IS_LABEL_BCOLOR_19 | STRING | 10 | — | Background color for label field 19 |
| 12 | IS_LABEL_BCOLOR_2 | STRING | 10 | — | Background color for label field 2 |
| 13 | IS_LABEL_BCOLOR_20 | STRING | 10 | — | Background color for label field 20 |
| 14 | IS_LABEL_BCOLOR_21 | STRING | 10 | — | Background color for label field 21 |
| 15 | IS_LABEL_BCOLOR_22 | STRING | 10 | — | Background color for label field 22 |
| 16 | IS_LABEL_BCOLOR_23 | STRING | 10 | — | Background color for label field 23 |
| 17 | IS_LABEL_BCOLOR_24 | STRING | 10 | — | Background color for label field 24 |
| 18 | IS_LABEL_BCOLOR_25 | STRING | 10 | — | Background color for label field 25 |
| 19 | IS_LABEL_BCOLOR_26 | STRING | 10 | — | Background color for label field 26 |
| 20 | IS_LABEL_BCOLOR_27 | STRING | 10 | — | Background color for label field 27 |
| 21 | IS_LABEL_BCOLOR_28 | STRING | 10 | — | Background color for label field 28 |
| 22 | IS_LABEL_BCOLOR_29 | STRING | 10 | — | Background color for label field 29 |
| 23 | IS_LABEL_BCOLOR_3 | STRING | 10 | — | Background color for label field 3 |
| 24 | IS_LABEL_BCOLOR_30 | STRING | 10 | — | Background color for label field 30 |
| 25 | IS_LABEL_BCOLOR_4 | STRING | 10 | — | Background color for label field 4 |
| 26 | IS_LABEL_BCOLOR_5 | STRING | 10 | — | Background color for label field 5 |
| 27 | IS_LABEL_BCOLOR_6 | STRING | 10 | — | Background color for label field 6 |
| 28 | IS_LABEL_BCOLOR_7 | STRING | 10 | — | Background color for label field 7 |
| 29 | IS_LABEL_BCOLOR_8 | STRING | 10 | — | Background color for label field 8 |
| 30 | IS_LABEL_BCOLOR_9 | STRING | 10 | — | Background color for label field 9 |
| 31 | IS_LABEL_CDATE | DATE | 4 | — | Created date |
| 32 | IS_LABEL_CUST | STRING | 10 | — | Customer code restriction |
| 33 | IS_LABEL_DESC | STRING | 30 | — | Label template description |
| 34 | IS_LABEL_DFLT | STRING | 1 | — | Default template flag (Y/N) |
| 35 | IS_LABEL_EDATE | DATE | 4 | — | Expiration date |
| 36 | IS_LABEL_EXTRA | STRING | 100 | — | Reserved extra field |
| 37 | IS_LABEL_FCOLOR_1 | STRING | 10 | — | Foreground/font color for label field 1 |
| 38 | IS_LABEL_FCOLOR_10 | STRING | 10 | — | Foreground/font color for label field 10 |
| 39 | IS_LABEL_FCOLOR_11 | STRING | 10 | — | Foreground/font color for label field 11 |
| 40 | IS_LABEL_FCOLOR_12 | STRING | 10 | — | Foreground/font color for label field 12 |
| 41 | IS_LABEL_FCOLOR_13 | STRING | 10 | — | Foreground/font color for label field 13 |
| 42 | IS_LABEL_FCOLOR_14 | STRING | 10 | — | Foreground/font color for label field 14 |
| 43 | IS_LABEL_FCOLOR_15 | STRING | 10 | — | Foreground/font color for label field 15 |
| 44 | IS_LABEL_FCOLOR_16 | STRING | 10 | — | Foreground/font color for label field 16 |
| 45 | IS_LABEL_FCOLOR_17 | STRING | 10 | — | Foreground/font color for label field 17 |
| 46 | IS_LABEL_FCOLOR_18 | STRING | 10 | — | Foreground/font color for label field 18 |
| 47 | IS_LABEL_FCOLOR_19 | STRING | 10 | — | Foreground/font color for label field 19 |
| 48 | IS_LABEL_FCOLOR_2 | STRING | 10 | — | Foreground/font color for label field 2 |
| 49 | IS_LABEL_FCOLOR_20 | STRING | 10 | — | Foreground/font color for label field 20 |
| 50 | IS_LABEL_FCOLOR_21 | STRING | 10 | — | Foreground/font color for label field 21 |
| 51 | IS_LABEL_FCOLOR_22 | STRING | 10 | — | Foreground/font color for label field 22 |
| 52 | IS_LABEL_FCOLOR_23 | STRING | 10 | — | Foreground/font color for label field 23 |
| 53 | IS_LABEL_FCOLOR_24 | STRING | 10 | — | Foreground/font color for label field 24 |
| 54 | IS_LABEL_FCOLOR_25 | STRING | 10 | — | Foreground/font color for label field 25 |
| 55 | IS_LABEL_FCOLOR_26 | STRING | 10 | — | Foreground/font color for label field 26 |
| 56 | IS_LABEL_FCOLOR_27 | STRING | 10 | — | Foreground/font color for label field 27 |
| 57 | IS_LABEL_FCOLOR_28 | STRING | 10 | — | Foreground/font color for label field 28 |
| 58 | IS_LABEL_FCOLOR_29 | STRING | 10 | — | Foreground/font color for label field 29 |
| 59 | IS_LABEL_FCOLOR_3 | STRING | 10 | — | Foreground/font color for label field 3 |
| 60 | IS_LABEL_FCOLOR_30 | STRING | 10 | — | Foreground/font color for label field 30 |
| 61 | IS_LABEL_FCOLOR_4 | STRING | 10 | — | Foreground/font color for label field 4 |
| 62 | IS_LABEL_FCOLOR_5 | STRING | 10 | — | Foreground/font color for label field 5 |
| 63 | IS_LABEL_FCOLOR_6 | STRING | 10 | — | Foreground/font color for label field 6 |
| 64 | IS_LABEL_FCOLOR_7 | STRING | 10 | — | Foreground/font color for label field 7 |
| 65 | IS_LABEL_FCOLOR_8 | STRING | 10 | — | Foreground/font color for label field 8 |
| 66 | IS_LABEL_FCOLOR_9 | STRING | 10 | — | Foreground/font color for label field 9 |
| 67 | IS_LABEL_FLAG | STRING | 1 | — | Status flag |
| 68 | IS_LABEL_ITEM | STRING | 15 | — | Item code |
| 69 | IS_LABEL_NTYPE_1 | STRING | 3 | — | Field type code for label slot 1 |
| 70 | IS_LABEL_NTYPE_10 | STRING | 3 | — | Field type code for label slot 10 |
| 71 | IS_LABEL_NTYPE_11 | STRING | 3 | — | Field type code for label slot 11 |
| 72 | IS_LABEL_NTYPE_12 | STRING | 3 | — | Field type code for label slot 12 |
| 73 | IS_LABEL_NTYPE_13 | STRING | 3 | — | Field type code for label slot 13 |
| 74 | IS_LABEL_NTYPE_14 | STRING | 3 | — | Field type code for label slot 14 |
| 75 | IS_LABEL_NTYPE_15 | STRING | 3 | — | Field type code for label slot 15 |
| 76 | IS_LABEL_NTYPE_16 | STRING | 3 | — | Field type code for label slot 16 |
| 77 | IS_LABEL_NTYPE_17 | STRING | 3 | — | Field type code for label slot 17 |
| 78 | IS_LABEL_NTYPE_18 | STRING | 3 | — | Field type code for label slot 18 |
| 79 | IS_LABEL_NTYPE_19 | STRING | 3 | — | Field type code for label slot 19 |
| 80 | IS_LABEL_NTYPE_2 | STRING | 3 | — | Field type code for label slot 2 |
| 81 | IS_LABEL_NTYPE_20 | STRING | 3 | — | Field type code for label slot 20 |
| 82 | IS_LABEL_NTYPE_21 | STRING | 3 | — | Field type code for label slot 21 |
| 83 | IS_LABEL_NTYPE_22 | STRING | 3 | — | Field type code for label slot 22 |
| 84 | IS_LABEL_NTYPE_23 | STRING | 3 | — | Field type code for label slot 23 |
| 85 | IS_LABEL_NTYPE_24 | STRING | 3 | — | Field type code for label slot 24 |
| 86 | IS_LABEL_NTYPE_25 | STRING | 3 | — | Field type code for label slot 25 |
| 87 | IS_LABEL_NTYPE_26 | STRING | 3 | — | Field type code for label slot 26 |
| 88 | IS_LABEL_NTYPE_27 | STRING | 3 | — | Field type code for label slot 27 |
| 89 | IS_LABEL_NTYPE_28 | STRING | 3 | — | Field type code for label slot 28 |
| 90 | IS_LABEL_NTYPE_29 | STRING | 3 | — | Field type code for label slot 29 |
| 91 | IS_LABEL_NTYPE_3 | STRING | 3 | — | Field type code for label slot 3 |
| 92 | IS_LABEL_NTYPE_30 | STRING | 3 | — | Field type code for label slot 30 |
| 93 | IS_LABEL_NTYPE_4 | STRING | 3 | — | Field type code for label slot 4 |
| 94 | IS_LABEL_NTYPE_5 | STRING | 3 | — | Field type code for label slot 5 |
| 95 | IS_LABEL_NTYPE_6 | STRING | 3 | — | Field type code for label slot 6 |
| 96 | IS_LABEL_NTYPE_7 | STRING | 3 | — | Field type code for label slot 7 |
| 97 | IS_LABEL_NTYPE_8 | STRING | 3 | — | Field type code for label slot 8 |
| 98 | IS_LABEL_NTYPE_9 | STRING | 3 | — | Field type code for label slot 9 |
| 99 | IS_LABEL_NUM | STRING | 15 | — | Label template number/ID |
| 100 | IS_LABEL_OBS | STRING | 1 | — | Obsolete flag (Y/N) |
| 101 | IS_LABEL_RTM | STRING | 12 | — | RTM report template filename |
| 102 | IS_LABEL_VEND | STRING | 10 | — | Vendor code restriction |

## ISLOTS
**PARENT COMPONENT LOT TO SERIAL MAP**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | Assembly date |
| 2 | IS_SER_CDESC | STRING | 30 | — | Child/component description |
| 3 | IS_SER_COMP | STRING | 15 | — | Component item code |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | Component serial number |
| 5 | IS_SER_EXRA | STRING | 100 | — | Reserved extra field |
| 6 | IS_SER_FDATE | DATE | 4 | — | Final assembly date |
| 7 | IS_SER_PARENT | STRING | 15 | — | Parent item code |
| 8 | IS_SER_PDESC | STRING | 30 | — | Parent item description |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | Parent serial number |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISLTYPE
**LINK TYPE (NOT USED)**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LT_DESC | STRING | 30 | — | Lot type description |
| 2 | IS_LT_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_LT_SEC | INTEGER | 2 | — | Security level |
| 4 | IS_LT_TYPE | STRING | 3 | — | Lot type code |

## ISPOBOX
**NOT USED**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | Box number within shipment |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | Item code |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | Pack date |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | Reserved extra field |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | Box height (inches) |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | Invoice number |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | Box length (inches) |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | SO line number |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | Lot number |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | Quantity packed |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | Serial number |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | Shipper number |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | Ship-via code |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | Skid/pallet number |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | Sales order number |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | Temporary record flag (Y/N) |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | Carrier tracking number |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | UCC-128 barcode |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | Box width (inches) |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | Box weight (lbs) |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISPOHTRK

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TRK_CDATE | DATE | 4 | — | Creation date |
| 2 | IS_TRK_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_TRK_NUM | STRING | 25 | — | Tracking number |
| 4 | IS_TRK_ORD | NUMERIC | 8 | — | Order number |
| 5 | IS_TRK_RDATE | DATE | 4 | — | Required/delivery date |
| 6 | IS_TRK_SHPVIA | STRING | 10 | — | Ship-via carrier code |
| 7 | IS_TRK_STATUS | STRING | 50 | — | Carrier tracking status |

## ISPOLOG

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISPO_LOG_DATE | DATE | 4 | — | Log entry date |
| 2 | ISPO_LOG_EMP | INTEGER | 2 | — | Employee number |
| 3 | ISPO_LOG_EXTRA | STRING | 100 | — | Reserved extra field |
| 4 | ISPO_LOG_NAME | STRING | 50 | — | User full name |
| 5 | ISPO_LOG_PONUM | NUMERIC | 8 | — | Purchase order number |
| 6 | ISPO_LOG_PRGM | STRING | 8 | — | Program that created entry |
| 7 | ISPO_LOG_REASON | STRING | 50 | — | Reason for change/cancel |
| 8 | ISPO_LOG_TIME | TIME | 4 | — | Log entry time |
| 9 | ISPO_LOG_WHO | STRING | 15 | — | User who made the change |

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
| 1 | IS_TRK_CDATE | DATE | 4 | — | Creation date |
| 2 | IS_TRK_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | IS_TRK_NUM | STRING | 25 | — | Tracking number |
| 4 | IS_TRK_ORD | NUMERIC | 8 | — | Order number |
| 5 | IS_TRK_RDATE | DATE | 4 | — | Required/delivery date |
| 6 | IS_TRK_SHPVIA | STRING | 10 | — | Ship-via carrier code |
| 7 | IS_TRK_STATUS | STRING | 50 | — | Carrier tracking status |

## ISPRESN

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PRESN_REASON | STRING | 30 | — | PO cancellation reason |

## ISREPDEF
**Report definitions** — used by T7REPDEF/EXCOM/T7SOAXCOM. Stores saved report filter configurations by program and user.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_DEF_EXTRA | STRING | 50 | — | Reserved extra field |
| 2 | ISREP_DEF_LABEL | STRING | 5 | — | Report label/code |
| 3 | ISREP_DEF_TITLE | STRING | 30 | — | Report title |

## ISRTLOAD
**Routing load runtime table** — used by T7SOA/T7SOB/T7SOB75 (SO entry programs). Loads routing cost data for outside-process operations during SO entry.

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LOAD_ALOAD | STRING | 15 | — | Auto-load code |
| 2 | IS_LOAD_BALQTY | NUMERIC | 8 | 2 | Balance quantity remaining |
| 3 | IS_LOAD_BIN | STRING | 15 | — | Bin location |
| 4 | IS_LOAD_CNTR | INTEGER | 2 | — | Load record counter |
| 5 | IS_LOAD_DATE1 | DATE | 4 | — | Load date 1 |
| 6 | IS_LOAD_DATE2 | DATE | 4 | — | Load date 2 |
| 7 | IS_LOAD_DESC | STRING | 30 | — | Load item description |
| 8 | IS_LOAD_EXTRA | STRING | 100 | — | Reserved extra field |
| 9 | IS_LOAD_ITEM | STRING | 15 | — | Item code |
| 10 | IS_LOAD_LOADNUM | NUMERIC | 8 | — | Load number |
| 11 | IS_LOAD_LOADQTY | NUMERIC | 8 | 2 | Load quantity |
| 12 | IS_LOAD_LOC | STRING | 10 | — | Warehouse location |
| 13 | IS_LOAD_LOT | STRING | 15 | — | Lot number |
| 14 | IS_LOAD_NUM2 | NUMERIC | 8 | — | Secondary reference number |
| 15 | IS_LOAD_ORDQTY | NUMERIC | 8 | 2 | Ordered quantity |
| 16 | IS_LOAD_SCANQTY | NUMERIC | 8 | 2 | Scanned/completed quantity |
| 17 | IS_LOAD_SCCOGS | NUMERIC | 8 | 4 | Shipping/cost of goods rate |
| 18 | IS_LOAD_SER | STRING | 25 | — | Serial number |
| 19 | IS_LOAD_SOLINE | STRING | 3 | — | SO line number |
| 20 | IS_LOAD_SONUM | NUMERIC | 8 | — | Sales order number |
| 21 | IS_LOAD_TRUCK | STRING | 15 | — | Truck/carrier code |

## ISRTMS
**RTM printer assignments** — used by J7CCSOLABELS/J7NMITEMRTM/J7NMRTMPRINTER. Maps items to specific RTM report templates and printers.

Fields: 29

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RTM_CONTLBL | STRING | 12 | — | Continuous label RTM template |
| 2 | IS_RTM_CUST | STRING | 10 | — | Customer code restriction |
| 3 | IS_RTM_DATE | DATE | 4 | — | Record creation date |
| 4 | IS_RTM_DESC | STRING | 30 | — | RTM mapping description |
| 5 | IS_RTM_DFLT | STRING | 1 | — | Default mapping flag (Y/N) |
| 6 | IS_RTM_EXTRA | STRING | 100 | — | Reserved extra field |
| 7 | IS_RTM_FLAG | STRING | 1 | — | Status flag |
| 8 | IS_RTM_ITEM | STRING | 15 | — | Item code |
| 9 | IS_RTM_MISCLBL1 | STRING | 12 | — | Miscellaneous label 1 RTM template |
| 10 | IS_RTM_MISCLBL2 | STRING | 12 | — | Miscellaneous label 2 RTM template |
| 11 | IS_RTM_MISCLBL3 | STRING | 12 | — | Miscellaneous label 3 RTM template |
| 12 | IS_RTM_MIXEDLBL | STRING | 12 | — | Mixed pallet label RTM template |
| 13 | IS_RTM_PARTLBL | STRING | 12 | — | Part label RTM template |
| 14 | IS_RTM_PRINTER_1 | STRING | 90 | — | Printer path/name for RTM slot 1 |
| 15 | IS_RTM_PRINTER_10 | STRING | 90 | — | Printer path/name for RTM slot 10 |
| 16 | IS_RTM_PRINTER_2 | STRING | 90 | — | Printer path/name for RTM slot 2 |
| 17 | IS_RTM_PRINTER_3 | STRING | 90 | — | Printer path/name for RTM slot 3 |
| 18 | IS_RTM_PRINTER_4 | STRING | 90 | — | Printer path/name for RTM slot 4 |
| 19 | IS_RTM_PRINTER_5 | STRING | 90 | — | Printer path/name for RTM slot 5 |
| 20 | IS_RTM_PRINTER_6 | STRING | 90 | — | Printer path/name for RTM slot 6 |
| 21 | IS_RTM_PRINTER_7 | STRING | 90 | — | Printer path/name for RTM slot 7 |
| 22 | IS_RTM_PRINTER_8 | STRING | 90 | — | Printer path/name for RTM slot 8 |
| 23 | IS_RTM_PRINTER_9 | STRING | 90 | — | Printer path/name for RTM slot 9 |
| 24 | IS_RTM_PROGRAM | STRING | 15 | — | Program/module code |
| 25 | IS_RTM_QTY | INTEGER | 2 | — | Default print quantity |
| 26 | IS_RTM_QUICKLBL | STRING | 12 | — | Quick label RTM template |
| 27 | IS_RTM_RTM | STRING | 12 | — | Default RTM template filename |
| 28 | IS_RTM_SHIPLBL | STRING | 12 | — | Shipping label RTM template |
| 29 | IS_RTM_VEND | STRING | 10 | — | Vendor code restriction |

## ISSCOMP
**SPC component specifications** — used by T7SCOMP/T7SPC. Statistical Process Control; defines which components/features are inspected per process.

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SCOMP | STRING | 50 | — | Complaint description |
| 2 | IS_SCOMP_COMPND | STRING | 30 | — | Complainant name |
| 3 | IS_SCOMP_DETAIL | STRING | 20 | — | Complaint detail code |
| 4 | IS_SCOMP_VIS | STRING | 1 | — | Visible flag (Y/N) |
| 5 | IS_SCOMP_WHO | STRING | 40 | — | Who logged complaint |

## ISSDET
**SPC detail measurements** — used by T7SDET/T7SPC/T7SPCLIVEGRID. Stores individual measurement readings per SPC inspection sample.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SDET_DETAIL | STRING | 20 | — | Detail code |
| 2 | IS_SDET_SUB | STRING | 1 | — | Sub-detail flag |
| 3 | IS_SDET_TYPE | STRING | 20 | — | Detail type code |
| 4 | IS_SDET_WHO | STRING | 40 | — | Who entered record |

## ISSEPROC
**SPC process definitions** — used by T7SEPROC/T7SPC. Defines SPC measurement processes with control limits and specifications.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SEPROC_PROC | STRING | 25 | — | Process code |
| 2 | IS_SEPROC_WHO | STRING | 40 | — | Owner/department |

## ISSEQUIP
**NOT USED**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SEQUIP_DESC | STRING | 40 | — | Equipment description |
| 2 | IS_SEQUIP_NAME | STRING | 20 | — | Equipment name/code |

## ISSERR
**SPC error/defect records** — used by T7SPC/T7SPCLIVEGRID/T7SPCREP. Records defect events with error code, process, quantity, and WO reference.

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SERR_ADIAG | STRING | 1000 | — | Appended diagnosis text |
| 2 | IS_SERR_ADOF | STRING | 1000 | — | Appended defect-of text |
| 3 | IS_SERR_AREWORK | STRING | 1000 | — | Appended rework instructions |
| 4 | IS_SERR_COUNT | INTEGER | 2 | — | Error count |
| 5 | IS_SERR_DATE | DATE | 4 | — | Error logged date |
| 6 | IS_SERR_DIAG | STRING | 0 | — | Diagnosis notes (memo) |
| 7 | IS_SERR_DOF | STRING | 0 | — | Defect-of notes (memo) |
| 8 | IS_SERR_ERROR | STRING | 25 | — | Error type code |
| 9 | IS_SERR_EXTRA | STRING | 50 | — | Reserved extra field |
| 10 | IS_SERR_OPER | INTEGER | 2 | — | Routing operation number |
| 11 | IS_SERR_PROCESS | STRING | 25 | — | Process code |
| 12 | IS_SERR_REF | STRING | 50 | — | Reference (serial, lot, or order) |
| 13 | IS_SERR_REWORK | STRING | 0 | — | Rework instructions (memo) |
| 14 | IS_SERR_SERIAL | STRING | 20 | — | Serial number |
| 15 | IS_SERR_TIME | TIME | 4 | — | Error logged time |
| 16 | IS_SERR_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 17 | IS_SERR_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISSETYPE
**SPC error/event type codes** — used by T7SETYPE/T7SPC/T7SPCREP. Defines categories of defects (error types) for SPC classification.

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SETYPE_ERR | STRING | 25 | — | Error type code |
| 2 | IS_SETYPE_WHO | STRING | 40 | — | Owner/department |

## ISSHIPA
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SHPA_CODE | STRING | 10 | — | Shipping API code |
| 2 | IS_SHPA_EXTRA | STRING | 50 | — | Reserved extra field |
| 3 | IS_SHPA_PASS | STRING | 30 | — | API password |
| 4 | IS_SHPA_TOKEN | STRING | 30 | — | API authentication token |
| 5 | IS_SHPA_USER | STRING | 30 | — | API username |

## ISSMTCFG
**SM time configuration** — used by T7SMTEND/T7SMTSET. Stores scheduling time-slot configuration for the SM scheduling module.

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SMT_CAP | INTEGER | 2 | — | Machine capacity |
| 2 | IS_SMT_CNTR | INTEGER | 2 | — | Counter |
| 3 | IS_SMT_COMP | STRING | 15 | — | Component item code |
| 4 | IS_SMT_CURRENT | STRING | 1 | — | Currently active flag (Y/N) |
| 5 | IS_SMT_DATE | DATE | 4 | — | Transaction date |
| 6 | IS_SMT_EMP | STRING | 4 | — | Employee code |
| 7 | IS_SMT_EXTRA | STRING | 50 | — | Reserved extra field |
| 8 | IS_SMT_LOT | STRING | 15 | — | Lot number |
| 9 | IS_SMT_MACHINE | STRING | 4 | — | Machine code |
| 10 | IS_SMT_OPER | STRING | 3 | — | Operation code |
| 11 | IS_SMT_REEL | INTEGER | 2 | — | Reel/feeder slot number |
| 12 | IS_SMT_RQTY | NUMERIC | 8 | 4 | Remaining quantity on reel |
| 13 | IS_SMT_TIME | TIME | 4 | — | Transaction time |
| 14 | IS_SMT_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 15 | IS_SMT_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISSNOTES
**NOT USED**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_NOTE_ALPHA | STRING | 6000 | — | Note text (long string field) |
| 2 | IS_NOTE_CDATE | DATE | 4 | — | Created date |
| 3 | IS_NOTE_CONTACT | STRING | 30 | — | Contact name |
| 4 | IS_NOTE_CTIME | STRING | 10 | — | Created time |
| 5 | IS_NOTE_CWHO | STRING | 15 | — | Created by user |
| 6 | IS_NOTE_EDATE | DATE | 4 | — | Edited date |
| 7 | IS_NOTE_ETIME | STRING | 10 | — | Edited time |
| 8 | IS_NOTE_EWHO | STRING | 15 | — | Edited by user |
| 9 | IS_NOTE_EXTRA | STRING | 100 | — | Reserved extra field |
| 10 | IS_NOTE_GROUP | STRING | 4 | — | Note group/category |
| 11 | IS_NOTE_ID | STRING | 48 | — | Entity ID (customer, order, etc.) |
| 12 | IS_NOTE_NOTE | STRING | 0 | — | Note text (memo field) |
| 13 | IS_NOTE_PRIVATE | STRING | 1 | — | Private note flag (Y/N) |
| 14 | IS_NOTE_TYPE | STRING | 3 | — | Note type code |

## ISSPC
**SPC master records** — used by T7SPC/T7SPCLIVEGRID/T7ROJA. Master SPC measurement log: WO/Sequence/Inspector/Employee/Accepted/Rework/Scrap qtys.

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SPC_ANOTES | STRING | 1000 | — | Appended notes text |
| 2 | IS_SPC_CUST | STRING | 10 | — | Customer code |
| 3 | IS_SPC_DATE | DATE | 4 | — | Sample date |
| 4 | IS_SPC_DETAIL | STRING | 20 | — | Detail type code |
| 5 | IS_SPC_EMPNUM | INTEGER | 2 | — | Employee number |
| 6 | IS_SPC_EXTRA | STRING | 100 | — | Reserved extra field |
| 7 | IS_SPC_GOOD | INTEGER | 2 | — | Good units count |
| 8 | IS_SPC_NOTES | STRING | 0 | — | Notes (memo field) |
| 9 | IS_SPC_OPER | INTEGER | 2 | — | Routing operation number |
| 10 | IS_SPC_PART | STRING | 15 | — | Part/item code |
| 11 | IS_SPC_REWORK | INTEGER | 2 | — | Rework units count |
| 12 | IS_SPC_SIDE | STRING | 1 | — | Board/panel side (A/B) |
| 13 | IS_SPC_TESTE_1 | STRING | 60 | — | Test equipment entry 1 |
| 14 | IS_SPC_TESTE_2 | STRING | 60 | — | Test equipment entry 2 |
| 15 | IS_SPC_TESTE_3 | STRING | 60 | — | Test equipment entry 3 |
| 16 | IS_SPC_TESTR | STRING | 1 | — | Test result flag (P/F) |
| 17 | IS_SPC_TESTT | STRING | 30 | — | Test type description |
| 18 | IS_SPC_TIME | TIME | 4 | — | Sample time |
| 19 | IS_SPC_TYPE | STRING | 20 | — | Sample type description |
| 20 | IS_SPC_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 21 | IS_SPC_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISSTEQUI
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | Asset/equipment type code |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | Type description |
| 3 | IS_STYPE_WHO | STRING | 40 | — | Owner/department |

## ISSTRACK
**SPC session tracking** — used by T7SPC. Audit trail for SPC data entry sessions.

Fields: 13

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STRACK_AR | STRING | 1 | — | A/R related flag (Y/N) |
| 2 | IS_STRACK_CLOT | STRING | 15 | — | Child lot number |
| 3 | IS_STRACK_COMP | STRING | 15 | — | Component item code |
| 4 | IS_STRACK_CSER | STRING | 20 | — | Component serial number |
| 5 | IS_STRACK_DATE | DATE | 4 | — | Tracking date |
| 6 | IS_STRACK_EXTRA | STRING | 50 | — | Reserved extra field |
| 7 | IS_STRACK_NOTE | STRING | 1000 | — | Tracking note |
| 8 | IS_STRACK_OPER | INTEGER | 2 | — | Routing operation |
| 9 | IS_STRACK_PROC | STRING | 25 | — | Process code |
| 10 | IS_STRACK_PSER | STRING | 20 | — | Parent serial number |
| 11 | IS_STRACK_TIME | TIME | 4 | — | Tracking time |
| 12 | IS_STRACK_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 13 | IS_STRACK_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISSTTYPE
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | Asset/equipment type code |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | Type description |
| 3 | IS_STYPE_WHO | STRING | 40 | — | Owner/department |

## ISSTYPE
**SPC/general type codes** — used by T7GENAED/T7GENGET/T7SDET/T7SERR. General event type codes shared between SPC and QC modules.

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_STYPE_ASSET | STRING | 25 | — | Asset/equipment type code |
| 2 | IS_STYPE_TYPE | STRING | 60 | — | Type description |
| 3 | IS_STYPE_WHO | STRING | 40 | — | Owner/department |

## ISTOOLOG
**NOT USED**

Fields: 34

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISTOOL_ACTHRS | NUMERIC | 8 | 1 | Actual hours on tool |
| 2 | ISTOOL_ALPHA_1 | STRING | 30 | — | Tool log alpha field 1 |
| 3 | ISTOOL_ALPHA_2 | STRING | 30 | — | Tool log alpha field 2 |
| 4 | ISTOOL_ALPHA_3 | STRING | 30 | — | Tool log alpha field 3 |
| 5 | ISTOOL_ALPHA_4 | STRING | 30 | — | Tool log alpha field 4 |
| 6 | ISTOOL_ALPHA_5 | STRING | 30 | — | Tool log alpha field 5 |
| 7 | ISTOOL_COST | NUMERIC | 8 | 2 | Tool maintenance cost |
| 8 | ISTOOL_DATE | DATE | 4 | — | Log entry date |
| 9 | ISTOOL_DATES_1 | DATE | 4 | — | Tool log date 1 |
| 10 | ISTOOL_DATES_2 | DATE | 4 | — | Tool log date 2 |
| 11 | ISTOOL_DATES_3 | DATE | 4 | — | Tool log date 3 |
| 12 | ISTOOL_EMP | INTEGER | 2 | — | Employee number |
| 13 | ISTOOL_ESTHRS | NUMERIC | 8 | 1 | Estimated hours on tool |
| 14 | ISTOOL_EXTRA | STRING | 100 | — | Reserved extra field |
| 15 | ISTOOL_FLAG_1 | STRING | 1 | — | Tool log flag 1 |
| 16 | ISTOOL_FLAG_2 | STRING | 1 | — | Tool log flag 2 |
| 17 | ISTOOL_FLAG_3 | STRING | 1 | — | Tool log flag 3 |
| 18 | ISTOOL_ITEM | STRING | 15 | — | Tool item code |
| 19 | ISTOOL_LOGNUM | NUMERIC | 8 | — | Log entry number |
| 20 | ISTOOL_NOTES_1 | STRING | 60 | — | Tool log note line 1 |
| 21 | ISTOOL_NOTES_10 | STRING | 60 | — | Tool log note line 10 |
| 22 | ISTOOL_NOTES_2 | STRING | 60 | — | Tool log note line 2 |
| 23 | ISTOOL_NOTES_3 | STRING | 60 | — | Tool log note line 3 |
| 24 | ISTOOL_NOTES_4 | STRING | 60 | — | Tool log note line 4 |
| 25 | ISTOOL_NOTES_5 | STRING | 60 | — | Tool log note line 5 |
| 26 | ISTOOL_NOTES_6 | STRING | 60 | — | Tool log note line 6 |
| 27 | ISTOOL_NOTES_7 | STRING | 60 | — | Tool log note line 7 |
| 28 | ISTOOL_NOTES_8 | STRING | 60 | — | Tool log note line 8 |
| 29 | ISTOOL_NOTES_9 | STRING | 60 | — | Tool log note line 9 |
| 30 | ISTOOL_OPER | INTEGER | 2 | — | Routing operation |
| 31 | ISTOOL_TOOL | STRING | 15 | — | Tool code |
| 32 | ISTOOL_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 33 | ISTOOL_WORKDESC | STRING | 60 | — | Work description |
| 34 | ISTOOL_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISUSAGE
**Item usage history** — used by T7INA/T7INAS/T7INF/T7INP (IN programs). Tracks per-item usage metrics and consumption history.

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISTS_USE_AMT_1 | NUMERIC | 8 | 2 | Item usage dollar amount for period 1 |
| 2 | ISTS_USE_AMT_10 | NUMERIC | 8 | 2 | Item usage dollar amount for period 10 |
| 3 | ISTS_USE_AMT_11 | NUMERIC | 8 | 2 | Item usage dollar amount for period 11 |
| 4 | ISTS_USE_AMT_12 | NUMERIC | 8 | 2 | Item usage dollar amount for period 12 |
| 5 | ISTS_USE_AMT_13 | NUMERIC | 8 | 2 | Item usage dollar amount for period 13 |
| 6 | ISTS_USE_AMT_14 | NUMERIC | 8 | 2 | Item usage dollar amount for period 14 |
| 7 | ISTS_USE_AMT_15 | NUMERIC | 8 | 2 | Item usage dollar amount for period 15 |
| 8 | ISTS_USE_AMT_16 | NUMERIC | 8 | 2 | Item usage dollar amount for period 16 |
| 9 | ISTS_USE_AMT_17 | NUMERIC | 8 | 2 | Item usage dollar amount for period 17 |
| 10 | ISTS_USE_AMT_18 | NUMERIC | 8 | 2 | Item usage dollar amount for period 18 |
| 11 | ISTS_USE_AMT_19 | NUMERIC | 8 | 2 | Item usage dollar amount for period 19 |
| 12 | ISTS_USE_AMT_2 | NUMERIC | 8 | 2 | Item usage dollar amount for period 2 |
| 13 | ISTS_USE_AMT_20 | NUMERIC | 8 | 2 | Item usage dollar amount for period 20 |
| 14 | ISTS_USE_AMT_21 | NUMERIC | 8 | 2 | Item usage dollar amount for period 21 |
| 15 | ISTS_USE_AMT_22 | NUMERIC | 8 | 2 | Item usage dollar amount for period 22 |
| 16 | ISTS_USE_AMT_23 | NUMERIC | 8 | 2 | Item usage dollar amount for period 23 |
| 17 | ISTS_USE_AMT_24 | NUMERIC | 8 | 2 | Item usage dollar amount for period 24 |
| 18 | ISTS_USE_AMT_25 | NUMERIC | 8 | 2 | Item usage dollar amount for period 25 |
| 19 | ISTS_USE_AMT_26 | NUMERIC | 8 | 2 | Item usage dollar amount for period 26 |
| 20 | ISTS_USE_AMT_3 | NUMERIC | 8 | 2 | Item usage dollar amount for period 3 |
| 21 | ISTS_USE_AMT_4 | NUMERIC | 8 | 2 | Item usage dollar amount for period 4 |
| 22 | ISTS_USE_AMT_5 | NUMERIC | 8 | 2 | Item usage dollar amount for period 5 |
| 23 | ISTS_USE_AMT_6 | NUMERIC | 8 | 2 | Item usage dollar amount for period 6 |
| 24 | ISTS_USE_AMT_7 | NUMERIC | 8 | 2 | Item usage dollar amount for period 7 |
| 25 | ISTS_USE_AMT_8 | NUMERIC | 8 | 2 | Item usage dollar amount for period 8 |
| 26 | ISTS_USE_AMT_9 | NUMERIC | 8 | 2 | Item usage dollar amount for period 9 |
| 27 | ISTS_USE_CODE | STRING | 15 | — | Item/part code |
| 28 | ISTS_USE_QTY_1 | NUMERIC | 8 | 2 | Item usage quantity for period 1 |
| 29 | ISTS_USE_QTY_10 | NUMERIC | 8 | 2 | Item usage quantity for period 10 |
| 30 | ISTS_USE_QTY_11 | NUMERIC | 8 | 2 | Item usage quantity for period 11 |
| 31 | ISTS_USE_QTY_12 | NUMERIC | 8 | 2 | Item usage quantity for period 12 |
| 32 | ISTS_USE_QTY_13 | NUMERIC | 8 | 2 | Item usage quantity for period 13 |
| 33 | ISTS_USE_QTY_14 | NUMERIC | 8 | 2 | Item usage quantity for period 14 |
| 34 | ISTS_USE_QTY_15 | NUMERIC | 8 | 2 | Item usage quantity for period 15 |
| 35 | ISTS_USE_QTY_16 | NUMERIC | 8 | 2 | Item usage quantity for period 16 |
| 36 | ISTS_USE_QTY_17 | NUMERIC | 8 | 2 | Item usage quantity for period 17 |
| 37 | ISTS_USE_QTY_18 | NUMERIC | 8 | 2 | Item usage quantity for period 18 |
| 38 | ISTS_USE_QTY_19 | NUMERIC | 8 | 2 | Item usage quantity for period 19 |
| 39 | ISTS_USE_QTY_2 | NUMERIC | 8 | 2 | Item usage quantity for period 2 |
| 40 | ISTS_USE_QTY_20 | NUMERIC | 8 | 2 | Item usage quantity for period 20 |
| 41 | ISTS_USE_QTY_21 | NUMERIC | 8 | 2 | Item usage quantity for period 21 |
| 42 | ISTS_USE_QTY_22 | NUMERIC | 8 | 2 | Item usage quantity for period 22 |
| 43 | ISTS_USE_QTY_23 | NUMERIC | 8 | 2 | Item usage quantity for period 23 |
| 44 | ISTS_USE_QTY_24 | NUMERIC | 8 | 2 | Item usage quantity for period 24 |
| 45 | ISTS_USE_QTY_25 | NUMERIC | 8 | 2 | Item usage quantity for period 25 |
| 46 | ISTS_USE_QTY_26 | NUMERIC | 8 | 2 | Item usage quantity for period 26 |
| 47 | ISTS_USE_QTY_3 | NUMERIC | 8 | 2 | Item usage quantity for period 3 |
| 48 | ISTS_USE_QTY_4 | NUMERIC | 8 | 2 | Item usage quantity for period 4 |
| 49 | ISTS_USE_QTY_5 | NUMERIC | 8 | 2 | Item usage quantity for period 5 |
| 50 | ISTS_USE_QTY_6 | NUMERIC | 8 | 2 | Item usage quantity for period 6 |
| 51 | ISTS_USE_QTY_7 | NUMERIC | 8 | 2 | Item usage quantity for period 7 |
| 52 | ISTS_USE_QTY_8 | NUMERIC | 8 | 2 | Item usage quantity for period 8 |
| 53 | ISTS_USE_QTY_9 | NUMERIC | 8 | 2 | Item usage quantity for period 9 |
| 54 | ISTS_USE_TYPE | STRING | 1 | — | Usage record type code |

## ISVAR
**NOT USED**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_VAR_ADD1 | STRING | 30 | — | Address line 1 |
| 2 | IS_VAR_ADD2 | STRING | 30 | — | Address line 2 |
| 3 | IS_VAR_CITY | STRING | 20 | — | City |
| 4 | IS_VAR_COMPANY | STRING | 30 | — | Company name |
| 5 | IS_VAR_CONTACT | STRING | 30 | — | Primary contact name |
| 6 | IS_VAR_EMAIL1_1 | STRING | 50 | — | Email address 1 |
| 7 | IS_VAR_EMAIL1_2 | STRING | 50 | — | Email address 2 |
| 8 | IS_VAR_EMAIL1_3 | STRING | 50 | — | Email address 3 |
| 9 | IS_VAR_EMAIL1_4 | STRING | 50 | — | Email address 4 |
| 10 | IS_VAR_EMAIL1_5 | STRING | 50 | — | Email address 5 |
| 11 | IS_VAR_EXTRA | STRING | 150 | — | Reserved extra field |
| 12 | IS_VAR_LOGO | STRING | 256 | — | Path to company logo file |
| 13 | IS_VAR_STATE | STRING | 2 | — | State code |
| 14 | IS_VAR_WEB | STRING | 100 | — | Company website URL |
| 15 | IS_VAR_WEBSUP | STRING | 100 | — | Support website URL |
| 16 | IS_VAR_WEBUPD | STRING | 100 | — | Update/download website URL |
| 17 | IS_VAR_ZIP | STRING | 8 | — | Zip/postal code |

## JGPITEMS
**Physical inventory items (legacy)** — used by T7ING/T7INH/T7INI/T7INJ. JG-era physical inventory item records (86 fields). PI count storage.

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JGP_ALLERGEN_1 | STRING | 100 | — | Allergen declaration line 1 |
| 2 | JGP_ALLERGEN_2 | STRING | 100 | — | Allergen declaration line 2 |
| 3 | JGP_ALLERGEN_3 | STRING | 100 | — | Allergen declaration line 3 |
| 4 | JGP_ALLERGEN_4 | STRING | 100 | — | Allergen declaration line 4 |
| 5 | JGP_ALLERGEN_5 | STRING | 100 | — | Allergen declaration line 5 |
| 6 | JGP_ALLERGEN_6 | STRING | 100 | — | Allergen declaration line 6 |
| 7 | JGP_ALLERGEN_7 | STRING | 100 | — | Allergen declaration line 7 |
| 8 | JGP_ALLERGEN_8 | STRING | 100 | — | Allergen declaration line 8 |
| 9 | JGP_ALLERGEN_9 | STRING | 100 | — | Allergen declaration line 9 |
| 10 | JGP_ASTM | STRING | 1 | — | ASTM standard applicable flag (Y/N) |
| 11 | JGP_C_OF_ORIGIN | STRING | 30 | — | Country of origin |
| 12 | JGP_CATALOG | STRING | 750 | — | Catalog description / text block |
| 13 | JGP_CERT_1 | STRING | 100 | — | Certification code/statement 1 |
| 14 | JGP_CERT_2 | STRING | 100 | — | Certification code/statement 2 |
| 15 | JGP_CERT_3 | STRING | 100 | — | Certification code/statement 3 |
| 16 | JGP_CERT_4 | STRING | 100 | — | Certification code/statement 4 |
| 17 | JGP_CERT_5 | STRING | 100 | — | Certification code/statement 5 |
| 18 | JGP_CERT_6 | STRING | 100 | — | Certification code/statement 6 |
| 19 | JGP_CERT_7 | STRING | 100 | — | Certification code/statement 7 |
| 20 | JGP_CERT_8 | STRING | 100 | — | Certification code/statement 8 |
| 21 | JGP_CERT_9 | STRING | 100 | — | Certification code/statement 9 |
| 22 | JGP_EXTRA | STRING | 100 | — | Reserved extra field |
| 23 | JGP_GEN_ALPHA_1 | STRING | 15 | — | Generic alpha field 1 |
| 24 | JGP_GEN_ALPHA_2 | STRING | 15 | — | Generic alpha field 2 |
| 25 | JGP_GEN_ALPHA_3 | STRING | 15 | — | Generic alpha field 3 |
| 26 | JGP_GEN_ALPHA_4 | STRING | 15 | — | Generic alpha field 4 |
| 27 | JGP_GEN_ALPHA_5 | STRING | 15 | — | Generic alpha field 5 |
| 28 | JGP_GEN_DATE_1 | DATE | 4 | — | Generic date field 1 |
| 29 | JGP_GEN_DATE_2 | DATE | 4 | — | Generic date field 2 |
| 30 | JGP_GEN_DATE_3 | DATE | 4 | — | Generic date field 3 |
| 31 | JGP_GEN_DATE_4 | DATE | 4 | — | Generic date field 4 |
| 32 | JGP_GEN_DATE_5 | DATE | 4 | — | Generic date field 5 |
| 33 | JGP_GEN_FLAG_1 | STRING | 1 | — | Generic flag 1 (Y/N) |
| 34 | JGP_GEN_FLAG_2 | STRING | 1 | — | Generic flag 2 (Y/N) |
| 35 | JGP_GEN_FLAG_3 | STRING | 1 | — | Generic flag 3 (Y/N) |
| 36 | JGP_GEN_FLAG_4 | STRING | 1 | — | Generic flag 4 (Y/N) |
| 37 | JGP_GEN_FLAG_5 | STRING | 1 | — | Generic flag 5 (Y/N) |
| 38 | JGP_GEN_NUM | NUMERIC | 8 | — | Generic numeric field |
| 39 | JGP_IND_CUBE | NUMERIC | 8 | 4 | Individual unit cubic volume |
| 40 | JGP_IND_D | NUMERIC | 8 | 4 | Individual unit depth |
| 41 | JGP_IND_H | NUMERIC | 8 | 4 | Individual unit height |
| 42 | JGP_IND_UPC | STRING | 13 | — | Individual unit UPC barcode |
| 43 | JGP_IND_W | NUMERIC | 8 | 4 | Individual unit width |
| 44 | JGP_IND_WT | NUMERIC | 8 | 4 | Individual unit weight |
| 45 | JGP_ISBN | STRING | 17 | — | ISBN number (if applicable) |
| 46 | JGP_ITEM | STRING | 15 | — | Item/part code |
| 47 | JGP_LITEM | STRING | 30 | — | Long item description |
| 48 | JGP_LOCATION1 | STRING | 10 | — | Inventory bin location 1 |
| 49 | JGP_LOCATION2 | STRING | 10 | — | Inventory bin location 2 |
| 50 | JGP_LOCATION3 | STRING | 10 | — | Inventory bin location 3 |
| 51 | JGP_LONG_DESC | STRING | 750 | — | Long/extended item description |
| 52 | JGP_MC_BARCODE | STRING | 14 | — | Master carton barcode |
| 53 | JGP_MC_QTY | NUMERIC | 8 | 2 | Master carton quantity |
| 54 | JGP_MCART_CUBE | NUMERIC | 8 | 4 | Master carton cubic volume |
| 55 | JGP_MCART_D | NUMERIC | 8 | 4 | Master carton depth |
| 56 | JGP_MCART_H | NUMERIC | 8 | 4 | Master carton height |
| 57 | JGP_MCART_W | NUMERIC | 8 | 4 | Master carton width |
| 58 | JGP_MCART_WT | NUMERIC | 8 | 4 | Master carton weight |
| 59 | JGP_MIN_AGE | INTEGER | 2 | — | Minimum age requirement (years) |
| 60 | JGP_NET_ACOST | NUMERIC | 8 | 2 | Net actual cost |
| 61 | JGP_NET_COST | STRING | 1 | — | Net cost flag |
| 62 | JGP_PAL_BARCODE | STRING | 14 | — | Pallet barcode |
| 63 | JGP_PAL_QTY | NUMERIC | 8 | 2 | Pallet quantity |
| 64 | JGP_PALLET_CUBE | NUMERIC | 8 | 4 | Pallet cubic volume |
| 65 | JGP_PALLET_D | NUMERIC | 8 | 4 | Pallet depth |
| 66 | JGP_PALLET_H | NUMERIC | 8 | 4 | Pallet height |
| 67 | JGP_PALLET_W | NUMERIC | 8 | 4 | Pallet width |
| 68 | JGP_PALLET_WT | NUMERIC | 8 | 4 | Pallet weight |
| 69 | JGP_PREF_CRIT | STRING | 1 | — | Preferred vendor criteria flag |
| 70 | JGP_PRODUCER | STRING | 1 | — | Producer flag |
| 71 | JGP_REVDT_BACK | STRING | 4 | — | Revision date (back of label) |
| 72 | JGP_REVDT_FRONT | STRING | 4 | — | Revision date (front of label) |
| 73 | JGP_SP_BARCODE | STRING | 14 | — | Shipping pack barcode |
| 74 | JGP_SP_QTY | NUMERIC | 8 | 2 | Shipping pack quantity |
| 75 | JGP_SPACK_CUBE | NUMERIC | 8 | 4 | Shipping pack cubic volume |
| 76 | JGP_SPACK_D | NUMERIC | 8 | 4 | Shipping pack depth |
| 77 | JGP_SPACK_H | NUMERIC | 8 | 4 | Shipping pack height |
| 78 | JGP_SPACK_W | NUMERIC | 8 | 4 | Shipping pack width |
| 79 | JGP_SPACK_WT | NUMERIC | 8 | 4 | Shipping pack weight |
| 80 | JGP_TARRIF_CODE | STRING | 15 | — | Tariff/HTS code |
| 81 | JGP_UOM_CUBE | NUMERIC | 8 | 4 | UOM unit cubic volume |
| 82 | JGP_UOM_D | NUMERIC | 8 | 4 | UOM unit depth |
| 83 | JGP_UOM_H | NUMERIC | 8 | 4 | UOM unit height |
| 84 | JGP_UOM_UPC | STRING | 13 | — | UOM unit UPC barcode |
| 85 | JGP_UOM_W | NUMERIC | 8 | 4 | UOM unit width |
| 86 | JGP_UOM_WT | NUMERIC | 8 | 4 | UOM unit weight |

## JSPCNLCD
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JSP_CNLCD_CDATE | DATE | 4 | — | Created date |
| 2 | JSP_CNLCD_CODE | STRING | 1 | — | Cancel reason code |
| 3 | JSP_CNLCD_DESC | STRING | 30 | — | Cancel reason description |
| 4 | JSP_CNLCD_EXTRA | STRING | 100 | — | Reserved extra field |
| 5 | JSP_CNLCD_LCODE | STRING | 10 | — | Long reason code |
| 6 | JSP_CNLCD_WHO | STRING | 20 | — | Created by user |

## JSPCNLSO
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | JSP_CNLSO_CDATE | DATE | 4 | — | Cancel date |
| 2 | JSP_CNLSO_CQTY | NUMERIC | 8 | 2 | Cancelled quantity |
| 3 | JSP_CNLSO_CTIME | TIME | 4 | — | Cancel time |
| 4 | JSP_CNLSO_CUST | STRING | 10 | — | Customer code |
| 5 | JSP_CNLSO_EXTRA | STRING | 100 | — | Reserved extra field |
| 6 | JSP_CNLSO_FLAG | STRING | 1 | — | Status flag |
| 7 | JSP_CNLSO_GDATE | DATE | 4 | — | Guarantee date |
| 8 | JSP_CNLSO_ITEM | STRING | 15 | — | Item code |
| 9 | JSP_CNLSO_SONUM | NUMERIC | 8 | — | Sales order number |
| 10 | JSP_CNLSO_STAT | STRING | 1 | — | Order status code |
| 11 | JSP_CNLSO_UNUM | NUMERIC | 8 | 4 | Unit number |
| 12 | JSP_CNLSO_WHO | STRING | 20 | — | Cancelled by user |

## MENUFILE
**NOT USED**

Fields: 108

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MENU_CODE | STRING | 4 | — | Menu identifier code |
| 2 | MENU_ESCAPE | STRING | 4 | — | Escape/back menu code |
| 3 | MENU_LEFT | STRING | 4 | — | Left arrow navigation menu code |
| 4 | MENU_LINES_1 | STRING | 30 | — | Menu display text for line 1 |
| 5 | MENU_LINES_10 | STRING | 30 | — | Menu display text for line 10 |
| 6 | MENU_LINES_11 | STRING | 30 | — | Menu display text for line 11 |
| 7 | MENU_LINES_12 | STRING | 30 | — | Menu display text for line 12 |
| 8 | MENU_LINES_13 | STRING | 30 | — | Menu display text for line 13 |
| 9 | MENU_LINES_14 | STRING | 30 | — | Menu display text for line 14 |
| 10 | MENU_LINES_15 | STRING | 30 | — | Menu display text for line 15 |
| 11 | MENU_LINES_16 | STRING | 30 | — | Menu display text for line 16 |
| 12 | MENU_LINES_17 | STRING | 30 | — | Menu display text for line 17 |
| 13 | MENU_LINES_18 | STRING | 30 | — | Menu display text for line 18 |
| 14 | MENU_LINES_19 | STRING | 30 | — | Menu display text for line 19 |
| 15 | MENU_LINES_2 | STRING | 30 | — | Menu display text for line 2 |
| 16 | MENU_LINES_20 | STRING | 30 | — | Menu display text for line 20 |
| 17 | MENU_LINES_3 | STRING | 30 | — | Menu display text for line 3 |
| 18 | MENU_LINES_4 | STRING | 30 | — | Menu display text for line 4 |
| 19 | MENU_LINES_5 | STRING | 30 | — | Menu display text for line 5 |
| 20 | MENU_LINES_6 | STRING | 30 | — | Menu display text for line 6 |
| 21 | MENU_LINES_7 | STRING | 30 | — | Menu display text for line 7 |
| 22 | MENU_LINES_8 | STRING | 30 | — | Menu display text for line 8 |
| 23 | MENU_LINES_9 | STRING | 30 | — | Menu display text for line 9 |
| 24 | MENU_LL_COL | INTEGER | 2 | — | Lower-left display column position |
| 25 | MENU_LL_ROW | INTEGER | 2 | — | Lower-left display row position |
| 26 | MENU_NAMES_1 | STRING | 4 | — | Menu item program name/code for slot 1 |
| 27 | MENU_NAMES_10 | STRING | 4 | — | Menu item program name/code for slot 10 |
| 28 | MENU_NAMES_11 | STRING | 4 | — | Menu item program name/code for slot 11 |
| 29 | MENU_NAMES_12 | STRING | 4 | — | Menu item program name/code for slot 12 |
| 30 | MENU_NAMES_13 | STRING | 4 | — | Menu item program name/code for slot 13 |
| 31 | MENU_NAMES_14 | STRING | 4 | — | Menu item program name/code for slot 14 |
| 32 | MENU_NAMES_15 | STRING | 4 | — | Menu item program name/code for slot 15 |
| 33 | MENU_NAMES_16 | STRING | 4 | — | Menu item program name/code for slot 16 |
| 34 | MENU_NAMES_17 | STRING | 4 | — | Menu item program name/code for slot 17 |
| 35 | MENU_NAMES_18 | STRING | 4 | — | Menu item program name/code for slot 18 |
| 36 | MENU_NAMES_19 | STRING | 4 | — | Menu item program name/code for slot 19 |
| 37 | MENU_NAMES_2 | STRING | 4 | — | Menu item program name/code for slot 2 |
| 38 | MENU_NAMES_20 | STRING | 4 | — | Menu item program name/code for slot 20 |
| 39 | MENU_NAMES_3 | STRING | 4 | — | Menu item program name/code for slot 3 |
| 40 | MENU_NAMES_4 | STRING | 4 | — | Menu item program name/code for slot 4 |
| 41 | MENU_NAMES_5 | STRING | 4 | — | Menu item program name/code for slot 5 |
| 42 | MENU_NAMES_6 | STRING | 4 | — | Menu item program name/code for slot 6 |
| 43 | MENU_NAMES_7 | STRING | 4 | — | Menu item program name/code for slot 7 |
| 44 | MENU_NAMES_8 | STRING | 4 | — | Menu item program name/code for slot 8 |
| 45 | MENU_NAMES_9 | STRING | 4 | — | Menu item program name/code for slot 9 |
| 46 | MENU_OPTIONS_1 | STRING | 1 | — | Menu option character for slot 1 |
| 47 | MENU_OPTIONS_10 | STRING | 1 | — | Menu option character for slot 10 |
| 48 | MENU_OPTIONS_11 | STRING | 1 | — | Menu option character for slot 11 |
| 49 | MENU_OPTIONS_12 | STRING | 1 | — | Menu option character for slot 12 |
| 50 | MENU_OPTIONS_13 | STRING | 1 | — | Menu option character for slot 13 |
| 51 | MENU_OPTIONS_14 | STRING | 1 | — | Menu option character for slot 14 |
| 52 | MENU_OPTIONS_15 | STRING | 1 | — | Menu option character for slot 15 |
| 53 | MENU_OPTIONS_16 | STRING | 1 | — | Menu option character for slot 16 |
| 54 | MENU_OPTIONS_17 | STRING | 1 | — | Menu option character for slot 17 |
| 55 | MENU_OPTIONS_18 | STRING | 1 | — | Menu option character for slot 18 |
| 56 | MENU_OPTIONS_19 | STRING | 1 | — | Menu option character for slot 19 |
| 57 | MENU_OPTIONS_2 | STRING | 1 | — | Menu option character for slot 2 |
| 58 | MENU_OPTIONS_20 | STRING | 1 | — | Menu option character for slot 20 |
| 59 | MENU_OPTIONS_3 | STRING | 1 | — | Menu option character for slot 3 |
| 60 | MENU_OPTIONS_4 | STRING | 1 | — | Menu option character for slot 4 |
| 61 | MENU_OPTIONS_5 | STRING | 1 | — | Menu option character for slot 5 |
| 62 | MENU_OPTIONS_6 | STRING | 1 | — | Menu option character for slot 6 |
| 63 | MENU_OPTIONS_7 | STRING | 1 | — | Menu option character for slot 7 |
| 64 | MENU_OPTIONS_8 | STRING | 1 | — | Menu option character for slot 8 |
| 65 | MENU_OPTIONS_9 | STRING | 1 | — | Menu option character for slot 9 |
| 66 | MENU_PROG_1 | STRING | 8 | — | Program file to run for menu slot 1 |
| 67 | MENU_PROG_10 | STRING | 8 | — | Program file to run for menu slot 10 |
| 68 | MENU_PROG_11 | STRING | 8 | — | Program file to run for menu slot 11 |
| 69 | MENU_PROG_12 | STRING | 8 | — | Program file to run for menu slot 12 |
| 70 | MENU_PROG_13 | STRING | 8 | — | Program file to run for menu slot 13 |
| 71 | MENU_PROG_14 | STRING | 8 | — | Program file to run for menu slot 14 |
| 72 | MENU_PROG_15 | STRING | 8 | — | Program file to run for menu slot 15 |
| 73 | MENU_PROG_16 | STRING | 8 | — | Program file to run for menu slot 16 |
| 74 | MENU_PROG_17 | STRING | 8 | — | Program file to run for menu slot 17 |
| 75 | MENU_PROG_18 | STRING | 8 | — | Program file to run for menu slot 18 |
| 76 | MENU_PROG_19 | STRING | 8 | — | Program file to run for menu slot 19 |
| 77 | MENU_PROG_2 | STRING | 8 | — | Program file to run for menu slot 2 |
| 78 | MENU_PROG_20 | STRING | 8 | — | Program file to run for menu slot 20 |
| 79 | MENU_PROG_3 | STRING | 8 | — | Program file to run for menu slot 3 |
| 80 | MENU_PROG_4 | STRING | 8 | — | Program file to run for menu slot 4 |
| 81 | MENU_PROG_5 | STRING | 8 | — | Program file to run for menu slot 5 |
| 82 | MENU_PROG_6 | STRING | 8 | — | Program file to run for menu slot 6 |
| 83 | MENU_PROG_7 | STRING | 8 | — | Program file to run for menu slot 7 |
| 84 | MENU_PROG_8 | STRING | 8 | — | Program file to run for menu slot 8 |
| 85 | MENU_PROG_9 | STRING | 8 | — | Program file to run for menu slot 9 |
| 86 | MENU_RIGHT | STRING | 4 | — | Right arrow navigation menu code |
| 87 | MENU_TITLE | STRING | 30 | — | Menu title text |
| 88 | MENU_TYPES_1 | STRING | 1 | — | Item type code for menu slot 1 |
| 89 | MENU_TYPES_10 | STRING | 1 | — | Item type code for menu slot 10 |
| 90 | MENU_TYPES_11 | STRING | 1 | — | Item type code for menu slot 11 |
| 91 | MENU_TYPES_12 | STRING | 1 | — | Item type code for menu slot 12 |
| 92 | MENU_TYPES_13 | STRING | 1 | — | Item type code for menu slot 13 |
| 93 | MENU_TYPES_14 | STRING | 1 | — | Item type code for menu slot 14 |
| 94 | MENU_TYPES_15 | STRING | 1 | — | Item type code for menu slot 15 |
| 95 | MENU_TYPES_16 | STRING | 1 | — | Item type code for menu slot 16 |
| 96 | MENU_TYPES_17 | STRING | 1 | — | Item type code for menu slot 17 |
| 97 | MENU_TYPES_18 | STRING | 1 | — | Item type code for menu slot 18 |
| 98 | MENU_TYPES_19 | STRING | 1 | — | Item type code for menu slot 19 |
| 99 | MENU_TYPES_2 | STRING | 1 | — | Item type code for menu slot 2 |
| 100 | MENU_TYPES_20 | STRING | 1 | — | Item type code for menu slot 20 |
| 101 | MENU_TYPES_3 | STRING | 1 | — | Item type code for menu slot 3 |
| 102 | MENU_TYPES_4 | STRING | 1 | — | Item type code for menu slot 4 |
| 103 | MENU_TYPES_5 | STRING | 1 | — | Item type code for menu slot 5 |
| 104 | MENU_TYPES_6 | STRING | 1 | — | Item type code for menu slot 6 |
| 105 | MENU_TYPES_7 | STRING | 1 | — | Item type code for menu slot 7 |
| 106 | MENU_TYPES_8 | STRING | 1 | — | Item type code for menu slot 8 |
| 107 | MENU_TYPES_9 | STRING | 1 | — | Item type code for menu slot 9 |
| 108 | MENU_WIDTH | INTEGER | 2 | — | Menu display width (columns) |

## MKASSIGN
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKASSIGN_ACCT | STRING | 10 | — | Account/customer code |
| 2 | MKASSIGN_NXTDAT | DATE | 4 | — | Next contact date |
| 3 | MKASSIGN_NXTSEQ | INTEGER | 2 | — | Next sequence step |
| 4 | MKASSIGN_PRCODE | NUMERIC | 8 | — | Price code |
| 5 | MKASSIGN_SALEND | DATE | 4 | — | Sale end date |
| 6 | MKASSIGN_TRACK | NUMERIC | 8 | — | Track/campaign number |

## MKDEF
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKDEF_CALENDAR | STRING | 1 | — | Calendar type code |
| 2 | MKDEF_ECNEXTID | NUMERIC | 8 | — | Next event class ID |
| 3 | MKDEF_ENEXTID | NUMERIC | 8 | — | Next event ID |
| 4 | MKDEF_FNEXTID | NUMERIC | 8 | — | Next form ID |
| 5 | MKDEF_FUCODE | STRING | 3 | — | Follow-up code |
| 6 | MKDEF_HISTORYCD | STRING | 2 | — | History code |
| 7 | MKDEF_PRICECD | NUMERIC | 8 | — | Default price code number |
| 8 | MKDEF_REQUIRE | STRING | 1 | — | Required fields flag (Y/N) |
| 9 | MKDEF_TCNEXTID | NUMERIC | 8 | — | Next tracking class ID |
| 10 | MKDEF_TNEXTID | NUMERIC | 8 | — | Next track ID |
| 11 | MKDEF_TRACK | NUMERIC | 8 | — | Active track number |

## MKEVENT
**NOT USED**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKEVENT_ACTIVE | STRING | 1 | — | Active flag (Y/N) |
| 2 | MKEVENT_CLASS | NUMERIC | 8 | — | Event class number |
| 3 | MKEVENT_DESC | STRING | 45 | — | Event description |
| 4 | MKEVENT_FORM | NUMERIC | 8 | — | Associated form number |
| 5 | MKEVENT_FUCODE | STRING | 3 | — | Follow-up code |
| 6 | MKEVENT_GENNAME | STRING | 45 | — | Generated event name |
| 7 | MKEVENT_HISTCD | STRING | 2 | — | History code |
| 8 | MKEVENT_MEDIA | STRING | 1 | — | Media type code |
| 9 | MKEVENT_NUM | NUMERIC | 8 | — | Event number |
| 10 | MKEVENT_REM1 | STRING | 60 | — | Remark line 1 |
| 11 | MKEVENT_REM2 | STRING | 60 | — | Remark line 2 |
| 12 | MKEVENT_SENDTO | INTEGER | 2 | — | Send-to employee number |

## MKFORM
**NOT USED**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKFORM_ACTIVE | STRING | 1 | — | Active flag (Y/N) |
| 2 | MKFORM_ATT | STRING | 25 | — | Attention/contact |
| 3 | MKFORM_DESC | STRING | 45 | — | Form description |
| 4 | MKFORM_FILE | STRING | 25 | — | Form file name |
| 5 | MKFORM_MEDIA | STRING | 1 | — | Media type code |
| 6 | MKFORM_NUM | NUMERIC | 8 | — | Form number |

## MKTCLASS
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTCLASS_ACTIVE | STRING | 1 | — | Active flag (Y/N) |
| 2 | MKTCLASS_CLASS | STRING | 45 | — | Tracking class description |
| 3 | MKTCLASS_NUM | NUMERIC | 8 | — | Tracking class number |

## MKTNOTE
**NOT USED**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKNOTE_TEXT | STRING | 70 | — | Note text line |
| 2 | MKTNOTE_LINE | INTEGER | 2 | — | Note line number |
| 3 | MKTNOTE_TRACK | NUMERIC | 8 | — | Track number |

## MKTRACK
**MK tracking** — used by T7GLJ (GL journal). Tracks GL journal entries for MK module transactions.

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTRACK_ACTIVE | STRING | 1 | — | Active flag (Y/N) |
| 2 | MKTRACK_CLASS | NUMERIC | 8 | — | Tracking class number |
| 3 | MKTRACK_DESC | STRING | 45 | — | Track description |
| 4 | MKTRACK_NUM | NUMERIC | 8 | — | Track number |

## MKTROUT
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MKTROUT_DAYSNXT | INTEGER | 2 | — | Days until next step |
| 2 | MKTROUT_EVENT | NUMERIC | 8 | — | Event number to trigger |
| 3 | MKTROUT_FIXED | STRING | 1 | — | Fixed date flag (Y/N) |
| 4 | MKTROUT_JUMP | STRING | 1 | — | Jump to sequence flag (Y/N) |
| 5 | MKTROUT_NEXTSEQ | INTEGER | 2 | — | Next sequence number to jump to |
| 6 | MKTROUT_PRICECD | NUMERIC | 8 | — | Price code |
| 7 | MKTROUT_SALEBEG | STRING | 1 | — | Mark sale begin flag (Y/N) |
| 8 | MKTROUT_SALECLO | STRING | 1 | — | Mark sale close flag (Y/N) |
| 9 | MKTROUT_SALELEN | INTEGER | 2 | — | Sale cycle length (days) |
| 10 | MKTROUT_SEQ | INTEGER | 2 | — | Sequence number |
| 11 | MKTROUT_TRACK | NUMERIC | 8 | — | Track number |

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
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | Freight amount per unit |
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
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | Option pricing method code |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | Replacement cost for cost tier 1 |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | Replacement cost for cost tier 10 |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | Replacement cost for cost tier 11 |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | Replacement cost for cost tier 12 |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | Replacement cost for cost tier 13 |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | Replacement cost for cost tier 14 |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | Replacement cost for cost tier 15 |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | Replacement cost for cost tier 2 |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | Replacement cost for cost tier 3 |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | Replacement cost for cost tier 4 |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | Replacement cost for cost tier 5 |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | Replacement cost for cost tier 6 |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | Replacement cost for cost tier 7 |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | Replacement cost for cost tier 8 |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | Replacement cost for cost tier 9 |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | Item specification line 1 |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | Item specification line 10 |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | Item specification line 11 |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | Item specification line 12 |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | Item specification line 2 |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | Item specification line 3 |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | Item specification line 4 |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | Item specification line 5 |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | Item specification line 6 |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | Item specification line 7 |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | Item specification line 8 |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | Item specification line 9 |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | Substitute item code 1 |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | Substitute item code 2 |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | Substitute item code 3 |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | Substitute item code 4 |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | Substitute item code 5 |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | Preferred vendor code 1 |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | Preferred vendor code 10 |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | Preferred vendor code 2 |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | Preferred vendor code 3 |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | Preferred vendor code 4 |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | Preferred vendor code 5 |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | Preferred vendor code 6 |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | Preferred vendor code 7 |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | Preferred vendor code 8 |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | Preferred vendor code 9 |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | Vendor 1 name |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | Vendor 10 name |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | Vendor 2 name |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | Vendor 3 name |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | Vendor 4 name |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | Vendor 5 name |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | Vendor 6 name |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | Vendor 7 name |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | Vendor 8 name |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | Vendor 9 name |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | Vendor 1 part code |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | Vendor 2 part code |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | Vendor 3 part code |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | Vendor 4 part code |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | Vendor 5 part code |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | Vendor 6 part code |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | Vendor 7 part code |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | Vendor 8 part code |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | Vendor 9 part code |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## MWOPTEMP
**NOT USED**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MWOP_CNTR | NUMERIC | 8 | — | Counter/sequence number |
| 2 | MWOP_EXTRA | STRING | 100 | — | Reserved extra field |
| 3 | MWOP_QTYCOM | NUMERIC | 8 | 2 | Quantity completed |
| 4 | MWOP_SERIAL | STRING | 25 | — | Serial number |
| 5 | MWOP_SRC | INTEGER | 2 | — | Source code |
| 6 | MWOP_STATUS | STRING | 10 | — | Work order status |
| 7 | MWOP_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 8 | MWOP_WOSUF | INTEGER | 2 | — | Work order suffix |

## NZITPRE
**NOT USED**

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | NZ_IPRE_DESC_1 | STRING | 30 | — | Item number prefix 1 description |
| 2 | NZ_IPRE_DESC_10 | STRING | 30 | — | Item number prefix 10 description |
| 3 | NZ_IPRE_DESC_11 | STRING | 30 | — | Item number prefix 11 description |
| 4 | NZ_IPRE_DESC_12 | STRING | 30 | — | Item number prefix 12 description |
| 5 | NZ_IPRE_DESC_13 | STRING | 30 | — | Item number prefix 13 description |
| 6 | NZ_IPRE_DESC_14 | STRING | 30 | — | Item number prefix 14 description |
| 7 | NZ_IPRE_DESC_15 | STRING | 30 | — | Item number prefix 15 description |
| 8 | NZ_IPRE_DESC_16 | STRING | 30 | — | Item number prefix 16 description |
| 9 | NZ_IPRE_DESC_17 | STRING | 30 | — | Item number prefix 17 description |
| 10 | NZ_IPRE_DESC_18 | STRING | 30 | — | Item number prefix 18 description |
| 11 | NZ_IPRE_DESC_2 | STRING | 30 | — | Item number prefix 2 description |
| 12 | NZ_IPRE_DESC_3 | STRING | 30 | — | Item number prefix 3 description |
| 13 | NZ_IPRE_DESC_4 | STRING | 30 | — | Item number prefix 4 description |
| 14 | NZ_IPRE_DESC_5 | STRING | 30 | — | Item number prefix 5 description |
| 15 | NZ_IPRE_DESC_6 | STRING | 30 | — | Item number prefix 6 description |
| 16 | NZ_IPRE_DESC_7 | STRING | 30 | — | Item number prefix 7 description |
| 17 | NZ_IPRE_DESC_8 | STRING | 30 | — | Item number prefix 8 description |
| 18 | NZ_IPRE_DESC_9 | STRING | 30 | — | Item number prefix 9 description |
| 19 | NZ_IPRE_NXTNUM_1 | NUMERIC | 8 | — | Next sequential item number for prefix 1 |
| 20 | NZ_IPRE_NXTNUM_10 | NUMERIC | 8 | — | Next sequential item number for prefix 10 |
| 21 | NZ_IPRE_NXTNUM_11 | NUMERIC | 8 | — | Next sequential item number for prefix 11 |
| 22 | NZ_IPRE_NXTNUM_12 | NUMERIC | 8 | — | Next sequential item number for prefix 12 |
| 23 | NZ_IPRE_NXTNUM_13 | NUMERIC | 8 | — | Next sequential item number for prefix 13 |
| 24 | NZ_IPRE_NXTNUM_14 | NUMERIC | 8 | — | Next sequential item number for prefix 14 |
| 25 | NZ_IPRE_NXTNUM_15 | NUMERIC | 8 | — | Next sequential item number for prefix 15 |
| 26 | NZ_IPRE_NXTNUM_16 | NUMERIC | 8 | — | Next sequential item number for prefix 16 |
| 27 | NZ_IPRE_NXTNUM_17 | NUMERIC | 8 | — | Next sequential item number for prefix 17 |
| 28 | NZ_IPRE_NXTNUM_18 | NUMERIC | 8 | — | Next sequential item number for prefix 18 |
| 29 | NZ_IPRE_NXTNUM_2 | NUMERIC | 8 | — | Next sequential item number for prefix 2 |
| 30 | NZ_IPRE_NXTNUM_3 | NUMERIC | 8 | — | Next sequential item number for prefix 3 |
| 31 | NZ_IPRE_NXTNUM_4 | NUMERIC | 8 | — | Next sequential item number for prefix 4 |
| 32 | NZ_IPRE_NXTNUM_5 | NUMERIC | 8 | — | Next sequential item number for prefix 5 |
| 33 | NZ_IPRE_NXTNUM_6 | NUMERIC | 8 | — | Next sequential item number for prefix 6 |
| 34 | NZ_IPRE_NXTNUM_7 | NUMERIC | 8 | — | Next sequential item number for prefix 7 |
| 35 | NZ_IPRE_NXTNUM_8 | NUMERIC | 8 | — | Next sequential item number for prefix 8 |
| 36 | NZ_IPRE_NXTNUM_9 | NUMERIC | 8 | — | Next sequential item number for prefix 9 |
| 37 | NZ_IPRE_PREFIX_1 | NUMERIC | 8 | — | Item number prefix value for slot 1 |
| 38 | NZ_IPRE_PREFIX_10 | NUMERIC | 8 | — | Item number prefix value for slot 10 |
| 39 | NZ_IPRE_PREFIX_11 | NUMERIC | 8 | — | Item number prefix value for slot 11 |
| 40 | NZ_IPRE_PREFIX_12 | NUMERIC | 8 | — | Item number prefix value for slot 12 |
| 41 | NZ_IPRE_PREFIX_13 | NUMERIC | 8 | — | Item number prefix value for slot 13 |
| 42 | NZ_IPRE_PREFIX_14 | NUMERIC | 8 | — | Item number prefix value for slot 14 |
| 43 | NZ_IPRE_PREFIX_15 | NUMERIC | 8 | — | Item number prefix value for slot 15 |
| 44 | NZ_IPRE_PREFIX_16 | NUMERIC | 8 | — | Item number prefix value for slot 16 |
| 45 | NZ_IPRE_PREFIX_17 | NUMERIC | 8 | — | Item number prefix value for slot 17 |
| 46 | NZ_IPRE_PREFIX_18 | NUMERIC | 8 | — | Item number prefix value for slot 18 |
| 47 | NZ_IPRE_PREFIX_2 | NUMERIC | 8 | — | Item number prefix value for slot 2 |
| 48 | NZ_IPRE_PREFIX_3 | NUMERIC | 8 | — | Item number prefix value for slot 3 |
| 49 | NZ_IPRE_PREFIX_4 | NUMERIC | 8 | — | Item number prefix value for slot 4 |
| 50 | NZ_IPRE_PREFIX_5 | NUMERIC | 8 | — | Item number prefix value for slot 5 |
| 51 | NZ_IPRE_PREFIX_6 | NUMERIC | 8 | — | Item number prefix value for slot 6 |
| 52 | NZ_IPRE_PREFIX_7 | NUMERIC | 8 | — | Item number prefix value for slot 7 |
| 53 | NZ_IPRE_PREFIX_8 | NUMERIC | 8 | — | Item number prefix value for slot 8 |
| 54 | NZ_IPRE_PREFIX_9 | NUMERIC | 8 | — | Item number prefix value for slot 9 |

## OPQCDESC
**Operation QC descriptions** — used by T7DCA/T7DCALABEL/T7ADCA (DC programs). QC description text per routing operation for the DC workstation display.

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | OPQC_DATE | DATE | 4 | — | QC inspection date |
| 2 | OPQC_DESC | STRING | 30 | — | QC description |
| 3 | OPQC_EXTRA | STRING | 50 | — | Reserved extra field |
| 4 | OPQC_OPER | INTEGER | 2 | — | Routing operation number |
| 5 | OPQC_QCCODE | STRING | 2 | — | QC result code |
| 6 | OPQC_QTY | NUMERIC | 8 | 2 | Inspected quantity |
| 7 | OPQC_SERIAL | STRING | 25 | — | Serial number |
| 8 | OPQC_UID | STRING | 30 | — | Unique ID |
| 9 | OPQC_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 10 | OPQC_WOSUF | INTEGER | 2 | — | Work order suffix |

## SUMCUST
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMCUST_COGS | NUMERIC | 8 | 4 | COGS for period |
| 2 | SUMCUST_CUST | STRING | 10 | — | Customer code |
| 3 | SUMCUST_MONTH | INTEGER | 2 | — | Month (1-12) |
| 4 | SUMCUST_SALES | NUMERIC | 8 | 4 | Sales amount for period |
| 5 | SUMCUST_YEAR | INTEGER | 2 | — | Year (2-digit) |

## SUMINV
**NOT USED**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMINV_DOL_ADJ | NUMERIC | 8 | 4 | Dollar amount of adjustments |
| 2 | SUMINV_DOL_FILL | NUMERIC | 8 | 4 | Dollar amount filled/shipped |
| 3 | SUMINV_DOL_ISS | NUMERIC | 8 | 4 | Dollar amount issued to WO |
| 4 | SUMINV_DOL_RSTK | NUMERIC | 8 | 4 | Dollar amount restocked |
| 5 | SUMINV_DOL_RWIP | NUMERIC | 8 | 4 | Dollar amount reversed WIP |
| 6 | SUMINV_DOL_SHPC | NUMERIC | 8 | 4 | Dollar amount shipped/customer |
| 7 | SUMINV_DOL_SHPS | NUMERIC | 8 | 4 | Dollar amount shipped/stock |
| 8 | SUMINV_DOL_WORC | NUMERIC | 8 | 4 | Dollar amount WO receipts |
| 9 | SUMINV_LOCATION | STRING | 10 | — | Warehouse location |
| 10 | SUMINV_MONTH | INTEGER | 2 | — | Month (1-12) |
| 11 | SUMINV_PARTNO | STRING | 15 | — | Part/item code |
| 12 | SUMINV_UN_ADJ | NUMERIC | 8 | 2 | Units adjusted |
| 13 | SUMINV_UN_FILL | NUMERIC | 8 | 2 | Units filled/shipped |
| 14 | SUMINV_UN_ISS | NUMERIC | 8 | 2 | Units issued to WO |
| 15 | SUMINV_UN_RSTK | NUMERIC | 8 | 2 | Units restocked |
| 16 | SUMINV_UN_RWIP | NUMERIC | 8 | 2 | Units reversed WIP |
| 17 | SUMINV_UN_SHPS | NUMERIC | 8 | 2 | Units shipped/stock |
| 18 | SUMINV_UN_WORC | NUMERIC | 8 | 2 | Units WO receipts |
| 19 | SUMINV_YEAR | INTEGER | 2 | — | Year (2-digit) |

## SUMWC
**NOT USED**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMWC_LABOR | NUMERIC | 8 | 2 | Labor hours for period |
| 2 | SUMWC_MONTH | INTEGER | 2 | — | Month (1-12) |
| 3 | SUMWC_SCRAP | NUMERIC | 8 | 2 | Scrap quantity for period |
| 4 | SUMWC_SETUP | NUMERIC | 8 | 2 | Setup hours for period |
| 5 | SUMWC_UNITS | NUMERIC | 8 | 2 | Units produced for period |
| 6 | SUMWC_WORKCTR | STRING | 12 | — | Work center code |
| 7 | SUMWC_YEAR | INTEGER | 2 | — | Year (2-digit) |

## TEMPOLD
**Used for**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCM_ACTD_CODE | STRING | 10 | — | Contact Code |
| 2 | BKCM_ACTD_DATE | DATE | 4 | — | Date |
| 3 | BKCM_ACTD_DCODE | STRING | 2 | — | Date Code |
| 4 | BKCM_ACTD_EXTRA | STRING | 100 | — | Activity extra detail field |

## TESTARRA
**NOT USED**

Fields: 101

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TARRAY_1 | STRING | 1 | — | Test array slot 1 (not used) |
| 2 | TARRAY_10 | STRING | 1 | — | Test array slot 10 (not used) |
| 3 | TARRAY_100 | STRING | 1 | — | Test array slot 100 (not used) |
| 4 | TARRAY_11 | STRING | 1 | — | Test array slot 11 (not used) |
| 5 | TARRAY_12 | STRING | 1 | — | Test array slot 12 (not used) |
| 6 | TARRAY_13 | STRING | 1 | — | Test array slot 13 (not used) |
| 7 | TARRAY_14 | STRING | 1 | — | Test array slot 14 (not used) |
| 8 | TARRAY_15 | STRING | 1 | — | Test array slot 15 (not used) |
| 9 | TARRAY_16 | STRING | 1 | — | Test array slot 16 (not used) |
| 10 | TARRAY_17 | STRING | 1 | — | Test array slot 17 (not used) |
| 11 | TARRAY_18 | STRING | 1 | — | Test array slot 18 (not used) |
| 12 | TARRAY_19 | STRING | 1 | — | Test array slot 19 (not used) |
| 13 | TARRAY_2 | STRING | 1 | — | Test array slot 2 (not used) |
| 14 | TARRAY_20 | STRING | 1 | — | Test array slot 20 (not used) |
| 15 | TARRAY_21 | STRING | 1 | — | Test array slot 21 (not used) |
| 16 | TARRAY_22 | STRING | 1 | — | Test array slot 22 (not used) |
| 17 | TARRAY_23 | STRING | 1 | — | Test array slot 23 (not used) |
| 18 | TARRAY_24 | STRING | 1 | — | Test array slot 24 (not used) |
| 19 | TARRAY_25 | STRING | 1 | — | Test array slot 25 (not used) |
| 20 | TARRAY_26 | STRING | 1 | — | Test array slot 26 (not used) |
| 21 | TARRAY_27 | STRING | 1 | — | Test array slot 27 (not used) |
| 22 | TARRAY_28 | STRING | 1 | — | Test array slot 28 (not used) |
| 23 | TARRAY_29 | STRING | 1 | — | Test array slot 29 (not used) |
| 24 | TARRAY_3 | STRING | 1 | — | Test array slot 3 (not used) |
| 25 | TARRAY_30 | STRING | 1 | — | Test array slot 30 (not used) |
| 26 | TARRAY_31 | STRING | 1 | — | Test array slot 31 (not used) |
| 27 | TARRAY_32 | STRING | 1 | — | Test array slot 32 (not used) |
| 28 | TARRAY_33 | STRING | 1 | — | Test array slot 33 (not used) |
| 29 | TARRAY_34 | STRING | 1 | — | Test array slot 34 (not used) |
| 30 | TARRAY_35 | STRING | 1 | — | Test array slot 35 (not used) |
| 31 | TARRAY_36 | STRING | 1 | — | Test array slot 36 (not used) |
| 32 | TARRAY_37 | STRING | 1 | — | Test array slot 37 (not used) |
| 33 | TARRAY_38 | STRING | 1 | — | Test array slot 38 (not used) |
| 34 | TARRAY_39 | STRING | 1 | — | Test array slot 39 (not used) |
| 35 | TARRAY_4 | STRING | 1 | — | Test array slot 4 (not used) |
| 36 | TARRAY_40 | STRING | 1 | — | Test array slot 40 (not used) |
| 37 | TARRAY_41 | STRING | 1 | — | Test array slot 41 (not used) |
| 38 | TARRAY_42 | STRING | 1 | — | Test array slot 42 (not used) |
| 39 | TARRAY_43 | STRING | 1 | — | Test array slot 43 (not used) |
| 40 | TARRAY_44 | STRING | 1 | — | Test array slot 44 (not used) |
| 41 | TARRAY_45 | STRING | 1 | — | Test array slot 45 (not used) |
| 42 | TARRAY_46 | STRING | 1 | — | Test array slot 46 (not used) |
| 43 | TARRAY_47 | STRING | 1 | — | Test array slot 47 (not used) |
| 44 | TARRAY_48 | STRING | 1 | — | Test array slot 48 (not used) |
| 45 | TARRAY_49 | STRING | 1 | — | Test array slot 49 (not used) |
| 46 | TARRAY_5 | STRING | 1 | — | Test array slot 5 (not used) |
| 47 | TARRAY_50 | STRING | 1 | — | Test array slot 50 (not used) |
| 48 | TARRAY_51 | STRING | 1 | — | Test array slot 51 (not used) |
| 49 | TARRAY_52 | STRING | 1 | — | Test array slot 52 (not used) |
| 50 | TARRAY_53 | STRING | 1 | — | Test array slot 53 (not used) |
| 51 | TARRAY_54 | STRING | 1 | — | Test array slot 54 (not used) |
| 52 | TARRAY_55 | STRING | 1 | — | Test array slot 55 (not used) |
| 53 | TARRAY_56 | STRING | 1 | — | Test array slot 56 (not used) |
| 54 | TARRAY_57 | STRING | 1 | — | Test array slot 57 (not used) |
| 55 | TARRAY_58 | STRING | 1 | — | Test array slot 58 (not used) |
| 56 | TARRAY_59 | STRING | 1 | — | Test array slot 59 (not used) |
| 57 | TARRAY_6 | STRING | 1 | — | Test array slot 6 (not used) |
| 58 | TARRAY_60 | STRING | 1 | — | Test array slot 60 (not used) |
| 59 | TARRAY_61 | STRING | 1 | — | Test array slot 61 (not used) |
| 60 | TARRAY_62 | STRING | 1 | — | Test array slot 62 (not used) |
| 61 | TARRAY_63 | STRING | 1 | — | Test array slot 63 (not used) |
| 62 | TARRAY_64 | STRING | 1 | — | Test array slot 64 (not used) |
| 63 | TARRAY_65 | STRING | 1 | — | Test array slot 65 (not used) |
| 64 | TARRAY_66 | STRING | 1 | — | Test array slot 66 (not used) |
| 65 | TARRAY_67 | STRING | 1 | — | Test array slot 67 (not used) |
| 66 | TARRAY_68 | STRING | 1 | — | Test array slot 68 (not used) |
| 67 | TARRAY_69 | STRING | 1 | — | Test array slot 69 (not used) |
| 68 | TARRAY_7 | STRING | 1 | — | Test array slot 7 (not used) |
| 69 | TARRAY_70 | STRING | 1 | — | Test array slot 70 (not used) |
| 70 | TARRAY_71 | STRING | 1 | — | Test array slot 71 (not used) |
| 71 | TARRAY_72 | STRING | 1 | — | Test array slot 72 (not used) |
| 72 | TARRAY_73 | STRING | 1 | — | Test array slot 73 (not used) |
| 73 | TARRAY_74 | STRING | 1 | — | Test array slot 74 (not used) |
| 74 | TARRAY_75 | STRING | 1 | — | Test array slot 75 (not used) |
| 75 | TARRAY_76 | STRING | 1 | — | Test array slot 76 (not used) |
| 76 | TARRAY_77 | STRING | 1 | — | Test array slot 77 (not used) |
| 77 | TARRAY_78 | STRING | 1 | — | Test array slot 78 (not used) |
| 78 | TARRAY_79 | STRING | 1 | — | Test array slot 79 (not used) |
| 79 | TARRAY_8 | STRING | 1 | — | Test array slot 8 (not used) |
| 80 | TARRAY_80 | STRING | 1 | — | Test array slot 80 (not used) |
| 81 | TARRAY_81 | STRING | 1 | — | Test array slot 81 (not used) |
| 82 | TARRAY_82 | STRING | 1 | — | Test array slot 82 (not used) |
| 83 | TARRAY_83 | STRING | 1 | — | Test array slot 83 (not used) |
| 84 | TARRAY_84 | STRING | 1 | — | Test array slot 84 (not used) |
| 85 | TARRAY_85 | STRING | 1 | — | Test array slot 85 (not used) |
| 86 | TARRAY_86 | STRING | 1 | — | Test array slot 86 (not used) |
| 87 | TARRAY_87 | STRING | 1 | — | Test array slot 87 (not used) |
| 88 | TARRAY_88 | STRING | 1 | — | Test array slot 88 (not used) |
| 89 | TARRAY_89 | STRING | 1 | — | Test array slot 89 (not used) |
| 90 | TARRAY_9 | STRING | 1 | — | Test array slot 9 (not used) |
| 91 | TARRAY_90 | STRING | 1 | — | Test array slot 90 (not used) |
| 92 | TARRAY_91 | STRING | 1 | — | Test array slot 91 (not used) |
| 93 | TARRAY_92 | STRING | 1 | — | Test array slot 92 (not used) |
| 94 | TARRAY_93 | STRING | 1 | — | Test array slot 93 (not used) |
| 95 | TARRAY_94 | STRING | 1 | — | Test array slot 94 (not used) |
| 96 | TARRAY_95 | STRING | 1 | — | Test array slot 95 (not used) |
| 97 | TARRAY_96 | STRING | 1 | — | Test array slot 96 (not used) |
| 98 | TARRAY_97 | STRING | 1 | — | Test array slot 97 (not used) |
| 99 | TARRAY_98 | STRING | 1 | — | Test array slot 98 (not used) |
| 100 | TARRAY_99 | STRING | 1 | — | Test array slot 99 (not used) |
| 101 | TEST | STRING | 10 | — | Test field (not used) |

## TESTFILE
**NOT USED**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | TESTFILE_1 | STRING | 10 | — | Test field 1 |
| 2 | TESTFILE_10 | NUMERIC | 8 | 2 | Test numeric field 10 |
| 3 | TESTFILE_11 | STRING | 50 | — | Test field 11 |
| 4 | TESTFILE_2 | STRING | 20 | — | Test field 2 |
| 5 | TESTFILE_3 | NUMERIC | 8 | 2 | Test numeric field 3 |
| 6 | TESTFILE_4 | NUMERIC | 8 | 2 | Test numeric field 4 |
| 7 | TESTFILE_5 | STRING | 40 | — | Test field 5 |
| 8 | TESTFILE_6 | NUMERIC | 8 | 4 | Test numeric field 6 |
| 9 | TESTFILE_7 | STRING | 40 | — | Test field 7 |
| 10 | TESTFILE_8 | STRING | 30 | — | Test field 8 |
| 11 | TESTFILE_9 | STRING | 25 | — | Test field 9 |

## WBTRVMEMO
**NOT USED**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BTRV_MEM_BUFF | STRING | 512 | — | Btrieve operation data buffer |
| 2 | BTRV_MEM_CNTR | INTEGER | 4 | — | Operation counter |
| 3 | BTRV_MEM_LINK | INTEGER | 4 | — | Linked record pointer |
| 4 | BTRV_MEM_SIZE | INTEGER | 4 | — | Buffer size |
| 5 | BTRV_MEM_SUBC | INTEGER | 4 | — | Subcode/operation code |

## WOBOMCHG
**WOBOM CHANGES (NOT USED)**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WBOM_CHG_ACOMP | STRING | 1 | — | After: component required flag (Y/N) |
| 2 | WBOM_CHG_AEXTRA | STRING | 100 | — | After: extra field |
| 3 | WBOM_CHG_AQTY | NUMERIC | 8 | 8 | After: quantity per assembly |
| 4 | WBOM_CHG_AREF | STRING | 20 | — | After: reference designator |
| 5 | WBOM_CHG_ASCRAP | NUMERIC | 8 | 2 | After: scrap factor |
| 6 | WBOM_CHG_BEXTRA | STRING | 100 | — | Before: extra field |
| 7 | WBOM_CHG_BQTY | NUMERIC | 8 | 8 | Before: quantity per assembly |
| 8 | WBOM_CHG_BREF | STRING | 20 | — | Before: reference designator |
| 9 | WBOM_CHG_BSCRAP | NUMERIC | 8 | 2 | Before: scrap factor |
| 10 | WBOM_CHG_CDATE | DATE | 4 | — | Change date |
| 11 | WBOM_CHG_COMP | STRING | 15 | — | Component item code |
| 12 | WBOM_CHG_DCOMP | STRING | 1 | — | Delete component flag (Y/N) |
| 13 | WBOM_CHG_PARENT | STRING | 15 | — | Parent assembly item code |
| 14 | WBOM_CHG_UID | STRING | 20 | — | Unique change ID |
| 15 | WBOM_CHG_USER | STRING | 15 | — | User who made the change |
| 16 | WBOM_CHG_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 17 | WBOM_CHG_WOSUF | INTEGER | 2 | — | Work order suffix |

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
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | Long product code/description |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | Manufacturer code |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | Net GL last year |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | Net GL month-to-date |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | Net GL variance |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | Net GL year-to-date |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | Primary material type code |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | Turnover rate |
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
