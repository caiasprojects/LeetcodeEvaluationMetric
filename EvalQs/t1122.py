from sol.x1122 import Solution 
 #Here is  a Python script that you can use to time the execution of the `relativeSortArray` function from the `Solution` class. This script uses the `timeit` module to measure the execution time of the function.
from sol.x1122 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1122 import Solution 
from typing import List

# Test case 1
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
expected_output = [2,2,2,1,4,3,3,9,6,7,19]

# Define the function to time
def timed_function():
    return solution.relativeSortArray(arr1, arr2)

# Time the function
import timeit
time_taken = timeit.timeit(timed_function, number=10000)

# Check if the result matches the expected output
result = timed_function()
assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases pass")
# print("Time taken:", time_taken, "seconds")
