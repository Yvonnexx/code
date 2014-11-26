#!/usr/bin/python

def longest(s):
    if s == '' or s == '(' or s == ')':
        return 0
    stack = [(-1, ')')]
    maxlen = 0
    for i in range(len(s)):
        if s[i] == ')' and stack[-1][1] == '(':
            stack.pop()
            maxlen = max(maxlen, i-stack[-1][0])
        else:
            stack.append((i, s[i]))
    return maxlen


print longest('(()')
print longest(')()())')
print longest('()')
