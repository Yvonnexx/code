#!/usr/bin/python

def binary_search(num, target):
    length = len(num)
    start = 0
    end = length - 1
    while start < end:
        mid = start + (end-start)/2
        if target > num[mid]:
            start = mid + 1
        else:
            end = mid
    return start

num = [1,2,3,4,5]
target = 3
print binary_search(num, target)
