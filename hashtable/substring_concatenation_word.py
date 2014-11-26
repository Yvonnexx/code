#!/usr/bin/python

class Solution:
    def findSubstring(self, S, L):
        dict = {}
        res = []
        step = len(L)*(len(L[0]))
        for i in range(len(S)-step+1):
            dict[S[i:i+step]] = i
        permutation = self.permute(L)
        for item in permutation:
            if item in dict:
                res.append(dict[item])
        res.sort()
        return res

    def permute(self, list):
        def dfs(list, valuelist):
            if len(valuelist) == len(list):
                res.append(''.join(valuelist[:]))
                return
            for i in range(len(list)):
                if list[i] in valuelist:
                    continue
                valuelist.append(list[i])
                dfs(list, valuelist)
                valuelist.pop()
        res = []
        dfs(list, [])
        return res

S = 'barfoothefoobarman'
L = ['foo', 'bar']

s = Solution()
print s.findSubstring(S, L)
