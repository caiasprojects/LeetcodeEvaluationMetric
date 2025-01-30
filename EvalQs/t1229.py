from sol.x1229 import Solution 
from sol.x1229 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1229 import Solution 
from typing import List
import timeit

# Test case 1
solution = Solution()
s1 = [[10,50],[60,120],[140,210]]
s2 = [[0,15],[60,70]]
d = 8
expected_output = [60, 68]

# Define and time the function
def timed_function():
    return solution.minAvailableDuration(s1, s2, d)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)

# Check if the result matches the expected output
result = timed_function()
assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases pass")
