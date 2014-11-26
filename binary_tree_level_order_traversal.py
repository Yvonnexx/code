#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    res = []
    if not root:
        return res
    level = [root]
    while level:
        nextlevel = []
        thislevel = []
        for tmp in level:
            thislevel.append(tmp.val)
            if tmp.left:
                nextlevel.append(tmp.left)
            if tmp.right:
                nextlevel.append(tmp.right)
        res.append(thislevel)
        level = nextlevel
    return res


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

print levelOrder(a)
