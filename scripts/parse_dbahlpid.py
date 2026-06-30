"""
Parse DBAHLPID.B — EvoERP help system ID table.
Maps menu/help topic codes to help page IDs.

Observed record format: '8XX-Y    ' (9 chars) + 1 byte ID
  8  = section prefix (all EVO help = section 8?)
  XX = 2-letter module code (AP=Accounts Payable, CM=Contact Manager, etc.)
  -Y = operation code (A, B, C, ...)
  (spaces) = padding to fixed width

Goal: extract all unique help topic codes and catalog by module.
Also check DBAHELP.B for the actual help text.
"""
import re
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")

# Module code mappings (confirmed + inferred from EVO menu codes)
KNOWN_MODULES = {
    'AD': 'Address Manager',
    'AI': 'Auto Inventory (unknown — to verify)',
    'AM': 'Auto Manager (unknown)',
    'AP': 'Accounts Payable',
    'AR': 'Accounts Receivable',
    'BM': 'Bill of Materials / Work Order (BOM)',
    'BR': 'Bank Reconciliation / unknown',
    'CM': 'Contact Manager (CRM)',
    'EC': 'Electronic Commerce / EDI',
    'FA': 'Fixed Assets',
    'GL': 'General Ledger',
    'IC': 'Inventory Control / Item Cost',
    'IN': 'Inventory',
    'JC': 'Job Costing',
    'LI': 'Label/List Print',
    'MF': 'Manufacturing',
    'MR': 'MRP (Material Requirements Planning)',
    'PO': 'Purchase Orders',
    'PR': 'Payroll',
    'PS': 'Point of Sale',
    'QC': 'Quality Control',
    'RO': 'Returns/Repairs',
    'SA': 'Sales Analysis',
    'SE': 'Service / Engineering',
    'SO': 'Sales Orders',
    'SU': 'System Utilities',
    'SY': 'System Setup',
    'WO': 'Work Orders',
}


def extract_help_codes(data):
    """Extract all help topic codes from DBAHLPID.B."""
    pattern = re.compile(rb'\x38([A-Z]{2})-([A-Z0-9])([ A-Z0-9-]*?)(?=\x00|\xff|[^\x20-\x7e])')

    # Match format: 0x38 = '8', then XX-Y followed by spaces
    # Use a string approach: extract all printable strings then filter
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 5:
                strings.append((start, ''.join(current)))
            current = []
    if current and len(current) >= 5:
        strings.append((start, ''.join(current)))

    # Filter to help codes: pattern '8XX-Y    ' (9 chars with spaces)
    help_code_pattern = re.compile(r'^8[A-Z]{2}-[A-Z0-9](\s{2,})?')
    raw_codes = [(pos, s) for pos, s in strings if help_code_pattern.match(s)]

    # Extract the canonical code (first 9 chars, trimmed) and trailing byte
    code_occurrences = defaultdict(list)
    for pos, s in raw_codes:
        # The code is the portion up to and including spaces: '8XX-Y    '
        # Usually format: '8AP-A    %' where % is trailing ID byte
        # Take first 9 chars as the key (8 + XX + - + Y + 4 spaces)
        code_full = s[:9].rstrip() if len(s) >= 9 else s.rstrip()
        # Remove the '8' prefix and trailing spaces
        code_clean = code_full.lstrip('8').rstrip()
        code_occurrences[code_clean].append(pos)

    # Count unique codes
    unique_codes = sorted(code_occurrences.keys())
    print(f"Unique help topic codes: {len(unique_codes)}")

    # Group by module
    by_module = defaultdict(list)
    for code in unique_codes:
        # code format: 'XX-Y' or 'XX-Y-Z'
        if len(code) >= 2:
            module = code[:2]
            by_module[module].append(code)

    print(f"Module codes found: {len(by_module)}")
    print()

    # Print by module with description
    all_ops = []
    for module in sorted(by_module.keys()):
        codes = sorted(by_module[module])
        desc = KNOWN_MODULES.get(module, '(unknown module)')
        ops = [c.split('-', 1)[1] if '-' in c else '?' for c in codes]
        print(f"  {module} ({desc}):")
        print(f"    {len(codes)} operations: {', '.join(ops)}")
        all_ops.append((module, desc, len(codes)))

    # Summary
    print(f"\nTotal modules: {len(by_module)}")
    print(f"Total operations: {sum(len(v) for v in by_module.values())}")
    print(f"\nModules by op count (desc):")
    for module, desc, cnt in sorted(all_ops, key=lambda x: -x[2]):
        print(f"  {module}: {cnt} ops  [{desc}]")

    return by_module, unique_codes


def check_dbahelp():
    """Check if DBAHELP.B is available (contains actual help text)."""
    path = SAMPLES / 'DBAHELP.B'
    if not path.exists():
        print("\nDBAHELP.B: not in samples/ — copy needed from network share")
        return
    data = path.read_bytes()
    print(f"\n=== DBAHELP.B ({len(data):,} bytes) ===")
    # Extract a sample of text
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 10:
                strings.append((start, ''.join(current)))
            current = []
    print(f"  Strings >=10 chars: {len(strings)}")
    for pos, s in strings[:20]:
        print(f"  [{pos:06X}] {s!r}")


if __name__ == '__main__':
    data = (SAMPLES / 'DBAHLPID.B').read_bytes()
    print(f"=== DBAHLPID.B ({len(data):,} bytes) ===\n")
    by_module, unique_codes = extract_help_codes(data)
    check_dbahelp()
