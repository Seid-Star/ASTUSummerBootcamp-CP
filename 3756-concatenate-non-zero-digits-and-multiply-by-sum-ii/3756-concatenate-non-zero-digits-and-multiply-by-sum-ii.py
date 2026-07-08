class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        digits = []
        pos = []
        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)
        sum_pre = [0]
        num_pre = [0]
        for x in digits:
            sum_pre.append(sum_pre[-1] + x)
            num_pre.append((num_pre[-1] * 10 + x) % MOD)
        ans = []
        import bisect
        for l, r in queries:
            left = bisect.bisect_left(pos, l)
            right = bisect.bisect_right(pos, r)
            if left == right:
                ans.append(0)
                continue
            digit_sum = sum_pre[right] - sum_pre[left]
            length = right - left
            x = (num_pre[right] - num_pre[left] * pow(10, length, MOD)) % MOD
            ans.append((x * digit_sum) % MOD)
        return ans