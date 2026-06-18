class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count=len(prices)
        l=0
        r=1
        while r<len(prices):
            if prices[r-1]-prices[r]==1:
                count+=(r-l)
            else:
                l=r
            r+=1
        return count


        