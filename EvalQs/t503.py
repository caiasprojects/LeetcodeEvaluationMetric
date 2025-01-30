
from sol.x503 import Solution 
from typing import List

# Test case 1
solution = Solution()
nums = [1,2,1]
expected_output = [2,-1,2]


# Check if the result matches the expected output
assert solution.nextGreaterElements(nums) == expected_output

# Test case 2
solution = Solution()
nums = [1,2,3,4,3]
expected_output = [2,3,4,-1,4]


# Check if the result matches the expected output
assert solution.nextGreaterElements(nums) == expected_output

# Test case 3
solution = Solution()
nums = [5,4,3,2,1]
expected_output = [-1,5,5,5,5]


# Check if the result matches the expected output
assert solution.nextGreaterElements(nums) == expected_output

# Test case 4
solution = Solution()
nums = []
expected_output = []


# Check if the result matches the expected output
assert solution.nextGreaterElements(nums) == expected_output
