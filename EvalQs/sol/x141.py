

from collections import deque

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps
            if slow == fast:
                return True
        return False