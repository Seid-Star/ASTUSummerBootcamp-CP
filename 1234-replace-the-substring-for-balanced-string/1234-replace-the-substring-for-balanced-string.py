class Solution:
    def balancedString(self, s: str) -> int:
        count=len(s)//4
        a=s.count('Q')-count
        b=s.count('W')-count
        c=s.count('E')-count
        d=s.count('R')-count
        a=max(0,a)
        b=max(0,b)
        c=max(0,c)
        d=max(0,d)
        if a==0 and b==0 and c==0 and d==0:
            return 0
        l=0
        r=0
        ans=len(s)
        while r<len(s):
            if s[r]=='Q':
                a-=1
            elif s[r]=='W':
                b-=1
            elif s[r]=='E':
                c-=1
            elif s[r]=='R':
                d-=1
            while a<=0 and b<=0 and c<=0 and d<=0:
                ans=min(ans,r-l+1)
                if s[l]=='Q':
                    a+=1
                elif s[l]=='W':
                    b+=1
                elif s[l]=='E':
                    c+=1
                elif s[l]=='R':
                    d+=1
                l+=1
            r+=1
        return ans