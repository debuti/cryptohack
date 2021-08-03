#!/usr/bin/env python3

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

bytes_xor_byte = lambda ba1, b2: bytearray([_a ^ b2 for _a in ba1])

input = bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for op in range(0,255):
  try: 
    flag = bytes_xor_byte(input, op).decode('utf-8')
    if "crypto" in flag:
      print(flag)
  except: pass