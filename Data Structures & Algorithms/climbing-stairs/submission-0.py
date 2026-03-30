class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)
        prev1=prev2=1
        for i in range(n-2, -1,-1):
            dp[i]=prev1+prev2
            temp=prev1
            prev1=dp[i]
            prev2=temp
        return dp[0]
        