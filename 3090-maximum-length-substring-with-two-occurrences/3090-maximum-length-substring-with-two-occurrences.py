class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        r = 0
        arr = []

        while r < len(s):
            a = s[l:r+1].count(s[r])

            if a <= 2:
                r += 1
            else:
                arr.append(r - l)
                l += 1

        arr.append(r - l)

        return max(arr)