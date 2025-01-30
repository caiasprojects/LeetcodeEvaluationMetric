
from sol.x273 import Solution 
from typing import List

# Test case 1
solution = Solution()
num = 123
assert solution.numberToWords(num) == "One Hundred Twenty Three"

# Test case 2
num = 12345
assert solution.numberToWords(num) == "Twelve Thousand Three Hundred Forty Five"

# Test case 3
num = 1234567
assert solution.numberToWords(num) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Test case 4
num = 0
assert solution.numberToWords(num) == "Zero"

# Test case 5
num = 1000000
assert solution.numberToWords(num) == "One Million"

