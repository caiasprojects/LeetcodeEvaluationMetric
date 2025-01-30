
from sol.x97 import Solution
# Generated Code
# Test case 1
solution = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
assert solution.isInterleave(s1, s2, s3) == True

# Test case 2
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
assert solution.isInterleave(s1, s2, s3) == False

# Test case 3
s1 = ""
s2 = ""
s3 = ""
assert solution.isInterleave(s1, s2, s3) == True

# Test case 4
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
assert solution.isInterleave(s1, s2, s3) == False

# Test case 5
s1 = "abc"
s2 = "def"
s3 = "adbecf"
assert solution.isInterleave(s1, s2, s3) == True

