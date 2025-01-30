

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur = nums[0]
        for i in range(1, n):
            if nums[i] - cur - 1 >= k:
                break
            else:
                k -= nums[i] - cur - 1
            cur = nums[i]
        return cur + k