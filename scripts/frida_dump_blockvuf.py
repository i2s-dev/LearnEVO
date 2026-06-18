#!/usr/bin/env python3
"""
Frida script: hook mode2_handler (0x74EB50) the very first time it's called,
dump cipher+0x3C contents (the block_buf / P) before EncryptBlock, and
compare against IV_dcy and Encrypt(zeros).

This tells us definitively what P_initial is at validation time.
"""
import frida, sys, hashlib

# Known values
iv_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')

script_src = r"""
'use strict';

var mode2 = ptr('0x0074EB50');
var encryptblock = ptr('0x00750248');  // vtable[0x58]

var callCount = 0;
var encCallCount = 0;

// Hook mode2_handler entry to dump cipher+0x3C before first EncryptBlock
Interceptor.attach(mode2, {
    onEnter: function(args) {
        callCount++;
        // mode2_handler(cipher=EAX, count=[ebp+8], dst=[ebp-0xc], src=[ebp-8])
        // In Delphi/TAS fastcall, 1st param via EAX register
        // But we're hooking with Frida which gives us 'this.context'
        var eax = this.context.eax;  // cipher object
        var ecx = this.context.ecx;
        var edx = this.context.edx;

        try {
            // Read cipher+0x3C = pointer to block_buf (P)
            var p_ptr = Memory.readU32(eax.add(0x3c));
            var p_bytes = Memory.readByteArray(ptr(p_ptr), 16);

            // Read cipher+0x38 = buffer1
            var b1_ptr = Memory.readU32(eax.add(0x38));
            var b1_bytes = Memory.readByteArray(ptr(b1_ptr), 16);

            send({
                event: 'mode2_entry',
                call: callCount,
                cipher: eax.toString(),
                p_ptr: p_ptr.toString(16),
                p_bytes: Array.from(new Uint8Array(p_bytes)).map(x => x.toString(16).padStart(2,'0')).join(''),
                b1_ptr: b1_ptr.toString(16),
                b1_bytes: Array.from(new Uint8Array(b1_bytes)).map(x => x.toString(16).padStart(2,'0')).join(''),
            });
        } catch(e) {
            send({event: 'mode2_entry_error', call: callCount, err: e.toString()});
        }
    }
});

// Hook EncryptBlock to see what's being encrypted
Interceptor.attach(encryptblock, {
    onEnter: function(args) {
        encCallCount++;
        var eax = this.context.eax;   // cipher
        var ecx = this.context.ecx;   // dst
        var edx = this.context.edx;   // src

        if (encCallCount <= 5) {
            try {
                var src_bytes = Memory.readByteArray(ptr(edx.toInt32()), 16);
                send({
                    event: 'encrypt_block',
                    call: encCallCount,
                    src: Array.from(new Uint8Array(src_bytes)).map(x => x.toString(16).padStart(2,'0')).join(''),
                    src_ptr: edx.toString(),
                    dst_ptr: ecx.toString(),
                    cipher: eax.toString(),
                });
            } catch(e) {
                send({event: 'encrypt_block_error', call: encCallCount, err: e.toString()});
            }
        }
    }
});

send({event: 'ready', mode2: mode2.toString(), encryptblock: encryptblock.toString()});
"""

def on_message(msg, data):
    if msg['type'] == 'send':
        p = msg['payload']
        ev = p.get('event','')
        if ev == 'ready':
            print(f'[+] Hooks live: mode2={p["mode2"]}, encryptblock={p["encryptblock"]}')
        elif ev == 'mode2_entry':
            pb = bytes.fromhex(p['p_bytes'])
            b1 = bytes.fromhex(p['b1_bytes'])
            match_iv = '*** MATCHES IV_DCY!' if pb == iv_dcy else ''
            print(f'\n=== mode2_handler call #{p["call"]} ===')
            print(f'  cipher     = {p["cipher"]}')
            print(f'  P (0x3C→)  = {p["p_bytes"]}  {match_iv}')
            print(f'  b1 (0x38→) = {p["b1_bytes"]}')
        elif ev == 'mode2_entry_error':
            print(f'[!] mode2 error #{p["call"]}: {p["err"]}')
        elif ev == 'encrypt_block':
            print(f'  EncryptBlock #{p["call"]}: src={p["src"]}')
        elif ev == 'encrypt_block_error':
            print(f'[!] EncryptBlock error #{p["call"]}: {p["err"]}')
    elif msg['type'] == 'error':
        print(f'[ERROR] {msg["description"]}')

print('[*] Attaching to evoerp.exe ...')
try:
    session = frida.attach('evoerp.exe')
except frida.ProcessNotFoundError:
    print('[!] evoerp.exe not running. Launch EvoERP first, then re-run.')
    sys.exit(1)

script = session.create_script(script_src)
script.on('message', on_message)
script.load()
print('[*] Hooks loaded. Open a DCY-encrypted module in EvoERP to trigger.')
print('    Press Ctrl+C to stop.')
sys.stdin.read()
