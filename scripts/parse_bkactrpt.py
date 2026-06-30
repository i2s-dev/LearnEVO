"""
Parse BKACTRPT.MKD — EvoERP saved report configuration table.
Stored in DEV subfolder of DBAMFG$.

From FILEDICT.UPD, BKACTRPT fields are:
  BKAC.FROM.CAT    - from category
  BKAC.FROM.CLASS  - from class
  BKAC.FROM.DATE   - from date
  BKAC.FROM.DESC   - from description
  BKAC.FROM.PRICE  - from price
  BKAC.FROM.TYPE   - from type
  BKAC.FROM.WOPRE  - from WO prefix
  BKAC.ITEM.RANGE  - item range
  BKAC.NAME        - report configuration name
  BKAC.RTM         - RTM template filename
  + 13 more

Goal: extract (BKAC.NAME, BKAC.RTM) pairs to map report names to template files.
"""
import re
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def extract_report_records(filename='BKACTRPT.MKD'):
    path = SAMPLES / filename
    data = path.read_bytes()
    print(f"{filename}: {len(data):,} bytes")

    # Extract all printable strings >= 4 chars
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 4:
                s = ''.join(current).strip()
                if s:
                    strings.append((start, len(''.join(current)), s))
            current = []
    if len(current) >= 4:
        strings.append((start, len(''.join(current)), ''.join(current).strip()))

    print(f"Total strings (>=4 chars): {len(strings)}")

    # Find RTM file references
    rtm_strings = [(pos, s) for pos, _, s in strings if '.RTM' in s.upper() or '.rtm' in s]
    print(f"\nRTM file references ({len(rtm_strings)}):")
    for pos, s in rtm_strings[:30]:
        print(f"  [{pos:06X}] {s!r}")

    # Find report name candidates (mixed alphanumeric, reasonable length 5-40)
    report_names = []
    for pos, sz, s in strings:
        clean = s.strip()
        if 5 <= len(clean) <= 40 and any(c.isalpha() for c in clean) and ' ' in clean:
            report_names.append((pos, clean))

    print(f"\nPossible report names ({len(report_names)} total, showing first 40):")
    seen = set()
    for pos, name in report_names[:80]:
        if name not in seen:
            seen.add(name)
            print(f"  [{pos:06X}] {name!r}")

    # Try to find paired (name, RTM) records
    # The record format likely has: name field + RTM field close together
    print("\n--- Looking for name+RTM pairs ---")
    data_text = data.decode('ascii', errors='replace')
    # Search for RTM file names and look at context
    for m in re.finditer(r'[A-Z0-9]{2,8}\.RTM', data_text):
        rtm_name = m.group()
        pos = m.start()
        # Look backwards up to 80 bytes for a text description
        window_start = max(0, pos - 80)
        window = data[window_start:pos]
        text_before = ''.join(chr(b) if 32 <= b < 127 else '|' for b in window)
        # Find last clean text run before the RTM name
        parts = [p.strip() for p in text_before.split('|') if len(p.strip()) >= 4]
        if parts:
            name_candidate = parts[-1]
            print(f"  RTM={rtm_name!r:16} name_before={name_candidate!r}")


if __name__ == '__main__':
    extract_report_records()
