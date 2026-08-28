from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        # A palindrome can have at most one character
        # with an odd frequency.
        odd = [ch for ch in freq if freq[ch] % 2]

        if len(odd) > 1:
            return ""

        # Characters available for the left half
        half_count = Counter()

        for ch in freq:
            half_count[ch] = freq[ch] // 2

        half_len = n // 2
        target_half = target[:half_len]

        # Build a palindrome from its left half
        def build(left):
            middle = odd[0] if n % 2 else ""
            return left + middle + left[::-1]

        # --------------------------------------------------
        # 1. Check if target's first half itself is possible.
        #    If so, it gives the smallest possible palindrome
        #    with that first half.
        # --------------------------------------------------
        remaining = half_count.copy()
        possible = True

        for ch in target_half:
            if remaining[ch] == 0:
                possible = False
                break
            remaining[ch] -= 1

        if possible:
            candidate = build(target_half)

            # This handles:
            # s = "aac", target = "abb"
            # candidate = "aca" > "abb"
            if candidate > target:
                return candidate

        # --------------------------------------------------
        # 2. Find the smallest permutation of the left half
        #    that is strictly greater than target_half.
        # --------------------------------------------------
        for i in range(half_len - 1, -1, -1):

            remaining = half_count.copy()
            possible = True

            # Keep target_half[0:i] unchanged
            for j in range(i):
                ch = target_half[j]

                if remaining[ch] == 0:
                    possible = False
                    break

                remaining[ch] -= 1

            if not possible:
                continue

            # At position i, choose the smallest character
            # strictly greater than target_half[i].
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch > target_half[i] and remaining[ch] > 0:

                    remaining[ch] -= 1

                    # Fill the rest with the smallest possible chars
                    suffix = []

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        suffix.extend([c] * remaining[c])

                    left = target_half[:i] + ch + ''.join(suffix)

                    candidate = build(left)

                    if candidate > target:
                        return candidate

        return ""