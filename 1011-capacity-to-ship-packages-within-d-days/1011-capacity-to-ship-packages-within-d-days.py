class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high
        def Can(mid):
            count=1
            total=0
            for i in range(len(weights)):
                if total+weights[i]<=mid:
                    total+=weights[i]
                else:
                    count+=1
                    total=weights[i]
            return count<=days
        while low<=high:
            mid=(low+high)//2
            if Can(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans