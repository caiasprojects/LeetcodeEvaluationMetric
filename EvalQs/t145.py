
from sol.x145 import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Test case 1
solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
assert solution.postorderTraversal(root) == [3, 2, 1]

# Test case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert solution.postorderTraversal(root) == [2, 3, 1]

# Test case 3
root = TreeNode(1)
assert solution.postorderTraversal(root) == [1]

# Test case 4
assert solution.postorderTraversal(None) == []

# Test case 5
root = TreeNode(1)
root.left = TreeNode(2)
assert solution.postorderTraversal(root) == [2, 1]

