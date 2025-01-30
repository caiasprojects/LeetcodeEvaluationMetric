from sol.x1175 import Solution 
from sol.x1175 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1175 import Solution 
from typing import List
import bisect
import math
import timeit


# Test case 1
solution = Solution()
n = 5
assert solution.numPrimeArrangements(n) == 12

# Define and time the function
def timed_function():
    return solution.numPrimeArrangements(n)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# # print("Time taken:", time_taken, "seconds")
