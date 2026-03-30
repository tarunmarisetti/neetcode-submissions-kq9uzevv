class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]

        # base case
        dp[n][0]=0
        dp[n][1]=0

        for i in range(n-1, -1, -1):
            # buy
            dp[i][1]=max(dp[i+1][0]-prices[i],dp[i+1][1])  #we can buy, skip

            # sell
            dp[i][0]=max(dp[i+1][1]+prices[i], dp[i+1][0]) # we can sell or skip
        
        return dp[0][1]
            
        