from sol.x1006 import Solution 
from sol.x1006 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1006 import Solution 
from typing import List
import timeit

# Test case 1
solution = Solution()
N = 10
assert solution.clumsy(N) == 12

# Define and time the function
def timed_function():
    return solution.clumsy(N)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")
