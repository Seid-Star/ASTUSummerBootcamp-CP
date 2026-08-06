class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        a=len(s)
        count=0
        for i in range(a):
            c=0
            d=0
            for j in range(i,a):
                if s[j]=="0":
                    c+=1
                else:
                    d+=1
                if c<=k or d<=k:
                    count+=1
        return count