#!/usr/bin/python

def numDistinct(s, t):
    cnt = 0
    if len(s) == 0:
        if len(t) == 0:
            return 1
        else:
            return 0
    if len(t) == 0:
        return 1
    for i in range(len(s)):
        if s[i] == t[0]:
            cnt += numDistinct(s[i+1:], t[1:])
    return cnt

s = 'rabbbit'
t = 'rabbit'
print numDistinct(s, t)
