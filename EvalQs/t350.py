
from sol.x350 import Solution 
from typing import List
from collections import Counter

# Test case 1
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
assert solution.intersect(nums1, nums2) == [2, 2]

# Test case 2
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
assert solution.intersect(nums1, nums2) == [4, 9]

# Test case 3
nums1 = []
nums2 = [1, 2, 3]
assert solution.intersect(nums1, nums2) == []

# Test case 4
nums1 = [1, 2, 3]
nums2 = []
assert solution.intersect(nums1, nums2) == []

