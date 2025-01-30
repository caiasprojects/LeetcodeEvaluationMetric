from sol.x709 import Solution 
from typing import List

# Test case 1
solution = Solution()
str = "HELLO"
assert solution.toLowerCase(str) == "hello"

# Test case 2
str = "HELLO World"
assert solution.toLowerCase(str) == "hello world"

# Test case 3
str = "HELLO123"
assert solution.toLowerCase(str) == "hello123"

# Test case 4
str = "UPPERCASE"
assert solution.toLowerCase(str) == "uppercase"

# Test case 5
str = "MixEdCaSe"
assert solution.toLowerCase(str) == "mixedcase"

