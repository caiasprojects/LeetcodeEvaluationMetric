from sol.x1066 import Solution 
from sol.x1066 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1066 import Solution 
from typing import List
import heapq
import timeit


# Test case 1
solution = Solution()
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
assert solution.assignBikes(workers, bikes) == 6

# Define and time the function
def timed_function():
    return solution.assignBikes(workers, bikes)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")
