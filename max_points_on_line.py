#!/usr/bin/python

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

class Solution:
    #@param points, a list of points
    #@param an integer
    def maxPoints(self, points):
        if len(points) <= 1:
            return len(points)
        maxpoints = 1
        for i in range(len(points)):
            virtical = 1
            slops = {}
            samepoints = 0
            curmax = 1
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samepoints += 1
                elif points[i].x == points[j].x:
                    virtical += 1
                else:
                    slop = (points[j].y-points[i].y)*1.0/(points[j].x-points[i].x)
                    slops.setdefault(slop, 1)
                    slops[slop] += 1
                    if slops[slop] > curmax:
                        curmax = slops[slop]
            maxpoints = max(max(curmax, virtical)+samepoints, maxpoints)
        return maxpoints

s = Solution()
p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(3,4)
p4 = Point(1,1)
points = [p1, p2, p3, p4]
print s.maxPoints(points)
