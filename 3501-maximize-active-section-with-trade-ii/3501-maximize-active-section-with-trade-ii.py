import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')

        # ---- build runs ----
        run_start, run_end, run_char = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            run_start.append(i)
            run_end.append(j - 1)
            run_char.append(1 if s[i] == '1' else 0)
            i = j
        m = len(run_start)
        NEG = float('-inf')

        # ---- precompute static gain for each interior 1-run ----
        G = [NEG] * m
        for idx in range(1, m - 1):
            if run_char[idx] == 1:
                left_len = run_start[idx] - run_start[idx - 1]
                right_len = run_end[idx + 1] - run_end[idx]
                G[idx] = left_len + right_len

        # ---- sparse table for range max on G ----
        LOG = [0] * (m + 1)
        for i2 in range(2, m + 1):
            LOG[i2] = LOG[i2 // 2] + 1
        sparse = [G[:]]
        k = 1
        while (1 << k) <= m:
            prev = sparse[-1]
            half = 1 << (k - 1)
            length = m - (1 << k) + 1
            cur = [max(prev[i2], prev[i2 + half]) for i2 in range(length)]
            sparse.append(cur)
            k += 1

        def range_max(l, r):
            if l > r:
                return NEG
            length = r - l + 1
            k2 = LOG[length]
            return max(sparse[k2][l], sparse[k2][r - (1 << k2) + 1])

        def run_of(p):
            return bisect.bisect_right(run_start, p) - 1

        ans = []
        for l, r in queries:
            lo = run_of(l) + 1
            hi = run_of(r) - 1

            if lo > hi:
                ans.append(total_ones)
                continue

            leftmost = lo if run_char[lo] == 1 else lo + 1
            rightmost = hi if run_char[hi] == 1 else hi - 1

            if leftmost > hi or rightmost < lo or leftmost > rightmost:
                ans.append(total_ones)
                continue

            if leftmost == rightmost:
                i2 = leftmost
                left_len = run_start[i2] - max(run_start[i2 - 1], l)
                right_len = min(run_end[i2 + 1], r) - run_end[i2]
                best = left_len + right_len
            else:
                left_len = run_start[leftmost] - max(run_start[leftmost - 1], l)
                right_len_full = run_end[leftmost + 1] - run_end[leftmost]
                gain_left = left_len + right_len_full

                left_len_full = run_start[rightmost] - run_start[rightmost - 1]
                right_len = min(run_end[rightmost + 1], r) - run_end[rightmost]
                gain_right = left_len_full + right_len

                mid = range_max(leftmost + 1, rightmost - 1)
                best = max(gain_left, gain_right, mid)

            ans.append(total_ones + max(0, best))

        return ans