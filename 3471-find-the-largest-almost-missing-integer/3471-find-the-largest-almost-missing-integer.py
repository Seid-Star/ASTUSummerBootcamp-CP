class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in range(len(nums) - k + 1):
            window = set(nums[i:i + k])
            for x in window:
                freq[x] = freq.get(x, 0) + 1
        ans = -1
        for x in freq:
            if freq[x] == 1:
                ans = max(ans, x)
        return ans