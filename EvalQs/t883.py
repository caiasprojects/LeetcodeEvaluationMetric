
from sol.x883 import Solution 
from typing import List
# Test case
solution = Solution()
grid = [[1,2],[3,4]]
expected_output = 17

result = solution.projectionArea(grid)
# Check if the result matches the expected output
assert result == expected_output, f"Expected {expected_output} but got {result}"
##print("All test cases pass")

# Additional test cases
grid = [[1,0],[0,2]]
expected_output = 8
result = solution.projectionArea(grid)
assert result == expected_output, f"Expected {expected_output} but got {result}"
##print("All test cases pass")

grid = [[1,1,1],[1,0,1],[1,1,1]]
expected_output = 14
result = solution.projectionArea(grid)
assert result == expected_output, f"Expected {expected_output} but got {result}"
##print("All test cases pass")
