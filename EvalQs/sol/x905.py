

from typing import List

class Solution:
    def sortArrayByParity(self, A):
        # Use a list comprehension to efficiently filter and sort the array
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 != 0]