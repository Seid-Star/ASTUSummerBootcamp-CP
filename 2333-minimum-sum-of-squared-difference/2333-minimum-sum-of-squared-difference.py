class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        arr=[]
        for i in range(len(nums1)):
            arr.append(abs(nums1[i]-nums2[i]))

        k=k1+k2
        arr.sort(reverse=True)

        if sum(arr)<=k:
            return 0

        l=0
        r=max(arr)

        while l<r:
            mid=(l+r)//2
            count=0

            for i in arr:
                if i>mid:
                    count+=i-mid

            if count<=k:
                r=mid
            else:
                l=mid+1

        count=0
        need=0

        for i in arr:
            if i>l:
                count+=l*l
                need+=i-l
            else:
                count+=i*i

        k=k-need

        for i in range(len(arr)):
            if arr[i]>=l and k>0:
                count-=l*l
                count+=(l-1)*(l-1)
                k-=1

        return count