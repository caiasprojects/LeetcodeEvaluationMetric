from sol.x869 import Solution 
import timeit

# Initialize the solution instance
solution = Solution()

# Define test cases in the format (N, expected_output)
test_cases = [
    (1024, True),       # 2^10 = 1024
    (1, True),          # 2^0 = 1
    (2, True),          # 2^1 = 2
    (4, True),          # 2^2 = 4
    (8, True),          # 2^3 = 8
    (16, True),         # 2^4 = 16
    (32, True),         # 2^5 = 32
    (64, True),         # 2^6 = 64
    (128, True),        # 2^7 = 128
    (256, True),        # 2^8 = 256
    (512, True),        # 2^9 = 512
    (2048, True),       # 2^11 = 2048
    (1023, False),      # Not a power of 2
    (1234, False),      # Not a power of 2
    (45, False),        # Not a power of 2
    (50, False),        # Not a power of 2
    (1025, False),      # Not a power of 2
    (12, False),        # Not a power of 2
    (64, True),         # Repeated for consistency
    (36, False),        # Not a power of 2
    (8192, True),       # 2^13 = 8192
    (8193, False),      # Not a power of 2
]

# Run and time all test cases
for i, (N, expected_output) in enumerate(test_cases):
    # Check if the result matches the expected output
    result = solution.reorderedPowerOf2(N)
    assert result == expected_output, f"Test case {i + 1} failed: Expected {expected_output}, but got {result}"
    

print("All test cases passed")
