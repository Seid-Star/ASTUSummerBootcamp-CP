class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        a=-1
        b=-1
        c=-1
        count=0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                c=i
            if nums[i]==minK:
                a=i
            if nums[i]==maxK:
                b=i
            if a!=-1 and b!=-1:
                count+=max(0,min(a,b)-c)
        return count


        