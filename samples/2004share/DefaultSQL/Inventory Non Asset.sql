SELECT BKGLCOA.BKGL_ACCT, BKGLCOA.BKGL_TYPE, BKICMSTR.BKIC_PROD_CLASS, 
       BKICMSTR.BKIC_PROD_CODE, BKICMSTR.BKIC_PROD_DESC, BKICMSTR.BKIC_PROD_TYPE
FROM   BKGLCOA, BKICMSTR, CLASS
WHERE  CLASS.MTCLASS_CLASS = BKICMSTR.BKIC_PROD_CLASS
AND    BKGLCOA.BKGL_ACCT = CLASS.CLASS_GLA
AND    UPPER(BKGLCOA.BKGL_TYPE) <> 'A'
AND    BKICMSTR.BKIC_PROD_TYPE IN ('R','F','A','M')
--------------------------------------------------------------------------------------------------
--    Inventory Non Asset - Identify tangible inventory items posting to a GL Account 
--                          that is not an Asset account
--------------------------------------------------------------------------------------------------