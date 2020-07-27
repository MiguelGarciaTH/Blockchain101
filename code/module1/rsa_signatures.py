
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a small example of RSA using Crypto lib.
"""
import errno
from base64 import b64encode, b64decode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def sign(message):
    try:
        with open('privkey.pem', 'r') as f:
            key = RSA.importKey(f.read())
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise
        # No private key, generate a new one. This can take a few seconds.
        key = RSA.generate(4096)
        with open('privkey.pem', 'wb') as f:
            f.write(key.exportKey('PEM'))
        with open('pubkey.pem', 'wb') as f:
            f.write(key.publickey().exportKey('PEM'))

    hasher = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    signature_str = b64encode(signature)
    print(signature_str)
    return signature

def verify(message, signature):
    with open('pubkey.pem', 'rb') as f:
        key = RSA.importKey(f.read())
    hasher = SHA256.new(message)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, signature):
        print('Nice, the signature is valid!')
    else:
        print('No, the message was signed with the wrong private key or modified')

message = b'This message is from me, I promise.'
signature = sign(message)
verify(message, signature)
