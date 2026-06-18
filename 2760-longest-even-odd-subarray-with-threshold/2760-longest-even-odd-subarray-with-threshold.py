class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l=0
        r=0
        Max=0
        while r<len(nums):
            if nums[r]>threshold:
                r+=1
                l=r
                continue
            if l==r and nums[r]%2!=0:
                r+=1
                l=r
                continue
            if l<r and nums[r]%2==nums[r-1]%2:
                l=r
                continue
            Max=max(Max,r-l+1)
            r+=1
        return Max