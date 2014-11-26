#!/usr/bin/python

class Solution():
    def singleNumber(self, A):
        if not A or len(A) == 0:
            return -1
        res = 0
        for i in xrange(len(A)):
            res ^= A[i]
            print res
        return res
    def singlenumber(self, A):
        if not A or len(A) == 0:
            return -1
        res = 0
        neg = 0
        for i in xrange(32):
            c = 0
            d = 1<<i
            for j in xrange(len(A)):
                if A[j] > 0:
                    tmpNum = A[j]
                else:
                    tmpNum = -A[j]
                if tmpNum & d:
                    c += 1
            if c % 3:
                res |= d
        for j in A:
            if j<0:
                neg += 1
        if neg % 3:
            res = -res
        return res

if __name__ == "__main__":
    s = Solution()
    A = [2,2,2,3]
    a = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print s.singlenumber(a)
