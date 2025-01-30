from sol.x310 import Solution 
from typing import List 

solution = Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
expected_output = [1]


# Check if the result matches the expected output
result = solution.findMinHeightTrees(n, edges)

assert result == expected_output, f"Expected {expected_output}, but got {result}"
##print("All test cases pass")

# Test case 2
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
expected_output = [3, 4]

# Check if the result matches the expected output
result = solution.findMinHeightTrees(n, edges)
assert result == expected_output, f"Expected {expected_output}, but got {result}"
##print("All test cases pass")

# Test case 3
n = 1
edges = []
expected_output = [0]

result = solution.findMinHeightTrees(n, edges)
assert result == expected_output, f"Expected {expected_output}, but got {result}"
