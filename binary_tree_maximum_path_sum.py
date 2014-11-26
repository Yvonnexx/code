#!/usr/bin/python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

 
class Solution:
    def maxPathSum(self, root):
        self.maxsum = float('-inf')
        self.maxpath(root)
        return self.maxsum

    def maxpath(self, root):
        if not root:
            return 0
        lsum = self.maxpath(root.left)
        rsum = self.maxpath(root.right)
        import pdb;pdb.set_trace()
        self.maxsum = max(self.maxsum, lsum+root.val+rsum)
        return max(root.val+lsum, root.val+rsum, 0)

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
print s.maxPathSum(a)
