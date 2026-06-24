class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        Sum=nums[0]
        count=10**9
        while r<len(nums):
            if Sum>=target:
                count=min(count,r-l+1)
                Sum-=nums[l]
                l+=1
            else:
                r+=1
                if r<len(nums):
                    Sum+=nums[r]
        if count==10**9:
            return 0
        else:
            return count

        