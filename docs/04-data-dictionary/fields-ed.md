# ED — EDI: Field Reference

Status: verified-schema + completed field meanings (Pass 574k, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

BKEDIH (EDI SO headers) and BKEDIL (EDI SO lines) share the BKAR_INV_* / BKAR_INVL_*
prefix with AR/S&R invoice tables. ISEDINFO shares the ISSR_INFO_* prefix with the
supplemental info tables in the RM module. See fields-rm.md for those field definitions.

---

## BKEDIDUN
**CUSTOMER ID/EDI ENABLEMENT FILE** — EDI enrollment per customer

Fields: 7 | Key: BKEDI_DUN_CUST

One record per customer controlling EDI participation.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_DUN_ADVS | STRING | 1 | — | Advanced Shipping Notice enabled: `Y`=send ASN (856) for this customer |
| 2 | BKEDI_DUN_CUST | STRING | 10 | — | Customer Code (PK) |
| 3 | BKEDI_DUN_DUNS | STRING | 15 | — | Customer's D-U-N-S number (EDI trading partner identifier) |
| 4 | BKEDI_DUN_EDI | STRING | 1 | — | EDI enabled: `Y`=process EDI transactions for this customer |
| 5 | BKEDI_DUN_EFFDT | DATE | 4 | — | Effective Date |
| 6 | BKEDI_DUN_PRODS | STRING | 1 | — | Product catalog enabled: `Y`=send product data (832) to this customer |
| 7 | BKEDI_DUN_SHPCD | STRING | 1 | — | USING Ship to Codes Imported Y/N |

## BKEDIH
**TEMPORARY SO HEADERS** — EDI staging table for inbound SO headers

Fields: 82 | Key: BKAR_INV_NUM

Identical schema to BKARINV/ISSRINV (BKAR_INV_* prefix). Holds inbound EDI 850 PO
transactions pending import into the live SO tables. See [fields-rm.md](fields-rm.md)
ISSRINV section for all field definitions including CCOAMT, COMAMT, COMMPR_1/2,
CUSA2_1/2, DEPAMT, INDATE, ISCUR, ISMCDT, ISREV, ISRVDT, ISTXKY, ITMZTX_1/2, LINV^P,
RELNUM, RETEN, SCCOGS, SHPA2_1/2, TAXKEY, TRACK.

## BKEDIL
**TEMPORARY SO LINE ITEMS** — EDI staging table for inbound SO lines

Fields: 29 | Key: BKAR_INVL_INVNM + BKAR_INVL_CNTR

Identical schema to BKARINVL/ISSRINVL (BKAR_INVL_* prefix). Holds inbound EDI 850 PO
line items. See [fields-rm.md](fields-rm.md) ISSRINVL section for all field definitions
including COMPR_1/2, COOP, JOB^, SCCOG, UM_LN_1/2.

## BKEDMSTR
**EDI MASTER SETUP FILE** — singleton config for this company's EDI identity

Fields: 3 | Key: singleton

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_MST_DUNS | STRING | 15 | — | This company's D-U-N-S number (used as sender ID in EDI envelope) |
| 2 | BKEDI_MST_NEXTN | NUMERIC | 8 | — | Next EDI interchange control number (sequential counter) |
| 3 | BKEDI_MST_PATH | STRING | 66 | — | File system path for EDI file exchange directory |

## BKEDNOTE
**EDI NOTES** — free-text notes attached to EDI transactions

Fields: 3 | Key: BKEDI_NOTE_EDI

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_NOTE_EDI | NUMERIC | 8 | — | EDI transaction/order number |
| 2 | BKEDI_NOTE_NOTE | STRING | 80 | — | Note text (free-text message from EDI transaction) |
| 3 | BKEDI_NOTE_SO | NUMERIC | 8 | — | Sales order number this note applies to |

## BKEDPOST
**INVOICES SUBJECT TO EDI** — invoice/SO queue for outbound EDI ASN (856)

Fields: 2 | Key: BKEDI_POST_CUST + BKEDI_POST_INVN

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_POST_CUST | STRING | 10 | — | Customer code (FK → BKEDIDUN) |
| 2 | BKEDI_POST_INVN | NUMERIC | 8 | — | Invoice/SO number queued for EDI ASN transmission |

## ISEDINFO
**EDI SUPPLEMENTAL INFO** — user-configurable extended EDI fields

Fields: 54 | Key: ISSR_INFO_CODE + ISSR_INFO_UID

Identical schema to ISSRINFO/ISSRAINF (ISSR_INFO_* prefix) — same 20 AL + 20 ALPHA
alphanumeric slots, 5+5 DATE slots, CODE, EXTRA, SRNUM, UID. See [fields-rm.md](fields-rm.md)
ISSRINFO section for all field definitions.

**Confidence: 80/100** — BKEDIDUN confirmed from EDI standards context (DUNS, ASN=856, PO=850);
BKEDMSTR control number semantics clear from EDI ISA segment conventions; BKEDIH/BKEDIL/ISEDINFO
field definitions carry from their identical schemas in fields-rm.md; BKEDI_DUN_PRODS value
semantics and exact EDI transaction sets require RWN decryption to verify.
