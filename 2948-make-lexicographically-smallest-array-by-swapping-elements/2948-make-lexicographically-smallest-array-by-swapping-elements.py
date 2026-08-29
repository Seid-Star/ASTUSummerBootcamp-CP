class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((value, i) for i, value in enumerate(nums))
        ans = nums[:]
        left = 0

        while left < len(nums):
            right = left

            while right + 1 < len(nums) and arr[right + 1][0] - arr[right][0] <= limit:
                right += 1

            values = [arr[i][0] for i in range(left, right + 1)]
            indices = sorted(arr[i][1] for i in range(left, right + 1))

            for i, value in zip(indices, values):
                ans[i] = value

            left = right + 1

        return ans