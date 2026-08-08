class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = []

        for i in range(len(nums)):
            for x in nums[i]:
                arr.append((x, i))

        arr.sort()

        count = [0] * len(nums)
        have = 0
        left = 0
        ans = [arr[0][0], arr[-1][0]]

        for right in range(len(arr)):
            value, group = arr[right]

            if count[group] == 0:
                have += 1

            count[group] += 1

            while have == len(nums):
                lvalue, lgroup = arr[left]

                if arr[right][0] - lvalue < ans[1] - ans[0]:
                    ans = [lvalue, arr[right][0]]

                count[lgroup] -= 1

                if count[lgroup] == 0:
                    have -= 1

                left += 1

        return ans