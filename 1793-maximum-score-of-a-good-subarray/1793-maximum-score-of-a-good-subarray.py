class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l=k
        r=k
        Min=nums[k]
        Max=nums[k]
        while l>0 or r<len(nums)-1:
            if l==0:
                r+=1
            elif r==len(nums)-1:
                l-=1
            elif nums[l-1]>=nums[r+1]:
                l-=1
            else:
                r+=1
            Min=min(Min,nums[l],nums[r])
            Max=max(Max,Min*(r-l+1))
        return Max

       