class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                need[i] += 1
                t //= p

        if t != 1:
            return "-1"

        factor = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [3, 0, 0, 0],
            [0, 2, 0, 0]
        ]

        n = len(num)

        from functools import lru_cache

        @lru_cache(None)
        def can(length, a, b, c, d):
            if a == 0 and b == 0 and c == 0 and d == 0:
                return True

            if length == 0:
                return False

            if a > 3 * length or b > 2 * length or c > length or d > length:
                return False

            for digit in range(1, 10):
                f = factor[digit]

                if can(
                    length - 1,
                    max(0, a - f[0]),
                    max(0, b - f[1]),
                    max(0, c - f[2]),
                    max(0, d - f[3])
                ):
                    return True

            return False

        def build(length, a, b, c, d):
            ans = []

            while length:
                for digit in range(1, 10):
                    f = factor[digit]

                    na = max(0, a - f[0])
                    nb = max(0, b - f[1])
                    nc = max(0, c - f[2])
                    nd = max(0, d - f[3])

                    if can(length - 1, na, nb, nc, nd):
                        ans.append(str(digit))
                        a, b, c, d = na, nb, nc, nd
                        break

                length -= 1

            return ''.join(ans)

        cur = [0, 0, 0, 0]

        if '0' not in num:
            for ch in num:
                f = factor[int(ch)]
                for j in range(4):
                    cur[j] += f[j]

            if all(cur[j] >= need[j] for j in range(4)):
                return num

        prefixes = [[0, 0, 0, 0]]
        prefix = [0, 0, 0, 0]
        valid = True

        for ch in num:
            digit = int(ch)

            if digit == 0:
                valid = False

            if valid:
                f = factor[digit]
                for j in range(4):
                    prefix[j] += f[j]

            prefixes.append(prefix.copy())

        for i in range(n - 1, -1, -1):
            if '0' in num[:i]:
                continue

            for digit in range(int(num[i]) + 1, 10):
                f = factor[digit]

                a = max(0, need[0] - prefixes[i][0] - f[0])
                b = max(0, need[1] - prefixes[i][1] - f[1])
                c = max(0, need[2] - prefixes[i][2] - f[2])
                d = max(0, need[3] - prefixes[i][3] - f[3])

                remaining = n - i - 1

                if can(remaining, a, b, c, d):
                    return num[:i] + str(digit) + build(
                        remaining, a, b, c, d
                    )

        length = n + 1

        while True:
            for first in range(1, 10):
                f = factor[first]

                a = max(0, need[0] - f[0])
                b = max(0, need[1] - f[1])
                c = max(0, need[2] - f[2])
                d = max(0, need[3] - f[3])

                if can(length - 1, a, b, c, d):
                    return str(first) + build(
                        length - 1, a, b, c, d
                    )

            length += 1