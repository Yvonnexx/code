#!/usr/bin/python

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def detectCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head
        while True:
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        while head != slow:
            slow = slow.next
            head = head.next
        return head

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = c
    s = Solution()
    print s.detectCycle(a).val
