# EvoERP — Primary Key Reference
Status: partial | verified-from-INDEX.DDF

Primary keys extracted from INDEX.DDF (index_num=0 records) in the Pervasive DDF set at
`\\I2S109-SOLIDCRM\DBAMFG$\DDFFILES\`.

---

## AP / Purchase Orders (BKAP\*)

| Table | Primary Key |
|-------|-------------|
| BKAPAPO | BKAP_PO_NUM |
| BKAPAPOL | BKAP_POL_PONM |
| BKAPCHKF | BKAP_CHK_VNDCOD |
| BKAPDEP | BKAR_DEP_DEPNO |
| BKAPEIVT | BKAP_INVT_CODE |
| BKAPEVND | BKAP_VENDCODE |
| BKAPINVL | BKAP_INVL_CODE |
| BKAPINVT | BKAP_INVT_CODE |
| BKAPPO | BKAP_PO_NUM |
| BKAPPOL | BKAP_POL_PONM |
| BKAPQUOT | BKRFQ_NUM |
| BKAPRFQ | BKAP_PO_NUM |
| BKAPRFQL | BKAP_POL_PONM |
| BKAPRIVL | BKAP_INVL_CODE |
| BKAPVEND | BKAP_VENDCODE |

## AR / Accounts Receivable (BKAR\*)

| Table | Primary Key |
|-------|-------------|
| BKARCHKF | BKAP_CHK_VNDCOD |
| BKARCUST | BKAR_CUSTCODE |
| BKARDEP | BKAR_DEP_DEPNO |
| BKARECST | BKAR_CUSTCODE |
| BKAREIVT | BKAR_INVT_CODE |
| BKARHINV | BKAR_INV_NUM |
| BKARHIVL | BKAR_INVL_INVNM |
| BKARHTAX | BKAR_TAX_INVNO |
| BKARINV | BKAR_INV_NUM |
| BKARINVI | BKAR_INVI_SONUM |
| BKARINVL | BKAR_INVL_INVNM |
| BKARINVT | BKAR_INVT_CODE |
| BKARINVV | BKAR_INVV_CODE |
| BKARRINV | BKAR_INV_NUM |
| BKARRIVL | BKAR_INVL_INVNM |
| BKARSHIP | BKAR_CUSTCODE |
| BKARSIVL | BKAR_INVL_INVNM |
| BKART | BKART_TRXN |
| BKARTNOT | BKART_NOT_TRXN |
| BKARTXN | BKAR_TXN_SONUM |
| BKARTXNB | BKAR_TXN_SONUM |

## Bill of Materials (BKBM\*)

| Table | Primary Key |
|-------|-------------|
| BKBMAMTR | BKBM_PARENT |
| BKBMAVAL | BKBM_PARENT |
| BKBMCNFG | BKBM_CNFG_NUM |
| BKBMDIM | BKBM_DIM_PARENT |
| BKBMEMTR | BKBM_PARENT |
| BKBMMSTR | BKBM_PARENT |
| BKBMNOTE | BKBM_NT_PARENT |
| BKBMREMK | BKBM_RM_PARENT |
| BKBMSUMM | BKBM_PARENT |

## Contact Manager (BKCM\*)

| Table | Primary Key |
|-------|-------------|
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
| BKCMCTRL | BKCM_CTRL_USER |
| BKCMCUST | BKAR_CUSTCODE |
| BKCMDE | BKCM_ACCT_CODE |
| BKCMDTCD | BKCM_DTCD_DCODE |
| BKCMDUN | BKCM_DUN_REP |
| BKCMEACC | BKCM_ACCL_CODE |
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
| BKCMPCTF | BKCM_PCTF_CCODE |
| BKCMPCTH | BKCM_PCTH_CCODE |
| BKCMREP | BKCM_REP_REP |
| BKCMTEMP | BKCMT_KEYF |
| BKCMTERR | BKCM_TERR_TCODE |
| BKCMVNDF | BKCM_VNDF_VCODE |
| BKCMVNDH | BKCM_VNDH_VCODE |

## Data Collection (BKDC\*)

| Table | Primary Key |
|-------|-------------|
| BKDCCFG | BKDC_CFG_IDLEP |
| BKDCCLAB | LAB_ESSDATE |
| BKDCLAB | LAB_ESSDATE |
| BKDCSHFT | BKDC_SH_NAME1 |

## EDI (BKED\*)

| Table | Primary Key |
|-------|-------------|
| BKEDIDUN | BKEDI_DUN_CUST |
| BKEDIH | BKAR_INV_NUM |
| BKEDIL | BKAR_INVL_INVNM |
| BKEDMSTR | BKEDI_MST_NEXTN |
| BKEDNOTE | BKEDI_NOTE_EDI |

## Estimating (BKES\*)

| Table | Primary Key |
|-------|-------------|
| BKESTCFG | BKEST_CFG_NUM |
| BKESTQT | BKAR_INV_NUM |
| BKESTQTL | BKAR_INVL_INVNM |

## General Ledger (BKGL\*)

| Table | Primary Key | Notes |
|-------|-------------|-------|
| BKGLACHK | BKGL_CHK_CHKACT | GL check clearing |
| BKGLAGJL | BKGL_GJL_TRANSN | GL journal lines (archive) |
| BKGLAGJR | BKGL_GJ_TRANSDT | GL journal register (archive) |
| BKGLATRN | BKGL_TRN_GLACCT | GL transactions (archive) |
| BKGLCCOA | BKGLC_ACCT | GL COA (copy/company) |
| BKGLCHK | BKGL_CHK_CHKACT | GL check clearing |
| BKGLDESC | BK_DESC_CODE | GL descriptions |
| BKGLECOA | BKGL_ACCT | GL COA (edit) |
| BKGLETRN | BKGL_TRN_GLACCT | GL transactions (edit) |
| BKGLFCOA | BKGL_ACCT | GL COA (forecast) |
| BKGLFSTL | BKFS_NAME | Financial statement lines |
| BKGLGJLN | BKGL_GJL_TRANSN | GL journal lines |
| BKGLGJRN | BKGL_GJ_TRANSDT | GL journal register |
| BKGLHIST | BKGL_TRN_GLACCT | GL transaction history |
| BKGLICC | BKGL_CHK_CHKACT | GL intercompany clearing |
| BKGLRGJL | BKGL_GJL_TRANSN | GL journal lines (report) |
| BKGLRGJR | BKGL_GJ_TRANSDT | GL journal register (report) |
| BKGLTEMP | BKGL_TRN_GLACCT | GL transaction template |
| BKGLTGJL | BKGL_GJL_TRANSN | GL journal lines (temp) |
| BKGLTGJR | BKGL_GJ_TRANSDT | GL journal register (temp) |
| BKGLTMP | BKGL_TRN_GLACCT | GL temp table 1 |
| BKGLTMP2 | BKGL_TRN_GLACCT | GL temp table 2 |
| BKGLTMP3 | BKGL_TRN_GLACCT | GL temp table 3 |
| BKGLTRAN | BKGL_TRN_GLACCT | **GL journal entries (primary)** |
| BKGLX | BKGLX_POSTDATE | GL cross-ref |
| BKGLXH | BKGLX_POSTDATE | GL cross-ref history |

## Inventory (BKIC\*)

| Table | Primary Key |
|-------|-------------|
| BKICALTD | BKIC_ALTD_PCODE |
| BKICALTP | BKIC_ALTP_TYPE |
| BKICAMTR | BKIC_PROD_CODE |
| BKICAPMA | BKIC_PMAT_CUST |
| BKICDIM | BKICDIM_PARTNO |
| BKICELOC | BKIC_LOC_PROD |
| BKICEMTR | BKIC_PROD_CODE |
| BKICLOC | BKIC_LOC_PROD |
| BKICLOCM | BKIC_LOCM_CODE |
| BKICMFG | BKIC_MFG_PCODE |
| BKICMSTR | BKIC_PROD_CODE |
| BKICPMAT | BKIC_PMAT_CUST |
| BKICREF | BKART_TRXN + BKIC_REF_CUST |
| BKICREQ | BKIC_REQ_STATUS |
| BKICTAX | BKIC_TAX_STATE |
| BKICVAL | BKIC_VAL_CODE |

## MRP (BKMRP\*)

| Table | Primary Key |
|-------|-------------|
| BKMRPFC | BKMRP_FC_PART |
| BKMRPPO | BKMRP_PO_UID |
| BKMRPSW | BKMRP_SW_PART |

## Physical Inventory (BKPI\*)

| Table | Primary Key |
|-------|-------------|
| BKPIFROZ | BKPH_INFO_YEAR |
| BKPILCNT | BKPI_LOT_YEAR |
| BKPILOT | BKPI_LOT_YEAR |
| BKPIMSTR | BKPI_MSTR_YEAR |
| BKPIPHYS | BKPH_YEAR |
| BKPISCNT | BKPI_SER_YEAR |
| BKPISER | BKPI_SER_YEAR |

## Payroll (BKPR\*)

| Table | Primary Key |
|-------|-------------|
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
| BKPRMSTR | BKPR_EMP_NUM |
| BKPRSALE | BKPR_SLS_EMPNUM |
| BKPRSTFL | BKPR_ST_STCODE |
| BKPRTC | BKPR_TC_EMP |
| BKPRTCFG | BKPRT_CFG_KEY |
| BKPRW2 | BKPR_EMP_NUM |

## QC / RFQ / Routing (BKQ\*/BKRFQ\*/BKRT\*)

| Table | Primary Key |
|-------|-------------|
| BKQCMSTR | BKQC_VEND_CODE |
| BKQCTRAN | BKQC_TRN_PO |
| BKRFQ | BKRFQ_NUM |
| BKRTCST | BKRT_QUOTE |
| BKRTEMTR | MTRO_CODE |
| BKRTSPEC | BKRT_SPEC_PART |
| BKRTTEMP | BKRT_TEMP_CODE |

## Sales Analysis / Sales Orders (BKSA\*/BKSO\*)

| Table | Primary Key |
|-------|-------------|
| BKSAREPT | BKSA_TYPE |
| BKSOHLOT | BKAR_TXN_SONUM |
| BKSOHSER | BKAR_TXN_SONUM |
| BKSOLOCK | BKSO_LOCK_REC |
| BKSONOTE | BK_DESC_CODE |
| BKSOPO | BKMRP_PO_UID |
| BKSOX | BKSOX_POSTDATE |
| BKSOXH | BKSOX_POSTDATE |

## System / Configuration (BKSY\*)

| Table | Primary Key |
|-------|-------------|
| BKSYAP | BKSY_AP_PONUM |
| BKSYAR | BKSY_AR_TRXN |
| BKSYCFG | BKSY_CFG_ACCTG |
| BKSYLOG | BKSY_LOGON_CODE |
| BKSYMSTR | BKSY_ARINV_NUM |
| BKSYPRTR | BKSY_PRTR_NAME |
| BKSYUSER | BKSY_USER_CODE |

## Security (AHSYLOG, BKSL\*, BKUM\*)

| Table | Primary Key |
|-------|-------------|
| AHSYLOG | Xf$Name + AHSY_USER_LEVL |
| BKSLEVEL | BKSL_MENU |
| BKSLMSTR | BKSL_MSTR_LEVEL |
| BKUMSRTY | SCRTY_LEVEL |
| BKPSUSER | BKPS_USER_CODE |

## Work Orders (WORKCTR, WORKHORD, WORKSORD)

| Table | Primary Key |
|-------|-------------|
| WORKCTR | MTWC_WC |
| WORKHORD | MTWO_WIP_WOPRE |
| WORKSORD | MTWO_WIP_WOPRE |
| WORKORD | MTWO_WIP_WOPRE |

## Other

| Table | Primary Key |
|-------|-------------|
| BKACTRPT | BKAC_TYPE |
| BKFLDHLP | HLP_CODE |
| BKMATCST | BKMC_CODE |
| BKMATRIM | BKMA_TRIM_MACH |
| BKPOX | BKPOX_POSTDATE |
| BKPOXH | BKPOX_POSTDATE |
| BKSBMFG | BKSB_MFG_PARNT |
| BKSBPART | BKSB_PART_PARNT |
| BKSBVEND | BKSB_VEND_PARNT |
| BKSHORT | BK_SHORT_PCODE |
| BKYSMSTR | BKYS_WONUM |
| BKUPDATE | BKUP_COMPANY |
| BKISHTAX | BKIS_TAX_CODE |
| BKISTAX | BKIS_TAX_CODE |
| BKWOPO | BKMRP_PO_UID |

---

## Key Field Name Patterns

From the primary key data, EVO follows consistent naming conventions:
- `BK<MODULE>_<SHORTNAME>` — e.g., `BKAP_PO_NUM`, `BKAR_CUSTCODE`, `BKGL_TRN_GLACCT`
- `MT<MODULE>_<SHORTNAME>` — second-gen tables: `MTWO_WIP_WOPRE` (work order), `MTWC_WC` (work center)
- `BKPR_EMP_NUM` — payroll employee number (primary key for BKPRMSTR, BKPRW2)
- `BKPR_CURP_EMPNM` — current payroll by employee (BKPRCURP, BKPRHIST)
- `BKMRP_PO_UID` — MRP planned order UID (shared across BKMRPPO, BKWOPO, BKSOPO)

## Notable Findings

- **BKYSMSTR primary key is BKYS_WONUM** — not a simple counter; the YN[N] boolean flags
  table is keyed by work order number, suggesting configuration flags are per-WO or per-company.
  This needs further verification — may mean the table has a compound key or the "primary" index
  here is the first defined index rather than a true uniqueness constraint.
- **AHSYLOG has composite key**: `Xf$Name` + `AHSY_USER_LEVL` — user login name + security level.
- **BOM tables share BKBM_PARENT key** — all BOM-related tables (assembly, evaluation, structure,
  notes, remarks, summary) key off the parent part number, confirming tree structure.
- **GL transaction tables share BKGL_TRN_GLACCT key** — the GL account code is the primary
  lookup key for transaction history, templates, and temp tables.

---

*Last updated: 2026-06-11*
*Confidence: 72/100 — Primary keys extracted from INDEX.DDF for most tables; composite keys
where index_num=0 has multiple fields not yet fully enumerated; BKYSMSTR key interpretation uncertain.*
