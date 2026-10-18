
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod=10**9+7
        n=len(nums)

        arr=[[0]*(n+1) for i in range(n+1)]

        for i in range(n+1):
            arr[i][0]=1
            arr[i][i]=1

        for i in range(2,n+1):
            for j in range(1,i):
                arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])%mod

        def solve(nums):
            if len(nums)<=2:
                return 1

            a=nums[0]
            left=[]
            right=[]

            for i in range(1,len(nums)):
                if nums[i]<a:
                    left.append(nums[i])
                else:
                    right.append(nums[i])

            x=len(left)
            y=len(right)

            count=arr[x+y][x]
            count=count*solve(left)%mod
            count=count*solve(right)%mod

            return count

        return (solve(nums)-1)%mod
