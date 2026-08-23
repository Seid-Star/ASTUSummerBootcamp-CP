class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr=str(n)
        pro=1
        Sum=0
        for i in arr:
            pro*=int(i)
            Sum+=int(i)
        if n%(pro+Sum)==0:
            return True
        else:
            return False
        