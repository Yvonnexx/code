#!/usr/bin/python

class Solution:
    def solveNQueens(self, n):
        res = []
        onesolution = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            onesolution.append(row)
        self.solve(0, n, onesolution, res)
        return res

    def solve(self, row, n, onesolution, res):
        if row == n:
            for i in range(n):
                res.append(''.join(onesolution[i]))
                print res
        for col in range(n):
            if self.canAdd(onesolution, row, col):
                onesolution[row][col] = 'Q'
                self.solve(row+1, n, onesolution, res)
                onesolution[row][col] = '.'

    def canAdd(self, onesolution, row, col):
        for i in range(row):
            if onesolution[i][col] == 'Q':
                return False
            if col - row + i >=0 and onesolution[i][col-row+i] == 'Q':
                return False
            if col + row -i < len(onesolution) and onesolution[i][col+row-i] == 'Q':
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    n = 4
    m = 1
    print s.solveNQueens(m)

