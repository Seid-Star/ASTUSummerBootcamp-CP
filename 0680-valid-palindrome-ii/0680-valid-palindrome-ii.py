class Solution:
    def validPalindrome(self, s: str) -> bool:
        # l=0
        # while l<len(s):
        #     a=s[:l]+s[l+1:]
        #     b=a[::-1]
        #     if a==b:
        #         return True
        #     l+=1
        # return False
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                a=l+1
                b=r
                while a<b and s[a]==s[b]:
                    a+=1
                    b-=1
                if a>=b:
                    return True
                a=l
                b=r-1
                while a<b and s[a]==s[b]:
                    a+=1
                    b-=1
                return a>=b
            l+=1
            r-=1
        return True
        

