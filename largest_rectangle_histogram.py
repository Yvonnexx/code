#!/usr/bin/python

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxarea = 0
        h = height + [0]
        length = len(h)
        while i < length:
            if not stack or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxarea = max(maxarea, h[t]*(i if not stack else i-stack[-1]-1))
        return maxarea

if __name__ =="__main__":
    s = Solution()
    height = [2,1,5,6,2,3]
    print s.largestRectangleArea(height)
