
from sol.x125 import Solution
# Generated Code
# Test case 1
solution = Solution()
s = "A man, a plan, a canal: Panama"
assert solution.isPalindrome(s) == True

# Test case 2
s = "race a car"
assert solution.isPalindrome(s) == False

# Test case 3
s = " "
assert solution.isPalindrome(s) == True

# Test case 4
s = "a."
assert solution.isPalindrome(s) == True

# Test case 5
s = "ab"
assert solution.isPalindrome(s) == False

# Test case 6
s = "abba"
assert solution.isPalindrome(s) == True

# Test case 7
s = "abcba"
assert solution.isPalindrome(s) == True

# Test case 8
s = "abcdcba"
assert solution.isPalindrome(s) == True

# Test case 9
s = "abcd"
assert solution.isPalindrome(s) == False

# Test case 10
s = "12321"
assert solution.isPalindrome(s) == True

# Test case 11
s = "12345"
assert solution.isPalindrome(s) == False

# Test case 12
s = "123321"
assert solution.isPalindrome(s) == True

