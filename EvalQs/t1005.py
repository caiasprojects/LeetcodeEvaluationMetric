from sol.x1005 import Solution 
from sol.x1005 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1005 import Solution 
from typing import List
import heapq
import timeit


# Test case 1
solution = Solution()
A = [4, 2, 3]
K = 1
assert solution.largestSumAfterKNegations(A, K) == 5

# Define and time the function
def timed_function():
    return solution.largestSumAfterKNegations(A, K)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")
