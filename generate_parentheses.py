#!/usr/bin/python

def generateParenthesis(n):
    def dfs(left, right, value):
        if left == right == n:
            res.append(value)
            return
        if left < n:
            dfs(left+1, right, value+'(')
        if right < left <= n:
            dfs(left, right+1, value+')')
        return
    res = []
    dfs(0, 0, '')
    return res

def generate(n):
    def dfs(left, right, valuelist):
        if left == right == n:
            v = ''.join(valuelist)
            res.append(v)
            return
        if left < n:
            valuelist.append('(')
            dfs(left+1, right, valuelist)
            valuelist.pop()
        if right < left <= n:
            valuelist.append(')')
            dfs(left, right+1, valuelist)
            valuelist.pop()
    res = []
    dfs(0, 0, [])
    return res

print generateParenthesis(2)
print generate(2)
