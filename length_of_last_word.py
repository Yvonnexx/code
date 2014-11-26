#!/usr/bin/python

def lengthOfLastWord(s):
    tmp = s.split()
    return len(tmp[-1])

s = " "
print lengthOfLastWord(s)
