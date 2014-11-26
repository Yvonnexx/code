#!/usr/bin/python

def findMissing(vals, start, end):
    ranges = []
    prev = start - 1
    for i in range(len(vals)):
        if i == len(vals):
            curr = end + 1
        else:
            curr = vals[i]
        if curr - prev >= 2:
            ranges.append(getRange(prev+1, curr-1))
        prev = curr
    return ranges

def getRange(from, to):
    if 
