#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorder(self, root):
        first = []
        second = []
        first.append(root)
        while first:
            b = first.pop()
            second.append(b)
            if b.left:
                first.append(b.left)
            if b.right:
                first.append(b.right)
        return second[::-1]

    def postorderTraversal(self, root):
        result = []
        stack = []
        prev = None
        curr = root
        if not root:
            return result
        stack.append(root)
        while stack:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            else:
                result.append(curr.val)
                stack.pop()
            prev = curr
        return result
    
if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    s = Solution()
    print s.postorderTraversal(a)
    print s.postorder(a)
