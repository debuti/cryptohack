#!/usr/bin/env python3
import png

stringify = lambda i: "".join(chr(o) for o in i)
bytes_xor_byte = lambda ba1, b2: bytearray([_a ^ b2 for _a in ba1])
bytes_xor_bytes = lambda ba1, ba2: bytearray([_a ^ _b for _a, _b in zip(ba1, ba2)])

lemur = png.Reader(file=open('lemur.png', 'rb')).read()
flag = png.Reader(file=open('flag.png', 'rb')).read()
xorimg = [bytes_xor_bytes(lemurrow, flagrow) for lemurrow, flagrow in zip(lemur[2], flag[2])]

with open('out.png', 'wb') as out: png.Writer(lemur[0], lemur[1], greyscale=lemur[3]["greyscale"], bitdepth=lemur[3]["bitdepth"]).write(out, xorimg)