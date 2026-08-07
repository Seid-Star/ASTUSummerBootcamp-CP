class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        Max=0
        count=0
        coun=0
        while r<len(nums):
            if nums[r]==1:
                count+=1
                r+=1
            else:
                Max=max(Max,count+coun)
                coun=count
                count=0
                r+=1
        Max=max(Max,coun+count)
        if Max==len(nums):
            Max-=1
        return Max
            
        