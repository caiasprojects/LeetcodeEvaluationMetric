from sol.x29 import Solution
# Test case 1
solution = Solution()
dividend = 10
divisor = 3
assert solution.divide(dividend, divisor) == 3

# Test case 2
dividend = 100
divisor = 10
assert solution.divide(dividend, divisor) == 10

# Test case 3
dividend = 100
divisor = -10
assert solution.divide(dividend, divisor) == -10

# Test case 4
dividend = -100
divisor = 10
assert solution.divide(dividend, divisor) == -10

# Test case 5
dividend = 10
divisor = 0
assert solution.divide(dividend, divisor) == 0x7fffffff

# Test case 6
dividend = 0
divisor = 10
assert solution.divide(dividend, divisor) == 0

