
from sol.x78 import Solution
# Test case 1
solution = Solution()
nums = [1, 2, 3]
expected_output = [
    [],
    [1], [2], [3],
    [1, 2], [1, 3], [2, 3],
    [1, 2, 3]
]
assert sorted(solution.subsets(nums)) == sorted(expected_output)

# Test case 2
nums = [4, 5, 6]
expected_output = [
    [],
    [4], [5], [6],
    [4, 5], [4, 6], [5, 6],
    [4, 5, 6]
]
assert sorted(solution.subsets(nums)) == sorted(expected_output)

# Test case 3
nums = [7, 8, 9]
expected_output = [
    [],
    [7], [8], [9],
    [7, 8], [7, 9], [8, 9],
    [7, 8, 9]
]
assert sorted(solution.subsets(nums)) == sorted(expected_output)

