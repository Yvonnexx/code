#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return stack2[::-1]

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    root.right = a
    a.left = b
    print s.postorderTraversal(root)
