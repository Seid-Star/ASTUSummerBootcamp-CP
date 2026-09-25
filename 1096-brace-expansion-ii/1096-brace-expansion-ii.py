class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def solve(s):
            ans=set()
            cur={""}
            i=0
            while i<len(s):
                if s[i]=='{':
                    count=1
                    j=i+1
                    while count>0:
                        if s[j]=='{':
                            count+=1
                        elif s[j]=='}':
                            count-=1
                        j+=1
                    brr=solve(s[i+1:j-1])
                    temp=set()
                    for a in cur:
                        for b in brr:
                            temp.add(a+b)
                    cur=temp
                    i=j
                elif s[i]==',':
                    ans=ans|cur
                    cur={""}
                    i+=1
                else:
                    temp=set()
                    for a in cur:
                        temp.add(a+s[i])
                    cur=temp
                    i+=1
            ans=ans|cur
            return ans
        ans=solve(expression)
        return sorted(ans)
        