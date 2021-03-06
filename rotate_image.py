#!/usr/bin/python

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n-1-i):
            matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
    for i in range(n/2):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print rotate(matrix)
