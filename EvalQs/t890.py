from sol.x890 import Solution 

# Initialize the solution instance

solution = Solution()

# Define test cases
test_cases = [
    (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),  # Correctly matches based on the pattern
    (["aba", "baa", "aab", "aaab", "bb", "cc"], "aa", ["bb", "cc"]),  # Matches based on the pattern
    (["xyz", "xzy", "zyx", "yyx"], "xxy", ["yyx"]),  # Correct matches for pattern
    (["abcdefg", "ghijklm", "mnopqrs", "tuvwxyz"], "abc", []),  # No matches with long patterns
    (["apple", "banana", "cherry", "date"], "xxyz", []),  # No matching patterns
]

# Run and check all test cases
for i, (words, pattern, expected_output) in enumerate(test_cases):
    result = solution.findAndReplacePattern(words, pattern)
    assert result == expected_output, f"Test case {i + 1} failed: Expected {expected_output}, but got {result}"

print("All test cases passed")
