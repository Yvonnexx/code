#!/usr/bin/python

def getPermutation(n,k):
    res = ''
    k -= 1
    factor = 1
    for i in xrange(1, n):
        factor *= i
    print factor
    num = [i for i in range(1,n+1)]
    import pdb;pdb.set_trace()
    for i in reversed(range(n)):
        curr = num[k/factor]
        res += str(curr)
        num.remove(curr)
        if i != 0:
            k %= factor
            factor /= i
    return res

n = 3
k = 3
print getPermutation(n, k)
