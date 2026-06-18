class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max=sum(nums[0:k])
        a=Max
        b=0
        c=k
        while c<len(nums):
            Max=Max-nums[b]+nums[c]
            a=max(Max,a)
            c+=1
            b+=1
        return a/k