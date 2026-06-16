#!/usr/bin/env python3
"""
Capture the three unknowns needed to crack DCY body decryption.
Dynamically resolves evoerp.exe runtime base — works regardless of ASLR/relocation.

USAGE:
  1. Run this script first (it polls for the process)
  2. Launch EvoERP — script auto-attaches within 200ms
  3. Log in, open any module screen
  4. Ctrl+C to stop
"""
import frida, sys, time, hashlib

PROC_NAME = 'evoerp.exe'
PREFERRED_BASE = 0x400000   # evoerp.exe preferred ImageBase (from PE header)

# Static VAs at preferred base — runtime VAs = these + reloc_delta
SETKEY_VA    = 0x0074F8A4
MODE2_VA     = 0x0074EB50
ENCBLOCK_VA  = 0x00750248
CINIT_VA     = 0x0074E1F8

script_template = """
'use strict';

// Address computation: use module.base.add(RVA) — the ONLY pattern that works reliably.
// Never use ptr() on NativePointers; never use Memory.readU8/readU32.
var mod = Process.findModuleByName('evoerp.exe');
var SETKEY_RVA   = {setkey}   - {preferred};
var MODE2_RVA    = {mode2}    - {preferred};
var ENCBLOCK_RVA = {encblock} - {preferred};
var SETKEY   = mod.base.add(SETKEY_RVA);
var MODE2    = mod.base.add(MODE2_RVA);
var ENCBLOCK = mod.base.add(ENCBLOCK_RVA);

send({{event:'addrs',
      base:    mod.base.toString(),
      setkey:  SETKEY.toString(),
      mode2:   MODE2.toString(),
      encblock:ENCBLOCK.toString()}});

function bytesToHex(arr) {{
    var s = '';
    for (var i = 0; i < arr.length; i++) {{
        s += (arr[i] < 16 ? '0' : '') + arr[i].toString(16);
    }}
    return s;
}}

var setkeyCalls = 0, mode2Calls = 0, encCalls = 0;

// SetKey(EAX=cipher, EDX=key_buf, ECX=key_bits_int; [ESP+4]=iv_param)
Interceptor.attach(SETKEY, {{
    onEnter: function(args) {{
        try {{
            setkeyCalls++;
            // Read key bytes from buffer pointed to by EDX
            var key_arr = Array.from(new Uint8Array(this.context.edx.readByteArray(24)));
            // Read key_bits from ECX (integer register value)
            var key_bits = this.context.ecx.toInt32();
            // Read IV param from stack: ESP is top-of-stack (return addr), ESP+4 is first arg
            var iv_param = this.context.esp.add(4).readU32();
            send({{event:'setkey', call:setkeyCalls,
                   key_bits:key_bits, key_arr:key_arr, iv_param:iv_param}});
        }} catch(e) {{ send({{event:'err', where:'setkey', msg:e.toString()}}); }}
    }}
}});

// mode2_handler(EAX=cipher, ...)
Interceptor.attach(MODE2, {{
    onEnter: function(args) {{
        try {{
            mode2Calls++;
            if (mode2Calls > 6) return;
            // cipher+0x3C = pointer to P (block_buf); cipher+0x38 = pointer to buffer1
            var p_ptr  = this.context.eax.add(0x3c).readU32();
            var b1_ptr = this.context.eax.add(0x38).readU32();
            var p_arr  = Array.from(new Uint8Array(ptr(p_ptr).readByteArray(16)));
            var b1_arr = Array.from(new Uint8Array(ptr(b1_ptr).readByteArray(16)));
            send({{event:'mode2', call:mode2Calls, P:p_arr, buffer1:b1_arr}});
        }} catch(e) {{ send({{event:'err', where:'mode2', msg:e.toString()}}); }}
    }}
}});

// EncryptBlock(EAX=cipher, EDX=src/dst, ECX=dst) -- operates in-place on EDX buffer
// Read AFTER return (onLeave) so we see the encrypted output, not the plaintext input.
Interceptor.attach(ENCBLOCK, {{
    onEnter: function(args) {{
        this.src = this.context.edx;   // save NativePointer for onLeave
    }},
    onLeave: function(retval) {{
        try {{
            encCalls++;
            if (encCalls > 8) return;
            var out_arr = Array.from(new Uint8Array(this.src.readByteArray(16)));
            send({{event:'encrypt', call:encCalls, out:out_arr}});
        }} catch(e) {{ send({{event:'err', where:'encrypt', msg:e.toString()}}); }}
    }}
}});

send({{event:'ready'}});
"""

IV_DCY            = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
KEY_SHA1_MABUFOJU = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4

def arr_hex(arr):
    return ''.join(f'{b:02x}' for b in arr)

def on_message(msg, data):
    if msg['type'] != 'send':
        if msg['type'] == 'error':
            print(f'[FRIDA ERROR] {msg["description"]}')
        return
    p = msg['payload']
    ev = p.get('event', '')

    if ev == 'addrs':
        print(f'[+] evoerp.exe base = {p["base"]}')
        print(f'    SetKey   -> {p["setkey"]}')
        print(f'    mode2    -> {p["mode2"]}')
        print(f'    EncBlock -> {p["encblock"]}')
        print()
    elif ev == 'ready':
        print('[+] Hooks live — log in and open any screen\n')
    elif ev == 'setkey':
        key_b = bytes(p['key_arr'])
        key20 = key_b[:20]
        exp   = KEY_SHA1_MABUFOJU[:20]
        match = '*** = sha1(mabufoju) ***' if key20 == exp else f'DIFFERENT  sha1(mabufoju)={exp.hex()}'
        print(f'--- SetKey #{p["call"]} ---')
        print(f'  key_bits : {p["key_bits"]}')
        print(f'  key[0:24]: {key_b.hex()}')
        print(f'  key[0:20]: {key20.hex()}')
        print(f'             {match}')
        print(f'  IV param : 0x{p["iv_param"]:08x}')
        print()
    elif ev == 'mode2':
        p_b  = bytes(p['P'])
        b1_b = bytes(p['buffer1'])
        print(f'--- mode2 #{p["call"]} ---')
        print(f'  P       : {p_b.hex()}  {"*** = IV_DCY ***" if p_b == IV_DCY else ""}')
        print(f'  buffer1 : {b1_b.hex()}  {"*** = IV_DCY ***" if b1_b == IV_DCY else ""}')
        print()
    elif ev == 'encrypt':
        out_b = bytes(p['out'])
        print(f'  EncryptBlock #{p["call"]}: {out_b.hex()}')
    elif ev == 'err':
        print(f'[!] hook error ({p["where"]}): {p["msg"]}')

src = script_template.format(
    preferred = PREFERRED_BASE,
    setkey    = SETKEY_VA,
    mode2     = MODE2_VA,
    encblock  = ENCBLOCK_VA,
)

print(f'[*] Waiting for {PROC_NAME}...')
print( '    Run this script first, then launch EvoERP.\n')

session = None
while session is None:
    try:
        session = frida.attach(PROC_NAME)
    except frida.ProcessNotFoundError:
        time.sleep(0.1)

print(f'[+] Attached to {PROC_NAME}')
script = session.create_script(src)
script.on('message', on_message)
script.load()
sys.stdin.read()
