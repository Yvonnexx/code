#!/usr/bin/python

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def dfs(start, end, value, dict):
            for i in range(len(start)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if start[:i]+j+start[i+1:] in dict and start[:i]+j+start[i+1:] not in value:
                        dfs(start[:i]+j+start[i+1:], end, value+[start[:i]+j+start[i+1:]], dict)
                    if start[:i]+j+start[i+1:] == end:
                        res.append(value)
                        return
        res = [] 
        final = []
        dfs(start, end, [], dict)
        minlen = 999
        for item in res:
            if len(item) <= minlen:
                minlen = len(item)
        for item in res:
            if len(item) == minlen:
                final.append(item)
        for item in final:
            item.insert(0, start)
            item.append(end)
        return final 

if __name__ == "__main__":
    s = Solution()
    start = 'hit'
    end = 'cog'
    dict = ['hot', 'dot', 'dog', 'lot', 'log']
    print s.findLadders(start, end, dict)
