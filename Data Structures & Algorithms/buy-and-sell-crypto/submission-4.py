class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProfit=0
        n=len(prices)
        while r<n:
            if prices[r]>prices[l]:
                currProfit=prices[r]-prices[l]
                maxProfit=max(currProfit, maxProfit)
            else:
                l=r
            r+=1
        return maxProfit
        