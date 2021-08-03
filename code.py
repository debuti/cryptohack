#!/usr/bin/env python3

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

byte_xor = lambda ba1, ba2: bytearray([_a ^ _b for _a, _b in zip(ba1, ba2)])

KEY1 = bytearray.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2xorKEY1 = bytearray.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2xorKEY3 = bytearray.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAGxorKEY1xorKEY3xorKEY2 = bytearray.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = byte_xor(FLAGxorKEY1xorKEY3xorKEY2, byte_xor(KEY1, KEY2xorKEY3)).decode('utf-8')
print(flag)