class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub:str,t:str,k:int) -> bool:
            count = i = 0
            for x in t:
                if i < len(sub) and x==sub[i]:
                    i+=1
                    if i==len(sub):
                        i=0
                        count+=1
                        if count==k:
                            return True
            return False
        a=""
        b=deque([""])
        while b:
            c=b.popleft()
            for x in map(chr,range(ord('a'),ord('z')+1)):
                d=c+x
                if isK(d,s,k):
                    a=d
                    b.append(d)
        return a