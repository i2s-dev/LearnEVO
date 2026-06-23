"""Generic batch var extractor — reads named decrypted .RWN files and shows module-specific vars."""
import sys, struct, os, glob, argparse
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROC_ENTRY_SIZE = 53
VAR_ENTRY_SIZE  = 77
SRCNAME_SIZE    = 60
HEADER_SIZE     = 128
FILE_TABLE_OFF  = 0x80
FILE_ENTRY_SIZE = 16

def dw(data, off):
    return struct.unpack_from("<I", data, off)[0]

def parse_var_name(data, entry_off):
    type_byte = data[entry_off]
    if type_byte < 0x20:
        raw = data[entry_off+1:entry_off+15]
    else:
        raw = data[entry_off:entry_off+15]
    return raw.rstrip(b"\x00 ").decode("ascii", errors="replace"), type_byte

def extract_all(path):
    raw = open(path, "rb").read()
    if len(raw) >= 8 and raw[0:4] == raw[4:8]:
        data = raw[8:]
    else:
        data = raw
    if len(data) < HEADER_SIZE:
        return {}

    proc_table_size = dw(data, 0x0C)
    var_count       = dw(data, 0x14)
    var_table_size  = dw(data, 0x20)

    proc_count = proc_table_size // PROC_ENTRY_SIZE if proc_table_size >= PROC_ENTRY_SIZE else 0
    var_table_off = len(data) - var_table_size
    src_off       = var_table_off - SRCNAME_SIZE
    proc_off      = src_off - proc_table_size

    src_name = data[src_off:src_off+SRCNAME_SIZE].rstrip(b"\x00 ").decode("ascii", errors="replace") if src_off >= 0 else ""

    db_files = []
    off = FILE_TABLE_OFF
    while off + FILE_ENTRY_SIZE <= len(data):
        entry = data[off:off+FILE_ENTRY_SIZE]
        if entry == b"\x00" * FILE_ENTRY_SIZE:
            break
        name = entry.rstrip(b"\x00 ").decode("ascii", errors="replace")
        if name:
            db_files.append(name)
        off += FILE_ENTRY_SIZE

    vars_named = []
    for i in range(var_count):
        entry_off = var_table_off + i * VAR_ENTRY_SIZE
        if entry_off + VAR_ENTRY_SIZE > len(data):
            break
        name, type_byte = parse_var_name(data, entry_off)
        if name and not name.startswith("TEMP"):
            vars_named.append(name)

    procs_out = []
    for i in range(proc_count):
        off = proc_off + i * PROC_ENTRY_SIZE
        if off < 0 or off + PROC_ENTRY_SIZE > len(data):
            break
        name_len = data[off]
        raw_name = data[off+1:off+1+min(name_len, 15)]
        procs_out.append(raw_name.decode("ascii", errors="replace").rstrip("\x00"))

    return {
        "proc_count": proc_count,
        "var_count": var_count,
        "src_name": src_name,
        "db_files": db_files,
        "vars_named": vars_named,
        "procs": procs_out,
    }

# Common library vars to filter out
LIBRARY_PREFIXES = ("ISTS.CFG", "EMAIL.CFG", "EVO.CFG", "HOTBUTTON", "MKAHIST", "ARA.", "APA.",
                    "INA.", "INB.", "SOA.", "POA.", "WOA.", "DEFPRINT", "XCPATH", "WEBLINK",
                    "JAVA.", "HOST", "PORT", "NAME", "COMP", "TREEDEST", "RVAL", "DFM",
                    "NOPE", "DUMMY", "ISTS.ED", "BKAR.IS", "BKAR.GROSS", "BKAR.COGS", "BKAR.NET",
                    "BKAR.PNET", "LOOKUP", "ETBCOMBOVAL", "PROGRAM.H", "SWHO", "PLDN", "PTDN",
                    "ZRET", "ISTS.PATH", "ISTS.CFROM", "PRINTBOXES", "INV_IMAGE", "L.ICONSTR",
                    "MK.H", "WHO.H", "WBUFF", "FRMPRG", "RWHO", "ESETTINGS", "RETATVAL",
                    "SOB.LINES", "POB.LINES", "RESTOCK.AMT", "GL.FUTURE.DATE")

files_arg = sys.argv[1:] if len(sys.argv) > 1 else []
base = "samples/rwn_decrypted/"

for target in files_arg:
    matches = glob.glob(base + target + "*.dec") + glob.glob(base + target.lower() + "*.dec")
    matches = list(set(matches))
    if not matches:
        print(f"\n=== {target} — NOT FOUND ===")
        continue
    for f in sorted(matches):
        fname = os.path.basename(f)
        info = extract_all(f)
        if not info:
            print(f"\n=== {fname} — PARSE FAILED ===")
            continue
        named = info["vars_named"]
        prefixes = Counter()
        for v in named:
            p = v.split(".")[0] if "." in v else v[:8]
            prefixes[p] += 1
        unique_vars = [v for v in named if not any(v.startswith(p) for p in LIBRARY_PREFIXES)]
        print(f"\n=== {fname} ({info['proc_count']}p, {info['var_count']}v, {len(named)} non-TEMP, src={info['src_name']}) ===")
        print(f"  DB files ({len(info['db_files'])}): {info['db_files']}")
        print(f"  Procs ({len([p for p in info['procs'] if p.strip()])}): {[p for p in info['procs'] if p.strip()][:20]}")
        print(f"  Non-library vars ({len(unique_vars)}): {unique_vars[:60]}")
