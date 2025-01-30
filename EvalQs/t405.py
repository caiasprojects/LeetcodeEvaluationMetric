
# Generated Timing Code
from sol.x405 import Solution
# Generated Code
# Test case 1
solution = Solution()
num = 26
assert solution.toHex(num) == "1a"

# Test case 2
num = -1
assert solution.toHex(num) == "ffffffff"

# Test case 3
num = 0
assert solution.toHex(num) == "0"

