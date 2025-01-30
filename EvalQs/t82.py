
from sol.x82 import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Method to convert ListNode to list for comparison
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

# Test case 1
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

expected_output = ListNode(1)
expected_output.next = ListNode(2)
expected_output.next.next = ListNode(5)

# Define a function to compare two linked lists by converting to lists
def compare_linked_lists(l1, l2):
    return l1.to_list() == l2.to_list()

assert compare_linked_lists(solution.deleteDuplicates(head), expected_output)



# Additional test case 2
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)

expected_output = ListNode(2)
expected_output.next = ListNode(3)

assert compare_linked_lists(solution.deleteDuplicates(head), expected_output)

# Additional test case 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

expected_output = ListNode(1)
expected_output.next = ListNode(2)
expected_output.next.next = ListNode(3)
expected_output.next.next.next = ListNode(4)
expected_output.next.next.next.next = ListNode(5)

assert compare_linked_lists(solution.deleteDuplicates(head), expected_output)
