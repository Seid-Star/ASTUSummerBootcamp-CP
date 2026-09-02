class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        arr={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a in arr:
                return i,arr[a]
            arr[nums[i]]=i