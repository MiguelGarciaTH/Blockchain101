#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a small example of RSA using .
https://repl.it/@billbuchanan/rsasig#main.py
"""
from Crypto.Util.number import *
from Crypto import Random
import Crypto
import libnum
import sys

bits=60
msg="Hello"

if (len(sys.argv)>1):
        msg=str(sys.argv[1])
if (len(sys.argv)>2):
        bits=int(sys.argv[2])

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

n = p*q
PHI=(p-1)*(q-1)

v=65537
s=(libnum.invmod(v, PHI))

D=  bytes_to_long(msg.encode('utf-8'))

S=pow(D,s, n)
res=pow(S,v ,n)

print("Message=%s\np=%s\nq=%s\n\ns=%d\nv=%d\nN=%s\n\nSigning exponent (s,n)\nVerification exponent (v,n)\n\nSignature=%s\nCheck=%s" % (msg,p,q,s,v,n,S,(long_to_bytes(res))))
