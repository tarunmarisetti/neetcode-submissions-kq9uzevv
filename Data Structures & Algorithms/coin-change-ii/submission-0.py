class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1 #we can for zero amount with one way
        for coin in coins:
            for curr_amount in range(coin,amount+1):
                dp[curr_amount]+=dp[curr_amount-coin]
        return dp[amount]
        