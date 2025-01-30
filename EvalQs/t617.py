from sol.x617 import Solution 
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

solution = Solution()

# Test case 
t1 = TreeNode(1)
t2 = TreeNode(1)
merged_tree = solution.mergeTrees(t1, t2)
assert merged_tree.val == 2
assert merged_tree.left is None
assert merged_tree.right is None

# Test case 
t1 = TreeNode(1)
t1.left = TreeNode(2)
t2 = TreeNode(1)
t2.right = TreeNode(2)
merged_tree = solution.mergeTrees(t1, t2)
assert merged_tree.val == 2
assert merged_tree.left.val == 2
assert merged_tree.right.val == 2
