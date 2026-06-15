#!/usr/bin/env python3
"""
scripts/get_iv_dcy_spawn.py

Spawns evoerp.exe via Frida (process starts SUSPENDED), installs the
EncryptBlock hook BEFORE the first instruction runs, then resumes.
This guarantees we catch the very first DCY validation decrypt at startup,
before any caching can hide it.

USAGE
  1. Close EVO completely first.
  2. Run:  python scripts/get_iv_dcy_spawn.py
  3. EVO will open automatically.  Wait until the main menu appears.
  4. When the DCY block fires, IV is saved to scripts/iv_dcy_bytes.bin.
  5. Optionally open a module to confirm (RWN XOR will also be logged).
"""

import sys, os, hashlib, time, struct

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here  = os.path.dirname(os.path.abspath(__file__))
IV_OUT = os.path.join(_here, 'iv_dcy_bytes.bin')
EVO    = r'C:\ISTS\evoerp.exe'

EXP_XOR_DCY = 0x0955DC84
EXP_XOR_RWN = 0x3E0A37C5

_JS = r"""
'use strict';
var captured = false;

function le32(arr, off) {
    return ((arr[off] | (arr[off+1]<<8) | (arr[off+2]<<16) | (arr[off+3]<<24)) >>> 0);
}

function arm(mod) {
    if (!mod) { send({type:'err', msg:'Module not found'}); return; }
    var target = mod.base.add(0x350248);
    send({type:'info', msg:'Hook @ ' + target + '  base=' + mod.base});

    Interceptor.attach(target, {
        onEnter: function(args) { this.src = this.context.edx; },
        onLeave: function(retval) {
            try {
                var K    = new Uint8Array(this.src.readByteArray(16));
                var xor4 = (le32(K,0) ^ le32(K,4)) >>> 0;
                send({type:'hit', xor4: xor4});
                if (!captured && xor4 === 0x0955DC84) {
                    captured = true;
                    send({type:'K_dcy', K: Array.from(K)});
                }
            } catch(e) {}
        }
    });
}

// Spawn path: module is the main executable
arm(Process.enumerateModules()[0]);
"""

def main():
    try:
        import frida
    except ImportError:
        print("ERROR: pip install frida-tools")
        sys.exit(1)

    device   = frida.get_local_device()
    iv_found = [None]
    seen_xor = set()

    def on_msg(msg, data):
        if msg['type'] == 'error':
            print(f"[Frida] {msg.get('description','?')}")
            return
        p = msg.get('payload') or {}
        t = p.get('type','')

        if t == 'info':
            print(f"[*] {p['msg']}")

        elif t == 'hit':
            xv = p['xor4']
            if xv not in seen_xor:
                seen_xor.add(xv)
                tag = ''
                if xv == EXP_XOR_RWN: tag = '  <-- RWN (ignored)'
                elif xv == EXP_XOR_DCY: tag = '  <-- DCY *** MATCH ***'
                print(f"    XOR = 0x{xv:08X}{tag}")

        elif t == 'K_dcy':
            K = bytes(p['K'])
            print()
            print("=" * 60)
            print("  DCY VALIDATION BLOCK CAPTURED")
            print(f"  K = Encrypt(IV_dcy) : {K.hex(' ')}")

            sys.path.insert(0, _here)
            from twofish_pure import Twofish
            key = hashlib.sha1(b'mabufoju').digest() + b'\x00\x00\x00\x00'
            tf  = Twofish(key)
            IV  = tf.decrypt(K)
            K2  = tf.encrypt(IV)
            x2  = struct.unpack_from('<I',K2,0)[0] ^ struct.unpack_from('<I',K2,4)[0]

            print(f"  IV_dcy = Decrypt(K) : {IV.hex(' ')}")
            print(f"  Verify XOR          : 0x{x2:08X}  (exp 0x{EXP_XOR_DCY:08X})")
            ok = (x2 == EXP_XOR_DCY)
            print(f"  --> {'PASS' if ok else 'FAIL'}")
            print("=" * 60)

            if ok:
                with open(IV_OUT, 'wb') as f: f.write(IV)
                print(f"\n  Saved --> {IV_OUT}")
                iv_found[0] = IV
            else:
                print("  False positive; waiting for next DCY block...")

    print(f"[*] Spawning {EVO} (suspended) ...")
    try:
        pid = device.spawn([EVO])
    except Exception as e:
        print(f"ERROR spawning: {e}")
        print("Make sure EVO is fully closed first.")
        sys.exit(1)

    print(f"[*] PID {pid} -- attaching before resume ...")
    sess   = device.attach(pid)
    script = sess.create_script(_JS)
    script.on('message', on_msg)
    script.load()

    print(f"[*] Hook installed -- resuming EVO ...")
    device.resume(pid)
    print()
    print("=" * 60)
    print("  EVO is starting.  Wait for the main menu.")
    print("  DCY files load during startup -- no action needed.")
    print("  Once captured, open any module to confirm RWN XOR too.")
    print(f"  Timeout: 5 min.  Ctrl+C to abort.")
    print("=" * 60)
    print()

    deadline = time.time() + 300
    try:
        while iv_found[0] is None and time.time() < deadline:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Aborted.")

    if iv_found[0] is None:
        xors = ', '.join(f'0x{x:08X}' for x in sorted(seen_xor))
        print(f"\n[!] Timeout.  XOR values seen: {xors or 'none'}")
        print("    DCY validation block was not observed.")
        print("    DCY may use a different code path than RWN.")
    else:
        print("\n[*] Done.  Run: python scripts/verify_iv_dcy.py")

    try: sess.detach()
    except: pass


if __name__ == '__main__':
    main()
