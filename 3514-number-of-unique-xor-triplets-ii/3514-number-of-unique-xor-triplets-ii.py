from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(set(nums))

        MAX = 2048

        present = [False] * MAX
        for x in nums:
            present[x] = True

        vals = [i for i in range(MAX) if present[i]]

        pair = [False] * MAX
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        ans = [False] * MAX
        for x in range(MAX):
            if pair[x]:
                for v in vals:
                    ans[x ^ v] = True

        return sum(ans)