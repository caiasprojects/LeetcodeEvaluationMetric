from sol.x1209 import Solution 
from sol.x1209 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1209 import Solution 
from typing import List
import timeit

# Define the test case
solution = Solution()
s = "deeedbbcccbdaa"
k = 3
expected_output = "aa"

# Define and time the function
def timed_function():
    return solution.removeDuplicates(s, k)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)

# Check if the result matches the expected output
result = timed_function()
assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases pass")
