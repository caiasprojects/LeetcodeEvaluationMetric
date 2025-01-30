
from sol.x150 import Solution
# Test case 1
solution = Solution()
tokens = ["2", "1", "+", "3", "*"]
expected_output = 9


# Check if the output is correct
assert solution.evalRPN(tokens) == expected_output 
tokens = ["4", "13", "5", "/", "+"]
expected_output = 6
assert solution.evalRPN(tokens) == expected_output

# Test case 3
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
expected_output = 22
assert solution.evalRPN(tokens) == expected_output
