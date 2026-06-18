"""
Extract all SQL queries and interesting method names from EvoERP JAR classes.
Focus on: SQL strings, table names, field names, task names.
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

base = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\jar\extracted'

# Skip third-party Pervasive classes — only look at evoerp package
evoerp_classes = glob.glob(base + r'\com\evoerp\**\*.class', recursive=True)

# Keywords that suggest data/query/table content
sql_kws = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'FROM ', 'WHERE ', 'ISJAVA', 'IS_JAVA',
           'BKGL', 'BKAR', 'BKAP', 'BKIN', 'BKSO', 'BKWO', 'BKPO', 'BKBM', 'BKCM',
           'MTCAL', 'ISSHIP', 'CALEND', 'WORKORD', 'BKICMSTR']

hits = {}
for fpath in sorted(evoerp_classes):
    try:
        strings = extract_strings(fpath)
        class_hits = []
        for s in strings:
            su = s.upper()
            if any(kw in su for kw in sql_kws):
                class_hits.append(s)
        if class_hits:
            fname = fpath.replace(base, '').replace('\\', '/').lstrip('/')
            hits[fname] = class_hits
    except Exception as e:
        pass

for fname, strs in sorted(hits.items()):
    print(f'=== {fname} ===')
    for s in strs:
        print(f'  {repr(s)}')
    print()

print(f'Total: {len(hits)} classes with SQL/table hits')
