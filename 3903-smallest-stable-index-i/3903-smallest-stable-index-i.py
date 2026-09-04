class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        arr = []
        brr = []
        crr = []

        for i in range(len(nums)):
            arr.append(max(nums[:i+1]) - min(nums[i:]))

        for i in range(len(arr)):
            if arr[i] <= k:
                return i

        return -1