class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr=[0]*26
        for i in range(len(s)):
            arr[ord(s[i])-97]=i
        brr=[]
        l=0
        r=0
        for i in range(len(s)):
            r=max(r,arr[ord(s[i])-97])
            if i==r:
                brr.append(r-l+1)
                l=i+1
        return brr
        