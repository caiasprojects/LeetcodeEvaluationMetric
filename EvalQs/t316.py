
from sol.x316 import Solution 
from typing import List
# Test case
solution = Solution()
s = "cbacdcbc"

# Test cases
assert solution.removeDuplicateLetters("cbacdcbc") == "acdb"
assert solution.removeDuplicateLetters("bcabc") == "abc"
assert solution.removeDuplicateLetters("bbcaac") == "bac"
assert solution.removeDuplicateLetters("edebbed") == "bed"
assert solution.removeDuplicateLetters("") == ""
