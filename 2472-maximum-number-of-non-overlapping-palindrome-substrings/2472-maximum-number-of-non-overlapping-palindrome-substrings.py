class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        palindrome=[[False]*n for i in range(n)]

        for i in range(n):
            palindrome[i][i]=True

        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1

                if s[i]==s[j]:
                    if length==2 or palindrome[i+1][j-1]:
                        palindrome[i][j]=True

        dp=[0]*n

        for i in range(n):
            if i>0:
                dp[i]=dp[i-1]

            for j in range(i+1):
                length=i-j+1

                if length>=k and palindrome[j][i]:
                    if j==0:
                        dp[i]=max(dp[i],1)
                    else:
                        dp[i]=max(dp[i],dp[j-1]+1)

        return dp[n-1]