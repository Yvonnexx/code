#!/usr/bin/python

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1 for i in range(m)]]
        else:
            list = [[0 for i in range(n)] for j in range(m)]
            for i in range(n):
                list[0][i] = 1
            for i in range(m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1]

if __name__ == "__main__":
    m = 3
    n = 7
    s = Solution()
    print s.uniquePaths(m, n)
