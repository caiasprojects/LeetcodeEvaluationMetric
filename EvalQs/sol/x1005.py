from typing import List

from typing import List
import heapq
import timeit

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            val = heapq.heappop(A)
            heapq.heappush(A, -val)
        return sum(A)

