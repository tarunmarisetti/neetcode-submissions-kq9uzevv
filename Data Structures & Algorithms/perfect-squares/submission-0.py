class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        perfectsquares=[]
        num=1
        while num**2<=n:
            perfectsquares.append(num**2)
            num=num+1
        for square in perfectsquares:
            for j in range(square,n+1):
                dp[j]=min(dp[j],dp[j-square]+1)
        return dp[n]
        