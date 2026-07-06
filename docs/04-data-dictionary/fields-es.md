# ES — Estimating: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKESTCFG
**ESTIMATING CONFIGURATION**

Fields: 18

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEST_CFG_CLASS | STRING | 4 | — | Default product class for new estimates |
| 2 | BKEST_CFG_DAYS | INTEGER | 2 | — | Default days until estimate expires |
| 3 | BKEST_CFG_ENDLN_1 | STRING | 30 | — | Ending line text 1 (bottom of estimate form) |
| 4 | BKEST_CFG_ENDLN_2 | STRING | 30 | — | Ending line text 2 |
| 5 | BKEST_CFG_ENDLN_3 | STRING | 30 | — | Ending line text 3 |
| 6 | BKEST_CFG_ENDLN_4 | STRING | 30 | — | Ending line text 4 |
| 7 | BKEST_CFG_ENDLN_5 | STRING | 30 | — | Ending line text 5 |
| 8 | BKEST_CFG_EXTRA | STRING | 100 | — | Extra freeform field |
| 9 | BKEST_CFG_FORM | STRING | 1 | — | Form style code |
| 10 | BKEST_CFG_LAB^ | NUMERIC | 8 | 2 | Default labor markup % |
| 11 | BKEST_CFG_MAT^ | NUMERIC | 8 | 2 | Default material markup % |
| 12 | BKEST_CFG_NUM | NUMERIC | 8 | — | Next estimate number |
| 13 | BKEST_CFG_OH^ | NUMERIC | 8 | 2 | Default overhead markup % |
| 14 | BKEST_CFG_OP^ | NUMERIC | 8 | 2 | Default outside process markup % |
| 15 | BKEST_CFG_SONUM | NUMERIC | 8 | — | Associated sales order number |
| 16 | BKEST_CFG_STAT | STRING | 1 | — | Default estimate status code |
| 17 | BKEST_CFG_TOT^ | NUMERIC | 8 | 2 | Default total markup % |
| 18 | BKEST_CMPY_INFO | STRING | 1 | — | Print company info on estimate Y/N |

## BKMATCST
**MATERIAL COST FILE**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMC_CODE | STRING | 15 | — | Material / part code (key) |
| 2 | BKMC_COST_1 | NUMERIC | 8 | 4 | Cost per unit at qty break 1 |
| 3 | BKMC_COST_10 | NUMERIC | 8 | 4 | Cost per unit at qty break 10 |
| 4 | BKMC_COST_2 | NUMERIC | 8 | 4 | Cost per unit at qty break 2 |
| 5 | BKMC_COST_3 | NUMERIC | 8 | 4 | Cost per unit at qty break 3 |
| 6 | BKMC_COST_4 | NUMERIC | 8 | 4 | Cost per unit at qty break 4 |
| 7 | BKMC_COST_5 | NUMERIC | 8 | 4 | Cost per unit at qty break 5 |
| 8 | BKMC_COST_6 | NUMERIC | 8 | 4 | Cost per unit at qty break 6 |
| 9 | BKMC_COST_7 | NUMERIC | 8 | 4 | Cost per unit at qty break 7 |
| 10 | BKMC_COST_8 | NUMERIC | 8 | 4 | Cost per unit at qty break 8 |
| 11 | BKMC_COST_9 | NUMERIC | 8 | 4 | Cost per unit at qty break 9 |
| 12 | BKMC_DATE | DATE | 4 | — | Date cost last updated |
| 13 | BKMC_EXTRA | STRING | 50 | — | Extra freeform field |
| 14 | BKMC_MIN | NUMERIC | 8 | 2 | Minimum order quantity |
| 15 | BKMC_MINCST | NUMERIC | 8 | 4 | Minimum order cost |
| 16 | BKMC_QTY_1 | NUMERIC | 8 | 2 | Quantity breakpoint 1 |
| 17 | BKMC_QTY_10 | NUMERIC | 8 | 2 | Quantity breakpoint 10 |
| 18 | BKMC_QTY_2 | NUMERIC | 8 | 2 | Quantity breakpoint 2 |
| 19 | BKMC_QTY_3 | NUMERIC | 8 | 2 | Quantity breakpoint 3 |
| 20 | BKMC_QTY_4 | NUMERIC | 8 | 2 | Quantity breakpoint 4 |
| 21 | BKMC_QTY_5 | NUMERIC | 8 | 2 | Quantity breakpoint 5 |
| 22 | BKMC_QTY_6 | NUMERIC | 8 | 2 | Quantity breakpoint 6 |
| 23 | BKMC_QTY_7 | NUMERIC | 8 | 2 | Quantity breakpoint 7 |
| 24 | BKMC_QTY_8 | NUMERIC | 8 | 2 | Quantity breakpoint 8 |
| 25 | BKMC_QTY_9 | NUMERIC | 8 | 2 | Quantity breakpoint 9 |

## ESTSUM
**ESTIMATE MASTER**

Fields: 228

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTESUM_ATTN | STRING | 30 | — | Attention line |
| 2 | MTESUM_BOM_FLAG | STRING | 1 | — | BOM attached Y/N |
| 3 | MTESUM_CDATE | DATE | 4 | — | Creation date |
| 4 | MTESUM_CLASS | STRING | 4 | — | Product class |
| 5 | MTESUM_CODE | STRING | 15 | — | Part code (key) |
| 6 | MTESUM_COMM_RTE_1 | NUMERIC | 8 | 4 | Commission rate — salesperson 1 |
| 7 | MTESUM_COMM_RTE_2 | NUMERIC | 8 | 4 | Commission rate — salesperson 2 |
| 8 | MTESUM_COST_1 | NUMERIC | 8 | 4 | Total cost at qty break 1 |
| 9 | MTESUM_COST_10 | NUMERIC | 8 | 4 | Total cost at qty break 10 |
| 10 | MTESUM_COST_2 | NUMERIC | 8 | 4 | Total cost at qty break 2 |
| 11 | MTESUM_COST_3 | NUMERIC | 8 | 4 | Total cost at qty break 3 |
| 12 | MTESUM_COST_4 | NUMERIC | 8 | 4 | Total cost at qty break 4 |
| 13 | MTESUM_COST_5 | NUMERIC | 8 | 4 | Total cost at qty break 5 |
| 14 | MTESUM_COST_6 | NUMERIC | 8 | 4 | Total cost at qty break 6 |
| 15 | MTESUM_COST_7 | NUMERIC | 8 | 4 | Total cost at qty break 7 |
| 16 | MTESUM_COST_8 | NUMERIC | 8 | 4 | Total cost at qty break 8 |
| 17 | MTESUM_COST_9 | NUMERIC | 8 | 4 | Total cost at qty break 9 |
| 18 | MTESUM_CUSTCODE | STRING | 10 | — | Customer code |
| 19 | MTESUM_DATE | DATE | 4 | — | Estimate date |
| 20 | MTESUM_DESC | STRING | 30 | — | Part description |
| 21 | MTESUM_ENTBY | STRING | 15 | — | Entered by (user ID) |
| 22 | MTESUM_EX_FLAG | STRING | 1 | — | Exchange flag |
| 23 | MTESUM_EXPDATE | DATE | 4 | — | Expiration date |
| 24 | MTESUM_EXTRA2 | STRING | 100 | — | Extra freeform text |
| 25 | MTESUM_EXTRA^ | NUMERIC | 8 | 2 | Extra cost aggregate |
| 26 | MTESUM_EXTRA_1 | NUMERIC | 8 | 4 | Extra cost at qty break 1 |
| 27 | MTESUM_EXTRA_10 | NUMERIC | 8 | 4 | Extra cost at qty break 10 |
| 28 | MTESUM_EXTRA_2 | NUMERIC | 8 | 4 | Extra cost at qty break 2 |
| 29 | MTESUM_EXTRA_3 | NUMERIC | 8 | 4 | Extra cost at qty break 3 |
| 30 | MTESUM_EXTRA_4 | NUMERIC | 8 | 4 | Extra cost at qty break 4 |
| 31 | MTESUM_EXTRA_5 | NUMERIC | 8 | 4 | Extra cost at qty break 5 |
| 32 | MTESUM_EXTRA_6 | NUMERIC | 8 | 4 | Extra cost at qty break 6 |
| 33 | MTESUM_EXTRA_7 | NUMERIC | 8 | 4 | Extra cost at qty break 7 |
| 34 | MTESUM_EXTRA_8 | NUMERIC | 8 | 4 | Extra cost at qty break 8 |
| 35 | MTESUM_EXTRA_9 | NUMERIC | 8 | 4 | Extra cost at qty break 9 |
| 36 | MTESUM_FIN_DATE | DATE | 4 | — | Final / close date |
| 37 | MTESUM_L_O_CODE | STRING | 5 | — | Lost / order reason code |
| 38 | MTESUM_L_O_DATE | DATE | 4 | — | Lost / order date |
| 39 | MTESUM_LAB^ | NUMERIC | 8 | 2 | Labor cost aggregate |
| 40 | MTESUM_LAB_1 | NUMERIC | 8 | 4 | Labor cost at qty break 1 |
| 41 | MTESUM_LAB_10 | NUMERIC | 8 | 4 | Labor cost at qty break 10 |
| 42 | MTESUM_LAB_2 | NUMERIC | 8 | 4 | Labor cost at qty break 2 |
| 43 | MTESUM_LAB_3 | NUMERIC | 8 | 4 | Labor cost at qty break 3 |
| 44 | MTESUM_LAB_4 | NUMERIC | 8 | 4 | Labor cost at qty break 4 |
| 45 | MTESUM_LAB_5 | NUMERIC | 8 | 4 | Labor cost at qty break 5 |
| 46 | MTESUM_LAB_6 | NUMERIC | 8 | 4 | Labor cost at qty break 6 |
| 47 | MTESUM_LAB_7 | NUMERIC | 8 | 4 | Labor cost at qty break 7 |
| 48 | MTESUM_LAB_8 | NUMERIC | 8 | 4 | Labor cost at qty break 8 |
| 49 | MTESUM_LAB_9 | NUMERIC | 8 | 4 | Labor cost at qty break 9 |
| 50 | MTESUM_LABMU^ | NUMERIC | 8 | 2 | Labor markup % aggregate |
| 51 | MTESUM_LABMU_1 | NUMERIC | 8 | 4 | Labor markup % at qty break 1 |
| 52 | MTESUM_LABMU_10 | NUMERIC | 8 | 4 | Labor markup % at qty break 10 |
| 53 | MTESUM_LABMU_2 | NUMERIC | 8 | 4 | Labor markup % at qty break 2 |
| 54 | MTESUM_LABMU_3 | NUMERIC | 8 | 4 | Labor markup % at qty break 3 |
| 55 | MTESUM_LABMU_4 | NUMERIC | 8 | 4 | Labor markup % at qty break 4 |
| 56 | MTESUM_LABMU_5 | NUMERIC | 8 | 4 | Labor markup % at qty break 5 |
| 57 | MTESUM_LABMU_6 | NUMERIC | 8 | 4 | Labor markup % at qty break 6 |
| 58 | MTESUM_LABMU_7 | NUMERIC | 8 | 4 | Labor markup % at qty break 7 |
| 59 | MTESUM_LABMU_8 | NUMERIC | 8 | 4 | Labor markup % at qty break 8 |
| 60 | MTESUM_LABMU_9 | NUMERIC | 8 | 4 | Labor markup % at qty break 9 |
| 61 | MTESUM_LEAD_SRC | STRING | 4 | — | Lead source code |
| 62 | MTESUM_LEADTIME | STRING | 30 | — | Lead time description |
| 63 | MTESUM_LOC | STRING | 10 | — | Location code |
| 64 | MTESUM_MAT^ | NUMERIC | 8 | 2 | Material cost aggregate |
| 65 | MTESUM_MAT_1 | NUMERIC | 8 | 4 | Material cost at qty break 1 |
| 66 | MTESUM_MAT_10 | NUMERIC | 8 | 4 | Material cost at qty break 10 |
| 67 | MTESUM_MAT_2 | NUMERIC | 8 | 4 | Material cost at qty break 2 |
| 68 | MTESUM_MAT_3 | NUMERIC | 8 | 4 | Material cost at qty break 3 |
| 69 | MTESUM_MAT_4 | NUMERIC | 8 | 4 | Material cost at qty break 4 |
| 70 | MTESUM_MAT_5 | NUMERIC | 8 | 4 | Material cost at qty break 5 |
| 71 | MTESUM_MAT_6 | NUMERIC | 8 | 4 | Material cost at qty break 6 |
| 72 | MTESUM_MAT_7 | NUMERIC | 8 | 4 | Material cost at qty break 7 |
| 73 | MTESUM_MAT_8 | NUMERIC | 8 | 4 | Material cost at qty break 8 |
| 74 | MTESUM_MAT_9 | NUMERIC | 8 | 4 | Material cost at qty break 9 |
| 75 | MTESUM_MATMU^ | NUMERIC | 8 | 2 | Material markup % aggregate |
| 76 | MTESUM_MATMU_1 | NUMERIC | 8 | 4 | Material markup % at qty break 1 |
| 77 | MTESUM_MATMU_10 | NUMERIC | 8 | 4 | Material markup % at qty break 10 |
| 78 | MTESUM_MATMU_2 | NUMERIC | 8 | 4 | Material markup % at qty break 2 |
| 79 | MTESUM_MATMU_3 | NUMERIC | 8 | 4 | Material markup % at qty break 3 |
| 80 | MTESUM_MATMU_4 | NUMERIC | 8 | 4 | Material markup % at qty break 4 |
| 81 | MTESUM_MATMU_5 | NUMERIC | 8 | 4 | Material markup % at qty break 5 |
| 82 | MTESUM_MATMU_6 | NUMERIC | 8 | 4 | Material markup % at qty break 6 |
| 83 | MTESUM_MATMU_7 | NUMERIC | 8 | 4 | Material markup % at qty break 7 |
| 84 | MTESUM_MATMU_8 | NUMERIC | 8 | 4 | Material markup % at qty break 8 |
| 85 | MTESUM_MATMU_9 | NUMERIC | 8 | 4 | Material markup % at qty break 9 |
| 86 | MTESUM_MISC^ | NUMERIC | 8 | 2 | Misc cost aggregate |
| 87 | MTESUM_MISC_1 | NUMERIC | 8 | 4 | Misc cost at qty break 1 |
| 88 | MTESUM_MISC_10 | NUMERIC | 8 | 4 | Misc cost at qty break 10 |
| 89 | MTESUM_MISC_2 | NUMERIC | 8 | 4 | Misc cost at qty break 2 |
| 90 | MTESUM_MISC_3 | NUMERIC | 8 | 4 | Misc cost at qty break 3 |
| 91 | MTESUM_MISC_4 | NUMERIC | 8 | 4 | Misc cost at qty break 4 |
| 92 | MTESUM_MISC_5 | NUMERIC | 8 | 4 | Misc cost at qty break 5 |
| 93 | MTESUM_MISC_6 | NUMERIC | 8 | 4 | Misc cost at qty break 6 |
| 94 | MTESUM_MISC_7 | NUMERIC | 8 | 4 | Misc cost at qty break 7 |
| 95 | MTESUM_MISC_8 | NUMERIC | 8 | 4 | Misc cost at qty break 8 |
| 96 | MTESUM_MISC_9 | NUMERIC | 8 | 4 | Misc cost at qty break 9 |
| 97 | MTESUM_NAME | STRING | 30 | — | Customer / prospect name |
| 98 | MTESUM_NOTES_1 | STRING | 60 | — | Estimate notes line 1 |
| 99 | MTESUM_NOTES_10 | STRING | 60 | — | Estimate notes line 10 |
| 100 | MTESUM_NOTES_2 | STRING | 60 | — | Estimate notes line 2 |
| 101 | MTESUM_NOTES_3 | STRING | 60 | — | Estimate notes line 3 |
| 102 | MTESUM_NOTES_4 | STRING | 60 | — | Estimate notes line 4 |
| 103 | MTESUM_NOTES_5 | STRING | 60 | — | Estimate notes line 5 |
| 104 | MTESUM_NOTES_6 | STRING | 60 | — | Estimate notes line 6 |
| 105 | MTESUM_NOTES_7 | STRING | 60 | — | Estimate notes line 7 |
| 106 | MTESUM_NOTES_8 | STRING | 60 | — | Estimate notes line 8 |
| 107 | MTESUM_NOTES_9 | STRING | 60 | — | Estimate notes line 9 |
| 108 | MTESUM_OH^ | NUMERIC | 8 | 2 | Overhead cost aggregate |
| 109 | MTESUM_OH_1 | NUMERIC | 8 | 4 | Overhead cost at qty break 1 |
| 110 | MTESUM_OH_10 | NUMERIC | 8 | 4 | Overhead cost at qty break 10 |
| 111 | MTESUM_OH_2 | NUMERIC | 8 | 4 | Overhead cost at qty break 2 |
| 112 | MTESUM_OH_3 | NUMERIC | 8 | 4 | Overhead cost at qty break 3 |
| 113 | MTESUM_OH_4 | NUMERIC | 8 | 4 | Overhead cost at qty break 4 |
| 114 | MTESUM_OH_5 | NUMERIC | 8 | 4 | Overhead cost at qty break 5 |
| 115 | MTESUM_OH_6 | NUMERIC | 8 | 4 | Overhead cost at qty break 6 |
| 116 | MTESUM_OH_7 | NUMERIC | 8 | 4 | Overhead cost at qty break 7 |
| 117 | MTESUM_OH_8 | NUMERIC | 8 | 4 | Overhead cost at qty break 8 |
| 118 | MTESUM_OH_9 | NUMERIC | 8 | 4 | Overhead cost at qty break 9 |
| 119 | MTESUM_OHMU^ | NUMERIC | 8 | 2 | Overhead markup % aggregate |
| 120 | MTESUM_OHMU_1 | NUMERIC | 8 | 4 | Overhead markup % at qty break 1 |
| 121 | MTESUM_OHMU_10 | NUMERIC | 8 | 4 | Overhead markup % at qty break 10 |
| 122 | MTESUM_OHMU_2 | NUMERIC | 8 | 4 | Overhead markup % at qty break 2 |
| 123 | MTESUM_OHMU_3 | NUMERIC | 8 | 4 | Overhead markup % at qty break 3 |
| 124 | MTESUM_OHMU_4 | NUMERIC | 8 | 4 | Overhead markup % at qty break 4 |
| 125 | MTESUM_OHMU_5 | NUMERIC | 8 | 4 | Overhead markup % at qty break 5 |
| 126 | MTESUM_OHMU_6 | NUMERIC | 8 | 4 | Overhead markup % at qty break 6 |
| 127 | MTESUM_OHMU_7 | NUMERIC | 8 | 4 | Overhead markup % at qty break 7 |
| 128 | MTESUM_OHMU_8 | NUMERIC | 8 | 4 | Overhead markup % at qty break 8 |
| 129 | MTESUM_OHMU_9 | NUMERIC | 8 | 4 | Overhead markup % at qty break 9 |
| 130 | MTESUM_OL^ | NUMERIC | 8 | 2 | Outside labor cost aggregate |
| 131 | MTESUM_OLMU^ | NUMERIC | 8 | 2 | Outside labor markup % aggregate |
| 132 | MTESUM_OP^ | NUMERIC | 8 | 2 | Outside process cost aggregate |
| 133 | MTESUM_OP_1 | NUMERIC | 8 | 4 | Outside process cost at qty break 1 |
| 134 | MTESUM_OP_10 | NUMERIC | 8 | 4 | Outside process cost at qty break 10 |
| 135 | MTESUM_OP_2 | NUMERIC | 8 | 4 | Outside process cost at qty break 2 |
| 136 | MTESUM_OP_3 | NUMERIC | 8 | 4 | Outside process cost at qty break 3 |
| 137 | MTESUM_OP_4 | NUMERIC | 8 | 4 | Outside process cost at qty break 4 |
| 138 | MTESUM_OP_5 | NUMERIC | 8 | 4 | Outside process cost at qty break 5 |
| 139 | MTESUM_OP_6 | NUMERIC | 8 | 4 | Outside process cost at qty break 6 |
| 140 | MTESUM_OP_7 | NUMERIC | 8 | 4 | Outside process cost at qty break 7 |
| 141 | MTESUM_OP_8 | NUMERIC | 8 | 4 | Outside process cost at qty break 8 |
| 142 | MTESUM_OP_9 | NUMERIC | 8 | 4 | Outside process cost at qty break 9 |
| 143 | MTESUM_OPMU^ | NUMERIC | 8 | 2 | Outside process markup % aggregate |
| 144 | MTESUM_OPMU_1 | NUMERIC | 8 | 4 | Outside process markup % at qty break 1 |
| 145 | MTESUM_OPMU_10 | NUMERIC | 8 | 4 | Outside process markup % at qty break 10 |
| 146 | MTESUM_OPMU_2 | NUMERIC | 8 | 4 | Outside process markup % at qty break 2 |
| 147 | MTESUM_OPMU_3 | NUMERIC | 8 | 4 | Outside process markup % at qty break 3 |
| 148 | MTESUM_OPMU_4 | NUMERIC | 8 | 4 | Outside process markup % at qty break 4 |
| 149 | MTESUM_OPMU_5 | NUMERIC | 8 | 4 | Outside process markup % at qty break 5 |
| 150 | MTESUM_OPMU_6 | NUMERIC | 8 | 4 | Outside process markup % at qty break 6 |
| 151 | MTESUM_OPMU_7 | NUMERIC | 8 | 4 | Outside process markup % at qty break 7 |
| 152 | MTESUM_OPMU_8 | NUMERIC | 8 | 4 | Outside process markup % at qty break 8 |
| 153 | MTESUM_OPMU_9 | NUMERIC | 8 | 4 | Outside process markup % at qty break 9 |
| 154 | MTESUM_OPPTYPE | STRING | 2 | — | Opportunity type (2-char code) |
| 155 | MTESUM_OVALL^ | NUMERIC | 8 | 2 | Overall margin % aggregate |
| 156 | MTESUM_OVALL_1 | NUMERIC | 8 | 4 | Overall margin % at qty break 1 |
| 157 | MTESUM_OVALL_10 | NUMERIC | 8 | 4 | Overall margin % at qty break 10 |
| 158 | MTESUM_OVALL_2 | NUMERIC | 8 | 4 | Overall margin % at qty break 2 |
| 159 | MTESUM_OVALL_3 | NUMERIC | 8 | 4 | Overall margin % at qty break 3 |
| 160 | MTESUM_OVALL_4 | NUMERIC | 8 | 4 | Overall margin % at qty break 4 |
| 161 | MTESUM_OVALL_5 | NUMERIC | 8 | 4 | Overall margin % at qty break 5 |
| 162 | MTESUM_OVALL_6 | NUMERIC | 8 | 4 | Overall margin % at qty break 6 |
| 163 | MTESUM_OVALL_7 | NUMERIC | 8 | 4 | Overall margin % at qty break 7 |
| 164 | MTESUM_OVALL_8 | NUMERIC | 8 | 4 | Overall margin % at qty break 8 |
| 165 | MTESUM_OVALL_9 | NUMERIC | 8 | 4 | Overall margin % at qty break 9 |
| 166 | MTESUM_OVLMU^ | NUMERIC | 8 | 2 | Overall markup % aggregate |
| 167 | MTESUM_PRICE_1 | NUMERIC | 8 | 4 | Unit price at qty break 1 |
| 168 | MTESUM_PRICE_10 | NUMERIC | 8 | 4 | Unit price at qty break 10 |
| 169 | MTESUM_PRICE_2 | NUMERIC | 8 | 4 | Unit price at qty break 2 |
| 170 | MTESUM_PRICE_3 | NUMERIC | 8 | 4 | Unit price at qty break 3 |
| 171 | MTESUM_PRICE_4 | NUMERIC | 8 | 4 | Unit price at qty break 4 |
| 172 | MTESUM_PRICE_5 | NUMERIC | 8 | 4 | Unit price at qty break 5 |
| 173 | MTESUM_PRICE_6 | NUMERIC | 8 | 4 | Unit price at qty break 6 |
| 174 | MTESUM_PRICE_7 | NUMERIC | 8 | 4 | Unit price at qty break 7 |
| 175 | MTESUM_PRICE_8 | NUMERIC | 8 | 4 | Unit price at qty break 8 |
| 176 | MTESUM_PRICE_9 | NUMERIC | 8 | 4 | Unit price at qty break 9 |
| 177 | MTESUM_PROJ | STRING | 15 | — | Project number |
| 178 | MTESUM_QTREV | STRING | 9 | — | Quote revision level (e.g. A, B, …) |
| 179 | MTESUM_QTY_1 | NUMERIC | 8 | 2 | Quantity break 1 |
| 180 | MTESUM_QTY_10 | NUMERIC | 8 | 2 | Quantity break 10 |
| 181 | MTESUM_QTY_2 | NUMERIC | 8 | 2 | Quantity break 2 |
| 182 | MTESUM_QTY_3 | NUMERIC | 8 | 2 | Quantity break 3 |
| 183 | MTESUM_QTY_4 | NUMERIC | 8 | 2 | Quantity break 4 |
| 184 | MTESUM_QTY_5 | NUMERIC | 8 | 2 | Quantity break 5 |
| 185 | MTESUM_QTY_6 | NUMERIC | 8 | 2 | Quantity break 6 |
| 186 | MTESUM_QTY_7 | NUMERIC | 8 | 2 | Quantity break 7 |
| 187 | MTESUM_QTY_8 | NUMERIC | 8 | 2 | Quantity break 8 |
| 188 | MTESUM_QTY_9 | NUMERIC | 8 | 2 | Quantity break 9 |
| 189 | MTESUM_QUOTE | NUMERIC | 8 | — | Estimate / quote number (key) |
| 190 | MTESUM_REV | STRING | 4 | — | Revision level |
| 191 | MTESUM_RFQ | STRING | 15 | — | RFQ (request for quote) number |
| 192 | MTESUM_RT_FLAG | STRING | 1 | — | Routing attached Y/N |
| 193 | MTESUM_SETUP^ | NUMERIC | 8 | 2 | Setup cost aggregate |
| 194 | MTESUM_SETUP_1 | NUMERIC | 8 | 4 | Setup cost at qty break 1 |
| 195 | MTESUM_SETUP_10 | NUMERIC | 8 | 4 | Setup cost at qty break 10 |
| 196 | MTESUM_SETUP_2 | NUMERIC | 8 | 4 | Setup cost at qty break 2 |
| 197 | MTESUM_SETUP_3 | NUMERIC | 8 | 4 | Setup cost at qty break 3 |
| 198 | MTESUM_SETUP_4 | NUMERIC | 8 | 4 | Setup cost at qty break 4 |
| 199 | MTESUM_SETUP_5 | NUMERIC | 8 | 4 | Setup cost at qty break 5 |
| 200 | MTESUM_SETUP_6 | NUMERIC | 8 | 4 | Setup cost at qty break 6 |
| 201 | MTESUM_SETUP_7 | NUMERIC | 8 | 4 | Setup cost at qty break 7 |
| 202 | MTESUM_SETUP_8 | NUMERIC | 8 | 4 | Setup cost at qty break 8 |
| 203 | MTESUM_SETUP_9 | NUMERIC | 8 | 4 | Setup cost at qty break 9 |
| 204 | MTESUM_SLSP_NUM_1 | INTEGER | 2 | — | Salesperson 1 number |
| 205 | MTESUM_SLSP_NUM_2 | INTEGER | 2 | — | Salesperson 2 number |
| 206 | MTESUM_STATUS | STRING | 1 | — | Status (O=Open, Q=Quoted, W=Won, L=Lost) |
| 207 | MTESUM_TEMP_NUM | INTEGER | 2 | — | Template number |
| 208 | MTESUM_TOTAL_1 | NUMERIC | 8 | 4 | Grand total at qty break 1 |
| 209 | MTESUM_TOTAL_10 | NUMERIC | 8 | 4 | Grand total at qty break 10 |
| 210 | MTESUM_TOTAL_2 | NUMERIC | 8 | 4 | Grand total at qty break 2 |
| 211 | MTESUM_TOTAL_3 | NUMERIC | 8 | 4 | Grand total at qty break 3 |
| 212 | MTESUM_TOTAL_4 | NUMERIC | 8 | 4 | Grand total at qty break 4 |
| 213 | MTESUM_TOTAL_5 | NUMERIC | 8 | 4 | Grand total at qty break 5 |
| 214 | MTESUM_TOTAL_6 | NUMERIC | 8 | 4 | Grand total at qty break 6 |
| 215 | MTESUM_TOTAL_7 | NUMERIC | 8 | 4 | Grand total at qty break 7 |
| 216 | MTESUM_TOTAL_8 | NUMERIC | 8 | 4 | Grand total at qty break 8 |
| 217 | MTESUM_TOTAL_9 | NUMERIC | 8 | 4 | Grand total at qty break 9 |
| 218 | MTESUM_UM | STRING | 3 | — | Unit of measure |
| 219 | MTESUM_VOVHD_1 | NUMERIC | 8 | 4 | Variable overhead at qty break 1 |
| 220 | MTESUM_VOVHD_10 | NUMERIC | 8 | 4 | Variable overhead at qty break 10 |
| 221 | MTESUM_VOVHD_2 | NUMERIC | 8 | 4 | Variable overhead at qty break 2 |
| 222 | MTESUM_VOVHD_3 | NUMERIC | 8 | 4 | Variable overhead at qty break 3 |
| 223 | MTESUM_VOVHD_4 | NUMERIC | 8 | 4 | Variable overhead at qty break 4 |
| 224 | MTESUM_VOVHD_5 | NUMERIC | 8 | 4 | Variable overhead at qty break 5 |
| 225 | MTESUM_VOVHD_6 | NUMERIC | 8 | 4 | Variable overhead at qty break 6 |
| 226 | MTESUM_VOVHD_7 | NUMERIC | 8 | 4 | Variable overhead at qty break 7 |
| 227 | MTESUM_VOVHD_8 | NUMERIC | 8 | 4 | Variable overhead at qty break 8 |
| 228 | MTESUM_VOVHD_9 | NUMERIC | 8 | 4 | Variable overhead at qty break 9 |

## ISARECHG
**CHANGES TO ESTIMATES**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | After: actual ship date |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | After: commission % salesperson 1 |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | After: commission % salesperson 2 |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | After: discount amount |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | After: estimated ship date |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | After: extra field |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | After: location code |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | After: original order quantity |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | After: unit price |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | Before: actual ship date |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | Before: commission % salesperson 1 |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | Before: commission % salesperson 2 |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | Before: discount amount |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | Before: estimated ship date |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | Before: extra field |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | Before: location code |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | Before: original order quantity |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | Before: unit price |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | Change date |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | Estimate / invoice number (key) |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | Line ID changed (key) |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | Part code changed |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | Revision level |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | Sales order number |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | Unique change sequence number |
| 26 | ISAR_CHG_USER | STRING | 15 | — | User ID who made the change |

## ISBMESA
**ARCHIVED ESTIMATING BOM**

→ Identical schema to ISBMEST. See ISBMEST for field descriptions.

## ISBMEST
**ESTIMATING BOM**

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 10 | — | Component type code (N=Normal, O=Option) |
| 2 | BKBM_COMPONENT | STRING | 15 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | Effective date start |
| 4 | BKBM_DATE2 | DATE | 4 | — | Effective date end |
| 5 | BKBM_EST_LINE | NUMERIC | 8 | — | Estimate line number (key) |
| 6 | BKBM_EXTRA | STRING | 50 | — | Extra |
| 7 | BKBM_P_TYPE | STRING | 10 | — | Parent type code |
| 8 | BKBM_PARENT | STRING | 15 | — | Parent Part Code |
| 9 | BKBM_PROD_DUPOP | STRING | 1 | — | Duplicate Option blank / 1 / 2 |
| 10 | BKBM_PROD_LINE^ | INTEGER | 2 | — | Option line number (not used) |
| 11 | BKBM_PROD_OP | STRING | 3 | — | Option ( If  in second position) |
| 12 | BKBM_PROD_OPDSC | STRING | 5 | — | Option description code |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | Option active for qty break 1 Y/N |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | Option active for qty break 2 Y/N |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | Option active for qty break 3 Y/N |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | Option active for qty break 4 Y/N |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | Option active for qty break 5 Y/N |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | Option active for qty break 6 Y/N |
| 19 | BKBM_PROD_PRICE | NUMERIC | 8 | 4 | Option Pricing |
| 20 | BKBM_PROD_RTNUM | INTEGER | 2 | — | Routing  Sequence Number |
| 21 | BKBM_PROD_SCRAP | NUMERIC | 8 | 2 | Scrap Allowance Percent |
| 22 | BKBM_PROD_TYPE | STRING | 1 | — | Part Type |
| 23 | BKBM_PROD_VEND | STRING | 10 | — | Vendor Code |
| 24 | BKBM_QTY_REQD | NUMERIC | 8 | 8 | Quantity Required |
| 25 | BKBM_REFERENCE | STRING | 20 | — | Reference |
| 26 | BKBM_REV | STRING | 5 | — | Revision (not used) |
| 27 | BKBM_UID | STRING | 20 | — | Unique identifier for BOM entry |

## ISESADTL
**ARCHIVE ESTIMATE DETAIL**

→ Identical schema to ISESTDTL. See ISESTDTL for field descriptions.

## ISESAHDR
**ARCHIVE ESTIMATE HEADER**

→ Identical schema to ISESTHDR. See ISESTHDR for field descriptions.

## ISESALNE
**ARCHIVE ESTIMATE LINES**

→ Identical schema to ISESTLNE. See ISESTLNE for field descriptions.

## ISESTASM
**ARCHIVE ESTIMATES**

→ Identical schema to ESTSUM (MTESUM_ prefix). See ESTSUM for field descriptions.

## ISESTDTL
**ESTIMATE DETAIL**

Fields: 220

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_EST_BOM_FLAG | STRING | 1 | — | BOM attached Y/N |
| 2 | IS_EST_COST_1 | NUMERIC | 8 | 4 | Total cost at qty break 1 |
| 3 | IS_EST_COST_10 | NUMERIC | 8 | 4 | Total cost at qty break 10 |
| 4 | IS_EST_COST_2 | NUMERIC | 8 | 4 | Total cost at qty break 2 |
| 5 | IS_EST_COST_3 | NUMERIC | 8 | 4 | Total cost at qty break 3 |
| 6 | IS_EST_COST_4 | NUMERIC | 8 | 4 | Total cost at qty break 4 |
| 7 | IS_EST_COST_5 | NUMERIC | 8 | 4 | Total cost at qty break 5 |
| 8 | IS_EST_COST_6 | NUMERIC | 8 | 4 | Total cost at qty break 6 |
| 9 | IS_EST_COST_7 | NUMERIC | 8 | 4 | Total cost at qty break 7 |
| 10 | IS_EST_COST_8 | NUMERIC | 8 | 4 | Total cost at qty break 8 |
| 11 | IS_EST_COST_9 | NUMERIC | 8 | 4 | Total cost at qty break 9 |
| 12 | IS_EST_CUST | STRING | 10 | — | Customer code |
| 13 | IS_EST_DRAW | STRING | 15 | — | Drawing number |
| 14 | IS_EST_EX_FLAG | STRING | 1 | — | Exchange / option flag |
| 15 | IS_EST_EXPDTE | DATE | 4 | — | Expiration date |
| 16 | IS_EST_EXTRA2 | STRING | 100 | — | Extra freeform text |
| 17 | IS_EST_EXTRA^ | NUMERIC | 8 | 2 | Extra cost aggregate |
| 18 | IS_EST_EXTRA_1 | NUMERIC | 8 | 4 | Extra cost at qty break 1 |
| 19 | IS_EST_EXTRA_10 | NUMERIC | 8 | 4 | Extra cost at qty break 10 |
| 20 | IS_EST_EXTRA_2 | NUMERIC | 8 | 4 | Extra cost at qty break 2 |
| 21 | IS_EST_EXTRA_3 | NUMERIC | 8 | 4 | Extra cost at qty break 3 |
| 22 | IS_EST_EXTRA_4 | NUMERIC | 8 | 4 | Extra cost at qty break 4 |
| 23 | IS_EST_EXTRA_5 | NUMERIC | 8 | 4 | Extra cost at qty break 5 |
| 24 | IS_EST_EXTRA_6 | NUMERIC | 8 | 4 | Extra cost at qty break 6 |
| 25 | IS_EST_EXTRA_7 | NUMERIC | 8 | 4 | Extra cost at qty break 7 |
| 26 | IS_EST_EXTRA_8 | NUMERIC | 8 | 4 | Extra cost at qty break 8 |
| 27 | IS_EST_EXTRA_9 | NUMERIC | 8 | 4 | Extra cost at qty break 9 |
| 28 | IS_EST_LAB^ | NUMERIC | 8 | 2 | Labor cost aggregate |
| 29 | IS_EST_LAB_1 | NUMERIC | 8 | 4 | Labor cost at qty break 1 |
| 30 | IS_EST_LAB_10 | NUMERIC | 8 | 4 | Labor cost at qty break 10 |
| 31 | IS_EST_LAB_2 | NUMERIC | 8 | 4 | Labor cost at qty break 2 |
| 32 | IS_EST_LAB_3 | NUMERIC | 8 | 4 | Labor cost at qty break 3 |
| 33 | IS_EST_LAB_4 | NUMERIC | 8 | 4 | Labor cost at qty break 4 |
| 34 | IS_EST_LAB_5 | NUMERIC | 8 | 4 | Labor cost at qty break 5 |
| 35 | IS_EST_LAB_6 | NUMERIC | 8 | 4 | Labor cost at qty break 6 |
| 36 | IS_EST_LAB_7 | NUMERIC | 8 | 4 | Labor cost at qty break 7 |
| 37 | IS_EST_LAB_8 | NUMERIC | 8 | 4 | Labor cost at qty break 8 |
| 38 | IS_EST_LAB_9 | NUMERIC | 8 | 4 | Labor cost at qty break 9 |
| 39 | IS_EST_LABMU^ | NUMERIC | 8 | 2 | Labor markup % aggregate |
| 40 | IS_EST_LABMU_1 | NUMERIC | 8 | 4 | Labor markup % at qty break 1 |
| 41 | IS_EST_LABMU_10 | NUMERIC | 8 | 4 | Labor markup % at qty break 10 |
| 42 | IS_EST_LABMU_2 | NUMERIC | 8 | 4 | Labor markup % at qty break 2 |
| 43 | IS_EST_LABMU_3 | NUMERIC | 8 | 4 | Labor markup % at qty break 3 |
| 44 | IS_EST_LABMU_4 | NUMERIC | 8 | 4 | Labor markup % at qty break 4 |
| 45 | IS_EST_LABMU_5 | NUMERIC | 8 | 4 | Labor markup % at qty break 5 |
| 46 | IS_EST_LABMU_6 | NUMERIC | 8 | 4 | Labor markup % at qty break 6 |
| 47 | IS_EST_LABMU_7 | NUMERIC | 8 | 4 | Labor markup % at qty break 7 |
| 48 | IS_EST_LABMU_8 | NUMERIC | 8 | 4 | Labor markup % at qty break 8 |
| 49 | IS_EST_LABMU_9 | NUMERIC | 8 | 4 | Labor markup % at qty break 9 |
| 50 | IS_EST_LINE | NUMERIC | 8 | — | Detail line number (key) |
| 51 | IS_EST_LOSTDTE | DATE | 4 | — | Lost / no-bid date |
| 52 | IS_EST_MAT^ | NUMERIC | 8 | 2 | Material cost aggregate |
| 53 | IS_EST_MAT_1 | NUMERIC | 8 | 4 | Material cost at qty break 1 |
| 54 | IS_EST_MAT_10 | NUMERIC | 8 | 4 | Material cost at qty break 10 |
| 55 | IS_EST_MAT_2 | NUMERIC | 8 | 4 | Material cost at qty break 2 |
| 56 | IS_EST_MAT_3 | NUMERIC | 8 | 4 | Material cost at qty break 3 |
| 57 | IS_EST_MAT_4 | NUMERIC | 8 | 4 | Material cost at qty break 4 |
| 58 | IS_EST_MAT_5 | NUMERIC | 8 | 4 | Material cost at qty break 5 |
| 59 | IS_EST_MAT_6 | NUMERIC | 8 | 4 | Material cost at qty break 6 |
| 60 | IS_EST_MAT_7 | NUMERIC | 8 | 4 | Material cost at qty break 7 |
| 61 | IS_EST_MAT_8 | NUMERIC | 8 | 4 | Material cost at qty break 8 |
| 62 | IS_EST_MAT_9 | NUMERIC | 8 | 4 | Material cost at qty break 9 |
| 63 | IS_EST_MATMU^ | NUMERIC | 8 | 2 | Material markup % aggregate |
| 64 | IS_EST_MATMU_1 | NUMERIC | 8 | 4 | Material markup % at qty break 1 |
| 65 | IS_EST_MATMU_10 | NUMERIC | 8 | 4 | Material markup % at qty break 10 |
| 66 | IS_EST_MATMU_2 | NUMERIC | 8 | 4 | Material markup % at qty break 2 |
| 67 | IS_EST_MATMU_3 | NUMERIC | 8 | 4 | Material markup % at qty break 3 |
| 68 | IS_EST_MATMU_4 | NUMERIC | 8 | 4 | Material markup % at qty break 4 |
| 69 | IS_EST_MATMU_5 | NUMERIC | 8 | 4 | Material markup % at qty break 5 |
| 70 | IS_EST_MATMU_6 | NUMERIC | 8 | 4 | Material markup % at qty break 6 |
| 71 | IS_EST_MATMU_7 | NUMERIC | 8 | 4 | Material markup % at qty break 7 |
| 72 | IS_EST_MATMU_8 | NUMERIC | 8 | 4 | Material markup % at qty break 8 |
| 73 | IS_EST_MATMU_9 | NUMERIC | 8 | 4 | Material markup % at qty break 9 |
| 74 | IS_EST_MEMU^ | NUMERIC | 8 | 2 | Memo markup % aggregate |
| 75 | IS_EST_MEMU_1 | NUMERIC | 8 | 4 | Memo markup % at qty break 1 |
| 76 | IS_EST_MEMU_10 | NUMERIC | 8 | 4 | Memo markup % at qty break 10 |
| 77 | IS_EST_MEMU_2 | NUMERIC | 8 | 4 | Memo markup % at qty break 2 |
| 78 | IS_EST_MEMU_3 | NUMERIC | 8 | 4 | Memo markup % at qty break 3 |
| 79 | IS_EST_MEMU_4 | NUMERIC | 8 | 4 | Memo markup % at qty break 4 |
| 80 | IS_EST_MEMU_5 | NUMERIC | 8 | 4 | Memo markup % at qty break 5 |
| 81 | IS_EST_MEMU_6 | NUMERIC | 8 | 4 | Memo markup % at qty break 6 |
| 82 | IS_EST_MEMU_7 | NUMERIC | 8 | 4 | Memo markup % at qty break 7 |
| 83 | IS_EST_MEMU_8 | NUMERIC | 8 | 4 | Memo markup % at qty break 8 |
| 84 | IS_EST_MEMU_9 | NUMERIC | 8 | 4 | Memo markup % at qty break 9 |
| 85 | IS_EST_MISC^ | NUMERIC | 8 | 2 | Misc cost aggregate |
| 86 | IS_EST_MISC_1 | NUMERIC | 8 | 4 | Misc cost at qty break 1 |
| 87 | IS_EST_MISC_10 | NUMERIC | 8 | 4 | Misc cost at qty break 10 |
| 88 | IS_EST_MISC_2 | NUMERIC | 8 | 4 | Misc cost at qty break 2 |
| 89 | IS_EST_MISC_3 | NUMERIC | 8 | 4 | Misc cost at qty break 3 |
| 90 | IS_EST_MISC_4 | NUMERIC | 8 | 4 | Misc cost at qty break 4 |
| 91 | IS_EST_MISC_5 | NUMERIC | 8 | 4 | Misc cost at qty break 5 |
| 92 | IS_EST_MISC_6 | NUMERIC | 8 | 4 | Misc cost at qty break 6 |
| 93 | IS_EST_MISC_7 | NUMERIC | 8 | 4 | Misc cost at qty break 7 |
| 94 | IS_EST_MISC_8 | NUMERIC | 8 | 4 | Misc cost at qty break 8 |
| 95 | IS_EST_MISC_9 | NUMERIC | 8 | 4 | Misc cost at qty break 9 |
| 96 | IS_EST_NUM | NUMERIC | 8 | — | Estimate number (key) |
| 97 | IS_EST_OH^ | NUMERIC | 8 | 2 | Overhead cost aggregate |
| 98 | IS_EST_OH_1 | NUMERIC | 8 | 4 | Overhead cost at qty break 1 |
| 99 | IS_EST_OH_10 | NUMERIC | 8 | 4 | Overhead cost at qty break 10 |
| 100 | IS_EST_OH_2 | NUMERIC | 8 | 4 | Overhead cost at qty break 2 |
| 101 | IS_EST_OH_3 | NUMERIC | 8 | 4 | Overhead cost at qty break 3 |
| 102 | IS_EST_OH_4 | NUMERIC | 8 | 4 | Overhead cost at qty break 4 |
| 103 | IS_EST_OH_5 | NUMERIC | 8 | 4 | Overhead cost at qty break 5 |
| 104 | IS_EST_OH_6 | NUMERIC | 8 | 4 | Overhead cost at qty break 6 |
| 105 | IS_EST_OH_7 | NUMERIC | 8 | 4 | Overhead cost at qty break 7 |
| 106 | IS_EST_OH_8 | NUMERIC | 8 | 4 | Overhead cost at qty break 8 |
| 107 | IS_EST_OH_9 | NUMERIC | 8 | 4 | Overhead cost at qty break 9 |
| 108 | IS_EST_OHMU^ | NUMERIC | 8 | 2 | Overhead markup % aggregate |
| 109 | IS_EST_OHMU_1 | NUMERIC | 8 | 4 | Overhead markup % at qty break 1 |
| 110 | IS_EST_OHMU_10 | NUMERIC | 8 | 4 | Overhead markup % at qty break 10 |
| 111 | IS_EST_OHMU_2 | NUMERIC | 8 | 4 | Overhead markup % at qty break 2 |
| 112 | IS_EST_OHMU_3 | NUMERIC | 8 | 4 | Overhead markup % at qty break 3 |
| 113 | IS_EST_OHMU_4 | NUMERIC | 8 | 4 | Overhead markup % at qty break 4 |
| 114 | IS_EST_OHMU_5 | NUMERIC | 8 | 4 | Overhead markup % at qty break 5 |
| 115 | IS_EST_OHMU_6 | NUMERIC | 8 | 4 | Overhead markup % at qty break 6 |
| 116 | IS_EST_OHMU_7 | NUMERIC | 8 | 4 | Overhead markup % at qty break 7 |
| 117 | IS_EST_OHMU_8 | NUMERIC | 8 | 4 | Overhead markup % at qty break 8 |
| 118 | IS_EST_OHMU_9 | NUMERIC | 8 | 4 | Overhead markup % at qty break 9 |
| 119 | IS_EST_OL^ | NUMERIC | 8 | 2 | Outside labor cost aggregate |
| 120 | IS_EST_OLMU^ | NUMERIC | 8 | 2 | Outside labor markup % aggregate |
| 121 | IS_EST_OP^ | NUMERIC | 8 | 2 | Outside process cost aggregate |
| 122 | IS_EST_OP_1 | NUMERIC | 8 | 4 | Outside process cost at qty break 1 |
| 123 | IS_EST_OP_10 | NUMERIC | 8 | 4 | Outside process cost at qty break 10 |
| 124 | IS_EST_OP_2 | NUMERIC | 8 | 4 | Outside process cost at qty break 2 |
| 125 | IS_EST_OP_3 | NUMERIC | 8 | 4 | Outside process cost at qty break 3 |
| 126 | IS_EST_OP_4 | NUMERIC | 8 | 4 | Outside process cost at qty break 4 |
| 127 | IS_EST_OP_5 | NUMERIC | 8 | 4 | Outside process cost at qty break 5 |
| 128 | IS_EST_OP_6 | NUMERIC | 8 | 4 | Outside process cost at qty break 6 |
| 129 | IS_EST_OP_7 | NUMERIC | 8 | 4 | Outside process cost at qty break 7 |
| 130 | IS_EST_OP_8 | NUMERIC | 8 | 4 | Outside process cost at qty break 8 |
| 131 | IS_EST_OP_9 | NUMERIC | 8 | 4 | Outside process cost at qty break 9 |
| 132 | IS_EST_OPMU^ | NUMERIC | 8 | 2 | Outside process markup % aggregate |
| 133 | IS_EST_OPMU_1 | NUMERIC | 8 | 4 | Outside process markup % at qty break 1 |
| 134 | IS_EST_OPMU_10 | NUMERIC | 8 | 4 | Outside process markup % at qty break 10 |
| 135 | IS_EST_OPMU_2 | NUMERIC | 8 | 4 | Outside process markup % at qty break 2 |
| 136 | IS_EST_OPMU_3 | NUMERIC | 8 | 4 | Outside process markup % at qty break 3 |
| 137 | IS_EST_OPMU_4 | NUMERIC | 8 | 4 | Outside process markup % at qty break 4 |
| 138 | IS_EST_OPMU_5 | NUMERIC | 8 | 4 | Outside process markup % at qty break 5 |
| 139 | IS_EST_OPMU_6 | NUMERIC | 8 | 4 | Outside process markup % at qty break 6 |
| 140 | IS_EST_OPMU_7 | NUMERIC | 8 | 4 | Outside process markup % at qty break 7 |
| 141 | IS_EST_OPMU_8 | NUMERIC | 8 | 4 | Outside process markup % at qty break 8 |
| 142 | IS_EST_OPMU_9 | NUMERIC | 8 | 4 | Outside process markup % at qty break 9 |
| 143 | IS_EST_OPPTYPE | STRING | 2 | — | Opportunity type (2-char code) |
| 144 | IS_EST_ORDDESC | STRING | 30 | — | Order description |
| 145 | IS_EST_ORDDTE | DATE | 4 | — | Order date |
| 146 | IS_EST_OVALL^ | NUMERIC | 8 | 2 | Overall margin % aggregate |
| 147 | IS_EST_OVALL_1 | NUMERIC | 8 | 4 | Overall margin % at qty break 1 |
| 148 | IS_EST_OVALL_10 | NUMERIC | 8 | 4 | Overall margin % at qty break 10 |
| 149 | IS_EST_OVALL_2 | NUMERIC | 8 | 4 | Overall margin % at qty break 2 |
| 150 | IS_EST_OVALL_3 | NUMERIC | 8 | 4 | Overall margin % at qty break 3 |
| 151 | IS_EST_OVALL_4 | NUMERIC | 8 | 4 | Overall margin % at qty break 4 |
| 152 | IS_EST_OVALL_5 | NUMERIC | 8 | 4 | Overall margin % at qty break 5 |
| 153 | IS_EST_OVALL_6 | NUMERIC | 8 | 4 | Overall margin % at qty break 6 |
| 154 | IS_EST_OVALL_7 | NUMERIC | 8 | 4 | Overall margin % at qty break 7 |
| 155 | IS_EST_OVALL_8 | NUMERIC | 8 | 4 | Overall margin % at qty break 8 |
| 156 | IS_EST_OVALL_9 | NUMERIC | 8 | 4 | Overall margin % at qty break 9 |
| 157 | IS_EST_OVLMU^ | NUMERIC | 8 | 2 | Overall markup % aggregate |
| 158 | IS_EST_PART | STRING | 15 | — | Part code (key) |
| 159 | IS_EST_PRICE_1 | NUMERIC | 8 | 4 | Unit price at qty break 1 |
| 160 | IS_EST_PRICE_10 | NUMERIC | 8 | 4 | Unit price at qty break 10 |
| 161 | IS_EST_PRICE_2 | NUMERIC | 8 | 4 | Unit price at qty break 2 |
| 162 | IS_EST_PRICE_3 | NUMERIC | 8 | 4 | Unit price at qty break 3 |
| 163 | IS_EST_PRICE_4 | NUMERIC | 8 | 4 | Unit price at qty break 4 |
| 164 | IS_EST_PRICE_5 | NUMERIC | 8 | 4 | Unit price at qty break 5 |
| 165 | IS_EST_PRICE_6 | NUMERIC | 8 | 4 | Unit price at qty break 6 |
| 166 | IS_EST_PRICE_7 | NUMERIC | 8 | 4 | Unit price at qty break 7 |
| 167 | IS_EST_PRICE_8 | NUMERIC | 8 | 4 | Unit price at qty break 8 |
| 168 | IS_EST_PRICE_9 | NUMERIC | 8 | 4 | Unit price at qty break 9 |
| 169 | IS_EST_QTREV | STRING | 9 | — | Quote revision level |
| 170 | IS_EST_QTY_1 | NUMERIC | 8 | 2 | Quantity break 1 |
| 171 | IS_EST_QTY_10 | NUMERIC | 8 | 2 | Quantity break 10 |
| 172 | IS_EST_QTY_2 | NUMERIC | 8 | 2 | Quantity break 2 |
| 173 | IS_EST_QTY_3 | NUMERIC | 8 | 2 | Quantity break 3 |
| 174 | IS_EST_QTY_4 | NUMERIC | 8 | 2 | Quantity break 4 |
| 175 | IS_EST_QTY_5 | NUMERIC | 8 | 2 | Quantity break 5 |
| 176 | IS_EST_QTY_6 | NUMERIC | 8 | 2 | Quantity break 6 |
| 177 | IS_EST_QTY_7 | NUMERIC | 8 | 2 | Quantity break 7 |
| 178 | IS_EST_QTY_8 | NUMERIC | 8 | 2 | Quantity break 8 |
| 179 | IS_EST_QTY_9 | NUMERIC | 8 | 2 | Quantity break 9 |
| 180 | IS_EST_QUICK | STRING | 1 | — | Quick-add estimate flag Y/N |
| 181 | IS_EST_REV | STRING | 5 | — | Part revision level |
| 182 | IS_EST_RT_FLAG | STRING | 1 | — | Routing attached Y/N |
| 183 | IS_EST_SETMU | NUMERIC | 8 | 4 | Setup markup % |
| 184 | IS_EST_SETMU^ | NUMERIC | 8 | 2 | Setup markup % aggregate |
| 185 | IS_EST_SETUP^ | NUMERIC | 8 | 2 | Setup cost aggregate |
| 186 | IS_EST_SETUP_1 | NUMERIC | 8 | 4 | Setup cost at qty break 1 |
| 187 | IS_EST_SETUP_10 | NUMERIC | 8 | 4 | Setup cost at qty break 10 |
| 188 | IS_EST_SETUP_2 | NUMERIC | 8 | 4 | Setup cost at qty break 2 |
| 189 | IS_EST_SETUP_3 | NUMERIC | 8 | 4 | Setup cost at qty break 3 |
| 190 | IS_EST_SETUP_4 | NUMERIC | 8 | 4 | Setup cost at qty break 4 |
| 191 | IS_EST_SETUP_5 | NUMERIC | 8 | 4 | Setup cost at qty break 5 |
| 192 | IS_EST_SETUP_6 | NUMERIC | 8 | 4 | Setup cost at qty break 6 |
| 193 | IS_EST_SETUP_7 | NUMERIC | 8 | 4 | Setup cost at qty break 7 |
| 194 | IS_EST_SETUP_8 | NUMERIC | 8 | 4 | Setup cost at qty break 8 |
| 195 | IS_EST_SETUP_9 | NUMERIC | 8 | 4 | Setup cost at qty break 9 |
| 196 | IS_EST_SO | NUMERIC | 8 | — | Sales order number (if converted from estimate) |
| 197 | IS_EST_STATUS | STRING | 1 | — | Estimate status code |
| 198 | IS_EST_TEMP_NUM | INTEGER | 2 | — | Template number |
| 199 | IS_EST_TOTAL_1 | NUMERIC | 8 | 4 | Grand total at qty break 1 |
| 200 | IS_EST_TOTAL_10 | NUMERIC | 8 | 4 | Grand total at qty break 10 |
| 201 | IS_EST_TOTAL_2 | NUMERIC | 8 | 4 | Grand total at qty break 2 |
| 202 | IS_EST_TOTAL_3 | NUMERIC | 8 | 4 | Grand total at qty break 3 |
| 203 | IS_EST_TOTAL_4 | NUMERIC | 8 | 4 | Grand total at qty break 4 |
| 204 | IS_EST_TOTAL_5 | NUMERIC | 8 | 4 | Grand total at qty break 5 |
| 205 | IS_EST_TOTAL_6 | NUMERIC | 8 | 4 | Grand total at qty break 6 |
| 206 | IS_EST_TOTAL_7 | NUMERIC | 8 | 4 | Grand total at qty break 7 |
| 207 | IS_EST_TOTAL_8 | NUMERIC | 8 | 4 | Grand total at qty break 8 |
| 208 | IS_EST_TOTAL_9 | NUMERIC | 8 | 4 | Grand total at qty break 9 |
| 209 | IS_EST_VOVHD_1 | NUMERIC | 8 | 4 | Variable overhead at qty break 1 |
| 210 | IS_EST_VOVHD_10 | NUMERIC | 8 | 4 | Variable overhead at qty break 10 |
| 211 | IS_EST_VOVHD_2 | NUMERIC | 8 | 4 | Variable overhead at qty break 2 |
| 212 | IS_EST_VOVHD_3 | NUMERIC | 8 | 4 | Variable overhead at qty break 3 |
| 213 | IS_EST_VOVHD_4 | NUMERIC | 8 | 4 | Variable overhead at qty break 4 |
| 214 | IS_EST_VOVHD_5 | NUMERIC | 8 | 4 | Variable overhead at qty break 5 |
| 215 | IS_EST_VOVHD_6 | NUMERIC | 8 | 4 | Variable overhead at qty break 6 |
| 216 | IS_EST_VOVHD_7 | NUMERIC | 8 | 4 | Variable overhead at qty break 7 |
| 217 | IS_EST_VOVHD_8 | NUMERIC | 8 | 4 | Variable overhead at qty break 8 |
| 218 | IS_EST_VOVHD_9 | NUMERIC | 8 | 4 | Variable overhead at qty break 9 |
| 219 | IS_EST_WOPRE | NUMERIC | 8 | — | Work order prefix (if converted from estimate) |
| 220 | IS_EST_WOSUF | INTEGER | 2 | — | Work order suffix (if converted from estimate) |

## ISESTHDR
**ESTIMATE HEADER**

Fields: 82

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INV_BILA1 | STRING | 30 | — | Billing Address 1 |
| 2 | BKAR_INV_BILA2 | STRING | 30 | — | Billing Address 2 |
| 3 | BKAR_INV_BILA3 | STRING | 30 | — | Billing Address 3 |
| 4 | BKAR_INV_BILATN | STRING | 30 | — | Billing Attention |
| 5 | BKAR_INV_BILCNT | STRING | 30 | — | Billing Country |
| 6 | BKAR_INV_BILCOD | STRING | 10 | — | Bill To Code |
| 7 | BKAR_INV_BILCTY | STRING | 30 | — | Billing City |
| 8 | BKAR_INV_BILNME | STRING | 30 | — | Bill To Name |
| 9 | BKAR_INV_BILST | STRING | 2 | — | Billing State |
| 10 | BKAR_INV_BILZIP | STRING | 10 | — | Billing ZIP |
| 11 | BKAR_INV_CCOAMT | NUMERIC | 8 | 2 | Credit card overcharge amount |
| 12 | BKAR_INV_CHKNUM | NUMERIC | 8 | — | Check Number |
| 13 | BKAR_INV_COGS | NUMERIC | 8 | 2 | COGS |
| 14 | BKAR_INV_COMAMT | NUMERIC | 8 | 2 | Commission amount |
| 15 | BKAR_INV_COMMPR_1 | NUMERIC | 8 | 4 | Commission % salesperson 1 |
| 16 | BKAR_INV_COMMPR_2 | NUMERIC | 8 | 4 | Commission % salesperson 2 |
| 17 | BKAR_INV_CUSA1 | STRING | 30 | — | Customer Address 1 |
| 18 | BKAR_INV_CUSA2_1 | STRING | 30 | — | Customer Address 2 line 1 |
| 19 | BKAR_INV_CUSA2_2 | STRING | 30 | — | Customer Address 2 line 2 |
| 20 | BKAR_INV_CUSATT | STRING | 30 | — | Attention: |
| 21 | BKAR_INV_CUSCNT | STRING | 30 | — | Country |
| 22 | BKAR_INV_CUSCOD | STRING | 10 | — | Customer Code |
| 23 | BKAR_INV_CUSCTY | STRING | 26 | — | City |
| 24 | BKAR_INV_CUSNME | STRING | 30 | — | Customer Name |
| 25 | BKAR_INV_CUSORD | STRING | 25 | — | Customer Order |
| 26 | BKAR_INV_CUSST | STRING | 2 | — | State |
| 27 | BKAR_INV_CUSZIP | STRING | 10 | — | ZIP Code |
| 28 | BKAR_INV_DCODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_INV_DEPAMT | NUMERIC | 8 | 2 | Deposit amount |
| 30 | BKAR_INV_DESC | STRING | 30 | — | Orser Description |
| 31 | BKAR_INV_ENDLNE | STRING | 1 | — | Ending lines Y/N |
| 32 | BKAR_INV_ENTBY | STRING | 5 | — | Entered By |
| 33 | BKAR_INV_EXTRA | STRING | 150 | — | Extra |
| 34 | BKAR_INV_FOB | STRING | 15 | — | FOB |
| 35 | BKAR_INV_FRGHT | NUMERIC | 8 | 2 | Freight Amount |
| 36 | BKAR_INV_GLDPT | STRING | 4 | — | GL Department |
| 37 | BKAR_INV_INDATE | DATE | 4 | — | Date entered / document date |
| 38 | BKAR_INV_INVCD | STRING | 1 | — | INVCD X/P/Y |
| 39 | BKAR_INV_INVDTE | DATE | 4 | — | Invoice Date |
| 40 | BKAR_INV_ISCUR | STRING | 3 | — | Currency code (ISO 3-char) |
| 41 | BKAR_INV_ISMCDT | DATE | 4 | — | IS module change date |
| 42 | BKAR_INV_ISREV | STRING | 1 | — | IS revision flag |
| 43 | BKAR_INV_ISRVDT | DATE | 4 | — | IS revision date |
| 44 | BKAR_INV_ISTXKY | STRING | 10 | — | IS tax key |
| 45 | BKAR_INV_ITMZTX_1 | STRING | 1 | — | Item tax zone 1 |
| 46 | BKAR_INV_ITMZTX_2 | STRING | 1 | — | Item tax zone 2 |
| 47 | BKAR_INV_JOBNUM | STRING | 15 | — | Job Number 1 |
| 48 | BKAR_INV_LINV^P | NUMERIC | 8 | — | Last invoice pre-count |
| 49 | BKAR_INV_LOC | STRING | 10 | — | Location |
| 50 | BKAR_INV_NL | INTEGER | 2 | — | Number Lines |
| 51 | BKAR_INV_NUM | NUMERIC | 8 | — | Invoice Number |
| 52 | BKAR_INV_ORDDTE | DATE | 4 | — | Order Date |
| 53 | BKAR_INV_PCODE | INTEGER | 2 | — | Price Code |
| 54 | BKAR_INV_RELNUM | NUMERIC | 8 | — | Related order number |
| 55 | BKAR_INV_RETEN | NUMERIC | 8 | 2 | Retention / holdback amount |
| 56 | BKAR_INV_RTS | STRING | 1 | — | Ready To Ship Y/N |
| 57 | BKAR_INV_SCCOGS | NUMERIC | 8 | 2 | Supply chain COGS |
| 58 | BKAR_INV_SHIPDT | DATE | 4 | — | Ship Date |
| 59 | BKAR_INV_SHIPPR | NUMERIC | 8 | — | Shipper Number |
| 60 | BKAR_INV_SHPA1 | STRING | 30 | — | Ship Address 1 |
| 61 | BKAR_INV_SHPA2_1 | STRING | 30 | — | Ship Address 2 line 1 |
| 62 | BKAR_INV_SHPA2_2 | STRING | 30 | — | Ship Address 2 line 2 |
| 63 | BKAR_INV_SHPATN | STRING | 30 | — | Ship Attention |
| 64 | BKAR_INV_SHPCNT | STRING | 30 | — | Ship Country |
| 65 | BKAR_INV_SHPCOD | STRING | 10 | — | Ship To Code |
| 66 | BKAR_INV_SHPCTY | STRING | 26 | — | Ship City |
| 67 | BKAR_INV_SHPNME | STRING | 30 | — | Ship Name |
| 68 | BKAR_INV_SHPST | STRING | 2 | — | Shop State |
| 69 | BKAR_INV_SHPVIA | STRING | 15 | — | Ship Via |
| 70 | BKAR_INV_SHPZIP | STRING | 10 | — | Ship ZIP Code |
| 71 | BKAR_INV_SLSP | INTEGER | 2 | — | Salesperson 1 |
| 72 | BKAR_INV_SLSP2 | INTEGER | 2 | — | Sales Person 2 |
| 73 | BKAR_INV_SONUM | NUMERIC | 8 | — | Sales Order   Number |
| 74 | BKAR_INV_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 75 | BKAR_INV_TAXABL | STRING | 1 | — | Taxable Y/N |
| 76 | BKAR_INV_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 77 | BKAR_INV_TAXKEY | STRING | 4 | — | Tax key (4-char) |
| 78 | BKAR_INV_TAXRTE | NUMERIC | 8 | 4 | Tax Rate |
| 79 | BKAR_INV_TERMD | STRING | 10 | — | Terms Description |
| 80 | BKAR_INV_TERMNM | INTEGER | 2 | — | Terms Number |
| 81 | BKAR_INV_TOTAL | NUMERIC | 8 | 2 | Total |
| 82 | BKAR_INV_TRACK | STRING | 40 | — | Tracking number |

## ISESTLNE
**ESTIMATE LINES**

Fields: 29

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVL_ABQTY | NUMERIC | 8 | 2 | options Quantity |
| 2 | BKAR_INVL_ASD | DATE | 4 | — | Actual Ship Date |
| 3 | BKAR_INVL_CNTR | INTEGER | 2 | — | Line Counter |
| 4 | BKAR_INVL_COMPR_1 | NUMERIC | 8 | 4 | Commission % salesperson 1 |
| 5 | BKAR_INVL_COMPR_2 | NUMERIC | 8 | 4 | Commission % salesperson 2 |
| 6 | BKAR_INVL_COOP | NUMERIC | 8 | 2 | Co-op allowance |
| 7 | BKAR_INVL_ESD | DATE | 4 | — | Estimated Ship Date |
| 8 | BKAR_INVL_EXTRA | STRING | 100 | — | Extra |
| 9 | BKAR_INVL_FRGHT | NUMERIC | 8 | 2 | Freight |
| 10 | BKAR_INVL_INVNM | NUMERIC | 8 | — | Sales Order Number |
| 11 | BKAR_INVL_ITYPE | STRING | 1 | — | Part Type |
| 12 | BKAR_INVL_JOB^ | STRING | 10 | — | Job number (alternate key) |
| 13 | BKAR_INVL_LOC | STRING | 10 | — | Location |
| 14 | BKAR_INVL_OOQTY | NUMERIC | 8 | 2 | Original Order Quantity |
| 15 | BKAR_INVL_PCODE | STRING | 15 | — | Part Code |
| 16 | BKAR_INVL_PCOGS | NUMERIC | 8 | 4 | COGS |
| 17 | BKAR_INVL_PDESC | STRING | 30 | — | Part Description |
| 18 | BKAR_INVL_PDISC | NUMERIC | 8 | 2 | Discount |
| 19 | BKAR_INVL_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 20 | BKAR_INVL_PPRCE | NUMERIC | 8 | 4 | Price |
| 21 | BKAR_INVL_PQTY | NUMERIC | 8 | 2 | Quantity |
| 22 | BKAR_INVL_RTS | STRING | 1 | — | Ready to Ship |
| 23 | BKAR_INVL_SCCOG | NUMERIC | 8 | 4 | Supply chain COGS |
| 24 | BKAR_INVL_TXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 25 | BKAR_INVL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 26 | BKAR_INVL_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 27 | BKAR_INVL_UM_LN_1 | STRING | 3 | — | Unit of measure — alternate 1 |
| 28 | BKAR_INVL_UM_LN_2 | STRING | 3 | — | Unit of measure — alternate 2 |
| 29 | BKAR_INVL_USTD | NUMERIC | 8 | 2 | Units Shipped To Date |

## ISESTPO
**ESTIMATE RFQ**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_PO_CONF | STRING | 1 | — | Confirmation received Y/N |
| 2 | BKMRP_PO_DATE | DATE | 4 | — | RFQ date |
| 3 | BKMRP_PO_DONE | STRING | 10 | — | RFQ done / complete indicator |
| 4 | BKMRP_PO_ERD | DATE | 4 | — | Expected receipt date |
| 5 | BKMRP_PO_EST | STRING | 10 | — | Estimate number (key) |
| 6 | BKMRP_PO_ESTLNE | NUMERIC | 8 | — | Estimate line number (key) |
| 7 | BKMRP_PO_EXTRA | STRING | 50 | — | Extra freeform field |
| 8 | BKMRP_PO_MTREC | INTEGER | 4 | — | MRP record number |
| 9 | BKMRP_PO_PART | STRING | 15 | — | Part code |
| 10 | BKMRP_PO_PLANR | STRING | 4 | — | Planner code |
| 11 | BKMRP_PO_PRICE | NUMERIC | 8 | 4 | Quoted price from vendor |
| 12 | BKMRP_PO_QTY | NUMERIC | 8 | 2 | RFQ quantity |
| 13 | BKMRP_PO_UID | STRING | 20 | — | Unique identifier |
| 14 | BKMRP_PO_VEND | STRING | 10 | — | Vendor code |
| 15 | BKMRP_PO_WOPRE | NUMERIC | 8 | — | Work order prefix |
| 16 | BKMRP_PO_WOSUF | INTEGER | 2 | — | Work order suffix |

## ISICEST
**ESTIMATING INVENTORY MASTER**

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
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | Long part number (not used) |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | Manufacturer name |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | Net gross profit last year |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | Net gross profit month-to-date |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | Net gross profit variance |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | Net gross profit year-to-date |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | Price matrix code |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | Total on-hand book value |
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

## ISMICESA
**ARCHIVED ESTIMATNG ITEM MASTER**

→ Identical schema to ISMICEST. See ISMICEST for field descriptions.

## ISMICEST
**ESTIMATNG ITEM MASTER**

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
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | Freight amount aggregate |
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
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | Option price type code |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | Recurring cost tier 1 |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | Recurring cost tier 10 |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | Recurring cost tier 11 |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | Recurring cost tier 12 |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | Recurring cost tier 13 |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | Recurring cost tier 14 |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | Recurring cost tier 15 |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | Recurring cost tier 2 |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | Recurring cost tier 3 |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | Recurring cost tier 4 |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | Recurring cost tier 5 |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | Recurring cost tier 6 |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | Recurring cost tier 7 |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | Recurring cost tier 8 |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | Recurring cost tier 9 |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | Specification line 1 |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | Specification line 10 |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | Specification line 11 |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | Specification line 12 |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | Specification line 2 |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | Specification line 3 |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | Specification line 4 |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | Specification line 5 |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | Specification line 6 |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | Specification line 7 |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | Specification line 8 |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | Specification line 9 |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | Substitute part code 1 |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | Substitute part code 2 |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | Substitute part code 3 |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | Substitute part code 4 |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | Substitute part code 5 |
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
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | Preferred vendor name 1 |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | Preferred vendor name 10 |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | Preferred vendor name 2 |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | Preferred vendor name 3 |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | Preferred vendor name 4 |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | Preferred vendor name 5 |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | Preferred vendor name 6 |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | Preferred vendor name 7 |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | Preferred vendor name 8 |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | Preferred vendor name 9 |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | Vendor part code 1 |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | Vendor part code 2 |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | Vendor part code 3 |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | Vendor part code 4 |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | Vendor part code 5 |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | Vendor part code 6 |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | Vendor part code 7 |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | Vendor part code 8 |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | Vendor part code 9 |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## ISRTESA
**ARCHIVED ESTIMATING ROUTING**

→ Identical schema to ISRTEST. See ISRTEST for field descriptions.

## ISRTEST
**ESTIMATING ROUTING**

Fields: 62

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTRO_CLASS | STRING | 15 | — | not used |
| 2 | MTRO_CODE | STRING | 15 | — | Part Code |
| 3 | MTRO_DEF_TIME | TIME | 4 | — | Default cycle time |
| 4 | MTRO_DESC | STRING | 30 | — | Description |
| 5 | MTRO_EST_LINE | NUMERIC | 8 | — | Estimate line number (key) |
| 6 | MTRO_EST_TAG | STRING | 10 | — | Estimate tag / identifier (key) |
| 7 | MTRO_EXTRA | STRING | 150 | — | Extra |
| 8 | MTRO_FOVHD | NUMERIC | 8 | 4 | Fixed Overhead Rate |
| 9 | MTRO_INSTR_1 | STRING | 60 | — | Work instruction line 1 |
| 10 | MTRO_INSTR_10 | STRING | 60 | — | Work instruction line 10 |
| 11 | MTRO_INSTR_11 | STRING | 60 | — | Work instruction line 11 |
| 12 | MTRO_INSTR_12 | STRING | 60 | — | Work instruction line 12 |
| 13 | MTRO_INSTR_13 | STRING | 60 | — | Work instruction line 13 |
| 14 | MTRO_INSTR_14 | STRING | 60 | — | Work instruction line 14 |
| 15 | MTRO_INSTR_15 | STRING | 60 | — | Work instruction line 15 |
| 16 | MTRO_INSTR_2 | STRING | 60 | — | Work instruction line 2 |
| 17 | MTRO_INSTR_3 | STRING | 60 | — | Work instruction line 3 |
| 18 | MTRO_INSTR_4 | STRING | 60 | — | Work instruction line 4 |
| 19 | MTRO_INSTR_5 | STRING | 60 | — | Work instruction line 5 |
| 20 | MTRO_INSTR_6 | STRING | 60 | — | Work instruction line 6 |
| 21 | MTRO_INSTR_7 | STRING | 60 | — | Work instruction line 7 |
| 22 | MTRO_INSTR_8 | STRING | 60 | — | Work instruction line 8 |
| 23 | MTRO_INSTR_9 | STRING | 60 | — | Work instruction line 9 |
| 24 | MTRO_LABOR | NUMERIC | 8 | 4 | Labor Rate |
| 25 | MTRO_LEAD | INTEGER | 2 | — | Lead Time |
| 26 | MTRO_LONGTIME | NUMERIC | 8 | 7 | Longtime - Decimal Hrs. |
| 27 | MTRO_LOTSIZE | NUMERIC | 8 | — | Lot Size |
| 28 | MTRO_MACHINE | NUMERIC | 8 | 4 | Machine Rate |
| 29 | MTRO_MD_PROC_HR | STRING | 1 | — | Minutes/decimal or processes per hour flag |
| 30 | MTRO_MIN_CHG | NUMERIC | 8 | 2 | Minimum Charge (Outside Process) |
| 31 | MTRO_MISC_ACOST | NUMERIC | 8 | 2 | Misc accumulated cost |
| 32 | MTRO_NEGOVLP | NUMERIC | 8 | 2 | Negative Overlap |
| 33 | MTRO_NUM | INTEGER | 2 | — | Routing Number |
| 34 | MTRO_NUM_PERSON | NUMERIC | 8 | 2 | Number of Persons |
| 35 | MTRO_NUM_PROCES | INTEGER | 2 | — | Number of Processes |
| 36 | MTRO_OP_TEMP_NO | INTEGER | 2 | — | Template Number |
| 37 | MTRO_OPER | INTEGER | 2 | — | Operation |
| 38 | MTRO_OPERDESC | STRING | 30 | — | Operation Desciption |
| 39 | MTRO_OVERLAP | INTEGER | 2 | — | Overlap Hrs. |
| 40 | MTRO_PARTSHR | NUMERIC | 8 | 2 | Parts/Hour |
| 41 | MTRO_PIECE_RATE | NUMERIC | 8 | 2 | Piece Rate |
| 42 | MTRO_PRINT | STRING | 1 | — | not used |
| 43 | MTRO_PROC_PERHR | NUMERIC | 8 | 2 | Processes Per Hour |
| 44 | MTRO_R_TYPE | STRING | 10 | — | Routing type code (M=Machine, L=Labor, O=Outside) |
| 45 | MTRO_SETUP | NUMERIC | 8 | 4 | Setup Rate |
| 46 | MTRO_SETUPHRS | TIME | 4 | — | Setup Hours |
| 47 | MTRO_STD_TIME | STRING | 1 | — | Standard Time Y/N |
| 48 | MTRO_TIME_PERPR | TIME | 4 | — | Time per process |
| 49 | MTRO_TIMEPART | TIME | 4 | — | Time/Part |
| 50 | MTRO_TMACHDESC | STRING | 30 | — | Machine Description |
| 51 | MTRO_TMACHINE | STRING | 4 | — | Machine Code |
| 52 | MTRO_TOOL | STRING | 15 | — | Tool Code |
| 53 | MTRO_TOOLDESC | STRING | 30 | — | Tool Description |
| 54 | MTRO_TYPE | STRING | 1 | — | Type |
| 55 | MTRO_VENDCODE | STRING | 10 | — | Vendor Code |
| 56 | MTRO_VENDCOST | NUMERIC | 8 | 6 | Vendor Cost |
| 57 | MTRO_VENDNAME | STRING | 25 | — | Vendor Name |
| 58 | MTRO_VOVHD | NUMERIC | 8 | 4 | Variable Overhead Rate |
| 59 | MTRO_WC | STRING | 12 | — | Work Center |
| 60 | MTRO_WCDESC | STRING | 30 | — | Work Center Description |
| 61 | MTWO_MISC_COST | NUMERIC | 8 | 2 | Misc. Cost |
| 62 | MTWO_MISC_DESC | STRING | 30 | — | Misc. Description |
