#!/usr/bin/python

class Solution:
    def findMin(self, num):
        if not num or len(num) == 1:
            return num
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

if __name__ == "__main__":
    s = Solution()
    num2 = [1,2]
    num = [4,5,6,7,0,1,2]
    print s.findMin(num2)
