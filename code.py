#!/usr/bin/env python3
'''
A field F_p modulus p is the set of numbers that can be divided by p ex. [0, 1, ..., p-1]
'''

p = 17
r1 = (3**p)%p
print(f'3^{p} % {p} = {r1}')
r1 = (3**(p-1))%p
print(f'3^{p-1} % {p} = {r1}')

r2 = (5**p)%p
print(f'5^{p} % {p} = {r2}')
r2 = (5**(p-1))%p
print(f'5^{p-1} % {p} = {r2}')

r3 = (7**p)%p
print(f'7^{p} % {p} = {r3}')
r3 = (7**(p-1))%p
print(f'7^{p-1} % {p} = {r3}')

p = 65537
r4 = (273246787654**(p-1))%p
print(f'273246787654^{p-1} % {p} = {r4}')