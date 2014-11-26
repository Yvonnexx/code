#!/usr/bin/python

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

    def copyRandomList(self, head):
        if not head:
            return None
        curr = head
        while curr:
            newnode = RandomListNode(curr.label)
            newnode.next = curr.next
            curr.next = newnode
            curr = curr.next.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        newhead = head.next
        pold = head
        pnew = newhead 
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead

if __name__ == "__main__":
    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    d = RandomListNode(4)
    a.next = b
    b.next = c
    c.next = d
    a.random = c
    b.random = d
    s = Solution()
    result = s.copyRandomList(a)
    while result:
        print result.label
        result = result.next
