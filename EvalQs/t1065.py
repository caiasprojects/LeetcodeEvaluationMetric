from sol.x1065 import Solution 
from typing import List
from sol.x1065 import Solution 
# Generated new fixed Code

from typing import List
from sol.x1065 import Solution 
import timeit

# Test case 1
solution = Solution()
text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]
expected_output = [[3, 7], [9, 13], [10, 17]]

# Define and time the function
def timed_function():
    return solution.indexPairs(text, words)

# Time the test function
time_taken = timeit.timeit(timed_function, number=10000)
# print("Time taken:", time_taken, "seconds")

# Check if the result matches the expected output
result = timed_function()
assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases pass")
