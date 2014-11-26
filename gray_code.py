#!/usr/bin/python
import math
def gray(n):
    res = []
    size = int(math.pow(2,n))
    for i in range(size):
        res.append((i>>1)^i)
    return res

n = 2
print gray(2)
