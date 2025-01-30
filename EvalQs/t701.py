from sol.x701 import Solution 
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Insert a value
solution.insertIntoBST(root, 5)

# Additional test cases
assert solution.insertIntoBST(None, 5).val == 5, "Failed on empty tree"
assert solution.insertIntoBST(TreeNode(5), 3).left.val == 3, "Failed on left insertion"
assert solution.insertIntoBST(TreeNode(5), 7).right.val == 7, "Failed on right insertion"
