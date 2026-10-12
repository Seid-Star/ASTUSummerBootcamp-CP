class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        arr=[0]*32

        for i in nums:
            for j in range(32):
                if i & (1<<j):
                    arr[j]+=1

        brr=[]
        for i in range(k):
            c=0
            for j in range(32):
                if arr[j]>0:
                    c+=1<<j
                    arr[j]-=1
            brr.append(c)

        count=0
        for i in brr:
            count=(count+i*i)%mod

        return count