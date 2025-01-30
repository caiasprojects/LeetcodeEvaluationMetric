
# Generated Timing Code
from sol.x123 import Solution
# Generated Code
# Test case 1
solution = Solution()
prices = [3,3,5,0,0,3,1,4]
assert solution.maxProfit(prices) == 6

# Test case 2
prices = [1,2,3,4,5]
assert solution.maxProfit(prices) == 4

# Test case 3
prices = [7,6,4,3,1]
assert solution.maxProfit(prices) == 0

# Test case 4
prices = [1,2,4,2,5,7,2,4,9,0]
assert solution.maxProfit(prices) == 13

# Test case 5
prices = []
assert solution.maxProfit(prices) == 0

