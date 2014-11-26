#!/usr/bin/python

def restore(s):
    def dfs(s, start, value):
        if start == 4:
            if s == '':
                res.append(value[1:])
            return
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    dfs(s[i:], start+1, value+'.'+s[:i])
                if s[0] == '0':
                    break

    res = []
    dfs(s, 0, '')
    return res

s1 = '25525511135'
print restore(s1)
