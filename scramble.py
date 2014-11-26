#!/usr/bin/python

def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    if l1 != l2:
        return False
    for i in range(1, len(s1)):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        if isScramble(s1[:i], s2[len(s1)-i:]) and isScramble(s1[i:], s2[:(len(s1)-i)]):
            return True
    return False

s1 = 'great'
s2 = 'rgeat'
print isScramble(s1, s2)
