class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a=max(nums)
        count=0
        for i in nums:
            count+=(a-i)
        return count
        