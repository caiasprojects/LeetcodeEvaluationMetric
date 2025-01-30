from sol.x1190 import Solution 
# Generated new fixed Code

import timeit

# Test case
solution = Solution()
s = "(abcd)"
assert solution.reverseParentheses(s) == "dcba"

s = "(u(love)i)"
assert solution.reverseParentheses(s) == "iloveu"

s = "(ed(et(oc))el)"
assert solution.reverseParentheses(s) == "leetcode"

s = "a(bcdefghijkl(mno)p)q"
assert solution.reverseParentheses(s) == "apmnolkjihgfedcbq"

# Define the function to time
def timed_function(s):
    return solution.reverseParentheses(s)

# Time the function
time_taken = timeit.timeit(lambda: timed_function(s), number=10000)  # Change the number argument based on how many times you want to repeat the test

# # print("Time taken:", time_taken, "seconds")
