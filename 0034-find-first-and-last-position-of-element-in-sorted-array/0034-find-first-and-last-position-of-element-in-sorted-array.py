class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            a=nums.index(target)
            b=len(nums)-1-nums[::-1].index(target)
            return [a,b]
        else:
            return [-1,-1]

        