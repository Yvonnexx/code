#!/usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, n, k):
        res = []
        list = []
        num = []
        for i in range(1, n+1):
            num.append(i)
        self.generate(res, list, n)
        return res[k]
    
    def generate(self, res, list, n):
        if len(list) == n:
            res.append(list[:])
            return
        for i in range(1,n+1):
            if i in list:
                continue
            list.append(i)
            self.generate(res, list, n)
            list.pop()

if __name__ == "__main__":
    s = Solution()
    n = 9
    print s.permute(n, 54494)
