class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q = 0

        for i in range(half):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])

        # Bob can win when the '?' counts are equal
        # and the existing sums are already equal.
        if q == 0:
            return diff != 0

        # An odd difference in '?' counts means Alice wins.
        if q % 2 != 0:
            return True

        # Bob can win only when the fixed difference is
        # exactly compensated by the extra '?'.
        return diff != -9 * q // 2