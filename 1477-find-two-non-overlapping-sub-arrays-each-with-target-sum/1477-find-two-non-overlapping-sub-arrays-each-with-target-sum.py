class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        best = [1000000] * n

        l = 0
        tot = 0
        ans = 1000000
        best_len = 1000000

        for r in range(n):
            tot += arr[r]

            while tot > target:
                tot -= arr[l]
                l += 1

            if tot == target:
                length = r - l + 1

                if l > 0 and best[l - 1] != 1000000:
                    ans = min(ans, length + best[l - 1])

                best_len = min(best_len, length)

            best[r] = best_len

        if ans == 1000000:
            return -1

        return ans