class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=1
        if a*k not in nums:
            return a*k
        else:
            while a*k in nums:
                a+=1
            return a*k
        