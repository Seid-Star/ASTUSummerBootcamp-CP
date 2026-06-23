class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        a=0
        b=0
        count=0
        while l<r:
            d=height[l]
            e=height[r]
            if d<e:
                a=max(a,d)
                count+=a-d
                l+=1
            else:
                b=max(b,e)
                count+=b-e
                r-=1
        return count