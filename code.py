#!/usr/bin/env python3

def egcd(a, b):
    r = [a, b]
    s = [1, 0]
    t = [0, 1]

    while r[-1] != 0:
        q = r[-2]//r[-1]
        r.append(r[-2]-q*r[-1])
        s.append(s[-2]-q*s[-1])
        t.append(t[-2]-q*t[-1])

    print(" {}*{} + {}*{} = {} + {} = gcd({}, {}) = {}".format(a,s[-2],b,t[-2],a*s[-2],b*t[-2],a,b,q))
    return (q, s[-2], t[-2])

egcd(240, 46)
egcd(26513, 32321)