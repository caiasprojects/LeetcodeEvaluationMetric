

from typing import List

class Solution:
    def searchBST(self, root, val):
        if root is None:  # Handle empty tree case
            return None

        if root.val == val:  # Found the value
            return root

        if val < root.val:  # Search in the left subtree
            return self.searchBST(root.left, val)
        else:  # Search in the right subtree
            return self.searchBST(root.right, val)