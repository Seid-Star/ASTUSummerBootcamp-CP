class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - 97] += 1

        half = n // 2
        mid = ''
        halfcounts = [0] * 26
        for i in range(26):
            halfcounts[i] = counts[i] // 2
            if counts[i] % 2 == 1:
                mid = chr(97 + i)

        # Precompute factorials up to half
        fact = [1] * (half + 1)
        for i in range(1, half + 1):
            fact[i] = fact[i - 1] * i

        denom = 1
        for i in range(26):
            denom *= fact[halfcounts[i]]

        total = fact[half] // denom
        if k > total:
            return ""

        cnt = halfcounts[:]
        remaining = half
        result = []

        for _ in range(half):
            for c in range(26):
                if cnt[c] == 0:
                    continue
                denom_after = denom // cnt[c]  # exact: denom / cnt[c] since fact[v]/v = fact[v-1]
                # Check fact[remaining-1] // denom_after >= k  without doing a big division:
                if fact[remaining - 1] >= k * denom_after:
                    cnt[c] -= 1
                    denom = denom_after
                    remaining -= 1
                    result.append(chr(97 + c))
                    break
                else:
                    perm_count = fact[remaining - 1] // denom_after
                    k -= perm_count

        half_str = ''.join(result)
        return half_str + mid + half_str[::-1]