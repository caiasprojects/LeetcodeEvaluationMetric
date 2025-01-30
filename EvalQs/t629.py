
from sol.x629 import Solution
# Test case 1
solution = Solution()
n = 3
k = 0
assert solution.kInversePairs(n, k) == 1

# Test case 2
n = 3
k = 1
assert solution.kInversePairs(n, k) == 2

# Test case 3
n = 3
k = 2
assert solution.kInversePairs(n, k) == 2

# Test case 4
n = 3
k = 3
assert solution.kInversePairs(n, k) == 1

# Test case 5
n = 3
k = 4
assert solution.kInversePairs(n, k) == 0

