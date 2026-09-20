class Solution:
    def reverseDegree(self, s: str) -> int:
        normal='abcdefghijklmnopqrstuvwxyz'
        rev=normal[::-1]
        Sum=0
        for i in range(len(s)):
            Sum+=((i+1)*(rev.index(s[i])+1))
        return Sum

        