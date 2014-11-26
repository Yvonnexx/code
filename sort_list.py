#!/usr/bin/python

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.findMiddle(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(5)
    c = ListNode(4)
    d = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    s = Solution()
    result = s.sortList(a)
    while result:
        print result.val
        result = result.next
