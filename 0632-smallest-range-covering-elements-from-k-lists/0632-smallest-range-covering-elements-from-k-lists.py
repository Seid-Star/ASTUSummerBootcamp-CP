class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            for x in nums[i]:
                arr.append((x,i))     
        arr.sort()
        count=[0]*len(nums)
        g=0
        b=0
        brr=[arr[0][0],arr[-1][0]]        
        for a in range(len(arr)):
            c,d=arr[a]           
            if count[d]==0:
                g+=1           
            count[d]+=1          
            while g==len(nums):
                e,f=arr[b]              
                if arr[a][0]-e<brr[1]-brr[0]:
                    brr=[e,arr[a][0]]
                count[f]-=1
                if count[f]==0:
                    g-=1
                b+=1
        return brr