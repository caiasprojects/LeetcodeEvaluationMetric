
from sol.x495 import Solution
# Generated Code
# Test case 1
solution = Solution()
timeSeries = [1, 4]
duration = 2
assert solution.findPoisonedDuration(timeSeries, duration) == 4

# Test case 2
timeSeries = [1, 2]
duration = 2
assert solution.findPoisonedDuration(timeSeries, duration) == 3

# Test case 3
timeSeries = [1, 2, 3, 4, 5]
duration = 5
assert solution.findPoisonedDuration(timeSeries, duration) == 9

# Test case 4
timeSeries = [1, 2, 3, 4, 5]
duration = 1
assert solution.findPoisonedDuration(timeSeries, duration) == 5

# Test case 5
timeSeries = []
duration = 10
assert solution.findPoisonedDuration(timeSeries, duration) == 0

