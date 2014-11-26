#!/usr/bin/python

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        letter = 'abcdefghijklmnopqrstuvwxyz'
        def dfs(start, end, value):
            for i in range(len(start)):
                for j in letter:
                    tmp = start[:i]+j+start[i+1:]
                    if tmp == end:
                        value.append(end)
                        res.append(value)
                        return
                    if tmp in dict and tmp not in value:
                        dfs(tmp, end, value+[tmp])
        res = []
        dfs(start, end, [start])
        tmp = sorted(res, key=lambda x:len(x))
        if tmp:
            var = tmp[0]
            final = []
            final.append(var)
            for item in tmp[1:]:
                if len(item) == len(var):
                    final.append(item)
                else:
                    break
            return final

    def find(self, start, end, dict):
        def buildpath(path, word):
            if len(prevMap[word]) == 0:
                path.append(word)
                currpath = path[:]
                currpath.reverse()
                res.append(currpath)
                path.pop()
                return
            path.append(word)
            for

s = Solution()
start = 'hot'
end = 'dog'
dict = ['hot', 'dog']
print s.findLadders(start,end,dict)
