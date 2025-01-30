



class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> list[int]:
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create a Solution object
solution = Solution()

# Perform inorder traversal
inorder_traversal = solution.inorderTraversal(root)

# Print the inorder traversal
print(inorder_traversal)  # Output: [1, 3, 2]