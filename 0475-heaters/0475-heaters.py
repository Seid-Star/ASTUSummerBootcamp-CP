class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        a=0
        b=0
        for x in houses:
            while a<len(heaters)-1 and abs(heaters[a+1]-x)<=abs(heaters[a]-x):
                a+=1
            b=max(b,abs(heaters[a]-x))
        return b