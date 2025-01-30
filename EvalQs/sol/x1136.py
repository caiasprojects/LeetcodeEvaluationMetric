from typing import List, Tuple
 #This code will run the `minimumSemesters` function from the `Solution` class with the provided test case and print the time taken to run the function 10,000 times. The time taken is in seconds.

from typing import List, Tuple
import collections
import timeit

class Solution:
    def minimumSemesters(self, N: int, relations: List[Tuple[int, int]]) -> int:
        """
        :type N: int
        :type relations: List[Tuple[int, int]]
        :rtype: int
        """
        if N == 1:
            return 1
        graph = collections.defaultdict(list)
        for p, q in relations:
            graph[q-1].append(p-1)

        def need_semesters(n):
            if dp[n] > 0:   # node was visited
                return dp[n]
            if dp[n] == -1: # node is being visited, t #Here is  a cycle!
                return -1
            dp[n] = -1 # start visiting the node
            res = 0
            for p in graph[n]:
                a = need_semesters(p)
                if a == -1:
                    return -1
                res = max(res, a)
            dp[n] = res + 1
            return dp[n]

        dp = [0]*N
        for n in range(N):
            if need_semesters(n) == -1:
                return -1
        return max(dp)
