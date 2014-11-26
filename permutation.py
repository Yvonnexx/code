#!/usr/bin/python

def permute(num):
    def dfs(num, valuelist):
        if len(valuelist) == len(num):
            res.append(valuelist[:])
            return
        for i in range(len(num)):
            if num[i] in valuelist:
                continue
            valuelist.append(num[i])
            dfs(num, valuelist)
            valuelist.pop()
    res = []
    dfs(num, [])
    return res

num = [1,2,3]
print permute(num)
