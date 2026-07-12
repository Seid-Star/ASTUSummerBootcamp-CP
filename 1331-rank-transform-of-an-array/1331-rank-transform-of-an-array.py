from bisect import bisect_left

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        brr = sorted(set(arr))
        crr = []

        for x in arr:
            crr.append(bisect_left(brr, x) + 1)

        return crr