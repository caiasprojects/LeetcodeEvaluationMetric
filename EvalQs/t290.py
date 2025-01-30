
from sol.x290 import Solution
# Test case 1
solution = Solution()
pattern = "abba"
str = "dog cat cat dog"
assert solution.wordPattern(pattern, str) == True

# Test case 2
pattern = "abba"
str = "dog cat cat fish"
assert solution.wordPattern(pattern, str) == False

# Test case 3
pattern = "abba"
str = "dog dog dog dog"
assert solution.wordPattern(pattern, str) == False

# Test case 4
pattern = "abcd"
str = "dog cat cat dog"
assert solution.wordPattern(pattern, str) == False

