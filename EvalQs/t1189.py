from sol.x1189 import Solution 
from sol.x1189 import Solution 
from typing import List
# Generated new fixed Code

import timeit
from sol.x1189 import Solution 
from typing import List

# Test case 1
solution = Solution()
t = "balloonballoonballoon"
expected_output = 3

# Check if the result matches the expected output
result = solution.maxNumberOfBalloons(t)
assert result == expected_output

# Time the function
time_taken = timeit.timeit(lambda: solution.maxNumberOfBalloons(t), number=10000)  # Change the number argument based on how many times you want to repeat the test

# # print("Time taken:", time_taken, "seconds")

# Test case 2
t = "loonbalxballpoon"
expected_output = 2

# Check if the result matches the expected output
result = solution.maxNumberOfBalloons(t)
assert result == expected_output

# Time the function
time_taken = timeit.timeit(lambda: solution.maxNumberOfBalloons(t), number=10000)  # Change the number argument based on how many times you want to repeat the test

# # print("Time taken:", time_taken, "seconds")

# Test case 3
t = "leetcode"
expected_output = 0

# Check if the result matches the expected output
result = solution.maxNumberOfBalloons(t)
assert result == expected_output

# Time the function
time_taken = timeit.timeit(lambda: solution.maxNumberOfBalloons(t), number=10000)  # Change the number argument based on how many times you want to repeat the test

# # print("Time taken:", time_taken, "seconds")
