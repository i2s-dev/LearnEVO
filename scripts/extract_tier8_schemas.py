"""Extract specific table schemas from schema.md and write tier8-tables.md."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

SCHEMA_PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\ddf\schema.md'
OUT_PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\docs\04-data-dictionary\tier8-tables.md'

# Tables to extract — (table_name, description, module, pk_note)
TARGETS = [
    ('BKAPPO', 'AP Purchase Order Header', 'PO/AP', 'BKAP_PO_NUM (inferred)'),
    ('BKAPPOL', 'AP Purchase Order Lines', 'PO/AP', 'BKAP_PO_NUM + line counter (inferred)'),
    ('BKGLTRAN', 'GL Journal Transaction Lines', 'GL', 'BKGL_TRAN_* key fields (inferred)'),
    ('BKGLCOA', 'GL Chart of Accounts', 'GL', 'BKGL_COA_ACCT + BKGL_COA_DEPT'),
    ('BKDCSHFT', 'Data Collection Shift Definitions', 'DC', 'Shift number (inferred)'),
    ('BKDCTLAB', 'Data Collection Temporary Labor', 'DC', 'Composite (inferred)'),
    ('BKDCPLAB', 'Data Collection Pending Labor', 'DC', 'Composite (inferred)'),
    ('BKARCUST', 'AR Customer Master', 'AR', 'BKAR_CUST_CODE'),
    ('BKARINV', 'AR Invoice / Sales Order Header', 'AR/SO', 'BKAR_INV_INVNUM'),
    ('BKARINVL', 'AR Invoice Lines', 'AR/SO', 'BKAR_INVL_INVNUM + BKAR_INVL_CNTR'),
    ('BKAPVEND', 'AP Vendor Master', 'AP', 'BKAP_VEND_CODE'),
    ('BKAPINVL', 'AP Invoice / Voucher Lines', 'AP', 'BKAP_INVL_* key (inferred)'),
    ('WORKORD', 'Work Order Header', 'WO', 'WORK_WOPRE + WORK_WOSUF'),
    ('BKICMSTR', 'Inventory Item Master', 'IN', 'BKIC_PROD_CODE'),
    ('BKGLPER', 'GL Period Control', 'GL', 'BKGL_PER_* (inferred)'),
    ('BKBMMSTR', 'Bill of Materials', 'BM', 'BKBM_MSTR_PARENT + BKBM_MSTR_COMP'),
    ('BKARCCHK', 'AR Cash Receipts Check', 'AR', 'Composite (inferred)'),
    ('BKARTNOT', 'AR Transaction Notes', 'AR', 'BKART_TRXN + BKART_CNTR'),
    ('ARTTEMP', 'AR Temporary (session scratch)', 'AR', 'Composite (inferred)'),
    ('BKACTRPT', 'AC Activity Report Templates', 'AC', 'BKAC_TYPE + BKAC_NAME'),
]

with open(SCHEMA_PATH, encoding='utf-8', errors='replace') as f:
    schema_text = f.read()

# Parse schema.md into per-table sections
table_sections = {}
current_table = None
current_lines = []
for line in schema_text.split('\n'):
    m = re.match(r'^## (\w+)\s+\((\S+)\)', line)
    if m:
        if current_table:
            table_sections[current_table] = '\n'.join(current_lines)
        current_table = m.group(1)
        current_lines = [line]
    elif current_table:
        current_lines.append(line)
if current_table:
    table_sections[current_table] = '\n'.join(current_lines)

def extract_fields(section_text):
    """Return list of (num, name, type, offset, size) tuples."""
    rows = []
    for line in section_text.split('\n'):
        m = re.match(r'\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*(\w+)\s*\|\s*(\d+)\s*\|\s*(\d+)', line)
        if m:
            rows.append((int(m.group(1)), m.group(2), m.group(3), int(m.group(4)), int(m.group(5))))
    return rows

# Build the tier8 doc
lines = [
    '# EvoERP Data Dictionary — Tier 8 Tables (DDF-exact schemas)',
    '',
    'Status: partial — extracted directly from Pervasive DDF via schema.md (2026-06-18).',
    'Field names are exact; meanings are inferred from name patterns unless confirmed by DFM or SRC.',
    '',
    '---',
    '',
]

written = 0
for tname, desc, module, pk_note in TARGETS:
    if tname not in table_sections:
        lines.append(f'<!-- {tname} not found in schema.md -->')
        continue
    fields = extract_fields(table_sections[tname])
    if not fields:
        lines.append(f'<!-- {tname} found in schema.md but no field rows extracted -->')
        continue
    written += 1
    lines += [
        f'## {tname} — {desc}',
        '',
        f'**Module:** {module} | **Fields:** {len(fields)} | **File:** {tname}.B',
        f'**Primary key (inferred):** {pk_note}',
        '',
        '| # | Field | Type | Size | Inferred Meaning |',
        '|---|-------|------|------|-----------------|',
    ]
    for num, name, ftype, offset, size in fields:
        # Infer meaning from field name
        meaning = name
        # strip common prefixes like BKAP_PO_, BKGL_COA_, BKIC_PROD_
        clean = re.sub(r'^(BKAP?[A-Z_]+_|BKGL[A-Z_]+_|BKIC[A-Z_]+_|BKAR[A-Z_]+_|BKBM[A-Z_]+_|BKDC[A-Z_]+_|WORK_|BKAC_)', '', name, count=1)
        meaning = clean
        lines.append(f'| {num} | `{name}` | {ftype} | {size} | {meaning} |')
    lines.append('')
    lines.append(f'**Confidence: 65/100** — Field names exact from DDF; meanings inferred from names.')
    lines.append('')
    lines.append('---')
    lines.append('')

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Wrote tier8-tables.md with {written} table schemas, {sum(1 for l in lines if l.startswith("| "))} field rows.')
