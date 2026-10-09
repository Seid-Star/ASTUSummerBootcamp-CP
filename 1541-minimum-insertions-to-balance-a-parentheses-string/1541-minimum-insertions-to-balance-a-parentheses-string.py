class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        need=0
        for i in s:
            if i=='(':
                need+=2
                if need%2==1:
                    count+=1
                    need-=1
            else:
                need-=1
                if need<0:
                    count+=1
                    need=1
        return count+need