
from sol.x141 import Solution

# Test case 1
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

solution = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

assert solution.hasCycle(head) == True

# Test case 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
assert solution.hasCycle(head) == False

# Test case 3
head = ListNode(1)
assert solution.hasCycle(head) == False

# Test case 4
head = ListNode(1)
head.next = head
assert solution.hasCycle(head) == True

