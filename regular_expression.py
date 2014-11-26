#!/usr/bin/python

def isMatch(s, p):
    if len(p) == 0:
        return len(s) == 0
    if len(p) == 1 or p[1] != '*':
        if len(s) ==0 or (s[0]!=p[0] and p[0]!='.'):
            return False
        return isMatch(s[1:], p[1:])
    else:
        i = -1
        length = len(s)
        while i < length and (i<0 or p[0] == '.' or p[0] == s[i]):
            if isMatch(s[i+1:], p[2:]):
                return True
            i+= 1
        return False

print isMatch('aa', 'a')
print isMatch('aa', 'aa')
print isMatch('aaa', 'aa')
print isMatch('aa', 'a*')
print isMatch('aa', '.*')
print isMatch('ab', '.*')
print isMatch('aab', 'c*a*b')
