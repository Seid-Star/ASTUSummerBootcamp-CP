class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a=l-1
        b=0
       
        Min=10**9
        while l<=r:
            Tot=sum(nums[:l])
            if Tot>0:
                Min=min(Min,Tot)
            a=l
            b=0
            while a<len(nums):
                Tot+=nums[a]
                Tot-=nums[b]
                if Tot>0:
                    Min=min(Min,Tot)
                a+=1
                b+=1
            l+=1
        if Min==10**9:
            return -1
        else:
            return Min
                






        