class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        a=0
        b=len(nums)-1
        c=0
        while a<b:
            if nums[a]+nums[b]<target:
                c+=(b-a)
                a+=1
            else:
                b-=1
        return c