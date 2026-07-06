"""Analyze .RUN header structure to decode bytecode layout"""
import struct, os

BASE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO"

def analyze_run(path):
    with open(path, 'rb') as f:
        data = f.read()
    fname = os.path.basename(path)
    print(f"\n=== {fname} ({len(data):,} bytes) ===")

    # Show first 64 bytes
    for i in range(0, 64, 16):
        chunk = data[i:i+16]
        hex_str = ' '.join(f'{b:02X}' for b in chunk)
        asc_str = ''.join(chr(b) if 32<=b<127 else '.' for b in chunk)
        print(f'  {i:04X}: {hex_str:<48}  {asc_str}')

    print()

    # Try known offsets from the extraction script:
    # Header 0x08 = data channel total size
    dc_end = struct.unpack_from('<I', data, 8)[0]
    print(f'  0x08 (data_chan_end): {dc_end:,} = 0x{dc_end:06X}  ({dc_end/len(data)*100:.1f}%)')

    # Look for strings at the start of data channel
    # Data channel starts at offset 0x00 and goes to dc_end
    # Find first 0x41 0x00 LL LL string record
    first_str_pos = None
    for i in range(min(200, len(data))):
        if i+3 < len(data) and data[i] == 0x41 and data[i+1] == 0x00:
            length = struct.unpack_from('<H', data, i+2)[0]
            if 0 < length < 256:
                s = data[i+4:i+4+length]
                if all(32 <= b < 127 for b in s):
                    first_str_pos = i
                    print(f'  First string at 0x{i:04X}: len={length}, value={s.decode("ascii")}')
                    break

    # Scan for program identifier (after data channel strings)
    # Look for instruction-like patterns after dc_end
    if dc_end < len(data):
        instr_start = dc_end
        print(f'  Instruction area starts at: 0x{instr_start:04X}')
        print(f'  Next 32 bytes of instr area:')
        chunk = data[instr_start:instr_start+32]
        hex_str = ' '.join(f'{b:02X}' for b in chunk)
        print(f'    {hex_str}')

        # Count instruction bytes (7-byte fixed instructions in TAS6 .RUN?)
        remaining = len(data) - instr_start
        print(f'  Instruction area size: {remaining:,} bytes')
        if remaining % 7 == 0:
            print(f'  >> MATCHES 7-byte instruction size ({remaining//7} instructions)')
        if remaining % 6 == 0:
            print(f'  >> MATCHES 6-byte instruction size ({remaining//6} instructions)')
        if remaining % 5 == 0:
            print(f'  >> MATCHES 5-byte instruction size ({remaining//5} instructions)')
        if remaining % 8 == 0:
            print(f'  >> MATCHES 8-byte instruction size ({remaining//8} instructions)')

        # Check byte frequency in instruction area
        from collections import Counter
        instr_data = data[instr_start:]
        freq = Counter(instr_data)
        top10 = freq.most_common(10)
        print(f'  Top 10 bytes in instr area: {[(hex(b), cnt) for b,cnt in top10]}')

# Analyze multiple .RUN files
for fname in ['samples/run_sample/T6APB.RUN', 'samples/run_sample/T6WOC.RUN', 'samples/BKAPA.RUN', 'samples/BKAWLB.RUN']:
    path = os.path.join(BASE, fname)
    if os.path.exists(path):
        analyze_run(path)
    else:
        print(f"Not found: {fname}")
