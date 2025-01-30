
from sol.x226 import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case 1
solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

assert solution.invertTree(root) == root

# Test case 2: Empty tree
assert solution.invertTree(None) == None

# Test case 3: Tree with only one node
root = TreeNode(1)
assert solution.invertTree(root) == root

# Test case 4: Tree with two levels
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert solution.invertTree(root) == root
