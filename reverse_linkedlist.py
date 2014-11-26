#!/usr/bin/python

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorder(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = head.next
        head.next = None
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    s = Solution()
    result = s.reorder(a)
    while result:
        print result.val
        result = result.next
