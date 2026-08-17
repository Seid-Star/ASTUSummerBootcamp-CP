from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        # prefix sums
        pref = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            pref[i + 1] = pref[i] + v

        dp = [[0] * n for _ in range(n)]
        NEG = -10**18

        # left state for each i
        left_ptr = [-1] * n          # last added split k
        left_max = [NEG] * n         # max of pref[k+1] + dp[i][k]

        # right state for each j
        right_ptr = [j + 1 for j in range(n)]  # smallest s that is valid
        right_max = [NEG] * n        # max of dp[s][j] - pref[s]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                # ---------- update left state for interval [i, j] ----------
                # add splits k while L <= R
                while (left_ptr[i] + 1 <= j - 1 and
                       2 * pref[left_ptr[i] + 2] <= pref[i] + pref[j + 1]):
                    k = left_ptr[i] + 1
                    left_ptr[i] = k
                    val = pref[k + 1] + dp[i][k]
                    if val > left_max[i]:
                        left_max[i] = val

                # ---------- update right state for interval [i, j] ----------
                # add splits s (where s = k+1) while L >= R
                while (right_ptr[j] - 1 >= i + 1 and
                       2 * pref[right_ptr[j] - 1] >= pref[i] + pref[j + 1]):
                    s = right_ptr[j] - 1
                    right_ptr[j] = s
                    val = dp[s][j] - pref[s]
                    if val > right_max[j]:
                        right_max[j] = val

                # ---------- compute dp[i][j] ----------
                best = 0
                if left_ptr[i] >= i:
                    best = max(best, left_max[i] - pref[i])
                if right_ptr[j] <= j:
                    best = max(best, pref[j + 1] + right_max[j])

                dp[i][j] = best

        return dp[0][n - 1]