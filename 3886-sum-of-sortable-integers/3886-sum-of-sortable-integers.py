
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True
            prev_max = 0

            for i in range(0, n, k):
                arr = nums[i:i + k]
                count = 0

                for j in range(k):
                    if arr[j] > arr[(j + 1) % k]:
                        count += 1

                if count > 1:
                    possible = False
                    break

                if i > 0 and prev_max > min(arr):
                    possible = False
                    break

                prev_max = max(arr)

            if possible:
                ans += k

        return ans
