
from sol.x148 import Solution

# Test case 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
solution = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
sorted_head = solution.sortList(head)
assert sorted_head.val == 1
assert sorted_head.next.val == 2
assert sorted_head.next.next.val == 3
assert sorted_head.next.next.next.val == 4

# Test case 2: empty list
head = None
sorted_head = solution.sortList(head)
assert sorted_head == None

# Test case 3: list with one node
head = ListNode(1)
sorted_head = solution.sortList(head)
assert sorted_head.val == 1

# Test case 4: list with duplicate values
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
sorted_head = solution.sortList(head)
assert sorted_head.val == 2
assert sorted_head.next.val == 2
assert sorted_head.next.next.val == 3
assert sorted_head.next.next.next.val == 4

