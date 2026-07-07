class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=str(n)
        Sum=0
        b=''
        for i in a:
            Sum+=int(i)
            if i!='0':
                b+=i
        if b=='':
            b='0'
        return Sum*int(b)

        
        