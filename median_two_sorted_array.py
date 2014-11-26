#!/usr/bin/python

class Solution:
    # @return a float
    def findMedianSortedArray(self, A, B):
        length = len(A) + len(B)
        if length % 2:
            return self.getmedian(A,B,length/2+1)
        else:
            return 0.5*(self.getmedian(A,B,length/2)+self.getmedian(A,B,length/2+1))

    def getmedian(self, A, B, k):
        if len(A) > len(B):
            return self.gemedian(B,A,k)
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k/2, len(A))
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self.getmedian(A[pa:], B, k-pa)
        else:
            return self.getmedian(A, B[pb:], k-pb)

if __name__ == "__main__":
    s = Solution()
    A = [1,2,3,5]
    B = [1,6,8,10]
    print s.findMedianSortedArray(A, B)
