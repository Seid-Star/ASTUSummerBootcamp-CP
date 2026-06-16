class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        arr=[]
        while l<r:
            arr.append(nums[l]+nums[r])
            l+=1
            r-=1
        return max(arr)


        