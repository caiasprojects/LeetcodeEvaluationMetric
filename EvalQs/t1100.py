from sol.x1100 import Solution 
from sol.x1100 import Solution 
from typing import List
# Generated new fixed Code

from sol.x1100 import Solution 
from typing import List
import collections
import timeit



# Test case 1
solution = Solution()
S = "havefunonleetcode"
K = 5
expected_output = 6

result = solution.numKLenSubstrNoRepeats(S, K)
assert result == expected_output, f"Expected {expected_output} but got {result}"

# Define the function to time
def timed_function():
    return solution.numKLenSubstrNoRepeats(S, K)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test

# print("Time taken:", time_taken, "seconds")
