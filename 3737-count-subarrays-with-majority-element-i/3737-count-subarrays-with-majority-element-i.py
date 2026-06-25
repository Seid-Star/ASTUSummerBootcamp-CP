from typing import List
from bisect import bisect_left
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref=[0]
        cur=0
        for x in nums:
            cur+=1 if x==target else -1
            pref.append(cur)
        vals=sorted(set(pref))
        n=len(vals)
        class Fenwick:
            def __init__(self,n):
                self.bit=[0]*(n+1)
            def update(self,i,v):
                while i<=n:
                    self.bit[i]+=v
                    i+=i&-i
            def query(self,i):
                s=0
                while i:
                    s+=self.bit[i]
                    i-=i&-i
                return s

        bit=Fenwick(n)
        ans=0
        for p in pref:
            r=bisect_left(vals,p)+1
            ans+=bit.query(r-1)
            bit.update(r,1)
        return ans