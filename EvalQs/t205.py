
from sol.x205 import Solution
# Generated Code
# Test case 1
solution = Solution()
s = "egg"
t = "add"
assert solution.isIsomorphic(s, t) == True

# Test case 2
s = "foo"
t = "bar"
assert solution.isIsomorphic(s, t) == False

# Test case 3
s = "paper"
t = "title"
assert solution.isIsomorphic(s, t) == True

# Test case 4
s = "abcdefghijklmnopqrstuvwxyz"
t = "abcdefghijklmnopqrstuvwxyz"
assert solution.isIsomorphic(s, t) == True

# Test case 5
s = "abcdefghijklmnopqrstuvwxyzz"
t = "abcdefghijklmnopqrstuvwxyz"
assert solution.isIsomorphic(s, t) == False

