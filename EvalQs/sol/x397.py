

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 1:  # Optimized: Check for divisibility by 4 directly
                n -= 1
            else:
                n += 1
            ans += 1
        return ans