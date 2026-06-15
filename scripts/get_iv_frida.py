#!/usr/bin/env python3
"""
scripts/get_iv_frida.py  (v5 -- hook EncryptBlock, filter by XOR constant)

WHY THIS APPROACH
  mode2_handler is called for BOTH .RWN and .DCY file decryption.
  .DCY files use a different IV than .RWN files, so hooking mode2_handler
  and reading block_buf captures whichever file type happened to load first.
  Earlier attempts captured a .DCY IV because the user opened a sub-screen
  that loaded a .DCY data-dictionary file, not a .RWN module program.

  This version hooks EncryptBlock (the Twofish ECB primitive called by
  mode2_handler).  After EncryptBlock executes in-place on block_buf, the
  output K = Encrypt(IV) is in memory.  We check K[0:4] XOR K[4:8]:

    - RWN validation: K[0:4]^K[4:8] = 0x3E0A37C5  (constant across all 20+ .RWN)
    - DCY / other:   different XOR value

  The first EncryptBlock call whose output satisfies the XOR constraint is
  the RWN validation decrypt.  IV = Decrypt(K) is computed in Python.

KEY ADDRESSES
  EncryptBlock   RVA 0x350248  file 0x34F648  VA(preferred) 0x750248
  mode2_handler  RVA 0x34EB50  file 0x34DF50  (still hooked for diagnostics)

USAGE
  1. EVO must be running (main menu visible -- no module windows needed).
  2. Run:  python scripts/get_iv_frida.py
     Wait for the "ARMED" banner.
  3. Open any module from the EVO main menu
     (Work Orders, Inventory, Sales Orders, AP, AR, GL, etc.).
     A NEW module window opens and decrypts its .RWN file -- this fires
     the hook with the correct K.
     -- OR --
     If a module window is already open, CLOSE it and REOPEN it.
  4. IV is saved to scripts/iv_bytes.bin.
  5. Run: python scripts/verify_iv.py

WHAT TO AVOID
  Do NOT open sub-menus WITHIN an already-open module before the IV is
  captured.  Sub-menu navigation loads .DCY files (data dictionaries)
  which have a different IV.  The hook will correctly ignore these (XOR
  filter), but the first RWN load is still needed.
"""

import sys
import os
import subprocess
import threading
import hashlib
import time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here   = os.path.dirname(os.path.abspath(__file__))
IV_OUT  = os.path.join(_here, 'iv_bytes.bin')

TIMEOUT_SEC   = 600
WATCH_NAMES   = ('evoerp', 'tp7runtime')
EXP_XOR       = 0x3E0A37C5   # K[0:4]^K[4:8] for any .RWN validation decrypt

# EncryptBlock: EAX=cipher, EDX=src (block_buf ptr), ECX=dst (same ptr, in-place)
# After return: memory at original EDX contains K = Encrypt(original block_buf)
_JS = r"""
'use strict';
var captured = false;
var EXP_XOR  = 0x3E0A37C5;

function le32(arr, off) {
    return ((arr[off] | (arr[off+1]<<8) | (arr[off+2]<<16) | (arr[off+3]<<24)) >>> 0);
}

function armEncryptBlock(modName) {
    var mod = Process.findModuleByName(modName);
    if (!mod) return false;

    // EncryptBlock RVA 0x350248
    var eb_target = mod.base.add(0x350248);
    send({ type: 'info', msg: 'EncryptBlock hook @ ' + eb_target +
           ' in ' + modName + ' (base=' + mod.base + ')' });

    Interceptor.attach(eb_target, {
        onEnter: function(args) {
            // Save src pointer (EDX) -- block_buf ptr, encrypted in-place
            this.src = this.context.edx;
        },
        onLeave: function(retval) {
            if (captured) return;
            try {
                // Memory at this.src now contains K = Encrypt(original_block_buf)
                var K = new Uint8Array(this.src.readByteArray(16));
                var xor4 = le32(K, 0) ^ le32(K, 4);
                if (xor4 !== EXP_XOR) return;   // not a .RWN validation decrypt
                captured = true;
                send({ type: 'K',
                       K:    Array.from(K),
                       xor4: xor4.toString(16) });
            } catch(e) {
                // pointer may have been freed -- ignore
            }
        }
    });
    return true;
}

armEncryptBlock('evoerp.exe') || armEncryptBlock('tp7runtime.exe');
"""

_WMI_PS = r"""
$names = @('evoerp.exe','tp7runtime.exe')
$q  = "SELECT * FROM __InstanceCreationEvent WITHIN 1 " +
      "WHERE TargetInstance ISA 'Win32_Process'"
$w  = New-Object System.Management.ManagementEventWatcher($q)
$w.Start()
while ($true) {
    try {
        $e = $w.WaitForNextEvent(5000)
        $p = $e.TargetInstance
        if ($names -contains $p.Name) {
            Write-Host "$($p.ProcessId)|$($p.ParentProcessId)|$($p.Name)"
            [Console]::Out.Flush()
        }
    } catch { }
}
"""


def _find_pids(name):
    try:
        out = subprocess.check_output(
            ['powershell', '-NoProfile', '-Command',
             f'Get-Process | Where-Object {{$_.Name -eq "{name}"}} '
             f'| Select-Object -ExpandProperty Id'],
            stderr=subprocess.DEVNULL, text=True).strip()
        return [int(x) for x in out.split() if x] if out else []
    except Exception:
        return []


def _all_evo_pids():
    result = {}
    for name in WATCH_NAMES:
        for pid in _find_pids(name):
            result[pid] = name
    return result


def main():
    try:
        import frida
    except ImportError:
        print("ERROR: frida not installed.  Run:  pip install frida-tools")
        sys.exit(1)

    iv_found  = [None]
    sessions  = []
    hooked    = set()

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
        elif kind == 'K':
            # K = Encrypt(IV).  Compute IV = Decrypt(K).
            K = bytes(p['K'])
            print()
            print("=" * 60)
            print("  EncryptBlock fired with XOR = 0x3E0A37C5 -- RWN IV!")
            print("=" * 60)
            print(f"  K = Encrypt(IV) : {K.hex(' ')}")

            # Compute IV = Decrypt(K) using twofish_pure
            import sys as _sys
            _sys.path.insert(0, _here)
            from twofish_pure import Twofish
            import struct
            _key = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4
            tf   = Twofish(_key)
            IV   = tf.decrypt(K)
            K2   = tf.encrypt(IV)
            xor4 = struct.unpack_from('<I',K2,0)[0] ^ struct.unpack_from('<I',K2,4)[0]

            print(f"  IV = Decrypt(K) : {IV.hex(' ')}")
            print(f"  Verify Enc(IV) XOR = 0x{xor4:08X}  (exp 0x{EXP_XOR:08X})")
            ok = (xor4 == EXP_XOR)
            print(f"  --> {'PASS -- IV is correct!' if ok else 'FAIL (false positive, retrying)'}")
            print("=" * 60)

            if ok:
                with open(IV_OUT, 'wb') as f:
                    f.write(IV)
                print(f"\n  Saved --> {IV_OUT}")
                print("  Next: python scripts/verify_iv.py")
                iv_found[0] = IV
            else:
                print("  (rare false positive; hook remains armed for next call)")

    device = frida.get_local_device()

    def hook_pid(pid, name):
        if pid in hooked:
            return
        hooked.add(pid)
        print(f"[*] Arming EncryptBlock hook in {name} PID {pid}")
        try:
            sess  = device.attach(pid)
            sc    = sess.create_script(_JS)
            sc.on('message', on_message)
            sc.load()
            sessions.append(sess)
        except Exception as e:
            print(f"    Attach failed for PID {pid}: {e}")

    def on_new_process(pid, ppid, name):
        print(f"\n[WMI] New {name} PID {pid}  PPID {ppid}")
        time.sleep(0.3)
        hook_pid(pid, name)

    existing = _all_evo_pids()
    if not existing:
        print("[!] No EVO process found.  Start EVO first.")
        sys.exit(1)

    for pid, name in existing.items():
        print(f"[*] Found {name}.exe PID {pid}")
        hook_pid(pid, name + '.exe')

    print("[*] Starting WMI process-creation monitor ...")
    wmi_th = threading.Thread(target=_wmi_thread, args=(on_new_process,), daemon=True)
    wmi_th.start()

    print()
    print("=" * 60)
    print("  ARMED.")
    print()
    print("  To capture the IV, open a MODULE from the EVO main menu.")
    print("  Examples: Work Orders, Inventory, Sales Orders, AP, AR.")
    print()
    print("  Any module window opening decrypts a .RWN file --")
    print("  this fires EncryptBlock with the RWN IV.")
    print()
    print("  If a module is already open: CLOSE it and REOPEN it.")
    print()
    print(f"  Timeout: {TIMEOUT_SEC // 60} min.  Ctrl+C to abort.")
    print("=" * 60)
    print()

    deadline = time.time() + TIMEOUT_SEC
    try:
        while iv_found[0] is None and time.time() < deadline:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Aborted.")

    for sess in sessions:
        try:
            sess.detach()
        except Exception:
            pass

    if iv_found[0] is None:
        print(f"\n[!] Timeout: EncryptBlock with XOR=0x3E0A37C5 not seen.")
        print("    Make sure a new .RWN module window was opened (not a sub-screen).")
        print("    Fallback: scripts/x64dbg_get_iv.txt")
        sys.exit(1)


def _wmi_thread(callback):
    proc = subprocess.Popen(
        ['powershell', '-NoProfile', '-Command', _WMI_PS],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
    )
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        line = line.strip()
        if '|' in line:
            parts = line.split('|', 2)
            try:
                callback(int(parts[0]), int(parts[1]),
                         parts[2] if len(parts) > 2 else '?')
            except ValueError:
                pass


if __name__ == '__main__':
    main()
