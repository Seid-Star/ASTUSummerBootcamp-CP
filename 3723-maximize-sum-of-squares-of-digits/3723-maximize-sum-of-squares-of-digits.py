
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        a = ""
        for i in range(num):
            if sum >= 9:
                a += '9'
                sum -= 9
            else:
                a += str(sum)
                sum = 0

        return a
