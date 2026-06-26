class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        OFFSET = n
        SIZE = 2 * n + 2
        bit = [0] * (SIZE + 1)

        def update(i):
            i += 1
            while i <= SIZE:
                bit[i] += 1
                i += i & (-i)

        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        def count_less_than(val):
            if val == 0:
                return 0
            return query(val - 1)

        result = 0
        prefix = 0
        update(prefix + OFFSET)
        for num in nums:
            prefix += 1 if num == target else -1
            result += count_less_than(prefix + OFFSET)
            update(prefix + OFFSET)
        return result