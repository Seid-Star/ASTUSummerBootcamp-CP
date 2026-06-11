class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else:
            if target>max(nums):
                b=len(nums)
                return b
            elif target <min(nums):
                c=0
                return c
            else:
                for i in range(1,len(nums)):
                    if nums[i-1]<target<nums[i]:
                        return i       