#!/usr/bin/python

class Solution:
    """
    def wordBreak(self, s, dict):
        def dfs(s, value):
            if self.check(s, dict):
                if len(s) == 0:
                    res.append(value[1:])
                    return
                for i in range(1, len(s)+1):
                    if s[:i] in dict:
                        dfs(s[i:], value+' '+s[:i])
        res = []
        dfs(s, '')
        return res
    """ 
    def wordBreak(self, s, dict):
        def dfs(s, value):
            if self.check(s, dict):
                #import pdb;pdb.set_trace()
                if not s:
                    res.append(' '.join(value))
                    return
                for i in range(1,len(s)+1):
                    if s[:i] in dict:
                        dfs(s[i:], value+[s[:i]])
        res = []
        dfs(s, [])
        return res
    
    def check(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
        return dp[len(s)]
    
if __name__ == "__main__":
    s = Solution()
    str = 'a'
    dict = ['a']
    print s.wordBreak(str, dict)
