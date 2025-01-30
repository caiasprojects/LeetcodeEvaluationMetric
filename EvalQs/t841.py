
from sol.x841 import Solution 

solution = Solution()
rooms = [[1],[2],[3],[]]
assert solution.canVisitAllRooms(rooms) == True

rooms = [[1,3],[3,0,1],[2],[0]]
assert solution.canVisitAllRooms(rooms) == False

# Additional test cases
rooms = [[1, 3], [3, 0, 1], [2], [0]]
assert solution.canVisitAllRooms(rooms) == False

rooms = [[1], [2, 3], [0], [4]]
assert solution.canVisitAllRooms(rooms) == True

