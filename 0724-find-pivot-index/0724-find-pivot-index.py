class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr=[0]
        for i in nums:
            arr.append(arr[-1]+i)
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l]==arr[r]-arr[l+1]:
                return l
            l+=1
        return -1


        