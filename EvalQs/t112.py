
# Generated Timing Code
 
from sol.x112 import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case 1
solution = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
target_sum = 22
assert solution.hasPathSum(root, target_sum) == True

# Test case 2: Empty tree
root = None
assert solution.hasPathSum(root, target_sum) == False

# Test case 3: Tree with single node
root = TreeNode(5)
assert solution.hasPathSum(root, target_sum) == False
