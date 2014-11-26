#!/usr/bin/python

def singleNumber(num, k, l):
    if not num:
        return 0
    x = [None]*k
    import pdb;pdb.set_trace()
    x[0] = ~0
    for i in range(len(num)):
        t = x[k-1]
        for j in range(k-1, -1, -1):
            x[j] = (x[j-1] and num[i]) or (x[j] and ~num[i])
        x[0] = (t and num[i]) or (x[0] and ~num[i])
    return num[l]

num = [1,1,2,2,3]
k = 2
l = 1
print singleNumber(num, k, l)
