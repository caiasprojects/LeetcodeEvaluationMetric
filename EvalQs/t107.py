
from sol.x107 import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case 1
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root = None
assert solution.levelOrderBottom(root) == []

# Test case 3: Tree with only one node
root = TreeNode(1)
assert solution.levelOrderBottom(root) == [[1]]

# Test case 4: Tree with two levels
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert solution.levelOrderBottom(root) == [[2, 3], [1]]
