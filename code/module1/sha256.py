#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a small example of SHA256 using hashlib.
"""
import hashlib
from hashlib import blake2b
import random
import string
import time

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

rnd = get_random_string(32)

start_time = time.time()

rounds = 10000000
for i in range(0,rounds):
    m = hashlib.sha256(bytes(rnd, 'utf-8'))
#    print(m.hexdigest())

end_time = time.time()



h = blake2b(digest_size=32) #256 bits

start_time2 = time.time()
for i in range(0,rounds):
    h.update(bytes(rnd, 'utf-8'))
    h.digest()

end_time2 = time.time()
print(h.hexdigest())


elapsed_time = end_time - start_time
elapsed_time_milliSeconds = elapsed_time*1000
print("SHA256 elapsed time (msecs): ", elapsed_time_milliSeconds)

elapsed_time2 = end_time2 - start_time2
elapsed_time_milliSeconds2 = elapsed_time2*1000
print("Blake2 elapsed time (msecs): ", elapsed_time_milliSeconds2)
