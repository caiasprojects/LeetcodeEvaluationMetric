
from sol.x865 import Solution 

# Test case 1
solution = Solution()
s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3

# Test case 2
s = "bbbbbb"
assert solution.lengthOfLongestSubstring(s) == 1

# Test case 3
s = "pwwkew"
assert solution.lengthOfLongestSubstring(s) == 3

# Test case 4
s = ""
assert solution.lengthOfLongestSubstring(s) == 0

# Test case 5
s = " "
assert solution.lengthOfLongestSubstring(s) == 1

