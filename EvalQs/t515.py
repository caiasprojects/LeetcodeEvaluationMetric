
from sol.x515 import Solution
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(9)

# Test case 2
root2 = TreeNode(1)
root2.left = TreeNode(2)

# Test case 3
root3 = TreeNode(1)

# Test case 4
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.right = TreeNode(5)
root4.right.left = TreeNode(6)
root4.right.right = TreeNode(7)

solution = Solution()

# Check if the result matches the expected output
assert solution.largestValues(root1) == [1, 3, 9]
assert solution.largestValues(root2) == [1, 2]
assert solution.largestValues(root3) == [1]
assert solution.largestValues(root4) == [1, 3, 7]

