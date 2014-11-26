#!/usr/bin/python

def isOneEdit(s, t):
    m = len(s)
    n = len(t)
    if m > n:
        return isOneEdit(t, s)
    if n - m > 1:
        return False
    i = 0
    shift = n - m
    while i < m and s[i] == t[i]:
        i += 1
    if i == m:
        return shift > 0
    if shift == 0:
        i += 1
    while i < m and s[i] == t[i+shift]:
        i += 1
    return i == m

s = 'abcde'
t = 'abXde'

print isOneEdit(s, t)
