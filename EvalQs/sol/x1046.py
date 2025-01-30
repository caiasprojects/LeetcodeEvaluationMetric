from typing import List

from typing import List
import bisect
import timeit

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x != y:
                bisect.insort(stones, y-x)
            else:
                continue
        return stones[0] if stones else 0
