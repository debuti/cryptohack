#!/usr/bin/env python3
stringify = lambda i: "".join(chr(o) for o in i)
bytes_xor_byte = lambda ba1, b2: bytearray([_a ^ b2 for _a in ba1])
bytes_xor_bytes = lambda ba1, ba2: bytearray([_a ^ _b for _a, _b in zip(ba1, ba2)])

input = bytearray.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

key1 = b"crypto{"
key1 = [a ^ b for a, b in zip(input, key1)]
print("key1 = {}".format(stringify(key1)))
key2 = ord("}")
key2 = [key2 ^ input[-1]]
print("key2 = {}".format(stringify(key2)))
key = key1 + key2
widekey = (stringify(key)*(1+len(input)//len(key))).encode()
print("widekey = {}".format(widekey.decode('utf-8')))
flag = bytes_xor_bytes(input, widekey)
print("flag = {}".format(stringify(flag)))