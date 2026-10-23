class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold=0
        seeker=0
        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[seeker],nums[hold]=nums[hold],nums[seeker]
                hold+=1
            seeker+=1

        