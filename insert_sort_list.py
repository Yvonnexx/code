#!/usr/bin/python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val :
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next

if __name__ == "__main__":
    a = ListNode(7)
    b = ListNode(5)
    c = ListNode(4)
    d = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    s = Solution()
    result = s.insertSortList(a)
    while result:
        print result.val
        result = result.next
