
from sol.x696 import Solution 

# Test case
solution = Solution()
s = "00110"
assert solution.countBinarySubstrings(s) == 3

# Additional test cases
s = "10101"
assert solution.countBinarySubstrings(s) == 4

s = "11111"
assert solution.countBinarySubstrings(s) == 0

s = "01010"
assert solution.countBinarySubstrings(s) == 4

