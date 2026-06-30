# Cross-Module Foreign Key Relationships

Status: inferred from field-name pattern analysis (Pass 411, 2026-06-30).
Source: `samples/fk_inferred.csv` (270 relationships across 68 parent tables).

> **Important:** These FKs are **inferred** from matching field-name patterns, not from
> explicit FK constraints in the Pervasive DDF (EvoERP uses no DDF-level foreign key
> constraints). Each relationship is `referenced_table → referencing_table` via a shared
> field name that appears in both tables' schemas. Confidence varies by pattern type:
> - Module archive patterns (IS* / BK*A* naming): **very high** — this is the proven EvoERP
>   archive convention
> - Cross-module super-key patterns (ISSSRH, ISSRTXNS): **high** — confirmed by structure
> - Table name similarity (XXICMSTR, WORKSORD): **medium** — logical but naming is unusual

---

## Key Architecture Findings

### 1. Shared Invoice Number — BKAR_INV_NUM as universal key

`ISSSRH` (super-header) and `ISSSRL` (super-lines) act as universal cross-module invoice
lookup tables, keyed by `BKAR_INV_NUM`. Every invoice-bearing module has a child table:

| Module | Header child | Lines child |
|--------|-------------|------------|
| AR (active) | `BKARINV` | `BKARINVL` |
| AR (history) | `BKARHINV` | `BKARHIVL` |
| AR (archive) | `ISARAINV` | `ISARAIVL` |
| AR (reversed) | `BKARRINV` | `BKARRIVL` |
| AR (staged) | `BKARSIVL` | — |
| EDI | `BKEDIH` | `BKEDIL` |
| Estimate | `BKESTQT` | `BKESTQTL` |
| Estimate (archive h) | `ISARAHIN` | — |
| Estimate (archive inv) | `ISARAINV` | `ISARAIVL` |
| Estimate (archive hdr) | `ISESAHDR` | `ISESALNE` |
| Estimate (archive qt) | `ISESTAQT` | `ISESTAQL` |
| Estimate (header) | `ISESTHDR` | `ISESTLNE` |
| RMA (invoice) | `ISRMAINV` | `ISRMAIVL` |
| RMA (history) | `ISRMINV` | `ISRMINVL` |
| RMA (note desc) | `ISSNINV` | `ISSNINVL` |
| SR (invoice) | `ISSRAINV` | `ISSRAIVL` |
| SR (archive) | `ISSRAINV` | `ISSRAIVL` |
| SR (history inv) | `ISSRINV` | `ISSRINVL` |
| SR (archive inv) | `ISSRMINV` | `ISSRMIVL` |
| SR (remittance h) | `ISSRCH` | `ISSRCL` |
| SR (method h) | `ISSRMH` | `ISSRML` |
| SO (archive) | `ISSSOH` | `ISSSOL` |
| SO (quote h) | `ISSQTH` | `ISSQTL` |
| SO (EDI h) | `ISSEDH` | `ISSEDL` |
| SO (EDI s) | `ISSESH` | `ISSESL` |
| SO (note inv) | — | — |

**Implication:** EvoERP's invoice numbering is **global across all modules** — the same
sequence covers AR invoices, SO quotes, RMA returns, EDI orders, and SR work orders.
Any query on BKAR_INV_NUM can reach records in ~25 tables.

---

### 2. Shared Transaction Number — BKAR_TXN_SONUM

`ISSRTXNS` is the super-transaction table. All module transaction variants share the same
`BKAR_TXN_SONUM` key:

| Table | Type |
|-------|------|
| `BKARTXN`, `BKARTXNB`, `BKARTXNS` | AR transaction (main, batch, staged) |
| `ISARATXN`, `ISARATXS` | AR transaction archive |
| `BKSOHLOT`, `BKSOHSER` | SO header lot/serial tracking |
| `ISRMATXN`, `ISRMATXS`, `ISRMTXN`, `ISRMTXNS` | RMA transaction variants |
| `ISSNTXN`, `ISSNTXNS` | Note transaction (current, staged) |
| `ISSOALOT`, `ISSOASER` | SO archive lot/serial |
| `ISSRATXN`, `ISSRATXS`, `ISSRTXN` | SR transaction variants |

**Implication:** The transaction number (`SONUM` naming despite being used across AR/SO/RMA/SR)
is another global key — fulfillment, returns, and notes all index into the same number space.

---

### 3. Shared PO Number — BKAP_PO_NUM

`ISSRFQH/ISSRFQL` (RFQ super-header/lines) link all PO and RFQ variants:

Header children: `BKAPAPO`, `BKAPHPO`, `BKAPPO`, `BKAPRFQ`, `ISAPARFQ`, `ISAPOPO`, `ISSPOH`
Lines children: `BKAPAPOL`, `BKAPHPOL`, `BKAPPOL`, `BKAPRFQL`, `ISAPARFL`, `ISAPOPOL`, `ISSPOL`

The AP PO number space covers active POs, RFQ quotes, PO history, PO archives, and
staging tables in one number sequence.

---

### 4. NOTETEMP — Universal Note Template Parent

`NOTETEMP` (keyed by `BK_DESC_CODE`) is the master note/description template table. Every
module that allows free-text notes has a child table referencing this key:

| Module | Child table |
|--------|------------|
| AP | `BKAPADSC`, `BKAPDESC`, `BKAPHDSC` |
| AR | `BKARDESC`, `BKARDPST`, `BKARHDSC`, `BKARRDSC` |
| GL | `BKGLDESC` |
| Quote | `BKQTNOTE`, `BKQTTEMP` |
| RFQ | `BKRFQDES` |
| SO | `BKSONOTE` |
| AR archive | `ISARADSC`, `ISARAHDS` |
| RFQ archive | `ISRFQADS` |
| RMA | `ISRMADSC`, `ISRMDESC` |
| SR | `ISSRADSC`, `ISSRDESC` |
| WO | `ISWODESC`, `ISWOHDSC` |

21 child tables in 9 modules. NOTETEMP is one of the most-referenced master tables in EvoERP.

---

### 5. ROUTTEMP / XXICMSTR — Module Master Tables

**ROUTTEMP** (`MTRO_CODE`) is the routing template master:
Children: `BKRTEMTR`, `ISRTESA`, `ISRTEST`, `ROUTAING`, `ROUTING`

**XXICMSTR** (`BKIC_PROD_CODE`) appears to be an inventory item super-master:
Children: `BKICAMTR`, `BKICEMTR`, `BKICMSTR`, `ISICADT`, `ISICESA`, `ISICEST`, `ISICSTD`

Note: `XXICMSTR` is an unusual name (XX prefix = cross-module or placeholder). The actual
item master is `MTICMSTR` / `BKICMSTR`. This may be a view or alias used during analysis.

---

### 6. ISMYBOM — BOM Master Family

`ISMYBOM` (`BKBM_PARENT`) is parent to 9 BOM-related tables:
`BKBMAMTR`, `BKBMARC`, `BKBMAVAL`, `BKBMEMTR`, `BKBMMSTR`, `BKBMSUMM`, `ISBMESA`, `ISBMEST`, `ISBMTMP`

The BOM has active, archive, estimate, and temporary variants all under the same PARENT key.

---

### 7. ISSRINFO — Cross-Module Service Record Links

`ISSRINFO` (`ISSR_INFO_SRNUM`) links a SR (Service Repair) number to info records in
12 modules:

`ISBTCSB`, `ISEDINFO`, `ISESINFO`, `ISICINFO`, `ISQTINFO`, `ISRMAINF`, `ISRMHINF`,
`ISRMINFO`, `ISSOAINF`, `ISSOHINF`, `ISSOINFO`, `ISSRAINF`, `ISSRHINF`

This confirms SR records can be linked across EDI, Estimate, IC, Quote, RMA, SO, and SR
module contexts — the SR number is a cross-module reference point.

---

## GL Archive Pattern

GL has a clean archive triplet:

| Parent | Key | Archive children |
|--------|-----|-----------------|
| `BKGLTGJL` | `BKGL_GJL_TRANSN` | `BKGLAGJL`, `BKGLGJLN`, `BKGLRGJL` |
| `BKGLTGJR` | `BKGL_GJ_TRANSDT` | `BKGLAGJR`, `BKGLGJRN`, `BKGLRGJR` |
| `BKGLXH` | `BKGLX_POSTDATE` | `BKGLX` |
| `EMERSNGL` | `BKGL_ACCT` | `BKGLCOA`, `BKGLECOA`, `BKGLFCOA` |
| `ISGLFCOA` | `ISGL_ACCT` | `ISGLBDGT`, `ISGLCOA` |

EMERSNGL is the historical GL account master; ISGLFCOA is an extended version. Both
link to COA variants.

---

## PR (Payroll) Archive Pattern

| Parent | Key | Archive children |
|--------|-----|-----------------|
| `ISPRMSTR` | `BKPR_EMP_NUM` | `BKPRMSTR`, `BKPRW2`, `ISPRAMST` |
| `ISPRAHST` | `BKPR_CURP_EMPNM` | `BKPRCURP`, `BKPRHIST` |
| `ISPRSALE` | `BKPR_SLS_EMPNUM` | `BKPRBOOK`, `BKPRSALE` |
| `ISPRCONS` | `ISPR_CNS_EMP` | `ISPRACON` |

Employee number is the primary key for payroll master; current period and history both
reference it.

---

## AP Archive Pattern

| Parent | Key | Archive children |
|--------|-----|-----------------|
| `ISAPAVND` | `BKAP_VENDCODE` | `BKAPEVND`, `BKAPVEND` |
| `ISAPAINT` | `BKAP_INVT_CODE` | `BKAPEIVT`, `BKAPINVT` |

---

## AR/Customer Archive Pattern

| Parent | Key | Archive children |
|--------|-----|-----------------|
| `ISARACST` | `BKAR_CUSTCODE` | `BKARCUST`, `BKARECST`, `BKARSHIP`, `BKCMCUST` |
| `ISARAHTX` | `BKAR_TAX_INVNO` | `BKARHTAX` |
| `ISARAIVI` | `BKAR_INVI_SONUM` | `BKARINVI` |
| `ISARAT` | `BKART_TRXN` | `ARTTEMP`, `BKART` |
| `ISARATNT` | `BKART_NOT_TRXN` | `BKARTNOT` |

Note: `ISARACST` links `BKCMCUST` — the CM (Contact Manager) customer record is a child
of the AR customer, confirming CM and AR share a customer key space.

---

## DC (Data Collection) Archive

`BKDCTLAB` (`LAB_ESSDATE`) → `BKDCCLAB`, `BKDCHLAB`, `BKDCLAB`, `BKDCPLAB`
(DC labor: current, closed, history, pending)

---

## Full Table: All 68 Parent Tables and Their Child Counts

| Parent | Key Field | Child Count |
|--------|-----------|------------:|
| ISSSRH | BKAR_INV_NUM | 22 |
| ISSSRL | BKAR_INVL_INVNM | 22 |
| ISSRTXNS | BKAR_TXN_SONUM | 17 |
| NOTETEMP | BK_DESC_CODE | 20 |
| ISSRFQH | BKAP_PO_NUM | 7 |
| ISSRFQL | BKAP_POL_PONM | 7 |
| ISSRINFO | ISSR_INFO_SRNUM | 13 |
| ISMYBOM | BKBM_PARENT | 9 |
| XXICMSTR | BKIC_PROD_CODE | 7 |
| MTINVDEF | MTIC_PROD_CLASS | 7 |
| ISARACST | BKAR_CUSTCODE | 4 |
| BKCMCTRL | BKCM_CTRL_USER | 4 |
| BKCMTMP4 | BKCMT_KEYF | 4 |
| BKDCTLAB | LAB_ESSDATE | 4 |
| BKGLTGJL | BKGL_GJL_TRANSN | 3 |
| BKGLTGJR | BKGL_GJ_TRANSDT | 3 |
| EMERSNGL | BKGL_ACCT | 3 |
| ISARFQ | BKRFQ_NUM | 4 |
| ISESTPO | BKMRP_PO_VEND | 3 |
| ISGLFCOA | ISGL_ACCT | 2 |
| ISPRAHST | BKPR_CURP_EMPNM | 2 |
| ISPRMSTR | BKPR_EMP_NUM | 3 |
| ISPRSALE | BKPR_SLS_EMPNUM | 2 |
| ISQCSPEC | ISQC_SPC_LRNUM | 4 |
| ISSOHBOX | ISSO_BOX_SONUM | 5 |
| ISSRFQH | BKAP_PO_NUM | 7 |
| ROUTTEMP | MTRO_CODE | 5 |
| WOSROUT | MTWORO_WOPRE | 3 |
| WORKSORD | MTWO_WIP_WOPRE | 2 |
| ... | ... | ... |

(Full list in `samples/fk_inferred.csv`)

---

## Key Files

- `samples/fk_inferred.csv` — complete 270-row FK inference dataset
- `docs/04-data-dictionary/tier8-tables.md` — DDF-exact schemas for core tables
- `docs/04-data-dictionary/tier9-tables.md` — Java-confirmed table schemas
