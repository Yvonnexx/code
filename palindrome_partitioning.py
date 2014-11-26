#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPalindrome(self, s):
        for i in xrange(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    
    def dfs(self, s, string):
        if len(s) == 0:
            Solution.res.append(string)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], string+[s[:i]])

    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res
    
    def minCut(self, s):
        dp = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                    if s[i] == s[j] and ((j-i)<2 or p[i][j]):
                        p[i][j] = True
                        dp[i] = min(dp[j-1]+1, dp[i])
        return dp[0] -1 



if __name__ == "__main__":
    s  = Solution()
    str = "a"
    print s.minCut(str)
