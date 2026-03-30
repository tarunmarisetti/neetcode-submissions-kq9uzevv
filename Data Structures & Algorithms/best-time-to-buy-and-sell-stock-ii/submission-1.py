class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cache={}
        def dfs(i, isBuy):
            if i>=n:
                return 0
            if (i, isBuy) in cache:
                return cache[(i, isBuy)]

            if isBuy:
                # we can buy
                buy=dfs(i+1, not isBuy)-prices[i]
                # we can also skip buying
                skip=dfs(i+1, isBuy)
                cache[(i, isBuy)]=max(buy, skip)
            else:
                # we can sell
                sell=dfs(i+1, not isBuy)+prices[i]
                #we can also skip selling
                skip=dfs(i+1, isBuy)
                cache[(i, isBuy)]=max(sell, skip)
            return cache[(i, isBuy)]

        return dfs(0,True)


        