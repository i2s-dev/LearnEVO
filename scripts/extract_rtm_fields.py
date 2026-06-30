"""
Extract DataField bindings from all RTM (Delphi TPF0 binary DFM) files.

In TPF0 binary format, properties are stored as:
  1-byte name-length + name-bytes + type-tag + value-encoding

For string properties (DataField), the value encoding after the name is:
  type tag (1 byte: 0x12 = widestring, 0x06 = string, 0x0F = string also)
  then 1-byte length + string bytes (Pascal short string for short strings)
  OR 4-byte length + bytes (for long strings)

This script uses a pattern search approach: look for the byte sequence
for "DataField" as a length-prefixed name, then extract the following string.

Also extracts: FileName (template/subreport links), PipelineName, DataPipeline.
"""
import struct
import re
import csv
import sys
from pathlib import Path

SHARE = Path(r"\\i2s109-solidcrm\DBAMFG$")
OUT_CSV = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rtm_fields.csv")

# Properties to extract
TARGET_PROPS = ["DataField", "FileName", "DataPipeline", "PipelineName", "DatabaseName"]

def extract_strings_after_prop(data: bytes, prop_name: str) -> list[str]:
    """
    Find all occurrences of prop_name as a length-prefixed string in the binary,
    then extract the following string value.

    TPF0 property layout:
      [1 byte: name length][name bytes][type tag 1 byte][value]
    For string type tags, value is:
      [1 byte: str length][str bytes]  (short string)
    or for type 0x12 (widestring):
      [4 bytes: char count][chars (2 bytes each)]
    """
    results = []
    name_bytes = prop_name.encode('ascii')
    name_len = len(name_bytes)
    pattern = bytes([name_len]) + name_bytes

    offset = 0
    while True:
        idx = data.find(pattern, offset)
        if idx == -1:
            break

        # Position after the property name
        val_start = idx + 1 + name_len
        if val_start >= len(data):
            break

        type_tag = data[val_start]

        try:
            if type_tag in (0x06, 0x0F):  # Short string types
                str_len = data[val_start + 1]
                if val_start + 2 + str_len <= len(data):
                    s = data[val_start + 2: val_start + 2 + str_len].decode('ascii', errors='replace')
                    if s.strip():
                        results.append(s)
            elif type_tag == 0x12:  # WideString
                char_count = struct.unpack_from('<I', data, val_start + 1)[0]
                if char_count < 1000 and val_start + 5 + char_count * 2 <= len(data):
                    raw = data[val_start + 5: val_start + 5 + char_count * 2]
                    s = raw.decode('utf-16-le', errors='replace')
                    if s.strip():
                        results.append(s)
        except Exception:
            pass

        offset = idx + 1

    return results


def process_rtm(path: Path) -> dict:
    """Extract all target property bindings from a single RTM file."""
    try:
        data = path.read_bytes()
    except Exception as e:
        return {'error': str(e)}

    if not data.startswith(b'TPF0'):
        return {'error': 'not TPF0'}

    result = {}
    for prop in TARGET_PROPS:
        vals = extract_strings_after_prop(data, prop)
        if vals:
            result[prop] = sorted(set(vals))

    return result


def main():
    rtm_files = sorted(SHARE.glob("*.RTM")) + sorted(SHARE.glob("*.rtm"))
    print(f"Found {len(rtm_files)} RTM files")

    rows = []
    for rtm in rtm_files:
        result = process_rtm(rtm)
        if 'error' in result:
            rows.append({'file': rtm.name, 'property': 'ERROR', 'value': result['error']})
            continue

        for prop, vals in result.items():
            for val in vals:
                rows.append({'file': rtm.name, 'property': prop, 'value': val})

        if not result:
            rows.append({'file': rtm.name, 'property': '', 'value': ''})

    # Write CSV
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['file', 'property', 'value'])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Written {len(rows)} rows to {OUT_CSV}")

    # Print summary
    data_field_files = len({r['file'] for r in rows if r['property'] == 'DataField'})
    filename_files = len({r['file'] for r in rows if r['property'] == 'FileName'})
    print(f"Files with DataField: {data_field_files}")
    print(f"Files with FileName (subreport links): {filename_files}")

    # Unique DataField values
    all_df = sorted({r['value'] for r in rows if r['property'] == 'DataField'})
    print(f"\nTotal unique DataField values: {len(all_df)}")
    print("Sample (first 30):")
    for v in all_df[:30]:
        print(f"  {v}")


if __name__ == '__main__':
    main()
