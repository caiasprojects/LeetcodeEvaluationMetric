
from sol.x695 import Solution 

# Test case 1
solution = Solution()
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

# Check if the result matches the expected output
assert solution.maxAreaOfIsland(grid) == 6

# Test case 2
grid = [
  [0,0,0,0,0,0,0,0]
]

# Check if the result matches the expected output
assert solution.maxAreaOfIsland(grid) == 0

# Test case 3
grid = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]

# Check if the result matches the expected output
assert solution.maxAreaOfIsland(grid) == 4

