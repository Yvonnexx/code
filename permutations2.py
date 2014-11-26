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

def permuteUnique(num):
    res = []
    size = len(num)
    if size == 0:
        return []
    if size == 1:
        return [num]
    prev = None
    import pdb;pdb.set_trace()
    for i in range(size):
        if num[i] == prev:
            continue
        prev = num[i]
        for j in permuteUnique(num[:i]+num[i+1:]):
            res.append([num[i]]+j)
    return res

#num = [1,1,0,0,1,-1,-1,1]
num = [1,1,2]
#num = [1]
#print permuteUnique(num)
print permutation(num)
