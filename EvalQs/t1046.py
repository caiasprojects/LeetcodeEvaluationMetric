from sol.x1046 import Solution 
from sol.x1046 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1046 import Solution 
from typing import List
import bisect
import timeit


# Test case 1
solution = Solution()
stones = [2,7,4,1,8,1]
assert solution.lastStoneWeight(stones) == 1

# Define and time the function
def timed_function():
    return solution.lastStoneWeight(stones)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")
