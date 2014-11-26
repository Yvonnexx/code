#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        curr = root
        while curr:
            prev = None
            first_level_next = None
            while curr:
                if not first_level_next:
                    if curr.left:
                        first_level_next = curr.left
                    else:
                        first_level_next = curr.right
                if curr.left:
                    if prev:
                        prev.next = curr.left
                        prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                        prev = curr.right
                curr = curr.next
            curr = first_level_next
