

from typing import List

from collections import defaultdict, deque

import timeit

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res