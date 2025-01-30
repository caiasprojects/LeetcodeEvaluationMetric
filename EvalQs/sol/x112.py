



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, 0)]  # Use a stack to store nodes and their current sum
        while stack:
            node, current_sum = stack.pop()
            if not node:
                continue

            if not node.left and not node.right and current_sum == sum:
                return True

            if node.left:
                stack.append((node.left, current_sum + node.left.val))
            if node.right:
                stack.append((node.right, current_sum + node.right.val))

        return False