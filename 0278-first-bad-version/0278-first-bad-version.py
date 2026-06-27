# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a=0
        b=n+1
        while a+1<b:
            c=(a+b)//2
            if isBadVersion(c):
                b=c
            else:
                a=c
        return b

        