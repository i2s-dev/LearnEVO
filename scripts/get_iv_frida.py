#!/usr/bin/env python3
"""
scripts/get_iv_frida.py

Extracts block_buf (the initial IV) from a running or freshly-spawned
tp7runtime.exe by hooking mode2_handler (file offset 0x34DF50, RVA 0x34EB50).

BEHAVIOUR
    1. If tp7runtime.exe is ALREADY running: attaches to it.
       Navigate to any EVO module after this script starts — that loads an
       .RWN file and fires the hook.
    2. If tp7runtime.exe is NOT running: spawns it with EvoERPmenu.RWN.
       EVO will open normally.  Log in and navigate to any module.

    Either way, the hook fires the first time mode2_handler is called and
    saves the 16-byte IV to scripts/iv_bytes.bin.  The script then exits.

REQUIREMENTS
    pip install frida-tools

USAGE
    python scripts/get_iv_frida.py

    The script prints instructions once the hook is armed.
    You do NOT need to keep watching it — just use EVO normally.

KEY ADDRESSES (confirmed from disassembly)
    mode2_handler  file offset 0x34DF50  RVA 0x34EB50
    block_buf      cipher+0x3C           16 bytes = IV
"""

import sys
import os
import subprocess
import time

_here    = os.path.dirname(os.path.abspath(__file__))
IV_OUT   = os.path.join(_here, 'iv_bytes.bin')

TARGET_EXE = r'C:\ISTS\tp7runtime.exe'
TARGET_RWN = r'\\i2s109-solidcrm\DBAMFG$\EvoERPmenu.RWN'

# mode2_handler RVA (= preferred VA 0x74EB50 - preferred ImageBase 0x400000)
MODE2_RVA         = 0x34EB50
BLOCK_BUF_OFFSET  = 0x3C
IV_SIZE           = 16

# Wait up to 10 minutes — time for login + navigation
TIMEOUT_SEC = 600

_JS = """
'use strict';
var captured = false;

var mod = Process.findModuleByName('tp7runtime.exe');
if (!mod) {
    send({ type: 'error', msg: 'tp7runtime.exe module not found in process.' });
} else {
    var target = mod.base.add(0x34EB50);
    send({ type: 'info', msg: 'Hook armed at ' + target +
          ' (base ' + mod.base + ', RVA 0x34EB50)' });

    Interceptor.attach(target, {
        onEnter: function(args) {
            if (captured) return;
            captured = true;
            try {
                var eax = this.context.eax;
                var buf = ptr(eax).add(0x3C).readByteArray(16);
                send({ type: 'iv',
                       eax:   eax.toString(),
                       bytes: Array.from(new Uint8Array(buf)) });
            } catch(e) {
                send({ type: 'error', msg: 'Hook callback: ' + e.message });
            }
        }
    });
}
"""


def _find_tp7_pid():
    """Return PID of a running tp7runtime.exe, or None."""
    try:
        out = subprocess.check_output(
            ['powershell', '-NoProfile', '-Command',
             'Get-Process | Where-Object {$_.Name -eq "tp7runtime"} '
             '| Select-Object -First 1 -ExpandProperty Id'],
            stderr=subprocess.DEVNULL, text=True).strip()
        return int(out) if out else None
    except Exception:
        return None


def main():
    try:
        import frida
    except ImportError:
        print("ERROR: frida not installed.  Run:  pip install frida-tools")
        sys.exit(1)

    iv_found  = [None]
    pid_used  = [None]
    spawned   = [False]

    def on_message(message, data):
        if message['type'] == 'error':
            desc = message.get('description', str(message))
            print(f"\n[Frida error] {desc}")
            return
        p    = message.get('payload') or {}
        kind = p.get('type')
        if kind == 'info':
            print(f"[*] {p['msg']}")
        elif kind == 'error':
            print(f"[!] {p['msg']}")
        elif kind == 'iv':
            blist   = p['bytes']
            hex_str = ' '.join(f'{b:02x}' for b in blist)
            py_lit  = 'bytes([' + ', '.join(f'0x{b:02x}' for b in blist) + '])'
            print()
            print("=" * 54)
            print("  IV (block_buf) CAPTURED")
            print("=" * 54)
            print(f"  EAX (cipher obj) : {p['eax']}")
            print(f"  block_buf (IV)   : {hex_str}")
            print()
            print(f"  Python literal: {py_lit}")
            print("=" * 54)
            with open(IV_OUT, 'wb') as f:
                f.write(bytes(blist))
            print(f"\n  Saved → {IV_OUT}")
            print("  Next: python scripts/verify_iv.py")
            iv_found[0] = bytes(blist)

    # --- Find or spawn tp7runtime.exe ---
    existing_pid = _find_tp7_pid()

    if existing_pid:
        print(f"[*] Found running tp7runtime.exe  PID {existing_pid}")
        print("[*] Attaching (will not disturb your EVO session) ...")
        try:
            session = frida.attach(existing_pid)
        except Exception as e:
            print(f"[!] Attach failed: {e}")
            print("    Try running from an elevated (Administrator) prompt.")
            sys.exit(1)
        pid_used[0] = existing_pid
    else:
        print("[*] tp7runtime.exe is not running — spawning it now.")
        print(f"[*] EVO will open.  Log in and navigate to any module.")
        try:
            pid       = frida.spawn([TARGET_EXE, TARGET_RWN], cwd=r'C:\ISTS')
            session   = frida.attach(pid)
            spawned[0] = True
            pid_used[0] = pid
        except Exception as e:
            print(f"[!] Spawn failed: {e}")
            print("    Try running from an elevated (Administrator) prompt.")
            sys.exit(1)

    script = session.create_script(_JS)
    script.on('message', on_message)
    script.load()

    if spawned[0]:
        frida.resume(pid_used[0])

    print()
    print("Hook is ARMED.  Waiting for mode2_handler ...")
    print("  → If you attached to a running EVO: open any module now.")
    print("  → If EVO just launched: log in and open any module.")
    print(f"  → Timeout in {TIMEOUT_SEC//60} minutes.  Press Ctrl+C to abort.")
    print()

    deadline = time.time() + TIMEOUT_SEC
    try:
        while iv_found[0] is None and time.time() < deadline:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Aborted by user.")

    try:
        session.detach()
    except Exception:
        pass

    if iv_found[0] is None:
        remaining = max(0, int(deadline - time.time()))
        print(f"\n[!] Timeout: mode2_handler was not called within {TIMEOUT_SEC}s.")
        print("    Fallback: use scripts/x64dbg_get_iv.txt for manual extraction.")
        sys.exit(1)


if __name__ == '__main__':
    main()
