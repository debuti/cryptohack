#!/usr/bin/env python3

input = "label"
operator = 13

print("crypto{{{}}}".format("".join([chr(operator^ord(x)) for x in input])))
