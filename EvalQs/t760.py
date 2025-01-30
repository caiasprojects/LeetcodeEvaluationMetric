from sol.x760 import Solution 
from typing import List

# Test case
solution = Solution()
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
expected_output = [1, 4, 3, 2, 0]

result = solution.anagramMappings(A, B)

# Check if the result matches the expected output
assert result == expected_output

# Additional test case
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]
expected_output = [4, 3, 2, 1, 0]

result = solution.anagramMappings(A, B)

# Check if the result matches the expected output
assert result == expected_output

