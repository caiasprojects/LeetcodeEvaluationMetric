from typing import List
# Generated new fixed Code

from typing import List
import collections
import timeit

class Solution:
    def maxWidthRamp(self, A):
        ind, mx, index = float("inf"), 0, collections.defaultdict(list)
        for i, num in enumerate(A):
            index[num].append(i)
        A.sort()
        for i in range(len(A)):
            mx = max(mx, index[A[i]][-1] - ind)
            ind = min(ind, index[A[i]][0])
        return mx

