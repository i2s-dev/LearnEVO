SELECT TRANS.BKGL_TRN_PART, TRANS.BKGL_TRN_DATE, TRANS.BKGL_TRN_TYPE, 
       TRANS.BKGL_TRN_AMT
FROM   BKGLTRAN as TRANS
WHERE  NOT EXISTS
(SELECT *
 FROM   BKAPHPOL as BKAP
 WHERE  TRANS.BKGL_TRN_PART = BKAP.BKAP_POL_PCODE
 AND    TRANS.BKGL_TRN_DATE = BKAP.BKAP_POL_ARD
 AND    RTRIM(TRANS.BKGL_TRN_INVC) = LTRIM(RTRIM(BKAP.BKAP_POL_PONM))
 AND    TRANS.BKGL_TRN_AMT = ROUND(ABS(BKAP.BKAP_POL_PQTY*BKAP.BKAP_POL_PPRCE),2) 
 AND    LTRIM(ISNULL(BKAP.BKAP_POL_PCODE,'')) <> ''
)
AND UPPER(TRANS.BKGL_TRN_DESC) = 'RECEIVED/NOT INVOICED'
AND LTRIM(ISNULL(TRANS.BKGL_TRN_PART,'')) <> ''
------------------------------------------------------------------------------------------
--RNI Received - Identifies GL Transactions to the PO/RNI account from PO Receiving (PO-C) 
--               that do not have corresponding line items in the PO Receiver file.
------------------------------------------------------------------------------------------
------------------------Don't change above this line------------------------

AND TRANS.BKGL_TRN_DATE >=     '0000-00-00'
--Put start of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_DATE <=   '0000-00-00'
--Put end of date range here ^^^^^^^^^^^^ 'yyyy-mm-dd'

AND TRANS.BKGL_TRN_GLACCT = '**********'
--Put PO/RNI GL Acct here   ^^^^^^^^^^^^ '1234567890'