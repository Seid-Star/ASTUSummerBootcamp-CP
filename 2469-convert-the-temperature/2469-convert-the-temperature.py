class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kel=celsius+273.15
        Far=celsius*1.80+32.00
        arr=[Kel,Far]
        return arr
        