class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}# key=(index,isBuying), value=profit
        def dfs(index,isBuying):
            if index>=len(prices):
                return 0
            if (index,isBuying) in dp:
                return dp[(index,isBuying)]
            cooldown=dfs(index+1, isBuying)
            if isBuying:
                buy=dfs(index+1, not isBuying)-prices[index]
                dp[(index, isBuying)]=max(cooldown, buy)
            else:
                sell=dfs(index+2, not isBuying)+prices[index]
                dp[(index, isBuying)]=max(cooldown, sell)
            return dp[(index, isBuying)]
        return dfs(0,True)
            
            
        