#!/usr/bin/env python3

def mcd(a, b):
  if b == 0: return a
  return mcd(b, a%b)

print(mcd(12, 8))
print(mcd(66528, 52920))