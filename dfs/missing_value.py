#!/usr/bin/python

def missing_value(num):
    x1 = num[0]
    x2 = 1
    n = len(num)
    for i in range(1, n):
        x1 = x1 ^ num[i]
    for i in range(2, n+2):
        x2 = x2 ^ i
    return x1 ^ x2

num = [1,2,3,5]
print missing_value(num)
