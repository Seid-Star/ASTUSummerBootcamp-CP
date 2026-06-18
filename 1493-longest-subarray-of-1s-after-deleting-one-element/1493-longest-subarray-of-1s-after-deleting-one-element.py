class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        Max=0
        while r<len(nums):
            if nums[r]==0:
                count+=1
            while count>1:
                if nums[l]==0:
                    count-=1
                l+=1
            Max=max(Max,r-l)
            r+=1
        return Max