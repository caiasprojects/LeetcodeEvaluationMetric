from sol.x61 import Solution

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Test case setup
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2

# Assert the rotated list values
rotated_head = solution.rotateRight(head, k)
assert rotated_head.val == 4
assert rotated_head.next.val == 5
assert rotated_head.next.next.val == 1
assert rotated_head.next.next.next.val == 2
assert rotated_head.next.next.next.next.val == 3

