
from sol.x130 import Solution
# Test case
solution = Solution()

# Test case 1
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
solution.solve(board)
assert board == [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]
]

# Test case 2
board = [
    ["O", "O", "O"],
    ["O", "O", "O"],
["O", "O", "O"]
]
solution.solve(board)
assert board == [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

# Test case 3
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
solution.solve(board)
assert board == [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]

