class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            a=str(i)
            b=str(digit)
            count+=a.count(b)
        return count

        