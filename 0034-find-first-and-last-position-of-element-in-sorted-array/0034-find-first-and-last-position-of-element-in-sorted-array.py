class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        range=[-1,-1]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                range[0]=mid
                high=mid-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                range[1]=mid
                low=mid+1
        return range
        