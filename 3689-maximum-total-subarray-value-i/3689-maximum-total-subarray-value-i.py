class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a=max(nums)-min(nums)
        return a*k