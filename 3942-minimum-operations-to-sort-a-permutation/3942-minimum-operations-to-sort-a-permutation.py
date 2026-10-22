class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        if all(nums[i] == (nums[0] + i) % n for i in range(n)):
            k = (n - nums[0]) % n
            ans = min(ans, k if k == 0 else min(k, n - k + 2))

        if all(nums[i] == (nums[0] - i) % n for i in range(n)):
            k = (n - 1 - nums[0]) % n
            ans = min(ans, min(k + 1, n - k + 1))

        return ans if ans != float('inf') else -1