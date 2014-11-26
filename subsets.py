#!/usr/bin/python

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def dfs(start, valuelist):
            if valuelist not in res:
                print valuelist
                res.append(valuelist)
            if start == len(S):
                return 
            for i in range(start, len(S)):
                dfs(i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, [])
        return res

if __name__ =="__main__":
    s = Solution()
    s1 = [1,2,3]
    print s.subsets(s1)

