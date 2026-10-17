
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        a = len(nums)
        arr = []

        for i in nums:
            b = 0
            c = i
            while c > 0:
                b += c % 10
                c //= 10
            arr.append((b, i))

        brr = sorted(arr)
        pos = {}

        for i in range(a):
            pos[brr[i][1]] = i

        vis = [False] * a
        count = 0

        for i in range(a):
            if vis[i] or pos[nums[i]] == i:
                continue

            j = i
            size = 0

            while not vis[j]:
                vis[j] = True
                j = pos[nums[j]]
                size += 1

            count += size - 1

        return count
