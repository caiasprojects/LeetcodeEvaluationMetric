
from sol.x905 import Solution 
from typing import List
# Test case 1
solution = Solution()
A = [3, 1, 2, 4]
expected_output = [2, 4, 3, 1]

# Check if the result matches the expected output
result = solution.sortArrayByParity(A)
assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Test case 2
A = [1, 3, 5, 7]
expected_output = [1, 3, 5, 7]
result = solution.sortArrayByParity(A)
assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Test case 3
A = [2, 4, 6, 8]
expected_output = [2, 4, 6, 8]
result = solution.sortArrayByParity(A)
assert result == expected_output, f"Expected {expected_output}, but got {result}"

##print("All test cases pass")
