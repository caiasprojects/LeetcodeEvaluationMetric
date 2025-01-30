from sol.x85 import Solution
import timeit

# Initialize the solution instance
solution = Solution()

# Define test cases in the format (matrix, expected_output)
test_cases = [
    # Original test case
    ([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ], 6),  # Expected output: 6

    # Test case 2: Simple rectangle
    ([
        ["1", "1"],
        ["1", "1"]
    ], 4),  # Expected output: 4

    # Test case 3: No rectangles
    ([
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ], 0),  # Expected output: 0

    # Test case 4: One row of ones
    ([
        ["1", "1", "1", "1"]
    ], 4),  # Expected output: 4

    # Test case 9: Edge case with one element
    ([
        ["1"]
    ], 1),  # Expected output: 1

    # Test case 10: Full matrix of ones
    ([
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ], 9)   # Expected output: 9
]

# Run and time all test cases
for i, (matrix, expected_output) in enumerate(test_cases):
    # Check if the result matches the expected output
    result = solution.maximalRectangle(matrix)
    assert result == expected_output, f"Test case {i + 1} failed: Expected {expected_output}, but got {result}"
    
print("All test cases passed")
