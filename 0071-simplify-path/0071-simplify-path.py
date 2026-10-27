class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=path.split('/')
        brr=[]
        for i in arr:
            if i=='' or i=='.':
                continue
            elif i=='..':
                if len(brr)>0:
                    brr.pop()
            else:
                brr.append(i)
        
        return '/'+'/'.join(brr)
            



        