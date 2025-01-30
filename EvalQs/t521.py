
from sol.x521 import Solution
# Generated Code
# Test case 1
solution = Solution()
a = "aba"
b = "cdc"
assert solution.findLUSlength(a, b) == 3

# Test case 2
a = "abc"
b = "abc"
assert solution.findLUSlength(a, b) == -1

# Test case 3
a = "abc"
b = "def"
assert solution.findLUSlength(a, b) == 3

# Test case 4
a = "abcde"
b = "abc"
assert solution.findLUSlength(a, b) == 5

# Test case 5
a = "abc"
b = "abcde"
assert solution.findLUSlength(a, b) == 5


