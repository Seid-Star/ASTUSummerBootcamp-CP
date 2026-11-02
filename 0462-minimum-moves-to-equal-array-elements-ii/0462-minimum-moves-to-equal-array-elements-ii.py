class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        a=nums[len(nums)//2]
        count=0
        for i in nums:
            count+=abs(i-a)
        return count