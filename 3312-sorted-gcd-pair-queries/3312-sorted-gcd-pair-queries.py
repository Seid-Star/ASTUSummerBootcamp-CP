class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import Counter
        from math import gcd
        import bisect

        m=max(nums)
        freq=Counter(nums)

        count=[0]*(m+1)

        for i in range(1,m+1):
            total=0
            for j in range(i,m+1,i):
                total+=freq[j]
            count[i]=total*(total-1)//2

        for i in range(m,0,-1):
            for j in range(2*i,m+1,i):
                count[i]-=count[j]

        prefix=[]
        s=0
        for i in range(m+1):
            s+=count[i]
            prefix.append(s)

        ans=[]
        for q in queries:
            ans.append(bisect.bisect_right(prefix,q))

        return ans