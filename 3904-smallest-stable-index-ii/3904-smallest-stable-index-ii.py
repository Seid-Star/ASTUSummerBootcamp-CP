class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        right_min = [0] * n
        right_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        max_left = nums[0]

        for i in range(n):
            max_left = max(max_left, nums[i])

            if max_left - right_min[i] <= k:
                return i

        return -1