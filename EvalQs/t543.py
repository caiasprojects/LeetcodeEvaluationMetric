
from sol.x543 import Solution, TreeNode
# Test case 1
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

assert solution.diameterOfBinaryTree(root) == 3, "Test Case 1 Failed"

# Test case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solution.diameterOfBinaryTree(root) == 4, "Test Case 2 Failed"

# Test case 3
root = TreeNode(1)
assert solution.diameterOfBinaryTree(root) == 0, "Test Case 3 Failed"
