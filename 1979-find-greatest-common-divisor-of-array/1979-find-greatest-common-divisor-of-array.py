import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        c=math.gcd(a,b)
        return c
        