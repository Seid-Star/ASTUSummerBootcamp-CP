class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=2147483648
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans


        
        