



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers without using multiplication, division, or mod operator.

        Args:
            dividend: The dividend.
            divisor: The divisor.

        Returns:
            The quotient of the division.
        """
        if divisor == 0:
            return 2**31 - 1
        if dividend == 0:
            return 0

        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp = divisor
            count = 0
            while dividend >= temp << 1:
                temp <<= 1
                count += 1
            dividend -= temp
            quotient += 1 << count

        return sign * quotient

import unittest

class TestSolution(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution().divide(10, 3), 3)

    def test_example2(self):
        self.assertEqual(Solution().divide(7, -3), -2)

    def test_zero_divisor(self):
        self.assertEqual(Solution().divide(10, 0), 2**31 - 1)

    def test_zero_dividend(self):
        self.assertEqual(Solution().divide(0, 5), 0)

    def test_large_dividend(self):
        self.assertEqual(Solution().divide(153, 3), 51)

    def test_large_divisor(self):
        self.assertEqual(Solution().divide(1000000, 100000), 10)

if __name__ == '__main__':
    unittest.main()