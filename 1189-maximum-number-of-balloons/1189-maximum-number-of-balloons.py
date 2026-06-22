class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        B=text.count('b')
        A=text.count('a')
        L=text.count('l')//2
        O=text.count('o')//2
        N=text.count('n')
        return(min(B,A,L,O,N))

        