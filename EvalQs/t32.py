from sol.x32 import Solution
# Test case 1
solution = Solution()
s = "(()"
assert solution.longestValidParentheses(s) == 2

# Test case 2
s = ")()())"
assert solution.longestValidParentheses(s) == 4

# Test case 3
s = ""
assert solution.longestValidParentheses(s) == 0

# Test case 4
s = "()(()"
assert solution.longestValidParentheses(s) == 2

# Test case 5
s = "()(()()("
assert solution.longestValidParentheses(s) == 4

