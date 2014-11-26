#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedArrayToBST(self, num):
        return self.createBST(num, 0, len(num)-1)

    def createBST(self, num, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        root =TreeNode(num[mid])
        root.left = self.createBST(num, 0, mid-1)
        root.right = self.createBST(num, mid+1, end)
        return root

if __name__ == "__main__":
    s = Solution()
    num = [1,2,3]
    result = s.sortedArrayToBST(num)
    print result.val
