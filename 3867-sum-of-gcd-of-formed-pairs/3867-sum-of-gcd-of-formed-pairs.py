from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p=[]
        m=0
        for x in nums:
            m=max(m,x)
            p.append(gcd(x,m))
        p.sort()
        a=0
        l,r=0,len(p)-1
        while l<r:
            a+=gcd(p[l],p[r])
            l+=1
            r-=1
        return a
        