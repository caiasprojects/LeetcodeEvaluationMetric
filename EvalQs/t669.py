
from sol.x669 import Solution 
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test case 1
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
L = 1
R = 2


# Check if the result matches the expected output
result = solution.trimBST(root, L, R)
expected_output = TreeNode(1)
expected_output.right = TreeNode(2)

while result and expected_output:
    assert result.val == expected_output.val
    result = result.right if result.right else None
    expected_output = expected_output.right if expected_output.right else None 
    
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
L = 1
R = 3


# Check if the result matches the expected output
result = solution.trimBST(root, L, R)
expected_output = TreeNode(3)
expected_output.left = TreeNode(2)
expected_output.left.left = TreeNode(1)

while result and expected_output:
    assert result.val == expected_output.val
    result = result.right if result.right else None
    expected_output = expected_output.right if expected_output.right else None

