from sol.x999 import Solution 
# Generated new fixed Code

import timeit

# Test case
solution = Solution()
board = [[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Define the function to time
def timed_function():
    return solution.numRookCaptures(board)

# Time the function
time_taken = timeit.timeit(timed_function, number=10000)  # Change the number argument based on how many times you want to repeat the test

# print("Time taken:", time_taken, "seconds")

# Check if the result matches the expected output
assert solution.numRookCaptures(board) == 1

print("All test cases pass")
