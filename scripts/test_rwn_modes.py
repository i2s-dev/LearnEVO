#!/usr/bin/env python3
"""Test different CFB/OFB mode interpretations for RWN body decryption."""
import hashlib, sys, math
from collections import Counter
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV  = bytes.fromhex('9cdac345a5f01c2c965792d90b1abc1e')

def entropy(b):
    c = Counter(b); n = len(b)
    if n == 0: return 0
    return -sum((v/n)*math.log2(v/n) for v in c.values())

def strs(b, minlen=5):
    run = []; s = ''
    for x in b:
        if 32 <= x <= 126: s += chr(x)
        else:
            if len(s) >= minlen: run.append(s)
            s = ''
    return run

data = open('C:/Temp/t7msg_raw.bin','rb').read()

def test(name, pt_body):
    e = entropy(pt_body)
    ss = strs(pt_body)
    real = [x for x in ss if any(c.isalpha() for c in x) and not any(c in '{}\\|' for c in x)]
    print(f"{name:35s}  entropy={e:.3f}  strings={len(ss)}  real-looking={len(real)}")
    if real: print(f"  -> {real[:6]}")

tf = Twofish(KEY)
K0 = tf.encrypt(IV)
assert data[0:8] == bytes(a^b for a,b in zip(bytes([K0[i]^d for i,d in zip(range(8), data[0:8])]), K0[:8])) or True

# Mode A (current): block_buf = CT[0:8]+K0[8:16], full CFB-128
def mode_a():
    bb = bytes(data[0:8]) + bytes(K0[8:16])
    out = bytearray()
    for i in range(8, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
        bb = chunk if len(chunk)==16 else chunk + bb[len(chunk):]
    return bytes(out)

# Mode B: K0 continues — bytes 8-15 = CT[8:15] XOR K0[8:16], then CFB
def mode_b():
    out = bytearray(a^b for a,b in zip(data[8:16], K0[8:16]))
    bb = bytes(data[0:16])  # CT[0:16] as feedback
    for i in range(16, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
        bb = chunk if len(chunk)==16 else chunk + bb[len(chunk):]
    return bytes(out)

# Mode C: K0 continues — bytes 8-15 = CT[8:15] XOR K0[8:16], then OFB (K0 as seed)
def mode_c():
    out = bytearray(a^b for a,b in zip(data[8:16], K0[8:16]))
    bb = bytes(K0)
    for i in range(16, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        bb = bytes(K)
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    return bytes(out)

# Mode D: OFB from validation, block_buf = CT[0:8]+K0[8:16] (same start as A but OFB)
def mode_d():
    bb = bytes(data[0:8]) + bytes(K0[8:16])
    out = bytearray()
    for i in range(8, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        bb = bytes(K)  # OFB: no CT feedback
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    return bytes(out)

# Mode E: No partial block trick — pure CFB-128 from IV, body at byte 0
# (validation is just the first 8 bytes of the first CFB block)
def mode_e():
    bb = bytes(IV)
    out = bytearray()
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
        bb = chunk if len(chunk)==16 else chunk + bb[len(chunk):]
    return bytes(out[8:])  # skip validation bytes

# Mode F: pure OFB from IV
def mode_f():
    bb = bytes(IV)
    out = bytearray()
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        K = tf.encrypt(bb)
        bb = bytes(K)
        out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    return bytes(out[8:])  # skip validation bytes

test("Mode A: partial CFB (current impl)", mode_a())
test("Mode B: K0-cont + CFB-128", mode_b())
test("Mode C: K0-cont + OFB", mode_c())
test("Mode D: partial start + OFB", mode_d())
test("Mode E: pure CFB-128 from IV", mode_e())
test("Mode F: pure OFB from IV", mode_f())
