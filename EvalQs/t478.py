
from sol.x478 import Solution 
from typing import List
import random
import math


from typing import List
# Test case 1
solution = Solution(1, 0, 0)

# Test case 2: Check if the returned point is within the circle
for _ in range(1000):
    point = solution.randPoint()
    assert math.hypot(point[0], point[1]) <= solution.r, f"Point {point} is not within the circle"

# Test case 3: Check if the returned point is within the bounding box
for _ in range(1000):
    point = solution.randPoint()
    assert -solution.r <= point[0] <= solution.r and -solution.r <= point[1] <= solution.r, f"Point {point} is not within the bounding box"
