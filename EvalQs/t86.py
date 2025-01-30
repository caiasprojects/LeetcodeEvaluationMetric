
from sol.x86 import Solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Test case 1
solution = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
x = 3
expected_output = [1, 2, 2, 4, 3, 5] 
solution = Solution()
head = ListNode(1)
x = 0
expected_output = [1] 
solution = Solution()
head = ListNode(2)
head.next = ListNode(1)
x = 2
expected_output = [1, 2]

