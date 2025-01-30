
from sol.x168 import Solution
# Test case 1
solution = Solution()
n = 28
expected_output = "AB"


# Test case 2
n = 52
expected_output = "AZ"
assert solution.convertToTitle(n) == expected_output

# Test case 3
n = 702
expected_output = "ZZ"
assert solution.convertToTitle(n) == expected_output

# Test case 4
n = 1
expected_output = "A"
assert solution.convertToTitle(n) == expected_output

# Test case 5
n = 26
expected_output = "Z"
assert solution.convertToTitle(n) == expected_output

# Test case 6
n = 27
expected_output = "AA"
assert solution.convertToTitle(n) == expected_output

# Test case 7
n = 53
expected_output = "BA"
assert solution.convertToTitle(n) == expected_output

# Test case 8
n = 705
expected_output = "AAC"
assert solution.convertToTitle(n) == expected_output
