
from sol.x323 import Solution 
from typing import List
import collections

# Test case
solution = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
assert solution.countComponents(n, edges) == 2

# Additional test case
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
assert solution.countComponents(n, edges) == 1

# Test case with all nodes connected
n = 5
edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
assert solution.countComponents(n, edges) == 1

# Test case with no edges
n = 5
edges = []
assert solution.countComponents(n, edges) == 5

