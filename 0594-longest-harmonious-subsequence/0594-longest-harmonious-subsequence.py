class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # freq={}
        # for i in range(len(nums)):
        #     if nums[i] not in freq:
        #         freq[nums[i]]=1
        #     else:
        #         freq[nums[i]]+=1
        # Max=0
        # for j,k in freq.items():
        #     if j+1 in freq:
        #         Max=max(Max,k+freq[j+1])
        # return Max
        nums.sort()
        l=0
        r=0
        a=0
        while r<len(nums):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                a=max(a,r-l+1)
            r+=1
        return a