#!/usr/bin/python

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
def insert(intervals, newinterval):
    intervals.sort(key=lambda x: x.start)
    res = []
    length = len(intervals)
    for i in range(length):
        if res == []:
            res.append(intervals[i])
        else:
            size = len(res)
            if res[size-1].start <= intervals[i].start <= res[size-1].end:
                res[size-1].end = max(intervals[i].end, res[size-1].end)
            else:
                res.append(intervals[i])
    return res
"""
def insert(intervals, newinterval):
    intervals = intervals + [newinterval]
    intervals.sort(key=lambda x: x.start)
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        temp = stack[-1]
        if temp.end < intervals[i].start:
            stack.append(intervals[i])
        elif temp.end < intervals[i].end:
            temp.end = intervals[i].end
            stack.pop()
            stack.append(temp)
    return stack


interval1 = Interval(1,3)
interval2 = Interval(6,9)
intervals = [interval1, interval2]
interval3 = Interval(2,5)
newinterval = interval3
result = insert(intervals, newinterval)
for item in result:
    print str(item.start) + ' , ' + str(item.end)
