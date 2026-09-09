class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        b=0
        for i in prices:
            if i<a:
                a=i
            else:
                b=max(b,i-a)
        return b
            
