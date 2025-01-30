
class Solution(object):
        def grayCode(self, n):
            if n < 1:
                return [0]
            ans = [0]
            for i in range(1, 2 ** n):
                ans.append(ans[-1] ^ (i & -i))
            return ans