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
keywords = ['HKEY', 'HKLM', 'HKCU', 'ADDSUM', 'EVO ERP', 'EVOCALC', 'PERVASIVE', 'ACTIAN', 'JDBC.INI', 'JDBC\\']
hits = {}
for fpath in glob.glob(base + '\\**\\*.class', recursive=True):
    try:
        strings = extract_strings(fpath)
        for s in strings:
            su = s.upper()
            if any(kw in su for kw in keywords):
                fname = fpath.replace(base, '').replace('\\', '/').lstrip('/')
                if fname not in hits:
                    hits[fname] = []
                hits[fname].append(s)
    except Exception as e:
        pass

for fname, strs in sorted(hits.items()):
    print(f'=== {fname} ===')
    for s in strs:
        print(f'  {repr(s)}')

print(f'\nTotal: {len(hits)} classes with registry/path hits')
