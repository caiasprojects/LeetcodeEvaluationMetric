

from typing import List
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:  # Both trees are empty
            return None

        if not t1:  # t1 is empty
            return t2
        if not t2:  # t2 is empty
            return t1

        # Create a new node with the sum of values
        root = TreeNode(t1.val + t2.val)

        # Recursively merge the left subtrees
        root.left = self.mergeTrees(t1.left, t2.left)

        # Recursively merge the right subtrees
        root.right = self.mergeTrees(t1.right, t2.right)

        return root