class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        arr=[]
        brr=[]
        for i in nums:
            arr.append(str(i))
        for i in arr:
            brr.append(sum(map(int,i)))
        for i in range(len(brr)):
            if i==brr[i]:
                return i
        return -1
        
        