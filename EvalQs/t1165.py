from sol.x1165 import Solution 
from sol.x1165 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1165 import Solution 
from typing import List
import timeit

# Test case 1
solution = Solution()
k = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
assert solution.calculateTime(k, word) == 73

# Define and time the function
def timed_function():
    return solution.calculateTime(k, word)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# # print("Time taken:", time_taken, "seconds")
