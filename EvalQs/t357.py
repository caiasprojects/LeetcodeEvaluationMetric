
from sol.x357 import Solution
# Test case 1
solution = Solution()
n = 0
assert solution.countNumbersWithUniqueDigits(n) == 1

# Test case 2
n = 1
assert solution.countNumbersWithUniqueDigits(n) == 10

# Test case 3
n = 2
assert solution.countNumbersWithUniqueDigits(n) == 91

# Test case 4
n = 3
assert solution.countNumbersWithUniqueDigits(n) == 739

# Test case 5
n = 4
assert solution.countNumbersWithUniqueDigits(n) == 5275

# Test case 6
n = 5
assert solution.countNumbersWithUniqueDigits(n) == 32491

# Test case 7
n = 6
assert solution.countNumbersWithUniqueDigits(n) == 168571

# Test case 8
n = 7
assert solution.countNumbersWithUniqueDigits(n) == 712891

# Test case 9
n = 8
assert solution.countNumbersWithUniqueDigits(n) == 2345851

# Test case 10
n = 9
assert solution.countNumbersWithUniqueDigits(n) == 5611771

# Test case 11
n = 10
assert solution.countNumbersWithUniqueDigits(n) == 8877691
