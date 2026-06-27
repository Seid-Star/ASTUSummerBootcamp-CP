class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        b=(len(nums)*(len(nums)+1))//2
        return b-a
        