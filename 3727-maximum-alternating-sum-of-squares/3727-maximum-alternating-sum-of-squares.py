
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        Sum=0
        for i in range(len(nums)):
            if i < (len(nums)+1)//2:
                Sum+=nums[len(nums)-1-i]**2
            else:
                Sum-=nums[i-(len(nums)+1)//2]**2
        return Sum
