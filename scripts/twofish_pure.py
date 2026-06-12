#!/usr/bin/env python3
"""
Pure-Python Twofish block cipher (128-bit block, 128/192/256-bit keys).
Based on the Twofish specification by Schneier, Kelsey, Whiting, Wagner, Hall, Ferguson.

No C extensions required.

Usage:
    from twofish_pure import Twofish
    tf = Twofish(key_bytes)          # key = 16, 24, or 32 bytes
    ct = tf.encrypt(plaintext_block) # plaintext_block = 16 bytes, returns 16 bytes
    pt = tf.decrypt(cipher_block)    # cipher_block = 16 bytes, returns 16 bytes
"""

import struct

# ---------------------------------------------------------------------------
# Fixed q0 and q1 permutation tables (from Twofish specification, Appendix A)
# ---------------------------------------------------------------------------
_q0 = [
    0xA9,0x67,0xB3,0xE8,0x04,0xFD,0xA3,0x76,0x9A,0x92,0x80,0x78,0xE4,0xDD,0xD1,0x38,
    0x0D,0xC6,0x35,0x98,0x18,0xF7,0xEC,0x6C,0x43,0x75,0x37,0x26,0xFA,0x13,0x94,0x48,
    0xF2,0xD0,0x8B,0x30,0x84,0x54,0xDF,0x23,0x19,0x5B,0x3D,0x59,0xF3,0xAE,0xA2,0x82,
    0x63,0x01,0x83,0x2E,0xD9,0x51,0x9B,0x7C,0xA6,0xEB,0xA5,0xBE,0x16,0x0C,0xE3,0x61,
    0xC0,0x8C,0x3A,0xF5,0x73,0x2C,0x25,0x0B,0xBB,0x4E,0x89,0x6B,0x53,0x6A,0xB4,0xF1,
    0xE1,0xE6,0xBD,0x45,0xE2,0xF4,0xB6,0x66,0xCC,0x95,0x03,0x56,0xD4,0x1C,0x1E,0xD7,
    0xFB,0xC3,0x8E,0xB5,0xE9,0xCF,0xBF,0xBA,0xEA,0x77,0x39,0xAF,0x33,0xC9,0x62,0x71,
    0x81,0x79,0x09,0xAD,0x24,0xCD,0xF9,0xD8,0xE5,0xC5,0xB9,0x4D,0x44,0x08,0x86,0xE7,
    0xA1,0x1D,0xAA,0xED,0x06,0x70,0xB2,0xD2,0x41,0x7B,0xA0,0x11,0x31,0xC2,0x27,0x90,
    0x20,0xF6,0x60,0xFF,0x96,0x5C,0xB1,0xAB,0x9E,0x9C,0x52,0x1B,0x5F,0x93,0x0A,0xEF,
    0x91,0x85,0x49,0xEE,0x2D,0x4F,0x8F,0x3B,0x47,0x87,0x6D,0x46,0xD6,0x3E,0x69,0x64,
    0x2A,0xCE,0xCB,0x2F,0xFC,0x97,0x05,0x7A,0xAC,0x7F,0xD5,0x1A,0x4B,0x0E,0xA7,0x5A,
    0x28,0x14,0x3F,0x29,0x88,0x3C,0x4C,0x02,0xB8,0xDA,0xB0,0x17,0x55,0x1F,0x8A,0x7D,
    0x57,0xC7,0x8D,0x74,0xB7,0xC4,0x9F,0x72,0x7E,0x15,0x22,0x12,0x58,0x07,0x99,0x34,
    0x6E,0x50,0xDE,0x68,0x65,0xBC,0xDB,0xF8,0xC8,0xA8,0x2B,0x40,0xDC,0xFE,0x32,0xA4,
    0xCA,0x10,0x21,0xF0,0xD3,0x5D,0x0F,0x00,0x6F,0x9D,0x36,0x42,0x4A,0x5E,0xC1,0xE0,
]

_q1 = [
    0x75,0xF3,0xC6,0xF4,0xDB,0x7B,0xFB,0xC8,0x4A,0xD3,0xE6,0x6B,0x45,0x7D,0xE8,0x4B,
    0xD6,0x32,0xD8,0xFD,0x37,0x71,0xF1,0xE1,0x30,0x0F,0xF8,0x1B,0x87,0xFA,0x06,0x3F,
    0x5E,0xBA,0xAE,0x5B,0x8A,0x00,0xBC,0x9D,0x6D,0xC1,0xB1,0x0E,0x80,0x5D,0xD2,0xD5,
    0xA0,0x84,0x07,0x14,0xB5,0x90,0x2C,0xA3,0xB2,0x73,0x4C,0x54,0x92,0x74,0x36,0x51,
    0x38,0xB0,0xBD,0x5A,0xFC,0x60,0x62,0x96,0x6C,0x42,0xF7,0x10,0x7C,0x28,0x27,0x8C,
    0x13,0x95,0x9C,0xC7,0x24,0x46,0x3B,0x70,0xCA,0xE3,0x85,0xCB,0x11,0xD0,0x93,0xB8,
    0xA6,0x83,0x20,0xFF,0x9F,0x77,0xC3,0xCC,0x03,0x6F,0x08,0xBF,0x40,0xE7,0x2B,0xE2,
    0x79,0x0C,0xAA,0x82,0x41,0x3A,0xEA,0xB9,0xE4,0x9A,0xA4,0x97,0x7E,0xDA,0x7A,0x17,
    0x66,0x94,0xA1,0x1D,0x3D,0xF0,0xDE,0xB3,0x0B,0x72,0xA7,0x1C,0xEF,0xD1,0x53,0x3E,
    0x8F,0x33,0x26,0x5F,0xEC,0x76,0x2A,0x49,0x81,0x88,0xEE,0x21,0xC4,0x1A,0xEB,0xD9,
    0xC5,0x39,0x99,0xCD,0xAD,0x31,0x8B,0x01,0x18,0x23,0xDD,0x1F,0x4E,0x2D,0xF9,0x48,
    0x4F,0xF2,0x65,0x8E,0x78,0x5C,0x58,0x19,0x8D,0xE5,0x98,0x57,0x67,0x7F,0x05,0x64,
    0xAF,0x63,0xB6,0xFE,0xF5,0xB7,0x3C,0xA5,0xCE,0xE9,0x68,0x44,0xE0,0x4D,0x43,0x69,
    0x29,0x2E,0xAC,0x15,0x59,0xA8,0x0A,0x9E,0x6E,0x47,0xDF,0x34,0x35,0x6A,0xCF,0xDC,
    0x22,0xC9,0xC0,0x9B,0x89,0xD4,0xED,0xAB,0x12,0xA2,0x0D,0x52,0xBB,0x02,0x2F,0xA9,
    0xD7,0x61,0x1E,0xB4,0x50,0x04,0xF6,0xC2,0x16,0x25,0x86,0x56,0x55,0x09,0xBE,0x91,
]

# ---------------------------------------------------------------------------
# GF(2^8) multiplication helpers
# ---------------------------------------------------------------------------
def _gf_mul(a, b, poly):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= poly
    return p & 0xFF

# MDS uses poly 0x169; RS uses poly 0x14D
def _mds_mul(a, b): return _gf_mul(a, b, 0x169)
def _rs_mul(a, b):  return _gf_mul(a, b, 0x14D)

# Pre-compute GF tables for MDS columns
# MDS matrix columns (applied to each byte of the 32-bit word):
#   byte 0: [01, 5B, EF, EF]  (multiply by these to get column contributions)
#   byte 1: [EF, EF, 5B, 01]
#   byte 2: [5B, 01, EF, EF] -- actually let me define by rows:
#
# MDS matrix (rows × columns):
# [01 EF 5B 5B]   result byte 0
# [5B EF EF 01]   result byte 1
# [EF 5B 01 EF]   result byte 2
# [EF 01 EF 5B]   result byte 3
#
# So MDS(x0,x1,x2,x3) = [
#   x0^EF*x1^5B*x2^5B*x3,
#   5B*x0^EF*x1^EF*x2^x3,
#   EF*x0^5B*x1^x2^EF*x3,
#   EF*x0^x1^EF*x2^5B*x3
# ]

def _mds(x):
    """Apply MDS matrix to a 4-byte tuple, return 32-bit word (little-endian)."""
    x0, x1, x2, x3 = x
    def m(a, b): return _mds_mul(a, b)
    r0 = x0 ^ m(x1, 0xEF) ^ m(x2, 0x5B) ^ m(x3, 0x5B)
    r1 = m(x0, 0x5B) ^ m(x1, 0xEF) ^ m(x2, 0xEF) ^ x3
    r2 = m(x0, 0xEF) ^ m(x1, 0x5B) ^ x2 ^ m(x3, 0xEF)
    r3 = m(x0, 0xEF) ^ x1 ^ m(x2, 0xEF) ^ m(x3, 0x5B)
    return r0 | (r1 << 8) | (r2 << 16) | (r3 << 24)

def _rs_mds_encode(key_bytes_8):
    """
    RS encode 8 key bytes → 4 S-box key bytes.

    Implements polynomial reduction over GF(2^8) with poly 0x14D:
    generator = y^4 + (x+1/x)y^3 + xy^2 + (x+1/x)y + 1
    Matches the reference twofish-0.3/twofish.c Twofish_prepare_key RS block.
    """
    # poly[0..3] = accumulating result coefficients (y^0..y^3)
    # poly[4..11] = the 8 key bytes (y^4..y^11)
    poly = [0, 0, 0, 0] + list(key_bytes_8)
    # Reduce from highest coefficient (index 11) down to index 4
    for i in range(11, 3, -1):
        b = poly[i]
        bx  = ((b << 1) ^ (0x14d if b >> 7 else 0)) & 0xFF
        bxx = ((b >> 1) ^ (0xa6 if b & 1 else 0) ^ bx) & 0xFF
        poly[i-1] ^= bxx   # coeff of y^(i-1): * (x+1/x)
        poly[i-2] ^= bx    # coeff of y^(i-2): * x
        poly[i-3] ^= bxx   # coeff of y^(i-3): * (x+1/x)
        poly[i-4] ^= b     # coeff of y^(i-4): * 1
    return poly[0:4]

# ---------------------------------------------------------------------------
# h() function: apply key-dependent S-boxes + MDS
# ---------------------------------------------------------------------------
def _h(x, L, k):
    """
    x   : 32-bit integer input
    L   : list of S-box key bytes (each element is 4 bytes) in order [M_e[0], M_e[1], ...]
    k   : key length in words (2, 3, or 4)
    Returns a 32-bit integer.
    """
    b = [(x >> (8*i)) & 0xFF for i in range(4)]

    if k == 4:
        b[0] = _q1[b[0]] ^ L[3][0]
        b[1] = _q0[b[1]] ^ L[3][1]
        b[2] = _q0[b[2]] ^ L[3][2]
        b[3] = _q1[b[3]] ^ L[3][3]
    if k >= 3:
        b[0] = _q1[b[0]] ^ L[2][0]
        b[1] = _q1[b[1]] ^ L[2][1]
        b[2] = _q0[b[2]] ^ L[2][2]
        b[3] = _q0[b[3]] ^ L[2][3]
    # k=2 base case (confirmed against reference H02..H32 macros):
    # Col 0: q1(q0(q0(x)^L1)^L0)  Col 1: q0(q0(q1(x)^L1)^L0)
    # Col 2: q1(q1(q0(x)^L1)^L0)  Col 3: q0(q1(q1(x)^L1)^L0)
    b[0] = _q1[_q0[_q0[b[0]] ^ L[1][0]] ^ L[0][0]]
    b[1] = _q0[_q0[_q1[b[1]] ^ L[1][1]] ^ L[0][1]]
    b[2] = _q1[_q1[_q0[b[2]] ^ L[1][2]] ^ L[0][2]]
    b[3] = _q0[_q1[_q1[b[3]] ^ L[1][3]] ^ L[0][3]]

    return _mds(b)


def _ror32(x, n): return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
def _rol32(x, n): return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


class Twofish:
    """Twofish block cipher — 128-bit block, keys of 16/24/32 bytes."""

    def __init__(self, key: bytes):
        n = len(key)
        if n not in (16, 24, 32):
            raise ValueError(f"Key must be 16, 24, or 32 bytes, got {n}")
        k = n // 8  # number of 64-bit key words (2, 3, or 4)

        # Split key into even and odd 32-bit words (little-endian)
        words = list(struct.unpack_from(f'<{n//4}I', key))
        M_e = words[0::2]   # even: M[0], M[2], M[4], M[6]
        M_o = words[1::2]   # odd:  M[1], M[3], M[5], M[7]

        # Build S-box key material via RS encoding (for g() function).
        # S[i] = RS(key[8i..8i+7]) — one 4-byte group per 64-bit key chunk.
        # The S-vector is reversed so that s[0] = RS of the LAST chunk, matching
        # the reference's reverse-order storage (K+8*kCycles processed first).
        S = [_rs_mds_encode(list(key[8*i : 8*i+8])) for i in range(k)]
        S_rev = list(reversed(S))

        # Build raw-key byte groups for subkey generation.
        # The reference h(i, K, kCycles) uses L = K starting at K[0] for A
        # and L = K+4 for B, accessing bytes at offsets 0..3, 8..11, 16..19, 24..27.
        # M_e_groups[i] = 4 bytes at key offset 8i+0..3 (even words)
        # M_o_groups[i] = 4 bytes at key offset 8i+4..7 (odd words)
        M_e = [list(key[8*i   : 8*i+4]) for i in range(k)]
        M_o = [list(key[8*i+4 : 8*i+8]) for i in range(k)]

        # Generate 40 subkeys using the PHT (pseudo-Hadamard transform).
        # A uses even key words; B uses odd key words (NOT S_rev — that's only for g()).
        self._K = []
        rho = 0x01010101
        for i in range(20):
            A = _h(2*i * rho, M_e, k)
            B = _rol32(_h((2*i+1) * rho, M_o, k), 8)
            K2i   = (A + B) & 0xFFFFFFFF
            K2i1  = _rol32((A + 2*B) & 0xFFFFFFFF, 9)
            self._K.append(K2i)
            self._K.append(K2i1)

        # Build g() lookup tables (key-dependent S-boxes)
        # Pre-compute the full 4 lookup tables for g()
        self._g_table = [None, None, None, None]
        for j in range(4):
            tbl = []
            for x in range(256):
                b = [0, 0, 0, 0]
                b[j] = x
                # Apply same S-box pipeline as h() but only for byte j
                # We build the MDS-combined table
                if k == 4:
                    b[0] = _q1[b[0]] ^ S_rev[0][0] if j==0 else 0
                    # etc — this per-byte approach is complex; skip table opt
                tbl.append(0)
            # Don't use table; use h() directly in g()
        self._S_rev = S_rev
        self._k = k

    def _g(self, x):
        return _h(x, self._S_rev, self._k)

    def encrypt(self, block: bytes) -> bytes:
        if len(block) != 16:
            raise ValueError("Block must be 16 bytes")
        K = self._K
        P = list(struct.unpack_from('<4I', block))
        # Input whitening
        X = [P[i] ^ K[i] for i in range(4)]
        # 16 Feistel rounds
        for r in range(16):
            T0 = self._g(X[0])
            T1 = self._g(_rol32(X[1], 8))
            F0 = (T0 + T1 + K[8 + 2*r]) & 0xFFFFFFFF
            F1 = (T0 + 2*T1 + K[8 + 2*r + 1]) & 0xFFFFFFFF
            X[2] = _ror32(X[2] ^ F0, 1)
            X[3] = _rol32(X[3], 1) ^ F1
            X[0], X[1], X[2], X[3] = X[2], X[3], X[0], X[1]
        # Undo last swap, output whitening
        X[0], X[1], X[2], X[3] = X[2], X[3], X[0], X[1]
        C = [X[i] ^ K[4 + i] for i in range(4)]
        return struct.pack('<4I', *C)

    def decrypt(self, block: bytes) -> bytes:
        if len(block) != 16:
            raise ValueError("Block must be 16 bytes")
        K = self._K
        C = list(struct.unpack_from('<4I', block))
        # Undo output whitening
        X = [C[i] ^ K[4 + i] for i in range(4)]
        # 16 rounds in reverse (no pre-loop swap — ciphertext is already in the
        # correct order: [C16,D16,A16,B16] matches the reference's GET_INPUT layout)
        for r in range(15, -1, -1):
            T0 = self._g(X[0])
            T1 = self._g(_rol32(X[1], 8))
            F0 = (T0 + T1 + K[8 + 2*r]) & 0xFFFFFFFF
            F1 = (T0 + 2*T1 + K[8 + 2*r + 1]) & 0xFFFFFFFF
            X[2] = _rol32(X[2], 1) ^ F0   # undo ROR(x,1)
            X[3] = _ror32(X[3] ^ F1, 1)   # undo ROL(x,1)
            X[0], X[1], X[2], X[3] = X[2], X[3], X[0], X[1]
        # Mirror the encrypt's final swap (PUT_OUTPUT uses C,D,A,B order)
        X[0], X[1], X[2], X[3] = X[2], X[3], X[0], X[1]
        # Undo input whitening
        P = [X[i] ^ K[i] for i in range(4)]
        return struct.pack('<4I', *P)


# ---------------------------------------------------------------------------
# ECB / CBC helpers
# ---------------------------------------------------------------------------
def ecb_decrypt(key: bytes, data: bytes) -> bytes:
    tf = Twofish(key)
    out = bytearray()
    for i in range(0, len(data), 16):
        out += tf.decrypt(data[i:i+16])
    return bytes(out)

def cbc_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    tf = Twofish(key)
    out = bytearray()
    prev = iv
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        pt = bytearray(tf.decrypt(block))
        for j in range(16):
            pt[j] ^= prev[j]
        out += pt
        prev = block
    return bytes(out)

def ofb_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """OFB mode: encrypt IV repeatedly, XOR with ciphertext."""
    tf = Twofish(key)
    out = bytearray()
    keystream_block = iv
    for i in range(0, len(data), 16):
        keystream_block = tf.encrypt(keystream_block)
        block = data[i:i+16]
        for j in range(min(16, len(block))):
            out.append(block[j] ^ keystream_block[j])
    return bytes(out)

def cfb_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """CFB-128 mode."""
    tf = Twofish(key)
    out = bytearray()
    prev = iv
    for i in range(0, len(data), 16):
        ks = tf.encrypt(prev)
        block = data[i:i+16]
        pt = bytes(block[j] ^ ks[j] for j in range(min(16, len(block))))
        out += pt
        prev = block
    return bytes(out)


# ---------------------------------------------------------------------------
# Self-test using official Twofish test vectors (from the spec)
# ---------------------------------------------------------------------------
def _selftest():
    # Test vector 1: 128-bit all-zeros key, all-zeros plaintext
    key = bytes(16)
    pt  = bytes(16)
    expected_ct = bytes.fromhex('9F589F5CF6122C32B6BFEC2F2AE8C35A')
    tf = Twofish(key)
    ct = tf.encrypt(pt)
    assert ct == expected_ct, f"Enc128z failed: {ct.hex()} != {expected_ct.hex()}"
    assert tf.decrypt(ct) == pt, "Dec128z failed"

    # Test vector 2: 192-bit all-zeros key
    key2 = bytes(24)
    expected_ct2 = bytes.fromhex('EFA71F788965BD4453F860178FC19101')
    tf2 = Twofish(key2)
    ct2 = tf2.encrypt(pt)
    assert ct2 == expected_ct2, f"Enc192z failed: {ct2.hex()} != {expected_ct2.hex()}"

    # Test vector 3: 256-bit all-zeros key
    key3 = bytes(32)
    expected_ct3 = bytes.fromhex('57FF739D4DC92C1BD7FC01700CC8216F')
    tf3 = Twofish(key3)
    ct3 = tf3.encrypt(pt)
    assert ct3 == expected_ct3, f"Enc256z failed: {ct3.hex()} != {expected_ct3.hex()}"

    # Non-zero key test vectors (section B.2, I=3/I=4 from the Twofish book via
    # twofish-0.3/twofish.c test_vectors() — these exercise the subkey generation
    # and S-box key material paths that don't fire for all-zeros keys).
    k128 = bytes([0x9F,0x58,0x9F,0x5C,0xF6,0x12,0x2C,0x32,0xB6,0xBF,0xEC,0x2F,0x2A,0xE8,0xC3,0x5A])
    p128 = bytes([0xD4,0x91,0xDB,0x16,0xE7,0xB1,0xC3,0x9E,0x86,0xCB,0x08,0x6B,0x78,0x9F,0x54,0x19])
    c128 = bytes([0x01,0x9F,0x98,0x09,0xDE,0x17,0x11,0x85,0x8F,0xAA,0xC3,0xA3,0xBA,0x20,0xFB,0xC3])
    tf128 = Twofish(k128)
    got = tf128.encrypt(p128)
    assert got == c128, f"Enc128nz failed: {got.hex()} != {c128.hex()}"
    assert tf128.decrypt(c128) == p128, "Dec128nz failed"

    k192 = bytes([0x88,0xB2,0xB2,0x70,0x6B,0x10,0x5E,0x36,0xB4,0x46,0xBB,0x6D,0x73,0x1A,0x1E,0x88,
                  0xEF,0xA7,0x1F,0x78,0x89,0x65,0xBD,0x44])
    p192 = bytes([0x39,0xDA,0x69,0xD6,0xBA,0x49,0x97,0xD5,0x85,0xB6,0xDC,0x07,0x3C,0xA3,0x41,0xB2])
    c192 = bytes([0x18,0x2B,0x02,0xD8,0x14,0x97,0xEA,0x45,0xF9,0xDA,0xAC,0xDC,0x29,0x19,0x3A,0x65])
    tf192 = Twofish(k192)
    got = tf192.encrypt(p192)
    assert got == c192, f"Enc192nz failed: {got.hex()} != {c192.hex()}"
    assert tf192.decrypt(c192) == p192, "Dec192nz failed"

    k256 = bytes([0xD4,0x3B,0xB7,0x55,0x6E,0xA3,0x2E,0x46,0xF2,0xA2,0x82,0xB7,0xD4,0x5B,0x4E,0x0D,
                  0x57,0xFF,0x73,0x9D,0x4D,0xC9,0x2C,0x1B,0xD7,0xFC,0x01,0x70,0x0C,0xC8,0x21,0x6F])
    p256 = bytes([0x90,0xAF,0xE9,0x1B,0xB2,0x88,0x54,0x4F,0x2C,0x32,0xDC,0x23,0x9B,0x26,0x35,0xE6])
    c256 = bytes([0x6C,0xB4,0x56,0x1C,0x40,0xBF,0x0A,0x97,0x05,0x93,0x1C,0xB6,0xD4,0x08,0xE7,0xFA])
    tf256 = Twofish(k256)
    got = tf256.encrypt(p256)
    assert got == c256, f"Enc256nz failed: {got.hex()} != {c256.hex()}"
    assert tf256.decrypt(c256) == p256, "Dec256nz failed"

    print("All Twofish self-tests passed.")


if __name__ == '__main__':
    _selftest()
