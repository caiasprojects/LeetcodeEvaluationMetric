

from typing import List

from typing import List
import collections
import timeit

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            q = collections.deque([(sr, sc)])
            visited = set([(sr, sc)])  # Use a set to track visited cells efficiently
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old and (x, y) not in visited:
                        q.append((x, y))
                        visited.add((x, y))  # Add the new cell to the visited set
        return image