from sol.x17 import Solution
# Test case 1
solution = Solution()
digits = "23"
assert solution.letterCombinations(digits) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# Test case 2
digits = ""
assert solution.letterCombinations(digits) == []

# Test case 3
digits = "2"
assert solution.letterCombinations(digits) == ["a", "b", "c"]


