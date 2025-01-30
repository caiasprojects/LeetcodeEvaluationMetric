
# Generated Timing Code

from sol.x94 import Solution
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
assert solution.inorderTraversal(root) == [1, 3, 2]

# Test case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
assert solution.inorderTraversal(root) == [2, 4, 1, 3]

# Test case 3
root = TreeNode(1)
assert solution.inorderTraversal(root) == [1]

# Test case 4
root = TreeNode(1)
root.left = TreeNode(2)
assert solution.inorderTraversal(root) == [2, 1]

# Test case 5
root = TreeNode(1)
root.right = TreeNode(2)
assert solution.inorderTraversal(root) == [1, 2]

