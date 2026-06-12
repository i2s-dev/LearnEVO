#!/usr/bin/env python3
"""
scripts/get_iv_frida.py

Automatically extracts the initial IV (block_buf) from tp7runtime.exe by
hooking mode2_handler (the CFB/OFB decrypt entry point) at its first call.

HOW IT WORKS
    1. Launches tp7runtime.exe under Frida instrumentation.
    2. Hooks mode2_handler at RVA 0x34EB50 (VA 0x74EB50).
    3. On first call, EAX = cipher object; reads [EAX+0x3C] (16 bytes) = block_buf = IV.
    4. Prints the IV hex string and saves it to scripts/iv_bytes.bin.
    5. verify_iv.py can then cross-check against known .RWN files.
    6. rwn_decrypt.py can then batch-decrypt all 1,124 .RWN and .DCY files.

INSTALL
    pip install frida-tools

    (frida-tools bundles frida; no C compiler needed. Requires Python 3.7+.)

USAGE
    python scripts/get_iv_frida.py

    The script spawns tp7runtime.exe with suwin7.rwn, captures the IV, then
    prints it.  Close the tp7runtime.exe window after the IV is printed (or
    it will close automatically when Frida terminates it).

NOTES
    - If you get a "failed to spawn" error, try running from an elevated
      (Admin) PowerShell prompt.
    - tp7runtime.exe must be at C:\\ISTS\\tp7runtime.exe.
    - suwin7.rwn must exist at C:\\ISTS\\suwin7.rwn (verified present).

BACKGROUND
    Cipher: Twofish-CFB/OFB (DCPcrypt TDCP_twofish).
    Key: SHA1('mabufoju')[0:20] + 0x00*4 = 24-byte (192-bit) key.
    block_buf: uninitialized heap memory at cipher+0x3C.  The constructor
    calls GetMem but never zeroes it; the Init chain never touches it.
    Value is fixed for a given runtime session (heap state is deterministic
    at startup), so one debugger run is sufficient for all files.

    See docs/02-file-formats/decryption-findings.md and BROKEN.md B-004.
"""

import sys
import os
import time

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
TARGET_EXE   = r"C:\ISTS\tp7runtime.exe"
TARGET_ARG   = r"C:\ISTS\suwin7.rwn"
IV_OUT       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iv_bytes.bin")
TIMEOUT_SEC  = 45   # give tp7runtime up to 45 s to hit mode2_handler

# mode2_handler: file offset 0x34DF50 (VA 0x74EB50 = ImageBase 0x400000 + RVA 0x34EB50)
MODE2_RVA         = 0x34EB50
BLOCK_BUF_OFFSET  = 0x3C  # offset of block_buf inside the cipher object (EAX)
IV_SIZE           = 16

# ---------------------------------------------------------------------------
# Frida JavaScript payload (injected into tp7runtime.exe)
# ---------------------------------------------------------------------------
_JS = """
'use strict';

var MODE2_RVA        = 0x34EB50;
var BLOCK_BUF_OFFSET = 0x3C;
var IV_SIZE          = 16;
var captured         = false;

var base = Module.findBaseAddress('tp7runtime.exe');
if (!base) {
    send({ type: 'error', msg: 'tp7runtime.exe module not found in the target process.' });
} else {
    var target = base.add(MODE2_RVA);
    send({ type: 'info', msg: 'Hooked mode2_handler at ' + target +
          ' (base=' + base + ', rva=0x' + MODE2_RVA.toString(16) + ')' });

    Interceptor.attach(target, {
        onEnter: function(args) {
            if (captured) return;
            captured = true;

            // Delphi register calling convention: EAX = Self (cipher object)
            var self_ptr  = ptr(this.context.eax.toString());
            var blockBuf  = self_ptr.add(BLOCK_BUF_OFFSET);

            var raw   = blockBuf.readByteArray(IV_SIZE);
            var bytes = Array.from(new Uint8Array(raw));

            send({ type: 'iv',
                   eax:   this.context.eax.toString(),
                   bytes: bytes });
        }
    });
}
"""

# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main():
    try:
        import frida
    except ImportError:
        print("ERROR: frida not installed.  Run:  pip install frida-tools")
        sys.exit(1)

    iv_found = [None]

    def on_message(message, data):
        if message['type'] == 'error':
            print(f"[Frida runtime error] {message.get('description', message)}")
            return
        payload = message.get('payload') or {}
        kind    = payload.get('type')
        if kind == 'info':
            print(f"[*] {payload['msg']}")
        elif kind == 'error':
            print(f"[!] {payload['msg']}")
        elif kind == 'iv':
            blist   = payload['bytes']
            hex_str = ' '.join(f'{b:02x}' for b in blist)
            py_lit  = 'bytes([' + ', '.join(f'0x{b:02x}' for b in blist) + '])'
            print()
            print("=" * 54)
            print("  IV (block_buf) EXTRACTED")
            print("=" * 54)
            print(f"  Cipher object (EAX) : {payload['eax']}")
            print(f"  block_buf (IV)      : {hex_str}")
            print()
            print(f"  Python literal: {py_lit}")
            print("=" * 54)

            with open(IV_OUT, 'wb') as f:
                f.write(bytes(blist))
            print(f"\n  Saved to: {IV_OUT}")
            print("  Run:  python scripts/verify_iv.py   (cross-check)")
            print("  Run:  python scripts/rwn_decrypt.py  (batch decrypt)")
            iv_found[0] = bytes(blist)

    print(f"[*] Launching tp7runtime.exe under Frida ...")
    print(f"[*] Target  : {TARGET_EXE}")
    print(f"[*] Argument: {TARGET_ARG}")
    print(f"[*] Waiting for mode2_handler (up to {TIMEOUT_SEC}s) ...")
    print()

    try:
        pid = frida.spawn([TARGET_EXE, TARGET_ARG])
    except Exception as e:
        print(f"[!] Failed to spawn: {e}")
        print("    Try running this script from an elevated (Administrator) prompt.")
        sys.exit(1)

    try:
        session = frida.attach(pid)
        script  = session.create_script(_JS)
        script.on('message', on_message)
        script.load()
        frida.resume(pid)
    except Exception as e:
        print(f"[!] Failed to inject: {e}")
        frida.kill(pid)
        sys.exit(1)

    deadline = time.time() + TIMEOUT_SEC
    while iv_found[0] is None and time.time() < deadline:
        time.sleep(0.2)

    try:
        session.detach()
    except Exception:
        pass

    if iv_found[0] is None:
        print(f"\n[!] Timeout: mode2_handler was not called within {TIMEOUT_SEC} seconds.")
        print("    Possible causes:")
        print("    - suwin7.rwn is missing or corrupt")
        print("    - tp7runtime.exe crashed before loading the .RWN")
        print("    - RVA is wrong for this build of tp7runtime.exe")
        print()
        print("    Fallback: use scripts/x64dbg_get_iv.txt instead.")
        sys.exit(1)
    else:
        print()
        print("[*] Done.  tp7runtime.exe may still be running; close it manually.")


if __name__ == '__main__':
    main()
