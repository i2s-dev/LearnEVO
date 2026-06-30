# EvoERP -- Primary Key Reference (Complete)
Status: complete | verified-from-live-ODBC | Pass359 2026-06-26 | updated Pass407 2026-06-30

**Method (Pass 407 update):** Live ODBC query against DSN=DBA — `X$Index JOIN X$Field JOIN X$File`
where `Xi$Number = 0` (index segment 0 = primary key). `Xi$Field` joins to `Xe$Id` in X$Field.
Script: `scripts/extract_primary_keys.py`. Output: `samples/primary_keys.csv`.

This supersedes the Pass 359 binary INDEX.DDF parse (656 tables). ODBC is authoritative.

| Table count | PK confirmed | No PK in DDF | Notes |
|-------------|-------------|--------------|-------|
| 715 | 711 | 4 | ODBC live query 2026-06-30 |

Tables with **no index 0** in DDF: `BKSYHELP`, `ISDLCK1`, `ISDLCK2`, `TESTARRA`
— these are singleton config rows or write-only temp tables with no Btrieve PK defined.

**Primary key structure:**
- Single-field PKs: 532 tables
- Compound PKs (2+ fields): 179 tables

**DDF vs Btrieve-only architecture note:**
The 715 tables in DDF are accessible via ODBC (DSN=DBA). However, several major operational
modules use tables that are **NOT** in the DDF — they are Btrieve-only and accessible only via
TAS Pro direct file I/O. Known Btrieve-only (not in DDF) tables include:
- Main SO (Sales Order) header/line tables — only IS* extension tables (ISSOAINF etc.) are in DDF
- Main AP/AR/PO history might be archived to Btrieve-only files
- AHSYMSTR (user security master) — not in DDF under that name
Operational WO tables ARE in DDF: `WORKORD` (PK `MTWO_WIP_WOPRE`), `WORKHORD` (history),
`WOBOM` (BOM), `WOROUT` (routing), etc.

## AHSY

| Table | Primary Key (index 0) |
|-------|----------------------|
| AHSYLOG | AHSY_USER_LEVL + AHSY_USER_MENU |

## ARTT

| Table | Primary Key (index 0) |
|-------|----------------------|
| ARTTEMP | BKART_TRXN |

## BKAB

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKABCUST | BKAB_START |
| BKABVEND | BKAB_SERIAL |

## BKAC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKACTRPT | BKAC_TYPE + BKAC_NAME |

## BKAP

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKAPACCN | BKCM_ACCN_CODE |
| BKAPADSC | BK_DESC_CODE |
| BKAPAPO | BKAP_PO_NUM |
| BKAPAPOL | BKAP_POL_PONM |
| BKAPCHKF | BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| BKAPCHKH | BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| BKAPDEP | BKAR_DEP_DEPNO |
| BKAPDESC | BK_DESC_CODE |
| BKAPEIVT | BKAP_INVT_CODE |
| BKAPEVND | BKAP_VENDCODE |
| BKAPHDSC | BK_DESC_CODE |
| BKAPHPO | BKAP_PO_NUM |
| BKAPHPOL | BKAP_POL_PONM |
| BKAPINVL | BKAP_INVL_CODE + BKAP_INVL_NUM |
| BKAPINVT | BKAP_INVT_CODE |
| BKAPNOTE | BKAP_NOTE_SRCH1 + BKAP_NOTE_SRCH2 + BKAP_NOTE_DATE + BKAP_NOTE_ENTBY |
| BKAPPO | BKAP_PO_NUM |
| BKAPPOL | BKAP_POL_PONM |
| BKAPQUOT | BKRFQ_NUM |
| BKAPRFQ | BKAP_PO_NUM |
| BKAPRFQL | BKAP_POL_PONM |
| BKAPRIVL | BKAP_INVL_CODE + BKAP_INVL_NUM |
| BKAPVEND | BKAP_VENDCODE |
| BKAPVND2 | BKAP2_VENDCODE |

## BKAR

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKARCHKF | BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| BKARCHKH | BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| BKARCUST | BKAR_CUSTCODE |
| BKARDEP | BKAR_DEP_DEPNO |
| BKARDESC | BK_DESC_CODE |
| BKARDPST | BK_DESC_CODE + ?24 |
| BKARECST | BKAR_CUSTCODE |
| BKAREIVT | BKAR_INVT_CODE + BKAR_INVT_DATE + BKAR_INVT_NUM |
| BKARHDSC | BK_DESC_CODE |
| BKARHINV | BKAR_INV_NUM |
| BKARHIVL | BKAR_INVL_INVNM |
| BKARHTAX | BKAR_TAX_INVNO |
| BKARINV | BKAR_INV_NUM |
| BKARINVI | BKAR_INVI_SONUM |
| BKARINVL | BKAR_INVL_INVNM |
| BKARINVT | BKAR_INVT_CODE + BKAR_INVT_DATE + BKAR_INVT_NUM |
| BKARINVV | BKAR_INVV_CODE + BKAR_INVV_NUM |
| BKARRDSC | BK_DESC_CODE |
| BKARRINV | BKAR_INV_NUM |
| BKARRIVL | BKAR_INVL_INVNM |
| BKARSHIP | BKAR_CUSTCODE |
| BKARSIVL | BKAR_INVL_INVNM |
| BKART | BKART_TRXN |
| BKARTNOT | BKART_NOT_TRXN |
| BKARTXN | BKAR_TXN_SONUM |
| BKARTXNB | BKAR_TXN_SONUM |
| BKARTXNS | BKAR_TXN_SONUM |

## BKBM

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKBMAMTR | BKBM_PARENT |
| BKBMAVAL | BKBM_PARENT |
| BKBMCNFG | BKBM_CNFG_NUM |
| BKBMDIM | BKBM_DIM_PARENT |
| BKBMEMTR | BKBM_PARENT |
| BKBMERMK | BKBM_RM_PARENT + BKAR_INV_TRACK + BKFO_CFG_YN_2 |
| BKBMMSTR | BKBM_PARENT |
| BKBMNOTE | BKBM_NT_PARENT |
| BKBMREMK | BKBM_RM_PARENT |
| BKBMSUMM | BKBM_PARENT |

## BKCM

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKCMACCC | BKCM_ACCC_CCODE |
| BKCMACCL | BKCM_ACCL_CODE |
| BKCMACCN | BKCM_ACCN_CODE |
| BKCMACCT | BKCM_ACCT_CODE |
| BKCMACFC | BKCM_ACFC_FCODE |
| BKCMACTD | BKCM_ACTD_CODE |
| BKCMACTF | BKCM_ACTF_CODE |
| BKCMACTH | BKCM_ACTH_CODE |
| BKCMCNTD | BKCM_CNTD_TTLE1 |
| BKCMCTL1 | BKCM_CTRL_USER |
| BKCMCTL2 | BKCM_CTRL_USER |
| BKCMCTL3 | BKCM_CTRL_USER |
| BKCMCTL4 | BKCM_CTRL_USER |
| BKCMCTRL | BKCM_CTRL_USER |
| BKCMCUST | BKAR_CUSTCODE |
| BKCMDE | BKCM_ACCT_CODE |
| BKCMDTCD | BKCM_DTCD_DCODE |
| BKCMDUN | BKCM_DUN_REP |
| BKCMDUNH | BKCM_DUNH_ACCT |
| BKCMEACC | BKCM_ACCL_CODE |
| BKCMEACD | BKCM_ACTD_CODE |
| BKCMEACF | BKCM_ACTF_CODE |
| BKCMEACH | BKCM_ACTH_CODE |
| BKCMEACT | BKCM_ACCT_CODE |
| BKCMEFTM | BKCM_FTME_CODE |
| BKCMFORM | BKCM_FORM_CODE |
| BKCMFTME | BKCM_FTME_CODE |
| BKCMHCD2 | BKCM_HCD2_HCODE |
| BKCMHCOD | BKCM_HCOD_HCODE |
| BKCMLEAD | BKCM_LEAD_SCODE |
| BKCMMHST | BKCM_MHST_MCODE |
| BKCMPCFC | BKCM_PCFC_FCODE |
| BKCMPCNT | BKCM_PCNT_CCODE |
| BKCMPCTF | BKCM_PCTF_CCODE + BKCM_PCTF_REP + BKCM_PCTF_TYPE |
| BKCMPCTH | BKCM_PCTH_CCODE |
| BKCMREP | BKCM_REP_REP |
| BKCMSBDF | BKCM_SBDF_BINC |
| BKCMTEMP | BKCMT_KEYF |
| BKCMTERR | BKCM_TERR_TCODE |
| BKCMTMP1 | BKCMT_KEYF |
| BKCMTMP2 | BKCMT_KEYF |
| BKCMTMP3 | BKCMT_KEYF |
| BKCMTMP4 | BKCMT_KEYF |
| BKCMVNDF | BKCM_VNDF_VCODE |
| BKCMVNDH | BKCM_VNDH_VCODE |
| BKCMVNFC | BKCM_VNFC_FCODE |

## BKCP

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKCPEC | BKCP_EC_DATE |
| BKCPMSTR | BKCP_MST_CMPATH |

## BKDC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKDCCFG | BKDC_CFG_IDLEP |
| BKDCCLAB | LAB_ESSDATE |
| BKDCHLAB | LAB_ESSDATE |
| BKDCLAB | LAB_ESSDATE |
| BKDCPLAB | LAB_ESSDATE |
| BKDCSHFT | BKDC_SH_NAME1 |
| BKDCTLAB | LAB_ESSDATE |

## BKED

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKEDIDUN | BKEDI_DUN_CUST |
| BKEDIH | BKAR_INV_NUM |
| BKEDIL | ?76 + BKAR_INVL_INVNM |
| BKEDMSTR | BKEDI_MST_NEXTN |
| BKEDNOTE | BKEDI_NOTE_EDI |
| BKEDPOST | BKEDI_POST_INVN |

## BKES

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKESTCFG | BKEST_CFG_NUM |
| BKESTQT | BKAR_INV_NUM |
| BKESTQTL | BKAR_INVL_INVNM |

## BKFL

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKFLDHLP | HLP_CODE + HLP_INDEX |

## BKFO

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKFOCFG | BKFO_CFG_MANFET |

## BKGL

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKGLACHK | BKGL_CHK_CHKACT + BKGL_CHK_NUM |
| BKGLAGJL | BKGL_GJL_TRANSN |
| BKGLAGJR | BKGL_GJ_TRANSDT |
| BKGLATRN | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLCCOA | ?92 + BKGLC_ACCT |
| BKGLCHK | BKGL_CHK_CHKACT + BKGL_CHK_NUM |
| BKGLCOA | BKGL_ACCT |
| BKGLDESC | BK_DESC_CODE |
| BKGLECOA | BKGL_ACCT |
| BKGLETRN | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLFCOA | BKGL_ACCT |
| BKGLFSTL | BKFS_NAME + BKFS_LINE_NUM |
| BKGLGJLN | BKGL_GJL_TRANSN |
| BKGLGJRN | ?96 + BKGL_GJ_TRANSDT |
| BKGLHIST | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLICC | BKGL_CHK_CHKACT + BKGL_CHK_NUM |
| BKGLRGJL | BKGL_GJL_TRANSN |
| BKGLRGJR | BKGL_GJ_TRANSDT |
| BKGLSTMT | AHSY_USER_ACCES_4 + BKGL_STB_MN_TTL |
| BKGLTEMP | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLTGJL | BKGL_GJL_TRANSN |
| BKGLTGJR | BKGL_GJ_TRANSDT |
| BKGLTMP | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLTMP2 | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLTMP3 | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLTRAN | BKGL_TRN_GLACCT + BKGL_TRN_GLDPT + BKGL_TRN_DATE |
| BKGLX | BKGLX_POSTDATE |
| BKGLXH | BKGLX_POSTDATE |

## BKIC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKICALTD | BKIC_ALTD_PCODE |
| BKICALTP | BKIC_ALTP_TYPE + BKIC_ALTP_PCODE |
| BKICAMTR | BKIC_PROD_CODE |
| BKICAPMA | BKIC_PMAT_CUST |
| BKICDIM | BKICDIM_PARTNO |
| BKICELOC | BKIC_LOC_PROD |
| BKICEMTR | BKIC_PROD_CODE |
| BKICLOC | BKIC_LOC_PROD |
| BKICLOCM | BKIC_LOCM_CODE |
| BKICMFG | BKIC_MFG_PCODE + BKIC_MFG_MANUF |
| BKICMSTR | BKIC_PROD_CODE |
| BKICPMAT | BKIC_PMAT_CUST |
| BKICREF | BKART_TRXN + BKIC_REF_CUST |
| BKICREQ | BKIC_REQ_STATUS + BKIC_REQ_BY + BKIC_REQ_IDATE + BKIC_REQ_NUM |
| BKICTAX | BKIC_TAX_STATE |
| BKICVAL | BKIC_VAL_CODE + BKIC_VAL_DATE |

## BKIS

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKISHTAX | BKIS_TAX_CODE + BKIS_TAX_TRFLAG + BKIS_TAX_DATE |
| BKISTAX | BKIS_TAX_CODE + BKIS_TAX_TRFLAG + BKIS_TAX_DATE |

## BKLO

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKLOGON | BKLOGON_CODE |

## BKMA

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKMATCST | BKMC_CODE |
| BKMATRIM | BKMA_TRIM_MACH |

## BKMR

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKMRPFC | BKMRP_FC_PART |
| BKMRPPO | BKMRP_PO_UID + BKMRP_PO_VEND + BKMRP_PO_DATE |
| BKMRPSW | BKMRP_SW_PART |

## BKPC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKPCKIT | ?5742 |
| BKPCPLOT | ?5743 |

## BKPI

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKPIFROZ | BKPH_INFO_YEAR + BKPH_INFO_QTR + BKPH_INFO_LOC + BKPH_INFO_PROD |
| BKPILCNT | BKPI_LOT_YEAR + BKPI_LOT_QTR + BKPI_LOT_LOC + BKPI_LOT_CODE + BKPI_LOT_LOT |
| BKPILOT | BKPI_LOT_YEAR + BKPI_LOT_QTR + BKPI_LOT_LOC + BKPI_LOT_CODE + BKPI_LOT_LOT |
| BKPIMSTR | BKPI_MSTR_YEAR + BKPI_MSTR_QTR |
| BKPIPHYS | BKPH_YEAR + BKPH_QTR + BKPH_LOC + BKPH_CODE |
| BKPISCNT | BKPI_SER_YEAR + BKPI_SER_QTR + BKPI_SER_LOC + BKPI_SER_CODE + BKPI_SER_SERIAL |
| BKPISER | BKPI_SER_YEAR + BKPI_SER_QTR + BKPI_SER_LOC + BKPI_SER_CODE + BKPI_SER_SERIAL |

## BKPO

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKPOX | BKPOX_POSTDATE |
| BKPOXH | BKPOX_POSTDATE |

## BKPR

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKPRACOM | BKPR_COMM_SLSP |
| BKPRAGNT | BKPR_AGNT_NUM |
| BKPRBOOK | BKPR_SLS_EMPNUM |
| BKPRCOMM | BKPR_COMM_SLSP |
| BKPRCURP | BKPR_CURP_EMPNM |
| BKPRFTAX | BKPR_TAX_CODE |
| BKPRGLFL | BKPR_GL_STCODE |
| BKPRHCOM | BKPR_COMM_SLSP |
| BKPRHIST | BKPR_CURP_EMPNM |
| BKPRINFO | BKPR_INFO_NUM |
| BKPRMSTR | BKPR_EMP_NUM + BKAC_THRU_CLASS |
| BKPRSALE | BKPR_SLS_EMPNUM |
| BKPRSTFL | BKPR_ST_STCODE |
| BKPRTC | BKPR_TC_EMP |
| BKPRTCFG | BKPRT_CFG_KEY |
| BKPRW2 | BKPR_EMP_NUM |

## BKPS

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKPSUSER | BKPS_USER_CODE |

## BKQC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKQCMSTR | BKQC_VEND_CODE + BKQC_RECV_DATE + BKQC_PO_NUM + BKQC_RECVR_NUM + BKQC_POL_ITM_NO |
| BKQCTRAN | BKQC_TRN_PO + BKQC_TRN_RECVNM |

## BKQT

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKQTNOTE | BK_DESC_CODE |
| BKQTTEMP | BK_DESC_CODE |

## BKRF

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKRFQ | BKRFQ_NUM |
| BKRFQDES | BK_DESC_CODE |

## BKRT

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKRTCST | BKRT_QUOTE |
| BKRTEMTR | MTRO_CODE |
| BKRTSPEC | BKRT_SPEC_PART |
| BKRTTEMP | BKRT_TEMP_CODE |

## BKSA

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSAREPT | BKSA_TYPE + BKSA_NAME |

## BKSB

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSBMFG | BKSB_MFG_PARNT + BKSB_MFG_PROD + BKSB_MFG_CUST + BKSB_MFG_MANUF |
| BKSBPART | BKSB_PART_PARNT + BKSB_PART_PROD + BKSB_PART_CUST |
| BKSBVEND | BKSB_VEND_PARNT + BKSB_VEND_PROD + BKSB_VEND_CUST |

## BKSH

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSHORT | BK_SHORT_PCODE |

## BKSL

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSLEVEL | BKSL_MENU + BKSL_LEVEL |
| BKSLMSTR | BKSL_MSTR_LEVEL |

## BKSO

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSOHLOT | BKAR_TXN_SONUM |
| BKSOHSER | BKAR_TXN_SONUM |
| BKSOLOCK | BKSO_LOCK_REC |
| BKSONOTE | BK_DESC_CODE |
| BKSOPO | BKMRP_PO_UID + BKMRP_PO_VEND + BKMRP_PO_DATE |
| BKSOX | BKSOX_POSTDATE |
| BKSOXH | BKSOX_POSTDATE |

## BKSY

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKSYAP | BKSY_AP_PONUM |
| BKSYAR | BKSY_AR_TRXN |
| BKSYCFG | BKSY_CFG_ACCTG |
| BKSYHELP | (no index 0 -- singleton config or write-only temp) |
| BKSYLOG | BKSY_LOGON_CODE |
| BKSYMSTR | BKSY_ARINV_NUM |
| BKSYPRTR | BKSY_PRTR_NAME |
| BKSYUSER | BKSY_USER_CODE + BKSY_USER_COMP |

## BKUM

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKUMSRTY | SCRTY_LEVEL + SCRTY_MENU |

## BKUP

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKUPDATE | BKUP_COMPANY |

## BKWO

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKWOPO | BKMRP_PO_UID + BKMRP_PO_VEND + BKMRP_PO_DATE |

## BKYS

| Table | Primary Key (index 0) |
|-------|----------------------|
| BKYSMSTR | BKYS_WONUM |

## BOMC

| Table | Primary Key (index 0) |
|-------|----------------------|
| BOMCHG | BOM_CHG_PARENT + BOM_CHG_COMP + BOM_CHG_CDATE |

## BUCK

| Table | Primary Key (index 0) |
|-------|----------------------|
| BUCKETS | (DDF parse anomaly -- 34 fields) |

## CALE

| Table | Primary Key (index 0) |
|-------|----------------------|
| CALENDAR | (DDF parse anomaly -- 50 fields) |

## CALT

| Table | Primary Key (index 0) |
|-------|----------------------|
| CALTEMP | SHP_DATE |

## CCED

| Table | Primary Key (index 0) |
|-------|----------------------|
| CCEDIXRF | CC_EDI_CUSTCODE |

## CLAS

| Table | Primary Key (index 0) |
|-------|----------------------|
| CLASMSTR | MTCLASS_M_CLASS |
| CLASS | MTCLASS_CLASS |

## CUST

| Table | Primary Key (index 0) |
|-------|----------------------|
| CUSTCLAS | MTCLASS_M_CLASS |

## DBAC

| Table | Primary Key (index 0) |
|-------|----------------------|
| DBACNAME | BKAC_FROM_DEPT + CNAME_CODE |

## DBAF

| Table | Primary Key (index 0) |
|-------|----------------------|
| DBAFIFO | FIFO_PARTNO + FIFO_RECVDATE |

## DBAH

| Table | Primary Key (index 0) |
|-------|----------------------|
| DBAHLPID | DBA_HELP_REF |

## DISC

| Table | Primary Key (index 0) |
|-------|----------------------|
| DISCOUNT | BKIC_PMAT_CUST |

## DPTM

| Table | Primary Key (index 0) |
|-------|----------------------|
| DPTMENT | DPT_CODE |

## EMER

| Table | Primary Key (index 0) |
|-------|----------------------|
| EMERSNGL | BKGL_ACCT |

## ESTC

| Table | Primary Key (index 0) |
|-------|----------------------|
| ESTCHGS | MTESCH_QUOTE |

## ESTM

| Table | Primary Key (index 0) |
|-------|----------------------|
| ESTMAT | MTESMAT_QUOTE |

## ESTR

| Table | Primary Key (index 0) |
|-------|----------------------|
| ESTROUT | MTESRO_QUOTE |

## ESTS

| Table | Primary Key (index 0) |
|-------|----------------------|
| ESTSUM | MTESUM_QUOTE |

## EVOH

| Table | Primary Key (index 0) |
|-------|----------------------|
| EVOHLPID | DBA_HELP_REF |

## HELP

| Table | Primary Key (index 0) |
|-------|----------------------|
| HELPURL | HELP_URL_REF |

## INVA

| Table | Primary Key (index 0) |
|-------|----------------------|
| INVATXN | MTIT_TYPE |

## INVE

| Table | Primary Key (index 0) |
|-------|----------------------|
| INVETXN | MTIT_TYPE |

## INVT

| Table | Primary Key (index 0) |
|-------|----------------------|
| INVTXN | MTIT_TYPE + BKAC_FROM_TYPE |

## IS*

| Table | Primary Key (index 0) |
|-------|----------------------|
| IS2DBAR | IS2D_BAR_CODE + IS2D_BAR_TYPE + IS2D_BAR_ORDER |
| ISACAR | IS_NCR_NUM + BKCM_ACCN_CODE |
| ISACARFU | IS_CARFUP_CAR |
| ISACTION | IS_ACTION_TYPE |
| ISALINKS | IS_LNK_UID |
| ISALOT | MTLOT_CODE |
| ISAMRPF | BKMRP_FC_PART |
| ISANCR | IS_NCR_NUM |
| ISANOTES | IS_NOTE_ID |
| ISAPACHK | BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| ISAPAINL | BKAP_INVL_CODE + BKAP_INVL_NUM |
| ISAPAINT | BKAP_INVT_CODE |
| ISAPARFL | BKAP_POL_PONM |
| ISAPARFQ | BKAP_PO_NUM |
| ISAPAVND | BKAP_VENDCODE |
| ISAPCHG | ISAP_CHG_PONUM + ISAP_CHG_LINEID + ISAP_CHG_CDATE |
| ISAPEX | ISAPEX_VEND |
| ISAPHCHG | ISAP_CHG_PONUM + ISAP_CHG_LINEID + ISAP_CHG_CDATE |
| ISAPHQT | BKRFQ_NUM |
| ISAPOPO | BKAP_PO_NUM |
| ISAPOPOL | BKAP_POL_PONM |
| ISAPPROJ | ISAP_PROJ_VEND + ISAP_PROJ_INV + ISAP_PROJ_LINE |
| ISAPQPO | ISAP_QPO_PCODE |
| ISAPQTQT | BKRFQ_NUM |
| ISARACHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARACHK | BKCM_ACCN_M2LBL_3 + BKAP_CHK_VNDCOD + BKAP_CHK_INVNUM |
| ISARACST | BKAR_CUSTCODE |
| ISARADSC | BK_DESC_CODE |
| ISARAHDS | BK_DESC_CODE |
| ISARAHIL | BKAR_INVL_INVNM |
| ISARAHIN | BKAR_INV_NUM |
| ISARAHTX | BKAR_TAX_INVNO |
| ISARAINT | BKAR_INVT_CODE + BKAR_INVT_DATE + BKAR_INVT_NUM |
| ISARAINV | BKAR_INV_NUM |
| ISARAIVI | BKAR_INVI_SONUM |
| ISARAIVL | BKAR_INVL_INVNM |
| ISARAIVV | BKAR_INVV_CODE + BKAR_INVV_NUM |
| ISARAT | BKART_TRXN + BKCM_ACCN_DEAR_3 |
| ISARATNT | BKART_NOT_TRXN |
| ISARATXN | BKAR_TXN_SONUM |
| ISARATXS | BKAR_TXN_SONUM + BKCM_ACCN_DEAR_5 |
| ISARCHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARECHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISAREMND | IS_REM_DATE + IS_REM_TIME + IS_REM_WHO |
| ISAREX | ISAREX_CUST |
| ISARFQ | BKRFQ_NUM |
| ISARHCHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARICHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARINVX | ISAR_INV_SONUM |
| ISARMCHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARQCHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARRCHG | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARSCGH | ISAR_CHG_SONUM + ISAR_CHG_LINEID + ISAR_CHG_CDATE |
| ISARTXNB | ISAR_TXN_SONUM |
| ISASIGN | IS_SIGN_NUM |
| ISAUTODC | BMCM_ACCN_DATE1_2 + IS_AUTO_FILE |
| ISBANKS | IS_BANKS_NUM |
| ISBILLSH | IS_BILLSH_BILL |
| ISBINLOC | ISBIN_LOC_ITEM |
| ISBINLOT | BKAR_INV_TRACK + BKFO_CFG_YN_2 + IS_BINLOT_ITEM |
| ISBMESA | BKBM_PARENT |
| ISBMEST | BMCM_ACCN_DATE1_8 + BKBM_PARENT |
| ISBMTMP | BKBM_PARENT |
| ISBNMSTR | ISBN_MSTR_LOC |
| ISBOLMS | ISSO_BOX_SONUM |
| ISBRANDC | BKCM_ACCC_CCODE |
| ISBRANDS | BKCM_ACCL_CODE |
| ISBROKER | ISIS_BRK_CODE |
| ISBSF | ISBSF_STARTDATE |
| ISBTCSB | ISSR_INFO_SRNUM |
| ISBUILD | BKCM_ACCN_DATE2_10 + IS_BUILD_UID + IS_BUILD_SORT |
| ISCAR | IS_NCR_NUM |
| ISCARFUP | IS_CARFUP_CAR |
| ISCATMST | IS_CATM_CODE |
| ISCC | IS_CC_CODE + IS_CC_SORT |
| ISCCBTXN | BKCM_ACCN_ALPH1_8 + ISCC_TXN_JOB + ISCC_TXN_FABRIC + ISCC_TXN_LOT |
| ISCCICM | ISCC_ICM_CODE |
| ISCCMTF | ISCC_MTF_ITEM + ISCC_MTF_MTF |
| ISCHAIN | IS_CHAIN_USER |
| ISCHAINM | IS_CHAIN_USER |
| ISCMGRP | ISCC_MTF_ITEM + ISCC_MTF_MTF |
| ISCONVRT | IS_CONV_ITEM |
| ISCRISLS | ISCR_SLS_CUST + ISCR_SLS_ITEM |
| ISCTREVU | IS_CREVU_EMPNME |
| ISCYCLCD | IS_CYCLE_CODE |
| ISDCSER | ISDC_SER_WOPRE + ISDC_SER_WOSUF + ISDC_SER_OPER + ISDC_SER_EMP |
| ISDEFECT | IS_DEF_CODE |
| ISDEPT | IS_GF_DEPT |
| ISDIGSIG | IS_DSIG_EMP |
| ISDIV | IS_GF_DIV |
| ISDLCK1 | (no index 0 -- singleton config or write-only temp) |
| ISDLCK2 | (no index 0 -- singleton config or write-only temp) |
| ISDRILL | LOOKUP_FROM + BKCM_ACCN_ALPH2_10 |
| ISDRILLM | DRILLM_PARENT + DRILLM_CHILD |
| ISDROP | IS_DROP_CODE |
| ISDUTY | ISIS_DUTY_DCODE |
| ISEAB | IS_EAB_USER + IS_EAB_EMAIL |
| ISECO | IS_ECO_DRAW + IS_ECO_REVLVL + IS_ECO_PART |
| ISEDINFO | ISSR_INFO_SRNUM |
| ISESADTL | IS_EST_NUM |
| ISESAHDR | BKAR_INV_NUM |
| ISESALNE | BKAR_INVL_INVNM |
| ISESTAQL | BKCM_ACCN_PHLBL_2 + BKAR_INVL_INVNM |
| ISESTAQT | BKAR_INV_NUM |
| ISESTASM | MTESUM_QUOTE |
| ISESTDTL | IS_EST_NUM |
| ISESTHDR | BKAR_INV_NUM |
| ISESTLNE | BKAR_INVL_INVNM |
| ISESTPO | BKMRP_PO_UID + BKMRP_PO_VEND + BKMRP_PO_DATE |
| ISFIELDS | IS_FLDS_FD + IS_FLDS_NUM |
| ISFOBMRM | ISFO_BRM_UID |
| ISFOHEAD | ISFO_HDR_UID |
| ISFOHIST | ISFO_HIST_UID |
| ISFOLINE | ISFO_LIN_UID |
| ISFOORDL | ISFO_ORDL_UID + ISFO_ORDL_LINE |
| ISFSCLAS | IS_FIB_CLASS |
| ISFSEMP | IS_FIB_CLASS |
| ISFSINFO | IS_FIB_PROGRAM |
| ISFUTYPE | IS_FUTYPE_TYPE |
| ISFXASST | IS_FXA_NUMBER |
| ISFXATRN | IS_FXT_NUMBER + IS_FXT_DATE + IS_FXT_POSTED |
| ISGLBDGT | ISGL_ACCT |
| ISGLCOA | ISGL_ACCT |
| ISGLDATE | ISGL_FYDATE |
| ISGLFCOA | ISGL_ACCT |
| ISGLHDAT | ISGL_FYDATE |
| ISGLNBGT | ISGL_BGT_ACCT + ISGL_BGT_GLDPT |
| ISHLOTS | IS_SER_WOPRE + IS_SER_WOSUF |
| ISHSERIA | IS_SER_WOPRE + IS_SER_WOSUF |
| ISICADT | BKIC_PROD_CODE |
| ISICAMTR | IS_PROD_CODE |
| ISICESA | BKCM_ACCN_EMLBL_6 + BKIC_PROD_CODE |
| ISICEST | BKIC_PROD_CODE |
| ISICMSTR | IS_PROD_CODE |
| ISIS | IS_TAX |
| ISISATAX | BKIS_TAX_CODE + BKIS_TAX_TRFLAG + BKIS_TAX_DATE |
| ISITMCFG | IS_SERC_ITEM |
| ISITP | IS_ITP_NUM |
| ISJBSF | ISBSF_STARTDATE |
| ISJOB | IS_JOB_NUMB |
| ISLANDF | ISIS_LND_GLADT |
| ISLBLMAP | IS_LABEL_ITEM + IS_LABEL_NUM |
| ISLINKS | IS_LNK_UID |
| ISLOCCST | IS_LCST_PART + IS_LCST_LOC |
| ISLOG | IS_LOG_WHO |
| ISLOTS | IS_SER_WOPRE + IS_SER_WOSUF |
| ISLSMAP | IS_MAP_TRAYNUM |
| ISLTYPE | IS_LT_TYPE |
| ISMACS | IS_MACS_WOPRE + IS_MACS_WOSUF + IS_MACS_OPER |
| ISMCF | ISIS_MCF_CODE |
| ISMCR | ISIS_MCR_DATE |
| ISMICADT | MTIC_PROD_CLASS |
| ISMICESA | MTIC_PROD_CLASS + BKCM_ACCN_MSLBL_9 |
| ISMICEST | MTIC_PROD_CLASS |
| ISMRPFC | BKMRP_FC_PART |
| ISNCR | IS_NCR_NUM |
| ISNOTES | IS_NOTE_ID |
| ISNTYPE | IS_NT_TYPE |
| ISNUMBER | IS_NUM_CODE |
| ISORDDSC | IORD_DESC_CODE |
| ISORDECO | IS_OECO_SONUM + IS_OECO_UNUM + IS_OECO_PART |
| ISPOBOX | ISSO_BOX_SONUM |
| ISPODESC | IORD_DESC_CODE |
| ISPOHTRK | IS_TRK_ORD + IS_TRK_NUM + IS_TRK_CDATE |
| ISPOLOG | ISPO_LOG_DATE + ISPO_LOG_EMP |
| ISPOS | BKCM_ACCL_CODE |
| ISPOSC | BKCM_ACCC_CCODE |
| ISPOTRK | IS_TRK_ORD + IS_TRK_NUM + IS_TRK_CDATE |
| ISPREQ | IS_PREQ_WOPRE + IS_PREQ_WOSUF + IS_PREQ_PART |
| ISPRESN | IS_PRESN_REASON |
| ISPRINFO | ISPR_INFO_PROG |
| ISPRMSTR | BKPR_EMP_NUM |
| ISPRSALE | BKPR_SLS_EMPNUM |
| ISPRTEMP | ISPR_TRN_GLACCT + ISPR_TRN_GLDPT + ISPR_TRN_DATE |
| ISPRUDF | ISPR_UDF_DIV + ISPR_UDF_NUM |
| ISQCAMST | BKQC_VEND_CODE + BKQC_RECV_DATE + BKQC_PO_NUM + BKQC_RECVR_NUM + BKQC_POL_ITM_NO |
| ISQCATRN | BKQC_TRN_PO + BKQC_TRN_RECVNM |
| ISQCMTHD | ISQC_MTD_TSTCOD + BKCM_ACCN_DTLBL_9 |
| ISQCRSLT | ISQC_SPC_LRNUM |
| ISQCSPEC | ISQC_SPC_LRNUM |
| ISQRYSQL | IS_QRY_NAME |
| ISQSOA | IS_QSOA_UID + IS_QSOA_CUST |
| ISQTCODE | IS_CATM_CODE |
| ISQTINFO | ISSR_INFO_SRNUM |
| ISREMIND | IS_REM_DATE + IS_REM_TIME + IS_REM_WHO |
| ISREPDEF | ISREP_DEF_LABEL |
| ISREPLNK | ISREP_LNK_REPNM |
| ISREPORD | ISREP_ORD_INVNM + ISREP_ORD_ULID + ISREP_ORD_REPNM |
| ISRFQADS | BK_DESC_CODE |
| ISRMAAI | IS_RMA_NUM |
| ISRMAC | IS_RMA_CODE |
| ISRMADSC | BK_DESC_CODE |
| ISRMAI | IS_RMA_NUM |
| ISRMAINF | ISSR_INFO_SRNUM |
| ISRMAINV | BKAR_INV_NUM |
| ISRMAIVL | BKAR_INVL_INVNM |
| ISRMDESC | BK_DESC_CODE |
| ISRMHINF | ISSR_INFO_SRNUM |
| ISRMINFO | ISSR_INFO_SRNUM |
| ISRMINV | BKAR_INV_NUM |
| ISRMINVL | BKAR_INVL_INVNM |
| ISRMTXN | BKAR_TXN_SONUM |
| ISRMTXNS | BKAR_TXN_SONUM |
| ISROUTEX | IS_ROUT_CODE + IS_ROUT_OPER |
| ISRTESA | MTRO_CODE |
| ISRTEST | MTRO_CODE |
| ISRTLOAD | IS_LOAD_SONUM + IS_LOAD_ITEM + IS_LOAD_SCCOGS |
| ISRTMS | IS_RTM_CUST |
| ISSCHED | IS_SCHED_NAME |
| ISSCOMP | IS_SCOMP_DETAIL + IS_SCOMP_COMPND |
| ISSDET | IS_SDET_DETAIL |
| ISSEDH | BKAR_INV_NUM |
| ISSEDL | BKAR_INVL_INVNM |
| ISSEPROC | IS_SEPROC_PROC |
| ISSEQUIP | IS_SEQUIP_NAME |
| ISSERCNT | IS_SERC_ITEM |
| ISSERIAL | IS_SER_WOPRE + IS_SER_WOSUF |
| ISSERR | IS_SERR_WOPRE + IS_SERR_WOSUF + IS_SERR_OPER + IS_SERR_DATE + IS_SERR_TIME |
| ISSESH | BKAP_PO_ISBROKE + BKAR_INV_NUM |
| ISSESL | BKAR_INVL_INVNM |
| ISSETYPE | IS_SETYPE_ERR |
| ISSHIPA | IS_SHPA_CODE |
| ISSHIPCO | IS_SHIP_SHPCOD |
| ISSHPVIA | IS_SHPVIA_CUST |
| ISSIGN | IS_SIGN_NUM |
| ISSLSFC | BKAP_PO_QCTOTAL + BKMRP_FC_PART |
| ISSMTCFG | IS_SMT_WOPRE + IS_SMT_WOSUF + IS_SMT_OPER + IS_SMT_MACHINE |
| ISSNOTES | IS_NOTE_ID |
| ISSOABOX | ISSO_BOX_SONUM |
| ISSOAHBX | ISSO_BOX_SONUM |
| ISSOAINF | ISSR_INFO_SRNUM |
| ISSOALOT | BKAR_TXN_SONUM |
| ISSOASER | BKAR_TXN_SONUM |
| ISSOBOX | ISSO_BOX_SONUM |
| ISSOHBOX | (DDF parse anomaly -- 15 fields) |
| ISSOHINF | (DDF parse anomaly -- 53 fields) |
| ISSOINFO | ISSR_INFO_SRNUM |
| ISSOREVU | IS_SOVU_SONUM + BMCM_ACCN_DATE1_9 |
| ISSPC | IS_SPC_WOPRE + IS_SPC_WOSUF + IS_SPC_OPER + IS_SPC_TYPE |
| ISSPOH | BKAP_PO_NUM |
| ISSPOL | BKAP_POL_PONM |
| ISSQTH | BKAR_INV_NUM |
| ISSQTL | BKAR_INVL_INVNM |
| ISSRADSC | BK_DESC_CODE |
| ISSRAINF | ISSR_INFO_SRNUM |
| ISSRAINV | BKAR_INV_NUM |
| ISSRAIVL | BKAR_INVL_INVNM |
| ISSRAMMS | ISSR_MMS_SRVNUM |
| ISSRCH | BKAR_INV_NUM |
| ISSRCL | BKAR_INVL_INVNM |
| ISSRDESC | BK_DESC_CODE |
| ISSRFQH | BKAP_PO_NUM |
| ISSRFQL | BKAP_POL_PONM |
| ISSRHINF | ISSR_INFO_SRNUM |
| ISSRINFO | ISSR_INFO_SRNUM |
| ISSRINV | BKAR_INV_NUM |
| ISSRINVL | BKAR_INVL_INVNM |
| ISSRMH | BKAR_INV_NUM |
| ISSRMINV | BKAR_INV_NUM |
| ISSRMIVL | BKAR_INVL_INVNM |
| ISSRML | BKAR_INVL_INVNM |
| ISSRMMS | ISSR_MMS_SRVNUM |
| ISSRTXN | BKAR_TXN_SONUM |
| ISSRTXNS | BKAR_TXN_SONUM |
| ISSSOH | BKAR_INV_NUM |
| ISSSOL | BKAP_PO_SHPST + BKAR_INVL_INVNM |
| ISSSRH | BKAR_INV_NUM |
| ISSSRL | BKAR_INVL_INVNM |
| ISSTEQUI | IS_STYPE_TYPE |
| ISSTRACK | IS_STRACK_WOPRE + IS_STRACK_WOSUF + IS_STRACK_OPER + IS_STRACK_DATE + IS_STRACK_TIME |
| ISSTTYPE | IS_STYPE_TYPE |
| ISSTYPE | IS_STYPE_TYPE |
| ISTAXFIL | ISIS_TXF_CODE |
| ISTAXGRP | ISIS_TXG_NAME |
| ISTERMS | IS_TERMS_NUM |
| ISTOOLOG | ISTOOL_ITEM |
| ISTRIGRS | IS_TRIG_TRIGR + IS_TRIG_CODE |
| ISUDFINV | IS_UDF_NAME |
| ISUDMSTR | IS_UDM_CODE |
| ISUSAGE | ISTS_USE_CODE |
| ISVAR | IS_VAR_COMPANY |
| ISVARSQL | IS_VAR_QNAME + IS_VAR_ORDER |
| ISVNDADT | IS_VND_VEND |
| ISWOCLOG | IS_WOLOG_WOPRE + IS_WOLOG_WOSUF |
| ISWODESC | BK_DESC_CODE |
| ISWOEX | IS_WOEX_WOPRE + IS_WOEX_WOSUF |
| ISWOHDSC | BK_DESC_CODE |
| ISWOHEX | IS_WOEX_WOPRE + IS_WOEX_WOSUF |
| ISWOPRIO | IS_WOPRIO_PRIO |
| ISWOROEX | IS_WROEX_WOPRE + IS_WROEX_WOSUF + IS_WROEX_OPER |
| ISWOTRAY | IS_TRAY_WOPRE + IS_TRAY_WOSUF + IS_TRAY_OPER |
| ISWROHEX | IS_WROEX_WOPRE + IS_WROEX_WOSUF + IS_WROEX_OPER |

## JGPI

| Table | Primary Key (index 0) |
|-------|----------------------|
| JGPITEMS | JGP_ITEM |

## JSPC

| Table | Primary Key (index 0) |
|-------|----------------------|
| JSPCNLCD | JSP_CNLCD_CODE |
| JSPCNLSO | JSP_CNLSO_SONUM + JSP_CNLSO_UNUM |

## LANG

| Table | Primary Key (index 0) |
|-------|----------------------|
| LANGDICT | LANG_DICT_ECAPT + LANG_DICT_LANG |

## LOT

| Table | Primary Key (index 0) |
|-------|----------------------|
| LOT | MTLOT_CODE |

## MACH

| Table | Primary Key (index 0) |
|-------|----------------------|
| MACHINE | TMACH_MACHINE |

## MENU

| Table | Primary Key (index 0) |
|-------|----------------------|
| MENUFILE | MENU_CODE |

## MK*

| Table | Primary Key (index 0) |
|-------|----------------------|
| MKAHIST | MKAHIST_ACCT + MKAHIST_DATE |
| MKASSIGN | MKASSIGN_ACCT |
| MKDEF | MKDEF_REQUIRE |
| MKECLASS | MKECLASS_NUM |
| MKEVENT | MKEVENT_NUM |
| MKFORM | MKFORM_NUM |
| MKICLASS | MKECLASS_NUM |
| MKTCLASS | MKTCLASS_NUM |
| MKTNOTE | MKTNOTE_TRACK + MKTNOTE_LINE |
| MKTRACK | MKTRACK_NUM |
| MKTROUT | MKTROUT_TRACK + MKTROUT_SEQ |

## MT*

| Table | Primary Key (index 0) |
|-------|----------------------|
| MTEXCHG | EXCHG_QUOTE |
| MTICAMTR | MTIC_PROD_CLASS |
| MTICEMTR | MTIC_PROD_CLASS |
| MTICMSTR | MTIC_PROD_CLASS |
| MTINVDEF | MTIC_PROD_CLASS |
| MTMRP | BKAP_PO_TAXABLE + MTMRP_PARTNO |

## MWOP

| Table | Primary Key (index 0) |
|-------|----------------------|
| MWOPTEMP | MWOP_STATUS |

## NOTE

| Table | Primary Key (index 0) |
|-------|----------------------|
| NOTETEMP | BK_DESC_CODE |

## NZIT

| Table | Primary Key (index 0) |
|-------|----------------------|
| NZITPRE | NZ_IPRE_PREFIX_1 |

## OPQC

| Table | Primary Key (index 0) |
|-------|----------------------|
| OPQCDESC | OPQC_WOPRE + OPQC_WOSUF + OPQC_OPER |

## OUTH

| Table | Primary Key (index 0) |
|-------|----------------------|
| OUTHPROC | MTPO_WOPRE + BKAP_CHK_CHKDTE + MTPO_WOSUF + MTPO_DATE |

## OUTP

| Table | Primary Key (index 0) |
|-------|----------------------|
| OUTPROC | MTPO_WOPRE + MTPO_WOSUF + MTPO_DATE |

## PIBI

| Table | Primary Key (index 0) |
|-------|----------------------|
| PIBINLOC | PIBIN_LOC_ITEM |
| PIBINLOT | PI_BINLOT_ITEM |

## QCCO

| Table | Primary Key (index 0) |
|-------|----------------------|
| QCCODES | MTQC_CODE |

## ROCH

| Table | Primary Key (index 0) |
|-------|----------------------|
| ROCHG | RO_CHG_PART + RO_CHG_OPER + RO_CHG_CDATE |

## ROUT

| Table | Primary Key (index 0) |
|-------|----------------------|
| ROUTAING | BKAP_CHK_INVDTE + MTRO_CODE |
| ROUTING | MTRO_CODE |
| ROUTTEMP | MTRO_CODE |

## SCHE

| Table | Primary Key (index 0) |
|-------|----------------------|
| SCHEDCAL | SCH_CAL_DATE |

## SCHW

| Table | Primary Key (index 0) |
|-------|----------------------|
| SCHWO | SWO_WOPRE + SWO_WOSUF |

## SCRA

| Table | Primary Key (index 0) |
|-------|----------------------|
| SCRAP | MTSCRAP_CODE |

## SERI

| Table | Primary Key (index 0) |
|-------|----------------------|
| SERIAL | MTSER_CODE |
| SERIALH | MTSER_CODE |

## SUMC

| Table | Primary Key (index 0) |
|-------|----------------------|
| SUMCUST | SUMCUST_CUST + SUMCUST_YEAR + SUMCUST_MONTH |

## SUMI

| Table | Primary Key (index 0) |
|-------|----------------------|
| SUMINV | SUMINV_PARTNO + SUMINV_LOCATION + SUMINV_YEAR + SUMINV_MONTH |

## SUMP

| Table | Primary Key (index 0) |
|-------|----------------------|
| SUMPNCUS | SUMPNCUS_CUST + SUMPNCUS_PARTNO + SUMPNCUS_YEAR + SUMPNCUS_MONTH |

## SUMW

| Table | Primary Key (index 0) |
|-------|----------------------|
| SUMWC | SUMWC_WORKCTR + SUMWC_YEAR + SUMWC_MONTH |

## TEMP

| Table | Primary Key (index 0) |
|-------|----------------------|
| TEMPOLD | BKCM_ACTD_CODE |

## TEST

| Table | Primary Key (index 0) |
|-------|----------------------|
| TESTARRA | (no index 0 -- singleton config or write-only temp) |
| TESTFILE | TESTFILE_1 |

## TOOL

| Table | Primary Key (index 0) |
|-------|----------------------|
| TOOL | MTOOL_TOOL |

## WBTR

| Table | Primary Key (index 0) |
|-------|----------------------|
| WBTRVMEM | BTRV_MEM_CNTR + BTRV_MEM_SUBC |
| WBTRVMEMO | BTRV_MEM_CNTR + BTRV_MEM_SUBC |

## WCCT

| Table | Primary Key (index 0) |
|-------|----------------------|
| WCCTL | WCTL_WC + WCTL_START |

## WCTR

| Table | Primary Key (index 0) |
|-------|----------------------|
| WCTRLOAD | WC_LOAD_WC |
| WCTRSLOD | WC_LOAD_WC |

## WOBO

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOBOM | WOBOM_OPER + WOBOM_WOPRE + WOBOM_WOSUF |
| WOBOMCHG | WBOM_CHG_WOPRE + WBOM_CHG_WOSUF + WBOM_CHG_PARENT + WBOM_CHG_COMP + WBOM_CHG_UID |
| WOBOMHRM | WOBOM_RM_WOPRE |
| WOBOMREM | WOBOM_RM_WOPRE |

## WODA

| Table | Primary Key (index 0) |
|-------|----------------------|
| WODATE | WODATE_WOPRE + WODATE_WOSUF + WODATE_START + WODATE_FINISH |

## WOEL

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOELABOR | MTWOLA_OPER + MTWOLA_DATE + MTWOLA_WOPRE |

## WOEM

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOEMAT | WOMAT_DATE + WOMAT_WOPRE + WOMAT_WOSUF |

## WOER

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOERECV | MTWOR_WOPRE + MTWOR_WOSUF |

## WOEX

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOEXCHG | MTWO_EX_WOPRE + MTWO_EX_WOSUF |

## WOHB

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHBOM | WOBOM_OPER + WOBOM_WOPRE + WOBOM_WOSUF |

## WOHD

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHDATE | WODATE_WOPRE + WODATE_WOSUF + WODATE_START + WODATE_FINISH |

## WOHE

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHEXCHG | MTWO_EX_WOPRE + MTWO_EX_WOSUF |

## WOHL

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHLABOR | MTWOLA_OPER + MTWOLA_DATE + MTWOLA_WOPRE |

## WOHM

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHMAT | WOMAT_DATE + WOMAT_WOPRE + WOMAT_WOSUF |

## WOHR

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOHRECV | MTWOR_WOPRE + MTWOR_WOSUF |
| WOHROUT | MTWORO_WOPRE |

## WOLA

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOLABOR | MTWOLA_OPER + MTWOLA_DATE + MTWOLA_WOPRE |
| WOLABRPT | MTWOLA_OPER + MTWOLA_DATE + MTWOLA_WOPRE |

## WOMA

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOMAT | WOMAT_DATE + WOMAT_WOPRE + WOMAT_WOSUF |

## WORE

| Table | Primary Key (index 0) |
|-------|----------------------|
| WORECV | MTWOR_WOPRE + MTWOR_WOSUF |

## WORK

| Table | Primary Key (index 0) |
|-------|----------------------|
| WORKACHG | WO_CHG_WOPRE + WO_CHG_WOSUF + WO_CHG_CDATE |
| WORKCHG | WO_CHG_WOPRE + WO_CHG_WOSUF + WO_CHG_CDATE |
| WORKCTR | MTWC_WC |
| WORKHORD | MTWO_WIP_WOPRE |
| WORKORD | MTWO_WIP_WOPRE |
| WORKSORD | MTWO_WIP_WOPRE |

## WORO

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOROCHG | WORO_CHG_WOPRE + WORO_CHG_WOSUF + WORO_CHG_OPER + WORO_CHG_CDATE |
| WOROUT | MTWORO_WOPRE |
| WOROUTMP | MTWORO_WOPRE |

## WOSR

| Table | Primary Key (index 0) |
|-------|----------------------|
| WOSROUT | MTWORO_WOPRE |

## X$* (DDF meta)

| Table | Primary Key (index 0) |
|-------|----------------------|
| X$Attrib | Xa$Id + Xa$Type |
| X$Occurs | Xo$FileId |
| X$Proc | Xp$Name + Xp$Id |
| X$Relate | Xr$PId |
| X$Trigger | Xt$Name + Xt$Sequence |
| X$Variant | Xvar$FileId |
| X$View | Xv$Name |

## XXIC

| Table | Primary Key (index 0) |
|-------|----------------------|
| XXICMSTR | BKIC_PROD_CODE |
