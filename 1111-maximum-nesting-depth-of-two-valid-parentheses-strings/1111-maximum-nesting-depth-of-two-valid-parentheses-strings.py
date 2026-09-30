class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        count=0
        ans=[]
        for i in seq:
            if i=='(':
                count+=1
                ans.append(count%2)
            else:
                ans.append(count%2)
                count-=1
        return ans