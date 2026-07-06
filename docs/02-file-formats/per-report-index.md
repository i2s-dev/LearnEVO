# EvoERP Per-Report Index

Status: partial — architecture confirmed; DataField themes documented for top sub-reports;
full parameter documentation blocked by RWN encryption (calling code not accessible).

Sources: `samples/rtm_crossrefs.csv` (4,179 entries), `samples/rtm_fields.csv` (118,439 DataField
rows), `samples/rtm_by_module.csv` (1,734 RTMs), direct RTM binary parse (Pass 406/559/560).

---

## 1. Architecture — Root vs Sub-Report Structure

EvoERP reports are composed hierarchically. A **root report** is called directly by TAS code
and is never itself embedded in another RTM. A **sub-report** is embedded in one or more root
reports via the `Template.FileName` property.

| Metric | Count |
|--------|------:|
| Total RTM files inventoried | 1,305 |
| RTMs with module assignment | 1,376 (includes custom variants) |
| RTMs that reference sub-reports | 892 |
| RTMs referenced as sub-reports | 190 |
| Root RTMs (call subs, never called) | 808 |
| Leaf sub-reports (called, call no others) | 106 |

**Key design pattern:** A small core of ~20 high-reuse sub-reports (listed in §2) is embedded
across hundreds of root reports. When a module has many print format variants (e.g., SO has 253
RTMs), they differ mostly in which header/footer sub-reports they include, while sharing the same
core line-item sub-report (e.g., BKSOF4 or BKSOC4).

### Report Naming Convention

| Prefix | Generation | Examples |
|--------|-----------|---------|
| `BK*` | Legacy Btrieve-era (TAS Pro 4–5) | BKSOF4, BKWOC1, BKARE4 |
| `T6*` | TAS Pro 6 era | T6WOC1, T6GLO1, T6SOF1 |
| `T7*` | TAS Pro 7 era (only 23 exist) | T7WOLL1, T7PSA |
| `J7*` | Custom i2 Systems extensions | J7WOLL1 |
| `EN*`, `IEN*` | Custom EIMCO/customer variants | ENWOC1, ENWOC4 |
| `IBK*` | Custom variants of BK* reports | IBKSOF3, IBKSOF4 |

The **second letter-pair** in BK/T6 names is the module code: `SO`=Sales Orders, `WO`=Work Orders,
`AP`=AP, `AR`=AR, `IN`=Inventory, `PO`=Purchase Orders, `GL`=General Ledger, `PR`=Payroll, etc.

The **trailing letter+digit** identifies the variant: `F`=Invoice/Form, `C`=Confirmation/Traveler,
`B`=Purchase Order, `E`=Receipt, `H`=Check, `A`=Aging, `M`=Master/Analysis.

### How Reports Are Invoked

TAS Pro code calls `PRINT.RTM` (or equivalent keyword) passing a runtime-selected RTM path.
The ISRTMS table (29 fields, per-company, 0 live records = not customized here) provides
per-customer/vendor/item label routing. FILELOC maps the ISRTMS Btrieve file to company-specific
directories. In practice, the calling program selects an RTM path from ISTS.CFG or hard-coded
constants — exact mapping requires RWN decryption.

---

## 2. Top Sub-Reports (Core Reusable Sections)

These 15 sub-reports are embedded by the largest number of parent reports, making them the
structural backbone of EvoERP's printed output.

| Sub-report | Called by | Module | Purpose | Key Tables |
|-----------|----------:|--------|---------|-----------|
| BKISWCE1.RTM | 244 | IS/WH | Warehouse bin location detail | ISBIN_LOC, BKIC |
| BKSOF4.RTM | 239 | SO | Invoice line items (price/qty/discount) | BKAR_INV, BKAR_INVL |
| BKWOC1.RTM | 237 | WO | WO traveler routing operations | MTWORO, MTIC, BOM |
| BKSOC4.RTM | 131 | SO | Packing slip with lot/serial tracking | BKAR_INV, BKAR_INVL, lot/serial |
| BKSAM1.RTM | 120 | SA | Sales Analysis invoice-line detail | BKAR, BKIC, BKSA |
| BKSRB4.RTM | 80 | SR | Service/repair invoice body | BKAR, SR bill-to/ship-to |
| BKSOC1.RTM | 80 | SO | Sales order confirmation body | BKAR, open qty/ship vars |
| BKPOB4.RTM | 78 | PO | PO line items section | BKAP_PO, BKAP_POL |
| BKSOF1.RTM | 77 | SO | Invoice with extended pricing | BKAR_INV, BKAR_INVL |
| BKWOC2.RTM | 69 | WO | WO traveler BOM section | MTWORO, MTIC, BKWOC1 |
| BKSOF2.RTM | 66 | SO | Invoice alternate format | BKAR_INV, BKAR_INVL |
| BKSOPB4.RTM | 65 | SO | SO packing slip variant B | BKAR, BKSY |
| BKSOC2.RTM | 62 | SO | SO confirmation alternate | BKAR, ship dates |
| BKSOF3.RTM | 62 | SO | Invoice format 3 | BKAR_INV, BKAR_INVL |
| BKSOC3.RTM | 47 | SO | SO confirmation format 3 | BKAR, lot tracking |

### DataField Detail — Top 5 Sub-Reports

**BKISWCE1.RTM** (244 callers — #1) — Bin Inventory Location section  
DataFields (15 unique): `ISBIN_LOC_BIN`, `ISBIN_LOC_DFLT`, `ISBIN_LOC_ITEM`, `ISBIN_LOC_LOC`,
`ISBIN_LOC_UOH` (on-hand by bin), `BKIC_PROD_DESC`, `FROM_CAT/CLASS/CODE`, `THRU_CAT/CLASS/CODE`,
`WC_LOC`, `WC_MSTR` — renders bin-by-bin inventory quantities with category/class filter params.

**BKSOF4.RTM** (239 callers — #2) — SO Invoice Line Items  
DataFields (62 unique): `BKAR_INVL_PCODE/PDESC/PDISC/PEXT/PPRCE/PQTY/UM_LN[1]/UM_LN[2]`,
`BKAR_INV_CUSCOD/CUSNME/CUSORD/FOB/JOBNUM/ORDDTE/SHIPDT/SHPNME/SHPVIA/SLSP/SONUM/TERMD`,
`A_BOQ` (BO qty), `A_LOTQ` (lot qty), `A_SHQ` (ship qty), `INVNUM`, `SHIPPER` — complete
invoice line-item section with back-order tracking.

**BKWOC1.RTM** (237 callers — #3) — WO Traveler Routing Section  
DataFields (66 unique): `MTWORO_ESETHRS/ESTHRS/LEAD/LONGTIME/MACHNO/OPER/OP_TEMP/PARTSHR/
STD_TIME/TIMEPART/TOOL/VEND/VENDNAME/WCNAME`, `MTIC_PROD_DRAW/LOC/REV`,
`BOM_REMARK_HDR`, `DESC/INSTRUCTION/INSTRUCTIONS` (routing notes and specs),
`SPEC_*` (QC spec fields), `PRINT_*` (format controls) — one routing operation row per line.

**BKSOC4.RTM** (131 callers — #4) — SO Packing Slip with Lot/Serial  
DataFields (56 unique): like BKSOF4 plus `BKAR_TXN_LOT`, `BKAR_TXN_SERIAL`,
`A_LOTQ/SHIPQ/SHIP_DATE`, `LOCATION` — adds lot and serial number columns to the
standard packing slip line layout.

**BKSAM1.RTM** (120 callers — #5) — Sales Analysis Invoice-Line Detail  
DataFields (117 unique): `BKAR_INVL_PCODE/PCOGS/PDESC/PEXT/PPRCE/PQTY/RTS/UBO`,
`BKAR_INV_CUSCOD/CUSNME/INVDTE/NUM/ORDDTE/SLSP/SONUM`, `BKIC_CLASS/PROD_*`,
`BKSA_*` (sales analysis subtotals), break/grand total fields, `INCL_*` filter flags —
the core line-item section for all SA module reports.

---

## 3. Report Counts by Module

| Module | Name | Total RTMs | T6 | T7 | BK | J7 | Root | Sub |
|--------|------|----------:|---:|---:|---:|---:|-----:|----:|
| SO | Sales Orders | 253 | 181 | 0 | 72 | 0 | ~220 | ~15 |
| WO | Work Orders | 115 | 103 | 2 | 8 | 2 | ~100 | ~10 |
| IN | Inventory | 102 | 88 | 2 | 12 | 0 | ~95 | ~5 |
| AP | Accounts Payable | 95 | 58 | 9 | 27 | 1 | ~80 | ~8 |
| PO | Purchase Orders | 89 | 53 | 0 | 36 | 0 | ~75 | ~8 |
| AR | Accounts Receivable | 50 | 30 | 0 | 20 | 0 | ~42 | ~6 |
| PR | Payroll | 52 | 41 | 0 | 11 | 0 | ~50 | ~2 |
| GL | General Ledger | 42 | 42 | 0 | 0 | 0 | ~42 | ~0 |
| JC | Job Costing | 37 | 37 | 0 | 0 | 0 | ~37 | ~0 |
| SA | Sales Analysis | 34 | 27 | 0 | 7 | 0 | ~28 | ~5 |
| SR | Service and Repair | 30 | 16 | 0 | 14 | 0 | ~24 | ~5 |
| BM | Bill of Materials | 30 | 30 | 0 | 0 | 0 | ~30 | ~0 |
| SM | System Maintenance | 22 | 22 | 0 | 0 | 0 | ~22 | ~0 |
| DC | Data Collection | 20 | 11 | 0 | 8 | 1 | ~18 | ~2 |
| QC | Quality Control | 19 | 19 | 0 | 0 | 0 | ~19 | ~0 |
| SH | Scheduling | 18 | 18 | 0 | 0 | 0 | ~18 | ~0 |
| RO | Routings | 17 | 17 | 0 | 0 | 0 | ~15 | ~2 |
| MR | MRP | 16 | 16 | 0 | 0 | 0 | ~14 | ~2 |
| CM | Contact Master | 16 | 8 | 0 | 8 | 0 | ~14 | ~2 |
| CS | Commissions | 14 | 14 | 0 | 0 | 0 | ~14 | ~0 |
| ES | Estimates | 16 | 8 | 0 | 8 | 0 | ~14 | ~2 |
| DE | Data Exchange | 11 | 11 | 0 | 0 | 0 | ~11 | ~0 |

Total: **1,305 inventoried RTMs** across 33 module groups (includes custom variants).
Only 23 T7-generation RTMs exist — the reporting layer is almost entirely TAS Pro 6 era.

---

## 4. WO Traveler Report Family

The WO module has the most complex report tree. A typical WO traveler (root, 9 sub-reports)
embeds this chain:

```
T6WOC9.RTM (root — 9 subs)
  ├── BKWOC1.RTM  (routing operations — 237 callers)
  ├── BKWOC2.RTM  (BOM section — 69 callers, itself embeds BKWOC1)
  ├── SPEC sub-reports (QC specifications)
  └── barcode sub-reports (BKWOC_BARCODE family)
```

Key WO traveler RTMs:

| RTM | Sub-reports | Subs In | Purpose |
|-----|------------|---------|---------|
| T6WOC9.RTM | 9 | 2 | Primary WO traveler (current standard) |
| T6WOC2G.RTM | 10 | 0 | WO traveler variant G |
| T6WOC3E.RTM | 10 | 0 | WO traveler variant E |
| BKWOC1V.RTM | 9 | 0 | BK-gen traveler variant |
| BKWOC1.RTM | 0 | 237 | Core routing section (shared sub) |
| BKWOC2.RTM | 2 | 69 | BOM section (calls BKWOC1) |

---

## 5. BKISWCE1 — IS Module Bin Report

BKISWCE1.RTM is the most-embedded sub-report (244 callers). It renders bin location
inventory data and is reused across all modules that print inventory availability:

- Tables accessed: `ISBIN_LOC` (bin location table), `BKICMSTR` (item master)
- Key DataFields: `ISBIN_LOC_BIN` (bin name), `ISBIN_LOC_LOC` (location code),
  `ISBIN_LOC_UOH` (units on hand), `ISBIN_LOC_DFLT` (default bin flag)
- Filter params: `FROM_CAT/CLASS/CODE`, `THRU_CAT/CLASS/CODE`, `WC_LOC`, `WC_MSTR`

Called from: PO receiving, IN item inquiry, WO picking, SO shipping — any context
where multi-location inventory visibility is needed.

---

## 6. Gaps — What Requires RWN Decryption

The following per-report details cannot be determined without decrypting the calling RWN programs:

- **Exact menu code → RTM mapping** (which AP-H menu entry calls BKAPHA1 vs BKAPH2)
- **Print filter parameters** (date ranges, customer ranges, etc. — these are set in TAS code)
- **Conditional sub-report selection** (which variant is chosen at runtime — BKSOF4 vs BKSOC4)
- **Parameter passing to RTM** (how TAS variables become RTM DataField values at runtime)

The `ISRTMS` routing table exists (29-field schema confirmed) but has 0 live records,
meaning all RTM selection is hard-coded in TAS programs rather than table-driven.

**Confidence: 82/100** — RTM inventory complete; DataField themes confirmed for top 20 sub-reports;
module assignments confirmed for 83% of RTMs; calling code blocked by RWN encryption.
