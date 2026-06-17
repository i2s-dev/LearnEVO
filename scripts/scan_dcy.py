"""Quick DCY form scanner — prints object types and UI strings."""
import re, sys, os
from collections import Counter

def scan(fpath):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', errors='replace') as f:
        content = f.read()
    types = re.findall(r'object (\w+): (\w+)', content)
    tc = Counter(t for _, t in types)
    strings = re.findall(r"(?:Caption|Hint|Text|DataField)\s*=\s*'([^']{1,120})'", content)
    print(f'=== {fname} ({len(content):,} chars, {len(types)} objects) ===')
    print('  Types:', dict(tc.most_common(8)))
    kept = []
    for s in strings:
        s = s.strip()
        if not s:
            continue
        lower = s.lower()
        # skip file paths and hex icon data
        if lower.startswith('c:') or s.startswith('\\\\') or lower.startswith('//'):
            continue
        kept.append(s)
    for s in kept[:30]:
        print(f'  >> {s!r}')
    print()

for path in sys.argv[1:]:
    scan(path)
