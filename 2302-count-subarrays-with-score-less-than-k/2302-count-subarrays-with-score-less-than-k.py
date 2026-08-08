class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        l=0
        r=0
        Tot=0
        while r<len(nums):
            Tot+=nums[r]
            while Tot*(r-l+1)>=k:
                Tot-=nums[l]
                l+=1
            count+=r-l+1
            r+=1
        return count

        