#!/usr/bin/python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedListToBST(self, head):
        num = []
        curr = head
        while curr:
            num.append(curr.val)
            curr = curr.next
        return self.create(num, 0, len(num)-1)
    
    def create(self, num, start, end):
        if start > end:
            return None
        mid = (start + end)/2
        root = TreeNode(num[mid])
        root.left = self.create(num, start, mid-1)
        root.right = self.create(num, mid+1, end)
        return root

if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    c = ListNode(3)
    a.next = c
    result = s.sortedListToBST(a)
    print result.val
