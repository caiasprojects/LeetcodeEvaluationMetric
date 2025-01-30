
from sol.x700 import Solution 
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case
solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Test case 1: Value exists in the tree
assert solution.searchBST(root, 2).val == 2

# Test case 2: Value does not exist in the tree
assert solution.searchBST(root, 5) is None

# Test case 3: Value is the root of the tree
assert solution.searchBST(root, 4).val == 4

# Test case 4: Value is in the left subtree
assert solution.searchBST(root, 1).val == 1

# Test case 5: Value is in the right subtree
assert solution.searchBST(root, 7).val == 7

