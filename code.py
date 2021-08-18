#!/usr/bin/env python3
'''
A field F_p modulus p is the set of numbers that can be divided by p ex. [0, 1, ..., p-1]

From Hon solution to a previous challenge:
  if p is prime, for every integer a:
        pow(a, p) = a mod p
  and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p
'''

p = 13
g = 3
#g * d ≡ 1 mod p
for d in range(p):
    if (g*d)%p==1:
        print(f'{g} * {d} ≡ 1 mod {p}')
