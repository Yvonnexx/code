#!/usr/bin/python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next =None

class Solution:
    def rotateRight(self, head, k):
        if k == 0:
            return head
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
        curr.next = dummy.next
        step = count - (k%count)
        for i in range(step):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    k = 2
    s.rotateRight(a, k)
    """
    res = s.rotateRight(a,k)
    while res:
        print res.val
        res = res.next
    """
