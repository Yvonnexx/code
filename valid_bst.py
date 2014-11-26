#!/usr/bin/python
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    def isValidBST(self, root):
        def validBST(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return validBST(root.left, min, root.val) and validBST(root.right, root.val, max)
        return validBST(root, None, None) 
    """
    def isValidBST(self, root):
        return self.is_increasing(root)

    def is_increasing(self, root):
        prev = None
        if not root:
            return True
        if self.is_increasing(root.left):
            if prev and root.val <= prev.val:
                return False
            prev = root 
            return self.is_increasing(root.right)
        return False
    

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

print s.isValidBST(a)
