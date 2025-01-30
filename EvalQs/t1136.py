from sol.x1136 import Solution 
from sol.x1136 import Solution 
from typing import List, Tuple
 #This code will run the `minimumSemesters` function from the `Solution` class with the provided test case and print the time taken to run the function 10,000 times. The time taken is in seconds.
# Generated new fixed Code

from sol.x1136 import Solution 
from typing import List, Tuple
import collections
import timeit


# Test case 1
solution = Solution()
N = 3
relations = [(1,2),(2,3),(3,1)]
assert solution.minimumSemesters(N, relations) == -1

# Define and time the function
def timed_function():
    return solution.minimumSemesters(N, relations)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# # print("Time taken:", time_taken, "seconds")
