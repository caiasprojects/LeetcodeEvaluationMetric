from sol.x1160 import Solution 
from sol.x1160 import Solution 
from collections import Counter as cnt
from typing import List
# Generated new fixed Code

import timeit
from sol.x1160 import Solution 
from collections import Counter as cnt
from typing import List

# Test case 1
solution = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
expected_output = 6

# Run the function and check the result
result = solution.countCharacters(words, chars)
assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Define the function to time
def timed_function():
    return solution.countCharacters(words, chars)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test

# # print("Time taken:", time_taken, "seconds")
