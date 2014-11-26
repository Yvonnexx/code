#!/usr/bin/python

def subsets(S):
    def dfs(start, valuelist):
        res.append(valuelist)
        if start == len(S):
            return
        for i in range(start, len(S)):
            dfs(i+1, valuelist+[S[i]])
    S.sort()
    res = []
    dfs(0, [])
    return res


S = [1,2,3]
print subsets(S)
