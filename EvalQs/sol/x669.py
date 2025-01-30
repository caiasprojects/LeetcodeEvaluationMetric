

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        # Recursively trim the left subtree if the current node's value is outside the range
        if root.val < L:
            return self.trimBST(root.right, L, R)
        # Recursively trim the right subtree if the current node's value is outside the range
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # If the current node's value is within the range, return the node itself
        return root