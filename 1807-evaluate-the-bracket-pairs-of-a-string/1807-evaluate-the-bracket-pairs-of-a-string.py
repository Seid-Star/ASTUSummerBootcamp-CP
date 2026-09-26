class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic={}
        for a,b in knowledge:
            dic[a]=b
        brr=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                j=i+1
                while s[j]!=')':
                    j+=1
                key=s[i+1:j]
                if key in dic:
                    brr.append(dic[key])
                else:
                    brr.append('?')
                i=j+1
            else:
                brr.append(s[i])
                i+=1
        return ''.join(brr)