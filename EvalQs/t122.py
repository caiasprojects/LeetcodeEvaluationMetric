
from sol.x122 import Solution
# Test case 1
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
assert solution.maxProfit(prices) == 7

# Test case 2
prices = [1, 2, 3, 4, 5]
assert solution.maxProfit(prices) == 4

# Test case 3
prices = [5, 4, 3, 2, 1]
assert solution.maxProfit(prices) == 0

# Test case 4
prices = []
assert solution.maxProfit(prices) == 0

# Test case 5
prices = [1]
assert solution.maxProfit(prices) == 0


