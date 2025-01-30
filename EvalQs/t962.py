
from sol.x962 import Solution 
from typing import List
import collections
# Test case
solution = Solution()
A = [9,8,1,0,1,9,4,0,4,1]
assert solution.maxWidthRamp(A) == 7

# Additional test case 1
A = [9,8,7,6,5,4,3,2,1]
assert solution.maxWidthRamp(A) == 0

# Additional test case 2
A = [1,2,3,4,5,6,7,8,9]
assert solution.maxWidthRamp(A) == 8

