
from sol.x207 import Solution  # Ensure correct module path
# Test case 1
solution = Solution()
numCourses = 2
prerequisites = [[1, 0]]
assert solution.canFinish(numCourses, prerequisites) == True

# Test case 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
assert solution.canFinish(numCourses, prerequisites) == False

# Test case 3
numCourses = 3
prerequisites = [[0, 1], [0, 2], [1, 2]]
assert solution.canFinish(numCourses, prerequisites) == True

# Test case 4
numCourses = 3
prerequisites = [[0, 1], [1, 2], [2, 0]]
assert solution.canFinish(numCourses, prerequisites) == False

# Test case 5
numCourses = 4
prerequisites = [[0, 1], [1, 2], [2, 3]]
assert solution.canFinish(numCourses, prerequisites) == True

