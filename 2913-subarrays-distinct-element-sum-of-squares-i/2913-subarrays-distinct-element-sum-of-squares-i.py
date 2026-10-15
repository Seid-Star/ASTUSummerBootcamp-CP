
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        a = len(nums)
        count = 0
        for i in range(a):
            arr = set()
            for j in range(i, a):
                arr.add(nums[j])
                count += len(arr) * len(arr)
        return count
