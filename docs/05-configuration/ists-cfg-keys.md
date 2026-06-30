# ISTS.CFG.* Configuration Key Directory
Status: partial | verified-from-T7YSYN-symbol-table

## Overview

EvoERP stores its runtime configuration in two places:
- **BKYSMSTR** — system configuration table; holds all `ISTS.CFG.*` values
- **T7YSYN** — the BKYSMSTR editor program; its variable list is the most authoritative catalog of keys

The `ISTS.CFG.*` namespace is used inside TAS Pro programs to look up configuration values at runtime.
These keys are the human-readable names of fields/flags in BKYSMSTR.

**Source comparison:**
| Source | Key count | Notes |
|--------|-----------|-------|
| T7YSYN symbol table (this doc) | **495** | Authoritative — these have UI fields in the BKYSMSTR editor |
| grep across all rwn_strings files | ~535 | Wider but includes inferred/constructed key names; 40 extra may be computed at runtime |

The T7YSYN-based list is considered more reliable for "what settings actually exist and are user-configurable."

---

## Key Extraction

```python
# From rwn_symbols.json (pre-extracted symbol table for all 1,122 decrypted RWN programs)
for prog in data:
    if 'T7YSYN' in prog['path'].upper():
        cfg_keys = [v for v in prog['named_vars'] if 'ISTS.CFG.' in v]
```

T7YSYN is the BKYSMSTR editor (1,183 total named variables; 495 are ISTS.CFG keys).
Every ISTS.CFG key that appears in T7YSYN has a corresponding editor field in the system config UI.

---

## Prefix Distribution

| Prefix | Module | Count |
|--------|--------|-------|
| SO* | Sales Order | 75 |
| PO* | Purchase Order | 52 |
| WO* | Work Order | 39 |
| DC* | Data Collection | 35 |
| IN* | Inventory | 20 |
| AP* | Accounts Payable | 15 |
| HH* | Hand-Held devices | 15 |
| AR* | Accounts Receivable | 8 |
| SR* | Serial/Service tracking | 8 |
| RM*/RMD* | Return Merchandise Authorization | 12 |
| PR* | Payroll | 10 |
| AV* | Avalara tax integration | 5 |
| VO* | Void permissions (per module) | 6 |
| EV* | EvoNotes | 4 |
| CC* | Credit card | 4 |
| RO* | Routing | 3 |
| GL* | General Ledger | 3 |
| MR* | MRP | 3 |
| BM* | BOM | 3 |
| XC* | Cross-company | 4 |
| SM* | Messaging (SMG) | 3 |
| — | Global / misc | ~100 |

---

## Full Key Catalog by Module

### Global / System

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.ACCESS | Global access/permission check (read by all modules) |
| ISTS.CFG.PASSWD | Password required flag |
| ISTS.CFG.CFGLVL | Configuration security level |
| ISTS.CFG.ATOS | Auto-save / auto-post flag |
| ISTS.CFG.COORD | Screen coordinate mode |
| ISTS.CFG.DDNUM | Data dictionary number |
| ISTS.CFG.DIVOHD | Division overhead flag |
| ISTS.CFG.DIVSET | Division settings |
| ISTS.CFG.HREP | HR/employee report flag |
| ISTS.CFG.MAKCUS | Make-to-customer flag |
| ISTS.CFG.MSGLVL | Message level |
| ISTS.CFG.REPRT | Report output flag |
| ISTS.CFG.TPRTNT | Print-to-network flag |
| ISTS.CFG.ASTART | Auto-start flag |
| ISTS.CFG.AUTOPL | Auto place flag |
| ISTS.CFG.AUTOSL | Auto select flag |
| ISTS.CFG.BASEP | Base price mode |
| ISTS.CFG.BBCOLO | Background color |
| ISTS.CFG.BCCBOX | BCC box flag |
| ISTS.CFG.BILLTO | Bill-to override |
| ISTS.CFG.BLNKBN | Blank bin |
| ISTS.CFG.BLSTDC | Blank standard cost |
| ISTS.CFG.BOMRM | BOM remove flag |
| ISTS.CFG.BPSOQA | BP SO quantity |
| ISTS.CFG.BSCHKA | BS check A |
| ISTS.CFG.BSREF | BS reference |
| ISTS.CFG.BURDI | Burden indirect flag |
| ISTS.CFG.BURDN | Burden/overhead rate |
| ISTS.CFG.CANZWO | Cancel WO flag |
| ISTS.CFG.CAR8D | CAR 8D report flag |
| ISTS.CFG.CAROWN | CAR owner flag |
| ISTS.CFG.CATMST | Catalog master flag |
| ISTS.CFG.CHKBAL | Check balance flag |
| ISTS.CFG.CKSTDC | Check standard cost |
| ISTS.CFG.CLDISC | Class discount |
| ISTS.CFG.CMEST | Cost estimate flag |
| ISTS.CFG.CMPLOC | Component location |
| ISTS.CFG.CMQUOT | Cost/manufacturing quote |
| ISTS.CFG.COGSDP | COGS display |
| ISTS.CFG.CRHOLD | Credit hold flag |
| ISTS.CFG.CRMTTL | Credit memo total |
| ISTS.CFG.CROPEN | Credit open flag |
| ISTS.CFG.CRPSWD | Credit override password |
| ISTS.CFG.CSOUT | CS output flag |
| ISTS.CFG.CTRLBL | Control label |
| ISTS.CFG.DAYPAY | Day payment flag |
| ISTS.CFG.DBLKIT | Double kit flag |
| ISTS.CFG.DELBIN | Delete bin |
| ISTS.CFG.DISC99 | Discount 99 flag |
| ISTS.CFG.DSDTES | DS date test |
| ISTS.CFG.DTERES | Date resolution |
| ISTS.CFG.DUPLNS | Duplicate lines flag |
| ISTS.CFG.ECO | Engineering change order |
| ISTS.CFG.EPOQTY | Expected PO quantity |
| ISTS.CFG.ESAFRT | ESA freight flag |
| ISTS.CFG.ESDMSG | ESD message |
| ISTS.CFG.ESHMIC | ESH mic/mic flag |
| ISTS.CFG.FAMSG | FA message |
| ISTS.CFG.FOREC | Forecast flag |
| ISTS.CFG.FPCHK | FP check flag |
| ISTS.CFG.FPLOT | FP lot flag |
| ISTS.CFG.FPSER# | FP serial number |
| ISTS.CFG.FRTMAX | Freight maximum |
| ISTS.CFG.FTDSC | FTD description |
| ISTS.CFG.FXKEY | FX (currency) key |
| ISTS.CFG.GENBIN | Auto-generate bin |
| ISTS.CFG.GENITM | Auto-generate item |
| ISTS.CFG.HIDPTH | Hide path |
| ISTS.CFG.INKTDT | INK transaction date |
| ISTS.CFG.INVTTL | Inventory total flag |
| ISTS.CFG.ISTS | ISTS flag (self-identifier) |
| ISTS.CFG.ITP | ITP flag |
| ISTS.CFG.JOB | Job tracking enabled |
| ISTS.CFG.JOBCUS | Job customer flag |
| ISTS.CFG.JOBDEC | Job decimal places |
| ISTS.CFG.KITPRC | Kit pricing flag |
| ISTS.CFG.LABSC$ | Labor surcharge $ |
| ISTS.CFG.LEADHR | Lead hours |
| ISTS.CFG.LIMSCT | Limit scope |
| ISTS.CFG.LNGWT | Long weight flag |
| ISTS.CFG.LONGP | Long part number |
| ISTS.CFG.LOTWO | Lot WO tracking |
| ISTS.CFG.LRNUM | LR number |
| ISTS.CFG.LTWOSD | LT WO start date |
| ISTS.CFG.MANINV | Manual invoice flag |
| ISTS.CFG.MAXDC | Maximum DC sessions |
| ISTS.CFG.METIN | Metric input flag |
| ISTS.CFG.METR | Metric flag |
| ISTS.CFG.METSOF | Metric soft-convert |
| ISTS.CFG.MKFROM | Make-from flag |
| ISTS.CFG.MTERR | MT error flag |
| ISTS.CFG.NCRRMD | NCR remove date |
| ISTS.CFG.NEGCST | Negative cost handling |
| ISTS.CFG.NZETYP | Non-zero entry type |
| ISTS.CFG.OANDA | Open-and-do flag |
| ISTS.CFG.OQTYLN | Order quantity line |
| ISTS.CFG.ORDDSC | Order description |
| ISTS.CFG.ORIGPO | Original PO flag |
| ISTS.CFG.PICKT | Pick ticket flag |
| ISTS.CFG.PIPSW | PIP switch |
| ISTS.CFG.PIUID | PIP user ID |
| ISTS.CFG.PKINV | PK invoice |
| ISTS.CFG.PPTL | PP total flag |
| ISTS.CFG.PSFSEQ | PSF sequence |
| ISTS.CFG.PSTKIT | Post kit flag |
| ISTS.CFG.QTYADJ | Quantity adjustment |
| ISTS.CFG.QWOQTY | WO quantity flag |
| ISTS.CFG.RAISE | Raise flag |
| ISTS.CFG.RECYCL | Recycle/retain flag |
| ISTS.CFG.REVIEW | Review mode |
| ISTS.CFG.RRFPR | RR FP rate |
| ISTS.CFG.RTMSAV | RTM save flag |
| ISTS.CFG.RWOPER | RW operator flag |
| ISTS.CFG.RWWCT | RW work center |
| ISTS.CFG.SCCOMF | Scrap completion flag |
| ISTS.CFG.SCPMRK | Scrap mark |
| ISTS.CFG.SCRAP | Scrap tracking flag |
| ISTS.CFG.SCRCMP | Scrap complete flag |
| ISTS.CFG.SCRPQ | Scrap quantity flag |
| ISTS.CFG.SEQCHK | Sequence check flag |
| ISTS.CFG.SETQTY | Setup quantity |
| ISTS.CFG.SHIFT2 | Shift 2 enabled |
| ISTS.CFG.SHIFT3 | Shift 3 enabled |
| ISTS.CFG.SHPBIN | Ship bin |
| ISTS.CFG.SHPFOB | Ship FOB flag |
| ISTS.CFG.SHPHST | Ship history flag |
| ISTS.CFG.STDCST | Standard cost flag |
| ISTS.CFG.STDPK | Standard pack |
| ISTS.CFG.SUBCOS | Sub-cost flag |
| ISTS.CFG.TFNAME | Transfer filename |
| ISTS.CFG.TOOLLU | Tool lookup flag |
| ISTS.CFG.TRACK | Tracking flag |
| ISTS.CFG.TRKSER | Track serial |
| ISTS.CFG.TRNSCO | Transfer cost |
| ISTS.CFG.UCC14 | UCC-14 barcode flag |
| ISTS.CFG.UDMSTR | UD master flag |
| ISTS.CFG.UPLCST | Upload cost flag |
| ISTS.CFG.URNT | Unit rent flag |
| ISTS.CFG.USINI | US init flag |
| ISTS.CFG.USNGPR | Using price flag |
| ISTS.CFG.VACGLA | Vacation GL account A |
| ISTS.CFG.VACGLD | Vacation GL account D |
| ISTS.CFG.VNDEXP | Vendor expiry |
| ISTS.CFG.VNDPRX | Vendor prefix |
| ISTS.CFG.WARNTY | Warranty flag |
| ISTS.CFG.WCBF | Work center backflush |
| ISTS.CFG.WCDEPT | Work center department |
| ISTS.CFG.WHCTRL | Warehouse control |
| ISTS.CFG.WIPV | WIP valuation flag |
| ISTS.CFG.XDBA | Cross DBA flag |
| ISTS.CFG.XREBSS | Cross rebate SS |
| ISTS.CFG.ZPRCOM | Z-price commission |

---

### Access & Security

| Key | Meaning |
|-----|---------|
| ISTS.CFG.ACCESS | Global access/permission check (read by every module) |
| ISTS.CFG.PASSWD | Password required |
| ISTS.CFG.ARPSWD | AR password |
| ISTS.CFG.CRPSWD | Credit override password |
| ISTS.CFG.SOPSWD | SO password |
| ISTS.CFG.WOPSWD | WO password |
| ISTS.CFG.CFGLVL | Configuration access level |
| ISTS.CFG.EPASS | External/EDI password |

---

### Accounts Payable (AP*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.APADTE | AP date field A (aging period A) |
| ISTS.CFG.APBDTE | AP date field B (aging period B) |
| ISTS.CFG.APBSDT | AP base date |
| ISTS.CFG.APBVND | AP base/default vendor |
| ISTS.CFG.APCFTD | AP carry-forward date |
| ISTS.CFG.APCFTT | AP carry-forward type |
| ISTS.CFG.APCGLA | AP cost GL account A |
| ISTS.CFG.APCGLD | AP cost GL account D |
| ISTS.CFG.APCHK | AP check flag (enable check printing) |
| ISTS.CFG.APHXPT | AP hex print (dot-matrix format flag) |
| ISTS.CFG.APLANG | AP language |
| ISTS.CFG.APPRIX | AP price index |
| ISTS.CFG.APPVND | AP primary vendor flag |
| ISTS.CFG.APSORT | AP sort order preference |
| ISTS.CFG.APSTDC | AP standard cost flag |

AP check format is controlled by **BKYS.YN[48]** (not an ISTS.CFG key):
`'1'/'4'/'5'` → laser format (chains to BKAPHA); `'2'/'3'` → dot-matrix (BKAPH).

---

### Accounts Receivable (AR*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.ARADTE | AR date (aging base date) |
| ISTS.CFG.ARCBOM | AR customer BOM flag |
| ISTS.CFG.ARCSDT | AR customer start date |
| ISTS.CFG.AREMD | AR email/EDI flag |
| ISTS.CFG.ARFTD | AR future transaction date |
| ISTS.CFG.ARLCST | AR last cost flag |
| ISTS.CFG.ARPSWD | AR password |
| ISTS.CFG.ARSORT | AR sort order |

---

### Avalara Tax Integration (AV*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.AVAACT | Avalara active flag |
| ISTS.CFG.AVACO | Avalara company code |
| ISTS.CFG.AVACOD | Avalara tax code |
| ISTS.CFG.AVAKEY | Avalara API key |
| ISTS.CFG.AVATAX | Avalara tax enabled |

*Avalara is a cloud-based sales tax service. Presence of 5 ISTS.CFG keys confirms EvoERP has Avalara integration.*

---

### BOM Configuration (BM*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.BMAREF | BOM reference flag |
| ISTS.CFG.BMGADT | BOM global date |
| ISTS.CFG.BMTYPR | BOM type range |

---

### Credit Card (CC*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.CC | Credit card processing enabled |
| ISTS.CFG.CCDEF | CC default card type |
| ISTS.CFG.CCPSW | CC processing password |
| ISTS.CFG.CCUID | CC processor user ID |

---

### Analysis / Notifications (AN*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.ANAPA | Analysis AP A notification |
| ISTS.CFG.ANARA | Analysis AR A notification |

---

### Data Collection (DC*) — 35 keys

| Key | Inferred meaning | Confirmed |
|-----|-----------------|-----------|
| ISTS.CFG.DCABRK | DC session break threshold | inferred |
| ISTS.CFG.DCAENG | DC engine type / entry mode | inferred |
| ISTS.CFG.DCAHHD | DC hand-held device flag | inferred |
| ISTS.CFG.DCAPW1 | DC password 1 | inferred |
| ISTS.CFG.DCAPW2 | DC password 2 | inferred |
| ISTS.CFG.DCARUN | DC run mode flag | inferred |
| ISTS.CFG.DCAWC | DC default work center | inferred |
| ISTS.CFG.DCBEMP | DC barcode employee prefix | inferred |
| ISTS.CFG.DCCMP% | DC completion percentage threshold | inferred |
| ISTS.CFG.DCCOMP | DC completion tracking flag | inferred |
| ISTS.CFG.DCCQTY | DC current quantity tracking | inferred |
| ISTS.CFG.DCDAYS | DC history retention days | inferred |
| ISTS.CFG.DCDQTY | DC daily quantity threshold | inferred |
| ISTS.CFG.DCFREQ | DC polling/update frequency | inferred |
| ISTS.CFG.DCHLS | DC hours lookback | inferred |
| ISTS.CFG.DCIRWK | DC in-rework tracking flag | inferred |
| ISTS.CFG.DCLOGN | DC login required | inferred |
| ISTS.CFG.DCMACH | DC machine tracking | inferred |
| ISTS.CFG.DCMLST | DC machine list | inferred |
| ISTS.CFG.DCNCR | DC non-conformance report flag | inferred |
| ISTS.CFG.DCNEG | DC allow negative quantities | inferred |
| ISTS.CFG.DCNOSC | DC no-scan mode | inferred |
| ISTS.CFG.DCOASA | DC OA scrap A | inferred |
| ISTS.CFG.DCOASD | DC OA scrap D | inferred |
| ISTS.CFG.DCPDTE | DC process date override | inferred |
| ISTS.CFG.DCPREQ | DC prerequisite/prequalify flag | inferred |
| ISTS.CFG.DCREWK | DC rework tracking | inferred |
| ISTS.CFG.DCRSH | DC rush job flag | inferred |
| ISTS.CFG.DCSCRP | DC scrap tracking | inferred |
| ISTS.CFG.DCSEQ | DC sequence/screen mode — YN[228]: Y=mount BKDCAF alternate screen | **confirmed from BKDCA.SRC:193** |
| ISTS.CFG.DCSQTY | DC scanned quantity field | inferred |
| ISTS.CFG.DCSYNC | DC synchronize/auto-close — YN[229]: Y=auto-close on new job start | **confirmed from BKDCA.SRC** |
| ISTS.CFG.DCTIME | DC time tracking flag | inferred |
| ISTS.CFG.DCTMSS | DC time miss threshold | inferred |
| ISTS.CFG.DCTSWC | DC time-switch work center | inferred |

DC variant entry (from BKDCA.SRC):
- **DCA** — full labor entry: WO/Seq/Start/Finish/Parts/Scrap/Runhrs
- **DCB** — barcode scan: WO/Seq/Parts/Scrap only (no times)
- **DCC** — time only: WO/Seq/Start/Finish/Runhrs (no parts/scrap)

---

### EvoNotes (EV*)

| Key | Meaning |
|-----|---------|
| ISTS.CFG.EVOALT | EvoNotes alternate storage path |
| ISTS.CFG.EVOLNK | EvoNotes link flag |
| ISTS.CFG.EVOMAX | EvoNotes max entries |
| ISTS.CFG.EVONTS | EvoNotes enabled |

---

### General Ledger (GL*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.GLBSDT | GL base date |
| ISTS.CFG.GLCTRL | GL control flag |
| ISTS.CFG.GLDATE | GL date mode |

---

### Hand-Held Devices (HH*) — 15 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.HHALOT | HH allow lot tracking |
| ISTS.CFG.HHANEG | HH allow negative quantities |
| ISTS.CFG.HHASER | HH allow serial tracking |
| ISTS.CFG.HHCKIT | HH complete kit flag |
| ISTS.CFG.HHCPW1 | HH password 1 |
| ISTS.CFG.HHCPW2 | HH password 2 |
| ISTS.CFG.HHDBIN | HH default bin |
| ISTS.CFG.HHDCWO | HH DC work order mode |
| ISTS.CFG.HHEQTY | HH expected quantity |
| ISTS.CFG.HHFLOC | HH from-location |
| ISTS.CFG.HHLBLS | HH labels flag |
| ISTS.CFG.HHMAXQ | HH max quantity |
| ISTS.CFG.HHPOLN | HH PO line mode |
| ISTS.CFG.HHRALL | HH receive-all flag |
| ISTS.CFG.HHTLOC | HH to-location |

---

### Inventory (IN*) — 20 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.INACT | Inventory active flag |
| ISTS.CFG.INACUD | Inventory AC user-defined field |
| ISTS.CFG.INADTE | Inventory date |
| ISTS.CFG.INAMRP | Inventory auto-MRP flag |
| ISTS.CFG.INBBMA | INB BOM adjust flag |
| ISTS.CFG.INBBMR | INB BOM reorder flag |
| ISTS.CFG.INBCOC | INB cost-of-change flag |
| ISTS.CFG.INBESA | INB estimated standard adjust |
| ISTS.CFG.INBLS | INB labels |
| ISTS.CFG.INBPIC | INB picklist flag |
| ISTS.CFG.INBPOA | INB PO adjust |
| ISTS.CFG.INBSOA | INB SO adjust |
| ISTS.CFG.INBSOP | INB SO print |
| ISTS.CFG.INBTLS | INB total labels |
| ISTS.CFG.INBWOA | INB WO adjust |
| ISTS.CFG.INBXFR | INB transfer flag |
| ISTS.CFG.INCGL | Inventory cost GL flag |
| ISTS.CFG.INCNEG | Inventory cost negative flag |
| ISTS.CFG.INKTDT | INK transaction date |
| ISTS.CFG.INVTTL | Inventory total flag |

---

### Messaging / EvoSync (SM*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.SMGBDT | SMG begin date |
| ISTS.CFG.SMGEDT | SMG end date |
| ISTS.CFG.SMGSYN | SMG sync flag |

---

### MRP (MR*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.MRFDTE | MRP from-date |
| ISTS.CFG.MRPDAY | MRP planning horizon (days) |
| ISTS.CFG.MRPDOL | MRP dollar threshold |

---

### Payroll (PR*) — 10 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.PRCAT1 | Payroll category 1 |
| ISTS.CFG.PRCAT2 | Payroll category 2 |
| ISTS.CFG.PRCAT3 | Payroll category 3 |
| ISTS.CFG.PRCDTE | Payroll check date |
| ISTS.CFG.PRPOST | Payroll post flag |
| ISTS.CFG.PRQPST | Payroll quick-post flag |
| ISTS.CFG.PRSSNX | Payroll SSN export flag |
| ISTS.CFG.PRTL | Payroll total flag |
| ISTS.CFG.PRTPS | Payroll tips |
| ISTS.CFG.PRTSOA | Payroll SO allocation |

---

### Purchase Order (PO*) — 52 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.POACAL | PO calendar flag |
| ISTS.CFG.POACLS | PO close flag |
| ISTS.CFG.POADD | PO add flag |
| ISTS.CFG.POADEL | PO delete flag |
| ISTS.CFG.POADSC | PO description flag |
| ISTS.CFG.POADUE | PO due date flag |
| ISTS.CFG.POADYS | PO default days |
| ISTS.CFG.POAEBY | PO entered-by flag |
| ISTS.CFG.POAMFG | PO manufacturer flag |
| ISTS.CFG.POANO$ | PO amount (no-dollar display?) |
| ISTS.CFG.POAPOH | PO approval on-hold |
| ISTS.CFG.POARSK | PO archive key |
| ISTS.CFG.POASLM | PO allow slim/abbreviated mode |
| ISTS.CFG.POAVDT | PO vendor date |
| ISTS.CFG.POAVND | PO allow vendor |
| ISTS.CFG.POBLNS | PO blank lines |
| ISTS.CFG.POBSIG | PO buyer signature |
| ISTS.CFG.POCBF | PO carry-back flag |
| ISTS.CFG.POCBIN | PO bin location tracking |
| ISTS.CFG.POCERD | PO edit/range date |
| ISTS.CFG.POCFRT | PO freight flag |
| ISTS.CFG.POCHG | PO charge flag |
| ISTS.CFG.POCHK | PO check flag |
| ISTS.CFG.POCLBL | PO label flag |
| ISTS.CFG.POCLC0 | PO location control 0 |
| ISTS.CFG.POCLOT | PO lot tracking |
| ISTS.CFG.POCPIE | PO price percentage |
| ISTS.CFG.POCPJB | PO project/job flag |
| ISTS.CFG.POCPLL | PO pallet flag |
| ISTS.CFG.POCPV | PO print vendor flag |
| ISTS.CFG.POCRC2 | PO receipt 2 flag |
| ISTS.CFG.POCRN | PO create RN (receiving note) |
| ISTS.CFG.POCSER | PO serial tracking |
| ISTS.CFG.POCSTD | PO standard cost |
| ISTS.CFG.POCUCV | PO currency value flag |
| ISTS.CFG.POEDTE | PO expiration date |
| ISTS.CFG.POEPRX | PO extended price prefix |
| ISTS.CFG.POGLED | PO GL edit flag |
| ISTS.CFG.POGLTY | PO GL type |
| ISTS.CFG.POONLY | PO-only mode |
| ISTS.CFG.POPAMT | PO payment amount flag |
| ISTS.CFG.POPCOM | PO PO comment |
| ISTS.CFG.POPCRH | PO price change flag |
| ISTS.CFG.POPRIX | PO price index |
| ISTS.CFG.POPROM | PO promo flag |
| ISTS.CFG.POPSLP | PO packing slip flag |
| ISTS.CFG.POQITM | PO quantity-per-item threshold |
| ISTS.CFG.POQPRC | PO quantity price |
| ISTS.CFG.POREV | PO revision tracking |
| ISTS.CFG.POSEC | PO security flag |
| ISTS.CFG.POSIGN | PO signature required |
| ISTS.CFG.POXLOC | PO transfer location |

---

### Return Merchandise Authorization (RM*/RMD*) — 12 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.RMAAMT | RMA amount threshold |
| ISTS.CFG.RMACDT | RMA create date |
| ISTS.CFG.RMAFLT | RMA filter flag |
| ISTS.CFG.RMAINF | RMA info flag |
| ISTS.CFG.RMAMST | RMA master flag |
| ISTS.CFG.RMASTK | RMA stock adjustment |
| ISTS.CFG.RMAUPD | RMA update flag |
| ISTS.CFG.RMDACM | RMD accumulated flag |
| ISTS.CFG.RMDCWO | RMD credit work order |
| ISTS.CFG.RMDGLA | RMD GL account A |
| ISTS.CFG.RMDGLD | RMD GL account D |
| ISTS.CFG.RMDSRQ | RMD service request |

*12 RMA keys confirms EvoERP has a full Return Merchandise Authorization subsystem.*

---

### Routing (RO*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.ROADEC | Routing decimal places |
| ISTS.CFG.ROSTTY | Routing station type |
| ISTS.CFG.ROTTY | Routing type |

Additional routing YN flags (from BKROA.SRC source):
- YN[36] = default process hours; YN[37] = default std time; YN[38] = use template# as seq# (WOCALC); YN[66] = prompt for long time

---

### Sales Order (SO*) — 75 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.SOAARN | SO AR note flag |
| ISTS.CFG.SOAATT | SO attachment flag |
| ISTS.CFG.SOAAUD | SO audit flag |
| ISTS.CFG.SOACAL | SO calendar flag |
| ISTS.CFG.SOACDL | SO acknowledgment delivery |
| ISTS.CFG.SOACDT | SO acknowledgment date |
| ISTS.CFG.SOACFC | SO FC (freight charge?) flag |
| ISTS.CFG.SOACOM | SO company flag |
| ISTS.CFG.SOADEL | SO delete flag |
| ISTS.CFG.SOADSC | SO description flag |
| ISTS.CFG.SOAGPP | SO group price |
| ISTS.CFG.SOAINC | SO include flag |
| ISTS.CFG.SOAITM | SO item flag |
| ISTS.CFG.SOALOC | SO location flag |
| ISTS.CFG.SOAMA% | SO amount margin % |
| ISTS.CFG.SOAMAR | SO margin flag |
| ISTS.CFG.SOANO$ | SO amount (no-dollar display?) |
| ISTS.CFG.SOARCH | SO archive flag |
| ISTS.CFG.SOAREP | SO report flag |
| ISTS.CFG.SOASHP | SO ship flag |
| ISTS.CFG.SOASPK | SO salesperson/speaker flag |
| ISTS.CFG.SOASTN | SO station flag |
| ISTS.CFG.SOAUD | SO audit (2nd level) |
| ISTS.CFG.SOAUPC | SO UPC flag |
| ISTS.CFG.SOAVCK | SO availability check |
| ISTS.CFG.SOAXRF | SO cross-reference flag |
| ISTS.CFG.SOBLNS | SO blank lines |
| ISTS.CFG.SOCBOL | SO bill of lading |
| ISTS.CFG.SOCHG | SO change flag |
| ISTS.CFG.SOCLNS | SO close lines |
| ISTS.CFG.SOCOPY | SO copy flag |
| ISTS.CFG.SOCRTM | SO credit terms |
| ISTS.CFG.SOCUST | SO customer flag |
| ISTS.CFG.SODATE | SO date mode |
| ISTS.CFG.SODAYS | SO default days |
| ISTS.CFG.SODEL | SO delete |
| ISTS.CFG.SODWO | SO direct work order |
| ISTS.CFG.SOECDL | SO EDI delivery |
| ISTS.CFG.SOEDTE | SO end date |
| ISTS.CFG.SOEGSB | SO GSB (government?) flag |
| ISTS.CFG.SOELAB | SO extra label |
| ISTS.CFG.SOELOT | SO extra lot |
| ISTS.CFG.SOENBY | SO entered-by flag |
| ISTS.CFG.SOESDT | SO extra start date |
| ISTS.CFG.SOESER | SO extra serial |
| ISTS.CFG.SOESUR | SO extra surcharge |
| ISTS.CFG.SOEUBO | SO EU bill-of flag |
| ISTS.CFG.SOEVIA | SO extra via |
| ISTS.CFG.SOFLNS | SO fill lines |
| ISTS.CFG.SOFSND | SO fax/send flag |
| ISTS.CFG.SOGCFC | SO GC freight charge |
| ISTS.CFG.SOINFO | SO info flag |
| ISTS.CFG.SOIOC | SO IOC (immediate-or-cancel) |
| ISTS.CFG.SOITMZ | SO item zero flag |
| ISTS.CFG.SOLDYS | SO lead days |
| ISTS.CFG.SOLEAD | SO lead time |
| ISTS.CFG.SOLLOC | SO lower location |
| ISTS.CFG.SOLOT | SO lot tracking |
| ISTS.CFG.SONENG | SO no-engine mode |
| ISTS.CFG.SONMY | SO no-my-company flag |
| ISTS.CFG.SOONLY | SO-only mode |
| ISTS.CFG.SOOPEN | SO open flag |
| ISTS.CFG.SOPBLW | SO print below |
| ISTS.CFG.SOPCQT | SO price quoted |
| ISTS.CFG.SOPRCE | SO price flag |
| ISTS.CFG.SOPSWD | SO password |
| ISTS.CFG.SORND | SO round |
| ISTS.CFG.SORNDD | SO round down |
| ISTS.CFG.SORTS | SO sort |
| ISTS.CFG.SOSEC | SO security |
| ISTS.CFG.SOSER | SO serial tracking |
| ISTS.CFG.SOSPEC | SO special flag |
| ISTS.CFG.SOSTDP | SO standard price |
| ISTS.CFG.SOUPCH | SO up-charge |
| ISTS.CFG.SOXREF | SO cross-reference |

---

### Serial / Service Tracking (SR*) — 8 keys

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.SRAWOS | SR work order service flag |
| ISTS.CFG.SRBOM | SR BOM flag |
| ISTS.CFG.SRCBOM | SR customer BOM |
| ISTS.CFG.SRCOMM | SR commission flag |
| ISTS.CFG.SRINFO | SR info flag |
| ISTS.CFG.SRLOC | SR location flag |
| ISTS.CFG.SRPART | SR part flag |
| ISTS.CFG.SRTRAK | SR tracking flag |

---

### Ship-Via

| Key | Meaning |
|-----|---------|
| ISTS.CFG.VIACUS | Ship-via customer flag |
| ISTS.CFG.VIAMST | Ship-via master toggle |
| ISTS.CFG.VIAVND | Ship-via vendor flag |

---

### Void Permissions (VO*) — per-module void control

| Key | Meaning |
|-----|---------|
| ISTS.CFG.VOAP | Allow void in AP |
| ISTS.CFG.VOAR | Allow void in AR |
| ISTS.CFG.VOIC | Allow void in Inventory/Cost |
| ISTS.CFG.VOPO | Allow void in PO |
| ISTS.CFG.VOSO | Allow void in SO |
| ISTS.CFG.VOWO | Allow void in WO |

*Each flag controls whether users can void transactions in that module. Clean namespace design.*

---

### Work Order (WO*) — 39 keys

| Key | Inferred meaning | Confirmed |
|-----|-----------------|-----------|
| ISTS.CFG.WOABMR | WO add BOM revision | inferred |
| ISTS.CFG.WOADSC | WO description flag | inferred |
| ISTS.CFG.WOALOC | WO location flag | inferred |
| ISTS.CFG.WOAVCK | WO availability check | inferred |
| ISTS.CFG.WOAWN | WO auto WO number | inferred |
| ISTS.CFG.WOBASE | WO base calculation | inferred |
| ISTS.CFG.WOBS | WO balance sheet flag | inferred |
| ISTS.CFG.WOBWO1 | WO backflush WO 1 | inferred |
| ISTS.CFG.WOCALC | WO cost calculation method — YN[38]: Y=use template# as seq# | **confirmed from BKROA.SRC** |
| ISTS.CFG.WOCHDR | WO header flag | inferred |
| ISTS.CFG.WODSO | WO direct SO flag | inferred |
| ISTS.CFG.WOFAMI | WO family flag | inferred |
| ISTS.CFG.WOFDEC | WO family decimal | inferred |
| ISTS.CFG.WOFHOL | WO family holiday | inferred |
| ISTS.CFG.WOFOTH | WO family other | inferred |
| ISTS.CFG.WOFTEM | WO family template | inferred |
| ISTS.CFG.WOGADD | WO GA add flag | inferred |
| ISTS.CFG.WOGDSC | WO general description | inferred |
| ISTS.CFG.WOGKIT | WO kit generation | inferred |
| ISTS.CFG.WOGLOC | WO GL location | inferred |
| ISTS.CFG.WOGNEG | WO negative flag | inferred |
| ISTS.CFG.WOICST | WO individual cost | inferred |
| ISTS.CFG.WOILTX | WO IL tax | inferred |
| ISTS.CFG.WOIRND | WO in-round (sequence) | inferred |
| ISTS.CFG.WOISC% | WO ISC percentage | inferred |
| ISTS.CFG.WOISER | WO ISR flag | inferred |
| ISTS.CFG.WOITXN | WO inventory transaction flag | inferred |
| ISTS.CFG.WOIWOF | WO in-work-order flow | inferred |
| ISTS.CFG.WOJCLS | WO job close flag | inferred |
| ISTS.CFG.WOLBLS | WO labels | inferred |
| ISTS.CFG.WOMAKF | WO make-from flag | inferred |
| ISTS.CFG.WOMPST | WO master post flag | inferred |
| ISTS.CFG.WONEG | WO negative (second level) | inferred |
| ISTS.CFG.WOONLY | WO-only mode | inferred |
| ISTS.CFG.WOOPEN | WO open flag | inferred |
| ISTS.CFG.WOOVER | WO override flag | inferred |
| ISTS.CFG.WOPSWD | WO password | inferred |
| ISTS.CFG.WOSODT | WO SO date flag | inferred |
| ISTS.CFG.WOSSER | WO serial number service | inferred |

---

### Cross-Company / Cross-Module (XC*)

| Key | Inferred meaning |
|-----|-----------------|
| ISTS.CFG.XCMSOA | Cross-company SO/AR flag |
| ISTS.CFG.XCOMA | Cross-company A flag |
| ISTS.CFG.XCOMH | Cross-company H flag |
| ISTS.CFG.XCOMM | Cross-company M flag |

---

## Notes on YN[N] ↔ ISTS.CFG.* Mapping

In TAS Pro source, BKYSMSTR flags are accessed as `BKYS.YN[N]`.
The `ISTS.CFG.*` key string is the alias used to look up the numeric index at runtime.

BKYSMSTR has exactly **250 YN columns** (BKYS_YN_1 through BKYS_YN_250), confirmed from
live DSN=DBA ODBC schema query (Pass 382, 2026-06-29). The prior "354" figure was incorrect.

The 250 YN flags and the 495 ISTS.CFG keys are not 1:1 — some keys map to
BKYSMSTR string/numeric fields rather than YN flags.

### Confidence key
- **SRC** = confirmed from TAS Pro source code (highest confidence)
- **DFM** = matched from T7MDefaults.DFM by Top-position pairing (medium confidence; Setup tab entries less reliable due to label density)
- **inferred** = guessed from key name (low confidence)

### Full YN[N] Mapping Table (Pass 379+382, 2026-06-29)

**88 unique indices** (89 rows — YN[15] duplicated) of **250 total** YN[N] slots in BKYSMSTR.
Sources: `samples/T7MDefaults.DFM` (81 unique, parsed by `scripts/parse_mdefaults_dfm2.py`) +
`samples/dfm/T7MDefNDC.DFM` (8 additional: YN[200,202,209,212,213,214,215,218]) +
SRC file evidence (10 slots with direct code confirmation).
Remaining ~162 slots (of 250) not bound in any DFM — set programmatically or from other screens.

| YN[N] | Tab | Description | ISTS.CFG Key | Source |
|-------|-----|-------------|--------------|--------|
| YN[1] | Setup | Post COGS Transactions? | unknown | DFM |
| YN[2] | Setup | Post Inventory Adjustments? | unknown | DFM |
| YN[3] | Processing | Prevent Item Creation from ES-A | unknown | DFM |
| YN[4] | Setup | Fiscal Year Start Date | unknown | DFM |
| YN[5] | Setup | Post WO Transactions? | unknown | DFM |
| YN[15] | Processing | PO-A Default for change dates (Y,N) | unknown | DFM |
| YN[15] | Routing | ROB: Print Fixed and Variable Overhead as % (Y/N) | unknown | DFM (duplicate index — two controls share YN[15]) |
| YN[16] | Sales Commissions | Enter Commissions at Sales Order Entry? [Y/N] | unknown | DFM |
| YN[17] | Sales Commissions | Enter Commissions at Line Item Entry? [Y/N] | unknown | DFM |
| YN[18] | Sales Commissions | Enter Commissions for 2 Salespersons? [Y/N] | unknown | DFM |
| YN[19] | Processing | SOQA/INB: Disable Base Price passdown to subsid Co | unknown | DFM |
| YN[20] | Processing | Use Long Weight in Calculations? | ISTS.CFG.LNGWT | DFM+SRC (BKDCA:708 barcode flag) |
| YN[21] | Processing | IN-A: Disable Rebuild Stock Status | unknown | DFM |
| YN[22] | Processing | WOJ: Process WIP Variance | unknown | DFM |
| YN[23] | BOM | Require Sequence Entry - Type N (Non Inventory)? | unknown | DFM |
| YN[24] | BOM | Require Sequence Entry - Type L (Labor)? | unknown | DFM |
| YN[25] | BOM | Require Sequence Entry - Type T (Out Process)? | unknown | DFM |
| YN[26] | BOM | Require Sequence Entry - Type R, M, F, A? | unknown | DFM |
| YN[27] | Setup | Post PO Transactions? | unknown | DFM |
| YN[28] | Features / Options | Suppress Option Headers, Footers, Indents? | unknown | DFM |
| YN[29] | Setup | Copy Cust PO#s from WO#s as comment lines | unknown | DFM |
| YN[30] | Setup | AP-C Price change update PO Line price (Y/N/A) | unknown | DFM |
| YN[31] | Processing | IN-A: Disable Rebuild Stock Status | unknown | DFM |
| YN[32] | Setup | Copy Cust PO#s from WO#s as comment lines | unknown | DFM (may be same label/different variant) |
| YN[33] | Setup | Invoice PO Receipts through AP | unknown | DFM |
| YN[35] | Setup | Open Period End Date | unknown | DFM |
| YN[36] | Routing | Multiply or Divide by number of processes? (M/D) | unknown | DFM+SRC (BKROA.SRC:609) |
| YN[37] | Routing | Use standard time? | unknown | DFM+SRC (BKROA.SRC:656) |
| YN[38] | Routing | Make sequence equal template number? | ISTS.CFG.WOCALC | DFM+SRC (BKROA.SRC:392,1582) |
| YN[39] | Printing | SO Packing Slip form format: 1=SOC1.RTM (condensed), 2=SOC2.RTM (single qty), 3=SOC3.RTM (plain condensed), 4=SOC4.RTM (plain single qty) | unknown | DFM |
| YN[40] | Setup | Post Inventory Adjustments? | unknown | DFM (Top-pair may overlap YN[2] label) |
| YN[41] | Printing | Print Ending Lines (PO form?) | unknown | DFM |
| YN[42] | Printing | Sales Order Ending Lines (variant) | unknown | DFM |
| YN[43] | Printing | Print Title on RFQ? | unknown | DFM |
| YN[44] | Printing | Sales Quote Print Format Number | unknown | DFM |
| YN[45] | Printing | Print Discount Column on Forms? | unknown | DFM |
| YN[46] | Printing | Print Co. Name/Address on Forms? | unknown | DFM |
| YN[47] | Checking | Payroll check form format: 1=PRD1.RTM (laser), 2=PRD2.RTM (continuous) | unknown | DFM |
| YN[48] | Checking | AP check form format: 1=APHA1.RTM (stub/check/stub), 2=APH1.RTM (continuous), 4=APHA2.RTM (stub/stub/check), 5=APHA3.RTM (check/stub/stub) | unknown | DFM+SRC (Bkaph.src:60-81) |
| YN[50] | Setup | Post PO Transactions? | unknown | DFM (may overlap YN[27] label) |
| YN[57] | Scheduling | Display machine prompt in Enter Labor? | unknown | DFM |
| YN[59] | Scheduling | Allow entry to overlap settings in routings? | unknown | DFM+SRC (BKROA.SRC:647) |
| YN[62] | Printing | Decimalized Quantities on Forms? | unknown | DFM |
| YN[63] | Printing | Decimalized Quantities on Forms? | unknown | DFM (variant of YN[62]?) |
| YN[64] | Printing | Print Title on: Acknowledgments | unknown | DFM |
| YN[65] | Processing | Divide Overhead by # of Jobs Worked | unknown | DFM |
| YN[66] | Routing | Display long time prompt? | unknown | DFM+SRC (BKROA.SRC:629) |
| YN[67] | MRP | Include in MRP Generation? | unknown | DFM |
| YN[73] | Processing | Prevent Item Creation from PI-C | unknown | DFM |
| YN[74] | Printing | Print Discount Column on Forms? | unknown | DFM |
| YN[76] | Printing | SO Acknowledgment form format: 1=SOB1.RTM, 2=SOB2.RTM, 3=SOB3.RTM, 4=SOB4.RTM | unknown | DFM |
| YN[77] | Printing | SO Quote form format: 1=SOPB1.RTM, 2=SOPB2.RTM, 3=SOPB3.RTM, 4=SOPB4.RTM | unknown | DFM |
| YN[78] | Printing | PO form format: 1=POE1.RTM (universal), 2=POE2.RTM (plain paper) | unknown | DFM |
| YN[79] | Legacy Settings | Prompt for save in Enter Accounts? | unknown | DFM |
| YN[80] | Printing | Print Ending Lines (PO?) | unknown | DFM |
| YN[82] | Printing | Packing Slips (format number?) | unknown | DFM |
| YN[83] | Processing | SOQA/INB: Disable Base Price passdown to subsid Co | unknown | DFM |
| YN[84] | Processing | WOJ: Process WIP Variance | unknown | DFM |
| YN[85] | Processing | Divide Overhead by # of Jobs Worked | unknown | DFM |
| YN[86] | Processing | Prevent Item Creation from ES-A | unknown | DFM |
| YN[87] | Acct. Receivables | Print Co. Name/Addr on Statement | unknown | DFM |
| YN[200] | Scheduling | Use Lead Time Scheduling [F/B/N] | unknown | DFM |
| YN[202] | Processing | PO-C to update Std. Cost if Cost is $0.00 | unknown | DFM |
| YN[209] | Setup | Use Accounting Open Period Start Date in GL-B (label from backwards-scan in Setup tab) | unknown | DFM (approx) |
| YN[212] | Setup | Use Accounting Open Period Start Date in AP-B | unknown | DFM (approx) |
| YN[213] | Setup | Use Accounting Open Period Start Date in AR-C | unknown | DFM (approx) |
| YN[214] | Setup | (label ambiguous — Setup tab density) | unknown | DFM (approx) |
| YN[215] | Setup | (label ambiguous — Setup tab density) | unknown | DFM (approx) |
| YN[218] | Setup | DC-A/DC-C: Round Shift Start/Stop by X minutes | unknown | DFM |
| YN[220] | Printing | Invoices (format number?) | unknown | DFM |
| YN[222] | Setup | GL Department | unknown | DFM |
| YN[223] | Setup | Location | unknown | DFM |
| YN[225] | Processing | SOQA/INB: Disable Base Price passdown to subsid Co (variant) | unknown | DFM |
| YN[228] | Setup | DC-B/DC-G/WO-M: Default for Scrap Prompt | ISTS.CFG.DCSEQ | DFM+SRC (BKDCA.SRC:193-201) |
| YN[229] | Setup | Multijob DC auto-close on new job start | ISTS.CFG.DCSYNC | DFM+SRC (BKDCA.SRC) |
| YN[230] | Acct. Receivables | Invoice Age based on (1) age or (2) days past due | unknown | DFM |
| YN[231] | Setup | Open Period End Date | unknown | DFM |
| YN[237] | Scheduling | PO & DC update the actual start/finish dates of sequences? | unknown | DFM |
| YN[238] | Setup | Disable Recalc Est Cost in WO-A | unknown | DFM |
| YN[239] | Setup | Allow WOs for Make From Items | unknown | DFM |
| YN[240] | Estimates | Print Title on Quote? | unknown | DFM |
| YN[241] | Printing | Print Title on RFQ? | unknown | DFM |
| YN[242] | Printing | Print Co. Name/Address on Forms? | unknown | DFM |
| YN[243] | Printing | Sales Quotes (format number?) | unknown | DFM |
| YN[244] | Printing | Invoices (format number?) | unknown | DFM |
| YN[245] | Printing | Packing Slips (format number?) | unknown | DFM |
| YN[246] | Printing | Print Title on: Acknowledgments | unknown | DFM |
| YN[247] | Acct. Receivables | Print Title on Statement | unknown | DFM |
| YN[248] | MRP | Round MRP quantities to the next whole number? | unknown | DFM |
| YN[249] | Checking | AP check top margin offset (numeric value, not Y/N — stores pixel offset for top margin on AP checks) | unknown | SRC (Bkaph.src:349 `nTopMarg = val(bkys.yn[249])`) |

**Notes on duplicate/ambiguous labels in Setup tab:**
Several Setup tab entries show the same label description (e.g. "Post Inventory Adjustments?" for YN[2], YN[40], YN[213], YN[228]). This occurs because the Setup tab has many controls in close vertical proximity; Top-position pairing may capture a different setting's label. Treat Setup tab DFM entries with lower confidence than non-Setup tabs.

**Note on YN[249] numeric usage:** Not all YN[N] slots store Y/N flags. YN[249] stores a numeric
string (pixel offset). The column type in BKYSMSTR is STRING(2) for all YN slots, so numeric
values are stored as ASCII digit strings. Other slots may similarly store format codes (1–5) or
small integers rather than Y/N.

**Pass 382 corrections (2026-06-29):** Prior documentation incorrectly stated BKYSMSTR had 354
YN columns. Live ODBC query of DSN=DBA confirmed the actual count is 250 (BKYS_YN_1 through
BKYS_YN_250). The 89-row DFM-derived table is complete — no additional YN controls exist in
T7MDefaults.DFM or T7MDefNDC.DFM. The remaining ~161 slots (250 − 89) are set outside these
two forms.

### Live BKYSMSTR YN Values at i2 Systems (Pass 384, 2026-06-29)

Full BKYSMSTR row queried via DSN=DBA ODBC (single-row table). Key findings:

**DFM-mapped slots confirmed against live values:**

| YN[N] | Live Value | DFM Description | Validation |
|-------|-----------|-----------------|------------|
| YN[1] | 'F' | Post COGS Transactions? | ⚠ Not Y/N — stores format code |
| YN[9] | 'C' | (not in DFM table) | New: unknown code |
| YN[36] | 'D' | Multiply or Divide by processes (M/D) | ✓ Divide |
| YN[39] | '4' | SO Packing Slip format (1-4) | ✓ SOC4.RTM |
| YN[47] | '1' | Payroll check format (1=laser) | ✓ PRD1.RTM |
| YN[48] | '1' | AP check format (1=APHA1.RTM) | ✓ APHA1.RTM |
| YN[76] | '4' | SO Acknowledgment format (1-4) | ✓ SOB4.RTM |
| YN[77] | '4' | SO Quote format (1-4) | ✓ SOPB4.RTM |
| YN[78] | '2' | PO form format (1-2) | ✓ POE2.RTM plain paper |
| YN[200] | 'N' | Lead Time Scheduling (F/B/N) | ✓ None |
| YN[249] | '0' | AP check top margin offset | ✓ 0 px offset |

**New live values for unmapped slots (not in DFM table):**

Many previously-blank slots have non-null values at i2 Systems, confirming they are active
configuration settings not exposed in T7MDefaults.DFM. Representative sample:
`YN[6]`, `YN[7]`, `YN[8]`, `YN[10]`, `YN[11]`, `YN[12]`, `YN[13]`, `YN[14]` — all non-null
but descriptions unknown. Similarly, many slots in the YN[51]–YN[99] range have non-null values.

**Auto-number counters:** BKYS_WONUM=401 (next Work Order number at time of query).

### Complete YN[1]–[99] Live Snapshot (Pass 430, 2026-06-30)

Full live query via DSN=DBA ODBC. Total non-empty slots across all 250: **171** (up from the 82
reported in Pass 384, which was a partial scan). The definitive YN[1]–[99] live values are:

| YN[N] | Live Value | DFM Description (where known) |
|-------|-----------|-------------------------------|
| YN[1] | `'F'` | Post COGS Transactions? (⚠ not Y/N — format code) |
| YN[2] | *(blank)* | Post Inventory Adjustments? |
| YN[3] | `'N'` | Prevent Item Creation from ES-A |
| YN[4] | `'N'` | Fiscal Year Start Date |
| YN[5] | `'N'` | Post WO Transactions? |
| YN[6] | `'N'` | unknown |
| YN[7] | `'N'` | unknown |
| YN[8] | `'N'` | unknown |
| YN[9] | `'C'` | unknown (not in DFM table; 'C' = mode code) |
| YN[10] | `'N'` | unknown |
| YN[11] | `'N'` | unknown |
| YN[12] | `'N'` | unknown |
| YN[13] | `'N'` | unknown |
| YN[14] | `'N'` | unknown |
| YN[15] | `'N'` | PO-A Default for change dates (Y/N) |
| YN[16] | `'N'` | Enter Commissions at Sales Order Entry? |
| YN[17] | `'N'` | Enter Commissions at Line Item Entry? |
| YN[18] | `'Y'` | Enter Commissions for 2 Salespersons? |
| YN[19] | `'N'` | SOQA/INB: Disable Base Price passdown |
| YN[20] | `'N'` | Use Long Weight in Calculations? (SRC: DC barcode mode) |
| YN[21] | `'N'` | IN-A: Disable Rebuild Stock Status |
| YN[22] | `'Y'` | WOJ: Process WIP Variance |
| YN[23] | `'N'` | Require Sequence Entry - Type N |
| YN[24] | `'N'` | Require Sequence Entry - Type L |
| YN[25] | `'N'` | Require Sequence Entry - Type T |
| YN[26] | `'N'` | Require Sequence Entry - Type R,M,F,A |
| YN[27] | `'N'` | Post PO Transactions? |
| YN[28] | `'Y'` | Suppress Option Headers, Footers, Indents? |
| YN[29] | `'N'` | Copy Cust PO#s from WO#s as comment lines |
| YN[30] | `'N'` | AP-C Price change update PO Line price (Y/N/A) |
| YN[31] | `'I'` | (DFM: IN-A Disable Rebuild) ⚠ value 'I' ≠ Y/N — likely WOGKIT (kit issuance mode) |
| YN[32] | `'Y'` | Copy Cust PO#s from WO#s as comment lines (variant) |
| YN[33] | `'Y'` | Invoice PO Receipts through AP |
| YN[34] | *(blank)* | unknown |
| YN[35] | `'N'` | Open Period End Date |
| YN[36] | `'D'` | Multiply or Divide by # processes (M/D) — ✓ Divide |
| YN[37] | `'N'` | Use standard time? |
| YN[38] | `'N'` | Make sequence = template number? (SRC: ISTS.CFG.WOCALC) |
| YN[39] | `'4'` | SO Packing Slip format — ✓ SOC4.RTM |
| YN[40] | `'Y'` | Post Inventory Adjustments? (variant) |
| YN[41] | `'Y'` | Print Ending Lines (PO form?) |
| YN[42] | `'Y'` | Sales Order Ending Lines |
| YN[43] | `'N'` | Print Title on RFQ? |
| YN[44] | `'N'` | Sales Quote Print Format Number |
| YN[45] | `'N'` | Print Discount Column on Forms? |
| YN[46] | `'Y'` | Print Co. Name/Address on Forms? |
| YN[47] | `'1'` | Payroll check format — ✓ PRD1.RTM (laser) |
| YN[48] | `'1'` | AP check format — ✓ APHA1.RTM (stub/check/stub) |
| YN[49] | *(blank)* | unknown |
| YN[50] | `'A'` | (DFM: Post PO Transactions variant) ⚠ value 'A' ≠ Y/N |
| YN[51] | `'N'` | unknown |
| YN[52] | `'N'` | unknown |
| YN[53] | `'N'` | unknown |
| YN[54] | `'N'` | unknown |
| YN[55] | `'I'` | unknown (⚠ non-standard 'I' — possibly INGKIT kit mode for Inventory) |
| YN[56] | `'F'` | unknown (⚠ non-standard 'F') |
| YN[57] | `'N'` | Display machine prompt in Enter Labor? |
| YN[58] | `'W'` | unknown (⚠ non-standard 'W') |
| YN[59] | `'N'` | Allow entry to overlap settings in routings? (SRC: BKROA.SRC:647) |
| YN[60] | `'N'` | unknown |
| YN[61] | `'A'` | unknown (⚠ non-standard 'A') |
| YN[62] | `'Y'` | Decimalized Quantities on Forms? |
| YN[63] | `'Y'` | Decimalized Quantities on Forms? (variant) |
| YN[64] | `'Y'` | Print Title on: Acknowledgments |
| YN[65] | `'N'` | Divide Overhead by # of Jobs Worked |
| YN[66] | `'N'` | Display long time prompt? (SRC: ISTS.CFG.LNGWT, BKROA.SRC:629) |
| YN[67] | `'Y'` | Include in MRP Generation? |
| YN[68] | `'N'` | unknown |
| YN[69] | `'N'` | unknown |
| YN[70] | `'N'` | unknown |
| YN[71] | *(blank)* | unknown |
| YN[72] | *(blank)* | unknown |
| YN[73] | `'Y'` | Prevent Item Creation from PI-C |
| YN[74] | `'Y'` | Print Discount Column on Forms? |
| YN[75] | `'Y'` | unknown |
| YN[76] | `'4'` | SO Acknowledgment format — ✓ SOB4.RTM |
| YN[77] | `'4'` | SO Quote format — ✓ SOPB4.RTM |
| YN[78] | `'2'` | PO form format — ✓ POE2.RTM (plain paper) |
| YN[79] | `'Y'` | Prompt for save in Enter Accounts? |
| YN[80] | `'Y'` | Print Ending Lines (PO?) |
| YN[81] | `'N'` | unknown |
| YN[82] | `'Y'` | Packing Slips (format number?) |
| YN[83] | `'Y'` | SOQA/INB: Disable Base Price passdown (variant) |
| YN[84] | `'N'` | WOJ: Process WIP Variance (variant) |
| YN[85] | `'Y'` | Divide Overhead by # of Jobs Worked (variant) |
| YN[86] | `'Y'` | Prevent Item Creation from ES-A (variant) |
| YN[87] | `'Y'` | AR: Print Co. Name/Addr on Statement |
| YN[88] | `'N'` | unknown |
| YN[89] | `'P'` | unknown (⚠ non-standard 'P') |
| YN[90]–YN[101] | *(all blank)* | unknown — 12 consecutive empty slots |

**Non-standard mode codes in YN[1]-[99] (not Y/N/blank):**
`'F'`(YN[1]), `'C'`(YN[9]), `'I'`(YN[31],YN[55]), `'A'`(YN[50],YN[61]),
`'4'`(YN[39],YN[76],YN[77]), `'D'`(YN[36]), `'1'`(YN[47],YN[48]),
`'2'`(YN[78]), `'F'`(YN[56]), `'W'`(YN[58]), `'P'`(YN[89]).

**T7YSYN linear mapping — DISPROVEN (Pass 430, 2026-06-30):**
The T7YSYN symbol table lists 495 ISTS.CFG keys in editing-order. An earlier hypothesis mapped
YN slot N to the Nth key in T7YSYN's pool (the "linear mapping"). This is **wrong**. Counter-evidence:
- `BKROA.SRC:392,1582` confirms YN[38] = ISTS.CFG.WOCALC (linear mapping gives SCRCMP for YN[38])
- `BKROA.SRC:629` confirms YN[66] = ISTS.CFG.LNGWT (linear mapping gives PAYRQE for YN[66])

The T7YSYN symbol table order reflects the editor's UI layout, not the YN array index order.
The scratchpad file `yn_table.txt` (previous session) contains the full 250-slot linear mapping
table — treat its "ISTS.CFG Key" column as **T7YSYN pool order only, not confirmed slot assignments**.

The DFM+SRC analysis remains the only confirmed method for mapping slots to key names.

### YN[102]–YN[149]: Module Enable/Disable Block (Pass 384, full live data Pass 396)

Live values — full BKYSMSTR query (Pass 396 2026-06-30):

| YN[N] | Live value | GROUPS-order hypothesis (see below) |
|-------|------------|--------------------------------------|
| YN[102] | 'Y' | WO (Work Orders) |
| YN[103] | 'Y' | JC (Job Costing) |
| YN[104] | 'Y' | PO (Purchase Orders) |
| YN[105] | 'A' | MR (MRP) — 'A' = Advanced tier? |
| YN[106] | 'Q' | SH (Scheduling) — 'Q' = unknown tier |
| YN[107] | 'A' | DC (Data Collection) — 'A' = Advanced tier? |
| YN[108] | 'Y' | ES (Estimates) |
| YN[109] | 'Y' | QC (Quality Control) |
| YN[110] | 'Y' | IN (Inventory) |
| YN[111] | 'Y' | RO (Routings) |
| YN[112] | 'Y' | BM (Bill of Materials) |
| YN[113] | 'Y' | LC (Lot Control) |
| YN[114] | 'Y' | SC (Serial Control) |
| YN[115] | **'Z'** | FO (Features & Options) — **BKMENUSU BUTTONS "FO",30 = FO IS in the menu, Z ≠ unlicensed** |
| YN[116] | 'Y' | PI (Physical Inventory) |
| YN[117] | 'Y' | WC (Warehouse Control) |
| YN[118] | **'Z'** | SO (Sales Orders) — **GROUPS-order confirmed; 'Z' for SO is NOT "unlicensed" (SO is fully active with 3,686+ records)** |
| YN[119] | 'Y' | SR (Service and Repair) |
| YN[120] | 'Y' | RM (RMA) |
| YN[121] | 'Y' | SA (Sales Analysis) |
| YN[122] | ' ' | CS (Commissions) — **CS has active menu entries (CSA–CSM); ' ' ≠ unlicensed** |
| YN[123] | ' ' | CM (Contact Master) — **CM has active menu entries (CMA–CMM); ' ' ≠ unlicensed** |
| YN[124] | 'Y' | AR (Accounts Receivable) |
| YN[125] | 'Y' | CR (Contract Review) |
| YN[126] | 'Y' | QU (Queries & Reports) |
| YN[127] | 'Y' | SU (Query & Report Setup) |
| YN[128] | 'Y' | HH (Hand Held Programs) |
| YN[129] | '1' | UT (Utilities) — '1' = unknown sub-mode |
| YN[130] | 'Y' | SM (System Maintenance) |
| YN[131] | ' ' | SD (System Defaults) |
| YN[132] | 'Y' | IM (International Module) |
| YN[133] | 'Y' | PS (Password Security) |
| YN[134] | 'Y' | DE (Data Exchange) |
| YN[135] | 'Y' | TAS (System Configuration) |
| YN[136] | 'Y' | GL (General Ledger) |
| YN[137] | 'Y' | AP (Accounts Payable) |
| YN[138] | 'Y' | FA (Fixed Assets) |
| YN[139] | 'Y' | AM (Accounting Maintenance) |
| YN[140] | 'Y' | AD (Accounting Defaults) |
| YN[141] | 'Y' | PL (Pay Link) |
| YN[142] | 'Y' | PR (Payroll) |
| YN[143] | 'Y' | US (User Settings) |
| YN[144] | 'Y' | unknown (no GROUPS entry) |
| YN[145] | 'Y' | unknown |
| YN[146] | 'Y' | unknown |
| YN[147] | ' ' | unknown |
| YN[148] | 'Y' | unknown |
| YN[149] | 'Y' | unknown |

**Value semantics — CORRECTED (Pass 413, 2026-06-30):**

Prior "Z=disabled, space=unlicensed" interpretation was WRONG. BKMENUSU.TXT confirmation:
- FO='Z' but `"BUTTONS","Features and Options","FO", 30` — FO HAS 30 active operations
- SO='Z' but SO has 3,686+ live invoice records — fully in use
- CS=' ' but CSA–CSM all have active program entries in BKMENUSU.TXT
- CM=' ' but CMA–CMM all have active program entries in BKMENUSU.TXT

**These values do NOT indicate module enable/disable state. All 42 GROUPS modules are accessible.**

Actual semantics (unknown — requires T7YSYN.RWN decryption):
- `'Y'` = some standard mode (38/42 modules)
- `'Z'` = some alternate mode (FO and SO)
- `'A'` = some advanced mode (MR and DC — consistent with BKSYCFG.ADVWO/ADVDC pattern)
- `'Q'` = some special mode (SH/Scheduling)
- `'1'` = some numeric flag (UT/Utilities)
- `' '` = some mode (CS/CM/SD) — NOT "unlicensed" (all have active menu entries)

**GROUPS-order hypothesis — CONFIRMED (Pass 413, 2026-06-30):** BKMENUSU.TXT has exactly 42
GROUPS module entries in reading order (Mfg→Items→Sales→Queries→HandHeld→SystemMgr→
Accounting→PayLink→Payroll→Settings). YN[102]–YN[143] = 42 slots. EXACT COUNT MATCH.
Mapping: YN[102+N−1] = GROUPS entry N (1-indexed). Confirmed because:
- 42 GROUPS entries × 1:1 = YN[102]–YN[143] exactly fills the documented 48-slot range minus 6 extra
- YN[144]–YN[149] = 6 slots with no GROUPS entry
- Prior "contradiction" at YN[118]=SO was caused by wrong 'Z' interpretation, not wrong mapping
**The 1:1 GROUPS-order mapping is now confirmed as the best structural hypothesis. C:72/100.**
The exact value semantics per slot remain blocked (requires T7YSYN.RWN decryption).

**Count:** 48 slots (YN[102]–YN[149]). 42 GROUPS modules + 6 unaccounted slots (YN[144-149]).
Candidates for the 6 extra: NE, QT, RF, LI, ML, and/or reserved slots.

**Mapping definitively blocked:** T7YSYN.RWN (encrypted) maps module codes→YN indices.

---

### YN[150]–YN[250]: Complete Live Snapshot (Pass 415, 2026-06-30)

Full live query of BKYSMSTR via DSN=DBA ODBC. Key structural finding: **YN[150]–YN[198] are ALL EMPTY at i2 Systems** — 49 consecutive blank slots. This gap suggests this range is either unused in the current EVO build, reserved for a module not licensed at i2, or populated only in certain configurations.

**YN[199]–YN[250] live values:**

| YN[N] | Live Value | DFM Description (from existing DFM-mapped table) | Source |
|-------|-----------|---------------------------------------------------|--------|
| YN[199] | `'A'` | unknown | live only |
| YN[200] | `'N'` | Use Lead Time Scheduling [F/B/N] | DFM |
| YN[201] | `'1'` | unknown | live only |
| YN[202] | `'E'` | PO-C: update Std. Cost if Cost is $0.00 | DFM |
| YN[203] | `'Y'` | unknown | live only |
| YN[204] | `'Y'` | unknown | live only |
| YN[205] | `'Y'` | unknown | live only |
| YN[206] | `'Y'` | unknown | live only |
| YN[207] | `'Z'` | unknown | live only |
| YN[208] | `'Y'` | unknown | live only |
| YN[209] | `'Y'` | Use Acctg Open Period Start Date in GL-B | DFM (approx) |
| YN[210] | `'Y'` | unknown | live only |
| YN[211] | `'Y'` | unknown | live only |
| YN[212] | `'Y'` | Use Acctg Open Period Start Date in AP-B | DFM (approx) |
| YN[213] | `'Y'` | Use Acctg Open Period Start Date in AR-C | DFM (approx) |
| YN[214] | `'Y'` | (label ambiguous) | DFM (approx) |
| YN[215] | `'Y'` | (label ambiguous) | DFM (approx) |
| YN[216] | `'Y'` | unknown | live only |
| YN[217] | `'Y'` | unknown | live only |
| YN[218] | `'N'` | DC-A/DC-C: Round Shift Start/Stop by X minutes | DFM |
| YN[219] | *(blank)* | unknown | — |
| YN[220] | *(blank)* | Invoices (format number?) | DFM |
| YN[221] | *(blank)* | unknown | — |
| YN[222] | `'Y'` | GL Department | DFM |
| YN[223] | `'R'` | Location | DFM |
| YN[224] | `'4'` | unknown | live only |
| YN[225] | `'2'` | SOQA/INB: Disable Base Price passdown (variant) | DFM |
| YN[226] | `'0'` | unknown | live only |
| YN[227] | *(blank)* | unknown | — |
| YN[228] | `'Y'` | DC screen variant: Y=mount BKDCAF (simplified) | SRC (BKDCA.SRC:194) |
| YN[229] | `'N'` | DC multi-job/auto-close mode | SRC (BKDCA.SRC:228) |
| YN[230] | `'1'` | AR Invoice Age based on (1) age or (2) days past due | DFM |
| YN[231] | `'Y'` | Open Period End Date | DFM |
| YN[232] | `'4'` | unknown | live only |
| YN[233] | *(blank)* | unknown | — |
| YN[234] | *(blank)* | unknown | — |
| YN[235] | *(blank)* | unknown | — |
| YN[236] | *(blank)* | unknown | — |
| YN[237] | *(blank)* | PO & DC update actual start/finish dates of sequences? | DFM |
| YN[238] | `'Y'` | Disable Recalc Est Cost in WO-A | DFM |
| YN[239] | `'R'` | Allow WOs for Make From Items | DFM |
| YN[240] | `'Y'` | Estimates: Print Title on Quote? | DFM |
| YN[241] | `'Y'` | Printing: Print Title on RFQ? | DFM |
| YN[242] | `'Y'` | Printing: Print Co. Name/Address on Forms? | DFM |
| YN[243] | `'Y'` | Sales Quotes (format number?) | DFM |
| YN[244] | `'Y'` | Invoices (format number?) | DFM |
| YN[245] | `'Y'` | Packing Slips (format number?) | DFM |
| YN[246] | `'Y'` | Print Title on: Acknowledgments | DFM |
| YN[247] | `'Y'` | AR: Print Title on Statement | DFM |
| YN[248] | `'N'` | MRP: Round MRP quantities to next whole number? | DFM |
| YN[249] | `'0'` | AP check top margin offset (pixels) | SRC (Bkapha.src:269) |
| YN[250] | `'0'` | unknown | live only |

**Observations:**
- YN[199-218] is a 20-slot block of consecutive non-empty values. The value pattern ('A','N','1','E' + 'Y'×4 + 'Z' + 'Y'×10 + 'N') is superficially similar to the module-enable block at YN[102-143], but the DFM-mapped entries in this range (YN[200], YN[202], YN[209], YN[212-215], YN[218]) are individual named config settings, not module enables. The 'Z' at YN[207] and 'A' at YN[199] could be coincidental.
- YN[223]='R' and YN[239]='R' — 'R' is a non-standard value; likely a location/routing/report code.
- YN[224]='4', YN[225]='2', YN[226]='0', YN[230]='1', YN[232]='4' — numeric strings, format codes or counts.
- YN[243-247] all='Y' with DFM descriptions matching the printing format flags — but DFM said these store format numbers (1-4), so 'Y' here is anomalous unless 'Y'=default/inherit.
- YN[250]='0' — **new finding** (previously unknown/blank in prior passes).

---

## BKYS.GLNUM[N] / BKYS.GLDPT[N] — GL Account Slot Mapping

Pass 380 (2026-06-29): 19 of 40 GL account slots confirmed from T7MDefaults.DFM.
Each slot is a pair — GLNUM[N] = GL account number, GLDPT[N] = GL department code.
Source: DFM Top-position pairing (medium confidence; most Manufacturing/Acct.Sales tab entries are reliable).

| Slot | Module | GL Account Purpose |
|------|--------|--------------------|
| GLNUM[2] / GLDPT[2] | Accounting / Sales | AR Customer Deposits |
| GLNUM[3] / GLDPT[3] | Manufacturing | WO Absorbed Labor |
| GLNUM[4] / GLDPT[4] | Accounting / Sales | SO Retention |
| GLNUM[5] | Setup | **Company code** — live value 'I2S' (Pass 384); NOT a GL account number. Slot repurposed to store a short company identifier string. DFM label pairing was incorrect. |
| GLNUM[6] / GLDPT[6] | Manufacturing | WO Absorbed Fixed Overhead |
| GLNUM[7] / GLDPT[7] | Manufacturing | WO Absorbed Var Overhead |
| GLNUM[9] / GLDPT[9] | Manufacturing | WO Extra Costs |
| GLNUM[10] / GLDPT[10] | Manufacturing | WO Miscellaneous Costs |
| GLNUM[14] / GLDPT[14] | Manufacturing | IN Absorbed Freight In |
| GLNUM[15] | Customers | Default Customer Class Code (not a GL account — possibly repurposed slot) |
| GLNUM[16] | Customers | Default Discount Code (not a GL account — possibly repurposed slot) |
| GLNUM[17] / GLDPT[17] | Accounting / Sales | CS Agents Commission Payable |
| GLNUM[18] / GLDPT[18] | Accounting / Sales | CS Agents Commission Expense |
| GLNUM[20] / GLDPT[20] | Manufacturing | WO WIP Variance |
| GLNUM[21] / GLDPT[21] | Manufacturing | PO Purchase Price Variance |
| GLNUM[33] / GLDPT[33] | Accounting / Sales | AP Deposits |
| GLNUM[34] / GLDPT[34] | Manufacturing | WO WIP Inventory |
| GLNUM[35] / GLDPT[35] | Manufacturing | IN Cost of Goods Sold |
| GLNUM[36] / GLDPT[36] | Manufacturing | IN Inventory (Asset) |
| GLNUM[37] / GLDPT[37] | Accounting / Sales | SO Non-Taxable Sales |
| GLNUM[38] / GLDPT[38] | Accounting / Sales | SO Taxable Sales |

Slots 1, 8, 11–13, 19, 22–32, 39–40 not yet confirmed (labels either missing or ambiguous).

**Live GLNUM values confirmed (Pass 384, DSN=DBA):**
- GLNUM[2]='2115' (AR Customer Deposits — matches DFM description)
- GLNUM[3]='5001' (WO Absorbed Labor — matches DFM description)
- GLNUM[5]='I2S' (company code — NOT a GL account; see correction above)
- GLNUM[8]='51200' (purpose unknown — not in DFM table; slot 8 now partially confirmed as active)

## BKYS.VNUM[N], BKYS.NUM[N], BKYS.DESC[N], BKYS.DATE[N] — Non-YN Non-GL Scalar Slots

Pass 385 (2026-06-29): live DSN=DBA query + DFM binding extraction for all 20 non-YN non-GL
scalar slots in BKYSMSTR. Total BKYSMSTR column breakdown (355 fields confirmed):
250 YN + 40 GLNUM + 40 GLDPT + 5 NUM + 5 VNUM + 5 DESC + 5 DATE + 5 auto-numbers = 355.

### Auto-Number Counters

These 5 columns store the next available auto-number for each subsystem:

| Column | Live Value (i2S) | Purpose |
|--------|-----------------|---------|
| BKYS_WONUM | 401 | Next Work Order number |
| BKYS_QCNUM | 1 | Next QC Receipt number |
| BKYS_REQNUM | 0 | Next Requisition number (RE module) |
| BKYS_INVNUM | 1 | Next Invoice number (reset or not yet used) |
| BKYS_RBNUM | 20 | Next Report Batch number (RB — exact purpose unknown) |

### VNUM[N] Slots (5 slots, STRING type)

| Slot | DFM Description (T7MDefaults) | Live Value (i2S) | Confidence |
|------|-------------------------------|------------------|------------|
| VNUM[1] | (not bound in any DFM) | '1111' | DFM: unknown; live: likely a system code |
| VNUM[2] | "Recycle Fee Item Num" (Customers tab) | '0' | DFM (medium) — prior note "Salesperson #1" was a different label pairing error |
| VNUM[3] | "ROA: Recalc Parts/Hr when changing # Persons (Y/N/A)" (Routing tab) | '10' | DFM (medium); live '10' consistent with Routing sequence increment |
| VNUM[4] | (not bound in any DFM) | '0' | unknown |
| VNUM[5] | (not bound in any DFM) | '7' | unknown; value 7 may be a count or mode code |

### NUM[N] Slots (5 slots, NUMERIC type)

| Slot | DFM Description | Live Value (i2S) | Confidence |
|------|-----------------|------------------|------------|
| NUM[1] | "WO-K-M: Require a Reason code" (Setup tab) | 2 | DFM (low — Setup tab density); 2 could be a multi-option code |
| NUM[2] | (not bound in any DFM) | 7952 | unknown; 7952 is suspiciously specific — possibly a check number counter or print count |
| NUM[3] | (not bound in any DFM) | 1 | unknown |
| NUM[4] | (not bound in any DFM) | 1 | unknown |
| NUM[5] | (not bound in any DFM) | 50 | unknown; 50 could be max-users type cap (license allows 48) |

### DESC[N] Slots (5 slots, STRING type — 25 chars)

| Slot | DFM Description | Live Value (i2S) | Confidence |
|------|-----------------|------------------|------------|
| DESC[1] | "SOE: Enter BOL Info for EDI?" (Setup tab) | '' (blank) | DFM (low — label mismatch likely) |
| DESC[2] | (not bound in any DFM) | '' (blank) | unknown |
| DESC[3] | "Force Order Descriptions in SO/PO" (T7MDefNDC Setup) | 'PLANT' | DFM description may be wrong; live 'PLANT' suggests default dept/location code |
| DESC[4] | (not bound in any DFM) | '' (blank) | unknown |
| DESC[5] | (not bound in any DFM) | '' (blank) | unknown |

**Note on DESC[3]='PLANT':** The value 'PLANT' strongly suggests this stores a default
department code, location name, or facility identifier used as a fallback when no specific
dept/location is assigned. The DFM-derived label is likely a label-pairing error.

### DATE[N] Slots (5 slots, DATE type)

| Slot | DFM Description | Live Value (i2S) | Confidence |
|------|-----------------|------------------|------------|
| DATE[1] | (not bound in T7MDefaults DFM) | 2024-01-01 | Likely accounting open period start date (AR or fiscal year) |
| DATE[2] | (not bound in any DFM) | 2024-01-01 | Same as DATE[1] — possibly AP open period start |
| DATE[3] | (not bound in any DFM) | (null) | Not set at i2 Systems |
| DATE[4] | (not bound in any DFM) | 2020-12-31 | Prior period end date (last closed fiscal year or archived period) |
| DATE[5] | (not bound in any DFM) | 2020-12-31 | Same as DATE[4] — prior period variant |

**Observation:** DATE[1]=DATE[2]=2024-01-01 mirrors the current fiscal year start at i2 Systems.
DATE[4]=DATE[5]=2020-12-31 likely marks the last fully-archived/closed period.
The DFM references to YN[35]/YN[231]="Open Period End Date" and YN[4]="Fiscal Year Start Date"
are in the YN (string) block; DATE[N] may be the same concept stored as actual date objects.

## BKEST.CFG.* — Estimates Configuration Keys

Pass 380 (2026-06-29): 10 BKEST.CFG keys confirmed from T7MDefaults.DFM (Estimates tab).
These are stored in BKESTCFG (1-row config table for the Estimating module).

| Key | Description | Allowed Values |
|-----|-------------|----------------|
| BKEST.CFG.CLASS | Default Class Code for new estimates | — |
| BKEST.CFG.DAYS | Number of days to expiration date for quotes | — |
| BKEST.CFG.FORM | Customer Quote Print Format (1=ESD1.RTM universal, 2=ESD2.RTM letterhead) | 1,2 |
| BKEST.CFG.LAB% | Default Labor Margin % | — |
| BKEST.CFG.MAT% | Default Material Margin % | — |
| BKEST.CFG.OH% | Default Overhead Margin % | — |
| BKEST.CFG.OP% | Default Outside Processing (Outs Proc) Margin % | — |
| BKEST.CFG.STAT | Default Status Code for new estimates | A,C,I,X |
| BKEST.CFG.TOT% | Default Total Margin % | — |
| BKEST.CFG.ENDLN | (Printing context — may be shared with other modules) | — |

## DFM-Sourced ISTS.CFG Key Reference

Pass 380 (2026-06-29): All 504 ISTS.CFG key descriptions have been extracted from T7MDefaults.DFM
using Top-position label pairing. The complete mapping is in `samples/T7MDefaults_cfg_keys.csv`.

**Selected confirmed key descriptions** (supersede the inferred meanings above):

| Key | Confirmed Description | Source |
|-----|-----------------------|--------|
| ISTS.CFG.ACCESS | Allow CM-A to access AR-A [Legacy Settings] | DFM |
| ISTS.CFG.ACDCSQ | INB: Use TOOLS lookup and validation setup in RO-E | DFM |
| ISTS.CFG.ACKBO | Include BO on EDI Acknowledgments | DFM |
| ISTS.CFG.APBDTE | AP-B: Use Invoice Date as Post Date in AP-B | DFM |
| ISTS.CFG.APBSDT | AP-B: Use Accounting Open Period Start Date | DFM |
| ISTS.CFG.APBVND | AP-B: Prevent Creating New Vendors | DFM |
| ISTS.CFG.APCLST | AP-C: Update Last Cost when Changing Price | DFM |
| ISTS.CFG.APLINK | AP-C/AP-B: Enable Vendor Invoice Links [YNA] | DFM |
| ISTS.CFG.APLANG | AP-H: Print Check English/Spanish (E/S) | DFM |
| ISTS.CFG.APHXPT | AP-H: Export Program Name | DFM |
| ISTS.CFG.APPVND | AP-B/AP-F/PO-A/PO-C: Use Approved Vendors [YNP] | DFM |
| ISTS.CFG.APSORT | AP-B: Sort vendors by (1=Vendor/2=Name/3=State/4=Zip/5=Contact) | DFM |
| ISTS.CFG.ARADTE | Allow Edit of Customer Start Date in AR-A | DFM |
| ISTS.CFG.ARCBOM | BMA: Auto Archive BOM [Y/N] | DFM |
| ISTS.CFG.XCOMA | Enable Extended Commission System [Sales Commissions] | DFM |
| ISTS.CFG.XCOMH | Enable Overage within Extended Commissions [Sales Commissions] | DFM |
| ISTS.CFG.XCOMM | Enable Extended Commission System [Sales Commissions] | DFM |
| ISTS.CFG.XDBA | Permanently Disable DBA Classic | DFM |
| ISTS.CFG.XREBSS | DCA/B/C Allow access to view and modify the WC [Y/N] | DFM |
| ISTS.CFG.ZPRCOM | Save zero dollar value Commissions? [Y/N] | DFM |

For the full table of all 504 keys with DFM-sourced descriptions, see `samples/T7MDefaults_cfg_keys.csv`.

**Note on label quality:** Non-Setup-tab entries tend to have accurate pairings. Setup tab entries
(which contain hundreds of flags densely stacked) have lower pairing accuracy — treat them as
approximate. The CSV includes tab context to help identify likely-accurate vs ambiguous entries.

---

## Keys in Old Grep-Based List but NOT in T7YSYN

These keys appeared in rwn_strings grep results but are absent from T7YSYN's editor fields.
They may be dynamically constructed key names, computed values, or removed/deprecated flags:

```
APDUP, APOPEN, ARNEG
SOBACK, SOCRED, SOHOLD, SOINVP, SOPACK, SOSHIP, SOPRICE, SOTAX
POAUTO, POCONS, POMIN, POPRICE, PORECV, PORQST, POVEND, POXREF
WOAROP, WOSTEP, WOROUT
INCSTD, DCBSER, ROAPPH, FUPSWD
EDIBOL, EDIOUT
CCFEE
```

*Do not treat these as confirmed BKYSMSTR fields. They may be string literals that happen to
match the ISTS.CFG.* pattern rather than true configuration keys.*

---

## BKSYMSTR Live GL Account Scalars (Pass 416, 2026-06-30)

Live DSN=DBA query: `SELECT TOP 1 * FROM BKSYMSTR`. 286 total fields; 29 are meaningfully
non-zero, non-blank. All other fields (including all auto-number fields) are 0 or null.

### Auto-Number Fields — All Zero at i2 Systems

BKSYMSTR has 17 auto-number/record-counter fields; **all are 0.0** at i2 Systems:
- `BKSY_ARINV_NUM`, `BKSY_APINV_NUM`, `BKSY_APPO_NUM`, `BKSY_GJ_NUM` — invoice/PO/journal auto-num
- `BKSY_CHK_NUM_1` through `BKSY_CHK_NUM_9` — 9 per-bank check number counters (one per bank account slot)
- `BKSY_ARSO_NUM`, `BKSY_AP_RECNUM`, `BKSY_GJ_RECNUM`, `BKSY_AR_RECNUM` — record counters

**Interpretation:** i2 Systems uses manual document numbering for all transaction types (AP invoices,
PO numbers, journal entries, check numbers). Auto-numbering from BKSYMSTR is unused.
Note: `BKSY_CHK_NUM` (singular) does not exist — the field is `BKSY_CHK_NUM_1..9`.

### GL Account Mappings (live values, i2 Systems)

| Field | Live Value | Purpose |
|-------|-----------|---------|
| `BKSY_GL_CLRING` | '9999' | GL clearing account (9999 = not configured) |
| `BKSY_GL_RETEARN` | '9999' | GL retained earnings account (9999 = not configured) |
| `BKSY_GL_RELYR` | '3200' | GL prior-year retained earnings release account |
| `BKSY_GL_ARINTR` | '9999' | AR interest income GL account (not configured) |
| `BKSY_AR_GLACT` | '1200' | AR control account (Accounts Receivable) |
| `BKSY_AR_DISCGL` | '4004' | AR sales discount GL account |
| `BKSY_AR_DISCDPT` | '1' | AR discount department code |
| `BKSY_AR_FREIGHT` | '8517' | AR freight revenue GL account |
| `BKSY_AR_FRGTDPT` | '4' | AR freight department code |
| `BKSY_AP_GLACT` | '2110' | AP control account (Accounts Payable) |
| `BKSY_AP_DISCGL` | '5100' | AP purchase discount GL account |
| `BKSY_AP_DISCDPT` | '1' | AP discount department code |
| `BKSY_TAX_GLACT` | '9999' | Sales tax GL account (not configured) |
| `BKSY_PO_TAXGL` | '8805' | PO/purchasing tax GL account |
| `BKSY_PO_TAXDPT` | '0000' | PO tax department code |
| `BKSY_PO_FREIGHT` | '5102' | PO freight expense GL account |
| `BKSY_PO_FRGTDPT` | '0250' | PO freight department code |
| `BKSY_PO_RNI` | '2137' | Received-Not-Invoiced accrual account (PO receipt → awaiting AP invoice) |

### Financial Settings (live values)

| Field | Live Value | Purpose |
|-------|-----------|---------|
| `BKSY_FISCAL_YR` | 2026-01-01 | Current fiscal year start date |
| `BKSY_AR_INT_RTE` | 1.5 | AR late-payment interest rate (1.5% per period) |
| `BKSY_AR_INT_DAY` | 1 | AR interest calculation day of month |

### Aging Buckets (both AR and AP)

| Field | Value | Meaning |
|-------|-------|---------|
| `BKSY_AR_AGING_2` | 30 | AR aging bucket 2 cutoff (days) |
| `BKSY_AR_AGING_3` | 60 | AR aging bucket 3 cutoff |
| `BKSY_AR_AGING_4` | 90 | AR aging bucket 4 cutoff |
| `BKSY_AR_AGING_5` | 120 | AR aging bucket 5 cutoff |
| `BKSY_AP_AGING_2` | 30 | AP aging bucket 2 cutoff (days) |
| `BKSY_AP_AGING_3` | 60 | AP aging bucket 3 cutoff |
| `BKSY_AP_AGING_4` | 90 | AP aging bucket 4 cutoff |
| `BKSY_AP_AGING_5` | 120 | AP aging bucket 5 cutoff |

Standard 30/60/90/120 day aging for both AR and AP. No custom aging buckets at i2 Systems.

**Note on 9999 values:** GL account '9999' is used as a placeholder for accounts not configured
at i2 Systems (clearing, retained earnings, tax, AR interest). The actual chart-of-accounts
uses BKGLCOA as the master; 9999 may be the system-reserved placeholder number.

---

*Last updated: 2026-06-30 — Pass 416*
*Sources: T7YSYN symbol table + T7MDefaults.DFM Top-position pairing (89 YN entries + 504 ISTS.CFG entries + GL account slots) + DSN=DBA live BKSYMSTR query (Pass 416)*
*Confidence: 72/100 — 495 keys confirmed as BKYSMSTR editor fields; 504 keys have DFM-sourced descriptions (full CSV: samples/T7MDefaults_cfg_keys.csv); 19/40 GL account slots confirmed; 10 BKEST.CFG keys confirmed; BKSYMSTR GL account scalars fully live-confirmed (Pass 416); Setup tab label pairings remain less reliable.*
