#!/usr/bin/env python3
"""
scripts/get_iv_frida.py  (v3 -- child gating)

WHY THIS APPROACH
  Previous attempts to spawn tp7runtime.exe directly failed: the process
  fires the Twofish constructor 3 times (TAS runtime init) but exits via a
  single-instance check BEFORE loading any .RWN file, so mode2_handler
  never fires.

  Child gating solves this: we attach to the *already-running* evoerp.exe
  and ask Frida to pause every child process it spawns.  When the user
  closes a module window (WO-A, etc.) and reopens it, evoerp.exe calls
  CreateProcess to start a new tp7runtime.exe.  Frida pauses that child
  before it executes a single instruction, we inject the mode2_handler
  hook, then resume it.  The hook fires when the child decrypts its
  module .RWN file -- capturing the initial block_buf (= IV).

USAGE
  1. Make sure EVO is running normally (evoerp.exe + at least one module
     window like WO-A).
  2. Run:  python scripts/get_iv_frida.py
  3. In EVO, close a module window (e.g. WO-A).
  4. Reopen that module from the EVO menu.
  5. The hook fires and writes scripts/iv_bytes.bin.
  6. Run:  python scripts/verify_iv.py

KEY ADDRESSES (tp7runtime.exe / evoerp.exe -- byte-for-byte identical)
  mode2_handler   RVA 0x34EB50  file 0x34DF50
  block_buf       cipher+0x3C   16-byte inline array (initial IV)
  mode byte       cipher+0x34   set to 2 (CFB) by validate_func

NOTE ON block_buf
  block_buf is a 16-byte inline array inside the TDCP_blockcipher object at
  object_offset 0x3C.  It is allocated by GetMem but never zeroed, so its
  initial value is heap garbage that is deterministic on this installation
  (proven by all .RWN files sharing ct[0:4]^ct[4:8] = 0x3E0A37C5, meaning
  every compiled .RWN used the same IV at compile time and that IV recurs
  at runtime when the same process startup conditions are met).

  IMPORTANT: .DCY and .RWN files use DIFFERENT IVs.  Do not attempt to
  derive the .RWN IV from MDUMMY.DCY/DFM analysis -- that path is a dead
  end (verified exhaustively; see BROKEN.md).
"""

import sys
import os
import subprocess
import time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here  = os.path.dirname(os.path.abspath(__file__))
IV_OUT = os.path.join(_here, 'iv_bytes.bin')

TIMEOUT_SEC = 600  # 10 minutes

_JS = r"""
'use strict';
var captured = false;

function armHook(modName) {
    var mod = Process.findModuleByName(modName);
    if (!mod) return false;

    var target = mod.base.add(0x34EB50);
    send({ type: 'info',
           msg: 'hook armed in ' + modName + ' @ ' + target +
                ' (base=' + mod.base + ')' });

    Interceptor.attach(target, {
        onEnter: function(args) {
            if (captured) return;
            captured = true;
            try {
                var eax = this.context.eax;

                // block_buf is a 16-byte inline array at cipher+0x3C.
                var buf = ptr(eax).add(0x3C).readByteArray(16);
                var iv_arr = Array.from(new Uint8Array(buf));

                // Also attempt pointer dereference in case this build
                // uses a dynamic array at that field.
                var u32 = ptr(eax).add(0x3C).readU32();
                var deref = null;
                try {
                    if (u32 > 0x10000 && u32 < 0x7fff0000) {
                        deref = Array.from(
                            new Uint8Array(ptr(u32).readByteArray(16)));
                    }
                } catch(e2) {}

                send({
                    type:    'iv',
                    eax:     eax.toString(),
                    ptr_val: u32.toString(16),
                    direct:  iv_arr,
                    deref:   deref
                });
            } catch(e) {
                send({ type: 'error', msg: 'onEnter: ' + e.message });
            }
        }
    });
    return true;
}

// The main process may be evoerp.exe; children are tp7runtime.exe.
armHook('evoerp.exe') || armHook('tp7runtime.exe');
"""


def _find_pids(name):
    """Return list of PIDs matching the given process name (no .exe)."""
    try:
        out = subprocess.check_output(
            ['powershell', '-NoProfile', '-Command',
             f'Get-Process | Where-Object {{$_.Name -eq "{name}"}} '
             f'| Select-Object -ExpandProperty Id'],
            stderr=subprocess.DEVNULL, text=True).strip()
        return [int(x) for x in out.split() if x] if out else []
    except Exception:
        return []


def main():
    try:
        import frida
    except ImportError:
        print("ERROR: frida not installed.  Run:  pip install frida-tools")
        sys.exit(1)

    iv_found  = [None]
    sessions  = []

    def on_message(message, data):
        if message['type'] == 'error':
            print(f"\n[Frida] {message.get('description', str(message))}")
            return
        p    = message.get('payload') or {}
        kind = p.get('type', '')
        if kind == 'info':
            print(f"[*] {p['msg']}")
        elif kind == 'error':
            print(f"[!] {p['msg']}")
        elif kind == 'iv':
            d16  = bytes(p['direct'])
            dr16 = bytes(p['deref']) if p.get('deref') else None
            print()
            print("=" * 60)
            print("  mode2_handler FIRED -- IV CAPTURED")
            print("=" * 60)
            print(f"  EAX (cipher obj) : {p['eax']}")
            print(f"  cipher+0x3C u32  : 0x{p['ptr_val']}")
            print(f"  direct [0:16]    : {d16.hex(' ')}")
            if dr16:
                print(f"  deref  [0:16]    : {dr16.hex(' ')}")
            print("=" * 60)
            with open(IV_OUT, 'wb') as f:
                f.write(d16)
            print(f"\n  Saved direct --> {IV_OUT}")
            if dr16:
                dr_path = IV_OUT.replace('.bin', '_deref.bin')
                with open(dr_path, 'wb') as f:
                    f.write(dr16)
                print(f"  Saved deref  --> {dr_path}")
            print("  Next: python scripts/verify_iv.py")
            iv_found[0] = d16

    device = frida.get_local_device()

    # Arm hook on each existing tp7runtime.exe child process.
    # These won't re-fire mode2_handler for .RWN files already loaded,
    # but will catch any future dynamic .RWN loads in those processes.
    for pid in _find_pids('tp7runtime'):
        print(f"[*] Arming on existing tp7runtime.exe PID {pid}")
        try:
            sess = device.attach(pid)
            sc   = sess.create_script(_JS)
            sc.on('message', on_message)
            sc.load()
            sessions.append(sess)
        except Exception as e:
            print(f"    Could not attach to PID {pid}: {e}")

    # Enable child gating on evoerp.exe.
    evo_pids = _find_pids('evoerp')
    if not evo_pids:
        print("[!] evoerp.exe not found.  Start EVO first, then run this script.")
        sys.exit(1)

    evo_pid = evo_pids[0]
    print(f"[*] Attaching to evoerp.exe PID {evo_pid} for child gating ...")
    try:
        evo_sess = device.attach(evo_pid)
        evo_sess.enable_child_gating()
        sessions.append(evo_sess)
        print("[*] Child gating ENABLED on evoerp.exe")
    except Exception as e:
        print(f"[!] Child gating failed: {e}")
        print("    Try running from an elevated (Administrator) prompt.")

    def on_child_added(child):
        print(f"\n[*] Child spawned: PID {child.pid}  ({child.path})")
        try:
            ch_sess = device.attach(child.pid)
            sc      = ch_sess.create_script(_JS)
            sc.on('message', on_message)
            sc.load()
            sessions.append(ch_sess)
            print(f"[*] Hook armed in child PID {child.pid}")
        except Exception as e:
            print(f"[!] Child hook failed for PID {child.pid}: {e}")
        finally:
            try:
                device.resume(child.pid)
            except Exception:
                pass

    device.on('child-added', on_child_added)

    print()
    print("ARMED.  Steps to capture the IV:")
    print("  1. In EVO, CLOSE a module window (WO-A, WO-B, WO-C, etc.).")
    print("  2. Reopen that same module from the EVO main menu.")
    print("  3. Frida pauses the new tp7runtime.exe child before any code runs,")
    print("     injects the hook, then resumes it.")
    print("  4. mode2_handler fires when the module .RWN is decrypted.")
    print(f"  Timeout: {TIMEOUT_SEC // 60} min.  Ctrl+C to abort.")
    print()

    deadline = time.time() + TIMEOUT_SEC
    try:
        while iv_found[0] is None and time.time() < deadline:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Aborted by user.")

    device.off('child-added', on_child_added)
    for sess in sessions:
        try:
            sess.detach()
        except Exception:
            pass

    if iv_found[0] is None:
        print(f"\n[!] Timeout: mode2_handler did not fire within {TIMEOUT_SEC}s.")
        print("    Fallback: use scripts/x64dbg_get_iv.txt for manual extraction.")
        sys.exit(1)


if __name__ == '__main__':
    main()
