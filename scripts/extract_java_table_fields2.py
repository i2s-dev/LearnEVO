"""
Extract field names from Java table model classes in EvoPVT.jar.
Filter: strings that look like Pervasive field names (BK_/IS_/MT_ prefix patterns, etc.)
"""
import sys, os, glob, re
sys.stdout.reconfigure(encoding='utf-8')

def extract_strings(fpath):
    with open(fpath, 'rb') as f:
        data = f.read()
    if data[:4] != b'\xca\xfe\xba\xbe':
        return []
    cp_count = int.from_bytes(data[8:10], 'big')
    pos = 10
    strings = []
    j = 1
    while j < cp_count:
        tag = data[pos]
        pos += 1
        if tag == 1:
            length = int.from_bytes(data[pos:pos+2], 'big')
            pos += 2
            s = data[pos:pos+length]
            pos += length
            try:
                decoded = s.decode('utf-8', errors='replace')
                if len(decoded) > 2:
                    strings.append(decoded)
            except:
                pass
        elif tag in (7, 8, 16, 19, 20):
            pos += 2
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            pos += 4
        elif tag in (5, 6):
            pos += 8
            j += 1
        elif tag == 15:
            pos += 3
        j += 1
    return strings

def is_field_name(s):
    """Heuristic: EvoERP field names are uppercase with underscores, 3-40 chars."""
    if not s or len(s) < 3 or len(s) > 50:
        return False
    # Must be all uppercase or uppercase+underscores+digits
    if not re.match(r'^[A-Z][A-Z0-9_\.]+$', s):
        return False
    # Must have at least one underscore (field names) or be all alpha (table names)
    if '_' not in s and not s.isalpha():
        return False
    return True

base = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\jar\extracted\com\evoerp\sql'

targets = [
    'ISLINKS', 'ISSHIPCO', 'CALENDAR', 'WORKORD', 'AHSYLOG', 'BKSLEVEL',
    'BKSYUSER', 'BKLOGON', 'BKFLDHLP', 'BKUPDATE', 'ISBSF',
    'ISREMIND', 'ISSOHNFO', 'ISSOINFO', 'ISFOLINE', 'ISFOHEAD',
    'BKQCMSTR', 'ROUTING', 'WORKCTR', 'MACHINE',
    'BKICMSTR', 'BKICPMAT', 'BKICLOC',
    'BKBMMSTR', 'BKCMCUST', 'BKCMCTRL',
    'BKSYMSTR', 'BKSYCFG', 'Tables',
]

for tname in sorted(targets):
    fpath = os.path.join(base, tname + '.class')
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {tname}')
        continue
    strings = extract_strings(fpath)
    field_names = [s for s in strings if is_field_name(s)]
    sql = [s for s in strings if any(kw in s.upper() for kw in ['SELECT ', 'INSERT ', 'UPDATE ', 'FROM ', 'WHERE ', 'VALUES '])]
    print(f'=== {tname} ({len(field_names)} fields) ===')
    if sql:
        for s in sql:
            print(f'  SQL> {repr(s)}')
    for f in field_names:
        print(f'  {f}')
    print()
