
from sol.x393 import Solution
# Generated Code
# Test case 1
solution = Solution()
data = [197, 130, 1]
assert solution.validUtf8(data) == True

# Test case 2
data = [235, 140, 46]
assert solution.validUtf8(data) == False

# Test case 3
data = [240, 159, 145, 146]
assert solution.validUtf8(data) == True

# Test case 4
data = [248, 128, 128]
assert solution.validUtf8(data) == False

# Test case 5
data = [255, 255, 255]
assert solution.validUtf8(data) == False

