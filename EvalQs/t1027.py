
from sol.x1027 import Solution 
from typing import List
import collections
# Test case
solution = Solution()
A = [3,6,9,12]
assert solution.longestArithSeqLength(A) == 4

# Additional test cases
A = [9,4,7,2,10]
assert solution.longestArithSeqLength(A) == 3

A = [20,1,15,3,10,5,8]
assert solution.longestArithSeqLength(A) == 4

