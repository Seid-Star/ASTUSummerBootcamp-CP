class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count=0
        arr=[0]
        for i in gain:
            count+=i
            arr.append(count)
        return max(arr)

        