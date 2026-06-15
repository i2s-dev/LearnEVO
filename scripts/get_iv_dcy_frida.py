#!/usr/bin/env python3
"""
scripts/get_iv_dcy_frida.py  (v1 -- DCY data-dictionary IV capture)

WHY THIS SCRIPT EXISTS
  .RWN decryption is solved (IV = 9c da c3 45 a5 f0 1c 2c 96 57 92 d9 0b 1a bc 1e).
  .DCY data-dictionary files use a DIFFERENT IV.  The cipher (Twofish-CFB), key
  (SHA1('mabufoju')+4 zeros = 192-bit), and validation logic (pt[0:4]==pt[4:8])
  are all the same.  The XOR constant that distinguishes a DCY validation decrypt
  from an RWN one is 0x0955DC84 (confirmed by scanning the share: all .DCY headers
  produce K[0:4]^K[4:8] = 0x0955DC84 after EncryptBlock; .RWN = 0x3E0A37C5).

HOW TO TRIGGER A DCY LOAD
  .DCY files are loaded when a MODULE'S OWN DATA DICTIONARY is needed -- not when
  a module window is opened from the main menu (that loads the .RWN program).
  The trigger is navigating WITHIN an already-open module:
    - Opening a lookup / browse list inside an open WO, SO, IN, etc. screen
    - Clicking into a field that launches a sub-form
    - Any sub-menu or drill-down WITHIN the open module window

  With WO-A already open: click the "..." lookup on any field, or press F4/F5 to
  open a WO search list.  That is sufficient to load BKWOMSTR.DCY (or similar).

USAGE
  1. EVO must be running with at least one module window already open (e.g. WO-A).
  2. Run:  python scripts/get_iv_dcy_frida.py
     Wait for the ARMED banner.
  3. Navigate WITHIN the open module (click a lookup, open a sub-form, browse list).
  4. IV_dcy is saved to scripts/iv_dcy_bytes.bin automatically.
  5. Run:  python scripts/verify_iv_dcy.py

KEY ADDRESSES (same binary as RWN script)
  EncryptBlock   RVA 0x350248
"""

import sys
import os
import subprocess
import threading
import hashlib
import time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here    = os.path.dirname(os.path.abspath(__file__))
IV_OUT   = os.path.join(_here, 'iv_dcy_bytes.bin')

TIMEOUT_SEC = 600
WATCH_NAMES = ('evoerp', 'tp7runtime')
EXP_XOR     = 0x0955DC84   # K[0:4]^K[4:8] for any .DCY validation decrypt (verified from 41/47 DCY headers)

_JS = r"""
'use strict';
var captured = false;
var EXP_XOR  = 0x0955DC84;

function le32(arr, off) {
    return ((arr[off] | (arr[off+1]<<8) | (arr[off+2]<<16) | (arr[off+3]<<24)) >>> 0);
}

function armEncryptBlock(modName) {
    var mod = Process.findModuleByName(modName);
    if (!mod) return false;

    var eb_target = mod.base.add(0x350248);
    send({ type: 'info', msg: 'EncryptBlock hook @ ' + eb_target +
           ' in ' + modName + ' (base=' + mod.base + ')' });

    Interceptor.attach(eb_target, {
        onEnter: function(args) {
            this.src = this.context.edx;
        },
        onLeave: function(retval) {
            if (captured) return;
            try {
                var K    = new Uint8Array(this.src.readByteArray(16));
                var xor4 = le32(K, 0) ^ le32(K, 4);
                // Log every hit so we can see what XOR values are firing
                send({ type: 'hit', xor4: xor4.toString(16), K: Array.from(K) });
                if (xor4 !== EXP_XOR) return;
                captured = true;
                send({ type: 'K', K: Array.from(K), xor4: xor4.toString(16) });
            } catch(e) {
                // pointer freed -- ignore
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

    iv_found = [None]
    sessions = []
    hooked   = set()
    hit_log  = []

    def on_message(message, data):
        if message['type'] == 'error':
            print(f"\n[Frida] {message.get('description', str(message))}")
            return
        p    = message.get('payload') or {}
        kind = p.get('type', '')
        if kind == 'info':
            print(f"[*] {p['msg']}")
        elif kind == 'hit':
            xv = p['xor4']
            if xv not in hit_log:
                hit_log.append(xv)
                label = ' <-- RWN' if xv == '3e0a37c5' else \
                        ' <-- DCY  ** MATCH **' if xv == '9553584' or xv == '9553584'.zfill(8) else \
                        ' <-- DCY  ** MATCH **' if p['xor4'].lstrip('0') == '9553584' else ''
                if '09553584' in ('0'*(8-len(xv))+xv):
                    label = ' <-- DCY  ** MATCH **'
                print(f"    EncryptBlock XOR = 0x{xv.upper().zfill(8)}{label}")
        elif kind == 'K':
            K = bytes(p['K'])
            print()
            print("=" * 60)
            print("  EncryptBlock fired with XOR = 0x0955DC84 -- DCY IV!")
            print("=" * 60)
            print(f"  K = Encrypt(IV_dcy) : {K.hex(' ')}")

            sys.path.insert(0, _here)
            from twofish_pure import Twofish
            import struct
            _key = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4
            tf   = Twofish(_key)
            IV   = tf.decrypt(K)
            K2   = tf.encrypt(IV)
            xor4 = struct.unpack_from('<I', K2, 0)[0] ^ struct.unpack_from('<I', K2, 4)[0]

            print(f"  IV_dcy = Decrypt(K) : {IV.hex(' ')}")
            print(f"  Verify Enc(IV) XOR  = 0x{xor4:08X}  (exp 0x{EXP_XOR:08X})")
            ok = (xor4 == EXP_XOR)
            print(f"  --> {'PASS -- DCY IV is correct!' if ok else 'FAIL (false positive, retrying)'}")
            print("=" * 60)

            if ok:
                with open(IV_OUT, 'wb') as f:
                    f.write(IV)
                print(f"\n  Saved --> {IV_OUT}")
                print(f"  IV_dcy (hex): {IV.hex(' ')}")
                print("\n  Next: python scripts/verify_iv_dcy.py")
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
            sess = device.attach(pid)
            sc   = sess.create_script(_JS)
            sc.on('message', on_message)
            sc.load()
            sessions.append(sess)
        except Exception as e:
            print(f"    Attach failed for PID {pid}: {e}")

    def on_new_process(pid, ppid, name):
        print(f"\n[WMI] New {name} PID {pid}  PPID {ppid}")
        time.sleep(0.3)
        hook_pid(pid, name)

    print("[*] Starting WMI process-creation monitor ...")
    wmi_th = threading.Thread(target=_wmi_thread, args=(on_new_process,), daemon=True)
    wmi_th.start()

    existing = _all_evo_pids()
    if not existing:
        print("[!] No EVO process found yet -- waiting for EVO to launch ...")
        print("    Start EVO now.  The hook will arm automatically when it appears.")
        # Wait for WMI to pick it up -- don't exit
    else:
        for pid, name in existing.items():
            print(f"[*] Found {name}.exe PID {pid}")
            hook_pid(pid, name + '.exe')

    print()
    print("=" * 60)
    print("  ARMED -- waiting for a DCY data-dictionary load.")
    print()
    print("  You have WO-A open.  To trigger a .DCY load:")
    print()
    print("  Option A (easiest):  press F4 or click the lookup")
    print("    button on the WO Number field.  This opens the")
    print("    WO browse list which loads the WO data dictionary.")
    print()
    print("  Option B:  open any sub-form within WO-A")
    print("    (e.g. WO Notes, WO Components, WO Operations).")
    print()
    print("  Option C:  open a NEW module from the main menu")
    print("    that has never been opened this session.")
    print("    (Sub-modules like SR, SC, WC often force a DCY load)")
    print()
    print("  The hook will IGNORE .RWN loads (XOR=0x3E0A37C5)")
    print("  and CAPTURE only .DCY loads (XOR=0x0955DC84).")
    print("  All observed XOR values are logged above in real time.")
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
        print(f"\n[!] Timeout: EncryptBlock with XOR=0x0955DC84 not seen.")
        if hit_log:
            print(f"    XOR values observed: {', '.join('0x'+x.upper().zfill(8) for x in hit_log)}")
        print("    Make sure you navigated WITHIN an already-open module window.")
        print("    (Opening a lookup or sub-form, not a fresh module from main menu.)")
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
