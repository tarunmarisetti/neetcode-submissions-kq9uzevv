class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''we have two options every day buy or skip
        and in order to sell we need to buy 
        if we sell we can buy the next day thats means we need to skip the nect day

        state=(day, isBuying)'''
        cache={}
        def dfs(i, isBuying):
            if i>=len(prices):
                return 0
            if (i, isBuying) in cache:
                return cache[(i, isBuying)]
            if isBuying:
                buy=dfs(i+1, not isBuying)-prices[i]
                skip=dfs(i+1, isBuying)
                cache[(i, isBuying)]=max(buy, skip)
            else:
                sell=dfs(i+2, not isBuying)+prices[i]
                cooldown=dfs(i+1, isBuying)
                cache[(i, isBuying)]=max(sell, cooldown)
            return cache[(i, isBuying)]
        return dfs(0, True)
                


        