class Solution:
    def maxProduct(self, n: int) -> int:
        a=str(n)
        arr=[]
        for i in a:
            arr.append(int(i))
        arr.sort()
        return (arr[-1]*arr[-2])
        