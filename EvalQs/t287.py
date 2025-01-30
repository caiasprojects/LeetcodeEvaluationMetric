
from sol.x287 import Solution 
solution = Solution()

# Check if the result matches the expected output
assert solution.findDuplicate([1,3,4,2,2]) == 2
assert solution.findDuplicate([3,1,3,4,2]) == 3
assert solution.findDuplicate([1,1,1,1,1]) == 1


# Check if the result matches the expected output for edge cases
assert solution.findDuplicate([3,1,3,4,2,2,2]) == 2
assert solution.findDuplicate([1,1,1,1,1,1,1]) == 1
