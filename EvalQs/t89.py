
from sol.x89 import Solution
# Generated Code
# Test case 1
solution = Solution()
n = 2
assert solution.grayCode(n) == [0, 1, 3, 2]

# Test case 2
n = 3
assert solution.grayCode(n) == [0, 1, 3, 2, 6, 7, 5, 4]

# Test case 3
n = 4
assert solution.grayCode(n) == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
