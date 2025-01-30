
# Generated Timing Code
from sol.x242 import Solution
# Test case 1
solution = Solution()
s = "anagram"
t = "nagaram"
assert solution.isAnagram(s, t) == True

# Test case 2
s = "rat"
t = "car"
assert solution.isAnagram(s, t) == False

# Test case 3
s = "abc"
t = "cba"
assert solution.isAnagram(s, t) == True

# Test case 4
s = "aabbcc"
t = "aabbcc"
assert solution.isAnagram(s, t) == True

# Test case 5
s = "abc"
t = "abcd"
assert solution.isAnagram(s, t) == False

