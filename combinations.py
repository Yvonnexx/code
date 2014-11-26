#!/usr/bin/python
"""
def combine(n, k):
    rst = []
    solution = []
    generate(rst, solution ,n, k, 1)
    return rst

def generate(rst, solution, n, k, start):
    if len(solution) == k:
        rst.append(solution[:])
        return
    for i in range(start, n+1):
        solution.append(i)
        generate(rst, solution, n, k, i+1)
        solution.pop()

print combine(4,2)
"""

def combine(n,k):
    def dfs(start, value):
        if len(value) == k:
            res.append(value[:])
            return 
        for i in range(start, n+1):
            value.append(i)
            dfs(i+1, value)
            value.pop()
    res = []
    dfs(1, [])
    return res

print combine(4,2)
