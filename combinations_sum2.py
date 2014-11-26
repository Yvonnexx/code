#!/usr/bin/python

class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(candidates, target, start, valuelist):
            if target == 0 and valuelist not in res:
                return res.append(valuelist)
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    return
                dfs(candidates, target-candidates[i], i+1, valuelist+[candidates[i]])
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print s.combinationSum2(candidates, target)
