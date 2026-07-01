SELECT TRANS.BKGL_TRN_CODE, TRANS.BKGL_TRN_DATE, TRANS.BKGL_TRN_TYPE,
       TRANS.BKGL_TRN_AMT
FROM   BKGLTRAN as TRANS
WHERE  NOT EXISTS
(SELECT *
 FROM   (SELECT   BKAPHPO.BKAP_PO_VNDCOD, BKAPHPOL.BKAP_POL_PONM, BKAPHPOL.BKAP_POL_PSTDTE,
                  BKAPHPOL.BKAP_POL_INVNUM, 
                  ABS(SUM(BKAPHPOL.BKAP_POL_PQTY*BKAPHPOL.BKAP_POL_PPRCE)) as AMOUNT
         FROM     BKAPHPOL, BKAPHPO
         WHERE    ISNULL(RTRIM(BKAPHPOL.BKAP_POL_PCODE),'') <> ''
         AND      ISNULL(RTRIM(BKAPHPOL.BKAP_POL_INVNUM),'') <> ''
         AND      BKAPHPOL.BKAP_POL_PONM = BKAPHPO.BKAP_PO_NUM
         GROUP BY BKAPHPO.BKAP_PO_VNDCOD, BKAPHPOL.BKAP_POL_PONM, BKAPHPOL.BKAP_POL_PSTDTE, 
                  BKAPHPOL.BKAP_POL_INVNUM) as BKAP
 WHERE  TRANS.BKGL_TRN_CODE = BKAP.BKAP_PO_VNDCOD
 AND    TRANS.BKGL_TRN_DATE = BKAP.BKAP_POL_PSTDTE
 AND    SUBSTRING(TRANS.BKGL_TRN_INVC,2,9) = BKAP.BKAP_POL_INVNUM
 AND    TRANS.BKGL_TRN_AMT = ROUND(BKAP.AMOUNT,2)
)
AND UPPER(TRANS.BKGL_TRN_DESC) = 'RNI/INVOICED'
----------------------------------------------------------------------------------------------
--RNI Invoiced - Identifies GL Txns to the PO/RNI account from PO Invoicing (AP-C) that do not 
--               have corresponding line items in the PO Receiver file.
----------------------------------------------------------------------------------------------
-------------------------don't change above this line-----------------------------------------

AND TRANS.BKGL_TRN_DATE >=     '0000-00-00'
--Put start of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_DATE <=  '0000-00-00'
--Put end of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_GLACCT = '**********'
--Put PO/RNI GL Acct here   ^^^^^^^^^^^^   '1234567890'