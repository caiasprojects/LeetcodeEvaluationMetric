

from typing import List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head
        sHead = ListNode(-1)
        sDummy = sHead
        
        # Use two pointers to partition the list
        p = dummy
        q = dummy
        while p and p.next:
            if p.next.val < x:
                q.next = p.next
                p.next = p.next.next
                q = q.next
            else:
                p = p.next
        
        # Connect the two partitions
        q.next = dummy.next
        return sHead.next