class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nextBuy=0
        nextSell=0

        for i in range(len(prices)-1, -1, -1):
            currBuy=max(nextSell-prices[i], nextBuy)
            currSell=max(nextBuy+prices[i], nextSell)

            nextBuy=currBuy
            nextSell=currSell
        return nextBuy
            
        