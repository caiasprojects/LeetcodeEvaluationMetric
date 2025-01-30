from sol.x1007 import Solution 
from sol.x1007 import Solution 
from typing import List
# Generated new fixed Code

import timeit
from sol.x1007 import Solution 
from typing import List

# Test case
solution = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

# Check if the result matches the expected output
assert solution.minDominoRotations(A, B) == 2

# Define the function to time
def timed_function():
    return solution.minDominoRotations(A, B)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test

# print("Time taken:", time_taken, "seconds")
