class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]
        arr=s.split()
        brr=[]
        for i in range(len(arr)-1,-1,-1):
            if i!=0:
                brr.append(arr[i]+' ')
            else:
                brr.append(arr[i])
        return (''.join(brr))
        