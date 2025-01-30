
from sol.x835 import Solution 

# Test case 1
solution = Solution()
A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]
expected_output = 3

assert expected_output == solution.largestOverlap(A, B)

# Test case 2
A = [[1,1,1],[0,0,0],[0,0,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]
expected_output = 2

assert expected_output == solution.largestOverlap(A, B)

# Test case 3
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,1,1],[1,1,1],[1,1,1]]
expected_output = 9

assert expected_output == solution.largestOverlap(A, B)
A = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0,0,0],[0,0,0],[0,0,0]]
expected_output = 0

assert expected_output == solution.largestOverlap(A, B)
