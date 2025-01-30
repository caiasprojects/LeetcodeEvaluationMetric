# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.k = 0
        self.res = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = 0  # Reset k for each new call
        self.res = None  # Reset result for each new call
        self._inorder_traversal(root, k)
        return self.res

    def _inorder_traversal(self, node: TreeNode, k: int):
        if node is None:
            return

        if self.k < k:  # Traverse left
            self._inorder_traversal(node.left, k)

        self.k += 1  # Increment count
        if self.k == k:  # Found the k-th smallest
            self.res = node.val
            return

        if self.k < k:  # Traverse right
            self._inorder_traversal(node.right, k)
