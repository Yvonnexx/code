#!/usr/bin/python
import collections

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res

def recursive_preorder(root):
    def recursive(root, list):
        if root:
            list.append(root.val)
            recursive(root.left, list)
            recursive(root.right, list)
    list  = []
    recursive(root, list)
    return list

def inorder(root):
    stack = []
    res = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res

def recursive_inorder(root):
    def recursive(root, list):
        if not root:
            return
        recursive(root.left, list)
        list.append(root.val)
        recursive(root.right, list)
    list = []
    recursive(root, list)
    return list

def postorder(root):
    stack1 = []
    stack2 = []
    stack1 = [root]
    while stack1:
        root = stack1.pop()
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
        stack2.append(root.val)
    return stack2[::-1]

def recursive_postorder(root):
    def recursive(root, list):
        if not root:
            return
        recursive(root.right, list)
        recursive(root.left, list)
        list.append(root.val)
    list = []
    recursive(root, list)
    return list

def levelorder(root):
    res = []
    if not root:
        return res 
    level = [root]
    while level:
        thislevel = []
        nextlevel = []
        for temp in level:
            thislevel.append(temp.val)
            if temp.left:
                nextlevel.append(temp.left)
            if temp.right:
                nextlevel.append(temp.right)
        res.append(thislevel)
        level = nextlevel
    return res

def level(root):
    list = []
    q = collections.deque()
    q.append(root)
    while q:
        node = q.popleft()
        list.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return list

    
if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    #print preorder(a)
    #print recursive_preorder(a)
    #print inorder(a)
    #print recursive_inorder(a)
    #print postorder(a)
    #print recursive_postorder(a)
    print levelorder(a)
    print level(a)
