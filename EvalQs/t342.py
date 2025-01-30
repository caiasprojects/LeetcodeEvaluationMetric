
from sol.x342 import Solution
# Test case 1
solution = Solution()
num = 16
assert solution.isPowerOfFour(num) == True

# Test case 2
num = 64
assert solution.isPowerOfFour(num) == True

# Test case 3
num = 25
assert solution.isPowerOfFour(num) == False

# Test case 4
num = 0
assert solution.isPowerOfFour(num) == False

# Test case 5
num = -16
assert solution.isPowerOfFour(num) == False

