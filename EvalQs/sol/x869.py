

from typing import List

from collections import Counter

import timeit

class Solution:
    def reorderedPowerOf2(self, N):
        cnt = Counter(str(N))
        return any(cnt == Counter(str(1 << c)) for c in range(32))