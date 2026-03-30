class Solution:
    def numSquares(self, n: int) -> int:
        def getPerfectSquares(n):
            res=[]
            for i in range(1,n+1):
                if i**2 <=n:
                    res.append(i**2)
                else:
                    break
            return res

        perfectSquares=getPerfectSquares(n)

        dp=[float('inf')]*(n+1)
        dp[0]=0
        for perSqr in perfectSquares:
            for currTarget in range(1,n+1):            
                if currTarget-perSqr>=0:
                    dp[currTarget]=min(dp[currTarget], 1+dp[currTarget-perSqr])
        # print(dp)
        return dp[n]
        