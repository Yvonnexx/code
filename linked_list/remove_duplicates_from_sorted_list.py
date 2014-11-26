#!/usr/bin/python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        tmp = dummy.next
        while curr.next:
            while tmp.next and tmp.next.val == curr.next.val:
                tmp = tmp.next
            if tmp == curr.next:
                curr = curr.next
                tmp = curr.next
            else:
                curr.next = tmp.next
        return dummy.next
    




if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    result = s.deleteDuplicates(a)
    while result:
        print result.val
        result = result.next


