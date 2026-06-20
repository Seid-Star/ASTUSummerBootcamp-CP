from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        for i in range(1,len(restrictions)):
            idx1,h1=restrictions[i-1]
            idx2,h2=restrictions[i]
            restrictions[i][1]=min(h2,h1+(idx2-idx1))
        for i in range(len(restrictions)-2,-1,-1):
            idx1,h1=restrictions[i]
            idx2,h2=restrictions[i+1]
            restrictions[i][1]=min(h1,h2+(idx2-idx1))
        ans=0
        for i in range(len(restrictions)-1):
            idx1,h1=restrictions[i]
            idx2,h2=restrictions[i+1]
            dist=idx2-idx1
            diff=abs(h2-h1)
            ans=max(ans,max(h1,h2)+(dist-diff)//2)
        ans=max(ans,restrictions[0][1]+restrictions[0][0]-1)
        ans=max(ans,restrictions[-1][1]+(n-restrictions[-1][0]))
        return ans