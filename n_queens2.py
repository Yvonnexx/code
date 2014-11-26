#!/usr/bin/python

def totalNQueens(n):
    def check(k, j):
        for i in range(k):
            if board[i]==j or abs(board[i]-j) == abs(k-i):
                return False
        return True

    def dfs(start, value):
        if start == n:
            res.append(value)
            return
        for i in range(n):
            if check(start, i):
                board[start] = i
                s = '.'*n
                dfs(start+1, value+[s[:i]+'Q'+s[i+1:]])
    board = [-1 for i in range(n)]
    res = []
    dfs(0,[])
    return len(res)

n = 1
print totalNQueens(n)
