
from sol.x322 import Solution
# Test case 1
solution = Solution()
coins = [1, 2, 5]
amount = 11
assert solution.coinChange(coins, amount) == 3

# Test case 2
coins = [2]
amount = 3
assert solution.coinChange(coins, amount) == -1

# Test case 3
coins = [1]
amount = 0
assert solution.coinChange(coins, amount) == 0

# Test case 4
coins = [1]
amount = 1
assert solution.coinChange(coins, amount) == 1

# Test case 5
coins = [1]
amount = 2
assert solution.coinChange(coins, amount) == 2

