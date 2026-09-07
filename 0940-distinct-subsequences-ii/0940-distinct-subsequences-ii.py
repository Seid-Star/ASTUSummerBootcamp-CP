class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [1]
        last = {}

        for i in range(len(s)):
            x = 2 * dp[-1]

            if s[i] in last:
                x -= dp[last[s[i]]]

            dp.append(x % MOD)
            last[s[i]] = i

        return (dp[-1] - 1) % MOD