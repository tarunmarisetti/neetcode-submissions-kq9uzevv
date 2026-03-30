class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i, isBuying):
            if i>=len(prices):
                return 0
            if(i, isBuying) in memo:
                return memo[(i, isBuying)]
            if isBuying:
                buy=dfs(i+1, not isBuying)-prices[i]
                cooldown=dfs(i+1, isBuying)
                memo[(i, isBuying)]=max(buy, cooldown)
                return memo[(i, isBuying)]
            else:
                sell=dfs(i+2, not isBuying)+prices[i]
                cooldown=dfs(i+1, isBuying)
                memo[(i, isBuying)]=max(sell, cooldown)
                return memo[(i, isBuying)]
        return dfs(0,True)

        