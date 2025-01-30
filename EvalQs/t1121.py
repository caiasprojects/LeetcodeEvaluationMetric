
from sol.x1121 import Solution 
from typing import List
import collections
# Test case 1
solution = Solution()
nums = [1,2,3,4]
K = 3
assert solution.canDivideIntoSubsequences(nums, K) == True

# Test case 2
nums = [1,2,2,3,3,4,4]
K = 3
assert solution.canDivideIntoSubsequences(nums, K) == True

# Test case 3
nums = [1,2,2,3,3,4,4,5,5,6,6]
K = 4
assert solution.canDivideIntoSubsequences(nums, K) == True

# Test case 4
nums = [1,2,3,4,5]
K = 6
assert solution.canDivideIntoSubsequences(nums, K) == False

# Test case 5
nums = [1,1,1,2,2,2,3,3,3]
K = 3
assert solution.canDivideIntoSubsequences(nums, K) == True

