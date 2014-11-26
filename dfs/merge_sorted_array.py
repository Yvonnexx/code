#!/usr/bin/python

def merge(A, m, B, n):
    k = m + n -1
    i = m - 1
    j = n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    return A

A = [1,2,5]
B = [4,6]
print merge(A, 3, B, 2)
