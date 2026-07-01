SELECT TRANS.BKGL_TRN_PART, TRANS.BKGL_TRN_DATE, TRANS.BKGL_TRN_TYPE,
       TRANS.BKGL_TRN_AMT
FROM   BKGLTRAN AS TRANS 
WHERE ISNULL(RTRIM(TRANS.BKGL_TRN_CODE),'') <> ''
AND NOT EXISTS
(SELECT *
 FROM INVTXN as INV
 WHERE INV.MTIT_CODE = TRANS.BKGL_TRN_PART
 AND   INV.MTIT_DATE = TRANS.BKGL_TRN_DATE
 AND   ((INV.MTIT_TYPE = 'A' AND TRANS.BKGL_TRN_TYPE = 'OT') OR
        (INV.MTIT_TYPE = 'P' AND TRANS.BKGL_TRN_TYPE = 'RP') OR
        (INV.MTIT_TYPE = 'S' AND TRANS.BKGL_TRN_TYPE = 'RS') OR
        (INV.MTIT_TYPE = 'I' AND TRANS.BKGL_TRN_TYPE = 'WO') OR
        (INV.MTIT_TYPE = 'W' AND TRANS.BKGL_TRN_TYPE = 'WO') OR
        (INV.MTIT_TYPE = 'Q' AND TRANS.BKGL_TRN_TYPE = 'RP') OR
        (INV.MTIT_TYPE = 'M' AND TRANS.BKGL_TRN_TYPE = 'RP') OR
        (INV.MTIT_TYPE = 'T' AND TRANS.BKGL_TRN_TYPE = 'OT') OR
        (INV.MTIT_TYPE = 'C' AND TRANS.BKGL_TRN_TYPE = 'RP') OR
        (INV.MTIT_TYPE = 'R' AND TRANS.BKGL_TRN_TYPE = 'RS') OR
        (INV.MTIT_TYPE = 'J' AND TRANS.BKGL_TRN_TYPE = 'RP') OR
        (INV.MTIT_TYPE = 'O' AND TRANS.BKGL_TRN_TYPE = 'RP'))
 AND CAST(TRANS.BKGL_TRN_ENTDTE as CHAR(10)) = '20' + SUBSTRING(INV.MTIT_EXTRA,32,2) + '-' + 
                                                      SUBSTRING(INV.MTIT_EXTRA,26,2) + '-' + 
                                                      SUBSTRING(INV.MTIT_EXTRA,29,2)
 AND ROUND(ABS(INV.MTIT_QTY*INV.MTIT_AVGCOST),2) = TRANS.BKGL_TRN_AMT
)
--------------------------------------------------------------------------------------------
-- GL No Inv Txn - Find GL Transaction entries to a specified inventory account 
--                 with no corresponding Inventory Transaction
--------------------------------------------------------------------------------------------
----------------------------Don't change above this line------------------------------------

AND TRANS.BKGL_TRN_DATE >=     '0000-00-00'
--Put start of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_DATE <=   '0000-00-00'
--Put end of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_GLACCT = '**********'
--Put the GL Account here   ^^^^^^^^^^^^ in single quotes, no extra spaces