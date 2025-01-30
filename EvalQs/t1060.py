from sol.x1060 import Solution 

# Test case 1
solution = Solution()
nums = [4,7,9,10]
k = 1
expected_output = 5

assert solution.missingElement(nums, k) == expected_output

# Test case 2
nums = [4,7,9,10]
k = 3
expected_output = 8

assert solution.missingElement(nums, k) == expected_output

# Test case 3
nums = [1,2,4]
k = 3
expected_output = 6

assert solution.missingElement(nums, k) == expected_output
