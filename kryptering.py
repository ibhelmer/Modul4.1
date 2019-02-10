#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:12:15 2019

@author: Ib Helmer Nielsen
"""

import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

mykey = "7913test"
mymessage= 'Dette er min klar tekst som gerne skal encryptes så ingen kan læse den'

mes=encode(mykey,mymessage)
#og tilbage igen
print (decode(mykey,mes))
