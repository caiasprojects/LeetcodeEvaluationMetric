

from typing import List

import timeit
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        # Use a binary search tree property: if the new value is less than the current node, go left, otherwise go right
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root