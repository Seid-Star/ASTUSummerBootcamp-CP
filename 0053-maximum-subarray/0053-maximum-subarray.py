class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pref=[0]
        for i in nums:
            pref.append(pref[-1]+i)
        ans=nums[0]
        a=pref[0]
        b=nums[0]
        for i in range(1,len(pref)):
            c=pref[i]-a
            if c>b:
                b=c
            if pref[i]<a:
                a=pref[i]
        return b
