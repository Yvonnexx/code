#!/usr/bin/python

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def remove(self, target, head):
        curr = head
        prev = None
        while curr:
            if target == curr.val:
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head

s = Solution()
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
target = 1
res = s.remove(target, a)
while res:
    print res.val
    res = res.next
