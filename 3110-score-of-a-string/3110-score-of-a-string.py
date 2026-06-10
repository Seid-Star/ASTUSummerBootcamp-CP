class Solution:
    def scoreOfString(self, s: str) -> int:
        a=0
        for i in range(1,len(s)):
            a+=abs(ord(s[i])-ord(s[i-1]))
        return a


        