

from typing import List
from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        # Use a set to efficiently keep track of the frequencies of each number
        nums_set = set(nums)
        # Calculate the maximum frequency of any number
        max_freq = max(Counter(nums).values())
        # Check if the product of K and the maximum frequency is less than or equal to the total number of elements
        return K * max_freq <= len(nums)