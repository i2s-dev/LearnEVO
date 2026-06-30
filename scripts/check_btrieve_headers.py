"""Check headers of Btrieve table files."""
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")

files = ['MENUFILE.B', 'PRGFILE.B', 'BKSYUSER.B', 'BKSLEVEL.B', 'DBAHLPID.B', 'FIELDS.B', 'PRGFILE2.B']
for fname in files:
    path = SAMPLES / fname
    if not path.exists():
        print(f"{fname}: NOT FOUND")
        continue
    data = path.read_bytes()
    header = ' '.join(f'{b:02X}' for b in data[:16])
    unique_bytes = len(set(data[:512]))
    printable = sum(1 for b in data[:512] if 32 <= b < 127)
    ascii_pct = printable / min(512, len(data)) * 100
    magic = data[0:2]
    magic_str = ''.join(chr(b) if 32 <= b < 127 else '?' for b in magic)
    print(f"{fname:20}: {len(data):7} bytes | {header} | unique={unique_bytes}/256 | ascii%={ascii_pct:.0f}% | magic={magic_str!r}")
    # Show some of the content
    runs = []
    current = []
    for b in data:
        if 32 <= b < 127:
            current.append(chr(b))
        else:
            if len(current) >= 4:
                runs.append(''.join(current))
            current = []
    if current and len(current) >= 4:
        runs.append(''.join(current))
    if runs:
        print(f"  Sample strings: {runs[:5]}")
    else:
        print(f"  No printable strings! Likely encrypted/binary-packed")
    print()
