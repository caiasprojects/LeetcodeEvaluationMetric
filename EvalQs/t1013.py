from sol.x1013 import Solution 
from sol.x1013 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1013 import Solution 
from typing import List
import timeit

# Test case
solution = Solution()
A = [1,2,3,3]

# Define the function to time
def timed_function():
    return solution.canThreePartsEqualSum(A)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test

# print("Time taken:", time_taken, "seconds")

# Check if the result matches the expected output
assert solution.canThreePartsEqualSum(A) == True

print("All test cases pass")
