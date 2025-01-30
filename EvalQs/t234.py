
# Generated Timing Code
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from sol.x234 import Solution

# Generated Code
# Test case 1
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
assert solution.isPalindrome(head) == True

# Test case 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
assert solution.isPalindrome(head) == True

# Test case 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
assert solution.isPalindrome(head) == False

# Test case 4
head = ListNode(1)
assert solution.isPalindrome(head) == True

# Test case 5
head = ListNode(1)
head.next = ListNode(1)
assert solution.isPalindrome(head) == True

# Test case 6
head = ListNode(1)
head.next = ListNode(2)
assert solution.isPalindrome(head) == False

