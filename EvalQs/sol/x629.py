

class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10 ** 9 + 7
        upper = n * (n - 1) // 2
        if k == 0 or k == upper:
            return 1
        if k > upper:
            return 0

        dp = [0] * (k + 1)
        dp[0] = 1

        # Optimized DP calculation using a single loop
        for i in range(1, n + 1):
            temp = [1] * (k + 1)
            for j in range(1, k + 1):
                temp[j] = (temp[j - 1] + dp[j]) % MOD
                if j - i >= 0:
                    temp[j] = (temp[j] - dp[j - i]) % MOD
            dp = temp
        return dp[k]