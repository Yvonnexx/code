#!/usr/bin/python

def findMin(num):
    left = 0
    right = len(num) - 1
    length = len(num)
    if length == 1 or length == 2:
        return min(num[left], num[right])
    while left < right:
        mid = (left+right)/2
        if num[left] < num[right]:
            return num[left]
        if num[left] < num[mid]:
            left = mid+1
        elif num[left] == num[mid]:
            left += 1
        else:
            right = mid
    return num[left]

def find(num):
    if not num or len(num) == 1:
        return num[0]
    start = 0
    end = len(num) - 1
    while start < end:
        if num[start] < num[end]:
            return num[start]
        mid = start + (end - start)/2
        if num[start] <= num[mid]:
            start = mid + 1
        else:
            end = mid
    return num[start]

num = [4,5,6,7,0,1,2]
print findMin(num)
print find(num)
    
