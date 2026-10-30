#!/usr/bin/env python3
"""
verify_bridge.py -- SPIRAL Bridge Calibration Verifier  (rev 0.3-diffusion)

The Spiral Observatory sealed its trained transport model behind a "bridge key".
The key is derived from one calibration pair stored in checkpoint.npz, pushed
through the observatory's forward corruption process at the stored timestamp
t_star.  This script is supposed to rebuild that key and unseal bundle.enc.

STATUS: the key never matches.  Someone has been tampering with the schedule.

Usage:  python verify_bridge.py [checkpoint.npz] [bundle.enc]
"""
import hashlib
import hmac
import json
import os
import struct
import sys

import numpy as np

MAGIC = b"SPRLENC1"
QUANT = 1e6          # fixed-point quantisation used when hashing (do not change)


# --------------------------------------------------------------------------
#  Forward-process machinery  (VP-SDE / DDPM family)
# --------------------------------------------------------------------------
def alpha_bar_schedule(t, s=0.008):
    """Cosine variance-preserving schedule (Nichol & Dhariwal, 2021).

    Returns abar(t), the cumulative signal-retention coefficient, so that the
    marginal  q(x_t | x_0) = N( sqrt(abar) x_0 , (1 - abar) I ).
    t is a continuous time in [0, 1].
    """
    f = lambda u: np.cos((u + s) / (1.0 + s) * np.pi / 2.0) ** 2
    return float(f(t) / f(0.0))


def compute_ddpm_posterior(x0, eps, t):
    """Reparameterised forward marginal of the score-based diffusion process.

        x_t = sqrt(abar_t) * x_0 + sqrt(1 - abar_t) * eps ,   eps ~ N(0, I)

    Returns (x_t, target) where `target` is the epsilon-prediction regression
    target.  The score is  s_theta(x_t, t) = -eps / sqrt(1 - abar_t)  (Tweedie).
    """
    ab = alpha_bar_schedule(t)
    x_t = np.sqrt(ab) * x0 + np.sqrt(1.0 - ab) * eps
    target = eps                      # epsilon-parameterisation
    return x_t, target


# --------------------------------------------------------------------------
#  Key derivation + sealed-bundle I/O   (this part is correct)
# --------------------------------------------------------------------------
def quantize(a):
    return np.round(np.asarray(a, dtype=np.float64) * QUANT).astype("<i8").tobytes()


def bridge_key(x_t, target, t_star, salt):
    h = hashlib.sha256()
    h.update(b"SPIRAL-BRIDGE/1")
    h.update(salt)
    h.update(struct.pack("<d", float(t_star)))
    h.update(quantize(x_t))
    h.update(quantize(target))
    return h.digest()


def keystream_xor(key, nonce, data):
    blocks = [hashlib.sha256(key + nonce + i.to_bytes(8, "big")).digest()
              for i in range((len(data) + 31) // 32)]
    ks = np.frombuffer(b"".join(blocks), dtype=np.uint8)[: len(data)]
    return np.bitwise_xor(np.frombuffer(data, dtype=np.uint8), ks).tobytes()


def unseal(path, key):
    raw = open(path, "rb").read()
    assert raw[:8] == MAGIC, "not a SPIRAL bundle"
    (hlen,) = struct.unpack("<I", raw[8:12])
    header = json.loads(raw[12:12 + hlen])
    ct = raw[12 + hlen:]
    nonce = bytes.fromhex(header["nonce"])
    mac = hmac.new(key, nonce + ct, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(mac, header["mac"]):
        return None
    return keystream_xor(key, nonce, ct)


def main():
    ck_path = sys.argv[1] if len(sys.argv) > 1 else "checkpoint.npz"
    bd_path = sys.argv[2] if len(sys.argv) > 2 else "bundle.enc"
    ck = np.load(ck_path)
    t_star = float(ck["t_star"])
    salt = ck["salt"].tobytes()

    x_t, target = compute_ddpm_posterior(ck["x0"], ck["eps"], t_star)
    key = bridge_key(x_t, target, t_star, salt)

    plain = unseal(bd_path, key)
    if plain is None:
        print("[-] MAC mismatch: the bridge is not stable at t* = %.2f" % t_star)
        print("    (key fingerprint %s...)" % key.hex()[:16])
        sys.exit(1)

    os.makedirs("unlocked", exist_ok=True)
    import zipfile, io
    zipfile.ZipFile(io.BytesIO(plain)).extractall("unlocked")
    print("[+] Bridge verified. Contents written to ./unlocked/")


if __name__ == "__main__":
    main()