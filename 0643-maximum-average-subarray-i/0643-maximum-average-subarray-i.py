class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l=0
        r=k
        Max=sum(nums[:k])
        MaxA=Max/k
        while r<len(nums):
            Max-=nums[l]
            Max+=nums[r]
            if MaxA<(Max/k):
                MaxA=Max/k
            r+=1
            l+=1
        return MaxA


        