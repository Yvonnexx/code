#!/usr/bin/python

def MaxProd(A):
    if not A or len(A) == 0:
        return None
    length = len(A)
    maxtemp = mintemp = maxprod = A[0]
    for i in range(1, length):
        temp = [maxtemp*A[i], mintemp*A[i], A[i]]
        maxtemp = max(temp)
        mintemp = min(temp)
        maxprod = max(maxprod, maxtemp)
    return maxprod

if __name__ == "__main__":
    A = [-2, 3, -2, 4, 0, 5] 
    print MaxProd(A)

