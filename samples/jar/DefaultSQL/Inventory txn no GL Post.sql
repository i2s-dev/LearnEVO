
SELECT INV.MTIT_CODE, INV.MTIT_DATE, INV.MTIT_TYPE, 
       INV.MTIT_QTY, INV.MTIT_AVGCOST
FROM   INVTXN as INV
WHERE  NOT EXISTS
(SELECT *
 FROM (SELECT * 
       FROM   BKGLTRAN 
       WHERE  ISNULL(RTRIM(BKGLTRAN.BKGL_TRN_PART),'') <> '') as TRANS
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
-------------------------------------------------------------------------------------------------
-- Inventory txn no GL Post - Find Inventory Transaction entries with no corresponding GL entries
-------------------------------------------------------------------------------------------------
----------------------------Don't change above this line-----------------------------------------

AND INV.MTIT_DATE >=           '0000-00-00'
--Put start of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND INV.MTIT_DATE <=           '0000-00-00' 
--Put end of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'
