
# Generated Timing Code
from sol.x228 import Solution
# Generated Code
# Test case 1
solution = Solution()
nums = [0, 1, 2, 4, 5, 7]
expected_output = ["0->2", "4->5", "7"]
assert solution.summaryRanges(nums) == expected_output

# Test case 2
nums = []
expected_output = []
assert solution.summaryRanges(nums) == expected_output

# Test case 3
nums = [0]
expected_output = ["0"]
assert solution.summaryRanges(nums) == expected_output

