from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod=10**9+7
        dp=[[0]*201 for _ in range(201)]
        dp[0][0]=1
        for x in nums:
            ndp=[r[:] for r in dp]
            for g1 in range(201):
                for g2 in range(201):
                    if dp[g1][g2]:
                        ng1=x if g1==0 else gcd(g1,x)
                        ng2=x if g2==0 else gcd(g2,x)
                        ndp[ng1][g2]=(ndp[ng1][g2]+dp[g1][g2])%mod
                        ndp[g1][ng2]=(ndp[g1][ng2]+dp[g1][g2])%mod
            dp=ndp
        ans=0
        for g in range(1,201):
            ans=(ans+dp[g][g])%mod
        return ans