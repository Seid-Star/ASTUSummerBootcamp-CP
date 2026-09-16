class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]
        prefix = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(k + 1):
            prefix[0][j] = dp[0][j]

        for i in range(1, n):
            prefix[i][0] = (prefix[i - 1][0] + dp[i][0]) % mod

        for j in range(1, k + 1):
            for i in range(1, n):
                dp[i][j] = dp[i - 1][j]

                if i >= 1:
                    dp[i][j] += prefix[i - 1][j - 1]

                dp[i][j] %= mod

                prefix[i][j] = (prefix[i - 1][j] + dp[i][j]) % mod

        return dp[n - 1][k]