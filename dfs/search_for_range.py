#!/usr/bin/python

def searchRange(A, target):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left+right)/2
        if A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
        else:
            list = [0, 0]
            if A[left] == target:
                list[0] = left
            if A[right] == target:
                list[1] = right
            for i in range(mid, right+1):
                if A[i] != target:
                    list[1] = i - 1
                    break
            for i in range(mid, left-1, -1):
                if A[i] != target:
                    list[0] = i + 1
                    break
            return list
    return [-1, -1]
A = [5, 7, 7, 8, 8, 10]
target = 8
print searchRange(A, target#!/usr/bin/python
        
        def searchRange(A, target):
        left = 0
        right = len(A) - 1
        while left < right:
        mid = (left+right)/2
        if A[mid] > target:
        right = mid - 1
    elif A[mid] < target:
    left = mid + 1
else:
list = [0, 0]
if A[left] == target:
list[0] = leftif A[right] == target:
list[1] = rightfor i in range(mid, right+1);
    if A[i] != target:
    list[1] = i - 1
    break
for i in range(mid, left-1, -1):
if A[i] != target:
list[0] =1
breakreturn list    return [-1, -1]
A = [5, 7, 7, 8, 8, 10]
target = 8
print searchRange(A, target))
