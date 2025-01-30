
from sol.x1054 import Solution 
from typing import List

# Test case
solution = Solution()
s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3

# Additional test cases
s = "bbbbbb"
assert solution.lengthOfLongestSubstring(s) == 1

s = "pwwkew"
assert solution.lengthOfLongestSubstring(s) == 3

