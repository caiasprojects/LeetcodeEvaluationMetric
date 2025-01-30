from sol.x1221 import Solution 
 #Here is  a Python script that can be used to test the `balancedStringSplit` function from the provided Solution class. It also includes timing code to measure the time taken by the function.
from sol.x1221 import Solution
# Generated new fixed Code

import timeit
from sol.x1221 import Solution

# Test case 1
solution = Solution()
s = "RLRRLLRLRL"
expected_output = 4

# Check if the result matches the expected output
result = solution.balancedStringSplit(s)
assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Define the function to time
def timed_function():
    return solution.balancedStringSplit(s)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test


print("All test cases pass")
