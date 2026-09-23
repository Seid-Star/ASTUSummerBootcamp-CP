class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total=sum(nums)
        target=total-x
        if target<0:
            return -1
        l=0
        r=0
        cur=0
        Max=-1
        while r<len(nums):
            cur+=nums[r]
            while cur>target and l<=r:
                cur-=nums[l]
                l+=1
            if cur==target:
                Max=max(Max,r-l+1)      
            r+=1
        if Max==-1:
            return -1
        return len(nums)-Max