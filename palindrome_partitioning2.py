#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        def dfs(s, value):
            for i in range(1, len(s)+1):
                if self.is_palindrome(s[:i]) :
                    dfs(s[i:], value+[s[:i]])
            if len(s) == 0:
                res.append(value)
                return
        res = []
        dfs(s, [])
        final = min(res, key=len)
        return final

    def is_palindrome(self, str):
        for i in range(len(str)):
            if str[i] != str[len(str)-i-1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    str = 'aab'
    str1 = 'a'
    print s.minCut(str)
    print s.minCut(str1)
