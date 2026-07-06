# IM — International/Multi-Currency/Import: Field Reference

Status: verified-schema + completed field meanings (Pass 574d, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions present for
ISMCF (Y/N column confirmed fields); remaining field meanings inferred from naming and
multi-currency accounting conventions.

The IM module covers: international purchasing (landed cost, customs, duties), multi-currency
accounting (one currency code per ISMCF row, exchange rates in ISMCR), and optional IS-module
feature flags (ISIS singleton). At i2 Systems, MTEXCHG=0 — single-currency operation confirmed.

---

## ISBROKER
**CUSTOMS BROKER FEES** — broker fee schedule for import cost calculation

Fields: 4 | Key: ISIS_BRK_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_BRK_CODE | STRING | 10 | — | Broker code (PK — identifies this fee schedule) |
| 2 | ISIS_BRK_FLAT | NUMERIC | 8 | 2 | Flat fee amount charged per shipment |
| 3 | ISIS_BRK_PERC | NUMERIC | 8 | 6 | Percentage fee applied to declared shipment value |
| 4 | ISIS_BRK_TYPE | STRING | 1 | — | Fee type: `F`=flat only, `P`=percentage only, `B`=both (inferred) |

## ISDUTY
**DUTY CODES** — tariff/duty rate lookup table

Fields: 2 | Key: ISIS_DUTY_DCODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_DUTY_DCODE | STRING | 6 | — | Duty code (tariff/HTS classification code, PK) |
| 2 | ISIS_DUTY_PERC | NUMERIC | 8 | 3 | Duty rate — percentage applied to declared value |

## ISIS
**INTERNATIONAL DEFAULTS** — IS module feature flag singleton

Fields: 23 | Key: singleton (one record)

Configuration record controlling which IS-module features are enabled for this installation.
Most fields are Y/N enable flags. IS_DEMO is the demo/license expiry date.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_AUTO_TAX_CAL | STRING | 1 | — | Auto tax calculation enabled: `Y`=system calculates sales tax automatically |
| 2 | IS_COMM_PRICE | STRING | 1 | — | Commission on price enabled: `Y`=salesperson commissions calculated |
| 3 | IS_CUR_CVT | STRING | 1 | — | Currency conversion enabled: `Y`=multi-currency conversion active |
| 4 | IS_DEMO | DATE | 4 | — | Demo/trial expiry date (null if full license) |
| 5 | IS_EZPAY | STRING | 1 | — | EZ Pay module enabled: `Y`=credit card/electronic payment processing active |
| 6 | IS_IMAGING | STRING | 1 | — | Imaging/document attachment module enabled |
| 7 | IS_LANDED_COST | STRING | 1 | — | Landed cost module enabled: `Y`=broker/duty/freight costs applied to PO receipts |
| 8 | IS_MULTI_CPAY | STRING | 1 | — | Multi-currency payments enabled |
| 9 | IS_MULTI_CURR | STRING | 1 | — | Multi-currency module enabled |
| 10 | IS_PIC_PATH | STRING | 20 | — | File system path for item picture/image files |
| 11 | IS_PO_TAX | STRING | 1 | — | PO tax calculation enabled |
| 12 | IS_RETAIL_PRICE | STRING | 1 | — | Retail pricing module enabled |
| 13 | IS_RMA | STRING | 1 | — | RMA (Return Merchandise Authorization) module enabled |
| 14 | IS_SPEC_SUP | STRING | 1 | — | Special supervisor approval mode enabled |
| 15 | IS_SPEC_SUPF | INTEGER | 2 | — | Special supervisor from-level (minimum security level requiring supervisor sign-off) |
| 16 | IS_SPEC_SUPT | INTEGER | 2 | — | Special supervisor to-level (maximum level this applies to) |
| 17 | IS_TAX | STRING | 1 | — | Tax module enabled |
| 18 | IS_TAX_CVT | STRING | 1 | — | Tax currency conversion enabled |
| 19 | IS_TAX_FRM | STRING | 1 | — | Tax form printing enabled |
| 20 | IS_TAX_IN | STRING | 1 | — | Tax included in price (tax-inclusive pricing mode) |
| 21 | IS_UPC | STRING | 1 | — | UPC barcode module enabled |
| 22 | IS_UPC_1 | STRING | 6 | — | UPC manufacturer prefix (company portion of UPC barcode) |
| 23 | IS_UPC_2 | STRING | 5 | — | UPC system number suffix component |

## ISLANDF
**LANDED COST DEFAULTS** — GL account/department defaults for landed cost postings

Fields: 6 | Key: singleton

Three GL account+department pairs covering the main landed cost categories.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_LND_GLACF | STRING | 10 | — | GL account for customs/brokerage fee landed cost |
| 2 | ISIS_LND_GLADT | STRING | 10 | — | GL account for duty/tariff landed cost |
| 3 | ISIS_LND_GLAFR | STRING | 10 | — | GL account for freight landed cost |
| 4 | ISIS_LND_GLDCF | STRING | 4 | — | GL department for customs/brokerage fee |
| 5 | ISIS_LND_GLDDT | STRING | 4 | — | GL department for duty/tariff |
| 6 | ISIS_LND_GLDFR | STRING | 4 | — | GL department for freight |

## ISMCF
**MULTIPLE CURRENCY MASTER** — one record per supported currency

Fields: 49 | Key: ISIS_MCF_CODE

Defines each currency's identity, symbol, GL control accounts, and running balance accumulators.
At i2 Systems, single-currency — this table has 1 row (USD base currency).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_MCF_AMTAD | NUMERIC | 8 | 2 | AP discount exchange balance in this currency |
| 2 | ISIS_MCF_AMTAP | NUMERIC | 8 | 2 | Accounts payable open balance in this currency |
| 3 | ISIS_MCF_AMTAPD | NUMERIC | 8 | 2 | AP discount balance in this currency |
| 4 | ISIS_MCF_AMTAR | NUMERIC | 8 | 2 | Accounts receivable open balance in this currency |
| 5 | ISIS_MCF_AMTBNK | NUMERIC | 8 | 2 | Bank account balance in this currency |
| 6 | ISIS_MCF_AMTCS | NUMERIC | 8 | 2 | Cash receipts balance in this currency |
| 7 | ISIS_MCF_AMTFE | NUMERIC | 8 | 2 | Foreign exchange unrealized gain/loss balance |
| 8 | ISIS_MCF_AMTPOR | NUMERIC | 8 | 2 | PO receiving accrual balance (uninvoiced receipts) in this currency |
| 9 | ISIS_MCF_BASE | STRING | 1 | — | Base currency flag: `Y`=this is the domestic/functional currency |
| 10 | ISIS_MCF_CODE | STRING | 3 | — | ISO currency code (PK): USD, EUR, GBP, CAD, etc. |
| 11 | ISIS_MCF_DEC | INTEGER | 2 | — | Decimal places for this currency (2 for USD; 0 for JPY, etc.) |
| 12 | ISIS_MCF_DESC | STRING | 25 | — | Currency description (e.g., "US Dollars", "Euro") |
| 13 | ISIS_MCF_GLAADX | STRING | 10 | — | GL account for AP discount exchange gain/loss |
| 14 | ISIS_MCF_GLAAP | STRING | 10 | — | GL AP control account (accounts payable) |
| 15 | ISIS_MCF_GLAAPD | STRING | 10 | — | GL AP discount account |
| 16 | ISIS_MCF_GLAAPX | STRING | 10 | — | GL AP exchange gain/loss account |
| 17 | ISIS_MCF_GLAAR | STRING | 10 | — | GL AR control account (accounts receivable) |
| 18 | ISIS_MCF_GLAARD | STRING | 10 | — | GL AR discount account |
| 19 | ISIS_MCF_GLAARX | STRING | 10 | — | GL AR exchange gain/loss account |
| 20 | ISIS_MCF_GLABK | STRING | 10 | — | GL bank account |
| 21 | ISIS_MCF_GLABKX | STRING | 10 | — | GL bank exchange gain/loss account |
| 22 | ISIS_MCF_GLABS | STRING | 10 | — | GL balance sheet translation account (cumulative translation adjustment) |
| 23 | ISIS_MCF_GLACS | STRING | 10 | — | GL cash account (if separate from bank) |
| 24 | ISIS_MCF_GLACSX | STRING | 10 | — | GL cash exchange account |
| 25 | ISIS_MCF_GLAIS | STRING | 10 | — | GL intercompany settlement account |
| 26 | ISIS_MCF_GLAPDX | STRING | 10 | — | GL purchase discount exchange account |
| 27 | ISIS_MCF_GLAPO | STRING | 10 | — | GL PO accrual/uninvoiced receipts account |
| 28 | ISIS_MCF_GLAPOX | STRING | 10 | — | GL PO exchange gain/loss account |
| 29 | ISIS_MCF_GLDADX | STRING | 4 | — | GL dept for AP discount exchange |
| 30 | ISIS_MCF_GLDAP | STRING | 4 | — | GL dept for AP control |
| 31 | ISIS_MCF_GLDAPD | STRING | 4 | — | GL dept for AP discount |
| 32 | ISIS_MCF_GLDAPX | STRING | 4 | — | GL dept for AP exchange |
| 33 | ISIS_MCF_GLDAR | STRING | 4 | — | GL dept for AR control |
| 34 | ISIS_MCF_GLDARD | STRING | 4 | — | GL dept for AR discount |
| 35 | ISIS_MCF_GLDARX | STRING | 4 | — | GL dept for AR exchange |
| 36 | ISIS_MCF_GLDBK | STRING | 4 | — | GL dept for bank |
| 37 | ISIS_MCF_GLDBKX | STRING | 4 | — | GL dept for bank exchange |
| 38 | ISIS_MCF_GLDBS | STRING | 4 | — | GL dept for balance sheet translation |
| 39 | ISIS_MCF_GLDCS | STRING | 4 | — | GL dept for cash |
| 40 | ISIS_MCF_GLDCSX | STRING | 4 | — | GL dept for cash exchange |
| 41 | ISIS_MCF_GLDIS | STRING | 4 | — | GL dept for intercompany settlement |
| 42 | ISIS_MCF_GLDPDX | STRING | 4 | — | GL dept for purchase discount exchange |
| 43 | ISIS_MCF_GLDPO | STRING | 4 | — | GL dept for PO accrual |
| 44 | ISIS_MCF_GLDPOX | STRING | 4 | — | GL dept for PO exchange |
| 45 | ISIS_MCF_INTDAY | NUMERIC | 8 | — | Interest calculation days (for late payment interest) |
| 46 | ISIS_MCF_INTRES | NUMERIC | 8 | 3 | Interest reserve rate (percentage) |
| 47 | ISIS_MCF_SYMBOL | STRING | 1 | — | Currency symbol character (e.g., $, €, £) |
| 48 | ISIS_MCF_SYMDSC | STRING | 10 | — | Symbol description (e.g., "USD", "EUR") |
| 49 | ISIS_MCF_SYMPOS | STRING | 1 | — | Symbol position: `L`=before amount (prefix), `R`=after amount (suffix) |

## ISMCR
**MULTI-CURRENCY EXCHANGE RATE** — historical exchange rates by date

Fields: 22 | Key: ISIS_MCR_BASE + ISIS_MCR_DATE

One record per base currency × date. Up to 10 currency pair rates stored per row
(RATE_1..10 against SOURCE_1..10 counterpart currencies).

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_MCR_BASE | STRING | 3 | — | Base currency code (e.g., USD — the domestic functional currency) |
| 2 | ISIS_MCR_DATE | DATE | 4 | — | Rate effective date |
| 3 | ISIS_MCR_RATE_1 | NUMERIC | 8 | 6 | Exchange rate for currency slot 1 (units of SOURCE_1 per 1 BASE) |
| 4 | ISIS_MCR_RATE_10 | NUMERIC | 8 | 6 | Exchange rate for currency slot 10 |
| 5 | ISIS_MCR_RATE_2 | NUMERIC | 8 | 6 | Exchange rate for currency slot 2 |
| 6 | ISIS_MCR_RATE_3 | NUMERIC | 8 | 6 | Exchange rate for currency slot 3 |
| 7 | ISIS_MCR_RATE_4 | NUMERIC | 8 | 6 | Exchange rate for currency slot 4 |
| 8 | ISIS_MCR_RATE_5 | NUMERIC | 8 | 6 | Exchange rate for currency slot 5 |
| 9 | ISIS_MCR_RATE_6 | NUMERIC | 8 | 6 | Exchange rate for currency slot 6 |
| 10 | ISIS_MCR_RATE_7 | NUMERIC | 8 | 6 | Exchange rate for currency slot 7 |
| 11 | ISIS_MCR_RATE_8 | NUMERIC | 8 | 6 | Exchange rate for currency slot 8 |
| 12 | ISIS_MCR_RATE_9 | NUMERIC | 8 | 6 | Exchange rate for currency slot 9 |
| 13 | ISIS_MCR_SOURCE_1 | STRING | 3 | — | ISO code for currency slot 1 counterpart (e.g., EUR, GBP) |
| 14 | ISIS_MCR_SOURCE_10 | STRING | 3 | — | ISO code for currency slot 10 counterpart |
| 15 | ISIS_MCR_SOURCE_2 | STRING | 3 | — | ISO code for currency slot 2 counterpart |
| 16 | ISIS_MCR_SOURCE_3 | STRING | 3 | — | ISO code for currency slot 3 counterpart |
| 17 | ISIS_MCR_SOURCE_4 | STRING | 3 | — | ISO code for currency slot 4 counterpart |
| 18 | ISIS_MCR_SOURCE_5 | STRING | 3 | — | ISO code for currency slot 5 counterpart |
| 19 | ISIS_MCR_SOURCE_6 | STRING | 3 | — | ISO code for currency slot 6 counterpart |
| 20 | ISIS_MCR_SOURCE_7 | STRING | 3 | — | ISO code for currency slot 7 counterpart |
| 21 | ISIS_MCR_SOURCE_8 | STRING | 3 | — | ISO code for currency slot 8 counterpart |
| 22 | ISIS_MCR_SOURCE_9 | STRING | 3 | — | ISO code for currency slot 9 counterpart |

**Confidence: 78/100** — ISMCF confirmed-column (Y) fields from Excel validated; ISBROKER/ISDUTY/ISLANDF
meanings clear from import workflow context; ISIS flag semantics inferred from IS module architecture;
ISMCF GLA*/GLD* account pairing logic inferred from multi-currency accounting conventions; exact
IS_BROKER_TYPE values, IS_SPEC_SUP level semantics, and ISMCF balance update triggers require RWN decryption.
