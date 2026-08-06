class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            a=str(n)
            arr=[]
            count=1
            for i in a:
                arr.append(int(i))
            for j in arr:
                count*=j
            if count%t==0:
                break
            n+=1

        return n
        