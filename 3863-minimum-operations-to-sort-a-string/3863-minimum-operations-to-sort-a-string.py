
class Solution:
    def minOperations(self, s: str) -> int:
        a = sorted(s)
        n = len(s)

        if list(s) == a:
            return 0

        if n == 2:
            return -1

        if s[0] == a[0] or s[-1] == a[-1]:
            return 1

        if s[0] == a[-1] and s[-1] == a[0]:
            if s.count(s[0]) == 1 and s.count(s[-1]) == 1:
                return 3

        return 2
