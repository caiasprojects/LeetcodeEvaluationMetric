from sol.x1020 import Solution 
 #Here is  a Python script that times the execution of the `numEnclaves` method from the `Solution` class in the `x1020` module. The script uses the `timeit` module to measure the execution time of the method.
from sol.x1020 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1020 import Solution 
from typing import List
import timeit

# Test case 1
solution = Solution()
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
assert solution.numEnclaves(A) == 3

# Define and time the function
def timed_function():
    return solution.numEnclaves(A)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")
