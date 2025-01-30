
from sol.x733 import Solution 
from typing import List
import collections
# Test case
solution = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

# Check if the result matches the expected output
result = solution.floodFill(image, sr, sc, newColor)
assert result == [[2,2,2],[2,2,0],[2,0,1]]

# Additional test case
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
result = solution.floodFill(image, sr, sc, newColor)
assert result == [[0,0,0],[0,1,1]]

# Additional test case
image = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
newColor = 2
result = solution.floodFill(image, sr, sc, newColor)
assert result == [[0,0,0],[0,2,0]]

