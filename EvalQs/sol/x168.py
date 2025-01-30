

import math

class Solution(object):
    def convertToTitle(self, n):
        ans = ""
        while n > 0:
            n -= 1
            y = n % 26
            char = chr(ord("A") + y)
            ans += char
            n //= 26
        return ans[::-1]