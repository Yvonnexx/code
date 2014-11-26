#!/usr/bin/python

def wordBreak(s, dict):
    def dfs(s,value):
        if s in dict:
            value.append(s)
            v = ' '.join(value)
            res.append(v)
            return
        for i in range(len(s)):
            if s[:i] in dict:
                dfs(s[i:],value+[s[:i]])
    res = []
    dfs(s,[])
    return res

s1 = 'catsanddog'
dict1 = ['cat', 'cats', 'and', 'sand', 'dog']
s2 = 'helloworld'
dict2 = ['xx','yy','world']
print wordBreak(s1, dict1)
