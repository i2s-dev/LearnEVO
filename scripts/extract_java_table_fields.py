"""
Extract field names from key Java table model classes in EvoPVT.jar.
Focus on BKAP/BKAR/BKGL/ISLINKS/ISSHIPCO/CALENDAR/WORKORD tables.
"""
import sys, os, glob
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

base = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\jar\extracted\com\evoerp\sql'

# Tables of interest for documentation
targets = [
    'ISLINKS', 'ISSHIPCO', 'CALENDAR', 'WORKORD', 'AHSYLOG', 'BKSLEVEL',
    'BKSYUSER', 'BKLOGON', 'BKFLDHLP', 'BKUPDATE', 'ISBSF', 'ISNOTES',
    'ISREMIND', 'ISSOHNFO', 'ISSOINFO', 'ISFOLINE', 'ISFOHEAD',
    'BKQCMSTR', 'BKQCTRAN', 'ROUTING', 'WORKCTR', 'MACHINE',
    'BKICMSTR', 'BKICPMAT', 'BKICLOC',
    'BKBMMSTR', 'BKCMCUST', 'BKCMCTRL',
    'BKSYMSTR', 'BKSYCFG',
    'Tables',
]

for tname in targets:
    fpath = os.path.join(base, tname + '.class')
    if not os.path.exists(fpath):
        # Try recursive search
        found = glob.glob(base + r'\**\' + tname + '.class', recursive=True)
        if found:
            fpath = found[0]
        else:
            print(f'NOT FOUND: {tname}')
            continue
    strings = extract_strings(fpath)
    # Filter to likely field names: all-caps with underscores, length 3-40
    fields = [s for s in strings
              if s.isupper() or (s.replace('_','').replace('.','').isupper() and '_' in s)
              and 3 <= len(s) <= 40
              and not s.startswith('L') and not s.startswith('(')
              and not s.startswith('[')]
    # Also capture SQL fragments
    sql = [s for s in strings if any(kw in s.upper() for kw in ['SELECT', 'INSERT', 'UPDATE', 'FROM ', 'WHERE '])]
    print(f'=== {tname} ===')
    if sql:
        for s in sql:
            print(f'  SQL: {repr(s)}')
    # Print all strings that look like field names or method names
    for s in strings:
        if (s.upper() == s or s[0].isupper()) and 3 <= len(s) <= 50:
            if not s.startswith('L') and not s.startswith('(') and not s.startswith('['):
                if '/' not in s and '.' not in s and '<' not in s:
                    print(f'  {repr(s)}')
    print()
