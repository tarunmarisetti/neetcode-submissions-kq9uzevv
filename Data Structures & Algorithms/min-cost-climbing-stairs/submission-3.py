class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)
        dp=[0]*(n)
        dp[n-1]=0
        dp[n-2]=cost[-2]
        for i in range(n-3, -1, -1):
            dp[i]=cost[i]+min(dp[i+1], dp[i+2])
        # print(dp)
        return min(dp[0],dp[1])
        