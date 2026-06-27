# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a=0
        b=n
        while a<b:
            c=(a+b)//2
            if isBadVersion(c):
                b=c
            else:
                a=c+1
        return a

        