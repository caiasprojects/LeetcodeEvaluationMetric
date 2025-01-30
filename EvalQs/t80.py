
from sol.x80 import Solution
# Test case 1
solution = Solution()
nums1 = [1, 1, 1, 2, 2, 3]
expected_output1 = [1, 1, 2, 2, 3]  # After removing duplicates, valid elements are [1, 1, 2, 2, 3]
assert solution.removeDuplicates(nums1) == len(expected_output1)

# Test case 2
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
expected_output2 = [0, 0, 1, 1, 2, 3, 3]  # After removing duplicates, valid elements are [0, 0, 1, 1, 2, 3, 3]
assert solution.removeDuplicates(nums2) == len(expected_output2)

# Test case 3
nums3 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
expected_output3 = [1, 1, 2, 2, 3, 3]  # After removing duplicates, valid elements are [1, 1, 2, 2, 3, 3]
assert solution.removeDuplicates(nums3) == len(expected_output3)

# Test case 4
nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected_output4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # After removing duplicates, valid elements are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert solution.removeDuplicates(nums4) == len(expected_output4)

# Test case 5
nums5 = []
expected_output5 = []  # After removing duplicates, valid elements are []
assert solution.removeDuplicates(nums5) == len(expected_output5)

