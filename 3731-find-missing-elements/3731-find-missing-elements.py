class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        arr=[]
        for i in range(a+1,b):
            if i not in nums:
                arr.append(i)
        return arr
        