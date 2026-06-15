#!/usr/bin/env python3
"""
scripts/get_iv_frida.py  (v4 -- WMI process-creation monitor)

WHY THIS APPROACH
  Child gating on evoerp.exe failed because the module windows are NOT
  spawned as tp7runtime.exe children -- they spawn as additional evoerp.exe
  processes (or via a mechanism Frida's child gating does not intercept).

  This version uses a PowerShell WMI __InstanceCreationEvent watcher running
  in a background thread.  When any new evoerp.exe or tp7runtime.exe process
  appears, it is detected within ~1 second and Frida attaches to it
  immediately -- well before mode2_handler fires (~several seconds in).

USAGE
  1. Make sure EVO is running (main menu visible).
  2. Run:  python scripts/get_iv_frida.py
     Wait for the "ARMED" banner.
  3. Open any module from the EVO main menu (Work Orders, Inventory, etc.).
     A new process window will open; the hook fires when it decrypts its RWN.
     -- OR --
     Navigate within an already-open module to any sub-screen.  Each
     sub-screen load triggers mode2_handler in the same process.
  4. IV is saved to scripts/iv_bytes.bin.
  5. Run: python scripts/verify_iv.py

KEY ADDRESSES
  mode2_handler  RVA 0x34EB50  (same in evoerp.exe and tp7runtime.exe)
  block_buf      cipher+0x3C   16-byte inline array (initial IV)

PROCESS NAMES TO WATCH
  evoerp.exe    -- main EVO process AND module sub-windows
  tp7runtime.exe -- alternative name for same binary; some installs use it
"""

import sys
import os
import subprocess
import threading
import time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here   = os.path.dirname(os.path.abspath(__file__))
IV_OUT  = os.path.join(_here, 'iv_bytes.bin')

TIMEOUT_SEC   = 600   # 10 minutes
WATCH_NAMES   = ('evoerp', 'tp7runtime')   # without .exe

_JS = r"""
'use strict';
var captured = false;

function armHook(modName) {
    var mod = Process.findModuleByName(modName);
    if (!mod) return false;

    var target = mod.base.add(0x34EB50);
    send({ type: 'info',
           msg: 'hook armed in ' + modName + ' (PID ' + Process.id + ') @ ' + target });

    Interceptor.attach(target, {
        onEnter: function(args) {
            if (captured) return;
            captured = true;
            try {
                var eax = this.context.eax;
                // block_buf: 16-byte inline array at cipher+0x3C
                var iv_bytes = Array.from(
                    new Uint8Array(ptr(eax).add(0x3C).readByteArray(16)));
                // Also read raw u32 for dereference diagnostic
                var u32 = ptr(eax).add(0x3C).readU32();
                var deref = null;
                try {
                    if (u32 > 0x10000 && u32 < 0x7fff0000) {
                        deref = Array.from(
                            new Uint8Array(ptr(u32).readByteArray(16)));
                    }
                } catch(e2) {}
                send({ type: 'iv', pid: Process.id, eax: eax.toString(),
                       ptr_val: u32.toString(16),
                       direct: iv_bytes, deref: deref });
            } catch(e) {
                send({ type: 'error', msg: 'onEnter: ' + e.message });
            }
        }
    });
    return true;
}

armHook('evoerp.exe') || armHook('tp7runtime.exe');
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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
    pids = {}
    for name in WATCH_NAMES:
        for pid in _find_pids(name):
            pids[pid] = name
    return pids


def _attach_and_hook(pid, name, on_message_fn):
    """Attach Frida to pid and arm the mode2_handler hook."""
    import frida
    try:
        sess  = frida.attach(pid)
        sc    = sess.create_script(_JS)
        sc.on('message', on_message_fn)
        sc.load()
        print(f"[*] Hook armed in {name} PID {pid}")
        return sess
    except Exception as e:
        print(f"[!] Could not hook PID {pid} ({name}): {e}")
        return None


# ---------------------------------------------------------------------------
# WMI monitor -- runs in a background thread
# ---------------------------------------------------------------------------

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
                pid  = int(parts[0])
                ppid = int(parts[1])
                name = parts[2] if len(parts) > 2 else '?'
                callback(pid, ppid, name)
            except ValueError:
                pass


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    try:
        import frida
    except ImportError:
        print("ERROR: frida not installed.  Run:  pip install frida-tools")
        sys.exit(1)

    iv_found = [None]
    sessions = []
    hooked   = set()

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
            print(f"  PID (caught in) : {p['pid']}")
            print(f"  EAX cipher obj  : {p['eax']}")
            print(f"  cipher+0x3C u32 : 0x{p['ptr_val']}")
            print(f"  direct [0:16]   : {d16.hex(' ')}")
            if dr16:
                print(f"  deref  [0:16]   : {dr16.hex(' ')}")
            print("=" * 60)
            with open(IV_OUT, 'wb') as f:
                f.write(d16)
            print(f"\n  Saved direct --> {IV_OUT}")
            if dr16:
                dp = IV_OUT.replace('.bin', '_deref.bin')
                with open(dp, 'wb') as f:
                    f.write(dr16)
                print(f"  Saved deref  --> {dp}")
            print("  Next: python scripts/verify_iv.py")
            iv_found[0] = d16

    def hook_pid(pid, name):
        if pid in hooked:
            return
        hooked.add(pid)
        print(f"[*] New process detected: {name} PID {pid}")
        # Small delay to let the process finish loading its own DLLs
        time.sleep(0.2)
        sess = _attach_and_hook(pid, name, on_message)
        if sess:
            sessions.append(sess)

    def on_new_process(pid, ppid, name):
        print(f"\n[WMI] New {name} spotted: PID {pid}  PPID {ppid}")
        hook_pid(pid, name)

    # --- Arm on all already-running EVO processes ---
    existing = _all_evo_pids()
    if not existing:
        print("[!] No evoerp.exe or tp7runtime.exe found.")
        print("    Start EVO, then run this script.")
        sys.exit(1)

    for pid, name in existing.items():
        print(f"[*] Found existing {name}.exe PID {pid}")
        hook_pid(pid, name + '.exe')

    # --- Start WMI watcher for NEW processes ---
    print("[*] Starting WMI process-creation monitor ...")
    wmi_th = threading.Thread(target=_wmi_thread,
                              args=(on_new_process,), daemon=True)
    wmi_th.start()

    print()
    print("=" * 60)
    print("  ARMED.  Two ways to trigger the capture:")
    print()
    print("  A) Open any module from the EVO main menu")
    print("     (Work Orders, Inventory, Sales Orders, etc.)")
    print("     The new process that appears will be hooked.")
    print()
    print("  B) In an already-open module, navigate to any")
    print("     sub-screen (open a work order, drill into a")
    print("     record, open an entry form, etc.).")
    print("     That loads a new .RWN in the same process.")
    print()
    print(f"  Timeout: {TIMEOUT_SEC // 60} min.  Ctrl+C to abort.")
    print("=" * 60)
    print()

    deadline = time.time() + TIMEOUT_SEC
    try:
        while iv_found[0] is None and time.time() < deadline:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Aborted by user.")

    for sess in sessions:
        try:
            sess.detach()
        except Exception:
            pass

    if iv_found[0] is None:
        print(f"\n[!] Timeout: mode2_handler did not fire within {TIMEOUT_SEC}s.")
        print("    Fallback: see scripts/x64dbg_get_iv.txt")
        sys.exit(1)


if __name__ == '__main__':
    main()
