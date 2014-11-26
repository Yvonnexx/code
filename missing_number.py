#!/usr/bin/python

def missing(num):
    """
    tmp = 0
    res = 0
    for i in range(len(num)):
        tmp += num[i]
    for i in range(1, len(num)+2):
        res += i
    return res - tmp
    """
    tmp = 0
    temp = 0
    for i in range(len(num)):
        tmp ^= num[i]
        print tmp
    for i in range(1, len(num)+2):
        temp ^= i
    return tmp^temp

def single(num):
    res = 0
    for i in range(len(num)):
        res ^= num[i]
    return res

num = [1,2,3,5]
print missing(num)

"""
list = [1,1,2,3,3]
print single(list)
"""
