class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))
        left = min(max_idx, min_idx)
        right = max(max_idx, min_idx)
        option1 = right + 1
        option2 = n - left
        option3 = (left + 1) + (n - right)
        return min(option1, option2, option3)