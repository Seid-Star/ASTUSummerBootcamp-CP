class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k
        for i in range(len(nums)):
            new = [0] * k
            new[nums[i] % k] += 1
            for j in range(k):
                if dp[j] > 0:
                    x = (j * (nums[i] % k)) % k
                    new[x] += dp[j]
            for j in range(k):
                ans[j] += new[j]
            dp = new
        return ans