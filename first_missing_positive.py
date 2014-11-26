#!/usr/bin/python

def firstMissing(A):
    if len(A) == 0:
        return 0
    for i in range(len(A)):
        while A[i] != i+1:
            if A[i] <= 0 or A[i] > len(A) or A[i] == A[A[i]-1]:
                break
            temp = A[A[i]-1]
            A[A[i]-1] = A[i] 
            A[i] = temp
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1
    return len(A) + 1

A = [3,4,5]
print firstMissing(A)
