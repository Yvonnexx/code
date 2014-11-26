#!/usr/bin/python
"""
>>> exist(board, 'ABCCED')
True
>>> exist(board, 'SEE')
True
>>> exist(board, 'ABCB')
False
"""

def exist(board, word):
    if not board or len(board) == 0:
        return False
    if len(word) == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                rst = findboard(board, i, j, word, 0)
                if rst:
                    return True
    return False

def findboard(board, i, j, word, start):
    if start == len(word):
        return True
    if i< 0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[start]:
        return False
    board[i][j] = '#'
    rst = findboard(board, i-1, j, word, start+1) or findboard(board, i, j-1, word, start+1) or findboard(board, i+1, j, word, start+1) or findboard(board, i, j+1, word, start+1)
    board[i][j] = word[start]
    return rst


if __name__ == "__main__":
    board = [
             ['ABCE'],
             ['SFCS'], 
             ['ADEE']
             ]
    #import doctest
    #doctest.testmod()
    print exist(board, 'ABCCED')
    print exist(board, 'SEE')
    print exist(board, 'ABCB')
