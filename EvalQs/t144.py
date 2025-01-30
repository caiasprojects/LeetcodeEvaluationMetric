
from sol.x144 import Solution

# Test case 1
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
assert solution.preorderTraversal(root) == [1, 2, 3]

# Test case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert solution.preorderTraversal(root) == [1, 2, 3]

# Test case 3
root = TreeNode(1)
root.left = TreeNode(2)
assert solution.preorderTraversal(root) == [1, 2]

# Test case 4
root = TreeNode(1)
assert solution.preorderTraversal(root) == [1]

# Test case 5
assert solution.preorderTraversal(None) == []

