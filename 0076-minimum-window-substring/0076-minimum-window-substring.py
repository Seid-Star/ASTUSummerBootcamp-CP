from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a=Counter(t)
        b=defaultdict(int)
        c=[0,0]
        l,r=0,0
        length=float('inf')
        have,need=0,len(a)
        while r<len(s):
            b[s[r]]+=1
            if b[s[r]]==a[s[r]]:
                have+=1
            while have==need:
                if length>r-l+1:
                    length=r-l+1
                    c=[l,r]
                b[s[l]]-=1
                
                if b[s[l]]<a[s[l]]:
                    have-=1
                l+=1
            r+=1
        if length!=float('inf'):
            return s[c[0]:c[1]+1]
        else:
            return ""
        
